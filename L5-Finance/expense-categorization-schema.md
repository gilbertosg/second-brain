---
title: "Expense Categorization Schema — Routing Rules & Subcategory Dictionary"
type: reference
pillar_id: L5
owner: Gilberto Silva Gonzalez
created: 2026-08-02
last_updated: 2026-08-02
status: active
tags: [l5, finance, budget, categorization, schema, reference]
source_file: "00-Raw_Sources/L5_Finances/Financial Schema - Expense Categories.md"
related: [L5-Finance/_pillar, L5-Finance/household-income-2026, 02-Indexes/topic_maps/household-finance-relationship-map]
---

# Expense Categorization Schema — Routing Rules & Subcategory Dictionary

Canonical routing schema for classifying Gil + Luisa household transactions. This is a durable reference — use it to categorize any future transaction data, not just the July 2026 snapshot shown at the bottom. All 5 main groups are mutually exclusive; every transaction routes to exactly one.

---

## Main Category Routing Rules

| Group | Routing Rule |
|---|---|
| **NEEDS** | Required for survival, shelter, basic utilities, mandatory insurance, or essential health. Excludes lifestyle upgrades or discretionary spending. |
| **WANTS JOINT** | Shared discretionary spending — entertainment, dining, travel, or convenience services used by both. Includes shared subscriptions and joint social outings. |
| **SAVINGS / DEBT** | Payments toward outstanding debt principal/interest, minimum credit card payments, or transfers to retirement/investment/savings accounts. |
| **PERSONAL LU** | Solely for Lu's personal enjoyment, personal care, individual family support, or individual business expenses — separate from joint funds. |
| **PERSONAL GIL** | Solely for Gil's personal enjoyment, personal care, individual family support, or individual shopping — separate from joint funds. |

---

## Subcategory Dictionary

### NEEDS

| Subcategory | Definition | System Notes |
|---|---|---|
| Car + Gas | Vehicle ownership, fuel, maintenance | Nissan Kicks lease returned March 2026 — only the Mazda remains. Gas transactions must be explicitly tagged "gas" to separate from other maintenance. |
| Home Everbe | Everbe property (closed 2026-06-02) | **Strictly** HOA fees, maintenance, and furniture. Does **not** include the mortgage payment. |
| Groceries | Essential food/household items | — |
| Phones | Cellular plans, device payments | — |
| Luna | Pet expenses (food, vet, grooming, supplies) | — |
| Insurance | Auto, health, renters/homeowners, or life premiums | — |
| Electricity | Monthly electrical utility | — |
| Healthcare | Out-of-pocket medical, copays, prescriptions | Includes Lu's recurring face/acne treatment subscriptions. |
| CIRRUS (Rent + Water...) | Rent + integrated utilities, previous apartment | Historical only — Gil and Lu moved out 2026-06-08. Kept separate from Home Everbe to preserve the pre/post-move data boundary. |
| Mortgage | Everbe home loan principal + interest | First payment $3,200 scheduled 2026-08-01 — explains $0.00 balances in the June/July sample data. |

### WANTS JOINT

| Subcategory | Definition | System Notes |
|---|---|---|
| Travel & Vacation | Flights, lodging, in-destination activities | Explicit "Gil" or "Lu" label = individual; unlabeled = assume joint. |
| Restaurants - Joint | Dining out together | Includes food delivery to the house. |
| Bars & Nightlife - Joint | Drinks/social outings together | — |
| Subscriptions | Shared streaming/software/magazines | — |
| Other | Miscellaneous joint discretionary | — |
| Transportation (Uber) | Joint ride-sharing | — |
| Entertainment | Movies, concerts, recreational events | Largely inactive — route standard lifestyle spend to Bars & Nightlife or Travel instead, unless explicitly instructed otherwise. |
| Sports | Joint sporting activities/equipment/events | — |
| Eight Sleep - Affirm | Financed mattress payments | Loan paid off May 2026 — no further recurring charges expected. |
| Immigration | Legal fees/applications | Currently dormant. Historically Lu's Green Card; reserved for possible future use (e.g., Gil's citizenship). |

### SAVINGS / DEBT

| Subcategory | Definition |
|---|---|
| Loans | Personal or other outstanding loan payments |
| CC min payments | Minimum required credit card payments |
| Retirement | Contributions to retirement accounts, incl. the **MPI account** (a named account — see the MPI-naming caveat in [[L5-Finance/household-income-2026]], not to be conflated with the L5 "Monthly Passive Income" OKR) |

### PERSONAL LU

| Subcategory | Definition |
|---|---|
| Bar & Restaurants Lu | Lu's individual dining/drinks |
| Family Lu | Financial support/gifts to Lu's family |
| Shops & Clothing Lu | Lu's personal apparel/accessories spending |
| Lu Recruitment Business | Lu's recruitment business/professional expenses |
| Personal Care Lu | Grooming, haircuts, cosmetics, wellness |

### PERSONAL GIL

| Subcategory | Definition |
|---|---|
| Family Gil | Financial support/gifts to Gil's family (often Mexico) |
| Shops & Clothing Gil | Gil's personal apparel/accessories spending |
| Personal Image Gil | Grooming, haircuts, personal maintenance |
| Bar & Restaurants Gil | Gil's individual dining/drinks |

---

## Sample Snapshot — July 2026 (Reference Only)

> Source data explicitly states: **do not treat these values as fixed budgets.** This is a structural example of how Main Categories, Subcategories, and amounts relate — not a target or historical average to plan against.

| Main Category | Total |
|---|---|
| NEEDS | $3,862.35 |
| WANTS JOINT | $5,983.39 |
| SAVINGS / DEBT | $5,992.81 |
| PERSONAL LU | $130.55 |
| PERSONAL GIL | $383.18 |
| **Total Monthly Spend (Sample)** | **$16,352.28** |

Largest single subcategories in this sample: Loans ($4,465.62), Travel & Vacation ($1,854.56), Restaurants - Joint ($1,737.19), Car + Gas ($1,396.16), Bars & Nightlife - Joint ($1,470.33).
