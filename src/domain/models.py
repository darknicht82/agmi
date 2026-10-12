"""Modelos de dominio tipados (Pydantic v2) para A&G Market Intelligence.

Reglas:
- claim -> evidence -> source (trazabilidad estricta).
- Sin datos inventados: campos obligatorios exigen valores reales.
- Idempotencia y claves naturales: canonical_url y content_hash.
"""

from __future__ import annotations

from datetime import UTC, datetime
from enum import StrEnum

from pydantic import BaseModel, ConfigDict, Field, field_validator


class SourceType(StrEnum):
    JOB = "job"
    COMPANY = "company"
    NEWS = "news"
    DIRECTORY = "directory"
    DOCUMENT = "document"
    COMPETITOR = "competitor"


class AccessPolicy(StrEnum):
    PUBLIC = "public"
    RESTRICTED = "restricted"


class EvidenceType(StrEnum):
    JOB_POSTING = "job_posting"
    NEWS_ARTICLE = "news_article"
    COMPANY_PAGE = "company_page"
    PUBLIC_DOC = "public_doc"
    FORUM_POST = "forum_post"
    OTHER = "other"


class SignalType(StrEnum):
    HIRING = "hiring"
    MANUAL_PROCESS = "manual_process"
    SOFTWARE_USED = "software_used"
    COMPLAINT = "complaint"
    REPEATED_NEED = "repeated_need"
    COST = "cost"
    GROWTH = "growth"
    COMPLIANCE = "compliance"
    INTEGRATION = "integration"
    DATA_PROBLEM = "data_problem"
    OPERATIONAL_BOTTLENECK = "operational_bottleneck"


class Source(BaseModel):
    """Fuente registrada en el registry de A&G. Unidad de origen."""

    model_config = ConfigDict(frozen=True, extra="forbid")

    id: str = Field(..., min_length=3, description="Identificador único (ej. src_computrabajo_ec)")
    name: str = Field(..., min_length=2, description="Nombre legible de la fuente")
    url: str = Field(..., min_length=10, description="URL semilla o raíz")
    canonical_url: str = Field(..., min_length=10, description="URL canónica normalizada")
    domain: str = Field(..., min_length=3, description="Dominio de la fuente (ej. computrabajo.com.ec)")
    source_type: SourceType
    country: str = Field(default="EC", min_length=2, max_length=2, description="Código ISO del país")
    jurisdiction: str = Field(default="Ecuador", description="Jurisdicción legal")
    access_policy: AccessPolicy = Field(default=AccessPolicy.PUBLIC)
    crawl_frequency: str = Field(default="daily", description="Frecuencia planificada")
    first_seen_at: datetime = Field(default_factory=lambda: datetime.now(UTC))
    last_crawled_at: datetime | None = None
    access_status: str = Field(default="active", description="active, blocked, unreachable")
    robots_status: str = Field(default="allowed", description="allowed, disallowed, unknown")
    terms_review_status: str = Field(default="compliant", description="compliant, pending, restricted")
    content_hash: str | None = None
    active: bool = Field(default=True)


class Evidence(BaseModel):
    """Unidad mínima auditable. Contenido capturado con procedencia y hash."""

    model_config = ConfigDict(frozen=True, extra="forbid")

    id: str = Field(..., min_length=3, description="Identificador único (ej. evi_20261012_001)")
    source_id: str = Field(..., min_length=3, description="ID de la fuente originaria")
    captured_at: datetime = Field(default_factory=lambda: datetime.now(UTC))
    canonical_url: str = Field(..., min_length=10)
    title: str = Field(..., min_length=1, description="Título o encabezado del contenido")
    published_at: datetime | None = None
    author: str | None = None
    content_hash: str = Field(..., min_length=64, max_length=64, description="Hash SHA-256")
    excerpt: str = Field(..., min_length=10, description="Texto citado directamente de la evidencia")
    locator: str | None = Field(default=None, description="Selector CSS, ruta o número de párrafo")
    evidence_type: EvidenceType
    confidence: float = Field(default=1.0, ge=0.0, le=1.0)
    raw_artifact_path: str = Field(..., min_length=1, description="Ruta relativa del contenido crudo en data/raw/")


class Signal(BaseModel):
    """Señal estructurada extraída a partir de evidencia verificable."""

    model_config = ConfigDict(frozen=True, extra="forbid")

    id: str = Field(..., min_length=3)
    evidence_id: str = Field(..., min_length=3, description="Evidencia que respalda esta señal")
    type: SignalType
    text: str = Field(..., min_length=5, description="Extracto o formulación de la señal")
    description: str = Field(..., min_length=5)
    value: str | None = None
    sector: str = Field(..., min_length=2)
    entities: list[str] = Field(default_factory=list)
    confidence: float = Field(default=0.9, ge=0.0, le=1.0)


class Problem(BaseModel):
    """Ficha de problema comercial respaldada por evidencia (claim -> evidence -> source)."""

    model_config = ConfigDict(frozen=True, extra="forbid")

    id: str = Field(..., pattern=r"^PROBLEM-\d{3,}$", description="Formato estricto PROBLEM-###")
    title: str = Field(..., min_length=5)
    description: str = Field(..., min_length=10)
    sector: str = Field(..., min_length=2)
    affected_actor: str = Field(..., min_length=3, description="Quién sufre el problema")
    trigger: str = Field(..., min_length=3, description="Cuándo o por qué ocurre")
    frequency: int = Field(..., ge=1, le=5, description="1 (excepcional) a 5 (diario/recurrente)")
    urgency: int = Field(..., ge=1, le=5, description="1 (puede esperar) a 5 (urgente)")
    impact: int = Field(..., ge=1, le=5, description="1 (cosmético) a 5 (afecta dinero/operación)")
    current_solution: str = Field(..., min_length=3, description="Cómo se resuelve hoy (manual, hoja de cálculo, etc.)")
    alternatives: str = Field(..., min_length=3, description="Mapa de alternativas y competidores")
    access_path: str = Field(..., min_length=5, description="¿Cómo llegaríamos al primer cliente?")
    evidence_ids: list[str] = Field(..., min_length=1, description="Obligatorio: al menos una evidencia auditable")
    company_ids: list[str] = Field(default_factory=list)
    signal_ids: list[str] = Field(default_factory=list)
    confidence: float = Field(default=0.8, ge=0.0, le=1.0)
    status: str = Field(default="draft", description="draft, verified, candidate, rejected")

    @field_validator("evidence_ids")
    @classmethod
    def require_evidence(cls, v: list[str]) -> list[str]:
        if not v:
            raise ValueError("Un Problem exige al menos un evidence_id. Sin evidencia, no entra.")
        return v
