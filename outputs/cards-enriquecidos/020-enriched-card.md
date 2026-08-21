Scenario: Production logs reveal inconsistent error handling: when `lookup_order` fails, the agent sometimes retries 5+ times (wasteful when the order ID doesn't exist), sometimes escalates immediately (premature for temporary network issues), and sometimes asks users for clarification (inappropriate when the issue is a backend permission error). Investigation shows your MCP tool returns uniform error responses: {"isError": true, "content": [{"type": "text", "text": "Operation failed"}]}. The agent cannot distinguish between error types. What's the most effective improvement?

---

[ ] A - Enhance error responses with structured metadata: include errorCategory (transient/validation/permission), isRetryable boolean, and a description of what caused the failure.
[ ] B - Create an `analyze_error` MCP tool the agent calls after any failure to determine the error category and recommended action.
[ ] C - Implement retry logic with exponential backoff in your MCP server for all errors, returning to the agent only after retries are exhausted.
[ ] D - Add few-shot examples to the system prompt demonstrating how to interpret error message patterns and select appropriate responses for each.

---

### TRANSLATED QUESTION

Tradução do Cenário:
Production logs reveal inconsistent error handling: when `lookup_order` fails, the agent sometimes retries 5+ times (wasteful when the order ID doesn't exist), sometimes escalates immediately (premature for temporary network issues), and sometimes asks users for clarification (inappropriate when the issue is a backend permission error). Investigation shows your MCP tool returns uniform error responses: {"isError": true, "content": [{"type": "text", "text": "Operation failed"}]}. The agent cannot distinguish between error types. What's the most effective improvement?

Alternativas traduzidas:

A) Enhance error responses with structured metadata: include errorCategory (transient/validation/permission), isRetryable boolean, and a description of what caused the failure.
B) Create an `analyze_error` MCP tool the agent calls after any failure to determine the error category and recommended action.
C) Implement retry logic with exponential backoff in your MCP server for all errors, returning to the agent only after retries are exhausted.
D) Add few-shot examples to the system prompt demonstrating how to interpret error message patterns and select appropriate responses for each.

---

### EXPLANATION (TECH LEAD)

Explicação:
Esta questão analisa padrões de arquitetura de IA, gerenciamento de janela de contexto, engenharia de prompts e design de ferramentas para o cenário 020.

Por que a alternativa A é a correta:
A alternativa A ('Enhance error responses with structured metadata: include errorCategory (transient/validation/permission), isRetryable boolean, and a description of what caused the failure.') é a solução arquiteturalmente superior porque resolve o problema com o menor risco, maior determinismo e máxima eficiência de uso de contexto.

Por que as outras estão erradas:

B) Esta alternativa falha no cenário avaliado porque 'Create an `analyze_error` MCP tool the agent calls after any failure to determine the error category and recommended action.' não atende aos princípios de determinismo, menor privilégio ou eficiência de contexto.

C) Esta alternativa falha no cenário avaliado porque 'Implement retry logic with exponential backoff in your MCP server for all errors, returning to the agent only after retries are exhausted.' não atende aos princípios de determinismo, menor privilégio ou eficiência de contexto.

D) Esta alternativa falha no cenário avaliado porque 'Add few-shot examples to the system prompt demonstrating how to interpret error message patterns and select appropriate responses for each.' não atende aos princípios de determinismo, menor privilégio ou eficiência de contexto.

Dica importante:
Em arquiteturas de agentes com LLMs, prefira sempre soluções determinísticas, com escopo restrito e gerenciamento de contexto explícito.

---

### 🚸 CHILDREN EXPLANATION

Explicação:
Explicação simples sobre o desafio da pergunta 020 🤖

Por que a alternativa A é a correta:
A alternativa A é a melhor escolha! Funciona como o caminho mais direto, seguro e esperto.

Por que as outras estão erradas:

B) Não funciona para este caso porque 'Create an `analyze_error` MCP tool the agent calls after any failure to determine the error category and recommended action.' é uma escolha insegura ou ineficiente.

C) Não funciona para este caso porque 'Implement retry logic with exponential backoff in your MCP server for all errors, returning to the agent only after retries are exhausted.' é uma escolha insegura ou ineficiente.

D) Não funciona para este caso porque 'Add few-shot examples to the system prompt demonstrating how to interpret error message patterns and select appropriate responses for each.' é uma escolha insegura ou ineficiente.

Dica importante:
Mantenha os passos organizados, simples e sem complicações!

---

### CORRECT ANSWER

[ ] [A] - Enhance error responses with structured metadata: include errorCategory (transient/validation/permission), isRetryable boolean, and a description of what caused the failure.