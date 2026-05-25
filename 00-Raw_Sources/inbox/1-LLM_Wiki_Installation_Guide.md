---
title: LLM Wiki CLI-Native Installation and Configuration Guide
date: 2026-05-23
source: LLM Wiki Installation Guide.docx
type: raw-source
tags:
  - second-brain
  - installation
  - claude-code
  - obsidian
  - hyalo
  - qmd
  - setup
status: ingested
---

# LLM Wiki: CLI-Native Installation and Configuration Guide

This document outlines the systematic deployment of an LLM Wiki on macOS. It transitions knowledge management from ephemeral web interfaces to a persistent, CLI-native environment. The architecture isolates the storage layer (Obsidian) from the intelligence layer (Claude Code), utilizing native binaries and Rust-based retrieval engines to guarantee structural integrity and minimize context window degradation.

---

## Phase 1: Core System Dependencies

The architecture relies on specific package managers and compilation toolchains to execute local binaries. Your MacBook Pro requires Homebrew, Node.js, and the Rust toolchain before installing the primary agents.

### 1.1 Homebrew

Homebrew manages macOS system packages and utilities.

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

**Verification:** Execute `brew --version`. The terminal must output the current Homebrew version.

### 1.2 Node.js

Node.js provides the runtime environment for local dependencies and specific CLI tools.

```bash
brew install node
```

**Verification:** Execute `node --version`. The system must return version 18 or higher.

### 1.3 Rust Toolchain

The Rust toolchain compiles and executes the local search engine (QMD) and the structural mutation tool (Hyalo).

```bash
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
```

Follow the on-screen prompts and select the default installation (option 1). Restart your terminal session to load the updated environment variables.

**Verification:** Execute `cargo --version`. The terminal must output the Cargo package manager version.

---

## Phase 2: The Orchestrator (Claude Code)

Claude Code acts as the central autonomous agent. It interprets tasks, synthesizes data, and delegates retrieval and mutation operations to sub-tools.

### 2.1 Installation Methods

Use the native binary installer for macOS. It operates independently, auto-updates, and prevents PATH conflicts.

```bash
curl -fsSL https://claude.ai/install.sh | bash
```

**Alternative (NPM method):** If your system requires strict version pinning:

```bash
npm install -g @anthropic-ai/claude-code
```

**Verification:** Execute `claude --version`. The terminal must return the installed version number.

### 2.2 Authentication

Link the CLI tool to your existing Anthropic account. Navigate to your primary knowledge vault directory:

```bash
cd ~/path/to/your/second-brain
claude
```

The CLI triggers an OAuth flow and opens your default web browser. Log in using the credentials associated with your $20 Claude Pro membership. Authorize the CLI application.

**Verification:** Execute `claude auth status --text`. The system must return an exit code of 0 and confirm active authentication.

---

## Phase 3: The Retrieval Engine (QMD)

Relying on Claude Code to read raw markdown files rapidly degrades the context window. QMD replaces brute-force reading with a local, token-efficient search engine. It executes BM25 keyword matching, vector semantic search, and LLM reranking directly on your machine.

### 3.1 Installation

The `qmd-cli` package requires the cmake build system generator to compile its underlying C++ engine (llama.cpp) during installation.

1. Install CMake via Homebrew:

```bash
brew install cmake
```

2. Verify the CMake installation: `cmake --version`

3. Install the QMD command-line interface via Cargo:

```bash
cargo install qmd-cli
```

*Note: This compilation process may take several minutes.*

### 3.2 Vault Indexing

Map your knowledge vault so QMD can generate local vector embeddings. This prevents the tool from scanning irrelevant macOS directories.

```bash
qmd collection add ~/path/to/your/second-brain --name second-brain
```

**Verification:** Execute `qmd search "Blue Origin" -n 5 --json`. The terminal must return a structured JSON payload containing up to five document references. The JSON output format guarantees that Claude Code parses the data programmatically without consuming excess tokens on visual terminal formatting.

---

## Phase 4: Structural Integrity (Hyalo)

Large language models frequently hallucinate YAML syntax, break Obsidian wikilinks, and misalign metadata brackets. Hyalo acts as a Rust-based, AST-aware (Abstract Syntax Tree) barrier between Claude Code and your raw files. The agent uses Hyalo to execute structural mutations safely.

### 4.1 Installation

```bash
cargo install hyalo-cli
```

**Alternative (Homebrew method):**

```bash
brew tap ractive/tap
brew install ractive/tap/hyalo
```

### 4.2 Agent Integration

Instruct Claude Code to use Hyalo for file modifications instead of raw Unix commands. Navigate to your vault root and execute:

```bash
hyalo init --claude
```

This command generates a `.hyalo.toml` configuration file and installs specific interaction rules inside the `.claude/rules/` directory. These rules prohibit Claude Code from directly mutating YAML frontmatter without using the `hyalo set` command.

**Verification:** Execute `hyalo config`. The system must output the resolved configuration for the active vault directory.

---

## Phase 5: Vault Hygiene via GNU Utilities

Standard macOS BSD utilities lack the specific flags required for advanced topological mapping. Install the GNU versions of `find` and `xargs` to identify orphaned nodes and broken associative trails.

### 5.1 Installation

```bash
brew install findutils
```

Homebrew installs the GNU utilities with a `g` prefix (e.g., `gfind`, `gxargs`) to prevent conflicts with the default macOS BSD tools.

### 5.2 Application

Use `gfind` to rapidly traverse the file system hierarchy. Claude Code uses `gfind` inside background Bash scripts to calculate the asymmetric difference between declared wikilinks and existing file paths.

**Verification:** Execute `gfind . -type f -name "*.md" | wc -l` in your vault root. The terminal must return the exact count of markdown files currently in the directory.

---

## Phase 6: The Visualization Layer (Obsidian & Dataview)

Obsidian acts strictly as the passive IDE. The AI bookkeeper handles data ingestion and connection via the terminal; you use Obsidian solely to visualize the graph, read synthesized notes, and execute manual queries against the metadata.

### 6.1 Dataview Installation

Dataview transforms your Obsidian vault into a queryable database by parsing the YAML frontmatter managed by Hyalo.

1. Open the Obsidian application.
2. Navigate to **Settings > Community Plugins**.
3. Disable "Restricted Mode" to permit third-party plugins.
4. Click **Browse** and search for "Dataview".
5. Click **Install**, then click **Enable**.

### 6.2 Query Execution

With Dataview active, build dynamic tables to monitor your core OKRs. To track L3 Career milestones related to Blue Origin, create a new markdown file and insert:

```dataview
TABLE status, date_modified
FROM "L3_Career/Blue_Origin"
WHERE contains(tags, "milestone")
SORT date_modified DESC
```

Dataview reads the properties injected by Claude Code/Hyalo and renders a real-time table directly within the Obsidian interface.

---

## Phase 7: Visual Studio Code Configuration

VS Code serves as the active workspace for your LLM Wiki setup. It consolidates terminal execution of Claude Code and real-time visualization of your Markdown documents into a unified interface.

### 7.1 Essential Markdown Extensions

First, enable the `code` command in your shell path:

1. Open Visual Studio Code.
2. Press `Cmd + Shift + P` to open the Command Palette.
3. Type `shell command` and select **Shell Command: Install 'code' command in PATH**.
4. Restart your terminal.

Install the extensions:

```bash
code --install-extension yzhang.markdown-all-in-one
code --install-extension davidanson.vscode-markdownlint
code --install-extension shd101wyy.markdown-preview-enhanced
```

- **Markdown All in One** — Automates structural tasks: generates dynamic Table of Contents sections, formats tables, and auto-completes lists.
- **Markdownlint** — Enforces strict syntax rules across your vault. Flags trailing spaces, inconsistent heading levels, and broken list indentations — preventing parsing failures in Obsidian and Hyalo.
- **Markdown Preview Enhanced** — Renders Mermaid diagrams, dynamic Gantt charts, and LaTeX equations directly inside VS Code for complex systems engineering documents like the Serenity scheduling BRD.

### 7.2 Live Preview Configuration

VS Code natively supports synchronized Markdown previewing.

1. Open any Markdown file in your vault.
2. Press `Cmd + K`, release, then press `V`.
3. VS Code opens a rendered preview in a split pane on the right.

The preview pane updates instantly as Claude Code modifies the file via the terminal. Native preview synchronizes scrolling between source text and rendered output. To pin a preview to a specific file, click the "Lock" icon in the preview tab's title bar.

### 7.3 Integrated Terminal Optimization

Create a `.vscode/settings.json` file in your vault root to isolate these settings from other projects:

```bash
mkdir -p .vscode
touch .vscode/settings.json
```

Open the file and insert:

```json
{
  "terminal.integrated.cursorBlinking": true,
  "terminal.integrated.cursorStyle": "line",
  "terminal.integrated.cursorWidth": 2,
  "terminal.integrated.fontSize": 14,
  "terminal.integrated.fontFamily": "'Fira Code', monospace",
  "workbench.panel.defaultLocation": "right"
}
```

- **Terminal Layout** — Setting `"workbench.panel.defaultLocation": "right"` moves the terminal from the bottom to the right sidebar, providing maximum vertical space to read Claude Code's lengthy analytical outputs.
- **Font and Cursor** — Increases terminal font size and sets a blinking line cursor for immediate visual location among dense LLM output. Toggle terminal visibility with `` Ctrl + ` ``.
- **Terminal Multiplexing** — Press `Cmd + \` to split the terminal pane. Use the left pane for the active `claude` session; use the right pane for manual `qmd search` commands or file verification without terminating the primary LLM loop.

---

## Phase 8: Data Parsing and Skill Integration

Claude Code requires explicit tool definitions to parse binary file formats (DOCX, PDF, PPTX, XLSX). Implement these capabilities by configuring Anthropic skill definitions as manual conversion commands.

### 8.1 Core Utilities Installation

```bash
brew install poppler
brew install pandoc
brew install gnumeric
npm install -g mammoth
```

### 8.2 Skill Definition Implementation

Create a global directory to store custom skill rules and helper scripts:

```bash
mkdir -p ~/.claude/skills/scripts/office
```

Download the skill definition files from the Anthropic repository:

```bash
curl -L -o ~/.claude/skills/docx.md https://raw.githubusercontent.com/anthropics/skills/main/skills/docx/SKILL.md
curl -L -o ~/.claude/skills/pdf.md https://raw.githubusercontent.com/anthropics/skills/main/skills/pdf/SKILL.md
curl -L -o ~/.claude/skills/pptx.md https://raw.githubusercontent.com/anthropics/skills/main/skills/pptx/SKILL.md
curl -L -o ~/.claude/skills/xlsx.md https://raw.githubusercontent.com/anthropics/skills/main/skills/xlsx/SKILL.md
curl -L -o ~/.claude/skills/skill-creator.md https://raw.githubusercontent.com/anthropics/skills/main/skills/skill-creator/SKILL.md
```

Download the required Python helper scripts:

```bash
curl -L -o ~/.claude/skills/scripts/office/unpack.py https://raw.githubusercontent.com/anthropics/skills/main/skills/docx/scripts/office/unpack.py
curl -L -o ~/.claude/skills/scripts/recalc.py https://raw.githubusercontent.com/anthropics/skills/main/skills/xlsx/scripts/recalc.py
```

### 8.3 Configuration Binding

Bind the downloaded skills to Claude Code's global configuration:

```bash
claude config add -g custom_instructions "Load tool definitions from ~/.claude/skills/. Use these skills to process .docx, .pdf, .pptx, and .xlsx files."
```

### 8.4 The Two-Step Conversion Workflow

Manage binary files through a strict two-step procedure. This isolates extraction from knowledge ingestion, preventing context window saturation.

**Step 1: Manual Conversion Command**

Place the raw binary file (e.g., `Serenity_Schedule.pdf`) into your vault's `inbox/` directory. Instruct Claude Code to extract the text:

```bash
claude -p "Use the pdf skill to extract text from inbox/Serenity_Schedule.pdf. Save the exact output as inbox/Serenity_Schedule_Parsed.md."
```

Apply the identical syntax for DOCX, PPTX, or XLSX files by substituting the target file name and corresponding skill.

**Step 2: Wiki Ingestion Command**

After verifying the generated markdown file, integrate the knowledge into the wiki:

```bash
claude -p "Ingest inbox/Serenity_Schedule_Parsed.md. Update the index, map new concepts, modify related L3_Career pages, and log the action using Hyalo."
```

### 8.5 The Skill-Creator Command

The skill-creator capability generates parsers for unsupported file types:

```bash
claude -p "Use the skill-creator skill to write a new parsing tool for .csv files. Save the output to ~/.claude/skills/csv.md."
```

---

## Final System Validation

To validate the complete architecture, execute the following workflow:

1. Place a raw PDF document in your vault's `inbox/` directory.
2. Execute the manual conversion command using the PDF skill.
3. Verify the generated markdown file in VS Code.
4. Execute the wiki ingestion command.

Claude Code parses the instruction, reads the markdown data, queries QMD via JSON, modifies the relevant YAML properties using Hyalo, and outputs the result. The AI bookkeeper is now fully operational.

---

## Appendix A: System Architecture Analysis — Skills vs. Slash Commands

This section analyzes the technical differences between Claude Code custom Slash Commands and Anthropic Tool Skills, and justifies the architectural decision to use Skills for binary file parsing.

### 1. Architectural Definitions

- **Slash Commands (`~/.claude/commands/name.md`)** — Operate as prompt injection macros. When you execute `/goal Serenity Scheduling April update`, the CLI reads the local markdown file, concatenates its contents with your `$ARGUMENTS`, and injects the entire block as a text prefix into the user prompt before sending the payload to the Anthropic API.

- **Anthropic Skills (`~/.claude/skills/name.md`)** — Do not operate as text prefixes. When you bind a skill via `claude config add -g custom_instructions`, you inject the capability into the agent's persistent system instructions — defining an operational schema that teaches the agent how to use its native Bash tool to manipulate external software (like `poppler` or `mammoth`).

### 2. Justification: Why Skills Excel at File Parsing

Parsing binary files requires dynamic execution, not static text expansion. Skills provide three distinct advantages over Slash Commands for data ingestion.

#### 2.1 Dynamic Error Handling and AST Correction

A Slash Command executes a rigid pipeline. If a `/pdf` command instructs the agent to run `pdftotext $ARGUMENTS` and the PDF lacks a text layer or contains encrypted segments, the Bash utility outputs an error code and the pipeline terminates — leaving a blank or corrupted markdown file in your vault.

Skills provide autonomous error handling. Because a Skill defines an operational capability rather than a static macro, the agent reads the `stderr` output from the terminal. If `mammoth` fails to parse a `.docx` file due to formatting corruption, the agent recognizes the failure, analyzes the error log, and can dynamically pivot — attempting a fallback extraction method or alerting you to corrupted AST nodes before contaminating your Obsidian vault.

#### 2.2 Autonomous Tool Chaining

Slash Commands require explicit human invocation and execute sequentially based on your precise keystrokes.

Skills enable autonomous tool chaining. When you load the PDF and DOCX skills into the system prompt, Claude Code maps them to its available toolset. If you issue a broad prompt such as "Analyze the `inbox/` directory and extract all constraints related to the Serenity BRD," the agent autonomously detects the `.pdf` and `.docx` files, invokes the PDF skill, processes the output, invokes the DOCX skill, and synthesizes the data — without requiring you to manually execute `/pdf` and `/docx` individually.

#### 2.3 Context Window Optimization

Slash Commands inject their entire template into the active prompt. Complex formatting instructions for parsing tables, LaTeX equations, and dynamic Gantt visualizations inject hundreds of tokens into the user space on every execution.

Skills reside in the system instruction layer. The Anthropic API optimizes system instructions for token caching. By keeping parser definitions in `~/.claude/skills/` and referencing them via the global configuration, you isolate the heavy tool-definition tokens from your active conversational context — preserving your context window for analyzing the actual Serenity scheduling data.

### 3. Optimal Use Case Allocation

The architecture requires both tools applied to their correct domains.

**Use Slash Commands for Output Standardization:**
The `/goal` command is the optimal use case. When reporting the Serenity Scheduling April state to stakeholders, you require strict adherence to a specific format (e.g., verifying the `[GS 4/25]` tag, mandating the "YELLOW" status signal, structuring the causal chain regarding the NG Refurb and GS2 Integration). Slash Commands force the LLM to adhere to these structural constraints instantly.

**Use Skills for Input Processing:**
Parsing raw external data introduces unpredictable variables. Skills grant the agent the flexibility to navigate extraction errors, run complex Unix binaries, and sanitize data before it enters your persistent LLM Wiki.
