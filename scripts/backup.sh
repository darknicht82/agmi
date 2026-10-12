#!/usr/bin/env bash
# Backup Ley (AGNexus) — A&G Market Intelligence
# Crea una copia jerárquica en .backups/<fecha-hito>/ de ESTE proyecto.
# Permanente e inmutable. Nunca se escribe en .backups/ de otro proyecto.
# Idempotente: cada ejecución crea un timestamp nuevo (no pisa el anterior).
#
# Uso:
#   bash scripts/backup.sh            # hito con timestamp
#   bash scripts/backup.sh pre_hito   # etiqueta legible

set -euo pipefail

PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
LABEL="${1:-hito}"
TIMESTAMP="$(date +%Y%m%d_%H%M%S)"
DEST="${PROJECT_ROOT}/.backups/${LABEL}_${TIMESTAMP}"

if [ ! -d "${PROJECT_ROOT}" ]; then
  echo "ERROR: no se encuentra la raíz del proyecto: ${PROJECT_ROOT}" >&2
  exit 1
fi

mkdir -p "${DEST}"

# Copia jerárquica de todo excepto .backups (no auto-replicarse) y artefactos de entorno.
# Se usa rsync si existe; si no, tar. Un solo camino de datos: sin fallback silencioso
# entre rutas de destino — el destino es siempre ${DEST}.
if command -v rsync >/dev/null 2>&1; then
  rsync -a \
    --exclude '.backups' \
    --exclude '.git' \
    --exclude '__pycache__' \
    --exclude '.venv' \
    --exclude 'node_modules' \
    "${PROJECT_ROOT}/" "${DEST}/"
else
  tar -cf - \
    --exclude '.backups' \
    --exclude '.git' \
    --exclude '__pycache__' \
    --exclude '.venv' \
    -C "${PROJECT_ROOT}" . | tar -xf - -C "${DEST}"
fi

# Manifiesto de trazabilidad del propio backup
{
  echo "project: agmarketintelligence"
  echo "label: ${LABEL}"
  echo "created_at: $(date -Iseconds)"
  echo "source: ${PROJECT_ROOT}"
  echo "dest: ${DEST}"
} > "${DEST}/.backup-manifest"

FILE_COUNT="$(find "${DEST}" -type f | wc -l | tr -d ' ')"
echo "Backup Ley completo: ${DEST}"
echo "Archivos: ${FILE_COUNT}"
echo "PERMANENTE — no borrar."
