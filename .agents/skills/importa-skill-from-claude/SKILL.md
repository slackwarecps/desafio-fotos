---
name: importa-skill-from-claude
description: Importa automaticamente todas as skills e regras do Claude Code (.claude/skills/ e CLAUDE.md) para o formato do Antigravity/AGY (.agents/skills/ e AGENTS.md).
---

# Skill: Importar Skills do Claude Code para o Antigravity (AGY)

Esta skill automatiza a migração/importação de skills e diretrizes criadas no formato Claude Code (`.claude/skills/` e `CLAUDE.md`) para o formato nativo do Antigravity (`.agents/skills/` e `AGENTS.md`).

## Como Usar

### 1. Execução Automática via Python
Execute o script auxiliar incluído na skill:

```bash
python3 .agents/skills/importa-skill-from-claude/scripts/importa.py
```

### 2. Processo Passo a Passo Manual (se necessário)

1. **Copiar Diretório de Skills**:
   ```bash
   mkdir -p .agents/skills
   cp -r .claude/skills/* .agents/skills/
   ```

2. **Migrar Arquivo de Regras**:
   ```bash
   cp CLAUDE.md AGENTS.md
   ```

## O que a Skill Faz

1. **Detecção**: Localiza a pasta `.claude/skills/` e o arquivo `CLAUDE.md` no repositório.
2. **Cópia de Skills**: Mapeia todas as subpastas de skills e as copia para `.agents/skills/` preservando os arquivos `SKILL.md`, scripts e referências.
3. **Cópia de Regras**: Copia o arquivo `CLAUDE.md` para `AGENTS.md` na raiz do projeto para que o Antigravity reconheça as instruções gerais do projeto.
