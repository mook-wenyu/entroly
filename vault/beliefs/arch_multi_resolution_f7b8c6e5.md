---
claim_id: f7b8c6e5_multi_resolution
entity: multi_resolution_context
status: inferred
confidence: 0.87
sources:
  - entroly-core/src/knapsack_sds.rs:37
  - entroly-core/src/skeleton.rs:1
  - entroly-core/src/hierarchical.rs:1
  - entroly-core/src/conversation_pruner.rs:1
  - entroly-core/src/lib.rs:547
last_checked: 2026-04-04T12:00:00Z
derived_from:
  - knapsack_sds_18a33f4c
  - skeleton_18a33f4c
  - hierarchical_18a33f4c
  - conversation_pruner_18a33f4c
epistemic_layer: truth
boundary_note: "Fragment chunking = Truth. Resolution selection = Belief."
---

# Multi-Resolution Context: Three Independent Resolution Systems

Entroly implements multi-resolution context at three different scopes, each using the same principle (variable fidelity under budget constraint) but for different purposes.

## 1. Fragment Resolution (IOS/MRK) — Per-Fragment

Each fragment can be included at three resolutions (knapsack_sds.rs:37):
- **Full**: 100% information, 100% tokens
- **Skeleton**: ~70% information, ~20% tokens (signatures + structure)
- **Reference**: ~15% information, ~2% tokens (file path + function name)

The Multi-Resolution Knapsack (MCKP) formulation means the optimizer chooses resolution per-fragment. Under tight budget, critical fragments stay full while peripheral ones degrade to skeleton or reference. The information retention factors (0.70 skeleton, 0.15 reference) are tunable via autotune.

Skeleton extraction (skeleton.rs) is pattern-based (no tree-sitter), supporting 16 languages. It strips function bodies while keeping signatures, class definitions, imports. Returns None when skeleton would be >70% of original (not worth the overhead).

## 2. Hierarchical Compression (HCC) — Codebase-Wide

Three levels (hierarchical.rs):
- **Level 1**: One-line per file ("auth.py -> AuthService, login(), verify_token()") — ~3-8 tokens/file
- **Level 2**: Expanded skeletons for dependency-connected cluster around query
- **Level 3**: Full content for knapsack-optimal fragments

This gives the LLM a complete codebase map (L1) while focusing detail on relevant areas (L2/L3). Budget allocation across levels uses PageRank centrality on the dependency graph.

## 3. Conversation Pruning (Causal DAG) — Temporal

Four LOD tiers for conversation blocks (conversation_pruner.rs):
- **L0**: Full verbatim text (0% savings, 100% info)
- **L1**: Structural skeleton (~70% savings, ~85% info)
- **L2**: One-line semantic digest (~92% savings, ~35% info)
- **L3**: 64-bit SimHash fingerprint (~99% savings, ~5% info)

Progressive compression based on utilization thresholds (70/80/90/95%). Old conversation blocks gracefully degrade from L0 to L3 over time. Nothing is ever fully deleted — L3 fingerprints allow retrieval if the conversation circles back.

## The Unifying Principle

All three systems solve the same problem: maximize information density under a token budget by allowing variable fidelity. The key insight is that the "right" resolution depends on context — a fragment's importance relative to the current query, its position in the dependency graph, and its age in the conversation. The optimizer makes these decisions jointly, not independently.

## Related Modules

- **Modules:** [[conversation_pruner_18a33f4c]], [[fragment_18a33f4c]], [[hierarchical_18a33f4c]], [[knapsack_sds_18a33f4c]], [[skeleton_18a33f4c]]
- **Related architectures:** [[arch_optimize_pipeline_a7c2e1f0]]
