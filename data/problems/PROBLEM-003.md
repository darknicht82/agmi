# PROBLEM-003 — Negocios locales operando sin respaldos automáticos ni diagnóstico de seguridad básica

## Metadatos

- **ID:** PROBLEM-003
- **Sector:** Servicios Locales, Salud y Talleres
- **Estado:** verified
- **Score:** 4.35 / 5.00
- **Evidencia principal:** `evi_20261008_ekos_backup`
- **Fuente:** `src_ekos_negocios`
- **URL de evidencia:** `https://ekosnegocios.com/articulo/riesgos-digitales-y-seguridad-en-las-pymes-del-ecuador`
- **Fecha de evidencia:** 2026-10-08

---

## Ficha de 10 Puntos

### 1. Quién lo sufre
Consultorios médicos y dentales, farmacias independientes, ópticas, talleres automotrices y despachos jurídicos en ciudades ecuatorianas con 1 a 5 computadoras de trabajo.

### 2. Qué ocurre
Toda la operación del negocio (historial de clientes, deudas por cobrar, facturación y registros contables) reside en una sola computadora de escritorio con discos duros viejos, sin antivirus gestionado, sin copias de seguridad automáticas ni cifrado. Si la máquina se daña o sufre un malware, el negocio pierde toda su historia operativa.

### 3. Cuándo ocurre
El riesgo existe las 24 horas; el impacto ocurre sin aviso ante un fallo eléctrico, daño mecánico de disco o ataque de phishing.

### 4. Evidencia
- **ID Evidencia:** [evi_20261008_ekos_backup](file:///h:/Projects/agnexus/agmarketintelligence/data/evidence/evi_20261008_ekos_backup.json)
- **Cita textual:** *"Más del 70% de micro y pequeñas empresas en el país mantienen sus registros contables y de clientes en computadoras personales sin respaldos externos automáticos ni esquemas de contingencia."*
- **Señal de mercado previa:** Una asesoría informática y diagnóstico de este tipo **ya fue cobrada a un cliente comercial real** (ver [data/seed/capacidades.md](file:///h:/Projects/agnexus/agmarketintelligence/data/seed/capacidades.md)).

### 5. Solución actual
Copiar carpetas de vez en cuando a una memoria USB (cuando se acuerdan) o ninguna acción por desconocimiento técnico.

### 6. Alternativas y competidores
- Contratar empresas de TI corporativas con pólizas mensuales caras ($300–$800/mes) sobredimensionadas para un consultorio.
- Soporte informal del "técnico del barrio" que formatea sin verificar integridad de datos.

### 7. Cuánto cuesta el problema
- Pérdida de $1,000 a $10,000 en cobranzas no documentadas, historias clínicas y reconstrucción contable.
- Parálisis del negocio durante días o semanas.

### 8. Por qué A&G puede resolverlo
- Capacidad C-06 (Diagnóstico tecnológico) y C-08 (Consultoría y criterio de sistemas).
- Entrega rápida (1 a 3 días) de un diagnóstico claro: *problema → riesgo → recomendación → prioridad → costo estimado*.
- Instalación de un esquema simple de backup inmutable 3-2-1 local + nube cifrada.

### 9. Experimento de bajo costo (Pista A)
- **Oferta mínima:** *"Chequeo Tecnológico Express (1 día): auditamos tu computadora principal, tus respaldos y tu red. Te entregamos un informe de 2 páginas con tus vulnerabilidades críticas y te dejamos configurado el respaldo automático"*.
- **Público:** 10 consultorios y talleres en el sector local.
- **Precio test:** $60 a $120.
- **Criterio de abandono:** Si 10 profesionales locales no muestran preocupación tras ver el informe de riesgo de pérdida de datos.

### 10. Criterio de éxito
Al menos 2 profesionales contratan el diagnóstico inicial y el esquema de respaldo en menos de 10 días.

---

## Calificación de Dimensiones (1 a 5)

| Dimensión | Valor | Justificación |
| :--- | :---: | :--- |
| **pain** | 5 | Pérdida total de datos irrecuperable. |
| **frequency** | 2 | Evento catastrófico poco frecuente, pero riesgo constante. |
| **urgency** | 4 | La tranquilidad del dueño es alta una vez que es consciente del riesgo. |
| **ag_fit** | 5 | Capacidad C-06 con cobro real comprobado anteriormente. |
| **access** | 5 | Acceso físico directo e inmediato a locales comerciales y consultorios. |
| **repeatability** | 4 | Lista de verificación de diagnóstico altamente estandarizable. |
| **evidence** | 4 | Estudio estadístico nacional de Ekos y señal comercial interna previa. |
| **investment** | 1 | $0 inversión (conocimiento y scripts existentes). |

**Ruta al primer cliente (`access_path`):**
Visita presencial o llamada directa a 5 consultorios o negocios locales conocidos ofreciendo la revisión preventiva rápida.
