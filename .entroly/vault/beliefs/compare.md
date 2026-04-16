---
claim_id: b6c2ac4e-500e-46ae-b9cc-09d35cffaf1c
entity: compare
status: inferred
confidence: 0.75
sources:
  - bench/compare.py:152
  - bench/compare.py:167
  - bench/compare.py:188
  - bench/compare.py:262
  - bench/compare.py:298
  - bench/compare.py:34
  - bench/compare.py:77
  - bench/compare.py:83
last_checked: 2026-04-14T04:12:29.385291+00:00
derived_from:
  - belief_compiler
  - sast
---

# Module: compare

**Language:** python
**Lines of code:** 395


## Functions
- `def strategy_raw(corpus: list[dict], query: str, budget: int) -> list[dict]` — Stuff tokens in insertion order until budget exhausted.
- `def strategy_topk(corpus: list[dict], query: str, budget: int) -> list[dict]` — Rank by query term overlap (simulated cosine similarity), take top-K.
- `def strategy_entroly(corpus: list[dict], query: str, budget: int) -> list[dict]` — Knapsack-optimal selection with: - Information density scoring (entropy × (1 - boilerplate)) - Query relevance weighting - Submodular diversity (diminishing returns per module) - Near-duplicate detect
- `def evaluate(strategy_name: str, selected: list[dict], query: str, budget: int) -> dict` — Compute metrics for a context selection.
- `def main()`

## Dependencies
- `__future__`
- `hashlib`
- `math`
- `pathlib`
- `re`
- `sys`
- `time`
- `typing`
