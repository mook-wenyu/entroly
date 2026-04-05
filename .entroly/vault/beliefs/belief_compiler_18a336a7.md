---
claim_id: 18a336a708744054088bd654
entity: belief_compiler
status: inferred
confidence: 0.75
sources:
  - entroly\belief_compiler.py:38
  - entroly\belief_compiler.py:47
  - entroly\belief_compiler.py:59
  - entroly\belief_compiler.py:65
  - entroly\belief_compiler.py:78
last_checked: 2026-04-04T17:12:49Z
derived_from:
  - cogops_compiler
---

# Module: belief_compiler

**LOC:** 646

## Entities
- `def extract_skeleton(content: str, source: str) -> str:  # type: ignore` (function)
- `class CodeEntity:` (class)
- `def qualified_name(self) -> str` (function)
- `class ModuleMap:` (class)
- `class CompilationResult:` (class)
- `def extract_entities(content: str, file_path: str) -> List[CodeEntity]` (function)
- `class EntityResolver:` (class)
- `def __init__(self)` (function)
- `def add_entities(self, entities: List[CodeEntity]) -> None` (function)
- `def resolve_dependencies(self) -> None` (function)
- `def dependency_graph(self) -> Dict[str, List[str]]` (function)
- `def get_modules(self) -> Dict[str, List[CodeEntity]]` (function)
- `def generate_module_diagram(modules: Dict[str, List[CodeEntity]]) -> str` (function)
- `class BeliefCompiler:` (class)
- `def __init__(self, vault: VaultManager)` (function)
- `def compile_file(self, file_path: str, content: str) -> Optional[BeliefArtifact]` (function)
