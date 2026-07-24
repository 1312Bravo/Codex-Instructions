# Repository Structure

This repository is the source of truth for reusable Codex instruction assets.

## Why It Is Structured This Way

Codex uses different kinds of instruction files for different scopes:

- `AGENTS.md` gives Codex rules for the current repository.
- A packaged skill is a reusable folder with its own `SKILL.md`.
- Installed skills live in `C:\Users\Urh\.codex\skills\` so Codex can discover them across projects.

Because this repository is meant to store reusable skills, reusable behavior should live under `skills/` instead of as loose top-level files.

## Folder Layout

```text
Codex-Instructions/
  AGENTS.md
  README.md
  docs/
  scripts/
  skills/
```

## Root Files

`AGENTS.md` is only for maintaining this repository. It should not contain every reusable workflow rule.

`README.md` is the short human-facing overview of the repository.

## docs/

`docs/` contains explanations and supporting notes.

Use it for:

- how this repository works
- why it is structured this way
- longer notes about Codex instructions, skills, and workflows

## skills/

`skills/` contains reusable personal Codex skills.

Each skill should usually look like this:

```text
skills/
  skill-name/
    SKILL.md
    agents/
      openai.yaml
```

`SKILL.md` contains the instructions Codex reads when the skill is used.

`agents/openai.yaml` contains UI metadata such as display name, short description, and default prompt.

## scripts/

`scripts/` contains helpers for maintaining or installing instruction assets.

Currently, `Install-CodexSkill.py` copies skills from this repository into:

```text
C:\Users\Urh\.codex\skills\
```

Use it like this:

```powershell
python "C:\Users\Urh\Desktop\Urh\Github Repositories\Codex-Instructions\scripts\Install-CodexSkill.py" vibecode-app-builder
```

Or install all skills:

```powershell
python "C:\Users\Urh\Desktop\Urh\Github Repositories\Codex-Instructions\scripts\Install-CodexSkill.py" --all
```

## Current Skills

`data-science-project-workflow` stores reusable data science, notebook, dataframe, plotting, and analysis workflow guidance.

`vibecode-app-builder` stores reusable collaborative app-building guidance, including notes, docs, prompts, readable code, decision checkpoints, and cleanup habits.

## Mental Model

This repository stores the clean source copy.

`C:\Users\Urh\.codex\skills\` stores the installed copy Codex can use globally.

When a skill changes here, install it again so the global Codex copy is updated.
