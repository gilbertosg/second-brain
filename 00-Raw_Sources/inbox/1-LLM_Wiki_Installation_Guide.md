# **LLM Wiki: CLI-Native Installation and Configuration Guide**

This document outlines the systematic deployment of an LLM Wiki on macOS. It transitions knowledge management from ephemeral web interfaces to a persistent, CLI-native environment. The architecture isolates the storage layer (Obsidian) from the intelligence layer (Claude Code), utilizing native binaries and Rust-based retrieval engines to guarantee structural integrity and minimize context window degradation.

## **Phase 1: Core System Dependencies**

The architecture relies on specific package managers and compilation toolchains to execute local binaries. Your MacBook Pro requires Homebrew, Node.js, and the Rust toolchain before installing the primary agents.

### **1.1 Homebrew**

Homebrew manages macOS system packages and utilities.

Execute the following command in your terminal:

/bin/bash \-c "$(curl \-fsSL \[https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh\](https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh))"

**Verification:** Execute brew \--version. The terminal must output the current Homebrew version.

### **1.2 Node.js**

Node.js provides the runtime environment for local dependencies and specific CLI tools.

Execute the following command:

brew install node

**Verification:** Execute node \--version. The system must return version 18 or higher.

### **1.3 Rust Toolchain**

The Rust toolchain compiles and executes the local search engine (QMD) and the structural mutation tool (Hyalo).

Execute the official installer script:

curl \--proto '=https' \--tlsv1.2 \-sSf \[https://sh.rustup.rs\](https://sh.rustup.rs) | sh

Follow the on-screen prompts and select the default installation (option 1). Restart your terminal session to load the updated environment variables.

**Verification:** Execute cargo \--version. The terminal must output the Cargo package manager version.

## **Phase 2: The Orchestrator (Claude Code)**

Claude Code acts as the central autonomous agent. It interprets tasks, synthesizes data, and delegates retrieval and mutation operations to sub-tools.

### **2.1 Installation Methods**

Use the native binary installer for macOS. It operates independently, auto-updates, and prevents PATH conflicts.

Execute the native installer:

curl \-fsSL \[https://claude.ai/install.sh\](https://claude.ai/install.sh) | bash

*Alternative (NPM method):* If your system requires strict version pinning, execute the NPM command:

npm install \-g @anthropic-ai/claude-code

**Verification:** Execute claude \--version. The terminal must return the installed version number.

### **2.2 Authentication**

You must link the CLI tool to your existing Anthropic account.

Navigate to your primary knowledge vault directory:

cd \~/path/to/your/second-brain  
claude

The CLI triggers an OAuth flow and opens your default web browser. Log in using the credentials associated with your $20 Claude Pro membership. Authorize the CLI application.

**Verification:** Execute claude auth status \--text. The system must return an exit code of 0 and confirm active authentication.

## **Phase 3: The Retrieval Engine (QMD)**

Relying on Claude Code to read raw markdown files rapidly degrades the context window. QMD replaces brute-force reading with a local, token-efficient search engine. It executes BM25 keyword matching, vector semantic search, and LLM reranking directly on your machine.

### **3.1 Installation**

The qmd-cli package requires the cmake build system generator to compile its underlying C++ engine (llama.cpp) during installation.

1. Install CMake via Homebrew. Execute the following command:

brew install cmake

2. Verify the CMake installation. Execute cmake \--version.  
3. Install the QMD command-line interface via Cargo. Execute the following command:

cargo install qmd-cli

*Note: This compilation process may take several minutes.*

### **3.2 Vault Indexing**

You must explicitly map your knowledge vault so QMD can generate local vector embeddings. This prevents the tool from scanning irrelevant macOS directories.

Execute the initialization command, replacing the path with your specific Obsidian vault location:

qmd collection add \~/path/to/your/second-brain \--name second-brain

**Verification:** Execute qmd search "Blue Origin" \-n 5 \--json. The terminal must return a structured JSON payload containing up to five document references containing that exact string. The JSON output format guarantees that Claude Code parses the data programmatically without consuming excess tokens on visual terminal formatting.

## **Phase 4: Structural Integrity (Hyalo)**

Large language models frequently hallucinate YAML syntax, break Obsidian wikilinks, and misalign metadata brackets. Hyalo acts as a Rust-based, AST-aware (Abstract Syntax Tree) barrier between Claude Code and your raw files. The agent utilizes Hyalo to execute structural mutations safely.

### **4.1 Installation**

Install Hyalo via Cargo:

cargo install hyalo-cli

*Alternative (Homebrew method):*

brew tap ractive/tap  
brew install ractive/tap/hyalo

### **4.2 Agent Integration**

You must instruct Claude Code to use Hyalo for file modifications instead of raw Unix commands. Navigate to your vault root and execute the initialization command:

hyalo init \--claude

This command generates a .hyalo.toml configuration file and installs specific interaction rules inside the .claude/rules/ directory. These rules strictly prohibit Claude Code from directly mutating YAML frontmatter without utilizing the hyalo set command.

**Verification:** Execute hyalo config. The system must output the resolved configuration for the active vault directory.

## **Phase 5: Vault Hygiene via GNU Utilities**

Standard macOS BSD utilities lack the specific flags required for advanced topological mapping. You must install the GNU versions of find and xargs to identify orphaned nodes and broken associative trails.

### **5.1 Installation**

Install the GNU findutils package via Homebrew:

brew install findutils

Homebrew installs the GNU utilities with a g prefix (e.g., gfind, gxargs) to prevent conflicts with the default macOS BSD tools.

### **5.2 Application**

You use gfind to rapidly traverse the file system hierarchy. Claude Code utilizes gfind inside background Bash scripts to calculate the asymmetric difference between declared wikilinks and existing file paths.

**Verification:** Execute gfind . \-type f \-name "\*.md" | wc \-l in your vault root. The terminal must return the exact mathematical count of markdown files currently existing in the directory.

## **Phase 6: The Visualization Layer (Obsidian & Dataview)**

Obsidian acts strictly as the passive integrated development environment (IDE). The AI bookkeeper handles data ingestion and connection via the terminal; you use Obsidian solely to visualize the graph, read the synthesized notes, and execute manual queries against the metadata.

### **6.1 Dataview Installation**

Dataview transforms your Obsidian vault into a queryable database by parsing the YAML frontmatter managed by Hyalo.

1. Open the Obsidian application.  
2. Navigate to **Settings \> Community Plugins**.  
3. Disable "Restricted Mode" to permit third-party plugins.  
4. Click **Browse** and search for "Dataview".  
5. Click **Install**, then click **Enable**.

### **6.2 Query Execution**

With Dataview active, you build dynamic tables to monitor your core OKRs. For example, to track L3 Career milestones related to Blue Origin, create a new markdown file and insert the following code block:

\`\`\`dataview  
TABLE status, date\_modified  
FROM "L3\_Career/Blue\_Origin"  
WHERE contains(tags, "milestone")  
SORT date\_modified DESC  
\`\`\`

Dataview reads the properties injected by Claude Code/Hyalo and renders a real-time table of your career milestones directly within the Obsidian interface.

## **Phase 7: Visual Studio Code Configuration**

Visual Studio Code (VS Code) serves as the active workspace for your LLM Wiki setup. It consolidates the terminal execution of Claude Code and the real-time visualization of your Markdown documents into a unified interface. Configure the editor extensions and integrated terminal behavior to optimize readability and standardize formatting.

### **7.1 Essential Markdown Extensions**

Install the following extensions to automate formatting, enforce syntax rules, and render complex diagrams.

To install these extensions via the terminal, you must first enable the code command in your shell path.

1. Open Visual Studio Code.  
2. Press Cmd \+ Shift \+ P to open the Command Palette.  
3. Type shell command and select **Shell Command: Install 'code' command in PATH**.  
4. Restart your terminal.

Execute these commands in your macOS terminal to install the extensions directly:

code \--install-extension yzhang.markdown-all-in-one  
code \--install-extension davidanson.vscode-markdownlint  
code \--install-extension shd101wyy.markdown-preview-enhanced

**Markdown All in One:** This extension automates structural tasks. It generates dynamic Table of Contents sections, formats tables, and auto-completes lists. When Claude Code outputs raw lists, you use this extension to reformat the syntax using standard keyboard shortcuts.

**Markdownlint:** Large language models frequently output inconsistent Markdown syntax. Markdownlint enforces a strict set of rules across your vault. It flags trailing spaces, inconsistent heading levels, and broken list indentations. Fixing these syntax errors prevents parsing failures in Obsidian and Hyalo.

**Markdown Preview Enhanced:** For complex systems engineering documents, such as the Serenity scheduling BRD, the native preview lacks support for advanced diagramming. This extension renders Mermaid diagrams, dynamic Gantt charts, and complex LaTeX equations directly inside VS Code. It parses the dense technical constraints mapped by Claude Code and provides visual verification before you review the final graph in Obsidian.

### **7.2 Live Preview Configuration**

VS Code natively supports synchronized Markdown previewing.

1. Open any Markdown file in your vault.  
2. Press Cmd \+ K, release the keys, and press V.  
3. VS Code opens a rendered preview in a split pane on the right side of the screen.

As you type or as Claude Code modifies the file via the terminal, the preview pane updates instantly. The native preview synchronizes scrolling; scrolling the source text automatically scrolls the rendered preview to the identical position. To pin a preview to a specific file, click the "Lock" icon in the preview tab's title bar. This allows you navigate other files in the left pane while maintaining the visual reference on the right.

### **7.3 Integrated Terminal Optimization**

The integrated terminal acts as the primary interface for the AI bookkeeper. You execute Claude Code, QMD searches, and Hyalo commands from this panel. Configure the terminal for maximum readability during extended agent sessions.

Create a .vscode/settings.json file in your root vault directory to isolate these settings from your other software engineering projects. You must create the hidden directory before creating the file. Execute the following commands:

mkdir \-p .vscode  
touch .vscode/settings.json

Open the newly created file in VS Code and insert the following configuration block:

{  
  "terminal.integrated.cursorBlinking": true,  
  "terminal.integrated.cursorStyle": "line",  
  "terminal.integrated.cursorWidth": 2,  
  "terminal.integrated.fontSize": 14,  
  "terminal.integrated.fontFamily": "'Fira Code', monospace",  
  "workbench.panel.defaultLocation": "right"  
}

**Terminal Layout:** Setting "workbench.panel.defaultLocation": "right" moves the terminal from the bottom of the screen to the right sidebar. This vertical orientation matches the standard output format of CLI tools. It provides maximum vertical space to read Claude Code's lengthy analytical outputs without collapsing your Markdown editor view.

**Font and Cursor:** The configuration increases the terminal font size and sets a distinct, blinking line cursor. This visual distinction helps you immediately locate the active command prompt among dense blocks of synthesized text output by the LLM. Toggle the terminal visibility instantly using the \`Ctrl \+ \`\` shortcut.

**Terminal Multiplexing:** Managing a persistent AI bookkeeper requires executing simultaneous CLI processes. VS Code allows you to split the terminal pane. Press Cmd \+ \\ while focus is inside the terminal. Use the left pane to run the active claude agent session. Use the right pane to manually execute qmd search commands or verify file counts using GNU utilities without terminating the primary LLM loop. This eliminates context switching and streamlines the debugging process.

## **Phase 8: Data Parsing and Skill Integration**

Claude Code requires explicit tool definitions to parse binary file formats (DOCX, PDF, PPTX, XLSX). You implement these capabilities by downloading Anthropic skill definitions and configuring them as manual conversion commands.

### **8.1 Core Utilities Installation**

Install the underlying CLI binaries required to execute the file conversions. Execute the following commands in your terminal:

brew install poppler  
brew install pandoc  
brew install gnumeric  
npm install \-g mammoth

### **8.2 Skill Definition Implementation**

Create a global directory in your user home folder to store the custom skill rules and their associated helper scripts. This ensures the parsers operate across all your Claude Code projects globally, not just within the Obsidian vault.

mkdir \-p \~/.claude/skills/scripts/office

Download the specific SKILL.md files from the Anthropic repository into this global directory. Execute these commands:

curl \-L \-o \~/.claude/skills/docx.md \[https://raw.githubusercontent.com/anthropics/skills/main/skills/docx/SKILL.md\](https://raw.githubusercontent.com/anthropics/skills/main/skills/docx/SKILL.md)  
curl \-L \-o \~/.claude/skills/pdf.md \[https://raw.githubusercontent.com/anthropics/skills/main/skills/pdf/SKILL.md\](https://raw.githubusercontent.com/anthropics/skills/main/skills/pdf/SKILL.md)  
curl \-L \-o \~/.claude/skills/pptx.md \[https://raw.githubusercontent.com/anthropics/skills/main/skills/pptx/SKILL.md\](https://raw.githubusercontent.com/anthropics/skills/main/skills/pptx/SKILL.md)  
curl \-L \-o \~/.claude/skills/xlsx.md \[https://raw.githubusercontent.com/anthropics/skills/main/skills/xlsx/SKILL.md\](https://raw.githubusercontent.com/anthropics/skills/main/skills/xlsx/SKILL.md)  
curl \-L \-o \~/.claude/skills/skill-creator.md \[https://raw.githubusercontent.com/anthropics/skills/main/skills/skill-creator/SKILL.md\](https://raw.githubusercontent.com/anthropics/skills/main/skills/skill-creator/SKILL.md)

Download the required Python helper scripts. The DOCX and XLSX skills rely on these local scripts to properly unpack and recalculate the binary files before extraction. Execute these commands:

curl \-L \-o \~/.claude/skills/scripts/office/unpack.py https://raw.githubusercontent.com/anthropics/skills/main/skills/docx/scripts/office/unpack.py  
curl \-L \-o \~/.claude/skills/scripts/recalc.py https://raw.githubusercontent.com/anthropics/skills/main/skills/xlsx/scripts/recalc.py

### **8.3 Configuration Binding**

Bind the downloaded skills to Claude Code's global configuration. Execute the following command to force the agent to load these rules on startup across all directories:

claude config add \-g custom\_instructions "Load tool definitions from \~/.claude/skills/. Use these skills to process .docx, .pdf, .pptx, and .xlsx files."

### **8.4 The Two-Step Conversion Workflow**

You manage binary files through a strict two-step procedure. This isolates the extraction process from the knowledge ingestion process, preventing context window saturation.

**Step 1: Manual Conversion Command**

Place the raw binary file (e.g., Serenity\_Schedule.pdf) into your vault's inbox/ directory. Instruct Claude Code to execute the specific skill to extract the text and generate a markdown file. You execute the tool as a single prompt command using the \-p flag:

claude \-p "Use the pdf skill to extract text from inbox/Serenity\_Schedule.pdf. Save the exact output as inbox/Serenity\_Schedule\_Parsed.md."

Apply the identical syntax for DOCX, PPTX, or XLSX files by substituting the target file name and corresponding skill.

**Step 2: Wiki Ingestion Command**

After verifying the generated markdown file, instruct Claude Code to integrate the knowledge into the wiki. Execute this command:

claude \-p "Ingest inbox/Serenity\_Schedule\_Parsed.md. Update the index, map new concepts, modify related L3\_Career pages, and log the action using Hyalo."

### **8.5 The Skill-Creator Command**

The skill-creator capability allows you to generate parsers for unsupported file types. If you encounter a new format, execute this command to build the requisite skill:

claude \-p "Use the skill-creator skill to write a new parsing tool for .csv files. Save the output to \~/.claude/skills/csv.md."

## **Final System Validation**

To validate the complete architecture, execute the following workflow:

1. Place a raw PDF document in your vault's inbox/ directory.  
2. Execute the manual conversion command using the PDF skill.  
3. Verify the generated markdown file in VS Code.  
4. Execute the wiki ingestion command.

Claude Code parses the instruction, reads the markdown data, queries QMD via JSON, modifies the relevant YAML properties using Hyalo, and outputs the result. The AI bookkeeper is now fully operational.

## **Appendix A: System Architecture Analysis: Skills vs. Slash Commands**

This section analyzes the technical differences between Claude Code custom Slash Commands and Anthropic Tool Skills. It justifies the architectural decision to utilize Skills for binary file parsing within the LLM Wiki environment.

### **1\. Architectural Definitions**

A Slash Command operates as a prompt injection macro.

* **Slash Commands (\~/.claude/commands/name.md):** When you execute a command like /goal Serenity Scheduling April update, the CLI intercepts the command. It reads the local markdown file, concatenates its contents with your $ARGUMENTS, and injects the entire block as a text prefix into the user prompt before sending the payload to the Anthropic API.  
* **Anthropic Skills (\~/.claude/skills/name.md):** Skills do not operate as text prefixes. When you bind a skill via claude config add \-g custom\_instructions, you inject the capability into the agent's persistent system instructions. You define a specific operational schema that teaches the agent how to utilize its native Bash tool to manipulate external software (like poppler or mammoth).

### **2\. Justification: Why Skills Excel at File Parsing**

Parsing binary files (PDFs, DOCXs) requires dynamic execution, not static text expansion. Relying on Skills provides three distinct technical advantages over Slash Commands for data ingestion.

#### **2.1 Dynamic Error Handling and AST Correction**

A Slash Command executes a rigid pipeline. If you create a /pdf command that instructs the agent to run pdftotext $ARGUMENTS, the agent executes the instruction blindly. If the PDF lacks a text layer or contains encrypted segments, the Bash utility outputs an error code. The Slash Command pipeline terminates, leaving you with a blank or corrupted markdown file in your vault.

Skills provide autonomous error handling. Because the Skill defines an operational capability rather than a static macro, the agent reads the standard error (stderr) output from the terminal. If mammoth fails to parse a .docx file due to formatting corruption, the agent recognizes the failure, analyzes the error log, and can dynamically pivot—perhaps attempting a fallback extraction method or explicitly alerting you to the corrupted AST (Abstract Syntax Tree) nodes before contaminating your Obsidian vault.

#### **2.2 Autonomous Tool Chaining**

Slash Commands require explicit human invocation. They execute sequentially based on your precise keystrokes.

Skills enable autonomous tool chaining. When you load the PDF and DOCX skills into the system prompt, Claude Code maps them to its available toolset. If you issue a broad prompt such as, "Analyze the inbox/ directory and extract all constraints related to the Serenity BRD," the agent autonomously detects the .pdf and .docx files. It invokes the PDF skill, processes the output, immediately invokes the DOCX skill, processes the output, and synthesizes the data. A Slash Command requires you to manually execute /pdf and /docx individually.

#### **2.3 Context Window Optimization**

Slash Commands inject their entire template into the active prompt. If you create complex formatting instructions for parsing tables, LaTeX equations, and dynamic Gantt visualizations from binary files, the /pdf command injects hundreds of tokens into the user space on every execution.

Skills reside in the system instruction layer. The Anthropic API optimizes system instructions for token caching. By keeping the parser definitions in the \~/.claude/skills/ directory and referencing them via the global configuration, you isolate the heavy tool-definition tokens from your active conversational context, preserving your context window for analyzing the actual Serenity scheduling data.

### **3\. Optimal Use Case Allocation**

The architecture requires both tools applied to their correct domains.

**Use Slash Commands for Output Standardization:**

The implementation of the /goal command is the optimal use case for this technology. When reporting the Serenity Scheduling April state to stakeholders, you require strict adherence to a specific format (e.g., verifying the \[GS 4/25\] tag, mandating the "YELLOW" status signal, and structuring the causal chain regarding the NG Refurb and GS2 Integration). Slash Commands force the LLM to adhere to these structural constraints instantly.

**Use Skills for Input Processing:**

Parsing raw external data introduces unpredictable variables. Rely on Anthropic Skills to handle these variables. The Skills grant the agent the flexibility to navigate extraction errors, run complex Unix binaries, and sanitize the data before it enters your persistent LLM Wiki.