from pathlib import Path

import pytest
from src.ingestion.registry import SourceRegistry, SourceRegistryError


def test_registry_loading_and_lookup() -> None:
    seed_file = Path("data/seed/fuentes_ecuador.json")
    registry = SourceRegistry.from_json(seed_file)

    source = registry.get_by_id("src_computrabajo_ec")
    assert source.id == "src_computrabajo_ec"
    assert source.country == "EC"
    assert source.domain == "ec.computrabajo.com"

    # Lookup por dominio
    src_by_dom = registry.get_by_domain("ec.computrabajo.com")
    assert src_by_dom is not None
    assert src_by_dom.id == "src_computrabajo_ec"

    # Dominio no registrado
    assert not registry.is_domain_allowed("sitio-desconocido.xyz")


def test_registry_unknown_source_raises() -> None:
    seed_file = Path("data/seed/fuentes_ecuador.json")
    registry = SourceRegistry.from_json(seed_file)

    with pytest.raises(SourceRegistryError, match="no está registrada"):
        registry.get_by_id("src_fantasma")
