from pathlib import Path

import pytest
from src.adapters.n8n_adapter import N8nIngestPayload, ingest_from_n8n
from src.domain.models import EvidenceType, Source, SourceType
from src.ingestion.registry import SourceRegistry, SourceRegistryError
from src.security.url_guard import SSRFBlocked


@pytest.fixture
def mock_registry() -> SourceRegistry:
    source = Source(
        id="src_computrabajo_ec",
        name="CompuTrabajo Ecuador",
        url="https://ec.computrabajo.com",
        canonical_url="https://ec.computrabajo.com",
        domain="ec.computrabajo.com",
        source_type=SourceType.JOB,
        country="EC",
    )
    return SourceRegistry([source])


def test_ingest_from_n8n_success(tmp_path: Path, mock_registry: SourceRegistry) -> None:
    payload = N8nIngestPayload(
        source_id="src_computrabajo_ec",
        url="https://ec.computrabajo.com/ofertas/456?utm_source=n8n",
        content="<html><head><title>Vacante Integrador</title></head><body><p>Integrar ERP con facturación electrónica SRI.</p></body></html>",
        evidence_type=EvidenceType.JOB_POSTING,
    )

    result = ingest_from_n8n(payload, registry=mock_registry, data_dir=tmp_path)

    assert result.source.id == "src_computrabajo_ec"
    assert result.evidence.canonical_url == "https://ec.computrabajo.com/ofertas/456"
    assert result.evidence.title == "Vacante Integrador"
    assert "facturación electrónica SRI" in result.evidence.excerpt
    assert result.raw_artifact_path.exists()
    assert result.evidence_metadata_path.exists()


def test_ingest_from_n8n_unregistered_source(tmp_path: Path, mock_registry: SourceRegistry) -> None:
    payload = N8nIngestPayload(
        source_id="src_no_registrada",
        url="https://sitio-desconocido.com/oferta",
        content="<p>Contenido sin fuente en registro</p>",
    )

    with pytest.raises(SourceRegistryError, match="no está registrada"):
        ingest_from_n8n(payload, registry=mock_registry, data_dir=tmp_path)


def test_ingest_from_n8n_ssrf_blocked(tmp_path: Path, mock_registry: SourceRegistry) -> None:
    payload = N8nIngestPayload(
        source_id="src_computrabajo_ec",
        url="http://127.0.0.1:5678/webhook/test",
        content="<p>Intento de loopback local</p>",
    )

    with pytest.raises(SSRFBlocked):
        ingest_from_n8n(payload, registry=mock_registry, data_dir=tmp_path)
