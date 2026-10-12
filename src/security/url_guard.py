"""Guardia SSRF — validación de URLs antes de cualquier fetch.

El contenido remoto es no confiable. Esta es la primera línea de defensa.
Bloquea loopback, rangos privados, link-local y metadata endpoints.
"""

from __future__ import annotations

import ipaddress
import socket
from urllib.parse import urlparse


class SSRFBlocked(ValueError):
    """La URL apunta a un destino prohibido (SSRF)."""


_BLOCKED_HOSTS = frozenset(
    {
        "localhost",
        "localhost.localdomain",
        "0.0.0.0",
        "metadata.google.internal",
        "metadata",
    }
)


def _resolve_is_private(hostname: str) -> bool:
    try:
        infos = socket.getaddrinfo(hostname, None)
    except socket.gaierror as exc:
        raise SSRFBlocked(f"No se pudo resolver el host: {hostname!r}") from exc
    for info in infos:
        addr = info[4][0]
        try:
            ip = ipaddress.ip_address(addr)
        except ValueError as exc:
            raise SSRFBlocked(f"Dirección inválida resuelta: {addr!r}") from exc
        if (
            ip.is_private
            or ip.is_loopback
            or ip.is_link_local
            or ip.is_reserved
            or ip.is_multicast
        ):
            return True
    return False


def assert_public_http_url(url: str) -> str:
    """Valida que la URL sea http(s) público. Devuelve la URL normalizada.

    Regla cero fallbacks: si la URL es inválida o apunta a destino prohibido,
    se lanza SSRFBlocked. Nunca se intenta "igual y funciona".
    """
    parsed = urlparse(url)
    if parsed.scheme not in {"http", "https"}:
        raise SSRFBlocked(f"Esquema no permitido: {parsed.scheme!r} en {url!r}")
    hostname = parsed.hostname
    if not hostname:
        raise SSRFBlocked(f"URL sin host: {url!r}")
    host_l = hostname.lower().rstrip(".")
    if host_l in _BLOCKED_HOSTS:
        raise SSRFBlocked(f"Host bloqueado: {hostname!r}")
    # Literal IP en el hostname
    try:
        ip = ipaddress.ip_address(host_l)
    except ValueError:
        pass
    else:
        if (
            ip.is_private
            or ip.is_loopback
            or ip.is_link_local
            or ip.is_reserved
            or ip.is_multicast
        ):
            raise SSRFBlocked(f"IP privada/reservada bloqueada: {hostname!r}")
    if _resolve_is_private(host_l):
        raise SSRFBlocked(f"El host resuelve a red privada/loopback: {hostname!r}")
    return url
