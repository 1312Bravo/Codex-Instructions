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
5. Summarize important changes with links to the files that matter.

## Project Memory

Maintain lightweight project memory when the project has or should have these folders:

- `notes/` for durable product decisions, requirements, architecture choices, auth rules, data behavior, AI behavior, and portability decisions.
- `docs/` for practical app instructions, such as how to run the app and how the app works.
- `prompts/` for editable AI-agent or assistant prompts, kept separate from application code.

Do not record purely visual one-off tweaks in product notes unless they express a durable design principle or affect product behavior.

## Code Style

Keep code easy for the user to inspect and edit later.

- Prefer clear names, small files, straightforward functions, and boring structure.
- Add helpful comments that explain what important parts do and why they exist.
- Keep comments balanced: enough to orient the user, but not line-by-line noise.
- Prefer single-line text, strings, comments, and list items when they fit comfortably and express one idea.
- Use multiline formatting when a line is genuinely too long, separate lines express separate meanings, or the syntax is clearer that way.

## Cleanup Habit

From time to time, do a small cleanup pass before mess accumulates.

- Remove temporary prototypes once the direction is clear.
- Move repeated behavior into simple helpers when it improves readability.
- Keep generated files, logs, virtual environments, build outputs, and secrets out of source control.
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

- Explain the important pieces after implementing.
- Point to the files the user is most likely to edit later.
- Offer a short code walkthrough when the project structure changes.
- Keep momentum, but slow down and ask when the decision would shape the product long-term.
