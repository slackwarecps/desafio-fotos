# 📁 Estrutura do Projeto - Desafio Fotos

```
desafio-fotos/
│
├── 📄 README.md                    # Documentação principal do projeto
├── 📄 CLAUDE.md                    # Instruções para Claude Code
├── 📄 ESTRUTURA_PROJETO.md         # Este arquivo (visual guide)
│
├── 📚 docs/                        # DOCUMENTAÇÃO GERAL
│   ├── GUIA_RAPIDO.md             # Guia rápido para começar
│   ├── USAR_SKILL.md              # Como usar as skills
│   ├── REGRA_NUMERACAO.md         # Sistema de numeração de cards
│   ├── VALIDACAO_CHECKLIST.md     # Checklist de qualidade
│   ├── PROBLEMAS_RESOLVIDOS.md    # FAQ e problemas comuns
│   └── SCRIPTS_CANÔNICOS.md       # Scripts disponíveis
│
├── 🔧 scripts/                     # FERRAMENTAS E SCRIPTS
│   ├── gerar_cards.py             # Script principal para gerar cards (canônico)
│   ├── gerar_cards_claude.py      # Versão alternativa (Claude API)
│   ├── processar-cards.py         # Processamento de cards
│   ├── exporta_epub.py            # Exportar para EPUB
│   ├── rename_flashcards.sh       # Renomear flashcards
│   └── README.md                  # Instruções dos scripts
│
├── 📋 templates/                   # MODELOS E EXEMPLOS
│   ├── 001-card.md                # Template: card simples
│   ├── 001-enriched-card.md       # Template: card enriquecido
│   ├── deck-exemplo.md            # Exemplo de deck completo
│   └── README.md                  # Explicação dos templates
│
├── 🎓 cards/                       # FOTOS ORIGINAIS (IMAGENS)
│   ├── foto-001.png               # (Imagens das questões)
│   └── README.md                  # Regras de fotos
│
├── 📤 outputs/                     # ARQUIVOS EXPORTADOS
│   ├── cards-enriquecidos/        # 📝 FLASHCARDS GERADOS (Simples + Enriquecidos)
│   │   ├── 001-card.md
│   │   └── 001-enriched-card.md
│   ├── flashcards-deck-2026-07-19.pdf
│   ├── flashcards-deck-2026-07-19.epub
│   └── ...                        # (PDFs, EPUBs, etc)
│
└── 🔐 .claude/                     # CONFIGURAÇÃO CLAUDE CODE
    ├── settings.local.json         # Permissões e configurações
    ├── scheduled_tasks.lock        # Tarefas agendadas
    └── skills/                     # Skills customizadas do projeto
        ├── gerar-cards-enriquecidos/
        ├── exporta-cards-enriquecidos-para-pdf/
        └── exporta-cards-enriquecidos-para-epub/
```

## 🎯 Fluxo de Trabalho Recomendado

```
1️⃣  PREPARAÇÃO
    └─ Coloque fotos em cards/

2️⃣  GERAÇÃO
    └─ Execute: python3 scripts/gerar_cards.py
    └─ Cria: outputs/cards-enriquecidos/NNN-card.md + NNN-enriched-card.md

3️⃣  VALIDAÇÃO
    └─ Revise conforme: docs/VALIDACAO_CHECKLIST.md

4️⃣  EXPORTAÇÃO
    └─ PDF: /exporta-cards-enriquecidos-para-pdf
    └─ EPUB: /exporta-cards-enriquecidos-para-epub
    └─ Output: outputs/
```

## 📖 Guias Rápidos

| Preciso...                     | Veja...                          |
|--------------------------------|----------------------------------|
| Começar rápido                 | `docs/GUIA_RAPIDO.md`           |
| Usar as skills                 | `docs/USAR_SKILL.md`            |
| Validar cards                  | `docs/VALIDACAO_CHECKLIST.md`   |
| Entender numeração             | `docs/REGRA_NUMERACAO.md`       |
| Resolver problemas             | `docs/PROBLEMAS_RESOLVIDOS.md`  |
| Ver exemplos de cards          | `templates/`                     |
| Executar scripts               | `scripts/README.md`             |

## 🚀 Próximos Passos

1. **Leia primeiro:** `README.md` (visão geral do projeto)
2. **Guia rápido:** `docs/GUIA_RAPIDO.md`
3. **Primeira execução:** `python3 scripts/gerar_cards.py`
4. **Explorar:** `templates/` para ver exemplos
