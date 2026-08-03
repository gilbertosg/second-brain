---
title: "Household Income — 2026 Baseline"
type: financial-data
pillar_id: L5
owner: Gilberto Silva Gonzalez
created: 2026-08-02
last_updated: 2026-08-02
status: active
tags: [l5, finance, income, luisa, budget]
source_file: "00-Raw_Sources/L5_Finances/Household Income Report.md"
related: [L5-Finance/_pillar, L5-Finance/expense-categorization-schema, 01-Entities/luisa, 02-Indexes/topic_maps/household-finance-relationship-map]
---

# Household Income — 2026 Baseline

Baseline net-income logic for the Gil + Luisa household, derived from June 2026 (standard 2-paycheck month) and July 2026 (exceptional 3-paycheck month) snapshots. Both incomes come from the same employer, Blue Origin — Gil for ~3 years 9 months, Luisa since **2026-04-20**.

---

## Gross Income

| | Annual Gross (pre-tax) |
|---|---|
| Gil | $205,000 |
| Luisa | $123,000 |
| **Household** | **$328,000** |

Gil received an annual bonus in March 2026, used entirely for the house down payment (see [[L5-Finance/_pillar]] and the [[02-Indexes/topic_maps/household-finance-relationship-map]] for the home-purchase context).

---

## Net Income — Standard Month (June 2026, 2 Paychecks)

| | Biweekly Net | Monthly Net (2 checks) |
|---|---|---|
| Luisa | $3,563.07 (avg of $3,563.06 / $3,563.07) | $7,126.13 |
| Gil | $6,063.77 (sum of Personal + Bills + Debt allocations) | $12,127.54 |
| **Household** | **$9,626.84** | **$19,253.67** |

**Income split ratio (Gil / Luisa): 62.99% / 37.01%**

## Net Income — Exceptional Month (July 2026, 3 Paychecks)

| | Monthly Net |
|---|---|
| Gil | $18,261.73 |
| Luisa | $10,689.24 |
| **Household** | **$28,950.97** |

**Income split ratio (Gil / Luisa): 63.08% / 36.92%** — consistent with the standard-month ratio; the 3rd paycheck doesn't materially shift the split.

---

## Gil's Biweekly Net Salary — Account Routing

Every Gil paycheck splits three ways at deposit:

| Destination | Account | Standard Biweekly Amount |
|---|---|---|
| Personal | First Tech Rewards Checking (…5948) | $606.38 |
| Debt/Credit/Loans | Total Checking (…7379) | $2,425.51 |
| Bills | Total Checking (…7818) | $3,031.88 |

Luisa's paycheck routes as a single deposit to **Personal/Base — Adv Plus Banking (…0372)**, $3,563.07 standard biweekly. She does not pre-split at the account level the way Gil does; her budget categorization (per [[L5-Finance/expense-categorization-schema]]) happens downstream of that single deposit.

The July 3rd-paycheck deposit ($613.42 Personal / $2,453.68 Debt / $3,067.10 Bills for Gil, $3,563.08 for Luisa) is slightly higher than the standard biweekly figures above — treat the June figures as the stable baseline and July's 3rd check as a modest upside variance, not a new baseline.

---

## Data Gaps

- **MPI baseline not established.** `L5-Finance/_pillar.md`'s "Monthly Passive Income (MPI), grow 10%/month" OKR needs a starting figure to be measurable — this income report does not provide one. Separately, the expense schema references a **"MPI account"** under Retirement contributions, which is almost certainly a *named Blue Origin retirement account*, not the same thing as the "Monthly Passive Income" OKR metric. Treat these as two different concepts until Gil confirms otherwise — see the open gap in [[02-Indexes/topic_maps/household-finance-relationship-map]].
- Full date-by-date transaction log (8 entries for June, 12 for July) is preserved in the immutable raw source at `00-Raw_Sources/L5_Finances/Household Income Report.md` — not re-transcribed here.
