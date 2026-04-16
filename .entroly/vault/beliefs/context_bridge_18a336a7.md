---
claim_id: 18a336a708f055900907eb90
entity: context_bridge
status: stale
confidence: 0.75
sources:
  - entroly\context_bridge.py:52
  - entroly\context_bridge.py:67
  - entroly\context_bridge.py:76
  - entroly\context_bridge.py:86
  - entroly\context_bridge.py:147
last_checked: 2026-04-04T17:12:49Z
derived_from:
  - cogops_compiler
---

# Module: context_bridge

**LOC:** 2031

## Entities
- `class SessionContext:` (class)
- `class AgentBudget:` (class)
- `class HeartbeatResult:` (class)
- `class NkbeAllocator:` (class)
- `def allocate(self) -> Dict[str, int]` (function)
- `def reinforce(self, outcomes: Dict[str, float]) -> None` (function)
- `class _AgentState:` (class)
- `class CognitiveBus:` (class)
- `def __init__(self, novelty_threshold: float = 0.3, alpha: float = 0.1)` (function)
- `def subscribe(self, agent_name: str, event_types: Optional[List[str]] = None) -> None` (function)
- `def drain(self, agent_name: str, limit: int = 10) -> List[Dict[str, Any]]` (function)
- `def stats(self) -> Dict[str, Any]` (function)
- `class _BusEvent:` (class)
- `class _Subscriber:` (class)
- `class _RateCell:` (class)
- `def __init__(self, alpha: float = 0.1)` (function)
- `def observe(self, tick: int) -> None` (function)
- `def kl_divergence(self) -> float` (function)
- `def is_spike(self) -> bool` (function)
- `class AgentContext:` (class)
- `def ingest_workspace(self) -> Dict[str, Any]` (function)
- `def record_outcome(self, success: bool) -> None` (function)
- `def drain_events(self, agent_name: str, limit: int = 10) -> List[Dict[str, Any]]` (function)
- `def get_stats(self) -> Dict[str, Any]` (function)
- `class LodTier:` (class)
- `class AgentState:` (class)
- `class LODManager:` (class)
- `def __init__(self)` (function)
- `def unregister(self, agent_id: str) -> None` (function)
- `def update_load(self, agent_id: str, load_factor: float) -> Optional[str]` (function)
- `def tick(self) -> List[str]` (function)
- `def get_active_agents(self) -> List[str]` (function)
- `def get_budget_weights(self) -> Dict[str, float]` (function)
- `def stats(self) -> Dict[str, Any]` (function)
- `class SubagentOrchestrator:` (class)
- `def can_spawn(self, parent_id: str) -> Tuple[bool, str]` (function)
- `def despawn(self, child_id: str) -> None` (function)
- `def get_tree(self, root_id: str) -> Dict[str, Any]` (function)
- `def stats(self) -> Dict[str, Any]` (function)
- `class CronSessionManager:` (class)
- `class CronJob:` (class)
- `def unschedule(self, agent_id: str) -> None` (function)
- `def get_due_jobs(self, current_time: Optional[float] = None) -> List["CronSessionManager.CronJob"]` (function)
- `def stats(self) -> Dict[str, Any]` (function)
- `class MemoryBridge:` (class)
- `def __init__(self, bus: CognitiveBus)` (function)
- `def active(self) -> bool` (function)
- `def bridge_events(self) -> int` (function)
- `def tick(self) -> None` (function)
- `def stats(self) -> Dict[str, Any]` (function)
- `class CompressionLevel:` (class)
- `class HCCFragment:` (class)
- `class HCCEngine:` (class)
- `def __init__(self)` (function)
- `def optimize(self, token_budget: int) -> List[HCCFragment]` (function)
- `def get_content(self, frag: HCCFragment) -> str` (function)
- `class AutoTune:` (class)
- `def update(self, outcome: float, metrics: Dict[str, float]) -> Dict[str, float]` (function)
- `def get_weights(self) -> Dict[str, float]` (function)
- `def stats(self) -> Dict[str, Any]` (function)
- `class MultiAgentContext(AgentContext):` (class)
- `def __init__(self, **kwargs)` (function)
- `def despawn_subagent(self, child_id: str) -> None` (function)
- `def get_agent_tree(self, root_id: str = "main") -> Dict[str, Any]` (function)
- `def unschedule_cron(self, agent_id: str) -> None` (function)
- `def get_due_cron_jobs(self) -> list` (function)
- `def run_cron_job(self, job) -> SessionContext` (function)
- `def bridge_memories(self) -> int` (function)
- `def update_agent_load(self, agent_id: str, load: float) -> Optional[str]` (function)
- `def tick(self) -> None` (function)
- `def get_stats(self) -> Dict[str, Any]` (function)
