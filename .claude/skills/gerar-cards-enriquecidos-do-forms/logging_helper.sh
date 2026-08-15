#!/bin/bash

# Logging Helper for Coordinator
# Garante que TODA linha seja gravada no chat E no arquivo com timestamp

LOG_FILE="/Users/fabiopereira/Desktop/desafio-formularios/desafio.log"

# Função para adicionar timestamp e gravar em ambos os lugares
log_line() {
    local msg="$1"
    local has_timestamp=false

    # Verifica se a mensagem já começa com timestamp HH:MM:SS
    if [[ $msg =~ ^[0-9]{2}:[0-9]{2}:[0-9]{2} ]]; then
        has_timestamp=true
    fi

    # Se não tem timestamp e não é linha separadora, adiciona
    if [[ "$has_timestamp" == false ]] && [[ ! $msg =~ ^--- ]]; then
        local timestamp=$(date "+%H:%M:%S")
        msg="$timestamp $msg"
    fi

    # Imprime no chat
    echo "$msg"

    # Grava no arquivo
    echo "$msg" >> "$LOG_FILE"
}

# Função para linha separadora (sem timestamp)
log_separator() {
    local msg="$1"
    echo "$msg"
    echo "$msg" >> "$LOG_FILE"
}

# Função para bloco multi-linha com mesmo timestamp
log_block() {
    local title="$1"
    shift  # Remove primeiro argumento
    local lines=("$@")

    local timestamp=$(date "+%H:%M:%S")

    # Título com timestamp
    echo "$timestamp $title"
    echo "$timestamp $title" >> "$LOG_FILE"

    # Linhas do bloco com indentação (timestamp no título)
    for line in "${lines[@]}"; do
        echo "  $line"
        echo "  $line" >> "$LOG_FILE"
    done
}

# Função para iniciar execução
log_start() {
    local scope="$1"
    local timestamp=$(date "+%Y-%m-%d %H:%M:%S")

    echo ""
    echo "--- Execução iniciada em $timestamp (escopo: $scope) ---"
    echo "" >> "$LOG_FILE"
    echo "--- Execução iniciada em $timestamp (escopo: $scope) ---" >> "$LOG_FILE"
}

# Função para finalizar execução
log_end() {
    local timestamp=$(date "+%Y-%m-%d %H:%M:%S")

    echo "--- Execução concluída em $timestamp ---"
    echo ""
    echo "--- Execução concluída em $timestamp ---" >> "$LOG_FILE"
    echo "" >> "$LOG_FILE"
}

# Função para agent dispatch
log_agent_dispatch() {
    local agent="$1"
    local card_num="$2"

    local timestamp=$(date "+%H:%M:%S")
    local rótulo="Parser"

    case "$agent" in
        "card-parser") rótulo="Parser" ;;
        "card-translator") rótulo="Translator" ;;
        "card-enricher-tech") rótulo="Tech Enricher" ;;
        "card-enricher-kids") rótulo="Kids Enricher" ;;
        "gerador-de-reports") rótulo="Report Generator" ;;
    esac

    echo "$timestamp $rótulo $card_num iniciado..."
    echo "$timestamp $rótulo $card_num iniciado..." >> "$LOG_FILE"
}

# Função para agent completion
log_agent_complete() {
    local agent="$1"
    local card_num="$2"
    local status="${3:-OK}"

    local timestamp=$(date "+%H:%M:%S")
    local rótulo="Parser"

    case "$agent" in
        "card-parser") rótulo="Parser" ;;
        "card-translator") rótulo="Translator" ;;
        "card-enricher-tech") rótulo="Tech Enricher" ;;
        "card-enricher-kids") rótulo="Kids Enricher" ;;
        "gerador-de-reports") rótulo="Report Generator" ;;
    esac

    if [[ "$status" == "OK" ]]; then
        echo "$timestamp $rótulo $card_num completo ✓"
        echo "$timestamp $rótulo $card_num completo ✓" >> "$LOG_FILE"
    else
        echo "$timestamp $rótulo $card_num FALHOU ❌ — $status"
        echo "$timestamp $rótulo $card_num FALHOU ❌ — $status" >> "$LOG_FILE"
    fi
}

# Função para consolidação
log_consolidating() {
    local card_num="$1"
    local timestamp=$(date "+%H:%M:%S")

    echo "$timestamp Consolidando $card_num..."
    echo "$timestamp Consolidando $card_num..." >> "$LOG_FILE"
}

# Função para consolidação completa
log_consolidated() {
    local card_num="$1"
    local timestamp=$(date "+%H:%M:%S")

    echo "$timestamp $card_num consolidado ✓"
    echo "$timestamp $card_num consolidado ✓" >> "$LOG_FILE"
}

# Exemplos de uso:
# log_start "1 card"
# log_agent_dispatch "card-parser" "002"
# log_agent_complete "card-parser" "002" "OK"
# log_agent_complete "card-parser" "002" "Erro ao ler TSV"
# log_separator "--- Seção ---"
# log_end
