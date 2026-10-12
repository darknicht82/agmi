# 02 — Arquitectura

## Capas

1. **Sources** — registro de fuentes, URLs, permisos y frecuencia.
2. **Acquisition** — HTTP, Scrapy, Crawl4AI y, excepcionalmente, Browser Use.
3. **Raw storage** — captura original, metadata y hashes.
4. **Normalization** — HTML/documentos a texto/Markdown estructurado.
5. **Evidence** — fragmentos trazables con procedencia.
6. **Extraction** — señales, empresas, problemas y atributos mediante schemas.
7. **Verification** — corroboración y detección de contradicciones.
8. **Knowledge** — PostgreSQL para entidades y relaciones.
9. **Scoring** — priorización de problemas/oportunidades.
10. **Reporting** — Markdown/CSV/JSON inicialmente.
11. **Agentic layer** — orquestación, MCP y agentes después del MVP.

## Puertos / adapters

Definir interfaces para:

- `Crawler`
- `DocumentNormalizer`
- `EvidenceRepository`
- `SourceRepository`
- `LLMProvider`
- `Extractor`
- `Verifier`
- `Scorer`
- `ReportWriter`

La lógica de dominio no debe depender de Scrapy, Crawl4AI, Ollama, PostgreSQL o un proveedor concreto.

## Flujo

```text
SourceRegistry
    -> Acquisition
    -> RawCapture
    -> Normalize
    -> Hash/Deduplicate
    -> EvidenceStore
    -> StructuredExtraction
    -> Verification
    -> ProblemClustering
    -> OpportunityScoring
    -> Report
```

## Persistencia

PostgreSQL es la fuente operativa del conocimiento estructurado. Los archivos raw/evidence permanecen como artefactos de trazabilidad.
