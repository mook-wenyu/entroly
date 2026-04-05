---
claim_id: 18a336a72b23d6f02b3b6cf0
entity: health
status: inferred
confidence: 0.75
sources:
  - entroly-wasm\src\health.rs:44
  - entroly-wasm\src\health.rs:56
  - entroly-wasm\src\health.rs:69
  - entroly-wasm\src\health.rs:79
  - entroly-wasm\src\health.rs:87
last_checked: 2026-04-04T17:12:49Z
derived_from:
  - cogops_compiler
---

# Module: health

**LOC:** 850

## Entities
- `pub(crate) fn label(self) -> &'static str` (function)
- `pub struct ClonePair` (struct)
- `pub enum CloneType` (enum)
- `fn from_hamming(dist: u32) -> Option<CloneType>` (function)
- `pub(crate) fn label(self) -> &'static str` (function)
- `pub struct DeadSymbol` (struct)
- `pub struct GodFile` (struct)
- `pub struct ArchViolation` (struct)
- `pub struct NamingIssue` (struct)
- `pub struct HealthReport` (struct)
- `fn detect_clones(fragments: &[&ContextFragment]) -> Vec<ClonePair>` (function)
- `fn find_dead_symbols(` (function)
- `fn is_generic_symbol(sym: &str) -> bool` (function)
- `fn find_god_files(` (function)
- `fn classify_layer(source: &str) -> Option<(usize, &'static str)>` (function)
- `fn find_arch_violations(fragments: &[&ContextFragment]) -> Vec<ArchViolation>` (function)
- `fn find_layer_in_import(import_line: &str) -> Option<(usize, &'static str)>` (function)
- `fn find_naming_issues(fragments: &[&ContextFragment]) -> Vec<NamingIssue>` (function)
- `fn compute_code_health(` (function)
- `fn health_grade(score: f64) -> &'static str` (function)
- `pub fn analyze_health(` (function)
- `fn basename(path: &str) -> &str` (function)
- `fn to_snake_case(s: &str) -> String` (function)
- `fn to_pascal_case(s: &str) -> String` (function)
- `fn make_frag(id: &str, content: &str, source: &str) -> ContextFragment` (function)
- `fn test_exact_clone_detected()` (function)
- `fn test_same_file_not_cloned()` (function)
- `fn test_god_file_detection()` (function)
- `fn test_code_health_perfect_score()` (function)
- `fn test_code_health_decreases_with_clones()` (function)
- `fn test_arch_violation_domain_imports_api()` (function)
- `fn test_health_grade_mapping()` (function)
- `fn test_snake_case_conversion()` (function)
- `fn test_empty_codebase_no_panic()` (function)
- `fn test_naming_issue_python_camel_case()` (function)
