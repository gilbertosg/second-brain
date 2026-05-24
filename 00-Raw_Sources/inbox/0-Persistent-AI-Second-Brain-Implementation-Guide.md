---
title: Persistent AI Second Brain Implementation Guide
date: 2026-05-23
source: 0-Persistent_AI_Second_Brain_Implementation_Guide.docx
type: raw-source
tags:
  - second-brain
  - ai-architecture
  - claude-code
  - knowledge-management
  - obsidian
status: ingested
---

# Persistent AI Second Brain Implementation Guide

## Executive Summary: The Karpathy Paradigm

Standard AI chats and RAG (Retrieval-Augmented Generation) systems fail at long-term knowledge management. They rediscover information from scratch for every query. They do not accumulate context.

Andrej Karpathy engineered a structural alternative: the persistent LLM Wiki. Instead of retrieving fragments on demand, the LLM incrementally builds and maintains a structured, interlinked collection of markdown files. The wiki acts as a compounding artifact sitting between you and your raw data.

As a Sr. Technical Program Manager at Blue Origin, you manage complex, high-stakes data. Standard chat windows collapse under this cognitive load and delete the context upon closure. This architecture solves that failure point. It forces the AI to act as a permanent custodian of your second brain.

When you add a new source, the LLM reads it, extracts the data, and integrates it into the existing file structure. It updates entity pages, flags contradictions, and maintains cross-references. You curate the sources and direct the analysis. The LLM executes the administrative maintenance. The result is a knowledge base that compounds permanently with zero maintenance friction.

This document defines the sequence to construct this persistent, self-maintaining personal knowledge base. Standard browser-based AI chats function as short-term memory savants; they collapse complex context windows and delete data upon session closure. This architecture replaces ephemeral interactions with a system that reads, synthesizes, and permanently writes knowledge to a local file structure.

When this system maintains an uninterrupted, mathematically precise associative trail of your behaviors, it transitions from a system of record into a system of prediction. The knowledge compounds over time; the LLM maintains it, and you explore it.

---

## Phase 1: Three-Layer Architecture Setup

The system requires a strict local directory structure representing the three operational layers: Raw Sources (immutable truths), The Wiki (LLM-generated markdown), and The Schema (LLM instructions).

1. Open your terminal.

2. Execute the following commands to build the base architecture on your MacBook Pro:

```bash
mkdir -p ~/Gil-dev/second-brain/{00-Raw_Sources,01-Entities,L1-Health,L2-Relationships,L3-Career,L4-Growth,L5-Finance,L6-Hobbies,L7-Contribute}
mkdir -p ~/Gil-dev/second-brain/{02-Indexes/topic_maps,03-System_Logs}
touch ~/Gil-dev/second-brain/02-Indexes/index.md
touch ~/Gil-dev/second-brain/03-System_Logs/log.md
```

3. Initialize an Obsidian vault in the `~/Gil-dev/second-brain` directory. This provides the visual graph and manual review interface.

---

## Phase 2: Tooling Installation

The AI Bookkeeper requires CLI-native tools to search and manipulate the file system autonomously.

1. **Install Claude Code:** Execute `npm install -g @anthropic-ai/claude-code`. This installs the primary agent.

2. **Install qmd:** Install the lightweight local search engine. This component executes hybrid BM25/vector searches across the vault without rereading every file.
   Execute: `cargo install qmd` (requires Rust toolchain).

3. **Authenticate Claude Code:** Navigate to your vault (`cd ~/Gil-dev/second-brain`) and run `claude`. Follow the prompts to authenticate your Anthropic account.

4. **Configure Obsidian Plugins:** Install the "Dataview" plugin in Obsidian to query page frontmatter (tags, dates, source counts) and generate dynamic tables.

---

## Phase 3: The Schema Configuration (Command Level)

The schema defines the exact workflows the LLM must follow to maintain the wiki. You must instruct Claude Code to act as a disciplined custodian when executing specific tasks.

1. Create a global command configuration directory and file.
   Execute:

```bash
mkdir -p ~/.claude/commands
touch ~/.claude/commands/librarian.md
```

2. Open the file and paste the following strict instructions:

```
You are the AI Bookkeeper for Gilberto Silva Gonzalez.
Your function is to maintain, update, interconnect, and analyze a persistent local knowledge base.

You must follow four core operations:

1. INGEST: When I provide a new source document in the `00-Raw_Sources` directory:
- Read the document thoroughly. Never modify the raw source.
- Use `qmd` to search the vault for existing entities, projects, or topics.
- Extract key constraints, decisions, and data.
- Open the relevant existing markdown files in the L1-L7 directories and integrate the new information. Explicitly note where new data contradicts or strengthens existing claims.
- Detect cross-pillar intersections. When an ingested source spans multiple domains, automatically generate a synthesis document in `02-Indexes/topic_maps/` to bridge the isolated data points.
- Create new entity pages in `01-Entities` if novel concepts appear.
- Update `02-Indexes/index.md` with links and one-line summaries for any new pages.
- Append a chronological record of your actions to `03-System_Logs/log.md` using the prefix format: `## [YYYY-MM-DD] ingest | [Source Title]`.

2. QUERY: When I ask a question against the wiki:
- Search for relevant pages using `qmd` or by reading `index.md`.
- Read the pages and synthesize an answer with citations.
- File the synthesized answer back into the wiki as a new markdown page. Never let valuable synthesis disappear into the chat history.

3. LINT: When I instruct you to health-check the wiki:
- Scan for contradictions between pages.
- Flag stale claims superseded by newer sources.
- Identify orphan files lacking inbound links.
- Find missing cross-references or data gaps.
- Append a summary of your findings to `log.md`.

4. PREDICT: When I instruct you to predict blind spots:
- Analyze historical data across the L1-L7 directories.
- Track return on energy and systemic shifts in energy allocations.
- Output mathematical risk assessments (e.g., trajectory for burnout based on L2 decline versus L3 spikes) and save the report to `03-System_Logs`.

Never output the final synthesis to the chat interface alone. Always stitch the changes directly into the markdown files in the vault.
```

---

## Phase 4: Workspace Context Configuration (CLAUDE.md)

While the `/librarian` command triggers specific actions, Claude Code requires a persistent workspace configuration to understand the environment at all times. The CLAUDE.md file anchors the agent to your system rules and operates as the baseline intelligence for the directory.

1. Create the project-level context file.
   Execute: `touch ~/Gil-dev/second-brain/CLAUDE.md`

2. Open the file and insert these parameters:

```markdown
# Second Brain Workspace Configuration

## Role & Context
You operate within the Second Brain of Gilberto Silva Gonzalez (Sr. TPM at Blue Origin). This is a persistent knowledge graph. You act as the custodian of this data.

## Writing Conventions (Strict Enforcement)
- Always use active voice.
- Always remain objective.
- Eliminate clutter words.
- Eliminate weasel words entirely.
- Format all outputs in strict Markdown.
- Include YAML frontmatter for all new files.

## Directory Architecture Rules
- `00-Raw_Sources`: Immutable. You must read from this directory but never edit or delete files here.
- `01-Entities`: Store nodes for people, organizations, and systems here.
- `L1-L7`: Core operational pillars. Synthesize information and write artifacts here.
- `02-Indexes/index.md`: The master registry. Update this when creating new files.
- `03-System_Logs/log.md`: The chronological operation log.

## Tooling
- Always execute `qmd` to search the vault before creating new pages to prevent duplicates and maintain cross-references.
```

**Why this is necessary:** The CLAUDE.md file loads automatically at the start of every Claude Code session within the second-brain directory. Without it, the agent defaults to a standard conversational assistant with a blank slate. This file forces the agent to adhere instantly to your strict writing standards (active voice, objective phrasing, zero weasel words) and prevents it from hallucinating directory structures or modifying the immutable `00-Raw_Sources` folder. It establishes the rules of engagement before you type a single prompt.

---

## Phase 5: Initial Bulk Ingestion Strategy (66 Sources)

Do not execute a single command for all 66 files. A massive batch ingestion triggers context window collapse, degrades synthesis quality, and fails to build granular cross-references. Execute the initial ingestion using a thematic, chunked approach.

1. **Categorize the Baseline:** Group the 66 files by life area (e.g., place all technical BRDs in an `L3_Batch` folder inside `00-Raw_Sources`, and all habit/productivity books in an `L4_Batch` folder).

2. **Execute Thematic Chunks:** Process a maximum of 3 to 5 related files per command. This constraint forces the LLM to process the nuances of the data rather than generating shallow overviews.
   Example command:

```
claude /librarian "Execute Ingest Protocol: Read the 4 book summaries located in 00-Raw_Sources/L4_Batch. Write the new markdown files to the L4-Growth pillar, and immediately rebuild 02-Indexes/index.md."
```

3. **Verify the Graph:** After the agent completes a batch, open the Obsidian graph view. Visually verify the agent created the entity nodes and connected them to the appropriate L1-L7 index files.

4. **Lint After Every 15 Files:** Once you ingest 15 files (approximately 3 batches), run the Lint operation. This forces the agent to repair broken links and update the overarching index before the vault complexity increases.

5. **Repeat:** Move to the next thematic batch until all 66 files populate the persistent architecture.

---

## Phase 6: Standard Operations Protocol

Execute these protocols to run the system after the initial 66 sources exist in the vault.

### Establish a Strict Ingestion Trigger (The Ingest Operation)

The architecture describes the structure, but a system requires an ignition protocol. Execute this strict ingestion trigger when you capture new information to process the data and prevent context window collapse.

1. Move the immutable raw file into `~/Gil-dev/second-brain/00-Raw_Sources/`.
2. Open your terminal: `cd ~/Gil-dev/second-brain`.
3. Invoke the agent using the exact command prompt:

```
claude /librarian "Execute Ingest Protocol: Read the Serenity Scheduling BRD in 00-Raw_Sources. Write the new markdown files to the L3-Career architecture, and immediately rebuild 02-Indexes/index.md."
```

4. The agent executes the command, reads the source, modifies the L3 project files, rebuilds the master index, and appends the action to `log.md`.

### Mandate Cross-Pillar Topic Mapping

Rigid L1-L7 pillars create data silos. A book on high-performance habits impacts both L3-Career and L1-Health. The schema instructs the LLM to detect these cross-pillar intersections automatically.

1. The LLM evaluates the ingested source across all seven pillars.
2. When a source spans multiple domains, the LLM automatically generates a synthesis document in `02-Indexes/topic_maps/`.
3. This document bridges the isolated data points and prevents knowledge fragmentation.

### The Query Operation

Execute this operation to answer questions or generate new artifacts based on accumulated data.

1. Invoke the agent:

```
claude /librarian "Query the wiki. Analyze the data additions in L1-Health and L3-Career over the past 30 days. Calculate the ratio of career hours against physical recovery metrics. Save the output as a risk assessment dashboard in the L1-Health directory."
```

2. The agent reads the existing synthesis and creates a new, permanent artifact in the vault.

### The Lint Operation

Execute this operation weekly to maintain the structural integrity of the graph.

1. Invoke the agent:

```
claude /librarian "Lint the wiki. Find any orphan files in L3-Career and identify contradictions between my stated L1-Health goals and my actual logged metrics."
```

2. The agent repairs broken links, flags inconsistencies, and logs the maintenance cycle.

---

## Phase 7: The Predictive Analysis Protocol

Execute this operation monthly. The bookkeeper recognizes the architectural patterns of your life faster than you do. You use this to surface blind spots before you consciously feel the symptoms.

1. Invoke the agent:

```
claude /librarian "Predict blind spots. Analyze my journaling logs and L2-Relationships data against the recent spike in L3-Career hours over the last 90 days. Calculate my trajectory for burnout and write a warning report to the 03-System_Logs directory."
```

2. The agent calculates the return on energy, identifies misalignments, and mathematically warns you of impending systemic failures.

---

## Appendix: 3-Level Directory Architecture

This tree represents the target structure of the knowledge base up to 3 levels deep, populated with examples from your specific ecosystem (Blue Origin, health protocols, financial ledgers, etc.).

```
~/Gil-dev/second-brain/
├── 00-Raw_Sources/
│   ├── L1_Batch/          # e.g., Blood_Analysis_Biomarkers.pdf
│   ├── L3_Batch/          # e.g., Serenity_Scheduling_BRD.pdf
│   └── L4_Batch/          # e.g., Deep_Work_Cal_Newport.md
├── 01-Entities/
│   ├── Authors/           # e.g., Tiago_Forte.md, Tony_Robbins.md
│   ├── Organizations/     # e.g., Blue_Origin.md, Amazon.md
│   └── Systems/           # e.g., Jules_MES.md, Copilot_Money.md
├── 02-Indexes/
│   ├── index.md           # The master registry of all pages
│   └── topic_maps/        # e.g., high_performance_habits_L1_L3_map.md
├── 03-System_Logs/
│   ├── log.md             # Chronological append-only operations log
│   └── predictive_reports/  # e.g., burnout_trajectory_assessments/
├── L1-Health/
│   ├── protocols/         # e.g., gil_health_upgrade_protocol.md
│   └── dashboards/        # e.g., risk_assessment_dashboard.md
├── L2-Relationships/
│   ├── household/         # e.g., luisa_shared_tasks.md
│   └── network/           # e.g., friend_catchup_logs.md
├── L3-Career/
│   ├── systems_design/    # e.g., serenity_scheduling_architecture.md
│   └── weekly_reviews/    # e.g., week_17_review_brief.md
├── L4-Growth/
│   ├── methodologies/     # e.g., para_method.md, atomic_habits.md
│   └── habits/            # e.g., daily_habit_tracker_2026.md
├── L5-Finance/
│   ├── protocols/         # e.g., micro_execution_protocol.md
│   └── ledgers/           # e.g., debt_execution_strategy.md
├── L6-Hobbies/
│   └── travel/            # e.g., kennedy_space_center_log.md
└── L7-Contribute/
    └── guides/            # e.g., ai_system_guide_for_sister.md
```

### Root Pillar Initialization Mechanics

You create the root L1 through L7 folders manually. The LLM does not create these top-level pillars.

- **Who:** You (the system architect).
- **When:** During Phase 1 (Three-Layer Architecture Setup), before you authenticate the LLM or ingest any files.
- **How:** You execute the `mkdir -p ~/Gil-dev/second-brain/{...}` command in your terminal. This command builds the immutable skeleton of the Gil Operating System. The LLM relies on this pre-existing structure to route synthesized knowledge.

### Subfolder Generation Mechanics

The LLM agent dynamically generates the subfolders within the L1-L7 pillars during the INGEST operation. You do not create these folders manually.

1. **Semantic Analysis:** When the agent reads a raw source, it identifies the core domain and the specific sub-category based on the content.
2. **Directory Creation:** If a relevant subfolder (e.g., `systems_design/`) does not exist inside the target pillar (`L3-Career/`), the agent executes a terminal command to create it.
3. **File Placement:** The agent writes the synthesized markdown file directly into this new semantic subfolder.
4. **Taxonomy Alignment:** The agent aligns new subfolders with the Gil Operating System framework. It categorizes technical Blue Origin documentation into `L3-Career/systems_design/` and physical biomarker data into `L1-Health/dashboards/`.
