"""Verify the category digest pages against the extracted biomarker files.

Usage: python3 -I check_digests.py <dated folder> <L1-Health dir>

Checks: (1) each biomarker has exactly one entry (a `## <name>` heading) across the biomarker-digest-*.md pages;
(2) every `[raw file](...)` link resolves and points at that biomarker's file; (3) no run of 12 or more
consecutive words is shared with the raw file (copy check); (4) Tier 1 entries carry Causes and Follow-up when the raw file has those sections; Tier 2 entries carry neither;
only out-of-range entries carry Levers.
"""
import importlib.util
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("build_digest_skeleton", HERE / "build_digest_skeleton.py")
sk = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sk)
reg = sk.reg
RUN = 12


def words(text):
    return re.findall(r"[a-z0-9]+(?:['’-][a-z0-9]+)*", text.lower())


def longest_shared_run(a, b):
    """Longest run of consecutive words appearing in both lists (a = digest entry, b = raw file)."""
    index = {}
    for i in range(len(b) - 3):
        index.setdefault(tuple(b[i:i + 4]), []).append(i)
    best = 0
    for i in range(len(a) - 3):
        for j in index.get(tuple(a[i:i + 4]), ()):
            k = 4
            while i + k < len(a) and j + k < len(b) and a[i + k] == b[j + k]:
                k += 1
            best = max(best, k)
    return best


def main():
    folder, l1 = Path(sys.argv[1]).resolve(), Path(sys.argv[2]).resolve()
    items = {b["name"]: b for b in (reg.parse(p) for p in sorted(folder.glob("*.md")) if "data-report" not in p.name)}
    entries = {}
    problems = []
    for page in sorted(l1.glob("biomarker-digest-*.md")):
        text = page.read_text(encoding="utf-8")
        body = text.split("---", 2)[2]
        for chunk in re.split(r"\n(?=## )", body):
            m = re.match(r"## (.+?)(?: — .*)?\n", chunk)
            if not m or m[1] not in items:
                continue
            name = m[1]
            if name in entries:
                problems.append(f"duplicate entry: {name}")
            entries[name] = (page.name, chunk)
    for name, b in items.items():
        if name not in entries:
            problems.append(f"missing entry: {name}")
            continue
        page, chunk = entries[name]
        links = re.findall(r"\[raw file\]\(([^)]+)\)", chunk)
        if len(links) != 1:
            problems.append(f"{name}: expected 1 raw-file link, found {len(links)}")
        else:
            target = (l1 / links[0]).resolve()
            if not target.exists() or target.name != b["file"]:
                problems.append(f"{name}: raw-file link wrong or unresolved: {links[0]}")
        raw = (folder / b["file"]).read_text(encoding="utf-8")
        run = longest_shared_run(words(re.sub(r"\[raw file\]\([^)]*\)", "", chunk)), words(raw))
        if run >= RUN:
            problems.append(f"{name}: shares a {run}-word run with the raw file")
        oor = reg.status_of(b) in ("Above", "Below", "Out of range")
        tier1 = oor or name in sk.TRACKED
        has = lambda label: bool(re.search(rf"\*\*{label}", chunk))
        if tier1 and "\n## Causes" in raw and not has("Causes"):
            problems.append(f"{name}: Tier 1 entry lacks Causes")
        if tier1 and "\n## Follow up" in raw and not has("Follow-up"):
            problems.append(f"{name}: Tier 1 entry lacks Follow-up")
        if not tier1 and (has("Causes") or has("Follow-up")):
            problems.append(f"{name}: Tier 2 entry carries Causes or Follow-up")
        if has("Levers") != oor:
            problems.append(f"{name}: Levers line {'missing' if oor else 'present'} (out of range: {oor})")
    print(f"entries: {len(entries)} of {len(items)} biomarkers across {len(set(p for p, _ in entries.values()))} pages")
    print("problems:" if problems else "no problems")
    for p in problems:
        print("  -", p)


if __name__ == "__main__":
    main()
