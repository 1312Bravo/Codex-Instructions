# Codex Instructions

This repository stores the master instructions used by Codex for data science work.

## Quick Start
1. Edit `AGENTS.md` and `SKILL.md` here.
2. Sync them into the project you want to update.
3. Open that project in VS Code or Codex.

## What Is Here
- `AGENTS.md` for project rules
- `SKILL.md` for reusable workflow guidance
- `Sync-CodexInstructions.ps1` for copying the master instructions into a target project

## Sync Command
Run the PowerShell script and point it at the target project folder:

```powershell
powershell -ExecutionPolicy Bypass -File "<path-to-this-repo>\Sync-CodexInstructions.ps1" -TargetProjectPath "<path-to-target-project>"
```

## When To Sync
- Sync when you update the master instructions and want a project to use the new version.
- Sync when you start a new project that should inherit the same guidance.
- Do not sync if a project needs different instructions than the master copy.

## Notes
- Codex uses the instructions that exist inside the project folder it is working on.
- Keep this repository as the source of truth for reusable instructions.
