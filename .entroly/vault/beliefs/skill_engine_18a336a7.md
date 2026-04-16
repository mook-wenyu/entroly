---
claim_id: 18a336a70c1a33bc0c31c9bc
entity: skill_engine
status: stale
confidence: 0.75
sources:
  - entroly\skill_engine.py:36
  - entroly\skill_engine.py:52
  - entroly\skill_engine.py:62
  - entroly\skill_engine.py:71
  - entroly\skill_engine.py:172
last_checked: 2026-04-04T17:12:49Z
derived_from:
  - cogops_compiler
---

# Module: skill_engine

**LOC:** 520

## Entities
- `class SkillSpec:` (class)
- `class BenchmarkResult:` (class)
- `def success_rate(self) -> float` (function)
- `class SkillSynthesizer:` (class)
- `class SandboxedRunner:` (class)
- `def __init__(self, timeout_seconds: float = 10.0)` (function)
- `def run_tool(self, tool_code: str, query: str) -> Dict[str, Any]` (function)
- `class SkillBenchmark:` (class)
- `def __init__(self, runner: Optional[SandboxedRunner] = None)` (function)
- `def benchmark(self, skill: SkillSpec) -> BenchmarkResult` (function)
- `class SkillEngine:` (class)
- `def __init__(self, vault: VaultManager)` (function)
- `def benchmark_skill(self, skill_id: str) -> Dict[str, Any]` (function)
- `def promote_or_prune(self, skill_id: str) -> Dict[str, Any]` (function)
- `def list_skills(self) -> List[Dict[str, Any]]` (function)
