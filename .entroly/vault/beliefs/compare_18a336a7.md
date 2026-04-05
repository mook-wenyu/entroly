---
claim_id: 18a336a707f4d65c080c6c5c
entity: compare
status: inferred
confidence: 0.75
sources:
  - bench\compare.py:152
  - bench\compare.py:167
  - bench\compare.py:188
  - bench\compare.py:262
  - bench\compare.py:298
last_checked: 2026-04-04T17:12:49Z
derived_from:
  - cogops_compiler
---

# Module: compare

**LOC:** 394

## Entities
- `def strategy_raw(corpus: list[dict], query: str, budget: int) -> list[dict]` (function)
- `def strategy_topk(corpus: list[dict], query: str, budget: int) -> list[dict]` (function)
- `def strategy_entroly(corpus: list[dict], query: str, budget: int) -> list[dict]` (function)
- `def evaluate(strategy_name: str, selected: list[dict], query: str, budget: int) -> dict` (function)
- `def main()` (function)
