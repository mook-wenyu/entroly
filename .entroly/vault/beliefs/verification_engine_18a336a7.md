---
claim_id: 18a336a70c53d4dc0c6b6adc
entity: verification_engine
status: stale
confidence: 0.75
sources:
  - entroly\verification_engine.py:35
  - entroly\verification_engine.py:46
  - entroly\verification_engine.py:57
  - entroly\verification_engine.py:65
  - entroly\verification_engine.py:75
last_checked: 2026-04-04T17:12:49Z
derived_from:
  - cogops_compiler
---

# Module: verification_engine

**LOC:** 485

## Entities
- `class Contradiction:` (class)
- `class StaleReport:` (class)
- `class CoverageGap:` (class)
- `class BlastRadius:` (class)
- `class VerificationReport:` (class)
- `def to_dict(self) -> Dict[str, Any]` (function)
- `class VerificationEngine:` (class)
- `def full_verification_pass(self) -> VerificationReport` (function)
- `def check_belief(self, claim_id: str) -> Dict[str, Any]` (function)
- `def coverage_gaps(self, source_dir: str) -> List[CoverageGap]` (function)
