---
claim_id: 056ef2f1-d3fb-4936-9f1d-a86f7abf4538
entity: depgraph
status: inferred
confidence: 0.75
sources:
  - entroly-core/src/depgraph.rs:32
  - entroly-core/src/depgraph.rs:61
  - entroly-core/src/depgraph.rs:44
  - entroly-core/src/depgraph.rs:762
  - entroly-core/src/depgraph.rs:793
  - entroly-core/src/depgraph.rs:1010
  - entroly-core/src/depgraph.rs:1042
  - entroly-core/src/depgraph.rs:1053
  - entroly-core/src/depgraph.rs:1068
  - entroly-core/src/depgraph.rs:1252
last_checked: 2026-04-14T04:12:29.591071+00:00
derived_from:
  - belief_compiler
  - sast
---

# Module: depgraph

**Language:** rust
**Lines of code:** 1433

## Types
- `pub struct Dependency` — A directed dependency between two fragments.
- `pub struct DepGraph` — The dependency graph.
- `pub enum DepType`

## Functions
- `fn extract_identifiers(content: &str) -> Vec<String>` — Extract identifiers (function names, variable names) from source code. Fast, regex-free extraction for supported languages.
- `fn extract_definitions(content: &str) -> Vec<String>` — Extract symbol definitions (def, class, fn, struct, etc.)
- `fn extract_require_lhs(line: &str) -> Option<String>` — Extract the LHS variable name from `const foo = require('...')`.
- `fn extract_fn_name_from_line(line: &str) -> Option<String>` — Extract function name from a line like "fn process(" or "pub fn process(".
- `fn extract_struct_name_from_line(line: &str) -> Option<String>` — Extract struct/class name from a line like "struct Engine" or "pub struct Engine {".
- `fn is_keyword(word: &str) -> bool` — Check if an identifier is a language keyword (ignore these).
- `fn process_data(input: &str) -> PyResult<String>`
- `fn greet(name: &str) -> String`

## Dependencies
- `pyo3::prelude::`
- `serde::`
- `std::collections::`
- `wasm_bindgen::prelude::`
