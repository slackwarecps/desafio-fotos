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

## Processo Automático

1. **Detectar Cards Enriquecidos**
   - Encontra todos os arquivos `NNN-enriched-card.md` no diretório
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

Base de formatação:
- `/Users/fabioalvaropereira/Desktop/desafio-fotos/templates/deck-exemplo.md`

Cards de entrada:
- `/Users/fabioalvaropereira/Desktop/desafio-fotos/NNN-enriched-card.md`

Output:
- `/Users/fabioalvaropereira/Desktop/desafio-fotos/flashcards-deck-[DATA].pdf`
