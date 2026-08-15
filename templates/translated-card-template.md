# Template — Saída do `card-translator`

Este é o **layout canônico exato** do arquivo `NNN-enriched-card.md` logo após a etapa de tradução
(estágio 2 de 4 do pipeline). O `card-translator` deve produzir exatamente esta estrutura.

Referência viva: `outputs/cards-enriquecidos-forms/001-enriched-card.md`.

---

## Estrutura do arquivo (copiar literalmente)

```markdown
Scenario: <pergunta original em INGLÊS, sem as alternativas>

---

[ ] A - <opção A em INGLÊS>
[ ] B - <opção B em INGLÊS>
[ ] C - <opção C em INGLÊS>
[ ] D - <opção D em INGLÊS>

---

### TRANSLATED QUESTION

Cenário: <pergunta traduzida em PT-BR>

A) <opção A em PT-BR>
B) <opção B em PT-BR>
C) <opção C em PT-BR>
D) <opção D em PT-BR>

---

### EXPLANATION (TECH LEAD)

[PLACEHOLDER - Será preenchido pelo agente card-enricher-tech]

---

### 🚸 CHILDREN EXPLANATION

[PLACEHOLDER - Será preenchido pelo agente card-enricher-kids]

---

### CORRECT ANSWER

[PLACEHOLDER - Será preenchido pelo agente card-enricher-tech]
```

---

## Regras obrigatórias de formatação

O bloco em inglês (topo do arquivo) e o bloco PT-BR usam formatos **diferentes de propósito** —
não unifique os dois.

| Elemento | Bloco INGLÊS (topo) | Bloco PT-BR (`TRANSLATED QUESTION`) |
|---|---|---|
| Rótulo do cenário | `Scenario:` | `Cenário:` |
| Alternativas | `[ ] A - texto` | `A) texto` |
| Separador após as opções | `---` | `---` |
| Separador entre cenário e opções | `---` | **nenhum** (só uma linha em branco) |

Checklist antes de escrever o arquivo:

- [ ] O bloco em inglês foi copiado **sem alterações** de `NNN-card.md`
- [ ] O rótulo PT-BR é `Cenário:` — nunca `Scenario:`, nunca ausente
- [ ] As opções PT-BR usam `A)` `B)` `C)` `D)` — nunca `[ ] A -`, nunca `TRANSLATED_OPTION_A:`
- [ ] **Nenhum** identificador de placeholder (`TRANSLATED_QUESTION:`, `TRANSLATED_OPTION_X:`)
      aparece no arquivo — esses nomes são apenas conceituais, jamais texto literal de saída
- [ ] Não há `---` entre `Cenário:` e as opções PT-BR
- [ ] As 4 seções seguintes existem com os títulos exatos, na ordem:
      `### EXPLANATION (TECH LEAD)` → `### 🚸 CHILDREN EXPLANATION` → `### CORRECT ANSWER`
- [ ] Cada seção é separada por `---` isolado em sua própria linha
- [ ] Os três placeholders usam a forma literal `[PLACEHOLDER - Será preenchido pelo agente <nome>]`

> **Nota sobre `CORRECT ANSWER`:** quem preenche é o `card-enricher-tech`, e o formato é
> `[ ] X - <texto da alternativa em INGLÊS>` (o mesmo texto do bloco do topo, não a tradução).
> O `card-translator` apenas deixa o placeholder.

---

## Exemplo completo preenchido (card 001)

```markdown
Scenario: Your agent needs to insert a new helper function into the middle of a 150-line utility module, between two existing functions.

---

[ ] A - Use Edit with an extremely long `old_string` capturing 30+ lines of surrounding context
[ ] B - Use Edit's `replace_all` parameter to target a common pattern near the insertion point
[ ] C - Use Bash to append the function definition to the end of the file using a heredoc
[ ] D - Use Read to load the file, add the function at the appropriate location, then Write the updated file

---

### TRANSLATED QUESTION

Cenário: Seu agente precisa inserir uma nova função auxiliar no meio de um módulo utilitário de 150 linhas, entre duas funções existentes.

A) Usar Edit com um `old_string` extremamente longo capturando 30+ linhas de contexto ao redor
B) Usar o parâmetro `replace_all` do Edit para direcionar um padrão comum próximo ao ponto de inserção
C) Usar Bash para anexar a definição da função ao final do arquivo usando um heredoc
D) Usar Read para carregar o arquivo, adicionar a função no local apropriado, então Write do arquivo atualizado

---

### EXPLANATION (TECH LEAD)

[PLACEHOLDER - Será preenchido pelo agente card-enricher-tech]

---

### 🚸 CHILDREN EXPLANATION

[PLACEHOLDER - Será preenchido pelo agente card-enricher-kids]

---

### CORRECT ANSWER

[PLACEHOLDER - Será preenchido pelo agente card-enricher-tech]
```

---

## Erros reais já cometidos (não repetir)

| Card | Erro | Correto |
|---|---|---|
| 003 | Usou `Scenario:` no bloco PT-BR e `---` extra entre cenário e opções | `Cenário:` + linha em branco |
| 003/004 | Usou `[ ] A -` nas opções PT-BR | `A)` |
| 004 | Omitiu o rótulo `Cenário:` | Sempre incluir |
| 005 | Escreveu `TRANSLATED_OPTION_A:` literalmente no arquivo | `A)` |
