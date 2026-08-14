#!/usr/bin/env python3
"""
Script para gerar cards enriquecidos a partir de fotos de perguntas.
Processa imagens, extrai perguntas/opções e cria cards simples e enriquecidos.
"""

import os
import re
import json
from pathlib import Path
from anthropic import Anthropic

# Configuração
CARDS_DIR = Path("/Users/fabiopereira/Desktop/desafio-fotos/cards")
OUTPUT_DIR = Path("/Users/fabiopereira/Desktop/desafio-fotos/outputs/cards-enriquecidos")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

def read_image(image_path):
    """Lê uma imagem e retorna como base64."""
    import base64
    with open(image_path, "rb") as image_file:
        return base64.standard_b64encode(image_file.read()).decode("utf-8")

def extract_question_and_options(client, image_path, image_base64):
    """
    Extrai pergunta e 4 opções (A, B, C, D) da imagem usando Claude Vision.
    Retorna dict com 'question' e 'options' (lista de 4 strings).
    """
    response = client.messages.create(
        model="claude-opus-5",
        max_tokens=2000,
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "image",
                        "source": {
                            "type": "base64",
                            "media_type": "image/png",
                            "data": image_base64,
                        },
                    },
                    {
                        "type": "text",
                        "text": """Please extract the question/scenario and all 4 answer options (A, B, C, D) from this image.

Return the response in this JSON format:
{
    "question": "Full question text here",
    "options": [
        "Option A text",
        "Option B text",
        "Option C text",
        "Option D text"
    ]
}

Make sure to:
- Extract the COMPLETE question text, including all context
- Extract ALL 4 options exactly as they appear
- Return valid JSON only, no other text"""
                    }
                ],
            }
        ],
    )

    try:
        result = json.loads(response.content[0].text)
        return result
    except json.JSONDecodeError:
        print(f"❌ Failed to parse JSON response for {image_path.name}")
        return None

def determine_correct_answer(client, question, options):
    """
    Analisa a pergunta e opções para determinar automaticamente a resposta correta.
    Retorna índice (0-3) correspondente a A, B, C, D.
    """
    response = client.messages.create(
        model="claude-opus-5",
        max_tokens=1000,
        messages=[
            {
                "role": "user",
                "content": f"""Analyze this question and determine which answer (A, B, C, or D) is correct.

Question:
{question}

Options:
A) {options[0]}
B) {options[1]}
C) {options[2]}
D) {options[3]}

Return ONLY a JSON object with:
{{"answer": "A", "confidence": 0.95, "reasoning": "brief explanation"}}

The answer field must be exactly "A", "B", "C", or "D"."""
            }
        ],
    )

    try:
        result = json.loads(response.content[0].text)
        answer_letter = result.get("answer", "A").upper()
        # Convert letter to index (A=0, B=1, C=2, D=3)
        return ord(answer_letter) - ord('A'), result
    except (json.JSONDecodeError, ValueError):
        return 0, {}  # Default to A if parsing fails

def translate_to_portuguese(client, text):
    """Traduz texto para português mantendo fidelidade ao significado."""
    response = client.messages.create(
        model="claude-opus-5",
        max_tokens=1000,
        messages=[
            {
                "role": "user",
                "content": f"""Translate this text to Portuguese (Brazilian).
Maintain technical accuracy and keep technical terms in English when appropriate.
Return ONLY the translation, no explanations.

Text:
{text}"""
            }
        ],
    )
    return response.content[0].text.strip()

def generate_tech_explanation(client, question, options, correct_idx):
    """Gera explicação técnica (TECH LEAD) para o card enriquecido."""
    correct_letter = chr(ord('A') + correct_idx)
    response = client.messages.create(
        model="claude-opus-5",
        max_tokens=2000,
        messages=[
            {
                "role": "user",
                "content": f"""Create a TECH LEAD explanation for this multiple choice question.

Question: {question}

Options:
A) {options[0]}
B) {options[1]}
C) {options[2]}
D) {options[3]}

Correct Answer: {correct_letter}

Structure your response EXACTLY as follows (use these exact section headers):

Explicação:
[2-3 lines introducing the architectural pattern/concept being tested]

Por que a alternativa {correct_letter} é a correta:
[5-7 lines of deep technical analysis of why this is the best solution]

Por que as outras estão erradas:

A) [2-3 lines why A is wrong]
B) [2-3 lines why B is wrong]
C) [2-3 lines why C is wrong]
D) [2-3 lines why D is wrong]

Dica importante:
[2-3 lines about the related architectural pattern or design principle]

Make it technically rigorous and reference architectural patterns where relevant."""
            }
        ],
    )
    return response.content[0].text.strip()

def generate_children_explanation(client, question, options, correct_idx):
    """Gera explicação simples (CHILDREN) para o card enriquecido."""
    correct_letter = chr(ord('A') + correct_idx)
    response = client.messages.create(
        model="claude-opus-5",
        max_tokens=2000,
        messages=[
            {
                "role": "user",
                "content": f"""Create a CHILDREN EXPLANATION for this multiple choice question (simple language for beginners).

Question: {question}

Options:
A) {options[0]}
B) {options[1]}
C) {options[2]}
D) {options[3]}

Correct Answer: {correct_letter}

Structure your response EXACTLY as follows (use these exact section headers):

Explicação:
[2-3 lines explaining the concept in simple, accessible language using analogies where helpful]

Por que a alternativa {correct_letter} é a correta:
[3-4 lines explaining why this works in simple terms]

Por que as outras estão erradas:

A) [2-3 lines why A doesn't work]
B) [2-3 lines why B doesn't work]
C) [2-3 lines why C doesn't work]
D) [2-3 lines why D doesn't work]

Dica importante:
[2-3 lines about recurring patterns or connections to larger concepts]

Use accessible language without sacrificing technical accuracy. Use emojis if they help clarity."""
            }
        ],
    )
    return response.content[0].text.strip()

def create_simple_card(card_number, question, options):
    """Cria o arquivo de card simples (NNN-card.md)."""
    content = f"""Scenario: {question}

---

[ ] A - {options[0]}
[ ] B - {options[1]}
[ ] C - {options[2]}
[ ] D - {options[3]}
"""
    filename = OUTPUT_DIR / f"{card_number:03d}-card.md"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)
    return filename

def create_enriched_card(card_number, question, options, correct_idx,
                        question_pt, options_pt, tech_exp, children_exp):
    """Cria o arquivo de card enriquecido (NNN-enriched-card.md)."""
    correct_letter = chr(ord('A') + correct_idx)
    correct_option = options[correct_idx]

    content = f"""Scenario: {question}

---

[ ] A - {options[0]}
[ ] B - {options[1]}
[ ] C - {options[2]}
[ ] D - {options[3]}

---

### TRANSLATED QUESTION

{question_pt}

Alternativas traduzidas:

A) {options_pt[0]}
B) {options_pt[1]}
C) {options_pt[2]}
D) {options_pt[3]}

---

### EXPLANATION (TECH LEAD)

{tech_exp}

---

### 🚸 CHILDREN EXPLANATION

{children_exp}

---

### CORRECT ANSWER

[ ] {correct_letter} - {correct_option}
"""
    filename = OUTPUT_DIR / f"{card_number:03d}-enriched-card.md"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)
    return filename

def process_photos():
    """Processa todas as fotos no diretório cards/"""
    client = Anthropic()

    # Encontrar todas as fotos
    photo_files = sorted([f for f in CARDS_DIR.glob("foto-*.png")])

    print(f"\n🚀 Processando {len(photo_files)} fotos...\n")

    for idx, photo_path in enumerate(photo_files, 1):
        print(f"📸 Processando {photo_path.name} ({idx}/{len(photo_files)})...")

        # 1. Ler imagem
        image_base64 = read_image(photo_path)

        # 2. Extrair pergunta e opções
        print(f"   → Extraindo pergunta e opções...")
        extraction = extract_question_and_options(client, photo_path, image_base64)
        if not extraction:
            print(f"   ❌ Falha ao extrair de {photo_path.name}")
            continue

        question = extraction.get("question", "")
        options = extraction.get("options", [])

        if len(options) != 4:
            print(f"   ❌ Número incorreto de opções: {len(options)}")
            continue

        # 3. Determinar resposta correta
        print(f"   → Analisando resposta correta...")
        correct_idx, answer_info = determine_correct_answer(client, question, options)
        correct_letter = chr(ord('A') + correct_idx)

        # 4. Traduzir pergunta e opções para português
        print(f"   → Traduzindo para português...")
        question_pt = translate_to_portuguese(client, question)
        options_pt = [translate_to_portuguese(client, opt) for opt in options]

        # 5. Gerar explicações
        print(f"   → Gerando explicação técnica...")
        tech_exp = generate_tech_explanation(client, question, options, correct_idx)

        print(f"   → Gerando explicação simples...")
        children_exp = generate_children_explanation(client, question, options, correct_idx)

        # 6. Criar cards
        print(f"   → Criando cards...")
        simple_file = create_simple_card(idx, question, options)
        enriched_file = create_enriched_card(idx, question, options, correct_idx,
                                             question_pt, options_pt, tech_exp, children_exp)

        print(f"   ✅ Cards criados:")
        print(f"      - {simple_file.name}")
        print(f"      - {enriched_file.name}")
        print(f"      Resposta correta: {correct_letter}")
        print()

    print(f"\n✅ Processamento concluído!")

    # Listar todos os cards criados
    cards = sorted(OUTPUT_DIR.glob("*-card.md"))
    enriched = sorted(OUTPUT_DIR.glob("*-enriched-card.md"))

    print(f"\n📚 Cards Gerados:")
    print(f"   Simples: {len([c for c in cards if not 'enriched' in c.name])}")
    print(f"   Enriquecidos: {len(enriched)}")
    print(f"   Total: {len(cards) + len(enriched)}")

if __name__ == "__main__":
    process_photos()
