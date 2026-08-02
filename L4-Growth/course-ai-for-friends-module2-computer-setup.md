---
title: "AI for Friends — Module 2: Setting Up Your Computer (Optional Warm-Up)"
type: course-notes
pillar_id: L4
source_file:
  - "00-Raw_Sources/L4_Growth/2026-08-02/2-0_Setting_Up_Computer.md"
  - "00-Raw_Sources/L4_Growth/2026-08-02/2-1_Installing_Windows_terminal.md"
  - "00-Raw_Sources/L4_Growth/2026-08-02/2-2_Intalling_VS_Code.md"
  - "00-Raw_Sources/L4_Growth/2026-08-02/2-3_Navigating_Terminal.md"
created: 2026-08-02
tags: [l4, growth, ai, course, terminal, vs-code, windows]
related: [L4-Growth/course-ai-for-friends, L4-Growth/course-ai-for-friends-module3-claude-code]
---

# AI for Friends — Module 2: Setting Up Your Computer (Optional Warm-Up)

Synthesis of Lessons 2.1–2.3 (~25 min total). Explicitly optional: a low-stakes practice room for anyone who has never opened a terminal or code editor, aimed at making Module 3's real install feel familiar. Nothing here is a prerequisite — Module 3 installs everything from scratch and covers the terminal on its own. Windows 10/11 only, matching Module 3's install guide.

If only one lesson gets done, the course explicitly names **Lesson 2.3** as the one worth doing — it teaches the terminal commands Module 3 assumes the learner already knows.

---

## Lesson 2.1 — Installing Windows Terminal: **content gap**

The source file `2-1_Installing_Windows_terminal.md` is empty. Per the Module 2 index, this lesson should cover installing a standalone terminal from the Microsoft Store and setting PowerShell as its default profile — but no lesson content exists to synthesize. Low-impact gap: Module 3 uses VS Code's built-in integrated terminal instead of a standalone terminal app, so this lesson is skippable without consequence even within Module 2's own scope.

---

## Lesson 2.2 — Installing VS Code (Early Look)

A deliberately lighter, earlier pass at an install Module 3 covers in full — the goal is familiarity, not completeness.

1. Download from `code.visualstudio.com` (official site only) and install with default options.
2. Locate the **Extensions panel** (four-squares icon in the left sidebar, or `Ctrl+Shift+X`) and browse — install nothing yet. Module 3 specifies exactly which extensions to add.

---

## Lesson 2.3 — Navigating the Terminal (the lesson that matters)

Four commands cover the whole skill Module 3 assumes:

| Command | Does | Example |
|---|---|---|
| `pwd` | Shows current folder | `pwd` |
| `ls` | Lists files/folders in current location | `ls` |
| `cd FolderName` | Moves into a folder | `cd Documents` |
| `cd ..` | Moves up one level | `cd ..` |

Key reassurance: nothing executes until Enter is pressed, and a typo just produces a harmless error — it's not possible to break anything this way.

**Practice exercise** (7 commands, building a real folder structure):
```powershell
cd ~
pwd
mkdir ai-practice
cd ai-practice
mkdir shared
mkdir candidate-review
ls
```
Result: `~/ai-practice/{shared, candidate-review}` — confirmable by cross-checking in File Explorer.

> **Source-file note:** the raw file `2-3_Navigating_Terminal.md` contains this lesson's genuine content in its first ~162 lines. From that point on, the file is a copy-paste artifact duplicating the entire Module 3 index page (near-identical to `3-0_Claude-Code.md`). Only the true Lesson 2.3 content above was synthesized here; the duplicated tail was treated as a source-quality issue, not additional content — see [Module 3 Notes](course-ai-for-friends-module3-claude-code.md) for that material's actual home.

---

## What's Next

Module 3 ("Claude Code — AI on Your Own Files") is the real setup and does not depend on anything in this module.
