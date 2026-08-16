# Model Selection Notes

Last updated: 2026-08-16

These are practical working notes for choosing between GPT-5.4 mini, GPT-5.4, GPT-5.5, and the GPT-5.6 family: Luna, Terra, and Sol.

Sources:

- [OpenAI model catalog](https://developers.openai.com/api/docs/models)
- [OpenAI latest model guidance](https://developers.openai.com/api/docs/guides/latest-model)
- [GPT-5.4 mini model page](https://developers.openai.com/api/docs/models/gpt-5.4-mini)
- [GPT-5.4 model page](https://developers.openai.com/api/docs/models/gpt-5.4)
- [GPT-5.5 model page](https://developers.openai.com/api/docs/models/gpt-5.5)
- [GPT-5.6 Luna model page](https://developers.openai.com/api/docs/models/gpt-5.6-luna)
- [GPT-5.6 Terra model page](https://developers.openai.com/api/docs/models/gpt-5.6-terra)
- [GPT-5.6 Sol model page](https://developers.openai.com/api/docs/models/gpt-5.6-sol)

## Short Version

- Use `GPT-5.6 Sol` when quality matters most.
- Use `GPT-5.6 Terra` as the best balanced default for serious work.
- Use `GPT-5.6 Luna` for cheaper, faster, high-volume work.
- Use `GPT-5.5` when you want a strong previous frontier model or need compatibility with existing 5.5 behavior.
- Use `GPT-5.4` when you want capable professional work at lower cost than 5.5/Sol.
- Use `GPT-5.4 mini` for well-scoped coding, subagents, repeated tasks, and cost-sensitive workflows.

## Quick Decision By Task

| Task | Recommended Model | Effort | Why |
| --- | --- | --- | --- |
| Casual brainstorming, not code-related | `GPT-5.6 Terra` | `medium` | Best balance for useful ideas, structure, and judgment without overpaying for Sol. |
| Deep brainstorming, strategy, or important life/project decisions | `GPT-5.6 Sol` | `high` | Better for ambiguity, tradeoffs, critique, and seeing around corners. |
| Fast idea generation where quality is not critical | `GPT-5.6 Luna` | `low` | Cheap and fast for many rough ideas, names, lists, variations, and first drafts. |
| Writing, rewriting, tone, portfolio text, blog text | `GPT-5.6 Terra` | `medium` | Strong default for quality writing, structure, and voice. |
| Important final writing or sensitive messaging | `GPT-5.6 Sol` | `high` | Better when nuance, precision, and judgment matter more than speed. |
| Simple app prototype | `GPT-5.6 Terra` | `medium` | Good balance for implementation, product sense, and not making the code weird. |
| Very simple app or tiny UI change | `GPT-5.6 Luna` | `low` | Good enough when the task is narrow and clearly described. |
| Frontend design, layout, visual hierarchy | `GPT-5.6 Sol` | `high` | Official guidance says GPT-5.6 improves frontend aesthetics; use Sol when design quality matters. |
| Normal coding help | `GPT-5.6 Terra` | `medium` | Best everyday coding default. |
| Small, clear code edit | `GPT-5.6 Luna` or `GPT-5.4 mini` | `low` | Use cheaper/faster models when the edit is obvious and low-risk. |
| Hard debugging | `GPT-5.6 Sol` | `high` or `xhigh` | Debugging needs deeper reasoning and careful hypothesis testing. |
| Code review | `GPT-5.6 Terra` | `high` | Good default for finding issues without always using Sol. Use Sol for important or complex reviews. |
| Architecture or multi-file refactor planning | `GPT-5.6 Sol` | `high` | Better for system-level consequences, hidden dependencies, and long-term structure. |
| Data science notebook work | `GPT-5.6 Terra` | `medium` | Strong default for analysis, transformations, modeling, plots, and interpretation. |
| Hard data reasoning or model interpretation | `GPT-5.6 Sol` | `high` or `xhigh` | Use when the conclusion matters or the analysis has many traps. |
| Summaries, extraction, cleanup, formatting | `GPT-5.6 Luna` | `none` or `low` | Keep cheap tasks cheap. |
| Subagents or helper agents | `GPT-5.4 mini` or `GPT-5.6 Luna` | `low` | Good for narrow inspection, summarization, and repetitive support work. |
| Final answer after lots of work | `GPT-5.6 Terra` or `GPT-5.6 Sol` | `medium` or `high` | Use Terra for normal final summaries and Sol when quality or nuance matters. |

## Quick Defaults For Me

- Brainstorming: start with `GPT-5.6 Terra`, `effort = medium`.
- Brainstorming where the direction really matters: use `GPT-5.6 Sol`, `effort = high`.
- Simple apps: use `GPT-5.6 Terra`, `effort = medium`.
- Tiny app edits: use `GPT-5.6 Luna`, `effort = low`.
- Normal code: use `GPT-5.6 Terra`, `effort = medium`.
- Hard code/debugging/architecture: use `GPT-5.6 Sol`, `effort = high`.
- Cheap helper work: use `GPT-5.6 Luna` or `GPT-5.4 mini`, `effort = low`.

## Cost Overview

Prices below are from official OpenAI model pages, checked on 2026-08-16. Treat them as working notes and re-check official pricing before making product or budget decisions.

| Model | Input / 1M tokens | Cached Input / 1M tokens | Output / 1M tokens | Cost Position |
| --- | --- | --- | --- | --- |
| `GPT-5.4 mini` | `$0.75` | `$0.075` | `$4.50` | Cheapest listed option here |
| `GPT-5.6 Luna` | `$1.00` | `$0.10` | `$6.00` | Cheap 5.6-family option |
| `GPT-5.4` | `$2.50` | `$0.25` | `$15.00` | Mid-tier |
| `GPT-5.6 Terra` | `$2.50` | `$0.25` | `$15.00` | Mid-tier and usually best balanced default |
| `GPT-5.5` | `$5.00` | `$0.50` | `$30.00` | Expensive frontier tier |
| `GPT-5.6 Sol` | `$5.00` | `$0.50` | `$30.00` | Expensive frontier tier |

Practical cost notes:

- Output tokens are much more expensive than input tokens, so long answers cost more than long prompts.
- Higher effort can increase reasoning tokens, latency, and cost, so do not use `high`, `xhigh`, or `max` by default.
- For many small helper tasks, use `GPT-5.4 mini` or `GPT-5.6 Luna`.
- For normal work, `GPT-5.6 Terra` often gives the best quality/cost balance.
- For hard work, paying for `GPT-5.6 Sol` can be cheaper overall if it avoids wasted time, bad code, or repeated attempts.
- For high-volume workflows, test the cheapest model that passes quality checks instead of guessing.
- For prompts above 272K input tokens, some model pages mention higher pricing for the full request, so long-context jobs need extra cost attention.

## Model Overview

| Model | Practical Role | Best For | Avoid When |
| --- | --- | --- | --- |
| `GPT-5.4 mini` | Efficient mini model | Well-scoped code edits, subagents, repeated notebook/script tasks, formatting, simple refactors, cheap exploration | The task needs deep architecture, vague product judgment, hard debugging, or high-stakes reasoning |
| `GPT-5.4` | Older capable frontier model | Solid coding, analysis, professional writing, general implementation when cost matters | You want the best current quality or 5.6-specific efficiency |
| `GPT-5.5` | Strong previous frontier model | Complex coding and professional work, stable 5.5-era behavior, migration baseline before 5.6 | You can use 5.6 Sol/Terra and want newer quality/cost tradeoffs |
| `GPT-5.6 Luna` | Low-cost 5.6 family model | High-volume tasks, simple transformations, drafts, summaries, straightforward code edits, batch-like work | You need nuanced judgment, difficult debugging, or complex planning |
| `GPT-5.6 Terra` | Balanced 5.6 model | Default choice for most real work: coding, data analysis, moderate design decisions, review, refactoring, planning | Quality matters more than cost and the task is genuinely hard |
| `GPT-5.6 Sol` | Flagship 5.6 model | Hard reasoning, complex architecture, difficult bugs, strategic design, high-quality writing, important final answers | The task is simple, repetitive, cost-sensitive, or latency-sensitive |

## GPT-5.4 Mini

GPT-5.4 mini is a strong mini-tier model for coding, computer use, and subagent-style work. Use it when the task is clear, bounded, and benefits from speed or lower cost.

Good uses:

- Formatting and style cleanup.
- Small code edits where the desired outcome is obvious.
- Repetitive data-cleaning steps.
- Subagents that inspect files, summarize sections, or check narrow assumptions.
- Drafting first-pass notes that a stronger model can later refine.

Use more capable models when the task is ambiguous, involves many tradeoffs, or requires deep debugging.

## GPT-5.4

GPT-5.4 is a capable professional-work model and a reasonable lower-cost option compared with GPT-5.5 or GPT-5.6 Sol. It is useful when you want strong general work but do not need the newest model family.

Good uses:

- Normal coding tasks.
- Data analysis and notebook help.
- Refactoring with clear boundaries.
- Professional writing and structured explanations.
- Workflows where GPT-5.4 behavior is already tested and stable.

Use newer 5.6 models when visual/design judgment, coding quality, token efficiency, or current model-family behavior matters.

## GPT-5.5

GPT-5.5 is a strong frontier model for complex professional work. It is a good choice when you need high capability but are not ready to move the workflow to GPT-5.6.

Good uses:

- Complex coding and debugging.
- Professional writing and analysis.
- Existing workflows already tuned around GPT-5.5.
- Migration baseline before comparing against GPT-5.6 Terra or Sol.

If starting fresh, prefer GPT-5.6 Terra or Sol unless there is a reason to stay on 5.5.

## GPT-5.6 Luna

GPT-5.6 Luna is the cost-sensitive/high-volume model in the 5.6 family. Think of it as the model to use when you want 5.6-family behavior but the work is simple enough that flagship quality is unnecessary.

Good uses:

- Cheap high-volume processing.
- Straightforward summaries.
- Simple classification or labeling.
- Draft generation.
- Narrow code edits with clear instructions.
- Repeated low-risk helper tasks.

Use Terra or Sol when mistakes are expensive or the task requires judgment.

## GPT-5.6 Terra

GPT-5.6 Terra balances intelligence and cost. This should usually be the default 5.6-family choice when the task is real but not extreme.

Good uses:

- Most coding help.
- Data science notebooks and pipelines.
- Code review and refactoring.
- Product planning where cost still matters.
- Structured writing and project documentation.
- Multi-step work where Luna may be too shallow and Sol may be overkill.

Use Sol when quality is more important than cost, especially for hard debugging, architecture, or final decisions.

## GPT-5.6 Sol

GPT-5.6 Sol is the flagship/frontier model in the GPT-5.6 family. The `gpt-5.6` alias routes to Sol in the official model guidance, so treat unsuffixed 5.6 as the highest-capability 5.6 option.

Good uses:

- Difficult debugging.
- Architecture and system design.
- Important refactors.
- Complex multi-file changes.
- Strategic product decisions.
- High-quality final writing.
- Anything where a wrong answer would waste a lot of time.

Use Terra or Luna when the task is simple, repetitive, or cost-sensitive.

## Reasoning Effort

The `reasoning.effort` setting controls how much reasoning work the model is allowed to spend before answering. Higher effort can improve quality on difficult reasoning tasks, but usually costs more tokens and latency.

For GPT-5.6, official guidance lists these effort levels:

- `none`
- `low`
- `medium`
- `high`
- `xhigh`
- `max`

Practical usage:

- Use `none` for very simple responses, pure formatting, direct extraction, and latency-first tasks.
- Use `low` for simple coding, summaries, and cheap helper tasks where a little reasoning helps.
- Use `medium` as the normal default for balanced quality, cost, and speed.
- Use `high` for debugging, planning, refactoring, careful analysis, and tasks with several constraints.
- Use `xhigh` for hard technical work, architecture, difficult data reasoning, or when first attempts fail.
- Use `max` only for the hardest quality-first tasks where latency and cost are acceptable.

## Effort By Model

| Model | Good Starting Effort | Notes |
| --- | --- | --- |
| `GPT-5.4 mini` | `none` or `low` | Official model page says `none` is the default. Increase to `medium` or `high` only when the mini model needs more reasoning. |
| `GPT-5.4` | `low` or `medium` | Official model page says `none` is supported and is the default. Use `medium` when the task is real analysis or coding. |
| `GPT-5.5` | `medium` | Official model page lists `medium` as the default. Use `high` or `xhigh` for harder professional work. |
| `GPT-5.6 Luna` | `none` or `low` | Keep it cheap and fast. If you need `high`, consider Terra instead. |
| `GPT-5.6 Terra` | `medium` | Best default for most practical work. Move to `high` for deeper reasoning. |
| `GPT-5.6 Sol` | `medium` or `high` | Use `high`, `xhigh`, or `max` when quality matters more than speed/cost. |

## My Practical Defaults

Use these defaults unless the task says otherwise:

- Quick text or simple formatting: `GPT-5.6 Luna`, `effort = none`
- Small clear code edit: `GPT-5.6 Luna` or `GPT-5.4 mini`, `effort = low`
- Normal project work: `GPT-5.6 Terra`, `effort = medium`
- Data science notebook work: `GPT-5.6 Terra`, `effort = medium`
- Debugging or code review: `GPT-5.6 Terra`, `effort = high`
- Hard architecture or important decisions: `GPT-5.6 Sol`, `effort = high` or `xhigh`
- Very hard quality-first work: `GPT-5.6 Sol`, `effort = max`

## Migration Notes

When moving a workflow from GPT-5.4 or GPT-5.5 to GPT-5.6:

- Start with the same effort setting you already use.
- Test one effort level lower because GPT-5.6 may keep quality with fewer reasoning tokens.
- Compare output quality, latency, and cost on real tasks, not vibes.
- If `none` was used as the old latency baseline, keep it as a baseline and also test `low`.
- Do not use Sol for everything just because it is strongest. Use it when the task benefits from it.

## Simple Decision Tree

- Is the task hard, important, or ambiguous? Use `GPT-5.6 Sol`.
- Is it normal serious project work? Use `GPT-5.6 Terra`.
- Is it simple and high-volume? Use `GPT-5.6 Luna`.
- Is it a narrow helper/subagent task? Use `GPT-5.4 mini` or `GPT-5.6 Luna`.
- Is it an existing 5.5 workflow? Keep `GPT-5.5` until you compare it with 5.6.
- Is cost more important than best quality? Prefer Luna, mini, or Terra before Sol.
