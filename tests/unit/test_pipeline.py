from pathlib import Path
from unittest.mock import MagicMock

import httpx
import pytest
from src.domain.models import EvidenceType, Source, SourceType
from src.ingestion.http_fetcher import HttpFetcher
from src.ingestion.pipeline import IngestionPipeline


def test_pipeline_end_to_end_mock(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    # Asegurar ejecución offline y hermética
    monkeypatch.setattr("src.ingestion.http_fetcher.assert_public_http_url", lambda url: url)

    fetcher = HttpFetcher(rate_limit_per_min=600)
    mock_client = MagicMock(spec=httpx.Client)

    html_content = (
        b"<!DOCTYPE html><html><head><title>Pyme en Guayaquil busca automatizacion</title></head>"
        b"<body><p>Necesitamos conectar nuestro sistema de ventas con facturas SRI urgente.</p></body></html>"
    )

    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.headers = {"Content-Type": "text/html; charset=utf-8"}
    mock_response.iter_bytes.return_value = [html_content]
    mock_client.stream.return_value.__enter__.return_value = mock_response

    # Parcheamos fetcher para inyectar mock_client
    fetcher.fetch = lambda url: HttpFetcher.fetch(fetcher, url, client=mock_client)  # type: ignore

    pipeline = IngestionPipeline(fetcher=fetcher, data_dir=tmp_path)

    source = Source(
        id="src_mock_portal",
        name="Portal Empleo Mock",
        url="https://portalempleo.com.ec",
        canonical_url="https://portalempleo.com.ec",
        domain="portalempleo.com.ec",
        source_type=SourceType.JOB,
        country="EC",
    )

    res = pipeline.ingest_url(
        url="https://portalempleo.com.ec/oferta/101?utm_campaign=fb",
        source=source,
        evidence_type=EvidenceType.JOB_POSTING,
    )

    # Verificaciones
    assert res.source.id == "src_mock_portal"
    assert res.evidence.canonical_url == "https://portalempleo.com.ec/oferta/101"
    assert res.evidence.title == "Pyme en Guayaquil busca automatizacion"
    assert "facturas SRI" in res.evidence.excerpt
    assert res.raw_artifact_path.exists()
    assert res.evidence_metadata_path.exists()

    # Re-ejecución con el mismo contenido es idempotente
    res2 = pipeline.ingest_url(
        url="https://portalempleo.com.ec/oferta/101",
        source=source,
        evidence_type=EvidenceType.JOB_POSTING,
    )
    assert res2.evidence.content_hash == res.evidence.content_hash
