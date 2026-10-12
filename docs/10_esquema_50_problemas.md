# 10 — Esquema para los 50 problemas

## Estructura de ficha (`data/problems/PROBLEM-###.md`)

| Campo | Qué buscar |
| :--- | :--- |
| Sector | Comercio, servicios, turismo, salud, educación, etc. |
| Problema | Qué está ocurriendo |
| **Evidencia** | URL + fecha + extracto (obligatorio) |
| Quién lo sufre | Tipo de empresa/persona |
| Cómo lo resuelven hoy | Manual / hoja de cálculo / software / empleado / nada |
| Alternativas existentes | Mapa de alternativas (incluye "lo hacemos manualmente") |
| Costo del problema | Tiempo, dinero, errores, ventas |
| Frecuencia | Ocasional / frecuente / diario |
| Urgencia | Baja / media / alta |
| Solución posible | Qué podríamos hacer |
| **¿Lo puedes entregar hoy?** | Sí / parcialmente / no |
| Inversión inicial | $0 / baja / media |
| Potencial de repetición | Bajo / medio / alto |
| Potencial de producto | Bajo / medio / alto |
| **`access_path`** | **¿Cómo llegaríamos al primer cliente?** |

## Dimensiones 1–5

- **pain / dolor** — 1 = cosmético · 5 = afecta dinero, operaciones o cumplimiento
- **frequency** — 1 = excepcional · 5 = diario/recurrente
- **urgency** — 1 = puede esperar · 5 = necesita resolución pronto
- **ag_fit** — 1 = requiere capacidades inexistentes · 5 = resoluble con capacidades actuales (medido contra `data/seed/capacidades.md`)
- **access** — 1 = difícil llegar al comprador · 5 = canal claro para primer cliente
- **repeatability** — 1 = caso único · 5 = paquete/producto repetible
- **evidence** — 1 = señal débil · 5 = múltiples fuentes independientes
- **investment** — 1 = prácticamente $0 · 5 = inversión alta — *se usa como filtro, invertir el sentido al calcular score*

## Score inicial

```text
score =
  pain * 0.20 +
  frequency * 0.10 +
  urgency * 0.10 +
  ag_fit * 0.20 +
  access * 0.15 +
  repeatability * 0.15 +
  evidence * 0.10
```

La inversión se utiliza como **filtro**, no como sustituto de demanda.

## Gates (reglas de promoción)

Un problema **no** puede convertirse en oportunidad prioritaria si:

- `evidence < 3`
- `access < 2`
- `ag_fit < 3`

> **El score nunca compensa ausencia de evidencia.**

## Ficha comercial de 10 puntos

Cada problema debe terminar con:

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

## Variables del embudo (de `inicio.md`)

`demanda observada × dolor × capacidad nuestra × velocidad de entrega × inversión requerida × posibilidad de repetición × acceso al cliente`

Esto elimina ideas que suenan bonitas pero son malas oportunidades.

## Regla anti-humo

No decir *"se encontraron 437 problemas"*. Cada problema conserva evidencia original con URL, fecha y fuente.
