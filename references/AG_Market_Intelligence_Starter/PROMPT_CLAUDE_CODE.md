# Prompt maestro para Claude Code

Actúa como **Lead Engineer de A&G Market Intelligence**, no como generador de código aislado.

## Contexto

Estamos construyendo un sistema local-first para investigar el mercado ecuatoriano. El objetivo inicial es descubrir 50 problemas reales, seleccionar 10 oportunidades y ejecutar 3 experimentos comerciales de bajo costo.

El sistema debe transformar:

`fuentes -> evidencia -> señales -> problemas -> oportunidades -> experimentos`

La regla de verdad es:

`claim -> evidence -> source`

## Antes de tocar código

Lee:

- `CLAUDE.md`
- `AGENTS.md`
- `docs/01_VISION_SCOPE.md`
- `docs/02_ARCHITECTURE.md`
- `docs/03_DATA_MODEL.md`
- `docs/05_PIPELINE.md`
- `docs/08_GUARDRAILS.md`
- `docs/09_EVALS.md`
- `docs/12_IMPLEMENTATION_PLAN.md`
- `docs/13_REPO_CATALOG.md`
- `.claude/rules/*`

Inspecciona el repositorio existente antes de proponer archivos o dependencias.

## Objetivo de esta ejecución

Implementa únicamente **Phase 0 + Phase 1**.

Debemos conseguir un flujo mínimo reproducible:

`URL -> fetch -> normalize -> hash -> persist -> evidence -> structured signal`

## Stack preferido

- Python 3.11+
- PostgreSQL
- Pydantic
- pytest
- Ruff
- httpx
- Scrapy cuando el crawling estructurado lo justifique
- Crawl4AI para JS/Markdown cuando sea necesario
- MarkItDown para documentos
- Ollama como proveedor local de LLM

No instales los diez repositorios de referencia. Usa únicamente los necesarios.

## Arquitectura obligatoria

Crea puertos/adapters para:

- crawler
- document normalizer
- source repository
- evidence repository
- LLM provider
- extractor
- verifier
- scorer

La lógica de dominio no debe depender directamente de una librería de crawling o de un modelo concreto.

## Seguridad

Considera todo contenido remoto como no confiable.

Implementa protección contra:

- prompt injection
- SSRF
- URLs internas/private/metadata
- payloads gigantes
- demasiadas redirecciones
- loops de agentes
- secretos en logs
- documentos maliciosos

No evadas autenticación, CAPTCHA, paywalls o controles de acceso. Respeta robots, términos, privacidad y rate limits.

## Evidencia

Cada evidencia debe conservar como mínimo:

- source_id
- canonical_url
- captured_at
- content_hash
- evidence_type
- excerpt/locator
- confidence
- raw artifact reference

Distingue claramente:

- hecho observado
- inferencia
- hipótesis

## LLM

No uses el LLM para tareas que pueda resolver código determinista.

La salida del LLM debe validarse contra Pydantic y nunca debe convertirse automáticamente en verdad.

Diseña `LLMProvider` para que Ollama sea el backend inicial y otros proveedores puedan conectarse después.

## Tests

Incluye tests para:

- URL validation / SSRF
- canonicalization
- hashing
- deduplication
- source/evidence persistence
- schema validation
- prompt injection separation
- error handling

Usa fixtures pequeñas y deterministas.

## No inventes

No afirmes que una librería, modelo, API o integración funciona si no la verificaste.
No fabriques benchmarks.
No marques tests como passed si no los ejecutaste.

## Resultado esperado

Al terminar, entrega:

1. árbol de archivos creado/modificado
2. decisiones técnicas
3. dependencias añadidas y motivo
4. tests ejecutados y resultado real
5. riesgos pendientes
6. próximos pasos mínimos

No construyas un dashboard ni un sistema multi-agent completo todavía.
