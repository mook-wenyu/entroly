---
claim_id: ee6a73f0-ad2b-4b02-a654-ab1c955b65ed
entity: guardrails
status: inferred
confidence: 0.75
sources:
  - entroly-core/src/guardrails.rs:341
  - entroly-core/src/guardrails.rs:24
  - entroly-core/src/guardrails.rs:241
  - entroly-core/src/guardrails.rs:37
  - entroly-core/src/guardrails.rs:50
  - entroly-core/src/guardrails.rs:185
  - entroly-core/src/guardrails.rs:309
last_checked: 2026-04-14T04:12:29.599997+00:00
derived_from:
  - belief_compiler
  - sast
---

# Module: guardrails

**Language:** rust
**Lines of code:** 594

## Types
- `pub struct FeedbackTracker` — Feedback loop: record which fragments influenced a successful output.  Extended with per-fragment Welford variance tracking for RAVEN-UCB adaptive exploration (arXiv:2506.02933, June 2025).
- `pub enum Criticality` — Criticality level — overrides entropy and relevance scoring.
- `pub enum TaskType` — Adaptive budget allocation based on task type.  Different tasks need different context volumes: - Bug tracing: LARGE budget (need call chains, logs, history) - Refactoring: MEDIUM budget (need interfa

## Functions
- `fn path_depth(path: &str) -> usize` — Count directory depth: how many path separators precede the basename. "file:package.json" → 0, "file:src/types.ts" → 1, "file:a/b/c.ts" → 2
- `fn file_criticality(path: &str) -> Criticality` — Check if a file path matches critical file patterns.  Monorepo-aware: in monorepos (langfuse, turborepo, nx), config files like `package.json`, `tsconfig.json`, `types.ts` appear in *every* sub-packag
- `fn has_safety_signal(content: &str) -> bool` —  IMPORTANT: This must be TIGHT. Every match here force-pins the fragment, bypassing the budget. Broad patterns like "copyright" or "⚠️" caused hundreds of files to be pinned in real codebases, destroy
- `fn compute_ordering_priority(
    relevance: f64,
    criticality: Criticality,
    is_pinned: bool,
    dep_count: usize,
) -> f64` — Context ordering strategy.  LLMs are order-sensitive. Fragment ordering affects reasoning quality. We order by: pinned first → critical → high relevance → imports → rest

## Dependencies
- `serde::`
- `std::collections::HashMap`

## Key Invariants
- has_safety_signal:  IMPORTANT: This must be TIGHT. Every match here force-pins the fragment, bypassing the budget. Broa
