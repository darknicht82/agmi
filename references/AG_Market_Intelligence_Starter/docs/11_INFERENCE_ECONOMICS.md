# 11 — Economía de inferencia

## Orden de preferencia

1. Reglas deterministas.
2. Modelo local pequeño para clasificación/tagging.
3. Modelo local más capaz para síntesis.
4. Proveedor externo solo cuando aporte valor medible.

## Cache

Cachear por:

`content_hash + prompt_version + model + schema_version`

## No gastar tokens en

- HTML repetido
- contenido duplicado
- clasificación que puede resolverse con reglas
- reportes que no cambiaron

## Métricas

Costo por fuente, costo por evidencia útil, costo por problema validado y costo por experimento generado.
