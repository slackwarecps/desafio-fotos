#!/usr/bin/env python3
import csv
import re
import os
import json

OUTPUT_DIR = "outputs/cards-enriquecidos-forms"
os.makedirs(OUTPUT_DIR, exist_ok=True)

with open('outputs/cards-enriquecidos-forms/questions-parsed.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

print(f"Loaded {len(questions)} parsed questions.")
