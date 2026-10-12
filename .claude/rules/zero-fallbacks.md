# Cero fallbacks (regla absoluta AGNexus)

Un solo camino de datos en cada capa. Si falta el dato o la credencial, se lanza un **error duro y visible**.

## Prohibido

- `try X else Y` en rutas de datos
- columnas espejo / "por si acaso"
- `catch {}` que traga y sigue
- defaults silenciosos cuando falta un parámetro obligatorio
- alias persistidos que se resuelven en runtime
- "legacy fallback"

## Diseñar siempre

`un dato → una fuente → un camino de lectura`

Si no está o no es válido → `throw` con mensaje claro que diga **qué falta y cómo arreglarlo**.

Un parámetro obligatorio es obligatorio. Ejemplo: si el API pide `credentialId` o `accessToken`, exigir exactamente uno y devolver error si faltan ambos. Nunca "si no viene, uso el que había".

Migraciones: mover TODO o fallar con el id de la fila problemática. Nunca dejar filas a medias.

Ver también: `backups.md`, `evidence.md`, `security.md`.
