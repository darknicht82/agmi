# Plan — Arranque de A&G Market Intelligence

## Context

`H:\Projects\agnexus\agmarketintelligence` contiene solo `references/`:

| Qué es | Qué aporta |
| :--- | :--- |
| `inicio.md` (1858 líneas) | **Origen estratégico**: el porqué real (limbo financiero, ~$30 disponibles, capacidades sin convertir en activo). Ciclo 4 semanas, ofertas hipótesis, antifrágil. |
| `base.md` (1633 líneas) | Script generador del blueprint completo (15 docs + reglas + prompt maestro + manifiesto). |
| `base2.md` / `base3.md` | Análisis de herramientas; método de los 50 problemas desde evidencia. |
| `base4.md` (174 líneas) | **Confirmación del Starter materializado** + flujo central + regla CLAIM→EVIDENCE→SOURCE + "no construir todo de una" + siguiente paso Phase 0 ejecutable. |
| `AG_Market_Intelligence_Starter/` (28 archivos) | **Blueprint materializado y más limpio que las cadenas del script**: `README`, `CLAUDE.md`, `AGENTS.md`, `PROMPT_CLAUDE_CODE.md`, `repo-manifest.json`, `docs/01–15`, `.claude/rules/{security,evidence,tool-selection}`, `src/`, `tests/`, `data/{raw,processed,evidence}`. |
| 20 imágenes | Arquitectura de referencia (estructura GenAI/Agente IA/Production AI, Clean Architecture, DI, CI/CD, conectividad IA moderna, RAG variants, microservices/API gateway/webhooks). |

**Decisiones de usuario ya tomadas:**
1. Planes/análisis → `agmarketintelligence/docs/reportes_claude/YYYY-MM-DD-nombre.md`.
2. Nomenclatura de terceros: uso interno AGNexus/AGDevelop/Christian Aguirre por ahora, pero **sentar las bases** de qué poner y qué no para eventual comercialización. Regla de memoria actualizada: *identificadores ya desplegados y CHANGELOG histórico se quedan*.

### El porqué (de `inicio.md`)

> **"¿Qué problema puedo resolver con lo que ya sé hacer y conseguir que alguien me pague antes de construir demasiado?"**

Estrategia guía: **sobrevivir → observar → aprender → probar → cobrar → repetir → construir.**
Tres etapas: **Caja → Repetibilidad → Producto**. Cada experimento debe poder fallar sin hundir.

**Nada se fabrica:** `claim → evidence → source` obligatorio. El score nunca compensa ausencia de evidencia. Un número inventado no es línea base.

---

## Evaluación con tu perfil (lo que este plan debe frenar)

Conozco tu patrón: **amplia capacidad técnica + tendencia a construir mucho antes de comprobar si alguien quiere comprar**. `inicio.md` lo dice explícitamente. Por eso el plan se estructura para que el **primer valor sea comercial, no arquitectónico**:

| Tu riesgo | Salvaguarda en el plan |
| :--- | :--- |
| Construir la plataforma perfecta en vez de vender | El deliverable de la Semana 1 son **50 problemas con evidencia**, no código. La pista A (caja) va por delante de la pista B (plataforma). |
| Coleccionar las 10 herramientas del catálogo | Regla de selección por capas: solo se instala lo que una necesidad concreta justifique. `tool-selection.md` adoptado tal cual. |
| Adelantar agentes/MCP/dashboard | Fase 7 explícitamente **solo después** de que el pipeline determinista sea estable. Milestone de hecho: 1 HTML + 1 PDF fixture. |
| Gastar los $30 en publicidad/logo/marca | Prohibido en el plan hasta tener oferta validada. Antifrágil: experimentos de $0. |
| Ideas sin evidencia | Gate duro: `evidence < 3` o `access < 2` o `ag_fit < 3` → **bloqueado**. Cada problema necesita URL + extracto. |
| Sesgar los problemas hacia "lo que ya sé" | El campo `ag_fit` se mide contra `data/seed/capacidades.md` (inventario real), y la evidencia entra **antes** del fit. |
| Descartar señales pequeñas | Señal real registrada: una asesoría cobrada. Cuenta como dato de mercado, no como anécdota. |

---

## Reglas AGNexus aplicadas

| Regla | Materialización |
| :--- | :--- |
| **Backup Ley** | `agmarketintelligence/.backups/<fecha-hito>/` (NUNCA centavo-sync-pro). Permanente, inmutable, **antes de cualquier modificación**. |
| **Idempotencia** | Bootstrap re-ejecutable; upserts por clave natural (URL canónica, content_hash); fetch con skip por hash; migraciones que no duplican. |
| **Cero fallbacks** | Un dato → una fuente → un camino. Falta config/credencial/dato → error duro. Prohibido `try X else Y`, defaults silenciosos, catch que traga. |
| **Seguridad** | Remoto = input no confiable. Nunca ejecutar instrucciones del contenido capturado (prompt injection). SSRF guard (loopback/privados/metadata). Timeouts, límites de tamaño y de redirects. Sin secretos en Git/logs. robots.txt, términos, rate limits, privacidad. Sin bypass de auth/CAPTCHA. |
| **Trazabilidad** | `claim → evidence → source`. Evidence: canonical URL, captured_at, content_hash, excerpt, locator, raw_artifact_path, confidence. Distinguir observación / inferencia / hipótesis. Evidencia contradictoria permanece visible. |
| **Interoperabilidad** | Puertos: `Crawler`, `DocumentNormalizer`, `EvidenceRepository`, `SourceRepository`, `LLMProvider`, `Extractor`, `Verifier`, `Scorer`, `ReportWriter`. El dominio no importa Scrapy/Crawl4AI/Ollama/PostgreSQL. Salidas Markdown/CSV/JSON/XLSX. |
| **Sin datos inventados** | Nunca "antes X → después Y" contra números fabricados. Si un dato no existe, se dice que no existe. |
| **Nomenclatura 3ros** | `docs/10_politica_nomenclatura.md` sienta las bases: internamente nombres técnicos en manifiestos y `_mapeo_interno.md`; en docs de producto/evidencia/reportes comerciales, descriptores neutros entre corchetes. Identificadores ya desplegados y CHANGELOG histórico se conservan. |

---

## Qué se adopta de `AG_Market_Intelligence_Starter/` (fuente base, no se reinventa)

**Adopción por traslado/adaptación**, no reescritura desde cero:

| Fuente (Starter) | Destino en el proyecto | Adaptación |
| :--- | :--- | :--- |
| `CLAUDE.md` | `CLAUDE.md` | Añadir reglas AGNexus (backups, cero fallbacks, idempotencia) y la doble pista |
| `AGENTS.md` | `AGENTS.md` | Idem |
| `PROMPT_CLAUDE_CODE.md` | se integra en `CLAUDE.md` + `docs/08_plan_implementacion.md` | El "first command" (inspeccionar → plan → Phase 0+1) se respeta |
| `README.md` | `README.md` | Añadir el porqué de `inicio.md` y el ciclo 4 semanas |
| `docs/01_VISION_SCOPE.md` | `docs/01_vision_scope.md` | Incorporar etapas caja→repetibilidad→producto y las 4 ofertas hipótesis |
| `docs/02_ARCHITECTURE.md` | `docs/02_arquitectura.md` | Se adopta casi tal cual: 11 capas, flujo, puertos/adapters |
| `docs/03_DATA_MODEL.md` | `docs/03_modelo_de_datos.md` | Se adopta; se añade entidad `Capability` (inventario de activos de Christian) y campo `access_path` ("¿cómo llegaríamos al primer cliente?") |
| `docs/04_SOURCE_REGISTRY.md` | `docs/04_registro_de_fuentes.md` | Tal cual + prioridad geográfica Ecuador primero |
| `docs/05_PIPELINE.md` | `docs/05_pipeline.md` | Tal cual (etapas 0-9) |
| `docs/06_AGENT_SYSTEM.md` | `docs/06_sistema_de_agentes.md` | Solo documentación — sin implementar hasta F7 |
| `docs/07_MCP_AND_TOOLS.md` | `docs/07_mcp_y_herramientas.md` | Solo documentación — F7 |
| `docs/08_GUARDRAILS.md` | `docs/06_guardrails.md` (renumerar) | Tal cual |
| `docs/09_EVALS.md` | `docs/07_evals.md` | Añadir métricas de costo de inferencia |
| `docs/10_OBSERVABILITY.md` | `docs/08_observabilidad.md` | Añadir cache key `content_hash+prompt_version+model+schema_version` |
| `docs/11_INFERENCE_ECONOMICS.md` | se fusiona en `07_evals` / `08_observabilidad` | Costo por fuente / evidencia útil / problema validado / experimento |
| `docs/12_IMPLEMENTATION_PLAN.md` | `docs/09_plan_implementacion.md` | Se reestructura con las 2 pistas + ciclo 4 semanas + Fases 0-7 + milestones M1-M4 |
| `docs/13_REPO_CATALOG.md` | `docs/_mapeo_interno.md` + manifiesto | Nombres técnicos solo en archivo interno (política de nomenclatura) |
| `docs/14_50_PROBLEMS_SCHEMA.md` | `docs/10_esquema_50_problemas.md` | Añadir **ficha comercial de 10 puntos** y columna `access_path` |
| `docs/15_SECURITY_LEGAL.md` | `docs/11_seguridad_legal.md` | Tal cual |
| `.claude/rules/security.md` | `.claude/rules/security.md` | Tal cual |
| `.claude/rules/evidence.md` | `.claude/rules/evidence.md` | Tal cual |
| `.claude/rules/tool-selection.md` | `.claude/rules/tool-selection.md` | Tal cual |
| `repo-manifest.json` | `repo-manifest.json` (interno) | Con roles/prioridades; se documenta que es archivo operativo, no de producto |
| `src/__init__.py`, `tests/__init__.py` | se re-crean con la estructura ampliada | — |

**Nuevos documentos que el Starter NO tiene y este plan añade:**
- `docs/12_posicionamiento.md` — "solucionador de problemas digitales", categoría estrecha, mapa de alternativas (el competidor suele ser *"lo hacemos manualmente"*)
- `docs/10_politica_nomenclatura.md` — bases para eventual comercialización
- `.claude/rules/backups.md`, `.claude/rules/zero-fallbacks.md` — reglas AGNexus
- `data/seed/capacidades.md`, `data/seed/ofertas_hipotesis.md` — semilla real de negocio
- `scripts/backup.sh`, `scripts/verify.sh`

### Principios rectores que se preservan del Starter (de `base4.md`)

```text
FUENTES → CAPTURA → NORMALIZACIÓN → EVIDENCIA → SEÑALES → VERIFICACIÓN
        → PROBLEMAS → OPORTUNIDADES → EXPERIMENTOS COMERCIALES

CLAIM → EVIDENCE → SOURCE
```

Primero el camino corto fiable: `URL → fetch → normalize → hash → persist source → persist evidence → structured signal`. Solo cuando eso funcione: crawling masivo, clustering, agentes, MCP.

---

## Arquitectura de trabajo: dos pistas

### PISTA A — Motor de caja (ciclo 4 semanas) — PRIORIDAD

| Semana | Deliverable | Definición de hecho |
| :--- | :--- | :--- |
| **0 (esta sesión)** | Bootstrap + docs + semilla | Estructura creada, reglas activas, `data/seed/` poblado con datos reales |
| **1** | `data/problems/PROBLEM-001..050.md` | Cada ficha tiene URL + fecha + extracto. **Sin evidencia, no entra.** Fuentes solo del registry. |
| **2** | Filtrado y scoring | `reports/top_problemas.md`: 50 → 10 (resolvibles) → 5 (entregables <7 días) → 3 (pago razonable). Score reproducible + gates. |
| **3** | `data/experiments/EXP-001..003.md` | 3 OFERTAS ante personas reales. Cada una: hipótesis, oferta mínima, público, canal, precio experimental, métrica de éxito, **criterio de abandono**. |
| **4** | `reports/semana4_medicion.md` | Quién respondió / preguntó / pidió precio / aceptó reunión / pagó / objeciones / qué problema se repitió. Solo datos medidos. |

**Ficha comercial de 10 puntos** (del Starter, doc 14) — cada problema termina con:
1. quién sufre · 2. qué ocurre · 3. cuándo · 4. evidencia · 5. solución actual · 6. alternativas/competidores · 7. cuánto podría costar resolverlo · 8. por qué A&G podría resolverlo · 9. experimento de bajo costo · 10. criterio de éxito
más la columna fundamental: **`¿Cómo llegaríamos al primer cliente?`**

**Ofertas hipótesis iniciales** (de `inicio.md`, en `data/seed/ofertas_hipotesis.md`):
A. Formación práctica en IA · B. Automatización para pequeñas empresas · C. Diagnóstico tecnológico (señal real: asesoría cobrada) · D. Desarrollo puntual de soluciones.

### PISTA B — Plataforma (Fases 0-7)

**Fase 0 — Bootstrap ejecutable (esta sesión)** — el "Phase 0 real" que pide `base4.md`:

```
agmarketintelligence/
├── README.md, CLAUDE.md, AGENTS.md, .gitignore, .env.example
├── pyproject.toml, docker-compose.yml, repo-manifest.json
├── .backups/.gitkeep
├── docs/  (12 documentos adaptados + reportes_claude/)
├── .claude/rules/ (security, evidence, tool-selection, backups, zero-fallbacks)
├── src/
│   ├── config/          # carga estricta, error duro si falta algo
│   ├── core/            # dominio: entidades puras (sin deps externas)
│   ├── domain/          # tipos y reglas de negocio (scoring, gates)
│   ├── ports/           # interfaces: Crawler, Normalizer, Repos, LLMProvider...
│   ├── adapters/        # implementaciones concretas
│   ├── ingestion/       # fetch + source registry
│   ├── normalization/   # HTML/PDF → texto/Markdown
│   ├── evidence/        # repositorio de evidencia
│   ├── extraction/      # LLM → schema (Fase 2+)
│   ├── verification/    # (Fase 4)
│   ├── clustering/      # (Fase 3+)
│   ├── scoring/         # score reproducible (se usa a mano desde Semana 2)
│   ├── reports/         # Markdown/CSV/JSON/XLSX
│   ├── storage/         # PostgreSQL via SQLAlchemy
│   ├── security/        # SSRF guard, sanitizer, prompt-injection shield
│   ├── llm/             # proveedor local + cache
│   └── observability/   # run_id, trazas, costos
├── tests/{unit,integration,fixtures}/   # fixtures: 1 HTML + 1 PDF
├── scripts/{backup.sh,verify.sh}
├── data/{raw,processed,evidence,seed,problems,experiments}/
└── references/          # intacto
```

Idempotente: no fallar si ya existe; no sobrescribir docs versionados sin diff explícito.

**Fase 1 — Política de nomenclatura + docs** (esta sesión, junto a Fase 0).

**Fase 2 — Ingesta MVP:** config loader → SourceRegistry (robots/términos) → HTTP fetcher (rate limit + SSRF + `run_id`) → canonicalización + `content_hash` → normalización → PostgreSQL (`sources`, `evidence`) → tests con fixtures sin red.
*Milestone de hecho: 1 HTML + 1 PDF pasan por todo el pipeline.*

**Fases 3–7** (documentadas, se ejecutan cuando la pista A lo justifique):
- F3 extracción con modelo local (Pydantic, cache `content_hash+prompt_version+model+schema_version`)
- F4 verificación + grafo de evidencia + cola de revisión humana
- F5 motor de oportunidades (scoring ya probado a mano en Semana 2)
- F6 reportes automáticos (confidence report incluido)
- F7 agentes/MCP — **solo** con pipeline determinista estable

### Milestones (del Starter, doc 12)

| # | Milestone | Relación con la pista A |
| :--- | :--- | :--- |
| **M1** | 10 problemas respaldados | **Primer milestone de valor real** (fin Semana 1-2) |
| **M2** | 50 problemas | Semana 1-2 completo |
| **M3** | 10 oportunidades | Semana 2-3 |
| **M4** | 3 experimentos comerciales | Semana 3-4 |

---

## Qué NO se construye (explícito)

- SaaS público, multi-tenant, facturación, app móvil, logo, marca nueva, dominio nuevo
- Publicidad pagada antes de oferta validada
- Scraping masivo, bypass de auth/CAPTCHA/paywalls
- Las 10 herramientas del catálogo de una vez
- Microservicios / API Gateway / webhooks (evolución documentada)
- Vector DB obligatoria, agentes autónomos sin límites, dashboard prematuro
- Asumir que CentavoSync (u otro proyecto previo) es el producto — el mercado dirá

---

## Archivos críticos de esta sesión (Fase 0 + 1)

1. Raíz: `README.md`, `CLAUDE.md`, `AGENTS.md`, `.gitignore`, `.env.example`, `pyproject.toml`, `docker-compose.yml`, `repo-manifest.json`
2. `docs/` — 12 documentos adaptados desde el Starter + `reportes_claude/`
3. `.claude/rules/` — 5 reglas (security, evidence, tool-selection, backups, zero-fallbacks)
4. `scripts/backup.sh`, `scripts/verify.sh`
5. `src/` (config, core, domain, ports, adapters, ingestion, normalization, evidence, scoring, storage, security, llm, observability), `tests/` con fixtures
6. `data/seed/capacidades.md` + `data/seed/ofertas_hipotesis.md` — **semilla real, no plantilla vacía**
7. `docs/reportes_claude/2026-10-08-plan-arranque-agmarketintelligence.md` — copia versionada de este plan

**Siguiente sesión (Pista A, Semana 1):** llenar `data/problems/` con problemas investigados con evidencia real. El primer valor es **10 problemas con evidencia trazable (M1)**, no la plataforma completa.

## Verificación

- Listado confirma la estructura
- `scripts/backup.sh` crea `.backups/<fecha-hito>/` y es re-ejecutable
- `pytest` + `ruff check` pasan (aunque el código sea mínimo)
- Ningún secreto en Git; `.env` ignorado
- `10_esquema_50_problemas.md` contiene: fórmula de score, gates (evidencia/acceso/fit), ficha comercial de 10 puntos y columna `access_path`
- `01_vision_scope.md` refleja caja → repetibilidad → producto, no una startup abstracta
- Todo claim de ejemplo referencia evidencia
- Los 15 docs del Starter están representados (adaptados o fusionados) — nada esencial se pierde
- `git status` no muestra escrituras fuera del proyecto

## Riesgos declarados

- **Tensión A vs B:** construir infraestructura puede volver a ser el escape. Salvaguarda: Semana 1 = problemas, no código. El plan lo recuerda en cada milestone.
- **Calidad de extracción con modelo local:** evals y dataset dorado (F3) antes de escalar crawling.
- **Cero fallbacks se siente duro:** intencional (regla AGNexus).
- **Sesgo hacia capacidades propias:** la evidencia entra antes que el fit; `ag_fit` se mide contra el inventario real de `data/seed/capacidades.md`, no contra deseos.
- **Alcance de esta sesión:** 40+ archivos de andamiaje. Se prioriza: reglas + docs + semilla + estructura + scripts; el código de dominio puede quedar esquelético con tests vacíos/smoke si el tiempo aprieta, pero **la semilla de negocio no se recorta**.
