---
title: "AI for Friends — Module 3: Claude Code"
type: course-notes
pillar_id: L4
source_file:
  - "00-Raw_Sources/L4_Growth/2026-08-02/3-0_Claude-Code.md"
  - "00-Raw_Sources/L4_Growth/2026-08-02/3-1_Claude_Code_Installation.md"
created: 2026-08-02
tags: [l4, growth, ai, course, claude-code, vs-code, confidentiality, tooling]
related: [L4-Growth/course-ai-for-friends, L4-Growth/course-ai-for-friends-module1-foundations, L3-Career/_pillar, 02-Indexes/topic_maps/ai-course-cross-pillar-map]
---

# AI for Friends — Module 3: Claude Code — AI on Your Own Files

Synthesis of the module index (`3-0`) and the full onboarding guide (`3-1`, 75–90 min). Targets HR, industrial engineering, legal, and marketing professionals working across many documents at once. Core distinction: the web version of Claude is a conversation *about* documents; Claude Code works *directly on* them, inside a folder the learner opens, showing every proposed change as an approve/reject diff before anything saves.

---

## 1. When to Use What

| Need | Tool |
|---|---|
| Quick one-off question, no files | claude.ai (web) |
| Edit/create ONE Word/Excel/PowerPoint file | Claude Cowork |
| Work across MANY files, or a repeatable process | **Claude Code** |

Nine concrete advantages over web chat: whole-folder input (not one-by-one uploads), output lands as real saved files, bulk/repetitive work becomes one instruction, a `CLAUDE.md` file persists standing instructions across sessions, every edit is a reviewable diff, workflows are repeatable, multi-step work completes in one pass, files stay scoped to the opened folder only, and it works with the existing folder structure. Web chat remains better for phone use, brainstorming, quick questions with no files, and image/screenshot analysis — most users need both tools.

**Role-specific before/after** (illustrative, HR example): summarizing 40 résumés against a job description goes from 40 separate uploads with no consolidated output (web) to one folder → one ranked summary file (Claude Code). Legal, Marketing, and Industrial Engineering have parallel before/after tables in the source (clause comparison across contracts, campaign-copy consistency audits, shift-report cycle-time extraction).

---

## 2. Confidentiality — Read Before Using

> **Personal Claude Pro has no corporate data agreement, admin oversight, audit logs, or retention controls.** Practice on non-sensitive material only. Before running client files, employee records, or privileged material through it, check with IT/Legal — a Claude Team/Enterprise plan may be required instead.

This is the single most work-relevant guardrail in the course. It applies directly to Gil's own use of Claude Code on anything Blue-Origin-adjacent — see the compliance cross-pillar flag in [[02-Indexes/topic_maps/ai-course-cross-pillar-map]].

Safety habits taught alongside it: always read the diff before approving; default to Plan Mode for anything real; scope tightly (open the specific project folder, never `Documents` or the desktop root); keep a backup before bulk operations; never paste passwords/API keys/bank details; never run employee PII, salary data, investigation files, or privileged client material through a personal Pro plan without employer approval.

---

## 3. Installation (Windows + VS Code + Claude Pro)

1. **Claude Pro** — claude.ai → Settings → Upgrade to Pro (~$20/mo; the free tier does not include Claude Code).
2. **VS Code** — `code.visualstudio.com`, User Installer 64-bit, keep "Add to PATH" checked.
3. **Git for Windows** (recommended) — `git-scm.com/downloads/win`, defaults; adds Git Bash.
4. **Claude Code** — open Windows PowerShell, run `irm https://claude.ai/install.ps1 | iex`, then close and reopen the terminal (settings only apply to new windows).
5. **First run** — type `claude`, log in via Claude.ai account (not API key).
6. **Verify** — `claude --version`, `claude doctor`, then `claude` and say hello.

Common fixes: `claude` not recognized → reopen terminal, else add `%USERPROFILE%\.local\bin` to PATH; login/plan errors → confirm Pro is active in Settings; Defender/SmartScreen warnings on the installer are expected — only ever run it from the official `claude.ai` URL.

---

## 4. Recommended VS Code Extensions

| Tier | Extension | Publisher | Why |
|---|---|---|---|
| 1 | Claude Code | Anthropic | Graphical chat panel inside VS Code |
| 1 | Markdown All in One | Yu Zhang | Live preview, auto-TOC, formatting |
| 1 | Code Spell Checker | Street Side Software | Catches typos in drafts/policies |
| 1 | Rainbow CSV | mechatroner | Readable columns for .csv exports |
| 1 | vscode-pdf | tomoki1207 | View PDFs inside VS Code |

Tier 2 (situational): Excel Viewer/Data Preview, Markdown PDF export, Speech (local dictation), Draw.io Integration, Todo Tree, Live Share, Word Count. Explicitly skip developer-oriented extensions — GitLens, Docker, Python, ESLint, Prettier, language servers, Copilot — they add nothing for document work.

---

## 5. Terminal Basics and the Hands-On Tutorial

Six commands cover the entire guide: `pwd`, `dir`/`ls`, `cd foldername`, `cd ..`, `cls`/`clear`, `Ctrl+C`. Use only the VS Code integrated terminal (`Ctrl+` backtick).

**Core safety concept — the Project Folder:** Claude can only see and touch files inside the one folder opened in VS Code. Nothing outside it is visible or reachable.

**Tutorial arc** (sandbox folder with 3–5 non-confidential documents):
1. Ask a read-only question — zero risk, establishes that plain sentences work as commands.
2. Have Claude create a file (`summary.md`) — introduces the **permission prompt** (allow-once / allow-always / deny), the most important safety concept in the guide.
3. Have Claude edit that file and review the **diff** (side-by-side before/after) before approving — for Legal, functionally a redline review.
4. The bulk task (the real payoff): one instruction extracts title/date/topic from every document in the folder into a single `index.csv` — replacing what would be one upload-and-prompt cycle per document on the web.

**Plan Mode** (`Shift+Tab` twice, or `/plan`) restricts Claude to reading/thinking until a written plan is approved — the recommended default posture for anything touching real work.

**`CLAUDE.md`** is a plain-text file of standing instructions read automatically every session in that folder — brand voice/banned words (Marketing), required disclaimers/tone (HR), defined terms/citation format (Legal). Five lines is enough to change the next response noticeably.

**Essential slash commands:** `/help`, `/clear` (fresh start, also protects usage limits), `/model`, `/plan`, `/status`, `/doctor`, `/voice`.

**Talking to Claude effectively:** name the file and the job, one task at a time, state what "done" looks like (format/length/audience), use `@filename` to target a document. Vague → specific example: "Check these contracts" → "Flag any indemnity clause that caps liability below $1M."

**Usage limits:** Claude Pro has rolling ~5-hour session caps plus weekly caps, shared between web chat and Claude Code — `/clear` between unrelated tasks and avoid pointing at unnecessarily large folders.

---

## What's Next

Module 4 ("Building Your AI Personal Assistant" — Claude Projects/agents) is referenced as the natural continuation but has no source content in this raw batch. See the gap note in [Course Overview](course-ai-for-friends.md).
