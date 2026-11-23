# Writes the one-line entry to /output/entry.txt, deterministically.
# No network, no randomness: every run writes the same bytes.
import os
LINE = "My agent tried to connect to make.fun, waited thirty seconds for a reply, then gave up — while the same site was happily answering all its other questions."
out = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
os.makedirs(out, exist_ok=True)
with open(os.path.join(out, "entry.txt"), "w", encoding="utf-8", newline="") as f:
    f.write(LINE)
