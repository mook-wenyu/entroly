---
claim_id: 6c7fc59b-17dc-4aab-b68e-dd9c38d198fa
entity: health
status: inferred
confidence: 0.75
sources:
  - entroly-core/src/health.rs:56
  - entroly-core/src/health.rs:98
  - entroly-core/src/health.rs:108
  - entroly-core/src/health.rs:119
  - entroly-core/src/health.rs:130
  - entroly-core/src/health.rs:139
  - entroly-core/src/health.rs:69
  - entroly-core/src/health.rs:169
  - entroly-core/src/health.rs:236
  - entroly-core/src/health.rs:321
last_checked: 2026-04-14T04:12:29.604090+00:00
derived_from:
  - belief_compiler
  - sast
---

# Module: health

**Language:** rust
**Lines of code:** 851

## Types
- `pub struct ClonePair` — A pair of fragments that are near-duplicates (code clones).
- `pub struct DeadSymbol` — A symbol that appears to be defined but never referenced across all known fragments.
- `pub struct GodFile` — A "god file" — a fragment that too many others depend on.
- `pub struct ArchViolation` — An architectural layer violation — a lower-layer importing a higher-layer module.
- `pub struct NamingIssue` — Naming consistency issue: files that break established naming conventions.
- `pub struct HealthReport` — Full codebase health report.
- `pub enum CloneType` — Clone types (after Koschke et al., adapted for SimHash detection).

## Functions
- `fn detect_clones(fragments: &[&ContextFragment]) -> Vec<ClonePair>`
- `fn find_dead_symbols(
    fragments: &[&ContextFragment],
    dep_graph: &DepGraph,
) -> Vec<DeadSymbol>`
- `fn is_generic_symbol(sym: &str) -> bool` — Skip symbols that are so common they're meaningless as dead-code indicators.
- `fn find_god_files(
    fragments: &[&ContextFragment],
    dep_graph: &DepGraph,
) -> Vec<GodFile>`
- `fn classify_layer(source: &str) -> Option<(usize, &'static str)>`
- `fn find_arch_violations(fragments: &[&ContextFragment]) -> Vec<ArchViolation>`
- `fn find_layer_in_import(import_line: &str) -> Option<(usize, &'static str)>`
- `fn find_naming_issues(fragments: &[&ContextFragment]) -> Vec<NamingIssue>`
- `fn compute_code_health(
    n: usize,
    total_symbols: usize,
    clone_pairs: &[ClonePair],
    dead_symbols: &[DeadSymbol],
    god_files: &[GodFile],
    arch_violations: &[ArchViolation],
    naming_issues: &[NamingIssue],
) -> (f64, f64, f64, f64, f64, f64)`
- `fn health_grade(score: f64) -> &'static str`
- `fn analyze_health(
    fragments: &[&ContextFragment],
    dep_graph: &DepGraph,
) -> HealthReport`
- `fn basename(path: &str) -> &str`
- `fn to_snake_case(s: &str) -> String`
- `fn to_pascal_case(s: &str) -> String`

## Dependencies
- `crate::dedup::hamming_distance`
- `crate::depgraph::DepGraph`
- `crate::fragment::ContextFragment`
- `serde::`
- `std::collections::`
