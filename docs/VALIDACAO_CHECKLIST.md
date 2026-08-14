# ✅ Checklist de Validação da Skill Corrigida

Use este checklist para validar que todos os 5 problemas foram realmente resolvidos.

---

## 1️⃣ CLAUDE.md Dessincronizado

### ✓ Verificar

```bash
grep -i "SIMPLE EXPLANATION" /Users/fabioalvaropereira/Desktop/desafio-fotos/CLAUDE.md
```

**Resultado esperado:** Nenhuma linha (output vazio)

```bash
grep "🚸 CHILDREN EXPLANATION" /Users/fabioalvaropereira/Desktop/desafio-fotos/CLAUDE.md
```

**Resultado esperado:** Pelo menos 1 linha encontrada

### ✓ Ação
- [ ] Verificar CLAUDE.md tem "🚸 CHILDREN EXPLANATION" (não "SIMPLE EXPLANATION")

---

## 2️⃣ Scripts Python Paralelos

### ✓ Verificar

```bash
ls -la /Users/fabioalvaropereira/Desktop/desafio-fotos/*.py | grep -E "(gerar|processar)"
```

**Resultado esperado:**
```
gerar_cards.py           ✅ CANÔNICO
gerar_cards_claude.py    ❌ OBSOLETO (a deletar)
processar-cards.py       ❌ OBSOLETO (a deletar)
```

### ✓ Ação
- [ ] Arquivo `SCRIPTS_CANÔNICOS.md` existe
- [ ] Documenta qual script é canônico
- [ ] Lista scripts obsoletos

---

## 3️⃣ Idempotência (Verificar Código)

### ✓ Verificar

```bash
grep -A 5 "def verificar_idempotencia" /Users/fabioalvaropereira/Desktop/desafio-fotos/gerar_cards.py
```

**Resultado esperado:** Função existe e contém lógica de verificação

```bash
grep "verificar_idempotencia" /Users/fabioalvaropereira/Desktop/desafio-fotos/gerar_cards.py | head -3
```

**Resultado esperado:** Função é chamada no código

### ✓ Testar Script

```bash
cd /Users/fabioalvaropereira/Desktop/desafio-fotos

# Limpar um card existente para testar
rm 001-enriched-card.md 2>/dev/null || true

# Rodar script (deve gerar card 001)
python3 gerar_cards.py . . 2>&1 | grep -E "(⏭️|✅|Gerados)"

# Rodar de novo (deve PULAR card 001)
python3 gerar_cards.py . . 2>&1 | grep -E "(⏭️|Pulados)"
```

**Resultado esperado:**
- Primeira run: Gera card 001
- Segunda run: Pula card 001 (exibe "⏭️")

### ✓ Ação
- [ ] Função `verificar_idempotencia()` existe em `gerar_cards.py`
- [ ] Script pula arquivos existentes
- [ ] Flag `--force` funciona para regenerar

---

## 4️⃣ Numeração Sequencial

### ✓ Verificar

```bash
ls -1 /Users/fabioalvaropereira/Desktop/desafio-fotos/*-card.md 2>/dev/null | wc -l
```

**Resultado esperado:** Número de cards gerados

```bash
ls -1 /Users/fabioalvaropereira/Desktop/desafio-fotos/*-card.md 2>/dev/null | sort -t- -k1 -n
```

**Resultado esperado:**
```
001-card.md
002-card.md
003-card.md
004-card.md
...
(sem buracos na sequência)
```

### ✓ Verificar Documentação

```bash
cat /Users/fabioalvaropereira/Desktop/desafio-fotos/REGRA_NUMERACAO.md | head -20
```

**Resultado esperado:** Arquivo existe e explica numeração sequencial

### ✓ Ação
- [ ] Cards têm numeração CONTÍGUA (001, 002, 003... sem pular)
- [ ] Arquivo `REGRA_NUMERACAO.md` existe e documenta regra

---

## 5️⃣ Validação de Gabarito

### ✓ Verificar Código

```bash
grep -A 10 "def validar_gabarito" /Users/fabioalvaropereira/Desktop/desafio-fotos/gerar_cards.py | head -15
```

**Resultado esperado:** Função existe com lógica de validação

```bash
grep "validar_gabarito" /Users/fabioalvaropereira/Desktop/desafio-fotos/gerar_cards.py | grep -v "def validar"
```

**Resultado esperado:** Função é chamada no código (pelo menos 1 vez)

### ✓ Verificar Lógica

```bash
grep -C 2 "passada 1/2" /Users/fabioalvaropereira/Desktop/desafio-fotos/gerar_cards.py
```

**Resultado esperado:** Script faz 2 passadas de validação

### ✓ Testar Saída

Ao rodar `python3 gerar_cards.py . . --force`, você deve ver:

```
🔍 Validando gabarito (passada 1/2)...
✅ Gabarito validado: [A/B/C/D]
```

ou

```
🔍 Validando gabarito (passada 1/2)...
❌ Gabarito incorreto. Motivo: ...
🔄 Tentando novamente...
✅ Gabarito validado: [A/B/C/D]
```

### ✓ Ação
- [ ] Função `validar_gabarito()` existe em `gerar_cards.py`
- [ ] Função valida com 2 passadas
- [ ] Script mostra mensagens de validação

---

## 📊 Resumo Final

Verificar caixa para cada problema:

- [ ] 1️⃣  CLAUDE.md tem "🚸 CHILDREN EXPLANATION" (não "SIMPLE EXPLANATION")
- [ ] 2️⃣  SCRIPTS_CANÔNICOS.md existe e documenta qual usar
- [ ] 3️⃣  Script tem `verificar_idempotencia()` e pula arquivos existentes
- [ ] 4️⃣  Cards têm numeração contígua (001, 002, 003...)
- [ ] 5️⃣  Script tem `validar_gabarito()` com 2 passadas

---

## 🚀 Próximas Ações

### Se todas as caixas estão marcadas ✅
1. Deletar scripts obsoletos:
   ```bash
   rm gerar_cards_claude.py processar-cards.py
   rm -rf scripts/
   ```

2. Validar geração com novo run:
   ```bash
   python3 gerar_cards.py . . --force
   ```

3. Revisar alguns cards gerados para qualidade

4. Documentação está pronta para uso contínuo

---

## 📁 Referências Rápidas

- **Problemas Resolvidos:** `PROBLEMAS_RESOLVIDOS.md`
- **Scripts:** `SCRIPTS_CANÔNICOS.md`
- **Numeração:** `REGRA_NUMERACAO.md`
- **Skill:** `SKILL.md`
- **Guia Rápido:** `GUIA_RAPIDO.md`
