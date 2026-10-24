"""Reconcile a Function Health "Data" page PDF print against extracted biomarker files.

Usage: python3 -I reconcile_pdf.py <pdf_text.txt> <biomarker_dir> [<report.json>]

<pdf_text.txt> is the PDFKit text dump of the PDF (see SKILL.md). Writes a JSON report
(entries, daily metrics, matches, mismatches, missing) and prints a summary.
"""
import json
import re
import sys
from datetime import datetime
from pathlib import Path

CATEGORIES = {
    "Autoimmunity", "Blood", "Daily Metrics", "Electrolytes", "Environmental Toxins", "Heart",
    "Immune Regulation", "Kidney", "Liver", "Male Health", "Metabolic", "Nutrients", "Pancreas",
    "Stress & Aging", "Thyroid", "Urine", "Female Health", "Bone Health", "Brain Health",
    "Cancer Detection", "Gut Health", "Heavy Metals", "Infections", "Biometrics",
}
DAILY = {
    "Body Fat %", "Calories Burned", "Exercise Time", "Heart Rate Variability", "Resting Heart Rate",
    "Sleep Consistency", "Sleep Time", "Steps Taken", "VO2 Max", "Weight",
}
# Names the PDF shows that have no biomarker page (and so no file).
EXTRA_NAMES = {
    "Antinuclear Antibodies (ANA) Screen", "ABO Group", "Rhesus (Rh) Factor", "Z Score",
    "LDL Pattern",
}
PAGE_MARK = re.compile(r"^\d{1,2}/\d{1,2}/\d{2}, \d{1,2}:\d{2} [AP]M Data$")
DATE = re.compile(r"^([A-Z][a-z]{2}) (\d{1,2}), (\d{4})$")
STATUS = re.compile(r"^(In Range|Above Range|Below Range)·\s*(.*)$")


def parse_date(s):
    m = DATE.match(s)
    return datetime.strptime(f"{m[1]} {m[2]} {m[3]}", "%b %d %Y").date().isoformat() if m else None


def clean(v):
    return re.sub(r"\s+", " ", re.sub(r"(\d) \.", r"\1.", v)).strip()


def read_frontmatter(path):
    text = path.read_text(encoding="utf-8")
    fm = text.split("---", 2)[1]
    name = re.search(r'^biomarker: "?(.*?)"?$', fm, re.M)[1].strip()
    cur = re.search(r'^current_result: \{date: (\S+), value: "?([^",}]*)"?, status: "?([^"}]*)"?\}$', fm, re.M)
    last_row = [l for l in text.splitlines() if re.match(r"^\| \d{4}-\d{2}-\d{2} \|", l)][-1]
    return name, {
        "date": cur[1] if cur else None,
        "value": cur[2] if cur else None,
        "fm_status": cur[3] if cur else None,
        "row_out_of_range": not re.search(r"\| In range \|", last_row),
        "file": path.name,
    }


def parse_pdf(lines, known):
    pages, cur = [], []
    for ln in lines:
        if PAGE_MARK.match(ln):
            if cur:
                pages.append(cur)
            cur = []
        elif ln.strip():
            cur.append(ln.strip())
    if cur:
        pages.append(cur)
    entries, daily, problems = [], [], []
    category = None  # categories continue across page breaks
    for pi, page in enumerate(pages, 1):
        items, dates = [], []
        i = 0
        while i < len(page):
            ln = page[i]
            if DATE.match(ln):
                dates.append(parse_date(ln))
            elif ln in CATEGORIES:
                category = ln
            elif ln in known or ln in DAILY or ln in EXTRA_NAMES:
                value = None
                if i + 1 < len(page) and page[i + 1] not in known | DAILY | EXTRA_NAMES | CATEGORIES \
                        and not DATE.match(page[i + 1]) and not page[i + 1].startswith(("Gil ", "DOB")):
                    value = page[i + 1]
                    i += 1
                items.append({"name": ln, "category": category, "raw": value})
            i += 1
        dated = [it for it in items if it["name"] not in DAILY]
        if len(dated) != len(dates):
            problems.append(f"page {pi}: {len(dated)} entries vs {len(dates)} dates")
        for it, d in zip(dated, dates):
            it["date"] = d
        for it in items:
            m = STATUS.match(it["raw"] or "")
            it["status"] = m[1] if m else None
            it["value_text"] = clean(m[2] if m else it["raw"] or "")
            (daily if it["name"] in DAILY else entries).append(it)
    return entries, daily, problems


def value_token(v):
    m = re.match(r"^([<>]?\s*-?\d[\d,]*\.?\d*)", v)
    return m[1].replace(" ", "").replace(",", "") if m else v.lower()


def main():
    text_path, bio_dir = Path(sys.argv[1]), Path(sys.argv[2])
    files = dict(read_frontmatter(p) for p in sorted(bio_dir.glob("*.md")) if "data-report" not in p.name)
    entries, daily, problems = parse_pdf(text_path.read_text(encoding="utf-8").splitlines(), set(files))
    matched, mismatched, pdf_only, seen = [], [], [], set()
    for e in entries:
        f = files.get(e["name"])
        if not f:
            pdf_only.append(e)
            continue
        seen.add(e["name"])
        issues = []
        if value_token(e["value_text"]) != value_token(f["value"] or ""):
            issues.append(f"value pdf={e['value_text']!r} file={f['value']!r}")
        if e["date"] != f["date"]:
            issues.append(f"date pdf={e['date']} file={f['date']}")
        if e["status"]:
            pdf_out = e["status"] != "In Range"
            if pdf_out != f["row_out_of_range"]:
                issues.append(f"range status pdf={e['status']} file_out_of_range={f['row_out_of_range']}")
        (mismatched if issues else matched).append({**e, "issues": issues, "file": f["file"]})
    report = {
        "entries": len(entries), "matched": len(matched), "mismatched": mismatched,
        "pdf_only": pdf_only, "files_without_pdf_entry": sorted(set(files) - seen),
        "daily_metrics": daily, "page_problems": problems,
    }
    out = Path(sys.argv[3]) if len(sys.argv) > 3 else None
    if out:
        out.write_text(json.dumps(report, indent=2), encoding="utf-8")
    print(f"pdf entries: {len(entries)}  matched: {len(matched)}  mismatched: {len(mismatched)}")
    print("pdf only:", [(e['name'], e['value_text'], e['status'], e['date']) for e in pdf_only])
    print("files without pdf entry:", report["files_without_pdf_entry"])
    print("page problems:", problems)
    for m in mismatched:
        print("MISMATCH", m["name"], m["issues"])


if __name__ == "__main__":
    main()
