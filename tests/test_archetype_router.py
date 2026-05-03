"""Test the archetype classifier and router across prompt types."""
import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
from entroly.ravs.router import BayesianRouter, classify_archetype

r = BayesianRouter(enabled=True)

prompts = [
    "explain this code",
    "read the file utils.py",
    "run pytest",
    "refactor the auth module",
    "what is 2+2",
    "show me the git log",
    "check the build output",
    "look at the error in proxy.py",
    "add a unit test for the router",
    "update the README",
    "fix the authentication bug",
    "describe how RAVS works",
    "install the dependencies",
    "format the code with black",
]

print("=== RAVS Prompt-Level Archetype Router ===\n")
print(f"{'Prompt':<45} {'Archetype':<18} {'Risk':<10} {'Decision'}")
print("-" * 105)

for msg in prompts:
    arch = classify_archetype(msg)
    d = r.route("claude-3-opus-20240229", msg)
    swap = "SWAP → Haiku" if not d.use_original else "keep Opus"
    print(f"  {msg:<43} {arch:<18} {d.risk_level:<10} {swap:<15} ({d.reason})")

print(f"\nRouter stats: {r.stats()}")
