---
title: "Query — September 2026 Spend"
type: query
pillar_id: L5
owner: Gilberto Silva Gonzalez
created: 2026-10-24
last_updated: 2026-10-24
status: active
tags: [l5, finance, spend, september, query]
source_file: "L5-Finance/transactions-2026-jan-oct.csv"
related: [L5-Finance/transaction-analysis-2026-jan-oct, L5-Finance/_pillar, L5-Finance/expense-categorization-schema]
---

# Query — How much did I spend in September 2026?

**Answer: $24,374.51** in September 2026, using the vault's standard method (regular transactions, excluding rows tagged `To Review`). Including the 8 `To Review` rows ($419.03), the all-in figure is **$24,793.54**. Income for the month was $19,961.11, so September closed **−$4,413.40** net. Source: [[L5-Finance/transaction-analysis-2026-jan-oct]] §1 and the ledger `transactions-2026-jan-oct.csv` (198 September rows, 0 pending).

## Spend by group

| Group | Total | Txns | Share |
|---|---|---|---|
| NEEDS | $8,459.17 | 41 | 34.7% |
| WANTS JOINT | $8,436.41 | 105 | 34.6% |
| SAVINGS / DEBT | $5,902.86 | 11 | 24.2% |
| PERSONAL GIL | $851.69 | 15 | 3.5% |
| PERSONAL LU | $724.38 | 9 | 3.0% |
| **Total** | **$24,374.51** | **181** | 100% |

## Largest subcategories

| Subcategory | Group | Total | Txns |
|---|---|---|---|
| Loans | SAVINGS / DEBT | $4,913.36 | 7 |
| Travel & Vacation Joint | WANTS JOINT | $3,921.28 | 41 |
| Mortgage | NEEDS | $3,294.67 | 2 |
| Groceries | NEEDS | $1,565.76 | 8 |
| Bars & Nightlife - Joint | WANTS JOINT | $1,476.68 | 12 |
| Restaurants - Joint | WANTS JOINT | $1,288.48 | 25 |
| Subscriptions | WANTS JOINT | $1,277.71 | 16 |
| Car + Gas | NEEDS | $1,004.02 | 13 |
| Retirement | SAVINGS / DEBT | $725.00 | 1 |
| Home Everbe | NEEDS | $718.25 | 5 |

Largest single charges: Freedom Mtg Pymts $3,292.68 (9/1), Best Egg Payment $1,251.50 (9/2), Best Egg Payment $1,142.96 (9/21), First Tech FCU external transfer $1,104.21 (9/12), Renewal Membership Fee $895.00 (9/14), United of Omaha premium $725.00 (9/3).

## Observations

- **Fixed obligations dominate:** the mortgage payment ($3,292.68), loan payments ($4,913.36), and the Omaha premium ($725.00) total $8,931.04, or 36.6% of the month's spend.
- **Travel drove discretionary spend:** 41 joint travel transactions cost $3,921.28, more than any WANTS JOINT line.
- **September is the sixth net-negative complete month** of 2026 (income $19,961.11 vs. spend $24,374.51). The prior five were Feb–Jun.
- **Credits are netted in:** 8 negative regular rows (−$368.60 combined) reduce the total.

## Caveats

- The `Loans` figure includes the `Best Egg` payments. The $29,331.20 Marlette loan (Aug 19) is not in September's figures.
- 8 September rows tagged `To Review` ($419.03) are excluded from the headline and await Gil's categorization.
- Internal transfers are absent from the export by design.
