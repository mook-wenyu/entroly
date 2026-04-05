---
claim_id: e6a7b5d4_dedup_hierarchy
entity: dedup_hierarchy
status: inferred
confidence: 0.88
sources:
  - entroly-core/src/dedup.rs:1
  - entroly-core/src/lsh.rs:1
  - entroly-core/src/semantic_dedup.rs:1
  - entroly-core/src/knapsack_sds.rs:100
  - entroly-core/src/resonance.rs:38
  - entroly-core/src/lib.rs:400
last_checked: 2026-04-04T12:00:00Z
derived_from:
  - dedup_18a33f4c
  - lsh_18a33f4c
  - semantic_dedup_18a33f4c
  - knapsack_sds_18a33f4c
epistemic_layer: belief
boundary_note: "Covers both dedup (Truth) and hierarchical merging (Belief)."
---

# Four-Layer Deduplication Hierarchy

Entroly applies deduplication at four progressively broader levels, each catching a different class of redundancy. Understanding this hierarchy explains why four separate modules exist for what seems like "removing duplicates."

## Layer 1: Exact/Near-Exact Dedup (dedup.rs) — At Ingestion

SimHash fingerprinting (64-bit, word trigram features) + LSH banding (4 bands x 16 bits). Hamming threshold = 3 bits. Catches verbatim or near-verbatim duplicates at ingestion time. O(1) amortized. This is the cheapest check and runs first.

When a duplicate is caught, the existing fragment's access_count and frequency_score are updated instead of creating a new entry. This converts repeated ingestion into frequency signal.

## Layer 2: Fragment Consolidation / Maxwell's Demon (resonance.rs + lib.rs:400)

Every 5 turns, scans for fragment pairs with Hamming distance <= 8 (wider than dedup's 3). Groups near-duplicates, picks the winner (highest feedback multiplier), transfers access counts from losers to winner, evicts losers. This catches fragments that diverged slightly over time through re-ingestion with edits.

## Layer 3: Semantic Dedup (semantic_dedup.rs) — Pre-Selection Filter

Catches structurally different fragments carrying the same information (e.g., a docstring, a comment, and the code itself). Uses greedy marginal information gain: each candidate must contribute >= 30% new information (trigram Jaccard + identifier Jaccard) to pass. Runs BEFORE IOS selection.

This is the (1-1/e) submodular maximization guarantee from Nemhauser et al. (1978).

## Layer 4: IOS Diversity Penalty (knapsack_sds.rs:100) — During Selection

Even after semantic dedup, the IOS optimizer applies a real-time diversity penalty during greedy selection. Each candidate's marginal value is multiplied by diversity_factor = 1 - max_similarity(candidate, selected_set), estimated from SimHash Hamming distance.

This catches situational redundancy: two fragments that are individually unique but redundant given the specific fragments already selected for THIS query.

## Why Four Layers?

Each layer operates at a different point in the pipeline and catches a different type of redundancy:

| Layer | When | What it catches | Cost |
|-------|------|----------------|------|
| 1. SimHash dedup | Ingestion | Verbatim copies | O(1) |
| 2. Consolidation | Every 5 turns | Slow drift duplicates | O(N^2) but infrequent |
| 3. Semantic dedup | Pre-selection | Informationally equivalent | O(N * k) |
| 4. IOS diversity | During selection | Query-conditional redundancy | O(N * K) |

The cost increases at each layer, but so does the sophistication of what's detected. This is analogous to a CPU cache hierarchy: L1 is fast and simple, L4 is slow but catches everything.

## Related Modules

- **Modules:** [[cache_18a33f4c]], [[cognitive_bus_18a33f4c]], [[dedup_18a33f4c]], [[health_18a33f4c]], [[knapsack_sds_18a33f4c]], [[lsh_18a33f4c]], [[semantic_dedup_18a33f4c]]
- **Related architectures:** [[arch_information_theory_stack_d5f6a4c3]], [[arch_memory_lifecycle_b9dae8g7]], [[arch_optimize_pipeline_a7c2e1f0]]
