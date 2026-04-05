---
claim_id: 18a336a72ac3049c2ada9a9c
entity: dedup
status: inferred
confidence: 0.75
sources:
  - entroly-wasm\src\dedup.rs:23
  - entroly-wasm\src\dedup.rs:34
  - entroly-wasm\src\dedup.rs:46
  - entroly-wasm\src\dedup.rs:92
  - entroly-wasm\src\dedup.rs:105
last_checked: 2026-04-04T17:12:49Z
derived_from:
  - cogops_compiler
---

# Module: dedup

**LOC:** 255

## Entities
- `fn hash_token(token: &str) -> u64` (function)
- `fn normalized_content_hash(text: &str) -> u64` (function)
- `pub fn simhash(text: &str) -> u64` (function)
- `pub fn hamming_distance(a: u64, b: u64) -> u32` (function)
- `pub struct DedupIndex` (struct)
- `pub fn new(hamming_threshold: u32) -> Self` (function)
- `pub fn hamming_threshold(&self) -> u32` (function)
- `fn extract_bands(&self, fp: u64) -> Vec<u64>` (function)
- `pub fn insert(&mut self, fragment_id: &str, text: &str) -> Option<String>` (function)
- `pub fn remove(&mut self, fragment_id: &str)` (function)
- `pub fn size(&self) -> usize` (function)
- `pub fn get_fingerprint(&self, fragment_id: &str) -> Option<u64>` (function)
- `pub fn export_fingerprints(&self) -> Vec<(String, u64)>` (function)
- `fn test_identical_texts()` (function)
- `fn test_dedup_catches_exact()` (function)
- `fn test_dedup_allows_different()` (function)
