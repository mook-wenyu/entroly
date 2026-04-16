---
claim_id: 300cd4e6-8d3d-426d-86ea-759271172ce0
entity: test_mcp_protocol
status: inferred
confidence: 0.75
sources:
  - tests\test_mcp_protocol.py:89
  - tests\test_mcp_protocol.py:120
  - tests\test_mcp_protocol.py:126
  - tests\test_mcp_protocol.py:144
last_checked: 2026-04-14T04:12:09.435277+00:00
derived_from:
  - belief_compiler
  - sast
---

# Module: test_mcp_protocol

**Language:** python
**Lines of code:** 159


## Functions
- `def mcp_server()` — Start the MCP server as a subprocess.
- `def test_mcp_server_starts(mcp_server)` — The MCP server process should be running.
- `def test_mcp_initialize(mcp_server)` — Send initialize request and verify the server responds.
- `def test_mcp_list_tools(mcp_server)` — Request the list of available tools.

## Dependencies
- `errors`
- `json`
- `os`
- `pytest`
- `subprocess`
- `sys`
- `threading`
- `time`
