"""Almacenamiento de archivos idempotente y trazable en disco.

Reglas AGNexus:
- Idempotencia: almacenar dos veces el mismo contenido con el mismo hash es un no-op seguro.
- Cero fallbacks: si un directorio o archivo requerido no existe al leer, error duro y visible.
- Atomicidad: escrituras con atomic rename para evitar estados parciales corruptos.
"""

from __future__ import annotations

import json
from pathlib import Path
from tempfile import NamedTemporaryFile

from src.domain.models import Evidence


class StorageError(RuntimeError):
    """Error en la capa de almacenamiento de archivos."""


def save_raw_content(
    content: bytes,
    content_hash: str,
    ext: str = "html",
    data_dir: str | Path = "data",
) -> Path:
    """Guarda contenido crudo particionado por los primeros 2 caracteres del hash SHA-256.

    Ruta: {data_dir}/raw/{hash[:2]}/{content_hash}.{ext}
    Idempotente: si ya existe con el mismo tamaño, no lo sobreescribe innecesariamente.
    """
    if not content_hash or len(content_hash) < 2:
        raise StorageError(f"content_hash inválido: {content_hash!r}")

    base_path = Path(data_dir) / "raw" / content_hash[:2]
    base_path.mkdir(parents=True, exist_ok=True)

    clean_ext = ext.lstrip(".")
    target_file = base_path / f"{content_hash}.{clean_ext}"

    if target_file.exists() and target_file.stat().st_size == len(content):
        return target_file

    # Escritura atómica
    with NamedTemporaryFile(dir=base_path, delete=False, suffix=".tmp") as temp_file:
        temp_path = Path(temp_file.name)
        try:
            temp_file.write(content)
            temp_file.flush()
        except Exception as exc:
            temp_path.unlink(missing_ok=True)
            raise StorageError(f"Error escribiendo archivo crudo en {target_file}: {exc}") from exc

    temp_path.replace(target_file)
    return target_file


def save_evidence_metadata(evidence: Evidence, data_dir: str | Path = "data") -> Path:
    """Persiste metadatos estructurados de una Evidence en data/evidence/{evidence.id}.json.

    Idempotente y atómico.
    """
    base_path = Path(data_dir) / "evidence"
    base_path.mkdir(parents=True, exist_ok=True)

    target_file = base_path / f"{evidence.id}.json"
    raw_json = evidence.model_dump_json(indent=2)

    with NamedTemporaryFile(dir=base_path, delete=False, suffix=".tmp", mode="w", encoding="utf-8") as temp_file:
        temp_path = Path(temp_file.name)
        try:
            temp_file.write(raw_json)
            temp_file.flush()
        except Exception as exc:
            temp_path.unlink(missing_ok=True)
            raise StorageError(f"Error escribiendo metadata de evidence en {target_file}: {exc}") from exc

    temp_path.replace(target_file)
    return target_file


def load_evidence_metadata(evidence_id: str, data_dir: str | Path = "data") -> Evidence:
    """Carga una Evidence desde disco. Falla con FileNotFoundError si no existe (cero fallbacks)."""
    target_file = Path(data_dir) / "evidence" / f"{evidence_id}.json"
    if not target_file.is_file():
        raise FileNotFoundError(
            f"No existe el archivo de evidencia: {target_file}. "
            f"Regla de trazabilidad: una evidencia debe existir en disco."
        )

    with target_file.open("r", encoding="utf-8") as f:
        data = json.load(f)

    return Evidence.model_validate(data)
