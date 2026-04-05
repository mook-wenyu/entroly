---
claim_id: 18a336a72adf31802af6c780
entity: depgraph
status: inferred
confidence: 0.75
sources:
  - entroly-wasm\src\depgraph.rs:32
  - entroly-wasm\src\depgraph.rs:44
  - entroly-wasm\src\depgraph.rs:61
  - entroly-wasm\src\depgraph.rs:74
  - entroly-wasm\src\depgraph.rs:84
last_checked: 2026-04-04T17:12:49Z
derived_from:
  - cogops_compiler
---

# Module: depgraph

**LOC:** 1432

## Entities
- `pub struct Dependency` (struct)
- `pub enum DepType` (enum)
- `pub struct DepGraph` (struct)
- `pub fn new() -> Self` (function)
- `pub fn register_symbol(&mut self, symbol: &str, fragment_id: &str)` (function)
- `pub fn add_dependency(&mut self, dep: Dependency)` (function)
- `pub fn auto_link(&mut self, fragment_id: &str, content: &str)` (function)
- `fn extract_import_targets(content: &str) -> HashSet<String>` (function)
- `fn extract_ffi_exports(content: &str) -> Vec<(String, String)>` (function)
- `fn is_type_reference(lower_content: &str, ident: &str) -> bool` (function)
- `pub fn transitive_deps(&self, fragment_id: &str, max_depth: usize) -> Vec<String>` (function)
- `pub fn reverse_deps(&self, fragment_id: &str) -> Vec<String>` (function)
- `pub fn compute_dep_boosts(` (function)
- `pub fn connected_components(&self, fragment_ids: &[String]) -> Vec<Vec<String>>` (function)
- `pub fn symbol_definitions(&self) -> &HashMap<String, String>` (function)
- `pub fn has_symbol(&self, symbol: &str) -> bool` (function)
- `pub fn edge_count(&self) -> usize` (function)
- `pub fn node_count(&self) -> usize` (function)
- `pub fn extract_identifiers(content: &str) -> Vec<String>` (function)
- `fn extract_definitions(content: &str) -> Vec<String>` (function)
- `fn extract_require_lhs(line: &str) -> Option<String>` (function)
- `fn extract_fn_name_from_line(line: &str) -> Option<String>` (function)
- `fn extract_struct_name_from_line(line: &str) -> Option<String>` (function)
- `fn is_keyword(word: &str) -> bool` (function)
- `fn test_extract_definitions_python()` (function)
- `fn test_extract_definitions_rust()` (function)
- `fn test_dependency_boost()` (function)
- `fn test_connected_components()` (function)
- `fn test_transitive_deps()` (function)
- `fn test_extract_definitions_js_function()` (function)
- `fn test_extract_definitions_arrow_functions()` (function)
- `fn test_extract_definitions_ts_interface_type_enum()` (function)
- `fn test_extract_import_targets_default_import()` (function)
- `fn test_extract_import_targets_require()` (function)
- `fn test_pyo3_rust_to_python_linking()` (function)
- `fn process_data(input: &str) -> PyResult<String>` (function)
- `pub struct Engine` (struct)
- `fn test_jni_java_to_c_linking()` (function)
- `fn test_cgo_export_linking()` (function)
- `fn test_wasm_bindgen_linking()` (function)
- `pub fn greet(name: &str) -> String` (function)
- `fn test_napi_linking()` (function)
- `fn test_c_ffi_extern_c_linking()` (function)
- `fn test_cross_lang_dep_boost()` (function)
- `fn test_pymethods_exports_methods()` (function)
- `fn run(&self, input: &str) -> String` (function)
- `pub fn stop(&self)` (function)
