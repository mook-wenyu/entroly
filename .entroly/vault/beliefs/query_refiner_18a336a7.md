---
claim_id: 18a336a70be017f40bf7adf4
entity: query_refiner
status: inferred
confidence: 0.75
sources:
  - entroly\query_refiner.py:27
  - entroly\query_refiner.py:34
  - entroly\query_refiner.py:43
  - entroly\query_refiner.py:54
  - entroly\query_refiner.py:63
last_checked: 2026-04-04T17:12:49Z
derived_from:
  - cogops_compiler
---

# Module: query_refiner

**LOC:** 172

## Entities
- `def py_analyze_query(query: str, summaries: list) -> tuple:  # type: ignore[misc]` (function)
- `def py_refine_heuristic(query: str, summaries: list) -> str:  # type: ignore[misc]` (function)
- `class QueryRefiner:` (class)
- `def __init__(self, llm_fn: Optional[Callable[[str], str]] = None)` (function)
- `def analyze(self, query: str, fragment_summaries: List[str] | None = None) -> dict` (function)
- `def refine(self, query: str, fragment_summaries: List[str] | None = None) -> str` (function)
- `def make_openai_refine_fn(api_key: str, model: str = "gpt-4o-mini") -> Callable[[str], str]` (function)
