# 09 — Plan de implementación

## Dos pistas

| Pista | Qué | Prioridad |
| :--- | :--- | :--- |
| **A — Motor de caja** | Ciclo 4 semanas: 50 problemas → 10 → 5 → 3 ofertas → primer cobro | **Manda** |
| **B — Plataforma** | Infraestructura reproducible y auditable | Evolutivo |

**El deliverable de la Semana 1 son problemas, no código.**

---

## PISTA A — Ciclo comercial de 4 semanas

| Semana | Deliverable | Definición de hecho |
| :--- | :--- | :--- |
| **0** | Bootstrap + docs + semilla | Estructura creada, reglas activas, `data/seed/` poblado con datos reales |
| **1** | `data/problems/PROBLEM-###.md` | Cada ficha con URL + fecha + extracto. Sin evidencia, no entra. Fuentes solo del registry. |
| **2** | Filtrado y scoring | `reports/top_problemas.md`: 50 → 10 → 5 → 3. Score reproducible + gates. |
| **3** | `data/experiments/EXP-###.md` | 3 OFERTAS ante personas reales. Cada una con hipótesis, oferta mínima, público, canal, precio, métrica, **criterio de abandono**. |
| **4** | `reports/semana4_medicion.md` | Quién respondió / preguntó / pidió precio / aceptó reunión / pagó / objeciones / qué problema se repitió. Solo datos medidos. |

### Ficha comercial de 10 puntos (por problema)

1. quién sufre
2. qué ocurre
3. cuándo ocurre
4. evidencia
5. solución actual
6. alternativas / competidores
7. cuánto podría costar resolverlo
8. por qué A&G podría resolverlo
9. experimento de bajo costo
10. criterio de éxito

más la columna fundamental: **`¿Cómo llegaríamos al primer cliente?`** (`access_path`)

---

## PISTA B — Fases de plataforma

### Fase 0 — Bootstrap

Python 3.11+ · Docker Compose · [BD-PRINCIPAL] · Pydantic · pytest · Ruff · `.env.example` · estructura de puertos/adapters

### Fase 1 — Ingestion MVP

source registry · HTTP fetcher · raw storage · canonicalization · hashing · persistencia · [CONVERSOR-DOCUMENTOS] · [HERRAMIENTA-CRAWL-JS]

**Resultado:** `URL → documento normalizado → Source + Evidence`

### Fase 2 — Structured extraction

schemas Pydantic · proveedor de inferencia local · extraction agent · validación · confidence

**Resultado:** `Evidence → Signals / Problems / Companies`

### Fase 3 — Research

[HERRAMIENTA-CRAWL-VOLUMEN] · source queues · crawling programado · deduplicación · clustering

### Fase 4 — Verification

verifier · evidence graph · detección de contradicciones · cola de revisión humana

### Fase 5 — Opportunity engine

scoring · mapa de alternativas · hipótesis de oportunidad · plantillas de experimento

### Fase 6 — Reporting

Markdown · CSV/XLSX · dashboard local

### Fase 7 — Capa agente (opcional)

MCP y [HERRAMIENTA-NAVEGADOR-AGENTE] **únicamente después** de que el pipeline determinista funcione.

---

## Milestones

| # | Milestone | Relación pista A |
| :--- | :--- | :--- |
| **M1** | 10 problemas respaldados | **Primer milestone de valor real** |
| **M2** | 50 problemas | Semana 1-2 |
| **M3** | 10 oportunidades | Semana 2-3 |
| **M4** | 3 experimentos comerciales | Semana 3-4 |

**Primer milestone no es "scrapear Ecuador".** Es: obtener 10 problemas con evidencia trazable y reproducible.

---

## Proceso de desarrollo

Trabajar incrementalmente. **No construir todo el sistema en un solo pase.**

Por cada fase:

1. inspeccionar repositorio;
2. proponer cambio;
3. implementar;
4. testear;
5. documentar;
6. mostrar archivos cambiados;
7. declarar riesgos restantes.

Nunca reemplazar arquitectura en silencio. Nunca inventar dependencias. Nunca fabricar resultados de tests.
