---
claim_id: fda4ec1k_query_flow
entity: query_resolution_flow
status: inferred
confidence: 0.87
sources:
  - entroly-core/src/query.rs:1
  - entroly/query_refiner.py:43
  - entroly-core/src/cogops.rs:170
  - entroly-core/src/lib.rs:744
  - entroly-core/src/query_persona.rs:1
last_checked: 2026-04-04T12:00:00Z
derived_from:
  - query_18a33f4c
  - query_refiner_18a33f4c
  - query_persona_18a33f4c
  - cogops_18a33f4c
epistemic_layer: action
boundary_note: "Query parsing = Truth. Resolution routing = Action."
---

# Query Resolution Flow: From Vague Input to Optimized Context

A developer query undergoes five transformations before context is selected. This flow explains why the same query can produce different context sets over time.

## Stage 1: Vagueness Analysis (Rust, query.rs)

`compute_vagueness(query)` produces a [0,1] score:
- generic_verb_ratio * 0.5 (fraction of tokens like "fix", "help", "debug")
- short_penalty * 0.3 (< 3 tokens = 0.7, < 5 = 0.4, < 7 = 0.15)
- specificity_bonus * 0.7 (technical terms like "cwe", "sql", "mutex" reduce vagueness)
- camelCase identifiers add 0.2 specificity bonus

Threshold: vagueness >= 0.45 triggers refinement.

## Stage 2: Key Term Extraction (Rust, query.rs)

TF-IDF over a corpus of [query_tokens] + [fragment_summary_tokens]:
- TF: term count / total terms
- IDF: log(N / (1 + df)) + 1 (smooth IDF)
- Top 12 terms returned, sorted by TF-IDF score descending

Without fragment context, falls back to TF + word length bonus (longer = more specific).

## Stage 3: Heuristic Refinement (Rust, query.rs)

If needs_refinement=true, `refine_heuristic()` grounds the query in fragment vocabulary:
1. Score each fragment by token overlap with query terms
2. Take top-3 most relevant fragments
3. Extract unique technical terms (>= 4 chars, contains '_' or starts alphabetic)
4. Append: "[context: term1, term2, ...]" to original query

This is deterministic, offline, no LLM call. The optional LLM path (Python, query_refiner.py) can override for truly ambiguous queries.

## Stage 4: Intent Classification (Rust, cogops.rs:170)

`classify_intent(query)` maps to one of 13 EpistemicIntents via priority-ordered keyword matching. This determines:
- Which epistemic flow to use (FastAnswer vs VerifyBefore vs CompileOnDemand)
- Risk level (Low/Medium/High) affecting verification requirements
- Task-type budget multiplier from guardrails

## Stage 5: Query Persona Assignment (Rust, lib.rs:744)

The QueryPersonaManifold (Pitman-Yor process) assigns the query to an archetype:
1. Build TF-IDF feature vector from analysis
2. Compute PSM embedding features (vagueness, query length, term count)
3. Match to existing archetype or birth a new one (CRP probability)
4. Return per-archetype learned weights (override global PRISM weights)

This means "security audit" queries use different scoring weights than "refactor this function" queries, learned from past success/failure patterns per archetype.

## The Critical Insight

Stages 1-3 improve the query BEFORE it enters the optimizer. Stage 4 determines HOW the system processes it. Stage 5 determines WHICH weight profile is used. A "fix the bug" query gets refined, classified as Repair intent, and matched to a repair archetype that may emphasize recency (recent changes are likely the bug) over semantic similarity.

## Related Modules

- **Modules:** [[cogops_18a33f4c]], [[prism_18a33f4c]], [[query_18a33f4c]], [[query_persona_18a33f4c]], [[query_refiner_18a33f4c]], [[server_18a33f4c]]
- **Related architectures:** [[arch_rust_python_boundary_c4e5f3b2]]
