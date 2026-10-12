# 2026-10-09 — Decisión: skills externas de agente (watchlist, no instalación)

> Análisis interno de decisión. Nomenclatura: los nombres técnicos reales viven en
> `repo-manifest.json` (sección `skills_watchlist`) y en `docs/_mapeo_interno.md`.
> Este informe usa descriptores neutros donde habla de producto.

## Pregunta

¿Conviene sumar un catálogo de skills externas de agente al proyecto ahora?

## Respuesta corta

**El análisis sí aporta. La instalación, no — todavía.**

Queda registrado como **watchlist operativo** en `repo-manifest.json`. **Nada instalado.**

## Qué aporta la propuesta (se conserva)

1. La advertencia central es correcta y coincide con `.claude/rules/tool-selection.md`:
   no instalar por popularidad; integrar solo ante necesidad concreta.
2. La distinción es correcta: las skills **reducen trabajo**, no sustituyen
   validación comercial, datos fiables ni conversaciones con clientes.
3. La estructura Descubrir → Evaluar → Construir → Vender es compatible con
   Pista A/B y con las fases del plan.

## Por qué NO se instala ahora

| Motivo | Detalle |
| :--- | :--- |
| Cuello de botella real | Lo que falta es **evidencia citable de problemas ecuatorianos** (M1), no tooling. |
| Riesgo de perfil | Coleccionar capacidades antes de comprobar que alguien paga es el patrón que el plan existe para frenar. |
| Coste de oportunidad | Tiempo de instalación/revisión = tiempo que no va a `data/problems/`. |
| Presupuesto | Con oferta no validada, no se gasta en herramientas ni publicidad. |

## Riesgo de seguridad (el análisis lo subestima)

Una skill externa **no es un binario: es texto que reescribe cómo se comporta el agente**.
Instalarla equivale a seguir instrucciones incrustadas en contenido remoto, que es lo que
`.claude/rules/security.md` prohíbe.

Gate obligatorio antes de cualquier instalación (ya fijado en el manifiesto):

1. Leer el contenido completo de la skill.
2. Verificar permisos / acceso a red / pedidos de credenciales.
3. Verificar telemetría y licencia.
4. Comprobar servicios de pago ocultos.
5. Comprobar procedencia y actividad del repositorio original.

## Criterio de activación (norma fijada)

> Una skill entra cuando una **necesidad concreta del pipeline de Pista A**
> la justifica — no porque exista ni porque sea popular.

Orden de eventual activación:

1. **Investigación de tendencias** — candidato condicional, solo si produce URLs
   citables. Precaución: tendencias globales no son evidencia ecuatoriana
   (ver `docs/04_registro_de_fuentes.md`: *relación verificable con Ecuador*).
2. **Marketing / ofertas** — Semana 3 del ciclo (ofertas y experimentos).
3. **Disciplina de desarrollo** — valor bajo; `AGENTS.md` y la *definición de hecho*
   ya cubren spec → plan → implementar → test.
4. **UI/UX, identidad, presentaciones** — fuera de alcance hasta Fase 6+ u oferta validada.
5. **Enlaces no verificados** — bloqueados hasta localizar el repositorio original.

## Decisión tomada

- [x] Registrar catálogo como watchlist en `repo-manifest.json` → `skills_watchlist`
- [x] Fijar criterio de activación y gate de seguridad
- [ ] **No instalar nada** en esta etapa
- [ ] Re-evaluar la skill de investigación **al inicio de la investigación manual de M1**

## Relación con el objetivo rector

El sistema existe para responder: *¿qué problema puedo resolver hoy y que alguien
me pague antes de construir demasiado?* Ninguna skill resuelve eso por sí sola.
La evidencia sí. Por eso la prioridad sigue siendo `data/problems/` con
`claim → evidence → source`.
