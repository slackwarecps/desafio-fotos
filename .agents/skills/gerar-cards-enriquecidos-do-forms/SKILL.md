---
name: gerar-cards-enriquecidos-do-forms
description: Gera cartões enriquecidos e didáticos para flashcards SRS a partir das perguntas em formulario.tsv, com explicações para múltiplos níveis de aprendizado
---

# Skill: Gerar Cards Enriquecidos a partir do Formulário TSV

Implementação da skill que automatiza a geração de flashcards enriquecidos a partir de perguntas armazenadas em `formulario.tsv` (export de Google Forms).

---

## 🎯 Princípio Central: **Etapa Única Contínua**

**Para CADA pergunta processada:**
```
Parsear → Card Simples → Análise → Card Enriquecido → (próxima pergunta)
```

**❌ NÃO FAZER:** Criar todos os cards simples, depois voltar para enriquecer

**✅ FAZER:** Para cada pergunta, terminar completamente (simples + enriquecido) antes de passar para a próxima

---

## Fluxo de Execução — Etapa Única Contínua

**🎯 Princípio:** Para cada pergunta, gerar **AMBOS os cards (simples + enriquecido) em um fluxo único**, sem pausas ou confirmações intermediárias.

### Fase 1: Ler e Validar o TSV

Leia o arquivo `formulario.tsv` localizado na raiz do repositório:
```
/Users/fabiopereira/Desktop/desafio-fotos/formulario.tsv
```

**Estrutura do arquivo:**
- Linha 1: cabeçalho (`Carimbo de data/hora`, `perguntaRaw`, `Coluna 1`)
- Linhas 2–61: dados (60 perguntas)
- Cada linha de dados tem:
  - Col 1 (carimbo): ignorar (metadado temporal)
  - Col 2 (`perguntaRaw`): texto bruto completo com enunciado + 4 opções coladas
  - Col 3 (`Coluna 1`): índice sequencial 1–60 — **NÃO é o gabarito**, apenas um identificador

**Determinação de escopo:**
1. Verificar quantas linhas de dados já foram convertidas (existem pares `NNN-card.md` + `NNN-enriched-card.md` em `outputs/cards-enriquecidos-forms/`)
2. Se a skill foi chamada com argumento numérico (ex: `/gerar-cards-enriquecidos-do-forms 3`), processar as próximas N perguntas **novas**; sem argumento, processar **todas** as pendentes
3. "Já convertida" = ambos os arquivos `NNN-card.md` **E** `NNN-enriched-card.md` existem para aquela posição (mapeamento fixo: linha 2 do TSV → 001, linha 3 → 002, ... linha 61 → 060)

**Mapeamento de numeração:**
- Linha 2 do TSV (1ª pergunta de dados) → `001-card.md` + `001-enriched-card.md`
- Linha 3 do TSV (2ª pergunta de dados) → `002-card.md` + `002-enriched-card.md`
- ...
- Linha 61 do TSV (60ª pergunta de dados) → `060-card.md` + `060-enriched-card.md`

Numeração é **sempre sequencial pela ordem no arquivo**, zero-padded a 3 dígitos.

---

## ⚠️ PRINCÍPIO CRÍTICO: Fluxo Contínuo Sem Pausas

Para **cada pergunta processada**, executar os passos 2a-2e em **sequência ininterrupta**:

```
Para cada pergunta:
  └─ 2a: Verificar se já existe (ambos simples + enriquecido)
      ├─ Se sim → PULAR COMPLETAMENTE e ir próxima pergunta
      ├─ Se não → CONTINUAR (não pausar)
  └─ 2b: Parsear pergunta e opções
      └─ (Não pausar, ir direto para 2c)
  └─ 2c: Criar card simples (NNN-card.md)
      └─ (Não pausar, ir direto para 2d)
  └─ 2d: Analisar e determinar resposta correta
      └─ (Não pausar, ir direto para 2e)
  └─ 2e: Criar card enriquecido (NNN-enriched-card.md)
      └─ (Próxima pergunta)
```

**❌ ERRADO:**
- Criar todos os cards simples primeiro, depois depois voltar para enriquecer

**✅ CORRETO:**
- Para cada pergunta: simples → enriquecido → próxima pergunta

---

### Fase 2: Processar Cada Pergunta (Fluxo Único Contínuo)

**⚠️ IMPORTANTE:** Para cada pergunta, executar os passos 2a-2e **em sequência contínua, sem pausar**. Não criar o card simples e parar — criar AMBOS antes de passar para a próxima pergunta.

#### Passo 2a: Verificar Idempotência
- Se ambos os arquivos `NNN-card.md` **E** `NNN-enriched-card.md` já existem, **PULAR COMPLETAMENTE** esta pergunta
- Passar para a próxima

#### Passo 2b: Parsear Cada `perguntaRaw`

O texto em `perguntaRaw` contém o enunciado completo e as 4 opções coladas **sem separador visível**. As opções vêm no formato: `...to: A.texto_opcao_aB.texto_opcao_bC.texto_opcao_cD.texto_opcao_d`

**Exemplo real do arquivo:**
```
An agent is dropped into an unfamiliar repository and asked to add a feature. The best way to orient without burning context is to: A.Load every file into context so nothing is missed.B.Read the entry points and project structure, then search for the area the feature touches.C.Start editing the first file that looks related.D.Ask the user to explain every file.
```

**Regra de parse:**
1. O enunciado termina imediatamente **antes** do padrão ` A.` (espaço + letra maiúscula A-D + ponto)
2. Cada opção começa em `A.`, `B.`, `C.`, `D.` (maiúscula + ponto)
3. O texto da opção se estende até o próximo padrão `X.` (onde X é a próxima letra, ou fim da string)
4. **Atenção:** usar regex ou split que capture corretamente: o ponto após a letra é a fronteira, não um ponto solto dentro de uma frase
5. **Remover as alternativas do Scenario** — o texto final do Scenario deve conter APENAS a pergunta/cenário, sem as alternativas coladas

**Resultado esperado:**

**Input (TSV perguntaRaw):**
```
An agent is dropped into an unfamiliar repository and asked to add a feature. The best way to orient without burning context is to: A.Load every file into context so nothing is missed.B.Read the entry points and project structure, then search for the area the feature touches.C.Start editing the first file that looks related.D.Ask the user to explain every file.
```

**Output (Parsed):**
```python
question = "An agent is dropped into an unfamiliar repository and asked to add a feature. The best way to orient without burning context is to:"
options = {
    "A": "Load every file into context so nothing is missed.",
    "B": "Read the entry points and project structure, then search for the area the feature touches.",
    "C": "Start editing the first file that looks related.",
    "D": "Ask the user to explain every file."
}
```

⚠️ **Importante:** O `question` deve terminar na questão pura, SEM os prefixos `A.`, `B.`, `C.`, `D.` — essas alternativas ficam apenas na estrutura de `options`, nunca no Scenario final.

#### Passo 2c: Criar Card Simples

Imediatamente após o parse (sem pausar), crie o arquivo `outputs/cards-enriquecidos-forms/NNN-card.md` com a estrutura **EXATA**:

```markdown
Scenario: [Pergunta completa em inglês - SEM ALTERNATIVAS - TUDO NA MESMA LINHA]

---

[ ] A - [Opção A]
[ ] B - [Opção B]
[ ] C - [Opção C]
[ ] D - [Opção D]
```

**IMPORTANTE — Template de Scenario:**

❌ **NÃO FAZER:**
```markdown
Scenario: An agent is dropped into an unfamiliar repository and asked to add a feature. The best way to orient without burning context is to: A.Load every file into context so nothing is missed.B.Read the entry points and project structure, then search for the area the feature touches.C.Start editing the first file that looks related.D.Ask the user to explain every file.
```

✅ **FAZER:**
```markdown
Scenario: An agent is dropped into an unfamiliar repository and asked to add a feature. The best way to orient without burning context is to:
```

**Regras:**
- ❌ NÃO adicione título `# Pergunta 1:` ou similar
- ✅ Comece **DIRETO** com `Scenario: [pergunta pura]`
- ✅ A pergunta completa vai **na mesma linha** após "Scenario:", mas **SEM as alternativas coladas**
- ✅ Separador `---` antes das opções (linha em branco antes e depois)
- ✅ Opções com checkboxes `[ ] A -`, etc., sem o prefixo "A." da entrada TSV (remova o "A." antes de colocar no card)
- ✅ Alternativas NUNCA aparecem no Scenario — aparecem apenas abaixo do `---` como lista de checkboxes

#### Passo 2d: Analisar e Determinar a Resposta Correta

**IMEDIATAMENTE após criar o card simples** (sem pausar), analise a pergunta e as 4 opções para determinar **automaticamente** qual é a resposta correta com base no conhecimento técnico/arquitetural.

**Método:**
1. Use o Claude para analisar a pergunta e propor qual alternativa é a correta
2. Documente o **raciocínio técnico** (qual conceito/padrão a pergunta testa, por que essa alternativa é superior às outras)
3. Armazene a letra correta (A, B, C, ou D) para uso no passo seguinte

**IMPORTANTE:** O valor na coluna `Coluna 1` do TSV (1–60) é **apenas um índice sequencial** e **NÃO É O GABARITO**. Descarte esse valor — a resposta correta deve ser determinada por análise técnica.

#### Passo 2e: Criar Card Enriquecido (Etapa Final do Fluxo)

**SEM PAUSAR** entre os passos anteriores, crie o arquivo `outputs/cards-enriquecidos-forms/NNN-enriched-card.md` seguindo **EXATAMENTE** o template em `templates/001-enriched-card.md`.

**Estrutura obrigatória (em ordem):**

```markdown
Scenario: [Pergunta completa em inglês - SEM ALTERNATIVAS COLADAS]

---

[ ] A - [Opção A]
[ ] B - [Opção B]
[ ] C - [Opção C]
[ ] D - [Opção D]

---

### TRANSLATED QUESTION

[Pergunta traduzida em português - fiel ao significado, não literal]
Alternativas traduzidas:

A) [Opção A traduzida]
B) [Opção B traduzida]
C) [Opção C traduzida]
D) [Opção D traduzida]

---

### EXPLANATION (TECH LEAD)

Explicação:
[Introdução ao conceito/padrão testado - qual arquitetura/decisão a pergunta examina - 2-3 linhas]

Por que a alternativa [X] é a correta:
[Análise técnica PROFUNDA de por que essa é a melhor solução - 5-7 linhas bem estruturadas]

Por que as outras estão erradas:

A) [Análise específica de por que A está errada - 2-3 linhas]
B) [Análise específica de por que B está errada - 2-3 linhas]
C) [Análise específica de por que C está errada - 2-3 linhas]
(Refute TODAS as alternativas incorretas)

Dica importante:
[Padrão recorrente ou conceito-chave a lembrar - conexão com Clean Architecture, SOLID, design patterns - 2-3 linhas]

---

### 🚸 CHILDREN EXPLANATION

Explicação:
[Introdução ao conceito em linguagem acessível, narrativa/analogia se apropriado - 2-3 linhas]

Por que a alternativa [X] é a correta:
[Análise simples de por que funciona - 3-4 linhas, tecnicamente preciso mas sem jargão desnecessário]

Por que as outras estão erradas:

A) [Motivo específico de por que A não funciona - 2-3 linhas]
B) [Motivo específico de por que B não funciona - 2-3 linhas]
C) [Motivo específico de por que C não funciona - 2-3 linhas]
D) [Motivo específico de por que D não funciona - 2-3 linhas]

Dica importante:
[Padrão recorrente, conexão com tópico maior, como esse conceito aparece em outros contextos - 2-3 linhas]

---

### CORRECT ANSWER

[ ] [X] - [Texto completo da alternativa correta]
```

## Padrões de Qualidade

### EXPLANATION (TECH LEAD) — Estrutura Detalhada

**Ordem correta de seções:**

1. **Explicação:**
   - Introduz qual conceito/padrão/decisão arquitetural a pergunta testa
   - Contextualiza o problema testado
   - 2-3 linhas

2. **Por que a alternativa [X] é a correta:**
   - Análise técnica **PROFUNDA** de por que essa é a melhor solução
   - Conecta a princípios/padrões arquiteturais
   - Explica as implicações e benefícios da escolha
   - 5-7 linhas bem estruturadas

3. **Por que as outras estão erradas:**
   - Para **CADA alternativa incorreta**, explicar o **motivo específico**
   - ❌ **Nunca diga apenas:** "Essa alternativa está incorreta"
   - ✅ **Sempre diga:** "Isso falha porque..." ou "Problema: ... Consequência: ..."
   - Conecte o motivo da falha aos conceitos testados
   - 2-3 linhas por alternativa
   - **Refute TODAS as alternativas**

4. **Dica importante:**
   - Padrão recorrente relacionado (ex: "Least Privilege Pattern", "Strangler Fig Pattern")
   - Conexão com Clean Architecture, DDD, SOLID, design patterns
   - Como esse conceito aparece em outros contextos
   - 2-3 linhas

### 🚸 CHILDREN EXPLANATION — Estrutura Detalhada

**Tom:** Acessível para iniciantes/aprendizes. Use analogias, narrativas, emojis quando apropriado.

1. **Explicação:**
   - Introduz o conceito em linguagem simples
   - Use analogias práticas (ex: "é como quando você monta um quebra-cabeça...")
   - Tecnicamente preciso mas sem jargão desnecessário
   - 2-3 linhas (pode ser um pequeno parágrafo narrativo)

2. **Por que a alternativa [X] é a correta:**
   - Análise simples de por que funciona
   - Como um dev iniciante deveria pensar
   - 3-4 linhas, mantendo precisão técnica
   - Use analogias práticas quando apropriado

3. **Por que as outras estão erradas:**
   - Para **CADA alternativa**, explicar o motivo específico
   - ❌ **Nunca diga apenas:** "está errada"
   - ✅ **Padrão:** "A) [Problema específico] — [Consequência prática]"
   - Use emojis se apropriado para clareza (🅰️, 🅱️, ✅, ❌, etc.)
   - 2-3 linhas por alternativa
   - **Refute TODAS as alternativas**

4. **Dica importante:**
   - Padrão recorrente (ex: "Least Privilege Pattern")
   - Conexão com tópicos maiores
   - Como esse conceito aparece em outros contextos
   - 2-3 linhas

### Tradução (TRANSLATED QUESTION)

- ✅ Ser fiel ao significado, **não literal**
- ✅ Manter terminologia técnica em inglês quando apropriado (ex: "tool use", "agentic loop", "MCP server")
- ✅ Naturalizar a linguagem para PT-BR
- ✅ Não traduzir nomes de padrões consolidados

### Análise de Alternativas — Critério de Qualidade

- **Nunca diga apenas:** "Essa alternativa está incorreta"
- **Sempre diga o motivo específico:** "Isso falha porque..." ou "Problema: ... Consequência: ..."
- Conecte o motivo da falha aos conceitos testados

### Fase 3: Resumo Final

Ao final de **TODAS** as perguntas processadas, liste:
- ✅ Cards criados nesta execução (números: NNN-NNN) — indicar a pasta de saída `outputs/cards-enriquecidos-forms/`
- ✅ Total de pares criados (simples + enriquecido) nesta execução
- ✅ Quantos cards já existiam (pulados por idempotência)
- ℹ️ Quantas perguntas do TSV ainda restam pendentes (se houver)
- ✅ Confirmação de sucesso com estatísticas

---

## ⚠️ Notas Importantes

### Idempotência

A skill **não sobrescreve** cards já existentes, a menos que o usuário deseje regenerar explicitamente.

- **Comportamento padrão:** Se `NNN-card.md` e `NNN-enriched-card.md` já existem na pasta de saída, pule aquela pergunta
- **Regeneração:** Se o usuário deletar os arquivos manualmente e rodar a skill novamente, eles serão recriados

Isso protege cards que foram revisados manualmente.

### Numeração Sequencial

- Sempre zero-padded a **3 dígitos**: `001`, `002`, ..., `060`
- Baseada na **ordem no arquivo TSV** (linha 2 → 001, linha 3 → 002, etc.)
- Independente da coluna `Coluna 1` (que é apenas um índice)

### Pasta de Saída Dedicada

- Output vai para **`outputs/cards-enriquecidos-forms/`** (distinto de `outputs/cards-enriquecidos/`, que é usada pela skill de fotos)
- Isso evita colisão de numeração entre as duas fontes (fotos vs. forms)
- Futuras exportações PDF/EPUB podem processar ambas as pastas separadamente, ou pode-se consolidar as numerações se necessário

---

## Referências

Veja exemplos já criados:
- `/Users/fabiopereira/Desktop/desafio-fotos/templates/001-card.md` ← Template de card simples
- `/Users/fabiopereira/Desktop/desafio-fotos/templates/001-enriched-card.md` ← Template de card enriquecido

Esses templates mostram o tom, estrutura e profundidade esperados.

---

## Template de Referência — Scenario Correto vs. Incorreto

### ❌ FORMATO ERRADO (Alternativas coladas no Scenario)

```markdown
Scenario: An agent is dropped into an unfamiliar repository and asked to add a feature. The best way to orient without burning context is to: A.Load every file into context so nothing is missed.B.Read the entry points and project structure, then search for the area the feature touches.C.Start editing the first file that looks related.D.Ask the user to explain every file.
```

**Por que está errado:**
- Alternativas (A, B, C, D) estão coladas ao final do Scenario
- Confunde a pergunta pura com as respostas
- Dificulta leitura e processamento SRS

### ✅ FORMATO CORRETO (Alternativas separadas)

```markdown
Scenario: An agent is dropped into an unfamiliar repository and asked to add a feature. The best way to orient without burning context is to:

---

[ ] A - Load every file into context so nothing is missed.
[ ] B - Read the entry points and project structure, then search for the area the feature touches.
[ ] C - Start editing the first file that looks related.
[ ] D - Ask the user to explain every file.
```

**Por que está correto:**
- Scenario contém apenas a pergunta/cenário puro
- Alternativas aparecem como checkboxes separadas abaixo do `---`
- Estrutura limpa, legível, e pronta para SRS
- Padrão idêntico ao dos cards de fotos (`templates/001-card.md`)

---

## Checklist de Execução — Fluxo Contínuo

### Fase 1: Preparação
- [ ] Ler `formulario.tsv`
- [ ] Validar estrutura (3 colunas, 60 linhas de dados)
- [ ] Determinar quantas perguntas processar (conforme argumento ou todas)
- [ ] Verificar idempotência (quais pares já foram completamente convertidos)

### Fase 2: Para Cada Pergunta Nova (Fluxo Contínuo, sem pausas)
Para cada pergunta não processada:
  - [ ] **Passo 2a:** Verificar se ambos NNN-card.md e NNN-enriched-card.md existem
    - Se sim → PULAR COMPLETAMENTE (ir próxima pergunta)
    - Se não → CONTINUAR (não pausar)
  - [ ] **Passo 2b:** Parsear `perguntaRaw` em enunciado + 4 opções
  - [ ] **Passo 2c:** Criar `NNN-card.md` (card simples)
  - [ ] **Passo 2d:** Analisar e determinar resposta correta
  - [ ] **Passo 2e:** Criar `NNN-enriched-card.md` com:
    - [ ] Pergunta em inglês + opções
    - [ ] TRANSLATED QUESTION (tradução fiel PT-BR)
    - [ ] EXPLANATION (TECH LEAD):
      - [ ] Introdução ao conceito testado
      - [ ] Análise profunda de por que [X] é correta (5-7 linhas)
      - [ ] Por que A/B/C/D estão erradas (motivo específico cada uma)
      - [ ] Dica importante (padrão recorrente)
    - [ ] 🚸 CHILDREN EXPLANATION (mesma estrutura, linguagem acessível)
    - [ ] CORRECT ANSWER com checkbox

### Fase 3: Resumo Final
- [ ] Listar todos os pares de cards criados nesta execução (simples + enriquecido)
- [ ] Total de pares processados (NNN-NNN)
- [ ] Quantos pares foram pulados por idempotência
- [ ] Quantas perguntas ainda restam pendentes
- [ ] Confirmar sucesso e estatísticas
