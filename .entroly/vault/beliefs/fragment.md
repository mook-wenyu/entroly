---
claim_id: 82b36816-1724-4f47-90fe-7e3303760a19
entity: fragment
status: inferred
confidence: 0.75
sources:
  - entroly-core/src/fragment.rs:16
  - entroly-core/src/fragment.rs:135
  - entroly-core/src/fragment.rs:179
  - entroly-core/src/fragment.rs:192
last_checked: 2026-04-14T04:12:29.596765+00:00
derived_from:
  - belief_compiler
  - sast
---

# Module: fragment

**Language:** rust
**Lines of code:** 268

## Types
- `pub struct ContextFragment` — A single piece of context (code snippet, file content, tool result, etc.)

## Functions
- `fn compute_relevance(
    frag: &ContextFragment,
    w_recency: f64,
    w_frequency: f64,
    w_semantic: f64,
    w_entropy: f64,
    feedback_multiplier: f64,
) -> f64` —  Direct port of ebbiforge-core ContextScorer::score() but with entropy replacing emotion as the fourth dimension.  `feedback_multiplier` comes from FeedbackTracker::learned_value(): - > 1.0 = historic
- `fn softcap(x: f64, cap: f64) -> f64` — Logit softcap: `c · tanh(x / c)`.  Gemini-style bounded scoring. When `cap ≤ 0`, falls back to `min(x, 1)`.
- `fn apply_ebbinghaus_decay(
    fragments: &mut [ContextFragment],
    current_turn: u32,
    half_life: u32,
)` — Apply Ebbinghaus forgetting curve decay to all fragments.  recency(t) = exp(-λ · Δt) where λ = ln(2) / half_life  Same math as ebbiforge-core HippocampusEngine.

## Dependencies
- `pyo3::prelude::`
- `serde::`
