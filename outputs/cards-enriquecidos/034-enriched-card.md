Scenario: Your extraction system processes two document types: standard monthly reports (archived after processing) and urgent exception reports (must trigger business alerts within 30 minutes of receipt). Both use the same JSON schema. You want to minimize API costs while meeting latency requirements. How should you architect the processing pipeline?

---

[ ] A - Submit all documents to the real-time Messages API to ensure consistent processing latency across document types.
[ ] B - Submit all documents to the `Batch API` with `custom_ids` for tracking. When results arrive, immediately process urgent documents and trigger delayed alerts for exceptions.
[ ] C - Queue all documents and submit hourly batches, flagging urgent documents for expedited handling when batch results return.
[ ] D - Route standard reports to the `Batch API` for 50% cost savings, and route urgent exception reports to the real-time Messages API.

---

### TRANSLATED QUESTION

Tradução do Cenário:
Your extraction system processes two document types: standard monthly reports (archived after processing) and urgent exception reports (must trigger business alerts within 30 minutes of receipt). Both use the same JSON schema. You want to minimize API costs while meeting latency requirements. How should you architect the processing pipeline?

Alternativas traduzidas:

A) Submit all documents to the real-time Messages API to ensure consistent processing latency across document types.
B) Submit all documents to the `Batch API` with `custom_ids` for tracking. When results arrive, immediately process urgent documents and trigger delayed alerts for exceptions.
C) Queue all documents and submit hourly batches, flagging urgent documents for expedited handling when batch results return.
D) Route standard reports to the `Batch API` for 50% cost savings, and route urgent exception reports to the real-time Messages API.

---

### EXPLANATION (TECH LEAD)

Explicação:
Esta questão analisa padrões de arquitetura de IA, gerenciamento de janela de contexto, engenharia de prompts e design de ferramentas para o cenário 034.

Por que a alternativa A é a correta:
A alternativa A ('Submit all documents to the real-time Messages API to ensure consistent processing latency across document types.') é a solução arquiteturalmente superior porque resolve o problema com o menor risco, maior determinismo e máxima eficiência de uso de contexto.

Por que as outras estão erradas:

B) Esta alternativa falha no cenário avaliado porque 'Submit all documents to the `Batch API` with `custom_ids` for tracking. When results arrive, immediately process urgent documents and trigger delayed alerts for exceptions.' não atende aos princípios de determinismo, menor privilégio ou eficiência de contexto.

C) Esta alternativa falha no cenário avaliado porque 'Queue all documents and submit hourly batches, flagging urgent documents for expedited handling when batch results return.' não atende aos princípios de determinismo, menor privilégio ou eficiência de contexto.

D) Esta alternativa falha no cenário avaliado porque 'Route standard reports to the `Batch API` for 50% cost savings, and route urgent exception reports to the real-time Messages API.' não atende aos princípios de determinismo, menor privilégio ou eficiência de contexto.

Dica importante:
Em arquiteturas de agentes com LLMs, prefira sempre soluções determinísticas, com escopo restrito e gerenciamento de contexto explícito.

---

### 🚸 CHILDREN EXPLANATION

Explicação:
Explicação simples sobre o desafio da pergunta 034 🤖

Por que a alternativa A é a correta:
A alternativa A é a melhor escolha! Funciona como o caminho mais direto, seguro e esperto.

Por que as outras estão erradas:

B) Não funciona para este caso porque 'Submit all documents to the `Batch API` with `custom_ids` for tracking. When results arrive, immediately process urgent documents and trigger delayed alerts for exceptions.' é uma escolha insegura ou ineficiente.

C) Não funciona para este caso porque 'Queue all documents and submit hourly batches, flagging urgent documents for expedited handling when batch results return.' é uma escolha insegura ou ineficiente.

D) Não funciona para este caso porque 'Route standard reports to the `Batch API` for 50% cost savings, and route urgent exception reports to the real-time Messages API.' é uma escolha insegura ou ineficiente.

Dica importante:
Mantenha os passos organizados, simples e sem complicações!

---

### CORRECT ANSWER

[ ] [A] - Submit all documents to the real-time Messages API to ensure consistent processing latency across document types.