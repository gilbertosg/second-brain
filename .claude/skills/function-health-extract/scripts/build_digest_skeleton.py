"""Dump the source text needed to write one category digest page. Writes nothing to the vault.

Usage: python3 -I build_digest_skeleton.py <dated folder> <category | --list> [<out file>]

For each biomarker in the category it prints: name, raw file, result line, tier, and the sections to read.
Tier 2 (every biomarker): Why it matters, Summary.
Tier 1 (out of range now, or tracked in the vault): adds Causes and Follow up.
Out-of-range biomarkers also get Self care, Foods to eat, Foods to limit, and Supplements.
Edit TIER1 and TRACKED below when the tracked set changes.
"""
import importlib.util
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("build_registry", HERE / "build_registry.py")
reg = importlib.util.module_from_spec(spec)
spec.loader.exec_module(reg)

TRACKED = {
    "Testosterone, Free", "Testosterone, Total", "Sex Hormone Binding Globulin (SHBG)", "DHEA Sulfate",
    "Cortisol", "Hemoglobin A1c (HbA1c)", "Apolipoprotein B (ApoB)", "Homocysteine", "Vitamin D",
    "Ferritin", "Thyroid-Stimulating Hormone (TSH)", "Glucose", "Insulin",
}
CORE = ["Why it matters", "Summary"]
TIER1 = ["Causes", "Follow up"]
ACTIONS = ["Self care", "Foods to eat", "Foods to limit", "Supplements"]
LIMITS = {"Causes": 3000, "Follow up": 2500, "Self care": 1800, "Foods to eat": 1500, "Foods to limit": 1500, "Supplements": 2200}


def sections(path):
    text = path.read_text(encoding="utf-8")
    return {p.split("\n", 1)[0][3:].strip(): p for p in re.split(r"\n(?=## )", text) if p.startswith("## ")}


def result_line(b):
    rows = b["rows"]
    if not rows:
        return "no result"
    parts = [f"{reg.SHORT.get(d, d)}: {reg.strip_unit(v, b['unit'])}" for d, v, _, _ in rows]
    return f"{' -> '.join(parts)} {b['unit']} | status {reg.status_of(b)} | Quest {b['quest'] or '-'} | optimal {b['optimal'] or '-'}"


def main():
    folder = Path(sys.argv[1])
    items = [reg.parse(p) for p in sorted(folder.glob("*.md")) if "data-report" not in p.name]
    cats = sorted({b["category"] for b in items})
    if sys.argv[2] == "--list":
        for c in cats:
            print(c, sum(1 for b in items if b["category"] == c))
        return
    cat = sys.argv[2]
    chosen = sorted((b for b in items if b["category"] == cat), key=lambda b: b["name"].lower())
    out = []
    for b in chosen:
        oor = reg.status_of(b) in ("Above", "Below", "Out of range")
        tier = 1 if (oor or b["name"] in TRACKED) else 2
        wanted = CORE + (TIER1 if tier == 1 else []) + (ACTIONS if oor else [])
        secs = sections(folder / b["file"])
        out.append(f"=== {b['name']} | tier {tier}{' | OUT OF RANGE' if oor else ''} | file {b['file']}")
        out.append(f"RESULT: {result_line(b)}")
        for name in wanted:
            body = secs.get(name)
            if body is None:
                out.append(f"--- {name}: (section absent)")
                continue
            body = body.split("\n", 1)[1].strip()
            lim = LIMITS.get(name)
            out.append(f"--- {name}:\n{body[:lim] + ' [...truncated]' if lim and len(body) > lim else body}")
        out.append("")
    text = "\n".join(out)
    if len(sys.argv) > 3:
        Path(sys.argv[3]).write_text(text, encoding="utf-8")
        print(f"{cat}: {len(chosen)} biomarkers, {len(text) // 1024} KB -> {sys.argv[3]}")
    else:
        print(text)


if __name__ == "__main__":
    main()
