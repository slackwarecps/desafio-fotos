# 🔧 Scripts e Ferramentas

Utilitários para processar e exportar cards.

## 📋 Scripts Disponíveis

### 🎯 `gerar_cards.py` (Principal)
**Propósito:** Gerar cards enriquecidos a partir de fotos

```bash
python scripts/gerar_cards.py
```

**Fluxo:**
1. Detecta imagens em `cards/`
2. Extrai questões e opções (A, B, C, D)
3. Gera `NNN-card.md` (simples)
4. Gera `NNN-enriched-card.md` (com explicações em português)

**Saída:**
- `cards/NNN-card.md` - Card básico
- `cards/NNN-enriched-card.md` - Card enriquecido (TECH LEAD + CHILDREN)

---

### 🎯 `gerar_cards_claude.py` (Alternativa)
**Propósito:** Versão com API Claude alternativa

```bash
python scripts/gerar_cards_claude.py
```

Similar ao `gerar_cards.py`, mas usa configuração alternativa.

---

### 🔄 `processar-cards.py`
**Propósito:** Processar e validar cards existentes

```bash
python scripts/processar-cards.py
```

Útil para limpeza e validação em massa.

---

### 📤 `exporta_epub.py`
**Propósito:** Exportar cards para formato EPUB (e-book)

```bash
python scripts/exporta_epub.py
```

**Saída:** `outputs/flashcards-[DATA].epub`

Compatível com Google Play Books e leitores de e-book.

---

### 🏷️ `rename_flashcards.sh` (Legado)
**Propósito:** Renomear flashcards em massa (obsoleto, use a skill)

```bash
bash scripts/rename_flashcards.sh
```

---

## 🚀 Como Usar

### Opção 1: Via Skills (Recomendado) ⭐
```bash
/gerar-cards-enriquecidos
/exporta-cards-enriquecidos-para-pdf
/exporta-cards-enriquecidos-para-epub
```

### Opção 2: Direto com Python
```bash
cd /Users/fabioalvaropereira/Desktop/desafio-fotos
python scripts/gerar_cards.py
```

---

## 📚 Estrutura de Entrada

```
cards/
├── foto-001.png  (ou qualquer nome)
├── foto-002.png
└── ...
```

Coloque as fotos de questões neste diretório.

---

## 📤 Estrutura de Saída

```
cards/
├── foto-001.png
├── 001-card.md
├── 001-enriched-card.md
├── foto-002.png
├── 002-card.md
├── 002-enriched-card.md
└── ...

outputs/
├── flashcards-deck-2026-07-19.pdf
└── flashcards-2026-07-19.epub
```

---

## ⚙️ Dependências

- Python 3.9+
- Claude API (com chave em `ANTHROPIC_API_KEY`)
- Bibliotecas: `requests`, `json`, `os`, `datetime`

---

## 🐛 Troubleshooting

**Erro: "No such file or directory"**
- Verifique se está na raiz do projeto
- Coloque fotos em `cards/`

**Erro: "ANTHROPIC_API_KEY not set"**
- Configure: `export ANTHROPIC_API_KEY=sk-...`

**Scripts antigos não funcionam?**
- Use as skills: `/gerar-cards-enriquecidos`

---

**📖 Veja também:** `../docs/SCRIPTS_CANÔNICOS.md`
