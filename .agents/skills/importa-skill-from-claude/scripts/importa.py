#!/usr/bin/env python3
"""
Script helper para a skill importa-skill-from-claude.
Copia e adapta skills e regras da pasta .claude/ para a estrutura do Antigravity (.agents/).
"""

import os
import shutil

def import_claude_to_agy():
    project_root = os.getcwd()
    claude_skills_dir = os.path.join(project_root, ".claude", "skills")
    agents_skills_dir = os.path.join(project_root, ".agents", "skills")
    claude_md = os.path.join(project_root, "CLAUDE.md")
    agents_md = os.path.join(project_root, "AGENTS.md")

    print("=" * 60)
    print("🔄 Importador de Skills do Claude Code para o Antigravity (AGY)")
    print("=" * 60)

    # 1. Importar Skills
    if not os.path.exists(claude_skills_dir):
        print(f"⚠️  Diretório '{claude_skills_dir}' não encontrado.")
    else:
        os.makedirs(agents_skills_dir, exist_ok=True)
        skills = [d for d in os.listdir(claude_skills_dir) if os.path.isdir(os.path.join(claude_skills_dir, d))]

        if not skills:
            print("⚠️  Nenhuma skill encontrada em .claude/skills/")
        else:
            print(f"\n📂 Encontradas {len(skills)} skills em .claude/skills/:")
            for skill in skills:
                src = os.path.join(claude_skills_dir, skill)
                dst = os.path.join(agents_skills_dir, skill)

                # Se a skill de destino for a própria skill de importação, pula para evitar loops
                if skill == "importa-skill-from-claude" and src == dst:
                    continue

                shutil.copytree(src, dst, dirs_exist_ok=True)
                print(f"   ✓ Skill '{skill}' importada para .agents/skills/{skill}/")

    # 2. Importar CLAUDE.md para AGENTS.md
    if os.path.exists(claude_md):
        print(f"\n📄 Encontrado arquivo CLAUDE.md na raiz do projeto.")
        if not os.path.exists(agents_md):
            shutil.copy2(claude_md, agents_md)
            print(f"   ✓ Copiado CLAUDE.md → AGENTS.md (Regras do projeto ativadas no AGY)")
        else:
            print(f"   ℹ️  AGENTS.md já existe na raiz. Mantido intacto.")

    print("\n✨ Processo de importação concluído com sucesso!")

if __name__ == "__main__":
    import_claude_to_agy()
