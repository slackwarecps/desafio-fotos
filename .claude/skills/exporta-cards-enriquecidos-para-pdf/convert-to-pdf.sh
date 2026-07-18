#!/bin/bash

# Script para converter flashcards deck Markdown para PDF
# Uso: ./convert-to-pdf.sh [data: YYYY-MM-DD ou "latest"]

set -e

# Diretório de saída
OUTPUT_DIR="outputs"

# Determinar qual arquivo converter
if [ -z "$1" ] || [ "$1" = "latest" ]; then
  # Encontrar o arquivo mais recente
  MARKDOWN_FILE=$(ls -t "$OUTPUT_DIR"/flashcards-deck-*.md 2>/dev/null | head -1)

  if [ -z "$MARKDOWN_FILE" ]; then
    echo "❌ Nenhum arquivo flashcards-deck-*.md encontrado em $OUTPUT_DIR/"
    exit 1
  fi
else
  # Usar data fornecida
  MARKDOWN_FILE="$OUTPUT_DIR/flashcards-deck-$1.md"
fi

# Validar que o arquivo exists
if [ ! -f "$MARKDOWN_FILE" ]; then
  echo "❌ Arquivo não encontrado: $MARKDOWN_FILE"
  exit 1
fi

# Determinar nome do PDF
PDF_FILE="${MARKDOWN_FILE%.md}.pdf"

echo "📝 Convertendo para PDF..."
echo "   Entrada: $MARKDOWN_FILE"
echo "   Saída: $PDF_FILE"
echo ""

# Tentar com pandoc (ordem de preferência de engine PDF)
if command -v pandoc &> /dev/null; then
  echo "🔄 Executando pandoc..."

  # Tenta com wkhtmltopdf primeiro (melhor qualidade)
  if command -v wkhtmltopdf &> /dev/null; then
    echo "   Motor: wkhtmltopdf"
    pandoc "$MARKDOWN_FILE" \
      -o "$PDF_FILE" \
      --from markdown \
      --to pdf \
      --pdf-engine=wkhtmltopdf
  else
    # Fallback para engine padrão
    echo "   Motor: padrão (weasyprint ou similar)"
    pandoc "$MARKDOWN_FILE" \
      -o "$PDF_FILE" \
      --from markdown \
      --to pdf
  fi

  # Verificar se foi criado
  if [ -f "$PDF_FILE" ]; then
    SIZE=$(du -h "$PDF_FILE" | cut -f1)
    echo ""
    echo "✨ PDF gerado com sucesso!"
    echo "   Arquivo: $PDF_FILE"
    echo "   Tamanho: $SIZE"
  else
    echo "❌ Erro ao gerar PDF"
    exit 1
  fi
else
  echo "❌ Pandoc não está instalado!"
  echo ""
  echo "Para instalar pandoc:"
  echo "  macOS: brew install pandoc"
  echo "  Linux (Ubuntu/Debian): sudo apt-get install pandoc"
  echo "  Windows: chocolatey install pandoc"
  echo ""
  echo "Para melhor qualidade PDF, também instale wkhtmltopdf:"
  echo "  macOS: brew install wkhtmltopdf"
  echo "  Linux: sudo apt-get install wkhtmltopdf"
  exit 1
fi

# Mostrar resumo
echo ""
echo "📊 Arquivos disponíveis em $OUTPUT_DIR/:"
ls -1h "$OUTPUT_DIR"/flashcards-deck-*.{md,pdf} 2>/dev/null || true
