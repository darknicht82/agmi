# A&G Market Intelligence

Sistema local-first de inteligencia de mercado para investigar **problemas empresariales reales en Ecuador** y convertir evidencia pública en datos estructurados, hipótesis de negocio y experimentos comerciales.

## Por qué existe

> **"¿Qué problema puedo resolver con lo que ya sé hacer y conseguir que alguien me pague antes de construir demasiado?"**

No es una startup de scraping. Es un **proceso inteligente de reducción de incertidumbre**: sustituye la pregunta enorme *"¿qué hago con mi vida profesional?"* por una respuestable:

> *"¿Cuál de estos 50 problemas tiene evidencia suficiente para que yo haga un experimento?"*

**Estrategia guía:** sobrevivir → observar → aprender → probar → cobrar → repetir → construir.
**Tres etapas:** Caja → Repetibilidad → Producto.

Cada experimento debe poder fallar **sin hundir**. Antifrágil financieramente.

## Flujo central

```text
FUENTES → CAPTURA → NORMALIZACIÓN → EVIDENCIA → SEÑALES → VERIFICACIÓN
        → PROBLEMAS → OPORTUNIDADES → EXPERIMENTOS COMERCIALES
```

**Regla que gobierna todo:**

```text
CLAIM → EVIDENCE → SOURCE
```

Ninguna afirmación importante existe sin evidencia. El score **nunca** compensa ausencia de evidencia. Un número inventado **no** es línea base.

## Dos pistas

| Pista | Qué es | Prioridad |
| :--- | :--- | :--- |
| **A — Motor de caja** | 50 problemas con evidencia → 10 → 5 → 3 ofertas → primer cobro (ciclo 4 semanas) | **Manda** |
| **B — Plataforma** | Infraestructura reproducible y auditable que hace A escalable | Evolutivo |

El deliverable de la Semana 1 son **problemas**, no código.

## Milestones

| # | Milestone | Cuándo |
| :--- | :--- | :--- |
| **M1** | 10 problemas con evidencia trazable | Primer valor real |
| **M2** | 50 problemas | Semana 1-2 |
| **M3** | 10 oportunidades | Semana 2-3 |
| **M4** | 3 experimentos comerciales | Semana 3-4 |

## Principios

1. **Data First**: ningún insight sin evidencia.
2. **Cero humo**: separar hecho, inferencia e hipótesis.
3. **Evidence First**: URL, fecha, fuente y fragmento siempre conservados.
4. **Local First**: herramientas open source y modelos locales primero.
5. **Human in the Loop**: decisiones comerciales importantes no las toma el modelo solo.
6. **Legal by Design**: términos, robots.txt, límites, privacidad y derechos.
7. **Reproducible**: cada resultado se rastrea hasta su fuente.
8. **Small Bets**: validar demanda primero; construir después.
9. **Security by Default**: HTML, PDFs y páginas remotas son entradas no confiables.
10. **Cero fallbacks**: un solo camino de datos; error duro si falta algo.

## Cómo arrancar

```bash
cp .env.example .env          # completar valores obligatorios
docker compose up -d          # base de datos local
pip install -e ".[dev]"       # dependencias
bash scripts/verify.sh        # tests + lint
bash scripts/backup.sh        # Backup Ley antes de trabajar
```

## Estructura

- `docs/` — visión, arquitectura, modelo de datos, pipeline, reglas, plan
- `docs/reportes_claude/` — planes y análisis de Claude (con fecha)
- `.claude/rules/` — reglas del proyecto (seguridad, evidencia, backups, cero fallbacks)
- `data/seed/` — semilla real: capacidades e ofertas hipótesis
- `data/problems/` — fichas de problemas con evidencia
- `data/experiments/` — ofertas experimentales
- `src/` — código (puertos/adaptadores, dominio sin dependencias externas)
- `tests/` — unit + integration + fixtures
- `scripts/backup.sh`, `scripts/verify.sh`
- `references/` — material de origen (no se modifica)

## Fuera de alcance (explícito)

SaaS público, multi-tenant, facturación, app móvil, logo/marca nueva, publicidad antes de oferta validada, scraping masivo, bypass de auth/CAPTCHA, agentes autónomos sin límites, asumir que un proyecto previo es el producto.
