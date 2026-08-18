---
name: gerar-cards-enriquecidos-do-forms
description: Gera cartões enriquecidos e didáticos para flashcards SRS a partir das perguntas em formulario.tsv, usando orquestração paralela de 5 agentes especializados (parser, translator, tech-enricher, kids-enricher, gerador-de-reports) com teto de 5 agentes simultâneos e gerar um pdf ao final de tudo.
---

## COORDENADOR — INSTRUÇÕES DE EXECUÇÃO

Você é o coordenador desta skill. Sua missão é orquestrar 5 subagentes especializados para transformar perguntas TSV em flashcards enriquecidos e depois em um report em PDF.

### Fase 1: Parsear Argumentos e Validar Modo

Analise os argumentos passados:
- **Nenhum argumento**: Modo 1 (processar TODAS as perguntas pendentes)
- **Um número** (ex: `5`): Modo 2 (processar APENAS pergunta 5 = 005-card.md + 005-enriched-card.md)
- **Dois números** (ex: `10 20`, `de 10 a 20`): Modo 3 (processar intervalo pergunta 10 até 20, inclusive ambas)

Se argumentos forem inválidos (texto ao invés de número, intervalo ilógico, etc), rejeite com mensagem clara.

### Fase 2: Ler e Validar Arquivo TSV

1. Abra `formularios/formulario.tsv`
2. Verifique que tem cabeçalho na linha 1
3. Conte linhas de dados: `N = total_linhas - 1` (exclui cabeçalho)
4. Extraia o mapa: linha 2 → card 001, linha 3 → card 002, ..., linha N+1 → card NNN (com zero-padding de 3 dígitos)
5. Para Modo 2 e 3: valide que números estão entre 1 e N

### Fase 3: Aplicar AND Rule (Idempotência)

Para CADA pergunta no escopo (Modo 1, 2 ou 3):
- Verifique se AMBOS existem: `outputs/cards-enriquecidos-forms/NNN-card.md` E `outputs/cards-enriquecidos-forms/NNN-enriched-card.md`
- **Se AMBOS existem**: PULAR (marque como "idempotência — pulado")
- **Se nenhum ou apenas um existe**: marque para processar (4 estágios: parser → translator → tech → kids)

### Fase 4: Orquestração do Pipeline (Máx 5 Agentes Simultâneos)

Para CADA pergunta a processar:

**Estágio 1 (Parser):** 
- Disparar `Agent(subagent_type: "card-parser", prompt: "NNN=005, raw_text=...")`
- Aguardar resposta com status "PARSED NNN OK"
- Se falhar: marque erro e continue

**Estágio 2 (Translator):**
- Disparar `Agent(subagent_type: "card-translator", prompt: "NNN=005, card_path=...")`
- Aguardar resposta com status "TRANSLATED NNN OK"

**Estágio 3 (Tech Enricher):**
- Disparar `Agent(subagent_type: "card-enricher-tech", prompt: "NNN=005, enriched_path=...")`
- Aguardar resposta com status "ENRICHED_TECH NNN OK"

**Estágio 4 (Kids Enricher):**
- Disparar `Agent(subagent_type: "card-enricher-kids", prompt: "NNN=005, enriched_path=...")`
- Aguardar resposta com status "ENRICHED_KIDS NNN OK"

**Restrição de Paralelismo:**
- Máximo 5 agentes podem estar em voo SIMULTANEAMENTE
- Cada pergunta passa por 4 estágios em SEQUÊNCIA (parser → translator → tech → kids)
- DIFERENTES perguntas rodam em PARALELO
- Quando um agente termina, dispare o próximo da fila (ou próximo estágio da mesma pergunta)

### Fase 5: Integração com Logging

Use `logging_helper.sh` para sincronizar logs:
```bash
source .claude/skills/gerar-cards-enriquecidos-do-forms/logging_helper.sh

log_start "N cards"  # No início
log_agent_dispatch "card-parser" "005"  # Ao disparar
log_agent_complete "card-parser" "005" "OK"  # Ao completar
log_consolidating "005"  # Antes de consolidar
log_consolidated "005"  # Após consolidar
log_end  # No final
```

Garanta que CADA linha seja gravada NO CHAT E NO ARQUIVO `desafio.log` com timestamp — 100% sincronizados.

### Fase 6: Disparar Gerador-de-Reports (Obrigatório)

Assim que o ÚLTIMO kids-enricher terminar (status "ENRICHED_KIDS NNN OK") E não houver mais agentes em voo:

```bash
total_enriquecidos=$(ls outputs/cards-enriquecidos-forms/*-enriched-card.md 2>/dev/null | wc -l)

if [ "$total_enriquecidos" -gt 0 ]; then
    Agent(subagent_type: "gerador-de-reports", prompt: "cards_dir=outputs/cards-enriquecidos-forms/")
    Aguardar resposta com status "REPORT ... OK"
    log_agent_complete "gerador-de-reports" "XXX-YYY" "OK"
else
    log_info "Nenhum card enriquecido disponível — PDF pulado"
fi
```

**IMPORTANTE:** O PDF contém EXATAMENTE os `*-enriched-card.md` existentes no diretório, NÃO somente os dessa rodada. Se há 15 cards enriquecidos, o PDF terá 15 — não há número mágico.

### Fase 7: Gerar Resumo Final

Após o PDF (ou se nenhum card enriquecido), print:
```
✅ PROCESSAMENTO CONCLUÍDO

📊 Estatísticas:
  - Pulados por idempotência: N
  - Cards enriquecidos nesta execução: N
  - Falhas permanentes: N
  - Ainda pendentes: N
```

### Fase 8: Status Final

Log de conclusão com timestamp e caminho do PDF (se gerado).

---

# Skill: Gerar Cards Enriquecidos a partir do Formulário TSV (Pipeline de 4 Agentes)

Implementação da skill que automatiza a geração de flashcards enriquecidos a partir de perguntas armazenadas em `formularios/formulario.tsv`, usando um coordenador que orquestra **4 subagentes especializados** em paralelo, com teto de 5 agentes simultâneos.

Pipeline de 4 etapas:
1. **Parser** → extrai pergunta e opções, cria card simples
2. **Translator** → traduz para PT-BR
3. **Enricher Tech** → análise técnica profunda (EXPLANATION TECH LEAD)
4. **Enricher Kids** → análise acessível lúdica (🚸 CHILDREN EXPLANATION)

Cada linha passa por 4 estágios em sequência, mas linhas diferentes rodam em paralelo (máx 5 agentes em voo).

---

## Input e Escopo

### Arquivo de entrada
- **Localização:** `formularios/formulario.tsv` (na raiz do repositório)
- **Estrutura:**
  - Linha 1: cabeçalho (`Carimbo de data/hora`, `perguntaRaw`, `Coluna 1`)
  - Linhas 2..N+1: **N linhas de dados** — `N` é sempre **contado do arquivo**, nunca assumido
  - Col 2 (`perguntaRaw`): texto bruto com enunciado + 4 opções coladas (sem separador)
  - Col 3 (`Coluna 1`): índice sequencial 1–N — **NÃO é o gabarito**

> **`N` não é fixo.** Hoje o TSV tem 60 linhas, mas esse número é apenas o estado atual do
> arquivo. Todo cálculo (escopo, idempotência, total do deck, PDF) deriva de
> `N = linhas de dados do TSV`. Se o formulário crescer para 80 ou encolher para 12,
> nada nesta skill precisa mudar.

### Numeração de cards
- Linha 2 do TSV → `001-card.md` + `001-enriched-card.md`
- Linha 3 do TSV → `002-card.md` + `002-enriched-card.md`
- ... (sequencial)
- Linha N+1 do TSV → `NNN-card.md` + `NNN-enriched-card.md` (NNN = N com zero-padding de 3 dígitos)

### Escopo (qual pergunta processar)

**3 modos possíveis:**

1. **Todas as perguntas (sem argumento)**
   - Comando: `/gerar-cards-enriquecidos-do-forms`
   - Processa **todas as perguntas ainda pendentes** (que não têm ambos card simples + enriquecido)

2. **Pergunta específica (um número)**
   - Comando: `/gerar-cards-enriquecidos-do-forms 5`
   - Processa **apenas a pergunta número 5** (NNN=005)
   - Independente de já existir ou não

3. **Intervalo de perguntas (dois números)**
   - Comando: `/gerar-cards-enriquecidos-do-forms 10 20`
   - Processa **perguntas de 10 a 20** (inclusive ambos)
   - Exemplo: `/gerar-cards-enriquecidos-do-forms 1 10` (1 a 10)
   - Exemplo: `/gerar-cards-enriquecidos-do-forms 15 20` (15 a 20)

---

## Idempotência (Regra AND)

Para cada pergunta NNN:
- **Se AMBOS os arquivos já existem** (`NNN-card.md` E `NNN-enriched-card.md`): **PULAR COMPLETAMENTE**
- **Se só alguns estágios foram completados** (ex: card simples existe, mas enriquecido não): completar a partir do estágio seguinte
- **Se nenhum existe**: processar todos os 4 estágios

---

## Arquitetura e Fluxo (PERSISTÊNCIA PROGRESSIVA)

```
Coordenador (esta skill)
  │
  ├─ Fase 1: Ler formularios/formulario.tsv → mapa NNN → perguntaRaw
  │
  ├─ Fase 2: Aplicar escopo e idempotência, classificar cada linha
  │
  ├─ Fase 3: Orquestra subagentes em pipeline sequencial (máx 5 simultâneos)
  │    │
  │    ├──▶ Agent(subagent_type: "card-parser", prompt: NNN + perguntaRaw)
  │    │     → cria outputs/cards-enriquecidos-forms/NNN-card.md
  │    │     → devolve "PARSED NNN OK"
  │    │
  │    │  ao receber PARSED OK:
  │    │  ──▶ Agent(subagent_type: "card-translator", prompt: NNN + card_path)
  │    │      → cria/atualiza NNN-enriched-card.md com TRANSLATED QUESTION (PT-BR)
  │    │      → devolve "TRANSLATED NNN OK (CREATED/UPDATED)"
  │    │
  │    │   ao receber TRANSLATED OK:
  │    │   ──▶ Agent(subagent_type: "card-enricher-tech", prompt: NNN + enriched_path)
  │    │       → atualiza NNN-enriched-card.md com EXPLANATION (TECH LEAD) + CORRECT ANSWER
  │    │       → devolve "ENRICHED_TECH NNN OK (UPDATED)"
  │    │
  │    │    ao receber ENRICHED_TECH OK:
  │    │    ──▶ Agent(subagent_type: "card-enricher-kids", prompt: NNN + enriched_path)
  │    │        → atualiza NNN-enriched-card.md com 🚸 CHILDREN EXPLANATION
  │    │        → devolve "ENRICHED_KIDS NNN OK (FINAL)"
  │    │
  │    └─ Mantém fila de até 5 agentes em voo; conforme um termina, aciona o próximo
  │
  ├─ Fase 4: SEMPRE disparar gerador-de-reports (etapa obrigatória)
  │    │
  │    └─ Assim que o ÚLTIMO card-enricher-kids da execução devolver
  │       "ENRICHED_KIDS NNN OK (FINAL)" e não houver mais agentes em voo:
  │       ──▶ Agent(subagent_type: "gerador-de-reports", prompt: cards_dir)
  │           → gera outputs/Report dd-mm-yyyy hh:mm:ss.pdf
  │           → devolve "REPORT NNN-NNN OK <path>"
  │
  └─ Fase 5: Resumo final (criados / pulados / falhos / pendentes)
```

**IMPORTANTE:** Sem consolidação manual! Cada agente persiste progressivamente o arquivo final.

### Regra de Paralelismo
- **Máximo 5 agentes simultâneos** (contabiliza todos: parsers, translators, enrichers)
- Cada linha passa por 4 estágios em sequência (parser → translator → tech → kids)
- Linhas diferentes rodam em paralelo
- Quando um estágio completa, o coordenador dispara o próximo estágio daquela linha (ou a próxima linha se houver vaga)

### Regra de Logging Obrigatório (USANDO logging_helper.sh)

O coordenador **DEVE** usar `logging_helper.sh` para garantir logging sincronizado entre chat e arquivo.

**Arquivo de Log:**
- **Localização:** `desafio.log` na raiz do repositório
- **Modo:** Append (nunca sobrescrever — histórico acumulado de todas as rodadas)
- **Escrita:** Via funções em `logging_helper.sh` (automático + arquivo)

**Como usar logging_helper.sh no coordenador:**

```bash
# No início do script coordenador:
source .claude/skills/gerar-cards-enriquecidos-do-forms/logging_helper.sh

# Iniciar execução
log_start "N cards"

# Disparar agente
log_agent_dispatch "card-parser" "002"

# Agente completou com sucesso
log_agent_complete "card-parser" "002" "OK"

# Agente falhou
log_agent_complete "card-parser" "002" "Erro ao ler TSV"

# Consolidação
log_consolidating "002"
log_consolidated "002"

# Finalizar
log_end
```

**Garantias de logging_helper.sh:**
- ✓ Cada linha tem timestamp HH:MM:SS automaticamente
- ✓ Chat e arquivo **100% sincronizados** (idêntico)
- ✓ Append mode (nunca sobrescreve)
- ✓ Funções reutilizáveis: log_start, log_agent_dispatch, log_agent_complete, log_consolidating, log_consolidated, log_end, log_line

**Documentação completa:** Ver `LOGGING_GUIDE.md`

---

## Subagentes Utilizados

### 1. `card-parser` (`.claude/agents/card-parser.md`)
**Input:** `card_number`, `raw_text`
**Output:** arquivo `outputs/cards-enriquecidos-forms/NNN-card.md`
**Status:** `PARSED NNN OK` ou `PARSED NNN FAILED reason: ...`

### 2. `card-translator` (`.claude/agents/card-translator.md`)
**Input:** `card_number`, `card_path`
**Output:** Atualiza `NNN-enriched-card.md` com `TRANSLATED QUESTION` (PT-BR)
**Status:** `TRANSLATED NNN OK (CREATED)` ou `TRANSLATED NNN OK (UPDATED)` ou `TRANSLATED NNN FAILED reason: ...`

### 3. `card-enricher-tech` (`.claude/agents/card-enricher-tech.md`)
**Input:** `card_number`, `card_path`, `enriched_path`
**Output:** Atualiza `NNN-enriched-card.md` com `EXPLANATION (TECH LEAD)` + `CORRECT ANSWER`
**Status:** `ENRICHED_TECH NNN OK (UPDATED)` ou `ENRICHED_TECH NNN FAILED reason: ...`

### 4. `card-enricher-kids` (`.claude/agents/card-enricher-kids.md`)
**Input:** `card_number`, `card_path`, `enriched_path`
**Output:** Atualiza `NNN-enriched-card.md` com `🚸 CHILDREN EXPLANATION` (FINAL)
**Status:** `ENRICHED_KIDS NNN OK (FINAL)` ou `ENRICHED_KIDS NNN FAILED reason: ...`

---

## Workflow Detalhado

### Fase 1: Preparação

1. Ler `formularios/formulario.tsv`
2. Validar cabeçalho (3 colunas esperadas)
3. **Contar linhas de dados → `N`** (não presuma 60; use o que o arquivo tiver)
4. Montar mapa: `{ NNN_string: perguntaRaw_text }` (com exatamente `N` entradas)
5. Validar escopo (argumento numérico ou "todas as pendentes")

### Fase 2: Classificação por Idempotência

Para cada NNN de 001 até `N`:
- Se `NNN-card.md` E `NNN-enriched-card.md` existem → `skip`
- Se nenhum existe → `parse_translate_enrich_all_4_stages`
- Se só alguns estágios foram feitos → `continue_from_next_stage`

### Fase 3: Orquestração Paralela com Teto de 5 Agentes

**Algoritmo de fila (pseudocódigo):**

```python
agent_in_flight = {}  # { NNN: (current_stage, agent_id, retry_count) }
work_queue = [NNN para os quais classificação != "skip"]

# Linha separadora de início (impressa no chat e gravada em desafio.log)
print_log(f"--- Execução iniciada em {now()} (escopo: {len(work_queue)} pendentes) ---")

while work_queue ou agent_in_flight:
  
  # Disparar novos agentes até o teto (máx 5)
  while len(agent_in_flight) < 5 AND work_queue:
    NNN = work_queue.pop(0)
    
    # Determinar qual estágio disparar
    if deve_parsear(NNN):
      print_log(f"{timestamp()} Parser {NNN} iniciado...")
      agent_id = Agent(subagent_type="card-parser", prompt=...)
      agent_in_flight[NNN] = ("parse", agent_id, 0)
    elif deve_traduzir(NNN):
      print_log(f"{timestamp()} Translator {NNN} iniciado...")
      agent_id = Agent(subagent_type="card-translator", prompt=...)
      agent_in_flight[NNN] = ("translate", agent_id, 0)
    elif deve_enriquecer_tech(NNN):
      print_log(f"{timestamp()} Tech Enricher {NNN} iniciado...")
      agent_id = Agent(subagent_type="card-enricher-tech", prompt=...)
      agent_in_flight[NNN] = ("enrich_tech", agent_id, 0)
    elif deve_enriquecer_kids(NNN):
      print_log(f"{timestamp()} Kids Enricher {NNN} iniciado...")
      agent_id = Agent(subagent_type="card-enricher-kids", prompt=...)
      agent_in_flight[NNN] = ("enrich_kids", agent_id, 0)
    else:
      # Todos os 4 estágios completos, consolidar
      print_log(f"{timestamp()} Consolidando {NNN}...")
      consolidar(NNN)
      print_log(f"{timestamp()} {NNN} consolidado ✓")
      continue
  
  # Coletar notificações de conclusão
  for NNN, (stage, agent_id, retry_count) in agent_in_flight.items():
    if task completion notification para agent_id:
      
      # Parse status line da resposta
      if stage == "parse" and "PARSED NNN OK" in response:
        # OK, remover de in_flight e voltar à fila para próximo estágio
        print_log(f"{timestamp()} Parser {NNN} completo ✓")
        remove NNN from agent_in_flight
        work_queue.append(NNN)  # volta para translator
      
      elif stage == "parse" and "PARSED NNN FAILED" in response:
        if retry_count < 1:
          # Retry
          print_log(f"{timestamp()} Parser {NNN} retry (tentativa {retry_count+1}/1)...")
          agent_id = Agent(subagent_type="card-parser", ...)
          agent_in_flight[NNN] = ("parse", agent_id, retry_count+1)
        else:
          # Falha permanente
          print_log(f"{timestamp()} Parser {NNN} FALHOU ❌ — retry esgotado")
          failed_list.append(NNN)
          remove NNN from agent_in_flight
      
      # Padrão similar para translate, enrich_tech, enrich_kids (exemplos omitidos por brevidade)
      elif stage == "translate" and "TRANSLATED NNN OK" in response:
        print_log(f"{timestamp()} Translator {NNN} completo ✓")
        remove NNN from agent_in_flight
        work_queue.append(NNN)
      elif stage == "translate" and "TRANSLATED NNN FAILED" in response:
        print_log(f"{timestamp()} Translator {NNN} FALHOU ❌ — ...")
        failed_list.append(NNN)
        remove NNN from agent_in_flight
      
      # ... (enrich_tech e enrich_kids seguem padrão similar) ...
  
  # Sleep brevemente antes de próxima iteração

# Linha separadora de término
print_log(f"--- Execução concluída em {now()} ---")
```

**Resumo de chamadas `print_log(...)`:**
- `print_log()` imprime no chat **E** faz `Bash: echo "<linha>" >> desafio.log` automaticamente.
- Cada linha é idêntica em ambos (console e arquivo).
- O arquivo `desafio.log` acumula histórico de múltiplas execuções (append mode).

### Fase 4: Consolidação e Resumo Final

Ao término de todos os 4 estágios para uma linha, o coordenador:

1. Lê `/tmp/translated_NNN.txt` (pergunta + opções PT-BR)
2. Lê `/tmp/enriched_tech_NNN.txt` (análise técnica + resposta correta)
3. Lê `/tmp/enriched_kids_NNN.txt` (análise infantil)
4. Consolida tudo em `outputs/cards-enriquecidos-forms/NNN-enriched-card.md` com estrutura:

```markdown
Scenario: [pergunta em inglês, sem alternativas]

---

[ ] A - [opção A em inglês]
[ ] B - [opção B em inglês]
[ ] C - [opção C em inglês]
[ ] D - [opção D em inglês]

---

### TRANSLATED QUESTION

[Pergunta traduzida em PT-BR]

A) [Opção A traduzida]
B) [Opção B traduzida]
C) [Opção C traduzida]
D) [Opção D traduzida]

---

### EXPLANATION (TECH LEAD)

[Conteúdo de /tmp/enriched_tech_NNN.txt]

---

### 🚸 CHILDREN EXPLANATION

[Conteúdo de /tmp/enriched_kids_NNN.txt]

---

### CORRECT ANSWER

[ ] [X] - [Texto completo da alternativa correta]
```

5. Remove arquivos temporários: `/tmp/translated_NNN.txt`, `/tmp/enriched_tech_NNN.txt`, `/tmp/enriched_kids_NNN.txt`
6. Registra sucesso para NNN

Ao final, exibir resumo:

```
✅ PROCESSAMENTO CONCLUÍDO

📊 Estatísticas:
  - Pulados por idempotência: N
  - Cards enriquecidos nesta execução: N
  - Falhas permanentes: N
  - Ainda pendentes: N

🎯 Cards criados:
  - NNN-card.md: 001, 002, ...
  - NNN-enriched-card.md: 001, 002, ...

📁 Localização: outputs/cards-enriquecidos-forms/

✨ Status: [Sucesso total / Completado com falhas]
```

---

## Padrão de Qualidade Esperado

Ver specifications em `.claude/agents/card-parser.md`, `.claude/agents/card-translator.md`, `.claude/agents/card-enricher-tech.md`, `.claude/agents/card-enricher-kids.md`.

---

## Exemplo de Execução Esperada

### Comando: `/gerar-cards-enriquecidos-do-forms 3`

**Saída obrigatória do coordenador** (formato literal exigido, conforme **Regra de Logging Obrigatório** acima):

Cada linha abaixo é impressa no chat **E** gravada em `desafio.log` (exatamente igual em ambos):

```
🚀 Iniciando processamento de 3 perguntas (pipeline de 4 agentes)...

📖 Lendo formularios/formulario.tsv... ✓
  - 60 perguntas no total   ← valor CONTADO do TSV nesta execução, não constante
  - Determinando escopo: próximas 3 pendentes (001, 002, 003)

🔍 Verificando idempotência (AND):
  - 001: parse → translate → tech → kids
  - 002: parse → translate → tech → kids
  - 003: parse → translate → tech → kids

⚙️ Disparando pipeline paralelo (máx 5 agentes simultâneos)...
  - 14:23:45 Parser 001 iniciado...
  - 14:23:46 Parser 002 iniciado...
  - 14:23:50 Parser 001 completo ✓
  - 14:23:50 Translator 001 iniciado...
  - 14:23:51 Parser 003 iniciado...
  - 14:23:55 Parser 002 completo ✓
  - 14:23:55 Translator 002 iniciado...
  - 14:23:56 Parser 003 completo ✓
  - 14:23:56 Translator 003 iniciado...
  - 14:24:00 Translator 001 completo ✓
  - 14:24:00 Tech Enricher 001 iniciado...
  - 14:24:01 Translator 002 completo ✓
  - 14:24:01 Tech Enricher 002 iniciado...
  - 14:24:02 Translator 003 completo ✓
  - 14:24:02 Tech Enricher 003 iniciado...
  - 14:24:15 Tech Enricher 001 completo ✓
  - 14:24:15 Kids Enricher 001 iniciado...
  - 14:24:16 Tech Enricher 002 completo ✓
  - 14:24:16 Kids Enricher 002 iniciado...
  - 14:24:17 Tech Enricher 003 completo ✓
  - 14:24:17 Kids Enricher 003 iniciado...
  - 14:24:30 Kids Enricher 001 completo ✓
  - 14:24:30 Consolidando 001...
  - 14:24:31 Kids Enricher 002 completo ✓
  - 14:24:31 Consolidando 002...
  - 14:24:32 Kids Enricher 003 completo ✓
  - 14:24:32 Consolidando 003...

✅ PROCESSAMENTO CONCLUÍDO

📊 Estatísticas:
  - Pulados por idempotência: 0
  - Cards enriquecidos nesta execução: 3
  - Falhas permanentes: 0
  - Ainda pendentes: 57

🎯 Cards criados:
  - 001-card.md / 001-enriched-card.md ✓
  - 002-card.md / 002-enriched-card.md ✓
  - 003-card.md / 003-enriched-card.md ✓

📁 Localização: outputs/cards-enriquecidos-forms/

📋 Log de execução: desafio.log (arquivo acumulado com histórico de todas as rodadas)

✨ Próxima execução: /gerar-cards-enriquecidos-do-forms 3 (ou deixe vazio para processar os 57 restantes)
```

---

## Referências

- `.claude/agents/card-parser.md` — Spec do parser
- `.claude/agents/card-translator.md` — Spec do translator
- `.claude/agents/card-enricher-tech.md` — Spec do tech enricher
- `.claude/agents/card-enricher-kids.md` — Spec do kids enricher
- `templates/001-enriched-card.md` — Exemplo de card enriquecido final

### Templates de Formato (leitura obrigatória pelos agentes)

- `templates/translated-card-template.md` — Layout canônico da etapa do **translator**
  (bloco EN intacto + `Cenário:` + opções `A)`–`D)`)
- `templates/enriched-sections-template.md` — Layout canônico das etapas dos **enrichers**
  (TECH, KIDS e CORRECT ANSWER), incluindo a regra das **3 alternativas erradas** e o mapa de emojis
- `templates/pdf-report-template.md` — Layout canônico do **PDF** (fonte única, lida tanto pelo
  agente `gerador-de-reports` na Fase 4 quanto pela skill `/exporta-cards-enriquecidos-para-pdf`)

Referência viva do formato final: `outputs/cards-enriquecidos-forms/001-enriched-card.md`.


## Gerador de Reports (Etapa Automática e OBRIGATÓRIA)

### Quando Ativar

**SEMPRE**, ao final de toda execução, assim que o **último `card-enricher-kids` da rodada**
devolver `ENRICHED_KIDS NNN OK (FINAL)` e **não houver mais agentes em voo**.

### O tamanho do deck é DERIVADO, nunca fixo

O PDF contém **exatamente os cards enriquecidos que existirem no diretório** no momento do
disparo. Não há número mágico:

| Cards enriquecidos existentes | PDF gerado |
|---|---|
| 1 | PDF com 1 card (`Card 001/001`) |
| 3 | PDF com 3 cards (`Card 001/003` … `003/003`) |
| 15 (TSV tem 60 linhas, só 15 enriquecidas) | PDF com **15** cards — as 45 linhas não enriquecidas simplesmente não aparecem |
| 15 (TSV tem **1000** linhas) | PDF com **15** cards — o tamanho do TSV não influencia em nada |
| 60 | PDF com 60 cards |
| N (todas as linhas do TSV) | PDF com N cards |
| 0 | **não gera** — pula e loga |

**`60` NÃO é limite nem meta.** O universo é `N = número de linhas de dados do TSV`, e o deck
é o subconjunto `cards enriquecidos ⊆ N` já materializado.

O **N do TSV não entra na conta do PDF** — ele só define quanto trabalho ainda resta. O deck
é montado a partir dos arquivos em `outputs/cards-enriquecidos-forms/`, ponto. TSV com 60 ou
1000 linhas e 15 cards enriquecidos produzem o mesmo PDF: 15 questões.

**Única condição de pular:** o diretório `outputs/cards-enriquecidos-forms/` não contém
nenhum `*-enriched-card.md` (não há o que reportar). Registrar isso no log.

```bash
# Coordenador, após o último ENRICHED_KIDS OK e com a fila de agentes vazia:
source .claude/skills/gerar-cards-enriquecidos-do-forms/logging_helper.sh

total_enriquecidos=$(ls outputs/cards-enriquecidos-forms/*-enriched-card.md 2>/dev/null | wc -l)

if [ "$total_enriquecidos" -gt 0 ]; then
    # faixa = primeiro..último card enriquecido REAL (ex: "001-001", "001-003", "001-060")
    log_agent_dispatch "gerador-de-reports" "$faixa"

    # Dispara SEMPRE — 1 card ou N cards, o gatilho é o mesmo
    spawn_agent("gerador-de-reports", cards_dir="outputs/cards-enriquecidos-forms/")

    wait_for_response("REPORT OK")

    log_agent_complete "gerador-de-reports" "$faixa" "OK"
else
    log_info "Nenhum card enriquecido disponível — gerador-de-reports pulado"
fi
```

**Ordem correta das fases:** Fase 4 (report) acontece **antes** da Fase 5 (resumo final),
para que o caminho do PDF possa ser incluído no resumo apresentado ao usuário.

Se o agente responder `REPORT FAILED`, o coordenador registra a falha no log e segue para a
Fase 5 — a falha do PDF **não** invalida os cards já enriquecidos.

### O Que Faz

O agente `gerador-de-reports` lê todos os `*-enriched-card.md` e gera:

**Output:** `Report dd-mm-yyyy hh:mm:ss.pdf`

**Estrutura do PDF:**
- Capa com metadata (data, total de cards)
- Índice com todas as perguntas
- Todos os cards disponíveis formatados (pergunta EN + PT-BR + explicações + resposta)
- Rodapé com numeração de páginas

---

## Exemplo de Execução Completa

### Comando: `/gerar-cards-enriquecidos-do-forms 3`

**Saída esperada (com logging_helper.sh):**

```
--- Execução iniciada em 2026-08-15 16:52:52 (escopo: 3 cards) ---
16:52:52 Parser 001 iniciado...
16:53:27 Parser 001 completo ✓
16:53:27 Translator 001 iniciado...
16:55:12 Translator 001 completo ✓
16:55:12 Tech Enricher 001 iniciado...
16:56:11 Tech Enricher 001 completo ✓
16:56:11 Kids Enricher 001 iniciado...
16:57:14 Kids Enricher 001 completo ✓
16:57:14 Parser 002 iniciado...
... (cards 002 e 003)
17:15:30 Kids Enricher 003 completo ✓
17:15:30 Disparando gerador de PDF...
17:15:31 Report Generator iniciado...
17:18:45 Report Generator completo ✓
17:18:45 📄 PDF gerado: Report 15-08-2026 17:18:45.pdf
17:18:45 📁 Localização: outputs/Report 15-08-2026 17:18:45.pdf
17:18:45 ✅ PROCESSAMENTO CONCLUÍDO
17:18:45 📊 Estatísticas:
  - Pulados por idempotência: 0
  - Cards enriquecidos nesta execução: 3
  - Falhas permanentes: 0
  - Ainda pendentes: 57
17:15:30 🎯 Cards criados:
  - 001-enriched-card.md ✓
  - 002-enriched-card.md ✓
  - 003-enriched-card.md ✓
--- Execução concluída em 2026-08-15 17:18:45 ---
```

O bloco do gerador de PDF aparece em **todas** as execuções, logo após o último
`Kids Enricher NNN completo ✓` — inclusive em rodadas parciais como esta (3 cards).
O PDF consolida todos os `*-enriched-card.md` presentes no diretório, não só os da rodada.

