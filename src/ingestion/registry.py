"""Registro explícito de fuentes de A&G Market Intelligence.

Reglas:
- No hay crawling ciego: todo dominio debe estar previamente registrado en el registry.
- Cero fallbacks: si se solicita una fuente no registrada o inactiva, error duro.
- Filtro geográfico verificable: fuentes con relación directa con Ecuador.
"""

from __future__ import annotations

import json
from pathlib import Path

from src.domain.models import Source


class SourceRegistryError(RuntimeError):
    """Error en el registro de fuentes."""


class SourceRegistry:
    """Administrador en memoria del registro explícito de fuentes."""

    def __init__(self, sources: list[Source]) -> None:
        self._sources_by_id: dict[str, Source] = {s.id: s for s in sources}
        self._sources_by_domain: dict[str, Source] = {s.domain.lower(): s for s in sources}

    @classmethod
    def from_json(cls, json_path: Path | str) -> SourceRegistry:
        path = Path(json_path)
        if not path.is_file():
            raise FileNotFoundError(f"Archivo de registro no encontrado: {path}")

        with path.open("r", encoding="utf-8") as f:
            data = json.load(f)

        if not isinstance(data, list):
            raise SourceRegistryError(f"Se esperaba una lista de fuentes en {path}")

        sources = [Source.model_validate(item) for item in data]
        return cls(sources)

    def get_by_id(self, source_id: str) -> Source:
        source = self._sources_by_id.get(source_id)
        if source is None:
            raise SourceRegistryError(
                f"Fuente '{source_id}' no está registrada en el Source Registry. "
                f"Regla de seguridad: solo se permite consultar fuentes registradas."
            )
        if not source.active:
            raise SourceRegistryError(f"La fuente '{source_id}' está inactiva.")
        return source

    def get_by_domain(self, domain: str) -> Source | None:
        clean_domain = domain.lower().lstrip("www.")
        # Búsqueda exacta o coincidencia por sufijo de dominio
        for d, src in self._sources_by_domain.items():
            if d == clean_domain or clean_domain.endswith(f".{d}") or d.endswith(f".{clean_domain}"):
                return src if src.active else None
        return None

    def is_domain_allowed(self, domain: str) -> bool:
        return self.get_by_domain(domain) is not None

    def list_active(self) -> list[Source]:
        return [s for s in self._sources_by_id.values() if s.active]
