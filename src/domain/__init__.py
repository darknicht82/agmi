"""Módulo de dominio — A&G Market Intelligence."""

from src.domain.canonical import (
    canonicalize_url,
    compute_content_hash,
    compute_text_hash,
)
from src.domain.models import (
    AccessPolicy,
    Evidence,
    EvidenceType,
    Problem,
    Signal,
    SignalType,
    Source,
    SourceType,
)

__all__ = [
    "AccessPolicy",
    "Evidence",
    "EvidenceType",
    "Problem",
    "Signal",
    "SignalType",
    "Source",
    "SourceType",
    "canonicalize_url",
    "compute_content_hash",
    "compute_text_hash",
]
