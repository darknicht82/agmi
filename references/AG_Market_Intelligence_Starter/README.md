# A&G Market Intelligence

Sistema local-first y basado en evidencia para descubrir problemas reales del mercado ecuatoriano, convertirlos en oportunidades y validar ofertas comerciales.

## Objetivo inicial

1. Encontrar 50 problemas reales y documentados.
2. Reducirlos a 10 oportunidades con potencial comercial.
3. Diseñar 3 experimentos comerciales de bajo costo.
4. Conseguir evidencia de mercado antes de invertir en producto.

## Principio central

> Los datos sin contexto son ruido. La información sin análisis es archivo. El análisis convertido en decisión es ventaja.

Toda afirmación relevante debe poder recorrer esta cadena:

`claim -> evidence -> source`

## Arquitectura MVP

`Fuentes -> captura -> normalización -> deduplicación -> extracción -> verificación -> clustering -> scoring -> PostgreSQL -> reportes -> experimento comercial`

Local-first: PostgreSQL + Python + Pydantic + Ollama. Los modelos externos son opcionales y deben justificarse por valor.

## Fases

- Phase 0: bootstrap y contratos.
- Phase 1: ingestión, fuentes, evidencia y normalización.
- Phase 2: extracción estructurada con LLM local.
- Phase 3: investigación, crawling, deduplicación y clustering.
- Phase 4: verificación.
- Phase 5: oportunidades y scoring.
- Phase 6: reportes.
- Phase 7: agentes/MCP/browser automation solo cuando exista una necesidad demostrada.

## Primer hito

No construir un SaaS ni un dashboard complejo primero. El primer resultado útil es: **10 problemas respaldados por evidencia, con trazabilidad completa y al menos una hipótesis comercial por problema**.

## Repositorios de referencia

Ver `docs/13_REPO_CATALOG.md`.
