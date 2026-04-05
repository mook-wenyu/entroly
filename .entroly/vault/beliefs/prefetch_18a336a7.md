---
claim_id: 18a336a70b592b540b70c154
entity: prefetch
status: inferred
confidence: 0.75
sources:
  - entroly\prefetch.py:45
  - entroly\prefetch.py:91
  - entroly\prefetch.py:103
  - entroly\prefetch.py:133
  - entroly\prefetch.py:181
last_checked: 2026-04-04T17:12:49Z
derived_from:
  - cogops_compiler
---

# Module: prefetch

**LOC:** 297

## Entities
- `class PrefetchResult:` (class)
- `def extract_callees(source: str, language: str = "python") -> List[str]` (function)
- `def extract_imports(source: str, language: str = "python") -> List[str]` (function)
- `def infer_test_files(file_path: str) -> List[str]` (function)
- `class PrefetchEngine:` (class)
- `def __init__(self, co_access_window: int = 5)` (function)
- `def record_access(self, file_path: str, turn: int) -> None` (function)
- `def stats(self) -> dict` (function)
