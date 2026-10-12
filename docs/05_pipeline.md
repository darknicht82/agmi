# 05 — Pipeline de datos

## Etapa 0 — Seed

```json
{
  "url": "...",
  "source_type": "job|company|news|directory|document|competitor",
  "country": "EC",
  "tags": ["automation", "ai"]
}
```

## Etapa 1 — Fetch

Registrar: HTTP status · timestamp · final URL · content type · response time · crawler usado · error · `run_id`

## Etapa 2 — Capture

Conservar raw cuando sea legal y técnicamente razonable.

Separar: `data/raw/` · `data/processed/` · `data/evidence/`

## Etapa 3 — Normalize

- HTML → clean text/Markdown
- PDF → Markdown
- DOCX/XLSX/PPTX → Markdown
- JSON → canonical JSON

[CONVERSOR-DOCUMENTOS] principalmente para documentos. [HERRAMIENTA-CRAWL-JS] puede producir Markdown desde web.

## Etapa 4 — Deduplicate

Usar: canonical URL · content hash · normalized title · similarity

**No enviar duplicados al modelo.**

## Etapa 5 — Extract

El modelo recibe un schema estricto:

```json
{
  "facts": [],
  "signals": [],
  "problems": [],
  "companies": [],
  "claims_requiring_verification": []
}
```

## Etapa 6 — Verify

Para cada claim importante:

- ¿hay evidencia?
- ¿la evidencia realmente dice eso?
- ¿es hecho o inferencia?
- ¿hay otra fuente independiente?

## Etapa 7 — Score

Score reproducible (ver `docs/10_esquema_50_problemas.md`). Nunca puntuar desde la intuición del modelo.

## Etapa 8 — Persist

[BD-PRINCIPAL] como fuente de verdad. Búsqueda vectorial opcional y **no** sustituye la base relacional.

## Etapa 9 — Report

- top 50 problems
- top 10 opportunities
- top 3 experiments
- competitor map / map of alternatives
- source coverage
- confidence report

## Camino corto de validación (Fase 2)

```text
URL → fetch → normalize → hash → persist source → persist evidence → structured signal → persist candidate
```

Milestone de hecho: 1 página HTML + 1 PDF fixture procesados por el pipeline completo **en tests, sin red**.

## Cache de inferencia

Clave: `content_hash + prompt_version + model + schema_version`

No pagar dos veces por contenido idéntico.
