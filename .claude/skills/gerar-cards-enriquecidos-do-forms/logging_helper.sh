#!/bin/bash

# Logging Helper for Coordinator
# Garante que TODA linha seja gravada no chat E no arquivo com timestamp

# Raiz do projeto = 3 níveis acima deste script (.claude/skills/<skill>/)
# Resolve o caminho do próprio arquivo em bash (BASH_SOURCE) ou zsh (%x)
if [ -n "$BASH_VERSION" ]; then
    _LOG_HELPER_SELF="${BASH_SOURCE[0]}"
elif [ -n "$ZSH_VERSION" ]; then
    _LOG_HELPER_SELF="${(%):-%x}"
else
    _LOG_HELPER_SELF="$0"
fi
PROJECT_ROOT="$(cd "$(dirname "$_LOG_HELPER_SELF")/../../.." && pwd)"
LOG_FILE="$PROJECT_ROOT/desafio.log"

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
    local rotulo="Parser"

    case "$agent" in
        "card-parser") rotulo="Parser" ;;
        "card-translator") rotulo="Translator" ;;
        "card-enricher-tech") rotulo="Tech Enricher" ;;
        "card-enricher-kids") rotulo="Kids Enricher" ;;
        "gerador-de-reports") rotulo="Report Generator" ;;
    esac

    echo "$timestamp $rotulo $card_num iniciado..."
    echo "$timestamp $rotulo $card_num iniciado..." >> "$LOG_FILE"
}

# Função para agent completion
log_agent_complete() {
    local agent="$1"
    local card_num="$2"
    local card_status="${3:-OK}"

    local timestamp=$(date "+%H:%M:%S")
    local rotulo="Parser"

    case "$agent" in
        "card-parser") rotulo="Parser" ;;
        "card-translator") rotulo="Translator" ;;
        "card-enricher-tech") rotulo="Tech Enricher" ;;
        "card-enricher-kids") rotulo="Kids Enricher" ;;
        "gerador-de-reports") rotulo="Report Generator" ;;
    esac

    if [[ "$card_status" == "OK" ]]; then
        echo "$timestamp $rotulo $card_num completo ✓"
        echo "$timestamp $rotulo $card_num completo ✓" >> "$LOG_FILE"
    else
        echo "$timestamp $rotulo $card_num FALHOU ❌ — $card_status"
        echo "$timestamp $rotulo $card_num FALHOU ❌ — $card_status" >> "$LOG_FILE"
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
