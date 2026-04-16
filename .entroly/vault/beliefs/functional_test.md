---
claim_id: 06d04d29-9642-4b3b-86eb-1aef1e04d176
entity: functional_test
status: inferred
confidence: 0.75
sources:
  - tests\functional_test.py:24
last_checked: 2026-04-14T04:12:09.418695+00:00
derived_from:
  - belief_compiler
  - sast
---

# Module: functional_test

**Language:** python
**Lines of code:** 137


## Functions
- `def run_functional_test()`

## Dependencies
- `entroly.config`
- `entroly.server`
- `entroly_core`
- `json`
- `logging`
- `os`
- `pathlib`
- `shutil`
- `sys`
- `tempfile`
- `uuid`

## Linked Beliefs
- [[entroly_core]]
- [[config]]
