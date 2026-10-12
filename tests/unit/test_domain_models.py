from datetime import UTC, datetime

import pytest
from pydantic import ValidationError
from src.domain.models import (
    AccessPolicy,
    Evidence,
    EvidenceType,
    Problem,
    Source,
    SourceType,
)


def test_source_model_valid() -> None:
    src = Source(
        id="src_computrabajo_ec",
        name="CompuTrabajo Ecuador",
        url="https://ec.computrabajo.com",
        canonical_url="https://ec.computrabajo.com",
        domain="ec.computrabajo.com",
        source_type=SourceType.JOB,
        country="EC",
    )
    assert src.id == "src_computrabajo_ec"
    assert src.country == "EC"
    assert src.access_policy == AccessPolicy.PUBLIC


def test_evidence_model_valid() -> None:
    now = datetime.now(UTC)
    dummy_hash = "a" * 64
    evi = Evidence(
        id="evi_20261012_001",
        source_id="src_computrabajo_ec",
        captured_at=now,
        canonical_url="https://ec.computrabajo.com/ofertas/123",
        title="Desarrollador de Integraciones ERP",
        content_hash=dummy_hash,
        excerpt="Empresa en Guayaquil busca profesional para conectar ERP con SRI y facturación.",
        evidence_type=EvidenceType.JOB_POSTING,
        raw_artifact_path="raw/aa/dummy.html",
    )
    assert evi.id == "evi_20261012_001"
    assert evi.confidence == 1.0


def test_problem_model_requires_evidence() -> None:
    with pytest.raises(ValidationError) as exc_info:
        Problem(
            id="PROBLEM-001",
            title="Integración manual de facturas",
            description="Las empresas digitan facturas manualmente todos los días.",
            sector="Comercio",
            affected_actor="Contadores y dueños de pymes",
            trigger="Cierre mensual o recepción de compras",
            frequency=5,
            urgency=4,
            impact=4,
            current_solution="Hojas de Excel y tipeo manual",
            alternatives="Contratar pasantes / sistema ERP costoso",
            access_path="Contacto directo con estudios contables en Guayaquil",
            evidence_ids=[],  # Vacío deliberadamente
        )
    assert "evidence_ids" in str(exc_info.value)


def test_problem_model_valid() -> None:
    prob = Problem(
        id="PROBLEM-001",
        title="Integración manual de facturas electrónicas SRI",
        description="Las empresas descargan manualmente los XML del SRI y los digitan en Excel.",
        sector="Comercio y Servicios",
        affected_actor="Pymes y estudios contables en Ecuador",
        trigger="Cierre semanal de compras y declaraciones SRI",
        frequency=5,
        urgency=5,
        impact=4,
        current_solution="Hojas de cálculo manuales",
        alternatives="Asistentes contables / ERPs caros",
        access_path="Cámaras de comercio y estudios contables de Quito y Guayaquil",
        evidence_ids=["evi_20261012_001"],
    )
    assert prob.id == "PROBLEM-001"
    assert prob.frequency == 5
    assert len(prob.evidence_ids) == 1
