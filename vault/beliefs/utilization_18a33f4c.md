---
claim_id: 18a33f4c11c691cc03b81dcc
entity: utilization
status: inferred
confidence: 0.75
sources:
  - utilization.rs:28
  - utilization.rs:43
  - utilization.rs:55
  - utilization.rs:73
  - utilization.rs:82
  - utilization.rs:167
  - utilization.rs:172
  - utilization.rs:189
  - utilization.rs:202
  - utilization.rs:217
last_checked: 2026-04-04T19:51:14Z
derived_from:
  - cogops_compiler
  - sast
  - fragment_18a33f4c
  - depgraph_18a33f4c
epistemic_layer: truth
---

# Module: utilization

**Language:** rs
**Lines of code:** 236

## Types
- `pub struct FragmentUtilization` — Utilization score for a single injected fragment.
- `pub struct UtilizationReport` — Session-level utilization report.

## Functions
- `fn trigrams(text: &str) -> HashSet<Vec<String>>` — Extract word trigrams from text as a HashSet.
- `fn identifier_set(text: &str) -> HashSet<String>` — Extract identifiers from text as a HashSet.
- `pub fn score_utilization(` — Score how much of each injected fragment the LLM actually used in its response.  Call this after receiving the LLM response, passing in the fragments that were injected into the prompt context.
- `fn make_frag(id: &str, content: &str) -> ContextFragment`
- `fn test_full_utilization()`
- `fn test_zero_utilization()`
- `fn test_partial_utilization()`
- `fn test_empty_fragments()`
- `fn test_identifier_overlap_weighted_higher()`

## Related Modules

- **Depends on:** [[depgraph_18a33f4c]], [[fragment_18a33f4c]]
- **Used by:** [[lib_18a33f4c]]
- **Architecture:** [[arch_closed_loop_feedback_dbg2ca9i]], [[arch_rl_learning_loop_b3d4f2a1]], [[arch_scoring_dimensions_caf1b9h8]]
