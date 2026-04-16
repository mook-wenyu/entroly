---
claim_id: 0396feba-d850-4013-9380-5ba2e36d6276
entity: test_cogops_smoke
status: stale
confidence: 0.75
sources:
  - tests\test_cogops_smoke.py:37
  - tests\test_cogops_smoke.py:18
  - tests\test_cogops_smoke.py:39
  - tests\test_cogops_smoke.py:42
  - tests\test_cogops_smoke.py:15
  - tests\test_cogops_smoke.py:16
  - tests\test_cogops_smoke.py:45
last_checked: 2026-04-14T04:12:09.424054+00:00
derived_from:
  - belief_compiler
  - sast
---

# Module: test_cogops_smoke

**Language:** python
**Lines of code:** 200

## Types
- `class AuthService()` — Handles authentication and token rotation.

## Functions
- `def check(name, condition)`
- `def verify_token(self, token: str) -> bool` — Verify a JWT token.
- `def rotate_keys(self) -> None`

## Dependencies
- `entroly.belief_compiler`
- `entroly.change_pipeline`
- `entroly.epistemic_router`
- `entroly.evolution_logger`
- `entroly.flow_orchestrator`
- `entroly.skill_engine`
- `entroly.vault`
- `entroly.verification_engine`
- `json`
- `os`
- `tempfile`
