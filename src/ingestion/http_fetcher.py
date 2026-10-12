"""Cliente HTTP determinista con protección SSRF, rate limit y límites de payload.

Reglas:
- SSRF guard obligatorio antes de enviar request.
- Cero fallbacks: error duro si timeout, payload excedido o status de error.
- Respeto de rate limits por dominio.
- Procedencia y hashing SHA-256 de toda respuesta recibida.
"""

from __future__ import annotations

import logging
import time
from collections import defaultdict
from dataclasses import dataclass
from datetime import UTC, datetime
from urllib.parse import urlparse

import httpx
from src.domain.canonical import canonicalize_url, compute_content_hash
from src.security.url_guard import assert_public_http_url

logger = logging.getLogger("agmarket.ingestion")


class FetchError(RuntimeError):
    """Error al obtener contenido remoto."""


class RateLimitError(FetchError):
    """Límite de frecuencia por dominio alcanzado."""


class PayloadLimitExceeded(FetchError):
    """La respuesta excede el tamaño máximo permitido."""


@dataclass(frozen=True, slots=True)
class FetchResult:
    """Resultado inmutable de una petición HTTP."""

    url: str
    canonical_url: str
    status_code: int
    content_bytes: bytes
    content_type: str
    elapsed_ms: float
    content_hash: str
    fetched_at: datetime


class HttpFetcher:
    """Fetcher HTTP determinista y seguro."""

    def __init__(
        self,
        rate_limit_per_min: int = 6,
        timeout_seconds: int = 30,
        max_response_bytes: int = 10485760,  # 10 MB
        max_redirects: int = 3,
        user_agent: str = "AG-Market-Intelligence/1.0 (+https://github.com/darknicht82/agmi; internal-research)",
    ) -> None:
        self.rate_limit_per_min = rate_limit_per_min
        self.timeout_seconds = timeout_seconds
        self.max_response_bytes = max_response_bytes
        self.max_redirects = max_redirects
        self.user_agent = user_agent
        self._min_interval_seconds = 60.0 / max(1, rate_limit_per_min)
        self._domain_last_request: dict[str, float] = defaultdict(float)

    def _wait_for_rate_limit(self, domain: str) -> None:
        now = time.monotonic()
        last = self._domain_last_request[domain]
        elapsed = now - last
        if elapsed < self._min_interval_seconds:
            wait_time = self._min_interval_seconds - elapsed
            logger.debug("Rate limit para %s: esperando %.2fs", domain, wait_time)
            time.sleep(wait_time)
        self._domain_last_request[domain] = time.monotonic()

    def fetch(self, raw_url: str, client: httpx.Client | None = None) -> FetchResult:
        """Obtiene una URL de forma determinista con todas las guardas activas.

        Lanza:
            SSRFBlocked: si la URL resuelve a host privado o inválido.
            PayloadLimitExceeded: si excede max_response_bytes.
            FetchError: si hay error de conexión, timeout o status HTTP != 200.
        """
        # 1. Validación de seguridad SSRF
        assert_public_http_url(raw_url)

        # 2. Canonización de URL
        canon_url = canonicalize_url(raw_url)
        domain = (urlparse(canon_url).hostname or "").lower()

        # 3. Aplicar rate limit por dominio
        self._wait_for_rate_limit(domain)

        headers = {
            "User-Agent": self.user_agent,
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "es-EC,es;q=0.9,en;q=0.5",
        }

        start_time = time.perf_counter()
        fetched_at = datetime.now(UTC)

        # Manejador de cliente inyectable para testing
        close_client = False
        if client is None:
            client = httpx.Client(
                timeout=float(self.timeout_seconds),
                max_redirects=self.max_redirects,
                follow_redirects=True,
            )
            close_client = True

        try:
            with client.stream("GET", canon_url, headers=headers) as response:
                if response.status_code != 200:
                    raise FetchError(
                        f"Petición fallida a {canon_url}. HTTP Status {response.status_code} "
                        f"(esperado 200). Sin fallback."
                    )

                content_chunks: list[bytes] = []
                total_bytes = 0

                for chunk in response.iter_bytes():
                    total_bytes += len(chunk)
                    if total_bytes > self.max_response_bytes:
                        raise PayloadLimitExceeded(
                            f"Respuesta de {canon_url} excedió el límite de "
                            f"{self.max_response_bytes} bytes."
                        )
                    content_chunks.append(chunk)

                content_bytes = b"".join(content_chunks)
                content_type = response.headers.get("Content-Type", "application/octet-stream")
        except (httpx.TimeoutException, httpx.RequestError) as exc:
            raise FetchError(f"Error de red o timeout contactando {canon_url}: {exc}") from exc
        finally:
            if close_client:
                client.close()

        elapsed_ms = (time.perf_counter() - start_time) * 1000.0
        content_hash = compute_content_hash(content_bytes)

        logger.info(
            "Fetch exitoso: %s | Bytes: %d | Hash: %s... | Tiempo: %.1fms",
            canon_url,
            len(content_bytes),
            content_hash[:12],
            elapsed_ms,
        )

        return FetchResult(
            url=raw_url,
            canonical_url=canon_url,
            status_code=200,
            content_bytes=content_bytes,
            content_type=content_type,
            elapsed_ms=elapsed_ms,
            content_hash=content_hash,
            fetched_at=fetched_at,
        )
