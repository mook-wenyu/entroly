---
claim_id: 18a336a7092b8f4809432548
entity: epistemic_router
status: inferred
confidence: 0.75
sources:
  - entroly\epistemic_router.py:39
  - entroly\epistemic_router.py:56
  - entroly\epistemic_router.py:65
  - entroly\epistemic_router.py:77
  - entroly\epistemic_router.py:88
last_checked: 2026-04-04T17:12:49Z
derived_from:
  - cogops_compiler
---

# Module: epistemic_router

**LOC:** 548

## Entities
- `class EpistemicIntent(str, Enum):` (class)
- `class EpistemicFlow(str, Enum):` (class)
- `class RiskLevel(str, Enum):` (class)
- `class BeliefCoverage:` (class)
- `class RoutingDecision:` (class)
- `def to_dict(self) -> Dict[str, Any]` (function)
- `def classify_intent(query: str) -> EpistemicIntent` (function)
- `def assess_risk(query: str, intent: EpistemicIntent) -> RiskLevel` (function)
- `class EpistemicRouter:` (class)
- `def record_miss(self, query: str) -> None` (function)
- `def stats(self) -> Dict[str, Any]` (function)
