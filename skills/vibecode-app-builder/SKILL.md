---
name: vibecode-app-builder
description: Use when collaboratively building or evolving an app from natural-language product ideas, especially when the user wants Codex to implement directly while maintaining product notes, app docs, readable code, decision checkpoints, prompts, access-mode rules, and periodic cleanup.
---

# Vibecode App Builder

Use this skill to build apps in a collaborative "vibecode" style: the user describes intent, Codex implements, documents durable decisions, and keeps the code understandable for a user who may later edit it directly.

## Workflow

1. Listen for the product intent first, then inspect the local project structure before editing.
2. Implement small and medium changes directly when the direction is clear.
3. Ask before bigger product, architecture, data-storage, authentication, deployment, billing, or AI-behavior decisions.
4. Ask when access-mode placement is unclear, such as whether a feature belongs in demo mode, full/private mode, or both.
5. When a prototype or app entry file starts collecting multiple responsibilities, do a small structure pass before adding more features. Keep entry files as shells and move auth, data, AI, styling, and view logic into focused modules or folders.
6. Summarize important changes with links to the files that matter.

## Project Memory

Maintain lightweight project memory when the project has or should have these folders:

- `notes/` for durable product decisions, requirements, architecture choices, auth rules, data behavior, AI behavior, and portability decisions.
- `docs/` for practical app instructions, such as how to run the app and how the app works.
- `prompts/` for editable AI-agent or assistant prompts, kept separate from application code.
- App source folders should stay organized by responsibility. For example, keep configuration, auth, data sources, AI/agent logic, styling, and view/page sections in separate files once the app grows beyond a tiny prototype.

Do not record purely visual one-off tweaks in product notes unless they express a durable design principle or affect product behavior.

## Code Style

Keep code easy for the user to inspect and edit later.

- Prefer clear names, small files, straightforward functions, and boring structure.
- Keep app entry files small. They should mostly configure the page, call top-level views, and avoid holding large data definitions or feature logic.
- Split UI sections into view/page modules when it helps the user find and edit one part of the app without reading unrelated code.
- Add helpful comments that explain what important parts do and why they exist.
- Keep comments balanced: enough to orient the user, but not line-by-line noise.
- Prefer single-line text, strings, comments, and list items when they fit comfortably and express one idea.
- Use multiline formatting when a line is genuinely too long, separate lines express separate meanings, or the syntax is clearer that way.
- For Python code, organize larger files with clear section dividers:

```python
# ----------------------------------------------------------
# Section Title / Short Summary
# ----------------------------------------------------------
```

- For Python functions, prefer short comments above the function explaining what it does, the main steps, and what it returns.
- Use common sense with spacing around function comments: put a single-line helper comment directly above the function, and use a blank line after a multi-line description block only when it improves readability.
- Add blank lines inside functions only when they separate meaningful steps; keep tiny helpers compact.
- Do not use docstring blocks for these casual function explanations unless a real public API docstring is useful.
- Inside Python functions, add short comments for important logic blocks, such as `# Calculate aggregates across years`.

## Cleanup Habit

From time to time, do a small cleanup pass before mess accumulates.

- Remove temporary prototypes once the direction is clear.
- Move repeated behavior into simple helpers when it improves readability.
- Keep generated files, logs, virtual environments, build outputs, and secrets out of source control.
- Refactor opportunistically after a feature proves useful: move repeated or oversized blocks into focused modules before the next layer of features lands.
- Preserve user work and avoid unrelated refactors.

## AI And Auth

For apps with AI chat, coaching, agents, or personal data:

- Keep prompts editable and separate from app code.
- Do not expose API keys or secrets in browser/client code.
- Do not pretend responses are personalized before real context is connected.
- Prefer a safe default mode when identity is unknown.
- For owner/public apps, keep the same general app structure and unlock private data/actions only for authorized users.

## User Collaboration

The user may not want to read every code change. Codex should still keep them oriented.

- Treat requests about direction, design, prompts, card libraries, coaching tone, UX behavior, architecture, or "how should this work" as conversation-first unless the user clearly asks to edit files.
- Before changing code for ambiguous or strategic requests, pause and summarize the goal, the likely files or components affected, and the concrete edit plan.
- Ask for explicit permission before implementation when the request sounds like discussion, exploration, or product thinking, for example: "Should I start making these changes now?"
- Once the user confirms or gives a clear implementation command, proceed decisively without asking again for every small follow-up.
- Do not use this pause for narrow, unambiguous edits where the user clearly asked to change code.
- Explain the important pieces after implementing.
- Point to the files the user is most likely to edit later.
- Offer a short code walkthrough when the project structure changes.
- Keep momentum, but slow down and ask when the decision would shape the product long-term.
