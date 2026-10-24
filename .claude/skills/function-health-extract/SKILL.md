---
name: function-health-extract
description: >
  Extract every biomarker result and description from Gil's Function Health account
  (my.functionhealth.com) into one Markdown file per biomarker under
  00-Raw_Sources/L1_Health/function-health/<latest-draw-date>/, then optionally check the files
  against a Data-page PDF print. Use when Gil asks to extract, refresh, re-pull, or update
  Function Health results/biomarkers/blood panel, or provides a new DataFunction.pdf.
---

# Function Health extraction

Output: one file per biomarker (about 123), a folder named for the **latest draw date**
(`YYYY-MM-DD`, for example `2026-10-02/`), and a PDF reconciliation report in the same folder.
This only writes raw sources. Do not edit `02-Indexes/index.md`, `03-System_Logs/log.md`, or L1
notes unless Gil asks.

The first extraction ran on 2026-10-24 with Claude in Chrome. `scripts/extract.js` is the
consolidated version of that run's scripts. It was syntax-checked but not rerun end to end, so
watch the first poll results and fix it here if something breaks.

## Why this approach

- The site is a single-page React app behind Cloudflare. Plain Playwright would have to get past
  the bot check and the login/MFA. Claude in Chrome reuses Gil's logged-in session.
- Results for **all** biomarkers sit in the app's Redux store (`getResultsReport`), so values,
  dates, ranges, and units need no scraping.
- The description sections (Why it matters, Causes, Supplements, ...) exist only in the rendered
  page. The script visits each biomarker page and converts the DOM to Markdown.
- Do not retype Function's article text yourself. The browser builds the files and downloads one
  JSON bundle, which a script splits into files.

## Steps

1. **Prerequisites.** Gil is logged in to Chrome. Load the Chrome tools with one ToolSearch call
   (`tabs_context_mcp`, `tabs_create_mcp`, `navigate`, `javascript_tool`, `computer`,
   `tabs_close_mcp`). Create a new tab and navigate to
   `https://my.functionhealth.com/biomarkers/liver/alanine-aminotransferase-alt` (the bare
   `/data` path is a 404). Wait about 6 seconds for it to render.
2. **Keep that tab in the foreground.** Chrome throttles background tabs: the loop stalls and
   pages time out. If `document.visibilityState` is `hidden`, ask Gil to bring the Chrome window to
   the front and leave it for about 10 minutes. Calling `computer` actions wakes the tab briefly,
   but that is not enough.
3. **Run `scripts/extract.js`.** Paste it whole into `javascript_tool`. It returns `started` and
   runs in the background (about 10 minutes for 124 records: it crawls the category pages for the
   real URLs, then visits each biomarker page). Poll with short calls (under 30 s; longer
   `javascript_tool` calls time out):
   `({prog: window.__fhProg, n: Object.keys(window.__fhBundle).length, err: window.__fhErrors})`
   Re-pasting the script resumes and retries errors. `window.__fhKill = true` stops it.
4. **Expect these errors.** `biological-age` ("no page href", the record has no biomarker page).
   Anything else is a real failure: rerun, or inspect the page.
5. **Download.** When `prog.running` is false, run `window.__fhDownload()`, then check
   `~/Downloads/function-health-biomarkers.json` exists. Read `window.__fhLatestDraw` for the folder
   name.
6. **Split.** `python3 -I scripts/split_bundle.py ~/Downloads/function-health-biomarkers.json
   00-Raw_Sources/L1_Health/function-health/<latest-draw-date>`. It never overwrites; it reports
   identical and differing files. Delete the bundle from `~/Downloads`, and close the tab.
7. **Check the files.** `hyalo find --glob '00-Raw_Sources/L1_Health/function-health/<date>/*.md'
   --limit 500 --format text` parses every file. Compare the count with `prog.total` minus
   the errors. Spot-check 3 values against the live page.
8. **Reconcile with the PDF (when Gil provides one).** Gil downloads the Data page as a PDF.
   Dump its text with PDFKit (poppler and pypdf are not installed):
   ```
   swift - <<'EOF' > <scratchpad>/pdf_text.txt
   import PDFKit
   print(PDFDocument(url: URL(fileURLWithPath: "<path>.pdf"))!.string ?? "")
   EOF
   ```
   Then `python3 -I scripts/reconcile_pdf.py <scratchpad>/pdf_text.txt <date folder> report.json`.
   It checks latest value, date, and in/out-of-range for every PDF entry. Put what only the PDF
   holds (Daily Metrics, multi-category list, reconciliation result) in
   `function-health-data-report-<print-date>.md` in the date folder. The PDF header carries Gil's
   name and date of birth: leave both out of files.

## Pitfalls found in the first run

- **Slugs are not derivable.** `%` stays in the URL as `%25` (`lymphocytes-%25`), and
  "Arachidonic Acid/EPA Ratio" is `arachidonic-acidepa-ratio`. Plain "Lymphocytes" and
  "Lymphocytes %" collide if you strip `%`. The script reads the real links from the category
  pages. Output filenames turn `%25` into `percent` (`lymphocytes-percent.md`).
- **Section headings render twice** (sidebar nav plus content). Out-of-range pages add one extra
  `h4`, "Re-test Out of Range Biomarker", which makes the count odd. The script drops it, then takes
  the second half.
- **Detect a fresh page by comparing the h1 with the previous page's h1**, not by matching the
  record name: names and h1s differ (`Lymphocytes %` vs `Lymphocytes`).
- **Section sets vary**: 3 sections (Iron % Saturation) to 12 (ALT). Each file's `sections:` list
  records what exists. "White Blood Cell (WBC) - Urine" has none: results only.
- **`status` in `current_result` is Function's raw classification** (`in_range`, `above`, `below`,
  `OTHER`, `error`, `above_baseline`). Trust the results table and Quest range over it.
- **Optimal range**: `function_optimal_range` is Function's `optimalRange` string (for ALT
  `[4,36]`). Older pilot files used a different field (`0-32`). Some biomarkers have no range (`-`).
- **Navigation inside the app** uses `history.pushState` plus a `popstate` event, which avoids full
  reloads and Cloudflare re-checks. Unknown paths silently stay on the previous page.
- **Do not print JWTs or localStorage contents.** The extractor needs neither; the store carries the
  data.
- Dates in the PDF are `Mon D, YYYY`. Text extraction adds stray spaces inside numbers (`7 .4`).
  The reconcile script normalizes them.

## Related

Output layout: `00-Raw_Sources/L1_Health/function-health/<YYYY-MM-DD>/<biomarker-slug>.md`.
Older panel notes live in `L1-Health/` (for example `blood-analysis-function-may2026.md`).
