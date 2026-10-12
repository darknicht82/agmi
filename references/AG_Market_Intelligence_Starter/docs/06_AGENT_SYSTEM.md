# 06 — Sistema de agentes

## Agentes propuestos

- `ResearchAgent`: descubre fuentes y preguntas de investigación.
- `ExtractionAgent`: convierte evidencia en señales estructuradas.
- `VerificationAgent`: busca corroboración y contradicciones.
- `ClusteringAgent`: agrupa señales en problemas.
- `CompetitorAgent`: identifica soluciones existentes y sustitutos.
- `OpportunityAgent`: convierte problemas validados en oportunidades.
- `ReportAgent`: produce informes con trazabilidad.

## Orquestador

El orquestador controla:

- estado
- permisos
- límites
- retries
- timeouts
- presupuesto de tokens
- handoffs
- validación de schemas
- auditoría

## Loop

`Plan -> Act -> Observe -> Reflect -> Memory/Feedback`

La memoria debe almacenar hechos y resultados verificables, no opiniones del agente.

## Principio

Primero pipeline determinista. Después agentes. No usar un agente donde una función simple sea suficiente.
