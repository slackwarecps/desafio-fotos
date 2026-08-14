#!/bin/bash

# Script para renomear e mover fotos de pictures/ para cards/
# Uso: bash scripts/rename_pictures.sh

PICTURES_DIR="/Users/fabioalvaropereira/Desktop/desafio-fotos/pictures"
CARDS_DIR="/Users/fabioalvaropereira/Desktop/desafio-fotos/cards"

# Verificar se directory existe
if [ ! -d "$PICTURES_DIR" ]; then
    echo "❌ Diretório pictures/ não encontrado!"
    exit 1
fi

# Contar arquivos de imagem
count=$(find "$PICTURES_DIR" -type f \( -iname "*.png" -o -iname "*.jpg" -o -iname "*.jpeg" \) | wc -l)

if [ $count -eq 0 ]; then
    echo "❌ Nenhuma imagem encontrada em $PICTURES_DIR"
    exit 1
fi

echo "📸 Encontrado: $count arquivo(s) em $PICTURES_DIR"
echo ""

# Renomear e mover
counter=1
find "$PICTURES_DIR" -type f \( -iname "*.png" -o -iname "*.jpg" -o -iname "*.jpeg" \) | sort | while read file; do
    # Obter extensão
    ext="${file##*.}"

    # Formatar número com 3 dígitos
    num=$(printf "%03d" $counter)
    new_name="foto-${num}.${ext}"
    new_path="$CARDS_DIR/$new_name"

    # Mover e renomear
    mv "$file" "$new_path"
    echo "✅ $counter) $(basename "$file") → $new_name"

    counter=$((counter + 1))
done

echo ""
echo "✨ Renomeação completa!"
echo ""
echo "📂 Fotos movidas para: $CARDS_DIR"
find "$CARDS_DIR" -type f \( -iname "*.png" -o -iname "*.jpg" -o -iname "*.jpeg" \) | wc -l | xargs echo "Total:"
