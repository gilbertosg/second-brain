---
title: "Function Health — Data Page Report (printed 2026-10-24)"
type: raw-source
platform: Function Health
source_file: ~/Downloads/DataFunction.pdf
source_url: https://my.functionhealth.com/biomarkers
printed: 2026-10-24
latest_draw: 2026-10-02
previous_draw: 2026-05-19
pdf_entries: 132
unique_biomarkers: 123
reconciliation: all-matched
---

# Function Health — Data Page Report (printed 2026-10-24)

PDF print of the Function Health Data page (12 pages). It lists the latest value, range status, and draw date for each biomarker, grouped by category. This file records what the PDF adds beyond the per-biomarker files in this folder, and the result of checking the PDF against those files.

## Reconciliation against the biomarker files

| Check | Result |
|---|---|
| PDF entries | 132 (123 unique biomarkers; 8 appear under two or three categories) |
| Matched on latest value, draw date, and in/out-of-range flag | 132 of 132 |
| Mismatches | 0 |
| PDF biomarkers with no file | 0 |
| Files with no PDF entry | 0 (the "Biological Age" record has neither a file nor a PDF entry) |

The PDF shows only the latest result, so it does not verify the previous (2026-05-19) results.

### Out-of-range biomarkers in the PDF

| Biomarker | Status | Latest value | Draw date |
|---|---|---|---|
| High-Sensitivity C-Reactive Protein (hs-CRP) | Above Range | 1.2 mg/L | 2026-10-02 |
| LDL Medium | Above Range | 294 nmol/L | 2026-10-02 |
| LDL Particle Number | Above Range | 1309 nmol/L | 2026-10-02 |
| LDL Small | Above Range | 153 nmol/L | 2026-10-02 |
| Alanine Aminotransferase (ALT) | Above Range | 94 U/L | 2026-10-02 |
| Aspartate Aminotransferase (AST) | Above Range | 50 U/L | 2026-10-02 |
| Omega-3 Total / OmegaCheck | Below Range | 5.0 % by wt | 2026-05-19 |

Draw dates in this table come from the PDF's date column and match each biomarker's `current_result.date` in its file.

### Biomarkers listed under more than one category

| Biomarker | Categories in the PDF |
|---|---|
| Albumin, Random Urine without Creatinine | Kidney, Urine |
| Calcium | Electrolytes, Kidney, Nutrients |
| Chloride | Electrolytes, Kidney |
| DHEA Sulfate | Male Health, Stress & Aging |
| High-Sensitivity C-Reactive Protein (hs-CRP) | Heart, Immune Regulation |
| Magnesium, RBC | Electrolytes, Nutrients |
| Potassium | Electrolytes, Kidney |
| Sodium | Electrolytes, Kidney |

## Daily Metrics (PDF only)

Wearable-derived metrics on the Data page. They carry no draw date. Blank values were empty in the PDF.

| Metric | Value |
|---|---|
| Body Fat % | |
| Calories Burned | 864 cals |
| Exercise Time | 0 min |
| Heart Rate Variability | |
| Resting Heart Rate | |
| Sleep Consistency | |
| Sleep Time | |
| Steps Taken | 2,098 |
| VO2 Max | |
| Weight | |

## Notes

- The PDF omits the status prefix for a few markers (ABO Group, Rhesus (Rh) Factor, the five percent differentials such as `Basophils %`, `Omega-3 Total`, `Omega-6 Total`, and `Albumin, Random Urine without Creatinine`), so the check compares only value and date for those.
- The PDF prints the account holder's name and date of birth in its header. This file leaves both out.
