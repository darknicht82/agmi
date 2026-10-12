"""Servidor HTTP local para recibir eventos y webhooks desde n8n (aidev-n8n:5678).

Reglas:
- Escucha exclusivamente en 127.0.0.1 (sin exposición externa).
- Cero fallbacks: valida payload contra Pydantic y el Source Registry.
- Idempotente: procesa a través de ingest_from_n8n.
"""

from __future__ import annotations

import json
import logging
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path
from typing import ClassVar

from pydantic import ValidationError
from src.adapters.n8n_adapter import N8nIngestPayload, ingest_from_n8n
from src.ingestion.registry import SourceRegistry, SourceRegistryError
from src.security.url_guard import SSRFBlocked

logger = logging.getLogger("agmarket.adapters.n8n_server")


class N8nIngestHandler(BaseHTTPRequestHandler):
    """Manejador HTTP para peticiones POST desde n8n."""

    registry: ClassVar[SourceRegistry | None] = None
    data_dir: ClassVar[Path] = Path("data")

    def log_message(self, format: str, *args: object) -> None:
        logger.debug("%s - " + format, self.address_string(), *args)

    def do_POST(self) -> None:
        if self.path != "/api/v1/ingest":
            self.send_response(404)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(b'{"error": "Ruta no encontrada"}')
            return

        content_length = int(self.headers.get("Content-Length", 0))
        if content_length <= 0 or content_length > 10485760:  # 10 MB máx
            self.send_response(400)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(b'{"error": "Content-Length invalido o payload excede limite"}')
            return

        body = self.rfile.read(content_length)

        try:
            raw_data = json.loads(body.decode("utf-8"))
            payload = N8nIngestPayload.model_validate(raw_data)
        except (json.JSONDecodeError, ValidationError) as exc:
            self.send_response(400)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({"error": f"Payload invalido: {exc}"}).encode("utf-8"))
            return

        if self.registry is None:
            self.send_response(500)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(b'{"error": "SourceRegistry no inicializado en el servidor"}')
            return

        try:
            result = ingest_from_n8n(payload, registry=self.registry, data_dir=self.data_dir)
            response_data = {
                "status": "ok",
                "evidence_id": result.evidence.id,
                "canonical_url": result.evidence.canonical_url,
                "content_hash": result.evidence.content_hash,
                "is_duplicate": result.is_duplicate,
            }
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(response_data).encode("utf-8"))
        except (SourceRegistryError, SSRFBlocked, ValueError) as exc:
            self.send_response(400)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({"error": str(exc)}).encode("utf-8"))


def create_n8n_listener(
    registry: SourceRegistry,
    host: str = "127.0.0.1",
    port: int = 8765,
    data_dir: Path | str = "data",
) -> HTTPServer:
    """Crea y configura una instancia de HTTPServer para escuchar peticiones de n8n."""
    N8nIngestHandler.registry = registry
    N8nIngestHandler.data_dir = Path(data_dir)
    return HTTPServer((host, port), N8nIngestHandler)
