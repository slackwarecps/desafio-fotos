# Arquitetura: Pipeline de 4 Agentes com Persistência Progressiva

## Visão Geral

O pipeline de geração de cards enriquecidos agora funciona com **persistência progressiva**: cada agente especializado lê o arquivo enriquecido do estágio anterior, adiciona sua contribuição, e persiste o resultado **diretamente no arquivo final** (`NNN-enriched-card.md`).

**Benefícios:**
- ✅ Sem arquivos temporários intermediários
- ✅ Cada estágio deixa o arquivo progressivamente enriquecido
- ✅ Coordenador pode acompanhar visualmente o progresso
- ✅ Recuperação graceful se um agente falhar

---

## Fluxo de Execução (Novo)

### Para Card NNN:

```
Coordenador (esta skill)
  │
  ├─ Stage 1: Parser
  │  └─ Input: card_number + raw_text (do TSV)
  │  └─ Output: NNN-card.md
  │  └─ Status: PARSED NNN OK
  │
  ├─ Stage 2: Translator
  │  └─ Input: card_number + card_path (NNN-card.md)
  │  └─ Lê: NNN-card.md (pergunta + opções em inglês)
  │  └─ Cria/Atualiza: NNN-enriched-card.md com:
  │     • Scenario + Options (EN)
  │     • TRANSLATED QUESTION (PT-BR)
  │     • Placeholders vazios para Tech + Kids + Correct Answer
  │  └─ Status: TRANSLATED NNN OK (CREATED/UPDATED)
  │
  ├─ Stage 3: Tech Enricher
  │  └─ Input: card_number + card_path + enriched_path
  │  └─ Lê: NNN-card.md (referência) + NNN-enriched-card.md (já tem Translated)
  │  └─ Atualiza: NNN-enriched-card.md adicionando:
  │     • EXPLANATION (TECH LEAD) — análise técnica profunda (4 partes)
  │     • CORRECT ANSWER — letra + texto da alternativa correta
  │  └─ Status: ENRICHED_TECH NNN OK (UPDATED)
  │
  ├─ Stage 4: Kids Enricher
  │  └─ Input: card_number + card_path + enriched_path
  │  └─ Lê: NNN-card.md (referência) + NNN-enriched-card.md (já tem Translated + Tech)
  │  └─ Atualiza: NNN-enriched-card.md adicionando:
  │     • 🚸 CHILDREN EXPLANATION — linguagem acessível (4 partes)
  │  └─ Status: ENRICHED_KIDS NNN OK (FINAL)
  │
  └─ Card NNN está COMPLETO! ✅
```

**Resultado Final em `NNN-enriched-card.md`:**
```markdown
Scenario: [pergunta em inglês]

---

[ ] A - [opção A]
[ ] B - [opção B]
[ ] C - [opção C]
[ ] D - [opção D]

---

### TRANSLATED QUESTION

[Pergunta traduzida PT-BR]

A) [Opção A traduzida]
B) [Opção B traduzida]
C) [Opção C traduzida]
D) [Opção D traduzida]

---

### EXPLANATION (TECH LEAD)

[Análise técnica profunda com 4 partes]

---

### 🚸 CHILDREN EXPLANATION

[Explicação acessível com 4 partes]

---

### CORRECT ANSWER

[X] [Letra] - [Texto completo da alternativa correta]
```

---

## Alterações nos Agentes

### 1. card-parser.md
- ✅ **Sem alterações** — já cria apenas `NNN-card.md`

### 2. card-translator.md
- ✅ **JÁ ATUALIZADO** — cria/atualiza `NNN-enriched-card.md` com TRANSLATED QUESTION

### 3. card-enricher-tech.md
- ✅ **ATUALIZADO** — agora:
  - Lê `NNN-enriched-card.md` (em vez de arquivo temp)
  - Atualiza o arquivo adicionando EXPLANATION (TECH LEAD) + CORRECT ANSWER
  - Status: `ENRICHED_TECH NNN OK (UPDATED)`

### 4. card-enricher-kids.md
- ✅ **ATUALIZADO** — agora:
  - Lê `NNN-enriched-card.md` (em vez de arquivo temp)
  - Atualiza o arquivo adicionando 🚸 CHILDREN EXPLANATION
  - Status: `ENRICHED_KIDS NNN OK (FINAL)`

### 5. gerador-de-reports.md
- ✅ **Pronto para ser chamado** — lê todos os `*-enriched-card.md` do diretório
- Gera PDF com estrutura completa (capa + índice + cards)
- Output: `Report dd-mm-yyyy hh:mm:ss.pdf`

---

## Fluxo do Coordenador (Pseudocódigo)

```python
# Pipeline sequencial para cada card
for card_num in pending_cards:
    
    # Stage 1: Parser
    agent_parser = spawn_agent("card-parser", 
        card_number=card_num, raw_text=tsv_data[card_num])
    wait_for(agent_parser, "PARSED <NNN> OK")
    
    # Stage 2: Translator
    agent_translator = spawn_agent("card-translator",
        card_number=card_num, card_path=f"{card_num}-card.md")
    wait_for(agent_translator, "TRANSLATED <NNN> OK")
    
    # Stage 3: Tech Enricher
    agent_tech = spawn_agent("card-enricher-tech",
        card_number=card_num, 
        card_path=f"{card_num}-card.md",
        enriched_path=f"{card_num}-enriched-card.md")
    wait_for(agent_tech, "ENRICHED_TECH <NNN> OK")
    
    # Stage 4: Kids Enricher
    agent_kids = spawn_agent("card-enricher-kids",
        card_number=card_num,
        card_path=f"{card_num}-card.md",
        enriched_path=f"{card_num}-enriched-card.md")
    wait_for(agent_kids, "ENRICHED_KIDS <NNN> OK (FINAL)")
    
    # Card completo!
    log(f"Card {card_num} completo ✓")

# Após TODOS os cards completos (ou ao final da execução)
if all_completed_cards > 0:
    log("Disparando gerador de reports...")
    agent_reports = spawn_agent("gerador-de-reports",
        cards_dir="outputs/cards-enriquecidos-forms/")
    wait_for(agent_reports, "REPORT OK")
    log(f"PDF gerado: Report dd-mm-yyyy hh:mm:ss.pdf")
```

---

## Exemplo de Execução

### Comando: `/gerar-cards-enriquecidos-do-forms 1`

**Saída esperada:**

```
🚀 Iniciando processamento de 1 card (pipeline de 4 agentes orquestrados)

📖 Lendo formularios/formulario.tsv... ✓
  - 60 perguntas no total
  - Determinando escopo: próximo card (001)

🔍 Verificando idempotência (AND):
  - 001: nenhum arquivo anterior → executar 4 estágios

⚙️  Disparando pipeline...

Stage 1: Parser
  - 14:23:45 Parser 001 iniciado...
  - 14:23:50 Parser 001 completo ✓
  - Criado: 001-card.md

Stage 2: Translator
  - 14:23:50 Translator 001 iniciado...
  - 14:23:55 Translator 001 completo ✓
  - Criado/Atualizado: 001-enriched-card.md com TRANSLATED QUESTION ✓

Stage 3: Tech Enricher
  - 14:23:55 Tech Enricher 001 iniciado...
  - 14:24:10 Tech Enricher 001 completo ✓
  - Atualizado: 001-enriched-card.md com EXPLANATION (TECH LEAD) + CORRECT ANSWER ✓

Stage 4: Kids Enricher
  - 14:24:10 Kids Enricher 001 iniciado...
  - 14:24:25 Kids Enricher 001 completo ✓
  - Atualizado: 001-enriched-card.md com 🚸 CHILDREN EXPLANATION ✓

✅ Card 001 COMPLETO!

📊 Estatísticas:
  - Cards enriquecidos nesta execução: 1
  - Ainda pendentes: 59

📁 Arquivo Final:
  - outputs/cards-enriquecidos-forms/001-enriched-card.md (9.5 KB)

✨ Próximo: /gerar-cards-enriquecidos-do-forms 5 (processar próximos 5 cards)
```

---

## Chamada do Gerador de Reports

Quando **todos os 60 cards estiverem completos**, ou ao final de uma execução com cards completados, o coordenador chama automaticamente:

```
Disparando gerador de PDF com todos os cards completos...

  - 14:35:00 Report Generator iniciado...
  - 14:35:45 Report Generator completo ✓
  
PDF gerado: Report 15-08-2026 14:35:45.pdf

📁 Localização: outputs/Report 15-08-2026 14:35:45.pdf
   Tamanho: ~2.5 MB
   Cards inclusos: 60
   Estrutura: Capa + Índice + 60 Cards + Rodapé
```

---

## Vantagens da Arquitetura Persistente

| Aspecto | Antes | Agora |
|---------|-------|-------|
| **Arquivos temporários** | Sim (4 por card) | Não |
| **Progresso visível** | Apenas ao final | A cada estágio ✓ |
| **Recuperação de falha** | Reprocessar tudo | Continuar do próximo estágio ✓ |
| **Rastreabilidade** | Intermediários perdidos | Arquivo progressivo ✓ |
| **Consolidação** | Necessária (coordenador) | Cada agente faz ✓ |
| **Relatório final** | Manual | Automático ✓ |

---

## Logging e Monitoramento

Todos os eventos são registrados **em tempo real** no chat E no arquivo `desafio.log`:

```
--- Execução iniciada em 2026-08-15 14:23:45 (escopo: 1 card) ---
14:23:45 Parser 001 iniciado...
14:23:50 Parser 001 completo ✓
14:23:50 Translator 001 iniciado...
14:23:55 Translator 001 completo ✓
14:23:55 Tech Enricher 001 iniciado...
14:24:10 Tech Enricher 001 completo ✓
14:24:10 Kids Enricher 001 iniciado...
14:24:25 Kids Enricher 001 completo ✓
14:24:25 Card 001 COMPLETO! ✓
14:35:00 Report Generator iniciado...
14:35:45 Report Generator completo ✓
--- Execução concluída em 2026-08-15 14:35:45 ---
```

---

## Próximos Passos

1. ✅ Atualizar `card-enricher-tech.md` → Feito
2. ✅ Atualizar `card-enricher-kids.md` → Feito
3. ⏳ Atualizar coordenador para usar novo fluxo
4. ⏳ Testar com novo pipeline (reiniciar card 002)
5. ⏳ Configurar disparo automático do gerador-de-reports
