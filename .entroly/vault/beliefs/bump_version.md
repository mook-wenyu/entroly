---
claim_id: 45359168-36fa-4933-9b81-261454f2c539
entity: bump_version
status: inferred
confidence: 0.75
sources:
  - scripts\bump_version.py:30
  - scripts\bump_version.py:11
  - scripts\bump_version.py:13
  - scripts\bump_version.py:27
last_checked: 2026-04-14T04:12:09.415039+00:00
derived_from:
  - belief_compiler
  - sast
---

# Module: bump_version

**Language:** python
**Lines of code:** 50


## Functions
- `def main(argv: list[str]) -> int`

## Dependencies
- `__future__`
- `pathlib`
- `re`
- `sys`
