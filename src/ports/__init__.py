"""Puertos del dominio (interfaces).

El dominio NO depende de ninguna herramienta concreta.
Las implementaciones viven en `src/adapters/`.
"""

from __future__ import annotations

from typing import Protocol


class Crawler(Protocol):
    """Adquisición de contenido. Una URL entra, un documento capturado sale."""

    def fetch(self, url: str) -> bytes: ...


class DocumentNormalizer(Protocol):
    """HTML/PDF/Office -> texto/Markdown estructurado."""

    def normalize(self, raw: bytes, content_type: str) -> str: ...


class SourceRepository(Protocol):
    """Registro de fuentes. Upsert por URL canónica (idempotencia)."""

    def upsert(self, canonical_url: str, source_type: str, **meta: object) -> str: ...


class EvidenceRepository(Protocol):
    """Unidad mínima auditable. Upsert por content_hash (idempotencia)."""

    def save(
        self,
        source_id: str,
        canonical_url: str,
        content_hash: str,
        excerpt: str,
        locator: str,
        captured_at: str,
    ) -> str: ...


class LLMProvider(Protocol):
    """Proveedor de inferencia. El dominio no conoce el proveedor concreto."""

    def complete(self, prompt: str, schema: dict[str, object]) -> dict[str, object]: ...


class Extractor(Protocol):
    """Evidence -> Signals / Problems / Companies."""

    def extract(self, evidence_text: str) -> dict[str, object]: ...


class Verifier(Protocol):
    """Comprueba que los claims estén soportados por evidencia."""

    def verify(self, claim: str, evidence_ids: list[str]) -> bool: ...


class Scorer(Protocol):
    """Score reproducible por reglas. Nunca intuición del modelo."""

    def score(self, problem: dict[str, object]) -> float: ...


class ReportWriter(Protocol):
    """Salidas interoperables: Markdown / CSV / JSON / XLSX."""

    def write(self, report: dict[str, object], fmt: str, path: str) -> None: ...
