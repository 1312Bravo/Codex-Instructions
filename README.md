# Codex Instructions

This repository stores reusable Codex instruction assets.

## Structure

- `AGENTS.md` - repo-specific rules for maintaining this instruction repository
- `skills/` - reusable personal Codex skills
- `scripts/` - helper scripts for installing or maintaining instruction assets
- `docs/` - supporting notes and documentation

## Skills

- `skills/data-science-project-workflow/` - reusable data science workflow and style guidance
- `skills/plan-md-workflow/` - temporary PLAN.md workflow for brainstorming, planning, decisions, progress, and cleanup
- `skills/vibecode-app-builder/` - reusable collaborative app-building workflow

## Notes

- Keep reusable skills under `skills/<skill-name>/`.
- Keep root-level files focused on this repository itself.
- Install packaged skills into `C:\Users\Urh\.codex\skills\` when they should be available globally to Codex.
- See `docs/repository_structure.md` for a fuller explanation of how this repository works.

## Install Skills

Install one skill:

```powershell
python "C:\Users\Urh\Desktop\Urh\Github Repositories\Codex-Instructions\scripts\Install-CodexSkill.py" vibecode-app-builder
```

Install all skills:

```powershell
python "C:\Users\Urh\Desktop\Urh\Github Repositories\Codex-Instructions\scripts\Install-CodexSkill.py" --all
```
