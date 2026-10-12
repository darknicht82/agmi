Sí, seguimos. 👍

Y esta vez ya dejé **creado físicamente el paquete inicial**, no solamente el contenido conceptual que habíamos definido.

### 📦 Starter de A&G Market Intelligence

[**Descargar AG_Market_Intelligence_Starter.zip**](sandbox:/mnt/data/AG_Market_Intelligence_Starter.zip)

Incluye **28 archivos** con la estructura base:

```text
AG_Market_Intelligence_Starter/
│
├── README.md
├── CLAUDE.md
├── AGENTS.md
├── PROMPT_CLAUDE_CODE.md
├── repo-manifest.json
│
├── docs/
│   ├── 01_VISION_SCOPE.md
│   ├── 02_ARCHITECTURE.md
│   ├── 03_DATA_MODEL.md
│   ├── 04_SOURCE_REGISTRY.md
│   ├── 05_PIPELINE.md
│   ├── 06_AGENT_SYSTEM.md
│   ├── 07_MCP_AND_TOOLS.md
│   ├── 08_GUARDRAILS.md
│   ├── 09_EVALS.md
│   ├── 10_OBSERVABILITY.md
│   ├── 11_INFERENCE_ECONOMICS.md
│   ├── 12_IMPLEMENTATION_PLAN.md
│   ├── 13_REPO_CATALOG.md
│   ├── 14_50_PROBLEMS_SCHEMA.md
│   └── 15_SECURITY_LEGAL.md
│
├── .claude/
│   └── rules/
│       ├── security.md
│       ├── evidence.md
│       └── tool-selection.md
│
├── src/
├── tests/
└── data/
    ├── raw/
    ├── processed/
    └── evidence/
```

### Lo importante

No planteé esto como:

> "vamos a crear un scraper con IA".

Lo estructuré como **un sistema de inteligencia de mercado**, donde el scraper es solamente una de las capas.

El flujo central queda:

```text
FUENTES
   ↓
CAPTURA
   ↓
NORMALIZACIÓN
   ↓
EVIDENCIA
   ↓
SEÑALES
   ↓
VERIFICACIÓN
   ↓
PROBLEMAS
   ↓
OPORTUNIDADES
   ↓
EXPERIMENTOS COMERCIALES
```

Y la regla que va a gobernar todo:

```text
CLAIM
  ↓
EVIDENCE
  ↓
SOURCE
```

Eso es particularmente importante para nosotros porque **no queremos que Claude invente "problemas del mercado" basándose simplemente en lo que el modelo cree**.

---

### También dejé preparado Claude Code

El archivo:

```text
PROMPT_CLAUDE_CODE.md
```

ya contiene el prompt maestro para que Claude:

- lea la arquitectura;
- inspeccione el repositorio;
- implemente primero Phase 0 + Phase 1;
- use Python/PostgreSQL/Pydantic;
- mantenga ports/adapters;
- utilice Ollama como LLM local;
- incorpore Crawl4AI/MarkItDown cuando corresponda;
- no instale los 10 proyectos;
- implemente protección SSRF;
- considere el contenido web como **untrusted data**;
- proteja contra prompt injection;
- mantenga trazabilidad;
- escriba tests;
- no invente resultados.

### Y algo que considero importante

**No le estamos diciendo a Claude que construya todo de una.**

Primero tiene que conseguir esto:

```text
URL
 ↓
FETCH
 ↓
NORMALIZE
 ↓
HASH
 ↓
PERSIST
 ↓
EVIDENCE
 ↓
STRUCTURED SIGNAL
```

Cuando eso funcione bien, recién pasamos a crawling masivo, clustering, agentes, MCP, etc.

Eso reduce muchísimo el riesgo de terminar con una arquitectura espectacular que **no produce información comercialmente útil**.

---

## Siguiente paso

Yo haría ahora algo todavía más importante antes de entregárselo a Claude:

**construir el `Phase 0` real del proyecto**, es decir:

```text
docker-compose.yml
pyproject.toml
.env.example
src/
    core/
    domain/
    ports/
    adapters/
    ingestion/
    evidence/
    normalization/
    llm/
tests/
```

más el esquema inicial de PostgreSQL y los primeros tests de seguridad.

Ahí ya dejamos de estar solamente en la documentación y empezamos a tener **el esqueleto ejecutable de A&G Market Intelligence**.

Y después sí podemos darle el ZIP a Claude Code para que continúe desde una base muy controlada.
