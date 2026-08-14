#!/bin/bash

# Array com os nomes atuais e números de questão
declare -a files=(
    "Captura de Tela 2026-06-29 às 17.19.37.png:001"
    "Captura de Tela 2026-06-29 às 17.19.51.png:002"
    "Captura de Tela 2026-06-29 às 17.20.16.png:003"
    "Captura de Tela 2026-06-29 às 17.20.30.png:004"
    "Captura de Tela 2026-06-29 às 17.20.48.png:005"
    "Captura de Tela 2026-06-29 às 17.21.24.png:006"
    "Captura de Tela 2026-06-29 às 17.21.36.png:007"
    "Captura de Tela 2026-06-29 às 17.21.44.png:008"
    "Captura de Tela 2026-06-29 às 17.21.51.png:009"
    "Captura de Tela 2026-06-29 às 17.21.58.png:010"
    "Captura de Tela 2026-06-29 às 17.22.07.png:011"
    "Captura de Tela 2026-06-29 às 17.22.21.png:012"
    "Captura de Tela 2026-06-29 às 17.22.30.png:013"
    "Captura de Tela 2026-06-29 às 17.22.38.png:014"
    "Captura de Tela 2026-06-29 às 17.22.46.png:015"
)

# Mapear nomes dos arquivos para títulos extraídos dos markdown
declare -A titles=(
    ["001"]="Otimizar custos CI/CD com Claude: sincronismo vs Message Batches API"
    ["002"]="Técnica para batch processing em code review iterativo"
    ["003"]="Integrar findings de Claude Code em PRs com structured output"
    ["004"]="Gerenciar falsos positivos em análise automatizada com confiança"
    ["005"]="Melhorar feedback de código automático com prompting e contexto"
    ["006"]="Evitar limitações de self-review em sugestões de código"
    ["007"]="Reestruturar análise de PR com múltiplos passes"
    ["008"]="Reduzir sugestões duplicadas em geração de testes"
    ["009"]="Filtrar e priorizar findings por confiança"
    ["010"]="Consistência de severidade em análise de código"
    ["011"]="Reduzir falsos positivos em análise de comentários"
    ["012"]="Otimizar custos com Message Batches API em pipelines"
    ["013"]="Eliminar findings duplicados após commit"
    ["014"]="Executar Claude Code em pipeline automatizado"
    ["015"]="Otimizar custos com batch processing e timeout"
)

# Renomear arquivos markdown
for entry in "${files[@]}"; do
    IFS=':' read -r old_file num <<< "$entry"
    new_file="${num}-${titles[$num]}.md"
    
    # Segurança: limpar caracteres especiais do nome
    new_file=$(echo "$new_file" | sed 's/[^a-zA-Z0-9._-]/-/g' | sed 's/-\+/-/g' | sed 's/-\.md/.md/')
    
    old_md="${old_file%.*}.md"
    
    if [ -f "$old_md" ]; then
        echo "Renomeando: $old_md → $new_file"
        mv "$old_md" "$new_file"
    fi
done

echo "✅ Renomeação completa!"
ls -1 *.md | head -5
