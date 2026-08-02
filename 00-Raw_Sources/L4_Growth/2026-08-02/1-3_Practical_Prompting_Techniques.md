<!-- HERO: Lesson 1.3: Practical Prompting Techniques | Build your daily AI toolkit - four core techniques, one structured framework, and the validation habits that keep your outputs trustworthy. -->[cite: 1]

<!-- TOC: Overview#anchor-overview | Step 1: Four Core Techniques#anchor-step-1 | Step 2: The COSTARS Framework#anchor-step-2 | Step 3: Interview-Style Prompting#anchor-step-3 | Step 4: Responsible Validation Habits#anchor-step-4 | Step 5: Your Action Plan#anchor-step-5 | Verification#anchor-verification -->[cite: 1]

## Overview[cite: 1]

This lesson gives you four techniques you will use every day, a structured framework for complex prompts, a method for exploratory tasks, and six habits that keep every AI output trustworthy. By the end, you will run two production-ready prompts tailored to your own role.[cite: 1]

### Why This Matters[cite: 1]

Knowing that AI exists is not enough. Knowing how to direct it is the skill. Every technique in this lesson was selected because it solves a real problem you will encounter this week. You will leave with copy-paste prompts you can use today.[cite: 1]

### Prerequisites[cite: 1]

- [Lesson 1.1: How AI Models Work](1-1_How_AI_Models_Work.md)[cite: 1]
- [Lesson 1.2: Prompt Engineering vs. Context Engineering](1-2_Prompt_Engineering_vs_Context_Engineering.md)[cite: 1]

### Time to Complete[cite: 1]

**20 minutes**[cite: 1]

<!-- PROGRESS: Step 1: Four Core Techniques | Step 2: The COSTARS Framework | Step 3: Interview-Style Prompting | Step 4: Responsible Validation Habits | Step 5: Your Action Plan | Verification -->[cite: 1]

---[cite: 1]

<!-- ANCHOR: anchor-overview -->[cite: 1]
<!-- ANCHOR: anchor-step-1 -->[cite: 1]

## Step 1: Four Core Prompting Techniques[cite: 1]

Four techniques cover 90% of what you will do with Claude. Each one solves a different problem. Knowing when to reach for each one is the skill this step builds.[cite: 1]

### What You'll Do[cite: 1]

You will learn each technique, see a concrete example for your role, and identify which one applies to a task you will run this week.[cite: 1]

### Instructions[cite: 1]

1. Read the summary table. Focus on the "When to Use" column.[cite: 1]
2. Read the Few-Shot example for your closest role (HR or Legal).[cite: 1]
3. Read the Role Prompting examples. Find the one that matches your job title.[cite: 1]
4. Review the Chain-of-Thought and Meta Prompting examples in the expand sections.[cite: 1]
5. Identify which technique you will use first this week.[cite: 1]

### Key Concepts[cite: 1]

| Technique | What It Is | When to Use It |[cite: 1]
|---|---|---|[cite: 1]
| **Few-Shot Prompting** | Show the AI 1-3 examples of correct input/output. It mimics the pattern. | Data extraction, formatting transformations, classification. Any time you need consistent output structure. |[cite: 1]
| **Role Prompting** | Assign the AI a specific role. This shapes tone, vocabulary, depth, and priorities. | Any time you need domain expertise, a specific communication style, or audience-appropriate language. |[cite: 1]
| **Chain-of-Thought** | Ask the AI to reason step by step before giving a final answer. | Complex analysis, multi-factor decisions. Anything with safety or quality implications. |[cite: 1]
| **Meta Prompting** | Ask the AI to write the prompt for you. | When you know what you want but not how to ask for it. When you are new to AI. |[cite: 1]

### Few-Shot Example (HR)[cite: 1]

```text
I need you to extract candidate information from interview notes.

Example Input:
"Spoke with Maria on Tuesday. She has 8 years in operations management. Strong communication. Wants $145K. Available in 2 weeks."

Example Output:
| Field | Value |
|---|---|
| Name | Maria |
| Experience | 8 years, operations management |
| Strengths | Communication |
| Salary | $145K |
| Availability | 2 weeks |

Now process this input:
"Called James Friday. 12 years in supply chain, last 4 leading a logistics team. Looking for $160K range. Can start March 1. Great systems thinking."
``` [cite: 1]

<!-- EXPAND: Few-Shot Example - Legal (Contract Clause Risk Classification) -->[cite: 1]

```text
I need you to classify contract clauses by risk level.

Example Input:
"Either party may terminate this agreement for any reason with 15 days written notice."
Example Output:
HIGH RISK - Short termination-for-convenience window creates revenue instability. Action: Negotiate to 90 days and add an early-termination fee.

Example Input:
"This agreement renews automatically for successive one-year terms unless either party gives 60 days notice."
Example Output:
MEDIUM RISK - Auto-renewal is standard, and 60 days notice is reasonable. Action: Calendar the notice deadline; no redline needed.

Now classify this:
"The Provider's total liability under this agreement shall not exceed $10,000 in any circumstance, including gross negligence."
```[cite: 1]

<!-- /EXPAND -->[cite: 1]

<!-- EXPAND: Few-Shot Example - Industrial Engineering (Downtime Cause Classification) -->

```text
I need you to classify unplanned downtime events by root-cause category.

Example Input:
"Line 3 stopped for 45 min, changeover took longer than standard due to missing fixture."
Example Output:
SETUP/CHANGEOVER WASTE - Root cause: fixture not staged in advance. Action: pre-stage fixtures 15 minutes before scheduled changeover.

Example Input:
"Line 1 down 20 min, conveyor sensor misaligned again after last PM."
Example Output:
EQUIPMENT/MAINTENANCE - Root cause: sensor alignment not verified during preventive maintenance. Action: add alignment check to PM checklist.

Now classify this:
"Line 2 idle 30 min waiting on component delivery from receiving."
```

<!-- /EXPAND -->

### Role Prompting Examples by Title[cite: 1]

```text
HR:
"You are a senior recruiter with 10 years of experience hiring across technical and professional roles. You understand how to distinguish transferable skills from role-specific ones, and how to write inclusive, accurate job descriptions. Communicate in clear, candidate-friendly language."

Industrial Engineering:
"You are a senior industrial engineer with 10 years of experience in process optimization and Lean Six Sigma. You understand takt time, OEE, root-cause analysis, and the eight wastes. Communicate in precise, data-driven language appropriate for operations stakeholders."

Legal:
"You are a senior commercial contracts attorney with 12 years of experience. You understand indemnification, liability caps, termination rights, and auto-renewal terms. Flag risk precisely, quote the exact language at issue, and communicate in plain English for a business audience."
```[cite: 1]

```text
Marketing:
"You are a senior brand marketing manager with 10 years of experience across paid social, email, and content. You understand audience segmentation, campaign metrics, and consistent brand voice. Write concisely and persuasively for the target audience of each channel."
```[cite: 2]

<!-- EXPAND: Chain-of-Thought Examples -->[cite: 2]

**Legal - Escalate a Vendor Breach:**[cite: 2]

```text
You are a commercial contracts attorney.
I need to decide whether to formally escalate a vendor's breach of contract.

Think through this step by step:
1. The contract required delivery by August 15. The vendor delivered on September 10.
2. The delay cost us an estimated $40,000 in missed downstream commitments.
3. The contract includes a 30-day cure period and a liquidated damages clause of $500/day.
4. We rely on this vendor for two other active projects.

Based on these factors, recommend: send a formal notice of breach now, or open an informal resolution first? Show your reasoning.
```[cite: 2]

**Marketing - Allocate a Limited Ad Budget:**[cite: 2]

```text
I have a scheduling conflict. Two campaigns need the same limited ad budget this week, and I can fully fund only one.

Campaign A: Product launch, hard deadline Friday, tied to a press announcement that cannot move.
Campaign B: Seasonal promotion, hard deadline Sunday, historically our highest-revenue email of the quarter.

Think step by step:
Which campaign gets the budget?
What do I do with the other one?
What should I communicate to my director?
```[cite: 2]

<!-- /EXPAND -->[cite: 2]

<!-- EXPAND: Meta Prompting - Ask the AI to Write Your Prompt -->[cite: 2]

Use this formula when you know WHAT you want but not HOW to ask for it:[cite: 2]

```text
You are an expert at writing AI prompts.
I need a prompt that will [describe your goal].
The output should [describe format/structure].
The audience is [describe who will read it].
Write that prompt for me.
```[cite: 2]

**Example:**[cite: 2]

```text
You are an expert at writing AI prompts.
I need a prompt that will make an AI extract action items from meeting notes and format them as a checklist with owners and due dates.
The output should be a markdown table.
The audience is my team lead who needs a quick scan of commitments.
Write that prompt for me.
```[cite: 2]

The AI produces a better-structured prompt than most people write on their first attempt. Use this liberally. There is no penalty for asking the AI to help you talk to the AI.[cite: 2]

<!-- /EXPAND -->[cite: 2]

<!-- TIP: Combine Techniques for Best Results | Start every complex prompt with Role Prompting to set the foundation. Add Few-Shot examples for formatting. Add Chain-of-Thought for analysis. Stacking techniques produces the highest-quality outputs. -->[cite: 2]

---[cite: 2]

<!-- ANCHOR: anchor-step-2 -->[cite: 2]

## Step 2: The COSTARS Framework[cite: 2]

When a task is complex and multi-dimensional, a single sentence is not enough. COSTARS gives you a seven-component structure that eliminates guessing across every dimension of a prompt. It is the framework for your most important AI requests.[cite: 2]

### What You'll Do[cite: 2]

You will learn the seven COSTARS components, fill in a real prompt with your own role details, and run it in Claude to generate a personalized AI adoption roadmap.[cite: 2]

### Instructions[cite: 2]

1. Read the COSTARS component table. Memorize the seven letters.[cite: 2]
2. Copy the AI Launchpad Prompt below into Claude.[cite: 2]
3. Replace the two bracketed placeholders with your actual team and responsibilities.[cite: 2]
4. Submit the prompt and review your output. Are the time savings realistic? Are the first steps actionable?[cite: 2]
5. Save the output. You will use it again in Step 3.[cite: 2]

### Key Concepts[cite: 2]

| Letter | Component | What It Controls |[cite: 2]
|---|---|---|[cite: 2]
| **C** | Context | Background information: who you are, what the situation is, what has happened so far |[cite: 2]
| **O** | Objective | What you want the AI to accomplish. The specific task or goal. |[cite: 2]
| **S** | Style | How the output reads: professional, technical, conversational, or data-driven |[cite: 2]
| **T** | Tone | The emotional register: confident, empathetic, urgent, or neutral |[cite: 2]
| **A** | Audience | Who will read the output: your director, a new hire, an external client |[cite: 2]
| **R** | Response | What format you want: table, bullet points, email draft, numbered list |[cite: 2]
| **S** | Scope/Constraints | What the AI should NOT do: length limits, topics to avoid, assumptions to make |[cite: 2]

### The AI Launchpad Prompt (Copy and Fill In)[cite: 2]

```text
Context: I'm a member of the [team name] team focused on [key areas of your individual responsibility], and I'd like to identify specific ways AI can help reduce or eliminate mundane or repetitive tasks in my workflow, while keeping me in the strategic driver's seat as the validator and owner of all outputs.

Objective: You are a world-class AI transformation and process improvement consultant specialized in helping professionals across industries use AI as their thought partner. Identify 2-3 concrete opportunities where AI can amplify my capabilities while I maintain full strategic ownership.

Style: Professional and technical, backed by specific real-world industry examples and data points.

Tone: Confident and pragmatic, addressing both opportunities and implementation
```[cite: 2]

```text
challenges.

Audience: My manager and key stakeholders, who need to understand both the technical capabilities I will be leveraging, the practical ROI, and how I will maintain ownership and oversight of my work product.

Response: Provide a table with a prioritized list of concrete opportunities where AI can amplify my capabilities. For each opportunity, include:
1) What AI support looks like (inputs, outputs, my validation role)
2) How this changes my work and the estimated weekly time savings
3) A pro tip to avoid common pitfalls
4) An immediate recommended first step
5) What I would still own completely

Scope: Focus on my specific role. Do not recommend tools that require IT installation or admin access. Keep examples grounded in my day-to-day professional work.
```[cite: 3]

**Replace these two items before submitting:**[cite: 3]
- `[team name]` = e.g., "Marketing" or "Legal"[cite: 3]
- `[key areas of your individual responsibility]` = e.g., "managing brand campaigns across paid social channels" or "reviewing vendor contracts for compliance risk"[cite: 3]

<!-- TIP: This Is Your AI Launchpad | Every person in this training should run this prompt with their own role details. It produces a personalized AI adoption roadmap in under 2 minutes. Save the output and share it with your manager. -->[cite: 3]

<!-- NOTE: Use Only the Components That Apply | Context, Objective, and Response are the most critical. For simple tasks, skip Style, Tone, and Audience. For outputs that will reach your director or VP, include all seven. -->[cite: 3]

---[cite: 3]

<!-- ANCHOR: anchor-step-3 -->[cite: 3]

## Step 3: Interview-Style Prompting for Exploratory Tasks[cite: 3]

Sometimes you do not know exactly what you need. You have a vague goal but no clear path. Interview-style prompting flips the dynamic: instead of you crafting a perfect prompt, you ask the AI to interview you. The AI asks targeted questions, gathers context through conversation, and then produces a tailored output based on your answers.[cite: 3]

### What You'll Do[cite: 3]

You will run the full Interview-Style prompt in Claude, answer the AI's questions about your role and pain points, and receive a personalized output that often surfaces needs you had not fully articulated.[cite: 3]

### Instructions[cite: 3]

1. Copy the full prompt below into Claude.[cite: 3]
2. Replace "[YOUR ROLE AND TEAM]" with your actual role and team.[cite: 3]
3. Submit the prompt. The AI will ask you questions one at a time.[cite: 3]
4. Answer honestly. The more specific your answers, the better the final output.[cite: 3]
5. Compare your output to the AI Launchpad output from Step 2. Note what each approach surfaces that the other misses.[cite: 3]

### The Interview Prompt (Copy, Replace Role, and Submit)[cite: 3]

```text
You are an experienced AI transformation consultant who specializes in helping professionals across industries identify problems they can solve using AI. You have deep expertise in human-AI collaboration, process improvement, and understanding where AI adds massive value versus where human judgment remains critical. You are skilled at asking probing questions that help professionals uncover inefficiencies they might not have fully recognized.

I am a [YOUR ROLE AND TEAM] looking to identify specific ways AI can help reduce or eliminate mundane or repetitive tasks, while keeping me in the strategic driver's seat as the validator and owner of all outputs.

Please help me through an assessment by asking me targeted questions about my work:

Start by asking me up to three focused questions (one at a time) to clarify:
- My roles and responsibilities
- Specific challenges or pain points I experience in my daily work

Then ask up to three more focused questions (one at a time) to explore:
- Tasks that take longer than they should
- Repetitive work that could be automated
- Areas where I deal with information overload
- Strategic work I would do more of if I had time
- Places where I wish I had better insights
```[cite: 3]

```text
My goal: identify 2-3 concrete opportunities where AI could amplify my capabilities while I maintain full strategic ownership.

Once you have my answers, for each pain point I identify, produce a table with:
1) What AI support would look like (inputs, outputs, my validation role)
2) How this changes my work and estimated weekly time savings
3) A pro tip to avoid common pitfalls
4) An immediate recommended first step
5) What I would still own completely
```[cite: 3]

### COSTARS vs. Interview-Style: Which to Use[cite: 3]

| Dimension | COSTARS Prompt | Interview-Style Prompt |[cite: 3]
|---|---|---|[cite: 3]
| **User effort upfront** | High. You fill in all details yourself. | Low. The AI asks you the questions. |[cite: 3]
| **Speed to output** | Fast. One prompt, one response. | Slower. Multi-turn conversation (5-10 min). |[cite: 3]
| **Depth of output** | Good. Based on what you provided. | Excellent. The AI surfaces what you did not think to mention. |[cite: 3]
| **Best for** | Tasks where you know exactly what you need. | Exploratory tasks where you are still figuring out the problem. |[cite: 3]

<!-- INFO: Start Here If This Is Your First Session | Interview-Style prompting requires less upfront effort and produces more personalized results. Run this prompt before the COSTARS prompt if you are unsure what to ask for. Once you see the output, you can refine future prompts using COSTARS. -->[cite: 3]

<!-- TIP: Answer the AI's Questions Specifically | Vague answers produce vague output. When the AI asks about your pain points, name an actual task with an actual time cost: "I spend 3 hours every Friday manually compiling campaign results from three dashboards into a spreadsheet for my director." That level of specificity produces actionable recommendations. -->[cite: 3]

---[cite: 3]

<!-- ANCHOR: anchor-step-4 -->[cite: 3]

## Step 4: Responsible Validation Habits[cite: 3]

AI is a powerful tool. It is not infallible. AI systems generate confident-sounding text even when they are wrong. Every output requires human validation before it becomes a decision, a communication, or a deliverable. These six habits are not optional. They protect you, your team, and your stakeholders.[cite: 3]

### What You'll Do[cite: 3]

You will learn six validation habits, practice the self-critique technique on a real AI output, and internalize the boundary between what AI should and should not own.[cite: 4]

### Instructions[cite: 4]

1. Read the six habits in the table below. Focus on the "How to Apply" column.[cite: 4]
2. Read the self-critique example. Memorize the trigger phrase: "List 3 ways this could be wrong."[cite: 4]
3. Add the self-critique step to your routine: run it before you share any AI output with another person.[cite: 4]
4. Review the Safe vs. Human-Only table. Confirm you know where the line is for your role.[cite: 4]
5. Apply Habit 4 (Label Drafts) starting today. Never share AI output without a status label.[cite: 4]

### Key Concepts[cite: 4]

| Habit | What It Means | How to Apply It |[cite: 4]
|---|---|---|[cite: 4]
| **1. Source Check** | Where did this information come from? Can you verify it? | Ask yourself: "Can I trace this to your source system, a requirement doc, or verified data?" If not, treat it as unverified. |[cite: 4]
| **2. Plausibility Scan** | Does anything contradict what you already know? | Read the output with your domain expertise active. If a number, date, or claim seems off, investigate before accepting. |[cite: 4]
| **3. Self-Critique** | Make the AI challenge its own output. | After receiving a response, ask: "List 3 ways this could be wrong or incomplete." The AI identifies its own weak points. |[cite: 4]
| **4. Label Drafts** | Mark AI outputs with their status before sharing. | Always label outputs as "draft," "needs review," or "for brainstorming only." Never present AI output as final without human review. |[cite: 4]
| **5. Decompose Risky Tasks** | Break high-stakes work into safe sub-tasks. | Use Claude to summarize, reformat, or generate options. Keep humans in charge of conclusions and final communications. |[cite: 4]
| **6. Escalate Edge Cases** | Know when to stop and ask a human expert. | If you are unsure about compliance, legal, or reputational implications, ask your manager or your organization's AI/compliance lead. |[cite: 4]

### The Self-Critique Technique in Practice[cite: 4]

```text
(After receiving an AI-generated analysis)

You:
"List 3 ways this analysis could be wrong or incomplete."

Claude:
"1. I ranked candidates only on years of experience. Relevant skills and recent role
```[cite: 4]

```text
scope may matter more than raw tenure.
2. I assumed every résumé listed all relevant experience. Some candidates undersell prior roles, so I may have understated their fit.
3. I did not account for the job description's required certifications, which could disqualify a top-ranked candidate."
```[cite: 4]

### What AI Should and Should Not Own[cite: 4]

| Safe for AI | Keep Human-Only |[cite: 4]
|---|---|[cite: 4]
| Summarize meeting notes | Make hiring or firing decisions |[cite: 4]
| Draft emails (you review before sending) | Approve safety-critical procedures |[cite: 4]
| Format data into tables | Make legally binding representations |[cite: 4]
| Generate options for your consideration | Commit to deadlines on behalf of your team |[cite: 4]
| Extract action items from transcripts | Finalize brand or legal risk decisions |[cite: 4]
| Classify and prioritize items by criteria you define | Sign off on compliance determinations |[cite: 4]

<!-- WARNING: Partial Validation Is Not Validation | "It looks right" is not a validation method. Apply Source Check and Plausibility Scan to every AI output before sharing it. If something looks plausible but you cannot verify it, label it as unverified. -->[cite: 4]

<!-- TIP: The Self-Critique Takes 10 Seconds | Every time you plan to use AI output in a decision or communication, ask the AI to critique itself first. It catches errors that would otherwise reach your stakeholders. Make it a reflex, not an afterthought. -->[cite: 4]

---[cite: 4]

<!-- ANCHOR: anchor-step-5 -->[cite: 4]

## Step 5: Your Action Plan[cite: 4]

Techniques only become skills through practice. This step gives you a concrete three-day action plan and a decision guide that maps every situation to the right technique. By Friday, you will have run two real AI sessions and identified your highest-value AI opportunity.[cite: 4]

### What You'll Do[cite: 4]

You will review the technique selection guide, commit to a three-day action plan, and identify one recurring task you will use Claude for starting today.[cite: 4]

### Instructions[cite: 4]

1. Read the technique selection guide below. Find the row that matches a task you have this week.[cite: 4]
2. Copy the COSTARS prompt from Step 2, fill in your role, and run it today. Save the output.[cite: 4]
3. Copy the Interview-Style prompt from Step 3, run it tomorrow, and answer the AI's questions.[cite: 4]
4. By Friday: pick the single highest-value opportunity from either output. Spend 15 minutes using Claude for that task. Note what worked and what did not.[cite: 4]
5. Next week: share one finding with your team. What saved time? What would you do differently?[cite: 4]

### Technique Selection Guide[cite: 4]

| Situation | Use This | Why |[cite: 4]
|---|---|---|[cite: 4]
| You know what you want and the format is clear | Zero-Shot + COSTARS | Fast, one-shot execution with full coverage |[cite: 4]
| You need consistent formatting across multiple items | Few-Shot | Pattern matching eliminates variation |[cite: 4]
| You need domain expertise or a specific tone | Role Prompting | Sets vocabulary, depth, and priorities |[cite: 4]
| You are making a complex decision with multiple factors | Chain-of-Thought | Forces visible reasoning you can audit |[cite: 4]
| You are not sure what you need or how to ask | Interview-Style | AI gathers context through targeted questions |[cite: 4]
| You know the goal but cannot phrase the prompt | Meta Prompting | AI writes the prompt for you |[cite: 4]
| You need a comprehensive, multi-section output | COSTARS Framework | Covers all seven dimensions systematically |[cite: 4]

<!-- INFO: Context, Objective, and Response Are the Core Three | You do not need all seven COSTARS components every time. Simple tasks need only Objective and Response. Use Context, Audience, and Constraints when the task is complex, the output will be shared with others, or accuracy matters. -->[cite: 4]

<!-- TIP: Build Your Prompt Library | After you run both prompts this week, save the outputs and the prompts that generated them. Within one month, you will have a personal library of AI prompts covering your most common work. That library becomes your biggest productivity asset. -->[cite: 4]

---[cite: 4]

<!-- ANCHOR: anchor-verification -->[cite: 4]

## Verification[cite: 4]

You have completed all five steps. Confirm your understanding by checking each item below:[cite: 4]

- [ ] You can name all four core techniques and describe when to use each one[cite: 4]
- [ ] You can explain what each letter in COSTARS stands for[cite: 4]
- [ ] You can apply the self-critique technique and name at least three of the six validation habits[cite: 5]

<!-- NOTE: Not Working? | If any check feels unclear, revisit the step where that concept appeared. The Key Concepts tables in Steps 1 and 2 are your primary reference for techniques and the COSTARS framework. -->[cite: 5]

---[cite: 5]

<!-- CELEBRATION: Lesson Complete! | You now have four techniques, one structured framework, one exploratory method, and six validation habits - everything you need to use Claude effectively starting today. -->[cite: 5]

### What's Next[cite: 5]

**Next Lesson:** [Lesson 1.4: Choosing the Right AI Model](1-4_Choosing_AI_Model.md)[cite: 5]

**Related Resources:**[cite: 5]
- [claude.ai](https://claude.ai) - Run every prompt in this lesson[cite: 5]
- [Claude documentation](https://code.claude.com/docs) - Official product and feature documentation[cite: 5]
- [Claude support](https://support.claude.com) - Help center and account support[cite: 5]

<!-- TIP: Run Both Prompts Before Moving On | The COSTARS and Interview-Style prompts in this lesson are the two most valuable exercises in this curriculum. Complete both before starting Lesson 1.4. The outputs you generate will inform everything you build in the modules that follow. -->[cite: 5]

<!-- CHILDREN -->[cite: 5]