# 13 — Política de nomenclatura (bases para eventual comercialización)

## Contexto

Este sistema es de **uso interno** (AGNexus / AGDevelop / Christian Aguirre). No se descarta comercializarlo más adelante. Esta política **sienta las bases** de qué se nombra y qué no, para no tener que rehacer la documentación si el producto sale hacia afuera.

## Principio

> La documentación de producto **no menciona productos ni marcas ajenas**. Esos son base de trabajo, no algo que el lector necesite citar. Se sustituyen por **descriptores neutros entre corchetes**.

## Convención de descriptores

| Descriptor | Significado |
| :--- | :--- |
| `[HERRAMIENTA-CRAWL-VOLUMEN]` | motor de crawling estructurado de alto volumen |
| `[HERRAMIENTA-CRAWL-JS]` | crawler con renderizado JS y salida Markdown |
| `[HERRAMIENTA-ADAPTATIVA]` | scraper adaptativo a cambios de DOM |
| `[HERRAMIENTA-NAVEGADOR-AGENTE]` | agente que controla navegador real |
| `[CONVERSOR-DOCUMENTOS]` | convertidor de PDF/Office/imágenes a Markdown |
| `[MODELO-LOCAL]` | runtime de inferencia local |
| `[BD-PRINCIPAL]` | base de datos relacional principal |
| `[PLUGIN-BARATO]` | extensión económica de plataforma de e-commerce |
| `[PLATAFORMA-ORIGEN]` / `[MARCA-LEGADA]` | sistema del que se migró o referencia histórica |
| `[DOMINIO-ORIGEN]` / `[RUTA-ORIGEN]` | identificadores de origen |

La misma convención que `[MARCA-LEGADA]`: entre corchetes, mayúsculas, descriptor genérico.

## Dónde vive cada cosa

| Ámbito | Nombres permitidos |
| :--- | :--- |
| `pyproject.toml`, `docker-compose.yml`, `requirements` | nombres técnicos reales (operabilidad) |
| `repo-manifest.json` | nombres técnicos reales (**archivo operativo interno**) |
| `docs/_mapeo_interno.md` | tabla `[descriptor ↔ nombre real]` — **solo interno** |
| `docs/` de producto, visión, evidencia | **descriptores neutros** |
| Reportes comerciales / packs de cliente | **descriptores neutros** |
| Código / comentarios de código | descriptores; nombres reales solo en imports del gestor de paquetes |

## Excepciones duras (se conservan)

1. **Identificadores ya desplegados** — nombres técnicos que ya existen en sistemas en producción no se reescriben.
2. **CHANGELOG histórico** — la integridad histórica manda sobre la limpieza nominal.

En esos casos se **reporta honestamente** en lugar de ocultarlo.

## Por qué

- El producto puede entregarse a clientes. Nombrar marcas reales expone material ajeno y confunde al lector sobre de quién es el producto.
- Facilita la comercialización futura: la documentación ya nace limpia.

## Cómo se aplica

1. Al escribir docs, sustituir marca ajena por su descriptor.
2. Registrar la equivalencia en `docs/_mapeo_interno.md`.
3. Si algo ya está desplegado o es CHANGELOG, dejarlo y anotarlo.
4. No inventar nombres de marca propios ni logos hasta tener oferta validada (ver `docs/12_posicionamiento.md`).
