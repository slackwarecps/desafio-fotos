# Skill: Gerar Cards Enriquecidos a partir do Formulário TSV (Fluxo Multiagente)

Automatiza a geração de flashcards enriquecidos a partir de perguntas armazenadas em `formularios/formulario.tsv` (export de Google Forms), usando um coordenador que orquestra **4 subagentes especializados** em um pipeline paralelo, com teto de 5 agentes simultâneos. 

Pipeline de 4 agentes:
1. **card-parser** → parseia pergunta + opções, cria card simples
2. **card-translator** → traduz para PT-BR, cria seção TRANSLATED QUESTION
3. **card-enricher-tech** → análise técnica, preenche EXPLANATION (TECH LEAD) + CORRECT ANSWER
4. **card-enricher-kids** → explicação acessível, preenche 🚸 CHILDREN EXPLANATION

Explicações estruturadas em **dois níveis**: técnico (Tech Lead) e acessível (Children Explanation).

## 🚀 Uso Rápido

### Invocar a Skill Manualmente

```
/gerar-cards-enriquecidos-do-forms
```

Processa **todas as perguntas novas** do TSV (que ainda não foram convertidas).

### Limitar a Quantidade de Perguntas

```
/gerar-cards-enriquecidos-do-forms 3
```

Processa apenas as **próximas 3 perguntas novas** (útil para teste ou processamento incremental).

**Vantagens:**
- ✅ Processa incrementalmente — não é necessário gerar todas de uma vez
- ✅ Permite revisão do progresso antes de prosseguir
- ✅ Idempotente — não sobrescreve cards já existentes
- ✅ Não depende de memória/contexto do Claude entre execuções

---

## 📋 Processo de Geração — Pipeline Multiagente Paralelo de 4 Agentes

⚠️ **Arquitetura:** Um coordenador orquestra **4 subagentes especializados** em um pipeline paralelo:
- **Máximo 5 agentes simultâneos** (somados: parsers + translators + enrichers)
- Cada pergunta passa por **4 estágios em sequência** (parser → translator → tech enricher → kids enricher), mas **perguntas diferentes rodam em paralelo**
- Idempotência inteligente (AND): se ambos simple + enriched cards existem, pula completamente

### Fluxo de Pipeline de 4 Agentes

Para cada pergunta do TSV:
1. **Verificar idempotência (AND)** — Se **AMBOS** (simples + enriquecido) existem, PULAR completamente
2. **Etapa 1 (se necessário): Parser** — `card-parser` extrai pergunta + 4 opções, cria `NNN-card.md`
3. **Etapa 2: Translator** — `card-translator` traduz para PT-BR, cria seção `TRANSLATED QUESTION`, estrutura `NNN-enriched-card.md` com placeholders
4. **Etapa 3: Tech Enricher** — `card-enricher-tech` analisa, determina resposta correta, preenche `EXPLANATION (TECH LEAD)` + `CORRECT ANSWER`
5. **Etapa 4: Kids Enricher** — `card-enricher-kids` cria explicação acessível, preenche `🚸 CHILDREN EXPLANATION`
6. **Card Completo** — Todas as 5 seções preenchidas: EN + PT-BR + Tech + Kids + Answer
7. **Próxima Pergunta** — Enquanto pergunta N está no enricher de kids, pergunta N+1 pode estar no parser

```
Pergunta 001 → Parser (5s) → Translator (18s) → Tech Enricher (33s) → Kids Enricher (30s) → Completo! (86s)
Pergunta 002 → (paralelo) → Parser (5s) → Translator (18s) → Tech Enricher (33s) → Kids Enricher (30s) → Completo! (86s)
...
```

❌ **ERRADO:** Processar sequencialmente (uma pergunta inteira por vez na mesma sessão)
✅ **CORRETO:** Paralelismo com especialização (4 agentes independentes, múltiplas perguntas em voo)

---

## 📁 Estrutura de Saída

```
desafio-formularios/
├── formularios/
│   └── formulario.tsv                  # Arquivo fonte (Google Forms export)
└── outputs/
    └── cards-enriquecidos-forms/       # ← Saída desta skill
        ├── 001-card.md                 # Card simples
        ├── 001-enriched-card.md        # Card enriquecido
        ├── 002-card.md
        ├── 002-enriched-card.md
        ├── 003-card.md
        └── 003-enriched-card.md
```

**Nota:** Entrada corrigida para `formularios/formulario.tsv` (não raiz). Saída separada em `cards-enriquecidos-forms/` (não em `cards-enriquecidos/`, que é para fotos). Evita colisão de numeração.

---

## 🎯 Estrutura Corrigida dos Cards

### Card Simples (NNN-card.md)

```markdown
Scenario: [Pergunta completa em inglês - TUDO NA MESMA LINHA]

---

[ ] A - [Opção A]
[ ] B - [Opção B]
[ ] C - [Opção C]
[ ] D - [Opção D]
```

**Regras:**
- ❌ NÃO adicione título `# Pergunta N:`
- ✅ Comece direto com `Scenario:`
- ✅ Pergunta inteira na mesma linha
- ✅ Separador `---` antes das opções
- ✅ Opções com checkboxes

### Card Enriquecido (NNN-enriched-card.md)

**Estrutura:**
1. Pergunta em inglês + opções
2. Separador `---`
3. **TRANSLATED QUESTION** (português)
4. Separador `---`
5. **EXPLANATION (TECH LEAD)**
   - Explicação (qual padrão/conceito é testado)
   - Por que a alternativa [X] é correta (análise técnica profunda)
   - Por que as outras estão erradas (motivo específico para cada)
   - Dica importante (padrão recorrente)
6. Separador `---`
7. **🚸 CHILDREN EXPLANATION** (mesmo que acima, mas acessível e lúdico)
8. Separador `---`
9. **CORRECT ANSWER**

---

## 📖 Critérios de Qualidade

### EXPLANATION (TECH LEAD)

- **Explicação:** Qual padrão/conceito/decisão a pergunta testa
- **Por que [X] é correta:** Análise técnica profunda (5-7 linhas)
- **Por que outras erradas:** Motivo ESPECÍFICO para cada (2-3 linhas cada)
  - ❌ NÃO: "Está errada"
  - ✅ SIM: "A) Usa approach genérico, continuando o problema — o agente vai..."
- **Dica importante:** Padrão recorrente ou conexão com tópicos maiores

### 🚸 CHILDREN EXPLANATION

- **Tom:** Lúdico, narrativo, com analogias (robô, casa, restaurante, etc.)
- **Emojis:** Use se apropriado (🤖, 🅰️, 🅱️, ✅, ❌, etc.)
- **Linguagem:** Simples mas tecnicamente preciso
- **Motivos específicos:** Nunca apenas "está errada"

### Tradução (TRANSLATED QUESTION)

- ✅ Fiel ao significado (não literal)
- ✅ Português brasileiro naturalizado
- ✅ Manter termos técnicos em inglês (ex: "tool use", "MCP server")
- ✅ Não traduzir nomes de padrões

---

## 🔗 Referências

**Templates de Referência:**
- `templates/001-card.md` — Card simples
- `templates/001-enriched-card.md` — Card enriquecido

**Documentação Detalhada:**
- `.claude/skills/gerar-cards-enriquecidos-do-forms/SKILL.md` — Instruções completas

---

## 🎓 Padrão de Certificação

As questões testam conceitos de:
- Claude Models e capacidades
- Prompt engineering avançado
- Agentic systems e tool use
- Vision capabilities
- Best practices
- Padrões de arquitetura (Clean Architecture, DDD, SOLID)
- Trade-offs em design de sistemas

---

## ⚡ Características

- ✅ **Multiagente paralelo de 4 agentes** — coordenador orquestra parser + translator + tech enricher + kids enricher, máx 5 simultâneos
- ✅ **Especialização** — cada agente faz uma tarefa bem definida e reutilizável
- ✅ **Pipeline de 4 etapas** — parse → translate → tech analysis → kids analysis
- ✅ **Idempotência AND** — pula linha só se ambos os cards (simples + enriquecido) existem
- ✅ **Criação incremental** — cada agente materializa progresso (cria/atualiza arquivo, não deixa em /tmp)
- ✅ **Limite configurável** — processe N perguntas por execução (ou todas se sem argumento)
- ✅ **Numeração sequencial** — 001, 002, ... conforme ordem do TSV (quantas linhas houver)
- ✅ **Pasta dedicada** — output em `cards-enriquecidos-forms/`, separado de fotos
- ✅ **Reproduzível** — mesmo input sempre gera mesma estrutura
- ✅ **Retry inteligente** — tenta novamente uma vez em caso de falha antes de registrar permanente
- ✅ **Agente de Reports** — `gerador-de-reports` roda SEMPRE ao final e gera PDF com deck-style formatting

**Pipeline paralelo de 4 agentes otimizado para geração em volume, sem tamanho fixo — processa quantas linhas o TSV tiver. Cada agente independente e reutilizável. Nenhuma ambiguidade. Apenas cards de qualidade.**

---

## 📄 Etapa Final Automática: Gerador de Reports

O coordenador dispara o agente **`gerador-de-reports`** em **toda** execução, assim que o último
`card-enricher-kids` termina (inclusive em rodadas parciais como `/gerar-cards-enriquecidos-do-forms 3`).
Não é preciso invocá-lo manualmente. O PDF consolida **todos** os `*-enriched-card.md` do diretório,
não apenas os cards daquela rodada:

```bash
# (interno) Agent(subagent_type="gerador-de-reports", cards_dir="outputs/cards-enriquecidos-forms/")
# Gera: Report 15-08-2026 14:23:45.pdf
```

**Funcionalidades:**
- ✅ Lista automaticamente todos os cards enriquecidos disponíveis
- ✅ **Tamanho do deck derivado, nunca fixo** — 1 card enriquecido → PDF com 1 questão;
  15 enriquecidos (mesmo que o TSV tenha 60 ou 1000 linhas) → PDF com 15 questões
- ✅ Estrutura PDF profissional (capa, índice, cards, página final)
- ✅ Timestamp automático no nome do arquivo
- ✅ Formatação deck-style didático
- ✅ Todas as 5 seções incluídas (EN + PT-BR + Tech + Kids + Answer)
- ✅ Output: `outputs/Report dd-mm-yyyy hh:mm:ss.pdf`
