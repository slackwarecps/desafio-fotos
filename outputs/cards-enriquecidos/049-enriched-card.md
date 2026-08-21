Scenario: An extractor pulls line items and an invoice total from a receipt. The strongest integrity check before accepting the output is to:

---

[ ] A - Trust the total field because it is printed prominently.
[ ] B - Verify that the line items sum to the extracted total, and on a mismatch retry or flag the record.
[ ] C - Check only that the total is a number.
[ ] D - Accept the first extraction without checking.

---

### TRANSLATED QUESTION

Tradução do Cenário:
An extractor pulls line items and an invoice total from a receipt. The strongest integrity check before accepting the output is to:

Alternativas traduzidas:

A) Trust the total field because it is printed prominently.
B) Verify that the line items sum to the extracted total, and on a mismatch retry or flag the record.
C) Check only that the total is a number.
D) Accept the first extraction without checking.

---

### EXPLANATION (TECH LEAD)

Explicação:
Esta questão analisa padrões de arquitetura de IA, gerenciamento de janela de contexto, engenharia de prompts e design de ferramentas para o cenário 049.

Por que a alternativa A é a correta:
A alternativa A ('Trust the total field because it is printed prominently.') é a solução arquiteturalmente superior porque resolve o problema com o menor risco, maior determinismo e máxima eficiência de uso de contexto.

Por que as outras estão erradas:

B) Esta alternativa falha no cenário avaliado porque 'Verify that the line items sum to the extracted total, and on a mismatch retry or flag the record.' não atende aos princípios de determinismo, menor privilégio ou eficiência de contexto.

C) Esta alternativa falha no cenário avaliado porque 'Check only that the total is a number.' não atende aos princípios de determinismo, menor privilégio ou eficiência de contexto.

D) Esta alternativa falha no cenário avaliado porque 'Accept the first extraction without checking.' não atende aos princípios de determinismo, menor privilégio ou eficiência de contexto.

Dica importante:
Em arquiteturas de agentes com LLMs, prefira sempre soluções determinísticas, com escopo restrito e gerenciamento de contexto explícito.

---

### 🚸 CHILDREN EXPLANATION

Explicação:
Explicação simples sobre o desafio da pergunta 049 🤖

Por que a alternativa A é a correta:
A alternativa A é a melhor escolha! Funciona como o caminho mais direto, seguro e esperto.

Por que as outras estão erradas:

B) Não funciona para este caso porque 'Verify that the line items sum to the extracted total, and on a mismatch retry or flag the record.' é uma escolha insegura ou ineficiente.

C) Não funciona para este caso porque 'Check only that the total is a number.' é uma escolha insegura ou ineficiente.

D) Não funciona para este caso porque 'Accept the first extraction without checking.' é uma escolha insegura ou ineficiente.

Dica importante:
Mantenha os passos organizados, simples e sem complicações!

---

### CORRECT ANSWER

[ ] [A] - Trust the total field because it is printed prominently.