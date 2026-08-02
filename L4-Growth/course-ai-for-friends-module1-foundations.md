---
title: "AI for Friends — Module 1: AI Foundations"
type: course-notes
pillar_id: L4
source_file:
  - "00-Raw_Sources/L4_Growth/2026-08-02/1-0_AI_Foundations_module.md"
  - "00-Raw_Sources/L4_Growth/2026-08-02/1-1_How_AI_Models_Work.md"
  - "00-Raw_Sources/L4_Growth/2026-08-02/1-2_Prompt_Engineering_vs_Context_Engineering.md"
  - "00-Raw_Sources/L4_Growth/2026-08-02/1-3_Practical_Prompting_Techniques.md"
  - "00-Raw_Sources/L4_Growth/2026-08-02/1-4_Chossing_AI_Model.md"
created: 2026-08-02
tags: [l4, growth, ai, course, prompting, context-engineering, costars, model-selection]
related: [L4-Growth/course-ai-for-friends, L4-Growth/course-ai-for-friends-module3-claude-code, 02-Indexes/topic_maps/ai-course-cross-pillar-map]
---

# AI for Friends — Module 1: AI Foundations for Non-Technical Roles

Part of [AI for Friends — Course Overview](course-ai-for-friends.md).

Synthesis of Lessons 1.1–1.4 (55–70 min). Builds the conceptual AI fluency layer the rest of the course assumes: how models work, the two levers of output quality, four core prompting techniques plus the COSTARS framework, and model selection. Stated value proposition: 3–8 hr/week saved, compounding to 150–400 hr/year.

---

## 1. The Mental Model: AI Predicts, It Does Not Think

Three plain-English analogies, any one of which is sufficient:

| Analogy | Meaning | Implication |
|---|---|---|
| The well-read intern | Has processed billions of documents but predicts text rather than understanding it | Vague instructions produce vague results |
| The limited desk | The context window is working memory; when full, older information drops off | Paste only what the AI needs, not everything available |
| The literal executor | Follows instructions exactly as written, does not infer intent | Be specific — the AI will not fill gaps the way a colleague would |

**Core terms:** Prompt, Context window, Token (~¾ word), Agent, MCP Server (live connection to another app/system), Knowledge Base, Hallucination (confident false output produced when the model lacks real data and predicts instead), LLM, RAG.

**Three Stages of AI Capability:**

| Stage 1: AI Assistant | Stage 2: AI Agent | Stage 3: Agentic AI System |
|---|---|---|
| Follows rules; you provide all context | Achieves goals via multi-step workflows; pulls live data from connected systems | Multiple specialized agents coordinate and consolidate results |
| Widely available today | Widely available today | Still early/emerging |

**The 7-step agentic loop:** prompt → agent receives it → model reasons what to do → model selects a tool → tool executes against live data → agent reasons/loops if more data is needed → final response returned. A wrong answer usually breaks at tool selection or at the data the tool returned — ask the agent to "walk me through how you got that answer" to debug.

**Three operating principles:** (1) you are the pilot, the AI executes — you direct, validate, decide; (2) specificity wins — named fields, date ranges, sort order produce usable results; (3) AI accelerates judgment, it does not replace it.

---

## 2. Prompt Engineering vs. Context Engineering

Two independent levers, most people only use the first:

| | Prompt Engineering | Context Engineering |
|---|---|---|
| Controls | How you ask (wording, structure) | What you give the AI to work with |
| Analogy | Writing a clear email subject line | Attaching the right documents to the email |
| Nature | Transient, single-turn | Persistent, structured |

**Diagnostic rule:** when output is wrong, ask "did I give it the right information?" before "did I phrase it correctly?" — context problems cause most AI failures, and a hallucination cannot be fixed by rewriting the prompt.

**The Context Quality Spectrum:** no context → AI guesses, high hallucination; partial context → AI invents details that look plausible (the most dangerous state, because it isn't obviously wrong); full structured context → accurate, production-ready output.

**Five prompting patterns covering ~90% of use cases:**

| Pattern | Use When |
|---|---|
| Zero-shot | Task is simple and well-defined |
| Few-shot (1–3 examples) | Need consistent formatting across multiple items |
| Role prompting | Need a specific expertise level or communication style |
| Chain-of-thought | Analysis, safety/quality implications, complex decisions |
| Interview-style (AI asks you questions first) | Task is ambiguous or you're unsure what you need |

Patterns stack: Role Prompting to set the foundation → Few-Shot for formatting → Chain-of-Thought for analysis produces the highest-quality output.

**Managing the context window:** reuse a conversation while on the same workstream and earlier turns stay relevant; start fresh when the topic genuinely changed, the thread is long/messy, or the model starts referencing stale context ("contamination signal"). The **Summarize-and-Reset technique**: ask "summarize the key decisions and constraints from this conversation in 5 bullets," carry that summary into a new conversation's CONTEXT section.

**The Complete Prompt Formula:** `CONTEXT / ROLE / TASK / FORMAT / CONSTRAINTS`. Simple tasks need only TASK and FORMAT; complex or shared-output tasks warrant all five.

---

## 3. Four Core Prompting Techniques + COSTARS

| Technique | What It Is | When |
|---|---|---|
| Few-Shot | 1–3 example input/output pairs | Data extraction, classification, consistent formatting |
| Role Prompting | Assign the AI an identity/expertise | Domain expertise, specific tone |
| Chain-of-Thought | Ask for step-by-step reasoning before the answer | Complex, multi-factor decisions |
| Meta Prompting | Ask the AI to write the prompt for you | You know the goal, not the phrasing |

**COSTARS framework** (for complex, multi-dimensional prompts):

| Letter | Component | Controls |
|---|---|---|
| C | Context | Background — who you are, the situation |
| O | Objective | The specific task/goal |
| S | Style | Professional, technical, conversational, data-driven |
| T | Tone | Confident, empathetic, urgent, neutral |
| A | Audience | Who reads the output |
| R | Response | Format — table, bullets, email, list |
| S | Scope/Constraints | What the AI should not do |

Context, Objective, and Response are the critical three; Style/Tone/Audience/Scope matter most when output reaches a director/VP or accuracy is high-stakes.

**Interview-Style Prompting** (for exploratory tasks): the AI asks the user targeted questions about role, pain points, and inefficiencies before producing recommendations — lower upfront effort than COSTARS, often surfaces needs the user hadn't articulated. Use it first when unsure what to ask for; use COSTARS once the need is clear.

**Six Responsible Validation Habits** (non-optional):

1. **Source Check** — can this be traced to a real system or verified data?
2. **Plausibility Scan** — does anything contradict known domain facts?
3. **Self-Critique** — ask the AI: "List 3 ways this could be wrong or incomplete."
4. **Label Drafts** — never share AI output without a "draft / needs review" status.
5. **Decompose Risky Tasks** — use AI for summarizing/reformatting/generating options; humans own conclusions.
6. **Escalate Edge Cases** — compliance, legal, or reputational uncertainty goes to a human expert.

**Safe for AI vs. keep human-only:** AI may summarize, draft (for review), format, generate options, extract, classify. Humans alone make hiring/firing decisions, approve safety-critical procedures, make legally binding representations, commit to deadlines, finalize brand/legal risk, or sign off on compliance.

---

## 4. Choosing a Model

**Golden rule:** use the smallest, cheapest model that does the job well; upgrade only when the task demands it.

| Model (as of course creation) | Best For | Relative Cost |
|---|---|---|
| Claude Haiku 4.5 | Quick questions, formatting, simple classification, bulk repetitive work | 1x (baseline) |
| Claude Sonnet 4.5 | Reports, analysis, summaries, drafting — the default for ~80% of tasks | ~3x Haiku |
| Claude Opus 4.7 | Complex strategy, deep multi-step analysis, high-stakes deliverables | ~5x Haiku |

Google Gemini is the named exception for video/audio (Claude processes neither natively); dedicated tools (e.g., GPT Image 1 Mini, Whisper) cover image generation and transcription.

**Five-question decision flow:** simple/well-defined → Haiku; standard knowledge work → Sonnet (default); deep reasoning required → Opus; video/audio → Gemini; image generation → dedicated image tool.

**Token reference:** 1 token ≈ ¾ word; 1 page ≈ 500 tokens; a 1-hour meeting transcript ≈ 10,000–20,000 tokens.

> **Dated snapshot:** the specific model names/versions above (Haiku 4.5, Sonnet 4.5, Opus 4.7) reflect the model lineup at course creation (2026-08-02) and will go stale as Anthropic ships new models. Treat the *decision framework* (intelligence/speed/cost tradeoff, golden rule) as durable; re-verify the specific model table before reusing it.

---

## Application Note

The COSTARS "AI Launchpad Prompt" and the Interview-Style prompt (Lesson 1.3) are both directly reusable for Gil's own TPM work, not just course material — they're templates for generating a personalized AI-adoption roadmap against a real role and team.

---

## What's Next

Module 2 ([Setting Up Your Computer](course-ai-for-friends-module2-computer-setup.md)) is an optional warm-up; Module 3 ([Claude Code](course-ai-for-friends-module3-claude-code.md)) is the hands-on continuation and does not require Module 2.
