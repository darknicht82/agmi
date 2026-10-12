from datetime import UTC, datetime
from pathlib import Path

import pytest
from src.domain.models import Evidence, EvidenceType
from src.storage.file_storage import (
    load_evidence_metadata,
    save_evidence_metadata,
    save_raw_content,
)


def test_save_raw_content_idempotent(tmp_path: Path) -> None:
    content = b"Contenido de prueba HTML para guardar en data/raw"
    c_hash = "abcdef0123456789" * 4

    p1 = save_raw_content(content, c_hash, ext="html", data_dir=tmp_path)
    assert p1.exists()
    assert p1.stat().st_size == len(content)

    # Segunda llamada: no debe fallar ni duplicar
    p2 = save_raw_content(content, c_hash, ext="html", data_dir=tmp_path)
    assert p1 == p2


def test_evidence_metadata_lifecycle(tmp_path: Path) -> None:
    now = datetime.now(UTC)
    evi = Evidence(
        id="evi_test_001",
        source_id="src_test",
        captured_at=now,
        canonical_url="https://ejemplo.com.ec/test",
        title="Problema de inventario",
        content_hash="1234567890abcdef" * 4,
        excerpt="Empresa pierde horas cuadrando cajas manualmente.",
        evidence_type=EvidenceType.JOB_POSTING,
        raw_artifact_path="raw/12/dummy.html",
    )

    path = save_evidence_metadata(evi, data_dir=tmp_path)
    assert path.exists()

    loaded = load_evidence_metadata("evi_test_001", data_dir=tmp_path)
    assert loaded.id == evi.id
    assert loaded.title == evi.title
    assert loaded.content_hash == evi.content_hash


def test_load_evidence_metadata_missing_raises(tmp_path: Path) -> None:
    with pytest.raises(FileNotFoundError, match="No existe el archivo de evidencia"):
        load_evidence_metadata("evi_inexistente", data_dir=tmp_path)
