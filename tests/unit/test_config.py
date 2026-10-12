"""Tests de la regla de cero fallbacks en la configuración."""

from __future__ import annotations

import os
from collections.abc import Iterator

import pytest
from src.config.settings import ConfigError, load_settings

_REQUIRED = {
    "POSTGRES_HOST",
    "POSTGRES_PORT",
    "POSTGRES_DB",
    "POSTGRES_USER",
    "POSTGRES_PASSWORD",
    "DATA_DIR",
    "CRAWL_RATE_LIMIT_PER_MIN",
    "HTTP_TIMEOUT_SECONDS",
    "HTTP_MAX_RESPONSE_BYTES",
    "HTTP_MAX_REDIRECTS",
    "RUN_ENV",
    "LOG_LEVEL",
}

_VALID = {
    "POSTGRES_HOST": "localhost",
    "POSTGRES_PORT": "5432",
    "POSTGRES_DB": "agmarket",
    "POSTGRES_USER": "agmarket",
    "POSTGRES_PASSWORD": "test-only-not-a-secret",
    "DATA_DIR": "./data",
    "CRAWL_RATE_LIMIT_PER_MIN": "6",
    "HTTP_TIMEOUT_SECONDS": "30",
    "HTTP_MAX_RESPONSE_BYTES": "10485760",
    "HTTP_MAX_REDIRECTS": "3",
    "RUN_ENV": "dev",
    "LOG_LEVEL": "INFO",
}


@pytest.fixture(autouse=True)
def _clean_env() -> Iterator[None]:
    saved = {k: os.environ.get(k) for k in _REQUIRED}
    for key in _REQUIRED:
        os.environ.pop(key, None)
    yield
    for key, value in saved.items():
        if value is None:
            os.environ.pop(key, None)
        else:
            os.environ[key] = value


def test_load_settings_ok_with_full_env() -> None:
    os.environ.update(_VALID)
    settings = load_settings()
    assert settings.postgres_db == "agmarket"
    assert settings.http_max_redirects == 3
    assert settings.database_url.startswith("postgresql+psycopg://")


@pytest.mark.parametrize("missing", sorted(_REQUIRED))
def test_missing_required_variable_raises_hard_error(missing: str) -> None:
    env = dict(_VALID)
    del env[missing]
    os.environ.update(env)
    # Cero fallbacks: sin valor por defecto, error duro.
    with pytest.raises(ConfigError) as excinfo:
        load_settings()
    assert missing in str(excinfo.value)


def test_empty_variable_is_rejected_not_defaulted() -> None:
    env = dict(_VALID)
    env["POSTGRES_PASSWORD"] = ""
    os.environ.update(env)
    with pytest.raises(ConfigError):
        load_settings()


def test_non_integer_port_raises_hard_error() -> None:
    env = dict(_VALID)
    env["POSTGRES_PORT"] = "nope"
    os.environ.update(env)
    with pytest.raises(ConfigError) as excinfo:
        load_settings()
    assert "POSTGRES_PORT" in str(excinfo.value)
