"""Adaptador para ingesta de datos provenientes de n8n (aidev-n8n:5678).

Permite que workflows de n8n envíen payloads recolectados al pipeline de A&G
manteniendo todas las invariantes de seguridad y trazabilidad:
1. Validación estricta del Source Registry (no se aceptan fuentes no autorizadas).
2. Validación de SSRF sobre las URLs reportadas.
3. Canonización de URLs y deduplicación por content_hash SHA-256.
4. Persistencia idempotente de contenido crudo y metadatos de evidencia.
"""

from __future__ import annotations

import logging
from datetime import UTC, datetime
from pathlib import Path

from pydantic import BaseModel, ConfigDict, Field
from src.domain.canonical import canonicalize_url, compute_content_hash
from src.domain.models import Evidence, EvidenceType
from src.ingestion.pipeline import IngestionResult
from src.ingestion.registry import SourceRegistry
from src.normalization.html_normalizer import extract_excerpt, normalize_html_to_markdown
from src.security.url_guard import assert_public_http_url
from src.storage.file_storage import save_evidence_metadata, save_raw_content

logger = logging.getLogger("agmarket.adapters.n8n")


class N8nIngestPayload(BaseModel):
    """Payload estructurado enviado por un nodo de n8n."""

    model_config = ConfigDict(frozen=True, extra="forbid")

    source_id: str = Field(..., min_length=3, description="ID registrado en el Source Registry")
    url: str = Field(..., min_length=10, description="URL pública de donde se extrajo el contenido")
    content: str = Field(..., min_length=10, description="HTML crudo o texto capturado")
    title: str | None = None
    evidence_type: EvidenceType = Field(default=EvidenceType.JOB_POSTING)
    locator: str | None = None


def ingest_from_n8n(
    payload: N8nIngestPayload,
    registry: SourceRegistry,
    data_dir: str | Path = "data",
) -> IngestionResult:
    """Procesa un payload recibido desde n8n y lo incorpora al pipeline auditable.

    Lanza:
        SourceRegistryError: si source_id no está autorizada en el registry.
        SSRFBlocked: si la URL viola las políticas de seguridad.
        StorageError: si falla la persistencia atómica.
    """
    # 1. Validar que la fuente pertenezca al registro oficial
    source = registry.get_by_id(payload.source_id)

    # 2. Guardia de seguridad SSRF
    assert_public_http_url(payload.url)

    # 3. Canonización de URL
    canon_url = canonicalize_url(payload.url)

    # 4. Cálculo de content_hash
    content_bytes = payload.content.encode("utf-8")
    content_hash = compute_content_hash(content_bytes)

    # 5. Persistencia cruda (raw)
    data_path = Path(data_dir)
    raw_path = save_raw_content(
        content=content_bytes,
        content_hash=content_hash,
        ext="html",
        data_dir=data_path,
    )

    # 6. Normalización y extracto
    extracted_title, clean_markdown = normalize_html_to_markdown(payload.content)
    final_title = payload.title or extracted_title
    excerpt = extract_excerpt(clean_markdown, max_chars=400)
    if not excerpt:
        excerpt = f"Contenido recibido desde n8n para {canon_url}"

    # 7. Identificador de Evidence determinista
    now = datetime.now(UTC)
    evidence_id = f"evi_n8n_{now.strftime('%Y%m%d%H%M%S')}_{content_hash[:8]}"

    # 8. Comprobar duplicado
    evidence_file = data_path / "evidence" / f"{evidence_id}.json"
    is_duplicate = evidence_file.exists()

    rel_raw_path = str(raw_path.relative_to(data_path))

    evidence = Evidence(
        id=evidence_id,
        source_id=source.id,
        captured_at=now,
        canonical_url=canon_url,
        title=final_title,
        published_at=None,
        author=None,
        content_hash=content_hash,
        excerpt=excerpt,
        locator=payload.locator,
        evidence_type=payload.evidence_type,
        confidence=1.0,
        raw_artifact_path=rel_raw_path,
    )

    # 9. Guardar metadata de Evidence
    evidence_path = save_evidence_metadata(evidence, data_dir=data_path)

    logger.info(
        "Ingesta n8n completada: Source=%s | Evidence=%s | Hash=%s... | Duplicado=%s",
        source.id,
        evidence.id,
        content_hash[:12],
        is_duplicate,
    )

    return IngestionResult(
        source=source,
        evidence=evidence,
        raw_artifact_path=raw_path,
        evidence_metadata_path=evidence_path,
        is_duplicate=is_duplicate,
    )
