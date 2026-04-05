---
claim_id: 18a33f4c_mcp_client_01
entity: entroly_mcp_client
status: inferred
confidence: 0.70
sources:
  - entroly_mcp_client.py:1
  - entroly_mcp_client.py:8
  - entroly_mcp_client.py:17
last_checked: 2026-04-04T21:00:00Z
derived_from:
  - cogops_compiler
  - server_18a33f4c
epistemic_layer: action
---

# Module: entroly_mcp_client

**Language:** py
**Lines of code:** 25

Example Python client demonstrating how to interact with the Entroly MCP server over HTTP using httpx. Shows the two primary API calls: remember_fragment (ingest code) and optimize_context (retrieve optimized context for a query).

## Functions
- `remember_fragment` call -- POSTs a fragment (content, source, token_count) to `/remember_fragment` endpoint.
- `optimize_context` call -- POSTs a query with token_budget to `/optimize_context` endpoint.

## Related Modules
- [[server_18a33f4c]] -- The Entroly MCP server this client connects to
- [[fragment_18a33f4c]] -- Fragment schema used in remember_fragment payload
- [[knapsack_18a33f4c]] -- Optimization engine behind optimize_context
- [[integrate_entroly_mcp_18a33f4c]] -- Companion integration example
