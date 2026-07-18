# Script de Conversão: convert-to-pdf.sh

Script auxiliar para converter rapidamente o arquivo Markdown consolidado para PDF usando pandoc.

## Pré-requisitos

### Instalação (obrigatório)
```bash
# macOS
brew install pandoc

# Linux (Ubuntu/Debian)
sudo apt-get install pandoc

# Windows (com Chocolatey)
chocolatey install pandoc
```

### Opcional (para melhor qualidade PDF)
```bash
# macOS
brew install wkhtmltopdf

# Linux
sudo apt-get install wkhtmltopdf

# Windows
chocolatey install wkhtmltopdf
```

## Uso

### Opção 1: Converter o arquivo mais recente
```bash
./convert-to-pdf.sh latest
```

### Opção 2: Converter arquivo com data específica
```bash
./convert-to-pdf.sh 2026-07-18
```

Isso procurará por `outputs/flashcards-deck-2026-07-18.md` e gerará `outputs/flashcards-deck-2026-07-18.pdf`

### Opção 3: Sem argumentos (usa o mais recente)
```bash
./convert-to-pdf.sh
```

## Exemplo Completo

```bash
# 1. Gerar cards com a skill
/gerar-cards-enriquecidos

# 2. Exportar para Markdown consolidado
/exporta-cards-enriquecidos-para-pdf

# 3. Converter para PDF
cd /Users/fabioalvaropereira/Desktop/desafio-fotos
./.claude/skills/exporta-cards-enriquecidos-para-pdf/convert-to-pdf.sh
```

## Saída

```
📝 Convertendo para PDF...
   Entrada: outputs/flashcards-deck-2026-07-18.md
   Saída: outputs/flashcards-deck-2026-07-18.pdf

🔄 Executando pandoc...
   Motor: wkhtmltopdf

✨ PDF gerado com sucesso!
   Arquivo: outputs/flashcards-deck-2026-07-18.pdf
   Tamanho: 250 KB

📊 Arquivos disponíveis em outputs/:
flashcards-deck-2026-07-18.md
flashcards-deck-2026-07-18.pdf
```

## Troubleshooting

### "pandoc not found"
Pandoc não está instalado. Execute:
```bash
brew install pandoc  # macOS
# ou
sudo apt-get install pandoc  # Linux
```

### "PDF não foi gerado"
1. Verifique se o arquivo `.md` existe:
   ```bash
   ls -la outputs/flashcards-deck-*.md
   ```

2. Verifique se pandoc funciona:
   ```bash
   pandoc --version
   ```

3. Teste manualmente:
   ```bash
   pandoc outputs/flashcards-deck-2026-07-18.md \
     -o outputs/flashcards-deck-2026-07-18.pdf \
     --from markdown --to pdf
   ```

### PDF de qualidade ruim
Instale `wkhtmltopdf` para melhor qualidade:
```bash
brew install wkhtmltopdf  # macOS
# ou
sudo apt-get install wkhtmltopdf  # Linux
```

O script usará automaticamente se estiver disponível.

## Arquivos Gerados

### Antes (apenas Markdown)
```
outputs/
├── flashcards-deck-2026-07-18.md   (13 KB, editável)
```

### Depois (com PDF)
```
outputs/
├── flashcards-deck-2026-07-18.md   (13 KB, editável - MANTIDO)
└── flashcards-deck-2026-07-18.pdf  (250 KB, formatado)
```

## Automação

Para converter automaticamente após exportar, execute:

```bash
# Bash alias
alias convert-deck='./.claude/skills/exporta-cards-enriquecidos-para-pdf/convert-to-pdf.sh'

# Uso futuro
convert-deck latest
```

## Integração com Fluxo Completo

```bash
#!/bin/bash
# script-completo.sh

echo "1️⃣  Gerando cards..."
/gerar-cards-enriquecidos

echo "2️⃣  Exportando para PDF (Markdown)..."
/exporta-cards-enriquecidos-para-pdf

echo "3️⃣  Convertendo para PDF..."
./.claude/skills/exporta-cards-enriquecidos-para-pdf/convert-to-pdf.sh latest

echo "✨ Pronto! PDF disponível em outputs/"
open outputs/flashcards-deck-*.pdf  # macOS
```

Executar:
```bash
chmod +x script-completo.sh
./script-completo.sh
```
