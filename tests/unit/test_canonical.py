import pytest
from src.domain.canonical import (
    canonicalize_url,
    compute_content_hash,
    compute_text_hash,
)


def test_canonicalize_url_basic() -> None:
    raw = "HTTPS://WWW.Ejemplo.com.ec/Ruta/Principal/?utm_source=google&b=2&a=1#seccion"
    expected = "https://www.ejemplo.com.ec/Ruta/Principal?a=1&b=2"
    assert canonicalize_url(raw) == expected


def test_canonicalize_url_default_ports() -> None:
    assert canonicalize_url("http://example.com:80/path") == "http://example.com/path"
    assert canonicalize_url("https://example.com:443/path") == "https://example.com/path"
    assert canonicalize_url("https://example.com:8443/path") == "https://example.com:8443/path"


def test_canonicalize_url_invalid() -> None:
    with pytest.raises(ValueError, match="Esquema no soportado"):
        canonicalize_url("ftp://example.com/archivo")

    with pytest.raises(ValueError, match="URL inválida"):
        canonicalize_url("")


def test_compute_content_hash() -> None:
    text = "A&G Market Intelligence — Ecuador"
    h1 = compute_content_hash(text)
    h2 = compute_content_hash(text.encode("utf-8"))
    assert len(h1) == 64
    assert h1 == h2


def test_compute_text_hash_whitespace_insensitivity() -> None:
    t1 = "Problema con   facturacion electronica \n en Quito."
    t2 = "Problema con facturacion electronica en Quito."
    assert compute_text_hash(t1) == compute_text_hash(t2)
