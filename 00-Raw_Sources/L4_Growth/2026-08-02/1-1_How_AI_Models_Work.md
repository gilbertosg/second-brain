<!-- HERO: Lesson 1.1: How AI Models Work | Learn what AI actually does, how agents take action, and why clear instructions make all the difference. -->[cite: 1]

<!-- TOC: Overview#anchor-overview | Step 1: What an AI Model Actually Is#anchor-step-1 | Step 2: The Terms You Need to Know#anchor-step-2 | Step 3: Three Stages of AI Capability#anchor-step-3 | Step 4: How Agents Actually Work#anchor-step-4 | Step 5: What This Means for Your Work#anchor-step-5 | Verification#anchor-verification -->[cite: 1]

## Overview[cite: 1]

By the end of this lesson, you will understand what AI models actually do, recognize the terms you encounter daily, and know how to direct an AI agent to get real work done. You will also understand where AI tools sit on the capability spectrum today.[cite: 1]

### Why This Matters[cite: 1]

Most people use AI like a search engine. They type a vague question and accept a mediocre answer. Understanding how AI models work shifts your approach. You will give clearer instructions, get better results, and stop guessing at why the AI sometimes misses the mark.[cite: 1]

### Prerequisites[cite: 1]

- A Claude account (claude.ai) or interest in AI tools[cite: 1]
- No prior AI or technical knowledge required[cite: 1]

### Time to Complete[cite: 1]

**10 minutes**[cite: 1]

<!-- PROGRESS: Step 1: What AI Is | Step 2: Key Terms | Step 3: Three Stages of AI | Step 4: The Agentic Loop | Step 5: What This Means for You | Verification -->[cite: 1]

---[cite: 1]

<!-- ANCHOR: anchor-overview -->[cite: 1]

<!-- ANCHOR: anchor-step-1 -->[cite: 1]

## Step 1: What an AI Model Actually Is[cite: 1]

AI does not think. It predicts patterns at superhuman speed. This distinction changes how you use it. When you understand what is actually happening, you can give the AI the right inputs to get the right outputs.[cite: 1]

### What You'll Do[cite: 1]

You will learn three plain-English analogies for how AI works. Pick the one that clicks best and use it whenever you explain AI to a colleague.[cite: 1]

### Instructions[cite: 1]

1. Read the three analogies in the table below.[cite: 1]
2. Pick the one that resonates most with how you think.[cite: 1]
3. Use that analogy when you explain AI to someone new.[cite: 1]
4. Keep this mental model in mind as you read every other lesson in this curriculum.[cite: 1]
5. Do not try to memorize technical definitions. Focus on the pattern.[cite: 1]

### Key Concepts[cite: 1]

| Analogy | What It Means | What It Tells You |[cite: 1]
|---|---|---|[cite: 1]
| The well-read intern | AI has processed billions of documents but predicts text rather than understanding it | Vague instructions produce vague results |[cite: 1]
| The limited desk | The "context window" is the AI's working memory. When it fills up, older information drops off. | Paste only what the AI needs, not everything you have |[cite: 1]
| The literal executor | AI follows your instructions exactly as written. It does not infer what you meant. | Be specific. The AI will not fill in gaps the way a human colleague would. |[cite: 1]

<!-- INFO: The Core Insight | AI does not think. It predicts what text should come next based on patterns. Your job is to give it clear patterns to match against. The quality of your output is directly proportional to the quality of your input. -->[cite: 1]

<!-- TIP: One Sentence Rule | If you can state exactly what you want in one specific sentence, your AI output will be twice as good. Vague prompts produce vague answers. -->[cite: 1]

---[cite: 1]

<!-- ANCHOR: anchor-step-2 -->[cite: 1]

## Step 2: The Terms You Need to Know[cite: 1]

You will see these words constantly in Claude, in this curriculum, and in conversations about AI. You do not need to memorize all of them. You need to recognize them when you see them.[cite: 1]

### What You'll Do[cite: 1]

You will scan the terminology table below. Bookmark this lesson. Return to this table whenever a term confuses you later in the curriculum.[cite: 1]

### Instructions[cite: 1]

1. Read through the table once from top to bottom.[cite: 1]
2. Pay special attention to the four terms marked with an asterisk. You will use these every day.[cite: 1]
3. Do not try to memorize all 10 terms at once. Focus on **Prompt**, **Context window**, **Agent**, and **MCP Server** first.[cite: 1]
4. Bookmark this lesson so you can return to this table any time.[cite: 1]

### Key Concepts[cite: 1]

| Term | What It Means | Why You Care |[cite: 1]
|---|---|---|[cite: 1]
| **Prompt** * | The instruction or question you type to the AI | The quality of your prompt determines the quality of your answer |[cite: 1]
| **Context window** * | The AI's working memory. How much text it can process in one conversation. | If you paste too much, the AI forgets the earlier parts of your conversation |[cite: 1]
| **Token** | A chunk of text, roughly three-quarters of a word. Models measure capacity in tokens. | Large files cost more tokens and can overflow the context window |[cite: 1]
| **Model** | The specific AI brain you are talking to | Different models have different speeds, costs, and capabilities |[cite: 1]
| **LLM (Large Language Model)** | The technical name for AI models like Claude. They generate text by predicting the next word. | This is the technology running behind Claude and similar tools |[cite: 1]
| **Generative AI** | AI that creates new content (text, images, code) rather than sorting or classifying existing data | Claude is a generative AI tool |[cite: 1]
| **MCP Server** * | A live connection between your AI assistant and another system (a document store, calendar, or app) | MCP servers let your agent query real data instead of guessing answers |[cite: 1]
| **Agent** * | A pre-configured AI assistant with specific instructions and system connections | You will build your own Claude Project in Module 4 |[cite: 1]
| **Knowledge Base** | A collection of documents the AI can search to answer your questions | Upload your team's SOPs so the AI can answer questions from them |[cite: 1]
| **RAG (Retrieval Augmented Generation)** | The technique of fetching relevant documents first, then generating an answer based on them | This is how Knowledge Bases work behind the scenes |[cite: 1]

<!-- NOTE: Not a Quiz | You will not be tested on these terms. This table is a reference. The four asterisked terms appear in every lesson. Return here any time. -->[cite: 1]

<!-- TIP: Bookmark This Lesson | When a term in a later module confuses you, come back to this table. It covers everything you need for this entire curriculum. -->[cite: 1]

---[cite: 1]

<!-- ANCHOR: anchor-step-3 -->[cite: 1]

## Step 3: Three Stages of AI Capability[cite: 1]

Not all AI tools behave the same way. There is a spectrum from simple text generation to fully autonomous multi-agent systems. Knowing where a tool sits on this spectrum tells you what you can ask it to do and what you still need to do yourself.[cite: 1]

### What You'll Do[cite: 2]

You will compare the three stages of AI capability and identify where today's tools fall.[cite: 2]

### Instructions[cite: 2]

1. Read the three-stage comparison table below.[cite: 2]
2. Identify which stage describes your current use of AI.[cite: 2]
3. Note which stage represents where the technology is heading.[cite: 2]
4. Use Stage 1 for simple drafting. Use Stage 2 for multi-step workflows that need live data.[cite: 2]
5. Keep this spectrum in mind when you set expectations for any AI task.[cite: 2]

### Key Concepts[cite: 2]

| Stage 1: AI Assistant | Stage 2: AI Agent | Stage 3: Agentic AI System |[cite: 2]
|---|---|---|[cite: 2]
| **What it does** | Follows rules. Automates simple tasks. Requires you to provide all context. | Achieves goals. Handles multi-step workflows. Pulls live data from connected systems. | Fully autonomous. Multiple specialized agents work together and consolidate results. |[cite: 2]
| **Human Involvement** | You provide all the data and context. | You provide a goal and system access. | You provide the goal. The system handles the rest. |[cite: 2]
| **What this looks like** | Paste a meeting transcript into Claude. Ask it to summarize. It does exactly that and stops. | Ask an agent to review a folder of 40 résumés against a job description and rank the top candidates. It reads each file, compares them, and returns a ranked list. | A coordinating agent receives one request, delegates to separate résumé-screening, calendar-scheduling, and email-drafting agents, then delivers one consolidated hiring update. |[cite: 2]

<!-- INFO: Where the Tools Are Today | Stage 1 and Stage 2 are widely available in consumer and professional AI tools right now. Agents that connect to live systems are Stage 2. Stage 3 multi-agent systems are still early and emerging. -->[cite: 2]

<!-- TIP: Match the Tool to the Task | Use Stage 1 for simple drafting tasks. Use Stage 2 when you need live data from a connected system. Do not build a complex agent for a task you could accomplish with a single clear prompt. -->[cite: 2]

---[cite: 2]

<!-- ANCHOR: anchor-step-4 -->[cite: 2]

## Step 4: How Agents Actually Work[cite: 2]

When you send a message to an AI agent, more happens than you see. The agent reasons, selects tools, queries live systems, and loops back to check its own work before returning an answer. This loop is what makes agents powerful.[cite: 2]

### What You'll Do[cite: 2]

You will trace the seven-step agentic loop and understand what happens between your question and the agent's answer.[cite: 2]

### Instructions[cite: 2]

1. Read the seven steps below in order.[cite: 2]
2. Note that Steps 3 through 6 can repeat. The agent loops until it has enough information to answer.[cite: 2]
3. Recognize that you see only the final answer unless you ask the agent to show its reasoning.[cite: 2]
4. Use this understanding to debug wrong answers. A wrong answer usually breaks at Step 4 (wrong tool selected) or Step 6 (bad data returned from the system).[cite: 2]

### The Agentic Loop[cite: 2]

1. **You type a prompt.** "Which candidates in this folder have been in 'Interview Scheduled' status for more than 10 days?"[cite: 2]
2. **The agent receives your prompt.** It reads your request and its own standing instructions.[cite: 2]
3. **The agent invokes the model.** The AI decides what to do next. It reasons: "I need to search a connected system for candidates by status and start date."[cite: 2]
4. **The model selects a tool.** It picks the right source (an applicant tracking system or a local spreadsheet) and constructs the right query.[cite: 2]
5. **The tool executes.** The connected system runs the query against live data and returns results.[cite: 2]
6. **The agent reasons about the results.** It loops back if it needs more data or a different tool.[cite: 2]
7. **The agent returns the final response.** You get a consolidated, readable answer.[cite: 2]

![The agentic loop: a prompt flows through the model, to a tool, back to the model, and returns a final answer to the user](../assets/1-1_agentic_loop.png)[cite: 2]

<!-- NOTE: The Loop Can Repeat | Steps 3 through 6 can run multiple times in one conversation. The agent might query one system, then check another, then cross-reference a Knowledge Base before returning its answer. -->[cite: 2]

<!-- EXPAND: Troubleshooting - What If the Agent Gives a Wrong Answer? -->[cite: 2]

**Problem:** The agent returns outdated or incorrect data.[cite: 2]
**Cause:** The MCP server returned stale data, or the agent selected the wrong tool.[cite: 2]
**Fix:** Ask the agent to explain its reasoning. Say: "Walk me through how you got that answer." This surfaces which tool it used and what data it received.[cite: 2]

---[cite: 2]

**Problem:** The agent says it cannot answer your question.[cite: 2]
**Cause:** The required connection is not enabled on that agent, or your account does not have permission to access that system.[cite: 2]
**Fix:** Open your AI tool's settings and confirm the relevant connection is turned on. If it is on and the error persists, the permissions issue is in your connected app or system, not in the AI tool.[cite: 2]

<!-- /EXPAND -->[cite: 2]

---[cite: 2]

<!-- ANCHOR: anchor-step-5 -->[cite: 2]

## Step 5: What This Means for Your Work[cite: 2]

Understanding how AI works changes how you use it. Three principles separate effective AI users from frustrated ones. The goal is not to learn AI theory. The goal is to apply these principles every time you open Claude.[cite: 2]

### What You'll Do[cite: 2]

You will review three practical principles and compare a vague prompt to a specific one. Then you will commit to one real task you will try with Claude this week.[cite: 2]

### Instructions[cite: 2]

1. Read the three principles below.[cite: 2]
2. Compare the Before and After prompt examples.[cite: 2]
3. Notice the difference in what each prompt would return.[cite: 2]
4. Choose one task you repeat each week.[cite: 2]
5. Apply Principle 2 (specificity) to write a better prompt for that task today.[cite: 2]

<!-- INFO: The Three Principles | 1. You are the pilot, not the passenger. The AI executes. You direct, validate, and decide. 2. Specificity wins. Named fields, date ranges, and sort order produce usable results. 3. AI accelerates judgment. It does not replace it. You own the decision. -->[cite: 2]

<!-- TIP: Start With One Real Task | Open Claude today and use the specific prompt format above on something you actually need. The difference in output quality will be immediate. Iterate from there. -->[cite: 2]

---[cite: 2]

<!-- ANCHOR: anchor-verification -->[cite: 2]

## Verification[cite: 2]

You have completed all five steps. Confirm your understanding by checking each item below:[cite: 3]

- [ ] You can explain what a context window is without using technical jargon[cite: 3]
- [ ] You can name the four most important AI terms for daily work (Prompt, Context window, Agent, MCP Server)[cite: 3]

<!-- NOTE: Not Working? | If any check feels unclear, revisit the step where that concept appeared. The Key Concepts tables in Steps 1 and 2 are your primary reference. -->[cite: 3]

---[cite: 3]

<!-- CELEBRATION: Lesson Complete! | You now understand what AI models are, how agents take action using live data, and how to apply that knowledge to get better results at work. -->[cite: 3]

### What's Next[cite: 3]

**Next Lesson:** [Lesson 1.2: Prompt Engineering vs. Context Engineering](1-2_Prompt_Engineering_vs_Context_Engineering.md)[cite: 3]

**Related Resources:**[cite: 3]
- [claude.ai](https://claude.ai) - The Claude AI platform[cite: 3]
- [Claude documentation](https://code.claude.com/docs) - Official documentation[cite: 3]
- [Claude support](https://support.claude.com) - Help center and troubleshooting[cite: 3]

<!-- TIP: Practice Today | Open Claude now and use the specific prompt format from Step 5 on a real task. The faster you apply this to actual work, the faster your skills develop. -->[cite: 3]

<!-- CHILDREN -->[cite: 3]