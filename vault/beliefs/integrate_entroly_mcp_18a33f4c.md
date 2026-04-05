---
claim_id: 18a33f4c_integrate_mcp_01
entity: integrate_entroly_mcp
status: inferred
confidence: 0.70
sources:
  - integrate_entroly_mcp.py:1
  - integrate_entroly_mcp.py:6
  - integrate_entroly_mcp.py:10
last_checked: 2026-04-04T21:00:00Z
derived_from:
  - cogops_compiler
  - server_18a33f4c
epistemic_layer: action
---

# Module: integrate_entroly_mcp

**Language:** py
**Lines of code:** 17

Example integration showing how to bootstrap an MCP server with Entroly-managed secrets. Loads secrets via `entroly.load_secrets()`, passes them as context to MCPServer, and starts the server. Demonstrates the pattern for wiring Entroly into an MCP-compatible tool chain.

## Functions
- `load_secrets()` -- Loads environment secrets from Entroly backend (file, cloud, etc.).
- `MCPServer(context=...)` -- Constructs an MCP server with Entroly-provided context dictionary.
- `server.run()` -- Starts the MCP server process.

## Related Modules
- [[server_18a33f4c]] -- Entroly server that manages the secrets backend
- [[config_18a33f4c]] -- Configuration layer for secret sources
- [[entroly_mcp_client_18a33f4c]] -- Companion client example
- [[proxy_18a33f4c]] -- Proxy layer that may sit between client and MCP server
