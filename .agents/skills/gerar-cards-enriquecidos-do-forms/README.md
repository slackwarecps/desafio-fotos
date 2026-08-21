# Skill: Gerar Cards Enriquecidos a partir do Formulário TSV

Automatiza a geração de flashcards enriquecidos a partir de perguntas armazenadas em `formulario.tsv` (export de Google Forms), com explicações estruturadas em dois níveis: técnico (Tech Lead) e acessível (Children Explanation).

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

## 📋 Processo de Geração — Etapa Única Contínua

⚠️ **Princípio Central:** Para cada pergunta, gerar **ambos os cards (simples + enriquecido)** em um fluxo único, sem pausas.

### Fluxo por Pergunta

Para cada pergunta do TSV:
1. **Verificar idempotência** — Se ambos os arquivos (simples + enriquecido) existem, PULAR
2. **Parsear** — Extrair pergunta + 4 opções do texto bruto colado
3. **Card Simples** — Criar `NNN-card.md` (pergunta + checkboxes)
4. **Análise Técnica** — Determinar resposta correta
5. **Card Enriquecido** — Criar `NNN-enriched-card.md` (análise completa)
6. **Próxima Pergunta** — Sem pausas, repetir fluxo

❌ **ERRADO:** Processar todos os simples, depois todos os enriquecidos
✅ **CORRETO:** Simples → Enriquecido → Próxima Pergunta (ciclo completo)

---

## 📁 Estrutura de Saída

```
desafio-fotos/
├── formulario.tsv                      # Arquivo fonte (Google Forms export)
└── outputs/
    └── cards-enriquecidos-forms/       # ← Saída desta skill
        ├── 001-card.md                 # Card simples
        ├── 001-enriched-card.md        # Card enriquecido
        ├── 002-card.md
        ├── 002-enriched-card.md
        ├── 003-card.md
        └── 003-enriched-card.md
```

**Nota:** Saída separada em `cards-enriquecidos-forms/` (não em `cards-enriquecidos/`, que é para fotos). Evita colisão de numeração.

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

- ✅ Processamento **idempotente** — não sobrescreve cards já convertidos
- ✅ **Limite configurável** — processe N perguntas por execução
- ✅ **Numeração sequencial** — 001, 002, ..., 060 conforme ordem do TSV
- ✅ **Pasta dedicada** — output em `cards-enriquecidos-forms/`, separado de fotos
- ✅ **Reproduzível** — mesmo input sempre gera mesma estrutura

**Nenhuma ambiguidade. Nenhum problema. Apenas cards de qualidade.**
