#!/usr/bin/env python3
"""
Generator for all 60 enriched flashcards from formulario.tsv
Strictly follows .agents/skills/gerar-cards-enriquecidos-do-forms/SKILL.md
"""

import json
import os
import re
import sys

OUTPUT_DIR = "outputs/cards-enriquecidos-forms"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Load parsed questions
with open(os.path.join(OUTPUT_DIR, "questions-parsed.json"), "r", encoding="utf-8") as f:
    parsed_questions = json.load(f)

print(f"Loaded {len(parsed_questions)} questions from questions-parsed.json")
