---
title: "Transaction Analysis — Jan–Aug 2026"
type: analysis
pillar_id: L5
owner: Gilberto Silva Gonzalez
created: 2026-08-16
last_updated: 2026-08-16
status: active
tags: [l5, finance, budget, transactions, analysis, cash-flow]
source_file: "00-Raw_Sources/L5_Finances/2026-YTD-Jan-Aug.csv"
supersedes: "L5-Finance/transaction-analysis-2026-jan-jul.md"
related: [L5-Finance/_pillar, L5-Finance/household-income-2026, L5-Finance/expense-categorization-schema, L5-Finance/transactions-2026-jan-aug.csv, 02-Indexes/topic_maps/household-finance-relationship-map]
---

# Transaction Analysis — Jan–Aug 2026

Full-ledger analysis of every transaction from 2026-01-01 through 2026-08-16, computed by script against [[L5-Finance/expense-categorization-schema]]'s routing rules. The validated, annotated transaction-by-transaction ledger lives in [`transactions-2026-jan-aug.csv`](transactions-2026-jan-aug.csv) — this file is the summary and the findings.

**This file supersedes and replaces `transaction-analysis-2026-jan-jul.md` and `transactions-2026-jan-jul.csv`.** Gil confirmed the prior raw source (`00-Raw_Sources/L5_Finances/2026-YTD-Jan-Jul.csv`) contained errors that he and Luisa have since corrected. The new export (`2026-YTD-Jan-Aug.csv`) is the source of truth for all 2026 transactions and extends coverage through August 16. The old raw file remains untouched in `00-Raw_Sources` (immutable by policy) but its downstream L5-Finance outputs have been removed — see the Supersession Note below and the [[03-System_Logs/log|system log]] for the full record.

**Data quality (2026-08-16 export):** 1,702 rows, **zero** blank padding rows — a marked improvement over the Jan–Jul export's 8,541 blank rows out of 10,126. All figures below are computed from all 1,702 rows.

---

## 0. Supersession Note — What Changed vs. the Jan–Jul Ingest

Recomputing the same Jan 1 – Jul 31 window from the corrected source produces materially different totals than the original ingest. This is flagged explicitly rather than silently overwritten:

| Month | Old net (erroneous) | New net (corrected) | Δ |
|---|---|---|---|
| 2026-01 | +$3,674.08 | +$5,420.85 | +$1,746.77 |
| 2026-02 | −$1,420.22 | −$206.31 | +$1,213.91 |
| 2026-03 | −$7,550.85 | −$736.31 | +$6,814.54 |
| 2026-04 | −$3,842.68 | −$3,555.68 | +$287.00 |
| 2026-05 | −$1,610.04 | −$489.53 | +$1,120.51 |
| 2026-06 | −$4,704.34 | −$3,642.44 | +$1,061.90 |
| 2026-07 | +$10,519.73 | +$9,497.69 | −$1,022.04 |
| **Jan–Jul net** | **−$4,934.32** | **+$6,288.27** | **+$11,222.59** |

**The corrected data swings the Jan–Jul cash-flow picture from net-negative to net-positive — an $11,222.59 difference.** The count of net-negative months is unchanged (5 of 7: Feb, Mar, Apr, May, Jun), but the *magnitude* of each deficit dropped substantially, most notably March (−$7,551 → −$736, a $6,815 correction). Spend, not income, drove nearly all of the change — monthly income figures moved by only a few dollars to a few hundred dollars, while spend figures dropped by hundreds to low thousands most months.

Two other corrections worth noting:
- **Date format normalized:** the old raw file stored dates as `M/D/YY`; the new file uses ISO `YYYY-MM-DD`.
- **4 previously-flagged "To Review" items no longer appear as unresolved**, apparently corrected/reclassified: `Tmobile*auto Pay` ($467.27, 2026-05-21), `Zelle Payment To Luisa F Rangel` ($204.00, 2026-06-01), and two `Online-mobile Recurring` (−$35.00 each, 2026-06-05 and 2026-07-05). 2 new items were added for the August extension (see §7).
- **The MPI-tagged Mutual of Omaha transaction's sign flipped:** the old export showed a $5,500 positive amount; the new export shows **−$5,500.00**. Flagged, not resolved — see §3.

Gil should treat this document and `transactions-2026-jan-aug.csv` as authoritative going forward. Do not average or reconcile against the retired Jan–Jul figures.

---

## 1. Cash Flow — Jan 1 through Aug 16, 2026

| Month | Income | Spend | Net |
|---|---|---|---|
| 2026-01 | $23,033.37 | $17,612.52 | **+$5,420.85** |
| 2026-02 | $15,045.66 | $15,251.97 | −$206.31 |
| 2026-03 | $31,669.42 | $32,405.73 | −$736.31 |
| 2026-04 | $14,585.93 | $18,141.61 | −$3,555.68 |
| 2026-05 | $20,367.08 | $20,856.61 | −$489.53 |
| 2026-06 | $19,253.68 | $22,896.12 | −$3,642.44 |
| 2026-07 | $29,022.72 | $19,525.03 | **+$9,497.69** |
| 2026-08 (partial, thru 8/16) | $9,626.82 | $12,697.52 | −$3,070.70 |
| **YTD Total (Jan 1 – Aug 16)** | **$162,604.68** | **$159,387.11** | **+$3,217.57** |

**August is a partial month** (16 of 31 days) — its income figure understates the full month (only 1 of Gil's ~2 biweekly paychecks has likely landed) and should not be compared directly to the other rows or annualized. Excluding August, **Jan–Jul 2026 closed net-positive at +$6,288.27** (see §0) — 5 of 7 months were still individually net-negative, but the year-to-date trend is now positive, reversing the prior ingest's finding.

**Recommendation:** update `L5-Finance/_pillar.md`'s Strategic Context to reflect the corrected trend — cash flow is net-positive YTD, though monthly volatility (5 of 7 months negative) means the "12 months of positive cash flow" OKR still isn't being met on a month-by-month basis.

---

## 2. Mortgage — First Recurring Payment Now Confirmed

The schema doc predicted the first *recurring* mortgage payment would land 2026-08-01 at ~$3,200. The data confirms this:

| Date | Transaction | Amount |
|---|---|---|
| 2026-08-04 | Freedom Mtg Pymts | **$3,292.68** |

This is the first genuine recurring mortgage payment in the ledger — $92.68 above the schema doc's estimate, consistent with a standard escrow/insurance-inclusive payment. All prior "Mortgage" transactions (Jan–Jul) remain one-time home-purchase costs, not recurring payments:

| Date | Transaction | Amount |
|---|---|---|
| 2026-03-01 | Pulte North Florida Ga | $5,000.00 |
| 2026-03-17 | Pulte Mortgage L Pulte Mort | $947.00 |
| 2026-03-31 | Pulte Home Comp Pay | $10,000.00 |
| 2026-05-11 | Neptune Pol Asr4 Neptune Po (flood insurance) | $589.93 |
| 2026-06-01 | Online Domestic Wire Transfer — PGP Title of Florida (10602 Evening Star St, Orlando, FL) | $1,472.33 |
| 2026-06-01 | Online Domestic Wire Fee | $25.00 |

**Mortgage subcategory total, Jan–Aug: $21,326.94** (7 txns) — $18,034.26 in one-time purchase costs plus the first $3,292.68 recurring payment. As previously flagged, the $589.93 Neptune flood-insurance payment likely belongs under **Insurance**, not Mortgage — still not silently moved.

---

## 3. MPI Naming Question — Sign Correction, Still Unconfirmed

The $5,500 Mutual of Omaha transaction tagged `MPI` now appears as **−$5,500.00** on 2026-03-23 (previously +$5,500.00 in the erroneous export). It remains uncategorized (blank category/parent) and outside the Retirement subcategory, which now totals **$5,800.00** across 8 transactions.

**Status unchanged: strong evidence, not confirmed.** The sign flip doesn't resolve whether "MPI" refers to this Mutual of Omaha vehicle or the Blue Origin retirement plan — still recommend Gil confirm directly. See [[02-Indexes/topic_maps/household-finance-relationship-map]].

---

## 4. Spend by Main Category (Regular Transactions Only, Jan 1 – Aug 16)

| Group | Total | Txns |
|---|---|---|
| NEEDS | $73,639.20 | 351 |
| SAVINGS / DEBT | $41,319.17 | 158 |
| WANTS JOINT | $26,260.71 | 507 |
| PERSONAL LU | $12,119.42 | 184 |
| PERSONAL GIL | $10,345.47 | 128 |
| Taxes *(ungrouped — schema gap)* | $802.67 | 3 |
| Apartments-Houses / Archive *(ungrouped — schema gap)* | $316.26 | 3 |
| Blank category (incl. the MPI row) | −$5,415.79 | 4 |
| **Total regular spend** | **$159,387.11** | **1,338** |

*(24 additional "To Review"-tagged regular transactions are excluded from this table — see §7.)*

### NEEDS subcategory breakdown

| Subcategory | Total | Txns |
|---|---|---|
| Mortgage *(purchase costs + first recurring payment, see §2)* | $21,326.94 | 7 |
| CIRRUS (Rent + Water + Storage) | $15,866.92 | 7 |
| Groceries | $10,425.06 | 110 |
| Car + Gas | $7,922.76 | 82 |
| Home Everbe | $7,374.10 | 41 |
| Healthcare | $3,689.42 | 31 |
| Luna | $2,720.28 | 32 |
| Electricity | $1,623.71 | 10 |
| Phones | $1,363.52 | 20 |
| Insurance | $1,326.49 | 11 |

### SAVINGS / DEBT subcategory breakdown

| Subcategory | Total | Txns |
|---|---|---|
| Loans | $30,732.20 | 54 |
| CC min payments | $4,786.97 | 96 |
| Retirement | $5,800.00 | 8 |

### WANTS JOINT subcategory breakdown

| Subcategory | Total | Txns |
|---|---|---|
| Travel & Vacation | $8,327.33 | 69 |
| Restaurants - Joint | $7,796.47 | 138 |
| Bars & Nightlife - Joint | $3,966.01 | 41 |
| Other | $2,504.37 | 92 |
| Subscriptions | $2,449.35 | 129 |
| Eight Sleep - Affirm | $646.68 | 4 |
| Transportation (Uber) | $570.50 | 34 |

*(Entertainment, Sports, and Immigration had $0 activity — consistent with the schema doc's note that these are largely inactive.)*

### PERSONAL LU / PERSONAL GIL

| PERSONAL LU | Total | Txns | | PERSONAL GIL | Total | Txns |
|---|---|---|---|---|---|---|
| Shops & Clothing Lu | $3,355.46 | 115 | | Family Gil | $6,911.13 | 61 |
| Family Lu | $5,420.35 | 32 | | Bar & Restaurants Gil | $1,605.71 | 31 |
| Bar & Restaurants Lu | $1,493.75 | 18 | | Shops & Clothing Gil | $1,467.18 | 30 |
| Lu Recruitment Business | $1,119.32 | 5 | | Personal Image Gil | $361.45 | 6 |
| Personal Care Lu | $730.54 | 14 | | | | |

---

## 5. Schema Gaps Found (Original Categories Preserved, Not Reassigned)

| Category | Total | Txns | Issue |
|---|---|---|---|
| Taxes | $802.67 | 3 | Not in any defined schema group (TurboTax + IRS payment + service fee, all 2026-03-02). Same gap as the prior ingest — still unresolved. |
| Apartments-Houses (Archive) | $316.26 | 3 | Legacy category label — 2 Lowe's purchases (2026-05-30, $282.01 combined) plus 1 new August pair (Home Depot $596.88 and Wwp*Hometeam Pest Defense $33.25, both 2026-08-03 — home-improvement/pest-control spend). Schema's Home Everbe definition explicitly includes "furniture" — likely the correct home for these, but flagged rather than reassigned. |
| Blank category — "City Of Cocoa" utility payments | $84.53 | 2 | New gap not present in the Jan–Jul ingest: two water-utility payments (2026-01-06, $2.99 + $81.54) with no category assigned. Likely belongs under a water/utility NEEDS subcategory the schema doesn't currently define (Electricity is electric-only). |
| Blank category — Interest | −$0.32 | 1 | Bank account interest credit — immaterial, likely fine to leave uncategorized. |

---

## 6. Internal Transfers (236 transactions)

232 of 236 internal transfers carry no expense category (pure account-to-account movement — correctly excluded from the spend totals in §4). **4 transfers carry a real spend category** and are not included in those totals:

| Date | Transaction | Amount | Category |
|---|---|---|---|
| 2026-02-07 | Blumon Pay*serv Parkmiguel Hidalgo | $92.56 | Bar & Restaurants Gil |
| 2026-03-20 | Zelle Payment From Karol Rendon Monsalve | −$105.00 | Phones |
| 2026-04-25 | Zelle Payment To Dayana | $150.00 | CIRRUS (Rent + Water + Storage) |
| 2026-05-16 | Zelle Payment To Dayana | $175.00 | CIRRUS (Rent + Water + Storage) |

*(2 additional internal-transfer rows carry Gil's own "To Review" tag and are listed in §7 instead.)*

---

## 7. Pending Gil's Review (26 Transactions, Tagged "To Review")

These carry Gil's own "To Review" tag and are **not categorized by this analysis** — listed here for him to resolve directly. 2 are new since the Jan–Jul ingest (marked with **NEW**):

| Date | Transaction | Amount | Account |
|---|---|---|---|
| 2026-01-06 | Withdrawal Silva Gonzalez From | $600.00 | First Tech Rewards Checking |
| 2026-04-02 | Credit Balance Refund (sale Type) | $101.00 | Discover it Card |
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
| 2026-07-15 | Renewal Membership Fee | $195.00 | Platinum Card® |
| 2026-07-16 | Care.com* Care.com 7austin | $56.97 | Platinum Card® |
| 2026-07-18 | Kindle Unltd*3p5qk36m3 | $13.25 | Prime Visa |
| 2026-07-30 | Zelle Payment To Osiel | $63.00 | Total Checking |
| 2026-07-31 | Lemonade Insurance | $11.67 | Platinum Card® |
| 2026-08-03 | Home Depot **(NEW)** | $596.88 | Total Checking |
| 2026-08-09 | Amazon Mktpl*5h6ye3nh1 **(NEW)** | $67.99 | Prime Visa |

---

## Methodology

Computed by a Python script that: (1) parsed the raw CSV (1,702 rows, zero blank padding), (2) validated each `regular`-type transaction's `(category, parent category)` pair against the exact dictionary in [[L5-Finance/expense-categorization-schema]], (3) summed by group/subcategory/month, (4) recomputed the same logic against the retired Jan–Jul export to produce the §0 comparison table. No transaction's category or amount was altered — the annotated CSV only adds a `schema_check` column; all flagged items above point back to the original data.
