---
claim_id: 80f5092d-b737-4c42-b5e0-9f030975332d
entity: super_extractor
status: inferred
confidence: 0.75
sources:
  - scripts\super_extractor.py:4
  - scripts\super_extractor.py:25
  - scripts\super_extractor.py:45
  - scripts\super_extractor.py:53
last_checked: 2026-04-14T04:12:09.415573+00:00
derived_from:
  - belief_compiler
  - sast
---

# Module: super_extractor

**Language:** python
**Lines of code:** 87


## Functions
- `def extract_python(filepath)`
- `def extract_rust(filepath)`
- `def extract_generic(filepath)`
- `def main()`

## Dependencies
- `ast`
- `os`
