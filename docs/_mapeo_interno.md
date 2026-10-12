# Mapeo interno — descriptores ↔ nombres técnicos

> **ARCHIVO OPERATIVO INTERNO.** No incluir en reportes comerciales ni packs de cliente.
> Es el único lugar donde se documenta la equivalencia entre descriptores neutros y nombres técnicos reales.
> Ver `docs/13_politica_nomenclatura.md`.

## Descriptores del sistema

| Descriptor | Nombre técnico real | Rol |
| :--- | :--- | :--- |
| `[HERRAMIENTA-CRAWL-VOLUMEN]` | Scrapy | crawling estructurado de alto volumen |
| `[HERRAMIENTA-CRAWL-JS]` | Crawl4AI | renderizado JS → Markdown |
| `[HERRAMIENTA-ADAPTATIVA]` | Scrapling | scraping adaptativo |
| `[HERRAMIENTA-NAVEGADOR-AGENTE]` | Browser Use | interacción real con navegador |
| `[CONVERSOR-DOCUMENTOS]` | MarkItDown | PDF/Office/imagen → Markdown |
| `[BD-PRINCIPAL]` | PostgreSQL | base relacional principal |
| `[MODELO-LOCAL]` | Ollama | runtime de inferencia local |
| `[CLIENTE-HTTP]` | httpx | HTTP simple |
| `[PLUGIN-BARATO]` | (extensión de e-commerce de bajo costo) | alternativa barata del mapa |

## Dependencias MVP (instaladas)

| Paquete | Uso |
| :--- | :--- |
| `pydantic` | schemas en límites del sistema |
| `httpx` | fetch HTTP |
| `sqlalchemy` + `psycopg` | persistencia |
| `python-dotenv` | carga de entorno |
| `pytest`, `ruff`, `mypy` | dev |

## Catálogo de repos (referencia, no todas se instalan)

Ver `repo-manifest.json` en la raíz. Prioridad core / optional / not MVP.

**Regla:** no instalar los diez. MVP solo. El resto cuando una necesidad concreta lo justifique.

## Identificadores ya desplegados / históricos (excepción de la política)

Los nombres técnicos que ya existen en sistemas en producción y el CHANGELOG histórico **se conservan** tal cual. Se reporta honestamente en lugar de ocultarlo.

- `repo-manifest.json` conserva nombres reales (archivo operativo).
- Las dependencias en `pyproject.toml` conservan nombres reales (operabilidad).
