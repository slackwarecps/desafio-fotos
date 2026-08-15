---
name: exporta-cards-enriquecidos-para-pdf
description: Exporta todos os cards enriquecidos para um único arquivo PDF seguindo o padrão de deck didático
---

# Skill: Exporta Cards Enriquecidos para PDF

Consolida todos os cards enriquecidos (NNN-enriched-card.md) em um único arquivo PDF formatado como deck didático.

## Uso

```bash
/exporta-cards-enriquecidos-para-pdf
```

## Implementação Canônica (use esta, não improvise)

```bash
python3 .claude/skills/exporta-cards-enriquecidos-para-pdf/gerar_pdf.py
```

`gerar_pdf.py` faz o fluxo completo — descobre os cards, faz o parse das 5 seções, monta o HTML
e renderiza com **Chrome headless** (único caminho que produz emojis coloridos em vez de
quadrados pretos). Imprime na última linha `REPORT <primeiro>-<último> OK <caminho>`.

O `exporta.py` legado gera o Markdown consolidado e é mantido para esse uso; para PDF, o
caminho canônico é `gerar_pdf.py`.

## Template Canônico (leitura obrigatória)

O layout do PDF é definido **exclusivamente** por:

**`templates/pdf-report-template.md`**

Leia esse arquivo **antes** de gerar qualquer PDF. Ele é a fonte única compartilhada com o agente
`gerador-de-reports` (Fase 4 do pipeline), garantindo que o PDF automático e o exportado
manualmente tenham layout idêntico. Para mudar o layout, edite o template — nunca esta skill.

O template também define a regra do tamanho do deck: o PDF contém **exatamente** os cards
enriquecidos existentes no diretório (1 card → deck de 1; 15 cards → deck de 15), independente
de quantas linhas o `formulario.tsv` tenha.

## Processo Automático

1. **Detectar Cards Enriquecidos**
   - Encontra todos os arquivos `NNN-enriched-card.md` em `outputs/cards-enriquecidos-forms/`
   - Ordena por número (001, 002, 003, ...)

2. **Extrair Conteúdo**
   - Pergunta em inglês
   - Pergunta traduzida em português
   - EXPLANATION (TECH LEAD)
   - SIMPLE EXPLANATION
   - Resposta correta

3. **Gerar Documento Consolidado**
   - Capa com título e data
   - Cada pergunta em página separada (Question X/Y)
   - Cada resposta/explicação em página separada (Question X Answer)
   - Índice navegável

4. **Exportar para PDF**
   - Arquivo Markdown Raw: `outputs/flashcards-deck-[DATA].md` (mantido)
   - Comando pandoc automático: converte `.md` → `.pdf`
   - Arquivo PDF: `outputs/flashcards-deck-[DATA].pdf` (gerado)
   - Pronto para estudar ou compartilhar

## Formato de Saída

### Estrutura do PDF

```
Página 1: Capa
- Título: "Flashcards Deck - Claude Certified Architect"
- Data de geração
- Total de questões

Página 2: Índice (se muitos cards)
- Lista de questões com página

Páginas 3+: Questões (alternadas com respostas)
- Question 1 (página par)
- Question 1 Answer (página ímpar)
- Question 2 (página par)
- Question 2 Answer (página ímpar)
- ...
```

## O que Esperar

```
✅ Detectados cards enriquecidos:
   - 001-enriched-card.md
   - 002-enriched-card.md
   - 003-enriched-card.md
   ... (3 cards encontrados)

📝 Processando cards...
   ✓ Extraindo conteúdo...
   ✓ Formatando questões...
   ✓ Gerando documento Markdown...

📄 Consolidando em arquivo único...
   ✓ flashcards-deck-2026-07-18.md criado (13 KB)

🔄 Convertendo para PDF com pandoc...
   $ pandoc flashcards-deck-2026-07-18.md -o flashcards-deck-2026-07-18.pdf
   ✓ flashcards-deck-2026-07-18.pdf criado (formato PDF)

✨ Pronto! Deck exportado com sucesso.
   Arquivos:
   - flashcards-deck-2026-07-18.md (raw, editável)
   - flashcards-deck-2026-07-18.pdf (formatado, pronto para compartilhar)
   Total: 3 questões
   Páginas: 7
```

## Referência

Base de formatação (**fonte única — leitura obrigatória**):
- `templates/pdf-report-template.md`

Cards de entrada:
- `outputs/cards-enriquecidos-forms/NNN-enriched-card.md`

Output:
- `outputs/flashcards-deck-[DATA].pdf`

Consumidor irmão do mesmo template:
- `.claude/agents/gerador-de-reports.md` — gera `outputs/Report dd-mm-yyyy hh:mm:ss.pdf` na Fase 4 do pipeline
