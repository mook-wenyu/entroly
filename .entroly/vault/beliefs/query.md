---
claim_id: 84cdbbfd-fc4e-43b9-bbd0-1726cea5c45d
entity: query
status: inferred
confidence: 0.75
sources:
  - entroly-core/src/query.rs:58
  - entroly-core/src/query.rs:74
  - entroly-core/src/query.rs:81
  - entroly-core/src/query.rs:86
  - entroly-core/src/query.rs:99
  - entroly-core/src/query.rs:118
  - entroly-core/src/query.rs:170
  - entroly-core/src/query.rs:223
  - entroly-core/src/query.rs:250
  - entroly-core/src/query.rs:311
last_checked: 2026-04-14T04:12:29.657841+00:00
derived_from:
  - belief_compiler
  - sast
---

# Module: query

**Language:** rust
**Lines of code:** 423

## Types
- `pub struct QueryAnalysis`

## Functions
- `fn tokenize(text: &str) -> Vec<String>` — Tokenize text into lowercase words, removing stop words and punctuation.
- `fn is_stop_word(word: &str) -> bool`
- `fn tf(tokens: &[String]) -> HashMap<String, f64>` — Compute TF (term frequency) for a token list.
- `fn idf(corpus: &[Vec<String>]) -> HashMap<String, f64>` — Compute IDF (inverse document frequency) given a corpus of token lists. Uses log(N / (1 + df)) + 1 (smooth IDF).
- `fn extract_key_terms(
    query: &str,
    fragment_summaries: &[String],
    top_n: usize,
) -> Vec<String>` — Extract top-N key terms from a query using TF-IDF over the fragment corpus.  If `fragment_summaries` is empty, falls back to TF-only ranking.  Returns sorted (descending score) vector of term strings.
- `fn compute_vagueness(query: &str) -> (f64, String)` —  Algorithm: vagueness = generic_verb_ratio × 0.5 + short_penalty × 0.3 − specificity_bonus × 0.2  - `generic_verb_ratio`: fraction of tokens that are generic verbs ("fix", "help", "add") - `short_pena
- `fn analyze_query(query: &str, fragment_summaries: &[String]) -> QueryAnalysis` — Full query analysis: vagueness + key term extraction.
- `fn refine_heuristic(query: &str, fragment_summaries: &[String]) -> String` —  Algorithm: 1. Extract key terms from query 2. Find which fragments have highest vocabulary overlap with query terms 3. Inject top matching fragments' unique vocabulary into query 4. Reconstruct a mor
- `fn py_analyze_query(
    query: &str,
    fragment_summaries: Vec<String>,
) -> (f64, Vec<String>, bool, String)` — Analyze a query for vagueness and extract key terms.  Returns a tuple: (vagueness_score: float, key_terms: list[str], needs_refinement: bool, reason: str)
- `fn py_refine_heuristic(query: &str, fragment_summaries: Vec<String>) -> String` — Heuristic query refinement — grounded in fragment vocabulary, no LLM needed.  Returns the refined query string.

## Dependencies
- `pyo3::prelude::`
- `serde::Serialize`
- `std::collections::HashMap`
