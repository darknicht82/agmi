"""Script de inicio para el listener local de n8n (A&G Market Intelligence).

Uso:
    python scripts/run_listener.py

Levanta el servidor HTTP en 127.0.0.1:8765 para recibir payloads enviados
desde workflows en n8n (http://localhost:5678).
"""

from __future__ import annotations

import logging
import sys
from pathlib import Path

# Asegurar importación desde src
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from src.adapters.n8n_server import create_n8n_listener
from src.ingestion.registry import SourceRegistry


def main() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    )
    logger = logging.getLogger("agmarket.listener")

    project_root = Path(__file__).resolve().parent.parent
    seed_registry = project_root / "data" / "seed" / "fuentes_ecuador.json"
    data_dir = project_root / "data"

    if not seed_registry.is_file():
        logger.error("No se encontró el archivo de registro en: %s", seed_registry)
        sys.exit(1)

    registry = SourceRegistry.from_json(seed_registry)
    host = "127.0.0.1"
    port = 8765

    server = create_n8n_listener(
        registry=registry,
        host=host,
        port=port,
        data_dir=data_dir,
    )

    print("=" * 65)
    print("  A&G MARKET INTELLIGENCE — RECEPTOR LOCAL DE INGESTA (N8N)")
    print("=" * 65)
    print(f"  • Endpoint de ingesta: http://{host}:{port}/api/v1/ingest")
    print("  • n8n Web UI:          http://localhost:5678")
    print(f"  • Fuentes cargadas:    {len(registry.list_active())} activas")
    print(f"  • Directorio de datos: {data_dir}")
    print("=" * 65)
    print("Presiona Ctrl+C para detener el servidor.\n")

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nDeteniendo servidor de ingesta...")
        server.shutdown()
        server.server_close()
        print("Servidor detenido correctamente.")


if __name__ == "__main__":
    main()
