---
title: "Gil OS Second Brain — Teaching Summary"
type: reference
status: draft
audience: external
date: 2026-07-12
note: One-off teaching artifact. Not registered in vault index or system log.
---

# Gil OS & Second Brain - Summary

A complete walkthrough of what this project is, how it is built, and what has been accomplished so far. Written so you can explain or teach this system to someone who has never seen it.

---

## 1. What Is This Project?

**Gil OS** is a personal operating system. It is a structured framework for running every domain of life with the same intentionality you would apply to running a business or a software system.

The **Second Brain** is the knowledge graph that powers Gil OS. It is a persistent, AI-assisted vault where raw information (weekly reviews, books, blood tests, articles, workouts, financial data) gets ingested, synthesized, and transformed into structured knowledge that drives decisions and tracks progress.

### The Core Philosophy

> Life is an operating system. Pillars are processes. The vault is persistent memory.

Most people consume information but never synthesize it. They read a book, forget it in three weeks, and repeat. The Second Brain breaks that cycle:

1. **Raw input** enters via `00-Raw_Sources/` (articles, books, PDFs, data exports, journals, weekly reviews, notes).
2. **An AI librarian** (Claude) ingests, analyzes, and writes structured artifacts.
3. **Knowledge nodes** live in the appropriate pillar (`L1` through `L7`).
4. **Cross-pillar synthesis** surfaces connections that would otherwise stay invisible.
5. **The system compounds**. Each new input becomes richer because it can be cross-referenced against everything already in the vault.

The result is a system that knows your health history, your career trajectory, your projects, your Objectives and Key Results (OKRs), courses, and the books you have read. It can reason across all of them simultaneously.

---

## 2. Directory Architecture

```
second-brain/
├── 00-Raw_Sources/         # Immutable inputs. Read only. Never edited after deposit.
│
├── 01-Entities/            # Nodes for people, organizations, and systems
│
├── L1-Health/              # Synthesized knowledge — Mind & Physical Body
├── L2-Relationships/       # Synthesized knowledge — Relationships
├── L3-Career/              # Synthesized knowledge — Work / Career / Mission
├── L4-Growth/              # Synthesized knowledge — Personal Growth
├── L5-Finance/             # Synthesized knowledge — Finances
├── L6-Hobbies/             # Synthesized knowledge — Hobbies & Life Celebration
├── L7-Contribute/          # Synthesized knowledge — E7 Brand & Publishing
│
├── 02-Indexes/             # Master registry + cross-pillar topic maps
│   ├── index.md            # The authoritative page registry (updated every session)
│   ├── gil_os_master.md    # Canonical Gil OS system definition
│   └── topic_maps/         # Cross-pillar synthesis documents
│
└── 03-System_Logs/
    └── log.md              # Chronological record of every operation performed
```

### Key Rules

- `00-Raw_Sources/` is **immutable**. Once a file is deposited, it is never edited. It is the single source of truth for what was ingested.
- Every new file created in `L1`–`L7` is registered in `02-Indexes/index.md`.
- Every session is logged in `03-System_Logs/log.md` with sources ingested, files created, and critical findings.
- Each pillar directory contains a `_pillar.md` - the schema document that defines the pillar's purpose, OKRs, methodologies, and current status.

---

## 3. The 7 Life Pillar System

Gil OS organizes all of life into seven pillars, numbered L1–L7. The numbering reflects a rough hierarchy of foundation (health) to contribution (teaching/publishing).

| Life Pillar | Name | Core Principle |
|---|---|---|
| **L1** | Mind & Physical Body | Physical health is the substrate for every other pillar. Focuses on health, energy, fitness, nutrition, and mental peace. Example metric: Lift weights three times per week. |
| **L2** | Relationships | Invest in people and nurture relationships. Focuses on your partner, family connections, and close friends. |
| **L3** | Work / Career / Mission | Deep Work on the right problems, not just more work. Focuses on professional growth and daily work output. |
| **L4** | Personal Growth | Skills compound, so build deliberately, not opportunistically. Focuses on skill acquisition, reading, and internal development. |
| **L5** | Finances | Build the financial floor before reaching for the ceiling. Focuses on wealth generation, savings, and lifestyle funding. |
| **L6** | Hobbies & Life Celebration | Joy is not earned after work is done. It makes work sustainable. Focuses on joy, travel, and personal interests outside of work. |
| **L7** | Contribute | The system becomes more powerful when it is shared. Focuses on community impact. |

### 2026 OKRs by Pillar

#### [L1] Mind & Physical Body

Health:

- 😴Sleep 7:20 hr/day
- 🧎🏻Meditate Daily
- 🍎Eat well 4 e/week
- 🍸Alcohol ≤ 3 times e/w
- 🌙Bed time before 10:45pm
- 💤Reduce snoring 1:20 avg
- ☀️ 10 min sunlight 5x e/w
- 📵 Digital Sunset 30 min before sleep 5x e/w

Fitness:

- 🏃🏻‍♂️Exercise 4 times e/w
- 💪10 barras
- 🫀Loose 8kg
- 👤 Body fat 20%
- 🏋 3 heavy lift sessions e/w

#### [L2] Relationships

Relationship with partner:

- 👫Weekly dates 40,
- 💑Trips together 4
- 🏡 Define new place to live (new home)
- 🏦 Bi-weekly Dream & Finance

Family and Friends:

- 🇲🇽Visit Mexico 3 times
- 🇺🇲1 Parents visit
- 🇺🇲1 Siblings visit
- 🛬 Trip to Saltillo

#### [L3] Work / Career / Mission

Career:

- 🧑‍💻 Deep Work 10 hr/w
- 🏆Get path to Principal
- 📓Create Personal CRM 40
- 🚀Launch Serenity Scheduling
- 🤖1 Agent Award
- 🎖️Get Nomination at Work
- 🦾 work <40 e/w
- 🗡️ Launch TPM Samurai

Business:

- 👨🏻‍💼 Relaunch E7
- 🎥Relaunch Youtube Channel
- 📈Get to 100 subscribers
- 📋Get 2 clients

#### [L4] — Persnoal Growth

- 🎧Read/Listen 8 Books
- 📜Get 1 Certificate
- 🤖Complete 2 ML courses
- ✅Weekly Reviews
- 💻 AI/Projects 4

#### [L5] Finances

Personal:

- 📈Continue supporting parents
- 🏥Continue parents insurance
- 💳 Good Credit Score >750

Couple:

- 🏦Savings 5%/mo
- 🧩Positive Cash Flow
- 💰MPI 10%/mo

#### [L6] Hobbies and Celebrate Life

- ⚽️ Join a scoccer team
- 🏌 5 Golf lessons
- 🏝️ visit 4 new spots with Luna

#### [L7] Contribute

- 🪄Write 6 failure posts
- 👨‍💻New Gil’s website
- 🎥Post 12 videos to channel
- 💻Release 3 versions of websites
- ✍️ post 12 new blog posts

---

## 4. The Driver / Passenger Model

Not all pillars are equal at all times. Gil OS uses a **Driver / Passenger** allocation model:

- **Driver pillars** receive primary time and energy. Currently: L1 (Health) and L3-Career (Blue Origin).
- **Passenger pillars** run on fixed, time-boxed windows. E7 (L7 / L3-Business) runs **Saturday mornings only**. When a Driver pillar demands more, the Passenger track pauses. It never competes.

This prevents the common failure mode where a side project (E7) expands into the time budget of the primary mission (Blue Origin / Principal promotion). The Saturday constraint is both a ceiling and a protection mechanism.

---

## 5. Operational Loops

The system runs on three nested loops:

### Annual Loop - OKRs

Set at the start of each year. Reviewed quarterly. Each pillar has 3–5 measurable key results. The OKRs live in `L1`–`L7` pillar schemas and are visible in the master index.

### Weekly Loop - Friday Finish (Weekly Review)

A structured metacognitive session that:

1. Reviews the previous week's Habit Tracker data
2. Identifies the Big Rocks for the coming week (effectiveness, not just activity)
3. Schedules Deep Work blocks aligned to chronotype
4. Captures captures from the week into the vault

The Weekly Review is what separates System 2 (deliberate, rational planning) from Homer Self (reactive, impulsive execution). Without it, the week runs the person instead of the person running the week.

### Daily Loop - Habit Tracker

A lightweight daily capture of: sleep hours, nutrition adherence, exercise type, meditation, reading pages. This feeds the Weekly Review with objective data rather than subjective memory.

---

## 6. The Ingest Protocol

When new material enters the vault, the AI librarian follows a structured ingest process:

1. **Search the vault first** (`hyalo` CLI) — prevent duplicates, surface existing cross-references
2. **Read the source** — extract key information, data, frameworks, and findings
3. **Synthesize, do not copy** — write active-voice, clutter-free artifacts that distill insight, not transcribe content
4. **Place in the correct pillar** — create or update the appropriate `Lx/` file
5. **Update cross-references** — if the content touches multiple pillars, create or update a topic map in `02-Indexes/topic_maps/`
6. **Update the master index** — register the new file in `02-Indexes/index.md`
7. **Log the session** — append a structured entry to `03-System_Logs/log.md` with sources, files, findings, and contradictions resolved

Every session ends with a vault state report: total pages, new critical flags, contradictions resolved, and inbox items remaining.

---

## 7. Tooling & Conventions

| Tool / Convention | Purpose |
|---|---|
| `hyalo` CLI | Search and query the vault before creating new pages (prevents duplicates) |
| `02-Indexes/index.md` | Master page registry — updated every session |
| `03-System_Logs/log.md` | Chronological operation log — never deleted from |
| YAML frontmatter | Required on every new file (`title`, `type`, `status`, `tags`) |
| Active voice | Enforced across all vault writing |
| `_pillar.md` convention | Each `Lx/` directory has a schema document as its root |
| Topic maps | Cross-pillar synthesis files stored in `02-Indexes/topic_maps/` |

---

## Appendix - Session-by-Session Build Log (Real Example)

### Session 1 — Foundation Batch (2026-05-24)

**Sources ingested:** Gil OS system definition, High-Performance OS article, OKRs 2026

**Built:**

- `02-Indexes/gil_os_master.md` — the canonical system definition
- All 7 pillar schemas (`L1` through `L7` `_pillar.md` files)
- `02-Indexes/index.md` — master registry
- `03-System_Logs/log.md` — operation log

**Most important finding:** Four cross-pillar tensions identified at the outset — the most critical being L1↔L3 (health and career are both Drivers; burnout is a structural risk if both demand peak output simultaneously).

**Commands executed:**

> /librarian Execute Ingest Protocol: Read 'Effective_at_Life-Operating_System.md', 'The_High-Performance_Operating_System_How_to_Organize_Your_Life_for_Peace_of_Mind.md', and 'OKRs_2026.md' in 00-Raw_Sources/00-Foundation_Batch/. Write the Gil OS master definition to 02-Indexes/gil_os_master.md. Establish the baseline schema for the L1-L7 pillars, map the 2026 OKRs across the pillars, and immediately rebuild 02-Indexes/index.md.

---

### Session 2 — L1 Health Data (2026-05-24)

**Sources ingested:** Weight tracker (2023–2026), two blood analysis history files (Lifeforce / Spren, 7 draws)

**Built:**

- `L1-Health/weight-tracker.md` — full body composition history with OKR projection
- `L1-Health/blood-analysis.md` — all 7 blood draws, trend analysis
- `L1-Health/biomarker-reference.md` — interpretation reference for all tracked biomarkers
- `02-Indexes/topic_maps/health-performance-crossmap.md` — first L1→L3 risk linkage

**Most important finding:** Total Testosterone declined 34% from its Aug 2023 peak (399 ng/dL) to 262 ng/dL by Jan 2026. At age 33, this is below-expected for natural decline. DHEA-S also fell 53%. This is the first detection of what will become the vault's most critical health flag.

**Commands executed:**

> /librarian Execute Ingest Protocol: Read documents in L1_Batch 'Weight Tracker', 'Blood Analysis Biomarkers', and 'Blood Analysis Historical Results' in 00-Raw_Sources/L1_Batch/. Write the new markdown files to the L1-Health architecture, map any cross-pillar intersections for my health metrics, and immediately rebuild 02-Indexes/index.md.

---

### Session 3 — L1 Books Batch (2026-05-25)

**Sources ingested:** *Outlive* (Peter Attia), *Breaking the Habit of Being Yourself* (Joe Dispenza), *Life Force* (Tony Robbins), *Life Mastery Workbook* (Tony Robbins)

**Built:**

- `L1-Health/book-notes-attia-outlive.md`
- `L1-Health/book-notes-dispenza-breaking-habit.md`
- `L1-Health/book-notes-robbins-lifeforce.md`
- `L1-Health/book-notes-robbins-life-mastery.md`
- `02-Indexes/topic_maps/books-health-synthesis.md`

**Most important finding:** All four books independently diagnose the same root cause for the testosterone crisis — and each provides a different intervention vector. Attia: body composition → metabolic dysfunction. Dispenza: cortisol chemical addiction → HPA axis disruption. Robbins (Life Force): HOT (Hormone Optimization Therapy) as the direct pharmaceutical pathway. Robbins (Life Mastery): supplement stack addressing confirmed biochemical deficiencies. The vault's isolated data point (262 ng/dL) now has a complete four-vector intervention framework.

**Contradiction resolved:** Magnesium Glycinate (recommended in Life Mastery) vs. Magnesium L-Threonate (specified in protocol). L-Threonate crosses the blood-brain barrier; Glycinate does not. L-Threonate is the canonical recommendation for sleep architecture optimization.

**Commands executed:**

> /librarian Execute Ingest Protocol: Read 'Book-Breaking-the-Habit-of-Being-Yourself.md', 'Book-Life-Force\_Tony-Robbins.pdf', 'Book-Outlive-The-Science-And-Art-of-Longevity.md', and 'Life-Mastery-Workbook-Tony-Robbins.pdf' in 00-Raw\_Sources/L1\_Batch/. Write the new markdown files to the L1-Health architecture, map any cross-pillar intersections for my health metrics, and immediately rebuild 02-Indexes/index.md.

---

### Session 4 — Function Health Panel (2026-05-25)

**Source ingested:** Out-of-Range Biomarkers report, Function Health, May 19, 2026

**Built:**

- `L1-Health/blood-analysis-function-may2026.md` — full analysis of 5 out-of-range biomarkers

**Most important finding:** hs-CRP rose from 0.49 mg/L (Jan 2026) to 1.2 mg/L (May 2026) — a 2.4x increase in 4 months. This is systemic inflammation escalating. The Jan 2026 Spren "Heart score 96" was a false sense of security: it measured standard lipid markers, not particle-level data or inflammation. The prior "cardiovascular excellent" verdict was formally revised.

**Five out-of-range results form a unified signal:**

| Biomarker | Value | Severity |
|---|---|---|
| hs-CRP | 1.2 mg/L | 🔴 Critical |
| Glucose | 100 mg/dL | 🟡 Moderate |
| HDL Large | 6,147 nmol/L | 🟡 Moderate |
| LDL Peak Size | 222.4 Å | 🟡 Borderline |
| Omega-3 Total | 5.0% | 🟡 Moderate |

All five share the same upstream root cause: early metabolic dysfunction / visceral fat accumulation. Addressing body composition addresses all five simultaneously.

**Commands executed:**

> /librarian Execute Ingest Protocol: Read 'Out-of-Range-Biomarkers.md', 'Gil-Health-Upgrade-Protocol-Proposal.md', and 'Critical-Biomarkers-for-Male-Longevity-and-Performance.md' in 00-Raw\_Sources/L1\_Batch/. Write the new markdown files to the L1-Health architecture. Cross-reference the out-of-range metrics against the performance longevity benchmarks and your proposed upgrade protocol. Map all cross-pillar intersections. Immediately rebuild 02-Indexes/index.md

---

### Session 5 — Free Testosterone + Protocol (2026-05-25)

**Sources ingested:** Gil Health Upgrade Protocol Proposal, Critical Biomarkers for Male Longevity (Function Health, May 19, 2026)

**Built:**
- `L1-Health/protocol-health-upgrade.md` — 5-domain upgrade protocol
- `L1-Health/biomarker-scorecard-may2026.md` — Medicine 3.0 scorecard, Deficit Score 6/10
- `L1-Health/protocols/biomarker_correction_plan.md` — time-blocked daily execution schedule

**Most important finding:** Free Testosterone measured for the first time at **54.0 pg/mL**. The Medicine 3.0 action trigger is < 150 pg/mL. Gil is at 36% of the optimal minimum. Standard lab range (46–224 pg/mL) classifies this as "In Range" — which is why prior panels showed "healthy" testosterone despite persistent low-T symptoms. The biologically active fraction of testosterone (the part that drives muscle protein synthesis, cognitive dominance, and energy) is critically depleted.

**Key distinction established:** Total Testosterone (300 ng/dL, improving) vs. Free Testosterone (54.0 pg/mL, critical). The Total T improvement is real but largely offset by SHBG binding most of it. The bottleneck is bioavailability, not production.

**Protocol codified:**

- **Training:** Alpha/Beta/Gamma split (3 heavy compound sessions) + Zone 2 cardio + Zone 5 intervals
- **Supplements:** Creatine 5g, Magnesium L-Threonate ~145mg elemental, Omega-3 2g, D3 5,000 IU + K2 100mcg MK-7
- **Daily execution:** Morning supplement window + 10 Power Breaths + post-prandial 10-min walk + Digital Sunset 9 PM
- **Physician consult:** Full hormone panel requested (Free T, SHBG, LH, FSH, Estradiol, DHEA-S, Cortisol AM) + decision tree for Clomiphene / Enclomiphene / TRT

**Commands executed:**

> /librarian Execute Query Protocol: Synthesize the current 'Out-of-Range-Biomarkers' data against the 'Critical-Biomarkers-for-Male-Longevity-and-Performance' benchmarks and the 'Gil-Health-Upgrade-Protocol-Proposal'. Create an actionable, daily execution schedule that addresses the primary health deficiencies. Save this as 'L1-Health/protocols/biomarker\_correction\_plan.md'

---

### Sessions 6 & 7 — Career & Growth Synthesis (2026-06-20)

**Sources ingested:**

- *The 5 Hidden Habits Blocking Your Career Growth* (Jorge Luis Pando, The Effective Company, 10 pages)
- *Effective Week 2024 Curated Edition* (The Effective Company, 106 pages, 39 articles)

**Built:**

- `L3-Career/The-5-Hidden-Habits-Blocking-Your-Career-Growth.md`
- `L3-Career/book-notes-effective-week-2024.md`
- `L4-Growth/book-notes-effective-week-2024.md`
- `02-Indexes/topic_maps/career-productivity-crossmap.md`

**Most important findings:**

**PIE Model Gap — 🔴 Critical Career Flag**
Harvey Coleman's PIE research: career advancement is 10% Performance, 30% Image, 60% Exposure. L3 has no Image OKR. Gil tracks zero Image input metrics. The promotion case depends on Performance and a vague Exposure KR. Recommended fix: quarterly peer perception check + quarterly communication improvement goal.

**Deep Work Math Failure**
Async communication consumes ~6.2 hr/day (185 interactions × 2 min average). Meetings consume 25–50% of the workweek on top of that. In a 40-hour week, the remaining time available for Deep Work is 0–9 hours. The 10 hr/week Deep Work target requires three simultaneous interventions — GTD triage, communication norms, and chronotype-aligned scheduling. Any one or two alone are insufficient.

**L4 → L7 Teaching Loop (Not Yet Wired)**
Every book Gil reads could directly produce one E7 newsletter issue (Feynman Technique). Every ML course module could generate one TPM Samurai post. This removes the E7 "what to write about" bottleneck, converts L4 activity into L7 output, and generates L3 Exposure simultaneously. The loop shares the same raw material across three pillars — but is not yet connected.

**Stakeholder Map is the Missing System Input**
The Principal promotion loop (Manage Up → PIE Exposure → Sponsor relationship → Nomination) breaks at the Managing Up step if contributions are invisible. The 7-point 1:1 structure + stakeholder map (name / last touch / feedback / follow-up) are the two structural inputs that make the entire promotion system functional. Neither is currently built.

**Commands executed:**
> /librarian Execute Ingest Protocol: Read 'Copy of The 5 Hidden Habits Blocking Your Career Growth.pdf' and 'Copy of Effective Week 2024 Curation.pdf' in 00-Raw_Sources/L4_Batch/. Write the new markdown files to the L4-Growth and L3-Career architectures, map cross-pillar intersections regarding career progression and productivity systems, and immediately rebuild 02-Indexes/index.md

---

*This document is a teaching artifact. It is not registered in the vault index and does not affect the vault page count or operational state.*
