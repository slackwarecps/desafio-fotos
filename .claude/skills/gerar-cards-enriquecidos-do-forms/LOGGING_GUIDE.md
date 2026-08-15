# Guia de Logging para o Coordenador

## Overview

O coordenador **DEVE** garantir que cada linha de log seja gravada **identicamente** no:
1. **Chat** (saída visual ao usuário)
2. **Arquivo** (`desafio.log` - histórico persistido)

Sem exceção. Console e arquivo devem estar sincronizados 100%.

---

## Regras Obrigatórias

### ✅ Formato Correto

Cada linha deve começar com **timestamp HH:MM:SS**:

```
16:52:52 Parser 002 iniciado...
16:53:27 Parser 002 completo ✓
16:55:12 Translator 002 iniciado...
```

Exceção: Linhas separadoras (apenas `---`):

```
--- Execução iniciada em 2026-08-15 16:52:52 (escopo: 1 card) ---
```

### ❌ Evitar

NÃO gravar linhas sem timestamp:

```
🔍 Verificando idempotência (AND):    ← ❌ SEM TIMESTAMP
  - 002: nenhum arquivo anterior       ← ❌ SEM TIMESTAMP
```

### ✅ Indentação com Timestamp

Bloco de informações: timestamp NO TÍTULO, indentação no resto:

```
16:52:52 🔍 Verificando idempotência (AND):
  - 002: nenhum arquivo anterior
  - 003: nenhum arquivo anterior
```

---

## Usando o Logging Helper

O arquivo `logging_helper.sh` fornece funções prontas:

### 1. Iniciar Execução

```bash
source logging_helper.sh
log_start "1 card"
```

**Output:**
```
--- Execução iniciada em 2026-08-15 16:52:52 (escopo: 1 card) ---
```

### 2. Disparar Agente

```bash
log_agent_dispatch "card-parser" "002"
```

**Output:**
```
16:52:52 Parser 002 iniciado...
```

### 3. Agent Completou (Sucesso)

```bash
log_agent_complete "card-parser" "002" "OK"
```

**Output:**
```
16:53:27 Parser 002 completo ✓
```

### 4. Agent Completou (Falha)

```bash
log_agent_complete "card-parser" "002" "Erro ao ler TSV"
```

**Output:**
```
16:53:27 Parser 002 FALHOU ❌ — Erro ao ler TSV
```

### 5. Consolidando Card

```bash
log_consolidating "002"
log_consolidated "002"
```

**Output:**
```
16:57:14 Consolidando 002...
16:58:16 002 consolidado ✓
```

### 6. Finalizando Execução

```bash
log_end
```

**Output:**
```
--- Execução concluída em 2026-08-15 16:58:16 ---
```

---

## Exemplo de Fluxo Completo

```bash
#!/bin/bash

source logging_helper.sh

# Início
log_start "1 card"

# Leitura TSV
log_line "📖 Lendo formularios/formulario.tsv... ✓"

# Verificação
log_line "🔍 Verificando idempotência (AND):"
log_line "  - 002: nenhum arquivo anterior → 4 estágios"

# Pipeline
log_line "⚙️  Disparando pipeline..."

# Parser
log_agent_dispatch "card-parser" "002"
# ... espera agent terminar ...
log_agent_complete "card-parser" "002" "OK"

# Translator
log_agent_dispatch "card-translator" "002"
# ... espera agent terminar ...
log_agent_complete "card-translator" "002" "OK"

# Tech Enricher
log_agent_dispatch "card-enricher-tech" "002"
# ... espera agent terminar ...
log_agent_complete "card-enricher-tech" "002" "OK"

# Kids Enricher
log_agent_dispatch "card-enricher-kids" "002"
# ... espera agent terminar ...
log_agent_complete "card-enricher-kids" "002" "OK"

# Consolidação
log_consolidating "002"
# ... consolida ...
log_consolidated "002"

# Resumo
log_line "✅ PROCESSAMENTO CONCLUÍDO"
log_line "📊 Estatísticas:"
log_line "  - Pulados por idempotência: 0"
log_line "  - Cards enriquecidos nesta execução: 1"
log_line "  - Falhas permanentes: 0"
log_line "  - Ainda pendentes: 59"

# Fim
log_end
```

**Output (Chat E Arquivo desafio.log):**

```
--- Execução iniciada em 2026-08-15 16:52:52 (escopo: 1 card) ---
16:52:52 📖 Lendo formularios/formulario.tsv... ✓
16:52:52 🔍 Verificando idempotência (AND):
  - 002: nenhum arquivo anterior → 4 estágios
16:52:52 ⚙️  Disparando pipeline...
16:53:14 Parser 002 iniciado...
16:53:27 Parser 002 completo ✓
16:53:27 Translator 002 iniciado...
16:55:12 Translator 002 completo ✓
16:55:12 Tech Enricher 002 iniciado...
16:56:11 Tech Enricher 002 completo ✓
16:56:11 Kids Enricher 002 iniciado...
16:57:14 Kids Enricher 002 completo ✓
16:57:14 Consolidando 002...
16:58:16 002 consolidado ✓
16:58:16 ✅ PROCESSAMENTO CONCLUÍDO
16:58:16 📊 Estatísticas:
  - Pulados por idempotência: 0
  - Cards enriquecidos nesta execução: 1
  - Falhas permanentes: 0
  - Ainda pendentes: 59
--- Execução concluída em 2026-08-15 16:58:16 ---
```

---

## Garantias de Sincronização

### ✅ O que DEVE acontecer:

1. **Cada `echo "..."` no chat** corresponde a **exatamente uma linha** em `desafio.log`
2. **Ordem idêntica** em ambos os locais
3. **Timestamps idênticos** em ambos os locais
4. **Indentação idêntica** em ambos os locais
5. **Append mode** — nunca sobrescrever o arquivo

### ❌ Problemas Encontrados Antes:

- ✗ Linhas sem timestamp no arquivo
- ✗ Múltiplas linhas impressas sem timestamps individuais
- ✗ Resumo final sem timestamps
- ✗ Inconsistência entre chat e arquivo

---

## Checklist para o Coordenador

Antes de commitar o coordenador, verificar:

- [ ] Todas as linhas têm timestamp HH:MM:SS (ou são separadores `---`)
- [ ] Chat e arquivo estão **100% sincronizados**
- [ ] Nenhuma linha é impressa sem ser gravada no arquivo
- [ ] Nenhuma linha é gravada sem ser impressa no chat
- [ ] Indentação é preservada em ambos os locais
- [ ] Append mode: `>> desafio.log` (nunca `>`)

---

## Próximos Passos

1. Atualizar SKILL.md com novo fluxo de coordenador
2. Implementar coordenador usando `logging_helper.sh`
3. Testar com `/gerar-cards-enriquecidos-do-forms 1`
4. Validar que `desafio.log` está 100% sincronizado com chat
