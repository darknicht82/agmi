# 15 — MCP y herramientas

> **Documentación de diseño. Sin implementar hasta Fase 7.**
> Ver `docs/09_plan_implementacion.md`.

## Objetivo

MCP sirve como **capa de herramientas**, no como sustituto de la arquitectura.

## Tools propuestas

```text
source.search        source.fetch        source.crawl        source.get
evidence.store       evidence.search
company.upsert       problem.upsert      problem.search
competitor.search
score.calculate
report.generate
```

## Herramientas externas (cuando sea necesario)

navegador · repositorio de código · archivos · base de datos · web crawler · sistema de reportes

## Permisos

Cada tool declara:

- read / write
- network access
- domains allowed
- rate limit
- data classification

## Regla

Un agente de investigación **no** debe tener automáticamente permisos para:

- borrar datos
- enviar mensajes comerciales
- modificar infraestructura
- publicar contenido
- acceder a credenciales privadas

## Orden de incorporación

1. Pipeline determinista (Fases 1–2)
2. Verificación (Fase 4)
3. Scoring y reportes (Fases 5–6)
4. **Recién entonces** capa agente/MCP (Fase 7)

Nada de esto sustituye `claim → evidence → source`.
