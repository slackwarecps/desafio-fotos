#!/usr/bin/env python3
from __future__ import annotations

import os
import shutil
from pathlib import Path


def main() -> int:
    root = Path.cwd()
    claude_skills = root / ".claude" / "skills"
    agents_skills = root / ".agents" / "skills"
    claude_md = root / "CLAUDE.md"
    agents_md = root / "AGENTS.md"

    if not claude_skills.exists():
        print(f"Erro: não encontrei {claude_skills}")
        return 1

    agents_skills.mkdir(parents=True, exist_ok=True)

    imported = []
    for src in sorted(p for p in claude_skills.iterdir() if p.is_dir()):
        dst = agents_skills / src.name
        dst.mkdir(parents=True, exist_ok=True)
        for item in sorted(src.rglob("*")):
            relative = item.relative_to(src)
            target = dst / relative
            if item.is_dir():
                target.mkdir(parents=True, exist_ok=True)
                continue
            target.parent.mkdir(parents=True, exist_ok=True)
            tmp = target.with_name(f".{target.name}.tmp")
            shutil.copy2(item, tmp)
            os.replace(tmp, target)
        imported.append(src.name)

    if claude_md.exists():
        shutil.copy2(claude_md, agents_md)
        copied_rules = True
    else:
        copied_rules = False

    print("Importação concluída")
    if imported:
        print("Skills copiadas:")
        for name in imported:
            print(f"- {name}")
    if copied_rules:
        print("Regras copiadas: CLAUDE.md -> AGENTS.md")
    else:
        print("Regras não copiadas: CLAUDE.md não encontrado")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
