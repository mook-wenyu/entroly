---
claim_id: 8ab2e21f-d697-463f-8016-3e9780db1153
entity: utilization
status: inferred
confidence: 0.75
sources:
  - entroly-core/src/utilization.rs:28
  - entroly-core/src/utilization.rs:43
  - entroly-core/src/utilization.rs:55
  - entroly-core/src/utilization.rs:73
  - entroly-core/src/utilization.rs:82
last_checked: 2026-04-14T04:12:29.687862+00:00
derived_from:
  - belief_compiler
  - sast
---

# Module: utilization

**Language:** rust
**Lines of code:** 237

## Types
- `pub struct FragmentUtilization` — Utilization score for a single injected fragment.
- `pub struct UtilizationReport` — Session-level utilization report.

## Functions
- `fn trigrams(text: &str) -> HashSet<Vec<String>>` — Extract word trigrams from text as a HashSet.
- `fn identifier_set(text: &str) -> HashSet<String>` — Extract identifiers from text as a HashSet.
- `fn score_utilization(
    fragments: &[&ContextFragment],
    response: &str,
) -> UtilizationReport` — Score how much of each injected fragment the LLM actually used in its response.  Call this after receiving the LLM response, passing in the fragments that were injected into the prompt context.

## Dependencies
- `crate::depgraph::extract_identifiers`
- `crate::fragment::ContextFragment`
- `serde::`
- `std::collections::HashSet`
