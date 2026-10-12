# AGNexus — Estrategia y estructura web (v2)

**Estado:** borrador para validar · **Fecha:** 10 de octubre de 2026
**Alcance:** reordena el proyecto en tres capas (Objetivo → Estructura → Diseño) y propone una estructura mejorada para agnexus.online.

> Convención: **[A CONFIRMAR]** marca una decisión o dato que debe validar el propietario. Nada de lo marcado así debe publicarse como hecho hasta confirmarlo.

---

## 1. Punto de partida

**Hoy en el sitio** (según lo construido en WordPress):
- Publicadas: Inicio, Servicios, Nosotros y Contacto, con el constructor de YOOtheme.
- Menú principal activo en escritorio y móvil.
- Texto de marca aprobado: "Tecnología que conecta".

**Pendiente:**
- Logo en la cabecera (zona de widgets "Logo").
- Pie de página (hoy vacío).
- Formulario de contacto (plugin).
- Página de privacidad.
- Limpieza del contenido de ejemplo (entrada "Hello world!", página de ejemplo, widgets por defecto).
- Medición (analítica) y SEO básico: **no verificado** si existen.

**Limitación:** el aspecto visual real no se pudo comprobar desde las herramientas de trabajo; las observaciones de diseño son estructurales hasta revisar capturas.

**Lectura del diagnóstico recibido:** la crítica es acertada en el orden. El sitio se construyó a partir del documento maestro y de los textos aprobados, pero **no se cerró formalmente** la capa de objetivo (público, posicionamiento, captación de leads, indicadores). Esa es la base de las otras dos capas.

---

## 2. Capa 1 — Objetivo

### 2.1 Qué necesidad cumple el sitio (hipótesis) [A CONFIRMAR]

1. Que un decisor entienda en pocos segundos **qué hace AGNexus y para quién**.
2. **Generar consultas calificadas** (leads), no solo visitas.
3. Dar **credibilidad verificable** sin testimonios, clientes ni cifras inventadas.
4. Servir de base de **exposición**: buscadores, LinkedIn, referencias y propuestas comerciales.

### 2.2 Público [A CONFIRMAR prioridad]

| Segmento | Situación típica | Servicio que resuelve |
|---|---|---|
| A. Negocios con tienda online y sistema de gestión | Catálogo e inventario desalineados, datos copiados a mano | Integraciones y APIs; e-commerce |
| B. Empresas e instituciones con procesos manuales o sistemas heredados | Tareas repetitivas, información dispersa | Automatización; consultoría |
| C. Equipos que quieren adoptar IA con criterio | No saben por dónde empezar ni qué conviene | IA aplicada; consultoría |

### 2.3 Posicionamiento: tres caminos [A CONFIRMAR]

- **A. Integrador de plataformas** (e-commerce + sistemas de gestión): el más fácil de demostrar con experiencia real.
- **B. Estudio de IA aplicada:** más atractivo pero más saturado y más difícil de sostener sin casos.
- **C. Marca paraguas** (todo a la vez): riesgo de mensaje difuso.

**Recomendación:** liderar con **A** y presentar la IA y la automatización como **capa que se añade donde aporta**, no como promesa central. Propuesta de frase: *"AGNexus conecta tus plataformas y automatiza tus procesos, con IA donde aporta."* [A CONFIRMAR]

### 2.4 Conversión (captación de leads)

- **CTA principal:** "Cuéntanos qué necesitas conectar o mejorar" → formulario.
- **CTA secundario:** conocer servicios y casos.
- **Oferta de entrada** (por ejemplo, un diagnóstico inicial): alcance, duración y si tiene costo son **decisión del propietario** [A CONFIRMAR]. No se publican precios.
- **Formulario calificador:** nombre, correo, teléfono (opcional), qué herramientas usa hoy, qué quiere lograr, plazo aproximado.
- **Tiempo de respuesta prometido:** solo uno que se pueda cumplir [A CONFIRMAR].

### 2.5 Indicadores sugeridos (sin metas inventadas)

| Indicador | Qué mide |
|---|---|
| Consultas recibidas por mes | Captación |
| Consultas calificadas / total | Calidad del mensaje |
| Páginas más vistas y origen del tráfico | Exposición |
| Tiempo hasta la primera respuesta | Servicio |

La línea base es cero; las metas se fijan con el propietario tras los primeros meses.

### 2.6 Medición [A CONFIRMAR si ya existe]
Analítica y Search Console. Si se instalan, hay que informar el uso de cookies y datos en la página de privacidad.

---

## 3. Capa 2 — Estructura

### 3.1 Mapa del sitio propuesto

```
Inicio                                   /
├── Servicios (hub)                      /servicios/
│   ├── Integraciones y APIs             /servicios/integraciones-apis/
│   ├── Automatización e IA aplicada     /servicios/automatizacion-ia/
│   ├── Desarrollo web y e-commerce      /servicios/desarrollo-web-ecommerce/
│   └── Consultoría y analítica          /servicios/consultoria-analitica/
├── Soluciones                           /soluciones/        (solo con contenido validado)
├── Casos                                /casos/             (anónimos, validados)
├── Nosotros                             /nosotros/
├── Recursos (artículos)                 /recursos/          (opcional)
├── Contacto                             /contacto/
└── Privacidad                           /privacidad/
```

### 3.2 Función de cada página

| Página | Objetivo | CTA | Prioridad | Contenido que se necesita del propietario |
|---|---|---|---|---|
| Inicio | Explicar qué hace AGNexus, para quién y qué hacer a continuación | Contacto | P0 | Confirmar posicionamiento |
| Servicios (hub) | Orientar y derivar a cada servicio | Cada servicio / Contacto | P0 | — (ya existe) |
| 4 páginas de servicio | Resolver una necesidad concreta; posicionar en buscadores | Contacto | P1 | Alcance real, ejemplos anónimos, preguntas frecuentes |
| Soluciones | Mostrar productos propios con su **estado real** | Contacto | P1 | Estado y alcance validados de cada producto |
| Casos | Dar credibilidad sin nombres | Contacto | P1 | 2 o 3 casos: problema → enfoque → resultado verificable |
| Nosotros | Humanizar y explicar el método | Contacto | P0 | Confirmar hechos de la biografía |
| Recursos | Exposición y utilidad (SEO) | Contacto | P2 | Decidir si habrá artículos y con qué frecuencia |
| Contacto | Captar el lead | Formulario | P0 | Formulario, privacidad, tiempo de respuesta |
| Privacidad | Cumplimiento y confianza | — | P0 | Datos recogidos y tratamiento (revisión legal) |

### 3.3 Inicio v2 (orden propuesto)

1. **Hero:** qué hacemos, para quién y un CTA, con un visual de marca.
2. **Base de credibilidad:** años de experiencia, tecnologías habituales y sectores (anónimos). Sin logos de clientes ni testimonios.
3. **Problemas** que se reconocen en el día a día.
4. **Servicios** con enlace a cada página.
5. **Cómo trabajamos** (alcance claro, entregas por etapas, supervisión humana).
6. **Casos destacados** (cuando existan).
7. **Soluciones** con estado visible (producto propio / en exploración).
8. **Quién está detrás.**
9. **Preguntas frecuentes** (5 o 6, respondidas por el propietario).
10. **Cierre con formulario corto.**

---

## 4. Capa 3 — Diseño

### 4.1 Principios de experiencia (UX)
- Un mensaje y un CTA claros por pantalla.
- Contenido escaneable: títulos descriptivos, párrafos cortos.
- Móvil primero (el menú móvil ya funciona).
- Accesibilidad: contrastes verificados (ver paleta).
- Rapidez: imágenes ligeras y pocas fuentes.

### 4.2 Manual de marca mínimo

**Logo**
- Versiones: horizontal con eslogan, horizontal sin eslogan, para fondo oscuro, isotipo (negro, blanco y color) e icono de aplicación.
- Cabecera: horizontal **sin eslogan**. El eslogan solo en tamaños grandes (portada, Nosotros).
- Tamaños mínimos recomendados: horizontal ≥ 150 px de ancho en pantalla; isotipo ≥ 32 px; versión con eslogan ≥ 500 px.
- No deformar, no añadir efectos, no poner el degradado en textos.

**Color** (contrastes calculados)

| Rol | Color | Uso | Contraste |
|---|---|---|---|
| Texto y títulos | `#010c21` | Texto principal | 19,5:1 sobre blanco |
| Texto secundario | `#475569` | Descripciones | 7,6:1 sobre blanco |
| Primario | `#0054d5` | Botones y enlaces | 6,5:1 sobre blanco |
| Primario (hover) | `#0d26a5` | Estado hover | 11,4:1 sobre blanco |
| Sección oscura | `#001a4d` | Hero y cierres | 16,7:1 con texto blanco |
| Acento | `#00aefa` | Solo sobre fondo oscuro | 6,7:1 sobre `#001a4d` |
| Fondo suave | `#f3f6fb` | Secciones alternas | 18:1 con el texto principal |

El cian **no** se usa como texto sobre fondo blanco (2,5:1). Los degradados quedan para el logo.

**Tipografía** [A CONFIRMAR]: Sora para títulos e Inter para texto (ambas de licencia libre).

**Iconografía:** SVG de línea, trazo 2,5 px, azul primario, 48 px. Un solo estilo en todo el sitio.

**Imágenes:** sin stock genérico. Preferir esquemas de conexión, capturas reales de soluciones con datos anonimizados y diagramas simples.

**Tono de voz:** claro, técnico sin jerga, honesto sobre el estado de cada solución.
- Sí: "Está en exploración y todavía no se ofrece como producto."
- No: "Solución líder con resultados garantizados."

**Componentes:** botón primario y secundario, tarjetas de servicio, secciones alternas claras y oscuras, etiquetas de estado.

### 4.3 Idea creativa (propuesta) [A CONFIRMAR]
- **Concepto:** *Nexus* es el punto donde los sistemas se conectan.
- **Motivo visual:** la cinta plegada del isotipo como hilo conductor y diagramas de nodos conectados.
- **Visual del hero:** un esquema "antes y después": sistemas aislados → sistemas conectados.
- **Línea de campaña posible:** *"Menos copiar y pegar, más claridad."*

---

## 5. Exposición y SEO básico

- Título y descripción únicos por página (ya hay borradores de descripción guardados como extracto en cada página).
- Ideas de búsqueda [sin datos de volumen]: automatización de procesos, integración de tienda online con sistema de gestión, desarrollo e-commerce en Ecuador, IA aplicada a empresas.
- Mapa del sitio y datos estructurados de organización: requieren un plugin de SEO [A CONFIRMAR].
- Presencia externa: perfil de LinkedIn enlazado al sitio y, si aplica, perfil de empresa en Google.

---

## 6. Plan por fases (con aprobaciones)

| Fase | Contenido | Aprobación |
|---|---|---|
| 0. Cierre técnico | Logo en cabecera, pie, formulario, privacidad, limpieza del contenido de ejemplo, analítica | Cada cambio de ajustes o plugins |
| 1. Estrategia | Validar objetivo, público y posicionamiento; reescribir Inicio v2 | Textos y orden |
| 2. Servicios y casos | Cuatro páginas de servicio y 2 o 3 casos anónimos | Casos y alcance |
| 3. Soluciones y recursos | Página de Soluciones tras validar estados; primeros artículos | Estado de cada producto |
| 4. Medición | Revisar indicadores y ajustar | Cambios derivados |

---

## 7. Decisiones pendientes del propietario

1. Público prioritario (A, B o C).
2. Posicionamiento (A recomendado) y frase central.
3. Oferta de entrada: sí o no, formato y si tiene costo.
4. Casos que se pueden contar (sector, enfoque, resultado verificable).
5. Estado comercial de Centavo Sync Pro y si lleva página propia.
6. Canal de contacto preferido y tiempo de respuesta que se puede cumplir.
7. Artículos: sí o no, y frecuencia.
8. Analítica y plugin de SEO.
9. Idioma: solo español al inicio o versión en inglés.
10. Tipografía (Sora + Inter).

---

## 8. Reglas de contenido

- No inventar clientes, certificaciones, testimonios, métricas, funcionalidades, precios ni resultados.
- No confundir proyectos realizados con productos disponibles comercialmente.
- Cada solución muestra su **estado real**.
- Los casos se publican de forma anónima salvo autorización expresa.
- Los datos personales (correo personal, teléfono antiguo, tarifas) no se publican.
