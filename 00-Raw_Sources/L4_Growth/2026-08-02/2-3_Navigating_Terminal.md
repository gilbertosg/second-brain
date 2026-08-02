<!-- HERO: Lesson 2.3: Navigating in the Terminal | Four commands. That's the whole skill - and the real reason this module exists. -->

<!-- TOC: Overview#anchor-overview | Step 1: Learn the Four Commands#anchor-step-1 | Step 2: Run the Practice Exercise#anchor-step-2 | Step 3: Confirm What You Built#anchor-step-3 | Verification#anchor-verification -->

## Overview

By the end of this lesson, you will know four terminal commands and use them to create and inspect folders. This is the practical core of the optional module: type a command, press Enter, read the result.

### Why This Matters

Module 3 assumes you can type a command in a terminal and understand what comes back. That is the entire skill this lesson builds. Four commands cover it. Practice them once and the setup steps in Module 3 stop feeling foreign.

### Prerequisites

- None. This module is optional.

### Time to Complete

**~10 minutes**

<!-- PROGRESS: Step 1: The Four Commands | Step 2: Practice Exercise | Step 3: Confirm What You Built | Verification -->

---

<!-- ANCHOR: anchor-overview -->

<!-- TIP: The One Lesson Worth Doing | If you only do one lesson in this optional module, do this one. Module 3 assumes you can type a command and read the result. -->

<!-- ANCHOR: anchor-step-1 -->

## Step 1: Learn the Four Commands

A terminal is just a place to type instructions to your computer. You only need four commands to move around and see what is there. Everything else in Module 3 builds on these.

### What You'll Do

You will read a four-command table and understand what each one does before you type anything.

### Instructions

1. Read each command in the table below.
2. Note the example in the right column for each one.
3. Do not type anything yet. Just read.
4. Keep this table open. You will use it in the next step.

### The Four Commands

| Command | What It Does | Example |
|---|---|---|
| `pwd` | Shows what folder you're currently in | Type `pwd`, press Enter |
| `ls` | Shows all files and folders in your current location | Type `ls`, press Enter |
| `cd FolderName` | Moves you INTO a folder | `cd Documents` |
| `cd ..` | Moves you UP one folder level | `cd ..` |

<!-- INFO: Nothing Runs Until You Press Enter | Typing a command does nothing on its own. The terminal waits for you to press Enter before it acts. This means you can always fix a typo before running it. -->

<!-- TIP: A Typo Just Produces an Error | If you mistype a command, the terminal prints an error and does nothing harmful. Read the error, retype the command, and try again. You cannot break anything this way. -->

---

<!-- ANCHOR: anchor-step-2 -->

## Step 2: Run the Practice Exercise

Now you type. This short exercise moves you to your home folder, creates a practice folder with two subfolders, and lists them. Type one line, press Enter, read the result, then move to the next line.

### What You'll Do

You will type seven commands one at a time, pressing Enter after each and reading the output before continuing.

### Instructions

1. Type the first line, then press Enter.
2. Read whatever the terminal prints back.
3. Type the next line, press Enter, and read again.
4. Continue one line at a time until all seven are done.

### The Practice Block

```powershell
cd ~
pwd
mkdir ai-practice
cd ai-practice
mkdir shared
mkdir candidate-review
ls

<!-- ANCHOR: anchor-step-3 -->[cite: 1]

## Step 3: Confirm What You Built[cite: 1]

Reading the output tells you each command worked. This step maps every line you typed to what it did, then shows the folder structure you created. Confirming the result is how you build trust in the commands.[cite: 1]

### What You'll Do[cite: 1]

You will review what each command did and picture the folder structure now on your computer.[cite: 1]

### Instructions[cite: 1]

1. Read the table below, matching each command to its effect.[cite: 1]
2. Look at the folder tree that follows it.[cite: 1]
3. Open File Explorer and find the `ai-practice` folder to see the same thing visually.[cite: 1]

### What Each Command Did[cite: 1]

| Command | What It Did |[cite: 1]
|---|---|[cite: 1]
| `cd ~` | Moved you to your home folder |[cite: 1]
| `pwd` | Showed you where you are |[cite: 1]
| `mkdir ai-practice` | Created a new folder called "ai-practice" |[cite: 1]
| `cd ai-practice` | Moved you into that folder |[cite: 1]
| `mkdir shared` | Created a subfolder called "shared" |[cite: 1]
| `mkdir candidate-review` | Created a subfolder called "candidate-review" |[cite: 1]
| `ls` | Showed you the folders you just created |[cite: 1]

### The Structure You Now Have[cite: 1]

C:\Users\YourName

|_ ai-practice

|_ shared

|_ candidate-review\


<!-- TIP: Cross-Check With File Explorer | Open File Explorer, go to your home folder, and find ai-practice. Seeing the same folders you made in the terminal proves the commands did exactly what you typed. -->[cite: 2]

<!-- INFO: That's the Whole Skill | This is everything you need. When you reach Module 3, typing commands in a terminal will already feel routine. -->[cite: 2]

---[cite: 2]

<!-- ANCHOR: anchor-verification -->[cite: 2]

## Verification[cite: 2]

You have completed all three steps. Confirm your understanding by checking each item below:[cite: 2]

- [ ] You can state which folder you're in using `pwd`[cite: 2]
- [ ] `ls` lists shared and candidate-review inside ai-practice[cite: 2]
- [ ] You can move into a folder and back up one level without looking at the table[cite: 2]

<!-- NOTE: Not Working? | If `ls` does not show your subfolders, revisit Step 2 and confirm you ran `cd ai-practice` before creating them. The command table in Step 1 is your reference. -->[cite: 2]

---[cite: 2]

<!-- CELEBRATION: Lesson Complete! | You now know the four commands that carry you through every terminal step in this course, and you have used them to create real folders. -->[cite: 2]

### What's Next[cite: 2]

You've finished this optional warm-up. When you reach Module 3, typing commands in a terminal and browsing an editor will already feel routine - the real setup starts there.[cite: 2]

**Related Resources:**[cite: 2]
- [claude.ai](https://claude.ai) - The Claude AI platform[cite: 2]
- [Claude documentation](https://code.claude.com/docs) - Official documentation[cite: 2]
- [Claude support](https://support.claude.com) - Help center and troubleshooting[cite: 2]

<!-- TIP: Practice Once More | Open a terminal, run `pwd` and `ls`, then `cd` into a folder and back out with `cd ..`. Repeating the loop once more locks in the muscle memory before Module 3. -->[cite: 2]

<!-- CHILDREN -->[cite: 2]

<!-- HERO: Module 3: Claude Code - AI on Your Own Files | Point an AI assistant at a folder of your real documents and have it draft, edit, and organize them for you. No technical background required. -->[cite: 3]

<!-- TOC: Overview#anchor-overview | Lessons in This Module#anchor-lessons | Key Concepts#anchor-concepts | What's Next#anchor-next -->[cite: 3]

## Overview[cite: 3]

Claude Code is an AI assistant that works directly on the files and folders on your computer. You ask in plain English; it reads, drafts, edits, and organizes real documents. It shows you every proposed change before saving anything, so nothing lands without your approval.[cite: 3]

### Who This Module Is For[cite: 3]

This module targets professionals who work across many documents at once. No programming experience or terminal background is required.[cite: 3]

**Target roles:**[cite: 3]
- HR professionals[cite: 3]
- Legal professionals[cite: 3]
- Marketing professionals[cite: 3]

### Why This Matters[cite: 3]

The web version of Claude is a conversation *about* your documents. Claude Code works *on* them. Point it at a folder of many files and one instruction replaces dozens of individual uploads or copy-pastes. Output lands as real saved files, and every edit arrives as a before/after view you approve or reject.[cite: 3]

### What This Looks Like in Your Role[cite: 3]

| Role | What Changes |[cite: 3]
|---|---|[cite: 3]
| **HR** | Screen 40 resumes against one job description in a single pass instead of uploading them one by one. Standardize many job descriptions to one template in a batch rewrite, each saved back in place. |[cite: 3]
| **Legal** | Compare a clause such as indemnity language across many agreements in one pass with a single comparison table. Every edit arrives as a redline-style diff you approve or reject, and defined terms live permanently in a CLAUDE.md file instead of being re-explained each session. |[cite: 3]
| **Marketing** | Turn one piece of content into several channel variants as separate saved files from one instruction. Your brand voice and banned-words list live in CLAUDE.md and apply to everything drafted in that folder instead of being re-pasted into every chat. |[cite: 3]

### By the End of This Module, You Will[cite: 3]

- Understand what Claude Code does that the web version cannot, and when the web version is still the better choice[cite: 3]
- Have Claude Code installed and connected to your Claude Pro account[cite: 3]
- Run a real task against a folder of your own documents and get a saved file back[cite: 3]
- Know the safety habits that keep the tool scoped: Plan Mode, diff review, and tight folder scoping[cite: 3]

### Prerequisites[cite: 3]

- Claude Pro plan active (~$20/mo; the free tier does not include Claude Code)[cite: 3]
- Windows 10 (build 1809+) or Windows 11, 4 GB+ RAM, and the ability to install software[cite: 3]
- A folder of non-confidential practice documents[cite: 3]

### Time to Complete[cite: 3]

**~75 to 90 minutes**, one lesson. Best done in one sitting.[cite: 3]

---[cite: 3]

<!-- ANCHOR: anchor-overview -->[cite: 3]

<!-- ANCHOR: anchor-lessons -->[cite: 3]

## Lessons in This Module[cite: 3]

| # | Lesson | Duration | What You Will Learn |[cite: 3]
|---|---|---|---|[cite: 3]
| 3.1 | [Claude Code Onboarding Guide](3-1-claude-code-installation.md) | 75-90 min | When to use the web version versus Claude Code, full install and login, recommended VS Code extensions, terminal basics, a hands-on tutorial ending in a real saved file, CLAUDE.md, and reusable slash commands. |[cite: 3]

<!-- WARNING: Confidentiality - Read This Before You Start | Claude Pro is a personal subscription with no corporate data agreement, admin oversight, audit logs, or retention controls. Practice on non-sensitive material. Before running real client files, employee records, or privileged material through it, check with your employer's IT or Legal team. -->[cite: 3]

<!-- NOTE: You Cannot Break Your Computer | Claude asks permission before it changes anything and shows you exactly what it plans to change. Plan Mode restricts it to reading and thinking until you approve a written plan. -->[cite: 3]

<!-- INFO: When the Web Version is Still Better | Use the web version for quick one-off questions with no files, working from your phone, brainstorming out loud, or image and screenshot analysis. Most people use both. -->[cite: 3]

---[cite: 3]

<!-- ANCHOR: anchor-concepts -->[cite: 3]

## Key Concepts[cite: 3]

Core terms introduced in this module. The lesson where each term is first defined is listed so you can return to the source explanation.[cite: 3]

| Term | Defined In | Plain English Meaning |[cite: 3]
|---|---|---|[cite: 3]
| **Claude Code** | Lesson 3.1 | An AI assistant that reads, drafts, and edits the real files in a folder you open on your computer. |[cite: 3]
| **VS Code** | Lesson 3.1 | The free Microsoft program Claude Code runs inside. Like Word, but built to open a whole folder of files at once. |[cite: 3]
| **Project Folder** | Lesson 3.1 | The one folder you open. Claude can only see and touch files inside it, and nothing else. |[cite: 3]
| **Terminal** | Lesson 3.1 | A text box where you type instructions instead of clicking. You need about six commands total. |[cite: 3]
| **Diff** | Lesson 3.1 | A side-by-side before/after view of a change Claude proposes, which you approve or reject. |[cite: 3]
| **CLAUDE.md** | Lesson 3.1 | A plain-text file of standing instructions Claude reads automatically at the start of every session in that folder. |[cite: 3]
| **Slash Command** | Lesson 3.1 | A saved, reusable prompt you trigger with a short `/name` instead of retyping a long instruction. |[cite: 3]

<!-- EXPAND: Full Key Concepts Reference -->[cite: 3]

| Term | Defined In | Plain English Meaning |[cite: 3]
|---|---|---|[cite: 3]
| **Claude Cowork** | Lesson 3.1 | The option built for editing or creating a single Word, Excel, or PowerPoint file, with no terminal needed. |[cite: 3]
| **Plan Mode** | Lesson 3.1 | A setting that limits Claude to reading and thinking until you approve a written plan. Your best guardrail. |[cite: 3]
| **Permission Prompt** | Lesson 3.1 | The ask that appears before Claude writes or edits. Options are allow-once, allow-always, or deny. |[cite: 3]
| **Integrated Terminal** | Lesson 3.1 | The terminal panel built into VS Code, opened with Ctrl and the backtick key. The only terminal you need. |[cite: 3]
| **PowerShell** | Lesson 3.1 | A built-in Windows program for typing instructions. Used once, just for the install. |[cite: 3]
| **PATH** | Lesson 3.1 | The list of places Windows looks for programs. A command must be on it to run from any folder. |[cite: 3]
| **Extension** | Lesson 3.1 | A small add-on for VS Code, like an app for your phone, that adds features such as PDF viewing or spell check. |[cite: 3]
| **Markdown (.md)** | Lesson 3.1 | A simple plain-text formatting style. The recommended format to work in, exporting to Word or PDF at the end. |[cite: 3]
| **Model** | Lesson 3.1 | The specific AI doing the work, such as Sonnet or Opus, shown in the prompt's model indicator. |[cite: 3]
| **Token** | Lesson 3.1 | A unit of text usage that counts against your plan limit. |[cite: 3]
| **Usage Limits** | Lesson 3.1 | Claude Pro's rolling roughly 5-hour session caps plus weekly caps. Web chat and Claude Code share one pool. |[cite: 3]
| **Git for Windows** | Lesson 3.1 | A recommended free install that adds Git Bash, an alternative terminal, to your machine. |[cite: 3]

<!-- /EXPAND -->[cite: 4]

---[cite: 4]

<!-- ANCHOR: anchor-next -->[cite: 4]

## What's Next[cite: 4]

**Next Module:** [Module 4: Building Your AI Personal Assistant](4-agents.md)[cite: 4]

Module 4 covers how to build a Claude Project - a workspace that remembers your standing instructions and draws on your own reference documents, so you stop re-explaining yourself every time you open a new chat.[cite: 4]

**Support Resources:**[cite: 4]

| Resource | Link | Purpose |[cite: 4]
|---|---|---|[cite: 4]
| Claude | claude.ai | Sign up and use Claude in your browser |[cite: 4]
| Claude Docs | code.claude.com/docs | Official documentation |[cite: 4]
| Claude Support | support.claude.com | Help center and account support |[cite: 4]

<!-- CHILDREN -->[cite: 4]