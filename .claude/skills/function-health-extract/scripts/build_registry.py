"""Build the L1 Function Health registry page from a dated folder of extracted biomarker files.

Usage: python3 -I build_registry.py <dated folder> <output .md> [--vault-root <dir>]

Reads each biomarker file's frontmatter and results table (no network, no hand-typing) and writes
one row per biomarker: category, previous and latest value, change, status, ranges, source link.
"""
import re
import sys
from pathlib import Path

ROW = re.compile(r"^\| (\d{4}-\d{2}-\d{2}) \| (.*?) \| (.*?) \| (.*?) \|$")
SHORT = {"2026-05-19": "May 19", "2026-05-20": "May 20", "2026-10-02": "Oct 2"}


def fm_get(fm, key):
    m = re.search(rf"^{key}: (.*)$", fm, re.M)
    return m[1].strip().strip('"') if m else ""


def num(v):
    m = re.match(r"^[<>]?\s*(-?\d[\d,]*\.?\d*)", v)
    return float(m[1].replace(",", "")) if m and not v.startswith(("<", ">")) else None


def parse(path):
    text = path.read_text(encoding="utf-8")
    fm = text.split("---", 2)[1]
    rows = [ROW.match(l) for l in text.splitlines()]
    rows = [(m[1], m[2].strip(), m[3].strip(), m[4].strip()) for m in rows if m]
    return {
        "name": fm_get(fm, "biomarker").strip(),
        "category": fm_get(fm, "category"),
        "unit": fm_get(fm, "unit"),
        "fm_status": re.search(r'status: "?([^"}]*)"?\}', fm_get(fm, "current_result") + "}")[1]
        if "status:" in fm_get(fm, "current_result") else "",
        "quest": fm_get(fm, "quest_reference_range"),
        "optimal": fm_get(fm, "function_optimal_range"),
        "rows": rows,
        "file": path.name,
    }


def strip_unit(value, unit):
    v = value
    if unit and v.endswith(unit):
        v = v[: -len(unit)].strip()
    return v


def status_of(b):
    if not b["rows"]:
        return "—"
    state = b["rows"][-1][2]
    if state.startswith("In range"):
        return "In range"
    s = b["fm_status"].lower()
    if s.startswith("above"):
        return "Above"
    if s.startswith("below"):
        return "Below"
    return "Out of range"


def main():
    folder, out = Path(sys.argv[1]).resolve(), Path(sys.argv[2]).resolve()
    root = (Path(sys.argv[sys.argv.index("--vault-root") + 1]) if "--vault-root" in sys.argv else out.parent.parent).resolve()
    items = [parse(p) for p in sorted(folder.glob("*.md")) if "data-report" not in p.name]
    items.sort(key=lambda b: (b["category"], b["name"].lower()))
    dates = sorted({d for b in items for d, *_ in b["rows"]})
    latest = max(d for d in dates)
    rel = Path("..") / folder.relative_to(root)
    n_two = sum(1 for b in items if len(b["rows"]) >= 2)
    out_now = [b for b in items if status_of(b) in ("Above", "Below", "Out of range")]
    lines = [
        "---",
        'title: "L1 — Function Health Biomarker Registry"',
        "type: health-data",
        "pillar_id: L1",
        "owner: Gilberto Silva Gonzalez",
        "created: 2026-10-24",
        "last_updated: 2026-10-24",
        "status: active",
        "tags: [l1, blood, biomarkers, function-health, registry, generated]",
        f"sources:\n  - 00-Raw_Sources/L1_Health/function-health/{folder.name}/",
        f"draws: [{', '.join(dates)}]",
        f"biomarkers: {len(items)}",
        "generated_by: .claude/skills/function-health-extract/scripts/build_registry.py",
        "related: [L1-Health/blood-analysis-function-oct2026, L1-Health/blood-analysis-function-may2026, L1-Health/blood-analysis]",
        "---",
        "",
        "# L1 — Function Health Biomarker Registry",
        "",
        f"Every biomarker Function Health returned for the draws on {', '.join(SHORT.get(d, d) for d in dates)} (2026). "
        "Generated from the extracted raw files; do not edit by hand. Regenerate with "
        "`build_registry.py` after each new extraction.",
        "",
        f"- **Biomarkers:** {len(items)} ({n_two} with two results, {len(items) - n_two} with one)",
        f"- **Out of range at the latest result:** {len(out_now)}",
        "- **Status** comes from the latest result's in-range flag. **Quest range** is the lab reference range; "
        "**Function optimal** is Function Health's tighter range (blank or `-` where none exists).",
        "- Narrative analysis: [[L1-Health/blood-analysis-function-oct2026]] (Oct 2, 2026) and "
        "[[L1-Health/blood-analysis-function-may2026]] (May 19, 2026).",
        "",
    ]
    cat = None
    for b in items:
        if b["category"] != cat:
            cat = b["category"]
            lines += [
                f"## {cat}", "",
                "| Biomarker | Unit | Previous | Latest | Change | Status | Quest range | Function optimal | Source |",
                "|---|---|---|---|---|---|---|---|---|",
            ]
        rows = b["rows"]
        cur = rows[-1] if rows else None
        prev = rows[-2] if len(rows) > 1 else None
        fmt = lambda r: f"{strip_unit(r[1], b['unit'])} ({SHORT.get(r[0], r[0])})" if r else "—"
        change = "—"
        if prev:
            a, c = num(strip_unit(prev[1], b["unit"])), num(strip_unit(cur[1], b["unit"]))
            if a is not None and c is not None:
                pct = (c - a) / a * 100 if a else None
                change = f"{c - a:+g}" + (f" ({pct:+.0f}%)" if pct is not None else "")
        optimal = b["optimal"] if b["optimal"] not in ("-", "") else "—"
        lines.append(
            f"| {b['name']} | {b['unit']} | {fmt(prev)} | {fmt(cur)} | {change} | {status_of(b)} | "
            f"{b['quest'] or '—'} | {optimal} | [file]({rel / b['file']}) |"
        )
        nxt = items[items.index(b) + 1] if items.index(b) + 1 < len(items) else None
        if not nxt or nxt["category"] != cat:
            lines.append("")
    out.write_text("\n".join(lines).rstrip("\n") + "\n", encoding="utf-8")
    print(f"wrote {out} with {len(items)} rows; out of range: {[b['name'] for b in out_now]}")


if __name__ == "__main__":
    main()
