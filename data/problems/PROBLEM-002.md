# PROBLEM-002 — Desincronización manual de pedidos y stock entre WhatsApp / Tienda y Bodega

## Metadatos

- **ID:** PROBLEM-002
- **Sector:** Comercio, Retail y Distribución
- **Estado:** verified
- **Score:** 4.15 / 5.00
- **Evidencia principal:** `evi_20261011_multitrabajos_stock`
- **Fuente:** `src_multitrabajos_ec`
- **URL de evidencia:** `https://www.multitrabajos.com/empleos/coordinador-de-pedidos-y-e-commerce-quito`
- **Fecha de evidencia:** 2026-10-11

---

## Ficha de 10 Puntos

### 1. Quién lo sufre
Comercios minoristas, distribuidoras de repuestos, ferreterías y tiendas de moda en Quito y Guayaquil que venden por WhatsApp y redes sociales además de su punto físico.

### 2. Qué ocurre
Los vendedores toman pedidos por WhatsApp o catálogo web, pero el inventario está en un sistema local de bodega o en hojas de cálculo desactualizadas. Se venden productos agotados, se retrasan despachos y se pierde tiempo confirmando disponibilidad por teléfono con bodega.

### 3. Cuándo ocurre
A lo largo de todo el día operativo con picos en promociones o fines de semana.

### 4. Evidencia
- **ID Evidencia:** [evi_20261011_multitrabajos_stock](file:///h:/Projects/agnexus/agmarketintelligence/data/evidence/evi_20261011_multitrabajos_stock.json)
- **Cita textual:** *"Buscamos coordinador de e-commerce y atención para confirmar pedidos por WhatsApp, actualizar inventario manualmente en bodega y coordinar despacho en Excel."*

### 5. Solución actual
Una persona dedicada exclusivamente a chatear con los clientes y llamar a bodega para preguntar *"¿queda stock del código X?"*, anotando los pedidos en un Excel compartido.

### 6. Alternativas y competidores
- "Seguir haciéndolo por teléfono y WhatsApp" (la alternativa más común).
- Contratar software integral ERP / omnicanal de alto costo mensual ($120–$300/mes) que requiere migración traumática.

### 7. Cuánto cuesta el problema
- Sueldo de $460/mes (SBU Ecuador) de una persona haciendo de puente humano.
- 5% a 15% de ventas canceladas por falta de stock no avisada a tiempo.

### 8. Por qué A&G puede resolverlo
- Capacidad C-04 (E-commerce y operación de tienda online), C-02 (Integraciones entre sistemas) y C-03 (Automatización).
- Sincronización ligera entre base de datos de inventario / Google Sheets y catálogo de WhatsApp Business o Web.

### 9. Experimento de bajo costo (Pista A)
- **Oferta mínima:** *"Conector de inventario automático: tu catálogo de WhatsApp y pedidos sincronizados con tu hoja de cálculo o sistema en 48 horas"*.
- **Público:** 10 comercializadoras o distribuidores con catálogo en WhatsApp en Quito.
- **Precio test:** $150 a $250 configuración.
- **Criterio de abandono:** Si 10 tiendas no perciben el costo de las ventas perdidas como crítico, pivotar.

### 10. Criterio de éxito
Al menos 1 comercio paga la integración y reduce a cero las ventas de productos agotados en su primer mes.

---

## Calificación de Dimensiones (1 a 5)

| Dimensión | Valor | Justificación |
| :--- | :---: | :--- |
| **pain** | 4 | Pérdida directa de ventas y fricción con clientes insatisfechos. |
| **frequency** | 5 | Ocurre con cada pedido entrante. |
| **urgency** | 4 | Freno inmediato al crecimiento de ventas online. |
| **ag_fit** | 5 | Capacidad C-04 y C-02 comprobadas en casos previos. |
| **access** | 3 | Requiere contactar al dueño del negocio o jefe de ventas. |
| **repeatability** | 4 | La lógica de sincronización de stock es estándar. |
| **evidence** | 4 | Oferta laboral activa con contratación fija para esta tarea manual. |
| **investment** | 1 | $0 inversión (desarrollo propio). |

**Ruta al primer cliente (`access_path`):**
Auditoría rápida como cliente incógnito en 10 tiendas de Instagram/WhatsApp en Quito: detectar si tardan en confirmar stock y ofrecerles la solución directa.
