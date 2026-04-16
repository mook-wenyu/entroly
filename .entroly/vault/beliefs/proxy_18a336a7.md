---
claim_id: 18a336a70b99f0f80bb186f8
entity: proxy
status: stale
confidence: 0.75
sources:
  - entroly\proxy.py:104
  - entroly\proxy.py:111
  - entroly\proxy.py:119
  - entroly\proxy.py:130
  - entroly\proxy.py:135
last_checked: 2026-04-04T17:12:49Z
derived_from:
  - cogops_compiler
---

# Module: proxy

**LOC:** 1943

## Entities
- `class _CircuitBreaker:` (class)
- `def __init__(self, failure_threshold: int = 3, cooldown_s: float = 30.0)` (function)
- `def allow_request(self) -> bool` (function)
- `def record_success(self) -> None` (function)
- `def record_failure(self) -> None` (function)
- `def state(self) -> str` (function)
- `class _TokenBucket:` (class)
- `def __init__(self, capacity: float, refill_per_second: float)` (function)
- `def try_consume(self, cost: float = 1.0) -> bool` (function)
- `class _WelfordStats:` (class)
- `def __init__(self)` (function)
- `def add(self, x: float) -> None` (function)
- `def variance(self) -> float` (function)
- `def stddev(self) -> float` (function)
- `def to_dict(self) -> dict` (function)
- `class ImplicitFeedbackTracker:` (class)
- `def __init__(self)` (function)
- `def assess_response(self, response_text: str) -> float` (function)
- `def record_assessment(self, reward: float) -> None` (function)
- `def quality_trend(self) -> str` (function)
- `def stats(self) -> Dict[str, Any]` (function)
- `class _CusumEmaDriftDetector:` (class)
- `def __init__(self)` (function)
- `def update(self, reward: float) -> None` (function)
- `def trend(self) -> str` (function)
- `def reset(self) -> None` (function)
- `def to_dict(self) -> Dict[str, Any]` (function)
- `class PromptCompilerProxy:` (class)
- `def __init__(self, engine: Any, config: Optional[ProxyConfig] = None)` (function)
- `async def startup(self) -> None` (function)
- `async def shutdown(self) -> None` (function)
- `async def handle_proxy(self, request: Request) -> StreamingResponse | JSONResponse` (function)
- `async def event_generator()` (function)
