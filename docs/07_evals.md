# 07 — Evaluaciones (evals)

El sistema necesita **medir calidad antes de escalar**.

## Dataset dorado

Crear manualmente 50–100 ejemplos:

- páginas con problemas reales
- páginas irrelevantes
- duplicados
- contenido ambiguo
- publicidad disfrazada de evidencia
- contenido con intento de prompt injection

## Métricas

### Extracción

- schema validity
- field completeness
- factual support

### Retrieval

- precision@k
- recall@k
- duplicate rate

### Clasificación

- sector accuracy
- problem clustering agreement
- confidence calibration

### Inteligencia comercial

- evidence-backed problem rate
- false opportunity rate
- human acceptance rate

## Economía de inferencia

### Orden de preferencia

1. Reglas deterministas (no usar modelo si una regla basta).
2. Modelo local pequeño para clasificación/tagging.
3. Modelo local más capaz para síntesis.
4. Proveedor externo solo cuando aporte valor medible.

### Cache

Clave: `content_hash + prompt_version + model + schema_version`

### No gastar tokens en

- HTML repetido
- contenido duplicado
- clasificación resoluble con reglas
- reportes que no cambiaron

### Métricas de costo

- costo por fuente
- costo por evidencia útil
- costo por problema validado
- costo por experimento generado

## Regla de calidad

> Una oportunidad con score alto pero evidencia baja **queda bloqueada** para decisión comercial.

## Golden rule

> **El score nunca puede compensar la ausencia de evidencia.**
