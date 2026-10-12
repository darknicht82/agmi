# 11 — Seguridad, privacidad y uso responsable

Este proyecto investiga **información pública**. No es un sistema para recolectar indiscriminadamente datos personales.

## Permitido como objetivo

- información empresarial pública
- ofertas laborales públicas
- páginas comerciales públicas
- precios públicamente publicados
- documentación pública
- noticias
- publicaciones públicas
- catálogos públicos

## No objetivo

- credenciales
- cookies privadas
- tokens
- bases filtradas
- información detrás de autenticación sin autorización
- datos personales innecesarios
- bypass de controles de acceso

## Retención

Guardar la **mínima información** necesaria para:

1. verificar la evidencia;
2. reproducir el análisis;
3. mantener trazabilidad.

## Revisión humana

Antes de utilizar una conclusión externamente:

1. revisar evidencia;
2. revisar licencia/condiciones;
3. revisar privacidad;
4. revisar lenguaje;
5. eliminar afirmaciones no demostradas.

## Amenazas técnicas (defensas activas)

| Amenaza | Defensa |
| :--- | :--- |
| Prompt injection | contenido remoto = datos, nunca instrucciones |
| SSRF | bloquear loopback / privados / metadata; validar URL antes de fetch |
| Documentos maliciosos | sandbox de normalización, sin ejecución |
| Redirects inseguros | límite de redirects + validación en cada hop |
| Payloads excesivos | límite de tamaño de respuesta |
| Decompression bombs | límite de expansión |
| Profundidad de crawl excesiva | límite de profundidad |
| Loops de agentes | max iterations + timeout + stopping condition |

**No bypass de autenticación, CAPTCHA, paywalls ni restricciones técnicas.**

## Evidencia y lenguaje

- Distinguir hecho / inferencia / hipótesis
- No publicar conclusiones acusatorias automáticas sobre empresas o personas
- La evidencia contradictoria permanece visible
