<!-- HERO: Lesson 1.2: Prompt Engineering vs. Context Engineering | Master the two levers that determine AI output quality - and learn when to use each one. -->[cite: 4]

<!-- TOC: Overview#anchor-overview | Step 1: The Core Distinction#anchor-step-1 | Step 2: Better Prompts in Practice#anchor-step-2 | Step 3: Five Prompting Patterns#anchor-step-3 | Step 4: Context Engineering in Practice#anchor-step-4 | Step 5: Managing Your Context Window#anchor-step-5 | Step 6: Putting It All Together#anchor-step-6 | Verification#anchor-verification -->[cite: 4]

## Overview[cite: 4]

There are two ways to improve AI output. Most people only know the first one. This lesson gives you both. You will learn the difference between prompt engineering and context engineering, apply five proven prompting patterns, and build one complete high-quality prompt using a formula you can reuse every day.[cite: 4]

### Why This Matters[cite: 4]

Most AI frustration comes from one of two problems: a vague prompt or missing context. Understanding which problem you have tells you exactly how to fix it. You will stop guessing and start diagnosing.[cite: 4]

### Prerequisites[cite: 4]

- [Lesson 1.1: How AI Models Work](1-1_How_AI_Models_Work.md)[cite: 4]

### Time to Complete[cite: 4]

**20 minutes**[cite: 4]

<!-- PROGRESS: Step 1: The Core Distinction | Step 2: Better Prompts in Practice | Step 3: Five Prompting Patterns | Step 4: Context Engineering in Practice | Step 5: Managing Your Context Window | Step 6: Putting It All Together | Verification -->[cite: 4]

---[cite: 4]

<!-- ANCHOR: anchor-overview -->[cite: 4]

<!-- ANCHOR: anchor-step-1 -->[cite: 4]

## Step 1: The Core Distinction[cite: 4]

Two concepts control AI output quality. Prompt engineering controls how you ask. Context engineering controls what information you give the AI to work with. Most people spend all their time on the first one and ignore the second. The second one matters more.[cite: 4]

### What You'll Do[cite: 4]

You will learn the fundamental difference between the two concepts and the three rules for applying them to your daily work.[cite: 4]

### Instructions[cite: 4]

1. Read the definitions below. Notice they describe completely different types of work.[cite: 4]
2. Study the comparison table. Focus on the "Analogy" row - it makes the distinction concrete.[cite: 4]
3. Read the three application rules at the bottom of this step.[cite: 4]
4. Think of one AI interaction you had recently. Identify whether your problem was prompt quality, context quality, or both.[cite: 4]
5. Keep this distinction in mind for every step in this lesson.[cite: 4]

### Key Concepts[cite: 4]

**Prompt Engineering = How You Ask**[cite: 4]
The wording, structure, and specificity of your instruction to the model. This is the text you type.[cite: 4]

**Context Engineering = What You Give the AI to Work With**[cite: 4]
The information you provide or connect to the model so it can reason well. Examples: data sets, requirement documents, checklists, design notes, relevant wiki pages, constraints, and known rules.[cite: 4]

| Dimension | Prompt Engineering | Context Engineering |[cite: 4]
|---|---|---|[cite: 4]
| **Focus** | User-facing text (how you ask) | System-oriented data (what you provide) |[cite: 4]
| **Nature** | Transient, single-turn | Persistent, memory-managed |[cite: 4]
| **Method** | Trial-and-error iteration | Deterministic, structured pipelines |[cite: 4]
| **Input** | A single text instruction | An organized information payload |[cite: 4]
| **Analogy** | Writing a clear email subject line | Attaching the right documents to the email |[cite: 4]

**Three Rules for Applying Both Concepts:**[cite: 4]

1. **Front-load relevant information.** Paste or attach the right excerpt instead of asking the model to guess from nothing.[cite: 4]
2. **Constrain the scope.** Be explicit about which sources are authoritative vs. which are just ideas.[cite: 4]
3. **Persist and refine.** Reuse a conversation with accumulated context for one workstream instead of starting fresh for every question.[cite: 4]

<!-- INFO: The Key Principle | Good outcomes depend at least as much on context as on the wording of a single prompt. Stop optimizing your prompt. Start optimizing your context. -->[cite: 4]

<!-- TIP: Diagnose Before Fixing | When the AI gives you a wrong or weak answer, ask: "Did I give it the right information?" before "Did I phrase my question correctly?" Context problems cause most AI failures. -->[cite: 4]

---[cite: 4]

<!-- ANCHOR: anchor-step-2 -->[cite: 4]

## Step 2: Better Prompts in Practice[cite: 4]

A vague prompt forces the AI to guess. Every guess introduces error. The fix is not to be a better writer. The fix is to be more specific. This step shows you what that looks like in practice for your role.[cite: 4]

### What You'll Do[cite: 4]

You will compare weak prompts to strong prompts across three roles. You will identify the pattern that makes each strong prompt work.[cite: 4]

### Instructions[cite: 4]

1. Read the before/after examples in the columns below for HR and Marketing.[cite: 4]
2. Notice what specific information was added in each "After" example.[cite: 4]
3. Read the expanded examples for UX and Legal in the expand section below.[cite: 4]
4. Identify which role example is closest to your own daily work.[cite: 4]
5. Use the strong prompt as a model the next time you ask Claude a similar question.[cite: 4]

<!-- COLUMNS: 50/50 -->[cite: 4]

**HR:**[cite: 4]

```text
❌ Before:
"Summarize this."
```

*Vague. Summarize for whom? How long? What format?*[cite: 4]

```text
✅ After:
"Summarize this interview transcript as 5 bullet points for the hiring manager. Focus on the candidate's strengths and any concerns raised during the interview."
```

*Specifics: audience, length, format, focus area.*[cite: 4]

<!-- COLSEP -->[cite: 4]

**Marketing:**[cite: 4]

```text
❌ Before:
"What's late?"
```

*Late compared to what? Which campaign? Which channel?*[cite: 5]

```text
✅ After:
"Which social posts scheduled for this launch campaign have not gone out, are more than 2 days past their scheduled date? Show as a table: platform, scheduled date, days late. Sort by days late descending."
```

*Specifics: campaign, threshold, format, sort order.*[cite: 5]

<!-- /COLUMNS -->[cite: 5]

<!-- EXPAND: More Examples - HR, Industrial Engineering, and Legal -->[cite: 5]

**HR:**[cite: 5]

```text
❌ Before:
"Write a job description."
```

*For what role? What level? What team? What tone?*[cite: 5]

```text
✅ After:
"Write a job description for a Senior Account Manager on the customer success team. Requirements: 5+ years in B2B account management, CRM experience, and a track record of client retention. Use our standard job description format: summary, responsibilities, requirements, benefits. Tone: professional but warm."
```

**Legal:**[cite: 5]

```text
❌ Before:
"Review this contract."
```

*Review for what? Which clauses? What output?*[cite: 5]

```text
✅ After:
"Review this NDA for missing standard clauses. Check for: definition of confidential information, term length, return-of-materials, and governing law. List each missing or weak clause with a one-line note on the risk it creates."
```

**Industrial Engineering:**

```text
❌ Before:
"Check the downtime report."
```

*Which line? Which shift? What counts as downtime?*

```text
✅ After:
"Which production lines in this week's downtime report exceeded 30 minutes of unplanned downtime? Show as a table: line, date, duration, stated cause. Sort by duration descending."
```

<!-- /EXPAND -->[cite: 5]

<!-- INFO: The Specificity Rule | Every vague word in your prompt forces a guess. A prompt with five vague elements has roughly a 3% chance of producing exactly what you want. A prompt with five specific elements produces accurate results nearly every time. Specificity is the mechanism, not a nice-to-have. -->[cite: 5]

---[cite: 5]

<!-- ANCHOR: anchor-step-3 -->[cite: 5]

## Step 3: Five Prompting Patterns That Cover 90% of Your Work[cite: 5]

You do not need to memorize dozens of techniques. Five patterns cover almost everything you will do in Claude. This step gives you each pattern with a definition, a use case, and a ready-to-use example.[cite: 5]

### What You'll Do[cite: 5]

You will learn five prompting patterns and identify which one fits a task you do regularly this week.[cite: 5]

### Instructions[cite: 5]

1. Read each pattern name and the "When to Use" description.[cite: 5]
2. Identify which pattern matches a task you do today.[cite: 5]
3. Use Pattern 1 (zero-shot) for your simplest, most clearly defined task.[cite: 5]
4. Use Pattern 2 (few-shot) when you need consistent formatting across multiple items.[cite: 5]
5. Use Pattern 5 (interview-style) any time a task feels too ambiguous to start.[cite: 5]
6. Combine patterns when you need the highest-quality output. See the tip below.[cite: 5]

### Key Concepts[cite: 5]

| Pattern | What It Is | When to Use It |[cite: 5]
|---|---|---|[cite: 5]
| **1. Zero-Shot** | Ask once with clear instructions and constraints. No examples provided. | Simple, well-defined tasks where the format is obvious |[cite: 5]
| **2. Few-Shot** | Provide 1-3 examples of desired input/output before asking the model to continue the pattern | Transforming raw notes, classifying items, writing status summaries in a standard format |[cite: 5]
| **3. Role Prompting** | Explicitly assign the AI a role to align tone, depth, and vocabulary | When you need the AI to match a specific expertise level or communication style |[cite: 5]
| **4. Chain-of-Thought** | Ask the model to reason step by step before giving a final answer | Analysis tasks, anything with safety or quality implications, complex decisions |[cite: 5]
| **5. Interview-Style** | Ask the model to ask YOU clarifying questions before proposing solutions | When you are unsure what you need, or when the task is ambiguous |[cite: 5]

### Pattern 2 Example (Few-Shot)[cite: 5]

```text
Convert these raw notes from our campaign retro into formatted action items:

Input: "landing page load time hurt conversions, need dev to fix before next launch"
Output: *Action Item: Fix landing page load time before next launch. Owner: [Your Name]. Source: Campaign retro. Due: Before next launch.*

Input: "email open rates dropped, subject lines felt generic"
Output: *Action Item: A/B test more specific email subject lines. Owner: [Your Name]. Source: Campaign retro. Due: Next email send.*

Now convert this:
Input: "paid social spend ran over budget, no one was watching the daily caps"
...
```

<!-- EXPAND: Pattern 4 Example - Chain-of-Thought -->[cite: 5]

```text
I need to decide whether to escalate a vendor contract renewal that is 30 days from expiring. Walk me through the decision step by step:
(1) What is the current expiration date?
(2) When does a renewal decision need to be made?
(3) What is the cost of renewing vs. switching?
(4) What is the risk of letting it auto-renew?
(5) Based on these factors, recommend escalate or hold.
...
```

<!-- /EXPAND -->[cite: 5]

<!-- EXPAND: Pattern 5 Example - Interview-Style -->[cite: 5]

```text
I need to write a business case for a new employee onboarding tool.
Before you draft anything, ask me 5 clarifying questions about the problem, the audience, the budget, and the timeline.
...
```

<!-- /EXPAND -->[cite: 6]

<!-- NOTE: Combine Patterns for Best Results | Start with Role Prompting ("You are a senior recruiter..."), add Few-Shot examples, then request Chain-of-Thought reasoning. Stacking patterns produces the highest-quality outputs. -->[cite: 6]

---[cite: 6]

<!-- ANCHOR: anchor-step-4 -->[cite: 6]

## Step 4: Context Engineering in Practice[cite: 6]

A model is only as smart as its context. Without proper context, AI systems hallucinate or fail on complex tasks. They generate false data. They invent facts. Engineered context fixes this. This step shows you what good and bad context looks like for your role.[cite: 6]

### What You'll Do[cite: 6]

You will compare low-quality context to high-quality context across three roles and learn the context quality spectrum.[cite: 6]

### Instructions[cite: 6]

1. Read the before/after samples below for each role.[cite: 6]
2. Notice the pattern: good context is filtered, focused, and structured. Bad context is raw, bloated, or missing entirely.[cite: 6]
3. Apply the same pattern to one data source you use regularly (a contract, a résumé stack, a campaign report).[cite: 6]
4. Before your next AI session, spend 2 minutes extracting the relevant rows or sections instead of pasting the entire file.[cite: 6]
5. Compare the quality of the output to what you got before.[cite: 6]

### Examples by Role[cite: 6]

| Role | Bad Context | Good Context |[cite: 6]
|---|---|---|[cite: 6]
| **HR** | Paste 40 résumés and ask "help me screen these" | Paste the job requirements first, then 3 résumés at a time, and ask: "Score each 1-5 on relevant experience, years of experience, and leadership indicators. Show as a table." |[cite: 6]
| **Industrial Engineering** | Paste an entire month of maintenance logs and ask "what's wrong with the line" | Extract just this week's entries and ask: "Which failure codes appear more than twice? List code, frequency, and affected line." |
| **Legal** | Paste an entire 40-page merger agreement and ask "are there any risks?" | Extract just the Indemnification and Termination sections and ask: "Which clauses deviate from our standard template? List clause number, deviation, and risk level." |[cite: 6]
| **Marketing** | Ask "how did the campaign do?" with no data attached | Paste the campaign performance CSV filtered to last 30 days and ask: "Which channels underperformed their target CPA? Show channel, target, actual, and gap." |[cite: 6]

### The Context Quality Spectrum[cite: 6]

| Context Quality | What Happens |[cite: 6]
|---|---|[cite: 6]
| **No context** | AI guesses. High hallucination rate. Output is useless. |[cite: 6]
| **Partial context** | AI gets some things right and invents others. Dangerous because it looks plausible. |[cite: 6]
| **Full, structured context** | AI delivers accurate, grounded answers. Minimal hallucination. Production-ready output. |[cite: 6]

<!-- WARNING: Partial Context is the Most Dangerous State | Partial context produces output that looks correct but contains invented details. Always verify AI output against source data when you suspect your context was incomplete. -->[cite: 6]

<!-- TIP: The Context Rule | You cannot fix a hallucination by rewriting the prompt. You fix it by providing better context. If the model generates a wrong answer, your first question should be: "Did I give it the right information?" not "Did I phrase my question correctly?" -->[cite: 6]

---[cite: 6]

<!-- ANCHOR: anchor-step-5 -->[cite: 6]

## Step 5: Managing Your Context Window[cite: 6]

Every conversation has a limit. As it grows longer, the AI may forget earlier instructions, mix up old and new tasks, or give answers influenced by context you no longer want. Knowing when to keep going vs. when to start fresh is a practical skill you will use daily.[cite: 6]

### What You'll Do[cite: 6]

You will learn the decision criteria for reusing vs. resetting a conversation, and you will practice the summarize-and-reset technique for preserving key decisions when you switch topics.[cite: 6]

### Instructions[cite: 6]

1. Read the two-column decision guide below.[cite: 6]
2. Think about the last time an AI gave you a strange answer mid-conversation. Identify whether old context was the cause.[cite: 6]
3. Read the Summarize-and-Reset technique at the bottom of this step.[cite: 6]
4. Practice it now: open a long Claude conversation and run the summary prompt from Step 4 of the technique.[cite: 6]
5. Use this technique any time you need to switch topics while preserving decisions.[cite: 6]

<!-- COLUMNS: 50/50 -->[cite: 6]

**Reuse the same conversation when:**[cite: 6]

- You are on the same workstream: same document, same decision, same analysis, same meeting prep.[cite: 6]
- Earlier turns are still relevant. Examples:[cite: 6]
  - "We agreed earlier that 'high risk' means X."[cite: 6]
  - "Use the same table structure as before."[cite: 6]
- The conversation is not yet noisy. You have not gone off on tangents or mixed multiple projects into the same chat.[cite: 6]

<!-- COLSEP -->[cite: 6]

**Start a fresh conversation when:**[cite: 6]

- The topic has genuinely changed. You switched from "campaign performance analysis" to "job description writing."[cite: 6]
- The thread is long and messy with experiments, dead ends, or side questions. The model starts reusing outdated assumptions. It answers using the wrong audience or format from 20 turns ago.[cite: 6]
- Token use becomes inefficient. The AI is loading large chunks of irrelevant history to answer a simple new question.[cite: 6]

<!-- /COLUMNS -->[cite: 6]

### The Summarize-and-Reset Technique[cite: 6]

Use this when you need to start fresh but want to preserve key decisions from the current conversation.[cite: 6]

1. **ASK:** "Summarize the key decisions and constraints from this conversation in 5 bullet points."[cite: 6]
2. Copy that summary.[cite: 6]
3. Start a new conversation.[cite: 6]
4. Paste the summary in the "CONTEXT" section at the top of your first new prompt.[cite: 6]

```text
CONTEXT (from previous conversation):
- Decision 1: [AI-generated bullet]
- Decision 2: [AI-generated bullet]
- Decision 3: [AI-generated bullet]

TASK: [Your new question or request]
```

<!-- INFO: Think of It Like Cleaning Your Desk | You do not throw away your notes. You file the important ones and clear the clutter. The same[cite: 6]
principle applies to AI conversations. Preserve what matters. Clear what does not. -->[cite: 7]

<!-- TIP: Watch for the Contamination Signal | If the AI starts giving answers that reference something from 20 turns ago that is no longer relevant, your context window is contaminated. Start fresh and use the summarize-and-reset technique to carry over only what matters. -->[cite: 7]

---[cite: 7]

<!-- ANCHOR: anchor-step-6 -->[cite: 7]

## Step 6: Putting It All Together[cite: 7]

The goal of this lesson is not to teach you theory. It is to give you a formula you will use every day. This step shows you what that formula looks like in action.[cite: 7]

### What You'll Do[cite: 7]

You will study one complete, production-ready prompt that combines context engineering, role prompting, clear task definition, format specification, and constraints. Then you will adapt it for your own work.[cite: 7]

### Instructions[cite: 7]

1. Read the complete prompt example below.[cite: 7]
2. Notice how each labeled section eliminates a different type of guessing.[cite: 7]
3. Identify which section you most often skip in your current AI usage.[cite: 7]
4. Adapt this prompt template for one recurring report or output you produce this week.[cite: 7]
5. Compare the output quality to what you got from a single-sentence prompt.[cite: 7]

### The Complete Prompt Formula[cite: 7]

**Great AI Output = Clear Prompt + Right Context + Appropriate Pattern**[cite: 7]

```text
CONTEXT:
[Paste relevant data here - e.g., this week's applicant tracking system update]

ROLE:
You are a senior HR coordinator writing a weekly hiring pipeline update.

TASK:
Based on the pipeline data above, draft a weekly status update for the hiring manager.

FORMAT:
- Group by: Offers Extended, In Interview,
New Applicants, Stalled
- Include candidate name, role, and one-line status for each item
- Add a "Decisions Needed" section at the bottom
- Keep total length under 1 page

CONSTRAINTS:
- Only include candidates with activity in the last 7 days
- Flag anyone stalled in one stage for more than 10 days
- Do not include candidates already rejected
```

### What Each Section Does[cite: 7]

| Section | What It Controls | What Happens Without It |[cite: 7]
|---|---|---|[cite: 7]
| **CONTEXT** | The data and ground truth the AI reasons from | AI invents facts or gives generic answers |[cite: 7]
| **ROLE** | Tone, depth, vocabulary, and expertise level | AI defaults to a generic writing style that may not match your audience |[cite: 7]
| **TASK** | The core instruction and deliverable | AI misinterprets what you want and produces the wrong output type |[cite: 7]
| **FORMAT** | Structure, length, grouping, and layout | AI chooses its own format, which you then spend time reformatting |[cite: 7]
| **CONSTRAINTS** | What to exclude, what to flag, what rules to follow | AI includes irrelevant content and misses critical edge cases |[cite: 7]

<!-- NOTE: You Do Not Need All Five Sections Every Time | Simple tasks need only TASK and FORMAT. Use CONTEXT, ROLE, and CONSTRAINTS when the task is complex, when accuracy matters, or when the output will be shared with others. -->[cite: 7]

<!-- TIP: Save This Formula | Copy the CONTEXT/ROLE/TASK/FORMAT/CONSTRAINTS template into a note or a CLAUDE.md file. Use it as your starting point for any complex AI request. The sections you fill in are the sections that matter for that task. -->[cite: 7]

---[cite: 7]

<!-- ANCHOR: anchor-verification -->[cite: 7]

## Verification[cite: 7]

You have completed all six steps. Confirm your understanding by checking each item below:[cite: 7]

- [ ] You can explain the difference between prompt engineering and context engineering in one sentence[cite: 7]
- [ ] You can name at least three of the five prompting patterns and describe when to use each[cite: 7]
- [ ] You know the three context quality levels and can identify which one produces hallucinations that look correct[cite: 7]
- [ ] You know when to reuse a conversation and when to start fresh[cite: 7]

<!-- NOTE: Not Working? | If any check feels unclear, revisit the step where that concept appeared. The Key Concepts tables in Steps 1 and 3 are your primary reference for terminology and patterns. -->[cite: 7]

---[cite: 7]

<!-- CELEBRATION: Lesson Complete! | You now know the two levers that control AI output quality, five patterns that cover 90% of your work, and a formula you can apply to any complex AI request. -->[cite: 7]

### What's Next[cite: 7]

**Next Lesson:** [Lesson 1.3: Practical Prompting Techniques](1-3_Practical_Prompting_Techniques.md)[cite: 7]

**Related Resources:**[cite: 7]
- [claude.ai](https://claude.ai) - Start a conversation and apply these patterns[cite: 7]
- [Claude Documentation](https://code.claude.com/docs) - Official documentation[cite: 7]
- [Claude Support](https://support.claude.com) - Help articles and answers to common questions[cite: 7]

<!-- TIP: Build Your Formula Library | After you apply the CONTEXT/ROLE/TASK/FORMAT/CONSTRAINTS formula to one recurring task, save it. Within a month you will have a personal prompt library covering your most common work. -->[cite: 7]

<!-- CHILDREN -->[cite: 7]