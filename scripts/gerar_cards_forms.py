#!/usr/bin/env python3
"""
Script de geração dos 60 cards enriquecidos do formulário TSV.
Atende integralmente à skill /gerar-cards-enriquecidos-do-forms.
"""

import csv
import re
import os
import sys

OUTPUT_DIR = "outputs/cards-enriquecidos-forms"

def parse_pergunta_raw(text):
    """Extrai enunciado limpo e dicionário com as 4 alternativas (A, B, C, D)"""
    match = re.search(r'\s+A\.(.*?)(?=B\.)B\.(.*?)(?=C\.)C\.(.*?)(?=D\.)D\.(.*)', text, re.DOTALL)
    if match:
        q_text = text[:match.start()].strip()
        opt_a = match.group(1).strip()
        opt_b = match.group(2).strip()
        opt_c = match.group(3).strip()
        opt_d = match.group(4).strip()
        return q_text, {'A': opt_a, 'B': opt_b, 'C': opt_c, 'D': opt_d}
    else:
        m2 = re.search(r'^(.*?)\s+A\.(.*)', text, re.DOTALL)
        if m2:
            q_text = m2.group(1).strip()
            rest = 'A.' + m2.group(2)
            opts = {}
            parts = re.split(r'(?=[A-D]\.)', rest)
            for p in parts:
                p = p.strip()
                if p.startswith('A.'): opts['A'] = p[2:].strip()
                elif p.startswith('B.'): opts['B'] = p[2:].strip()
                elif p.startswith('C.'): opts['C'] = p[2:].strip()
                elif p.startswith('D.'): opts['D'] = p[2:].strip()
            return q_text, opts
        return text.strip(), {}

def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    tsv_path = "formulario.tsv"
    
    if not os.path.exists(tsv_path):
        print(f"❌ Arquivo {tsv_path} não encontrado!")
        sys.exit(1)

    with open(tsv_path, 'r', encoding='utf-8') as f:
        reader = csv.reader(f, delimiter='\t')
        header = next(reader)
        rows = list(reader)

    limit = None
    if len(sys.argv) > 1 and sys.argv[1].isdigit():
        limit = int(sys.argv[1])
        print(f"🎯 Limite configurado: processar até {limit} novas perguntas.")

    print(f"📋 Encontradas {len(rows)} perguntas em {tsv_path}.")

    processed_count = 0
    skipped_count = 0
    created_files = []

    # Importa banco de dados de análises das 60 perguntas
    from database_cards import DATA_60

    for idx, r in enumerate(rows, 1):
        num_str = f"{idx:03d}"
        simple_file = os.path.join(OUTPUT_DIR, f"{num_str}-card.md")
        enriched_file = os.path.join(OUTPUT_DIR, f"{num_str}-enriched-card.md")

        # Idempotência: pular se ambos existem
        if os.path.exists(simple_file) and os.path.exists(enriched_file):
            skipped_count += 1
            continue

        if limit is not None and processed_count >= limit:
            break

        q_raw = r[1]
        question, options = parse_pergunta_raw(q_raw)

        if not options or len(options) != 4:
            print(f"⚠️ Pergunta {num_str} malformada ao parsear. Pulando...")
            continue

        card_info = DATA_60.get(idx)
        if not card_info:
            print(f"⚠️ Análise da pergunta {num_str} não encontrada no banco. Pulando...")
            continue

        correct_letter = card_info['correct']
        trans_q = card_info['trans_q']
        trans_opts = card_info['trans_opts']
        tech = card_info['tech']
        child = card_info['child']

        # 1. Gerar Card Simples
        simple_content = f"""Scenario: {question}

---

[ ] A - {options['A']}
[ ] B - {options['B']}
[ ] C - {options['C']}
[ ] D - {options['D']}"""

        with open(simple_file, 'w', encoding='utf-8') as f_out:
            f_out.write(simple_content)

        # 2. Gerar Card Enriquecido
        why_err_tech = []
        for let in ['A', 'B', 'C', 'D']:
            if let != correct_letter:
                why_err_tech.append(f"{let}) {tech['why_err'][let]}")
        tech_err_str = "\n".join(why_err_tech)

        why_err_child = []
        for let in ['A', 'B', 'C', 'D']:
            if let != correct_letter:
                why_err_child.append(f"{let}) {child['why_err'][let]}")
        child_err_str = "\n".join(why_err_child)

        enriched_content = f"""Scenario: {question}

---

[ ] A - {options['A']}
[ ] B - {options['B']}
[ ] C - {options['C']}
[ ] D - {options['D']}

---

### TRANSLATED QUESTION

{trans_q}
Alternativas traduzidas:

A) {trans_opts['A']}
B) {trans_opts['B']}
C) {trans_opts['C']}
D) {trans_opts['D']}

---

### EXPLANATION (TECH LEAD)

Explicação:
{tech['intro']}

Por que a alternativa {correct_letter} é a correta:
{tech['why_correct']}

Por que as outras estão erradas:

{tech_err_str}

Dica importante:
{tech['tip']}

---

### 🚸 CHILDREN EXPLANATION

Explicação:
{child['intro']}

Por que a alternativa {correct_letter} é a correta:
{child['why_correct']}

Por que as outras estão erradas:

{child_err_str}

Dica importante:
{child['tip']}

---

### CORRECT ANSWER

[ ] [{correct_letter}] - {options[correct_letter]}"""

        with open(enriched_file, 'w', encoding='utf-8') as f_out:
            f_out.write(enriched_content)

        processed_count += 1
        created_files.append(num_str)
        print(f"  ✓ [{num_str}] Gerados {num_str}-card.md e {num_str}-enriched-card.md")

    print("\n✨ Resumo da Execução:")
    print(f"   - Cards criados nesta execução: {processed_count} pares")
    print(f"   - Cards pulados por idempotência: {skipped_count}")
    print(f"   - Total de perguntas no formulário: {len(rows)}")
    if created_files:
        print(f"   - Faixa processada: {created_files[0]} a {created_files[-1]}")
    print(f"   - Pasta de saída: {OUTPUT_DIR}/")

if __name__ == '__main__':
    main()
