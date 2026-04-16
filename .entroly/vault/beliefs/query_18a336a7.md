---
claim_id: 18a336a72bca19702be1af70
entity: query
status: stale
confidence: 0.75
sources:
  - entroly-wasm\src\query.rs:58
  - entroly-wasm\src\query.rs:74
  - entroly-wasm\src\query.rs:81
  - entroly-wasm\src\query.rs:86
  - entroly-wasm\src\query.rs:99
last_checked: 2026-04-04T17:12:49Z
derived_from:
  - cogops_compiler
---

# Module: query

**LOC:** 393

## Entities
- `pub struct QueryAnalysis` (struct)
- `fn tokenize(text: &str) -> Vec<String>` (function)
- `fn is_stop_word(word: &str) -> bool` (function)
- `fn tf(tokens: &[String]) -> HashMap<String, f64>` (function)
- `fn idf(corpus: &[Vec<String>]) -> HashMap<String, f64>` (function)
- `pub fn extract_key_terms(` (function)
- `pub fn compute_vagueness(query: &str) -> (f64, String)` (function)
- `pub fn analyze_query(query: &str, fragment_summaries: &[String]) -> QueryAnalysis` (function)
- `pub fn refine_heuristic(query: &str, fragment_summaries: &[String]) -> String` (function)
- `fn test_vague_query_high_score()` (function)
- `fn test_specific_query_low_score()` (function)
- `fn test_key_term_extraction_removes_stopwords()` (function)
- `fn test_key_terms_prefers_specific_tokens()` (function)
- `fn test_refinement_adds_context_terms()` (function)
- `fn test_refinement_noop_on_empty_fragments()` (function)
- `fn test_analyze_query_full()` (function)
- `fn test_analyze_query_vague_needs_refinement()` (function)
- `fn test_stopwords_filtered()` (function)
- `fn test_idf_penalizes_common_terms()` (function)
