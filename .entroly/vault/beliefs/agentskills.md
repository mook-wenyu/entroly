---
claim_id: c97d0667-ea4d-492f-a375-24ae6401b7f6
entity: agentskills
status: inferred
confidence: 0.75
sources:
  - entroly/integrations/agentskills.py:87
  - entroly/integrations/agentskills.py:19
  - entroly/integrations/agentskills.py:32
last_checked: 2026-04-14T04:12:29.457743+00:00
derived_from:
  - belief_compiler
  - sast
---

# Module: agentskills

**Language:** python
**Lines of code:** 178


## Functions
- `def export_promoted(
    vault_path: str | Path = ".entroly/vault",
    out_dir: str | Path = "./dist/agentskills",
) -> dict[str, Any]`

## Dependencies
- `__future__`
- `json`
- `pathlib`
- `shutil`
- `sys`
- `typing`
