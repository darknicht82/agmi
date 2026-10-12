"""Configuración estricta — regla de cero fallbacks (AGNexus).

Un dato -> una fuente -> un camino. Si falta una variable obligatoria,
se lanza error duro y visible. Nunca default silencioso.
"""

from __future__ import annotations

import os
from dataclasses import dataclass


class ConfigError(RuntimeError):
    """Falta o es inválida una variable de entorno obligatoria."""


def _require(name: str) -> str:
    value = os.environ.get(name)
    if value is None or value == "":
        raise ConfigError(
            f"Falta la variable de entorno obligatoria: {name}. "
            f"Defínela en .env (ver .env.example). Sin fallback."
        )
    return value


def _require_int(name: str) -> int:
    raw = _require(name)
    try:
        return int(raw)
    except ValueError as exc:
        raise ConfigError(
            f"La variable {name} debe ser un entero; se recibió: {raw!r}"
        ) from exc


@dataclass(frozen=True, slots=True)
class Settings:
    """Configuración validada del sistema. Inmutable."""

    postgres_host: str
    postgres_port: int
    postgres_db: str
    postgres_user: str
    postgres_password: str
    data_dir: str
    crawl_rate_limit_per_min: int
    http_timeout_seconds: int
    http_max_response_bytes: int
    http_max_redirects: int
    run_env: str
    log_level: str

    @property
    def database_url(self) -> str:
        return (
            f"postgresql+psycopg://{self.postgres_user}:{self.postgres_password}"
            f"@{self.postgres_host}:{self.postgres_port}/{self.postgres_db}"
        )


def load_settings() -> Settings:
    """Carga la configuración. Falla con ConfigError si falta algo obligatorio.

    Cero fallbacks: no existe valor por defecto para ninguna variable obligatoria.
    """
    return Settings(
        postgres_host=_require("POSTGRES_HOST"),
        postgres_port=_require_int("POSTGRES_PORT"),
        postgres_db=_require("POSTGRES_DB"),
        postgres_user=_require("POSTGRES_USER"),
        postgres_password=_require("POSTGRES_PASSWORD"),
        data_dir=_require("DATA_DIR"),
        crawl_rate_limit_per_min=_require_int("CRAWL_RATE_LIMIT_PER_MIN"),
        http_timeout_seconds=_require_int("HTTP_TIMEOUT_SECONDS"),
        http_max_response_bytes=_require_int("HTTP_MAX_RESPONSE_BYTES"),
        http_max_redirects=_require_int("HTTP_MAX_REDIRECTS"),
        run_env=_require("RUN_ENV"),
        log_level=_require("LOG_LEVEL"),
    )
