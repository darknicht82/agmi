# 08 — Guardrails

## Contenido remoto = datos no confiables

Todo contenido scrapeado puede contener instrucciones maliciosas. Nunca debe modificar el comportamiento del agente por sí mismo.

## Prompt injection

Detectar patrones de instrucciones dentro de contenido y mantener separación entre `data` e `instructions`.

## SSRF

Bloquear por defecto:

- localhost
- loopback
- RFC1918/private networks
- metadata endpoints
- puertos administrativos
- esquemas no permitidos

## Secretos

Nunca almacenar API keys, tokens o credenciales en prompts, Markdown, logs o Git.

## Crawling

Respetar robots.txt cuando aplique, términos de servicio, límites de frecuencia, privacidad y controles de acceso. Nunca intentar bypass.

## Documentos maliciosos

Sanitizar entradas y limitar tamaño, profundidad, número de páginas y tiempo de procesamiento.

## Agent loops

Todos los agentes deben tener límites de pasos, tiempo, presupuesto y reintentos.
