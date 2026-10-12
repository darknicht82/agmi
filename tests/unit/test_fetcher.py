from unittest.mock import MagicMock

import httpx
import pytest
from src.ingestion.http_fetcher import (
    FetchError,
    HttpFetcher,
    PayloadLimitExceeded,
)
from src.security.url_guard import SSRFBlocked


def test_fetcher_blocks_ssrf() -> None:
    fetcher = HttpFetcher()
    with pytest.raises(SSRFBlocked):
        fetcher.fetch("http://localhost:8080/secret")

    with pytest.raises(SSRFBlocked):
        fetcher.fetch("http://127.0.0.1:5432")


def test_fetcher_success_with_mock_client() -> None:
    fetcher = HttpFetcher(rate_limit_per_min=60)
    mock_client = MagicMock(spec=httpx.Client)

    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.headers = {"Content-Type": "text/html; charset=utf-8"}
    mock_response.iter_bytes.return_value = [b"<html><body><h1>Empresa Ecuador</h1></body></html>"]

    mock_client.stream.return_value.__enter__.return_value = mock_response

    res = fetcher.fetch("https://example.com/oferta?utm_source=fb", client=mock_client)

    assert res.canonical_url == "https://example.com/oferta"
    assert res.status_code == 200
    assert len(res.content_bytes) > 0
    assert len(res.content_hash) == 64


def test_fetcher_error_on_non_200() -> None:
    fetcher = HttpFetcher(rate_limit_per_min=60)
    mock_client = MagicMock(spec=httpx.Client)

    mock_response = MagicMock()
    mock_response.status_code = 404
    mock_client.stream.return_value.__enter__.return_value = mock_response

    with pytest.raises(FetchError, match="HTTP Status 404"):
        fetcher.fetch("https://example.com/not-found", client=mock_client)


def test_fetcher_payload_exceeded() -> None:
    fetcher = HttpFetcher(max_response_bytes=10, rate_limit_per_min=60)
    mock_client = MagicMock(spec=httpx.Client)

    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.headers = {"Content-Type": "text/html"}
    mock_response.iter_bytes.return_value = [b"123456789012345"]  # 15 bytes > 10

    mock_client.stream.return_value.__enter__.return_value = mock_response

    with pytest.raises(PayloadLimitExceeded, match="límite"):
        fetcher.fetch("https://example.com/large", client=mock_client)
