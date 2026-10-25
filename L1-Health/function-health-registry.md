---
title: "L1 — Function Health Biomarker Registry"
type: health-data
pillar_id: L1
owner: Gilberto Silva Gonzalez
created: 2026-10-24
last_updated: 2026-10-25
status: active
tags: [l1, blood, biomarkers, function-health, registry, generated]
sources:
  - 00-Raw_Sources/L1_Health/function-health/2026-10-02/
draws: [2026-05-19, 2026-05-20, 2026-10-02]
biomarkers: 123
generated_by: .claude/skills/function-health-extract/scripts/build_registry.py
related: [L1-Health/blood-analysis-function-oct2026, L1-Health/blood-analysis-function-may2026, L1-Health/blood-analysis]
---

# L1 — Function Health Biomarker Registry

Every biomarker Function Health returned for the draws on May 19, May 20, Oct 2 (2026). Generated from the extracted raw files; do not edit by hand. Regenerate with `build_registry.py` after each new extraction.

- **Biomarkers:** 123 (83 with two results, 40 with one)
- **Out of range at the latest result:** 7
- **Status** comes from the latest result's in-range flag. **Quest range** is the lab reference range; **Function optimal** is Function Health's tighter range (blank or `-` where none exists).
- Narrative analysis: [[L1-Health/blood-analysis-function-oct2026]] (Oct 2, 2026) and [[L1-Health/blood-analysis-function-may2026]] (May 19, 2026).

## Autoimmunity

Explainers: [[L1-Health/biomarker-digest-autoimmunity]]

| Biomarker | Unit | Previous | Latest | Change | Status | Quest range | Function optimal | Source |
|---|---|---|---|---|---|---|---|---|
| Antinuclear Antibodies (ANA) Screen |  | — | NEGATIVE (May 19) | — | In range | NEGATIVE | NEGATIVE | [file](../00-Raw_Sources/L1_Health/function-health/2026-10-02/antinuclear-antibodies-ana-screen.md) |
| Rheumatoid Factor (RF) | IU/mL | — | <10 (May 19) | — | In range | <14 | [0,14] | [file](../00-Raw_Sources/L1_Health/function-health/2026-10-02/rheumatoid-factor-rf.md) |

## Blood

Explainers: [[L1-Health/biomarker-digest-blood]]

| Biomarker | Unit | Previous | Latest | Change | Status | Quest range | Function optimal | Source |
|---|---|---|---|---|---|---|---|---|
| ABO Group |  | — | A (May 19) | — | In range | — | — | [file](../00-Raw_Sources/L1_Health/function-health/2026-10-02/abo-group.md) |
| Hematocrit | % | 46.8 (May 19) | 45.3 (Oct 2) | -1.5 (-3%) | In range | 39.4-51.1 | [40,45] | [file](../00-Raw_Sources/L1_Health/function-health/2026-10-02/hematocrit.md) |
| Hemoglobin | g/dL | 16.5 (May 19) | 15.8 (Oct 2) | -0.7 (-4%) | In range | 13.2-17.1 | [11.1,15.9] | [file](../00-Raw_Sources/L1_Health/function-health/2026-10-02/hemoglobin.md) |
| Mean Corpuscular Hemoglobin (MCH) | pg | 32.9 (May 19) | 32.6 (Oct 2) | -0.3 (-1%) | In range | 27.0-33.0 | [26,33] | [file](../00-Raw_Sources/L1_Health/function-health/2026-10-02/mean-corpuscular-hemoglobin-mch.md) |
| Mean Corpuscular Hemoglobin Concentration (MCHC) | g/dL | 35.3 (May 19) | 34.9 (Oct 2) | -0.4 (-1%) | In range | 31.6-35.4 | [31.5,35.7] | [file](../00-Raw_Sources/L1_Health/function-health/2026-10-02/mean-corpuscular-hemoglobin-concentration-mchc.md) |
| Mean Corpuscular Volume (MCV) | fL | 93.2 (May 19) | 93.4 (Oct 2) | +0.2 (+0%) | In range | 81.4-101.7 | [85,95] | [file](../00-Raw_Sources/L1_Health/function-health/2026-10-02/mean-corpuscular-volume-mcv.md) |
| Mean Platelet Volume (MPV) | fL | 10.7 (May 19) | 10.9 (Oct 2) | +0.2 (+2%) | In range | 7.5 - 12.5 | [7.2,11.7] | [file](../00-Raw_Sources/L1_Health/function-health/2026-10-02/mean-platelet-volume-mpv.md) |
| Platelet Count | Thousand/uL | 193 (May 19) | 206 (Oct 2) | +13 (+7%) | In range | 140-400 | [141,362] | [file](../00-Raw_Sources/L1_Health/function-health/2026-10-02/platelet-count.md) |
| Red Blood Cell (RBC) Count | Million/uL | 5.02 (May 19) | 4.85 (Oct 2) | -0.17 (-3%) | In range | 4.20-5.80 | [3.77,5.28] | [file](../00-Raw_Sources/L1_Health/function-health/2026-10-02/red-blood-cell-rbc-count.md) |
| Red Cell Distribution Width (RDW) | % | 13.5 (May 19) | 12.8 (Oct 2) | -0.7 (-5%) | In range | 11 - 15 | [11.7,15.4] | [file](../00-Raw_Sources/L1_Health/function-health/2026-10-02/red-cell-distribution-width-rdw.md) |
| Rhesus (Rh) Factor |  | — | RH(D) POSITIVE (May 19) | — | In range | — | — | [file](../00-Raw_Sources/L1_Health/function-health/2026-10-02/rhesus-rh-factor.md) |

## Electrolytes

Explainers: [[L1-Health/biomarker-digest-electrolytes]]

| Biomarker | Unit | Previous | Latest | Change | Status | Quest range | Function optimal | Source |
|---|---|---|---|---|---|---|---|---|
| Calcium | mg/dL | 9.6 (May 19) | 9.1 (Oct 2) | -0.5 (-5%) | In range | 8.6-10.3 | [8.6,10.3] | [file](../00-Raw_Sources/L1_Health/function-health/2026-10-02/calcium.md) |
| Carbon Dioxide | mmol/L | 26 (May 19) | 28 (Oct 2) | +2 (+8%) | In range | 20 - 32 | [23,32] | [file](../00-Raw_Sources/L1_Health/function-health/2026-10-02/carbon-dioxide.md) |
| Chloride | mmol/L | 104 (May 19) | 103 (Oct 2) | -1 (-1%) | In range | 98 - 110 | [98,110] | [file](../00-Raw_Sources/L1_Health/function-health/2026-10-02/chloride.md) |
| Potassium | mmol/L | 3.9 (May 19) | 4.0 (Oct 2) | +0.1 (+3%) | In range | 3.5-5.3 | [3.5,5.3] | [file](../00-Raw_Sources/L1_Health/function-health/2026-10-02/potassium.md) |

## Environmental Toxins

Explainers: [[L1-Health/biomarker-digest-environmental-toxins]]

| Biomarker | Unit | Previous | Latest | Change | Status | Quest range | Function optimal | Source |
|---|---|---|---|---|---|---|---|---|
| Lead | mcg/dL | — | 1.0 (May 19) | — | In range | <3.5 | [0,0] | [file](../00-Raw_Sources/L1_Health/function-health/2026-10-02/lead.md) |
| Mercury | mcg/L | — | <4 (May 19) | — | In range | <=10 | [0,0] | [file](../00-Raw_Sources/L1_Health/function-health/2026-10-02/mercury.md) |

## Heart

Explainers: [[L1-Health/biomarker-digest-heart]]

| Biomarker | Unit | Previous | Latest | Change | Status | Quest range | Function optimal | Source |
|---|---|---|---|---|---|---|---|---|
| Apolipoprotein B (ApoB) | mg/dL | — | 56 (May 19) | — | In range | <90 | [40,70] | [file](../00-Raw_Sources/L1_Health/function-health/2026-10-02/apolipoprotein-b-apob.md) |
| HDL Large | nmol/L | 6147 (May 19) | 7370 (Oct 2) | +1223 (+20%) | In range | > 6729 | (6729,) | [file](../00-Raw_Sources/L1_Health/function-health/2026-10-02/hdl-large.md) |
| HDL-Cholesterol | mg/dL | 66 (May 19) | 63 (Oct 2) | -3 (-5%) | In range | >= 40 | [60,) | [file](../00-Raw_Sources/L1_Health/function-health/2026-10-02/hdl-cholesterol.md) |
| LDL Medium | nmol/L | 203 (May 19) | 294 (Oct 2) | +91 (+45%) | Above | < 215 | (,215) | [file](../00-Raw_Sources/L1_Health/function-health/2026-10-02/ldl-medium.md) |
| LDL Particle Number | nmol/L | 1033 (May 19) | 1309 (Oct 2) | +276 (+27%) | Above | < 1138 | (,1138) | [file](../00-Raw_Sources/L1_Health/function-health/2026-10-02/ldl-particle-number.md) |
| LDL Pattern | Pattern | A (May 19) | A (Oct 2) | — | In range | A | A | [file](../00-Raw_Sources/L1_Health/function-health/2026-10-02/ldl-pattern.md) |
| LDL Peak Size | Angstrom | 222.4 (May 19) | 225.3 (Oct 2) | +2.9 (+1%) | In range | > 222.9 | (222.9,) | [file](../00-Raw_Sources/L1_Health/function-health/2026-10-02/ldl-peak-size.md) |
| LDL Small | nmol/L | 124 (May 19) | 153 (Oct 2) | +29 (+23%) | Above | <142 | (,142) | [file](../00-Raw_Sources/L1_Health/function-health/2026-10-02/ldl-small.md) |
| LDL-Cholesterol | mg/dL (calc) | 76 (May 19) | 82 (Oct 2) | +6 (+8%) | In range | < 100 | [20,70] | [file](../00-Raw_Sources/L1_Health/function-health/2026-10-02/ldl-cholesterol.md) |
| Lipoprotein (a) | nmol/L | — | <10 (May 19) | — | In range | <75 | [0,50) | [file](../00-Raw_Sources/L1_Health/function-health/2026-10-02/lipoprotein-a.md) |
| Non-HDL Cholesterol | mg/dL (calc) | 91 (May 19) | 99 (Oct 2) | +8 (+9%) | In range | < 130 | (,100) | [file](../00-Raw_Sources/L1_Health/function-health/2026-10-02/non-hdl-cholesterol.md) |
| Total Cholesterol | mg/dL | 157 (May 19) | 162 (Oct 2) | +5 (+3%) | In range | <200 | [125,199] | [file](../00-Raw_Sources/L1_Health/function-health/2026-10-02/total-cholesterol.md) |
| Total Cholesterol / HDL Ratio | (calc) | 2.4 (May 19) | 2.6 (Oct 2) | +0.2 (+8%) | In range | < 5 | (,3.5) | [file](../00-Raw_Sources/L1_Health/function-health/2026-10-02/total-cholesterol-hdl-ratio.md) |
| Triglycerides | mg/dL | 74 (May 19) | 91 (Oct 2) | +17 (+23%) | In range | <150 | [30,70] | [file](../00-Raw_Sources/L1_Health/function-health/2026-10-02/triglycerides.md) |

## Immune Regulation

Explainers: [[L1-Health/biomarker-digest-immune-regulation]]

| Biomarker | Unit | Previous | Latest | Change | Status | Quest range | Function optimal | Source |
|---|---|---|---|---|---|---|---|---|
| Basophils | cells/uL | 33 (May 19) | 37 (Oct 2) | +4 (+12%) | In range | 0 - 200 | [0,200] | [file](../00-Raw_Sources/L1_Health/function-health/2026-10-02/basophils.md) |
| Basophils % | % | 0.5 (May 19) | 0.5 (Oct 2) | +0 (+0%) | In range | — | — | [file](../00-Raw_Sources/L1_Health/function-health/2026-10-02/basophils-percent.md) |
| Eosinophils | cells/uL | 92 (May 19) | 118 (Oct 2) | +26 (+28%) | In range | 15 - 500 | [15,500] | [file](../00-Raw_Sources/L1_Health/function-health/2026-10-02/eosinophils.md) |
| Eosinophils % | % | 1.4 (May 19) | 1.6 (Oct 2) | +0.2 (+14%) | In range | — | — | [file](../00-Raw_Sources/L1_Health/function-health/2026-10-02/eosinophils-percent.md) |
| High-Sensitivity C-Reactive Protein (hs-CRP) | mg/L | 1.2 (May 19) | 1.2 (Oct 2) | +0 (+0%) | Above | 0 - 1 | (,1] | [file](../00-Raw_Sources/L1_Health/function-health/2026-10-02/high-sensitivity-c-reactive-protein-hs-crp.md) |
| Lymphocytes | cells/uL | 2119 (May 19) | 2264 (Oct 2) | +145 (+7%) | In range | 850-3900 | [850,3900] | [file](../00-Raw_Sources/L1_Health/function-health/2026-10-02/lymphocytes.md) |
| Lymphocytes % | % | 32.1 (May 19) | 30.6 (Oct 2) | -1.5 (-5%) | In range | — | — | [file](../00-Raw_Sources/L1_Health/function-health/2026-10-02/lymphocytes-percent.md) |
| Monocytes | cells/uL | 568 (May 19) | 718 (Oct 2) | +150 (+26%) | In range | 200-950 | [200,950] | [file](../00-Raw_Sources/L1_Health/function-health/2026-10-02/monocytes.md) |
| Monocytes % | % | 8.6 (May 19) | 9.7 (Oct 2) | +1.1 (+13%) | In range | — | — | [file](../00-Raw_Sources/L1_Health/function-health/2026-10-02/monocytes-percent.md) |
| Neutrophils | cells/uL | 3788 (May 19) | 4262 (Oct 2) | +474 (+13%) | In range | 1500-7800 | [1500,7800] | [file](../00-Raw_Sources/L1_Health/function-health/2026-10-02/neutrophils.md) |
| Neutrophils % | % | 57.4 (May 19) | 57.6 (Oct 2) | +0.2 (+0%) | In range | — | — | [file](../00-Raw_Sources/L1_Health/function-health/2026-10-02/neutrophils-percent.md) |
| White Blood Cell (WBC) Count | Thousand/uL | 6.6 (May 19) | 7.4 (Oct 2) | +0.8 (+12%) | In range | 3.8-10.8 | [4,11] | [file](../00-Raw_Sources/L1_Health/function-health/2026-10-02/white-blood-cell-wbc-count.md) |

## Kidney

Explainers: [[L1-Health/biomarker-digest-kidney]]

| Biomarker | Unit | Previous | Latest | Change | Status | Quest range | Function optimal | Source |
|---|---|---|---|---|---|---|---|---|
| Albumin, Random Urine without Creatinine | mg/dL | <0.2 (May 19) | 0.4 (Oct 2) | — | In range | See Note: | -0.2 | [file](../00-Raw_Sources/L1_Health/function-health/2026-10-02/albumin-random-urine-without-creatinine.md) |
| Blood Urea Nitrogen (BUN) | mg/dL | 12 (May 19) | 15 (Oct 2) | +3 (+25%) | In range | 7-25 | [7,25] | [file](../00-Raw_Sources/L1_Health/function-health/2026-10-02/blood-urea-nitrogen-bun.md) |
| Creatinine | mg/dL | 1.09 (May 19) | 0.97 (Oct 2) | -0.12 (-11%) | In range | 0.60-1.26 | [0.57,1] | [file](../00-Raw_Sources/L1_Health/function-health/2026-10-02/creatinine.md) |
| Creatinine-Based Estimated Glomerular Filtration Rate (eGFR) | mL/min/1.73m2 | 92 (May 19) | 106 (Oct 2) | +14 (+15%) | In range | >= 60 | [90,120] | [file](../00-Raw_Sources/L1_Health/function-health/2026-10-02/creatinine-based-estimated-glomerular-filtration-rate-egfr.md) |
| Sodium | mmol/L | 141 (May 19) | 139 (Oct 2) | -2 (-1%) | In range | 135 - 146 | [135,146] | [file](../00-Raw_Sources/L1_Health/function-health/2026-10-02/sodium.md) |

## Liver

Explainers: [[L1-Health/biomarker-digest-liver]]

| Biomarker | Unit | Previous | Latest | Change | Status | Quest range | Function optimal | Source |
|---|---|---|---|---|---|---|---|---|
| Alanine Aminotransferase (ALT) | U/L | 31 (May 19) | 94 (Oct 2) | +63 (+203%) | Above | 9-46 | 0-32 | [file](../00-Raw_Sources/L1_Health/function-health/2026-10-02/alanine-aminotransferase-alt.md) |
| Albumin | g/dL | 4.8 (May 19) | 4.7 (Oct 2) | -0.1 (-2%) | In range | 3.6 - 5.1 | [4,5] | [file](../00-Raw_Sources/L1_Health/function-health/2026-10-02/albumin.md) |
| Albumin / Globulin Ratio | (calc) | 2.0 (May 19) | 2.2 (Oct 2) | +0.2 (+10%) | In range | 1 - 2.5 | [1,2.5] | [file](../00-Raw_Sources/L1_Health/function-health/2026-10-02/albumin-globulin-ratio.md) |
| Alkaline Phosphatase (ALP) | U/L | 72 (May 19) | 72 (Oct 2) | +0 (+0%) | In range | 36-130 | [30,120] | [file](../00-Raw_Sources/L1_Health/function-health/2026-10-02/alkaline-phosphatase-alp.md) |
| Aspartate Aminotransferase (AST) | U/L | 21 (May 19) | 50 (Oct 2) | +29 (+138%) | Above | 10-40 | [10,40] | [file](../00-Raw_Sources/L1_Health/function-health/2026-10-02/aspartate-aminotransferase-ast.md) |
| Gamma-glutamyl Transferase (GGT) | U/L | 31 (May 19) | 40 (Oct 2) | +9 (+29%) | In range | 3 - 90 | [5,17] | [file](../00-Raw_Sources/L1_Health/function-health/2026-10-02/gamma-glutamyl-transferase-ggt.md) |
| Globulin | g/dL (calc) | 2.4 (May 19) | 2.1 (Oct 2) | -0.3 (-12%) | In range | 1.9-3.7 | [1.9,3.7] | [file](../00-Raw_Sources/L1_Health/function-health/2026-10-02/globulin.md) |
| Total Bilirubin | mg/dL | 0.7 (May 19) | 0.5 (Oct 2) | -0.2 (-29%) | In range | 0.2-1.2 | [0.58,1.2] | [file](../00-Raw_Sources/L1_Health/function-health/2026-10-02/total-bilirubin.md) |
| Total Protein | g/dL | 7.2 (May 19) | 6.8 (Oct 2) | -0.4 (-6%) | In range | 6.1-8.1 | [6,8.5] | [file](../00-Raw_Sources/L1_Health/function-health/2026-10-02/total-protein.md) |

## Male Health

Explainers: [[L1-Health/biomarker-digest-male-health]]

| Biomarker | Unit | Previous | Latest | Change | Status | Quest range | Function optimal | Source |
|---|---|---|---|---|---|---|---|---|
| Androstenedione | ng/dL | — | 75 (May 20) | — | In range | 40-190 | [40,190] | [file](../00-Raw_Sources/L1_Health/function-health/2026-10-02/androstenedione.md) |
| Dihydrotestosterone (DHT) | ng/dL | — | 15 (May 20) | — | In range | 12-65 | [12,65] | [file](../00-Raw_Sources/L1_Health/function-health/2026-10-02/dihydrotestosterone-dht.md) |
| Estradiol (E2) | pg/mL | 39 (May 19) | 35 (Oct 2) | -4 (-10%) | In range | <= 39 | [30,35] | [file](../00-Raw_Sources/L1_Health/function-health/2026-10-02/estradiol-e2.md) |
| Follicle Stimulating Hormone (FSH) | mIU/mL | 3.2 (May 19) | 3.1 (Oct 2) | -0.1 (-3%) | In range | 1.4 - 12.8 | 1.5-12.4 | [file](../00-Raw_Sources/L1_Health/function-health/2026-10-02/follicle-stimulating-hormone-fsh.md) |
| Luteinizing Hormone (LH) | mIU/mL | 1.4 (May 19) | 3.5 (Oct 2) | +2.1 (+150%) | In range | 1.5 - 9.3 | — | [file](../00-Raw_Sources/L1_Health/function-health/2026-10-02/luteinizing-hormone-lh.md) |
| Progesterone | ng/mL | — | <0.1 (Oct 2) | — | In range | 0 - 0.2 | — | [file](../00-Raw_Sources/L1_Health/function-health/2026-10-02/progesterone.md) |
| Prolactin | ng/mL | 9.9 (May 19) | 14.9 (Oct 2) | +5 (+51%) | In range | 2 - 18 | [5,5] | [file](../00-Raw_Sources/L1_Health/function-health/2026-10-02/prolactin.md) |
| Prostate Specific Antigen (PSA) %, Free | % (calc) | 40 (May 19) | 40 (Oct 2) | +0 (+0%) | In range | > 25 | (25,) | [file](../00-Raw_Sources/L1_Health/function-health/2026-10-02/prostate-specific-antigen-psa-percent-free.md) |
| Prostate Specific Antigen (PSA), Free | ng/mL | 0.2 (May 19) | 0.2 (Oct 2) | +0 (+0%) | In range | — | — | [file](../00-Raw_Sources/L1_Health/function-health/2026-10-02/prostate-specific-antigen-psa-free.md) |
| Prostate Specific Antigen (PSA), Total | ng/mL | 0.5 (May 19) | 0.5 (Oct 2) | +0 (+0%) | In range | 0 - 4 | -4 | [file](../00-Raw_Sources/L1_Health/function-health/2026-10-02/prostate-specific-antigen-psa-total.md) |
| Sex Hormone Binding Globulin (SHBG) | nmol/L | 13 (May 19) | 15 (Oct 2) | +2 (+15%) | In range | 10 - 50 | [10,50] | [file](../00-Raw_Sources/L1_Health/function-health/2026-10-02/sex-hormone-binding-globulin-shbg.md) |
| Testosterone, Free | pg/mL | 54.0 (May 19) | 64.1 (Oct 2) | +10.1 (+19%) | In range | 35 - 155 | [148.8,228.1] | [file](../00-Raw_Sources/L1_Health/function-health/2026-10-02/testosterone-free.md) |
| Testosterone, Total | ng/dL | 300 (May 19) | 285 (Oct 2) | -15 (-5%) | In range | 250 - 1100 | [500,1000] | [file](../00-Raw_Sources/L1_Health/function-health/2026-10-02/testosterone-total.md) |

## Metabolic

Explainers: [[L1-Health/biomarker-digest-metabolic]]

| Biomarker | Unit | Previous | Latest | Change | Status | Quest range | Function optimal | Source |
|---|---|---|---|---|---|---|---|---|
| Glucose | mg/dL | 100 (May 19) | 93 (Oct 2) | -7 (-7%) | In range | 65-99 | [70,85] | [file](../00-Raw_Sources/L1_Health/function-health/2026-10-02/glucose.md) |
| Hemoglobin A1c (HbA1c) | % | 5.2 (May 19) | 5.3 (Oct 2) | +0.1 (+2%) | In range | < 5.7 | [4.8,5.5] | [file](../00-Raw_Sources/L1_Health/function-health/2026-10-02/hemoglobin-a1c-hba1c.md) |
| Insulin | uIU/mL | 10.9 (May 19) | 12.5 (Oct 2) | +1.6 (+15%) | In range | <= 18.4 | [2,5] | [file](../00-Raw_Sources/L1_Health/function-health/2026-10-02/insulin.md) |
| Leptin | ng/mL | — | 4.5 (May 19) | — | In range | 1.8-19.9 | [1.8,19.9] | [file](../00-Raw_Sources/L1_Health/function-health/2026-10-02/leptin.md) |
| Uric Acid | mg/dL | — | 6.3 (May 19) | — | In range | 4.0-8.0 | [4,5.5] | [file](../00-Raw_Sources/L1_Health/function-health/2026-10-02/uric-acid.md) |

## Nutrients

Explainers: [[L1-Health/biomarker-digest-nutrients]]

| Biomarker | Unit | Previous | Latest | Change | Status | Quest range | Function optimal | Source |
|---|---|---|---|---|---|---|---|---|
| Arachidonic Acid/EPA Ratio |  | — | 20.2 (May 19) | — | In range | [3.7,40.7] | [3.7,40.7] | [file](../00-Raw_Sources/L1_Health/function-health/2026-10-02/arachidonic-acidepa-ratio.md) |
| Ferritin | ng/mL | — | 98 (May 19) | — | In range | 38-380 | [70,150] | [file](../00-Raw_Sources/L1_Health/function-health/2026-10-02/ferritin.md) |
| Homocysteine | umol/L | — | 10.0 (May 19) | — | In range | < or = 13.5 | [6,8] | [file](../00-Raw_Sources/L1_Health/function-health/2026-10-02/homocysteine.md) |
| Iron | mcg/dL | — | 89 (May 19) | — | In range | 50-180 | [50,180] | [file](../00-Raw_Sources/L1_Health/function-health/2026-10-02/iron.md) |
| Iron % Saturation | % (calc) | — | 29 (May 19) | — | In range | 20-48 | [20,48] | [file](../00-Raw_Sources/L1_Health/function-health/2026-10-02/iron-percent-saturation.md) |
| Iron Binding Capacity | mcg/dL (calc) | — | 305 (May 19) | — | In range | 250-425 | [250,450] | [file](../00-Raw_Sources/L1_Health/function-health/2026-10-02/iron-binding-capacity.md) |
| Magnesium, RBC | mg/dL | — | 6.4 (May 19) | — | In range | [4,6.4] | [5,6.4] | [file](../00-Raw_Sources/L1_Health/function-health/2026-10-02/magnesium-rbc.md) |
| Methylmalonic Acid (MMA) | nmol/L | — | 91 (May 19) | — | In range | 55-335 | [87,250] | [file](../00-Raw_Sources/L1_Health/function-health/2026-10-02/methylmalonic-acid-mma.md) |
| Omega 6 / 3 Ratio |  | — | 8.3 (May 19) | — | In range | [3.7,14.4] | [2,4] | [file](../00-Raw_Sources/L1_Health/function-health/2026-10-02/omega-6-3-ratio.md) |
| Omega-3 Total | % by wt | — | 5.0 (May 19) | — | In range | — | — | [file](../00-Raw_Sources/L1_Health/function-health/2026-10-02/omega-3-total.md) |
| Omega-3 Total / OmegaCheck | % by wt | — | 5.0 (May 19) | — | Below | [5.5,) | (5.4,) | [file](../00-Raw_Sources/L1_Health/function-health/2026-10-02/omega-3-total-omegacheck.md) |
| Omega-3: DHA | % by wt | — | 3.0 (May 19) | — | In range | [1.4,5.1] | [1.4,5.1] | [file](../00-Raw_Sources/L1_Health/function-health/2026-10-02/omega-3-dha.md) |
| Omega-3: DPA | % by wt | — | 1.4 (May 19) | — | In range | [0.8,1.8] | [0.8,1.8] | [file](../00-Raw_Sources/L1_Health/function-health/2026-10-02/omega-3-dpa.md) |
| Omega-3: EPA | % by wt | — | 0.7 (May 19) | — | In range | [0.2,2.3] | [0.2,2.3] | [file](../00-Raw_Sources/L1_Health/function-health/2026-10-02/omega-3-epa.md) |
| Omega-6 Total | % by wt | — | 41.7 (May 19) | — | In range | — | — | [file](../00-Raw_Sources/L1_Health/function-health/2026-10-02/omega-6-total.md) |
| Omega-6: Arachidonic Acid | % by wt | — | 13.7 (May 19) | — | In range | 8.6-15.6 | [8.6,15.6] | [file](../00-Raw_Sources/L1_Health/function-health/2026-10-02/omega-6-arachidonic-acid.md) |
| Omega-6: Linoleic Acid | % by wt | — | 25.0 (May 19) | — | In range | [18.6,29.5] | [18.6,29.5] | [file](../00-Raw_Sources/L1_Health/function-health/2026-10-02/omega-6-linoleic-acid.md) |
| Vitamin D | ng/mL | 54 (May 19) | 52 (Oct 2) | -2 (-4%) | In range | 30 - 100 | [45,100] | [file](../00-Raw_Sources/L1_Health/function-health/2026-10-02/vitamin-d.md) |
| Zinc | mcg/dL | — | 75 (May 19) | — | In range | [60,130] | [60,130] | [file](../00-Raw_Sources/L1_Health/function-health/2026-10-02/zinc.md) |

## Pancreas

Explainers: [[L1-Health/biomarker-digest-pancreas]]

| Biomarker | Unit | Previous | Latest | Change | Status | Quest range | Function optimal | Source |
|---|---|---|---|---|---|---|---|---|
| Amylase | U/L | — | 46 (May 19) | — | In range | 21-101 | [21,101] | [file](../00-Raw_Sources/L1_Health/function-health/2026-10-02/amylase.md) |
| Lipase | U/L | — | 35 (May 19) | — | In range | 7-60 | [7,60] | [file](../00-Raw_Sources/L1_Health/function-health/2026-10-02/lipase.md) |

## Stress & Aging

Explainers: [[L1-Health/biomarker-digest-stress-aging]]

| Biomarker | Unit | Previous | Latest | Change | Status | Quest range | Function optimal | Source |
|---|---|---|---|---|---|---|---|---|
| Cortisol | mcg/dL | 8.0 (May 19) | 14.7 (Oct 2) | +6.7 (+84%) | In range | 4 - 22 | [4,22] | [file](../00-Raw_Sources/L1_Health/function-health/2026-10-02/cortisol.md) |
| DHEA Sulfate | mcg/dL | 234 (May 19) | 212 (Oct 2) | -22 (-9%) | In range | 93 - 415 | [93,415] | [file](../00-Raw_Sources/L1_Health/function-health/2026-10-02/dhea-sulfate.md) |
| Insulin-like Growth Factor (IGF-1) | ng/mL | — | 190 (May 20) | — | In range | 53-331 | [130,190] | [file](../00-Raw_Sources/L1_Health/function-health/2026-10-02/insulin-like-growth-factor-igf-1.md) |
| Z Score | SD | — | 0.6 (May 20) | — | In range | [-2.0,2.0] | — | [file](../00-Raw_Sources/L1_Health/function-health/2026-10-02/z-score.md) |

## Thyroid

Explainers: [[L1-Health/biomarker-digest-thyroid]]

| Biomarker | Unit | Previous | Latest | Change | Status | Quest range | Function optimal | Source |
|---|---|---|---|---|---|---|---|---|
| Thyroglobulin Antibodies (TgAb) | IU/mL | — | <2 (May 19) | — | In range | <=2 | (,1] | [file](../00-Raw_Sources/L1_Health/function-health/2026-10-02/thyroglobulin-antibodies-tgab.md) |
| Thyroid Peroxidase Antibodies (TPO) | IU/mL | — | <1 (May 19) | — | In range | <9 | [0,9] | [file](../00-Raw_Sources/L1_Health/function-health/2026-10-02/thyroid-peroxidase-antibodies-tpo.md) |
| Thyroid-Stimulating Hormone (TSH) | mIU/L | — | 1.08 (May 19) | — | In range | 0.4-4.50 | [0.45,2] | [file](../00-Raw_Sources/L1_Health/function-health/2026-10-02/thyroid-stimulating-hormone-tsh.md) |
| Thyroxine (T4) Free | ng/dL | — | 1.5 (May 19) | — | In range | 0.8-1.8 | [1,1.5] | [file](../00-Raw_Sources/L1_Health/function-health/2026-10-02/thyroxine-t4-free.md) |
| Triiodothyronine (T3) Free | pg/mL | — | 3.6 (May 19) | — | In range | 2.3-4.2 | [3,4.4] | [file](../00-Raw_Sources/L1_Health/function-health/2026-10-02/triiodothyronine-t3-free.md) |

## Urine

Explainers: [[L1-Health/biomarker-digest-urine]]

| Biomarker | Unit | Previous | Latest | Change | Status | Quest range | Function optimal | Source |
|---|---|---|---|---|---|---|---|---|
| Appearance - Urine |  | CLEAR (May 19) | CLEAR (Oct 2) | — | In range | CLEAR | Clear | [file](../00-Raw_Sources/L1_Health/function-health/2026-10-02/appearance-urine.md) |
| Bacteria - Urine | /HPF | NONE SEEN (May 19) | NONE SEEN (Oct 2) | — | In range | NONE SEEN | NONE SEEN | [file](../00-Raw_Sources/L1_Health/function-health/2026-10-02/bacteria-urine.md) |
| Bilirubin - Urine |  | NEGATIVE (May 19) | NEGATIVE (Oct 2) | — | In range | NEGATIVE | NEGATIVE | [file](../00-Raw_Sources/L1_Health/function-health/2026-10-02/bilirubin-urine.md) |
| Color - Urine |  | YELLOW (May 19) | YELLOW (Oct 2) | — | In range | YELLOW | Yellow | [file](../00-Raw_Sources/L1_Health/function-health/2026-10-02/color-urine.md) |
| Glucose - Urine |  | NEGATIVE (May 19) | NEGATIVE (Oct 2) | — | In range | NEGATIVE | NEGATIVE | [file](../00-Raw_Sources/L1_Health/function-health/2026-10-02/glucose-urine.md) |
| Hyaline Casts - Urine | /LPF | NONE SEEN (May 19) | NONE SEEN (Oct 2) | — | In range | NONE SEEN | NONE SEEN | [file](../00-Raw_Sources/L1_Health/function-health/2026-10-02/hyaline-casts-urine.md) |
| Ketones - Urine |  | NEGATIVE (May 19) | NEGATIVE (Oct 2) | — | In range | NEGATIVE | NEGATIVE | [file](../00-Raw_Sources/L1_Health/function-health/2026-10-02/ketones-urine.md) |
| Leukocyte Esterase - Urine |  | NEGATIVE (May 19) | NEGATIVE (Oct 2) | — | In range | NEGATIVE | NEGATIVE | [file](../00-Raw_Sources/L1_Health/function-health/2026-10-02/leukocyte-esterase-urine.md) |
| Nitrite - Urine |  | NEGATIVE (May 19) | NEGATIVE (Oct 2) | — | In range | NEGATIVE | NEGATIVE | [file](../00-Raw_Sources/L1_Health/function-health/2026-10-02/nitrite-urine.md) |
| Occult Blood - Urine |  | NEGATIVE (May 19) | NEGATIVE (Oct 2) | — | In range | NEGATIVE | NEGATIVE | [file](../00-Raw_Sources/L1_Health/function-health/2026-10-02/occult-blood-urine.md) |
| pH - Urine |  | 8.0 (May 19) | 7.0 (Oct 2) | -1 (-12%) | In range | 5 - 8 | [5,8] | [file](../00-Raw_Sources/L1_Health/function-health/2026-10-02/ph-urine.md) |
| Protein - Urine |  | NEGATIVE (May 19) | NEGATIVE (Oct 2) | — | In range | NEGATIVE | NEGATIVE | [file](../00-Raw_Sources/L1_Health/function-health/2026-10-02/protein-urine.md) |
| Red Blood Cell (RBC) - Urine | /HPF | NONE SEEN (May 19) | NONE SEEN (Oct 2) | — | In range | <= 2 | [0,2] | [file](../00-Raw_Sources/L1_Health/function-health/2026-10-02/red-blood-cell-rbc-urine.md) |
| Specific Gravity - Urine |  | 1.005 (May 19) | 1.011 (Oct 2) | +0.006 (+1%) | In range | 1.001 - 1.035 | [1.001,1.035] | [file](../00-Raw_Sources/L1_Health/function-health/2026-10-02/specific-gravity-urine.md) |
| Squamous Epithelial Cells - Urine | /HPF | NONE SEEN (May 19) | NONE SEEN (Oct 2) | — | In range | <= 5 | [0,5] | [file](../00-Raw_Sources/L1_Health/function-health/2026-10-02/squamous-epithelial-cells-urine.md) |
| White Blood Cell (WBC) - Urine | /HPF | NONE SEEN (May 19) | NONE SEEN (Oct 2) | — | In range | <= 5 | — | [file](../00-Raw_Sources/L1_Health/function-health/2026-10-02/white-blood-cell-wbc-urine.md) |
