# Semilla — Capacidades reales (inventario A&G)

> **Archivo operativo interno.** Es la base del campo `ag_fit` del score: se mide contra esto, no contra deseos.
> No es un currículum ni una lista de tecnologías. Es **qué se puede entregar como resultado**.
> Ver `docs/10_esquema_50_problemas.md` y `data/seed/ofertas_hipotesis.md`.
> Nomenclatura: descriptores neutros (ver `docs/13_politica_nomenclatura.md`). Nombres reales en `docs/_mapeo_interno.md`.

## Criterios de esta lista

Una capacidad entra solo si se puede responder:

1. **¿Se puede entregar solo?** (sin equipo ni capital adicional)
2. **¿En cuántos días se entrega?**
3. **¿Hay algún caso/resultado que lo respalde?**

---

## Capacidades

### C-01 — Desarrollo de soluciones a medida

- **Qué resuelve:** un proceso del negocio que ninguna herramienta estándar cubre bien.
- **Entregable:** sistema interno, integración, formulario avanzado, dashboard, herramienta interna.
- **Solo:** sí.
- **Tiempo de entrega:** 7–30 días según alcance.
- **Evidencia de capacidad:** múltiples sistemas e integraciones entregados a lo largo de la trayectoria.

### C-02 — Integraciones entre sistemas y APIs

- **Qué resuelve:** información atrapada en dos sistemas que no se hablan; copiar y pegar manual.
- **Entregable:** flujo de datos automatizado, sincronización, puente entre plataformas.
- **Solo:** sí.
- **Tiempo:** 7–21 días.
- **Evidencia:** caso de marketplace de vehículos — conectar selección de vehículo con valoración y propuesta contextual de seguro (flujo *vehículo → valoración → contexto del comprador → seguro → conversión*). Histórico/desplegado: conserva su identificador.

### C-03 — Automatización de procesos operativos

- **Qué resuelve:** tareas repetitivas de copiar información entre [MENSAJERÍA], [CORREO], hojas de cálculo y sistemas.
- **Entregable:** automatización + capacitación para que el negocio la sostenga.
- **Solo:** sí.
- **Tiempo:** 3–14 días.
- **Evidencia:** experiencia en orquestación de flujos y automatización con herramientas de workflow.

### C-04 — E-commerce y operación de tienda online

- **Qué resuelve:** ventas online con inventario, facturación y operación desalineados.
- **Entregable:** configuración, integración, automatización de operación de tienda.
- **Solo:** sí.
- **Tiempo:** 7–30 días.
- **Evidencia:** proyecto de sincronización entre plataforma de e-commerce, inventario y sistema contable.

### C-05 — Formación práctica (Formador de Formadores)

- **Qué resuelve:** equipos que necesitan usar tecnología/IA en su trabajo real, no teoría.
- **Entregable:** taller individual, taller 3–5 personas, capacitación empresarial, acompañamiento.
- **Solo:** sí.
- **Tiempo:** 1–7 días de preparación; entrega en sesión.
- **Evidencia:** formación de formadores; trayectoria combinando práctica técnica con enseñanza.

### C-06 — Diagnóstico tecnológico

- **Qué resuelve:** negocios que no saben qué tienen, qué les falta ni qué les está costando dinero.
- **Entregable:** informe breve — *problema → riesgo → recomendación → prioridad → costo estimado*.
- **Solo:** sí.
- **Tiempo:** 1–5 días.
- **Evidencia de mercado (señal real):** **una asesoría informática ya cobrada** a un cliente comercial. No es una anécdota: es un dato de que alguien pagó por este conocimiento.

### C-07 — Aplicación de IA a procesos reales

- **Qué resuelve:** procesamiento de información, reportes, atención, contenido, análisis.
- **Entregable:** flujo con IA integrado a un proceso concreto del negocio.
- **Solo:** sí.
- **Tiempo:** 3–21 días.
- **Evidencia:** experiencia práctica con IA aplicada a automatización, programación y flujos de trabajo.

### C-08 — Consultoría y criterio de sistemas

- **Qué resuelve:** decisiones tecnológicas tomadas sin entender el problema del negocio.
- **Entregable:** recomendación accionable, no consultoría interminable.
- **Solo:** sí.
- **Tiempo:** 1–5 días.
- **Evidencia:** experiencia transversal en sistemas empresariales, comercio, servicios y soporte.

---

## Contexto empresarial acumulado (activo, no lista de tech)

Sectores y funciones vistas en la práctica: comercio · turismo · banca · servicios · sistemas internos · pagos · marketing · ventas · soporte · usuarios · procesos · errores · infraestructura · datos.

**Propuesta de entrada derivada:**

> *"No empiezo preguntándote qué tecnología quieres. Empiezo entendiendo qué problema tienes y después te digo qué tecnología tiene sentido."*

---

## Criterio de filtrado de oportunidades

Las capacidades **no** determinan qué problema merece entrar. El orden es:

1. **Evidencia** (hay que demostrar que el problema existe)
2. **Acceso** (hay que poder llegar al primero)
3. **`ag_fit`** (recién aquí se mide contra este inventario)

Gate: `ag_fit < 3` → bloqueado para oportunidad prioritaria.

---

## Señales de mercado ya registradas

| Señal | Tipo | Peso |
| :--- | :--- | :--- |
| Una asesoría informática cobrada a un cliente comercial | pago real por conocimiento | Alto — prueba de que se puede cobrar |
| Participación en solución de marketplace de vehículos con propuesta contextual de seguro | integración tecnológica + oportunidad comercial | Alto — demostración de conectar tecnología con conversión |
| Proyecto de sincronización e-commerce / inventario / contabilidad | problema empresarial concreto identificado | Medio — hipótesis de producto a validar |

Estas señales **no** son conclusiones: son el punto de partida de la investigación de los 50 problemas.
