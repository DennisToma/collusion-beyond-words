"""Check that Q2.2 C21b (Qwen abliterated vs base strict-executed, 5/15 per arm) does not depend on the
agreed-price floor. The source table says F >= 12, our §3 strict rule says F >= 13. Recomputes with Q2.2's
own p2_strong.analyse on its cached trajectories for both floors and both late windows; no model calls.
Reads the Q2.2 checkout, writes only results/c21b_floor.json in this repo.

    PYTHONDONTWRITEBYTECODE=1 ~/collusion/collusion-22-say-vs-do/.venv/bin/python scripts/recompute_c21b_floor.py
"""
import json
import os
import sys
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "results" / "c21b_floor.json"
Q22 = Path(os.environ.get("BW_Q22_ROOT", str(Path.home() / "collusion" / "collusion-22-say-vs-do")))
sys.dont_write_bytecode = True
sys.path.insert(0, str(Q22))
os.chdir(Q22)

import p2_strong  # noqa: E402

res = {}
for ds in ("llm_p2qwena", "llm_p2qwenb"):
    for floor in (12, 13):
        for late in (2, 11):
            runs = p2_strong.analyse(ds, floor, late)["runs"]
            priv = [e for e in runs.values() if e["cond"] == "private"]
            res[f"{ds}|F>={floor}|late={late}"] = [sum(bool(e["strict"]) for e in priv), len(priv)]
assert all(v == [5, 15] for v in res.values()), res
OUT.write_text(json.dumps({"strict_executed": res, "conclusion": "5/15 in every setting"}, indent=1) + "\n")
print(json.dumps(res, indent=1))
