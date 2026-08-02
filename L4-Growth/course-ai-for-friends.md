---
title: "AI for Friends — Course Overview"
type: course-notes
pillar_id: L4
owner: Gilberto Silva Gonzalez
created: 2026-08-02
last_updated: 2026-08-02
status: active
tags: [l4, growth, ai, course, teaching, claude-code, prompting]
sources:
  - "00-Raw_Sources/L4_Growth/2026-08-02/1-0_AI_Foundations_module.md"
  - "00-Raw_Sources/L4_Growth/2026-08-02/1-1_How_AI_Models_Work.md"
  - "00-Raw_Sources/L4_Growth/2026-08-02/1-2_Prompt_Engineering_vs_Context_Engineering.md"
  - "00-Raw_Sources/L4_Growth/2026-08-02/1-3_Practical_Prompting_Techniques.md"
  - "00-Raw_Sources/L4_Growth/2026-08-02/1-4_Chossing_AI_Model.md"
  - "00-Raw_Sources/L4_Growth/2026-08-02/2-0_Setting_Up_Computer.md"
  - "00-Raw_Sources/L4_Growth/2026-08-02/2-1_Installing_Windows_terminal.md"
  - "00-Raw_Sources/L4_Growth/2026-08-02/2-2_Intalling_VS_Code.md"
  - "00-Raw_Sources/L4_Growth/2026-08-02/2-3_Navigating_Terminal.md"
  - "00-Raw_Sources/L4_Growth/2026-08-02/3-0_Claude-Code.md"
  - "00-Raw_Sources/L4_Growth/2026-08-02/3-1_Claude_Code_Installation.md"
related: [L4-Growth/_pillar, L4-Growth/course-ai-for-friends-module1-foundations, L4-Growth/course-ai-for-friends-module2-computer-setup, L4-Growth/course-ai-for-friends-module3-claude-code, 01-Entities/ai-for-friends-course, 02-Indexes/topic_maps/ai-course-cross-pillar-map]
---

# AI for Friends — Course Overview

"AI for Friends" is an AI-literacy course Gil created and taught to his friends, targeting non-technical professionals (HR, industrial engineering, legal, marketing) with no prior AI or coding background. It teaches AI fluency conceptually, then hands-on tool setup, culminating in Claude Code as a document-automation assistant. This page indexes the course; module-level synthesis lives in the three linked files below.

---

## Course Structure

| Module | Status | Time | Synthesis |
|---|---|---|---|
| 1 — AI Foundations | Complete (5 files: 1-0 index + 1-1 to 1-4) | 55–70 min | [Module 1 Notes](course-ai-for-friends-module1-foundations.md) |
| 2 — Setting Up Your Computer (optional warm-up) | Partial — 1 of 4 source files empty | 25 min | [Module 2 Notes](course-ai-for-friends-module2-computer-setup.md) |
| 3 — Claude Code | Complete (2 files: 3-0 index + 3-1 lesson) | 75–90 min | [Module 3 Notes](course-ai-for-friends-module3-claude-code.md) |
| 4 — Building Your AI Personal Assistant (Claude Projects/agents) | **Not created** — referenced as "what's next" in Modules 2 and 3, no source content exists | — | — |

Target audience across all modules: HR, industrial engineering, legal, and marketing professionals. Module 2 is explicitly optional — Module 3 is fully self-contained and does not depend on it.

---

## Source Quality Notes

- **`2-1_Installing_Windows_terminal.md` is empty.** Module 2's index (`2-0`) references this lesson (installing standalone Windows Terminal + setting PowerShell as default), but the source file has no content. Not fabricated here — flagged as a gap. Module 3 does not depend on it (it uses VS Code's integrated terminal instead), so the gap has no downstream effect on Module 3.
- **`2-3_Navigating_Terminal.md` contains a concatenation artifact.** Lines 1–162 are the genuine Lesson 2.3 content (terminal commands + practice exercise). From line 163 onward, the file duplicates the entire Module 3 index page content almost verbatim (matching `3-0_Claude-Code.md`). Only the first part was treated as Lesson 2.3; the duplicated tail was not double-counted in synthesis.
- **Module 4 has no source material** in this raw batch — only forward references ("what's next: Building Your AI Personal Assistant / Claude Projects") in `2-0` and `3-0`. If Gil creates Module 4 content later, ingest it as a new raw-source batch and add a fourth module-notes file here.

---

## Cross-Pillar Links

| Link | Direction | Note |
|---|---|---|
| [[L3-Career/_pillar]] | L4 → L3 | Course creation/delivery is evidence for the Agent Award KR and the Principal-promotion AI-differentiator narrative; the confidentiality/compliance content in Module 3 applies directly to Gil's own Blue Origin work |
| [[L7-Contribute/_pillar]] | L4 → L7 | Realized instance of the previously-unwired "L4 → L7 Teaching Loop" ([[02-Indexes/topic_maps/career-productivity-crossmap]]) — course material is ready-made content for the blog/video KRs |
| [[01-Entities/ai-for-friends-course]] | — | Connecting entity node for this course across pillars |

Full analysis: [[02-Indexes/topic_maps/ai-course-cross-pillar-map]]

---

## Notes

- Counts toward the L4 2026 OKR "4 AI/side projects" ([[L4-Growth/_pillar]]).
- Course source files use a custom HTML-comment markup (`<!-- HERO -->`, `<!-- TOC -->`, `<!-- ANCHOR -->`, `<!-- EXPAND -->`) consistent with export from a course-building platform, not native vault Markdown. Synthesis here is written in the vault's own conventions rather than preserving that markup.
- Two filenames in the raw batch contain typos (`1-4_Chossing_AI_Model.md`, `2-2_Intalling_VS_Code.md`) — left as-is since `00-Raw_Sources` is immutable.
