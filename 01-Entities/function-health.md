---
title: "Function Health"
type: entity
entity_type: organization
owner: Gilberto Silva Gonzalez
status: active
created: 2026-10-25
last_updated: 2026-10-25
tags: [entity, organization, l1, l5, blood-testing, biomarkers]
sources:
  - 00-Raw_Sources/L1_Health/function-health/2026-10-02/
related: [L1-Health/function-health-registry, L1-Health/blood-analysis, L1-Health/blood-analysis-function-may2026, L1-Health/blood-analysis-function-oct2026, L1-Health/_pillar, L5-Finance/transaction-analysis-2026-jan-oct]
---

# Function Health

**What it is:** blood-testing membership service (my.functionhealth.com). Function reports each biomarker against the lab's reference range and against its own tighter "optimal" range, and writes an explainer for each marker. Gil's panels use the Quest reference ranges shown in the export.
**Role in the vault:** primary source of L1 blood data since May 2026. Earlier panels (2022 to Jan 2026) came from Spren and other providers; see [[L1-Health/blood-analysis]].

## Draws

| Draw | Biomarkers | Analysis |
|---|---|---|
| May 19, 2026 (first panel) | 123 (incl. 40 not retested in Oct) | [[L1-Health/blood-analysis-function-may2026]] |
| Oct 2, 2026 (second panel) | 83 (the 40 May-only markers have no Oct result) | [[L1-Health/blood-analysis-function-oct2026]] |

- **All values and ranges:** [[L1-Health/function-health-registry]] (generated, 123 rows).
- **Explainers by category:** 15 digest pages listed under "L1 Biomarker Digests" in [[02-Indexes/index]].
- **Out of range on Oct 2:** 7 biomarkers (ALT, AST, hs-CRP, LDL Particle Number, LDL Medium, LDL Small, OmegaCheck); see [[L1-Health/liver-enzymes-alt-ast-oct2026]] for the liver flags.

## Data Pipeline

- **Raw files:** one Markdown file per biomarker in `00-Raw_Sources/L1_Health/function-health/<draw-date>/` (immutable), plus a PDF reconciliation report (132 of 132 PDF entries matched).
- **Extraction:** project skill `function-health-extract` (`.claude/skills/function-health-extract/`) through Claude in Chrome in Gil's logged-in session.
- **Gap:** Biological Age appears in the account but has no biomarker page, so the vault holds no value for it.
- **Privacy rule:** the Function PDF header carries a date of birth and full name. Neither goes into any vault file.

## Cost (L5)

The Jan–Oct 2026 ledger lists three Function Health charges, all categorized Healthcare / NEEDS: $365 and $199 on 2026-05-18, and $326 on 2026-09-28, $890 in total (ledger CSV `L5-Finance/transactions-2026-jan-oct.csv`; analysis in [[L5-Finance/transaction-analysis-2026-jan-oct]]). The ledger does not say what each charge covers.

## Why This Matters Across Pillars

- **L1:** the Oct panel drives the current alert list in [[L1-Health/_pillar]] (liver, LDL particles, hs-CRP, Free T) and the proposed protocol changes.
- **L5:** recurring healthcare spend inside the NEEDS group ([[L5-Finance/_pillar]]).
- **L3:** the testosterone-to-Deep-Work chain in [[02-Indexes/topic_maps/health-performance-crossmap]] rests on Function data.

## Notes

- Function's own ranges disagree in places (MCV 85–90 vs 85–95 fL; omega-3 doses); the digest ingest entry in `03-System_Logs/log.md` records them.
- Refresh the registry and digests after each new draw by following the skill.
