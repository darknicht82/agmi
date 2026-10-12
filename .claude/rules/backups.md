# Backup Ley (AGNexus)

Antes de procesar o modificar cualquier archivo, crear copia de seguridad jerárquica en:

```text
H:\Projects\agnexus\agmarketintelligence\.backups\<fecha-hito>\
```

- Los backups son **permanentes e inmutables**. NO se borran.
- Cada proyecto es dueño de sus backups. **NUNCA** escribir en `.backups/` de otro proyecto.
- El destino es `.backups/` de ESTE proyecto, no de centavo-sync-pro ni nexo-pulse.

## Cómo

```bash
bash scripts/backup.sh            # crea .backups/<fecha-hito>/ con el estado actual
bash scripts/backup.sh pre_hito   # etiqueta legible para el hito
```

Idempotente: puede re-ejecutarse; crea un timestamp nuevo cada vez (no pisa el anterior).
