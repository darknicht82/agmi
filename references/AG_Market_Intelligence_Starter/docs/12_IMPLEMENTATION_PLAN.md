# 12 — Plan de implementación

## Phase 0 — Bootstrap

- Python 3.11+
- Docker Compose
- PostgreSQL
- Pydantic
- pytest
- Ruff
- `.env.example`
- estructura de puertos/adapters

## Phase 1 — Ingestion MVP

- source registry
- HTTP fetcher
- raw storage
- canonicalization
- hashing
- PostgreSQL
- MarkItDown
- Crawl4AI

## Phase 2 — Extraction

- schemas Pydantic
- proveedor LLM local
- extracción estructurada
- validación
- confidence

## Phase 3 — Research

- Scrapy
- queues
- crawling programado
- deduplicación
- clustering

## Phase 4 — Verification

- corroboración
- contradicciones
- source weighting

## Phase 5 — Opportunity engine

- scoring
- competitor analysis
- commercial fit

## Phase 6 — Reporting

- Markdown
- CSV/JSON
- eventualmente dashboard

## Phase 7 — Agentic/MCP

Solo después de que el pipeline determinista sea estable.

## Milestones

M1: 10 problemas respaldados.
M2: 50 problemas.
M3: 10 oportunidades.
M4: 3 experimentos comerciales.
