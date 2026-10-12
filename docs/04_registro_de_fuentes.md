# 04 — Registro de fuentes

El sistema mantiene una lista **explícita** de fuentes. No hay crawling indiscriminado.

## Categorías iniciales

### A. Demanda laboral

Objetivo: detectar problemas por los que las empresas están pagando talento.

Áreas: desarrollo · automatización · IA · integración · ERP · CRM · datos · soporte · e-commerce · BI · QA

### B. Empresas

Sectores con alta operación manual: empresas ecuatorianas · e-commerce · distribuidores · turismo · servicios profesionales · manufactura · salud · educación.

### C. Problemas publicados

comunidades · publicaciones públicas · blogs · noticias · reseñas · páginas de soporte · documentación

### D. Competidores / alternativas

Registrar: nombre · URL · problema que resuelve · precio cuando sea público · segmento · funcionalidades · limitaciones observables.

**Regla de alternativas:** el competidor real suele ser *"así lo hacemos manualmente y hasta ahora funciona"*, no el otro software. Mapa de alternativas: software especializado · plugin barato · hoja de cálculo · empleado manual · combinación de herramientas.

### E. Documentos

PDFs públicos · informes · estudios · normativa pública · catálogos · documentos empresariales públicos

## Prioridad geográfica

1. **Ecuador** (Quito / Guayaquil / Cuenca)
2. Colombia
3. Perú
4. Latinoamérica
5. Internacional, solo como benchmark

## Regla

> La fuente no se considera "evidencia de mercado ecuatoriano" solo porque esté en español.
> **Debe existir una relación verificable con Ecuador.**

## Alcance de acceso permitido

- Información empresarial pública
- Ofertas laborales públicas
- Páginas comerciales públicas
- Precios públicamente publicados
- Documentación pública
- Noticias y publicaciones públicas
- Catálogos públicos

## No objetivo

credenciales · cookies privadas · tokens · bases filtradas · información tras autenticación sin autorización · datos personales innecesarios · bypass de controles de acceso

## Antes de crawlear un dominio

1. Confirmar que está en este registro.
2. Confirmar el alcance permitido.
3. Comprobar robots.txt y términos cuando aplique.
4. Aplicar rate limits.
5. Guardar procedencia.
