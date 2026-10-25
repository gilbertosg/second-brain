---
title: "Household Finance × Relationship — Cross-Pillar Synthesis"
type: topic-map
pillars: [L5, L2, L3]
sources:
  - "L5-Finance/household-income-2026.md"
  - "L5-Finance/expense-categorization-schema.md"
  - "L5-Finance/transaction-analysis-2026-jan-oct.md"
  - "01-Entities/luisa.md"
  - "L2-Relationships/_pillar.md"
  - "L3-Career/_pillar.md"
created: 2026-08-02
last_updated: 2026-10-24
tags: [finance, relationship, l2, l3, l5, home-purchase, income-concentration, luisa, cash-flow]
---

# Household Finance × Relationship — Cross-Pillar Synthesis

The 2026-08-02 L5 Finance ingest (Household Income Report + Expense Categorization Schema) surfaces two structural findings that single-pillar analysis would miss: a stale L2 milestone that's actually already resolved, and a household income concentration risk that spans L3 and L5.

---

## 1. L5 → L2: The New-Home Decision Is Resolved, Not Pending

`L2-Relationships/_pillar.md`'s 2026 OKR table lists **"Define new home — Identify and decide on new place to live — Milestone"** as an open item, and its Strategic Context calls it "the highest-risk L5 event in 2026." The income report shows this is stale:

```
Prior L2 status:        "Identify and decide on new place to live" (open milestone)
Financial reality:       Everbe property CLOSED 2026-06-02
                          Down payment funded by Gil's March 2026 bonus
                          First mortgage payment scheduled 2026-08-01
                          Previous residence (CIRRUS) vacated 2026-06-08
```

**Key finding:** the decision phase is over; the household is now in the *execution* phase (HOA fees, furniture, mortgage payments — see the "Home Everbe" and "Mortgage" subcategories in [[L5-Finance/expense-categorization-schema]]). L2's OKR and Strategic Context should reflect this transition, and the bi-weekly Dream & Finance meetings likely shift focus from "which home" to "settling into Everbe" and general financial alignment.

---

## 2. L5 ↔ L3: Single-Employer Household Income Concentration

Luisa joined Blue Origin ([[01-Entities/blue-origin]]) on 2026-04-20 — the same employer Gil has worked at for ~3 years 9 months. As of this ingest, **100% of household net income comes from one employer.**

```
Household Net Income (June 2026, standard month): $19,253.67
├── Gil   (Blue Origin): $12,127.54  (62.99%)
└── Luisa (Blue Origin): $ 7,126.13  (37.01%)
                          ─────────
                          100% single-employer
```

**Finding:** this is a meaningful concentration risk that neither `L3-Career/_pillar.md` nor `L5-Finance/_pillar.md` currently names. A layoff, restructuring, or company-wide event at Blue Origin would affect both income streams simultaneously — unlike a household where partners work at different companies. This doesn't require action, but it is a risk factor worth acknowledging in L5's financial planning posture (e.g., emergency fund sizing) and is directly relevant if L3's Principal-promotion or Agent Award context ever involves org-wide uncertainty.

---

## 3. MPI Naming Question — Updated with Transaction Evidence (2026-10-24)

`L5-Finance/_pillar.md`'s Couple OKR table includes **"Monthly Passive Income (MPI) — grow MPI by 10%/month."** The expense schema separately references a **"MPI account"** under the Retirement subcategory (Savings/Debt group). Originally flagged here as an unresolved naming collision, tentatively guessed to be a Blue Origin retirement account.

**Evidence from the refreshed Jan–Oct 2026 ledger (re-ingested 2026-10-24):**

- A **−$5,500.00 row from Mutual of Omaha on 2026-03-23, tagged `MPI`**, with a blank category, sits outside the Retirement subcategory (see [[L5-Finance/transaction-analysis-2026-jan-oct.md]] §3).
- The Retirement subcategory totals **$7,250.00 across ten monthly $725.00 `United Of Omaha - Ins Prem` debits** (Jan 5–Oct 5). United of Omaha Life Insurance Company operates within the Mutual of Omaha group.
- **Direction changed:** the export records income as negative amounts, so −$5,500.00 is an **inflow**. Earlier versions of this page described it as a payment *to* Mutual of Omaha. The direction (withdrawal, loan, refund, or other) is unconfirmed.

Together these suggest **MPI is an Omaha-group insurance/investment product** (commonly an IUL-type policy marketed as an income vehicle), not a Blue Origin retirement plan. **Still not confirmed.** Flagged for Gil: is the Omaha policy the vehicle the "Monthly Passive Income" OKR tracks, and what was the March $5,500 inflow?

---

## 4. Cross-Pillar Impact Matrix

| Source Pillar | Target Pillar | Mechanism | Urgency |
|---|---|---|---|
| L5 (home purchase closed) | L2 (new-home OKR) | OKR status is stale — decision resolved, execution phase active | 🔴 High |
| L3 (Luisa joins Blue Origin) | L5 (income structure) | Household income now 100% single-employer — concentration risk | 🟡 Med |
| L5 (MPI tagged transaction) | L5 (MPI OKR) | $5,500 Mutual of Omaha row tagged "MPI" (an inflow under the export's sign convention) plus ten monthly $725 United of Omaha premiums suggest a specific insurance/investment vehicle, not a generic retirement account — still needs Gil's confirmation | 🟡 Med |
| L5 (mortgage starts Aug 1) | L5 (budget baseline) | Three recurring payments confirmed (2026-08-04, 09-01, 10-01; $3,292.68 each vs. schema doc's ~$3,200 estimate). The Oct 1 payment is coded `Loans`, not `Mortgage`. The $18,034.26 of one-time purchase costs sits in the same bucket | 🟢 Low |
| L5 (cash flow reality, refreshed 2026-10-24) | L5 (positive-cash-flow OKR) | Headline YTD net is +$37,575.18 through Oct 23, but a one-time $29,331.20 loan inflow (Marlette Funding, 8/19) inflates it. Adjusted YTD net is +$8,243.98; 6 of 9 complete months closed net-negative. See [[L5-Finance/transaction-analysis-2026-jan-oct.md]] §0–1 | 🔴 High |

---

## 5. Open Gaps and Recommended Actions

| Gap | Evidence | Recommended Action |
|---|---|---|
| L2 "Define new home" OKR stale | Everbe closed 2026-06-02, per income report | Update `L2-Relationships/_pillar.md` OKR status to reflect resolution (done as part of this ingest) |
| MPI naming ambiguity | $5,500 Mutual of Omaha row tagged "MPI" sits outside the Retirement subcategory; Retirement is ten monthly $725 United of Omaha premiums; the row is an inflow, not a payment (2026-10-24 evidence) | Ask Gil directly to confirm: is the Omaha policy the vehicle the OKR tracks, and what was the March inflow? |
| MPI OKR baseline still missing | `L5-Finance/_pillar.md` Notes already flagged this before this ingest; still unresolved | Capture a starting MPI figure once the naming question is settled |
| No emergency-fund sizing tied to single-employer risk | Concentration finding above, no existing L5 OKR addresses it | Consider whether the "12 months positive cash flow" KR should be reframed with the concentration risk in mind |
| Positive-cash-flow OKR volatility not tracked | Adjusted YTD net is +$8,243.98 (headline +$37,575.18 includes a $29,331.20 loan), but 6 of 9 complete months closed negative (2026-10-24 evidence) | Track monthly cash flow explicitly against the 12-month target, and reframe the KR so a one-time financing inflow cannot satisfy it |
| Unexplained $29,331.20 loan inflow | Marlette Funding / Cross River Bank credit on 2026-08-19, tags `Loan, Lu`, no category; the last Upstart loan payment posted 2026-07-29 and no repayment rows follow | Gil to state the loan's purpose and terms (refinance of the Upstart loan?) and add its repayment to the budget baseline |
| Oct 1 mortgage payment coded `Loans` | `Freedom Mtg Pymts` $3,292.68 lands in SAVINGS / DEBT, while Aug and Sep landed in NEEDS/Mortgage | Gil to confirm the intended category |
| Internal transfers no longer exported | 233 of 236 prior transfer rows are absent by Gil's choice | Accept reduced visibility into account-to-account movement; request a transfer export if a reconciliation need arises |
| 5 taxonomy gaps in expense schema | "Taxes," "Apartments-Houses/Archive," a "City Of Cocoa" water-utility gap, a new "Church" category ($63.39, 6 txns), and the `Travel & Vacation Joint/Lu/Gil` names missing from the schema doc (2026-10-24 evidence) | Gil to decide: add "Taxes" and a giving/church subcategory; define a water-utility subcategory; update the schema doc with the three travel subcategory names |

---

*For related vault documents see: [[L5-Finance/household-income-2026]], [[L5-Finance/expense-categorization-schema]], [[L5-Finance/transaction-analysis-2026-jan-oct.md]], [[01-Entities/luisa]], [[L2-Relationships/_pillar]], [[L3-Career/_pillar]]*
