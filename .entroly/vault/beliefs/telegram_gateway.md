---
claim_id: c82d365a-6754-485a-99eb-4b7adf19eb0a
entity: telegram_gateway
status: inferred
confidence: 0.75
sources:
  - entroly/integrations/telegram_gateway.py:51
  - entroly/integrations/telegram_gateway.py:52
  - entroly/integrations/telegram_gateway.py:74
  - entroly/integrations/telegram_gateway.py:78
  - entroly/integrations/telegram_gateway.py:90
  - entroly/integrations/telegram_gateway.py:109
  - entroly/integrations/telegram_gateway.py:48
last_checked: 2026-04-14T04:12:29.465025+00:00
derived_from:
  - belief_compiler
  - sast
---

# Module: telegram_gateway

**Language:** python
**Lines of code:** 294

## Types
- `class TelegramGateway()`

## Functions
- `def __init__(
        self,
        token: str,
        chat_id: str | int,
        vault_path: str | Path = ".entroly/vault",
        poll_interval_s: float = 30.0,
    )`
- `def attach(self, daemon: Any) -> None` — Wire a running EvolutionDaemon so we can surface its events.
- `def start(self) -> None`
- `def stop(self) -> None`
- `def send(self, text: str) -> dict[str, Any]`

## Dependencies
- `__future__`
- `json`
- `logging`
- `os`
- `pathlib`
- `threading`
- `time`
- `typing`
- `urllib.parse`
- `urllib.request`
