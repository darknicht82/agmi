# 02 — Arquitectura

## Capas

1. **Sources** — registro de fuentes, URLs, permisos y frecuencia.
2. **Acquisition** — HTTP, [HERRAMIENTA-CRAWL-VOLUMEN], [HERRAMIENTA-CRAWL-JS] y, excepcionalmente, [HERRAMIENTA-NAVEGADOR-AGENTE].
3. **Raw storage** — captura original, metadata y hashes.
4. **Normalization** — HTML/documentos a texto/Markdown estructurado.
5. **Evidence** — fragmentos trazables con procedencia.
6. **Extraction** — señales, empresas, problemas y atributos mediante schemas.
7. **Verification** — corroboración y detección de contradicciones.
8. **Knowledge** — [BD-PRINCIPAL] para entidades y relaciones.
9. **Scoring** — priorización de problemas/oportunidades.
10. **Reporting** — Markdown/CSV/JSON inicialmente.
11. **Agentic layer** — orquestación, MCP y agentes **después** del MVP.

> Nota de nomenclatura: los nombres técnicos reales viven en `docs/_mapeo_interno.md` y `repo-manifest.json`. Ver `docs/13_politica_nomenclatura.md`.

## Puertos / adapters

Interfaces a definir (el dominio **no** depende de ninguna herramienta concreta):

- `Crawler`
- `DocumentNormalizer`
- `EvidenceRepository`
- `SourceRepository`
- `LLMProvider`
- `Extractor`
- `Verifier`
- `Scorer`
- `ReportWriter`

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

Flujo rector (de `base4.md`):

```text
FUENTES → CAPTURA → NORMALIZACIÓN → EVIDENCIA → SEÑALES → VERIFICACIÓN
        → PROBLEMAS → OPORTUNIDADES → EXPERIMENTOS COMERCIALES

CLAIM → EVIDENCE → SOURCE
```

## Persistencia

[BD-PRINCIPAL] es la fuente operativa del conocimiento estructurado. Los archivos raw/evidence permanecen como artefactos de trazabilidad.

## Regla de selección de crawler

| Necesidad | Herramienta |
| :--- | :--- |
| HTTP simple | cliente HTTP ligero |
| HTML estructurado y volumen | [HERRAMIENTA-CRAWL-VOLUMEN] |
| JS/renderizado + Markdown | [HERRAMIENTA-CRAWL-JS] |
| DOM cambiante | [HERRAMIENTA-ADAPTATIVA] |
| interacción real con navegador | [HERRAMIENTA-NAVEGADOR-AGENTE] |

No instalar todas como dependencias obligatorias.

## Camino corto primero

```text
URL → fetch → normalize → hash → persist source → persist evidence → structured signal
```

Solo cuando eso funcione de forma fiable: crawling masivo, clustering, agentes, MCP.
