---
title: "Transaction Analysis — Jan–Oct 2026"
type: analysis
pillar_id: L5
owner: Gilberto Silva Gonzalez
created: 2026-10-24
last_updated: 2026-10-24
status: active
tags: [l5, finance, budget, transactions, analysis, cash-flow]
source_file: "00-Raw_Sources/L5_Finances/2026-YTD-Jan-1-Oct-24.csv"
supersedes: "L5-Finance/transaction-analysis-2026-jan-aug.md"
related: [L5-Finance/_pillar, L5-Finance/household-income-2026, L5-Finance/expense-categorization-schema, L5-Finance/transactions-2026-jan-oct.csv, 02-Indexes/topic_maps/household-finance-relationship-map]
---

# Transaction Analysis — Jan–Oct 2026

Full-ledger analysis of every transaction from 2026-01-01 through 2026-10-23, computed by script against [[L5-Finance/expense-categorization-schema]]'s routing rules. The validated, annotated ledger lives in [`transactions-2026-jan-oct.csv`](transactions-2026-jan-oct.csv). This file holds the summary and the findings.

**This file supersedes and replaces `transaction-analysis-2026-jan-aug.md` and `transactions-2026-jan-aug.csv`.** Gil and Luisa updated their inputs and re-exported the full 2026 history. The new export (`2026-YTD-Jan-1-Oct-24.csv`) is the sole source of truth for all 2026 transactions. The prior raw exports stay untouched in `00-Raw_Sources` (immutable by policy); only their derived L5 outputs are retired. The [[03-System_Logs/log|system log]] records the full operation.

**Data scope (2026-10-24 export):** 1,876 rows — 1,751 regular, 125 income, **0 internal transfers**. Gil left transfers out of this export on purpose, so the transfer analysis from prior ingests no longer applies. 5 rows carry `pending` status (all dated 2026-10-23); this analysis counts them without a flag. **October is a partial month** (Oct 1–23).

**Method note (unchanged from prior ingests):** income = negated sum of `income` rows; spend = sum of `regular` rows *excluding* those tagged `To Review`. In this export, income carries a negative sign and spend a positive sign, so a negative `regular` amount is an inflow.

---

## 0. Supersession Note — What Changed vs. the Jan–Aug Ingest

Recomputing the identical Jan 1 – Aug 16 window from the new export:

| Period | Old net (Jan–Aug export) | New net (this export) | Δ |
|---|---|---|---|
| 2026-01 through 2026-04 | *(unchanged, see §1)* | *(unchanged)* | $0.00 |
| 2026-05 | −$489.53 | −$691.14 | −$201.61 |
| 2026-06 | −$3,642.44 | −$3,793.76 | −$151.32 |
| 2026-07 | +$9,497.69 | +$9,094.71 | −$402.98 |
| 2026-08 (1st–16th) | −$3,070.70 | −$3,422.95 | −$352.25 |
| **Jan 1 – Jul 31** | **+$6,288.27** | **+$5,532.36** | **−$755.91** |
| **Jan 1 – Aug 16** | **+$3,217.57** | **+$2,109.41** | **−$1,108.16** |

Income for the window did not change ($162,604.68). Spend rose by $1,108.16, all of it in May–August. January through April match the prior ingest to the cent.

**What changed in the data:**

- **90 rows were recategorized** (same date, name, amount, and account). 78 are travel-related: 69 moved from the generic `Travel & Vacation` bucket into owner-specific subcategories (`Travel & Vacation Joint` 43, `Travel & Vacation Lu` 21 moved to PERSONAL LU, `Travel & Vacation Gil` 5 moved to PERSONAL GIL), 6 moved from `Bar & Restaurants Lu` into `Travel & Vacation Lu`, and 3 moved from Groceries or blank into a travel subcategory. The other 12 are scattered fixes: 3 `Shops & Clothing Lu` → `Subscriptions`, 2 `Shops & Clothing Lu` → `Home Everbe`, 2 `Archive/Apartments-Houses` → `Home Everbe`, 2 blank → `CC min payments`, and 3 single-row moves. 14 rows also changed tags.
- **12 rows left and 18 rows joined** the Jan 1 – Aug 15 window. Most of the churn is renamed duplicates (e.g., `Foxtail Coffee - 1097 - Canvas` → `Foxtail Coffee`, `Everbe Master Property Own` → `Propay`, `Jetblue` $377.40 → $313.40). The additions also include small items dated Jul 22 – Aug 8 with no account detail (Regal Cinemas $61.74, two PayByPhone charges, Uber, Apple, and interest/deposit credits). Three `Online-mobile Recurring` −$35.00 credits dropped out.
- **233 of 236 internal transfers disappeared** by design (see Data scope).
- **To Review count rose from 26 to 42.** 7 prior items cleared (Credit Balance Refund $101.00, Renewal Membership Fee $195.00 on 7/15, Care.com, Kindle, Zelle to Osiel, Lemonade, and Home Depot $596.88); 19 carry over; 23 are new (see §7).
- **Jan–Aug net-negative month count is unchanged:** Feb, Mar, Apr, May, Jun are still negative. September adds a sixth (§1).

Treat this document and `transactions-2026-jan-oct.csv` as authoritative. Do not reconcile against the retired Jan–Aug figures.

---

## 1. Cash Flow — Jan 1 through Oct 23, 2026

| Month | Income | Spend | Net |
|---|---|---|---|
| 2026-01 | $23,033.37 | $17,612.52 | **+$5,420.85** |
| 2026-02 | $15,045.66 | $15,251.97 | −$206.31 |
| 2026-03 | $31,669.42 | $32,405.73 | −$736.31 |
| 2026-04 | $14,585.93 | $18,141.61 | −$3,555.68 |
| 2026-05 | $20,367.08 | $21,058.22 | −$691.14 |
| 2026-06 | $19,253.68 | $23,047.44 | −$3,793.76 |
| 2026-07 | $29,022.72 | $19,928.01 | **+$9,094.71** |
| 2026-08 | $19,273.74 | −$11,475.08 | **+$30,748.82** ⚠ |
| 2026-09 | $19,961.11 | $24,374.51 | −$4,413.40 |
| 2026-10 (partial, Oct 1–23) | $20,278.80 | $14,571.40 | +$5,707.40 |
| **YTD (Jan 1 – Oct 23)** | **$212,491.51** | **$174,916.33** | **+$37,575.18** |

### ⚠ Critical finding — a $29,331.20 loan inflow distorts August

On 2026-08-19, a `regular`-type row `Transfer Cross River Bank From Marlette Funding` posted at **−$29,331.20** (account Adv Plus Banking, tags `Loan, Lu`, no category). The method counts negative `regular` rows as negative spend, so this loan **proceeds** inflow turns August spend negative and inflates net by $29,331.20. A loan inflow is financing, not earned income. This analysis keeps the headline method for continuity and reports an adjusted view alongside it:

| View | Aug net | Jan–Sep net (9 complete months) | YTD net (through Oct 23) |
|---|---|---|---|
| Headline (method unchanged) | +$30,748.82 | +$31,867.78 | +$37,575.18 |
| **Adjusted (excludes the $29,331.20 loan proceeds)** | **+$1,417.62** | **+$2,536.58** | **+$8,243.98** |

Use the adjusted view when judging the "12 months of positive cash flow" OKR. No `Marlette` or `Cross River` repayment rows appear after 8/19. The last `Upstart Network` loan payment ($613.89) posted 2026-07-29, and none follow. Whether the Marlette proceeds refinanced the Upstart loan is unconfirmed; Gil should state the loan's purpose and terms. The row's category stays blank, not reassigned.

### Month-level read (adjusted for the loan)

- **6 of 9 complete months closed net-negative** (Feb, Mar, Apr, May, Jun, Sep). Net-positive months: Jan, Jul, Aug.
- **October is partial.** The +$5,707.40 covers Oct 1–23 only (including 5 pending rows dated 10/23) and must not be compared with complete months.
- Income stays steady at roughly $19–20K per month from June onward (excluding the July $29.0K and March $31.7K spikes).

**Recommendation:** the 12-month positive-cash-flow OKR is not met month-by-month. Reframe it around a rolling or YTD target. See the open gap in [[02-Indexes/topic_maps/household-finance-relationship-map]].

---

## 2. Mortgage — Three Recurring Payments Now in the Ledger

| Date | Transaction | Amount | Category in export |
|---|---|---|---|
| 2026-08-04 | Freedom Mtg Pymts | $3,292.68 | Mortgage / NEEDS |
| 2026-09-01 | Freedom Mtg Pymts | $3,292.68 | Mortgage / NEEDS |
| 2026-10-01 | Freedom Mtg Pymts | $3,292.68 | **Loans / SAVINGS-DEBT** |

The payment holds flat at **$3,292.68** across three months. The October payment carries a different category (`Loans`) than August and September (`Mortgage`). The export categorizes it that way, so this analysis does not move it, but it shifts $3,292.68 from NEEDS to SAVINGS / DEBT. Gil should confirm which bucket he intends.

One-time Mortgage-bucket costs (unchanged from prior ingests): Pulte North Florida $5,000.00 (3/1), Pulte Mortgage $947.00 (3/17), Pulte Home Comp $10,000.00 (3/31), Neptune flood insurance $589.93 (5/11), PGP Title wire $1,472.33 and wire fee $25.00 (6/1) — **$18,034.26** total.

**Mortgage subcategory total: $24,858.60 across 11 transactions** = $18,034.26 one-time + $6,585.36 recurring (Aug and Sep) + **$238.98 of HOA and dues** (Everbe Master Property $235.00 on 10/2 and two $1.99 Integrators Assn dues). The schema assigns HOA fees to **Home Everbe**, not Mortgage, so the $238.98 likely belongs under Home Everbe. As before, the $589.93 flood-insurance payment likely belongs under Insurance. This analysis flags both and moves neither.

---

## 3. MPI Naming Question — Still Unconfirmed, New Observations

- The $5,500 Mutual of Omaha row (2026-03-23, tag `MPI`) appears as **−$5,500.00** with a blank category. In this export's sign convention (income = negative), a negative amount is an **inflow**. Prior vault pages describe it as a payment *to* Mutual of Omaha. Gil should confirm the direction: contribution, withdrawal, loan, or refund.
- The **Retirement** subcategory totals **$7,250.00 across 10 transactions** — ten monthly `United Of Omaha - Ins Prem` debits of **$725.00** (Jan 5 through Oct 5). The prior ingest showed $5,800.00 over 8 transactions, the same payment stream. United of Omaha Life Insurance Company operates within the Mutual of Omaha group, which strengthens the link between the `MPI` row and an Omaha-based insurance product.
- 2 rows tagged `Reputation/MCI` (Tmone Llc Payroll, 2026-03-28, $1,106.25 and $1,446.64; $2,552.89 total) are income, unrelated to MPI.

**Status:** strong evidence that MPI is an Omaha-group vehicle, but not confirmed. See [[02-Indexes/topic_maps/household-finance-relationship-map]].

---

## 4. Spend by Main Category (Regular Transactions Only, Jan 1 – Oct 23)

| Group | Total | Txns |
|---|---|---|
| NEEDS | $88,609.52 | 448 |
| SAVINGS / DEBT | $56,667.46 | 186 |
| WANTS JOINT | $35,380.32 | 648 |
| PERSONAL GIL | $13,933.38 | 176 |
| PERSONAL LU | $13,923.92 | 234 |
| Taxes *(ungrouped — schema gap)* | $802.67 | 3 |
| Apartments-Houses / Archive *(ungrouped — schema gap)* | $283.01 | 2 |
| Church *(ungrouped — new schema gap)* | $63.39 | 6 |
| Blank category (includes the $29,331.20 loan inflow and the −$5,500 MPI row) | −$34,747.34 | 6 |
| **Total regular spend** | **$174,916.33** | **1,709** |

*(42 additional `To Review`-tagged regular transactions are excluded from this table — see §7.)*

### NEEDS

| Subcategory | Total | Txns |
|---|---|---|
| Mortgage *(see §2)* | $24,858.60 | 11 |
| CIRRUS (Rent + Water + Storage) | $15,866.92 | 7 |
| Groceries | $13,351.71 | 132 |
| Car + Gas | $10,655.05 | 112 |
| Home Everbe | $9,576.37 | 54 |
| Healthcare | $4,624.08 | 37 |
| Luna | $3,562.04 | 39 |
| Phones | $2,454.44 | 30 |
| Electricity | $2,109.85 | 13 |
| Insurance | $1,550.46 | 13 |

### SAVINGS / DEBT

| Subcategory | Total | Txns |
|---|---|---|
| Loans *(includes the 10/1 Freedom Mtg payment, $3,292.68)* | $43,573.28 | 68 |
| Retirement *(10 × $725 United of Omaha premium)* | $7,250.00 | 10 |
| CC min payments | $5,844.18 | 108 |

### WANTS JOINT

| Subcategory | Total | Txns |
|---|---|---|
| Travel & Vacation Joint | $10,073.45 | 90 |
| Restaurants - Joint | $9,744.67 | 171 |
| Bars & Nightlife - Joint | $5,442.69 | 53 |
| Other | $4,486.64 | 120 |
| Subscriptions | $3,961.79 | 170 |
| Eight Sleep - Affirm | $646.68 | 4 |
| Transportation (Uber) | $590.48 | 36 |
| Entertainment | $433.92 | 4 |

`Entertainment` is now active (4 transactions), contrary to the schema note that it sits largely dormant. `Sports` and `Immigration` still show $0.

### PERSONAL LU / PERSONAL GIL

| PERSONAL LU | Total | Txns | | PERSONAL GIL | Total | Txns |
|---|---|---|---|---|---|---|
| Family Lu | $6,294.10 | 38 | | Family Gil | $8,335.38 | 75 |
| Shops & Clothing Lu | $2,725.39 | 119 | | Shops & Clothing Gil | $2,034.75 | 42 |
| Travel & Vacation Lu | $2,583.55 | 29 | | Bar & Restaurants Gil | $1,953.23 | 47 |
| Personal Care Lu | $1,048.65 | 18 | | Travel & Vacation Gil | $1,176.52 | 4 |
| Bar & Restaurants Lu | $893.91 | 22 | | Personal Image Gil | $433.50 | 8 |
| Lu Recruitment Business | $378.32 | 8 | | | | |

---

## 5. Tag Analysis (New)

The prior exports carried almost no tags. This export populates them. Tags are not mutually exclusive, and the `To Review` tag appears separately in §7.

| Tag | Type | Txns | Total | Note |
|---|---|---|---|---|
| Blue Origin | income | 74 | $182,733.75 | Payroll income for both earners; 86% of YTD income |
| Variable Income | income | 7 | $18,442.57 | Gil's tag for irregular income |
| Reputation/MCI | income | 2 | $2,552.89 | Tmone Llc payroll, 2026-03-28 |
| Gas | regular | 40 | $1,782.70 | Fuel purchases, per schema's "tag gas explicitly" rule |
| Dayana Cleaning | regular | 10 | $1,460.00 | Payments tagged to the cleaning provider |
| Gil | regular | 12 | $1,248.58 | Individually labeled Gil spend |
| Tolls | regular | 16 | $640.00 | Toll charges |
| Lu | regular | 27 | −$27,311.25 | Includes the −$29,331.20 loan; **+$2,019.95 excluding it** |
| MPI | regular | 1 | −$5,500.00 | See §3 |
| Loan | regular | 1 | −$29,331.20 | See §1 |

`Dayana Cleaning` suggests a recurring service provider, but 10 transactions do not yet justify an entity page. Revisit after the next ingest.

---

## 6. Schema Gaps Found (Original Categories Preserved, Not Reassigned)

| Category | Total | Txns | Issue |
|---|---|---|---|
| Taxes | $802.67 | 3 | Not in any schema group (TurboTax, IRS payment, service fee, all 2026-03-02). Unchanged since the first ingest. |
| Church | $63.39 | 6 | **New.** St. Isaac Jogues payments (Aug 16 – Oct 4) with no parent group. The schema defines no giving/donations subcategory. |
| Apartments-Houses (Archive) | $283.01 | 2 | Two Lowe's purchases on 2026-05-30. The August rows that shared this label moved to `Home Everbe` in the new export, which resolves part of the prior gap. |
| Blank category — loan inflow | −$29,331.20 | 1 | See §1. |
| Blank category — MPI | −$5,500.00 | 1 | See §3. |
| Blank category — City of Cocoa water | $84.53 | 2 | No water-utility subcategory exists (Electricity is electric-only). Unchanged. |
| Blank category — Interest | −$0.67 | 2 | Bank interest credits, immaterial. |
| Subcategory names not in the schema doc | — | 4 names | `Travel & Vacation Joint`, `Travel & Vacation Lu`, `Travel & Vacation Gil` (see §0) and `Entertainment` activity. The schema doc names only `Travel & Vacation`. Validation accepted these as valid because the schema's system note says explicit Gil/Lu labels mark individual travel. Update [[L5-Finance/expense-categorization-schema]] to list them. |

---

## 7. Pending Gil's Review (42 Transactions, Tagged "To Review")

These carry Gil's own `To Review` tag. This analysis does not categorize them and excludes them from the §1 and §4 totals. 19 carry over from the Jan–Aug list; **23 are new** (marked NEW). Amazon charges make up 21 of the 42.

| Date | Transaction | Amount | Account |
|---|---|---|---|
| 2026-01-06 | Withdrawal Silva Gonzalez From | $600.00 | First Tech Rewards Checking |
| 2026-05-16 | Transaction: Rmtly* M85be 1111 Third Ave., Suite | $701.99 | First Tech Rewards Checking |
| 2026-05-16 | Methodiq*health | $91.82 | Platinum Card® |
| 2026-05-18 | Kindle Unltd*fy2751o63 | $13.25 | Prime Visa |
| 2026-05-18 | Uber | $9.99 | Platinum Card® |
| 2026-05-18 | Amazon Mktpl*nk86761f3 | $163.42 | Prime Visa |
| 2026-05-19 | Apple.com-bill Internet Charge | $24.28 | Platinum Card® |
| 2026-05-21 | 0095 Dr Phillips Cenorlando | $70.60 | Platinum Card® |
| 2026-05-21 | 0095 Dr Phillips Cenorlando | $59.92 | Platinum Card® |
| 2026-05-29 | Uber | $9.99 | Apple Card |
| 2026-06-07 | Amazon Prime | $5.65 | Platinum Card® |
| 2026-06-08 | Spaceport- Ticketing | $241.82 | Prime Visa |
| 2026-06-10 | Teriyaki Mad Cat 210melbourne | $375.50 | Platinum Card® |
| 2026-06-11 | Transaction: Rmtly* B5ac8 1111 Third Ave., Suite | $151.99 | First Tech Rewards Checking |
| 2026-06-14 | Renewal Membership Fee | $195.00 | Platinum Card® |
| 2026-06-14 | Rentaltoll | $56.30 | Platinum Card® |
| 2026-06-23 | Uber | $9.99 | Platinum Card® |
| 2026-06-24 | Godaddy | $25.64 | Platinum Card® |
| 2026-06-29 | Ach Debit: Applecard Gsbank - Payment **(NEW)** | $95.29 | First Tech Rewards Checking |
| 2026-08-09 | Amazon Mktpl*5h6ye3nh1 | $67.99 | Prime Visa |
| 2026-09-01 | Amazon Mktpl*5q0i466q0 **(NEW)** | $31.05 | Prime Visa |
| 2026-09-04 | American Express **(NEW)** | $70.02 | Platinum Card® |
| 2026-09-08 | Interest Charged On Purchases **(NEW)** | $9.06 | Atmos Rewards Ascent Visa Signature |
| 2026-09-08 | Bank Of America Payment M **(NEW)** | $36.00 | Total Checking |
| 2026-09-16 | Amazon Mktpl*5r5ix **(NEW)** | $133.09 | Prime Visa |
| 2026-09-17 | Amazon Mktpl*5r6at43i2 **(NEW)** | $30.89 | Prime Visa |
| 2026-09-19 | Amazon Mktpl*5r1a19xh0 **(NEW)** | $53.24 | Prime Visa |
| 2026-09-20 | Amazon.com*5r18f82t0 **(NEW)** | $55.68 | Prime Visa |
| 2026-10-01 | American Express Ach **(NEW)** | $20.64 | Total Checking |
| 2026-10-08 | Amazon Mktpl*5e0ie1cz0 **(NEW)** | $112.85 | Prime Visa |
| 2026-10-08 | Amazon Mktpl*5e8lg9c30 **(NEW)** | $34.99 | Prime Visa |
| 2026-10-13 | Amazon Mktpl*hx **(NEW)** | $139.27 | Prime Visa |
| 2026-10-13 | Amazon Mktplu0wc2 **(NEW)** | $127.42 | Prime Visa |
| 2026-10-13 | Amazon Mktpl*5e3ph8cr2 **(NEW)** | $94.79 | Prime Visa |
| 2026-10-15 | Amazon Mktpl*5e28a80u2 **(NEW)** | $170.46 | Prime Visa |
| 2026-10-15 | Amazon Mktpl*5e1hr **(NEW)** | $8.51 | Prime Visa |
| 2026-10-15 | Amazon Mktpl*jq6841b33 **(NEW)** | $8.51 | Prime Visa |
| 2026-10-16 | Amazon.com47v83 **(NEW)** | $12.96 | Prime Visa |
| 2026-10-16 | Amazon Mktpl*601wj1ti3 **(NEW)** | $20.35 | Prime Visa |
| 2026-10-17 | Amazon Mktpl*9a9ws0m73 **(NEW)** | $94.79 | Prime Visa |
| 2026-10-17 | Amazon Mktpl*e90n55w73 **(NEW)** | $35.11 | Prime Visa |
| 2026-10-22 | Amazon Mktpl*h376g7d63 **(NEW)** | $60.59 | Prime Visa |

**To Review total: $4,330.70** across 42 transactions (script-computed sum of `amount`).

---

## Methodology

A Python script (run with `python3 -I`) (1) parsed the raw CSV (1,876 rows, no blank padding), (2) validated each `regular` row's `(parent category, category)` pair against the dictionary in [[L5-Finance/expense-categorization-schema]], extended with the `Travel & Vacation Joint/Lu/Gil` names, (3) summed by group, subcategory, month, and tag, (4) recomputed the same logic against `2026-YTD-Jan-Aug.csv` for the §0 comparison, and (5) matched rows between exports on `(date, name, amount, account mask)` to count recategorizations, removals, and additions. The annotated CSV only adds a `schema_check` column: `OK`, `OK:INCOME`, `TO_REVIEW`, `GAP:BLANK_CATEGORY`, or `GAP:UNMAPPED[parent/category]`. No source value changed; the script asserted that all 13 source columns in the output match the raw file for all 1,876 rows. `OK:TRANSFER` no longer applies because the export has no transfers.
