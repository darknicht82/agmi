#!/usr/bin/env bash
# Verificación local — A&G Market Intelligence
# tests + lint + typecheck. Un solo camino: si algo falla, sale con error duro.
# Uso: bash scripts/verify.sh

set -euo pipefail

PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "${PROJECT_ROOT}"

echo "== Backup Ley previo (regla AGNexus) =="
bash scripts/backup.sh pre_verify

echo ""
echo "== pytest =="
python -m pytest tests/

echo ""
echo "== ruff check =="
python -m ruff check src tests

echo ""
echo "== mypy =="
python -m mypy src

echo ""
echo "Verificación completa OK."
