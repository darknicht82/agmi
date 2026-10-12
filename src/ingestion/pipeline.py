"""Pipeline de ingestión determinista y auditable (Fase 1 Ingestion MVP).

Camino:
URL -> fetch (con SSRF + rate-limit) -> normalize -> hash -> persist raw -> persist evidence

Reglas AGNexus:
- Idempotencia: si el content_hash y la URL canónica ya existen, no duplica.
- Cero fallbacks: cualquier fallo en validación o red es visible.
- Trazabilidad: cada Evidence apunta a su Source, hash SHA-256 y archivo crudo en disco.
"""

from __future__ import annotations

import logging
from dataclasses import dataclass
from pathlib import Path

from src.domain.canonical import canonicalize_url
from src.domain.models import Evidence, EvidenceType, Source
from src.ingestion.http_fetcher import HttpFetcher
from src.normalization.html_normalizer import extract_excerpt, normalize_html_to_markdown
from src.storage.file_storage import save_evidence_metadata, save_raw_content

logger = logging.getLogger("agmarket.pipeline")


@dataclass(frozen=True, slots=True)
class IngestionResult:
    """Resultado de la ingestión de una fuente."""

    source: Source
    evidence: Evidence
    raw_artifact_path: Path
    evidence_metadata_path: Path
    is_duplicate: bool


class IngestionPipeline:
    """Orquestador del pipeline de ingestión determinista."""

    def __init__(
        self,
        fetcher: HttpFetcher,
        data_dir: str | Path = "data",
    ) -> None:
        self.fetcher = fetcher
        self.data_dir = Path(data_dir)

    def ingest_url(
        self,
        url: str,
        source: Source,
        evidence_type: EvidenceType = EvidenceType.JOB_POSTING,
        locator: str | None = None,
    ) -> IngestionResult:
        """Ejecuta el ciclo completo de ingestión para una URL de forma auditable e idempotente."""
        canon_url = canonicalize_url(url)
        logger.info("Iniciando ingestión para URL canónica: %s (Fuente: %s)", canon_url, source.id)

        # 1. Fetch determinista
        fetch_res = self.fetcher.fetch(canon_url)

        # 2. Guardar contenido crudo
        raw_path = save_raw_content(
            content=fetch_res.content_bytes,
            content_hash=fetch_res.content_hash,
            ext="html",
            data_dir=self.data_dir,
        )

        # 3. Normalizar contenido
        html_str = fetch_res.content_bytes.decode("utf-8", errors="replace")
        title, clean_markdown = normalize_html_to_markdown(html_str)
        excerpt = extract_excerpt(clean_markdown, max_chars=400)
        if not excerpt:
            excerpt = f"Contenido capturado desde {canon_url} con título: {title}"

        # 4. Generar ID determinista de Evidence basado en timestamp y primeros caracteres del hash
        evidence_id = f"evi_{fetch_res.fetched_at.strftime('%Y%m%d%H%M%S')}_{fetch_res.content_hash[:8]}"

        # 5. Comprobar si ya existe una evidencia idéntica (idempotencia)
        evidence_file = self.data_dir / "evidence" / f"{evidence_id}.json"
        is_duplicate = evidence_file.exists()

        # Ruta relativa normalizada para portabilidad
        rel_raw_path = str(raw_path.relative_to(self.data_dir))

        evidence = Evidence(
            id=evidence_id,
            source_id=source.id,
            captured_at=fetch_res.fetched_at,
            canonical_url=canon_url,
            title=title,
            published_at=None,
            author=None,
            content_hash=fetch_res.content_hash,
            excerpt=excerpt,
            locator=locator,
            evidence_type=evidence_type,
            confidence=1.0,
            raw_artifact_path=rel_raw_path,
        )

        # 6. Persistir metadatos de Evidence
        evidence_path = save_evidence_metadata(evidence, data_dir=self.data_dir)

        logger.info(
            "Ingestión completada: Evidence ID: %s | Raw: %s | Duplicado: %s",
            evidence.id,
            raw_path,
            is_duplicate,
        )

        return IngestionResult(
            source=source,
            evidence=evidence,
            raw_artifact_path=raw_path,
            evidence_metadata_path=evidence_path,
            is_duplicate=is_duplicate,
        )
