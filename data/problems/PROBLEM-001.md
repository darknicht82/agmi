# PROBLEM-001 — Descarga y conciliación manual de comprobantes y retenciones electrónicas SRI

## Metadatos

- **ID:** PROBLEM-001
- **Sector:** Comercio y Servicios Profesionales
- **Estado:** verified
- **Score:** 4.55 / 5.00
- **Evidencia principal:** `evi_20261010_computrabajo_sri`
- **Fuente:** `src_computrabajo_ec`
- **URL de evidencia:** `https://ec.computrabajo.com/ofertas-de-trabajo/oferta-de-trabajo-de-asistente-contable-con-manejo-de-sri-en-guayaquil`
- **Fecha de evidencia:** 2026-10-10

---

## Ficha de 10 Puntos

### 1. Quién lo sufre
Estudios contables independientes, contadores externos y pymes comerciales/distribuidoras en Ecuador (Quito, Guayaquil, Cuenca) que procesan más de 50 facturas y retenciones al mes.

### 2. Qué ocurre
Descarga manual comprobante por comprobante desde el portal SRI en Línea, extracción de archivos XML/ZIP, conversión a Excel y digitación manual de retenciones para cruzar con compras. Proceso tedioso, propenso a errores tipográficos y omisiones.

### 3. Cuándo ocurre
Diariamente en recepción de compras y con pico de alta presión entre los días 10 y 28 de cada mes (fechas límite de declaraciones tributarias según el noveno dígito del RUC).

### 4. Evidencia
- **ID Evidencia:** [evi_20261010_computrabajo_sri](file:///h:/Projects/agnexus/agmarketintelligence/data/evidence/evi_20261010_computrabajo_sri.json)
- **Cita textual:** *"Requerido: Asistente contable con experiencia en descarga diaria de comprobantes electrónicos del portal SRI en línea, digitación en hoja de cálculo y conciliación de retenciones emitidas y recibidas."*

### 5. Solución actual
Contratación de pasantes o asistentes dedicados 2 a 4 horas al día a descargar, copiar y pegar datos en hojas de cálculo de Excel.

### 6. Alternativas y competidores
- Contratar más personal administrativo o pasantes contables.
- Módulos caros de ERPs empresariales cerrados ($800–$2,500/año) que muchas microempresas no pueden pagar.
- Herramientas manuales o macros de Excel desactualizadas que fallan con cambios del SRI.

### 7. Cuánto cuesta el problema
- $300 a $500 mensuales en salario/horas hombre por empresa o despacho contable.
- Riesgo de multas tributarias e intereses por retenciones no cruzadas a tiempo.

### 8. Por qué A&G puede resolverlo
- Capacidad C-02 (Integraciones entre sistemas y APIs) y C-03 (Automatización de procesos operativos).
- Experiencia en normalización de XMLs, scripts deterministas y flujos automatizados con n8n/Python.
- Entrega de un MVP funcional en 3 a 7 días.

### 9. Experimento de bajo costo (Pista A)
- **Oferta mínima:** *"Script / Flujo local que descarga y consolida automáticamente todos tus XMLs del SRI en un Excel listo para tu conciliación en 1 clic"*.
- **Público:** 10 contadores independientes y estudios contables en Guayaquil/Quito.
- **Precio test:** $75 a $150 pago único de instalación y configuración inicial.
- **Criterio de abandono:** Si tras contactar a 15 contadores ninguno solicita demostración o pide precio, se descarta.

### 10. Criterio de éxito
Al menos 2 contadores pagan la configuración inicial y confirman ahorro de más del 80% de tiempo en el cierre semanal.

---

## Calificación de Dimensiones (1 a 5)

| Dimensión | Valor | Justificación |
| :--- | :---: | :--- |
| **pain** | 4 | Afecta tiempo directo de contabilidad y riesgo tributario. |
| **frequency** | 5 | Diario / semanal. |
| **urgency** | 5 | Declaraciones mensuales SRI con fechas límites no postergables. |
| **ag_fit** | 5 | Totalmente alineado con capacidades C-02 y C-03 (entregable solo en <7 días). |
| **access** | 4 | Canal claro: grupos de contadores en LinkedIn, cámaras y despachos locales. |
| **repeatability** | 5 | Misma estructura de XML para todas las empresas en Ecuador. |
| **evidence** | 4 | Oferta laboral activa contratando personal explícitamente para esta labor. |
| **investment** | 1 | $0 inversión adicional (código determinista propio / n8n local). |

**Ruta al primer cliente (`access_path`):**
Mensaje directo a 10 contadores en LinkedIn / WhatsApp en Guayaquil ofreciendo auditar su flujo de descarga del SRI en 15 minutos sin costo.
