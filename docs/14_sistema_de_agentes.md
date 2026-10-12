# 14 — Sistema de agentes

> **Documentación de diseño. Sin implementar hasta Fase 7.**
> Ver `docs/09_plan_implementacion.md`.

## Principio

No crear un único agente gigante. Usar agentes especializados con responsabilidades pequeñas.

## Agentes

| Agente | Responsabilidad | Límite |
| :--- | :--- | :--- |
| **Research** | encuentra y resume evidencia | no decide qué negocio construir |
| **Extraction** | convierte contenido en schema estructurado | schema estricto |
| **Verification** | comprueba que los claims estén soportados | evidencia obligatoria |
| **Problem Clustering** | agrupa problemas similares | no inventa problemas |
| **Competitor** | identifica alternativas existentes | incluye "lo hacemos manualmente" |
| **Opportunity** | calcula hipótesis comercial con datos disponibles | score por reglas, no por intuición |
| **Report** | produce informes legibles | sin afirmaciones no demostradas |

## Orquestador

Controla: estado · reintentos · límites · costos · permisos · trazabilidad · handoffs

> **No permitir que un agente ejecute crawling ilimitado por sí mismo.**

## Agentic loop

```text
PLAN → ACT → OBSERVE → REFLECT → MEMORY / FEEDBACK → NEXT ACTION
```

El ciclo termina cuando:

- se cumple el objetivo;
- se alcanza el presupuesto;
- no queda evidencia útil;
- se requiere intervención humana;
- se alcanza el máximo de iteraciones.

Cada loop tiene: max iterations · timeout · tool allowlist · audit log · stopping condition.

## Permisos

Un agente de investigación **no** tiene automáticamente permisos para:

- borrar datos
- enviar mensajes comerciales
- modificar infraestructura
- publicar contenido
- acceder a credenciales privadas

Ningún agente obtiene acceso de red o de escritura sin restricciones.
