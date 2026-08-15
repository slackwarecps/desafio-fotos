# Template Canônico do Relatório PDF

**Fonte única de verdade para o layout do PDF do deck.** Qualquer geração de PDF neste projeto
deve seguir este arquivo — não duplique o layout em agentes, skills ou scripts.

**Implementação canônica (obrigatória):**
`.claude/skills/exporta-cards-enriquecidos-para-pdf/gerar_pdf.py`

```bash
python3 .claude/skills/exporta-cards-enriquecidos-para-pdf/gerar_pdf.py [cards_dir] [outputs_dir]
```

**NÃO escreva um gerador novo a cada execução.** Rode o script. Improvisar o PDF foi o que
produziu, em rodadas anteriores, emojis virando quadrados pretos (tofu) e markdown literal
(`**Explicação:**` impresso na página). Se o layout precisar mudar, altere este template **e**
o script — nunca só um dos dois.

**Consumidores:**
- `.claude/agents/gerador-de-reports.md` — Fase 4 do pipeline (executa o script)
- `.claude/skills/exporta-cards-enriquecidos-para-pdf/` — exportação manual (mesmo script)

---

## Regra fundamental: o deck é o que existe

O PDF contém **exatamente** os `*-enriched-card.md` presentes em
`outputs/cards-enriquecidos-forms/` no momento da geração.

- `TOTAL` = número real de cards encontrados. 1 card → deck de 1. 15 cards → deck de 15.
- O tamanho do `formulario.tsv` é **irrelevante**: 60 ou 1000 linhas com 15 cards enriquecidos
  produzem o mesmo PDF de 15 questões.
- Lacunas na sequência (001, 002, 007) são normais. **Nunca** invente conteúdo, placeholder ou
  página vazia para números ausentes.
- A numeração exibida usa a **posição no deck**, não o número do arquivo: o terceiro card do
  deck é `Card 003/TOTAL` mesmo que o arquivo seja `007-enriched-card.md` (o número do arquivo
  aparece à direita do cabeçalho, como referência).

---

## Pipeline de renderização (não substituir)

```
NNN-enriched-card.md  →  parse das 5 seções  →  HTML + CSS  →  Chrome headless  →  PDF
```

**Chrome headless é obrigatório:**

```
/Applications/Google Chrome.app/Contents/MacOS/Google Chrome \
  --headless --disable-gpu --no-pdf-header-footer --print-to-pdf=<saída> <arquivo.html>
```

Motivo: é o único renderizador testado nesta máquina que embute **Apple Color Emoji** como
bitmap colorido. Alternativas descartadas por falharem com emoji:
- `reportlab` / `fpdf2` — fontes sem cobertura de emoji → quadrados pretos
- `weasyprint` — gera o PDF, mas não embute o glifo colorido
- `pandoc` direto para LaTeX — mesma limitação de fonte

---

## Nome e destino do arquivo

- **Formato:** `Report dd-mm-yyyy hh:mm:ss.pdf`
- **Exemplo:** `Report 15-08-2026 14:23:45.pdf`
- **Destino:** `outputs/`
- O HTML intermediário é temporário e **removido** ao final (não deixar lixo em `outputs/`)

---

## Regras de formatação — o que causou os defeitos

### ❌ Proibido

- **Arte ASCII e box-drawing** (`╔══╗`, `║`, `─────`) para molduras, réguas e separadores.
  Esses caracteres não existem nas fontes usadas e saem como **quadrados pretos**.
  Use elementos reais: `border`, `background`, `border-radius`, `border-bottom`.
- **Markdown cru na página.** `**negrito**`, `*itálico*` e `` `código` `` devem ser
  **renderizados** como `<strong>`, `<em>` e `<code>` — nunca impressos literalmente.
- **Texto corrido colapsado.** Parágrafos separados por linha em branco no card devem virar
  `<p>` distintos; blocos de alternativas (`A) …`, `B) …`) devem virar lista, com a letra
  destacada — igual nos dois idiomas.

### ✅ Obrigatório

- **Quebra de página entre a pergunta em inglês e a em português.** O bloco
  `PERGUNTA (PORTUGUÊS)` sempre abre uma página nova (`page-break-before: always`), para que o
  enunciado em inglês e suas alternativas possam ser lidos e respondidos sem que a tradução
  apareça no mesmo campo de visão
- Numeração de páginas no rodapé; novo card sempre começa em página nova (`page-break-after`)
- Cabeçalho do card: barra azul (`#1a4f9c`) arredondada, com `Card NNN/TOTAL` à esquerda e o
  número do arquivo à direita
- Cada bloco abre com **ícone + título** azul e régua fina (`border-bottom`) abaixo
- Rótulos internos (`Explicação:`, `Por que a alternativa X é a correta:`, `Por que as outras
  estão erradas:`, `Dica importante:`) em azul e negrito, como subtítulos
- Resposta correta em caixa verde-clara com barra lateral verde e a letra em destaque
- Corpo 11,5pt / `line-height` 1.55; títulos 12–26pt; margens A4 18/16/20/16mm
- UTF-8 preservado; PDF **selecável e copiável** (texto real, nunca imagem de página)

---

## Estrutura do documento

### 1. Capa

- Ícone 🧠 grande, centralizado
- Título **FLASHCARDS DECK** em azul
- Régua azul curta abaixo do título
- Subtítulo `Claude Certified Architect · Foundations Certification`
- Metadados: `Gerado em dd/mm/yyyy hh:mm:ss` e `Total de cards: TOTAL`

### 2. Índice — 📑 Índice de Perguntas

Uma linha por card, em ordem numérica: número do arquivo em azul + início do enunciado em
inglês truncado (~95 caracteres), separadas por linha fina.

### 3. Páginas de card

Cabeçalho `Card NNN/TOTAL` seguido dos 5 blocos, nesta ordem e com estes ícones. O card ocupa
**no mínimo duas páginas**: a primeira termina no bloco em inglês, e o bloco em português abre
a página seguinte.

| Ícone | Bloco | Seção de origem no `NNN-enriched-card.md` |
|---|---|---|
| 📘 | PERGUNTA (ENGLISH) | `Scenario:` + opções `[ ] A-D` |
| 🇧🇷 | PERGUNTA (PORTUGUÊS) | `### TRANSLATED QUESTION` |
| 🧠 | ANÁLISE TÉCNICA (TECH LEAD) | `### EXPLANATION (TECH LEAD)` |
| 🚸 | EXPLICAÇÃO ACESSÍVEL (CRIANÇAS) | `### 🚸 CHILDREN EXPLANATION` |
| ✅ | RESPOSTA CORRETA | `### CORRECT ANSWER` |

> Atenção ao parsing de `### CORRECT ANSWER`: é a **última** seção do arquivo e não tem `---`
> depois dela. A regex precisa aceitar fim-de-arquivo como delimitador, senão a resposta sai
> vazia no PDF.

### 4. Página final

- Título 🏁 **Fim do Deck**
- `Cards neste deck: TOTAL` e data de geração
- Lista dos 5 blocos que compõem cada card (com os mesmos ícones)
- Rodapé: `Para uso em Spaced Repetition Systems (SRS)`

---

## Verificação após gerar

1. O script imprime `REPORT <primeiro>-<último> OK <caminho>` (ou `REPORT FAILED reason: …`)
2. Abrir o PDF e conferir, em pelo menos uma página de card:
   - emojis **coloridos**, sem quadrados pretos em nenhum lugar
   - nenhum `**` ou `` ` `` visível no texto
   - alternativas em lista nos dois idiomas
   - bloco de resposta correta preenchido com a letra e o texto
