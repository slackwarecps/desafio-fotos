#!/usr/bin/env python3
"""
Script Automatizado: Geração de Cards Enriquecidos para Flashcards SRS

Processa fotos no diretório e gera cards enriquecidos seguindo EXATAMENTE
o padrão dos templates (templates/001-card.md e templates/001-enriched-card.md).

Uso:
    python3 gerar_cards.py [fotos_path] [output_path]

    Exemplo:
    python3 gerar_cards.py . .
    python3 gerar_cards.py /path/to/fotos /path/to/output
"""

import os
import sys
import json
import re
from pathlib import Path
from datetime import datetime
from anthropic import Anthropic

# Inicializar cliente Anthropic
client = Anthropic()

# Configurações
TEMPLATE_CARD_SIMPLES = """Scenario: {pergunta}

---

[ ] A - {opcao_a}
[ ] B - {opcao_b}
[ ] C - {opcao_c}
[ ] D - {opcao_d}"""

TEMPLATE_CARD_ENRIQUECIDO = """Scenario: {pergunta}

---

[ ] A - {opcao_a}
[ ] B - {opcao_b}
[ ] C - {opcao_c}
[ ] D - {opcao_d}

---

### TRANSLATED QUESTION

{pergunta_pt}
Alternativas traduzidas:

A) {opcao_a_pt}
B) {opcao_b_pt}
C) {opcao_c_pt}
D) {opcao_d_pt}

---

### EXPLANATION (TECH LEAD)

Explicação:
{explicacao}

Por que a alternativa {resposta} é a correta:
{analise_correta}

Por que as outras estão erradas:

A) {analise_a_errada}
B) {analise_b_errada}
C) {analise_c_errada}
D) {analise_d_errada}

Dica importante:
{dica_importante}

---

### 🚸 CHILDREN EXPLANATION

Explicação:
{explicacao_simples}

Por que a alternativa {resposta} é a correta:
{analise_correta_simples}

Por que as outras estão erradas:

A) {analise_a_errada_simples}
B) {analise_b_errada_simples}
C) {analise_c_errada_simples}
D) {analise_d_errada_simples}

Dica importante:
{dica_importante_simples}

---

### CORRECT ANSWER

[ ] {resposta} - {texto_resposta}"""


def extrair_conteudo_imagem(caminho_imagem: str) -> dict:
    """Extrai pergunta e opções de uma imagem usando Claude Vision."""
    print(f"  📸 Lendo imagem: {Path(caminho_imagem).name}")

    with open(caminho_imagem, "rb") as f:
        image_data = f.read()

    import base64
    image_base64 = base64.standard_b64encode(image_data).decode("utf-8")

    # Determinar tipo de mídia
    ext = Path(caminho_imagem).suffix.lower()
    media_type = "image/png" if ext == ".png" else "image/jpeg"

    # Usar Claude Vision para extrair conteúdo
    message = client.messages.create(
        model="claude-opus-4-1-20250805",
        max_tokens=2000,
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "image",
                        "source": {
                            "type": "base64",
                            "media_type": media_type,
                            "data": image_base64,
                        },
                    },
                    {
                        "type": "text",
                        "text": """Extraia exatamente o seguinte desta imagem de pergunta de múltipla escolha:

1. A pergunta completa (em inglês)
2. A opção A (texto completo)
3. A opção B (texto completo)
4. A opção C (texto completo)
5. A opção D (texto completo)

Responda em JSON com esta estrutura:
{
  "pergunta": "...",
  "opcao_a": "...",
  "opcao_b": "...",
  "opcao_c": "...",
  "opcao_d": "..."
}"""
                    }
                ],
            }
        ],
    )

    # Parse JSON response
    resposta = message.content[0].text
    try:
        json_match = re.search(r'\{.*\}', resposta, re.DOTALL)
        if json_match:
            return json.loads(json_match.group())
    except json.JSONDecodeError:
        pass

    raise ValueError(f"Não conseguiu extrair conteúdo de {caminho_imagem}")


def validar_gabarito(pergunta: str, opcao_correta: str, justificativa: str, tentativa: int = 1) -> tuple[str, str]:
    """Valida o gabarito com múltiplas passadas. Retorna (resposta, justificativa_validada)."""
    if tentativa > 2:
        print(f"  ⚠️  Gabarito validado após 2 passadas")
        return opcao_correta, justificativa

    print(f"  🔍 Validando gabarito (passada {tentativa}/2)...")

    # Usar Claude para validar
    message = client.messages.create(
        model="claude-opus-4-1-20250805",
        max_tokens=1500,
        messages=[
            {
                "role": "user",
                "content": f"""Analise criticamente esta pergunta de certificação e valide a resposta proposta:

PERGUNTA: {pergunta}

RESPOSTA PROPOSTA: {opcao_correta}

JUSTIFICATIVA ATUAL: {justificativa}

Faça:
1. Analise se a resposta proposta está TECNICAMENTE CORRETA
2. Se houver erro, qual seria a resposta correta?
3. Responda em JSON:
{{
  "é_correto": true/false,
  "resposta_corrigida": "A|B|C|D ou null se correto",
  "motivo": "Se houver erro, explique. Se estiver correto, escreva 'VALIDADO'"
}}"""
            }
        ],
    )

    try:
        resposta = message.content[0].text
        json_match = re.search(r'\{.*\}', resposta, re.DOTALL)
        validacao = json.loads(json_match.group())

        if validacao["é_correto"]:
            print(f"  ✅ Gabarito validado: {opcao_correta}")
            return opcao_correta, justificativa
        else:
            # Se incorreto, tentar de novo com correção
            if tentativa < 2:
                print(f"  ❌ Gabarito incorreto. Motivo: {validacao['motivo']}")
                print(f"  🔄 Tentando novamente com resposta corrigida...")
                return validar_gabarito(pergunta, validacao["resposta_corrigida"], validacao["motivo"], tentativa + 1)
            else:
                print(f"  ⚠️  Validação final: {opcao_correta} (revisar manualmente)")
                return opcao_correta, justificativa
    except Exception as e:
        print(f"  ⚠️  Erro na validação: {e}. Usando resposta proposta.")
        return opcao_correta, justificativa


def gerar_cards_enriquecidos(numero: int, conteudo: dict) -> tuple:
    """Gera cards simples e enriquecido usando Claude."""
    print(f"  ✏️  Gerando cards enriquecidos para pergunta {numero}...")

    pergunta = conteudo["pergunta"]
    opcao_a = conteudo["opcao_a"]
    opcao_b = conteudo["opcao_b"]
    opcao_c = conteudo["opcao_c"]
    opcao_d = conteudo["opcao_d"]

    # Usar multi-turn conversation para gerar tudo
    conversation = []

    # Primeiro turno: analisar questão e gerar tradução + determinar resposta correta
    conversation.append({
        "role": "user",
        "content": f"""Analise esta pergunta de certificação Claude Architect:

PERGUNTA: {pergunta}

OPÇÕES:
A) {opcao_a}
B) {opcao_b}
C) {opcao_c}
D) {opcao_d}

Faça:
1. Traduza FIELMENTE (não literal) para português a pergunta e as 4 opções
2. Analise qual é a resposta correta
3. Responda em JSON:
{{
  "pergunta_pt": "...",
  "opcao_a_pt": "...",
  "opcao_b_pt": "...",
  "opcao_c_pt": "...",
  "opcao_d_pt": "...",
  "resposta": "A|B|C|D",
  "justificativa": "Por que essa é a correta"
}}"""
    })

    resposta1 = client.messages.create(
        model="claude-opus-4-1-20250805",
        max_tokens=2000,
        messages=conversation
    )

    msg1 = resposta1.content[0].text
    conversation.append({"role": "assistant", "content": msg1})

    try:
        json_match = re.search(r'\{.*\}', msg1, re.DOTALL)
        analise1 = json.loads(json_match.group())
    except:
        raise ValueError("Erro ao parsear resposta de tradução")

    # Validar gabarito com múltiplas passadas
    resposta_validada, justificativa_validada = validar_gabarito(
        conteudo["pergunta"],
        analise1["resposta"],
        analise1["justificativa"]
    )
    analise1["resposta"] = resposta_validada
    analise1["justificativa"] = justificativa_validada

    # Segundo turno: gerar EXPLANATION (TECH LEAD)
    conversation.append({
        "role": "user",
        "content": f"""Agora gere a seção EXPLANATION (TECH LEAD) para esta pergunta.

Estrutura OBRIGATÓRIA:
1. Explicação: (qual conceito testado - 2-3 linhas)
2. Por que a alternativa {analise1['resposta']} é a correta: (análise técnica profunda - 5-7 linhas)
3. Por que as outras estão erradas: (para CADA alternativa, motivo ESPECÍFICO - 2-3 linhas cada)
4. Dica importante: (padrão recorrente - 2-3 linhas)

Responda em JSON:
{{
  "explicacao": "...",
  "analise_correta": "...",
  "analise_a_errada": "...",
  "analise_b_errada": "...",
  "analise_c_errada": "...",
  "analise_d_errada": "...",
  "dica_importante": "..."
}}

CRÍTICO: NUNCA diga apenas "está errada". SEMPRE explique O MOTIVO específico."""
    })

    resposta2 = client.messages.create(
        model="claude-opus-4-1-20250805",
        max_tokens=3000,
        messages=conversation
    )

    msg2 = resposta2.content[0].text
    conversation.append({"role": "assistant", "content": msg2})

    try:
        json_match = re.search(r'\{.*\}', msg2, re.DOTALL)
        analise2 = json.loads(json_match.group())
    except:
        raise ValueError("Erro ao parsear EXPLANATION (TECH LEAD)")

    # Terceiro turno: gerar 🚸 CHILDREN EXPLANATION
    conversation.append({
        "role": "user",
        "content": f"""Agora gere a seção 🚸 CHILDREN EXPLANATION para esta pergunta.

Estrutura OBRIGATÓRIA (tom LÚDICO, acessível, com analogias e emojis):
1. Explicação: (narrativa/analogia prática - 2-3 linhas)
2. Por que a alternativa {analise1['resposta']} é a correta: (simples mas preciso - 3-4 linhas)
3. Por que as outras estão erradas: (para CADA alternativa, motivo ESPECÍFICO em tom simples - 2-3 linhas cada)
4. Dica importante: (padrão recorrente - 2-3 linhas)

Use analogias práticas (casa velha, robô, restaurante, quebra-cabeça, etc).
Use emojis se apropriado (🤖, 🅰️, 🅱️, ✅, ❌, 🚫, etc).

Responda em JSON:
{{
  "explicacao_simples": "...",
  "analise_correta_simples": "...",
  "analise_a_errada_simples": "...",
  "analise_b_errada_simples": "...",
  "analise_c_errada_simples": "...",
  "analise_d_errada_simples": "...",
  "dica_importante_simples": "..."
}}"""
    })

    resposta3 = client.messages.create(
        model="claude-opus-4-1-20250805",
        max_tokens=3000,
        messages=conversation
    )

    msg3 = resposta3.content[0].text

    try:
        json_match = re.search(r'\{.*\}', msg3, re.DOTALL)
        analise3 = json.loads(json_match.group())
    except:
        raise ValueError("Erro ao parsear CHILDREN EXPLANATION")

    # Montar dados completos
    dados_completos = {
        **conteudo,
        **analise1,
        **analise2,
        **analise3,
    }

    # Gerar card simples
    card_simples = TEMPLATE_CARD_SIMPLES.format(
        pergunta=conteudo["pergunta"],
        opcao_a=conteudo["opcao_a"],
        opcao_b=conteudo["opcao_b"],
        opcao_c=conteudo["opcao_c"],
        opcao_d=conteudo["opcao_d"],
    )

    # Gerar card enriquecido
    card_enriquecido = TEMPLATE_CARD_ENRIQUECIDO.format(
        pergunta=conteudo["pergunta"],
        opcao_a=conteudo["opcao_a"],
        opcao_b=conteudo["opcao_b"],
        opcao_c=conteudo["opcao_c"],
        opcao_d=conteudo["opcao_d"],
        pergunta_pt=analise1["pergunta_pt"],
        opcao_a_pt=analise1["opcao_a_pt"],
        opcao_b_pt=analise1["opcao_b_pt"],
        opcao_c_pt=analise1["opcao_c_pt"],
        opcao_d_pt=analise1["opcao_d_pt"],
        resposta=analise1["resposta"],
        texto_resposta={
            "A": conteudo["opcao_a"],
            "B": conteudo["opcao_b"],
            "C": conteudo["opcao_c"],
            "D": conteudo["opcao_d"],
        }[analise1["resposta"]],
        explicacao=analise2["explicacao"],
        analise_correta=analise2["analise_correta"],
        analise_a_errada=analise2["analise_a_errada"],
        analise_b_errada=analise2["analise_b_errada"],
        analise_c_errada=analise2["analise_c_errada"],
        analise_d_errada=analise2["analise_d_errada"],
        dica_importante=analise2["dica_importante"],
        explicacao_simples=analise3["explicacao_simples"],
        analise_correta_simples=analise3["analise_correta_simples"],
        analise_a_errada_simples=analise3["analise_a_errada_simples"],
        analise_b_errada_simples=analise3["analise_b_errada_simples"],
        analise_c_errada_simples=analise3["analise_c_errada_simples"],
        analise_d_errada_simples=analise3["analise_d_errada_simples"],
        dica_importante_simples=analise3["dica_importante_simples"],
    )

    return card_simples, card_enriquecido


def verificar_idempotencia(numero: int, output_path: Path) -> bool:
    """Verifica se cards já foram gerados para este número."""
    numero_str = str(numero).zfill(3)
    arquivo_simples = output_path / f"{numero_str}-card.md"
    arquivo_enriquecido = output_path / f"{numero_str}-enriched-card.md"

    if arquivo_simples.exists() and arquivo_enriquecido.exists():
        return True
    return False


def main():
    """Função principal."""
    # Argumentos
    fotos_path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("cards")
    output_path = Path(sys.argv[2]) if len(sys.argv) > 2 else Path("outputs/cards-enriquecidos")

    # Flag para forçar regeneração
    force = "--force" in sys.argv or "-f" in sys.argv

    print(f"\n🚀 Gerando Cards Enriquecidos SRS")
    print(f"📁 Fotos: {fotos_path}")
    print(f"📁 Output: {output_path}\n")

    # Garantir que o diretório de saída existe
    output_path.mkdir(parents=True, exist_ok=True)

    # Encontrar fotos
    imagens = sorted(
        list(fotos_path.glob("*.png")) + list(fotos_path.glob("*.jpg")) + list(fotos_path.glob("*.jpeg")),
        key=lambda x: x.stat().st_mtime
    )

    # Flag para limitar processamento
    if "--limit" in sys.argv:
        try:
            limit_idx = sys.argv.index("--limit")
            limit_val = int(sys.argv[limit_idx + 1])
            imagens = imagens[:limit_val]
            print(f"⚠️  Limitando o processamento para as primeiras {limit_val} imagens.")
        except (ValueError, IndexError):
            print("⚠️  Aviso: Formato inválido para --limit. Exemplo: --limit 5")

    if not imagens:
        print("❌ Nenhuma imagem encontrada!")
        return

    print(f"✅ Encontradas {len(imagens)} imagens a processar\n")

    # Processar cada imagem
    cards_gerados = 0
    cards_pulados = 0

    for idx, imagem_path in enumerate(imagens, 1):
        print(f"{'='*60}")
        print(f"Processando foto {idx}/{len(imagens)}: {imagem_path.name}")
        print(f"{'='*60}\n")

        # Verificar idempotência
        if not force and verificar_idempotencia(idx, output_path):
            numero_str = str(idx).zfill(3)
            print(f"⏭️  Cards já existem para foto {idx}")
            print(f"   (use --force para regenerar)\n")
            cards_pulados += 1
            continue

        try:
            # Extrair conteúdo
            conteudo = extrair_conteudo_imagem(str(imagem_path))
            print(f"✅ Conteúdo extraído\n")

            # Gerar cards
            card_simples, card_enriquecido = gerar_cards_enriquecidos(idx, conteudo)
            print(f"✅ Cards gerados\n")

            # Salvar arquivos
            numero_str = str(idx).zfill(3)
            arquivo_simples = output_path / f"{numero_str}-card.md"
            arquivo_enriquecido = output_path / f"{numero_str}-enriched-card.md"

            arquivo_simples.write_text(card_simples, encoding="utf-8")
            arquivo_enriquecido.write_text(card_enriquecido, encoding="utf-8")

            print(f"✅ Salvos:")
            print(f"   - {arquivo_simples.name}")
            print(f"   - {arquivo_enriquecido.name}\n")
            cards_gerados += 1

        except Exception as e:
            print(f"❌ Erro ao processar {imagem_path.name}: {e}\n")
            continue

    print(f"{'='*60}")
    print(f"✨ Concluído!")
    print(f"   ✅ Gerados: {cards_gerados}")
    print(f"   ⏭️  Pulados (já existem): {cards_pulados}")
    print(f"   📊 Total processado: {len(imagens)}")
    if cards_pulados > 0:
        print(f"\n💡 Dica: use --force para regenerar cards existentes")
    print(f"{'='*60}\n")


if __name__ == "__main__":
    main()
