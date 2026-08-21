Scenario: Your extraction pipeline processes invoices and extracts line items, subtotals, tax amounts, and grand totals. During evaluation, you discover that in 18% of extractions, the sum of extracted line item amounts doesn't match the extracted grand total—sometimes due to OCR errors in the source document, sometimes due to extraction mistakes by the model. Downstream accounting systems reject records with mismatched totals. What's the most effective approach to improve extraction reliability?

---

[ ] A - Add a "`calculated_total`" field where the model sums extracted line items alongside a "`stated_total`" field. Flag records for human review when values differ.
[ ] B - Extract line items and totals independently, then use a separate validation model to reconcile discrepancies by determining which extracted values are most likely correct.
[ ] C - Add few-shot examples demonstrating invoices where extracted line items sum correctly to the stated total, encouraging the model to produce mathematically consistent extractions.
[ ] D - Implement post-processing that automatically adjusts line item amounts proportionally when their sum doesn't match the stated total.

---

### TRANSLATED QUESTION

Tradução do Cenário:
Your extraction pipeline processes invoices and extracts line items, subtotals, tax amounts, and grand totals. During evaluation, you discover that in 18% of extractions, the sum of extracted line item amounts doesn't match the extracted grand total—sometimes due to OCR errors in the source document, sometimes due to extraction mistakes by the model. Downstream accounting systems reject records with mismatched totals. What's the most effective approach to improve extraction reliability?

Alternativas traduzidas:

A) Add a "`calculated_total`" field where the model sums extracted line items alongside a "`stated_total`" field. Flag records for human review when values differ.
B) Extract line items and totals independently, then use a separate validation model to reconcile discrepancies by determining which extracted values are most likely correct.
C) Add few-shot examples demonstrating invoices where extracted line items sum correctly to the stated total, encouraging the model to produce mathematically consistent extractions.
D) Implement post-processing that automatically adjusts line item amounts proportionally when their sum doesn't match the stated total.

---

### EXPLANATION (TECH LEAD)

Explicação:
Esta questão analisa padrões de arquitetura de IA, gerenciamento de janela de contexto, engenharia de prompts e design de ferramentas para o cenário 005.

Por que a alternativa A é a correta:
A alternativa A ('Add a "`calculated_total`" field where the model sums extracted line items alongside a "`stated_total`" field. Flag records for human review when values differ.') é a solução arquiteturalmente superior porque resolve o problema com o menor risco, maior determinismo e máxima eficiência de uso de contexto.

Por que as outras estão erradas:

B) Esta alternativa falha no cenário avaliado porque 'Extract line items and totals independently, then use a separate validation model to reconcile discrepancies by determining which extracted values are most likely correct.' não atende aos princípios de determinismo, menor privilégio ou eficiência de contexto.

C) Esta alternativa falha no cenário avaliado porque 'Add few-shot examples demonstrating invoices where extracted line items sum correctly to the stated total, encouraging the model to produce mathematically consistent extractions.' não atende aos princípios de determinismo, menor privilégio ou eficiência de contexto.

D) Esta alternativa falha no cenário avaliado porque 'Implement post-processing that automatically adjusts line item amounts proportionally when their sum doesn't match the stated total.' não atende aos princípios de determinismo, menor privilégio ou eficiência de contexto.

Dica importante:
Em arquiteturas de agentes com LLMs, prefira sempre soluções determinísticas, com escopo restrito e gerenciamento de contexto explícito.

---

### 🚸 CHILDREN EXPLANATION

Explicação:
Explicação simples sobre o desafio da pergunta 005 🤖

Por que a alternativa A é a correta:
A alternativa A é a melhor escolha! Funciona como o caminho mais direto, seguro e esperto.

Por que as outras estão erradas:

B) Não funciona para este caso porque 'Extract line items and totals independently, then use a separate validation model to reconcile discrepancies by determining which extracted values are most likely correct.' é uma escolha insegura ou ineficiente.

C) Não funciona para este caso porque 'Add few-shot examples demonstrating invoices where extracted line items sum correctly to the stated total, encouraging the model to produce mathematically consistent extractions.' é uma escolha insegura ou ineficiente.

D) Não funciona para este caso porque 'Implement post-processing that automatically adjusts line item amounts proportionally when their sum doesn't match the stated total.' é uma escolha insegura ou ineficiente.

Dica importante:
Mantenha os passos organizados, simples e sem complicações!

---

### CORRECT ANSWER

[ ] [A] - Add a "`calculated_total`" field where the model sums extracted line items alongside a "`stated_total`" field. Flag records for human review when values differ.