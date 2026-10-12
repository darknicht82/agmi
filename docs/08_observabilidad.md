# 08 — Observabilidad

## Registro por cada ejecución de pipeline

- `run_id`
- `source_id`
- crawler usado
- duration
- pages
- bytes
- errors
- retries
- modelo de inferencia usado
- input / output tokens
- estimated cost
- cache hit/miss
- extraction confidence
- human corrections

## Trazas

Cada ejecución debe poder reconstruirse:

```text
run
 ├── source
 ├── fetch
 ├── normalize
 ├── extraction
 ├── verification
 ├── scoring
 └── report
```

## Logs separados

- application logs
- crawler logs
- security logs
- audit logs

**Nunca registrar secretos** (ver `.claude/rules/security.md`).

## Economía de inferencia (integrada)

- Cache key: `content_hash + prompt_version + model + schema_version`
- Preferir reglas deterministas sobre inferencia
- Preferir modelo local sobre proveedor externo
- Medir costo por fuente / evidencia útil / problema validado / experimento

Ver `docs/07_evals.md`.
