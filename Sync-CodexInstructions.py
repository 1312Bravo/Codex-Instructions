"""
Sync Codex instruction files to another project directory from the terminal.

Usage:
    python Sync-CodexInstructions.py "C:\\path\\to\\project"
"""

from __future__ import annotations

import shutil
import sys
from pathlib import Path


def main() -> int:
    if len(sys.argv) != 2:
        print('Usage: python Sync-CodexInstructions.py "C:\\path\\to\\project"')
        return 1

    target_project_path = Path(sys.argv[1]).expanduser().resolve()
    script_root = Path(__file__).resolve().parent
    source_files = ("AGENTS.md", "SKILL.md")

    if not target_project_path.exists():
        raise FileNotFoundError(f"Target project path does not exist: {target_project_path}")

    for name in source_files:
        source = script_root / name
        destination = target_project_path / name

        if not source.exists():
            raise FileNotFoundError(f"Missing source file: {source}")

        shutil.copy2(source, destination)
        print(f"Copied {name} -> {destination}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
