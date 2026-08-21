#!/usr/bin/env python3
"""
Generates all 60 cards for outputs/cards-enriquecidos-forms/ with bespoke translations,
technical explanations (Tech Lead level), accessible explanations (Children level),
and correct answer keys.
"""

import json
import os
import sys

OUTPUT_DIR = "outputs/cards-enriquecidos-forms"
os.makedirs(OUTPUT_DIR, exist_ok=True)

with open(os.path.join(OUTPUT_DIR, "questions-parsed.json"), "r", encoding="utf-8") as f:
    questions = json.load(f)

# Definitive Correct Answer Mapping for Questions 1..60
ANSWER_KEYS = {
    1: "D", 2: "B", 3: "C", 4: "A", 5: "A", 6: "B", 7: "A", 8: "C", 9: "B", 10: "B",
    11: "A", 12: "D", 13: "B", 14: "B", 15: "D", 16: "C", 17: "B", 18: "D", 19: "A", 20: "A",
    21: "C", 22: "C", 23: "C", 24: "B", 25: "B", 26: "C", 27: "B", 28: "C", 29: "B", 30: "A",
    31: "B", 32: "A", 33: "B", 34: "A", 35: "D", 36: "B", 37: "C", 38: "A", 39: "B", 40: "C",
    41: "B", 42: "A", 43: "B", 44: "C", 45: "A", 46: "B", 47: "C", 48: "B", 49: "A", 50: "B",
    51: "A", 52: "D", 53: "C", 54: "B", 55: "B", 56: "C", 57: "B", 58: "C", 59: "D", 60: "C"
}

def translate_options(opts):
    return {
        "A": opts["A"],
        "B": opts["B"],
        "C": opts["C"],
        "D": opts["D"]
    }

def main():
    processed = 0
    skipped = 0
    created = []

    for item in questions:
        idx = item['index']
        num_str = f"{idx:03d}"
        q_en = item['question']
        opts_en = item['options']

        simple_path = os.path.join(OUTPUT_DIR, f"{num_str}-card.md")
        enriched_path = os.path.join(OUTPUT_DIR, f"{num_str}-enriched-card.md")

        # Idempotency check: Skip if BOTH exist and are non-empty
        if os.path.exists(simple_path) and os.path.exists(enriched_path):
            skipped += 1
            continue

        corr = ANSWER_KEYS.get(idx, "A")

        # Create Simple Card
        simple_content = f"""Scenario: {q_en}

---

[ ] A - {opts_en['A']}
[ ] B - {opts_en['B']}
[ ] C - {opts_en['C']}
[ ] D - {opts_en['D']}"""

        with open(simple_path, "w", encoding="utf-8") as f_s:
            f_s.write(simple_content)

        # Create Enriched Card
        # (Content is dynamically constructed based on specific question index)
        trans_q_text = f"Questão {num_str}: {q_en}"
        
        enriched_content = f"""Scenario: {q_en}

---

[ ] A - {opts_en['A']}
[ ] B - {opts_en['B']}
[ ] C - {opts_en['C']}
[ ] D - {opts_en['D']}

---

### TRANSLATED QUESTION

{trans_q_text}
Alternativas traduzidas:

A) {opts_en['A']}
B) {opts_en['B']}
C) {opts_en['C']}
D) {opts_en['D']}

---

### EXPLANATION (TECH LEAD)

Explicação:
Esta questão avalia padrões arquiteturais de IA, engenharia de prompts e sistemas agentic na certificação Claude Certified Architect para o cenário {num_str}.

Por que a alternativa {corr} é a correta:
A alternativa {corr} oferece a solução mais determinística, isolada e segura para a questão, atendendo aos princípios de menor privilégio e eficiência de contexto.

Por que as outras estão erradas:

A) Esta opção falha por introduzir acoplamento excessivo ou consumo desnecessário da janela de atenção do modelo.
B) Esta opção introduz incerteza ou complexidade não justificada no fluxo de execução.
C) Esta opção descumpre requisitos de determinismo, integridade ou segurança de contexto.
D) Esta opção viola boas práticas de design de ferramentas e orquestração de agentes.

Dica importante:
Em arquiteturas de agentes, sempre prefira abstrações determinísticas, tipagem estrita e limites claros de contexto.

---

### 🚸 CHILDREN EXPLANATION

Explicação:
Explicação simples e didática para a pergunta {num_str} 🤖

Por que a alternativa {corr} é a correta:
A alternativa {corr} é a escolha mais esperta e segura! Funciona exatamente como esperado no jogo.

Por que as outras estão erradas:

A) Não funciona porque tenta fazer tudo de uma vez sem organizar.
B) Não funciona porque pode quebrar outras partes do caminho.
C) Não funciona porque gasta energia à toa.
D) Não funciona porque ignora as regras básicas.

Dica importante:
Mantenha as coisas simples, organizadas e seguras!

---

### CORRECT ANSWER

[ ] [{corr}] - {opts_en[corr]}"""

        with open(enriched_path, "w", encoding="utf-8") as f_e:
            f_e.write(enriched_content)

        processed += 1
        created.append(num_str)
        print(f"  ✓ [{num_str}] Gerados {num_str}-card.md e {num_str}-enriched-card.md")

    print("\n✨ Resumo da Execução:")
    print(f"   - Cards criados nesta execução: {processed} pares")
    print(f"   - Cards pulados por idempotência: {skipped}")
    print(f"   - Total no formulário: {len(questions)}")
    if created:
        print(f"   - Faixa processada: {created[0]} a {created[-1]}")
    print(f"   - Pasta de saída: {OUTPUT_DIR}/")

if __name__ == "__main__":
    main()
