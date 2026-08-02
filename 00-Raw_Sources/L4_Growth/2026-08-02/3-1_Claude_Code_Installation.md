# Claude Code Onboarding Guide
### For Marketing, HR, Legal, and Industrial Engineering Professionals — Windows + VS Code + Claude Pro

---

## Section 0: Before We Start

**What Claude Code is:** an AI assistant that works directly on the files and folders on your computer. You ask in plain English; it reads, drafts, edits, and organizes real documents.

**What VS Code is:** the window it all happens in. Think Microsoft Word, but built to open a whole *folder* of files at once instead of one document.

**The relationship:** VS Code is the office; Claude Code is the assistant sitting in it.

> 🔒 **Confidentiality — read this first**
> Claude Pro is a *personal* subscription with no corporate data agreement, admin oversight, audit logs, or retention controls. Practice on non-sensitive material. Before running real client files, employee records, or privileged material through it, check with your employer's IT/Legal — they may require Claude Team/Enterprise instead of a personal Pro plan.

**Cost:** Claude Pro, ~$20/mo (~$17/mo billed annually). The free tier does **not** include Claude Code. Subscribe *before* your session.

**Time required:** ~75–90 minutes.

**What success looks like:** by the end, you'll have pointed Claude at a folder of documents and had it produce a real, saved summary file — without copying or pasting anything.

**Reassurance:** you cannot break your computer doing this. Claude asks permission before it changes anything, and shows you exactly what it plans to change.

> 💬 **In Plain English:** This guide teaches you to point an AI assistant at a folder of real files on your computer and have it do useful work in that folder — safely, and only with your permission at every step.

### Prerequisites Checklist
- [ ] Windows 10 (build 1809+) or Windows 11
- [ ] 4 GB+ RAM
- [ ] Claude Pro plan active (claude.ai)
- [ ] Claude login credentials handy
- [ ] Ability to install software on the machine
- [ ] A folder of **non-confidential** practice documents

---

## Section 1: Web vs. Claude Code — Which Do I Use?

### 1.0 Quick Decision Guide (Start Here)

Answer one question: **Do you need to work with files and folders, or just ask a question?**

| If you... | Use this |
|---|---|
| Have a quick question, no files involved | **claude.ai (web)** |
| Need to edit or create ONE Word/Excel/PowerPoint file | **Claude Cowork** |
| Need to work across MANY files, or repeat the same task over and over | **Claude Code** (this guide) |

> 💬 **In Plain English:** Web is for talking. Cowork is for one document. Claude Code is for a whole folder of documents at once. This guide is about the third one.

> 📋 **Is this the right tool for you?**
>
> | Tool | Best for |
> |---|---|
> | claude.ai (web) | Quick one-off questions, no files involved |
> | Claude Cowork | Single-document Office work, no terminal needed |
> | **Claude Code** | Whole folders, bulk work, repeatable processes |

> **The core difference in one sentence:**
> The web version is a conversation *about* your documents.
> Claude Code works *on* your documents.

### 1.1 The Nine Concrete Advantages

1. **Whole folders, not one upload at a time** — point it at a folder of 40 contracts or 200 résumés, instead of uploading files one by one.
2. **Output lands as real, saved files** — no copy-paste from a chat window into Word.
3. **Bulk / repetitive work becomes one instruction** — e.g., "extract the termination date from each of these 60 agreements into one table."
4. **It remembers your project** — a `CLAUDE.md` file (a plain text file that holds your standing instructions) holds your house style, tone, or defined terms across every session.
5. **You see exactly what changed** — every edit is a before/after "diff" (a side-by-side comparison view) you approve or reject. For Legal, this is redline-style review of the AI's own work.
6. **Repeatable, saved workflows** — turn a recurring task into a reusable process.
7. **Multi-step work in one pass** — read, compare, flag, and summarize in one request.
8. **Files stay scoped to what you open** — you control exactly what it can see.
9. **Works with your existing folder structure** — no parallel filing system.

> 💬 **In Plain English:** Claude Code saves you from doing the same copy-paste task 40 times. You describe the job once; it touches every file for you and shows you the results before anything is final.

### 1.2 Before / After — Marketing

| Task | Web version | Claude Code |
|---|---|---|
| Repurpose one blog post into 8 channel variants | 8 separate prompts, 8 copy-pastes | One instruction → 8 saved files |
| Enforce brand voice across a campaign | Re-paste the style guide every chat | `CLAUDE.md` holds it permanently |
| Audit 50 pieces of copy for consistency | Impractical | One pass over the folder |
| Build a competitor comparison from 12 PDFs | Upload limits, no persistence | Point at the folder, get one table |

### 1.3 Before / After — Human Resources

| Task | Web version | Claude Code |
|---|---|---|
| Summarize 40 résumés against a job description | 40 uploads, no consolidated output | One folder → one ranked summary file |
| Standardize 15 job descriptions to one template | 15 chats, manual reassembly | Batch rewrite, each saved back |
| Extract dates/terms from offer letters | Manual, error-prone | One structured table |
| Propagate a policy change across related docs | Manual tracking | Multi-file edit with diffs to approve |

### 1.4 Before / After — Legal

| Task | Web version | Claude Code |
|---|---|---|
| Compare clause language across 30 agreements | Upload-limited, loses thread | One pass, one comparison table |
| Maintain a defined-terms glossary across a deal | Re-explain every session | Persistent in `CLAUDE.md` |
| First-pass risk review of a document set | One doc at a time | Whole folder, flagged findings file |
| Iterate a draft with full change visibility | Copy-paste, no history | Diff review on every edit |

### 1.5 Before / After — Industrial Engineering

| Task | Web version | Claude Code |
|---|---|---|
| Extract cycle-time and downtime data from 20 shift reports | 20 uploads, no consolidated output | One folder → one table |
| Compare SOP language across multiple work-cell documents | Upload-limited, loses thread | One pass, one comparison table |
| Standardize root-cause write-ups (5-Why / fishbone) to one template | Manual reassembly | Batch rewrite, each saved back |
| Audit a folder of maintenance logs for recurring failure codes | Impractical | One pass over the folder |

### 1.6 When the Web Version Is Actually Better
- Quick one-off questions with no files involved
- Working from your phone
- Brainstorming out loud
- Image or screenshot analysis
- You don't want to open a terminal today

> **Honest framing:** Web for thinking. Claude Code for producing. Most people use both.

### 1.7 What It Costs You
A ~30-minute learning curve (mostly one-time), being on a computer rather than a phone, and typing a few commands. That's the whole price.

---

## Section 2: Installation

> 💬 **In Plain English:** You're installing two free programs (VS Code and Claude Code) and connecting them to your paid Claude Pro account. Every step below has a "checkpoint" so you know you're on track.

### 2.1 Get Claude Pro
1. Go to claude.ai → create account → **Settings → Upgrade to Pro** (~$20/mo)
2. ✅ Checkpoint: "Pro" is visible on your account

### 2.2 Install Visual Studio Code
> 🗣️ **Plain English — what is VS Code?** A free program from Microsoft for viewing and editing files. Think of it as a more powerful File Explorer window that Claude Code lives inside.

1. Download from **code.visualstudio.com** (official site only)
2. Choose **User Installer, 64-bit** (no admin rights required)
3. On the checkbox screen: keep **"Add to PATH"** checked; check **"Open with Code"** context menu options
4. First launch: dismiss the welcome tour. Orient yourself to:
- **Explorer** (left) — your files
- **Editor** (center) — where documents open
- **Terminal panel** (bottom) — where you type commands (more on this in Section 4)
- **Status bar** (very bottom)
5. ✅ Checkpoint: VS Code opens cleanly

### 2.3 Install Git for Windows (Recommended)
1. Download from **git-scm.com/downloads/win**
2. Accept every default in the installer
3. ✅ Checkpoint: "Git Bash" appears in the Start menu

### 2.4 Install Claude Code
> 🗣️ **Plain English — what is PowerShell?** A built-in Windows program where you type instructions instead of clicking icons. You'll use it once, just for this install.

1. Open **Windows PowerShell** (Start menu → type "PowerShell"). No admin rights needed.
2. Run:
```powershell
irm https://claude.ai/install.ps1 | iex
```
3. Scrolling text and a download progress bar are normal — this means it's working, not stuck.
4. ⚠️ Close PowerShell and open a brand-new window once it finishes — settings only apply to terminals opened afterward.

### 2.5 First Run & Login
1. Type `claude`, press Enter
2. Choose Claude.ai account login (not "API key")
3. A browser opens → log in → approve → return to the terminal
4. ✅ Checkpoint: you're at the Claude Code prompt, no login nag

### 2.6 Verify Everything Works
```powershell
claude --version
claude doctor
claude
```
Type `hello`. If Claude replies, setup is complete.

### 2.7 Troubleshooting

| Symptom | Fix |
|---|---|
| `claude` not recognized | Close and reopen the terminal first. Still broken → add `%USERPROFILE%\.local\bin` to PATH |
| Stuck at login / plan error | Pro isn't active — check Settings on claude.ai |
| Defender/SmartScreen warning | Expected for a PowerShell installer; only ever run this for the official claude.ai URL |
| Anything else | Run `claude doctor` first, then see code.claude.com/docs/en/troubleshoot-install |

---

## Section 3: Recommended VS Code Extensions

> 💬 **In Plain English:** Extensions are small add-ons, like apps for your phone. The ones below make VS Code friendlier for document work. You do not need all of them — Tier 1 is enough to get started.

### 3.1 How to Install an Extension
Press Ctrl+Shift+X → search by name → click Install → Reload if prompted.

### 3.2 Tier 1 — Install These

| Extension | Publisher | Why you need it |
|---|---|---|
| Claude Code | Anthropic | Graphical chat panel inside VS Code — friendlier than the terminal |
| Markdown All in One | Yu Zhang | Live preview, auto table-of-contents, easy formatting |
| Code Spell Checker | Street Side Software | Catches typos in copy, policies, and drafts as you type |
| Rainbow CSV | mechatroner | Makes spreadsheet exports (.csv) readable in columns |
| vscode-pdf | tomoki1207 | View PDFs inside VS Code |

### 3.3 Tier 2 — Add If Useful

| Extension | Best for | Why |
|---|---|---|
| Excel Viewer / Data Preview | HR, Marketing | Grid view for .xlsx/.csv |
| Markdown PDF | All | Export Claude's markdown output to polished PDF/HTML |
| Speech (ms-vscode.vscode-speech) | Anyone | Dictate prompts instead of typing; runs locally |
| Draw.io Integration | Marketing | Diagrams, funnels, org charts |
| Todo Tree | HR, Legal | Surfaces open items across a folder |
| Live Share | Teams | Real-time collaborative sessions |
| Word Count | Marketing, Legal | Live word/character counts |

### 3.4 Extensions to Skip
Skip: GitLens, Docker, Python, ESLint, Prettier, language servers, Copilot. These are software-developer tools and add nothing for document work.

### 3.5 Two Settings Worth Changing
- Word Wrap on (Alt+Z) — long paragraphs won't scroll sideways
- Theme + font size — Ctrl+Shift+P → "Color Theme"
- Optional: disable the minimap for less visual clutter

---

## Section 4: Terminal Basics

> 💬 **In Plain English:** A "terminal" is a text box where you type instructions instead of clicking. You only need ONE terminal and SIX commands for this whole guide — everything else in this section is optional background.

### 4.1 What a Terminal Is
File Explorer lets you click through folders. A terminal does the same things by typing. You need about six commands total — you are not learning to code.

### 4.2 Just Use This One
For everything in this guide, use the **VS Code Integrated Terminal** — the terminal panel built into VS Code (open it with **Ctrl + `**, the backtick key, top-left of your keyboard). You never need to open a separate terminal program.

### 4.3 Other Terminals (Optional Background — Skip If You're in a Hurry)

| Terminal | What it is | When you'll use it |
|---|---|---|
| Windows PowerShell | Modern Windows default shell | Installation (Section 2.4) only |
| Git Bash | Unix-style shell from Git for Windows | Optional alternative |
| Command Prompt (cmd.exe) | Legacy Windows shell | Avoid |
| Windows Terminal | Microsoft's tabbed terminal app | Optional, nicer host for PowerShell |

### 4.4 The Six Commands
1. `pwd` — where am I?
2. `dir` (PowerShell) / `ls` (Git Bash) — what's in this folder?
3. `cd foldername` — go into a folder
4. `cd ..` — go back up one
5. `cls` / `clear` — tidy the screen
6. `Ctrl + C` — stop whatever's running

### 4.5 Survival Tips
Nothing runs until you press Enter. Up arrow recalls your last command. Tab autocompletes names. Right-click to paste in some terminals. A typo just produces an error message — it doesn't damage anything.

---

## Section 5: Hands-On Tutorial

### 5.1 The One Concept: The Project Folder
Claude can only see and touch files in the folder you open. This is a safety and confidentiality feature — you control exactly what it can access.

Create a sandbox folder: `Documents\claude-practice`, with 3–5 non-confidential sample documents.

> 💬 **In Plain English:** Claude is boxed into the one folder you open. It cannot see your whole computer, your email, or any other folder unless you open that folder too.

### 5.2 Open the Folder
1. File → Open Folder → select claude-practice (or right-click the folder → "Open with Code")
2. Approve the "Trust the authors" prompt
3. Tour the Explorer sidebar
4. Open the terminal (Ctrl + `)

### 5.3 Working With Word, PDF, and Excel Files
- Works natively and beautifully: plain text, Markdown (.md), .csv, .txt
- Works with caveats: PDFs (readable, not directly editable), .docx (readable but formatting is compressed)
- Recommended workflow: work in Markdown, export to Word/PDF at the end
- Tip: ask Claude to convert .docx/PDF content to Markdown as step one of a project

### 5.4 Start Claude Code
Type `claude`, press Enter. Note the prompt box, model indicator (which AI is answering you), and status line. Say hello and get a reply — your first win, about two minutes in.

### 5.5 Exercise 1 — Ask a Question (Read-Only, Zero Risk)
"What documents are in this folder, and what is each one about?"

You type normal sentences, not commands. This is the mental unlock.

### 5.6 Exercise 2 — Have Claude Create a File
"Read all the documents in this folder and create a file called summary.md with a one-paragraph summary of each."

The permission prompt: Claude asks before writing. Options are allow-once, allow-always, or deny. This is the most important safety concept in this guide.

Watch the new file appear in the Explorer sidebar.

### 5.7 Exercise 3 — Have Claude Edit, and Review the Diff
"Add a 'Key Risks' section to summary.md with three bullets."

Review the diff view — a side-by-side before/after — and approve or reject it. For Legal: this is a redline of the AI's proposed changes. Nothing lands without your approval. Claude proposes; you decide.

### 5.8 Exercise 4 — The Bulk Task (The Real Payoff)
"For each document in this folder, pull out the title, date, and main topic, and put them all into one table in index.csv."

Open the result with Rainbow CSV. That was one instruction. On the web version, it would have been one upload and one prompt per document.

> 💬 **In Plain English:** This is the whole point of Claude Code — one sentence did the work of 40 separate uploads.

### 5.9 Plan Mode — Your Best Guardrail
Claude can only read and think — not change anything — until you approve a written plan. Turn it on with Shift+Tab (twice) or /plan. Recommended as your default starting posture for anything touching real work.

### 5.10 CLAUDE.md — Teach Claude Your Standards Once
A plain-text file in the folder that Claude reads automatically every session.

- Marketing: brand voice, banned words, approved product naming, reading level
- HR: required disclaimers, tone guidance, template structure, inclusive-language rules
- Legal: defined terms, citation format, jurisdiction, flags for indemnity/liability language

Try writing a five-line CLAUDE.md and watch the next response change.

### 5.11 Essential Slash Commands

| Command | What it does |
|---|---|
| /help | Everything available |
| /clear | Fresh start (also helps stay under usage limits) |
| /model | See or switch the AI model |
| /plan | Turn on Plan Mode |
| /status | Session info |
| /doctor | Health check |
| /voice | Dictate instead of type |

To exit: /exit, or press Ctrl+C twice.

### 5.12 How to Talk to Claude Effectively
- Name the what and the where — name the file
- One job at a time
- Say what "done" looks like (format, length, audience)
- Use @filename to point at a specific document
- If the result is wrong, just say so in plain English

| Vague | Specific |
|---|---|
| "Make this better" | "Shorten this to 150 words, keep the same call to action" |
| "Check these contracts" | "Flag any indemnity clause that caps liability below $1M" |
| "Fix the résumés" | "Standardize each résumé's date format to MM/YYYY" |
| "Summarize this" | "Summarize in 3 bullets, written for a non-technical VP" |

**Example prompts by role.** These are the kind of one-line requests that show what "specific" looks like in real work:

- **HR:** "Read the résumé spreadsheet in this folder and flag any candidate who's been in 'Interview Scheduled' for more than 10 days."
- **Industrial Engineering:** "Read the shift-report folder and flag any production line with more than 30 minutes of unplanned downtime this week."
- **Legal:** "Compare the indemnity clause across all contracts in this folder and flag any that cap liability below $1M."
- **Marketing:** "Read the campaign performance CSV and tell me which channel had the highest click-through rate."

### 5.13 Usage Limits
Claude Pro has rolling ~5-hour session limits plus weekly caps. Claude Code and claude.ai chat draw from the same usage pool. Use /clear between unrelated tasks, avoid pointing at unnecessarily large folders, and check your usage anytime under Settings → Usage on claude.ai.

### 5.14 Safety, Confidentiality, and Good Habits
✅ Always read the diff before approving
✅ Start in Plan Mode for anything real
✅ Scope tightly — open the specific project folder, never Documents or Desktop root
✅ Keep a backup before any bulk operation

❌ Never paste passwords, API keys, or bank details
❌ Don't run employee PII, salary data, investigation files, or privileged client material through a personal Pro plan without employer approval
❌ Don't approve changes you don't understand — ask Claude to explain instead