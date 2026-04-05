---
claim_id: 18a336a70c421cec0c59b2ec
entity: vault
status: inferred
confidence: 0.75
sources:
  - entroly\vault.py:49
  - entroly\vault.py:55
  - entroly\vault.py:66
  - entroly\vault.py:80
  - entroly\vault.py:99
last_checked: 2026-04-04T17:12:49Z
derived_from:
  - cogops_compiler
---

# Module: vault

**LOC:** 426

## Entities
- `class VaultConfig:` (class)
- `def path(self) -> Path` (function)
- `class BeliefArtifact:` (class)
- `def to_markdown(self) -> str` (function)
- `def to_dict(self) -> Dict[str, Any]` (function)
- `class VerificationArtifact:` (class)
- `def to_markdown(self) -> str` (function)
- `class VaultManager:` (class)
- `def __init__(self, config: Optional[VaultConfig] = None)` (function)
- `def ensure_structure(self) -> Dict[str, Any]` (function)
- `def write_belief(self, artifact: BeliefArtifact) -> Dict[str, Any]` (function)
- `def read_belief(self, entity: str) -> Optional[Dict[str, Any]]` (function)
- `def list_beliefs(self) -> List[Dict[str, Any]]` (function)
- `def write_verification(self, artifact: VerificationArtifact) -> Dict[str, Any]` (function)
- `def coverage_index(self) -> Dict[str, Any]` (function)
