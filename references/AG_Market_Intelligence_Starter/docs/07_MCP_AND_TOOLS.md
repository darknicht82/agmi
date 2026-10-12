# 07 — MCP y herramientas

MCP se incorpora después de estabilizar los contratos internos.

## Herramientas conceptuales

- `source.search`
- `source.fetch`
- `source.crawl`
- `source.get`
- `evidence.store`
- `evidence.search`
- `company.upsert`
- `problem.upsert`
- `problem.search`
- `competitor.search`
- `score.calculate`
- `report.generate`

## Cada herramienta debe declarar

- read/write
- acceso a red
- dominios permitidos
- límites
- datos sensibles que puede tocar
- timeout
- formato de entrada/salida

## Seguridad MCP

Una herramienta que puede escribir o acceder a red no debe quedar disponible a cualquier agente por defecto. Aplicar mínimo privilegio.
