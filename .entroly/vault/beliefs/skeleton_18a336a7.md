---
claim_id: 18a336a72c46b1242c5e4724
entity: skeleton
status: stale
confidence: 0.75
sources:
  - entroly-wasm\src\skeleton.rs:19
  - entroly-wasm\src\skeleton.rs:39
  - entroly-wasm\src\skeleton.rs:85
  - entroly-wasm\src\skeleton.rs:128
  - entroly-wasm\src\skeleton.rs:133
last_checked: 2026-04-04T17:12:49Z
derived_from:
  - cogops_compiler
---

# Module: skeleton

**LOC:** 2573

## Entities
- `pub enum Lang` (enum)
- `fn detect_lang(source: &str) -> Lang` (function)
- `pub fn extract_skeleton(content: &str, source: &str) -> Option<String>` (function)
- `fn leading_spaces(line: &str) -> usize` (function)
- `fn count_char(s: &str, ch: char) -> usize` (function)
- `fn extract_python_skeleton(content: &str) -> String` (function)
- `fn extract_rust_skeleton(content: &str) -> String` (function)
- `fn extract_js_skeleton(content: &str) -> String` (function)
- `fn extract_go_skeleton(content: &str) -> String` (function)
- `fn extract_java_skeleton(content: &str) -> String` (function)
- `fn extract_cpp_skeleton(content: &str) -> String` (function)
- `fn extract_swift_skeleton(content: &str) -> String` (function)
- `fn extract_shell_skeleton(content: &str) -> String` (function)
- `fn is_rust_type_def(trimmed: &str) -> bool` (function)
- `fn is_js_method_sig(trimmed: &str) -> bool` (function)
- `fn is_java_type_def(trimmed: &str) -> bool` (function)
- `fn is_java_method_line(trimmed: &str) -> bool` (function)
- `fn is_cpp_function_def(trimmed: &str) -> bool` (function)
- `fn is_swift_type_def(trimmed: &str) -> bool` (function)
- `fn extract_ruby_skeleton(content: &str) -> String` (function)
- `fn extract_php_skeleton(content: &str) -> String` (function)
- `fn is_php_type_def(trimmed: &str) -> bool` (function)
- `fn is_php_function_line(trimmed: &str) -> bool` (function)
- `fn extract_sfc_skeleton(content: &str) -> String` (function)
- `pub enum Block` (enum)
- `fn extract_html_skeleton(content: &str) -> String` (function)
- `fn extract_css_skeleton(content: &str) -> String` (function)
- `fn test_python_skeleton()` (function)
- `fn test_rust_skeleton()` (function)
- `pub struct Fragment` (struct)
- `pub fn new(id: String) -> Self` (function)
- `pub fn score(&self) -> f64` (function)
- `fn helper(x: u32) -> u32` (function)
- `fn test_js_skeleton()` (function)
- `fn test_ts_interface_kept()` (function)
- `fn test_unknown_lang_returns_none()` (function)
- `fn test_short_content_returns_none()` (function)
- `fn test_skeleton_too_similar_returns_none()` (function)
- `fn test_go_skeleton()` (function)
- `fn test_java_skeleton()` (function)
- `fn test_cpp_skeleton()` (function)
- `fn test_ruby_skeleton()` (function)
- `fn test_php_skeleton()` (function)
- `fn test_vue_sfc_skeleton()` (function)
- `fn test_html_skeleton()` (function)
- `fn test_css_skeleton()` (function)
