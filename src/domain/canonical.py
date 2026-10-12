"""Funciones de canonización determinista e idempotencia.

Reglas AGNexus:
- Claves naturales: URL canónica y content_hash SHA-256.
- Idempotencia: Todo procesamiento debe poder re-ejecutarse sin duplicar ni corromper estado.
"""

from __future__ import annotations

import hashlib
import posixpath
import re
from urllib.parse import parse_qsl, urlencode, urlparse, urlunparse

_STRIP_QUERY_PARAMS = frozenset(
    {
        "utm_source",
        "utm_medium",
        "utm_campaign",
        "utm_term",
        "utm_content",
        "utm_id",
        "fbclid",
        "gclid",
        "msclkid",
        "dclid",
        "ref",
        "_ga",
        "_gl",
        "mc_cid",
        "mc_eid",
    }
)


def canonicalize_url(raw_url: str) -> str:
    """Normaliza una URL de forma determinista para deduplicación e idempotencia.

    - Convierte scheme y hostname a minúsculas.
    - Remueve puertos por defecto (80 para http, 443 para https).
    - Normaliza path relativo y elimina trailing slashes superfluos.
    - Elimina parámetros de tracking conocidos (utm_*, fbclid, gclid, etc.).
    - Ordena alfabéticamente los parámetros de query restantes.
    - Remueve fragments (#hash).
    """
    if not raw_url or not isinstance(raw_url, str):
        raise ValueError(f"URL inválida para canonización: {raw_url!r}")

    parsed = urlparse(raw_url.strip())
    scheme = parsed.scheme.lower()
    if scheme not in {"http", "https"}:
        raise ValueError(f"Esquema no soportado para canonización: {scheme!r}")

    hostname = (parsed.hostname or "").lower().rstrip(".")
    if not hostname:
        raise ValueError(f"URL sin hostname válido: {raw_url!r}")

    # Puerto: omitir si es el default
    port = parsed.port
    if (scheme == "http" and port == 80) or (scheme == "https" and port == 443):
        netloc = hostname
    elif port is not None:
        netloc = f"{hostname}:{port}"
    else:
        netloc = hostname

    # Path normalization
    raw_path = parsed.path or "/"
    norm_path = posixpath.normpath(raw_path)
    if raw_path.endswith("/") and not norm_path.endswith("/"):
        norm_path += "/"
    if not norm_path.startswith("/"):
        norm_path = "/" + norm_path
    # Si es solo /index.html o /index.php en raíz, mantener canónico
    if norm_path != "/" and norm_path.endswith("/"):
        norm_path = norm_path.rstrip("/")

    # Query params
    filtered_params = [
        (k, v)
        for k, v in parse_qsl(parsed.query, keep_blank_values=False)
        if k.lower() not in _STRIP_QUERY_PARAMS
    ]
    filtered_params.sort(key=lambda item: (item[0], item[1]))
    clean_query = urlencode(filtered_params)

    return urlunparse((scheme, netloc, norm_path, "", clean_query, ""))


def compute_content_hash(content: bytes | str) -> str:
    """Calcula el hash SHA-256 hexadecimal de un contenido binario o texto."""
    if isinstance(content, str):
        data = content.encode("utf-8")
    elif isinstance(content, bytes):
        data = content
    else:
        raise TypeError(f"El contenido debe ser bytes o str, no {type(content).__name__}")
    return hashlib.sha256(data).hexdigest()


def compute_text_hash(text: str) -> str:
    """Calcula hash SHA-256 de texto normalizando espacios y saltos de línea."""
    if not isinstance(text, str):
        raise TypeError(f"Se esperaba str, se recibió {type(text).__name__}")
    normalized = re.sub(r"\s+", " ", text.strip())
    return compute_content_hash(normalized.encode("utf-8"))
