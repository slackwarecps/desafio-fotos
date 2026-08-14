# 📋 Scripts Canônicos vs Obsoletos

## ✅ SCRIPT CANÔNICO (Usar Este)

**Arquivo:** `gerar_cards.py`

**Características:**
- ✅ Tem idempotência (verifica arquivos existentes)
- ✅ Validação de gabarito com múltiplas passadas
- ✅ Logging detalhado
- ✅ Documentado no SKILL.md
- ✅ Função: Gerar cards simples + enriquecidos com qualidade validada

**Como usar:**
```bash
python3 gerar_cards.py . .
```

---

## ❌ SCRIPTS OBSOLETOS (NÃO USAR)

Estes scripts estão **OBSOLETOS** e podem estar dessincronizados da spec atual:

### 1. `gerar_cards_claude.py`
- **Motivo de obsolência:** Substituído por `gerar_cards.py` com validação melhorada
- **Ação:** Será deletado após migração (manter apenas se tem código único)
- **Não use:** Use `gerar_cards.py` em seu lugar

### 2. `processar-cards.py`
- **Motivo de obsolência:** Função sobreposta por `gerar_cards.py`
- **Ação:** Será deletado após migração
- **Não use:** Use `gerar_cards.py` em seu lugar

### 3. `scripts/gerar_cards_enriquecidos.py`
- **Motivo de obsolência:** Versão anterior antes de consolidação
- **Ação:** Será deletado após migração
- **Não use:** Use `gerar_cards.py` em seu lugar

---

## 📝 Regra de Ouro

**Sempre use:** `python3 gerar_cards.py . .`

**Nunca use:** Outros scripts paralelos

---

## 🗑️ Limpeza Recomendada

Após validar que `gerar_cards.py` funciona:

```bash
rm gerar_cards_claude.py
rm processar-cards.py
rm -rf scripts/
```

Mantém apenas **uma fonte de verdade**.
