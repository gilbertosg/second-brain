"""Split the extractor's JSON bundle into one Markdown file per biomarker.

Usage: python3 -I split_bundle.py <function-health-biomarkers.json> <output dir>
Existing files are never overwritten; identical and differing ones are reported.
"""
import json
import sys
from pathlib import Path

bundle_path, out_dir = Path(sys.argv[1]), Path(sys.argv[2])
bundle = json.loads(bundle_path.read_text(encoding="utf-8"))
out_dir.mkdir(parents=True, exist_ok=True)

written, skipped_same, differs = [], [], []
for slug, md in sorted(bundle.items()):
    target = out_dir / f"{slug}.md"
    if target.exists():
        old = target.read_text(encoding="utf-8")
        (skipped_same if old == md else differs).append(slug)
        continue
    target.write_text(md.rstrip("\n") + "\n", encoding="utf-8")
    written.append(slug)

print(f"bundle entries: {len(bundle)}")
print(f"written: {len(written)}")
print(f"existing, identical: {len(skipped_same)} {skipped_same}")
print(f"existing, different (not overwritten): {len(differs)} {differs}")
