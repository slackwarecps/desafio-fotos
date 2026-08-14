# 🔢 Regra de Numeração de Cards

## Regra Principal

**Os cards são gerados com numeração CONTÍGUA na pasta `outputs/cards-enriquecidos/`, começando do 001, independente da ordem de processamento das fotos.**

```
cards/foto-001.png → outputs/cards-enriquecidos/001-card.md, outputs/cards-enriquecidos/001-enriched-card.md
cards/foto-002.png → outputs/cards-enriquecidos/002-card.md, outputs/cards-enriquecidos/002-enriched-card.md
cards/foto-003.png → outputs/cards-enriquecidos/003-card.md, outputs/cards-enriquecidos/003-enriched-card.md
...
cards/foto-022.png → NÃO é 022-card.md, mas SIM outputs/cards-enriquecidos/004-card.md (4º a ser processado)
cards/foto-039.png → NÃO é 039-card.md, mas SIM outputs/cards-enriquecidos/005-card.md (5º a ser processado)
```

---

## Por Quê?

1. **Idempotência:** Numeração sequencial garante que rerun do script não gera conflitos
2. **Consistência:** Cada card tem um número único e previsível
3. **Clareza:** Não há "buracos" na numeração (001, 002, 003... sem pular)

---

## Comportamento do Script

### First Run (Nenhum card existe)
```bash
python3 scripts/gerar_cards.py
```

Encontra fotos em qualquer ordem/nome na pasta `cards/`:
- Processa na ordem de modificação (ls -lt)
- Gera `outputs/cards-enriquecidos/001-card.md`, `002-card.md`, `003-card.md`... sequencial

### Rerun (Cards já existem)
```bash
python3 scripts/gerar_cards.py
```

Comportamento:
- ✅ Pula fotos que já têm cards na pasta de destino (idempotência)
- ✅ Continua numeração de onde parou
- Se `outputs/cards-enriquecidos/001-card.md` já existe, pula a primeira foto correspondente
- Se `cards/foto-022.png` não tem card, gera `outputs/cards-enriquecidos/004-card.md` (próximo número sequencial)

### Regenerar Tudo
```bash
python3 scripts/gerar_cards.py --force
```

Força:
- ❌ Sobrescreve todos os cards em `outputs/cards-enriquecidos/`
- ✅ Mantém numeração sequencial
- Use apenas se tiver certeza!

---

## Exemplo Prático

### Estado Inicial (Imagens em `cards/`)
```
cards/foto-001.png
cards/foto-002.png
cards/foto-022.png
cards/foto-039.png
```

### Após `python3 scripts/gerar_cards.py`
```
cards/foto-001.png → outputs/cards-enriquecidos/001-card.md, outputs/cards-enriquecidos/001-enriched-card.md
cards/foto-002.png → outputs/cards-enriquecidos/002-card.md, outputs/cards-enriquecidos/002-enriched-card.md
cards/foto-022.png → outputs/cards-enriquecidos/003-card.md, outputs/cards-enriquecidos/003-enriched-card.md ⬅️ Numeração contígua!
cards/foto-039.png → outputs/cards-enriquecidos/004-card.md, outputs/cards-enriquecidos/004-enriched-card.md ⬅️ Não é 039!
```

### Se Rodar de Novo
```bash
python3 scripts/gerar_cards.py
```

Resultado:
```
⏭️  Cards já existem para foto 1 (pula)
⏭️  Cards já existem para foto 2 (pula)
⏭️  Cards já existem para foto 3 (pula)
⏭️  Cards já existem para foto 4 (pula)
✨ Concluído! Gerados: 0, Pulados: 4
```

---

## Regra Implícita

**A ordem de processamento é:**
1. Listar todas as imagens no diretório `cards/`
2. Ordenar por **data de modificação** (mais antigas primeiro)
3. Processar sequencialmente
4. Numerar na ordem de processamento (001, 002, 003...)

**Não depende de:** Nome do arquivo, data de criação, tamanho, etc.

**Depende de:** Data de modificação (ls -lt)

---

## Se Precisar Manter Nomes Específicos

Se você quer que `foto-022.png` gere `022-card.md`:

1. ❌ NÃO faça: Renomear fotos para 001, 002, 003... (perde ligação)
2. ✅ FAÇA: Usar script customizado que respeita números no nome da foto

Para agora, **use a regra padrão:** numeração sequencial começando do 001.
