"""Install reusable skills from this repository into the local Codex skills folder.

Usage:
    python scripts\\Install-CodexSkill.py vibecode-app-builder
    python scripts\\Install-CodexSkill.py --all
"""

from __future__ import annotations

import shutil
import sys
from pathlib import Path


def _copy_skill(source: Path, destination: Path) -> None:
    if destination.exists():
        shutil.rmtree(destination)

    shutil.copytree(source, destination)
    print(f"Installed {source.name} -> {destination}")


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: python scripts\\Install-CodexSkill.py <skill-name|--all>")
        return 1

    repo_root = Path(__file__).resolve().parent.parent
    skills_root = repo_root / "skills"
    codex_skills_root = Path.home() / ".codex" / "skills"
    requested_skill = sys.argv[1]

    if not skills_root.exists():
        raise FileNotFoundError(f"Skills folder does not exist: {skills_root}")

    codex_skills_root.mkdir(parents=True, exist_ok=True)

    if requested_skill == "--all":
        for source in sorted(path for path in skills_root.iterdir() if path.is_dir()):
            _copy_skill(source, codex_skills_root / source.name)

        return 0

    source = skills_root / requested_skill
    if not source.exists():
        raise FileNotFoundError(f"Unknown skill: {requested_skill}")

    _copy_skill(source, codex_skills_root / source.name)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
