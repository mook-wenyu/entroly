---
claim_id: 18a336a708966f1c08ae051c
entity: change_pipeline
status: inferred
confidence: 0.75
sources:
  - entroly\change_pipeline.py:36
  - entroly\change_pipeline.py:50
  - entroly\change_pipeline.py:60
  - entroly\change_pipeline.py:71
  - entroly\change_pipeline.py:80
last_checked: 2026-04-04T17:12:49Z
derived_from:
  - cogops_compiler
---

# Module: change_pipeline

**LOC:** 450

## Entities
- `class ChangeSet:` (class)
- `class BeliefDiff:` (class)
- `class ReviewFinding:` (class)
- `class PRBrief:` (class)
- `def to_markdown(self) -> str` (function)
- `def parse_diff(diff_text: str, commit_message: str = "") -> ChangeSet` (function)
- `def review_diff(diff_text: str) -> List[ReviewFinding]` (function)
- `class ChangePipeline:` (class)
- `def __init__(self, vault: VaultManager, verification: VerificationEngine)` (function)
- `def refresh_docs(self, changed_files: List[str]) -> Dict[str, Any]` (function)
