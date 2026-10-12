# 10 — Observabilidad

Cada ejecución debe tener `run_id`.

Registrar como mínimo:

- run_id
- source_id
- crawler
- started_at / finished_at
- duration
- pages
- bytes
- errors
- retries
- model
- tokens
- cache hit/miss
- extraction confidence
- human corrections

## Trace

`run -> source -> fetch -> normalize -> extraction -> verification -> scoring -> report`

Los logs deben permitir reconstruir por qué una oportunidad terminó en un reporte.
