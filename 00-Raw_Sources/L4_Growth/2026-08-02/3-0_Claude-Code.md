<!-- HERO: Module 3: Claude Code — AI on Your Own Files | Point an AI assistant at a folder of your real documents and have it draft, edit, and organize them for you. No technical background required. -->

<!-- TOC: Overview#anchor-overview | Lessons in This Module#anchor-lessons | Key Concepts#anchor-concepts | What's Next#anchor-next -->

## Overview

Claude Code is an AI assistant that works directly on the files and folders on your computer. You ask in plain English; it reads, drafts, edits, and organizes real documents. It shows you every proposed change before saving anything, so nothing lands without your approval.

### Who This Module Is For

This module targets professionals who work across many documents at once. No programming experience or terminal background is required.

**Target roles:**
- HR professionals
- Industrial engineering professionals
- Legal professionals
- Marketing professionals

### Why This Matters

The web version of Claude is a conversation *about* your documents. Claude Code works *on* them. Point it at a folder of many files and one instruction replaces dozens of individual uploads or copy-pastes. Output lands as real saved files, and every edit arrives as a before/after view you approve or reject.

### What This Looks Like in Your Role

| Role | What Changes |
|---|---|
| **HR** | Screen 40 résumés against one job description in a single pass instead of uploading them one by one. Standardize many job descriptions to one template as a batch rewrite, each saved back in place. |
| **Industrial Engineering** | Compare cycle-time and downtime data across many shift reports in a single pass instead of exporting each one separately. Standard operating procedures and process terminology (takt time, changeover, OEE) live permanently in a CLAUDE.md file instead of being re-explained each session. |
| **Legal** | Compare a clause such as indemnity language across many agreements in one pass with a single comparison table. Every edit arrives as a redline-style diff you approve or reject, and defined terms live permanently in a CLAUDE.md file instead of being re-explained each session. |
| **Marketing** | Turn one piece of content into several channel variants as separate saved files from one instruction. Your brand voice and banned-words list live in CLAUDE.md and apply to everything drafted in that folder instead of being re-pasted into every chat. |

### By the End of This Module, You Will

- Understand what Claude Code does that the web version cannot, and when the web version is still the better choice
- Have Claude Code installed and connected to your Claude Pro account
- Run a real task against a folder of your own documents and get a saved file back
- Know the safety habits that keep the tool scoped: Plan Mode, diff review, and tight folder scoping

### Prerequisites

- Claude Pro plan active (~$20/mo; the free tier does not include Claude Code)
- Windows 10 (build 1809+) or Windows 11, 4 GB+ RAM, and the ability to install software
- A folder of non-confidential practice documents

### Time to Complete

**75 to 90 minutes**, one lesson. Best done in one sitting.

---

<!-- ANCHOR: anchor-overview -->

<!-- ANCHOR: anchor-lessons -->

## Lessons in This Module

| # | Lesson | Duration | What You Will Learn |
|---|--------|----------|---------------------|
| 3.1 | [Claude Code Onboarding Guide](3-1-claude-code-installation.md) | 75-90 min | When to use the web version versus Claude Code, full install and login, recommended VS Code extensions, terminal basics, a hands-on tutorial ending in a real saved file, CLAUDE.md, and reusable slash commands. |

<!-- WARNING: Confidentiality — Read This Before You Start | Claude Pro is a personal subscription with no corporate data agreement, admin oversight, audit logs, or retention controls. Practice on non-sensitive material. Before running real client files, employee records, or privileged material through it, check with your employer's IT or Legal team. -->

<!-- NOTE: You Cannot Break Your Computer | Claude asks permission before it changes anything and shows you exactly what it plans to change. Plan Mode restricts it to reading and thinking until you approve a written plan. -->

<!-- INFO: When the Web Version Is Still Better | Use the web version for quick one-off questions with no files, working from your phone, brainstorming out loud, or image and screenshot analysis. Most people use both. -->

---

<!-- ANCHOR: anchor-concepts -->

## Key Concepts

Core terms introduced in this module. The lesson where each term is first defined is listed so you can return to the source explanation.

| Term | Defined In | Plain English Meaning |
|------|-----------|----------------------|
| **Claude Code** | Lesson 3.1 | An AI assistant that reads, drafts, and edits the real files in a folder you open on your computer. |
| **VS Code** | Lesson 3.1 | The free Microsoft program Claude Code runs inside. Like Word, but built to open a whole folder of files at once. |
| **Project Folder** | Lesson 3.1 | The one folder you open. Claude can only see and touch files inside it, and nothing else. |
| **Terminal** | Lesson 3.1 | A text box where you type instructions instead of clicking. You need about six commands total. |
| **Diff** | Lesson 3.1 | A side-by-side before/after view of a change Claude proposes, which you approve or reject. |
| **CLAUDE.md** | Lesson 3.1 | A plain-text file of standing instructions Claude reads automatically at the start of every session in that folder. |
| **Slash Command** | Lesson 3.1 | A saved, reusable prompt you trigger with a short `/name` instead of retyping a long instruction. |

<!-- EXPAND: Full Key Concepts Reference -->

| Term | Defined In | Plain English Meaning |
|------|-----------|----------------------|
| **Claude Cowork** | Lesson 3.1 | The option built for editing or creating a single Word, Excel, or PowerPoint file, with no terminal needed. |
| **Plan Mode** | Lesson 3.1 | A setting that limits Claude to reading and thinking until you approve a written plan. Your best guardrail. |
| **Permission Prompt** | Lesson 3.1 | The ask that appears before Claude writes or edits. Options are allow-once, allow-always, or deny. |
| **Integrated Terminal** | Lesson 3.1 | The terminal panel built into VS Code, opened with Ctrl and the backtick key. The only terminal you need. |
| **PowerShell** | Lesson 3.1 | A built-in Windows program for typing instructions. Used once, just for the install. |
| **PATH** | Lesson 3.1 | The list of places Windows looks for programs. A command must be on it to run from any folder. |
| **Extension** | Lesson 3.1 | A small add-on for VS Code, like an app for your phone, that adds features such as PDF viewing or spell check. |
| **Markdown (.md)** | Lesson 3.1 | A simple plain-text formatting style. The recommended format to work in, exporting to Word or PDF at the end. |
| **Model** | Lesson 3.1 | The specific AI doing the work, such as Sonnet or Opus, shown in the prompt's model indicator. |
| **Token** | Lesson 3.1 | A unit of text usage that counts against your plan limit. |
| **Usage Limits** | Lesson 3.1 | Claude Pro's rolling roughly 5-hour session caps plus weekly caps. Web chat and Claude Code share one pool. |
| **Git for Windows** | Lesson 3.1 | A recommended free install that adds Git Bash, an alternative terminal, to your machine. |

<!-- /EXPAND -->

---

<!-- ANCHOR: anchor-next -->

## What's Next

**Next Module:** [Module 4: Building Your AI Personal Assistant](4-agents.md)

Module 4 covers how to build a Claude Project — a workspace that remembers your standing instructions and draws on your own reference documents, so you stop re-explaining yourself every time you open a new chat.

**Support Resources:**

| Resource | Link | Purpose |
|----------|------|----------|
| Claude | claude.ai | Sign up and use Claude in your browser |
| Claude Docs | code.claude.com/docs | Official documentation |
| Claude Support | support.claude.com | Help center and account support |

<!-- CHILDREN -->