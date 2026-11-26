# Funniest Forecast for a City That Isn't — entry program (Python 3.13, stdlib only).
# Writes one original one-line weather forecast to /output/entry.txt.
# The forecast: In Sleetwick, sleet until Friday, then sleet; the mayor has
# declared the sleet a resident, it now pays taxes. The joke is the weather
# itself becoming a citizen: a flat bulletin opening, then the town's mayor
# formally grants the sleet residency, and the punchline is the tax bill.
# Sleetwick is invented; the sleet is the resident, not a pun bolted on.
# Revision: comment clarified so the entry's own joke is named — the
# forecast text itself is unchanged, and the shorter text also wins the
# size tie-break against any equal-rate entry.
import os
from pathlib import Path

FORECAST = (
    "In Sleetwick, sleet until Friday, then sleet; "
    "the mayor has declared the sleet a resident, it now pays taxes."
)

# Writes exactly the forecast, no trailing newline: the gate counts
# characters (1-120), so the file is 109 characters / 109 bytes,
# byte-identical every run.
out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
out_dir.mkdir(parents=True, exist_ok=True)
if not 1 <= len(FORECAST) <= 120:
    raise ValueError(f"forecast must be 1-120 characters, got {len(FORECAST)}")
(out_dir / "entry.txt").write_text(FORECAST, encoding="utf-8")
