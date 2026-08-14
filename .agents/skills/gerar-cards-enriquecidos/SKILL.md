---
name: gerar-cards-enriquecidos
description: Gera cartões enriquecidos e didáticos para flashcards SRS a partir de fotos no diretório, com explicações para múltiplos níveis de aprendizado
---

# Skill: Gerar Cards Enriquecidos com Explicações Didáticas

Implementação da skill que automatiza a geração de flashcards enriquecidos a partir de fotos.

## Fluxo de Execução

### Fase 1: Detectar e Renomear Fotos

```bash
# Listar todas as imagens na pasta cards
find cards -maxdepth 1 \( -name "*.png" -o -name "*.jpg" -o -name "*.jpeg" \) -type f | sort
```

Para cada foto encontrada que não segue o padrão `foto-NNN.png` em `cards/`:
1. Ordene por data de modificação (`stat` ou `ls -lt`)
2. Renomeie para `cards/foto-001.png`, `cards/foto-002.png`, etc. usando `mv`
3. Informe ao Fabão sobre cada renomeação

Exemplo de output:
```
✅ Renomeando fotos encontradas:
   - "cards/Screenshot 2026-07-18 at 08.46.16.png" → cards/foto-001.png
   - "cards/Screenshot 2026-07-18 at 08.46.21.png" → cards/foto-002.png
```

### Fase 2: Processar Cada Foto

Para cada arquivo `cards/foto-001.png`, `cards/foto-002.png`, etc. (em ordem numérica):

#### Passo 1: Ler a Imagem
Use a ferramenta `Read` com o caminho absoluto:
```
/Users/fabioalvaropereira/Desktop/desafio-fotos/cards/foto-001.png
```

#### Passo 2: Extrair Conteúdo
Leia a imagem e extraia:
- **Pergunta/Cenário**: Texto completo da pergunta (em inglês)
- **Opções**: As 4 alternativas rotuladas A, B, C, D

Exemplo de extração:
```
Pergunta: "You are building a multi-agent research system..."
A - Allow fetch_url for any link...
B - Replace fetch_url with a load_document tool...
C - Keep fetch_url available, but add prompt instructions...
D - Give the document analysis subagent web search tools...
```

#### Passo 3: Criar Card Simples
Crie o arquivo `outputs/cards-enriquecidos/001-card.md` com o conteúdo extraído.

**Estrutura EXATA (conforme template 001-card.md):**

```markdown
Scenario: [Pergunta completa em inglês - TUDO NA MESMA LINHA após "Scenario:"]

---

[ ] A - [Opção A]
[ ] B - [Opção B]
[ ] C - [Opção C]
[ ] D - [Opção D]
```

**IMPORTANTE:**
- ❌ NÃO adicione título `# Pergunta 1:`
- ✅ Comece DIRETO com `Scenario: [pergunta]`
- ✅ A pergunta completa vai na mesma linha após "Scenario:"
- ✅ Separador `---` antes das opções
- ✅ Opções com checkboxes `[ ] A -`, etc.









#### Passo 4: Analisar e Determinar a Resposta Correta
Analise a pergunta e as opções para determinar automaticamente qual é a resposta correta com base no conhecimento técnico/arquitetural.









#### Passo 5: Criar Card Enriquecido

Crie o arquivo `outputs/cards-enriquecidos/001-enriched-card.md` seguindo **EXATAMENTE** o template em `templates/001-enriched-card.md`:

**Estrutura obrigatória:**

```markdown
Scenario: [Pergunta completa em inglês - TUDO NA MESMA LINHA após "Scenario:"]

---

[ ] A - [Opção A]
[ ] B - [Opção B]
[ ] C - [Opção C]
[ ] D - [Opção D]

---

### TRANSLATED QUESTION
[Pergunta traduzida em português - fiel, não literal]
Alternativas traduzidas:

A) [Opção A traduzida]
B) [Opção B traduzida]
C) [Opção C traduzida]
D) [Opção D traduzida]

---

### EXPLANATION (TECH LEAD)

Explicação:
[Introdução ao conceito testado - qual padrão/decisão arquitetural a pergunta testa - 2-3 linhas]

Por que a alternativa [X] é a correta:
[Análise técnica profunda de por que essa é a melhor solução - 5-7 linhas]

Por que as outras estão erradas:

A) [Análise específica de por que A está errada - 2-3 linhas]
B) [Análise específica de por que B está errada - 2-3 linhas]
C) [Análise específica de por que C está errada - 2-3 linhas]
(Refute TODAS as alternativas incorretas)

Dica importante:
[Padrão recorrente ou conceito-chave a lembrar - 2-3 linhas]

---

### 🚸 CHILDREN EXPLANATION

Explicação:
[Introdução ao conceito testado em linguagem acessível e lúdica - 2-3 linhas. Use analogias e narrativa se apropriado]

Por que a alternativa [X] é a correta:
[Análise simples de por que funciona - 3-4 linhas, mas técnicamente preciso]

Por que as outras estão erradas:

A) [Motivo específico de por que A não funciona - 2-3 linhas]
B) [Motivo específico de por que B não funciona - 2-3 linhas]
C) [Motivo específico de por que C não funciona - 2-3 linhas]
D) [Motivo específico de por que D não funciona - 2-3 linhas]

Dica importante:
[Padrão recorrente ou conexão com conceito maior - 2-3 linhas]

---

### CORRECT ANSWER

[ ] [X] - [Texto completo da alternativa correta]
```

## Padrões de Qualidade

### EXPLANATION (TECH LEAD) — Estrutura Detalhada

**Ordem correta de seções (conforme template):**

1. **Explicação:**
   - Introduz qual conceito/padrão/decisão arquitetural a pergunta testa
   - Contextualiza o problema
   - 2-3 linhas

2. **Por que a alternativa [X] é a correta:**
   - Análise técnica PROFUNDA de por que essa é a melhor solução
   - Conecta a princípios/padrões arquiteturais
   - Explica as implicações e benefícios
   - 5-7 linhas bem estruturadas

3. **Por que as outras estão erradas:**
   - Para CADA alternativa incorreta, explicar O MOTIVO específico
   - **Não dizer apenas "está errada"**
   - Conectar a consequências ou problemas que causam
   - 2-3 linhas por alternativa
   - Refute TODAS as alternativas

4. **Dica importante:**
   - Padrão recorrente relacionado (ex: "Strangler Fig Pattern", "Least Privilege")
   - Conexão com Clean Architecture, DDD, SOLID, design patterns
   - Como esse conceito aparece em outros contextos
   - 2-3 linhas

### 🚸 CHILDREN EXPLANATION — Estrutura Detalhada

**Tom:** Acessível para iniciantes/aprendizes. Use analogias, narrativas, emojis se ajudarem na compreensão.

1. **Explicação:**
   - Introduz o conceito em linguagem simples e lúdica
   - Use analogias práticas (ex: "é como quando você monta um quebra-cabeça...")
   - Técnicamente preciso mas sem jargão desnecessário
   - 2-3 linhas (pode ser um pequeno parágrafo narrativo)

2. **Por que a alternativa [X] é a correta:**
   - Análise simples de por que funciona
   - Como um dev iniciante deveria pensar
   - 3-4 linhas, mantendo precisão técnica
   - Use analogias práticas quando apropriado
   - Exemplo: "Substituir a ferramenta genérica por uma com validação resolve o problema porque o agente não consegue acessar URLs fora do catálogo — é como dar uma chave que só funciona em certos quartos"

3. **Por que as outras estão erradas:**
   - Para CADA alternativa, explicar o motivo específico
   - **CRÍTICO:** Não dizer apenas "está errada"
   - Use emojis se apropriado para clareza
   - Padrão: "A) [Problema específico] — [Consequência prática]"
   - 2-3 linhas por alternativa
   - Refute TODAS as alternativas

4. **Dica importante:**
   - Padrão recorrente (ex: "Least Privilege Pattern")
   - Conexão com tópicos maiores
   - Como esse conceito aparece em outros contextos
   - 2-3 linhas

### Tradução
- Ser fiel ao significado, não literal
- Manter terminologia técnica em inglês quando apropriado
- Naturalizar a linguagem para PT-BR
- Não traduzir nomes de padrões consolidados

### Análise de Alternativas — Critério de Qualidade
- **Nunca diga apenas:** "Essa alternativa está incorreta"
- **Sempre diga o motivo específico:** "Isso falha porque..." ou "Problema: ... Consequência: ..."
- Conecte o motivo da falha aos conceitos testados

## Referências

Veja exemplos já criados:
- `/Users/fabioalvaropereira/Desktop/desafio-fotos/templates/001-enriched-card.md` ← Template de referência

Esses exemplos mostram o tom, estrutura e profundidade esperados.

## Checklist de Execução

- [ ] Detectar todas as fotos na pasta `cards/`
- [ ] Renomear fotos em `cards/` que não estão em padrão `foto-NNN.png`
- [ ] Informar Fabão sobre as renomeações
- [ ] Para cada foto:
  - [ ] Ler a imagem
  - [ ] Extrair pergunta + 4 opções
  - [ ] Criar `outputs/cards-enriquecidos/NNN-card.md` com estrutura simples
  - [ ] Analisar automaticamente e determinar resposta correta
  - [ ] Traduzir conteúdo para português
  - [ ] Criar `outputs/cards-enriquecidos/NNN-enriched-card.md` com:
    - [ ] Pergunta em inglês + opções
    - [ ] TRANSLATED QUESTION com tradução fiel
    - [ ] EXPLANATION (TECH LEAD) com: padrão testado, trade-off, análise correta, por que outras falham, conceito conectado
    - [ ] 🚸 CHILDREN EXPLANATION com: explicação, por que correta, por que outras erradas, dica importante
    - [ ] CORRECT ANSWER com checkbox
- [ ] Listar todos os cards criados ao final
- [ ] Confirmar sucesso

---

## ⚠️ Problemas Críticos Resolvidos

### 1️⃣ CLAUDE.md Dessincronizado
- **Problema:** Referia-se a "SIMPLE EXPLANATION" mas skill usa "🚸 CHILDREN EXPLANATION"
- **Solução:** ✅ CLAUDE.md atualizado

### 2️⃣ Scripts Python Paralelos Confusos
- **Problema:** gerar_cards.py, gerar_cards_claude.py, processar-cards.py causam confusão
- **Solução:** ✅ Script canônico: `gerar_cards.py`. Veja `SCRIPTS_CANÔNICOS.md`

### 3️⃣ Falta Idempotência (Risco de Sobrescrever)
- **Problema:** Rerun da skill sobrescrevia cards revisados manualmente
- **Solução:** ✅ Script agora:
  - Verifica se `NNN-card.md` + `NNN-enriched-card.md` já existem
  - Pula se existem (idempotência)
  - Usa `--force` para regenerar: `python3 scripts/gerar_cards.py cards outputs/cards-enriquecidos --force`

### 4️⃣ Numeração Não Contígua Ambígua
- **Problema:** foto-022.png gera 022-card.md ou 003-card.md?
- **Solução:** ✅ SEMPRE numeração sequencial (001, 002, 003...) conforme ordem de processamento
  - Veja `REGRA_NUMERACAO.md` para detalhes

### 5️⃣ Sem Validação Cruzada do Gabarito
- **Problema:** Resposta correta decidida em uma única passada (arriscado)
- **Solução:** ✅ Script agora valida gabarito com 2 passadas:
  - 1ª: Claude propõe resposta
  - 2ª: Claude valida a resposta proposta
  - Se inconsistência, tenta corrigir automaticamente
  - Resultado mais confiável para certificação
