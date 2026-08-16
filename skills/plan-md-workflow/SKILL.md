---
name: plan-md-workflow
description: Use when the user is brainstorming ideas, listing many things they want to do, shaping a feature or project direction, asking for a plan, roadmap, TODO structure, staged implementation plan, or wants Codex to maintain a temporary PLAN.md while discussion and work evolve.
---

# PLAN.md Workflow

Use this skill to turn open-ended user ideas into a temporary working `PLAN.md` that keeps the conversation grounded, critical, and easy to continue.

## Core Behavior

- Treat the user's ideas as direction and raw material, not as a finished plan.
- Constructively review, evaluate, reorder, and adjust the ideas before writing them down.
- Act like an experienced colleague: preserve the user's goal, improve the path, surface risks, and suggest better alternatives when useful.
- Keep the plan practical and editable, not over-engineered.
- Use `PLAN.md` as a temporary working file unless the user asks for a permanent project plan.

## When To Create PLAN.md

Create or propose a `PLAN.md` when the user:

- Brainstorms several ideas, features, tasks, or possible directions.
- Enumerates what they want to do and the work would benefit from structure.
- Talks through product design, data analysis direction, architecture, writing structure, prompts, UX, refactors, or multi-step implementation.
- Says something like "let's plan", "make a plan", "we need to organize this", "I want to do these things", or "keep track of this".
- Starts moving through a multi-step plan where decisions and progress should stay visible.

Do not create `PLAN.md` for a tiny one-step edit, a simple question, or a task where a short answer is enough.

## Placement

- Put `PLAN.md` in the smallest correct project folder that owns the work.
- If the user names a subproject, feature folder, notebook folder, app folder, or package, place `PLAN.md` there.
- If the plan spans the whole repository, place `PLAN.md` at the repository root.
- If the plan spans multiple separate projects, ask before choosing one location.
- If the correct folder is unclear, inspect the project structure first and choose the most specific reasonable location, or ask one sharp question if the choice has consequences.
- Before creating a new `PLAN.md`, check whether one already exists in the target folder. If it exists, read it and update it instead of overwriting it blindly.

## PLAN.md Structure

Use a clean structure like this, adapted to the project:

```markdown
# Plan

## Goal
One clear paragraph describing what we are trying to achieve.

## Current Understanding
- What the user wants.
- What is already known from the project.
- Important assumptions.

## Critical Review
- What seems strong.
- What may be risky, unclear, too broad, or unnecessary.
- Adjustments Codex recommends.

## Proposed Direction
- The refined approach.
- Why this path is better than obvious alternatives.

## Tasks
- [ ] Concrete task
- [ ] Concrete task
- [ ] Concrete task

## Decisions
- Decision already made and why.

## Open Questions
- Question that still blocks or shapes the work.

## Progress
- What has been completed or changed so far.
```

Keep the structure lighter for small plans and more detailed for large plans.

## Writing Style

- Write clearly and directly, with short sections and practical bullets.
- Keep one idea on one line when it fits comfortably.
- Prefer useful judgment over neutral transcription.
- Keep the user's language and intent recognizable, but make the plan cleaner than the raw conversation.
- Separate user goals from Codex recommendations when that distinction matters.
- Mark uncertain items as assumptions or open questions.
- Avoid making the plan sound final when the direction is still being shaped.

## Updating PLAN.md

- Update `PLAN.md` as the conversation evolves, especially when goals, decisions, scope, priorities, or completed tasks change.
- Do not update the file after every minor sentence; update it after meaningful decisions or progress.
- When a task is completed, check it off or move it into `Progress`.
- When the user changes direction, preserve the relevant history briefly, but keep the active plan focused.
- If the plan becomes stale or too long, do a cleanup pass so it remains useful.
- If implementation starts from the plan, keep `PLAN.md` aligned with what actually happened.

## End Of Plan

- When the plan appears complete, tell the user what is done and what, if anything, remains.
- Ask whether to delete the temporary `PLAN.md`, keep it as project memory, or convert it into durable documentation.
- Do not delete `PLAN.md` without explicit permission unless the user already gave that instruction.
- If deleting it, mention that it was deleted.
- If keeping it, make sure the final state is clean and not misleading.

## Guardrails

- Do not use `PLAN.md` as a way to avoid acting when the user gave a clear implementation request.
- Do not treat every casual thought as a planning task.
- Do not overwrite an existing long-term plan with a temporary conversation plan.
- Do not hide disagreements: if the user's idea seems weak, risky, or unnecessarily complex, say so constructively and reflect the better path in the plan.
- Keep the plan synchronized with reality, not just with the original conversation.
