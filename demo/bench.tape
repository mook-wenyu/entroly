# Trust benchmark — proves all 16 claims, deterministic, no API keys, < 2s.
#
# Render: `vhs demo/bench.tape`
# Output: demo/bench.gif (and bench.mp4)
#
# This is the "trust me, run this on your own machine" GIF. Pair with the
# verify_claims.py table in the README.

Output demo/bench.gif
Output demo/bench.mp4

Require entroly
Require python

Set FontSize 16
Set Width 1400
Set Height 900
Set Padding 40
Set Theme "TokyoNight"
Set WindowBar Colorful
Set Framerate 30

# Use the entroly source tree itself — it's checked into the repo so the
# tape is fully reproducible from a fresh clone.
Type "cd ~/entroly"
Enter
Sleep 800ms

Type "clear"
Enter
Sleep 500ms

# Run the trust benchmark — 5 independent claims, < 2 seconds, no network.
Type "python bench/trust_bench.py"
Sleep 800ms
Enter

# Long enough to read the PASS lines for compression / classifier /
# hook coverage / router logic / determinism.
Sleep 8s

# Then run verify_claims against the entroly repo itself — the second
# layer of proof: 16 README claims verified against the live engine.
Type "clear"
Enter
Sleep 500ms

Type "python -m tests.verify_claims"
Sleep 800ms
Enter

# Hold long enough for the [PASS] rows to scroll past and the
# "16/16 claims verified" summary to be readable.
Sleep 12s
