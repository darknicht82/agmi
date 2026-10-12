"""Tests de la guardia SSRF (seguridad de límite)."""

from __future__ import annotations

import pytest
from src.security.url_guard import SSRFBlocked, assert_public_http_url


@pytest.mark.parametrize(
    "url",
    [
        "http://localhost/admin",
        "http://127.0.0.1:8080/x",
        "http://0.0.0.0/",
        "http://10.0.0.5/api",
        "http://192.168.1.1/",
        "http://172.16.0.1/",
        "http://169.254.169.254/latest/meta-data/",
        "http://[::1]/",
        "ftp://example.com/file",
        "file:///etc/passwd",
    ],
)
def test_blocked_targets(url: str) -> None:
    with pytest.raises(SSRFBlocked):
        assert_public_http_url(url)


def test_missing_host_is_blocked() -> None:
    with pytest.raises(SSRFBlocked):
        assert_public_http_url("http:///path-only")


def test_public_http_url_passes() -> None:
    url = "https://example.com/page"
    assert assert_public_http_url(url) == url
