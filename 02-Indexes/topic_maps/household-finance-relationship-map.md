---
title: "Household Finance × Relationship — Cross-Pillar Synthesis"
type: topic-map
pillars: [L5, L2, L3]
sources:
  - "L5-Finance/household-income-2026.md"
  - "L5-Finance/expense-categorization-schema.md"
  - "L5-Finance/transaction-analysis-2026-jan-jul.md"
  - "01-Entities/luisa.md"
  - "L2-Relationships/_pillar.md"
  - "L3-Career/_pillar.md"
created: 2026-08-02
last_updated: 2026-08-02
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

Luisa joined Blue Origin on 2026-04-20 — the same employer Gil has worked at for ~3 years 9 months. As of this ingest, **100% of household net income comes from one employer.**

```
Household Net Income (June 2026, standard month): $19,253.67
├── Gil   (Blue Origin): $12,127.54  (62.99%)
└── Luisa (Blue Origin): $ 7,126.13  (37.01%)
                          ─────────
                          100% single-employer
```

**Finding:** this is a meaningful concentration risk that neither `L3-Career/_pillar.md` nor `L5-Finance/_pillar.md` currently names. A layoff, restructuring, or company-wide event at Blue Origin would affect both income streams simultaneously — unlike a household where partners work at different companies. This doesn't require action, but it is a risk factor worth acknowledging in L5's financial planning posture (e.g., emergency fund sizing) and is directly relevant if L3's Principal-promotion or Agent Award context ever involves org-wide uncertainty.

---

## 3. MPI Naming Question — Updated with Transaction Evidence (2026-08-02)

`L5-Finance/_pillar.md`'s Couple OKR table includes **"Monthly Passive Income (MPI) — grow MPI by 10%/month."** The expense schema separately references a **"MPI account"** under the Retirement subcategory (Savings/Debt group). Originally flagged here as an unresolved naming collision, tentatively guessed to be a Blue Origin retirement account.

**New evidence from the Jan–Jul 2026 transaction ledger revises that guess:** a **$5,500 payment to Mutual of Omaha on 2026-03-23, tagged `MPI`**, sits outside the standard Retirement subcategory (which totals only $5,075 across 7 unrelated transactions — see [[L5-Finance/transaction-analysis-2026-jan-jul.md]] §3). A lump-sum payment to an insurance company, tagged with the exact OKR acronym, strongly suggests **MPI is a specific Mutual of Omaha investment/insurance product** (commonly an IUL-type policy marketed as an income vehicle) — not a Blue Origin retirement plan account as first guessed.

**Still not fully confirmed.** This is materially stronger evidence than the original guess, but not certain. Flagged for Gil to confirm directly: is the Mutual of Omaha policy the same vehicle the "Monthly Passive Income" OKR tracks?

---

## 4. Cross-Pillar Impact Matrix

| Source Pillar | Target Pillar | Mechanism | Urgency |
|---|---|---|---|
| L5 (home purchase closed) | L2 (new-home OKR) | OKR status is stale — decision resolved, execution phase active | 🔴 High |
| L3 (Luisa joins Blue Origin) | L5 (income structure) | Household income now 100% single-employer — concentration risk | 🟡 Med |
| L5 (MPI tagged transaction) | L5 (MPI OKR) | $5,500 Mutual of Omaha payment tagged "MPI" suggests a specific insurance/investment vehicle, not a generic retirement account — still needs Gil's confirmation | 🟡 Med |
| L5 (mortgage starts Aug 1) | L5 (budget baseline) | Jan–Jul "Mortgage" transactions ($18,034.26) are one-time purchase costs (Pulte builder payments, title wire, flood insurance), not recurring payments — first real recurring mortgage month (August) will look structurally different | 🟢 Low |
| L5 (cash flow reality) | L5 (positive-cash-flow OKR) | 5 of 7 months Jan–Jul closed net-negative (YTD −$4,934.32) — contradicts the pillar's "stability" framing; see [[L5-Finance/transaction-analysis-2026-jan-jul.md]] §1 | 🔴 High |

---

## 5. Open Gaps and Recommended Actions

| Gap | Evidence | Recommended Action |
|---|---|---|
| L2 "Define new home" OKR stale | Everbe closed 2026-06-02, per income report | Update `L2-Relationships/_pillar.md` OKR status to reflect resolution (done as part of this ingest) |
| MPI naming ambiguity | $5,500 Mutual of Omaha payment tagged "MPI" sits outside the Retirement subcategory (2026-08-02 evidence) | Ask Gil directly to confirm: is the Mutual of Omaha policy the vehicle the OKR tracks? |
| MPI OKR baseline still missing | `L5-Finance/_pillar.md` Notes already flagged this before this ingest; still unresolved | Capture a starting MPI figure once the naming question is settled |
| No emergency-fund sizing tied to single-employer risk | Concentration finding above, no existing L5 OKR addresses it | Consider whether the "12 months positive cash flow" KR should be reframed with the concentration risk in mind |
| Positive-cash-flow OKR not tracking reality | 5 of 7 months Jan–Jul 2026 net-negative (2026-08-02 evidence) | Track actual monthly cash flow explicitly against the 12-month target rather than assuming stability |
| 3 taxonomy gaps in expense schema | "Taxes" and "Apartments-Houses/Archive" categories have no defined group (2026-08-02 evidence) | Gil to decide: add "Taxes" as a NEEDS subcategory; confirm "Apartments-Houses" purchases should route to "Home Everbe" |

---

*For related vault documents see: [[L5-Finance/household-income-2026]], [[L5-Finance/expense-categorization-schema]], [[L5-Finance/transaction-analysis-2026-jan-jul.md]], [[01-Entities/luisa]], [[L2-Relationships/_pillar]], [[L3-Career/_pillar]]*
