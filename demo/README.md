# Entroly Demo Tapes

Reproducible terminal recordings powered by [VHS](https://github.com/charmbracelet/vhs).
Every GIF in the README hero row is generated from a `.tape` file in this
directory — no Photoshop, no After Effects, no faked output.

## Tapes

| Tape | What it shows | Render |
|---|---|---|
| [dashboard.tape](dashboard.tape) | `entroly go` auto-detect + proxy + dashboard URL | `vhs demo/dashboard.tape` |
| [bench.tape](bench.tape) | `bench/trust_bench.py` + `tests/verify_claims.py` going green | `vhs demo/bench.tape` |
| [../demo.tape](../demo.tape) | `entroly wrap claude` end-to-end (legacy location) | `vhs demo.tape` |

## Recording requirements

```bash
# macOS
brew install vhs

# Linux / Windows
go install github.com/charmbracelet/vhs@latest

# Once you have vhs:
vhs demo/dashboard.tape
vhs demo/bench.tape
```

Each tape produces both `.gif` (for the README) and `.mp4` (for tweets).

## Editing rules

- **No fictional metrics.** If a tape shows a number, it must be the number
  the engine actually produced on the recorder's machine. If you re-record
  on a different repo and the savings shift, update the README to match.
- **Keep tapes < 30 seconds.** Anything longer doesn't loop well on social.
- **Real repos only.** Don't record against `examples/` — pick something
  recognizable (httpie, fastapi, your own monorepo) and check the path
  is updated at the top of the tape.
- **Re-record on every major release.** Outdated GIFs are worse than no GIFs.

## When something looks off in the GIF

VHS captures real terminal output. If a number in the recording doesn't
match the README:

1. The README is wrong → fix the README.
2. The engine regressed → fix the engine.
3. You ran on a different repo → update the README to say "on the X repo"
   or re-record on the canonical one.

Never edit the GIF to match a marketing claim. The whole point of these
tapes is that any visitor can re-run them and see the same output.
