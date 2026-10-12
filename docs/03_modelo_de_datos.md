# 03 — Modelo de datos

## Entidades principales

### Source

- id
- name
- url
- canonical_url
- domain
- source_type
- country
- jurisdiction
- access_policy
- crawl_frequency
- first_seen_at
- last_crawled_at
- access_status
- robots_status
- terms_review_status
- content_hash
- active

### Evidence

- id
- source_id
- captured_at
- canonical_url
- title
- published_at
- author
- content_hash
- excerpt
- locator
- evidence_type
- confidence
- raw_artifact_path

**Evidence es la unidad mínima auditable.**

### Company

- id
- name
- domain
- sector
- country
- city
- size_estimate
- source_evidence_ids

### Signal

- id
- evidence_id
- type
- text
- description
- value
- sector
- entities
- confidence

Tipos iniciales: `hiring`, `manual_process`, `software_used`, `complaint`, `repeated_need`, `cost`, `growth`, `compliance`, `integration`, `data_problem`, `operational_bottleneck`.

### Problem

- id
- title
- description
- sector
- affected_actor
- trigger
- frequency
- urgency
- impact
- current_solution
- alternatives
- **access_path** — ¿cómo llegaríamos al primer cliente?
- evidence_ids
- company_ids
- signal_ids
- confidence
- status

### Capability

Inventario real de capacidades (base del campo `ag_fit`). Ver `data/seed/capacidades.md`.

- id
- name
- description
- deliverable_alone (bool)
- time_to_deliver_days
- proof_refs (casos/evidencia de que se puede entregar)

### Opportunity

- id
- problem_id
- target_customer
- proposed_solution
- ag_capability
- time_to_first_delivery
- estimated_initial_cost
- repeatability
- accessibility
- competitive_intensity
- commercial_score
- status

### Experiment

- id
- opportunity_id
- hypothesis
- offer
- channel
- target
- price_test
- success_metric
- success_threshold
- deadline
- **abandonment_criteria**
- result
- decision

## Regla de trazabilidad

Ningún `Problem` puede pasar a prioridad comercial sin referencias a `Evidence`.

```text
claim → evidence → source
```

Nunca guardar una afirmación importante únicamente como texto generado por un modelo.

## Tipos de claim

| Tipo | Qué es | Regla |
| :--- | :--- | :--- |
| `fact` | observación directa con evidencia | requiere evidencia |
| `inference` | derivación razonada | se marca como tal |
| `hypothesis` | supuesto por validar | **nunca** se promueve a fact |
