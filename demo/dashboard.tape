# entroly go — auto-detect repo, start proxy + dashboard, show indexing speed.
#
# Render: `vhs demo/dashboard.tape`
# Output: demo/dashboard.gif (and dashboard.mp4)
#
# This tape captures the *terminal* side of `entroly go`. Pair the resulting
# GIF with a static screenshot of the auto-opened browser dashboard
# (http://localhost:9378) for the README hero.

Output demo/dashboard.gif
Output demo/dashboard.mp4

Require entroly

Set FontSize 16
Set Width 1400
Set Height 800
Set Padding 40
Set Theme "TokyoNight"
Set WindowBar Colorful
Set Framerate 30

# Drop into a real, mid-size repo. The path below assumes you have a
# fresh clone of a representative project (httpie, fastapi, langchain,
# or your own monorepo). For the canonical recording we use:
#   git clone --depth=1 https://github.com/encode/httpie ~/repos/httpie
Type "cd ~/repos/httpie"
Enter
Sleep 1s

Type "clear"
Enter
Sleep 500ms

# The hero command — this is what we want viewers to remember.
Type "entroly go"
Sleep 800ms
Enter

# Indexing finishes in well under a second on most repos. Hold long enough
# for the "Auto-indexed N files in X.Xs" line to be readable, then for the
# Dashboard URL to appear.
Sleep 6s

# Show that the proxy is live and ready to receive traffic.
Type "curl -s http://localhost:9377/health | head -1"
Enter
Sleep 2s

# Show the dashboard URL is responding.
Type "curl -s -o /dev/null -w 'dashboard: %{http_code}\\n' http://localhost:9378"
Enter
Sleep 2s

# Stop the daemon cleanly so the recording ends in a known state.
Type "curl -s -X POST http://localhost:9378/api/control/stop > /dev/null && echo 'stopped'"
Enter
Sleep 2s
