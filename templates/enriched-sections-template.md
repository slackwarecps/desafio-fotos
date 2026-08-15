# Template — Seções de Enriquecimento (`card-enricher-tech` e `card-enricher-kids`)

Layout canônico das seções `EXPLANATION (TECH LEAD)`, `🚸 CHILDREN EXPLANATION` e
`CORRECT ANSWER` do arquivo `NNN-enriched-card.md`.

Referência viva: `outputs/cards-enriquecidos-forms/001-enriched-card.md` (TECH)
e `outputs/cards-enriquecidos-forms/002-enriched-card.md` (KIDS).

---

## ⚠️ REGRA CRÍTICA: são 3 alternativas erradas, não 4

Cada card tem **4 alternativas (A–D)** e **exatamente 1 correta**.
Portanto a seção "Por que as outras estão erradas" lista **SEMPRE 3 itens** — as três
alternativas que **não** são a resposta.

🚫 **NUNCA inclua a alternativa correta na lista de erradas.** Isso é uma contradição
que inutiliza o card para estudo.

| Resposta correta | Itens em "Por que as outras estão erradas" |
|---|---|
| A | B, C, D |
| B | A, C, D |
| C | A, B, D |
| D | A, B, C |

🚫 **Nunca renomeie o rótulo.** Se você está explicando a alternativa B, o item começa
com `B)` — nunca `A)`, nunca `ALTERNATIVA B`, nunca `❌ ALTERNATIVA B`.
O rótulo tem que casar com a letra que está sendo criticada.

Antes de escrever, monte mentalmente a lista: *"a resposta é X, logo eu refuto {A,B,C,D} − {X}"*.

---

## Seção `### EXPLANATION (TECH LEAD)`

```markdown
### EXPLANATION (TECH LEAD)

**Explicação:**
<2-3 linhas: qual conceito/padrão/decisão arquitetural a pergunta testa>

**Por que a alternativa <X> é a correta:**
<5-7 linhas de análise técnica profunda, conectada a princípios e padrões>

**Por que as outras estão erradas:**

<L1>) <por que falha — problema específico e consequência>

<L2>) <por que falha — problema específico e consequência>

<L3>) <por que falha — problema específico e consequência>

**Dica importante:**
<2-3 linhas: padrão recorrente e conexão com conceitos maiores>
```

Regras de formatação:
- Os 4 sub-cabeçalhos em **negrito**, cada um em sua própria linha, com o texto começando na linha seguinte
- Itens das erradas: `A)` / `B)` / `C)` / `D)` — letra simples, **sem emoji** (emoji é exclusivo do KIDS)
- Uma linha em branco entre cada item
- `<L1> <L2> <L3>` são as três letras erradas, em ordem alfabética

---

## Seção `### 🚸 CHILDREN EXPLANATION`

```markdown
### 🚸 CHILDREN EXPLANATION

**Explicação:**
<2-3 linhas em linguagem simples, com analogia do mundo real>

**Por que a alternativa <X> é a correta:**
<3-4 linhas, linguagem acessível, mantendo precisão>

**Por que as outras estão erradas:**

<L1>) <emoji> <por que não funciona, sem jargão>

<L2>) <emoji> <por que não funciona, sem jargão>

<L3>) <emoji> <por que não funciona, sem jargão>

**Dica importante:**
<2-3 linhas: a lição para levar, em linguagem simples>
```

Mesma estrutura do TECH, com uma diferença: cada item leva o emoji da **sua própria letra**,
logo após o rótulo.

### Mapa de emojis (obrigatório)

| Letra | Emoji |
|---|---|
| A | 🅰️ |
| B | 🅱️ |
| C | 🅲️ |
| D | 🅳️ |

🚫 Nunca use `⚪` para a alternativa C — o emoji correto é `🅲️`.
🚫 O emoji tem que corresponder à letra do item: `C) 🅲️`, jamais `C) 🅱️`.

---

## Seção `### CORRECT ANSWER`

Preenchida pelo `card-enricher-tech`. Uma única linha:

```markdown
### CORRECT ANSWER

[ ] <X> - <texto completo da alternativa em INGLÊS>
```

- O texto é copiado **do bloco em inglês no topo do arquivo**, não da tradução
- Marcador é `[ ]` — nunca `[X]`, nunca `**X**`
- Formato `[ ] D - texto`, com espaços em torno do hífen

---

## Checklist antes de responder

- [ ] A lista de erradas tem **exatamente 3 itens**
- [ ] A alternativa correta **não** aparece na lista de erradas
- [ ] Cada rótulo casa com a alternativa que o texto realmente critica
- [ ] Nenhum item repete a mesma alternativa de outro item
- [ ] TECH sem emoji nos rótulos; KIDS com o emoji certo para cada letra
- [ ] Os 4 sub-cabeçalhos em negrito estão presentes e na ordem
- [ ] Seções preservadas: você **não** apagou nem alterou nada que outro agente escreveu

---

## Erros reais já cometidos (não repetir)

| Card | Erro | Correto |
|---|---|---|
| 004 | Listou 4 erradas, incluindo a alternativa A que é a resposta correta | Listar só B, C, D |
| 004 | Dois itens diferentes descreviam a mesma alternativa B | Um item por alternativa |
| 004 | TECH usou bullets `- **B (...):**` | `B) texto` |
| 005 | Rótulo deslocado: `A) ❌ ALTERNATIVA B` | `B) ...` |
| 005 | KIDS usou `🅰️` para a alternativa B | `B) 🅱️` |
| 002/005 | Usou `⚪` para a alternativa C | `C) 🅲️` |
| 003 | TECH sem os sub-cabeçalhos em negrito | Incluir os 4 |
| 002 | `CORRECT ANSWER` com marcador `[X] B -` | `[ ] B -` |
