---
title: "Transaction Analysis — Jan–Jul 2026"
type: analysis
pillar_id: L5
owner: Gilberto Silva Gonzalez
created: 2026-08-02
last_updated: 2026-08-02
status: active
tags: [l5, finance, budget, transactions, analysis, cash-flow]
source_file: "00-Raw_Sources/L5_Finances/2026-YTD-Jan-Jul.csv"
related: [L5-Finance/_pillar, L5-Finance/household-income-2026, L5-Finance/expense-categorization-schema, L5-Finance/transactions-2026-jan-jul.csv, 02-Indexes/topic_maps/household-finance-relationship-map]
---

# Transaction Analysis — Jan–Jul 2026

Full-ledger analysis of every real transaction from 2026-01-01 through 2026-07-31, computed by script (not hand-tallied) against [[L5-Finance/expense-categorization-schema]]'s routing rules. The validated, annotated transaction-by-transaction ledger lives in [`transactions-2026-jan-jul.csv`](transactions-2026-jan-jul.csv) — this file is the summary and the findings.

**Data-quality note:** the raw export (`00-Raw_Sources/L5_Finances/2026-YTD-Jan-Jul.csv`) contains 10,126 rows, but **8,541 are entirely blank** (an export artifact — likely a padded spreadsheet range). Only **1,585 rows are real transactions**. All figures below are computed from those 1,585 rows only.

---

## 1. Cash Flow Reality Check — Contradicts the "Positive Cash Flow" OKR Framing

**5 of the first 7 months of 2026 closed net-negative.** `L5-Finance/_pillar.md`'s Strategic Context describes 2026 as a "stability and positive cash flow" year and carries a "12 months of positive cash flow" OKR — the actual data doesn't support that framing so far this year.

| Month | Income | Spend | Net |
|---|---|---|---|
| 2026-01 | $23,158.83 | $19,484.75 | **+$3,674.08** |
| 2026-02 | $15,082.58 | $16,502.80 | −$1,420.22 |
| 2026-03 | $31,507.04 | $39,057.89 | −$7,550.85 |
| 2026-04 | $14,585.98 | $18,428.66 | −$3,842.68 |
| 2026-05 | $20,367.13 | $21,977.17 | −$1,610.04 |
| 2026-06 | $19,253.67 | $23,958.01 | −$4,704.34 |
| 2026-07 | $28,950.97 | $18,431.24 | **+$10,519.73** |
| **YTD Total** | **$152,906.20** | **$157,840.52** | **−$4,934.32** |

March's deficit is explained by home-purchase costs (see §2) and is not representative of ongoing spending. July's surplus coincides with the 3rd-paycheck month. Excluding March, the Jan–Jul net would be **+$2,616.53** — still thin, not the "stable positive" picture the OKR context assumes.

**Recommendation:** update `L5-Finance/_pillar.md`'s Strategic Context to track actual monthly cash flow against the 12-month target explicitly, rather than describing 2026 as already stable.

---

## 2. "Mortgage" Category = Home-Purchase Costs, Not Recurring Payments (Important Nuance)

6 transactions totaled **$18,034.26** under the "Mortgage" category Jan–Jul — but **none of these are the recurring monthly mortgage payment**. They are one-time home-purchase-process costs:

| Date | Transaction | Amount |
|---|---|---|
| 2026-03-01 | Pulte North Florida Ga | $5,000.00 |
| 2026-03-17 | Pulte Mortgage L Pulte Mort | $947.00 |
| 2026-03-31 | Pulte Home Comp Pay | $10,000.00 |
| 2026-05-11 | Neptune Pol Asr4 Neptune Po (flood insurance) | $589.93 |
| 2026-06-01 | Online Domestic Wire Transfer — PGP Title of Florida | $1,472.33 |
| 2026-06-01 | Online Domestic Wire Fee | $25.00 |

**New finding: Everbe is a Pulte-built home.** The 3 March payments to Pulte Homes/Pulte Mortgage ($15,947 combined) are builder deposits/lock fees, not mortgage principal. The June 1 wire to "PGP Title of Florida Inc" references **Property: 10602 Evening Star Street, Orlando, FL** — one day before the 2026-06-02 closing date already on file, an independent confirmation of that date. (The zip code in the wire memo is garbled in the source export — appears as "328 29" — not repeated here as a clean figure.)

**Likely miscategorization:** the $589.93 Neptune payment is flood insurance and probably belongs under the **Insurance** subcategory, not Mortgage — flagged in the ledger as `NOTE`, not silently moved.

This is consistent with, not contradictory to, the expense schema's note that the first *recurring* mortgage payment ($3,200) starts 2026-08-01 — August data (not covered by this CSV) will look structurally different.

---

## 3. MPI Naming Question — New Evidence

A **$5,500 payment to Mutual of Omaha on 2026-03-23, tagged `MPI`**, is **not** counted in the "Retirement" subcategory (which totals only $5,075 across 7 unrelated transactions). This is meaningful evidence — a lump-sum payment to an insurance company, tagged with the exact OKR acronym, sitting outside the standard retirement bucket — that **"MPI" likely refers to a specific Mutual of Omaha investment/insurance product** (commonly IUL-type policies marketed as income vehicles), distinct from Blue Origin's standard retirement plan.

**Status: strong evidence, not confirmed.** Updated in [[02-Indexes/topic_maps/household-finance-relationship-map]] — still recommend Gil confirm directly rather than treating this as settled.

---

## 4. Spend by Main Category (Regular Transactions Only, Jan–Jul)

| Group | Total | Txns |
|---|---|---|
| NEEDS | $67,430.66 | 319 |
| SAVINGS / DEBT | $39,454.23 | 142 |
| WANTS JOINT | $32,865.39 | 480 |
| PERSONAL GIL | $11,234.88 | 130 |
| PERSONAL LU | $10,879.97 | 183 |
| Taxes *(ungrouped — schema gap)* | $802.67 | 3 |
| Apartments-Houses / Archive *(ungrouped — schema gap)* | $283.01 | 2 |
| Blank category (incl. the MPI row) | −$5,110.29 | 7 |
| **Total regular spend** | **$157,840.52** | **1,266** |

### NEEDS subcategory breakdown

| Subcategory | Total | Txns |
|---|---|---|
| Mortgage *(purchase costs, see §2)* | $18,034.26 | 6 |
| CIRRUS (Rent + Water + Storage) | $15,866.92 | 7 |
| Groceries | $9,027.33 | 96 |
| Car + Gas | $7,701.67 | 78 |
| Home Everbe | $6,966.35 | 39 |
| Healthcare | $3,191.62 | 26 |
| Luna | $2,743.28 | 32 |
| Phones | $1,714.86 | 18 |
| Insurance | $1,229.07 | 9 |
| Electricity | $955.30 | 8 |

### SAVINGS / DEBT subcategory breakdown

| Subcategory | Total | Txns |
|---|---|---|
| Loans | $29,133.90 | 42 |
| CC min payments | $5,245.33 | 93 |
| Retirement | $5,075.00 | 7 |

### WANTS JOINT subcategory breakdown

| Subcategory | Total | Txns |
|---|---|---|
| Other | $9,733.78 | 83 |
| Travel & Vacation | $8,124.08 | 65 |
| Restaurants - Joint | $7,327.49 | 127 |
| Bars & Nightlife - Joint | $3,987.91 | 42 |
| Subscriptions | $2,501.07 | 125 |
| Eight Sleep - Affirm | $646.68 | 4 |
| Transportation (Uber) | $544.38 | 34 |

*(Entertainment, Sports, and Immigration had $0 activity — consistent with the schema doc's note that these are largely inactive.)*

### PERSONAL LU / PERSONAL GIL

| PERSONAL LU | Total | Txns | | PERSONAL GIL | Total | Txns |
|---|---|---|---|---|---|---|
| Shops & Clothing Lu | $4,542.24 | 128 | | Family Gil | $7,898.40 | 64 |
| Family Lu | $3,861.27 | 25 | | Bar & Restaurants Gil | $1,586.46 | 32 |
| Lu Recruitment Business | $1,119.32 | 5 | | Shops & Clothing Gil | $1,388.57 | 28 |
| Personal Care Lu | $805.11 | 14 | | Personal Image Gil | $361.45 | 6 |
| Bar & Restaurants Lu | $552.03 | 11 | | | | |

---

## 5. Schema Gaps Found (Original Categories Preserved, Not Reassigned)

| Category | Total | Txns | Issue |
|---|---|---|---|
| Taxes | $802.67 | 3 | Not in any defined schema group (TurboTax + IRS payment + service fee, all 2026-03-02). Likely belongs under NEEDS, but not Gil's call to make unilaterally. |
| Apartments-Houses (Archive) | $283.01 | 2 | Legacy category label, 2 Lowe's purchases (2026-05-30). Schema's own Home Everbe definition explicitly includes "furniture" — likely the correct home for these, but flagged rather than reassigned. |

---

## 6. Internal Transfers ($11,092.06 net across 213 transactions)

209 of 213 internal transfers carry no expense category (pure account-to-account movement — debt paydowns, savings transfers — correctly excluded from the spend totals above). **4 transfers carry a real spend category** and are not included in §4's totals:

| Date | Transaction | Amount | Category |
|---|---|---|---|
| 2026-02-07 | Blumon Pay*serv Parkmiguel Hidalgo | $92.56 | Bar & Restaurants Gil |
| 2026-03-20 | Zelle Payment From Karol Rendon Monsalve | −$105.00 | Phones |
| 2026-04-25 | Zelle Payment To Dayana | $150.00 | CIRRUS (Rent + Water + Storage) |
| 2026-05-16 | Zelle Payment To Dayana | $175.00 | CIRRUS (Rent + Water + Storage) |

---

## 7. Pending Gil's Review (28 Transactions, Tagged "To Review")

These carry Gil's own "To Review" tag and are **not categorized by this analysis** — listed here for him to resolve directly:

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
| 2026-05-21 | Tmobile*auto Pay | $467.27 | Adv Plus Banking |
| 2026-05-29 | Uber | $9.99 | Apple Card |
| 2026-06-01 | Zelle Payment To Luisa F Rangel | $204.00 | Adv Plus Banking |
| 2026-06-05 | Online-mobile Recurring | −$35.00 | Atmos Rewards Ascent Visa Signature |
| 2026-06-07 | Amazon Prime | $5.65 | Platinum Card® |
| 2026-06-08 | Spaceport- Ticketing | $241.82 | Prime Visa |
| 2026-06-10 | Teriyaki Mad Cat 210melbourne | $375.50 | Platinum Card® |
| 2026-06-11 | Transaction: Rmtly* B5ac8 1111 Third Ave., Suite | $151.99 | First Tech Rewards Checking |
| 2026-06-14 | Renewal Membership Fee | $195.00 | Platinum Card® |
| 2026-06-14 | Rentaltoll | $56.30 | Platinum Card® |
| 2026-06-23 | Uber | $9.99 | Platinum Card® |
| 2026-06-24 | Godaddy | $25.64 | Platinum Card® |
| 2026-07-05 | Online-mobile Recurring | −$35.00 | Atmos Rewards Ascent Visa Signature |
| 2026-07-15 | Renewal Membership Fee | $195.00 | Platinum Card® |
| 2026-07-16 | Care.com* Care.com 7austin | $56.97 | Platinum Card® |
| 2026-07-18 | Kindle Unltd*3p5qk36m3 | $13.25 | Prime Visa |
| 2026-07-30 | Zelle Payment To Osiel | $63.00 | Total Checking |
| 2026-07-31 | Lemonade Insurance | $11.67 | Platinum Card® |

---

## Methodology

Computed by a Python script that: (1) parsed the raw CSV and discarded the 8,541 fully-blank rows, (2) validated each `regular`-type transaction's `(category, parent category)` pair against the exact dictionary in [[L5-Finance/expense-categorization-schema]], (3) summed by group/subcategory/month. Income total for June ($19,253.67) and July ($28,950.97) were cross-checked against [[L5-Finance/household-income-2026]] and matched exactly, confirming this CSV is consistent with the previously-ingested income report. No transaction's category or amount was altered — the annotated CSV only adds a `schema_check` column; all flagged items above point back to the original data.
