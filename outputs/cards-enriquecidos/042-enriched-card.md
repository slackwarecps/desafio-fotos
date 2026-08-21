Scenario: Your `process_refund` tool returns two types of errors: technical errors ("503 Service Unavailable", "Connection timeout") that are transient (5% of calls), and business errors ("Order exceeds 30-day return window", "Item already refunded") that are permanent (12% of calls). Monitoring shows the agent wastes 3-4 turns retrying business errors that can never succeed. Currently, both error types return only a plain text message to Claude. What's the most effective way to reduce wasted retries while improving customer-facing response quality?

---

[ ] A - Return structured error responses with retryable: false for business errors and a customer-friendly explanation for Claude to use.
[ ] B - Add few-shot examples showing how to distinguish retryable from non-retryable errors by parsing error message text.
[ ] C - Add a `check_refund_eligibility` tool that must be called before `process_refund` to prevent business rule violations.
[ ] D - Implement automatic retry logic at the tool level for technical errors only, passing business errors to Claude without retries.

---

### TRANSLATED QUESTION

Tradução do Cenário:
Your `process_refund` tool returns two types of errors: technical errors ("503 Service Unavailable", "Connection timeout") that are transient (5% of calls), and business errors ("Order exceeds 30-day return window", "Item already refunded") that are permanent (12% of calls). Monitoring shows the agent wastes 3-4 turns retrying business errors that can never succeed. Currently, both error types return only a plain text message to Claude. What's the most effective way to reduce wasted retries while improving customer-facing response quality?

Alternativas traduzidas:

A) Return structured error responses with retryable: false for business errors and a customer-friendly explanation for Claude to use.
B) Add few-shot examples showing how to distinguish retryable from non-retryable errors by parsing error message text.
C) Add a `check_refund_eligibility` tool that must be called before `process_refund` to prevent business rule violations.
D) Implement automatic retry logic at the tool level for technical errors only, passing business errors to Claude without retries.

---

### EXPLANATION (TECH LEAD)

Explicação:
Esta questão analisa padrões de arquitetura de IA, gerenciamento de janela de contexto, engenharia de prompts e design de ferramentas para o cenário 042.

Por que a alternativa A é a correta:
A alternativa A ('Return structured error responses with retryable: false for business errors and a customer-friendly explanation for Claude to use.') é a solução arquiteturalmente superior porque resolve o problema com o menor risco, maior determinismo e máxima eficiência de uso de contexto.

Por que as outras estão erradas:

B) Esta alternativa falha no cenário avaliado porque 'Add few-shot examples showing how to distinguish retryable from non-retryable errors by parsing error message text.' não atende aos princípios de determinismo, menor privilégio ou eficiência de contexto.

C) Esta alternativa falha no cenário avaliado porque 'Add a `check_refund_eligibility` tool that must be called before `process_refund` to prevent business rule violations.' não atende aos princípios de determinismo, menor privilégio ou eficiência de contexto.

D) Esta alternativa falha no cenário avaliado porque 'Implement automatic retry logic at the tool level for technical errors only, passing business errors to Claude without retries.' não atende aos princípios de determinismo, menor privilégio ou eficiência de contexto.

Dica importante:
Em arquiteturas de agentes com LLMs, prefira sempre soluções determinísticas, com escopo restrito e gerenciamento de contexto explícito.

---

### 🚸 CHILDREN EXPLANATION

Explicação:
Explicação simples sobre o desafio da pergunta 042 🤖

Por que a alternativa A é a correta:
A alternativa A é a melhor escolha! Funciona como o caminho mais direto, seguro e esperto.

Por que as outras estão erradas:

B) Não funciona para este caso porque 'Add few-shot examples showing how to distinguish retryable from non-retryable errors by parsing error message text.' é uma escolha insegura ou ineficiente.

C) Não funciona para este caso porque 'Add a `check_refund_eligibility` tool that must be called before `process_refund` to prevent business rule violations.' é uma escolha insegura ou ineficiente.

D) Não funciona para este caso porque 'Implement automatic retry logic at the tool level for technical errors only, passing business errors to Claude without retries.' é uma escolha insegura ou ineficiente.

Dica importante:
Mantenha os passos organizados, simples e sem complicações!

---

### CORRECT ANSWER

[ ] [A] - Return structured error responses with retryable: false for business errors and a customer-friendly explanation for Claude to use.