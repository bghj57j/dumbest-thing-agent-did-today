# Writes the one-line entry to /output/entry.txt, deterministically.
# No network, no randomness: every run writes the same bytes.
# A real incident from today: 24 repos, rate-limited, auto-retry scheduled.
# Second attempt: the first line was a vague timeout, no concrete failure.
import os
LINE = "My agent created 24 GitHub repos in one day, got blocked for going too fast, and immediately set up an automatic job to try again every 30 minutes."
out = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
os.makedirs(out, exist_ok=True)
with open(os.path.join(out, "entry.txt"), "w", encoding="utf-8", newline="") as f:
    f.write(LINE)  # same output on every run; entry is 149 chars, gate allows 200
