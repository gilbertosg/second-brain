---
title: "L1 — Blood Analysis: Function Health Panel (Oct 2, 2026)"
type: health-data
pillar_id: L1
owner: Gilberto Silva Gonzalez
test_date: 2026-10-02
previous_test_date: 2026-05-19
platform: Function Health
created: 2026-10-24
last_updated: 2026-10-24
status: active
tags: [l1, blood, biomarkers, liver, lipid-fractionation, hormones, inflammation, function-health, health-data]
sources:
  - 00-Raw_Sources/L1_Health/function-health/2026-10-02/
  - 00-Raw_Sources/L1_Health/function-health/2026-10-02/function-health-data-report-2026-10-24.md
related: [L1-Health/blood-analysis-function-may2026, L1-Health/function-health-registry, L1-Health/blood-analysis, L1-Health/biomarker-reference, L1-Health/_pillar, L1-Health/protocol-health-upgrade, 02-Indexes/topic_maps/health-performance-crossmap]
---

# L1 — Blood Analysis: Function Health Panel (Oct 2, 2026)

**Platform:** Function Health (Quest lab draw)
**Test date:** Oct 2, 2026 (second Function Health panel; prior panel May 19, 2026)
**Age at test:** 33 (from the account profile in the Function PDF header; the May note's "34" disagrees, see [Data quality](#data-quality-notes))
**Coverage:** 123 biomarkers returned. 83 have both a May and an Oct result; 39 have a May result only (not retested); 1 has an Oct result only (Progesterone). All 123 are in [[L1-Health/function-health-registry]]. A Data-page PDF export (printed 2026-10-24) matches the extracted files on all 132 entries; see [[00-Raw_Sources/L1_Health/function-health/2026-10-02/function-health-data-report-2026-10-24]].

**Headline:** Seven biomarkers sit out of range. Two are new liver flags (ALT 94, AST 50). Three are new LDL particle flags. hs-CRP is unchanged and still above range. Four May flags resolved (glucose, HDL Large, LDL Peak Size, LH). Free Testosterone improved but stays far below the vault's action trigger.

---

## Out-of-Range Biomarkers — Oct 2026

| # | Biomarker | May 19 | Oct 2 | Change | Quest range | Function optimal | Status |
|---|---|---|---|---|---|---|---|
| 1 | **ALT** | 31 U/L | **94 U/L** | +63 (+203%) | 9–46 | 0–32 | 🔴 **NEW** — 2× the upper limit |
| 2 | **AST** | 21 U/L | **50 U/L** | +29 (+138%) | 10–40 | 10–40 | 🔴 **NEW** |
| 3 | **LDL Particle Number** | 1033 nmol/L | **1309 nmol/L** | +276 (+27%) | < 1138 | < 1138 | 🔴 **NEW** — was in range |
| 4 | **LDL Medium** | 203 nmol/L | **294 nmol/L** | +91 (+45%) | < 215 | < 215 | 🔴 **NEW** — was in range |
| 5 | **LDL Small** | 124 nmol/L | **153 nmol/L** | +29 (+23%) | < 142 | < 142 | 🔴 **NEW** — was in range |
| 6 | **hs-CRP** | 1.2 mg/L | **1.2 mg/L** | 0 | 0–1 | ≤ 1 | 🔴 Persistent — above range on both draws |
| 7 | **Omega-3 Total / OmegaCheck** | 5.0 % by wt | — | not retested | ≥ 5.5 | > 5.4 | 🟡 Below range at the last measurement (May) |

**Resolved since May (4):**

| Biomarker | May 19 | Oct 2 | Note |
|---|---|---|---|
| Glucose | 100 mg/dL (above range) | 93 mg/dL | In Quest range (65–99); still above Function's 70–85 optimal |
| HDL Large | 6,147 nmol/L (below) | 7,370 nmol/L | +20%; now above the > 6,729 threshold |
| LDL Peak Size | 222.4 Å (below) | 225.3 Å | Now above the > 222.9 threshold; LDL Pattern A on both draws |
| Luteinizing Hormone (LH) | 1.4 mIU/mL (below range) | 3.5 mIU/mL | In range (1.5–9.3) |

---

## Liver

| Biomarker | May 19 | Oct 2 | Quest range | Status |
|---|---|---|---|---|
| ALT | 31 | **94** | 9–46 | 🔴 Above |
| AST | 21 | **50** | 10–40 | 🔴 Above |
| GGT | 31 | 40 | 3–90 | In range; above Function optimal (5–17) on both draws, +29% |
| Alkaline Phosphatase | 72 | 72 | 36–130 | In range |
| Total Bilirubin | 0.7 | 0.5 | 0.2–1.2 | In range |
| Albumin | 4.8 | 4.7 | 3.6–5.1 | In range |
| Globulin | 2.4 | 2.1 | 1.9–3.7 | In range |

- ALT/AST ratio is 0.53 (94 / 50). Function's AST page states a ratio above 2 aligns with alcohol-related injury and a lower ratio points toward viral, fatty, or drug-induced hepatocellular damage. The ratio narrows the differential. It does not diagnose.
- Function's AST page calls AST non-specific to one organ and lists muscle injury and strenuous unaccustomed exercise as causes of transient elevation. Its ALT page places ALT mainly in liver and muscle cells. The panel does not include CK, so muscle versus liver origin stays open.
- ALP, bilirubin, and albumin stay in range. GGT stays inside Quest's range but sits above Function's tighter 5–17 optimal band on both draws and rose 29%.
- Full synthesis, causes against Gil's own context, and retest guidance: [[L1-Health/liver-enzymes-alt-ast-oct2026]].

---

## Lipids and Particle Quality

| Biomarker | May 19 | Oct 2 | Quest range | Function optimal | Direction |
|---|---|---|---|---|---|
| LDL Particle Number | 1033 | **1309** | < 1138 | < 1138 | 🔴 Worse, now above |
| LDL Small | 124 | **153** | < 142 | < 142 | 🔴 Worse, now above |
| LDL Medium | 203 | **294** | < 215 | < 215 | 🔴 Worse, now above |
| LDL Peak Size (Å) | 222.4 | 225.3 | > 222.9 | > 222.9 | 🟢 Better, now in range |
| LDL Pattern | A | A | A | A | Unchanged |
| HDL Large | 6147 | 7370 | > 6729 | > 6729 | 🟢 Better, now in range |
| LDL-Cholesterol (calc) | 76 | 82 | < 100 | 20–70 | 🟡 Up 8%; above Function optimal |
| Non-HDL Cholesterol (calc) | 91 | 99 | < 130 | < 100 | 🟡 Up 9%; at Function's ceiling |
| Triglycerides | 74 | 91 | < 150 | 30–70 | 🟡 Up 23%; above Function optimal |
| Total Cholesterol | 157 | 162 | < 200 | 125–199 | In range |
| HDL-Cholesterol | 66 | 63 | ≥ 40 | ≥ 60 | In range |
| ApoB | 56 | — | < 90 | 40–70 | Not retested |
| Lipoprotein (a) | < 10 | — | < 75 | 0–50 | Not retested |

The picture splits. Particle size and large-HDL count improved. Particle count (LDL-P) and the medium and small LDL counts rose, alongside higher triglycerides, LDL-C, non-HDL-C, and fasting insulin (below). Function's LDL pages tie a high particle count with high small-LDL to insulin resistance and name ApoB as a companion risk marker. ApoB was not drawn in October, so the last value (56 mg/dL, May) cannot confirm or rule out the particle-count rise.

---

## Hormones

| Biomarker | May 19 | Oct 2 | Quest range | Function optimal | Note |
|---|---|---|---|---|---|
| Testosterone, Free | 54.0 pg/mL | **64.1** | 35–155 | 148.8–228.1 | +19%; still 57% below the optimal floor |
| Testosterone, Total | 300 ng/dL | 285 | 250–1100 | 500–1000 | −5%; below optimal on both draws |
| SHBG | 13 nmol/L | 15 | 10–50 | 10–50 | +15%; in range |
| Cortisol | 8.0 mcg/dL | **14.7** | 4–22 | 4–22 | +84%; in range |
| DHEA-S | 234 mcg/dL | 212 | 93–415 | 93–415 | −9%; in range |
| Estradiol (E2) | 39 pg/mL | 35 | ≤ 39 | 30–35 | In range |
| LH | 1.4 mIU/mL | 3.5 | 1.5–9.3 | — | Back in range (May below range) |
| FSH | 3.2 mIU/mL | 3.1 | 1.4–12.8 | 1.5–12.4 | In range |
| Prolactin | 9.9 ng/mL | 14.9 | 2–18 | 5–5 as exported | +51%; in range |
| PSA, Total | 0.5 ng/mL | 0.5 | 0–4 | — | Unchanged |

Function's export does not record draw time or fasting status. The cortisol comparison (8.0 versus 14.7) needs that context before it is read as a change in stress physiology.

---

## Metabolic, Inflammation, and Other Systems

| Biomarker | May 19 | Oct 2 | Quest range | Function optimal | Note |
|---|---|---|---|---|---|
| HbA1c (%) | 5.2 | **5.3** | < 5.7 | 4.8–5.5 | Sits on the vault's 5.3% action line (see below) |
| Glucose (mg/dL) | 100 | 93 | 65–99 | 70–85 | Resolved vs Quest range |
| Insulin (uIU/mL) | 10.9 | 12.5 | ≤ 18.4 | 2–5 | +15%; 2.5× the top of Function optimal |
| hs-CRP (mg/L) | 1.2 | 1.2 | 0–1 | ≤ 1 | Unchanged, above range |
| Vitamin D (ng/mL) | 54 | 52 | 30–100 | 45–100 | In range, drifting down from 65 (Jan, Spren) |
| Uric acid | — | 6.3 (May) | 4.0–8.0 | 4.0–5.5 | Not retested; above Function optimal |
| Creatinine / BUN | 1.09 / 12 | 0.97 / 15 | in range | in range | Kidney markers stable |
| WBC | 6.6 | 7.4 | 3.8–10.8 | 4–11 | In range |
| Hematocrit / Hemoglobin | 46.8 / 16.5 | 45.3 / 15.8 | in range | in range | Slight decline |
| MCH (pg) | 32.9 | 32.6 | 27.0–33.0 | 26–33 | In range on both draws |
| Calcium / Sodium / Potassium | 9.6 / 141 / 3.9 | 9.1 / 139 / 4.0 | in range | in range | Stable |
| Urine panel (16 markers) | in range | in range | — | — | All in range; WBC–Urine reads "none seen" |

---

## Not Retested in October (latest value is May)

ApoB 56, Lp(a) < 10, Omega-3 Total/OmegaCheck 5.0 (and the full omega-3/6 fractions), Homocysteine 10.0, TSH 1.08, T4 Free 1.5, T3 Free 3.6, Ferritin 98, Iron/TIBC/% saturation, Zinc 75, Magnesium RBC 6.4, MMA 91, Uric acid 6.3, Leptin 4.5, IGF-1 190, DHT 15, Androstenedione 75, Z Score 0.6, Amylase/Lipase, thyroid antibodies, ANA, RF, Lead, Mercury, blood type. Several are protocol-tracked (ApoB, Omega-3, Homocysteine). Add them to the next draw.

---

## Contradicts / Strengthens: Existing Vault Claims

| Existing claim (page) | Oct 2026 data | Verdict |
|---|---|---|
| "ALT / AST: Consistently healthy" ([[L1-Health/biomarker-reference]], Organ Health table) | ALT 94, AST 50, both above range; May was 31 / 21 | ❌ **Contradicted** |
| MCH "persistently HIGH (3/3 draws)"; request MCH on next draw ([[L1-Health/biomarker-reference]], [[L1-Health/blood-analysis]]) | MCH 32.9 (May) and 32.6 (Oct), both under the 33.0 limit | ❌ **Superseded**: the requested retest happened and reads in range |
| Cortisol "Low (2026)", Spren 7.6 in Jan ([[L1-Health/blood-analysis]], [[L1-Health/biomarker-reference]]) | 8.0 (May) then 14.7 (Oct), inside Spren's 10–15 band | ❌ **Superseded** pending draw-time context |
| TSH "low-trending", 0.64 in Jan ([[L1-Health/biomarker-reference]]) | 1.08 in May, inside Function's 0.45–2 optimal; not retested | ❌ **Superseded** (Jan → May reversal) |
| Ferritin "declining trend", 163 → 84 ([[L1-Health/blood-analysis]]) | 98 in May (+17% vs Jan); not retested | ❌ **Superseded** |
| LDL Peak Size "trending toward small/dense Pattern B" ([[L1-Health/blood-analysis-function-may2026]]) | 225.3 Å, above the optimal threshold; Pattern A on both draws | ❌ **Contradicted** for peak size and pattern |
| …but LDL particle counts | LDL Small and Medium both above range; LDL-P above range | ⚠ **New conflict** with the peak-size result; ApoB needed to adjudicate |
| "Metabolic syndrome dyad": low HDL Large + borderline glucose ([[L1-Health/blood-analysis-function-may2026]]) | Both resolved. Insulin, triglycerides, LDL-P, LDL-C, non-HDL-C all rose | ⚠ **Split**: the two flagged markers cleared; broader drift continued |
| hs-CRP 1.2, action trigger breached ([[L1-Health/protocol-health-upgrade]]) | 1.2 again; above range on both draws | ✅ **Strengthened**: no movement over 4.5 months |
| Free T 54.0, "action trigger breached" ([[L1-Health/protocol-health-upgrade]]) | 64.1 pg/mL, +19%, still under the 150 trigger | ✅ **Strengthened**: still critical, improving |
| "High SHBG (sequestering T)"; "the bottleneck is bioavailability (SHBG), not production" ([[02-Indexes/topic_maps/health-performance-crossmap]], [[L1-Health/blood-analysis]], `index.md` Session 5 note) | SHBG 13 (May) and 15 nmol/L (Oct), low-normal in a 10–50 range. Total T is the low value (300, then 285). LH read 1.4 mIU/mL in May (below range) before 3.5 in Oct | ❌ **Contradicted**: the data does not show SHBG binding; a physician decides which axis is limiting |
| "If two consecutive quarterly panels confirm Free T below trigger: clinical consultation" ([[L1-Health/protocol-health-upgrade]], line 78) | May 54.0 and Oct 64.1 are two consecutive panels below 150 (4.5 months apart) | ⚠ **Escalation criterion met**; see proposals |
| Total T 262 → 300 "first positive reversal since Aug 2023" ([[L1-Health/blood-analysis]]) | 285 ng/dL in Oct, −5% from May | ⚠ **Partly reversed**: still +9% vs Jan, not sustained |
| HbA1c 5.2%, trigger "> 5.3%" not breached ([[L1-Health/protocol-health-upgrade]]) | 5.3% | ⚠ **At the line**; vault wording conflicts (see below) |
| "Excellent traditional lipids (LDL 46, TG 44, ApoB 62)" ([[L1-Health/blood-analysis-function-may2026]]) | Function May/Oct: LDL-C 76 → 82, TG 74 → 91, ApoB 56 (May) | ⚠ **Different platform and date**: the 46 / 44 / 62 values are Jan 2026 (Spren). The Function values are higher |
| Insulin "0.95 uIU/mL, very low, high sensitivity" (Jan 2024, [[L1-Health/biomarker-reference]]) | 10.9 (May) → 12.5 (Oct) | ⚠ **Strengthens metabolic-drift concern**; assay differences between InsideTracker and Quest limit a direct comparison |
| DHEA-S "Low, significant decline" ([[L1-Health/biomarker-reference]]) | 234 (May), 212 (Oct) vs Jan 215 | ✅ **Strengthened** against Spren's 260–520 band; in range by Quest (93–415) |
| Estradiol "not recently tested" ([[L1-Health/biomarker-reference]]) | 39 → 35 pg/mL | ❌ **Outdated**: now measured twice |
| FSH/LH "historically healthy" ([[L1-Health/biomarker-reference]]) | LH 1.4 in May was below range; 3.5 in Oct | ⚠ **Refined**: one out-of-range reading, resolved |
| Vitamin D "65.36 healthy" (Jan) ([[L1-Health/biomarker-reference]]) | 54 (May) → 52 (Oct) | ✅ Still healthy; downward drift of 20% since Jan |

---

## Proposed Protocol Changes (for Gil's review; not applied)

`protocol-health-upgrade.md` and `protocols/biomarker_correction_plan.md` stay unchanged until approved.

| # | Proposal | Reason | Target file |
|---|---|---|---|
| 1 | Mark the Free T clinical-consultation criterion as met and schedule the physician consult. The correction plan already holds a consult-prep section | Two consecutive panels below 150 pg/mL; the correction plan counts one confirmed panel as 1 of 2 for pharmacological-intervention eligibility, and its decision tree puts SHBG 15 on the "production problem" branch ([[02-Indexes/topic_maps/health-performance-crossmap]]) | `protocol-health-upgrade.md` (Domain 2), `biomarker_correction_plan.md` |
| 2 | Add ALT and AST to the Critical Biomarker Table with an action trigger and a physician-review step. Include medication, supplement, and alcohol review before the retest | New flags, ALT at 2× the upper limit | `protocol-health-upgrade.md` |
| 3 | Add LDL Particle Number to the table and add ApoB (with Lp(a)) to the next draw | LDL-P up 27%, ApoB last drawn in May | `protocol-health-upgrade.md` |
| 4 | Resolve the HbA1c trigger wording. The protocol says "> 5.3%" (lines 69 and 85); the scorecard says "if ≥ 5.3%" (line 168). Oct is exactly 5.3% | Under ">" no action; under "≥" the carbohydrate-sequencing protocol activates | `protocol-health-upgrade.md`, `biomarker-scorecard-may2026.md` |
| 5 | Add the non-retested protocol markers to the next draw: ApoB, Omega-3, Homocysteine, TSH | They carry May values only | next-draw checklist |
| 6 | Record draw time and fasting status with each draw | Cortisol moved 8.0 → 14.7 with no context | next-draw checklist |
| 7 | Log adherence to the hs-CRP actions (omega-3 2–3 g/day, Zone 2 cardio, antigen review); the vault records the actions but not whether they happened, and hs-CRP is unchanged | Unchanged 1.2 mg/L over 4.5 months | `protocol-health-upgrade.md` |

These are data-driven proposals, not medical advice. Liver and lipid-particle findings need physician interpretation.

---

## Data Quality Notes

- **Source:** per-biomarker files extracted from the Function Health web app (results from the app's data store, descriptions from the rendered page). A Data-page PDF reconciles 132 of 132 entries on latest value, date, and in/out-of-range flag. See [[L1-Health/function-health-registry]].
- **Age:** Function's profile implies age 33 on both May 19 and Oct 2. [[L1-Health/blood-analysis-function-may2026]] and the timeline in [[L1-Health/blood-analysis]] state 34 for May.
- **Free T reference range:** the Function export lists Quest range 35–155 pg/mL; the vault tables quote 46–224. Function's optimal range (148.8–228.1) matches the vault's Medicine 3.0 floor.
- **Omega-3 threshold:** Quest range ≥ 5.5, Function optimal > 5.4. The vault uses ≥ 5.5.
- **`status` field:** Function's raw classification is inconsistent (`in_range`, `above`, `below`, `OTHER`, `error`). This page uses the results table's in-range flag and the Quest range.
- **Biological Age:** the results record has no biomarker page and no value, so it is absent.
- **Pilot file:** `alanine-aminotransferase-alt.md` records an older optimal range (0–32); the Function page text and bulk extraction give 4–36. The registry shows 0–32 as exported.

---

## Cross-Reference

- [[L1-Health/function-health-registry]] — all 123 biomarkers, generated from the raw files
- [[L1-Health/blood-analysis-function-may2026]] — May 19, 2026 panel (baseline for every delta above)
- [[L1-Health/blood-analysis]] — full draw history
- [[L1-Health/biomarker-reference]] — interpretation guide (liver row corrected in this ingest)
- [[L1-Health/liver-enzymes-alt-ast-oct2026]] — liver synthesis
- [[L1-Health/protocol-health-upgrade]] — action triggers referenced above
- [[02-Indexes/topic_maps/health-performance-crossmap]] — cortisol, Free T, and liver links to the L3 performance chain; SHBG chain corrected
