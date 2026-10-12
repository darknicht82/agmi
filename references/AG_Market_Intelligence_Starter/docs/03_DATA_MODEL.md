# 03 — Modelo de datos

## Entidades principales

### Source

- id
- name
- url
- domain
- source_type
- jurisdiction
- access_policy
- crawl_frequency
- last_crawled_at
- active

### Evidence

- id
- source_id
- captured_at
- canonical_url
- content_hash
- evidence_type
- excerpt
- locator
- confidence
- raw_artifact_path

### Company

- id
- name
- domain
- sector
- country
- source_evidence_ids

### Signal

- id
- evidence_id
- signal_type
- text
- sector
- entities
- confidence

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
- evidence_ids
- company_ids
- signal_ids
- confidence
- status

### Opportunity

- id
- problem_id
- target_customer
- proposed_solution
- ag_capability
- time_to_first_delivery
- initial_cost
- repeatability
- accessibility
- competitive_intensity
- commercial_score

### Experiment

- id
- opportunity_id
- hypothesis
- offer
- channel
- target
- price_test
- success_metric
- threshold
- deadline
- result
- decision

## Regla de trazabilidad

Ningún `Problem` puede pasar a prioridad comercial sin referencias a `Evidence`.
