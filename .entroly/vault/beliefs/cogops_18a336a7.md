---
claim_id: 18a336a70cfa55140d11eb14
entity: cogops
status: inferred
confidence: 0.75
sources:
  - entroly-core\src\cogops.rs:26
  - entroly-core\src\cogops.rs:43
  - entroly-core\src\cogops.rs:63
  - entroly-core\src\cogops.rs:72
  - entroly-core\src\cogops.rs:84
last_checked: 2026-04-04T17:12:49Z
derived_from:
  - cogops_compiler
---

# Module: cogops

**LOC:** 1603

## Entities
- `pub enum EpistemicIntent` (enum)
- `fn as_str(&self) -> &'static str` (function)
- `pub enum EpistemicFlow` (enum)
- `fn as_str(&self) -> &'static str` (function)
- `pub enum RiskLevel` (enum)
- `fn as_str(&self) -> &'static str` (function)
- `pub struct CodeEntity` (struct)
- `pub struct BeliefArtifact` (struct)
- `pub struct RoutingDecision` (struct)
- `pub struct Contradiction` (struct)
- `pub struct ChangeSet` (struct)
- `pub struct ReviewFinding` (struct)
- `pub fn classify_intent(query: &str) -> EpistemicIntent` (function)
- `pub fn assess_risk(query: &str) -> RiskLevel` (function)
- `pub fn extract_entities(content: &str, file_path: &str) -> Vec<CodeEntity>` (function)
- `fn extract_python_entities(content: &str, file_path: &str) -> Vec<CodeEntity>` (function)
- `fn extract_rust_entities(content: &str, file_path: &str) -> Vec<CodeEntity>` (function)
- `fn extract_js_entities(content: &str, file_path: &str) -> Vec<CodeEntity>` (function)
- `fn get_next_docstring(lines: &[&str], after: usize) -> String` (function)
- `fn get_rust_doc(lines: &[&str], before: usize) -> String` (function)
- `fn ensure_vault(vault_path: &Path)` (function)
- `fn generate_claim_id() -> String` (function)
- `fn write_belief_artifact(vault_path: &Path, artifact: &BeliefArtifact) -> Result<String, String>` (function)
- `fn read_all_beliefs(vault_path: &Path) -> Vec<BeliefArtifact>` (function)
- `fn parse_belief_frontmatter(content: &str) -> Option<BeliefArtifact>` (function)
- `pub fn detect_contradictions(beliefs: &[BeliefArtifact]) -> Vec<Contradiction>` (function)
- `pub fn compute_blast_radius(beliefs: &[BeliefArtifact], changed_files: &[&str]) -> (Vec<String>, Vec<String>, &'static str)` (function)
- `pub fn parse_diff(diff_text: &str, commit_msg: &str) -> ChangeSet` (function)
- `pub fn review_diff(diff_text: &str) -> Vec<ReviewFinding>` (function)
- `pub fn select_flow(` (function)
- `pub struct CogOpsEngine` (struct)
- `pub fn new(vault_path: String, miss_threshold: u32, freshness_hours: f64, min_confidence: f64) -> Self` (function)
- `pub fn classify_intent(&self, query: &str) -> String` (function)
- `pub fn route(&mut self, query: &str, is_event: bool, event_type: &str) -> PyResult<PyObject>` (function)
- `pub fn extract_entities(&self, content: &str, file_path: &str) -> PyResult<PyObject>` (function)
- `pub fn compile_beliefs(&mut self, directory: &str, max_files: usize) -> PyResult<PyObject>` (function)
- `pub fn verify_beliefs(&self) -> PyResult<PyObject>` (function)
- `pub fn blast_radius(&self, changed_files: Vec<String>) -> PyResult<PyObject>` (function)
- `pub fn process_change(&self, diff_text: &str, commit_msg: &str, pr_title: &str) -> PyResult<PyObject>` (function)
- `pub fn write_belief(&self, entity: &str, title: &str, body: &str,` (function)
- `pub fn vault_status(&self) -> PyResult<PyObject>` (function)
- `pub fn create_skill(&self, entity_key: &str, failing_queries: Vec<String>) -> PyResult<PyObject>` (function)
- `pub fn list_skills(&self) -> PyResult<PyObject>` (function)
- `pub fn coverage_gaps(&self, directory: &str) -> PyResult<PyObject>` (function)
- `pub fn refresh_beliefs(&self, changed_files: Vec<String>) -> PyResult<PyObject>` (function)
- `pub fn benchmark_skill(&self, skill_id: &str) -> PyResult<PyObject>` (function)
- `pub fn promote_skill(&self, skill_id: &str) -> PyResult<PyObject>` (function)
- `pub fn execute_flow(&mut self, query: &str, diff_text: &str, is_event: bool, event_type: &str) -> PyResult<PyObject>` (function)
- `fn extract_entity_key(query: &str) -> String` (function)
- `fn chrono_iso() -> String` (function)
- `fn days_to_ymd(mut days: u64) -> (u64, u64, u64)` (function)
- `fn is_leap(y: u64) -> bool` (function)
- `fn extract_fm_value(content: &str, key: &str) -> Option<String>` (function)
- `fn collect_source_files(dir: &Path, skip: &HashSet<&str>, exts: &HashSet<&str>, out: &mut Vec<PathBuf>, max: usize)` (function)
