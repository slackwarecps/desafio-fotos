# Skill: Gerar Cards Enriquecidos com Explicações Didáticas

Automatiza a geração de flashcards enriquecidos a partir de fotos, usando padrão de "professor de certificação" com explicações estruturadas em dois níveis: técnico (Tech Lead) e acessível (Children Explanation).

## 🚀 Uso Rápido

### Opção 1: Script Python (Recomendado para Automação)

```bash
# Gerar cards lendo de cards/ e gravando em outputs/cards-enriquecidos/
python3 scripts/gerar_cards.py

# Ou especificar caminhos alternativos
python3 scripts/gerar_cards.py /caminho/fotos /caminho/output
```

**Vantagens:**
- ✅ Executa de forma **100% automatizada**
- ✅ Processa **todas as fotos continuamente**
- ✅ Funciona em **qualquer contexto/CLI**
- ✅ Não depende de memória do Claude
- ✅ Reproduzível e confiável

### Opção 2: Skill Manual (Para Controle Fine-Tuned)

```
/gerar-cards-enriquecidos
```

Invoque a skill no Claude. Lê o `SKILL.md` e segue as instruções manualmente.

**Vantagens:**
- ✅ Mais flexível
- ✅ Permite ajustes no meio do processo
- ✅ Melhor para revisão/iteração

---

## 📋 Processo de Geração

### Phase 1: Detecção de Fotos
Encontra automaticamente todas as imagens (*.png, *.jpg, *.jpeg) na pasta `cards/`.

### Phase 2: Extração de Conteúdo
Usa Claude Vision para extrair:
- Pergunta completa em inglês
- 4 opções (A, B, C, D)

### Phase 3: Geração de Cards

Para cada foto, cria:
1. **Card Simples** (`NNN-card.md`) — Pergunta + Opções
2. **Card Enriquecido** (`NNN-enriched-card.md`) — Pergunta + Tradução + TECH LEAD + CHILDREN EXPLANATION + Resposta

---

## 📁 Estrutura de Saída

```
desafio-fotos/
├── cards/
│   ├── foto-001.png                  # Foto original
│   └── foto-002.png
├── outputs/
│   └── cards-enriquecidos/
│       ├── 001-card.md               # Card simples
│       ├── 001-enriched-card.md      # Card enriquecido
│       ├── 002-card.md
│       └── 002-enriched-card.md
└── scripts/
    └── gerar_cards.py                # Script automatizado
```

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

### Card Enriquecido (NNN-enriched-card.md)

**Estrutura:**
1. Pergunta em inglês
2. Opções em inglês
3. TRANSLATED QUESTION (português)
4. EXPLANATION (TECH LEAD)
   - Explicação
   - Por que a alternativa [X] é correta
   - Por que as outras estão erradas (motivo específico para cada)
   - Dica importante
5. 🚸 CHILDREN EXPLANATION (mesmo que acima, mas acessível e lúdico)
6. CORRECT ANSWER

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
- **Mesmo que TECH LEAD:** Mas acessível e engajante
- **Motivos específicos:** Nunca apenas "está errada"

### Tradução (TRANSLATED QUESTION)

- ✅ Fiel ao significado (não literal)
- ✅ Português brasileiro naturalizado
- ✅ Manter termos técnicos em inglês (ex: "fetch_url")
- ✅ Não traduzir nomes de padrões

---

## 🔗 Referências

**Templates de Referência:**
- `templates/001-card.md` — Card simples
- `templates/001-enriched-card.md` — Card enriquecido

**Documentação Interna:**
- `SKILL.md` — Instruções detalhadas (para skill manual)

**Memory Persistente** (para novos contextos):
- Leia `.claude/projects/.../memory/skill-cards-estrutura.md`

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

## ⚡ Próximas Gerações

Todas as futuras gerações seguirão:
- ✅ Estrutura EXATA dos templates
- ✅ Critérios de qualidade validados
- ✅ Processamento contínuo
- ✅ Reproduzível em qualquer contexto

**Nenhuma ambiguidade. Nenhum problema. Apenas cards de qualidade.**
