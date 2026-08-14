# 🗺️ Índice de Navegação

Mapa visual para navegar pelo projeto Desafio Fotos.

---

## 🎯 Por Objetivo

### 🚀 Quero Começar Rápido
```
1. Leia: README.md
2. Leia: docs/GUIA_RAPIDO.md
3. Coloque fotos em: cards/
4. Execute: /gerar-cards-enriquecidos
```

### 📸 Quero Adicionar Novas Fotos
```
1. Coloque em: cards/
2. Execute: /gerar-cards-enriquecidos
3. Valide: docs/VALIDACAO_CHECKLIST.md
```

### 📚 Quero Exportar para PDF
```
1. Certifique-se que cards estão em: outputs/cards-enriquecidos/NNN-enriched-card.md
2. Execute: /exporta-cards-enriquecidos-para-pdf
3. Resultado em: outputs/flashcards-deck-*.pdf
```

### 📱 Quero Exportar para EPUB
```
1. Certifique-se que cards estão em: outputs/cards-enriquecidos/NNN-enriched-card.md
2. Execute: /exporta-cards-enriquecidos-para-epub
3. Resultado em: outputs/flashcards-*.epub
4. Abra em Google Play Books ou similar
```

### 🔧 Quero Executar Scripts Manualmente
```
1. Leia: scripts/README.md
2. Leia: docs/SCRIPTS_CANÔNICOS.md
3. Execute scripts em: scripts/
```

### ✅ Quero Validar Qualidade
```
1. Leia: docs/VALIDACAO_CHECKLIST.md
2. Revise: outputs/cards-enriquecidos/NNN-enriched-card.md
3. Corrija conforme checklist
```

### 🐛 Encontrei um Problema
```
1. Procure em: docs/PROBLEMAS_RESOLVIDOS.md
2. Se não encontrar, abra issue no GitHub
```

### 👀 Quero Ver Exemplos
```
1. Veja: templates/001-card.md (simples)
2. Veja: templates/001-enriched-card.md (enriquecido)
3. Veja: templates/deck-exemplo.md (completo)
4. Leia: templates/README.md (explicação)
```

---

## 📂 Por Diretório

### 📄 Raiz (`/`)
| Arquivo | Propósito |
|---------|-----------|
| `README.md` | 📖 Documentação principal do projeto |
| `CLAUDE.md` | 🤖 Instruções para Claude Code |
| `ESTRUTURA_PROJETO.md` | 📊 Visualização da estrutura |
| `INDICE_NAVEGACAO.md` | 🗺️ Este arquivo |

### 📚 Documentação (`docs/`)
| Arquivo | Para Quem |
|---------|-----------|
| `README.md` | Índice de documentação |
| `GUIA_RAPIDO.md` | ⭐ Começar agora |
| `USAR_SKILL.md` | Usar as skills |
| `REGRA_NUMERACAO.md` | Entender o sistema de nomes |
| `VALIDACAO_CHECKLIST.md` | Garantir qualidade |
| `PROBLEMAS_RESOLVIDOS.md` | 🐛 Troubleshooting |
| `SCRIPTS_CANÔNICOS.md` | Referência de scripts |

### 🔧 Scripts (`scripts/`)
| Script | Propósito |
|--------|-----------|
| `gerar_cards.py` | ⭐ Gerar cards (principal) |
| `gerar_cards_claude.py` | Gerar cards (alternativa) |
| `processar-cards.py` | Processar/validar cards |
| `exporta_epub.py` | Exportar para EPUB |
| `rename_flashcards.sh` | Renomear flashcards (legado) |
| `README.md` | Como usar scripts |

### 📋 Templates (`templates/`)
| Arquivo | Propósito |
|---------|-----------|
| `001-card.md` | Exemplo: card simples |
| `001-enriched-card.md` | Exemplo: card enriquecido |
| `deck-exemplo.md` | Exemplo: deck completo |
| `README.md` | Explicação dos templates |

### 🎓 Fotos Originais (`cards/`)
| Arquivo | Criado Por |
|---------|-----------|
| `foto-NNN.png` | Você (coloque aqui) |
| `README.md` | Instruções |

### 📤 Outputs (`outputs/`)
| Arquivo / Pasta | Criado Por |
|---------|-----------|
| `cards-enriquecidos/` | `python3 scripts/gerar_cards.py` (Gera `NNN-card.md` e `NNN-enriched-card.md`) |
| `flashcards-deck-*.pdf` | `/exporta-cards-enriquecidos-para-pdf` |
| `flashcards-*.epub` | `/exporta-cards-enriquecidos-para-epub` |
| `README.md` | Instruções |

### 🔐 Configuração (`.claude/`)
Não edite manualmente. Gerenciado por Claude Code.

---

## 🔀 Fluxos Comuns

### Fluxo 1: Criar Novo Card do Zero

```
Start
  ↓
[Coloque foto em cards/]
  ↓
[Execute: python3 scripts/gerar_cards.py]
  ↓
[Leia: docs/VALIDACAO_CHECKLIST.md]
  ↓
[Edite outputs/cards-enriquecidos/NNN-enriched-card.md se necessário]
  ↓
[Execute: /exporta-cards-enriquecidos-para-pdf]
  ↓
[Abra em PDF output]
  ↓
Fim ✅
```

### Fluxo 2: Editando Card Existente

```
Start
  ↓
[Edite: outputs/cards-enriquecidos/NNN-enriched-card.md]
  ↓
[Leia: docs/VALIDACAO_CHECKLIST.md]
  ↓
[Execute: /exporta-cards-enriquecidos-para-pdf]
  ↓
[Verifique em PDF]
  ↓
Fim ✅
```

### Fluxo 3: Exportar Todos os Cards

```
Start
  ↓
[Certifique: outputs/cards-enriquecidos/NNN-enriched-card.md existem]
  ↓
[Execute: /exporta-cards-enriquecidos-para-pdf]
  ↓
[Resultado: outputs/flashcards-deck-*.pdf]
  ↓
[Execute: /exporta-cards-enriquecidos-para-epub]
  ↓
[Resultado: outputs/flashcards-*.epub]
  ↓
Fim ✅
```

---

## 🎓 Hierarquia de Documentos (Do Básico ao Avançado)

```
Iniciante
    ↓
    └─ README.md (raiz)
       └─ docs/GUIA_RAPIDO.md
          └─ docs/USAR_SKILL.md
             └─ templates/README.md

Intermediário
    ↓
    └─ docs/REGRA_NUMERACAO.md
       └─ docs/VALIDACAO_CHECKLIST.md
          └─ templates/ (exemplos)

Avançado
    ↓
    └─ scripts/README.md
       └─ docs/SCRIPTS_CANÔNICOS.md
          └─ Editar scripts Python

Troubleshooting
    ↓
    └─ docs/PROBLEMAS_RESOLVIDOS.md
       └─ scripts/README.md
```

---

## 🚀 Quick Links (Atalhos)

| Preciso | Link | Tempo |
|---------|------|-------|
| Começar agora | `docs/GUIA_RAPIDO.md` | 5 min ⚡ |
| Ver exemplo | `templates/001-enriched-card.md` | 2 min |
| Gerar cards | Execute `python3 scripts/gerar_cards.py` | 1-2 min |
| Validar cards | `docs/VALIDACAO_CHECKLIST.md` | 5-10 min |
| Exportar PDF | Execute `/exporta-cards-enriquecidos-para-pdf` | 1 min |
| Exportar EPUB | Execute `/exporta-cards-enriquecidos-para-epub` | 1 min |
| Troubleshooting | `docs/PROBLEMAS_RESOLVIDOS.md` | ⏱️ |

---

## 📞 Suporte

- **Dúvidas sobre fluxo?** → `docs/GUIA_RAPIDO.md`
- **Erro ao executar?** → `docs/PROBLEMAS_RESOLVIDOS.md`
- **Qual é a regra X?** → `docs/REGRA_NUMERACAO.md`
- **Qualidade do card?** → `docs/VALIDACAO_CHECKLIST.md`
- **Como usar script?** → `scripts/README.md`

---

**💡 Próximo passo?** Leia `docs/GUIA_RAPIDO.md` agora! 🚀
