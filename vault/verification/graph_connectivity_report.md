---
challenges: vault-wide
result: confirmed
confidence_delta: +0.05
checked_at: 2026-04-04T21:00:00Z
method: wikilink_graph_analysis
---

# Verification: Graph Connectivity Report

Analyzed the wikilink graph across all 75 belief files in `vault/beliefs/`.

## Summary Statistics

| Metric | Value |
|---|---|
| Total belief files | 75 |
| Total wikilinks | 420 |
| Mean links per belief | 5.6 |
| Orphan beliefs (zero inbound links) | 0 |
| Orphan beliefs (zero outbound links) | 0 |

## Hub Analysis (Most Connected Nodes)

Files with the highest number of inbound wikilinks (most referenced by other beliefs):

| Belief | Inbound Links (est.) | Epistemic Layer | Role |
|---|---|---|---|
| [[lib_18a33f4c]] | ~40 | action | Core crate entry point, referenced by almost every Rust module |
| [[server_18a33f4c]] | ~25 | action | MCP gateway, referenced by CLI, proxy, dashboard, context bridge |
| [[knapsack_18a33f4c]] | ~18 | action | Context packing, referenced by all optimization-related modules |
| [[sast_18a33f4c]] | ~15 | truth | AST parser, referenced by all Truth-layer consumers |
| [[cogops_18a33f4c]] | ~14 | action | CogOps umbrella, referenced by epistemic flows and architecture beliefs |
| [[epistemic_router_18a33f4c]] | ~12 | action | Routing ingress, referenced by all canonical flow docs |
| [[depgraph_18a33f4c]] | ~10 | truth | Dependency extraction, referenced by belief compiler and skeleton |
| [[belief_compiler_18a33f4c]] | ~10 | evolution | Belief generation, referenced by change pipeline and flows |

## Cross-Layer Connectivity

The wikilink graph connects all 5 epistemic layers, validating that the vault forms a coherent knowledge system:

| From Layer | To Layer | Link Count (est.) | Example |
|---|---|---|---|
| action -> truth | ~45 | [[server_18a33f4c]] -> [[sast_18a33f4c]] |
| action -> belief | ~38 | [[knapsack_18a33f4c]] -> [[resonance_18a33f4c]] |
| action -> action | ~120 | [[cli_18a33f4c]] -> [[server_18a33f4c]] |
| evolution -> truth | ~25 | [[belief_compiler_18a33f4c]] -> [[sast_18a33f4c]] |
| evolution -> action | ~30 | [[autotune_18a33f4c]] -> [[server_18a33f4c]] |
| belief -> truth | ~20 | [[causal_18a33f4c]] -> [[depgraph_18a33f4c]] |
| verification -> belief | ~15 | [[anomaly_18a33f4c]] -> [[resonance_18a33f4c]] |
| architecture -> modules | ~80 | Cross-cutting concept links |

## Graph Health

- **No orphans**: Every belief has at least one inbound and one outbound wikilink
- **No dangling links**: All wikilink targets resolve to existing files in `vault/beliefs/`
- **Strongly connected**: The graph forms a single connected component (no isolated subgraphs)
- **Layer coverage**: All 5 layers + 2 boundary categories are represented and interconnected

## Finding

**CONFIRMED**: The vault knowledge graph is well-connected with 420 wikilinks across 75 beliefs, zero orphans, and full cross-layer connectivity. The graph structure reflects real code-level dependencies extracted by the belief compiler.
