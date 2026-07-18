#!/usr/bin/env python3
"""
Script para gerar cards enriquecidos a partir de fotos no diretório
Uso: python3 gerar_cards_enriquecidos.py
"""

import os
import sys
import re
from pathlib import Path


def find_photos():
    """Encontra todas as fotos no padrão foto-NNN.png"""
    current_dir = Path.cwd()
    photos = sorted([f for f in current_dir.glob("foto-*.png")])
    return photos


def extract_number(photo_path):
    """Extrai o número da foto (001, 002, etc)"""
    match = re.search(r"foto-(\d+)\.png", photo_path.name)
    if match:
        return match.group(1)
    return None


def create_basic_card(number, content):
    """Cria um arquivo card básico (foto-NNN.md)"""
    card_file = Path.cwd() / f"{number}-card.md"
    card_file.write_text(content, encoding="utf-8")
    return card_file


def create_enriched_card(number, content_dict):
    """Cria um arquivo enriched-card.md com tradução e explicação"""
    enriched_file = Path.cwd() / f"{number}-enriched-card.md"

    enriched_content = f"""{content_dict['original_question']}
---
{content_dict['options']}
---
### TRANSLATED QUESTION
{content_dict['translated_question']}

Alternativas traduzidas:

{content_dict['translated_options']}
---
### EXPLANATION
{content_dict['explanation']}
---
### CORRECT ANSWER
Alternativa Correta: {content_dict['correct_answer']}
"""

    enriched_file.write_text(enriched_content, encoding="utf-8")
    return enriched_file


def main():
    """Main flow"""
    photos = find_photos()

    if not photos:
        print("❌ Nenhuma foto encontrada no padrão foto-NNN.png")
        return

    print(f"✅ Encontradas {len(photos)} fotos:")
    for photo in photos:
        print(f"   - {photo.name}")

    print("\n⚠️  Este script requer entrada manual do usuário.")
    print("Para cada foto, você será solicitado a:")
    print("   1. Confirmar o conteúdo extraído")
    print("   2. Indicar a resposta correta (A/B/C/D)")
    print("   3. Fornecer tradução e explicação\n")

    print("Por favor, use o Claude Code com /gerar-cards-enriquecidos")
    print("para uma experiência interativa e automática.\n")

    print("Fotos prontas para processamento:")
    for photo in photos:
        number = extract_number(photo)
        print(f"   {number}: {photo.name}")


if __name__ == "__main__":
    main()
