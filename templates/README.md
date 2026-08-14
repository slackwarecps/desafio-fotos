# 📋 Templates e Exemplos

Modelos de cards e deck para referência.

## 📄 Templates

### 🎯 `001-card.md` (Simple Card)
**Propósito:** Template do card básico

```markdown
[Question in English]
---
[ ] A - [Option A]
[ ] B - [Option B]
[ ] C - [Option C]
[ ] D - [Option D]
```

**Estrutura:**
- Questão em inglês
- Separador `---`
- 4 opções (A, B, C, D)
- Sem explicações

---

### 🎓 `001-enriched-card.md` (Enriched Card)
**Propósito:** Template do card enriquecido com explicações

**Seções:**
1. **ORIGINAL QUESTION** - Questão em inglês
2. **TRANSLATED QUESTION** - Tradução em português
3. **EXPLANATION (TECH LEAD)** - Explicação técnica profunda
4. **CHILDREN EXPLANATION** - Explicação acessível/simplificada
5. **CORRECT ANSWER** - Resposta marcada (A/B/C/D)

**Usado por:**
- `/gerar-cards-enriquecidos` (skill)
- SRS (Spaced Repetition Systems)
- Estudos de Arquitetura e Design Patterns

---

### 🎴 `deck-exemplo.md` (Deck Example)
**Propósito:** Exemplo de deck completo (vários cards)

**Mostra:**
- Múltiplos cards sequenciais
- Formatação para PDF/EPUB
- Índice de conteúdo
- Paginação

**Gerado por:**
- `/exporta-cards-enriquecidos-para-pdf`
- `/exporta-cards-enriquecidos-para-epub`

---

## 🔍 Exemplos de Seções

### EXPLANATION (TECH LEAD) ✨

```markdown
### EXPLANATION (TECH LEAD)

**Pattern/Concept Being Tested:** [nome do padrão]

The correct answer is **[LETRA]** because:
- [Razão técnica 1]
- [Razão técnica 2]

Why **[LETRA]** is wrong:
- [Motivo específico]
...
```

### CHILDREN EXPLANATION 👶

```markdown
### 🚸 CHILDREN EXPLANATION

**Simple Concept:** [Explicação em linguagem simples]

**Why the right answer works:**
- [Razão em linguagem acessível]

**Why others don't work:**
- [Alternativa 1]: [Por quê?]
- [Alternativa 2]: [Por quê?]
```

---

## 📊 Estatísticas

| Template | Propósito | Seções | Público |
|----------|-----------|--------|---------|
| `001-card.md` | Card básico | 2 | Estudo rápido |
| `001-enriched-card.md` | Card completo | 5+ | Aprendizado profundo |
| `deck-exemplo.md` | Múltiplos cards | - | Referência |

---

## 🎯 Quando Usar Cada Um

| Situação | Template | Comando |
|----------|----------|---------|
| Estudo rápido | `001-card.md` | Uso manual |
| Aprendizado profundo | `001-enriched-card.md` | `/gerar-cards-enriquecidos` |
| Exportar para PDF | `deck-exemplo.md` | `/exporta-cards-enriquecidos-para-pdf` |
| Exportar para EPUB | `deck-exemplo.md` | `/exporta-cards-enriquecidos-para-epub` |

---

## 📝 Checklist de Qualidade

Ao criar novo card, valide contra:

- ✅ Questão em inglês está clara
- ✅ Tradução em português é fiel (não literal)
- ✅ Explicação técnica menciona padrões/conceitos
- ✅ Explicação técnica explica POR QUÊ (não apenas que)
- ✅ Explicação infantil usa linguagem acessível
- ✅ Respostas erradas têm análise individual
- ✅ Resposta correta está marcada
- ✅ Sem typos ou erros de formatação

---

**📚 Veja também:** `../docs/VALIDACAO_CHECKLIST.md`
