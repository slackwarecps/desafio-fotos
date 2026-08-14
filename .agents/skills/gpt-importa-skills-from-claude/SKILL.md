---
name: gpt-importa-skills-from-claude
description: Importa skills e regras do Claude Code (.claude/skills e CLAUDE.md) para o formato do GPT Codex (.agents/skills e AGENTS.md).
---

# Importar skills do Claude para o GPT Codex

Use esta skill quando precisar migrar a configuração do Claude Code para o formato usado pelo GPT Codex.

## O que ela faz

- Copia todas as skills de `.claude/skills/` para `.agents/skills/`
- Copia `CLAUDE.md` para `AGENTS.md`
- Preserva a estrutura de diretórios e os arquivos internos das skills

## Uso

Execute o script incluído na skill:

```bash
python3 .agents/skills/gpt-importa-skills-from-claude/scripts/importa.py
```

## Comportamento esperado

- Se a skill já existir em `.agents/skills/`, o conteúdo é atualizado no local
- Se `CLAUDE.md` existir, ele é espelhado para `AGENTS.md`
- A execução deve ser feita na raiz do repositório

