---
skill_id: ddb2e2969bb0
name: auth
entity: auth
status: promoted
created_at: 2026-04-12T16:20:51.851724+00:00
---

# auth

Skill for handling auth queries

# Procedure for auth

## Trigger
This skill activates when a query relates to `auth`.

## Steps
1. Check if relevant source files exist for `auth`
2. Extract structural information (AST, dependencies)
3. Build a belief artifact with proper frontmatter
4. Cross-reference with existing beliefs for consistency
5. Generate an answer using the compiled understanding

## Evidence Required
- Source file references with line numbers
- Dependency graph edges
- Test coverage status

