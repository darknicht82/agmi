import threading
from pathlib import Path

import httpx
import pytest
from src.adapters.n8n_server import create_n8n_listener
from src.domain.models import Source, SourceType
from src.ingestion.registry import SourceRegistry


@pytest.fixture
def test_server(tmp_path: Path):
    source = Source(
        id="src_computrabajo_ec",
        name="CompuTrabajo Ecuador",
        url="https://ec.computrabajo.com",
        canonical_url="https://ec.computrabajo.com",
        domain="ec.computrabajo.com",
        source_type=SourceType.JOB,
        country="EC",
    )
    registry = SourceRegistry([source])

    # Port 0 asigna un puerto libre automáticamente por el SO
    server = create_n8n_listener(registry=registry, host="127.0.0.1", port=0, data_dir=tmp_path)
    port = server.server_port

    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()

    yield f"http://127.0.0.1:{port}"

    server.shutdown()
    server.server_close()


def test_n8n_server_valid_ingest(test_server: str) -> None:
    client = httpx.Client(base_url=test_server)
    payload = {
        "source_id": "src_computrabajo_ec",
        "url": "https://ec.computrabajo.com/ofertas/888",
        "content": "<html><head><title>Prueba n8n</title></head><body><p>Detalle de oferta SRI</p></body></html>",
    }

    res = client.post("/api/v1/ingest", json=payload)
    assert res.status_code == 200
    data = res.json()
    assert data["status"] == "ok"
    assert "evidence_id" in data
    assert data["canonical_url"] == "https://ec.computrabajo.com/ofertas/888"


def test_n8n_server_unregistered_source(test_server: str) -> None:
    client = httpx.Client(base_url=test_server)
    payload = {
        "source_id": "src_no_valida",
        "url": "https://otro-sitio.com/123",
        "content": "<p>Contenido</p>",
    }

    res = client.post("/api/v1/ingest", json=payload)
    assert res.status_code == 400
    assert "no está registrada" in res.json()["error"]


def test_n8n_server_not_found(test_server: str) -> None:
    client = httpx.Client(base_url=test_server)
    res = client.post("/api/v1/otra_ruta", json={})
    assert res.status_code == 404
