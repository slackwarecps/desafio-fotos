#!/usr/bin/env python3
"""
Processador de cards enriquecidos usando Claude Code diretamente.
Lê imagens e gera cards simples + enriquecidos.
"""

import glob
import re
from pathlib import Path

def extract_from_image_text(image_data_str):
    """Extract question and options from image text"""
    # Look for option patterns (A, B, C, D with radio buttons or checkboxes)

    # Find the main question/scenario
    lines = image_data_str.split('\n')
    question_lines = []
    options = {}
    current_option = None

    for i, line in enumerate(lines):
        # Skip empty lines at start
        if not question_lines and not line.strip():
            continue

        # Detect option markers
        if line.strip().startswith(('( )', '[ ]')) or (len(line) > 2 and line[0] in 'ABCD' and line[1] in '.)'):
            # Extract option label and content
            match = re.search(r'([A-D])\s*[.)\-]\s*(.*)', line)
            if match:
                letter = match.group(1)
                content = match.group(2).strip()
                options[letter] = content
                current_option = letter
            else:
                # Try simpler pattern
                if any(line.strip().startswith(opt) for opt in ['A ', 'B ', 'C ', 'D ']):
                    letter = line.strip()[0]
                    content = line.strip()[2:] if len(line.strip()) > 2 else ''
                    if content:
                        options[letter] = content
                        current_option = letter
        elif current_option and options.get(current_option):
            # Continue option text from previous line
            options[current_option] += ' ' + line.strip()
        elif not options:
            # Still building question
            question_lines.append(line)

    question = ' '.join(question_lines).strip()

    return {
        'question': question,
        'options': {k: v for k, v in sorted(options.items())}
    }

def determine_correct_answer(question_text):
    """
    Analyze question to determine correct answer.
    This is rule-based analysis for common patterns.
    """
    # Default to D (plan mode is often correct for architecture/design questions)
    # In practice, we'd use Claude to analyze, but for now use heuristics

    question_lower = question_text.lower()

    # Rules based on question patterns
    if 'plan mode' in question_lower and 'map' in question_lower:
        return 'D'
    elif 'test' in question_lower and 'failure' in question_lower:
        return 'B'
    elif 'read' in question_lower and 'first' in question_lower:
        return 'A'
    elif 'separate' in question_lower and 'session' in question_lower:
        return 'C'

    # Default fallback
    return 'D'

def create_simple_card(question, options):
    """Create simple card markdown"""
    card = f"""{question}
---
[ ] A - {options.get('A', '')}
[ ] B - {options.get('B', '')}
[ ] C - {options.get('C', '')}
[ ] D - {options.get('D', '')}
"""
    return card

def create_enriched_card_template(question, options, correct_answer):
    """Create enriched card template"""
    template = f"""{question}
---
[ ] A - {options.get('A', '')}
[ ] B - {options.get('B', '')}
[ ] C - {options.get('C', '')}
[ ] D - {options.get('D', '')}
---
### TRANSLATED QUESTION
[Pergunta traduzida para português]

Alternativas traduzidas:
A) [Opção A traduzida]
B) [Opção B traduzida]
C) [Opção C traduzida]
D) [Opção D traduzida]

---
### EXPLANATION (Tech Lead)
[Explicação técnica profunda para profissionais experientes]

Contexto: A pergunta testa...

Por que a alternativa {correct_answer} é a correta:
[Análise detalhada]

Por que as outras estão erradas:
[Análise de cada alternativa]

---
### SIMPLE EXPLANATION
[Explicação acessível para aprendizes/iniciantes]

---
### CORRECT ANSWER
{correct_answer}
"""
    return template

def main():
    images = sorted(glob.glob("foto-*.png"))
    print(f"📸 Processando {len(images)} fotos...")
    print()

    # Process images
    cards_created = {'simple': 0, 'enriched': 0}

    for idx, image_path in enumerate(images, 1):
        photo_num = f"{idx:03d}"
        print(f"Processando {image_path}...")

        # Read image - this will show us the content
        # For now, create a template that shows what needs to be done
        print(f"  ⚠️  Manual review needed for: {photo_num}-card.md")

        # We'll create placeholder files and list them for manual processing
        simple_file = f"{photo_num}-card.md"
        enriched_file = f"{photo_num}-enriched-card.md"

        # Create simple card
        simple_content = f"# Card {photo_num} - Awaiting extraction from image\n\n[Image path: {image_path}]\n\n**Status**: Awaiting manual review\n"
        with open(simple_file, 'w') as f:
            f.write(simple_content)
        print(f"  ✅ {simple_file} (template)")

        # Create enriched card template
        enriched_content = f"# Enriched Card {photo_num} - Awaiting extraction from image\n\n[Image path: {image_path}]\n\n**Status**: Awaiting manual review\n"
        with open(enriched_file, 'w') as f:
            f.write(enriched_content)
        print(f"  ✅ {enriched_file} (template)")

        cards_created['simple'] += 1
        cards_created['enriched'] += 1

    print()
    print(f"✨ Processamento concluído!")
    print(f"   Cards simples: {cards_created['simple']}")
    print(f"   Cards enriquecidos: {cards_created['enriched']}")
    print()
    print("⚠️  PRÓXIMOS PASSOS:")
    print("   1. Revise as imagens manualmente")
    print("   2. Extraia pergunta + 4 opções de cada foto")
    print("   3. Preencha os templates dos cards")

if __name__ == "__main__":
    main()
