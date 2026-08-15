# Template Canônico do Relatório PDF

**Fonte única de verdade para o layout do PDF do deck.** Qualquer geração de PDF neste projeto
deve seguir este arquivo — não duplique o layout em agentes, skills ou scripts.

**Consumidores:**
- `.claude/agents/gerador-de-reports.md` — leitura obrigatória antes de gerar o PDF (Fase 4 do pipeline)
- `.claude/skills/exporta-cards-enriquecidos-para-pdf/` — mesma estrutura ao exportar manualmente

---

## Regra fundamental: o deck é o que existe

O PDF contém **exatamente** os `*-enriched-card.md` presentes em
`outputs/cards-enriquecidos-forms/` no momento da geração.

- `TOTAL` = número real de cards encontrados. 1 card → deck de 1. 15 cards → deck de 15.
- O tamanho do `formulario.tsv` é **irrelevante**: 60 ou 1000 linhas com 15 cards enriquecidos
  produzem o mesmo PDF de 15 questões.
- Lacunas na sequência (001, 002, 007) são normais. **Nunca** invente conteúdo, placeholder ou
  página vazia para números ausentes.
- A numeração exibida usa a **posição no deck**, não o número do arquivo:
  o terceiro card do deck é `Card 003/TOTAL` mesmo que o arquivo seja `007-enriched-card.md`.

---

## Nome e destino do arquivo

- **Formato:** `Report dd-mm-yyyy hh:mm:ss.pdf`
- **Exemplo:** `Report 15-08-2026 14:23:45.pdf`
- **Destino:** `/Users/fabiopereira/Desktop/desafio-formularios/outputs/`

---

## Estrutura do documento

### 1. Página de Capa

```
╔══════════════════════════════════════════╗
║                                          ║
║      FLASHCARDS DECK - ENRIQUECIDOS     ║
║                                          ║
║         Claude Certified Architect       ║
║           Foundations Certification      ║
║                                          ║
║     Generated: [dd/mm/yyyy hh:mm:ss]    ║
║     Total Cards: [TOTAL]                 ║
║                                          ║
╚══════════════════════════════════════════╝
```

### 2. Índice / Table of Contents

Uma linha por card, na ordem numérica dos arquivos, com o início do enunciado em inglês truncado:

```
ÍNDICE DE PERGUNTAS

001 - Your agent needs to insert a new helper function...
002 - A user asks a support agent for specific legal advice...
003 - An engineer who just joined the team asks...
...
```

### 3. Página de Card (uma por card)

```
╔════════════════════════════════════════════════════════════╗
║  Card [POSIÇÃO]/[TOTAL]                          Página N  ║
╚════════════════════════════════════════════════════════════╝

PERGUNTA (ENGLISH):
Your agent needs to insert a new helper function into the
middle of a 150-line utility module...

OPTIONS:
[ ] A - Use Edit with an extremely long `old_string`...
[ ] B - Use Edit's `replace_all` parameter...
[ ] C - Use Bash to append the function definition...
[ ] D - Use Read to load the file, add the function...

─────────────────────────────────────────────────────────────

PERGUNTA (PORTUGUÊS):
Seu agente precisa inserir uma nova função auxiliar no meio
de um módulo utilitário de 150 linhas...

OPÇÕES:
A) Use Edit com um `old_string` extremamente longo...
B) Use o parâmetro `replace_all` do Edit...
C) Use Bash para adicionar a definição da função...
D) Use Read para carregar o arquivo, adicionar...

─────────────────────────────────────────────────────────────

ANÁLISE TÉCNICA (TECH LEAD):
Explicação: Esta pergunta testa...
Por que D é correta: A abordagem Read-Modify-Write...
Por que A/B/C estão erradas: A) O `old_string`... B)...
Dica importante: O padrão Read-Modify-Write é...

─────────────────────────────────────────────────────────────

EXPLICAÇÃO ACESSÍVEL (CRIANÇAS):
Explicação: Imagina que você quer inserir algo no meio...
Por que D é correta: Porque você carrega tudo...
Por que A/B/C estão erradas: A) Procurar é difícil...
Dica importante: Quando precisar mudar algo...

─────────────────────────────────────────────────────────────

RESPOSTA CORRETA:
✓ D - Use Read to load the file, add the function at
      the appropriate location, then Write the updated file
```

**Mapa de origem** — cada bloco vem de uma seção do `NNN-enriched-card.md`:

| Bloco no PDF | Seção no card enriquecido |
|---|---|
| PERGUNTA (ENGLISH) + OPTIONS | `Scenario:` + opções `[ ] A-D` |
| PERGUNTA (PORTUGUÊS) + OPÇÕES | `### TRANSLATED QUESTION` |
| ANÁLISE TÉCNICA (TECH LEAD) | `### EXPLANATION (TECH LEAD)` |
| EXPLICAÇÃO ACESSÍVEL (CRIANÇAS) | `### 🚸 CHILDREN EXPLANATION` |
| RESPOSTA CORRETA | `### CORRECT ANSWER` |

### 4. Página Final

```
═══════════════════════════════════════════════════════════════
FIM DO DECK

Cards neste deck: [TOTAL]
Gerado em: dd/mm/yyyy hh:mm:ss

Estrutura de cada card:
• PERGUNTA (ENGLISH)
• OPÇÕES (A, B, C, D)
• PERGUNTA (PORTUGUÊS)
• ANÁLISE TÉCNICA (TECH LEAD)
• EXPLICAÇÃO ACESSÍVEL (CRIANÇAS)
• RESPOSTA CORRETA

Para uso em Spaced Repetition Systems (SRS)
═══════════════════════════════════════════════════════════════
```

---

## Padrões de formatação

- Capa profissional, índice navegável, quebra de página entre cards
- Numeração de páginas consistente no rodapé
- Corpo 12–14pt, títulos 16–18pt, margens e espaçamento adequados
- UTF-8 preservado (acentos e emojis)
- PDF **selecável e copiável** (texto real, nunca imagem)
- Metadata preenchida: title, author, created date
- Todas as 5 seções presentes em cada card; nenhum card duplicado
