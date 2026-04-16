---
claim_id: 4a3dc64c-cca4-4bd2-ae6f-ff8f3b71ff59
entity: extractor
status: inferred
confidence: 0.75
sources:
  - scripts\extractor.py:5
  - scripts\extractor.py:22
  - scripts\extractor.py:52
last_checked: 2026-04-14T04:12:09.415573+00:00
derived_from:
  - belief_compiler
  - sast
---

# Module: extractor

**Language:** python
**Lines of code:** 72


## Functions
- `def extract_python(filepath)`
- `def extract_rust(filepath)`
- `def main()`

## Dependencies
- `ast`
- `json`
- `os`
