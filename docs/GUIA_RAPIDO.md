# 🚀 Guia Rápido: Geração de Cards Enriquecidos

## Comece Aqui

### Opção 1: Automatizado (Recomendado) ⭐

```bash
python3 scripts/gerar_cards.py
```

Processa **TODAS as fotos** na pasta `cards/` automaticamente, gera **todos os cards** na pasta `outputs/cards-enriquecidos/`, sem intervenção.

### Opção 2: Manual (No Claude)

```
/gerar-cards-enriquecidos
```

---

## O que é Gerado?

Para cada foto:

```
cards/foto-001.png
└── outputs/cards-enriquecidos/
    ├── 001-card.md          (simples: pergunta + opções)
    └── 001-enriched-card.md (enriquecido: tradução + 2 explicações + resposta)
```

---

## Estrutura dos Cards

### Card Simples

```markdown
Scenario: Pergunta completa aqui...

---

[ ] A - Opção A
[ ] B - Opção B
[ ] C - Opção C
[ ] D - Opção D
```

### Card Enriquecido

```markdown
Scenario: Pergunta aqui...

---

[ ] A - Opção A
[ ] B - Opção B
[ ] C - Opção C
[ ] D - Opção D

---

### TRANSLATED QUESTION
Pergunta em português
Alternativas traduzidas:
A) ...

---

### EXPLANATION (TECH LEAD)
Explicação:
Por que alternativa X é correta:
Por que as outras estão erradas:
Dica importante:

---

### 🚸 CHILDREN EXPLANATION
[Mesmo que acima, mas lúdico com emojis]

---

### CORRECT ANSWER
[ ] X - Texto da resposta
```

---

## Regras de Ouro 🎯

### ❌ NUNCA FAÇA:
- "Essa alternativa está errada" (sem explicar por quê)
- Título `# Pergunta 1:` no card simples
- Quebrar pergunta em múltiplas linhas (tem que ser tudo após "Scenario:")
- Tradução literal (faça fiel ao significado)

### ✅ SEMPRE FAÇA:
- Explicar O MOTIVO específico de cada erro
- "A) [Motivo] — [Consequência]"
- Começar card simples direto com `Scenario:`
- Usar analogias na CHILDREN EXPLANATION (robô, casa, etc.)
- Adicionar emojis na CHILDREN EXPLANATION se apropriado

---

## Próximas Vezes

### Se usar o script Python:
```bash
python3 scripts/gerar_cards.py
```

### Se fechar e abrir novo contexto:
- O script está lá, é autossuficiente
- Leia `.claude/projects/.../memory/skill-cards-estrutura.md`
- Execute `python3 scripts/gerar_cards.py`

### Não há ambiguidades. Não há problemas. Só qualidade. ✨

---

## Referências

- **Templates:** `templates/001-card.md`, `templates/001-enriched-card.md`
- **Script:** `scripts/gerar_cards.py`
- **Memoria:** `.claude/projects/.../memory/skill-cards-estrutura.md`
- **Skill Manual:** `/gerar-cards-enriquecidos` (se quiser instruções via Claude)
