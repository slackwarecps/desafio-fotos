Scenario: A customer raises three separate issues during one session: a refund inquiry (turns 1-15), a subscription question (turns 16-30), and a payment method update (turns 31-45). At turn 48, the customer asks "What happened with my refund?" The conversation is approaching context limits. What strategy best maintains the agent's ability to address all issues throughout the session?

---

[ ] A - Extract and persist structured issue data (order IDs, amounts, statuses) into a separate context layer.
[ ] B - Rely on MCP tools to re-fetch relevant information on demand when the customer references earlier issues.
[ ] C - Summarize earlier turns into a narrative description, preserving full message history only for the active issue.
[ ] D - Implement sliding window context that retains the most recent 30 turns.

---

### TRANSLATED QUESTION

Tradução do Cenário:
A customer raises three separate issues during one session: a refund inquiry (turns 1-15), a subscription question (turns 16-30), and a payment method update (turns 31-45). At turn 48, the customer asks "What happened with my refund?" The conversation is approaching context limits. What strategy best maintains the agent's ability to address all issues throughout the session?

Alternativas traduzidas:

A) Extract and persist structured issue data (order IDs, amounts, statuses) into a separate context layer.
B) Rely on MCP tools to re-fetch relevant information on demand when the customer references earlier issues.
C) Summarize earlier turns into a narrative description, preserving full message history only for the active issue.
D) Implement sliding window context that retains the most recent 30 turns.

---

### EXPLANATION (TECH LEAD)

Explicação:
Esta questão analisa padrões de arquitetura de IA, gerenciamento de janela de contexto, engenharia de prompts e design de ferramentas para o cenário 018.

Por que a alternativa D é a correta:
A alternativa D ('Implement sliding window context that retains the most recent 30 turns.') é a solução arquiteturalmente superior porque resolve o problema com o menor risco, maior determinismo e máxima eficiência de uso de contexto.

Por que as outras estão erradas:

A) Esta alternativa falha no cenário avaliado porque 'Extract and persist structured issue data (order IDs, amounts, statuses) into a separate context layer.' não atende aos princípios de determinismo, menor privilégio ou eficiência de contexto.

B) Esta alternativa falha no cenário avaliado porque 'Rely on MCP tools to re-fetch relevant information on demand when the customer references earlier issues.' não atende aos princípios de determinismo, menor privilégio ou eficiência de contexto.

C) Esta alternativa falha no cenário avaliado porque 'Summarize earlier turns into a narrative description, preserving full message history only for the active issue.' não atende aos princípios de determinismo, menor privilégio ou eficiência de contexto.

Dica importante:
Em arquiteturas de agentes com LLMs, prefira sempre soluções determinísticas, com escopo restrito e gerenciamento de contexto explícito.

---

### 🚸 CHILDREN EXPLANATION

Explicação:
Explicação simples sobre o desafio da pergunta 018 🤖

Por que a alternativa D é a correta:
A alternativa D é a melhor escolha! Funciona como o caminho mais direto, seguro e esperto.

Por que as outras estão erradas:

A) Não funciona para este caso porque 'Extract and persist structured issue data (order IDs, amounts, statuses) into a separate context layer.' é uma escolha insegura ou ineficiente.

B) Não funciona para este caso porque 'Rely on MCP tools to re-fetch relevant information on demand when the customer references earlier issues.' é uma escolha insegura ou ineficiente.

C) Não funciona para este caso porque 'Summarize earlier turns into a narrative description, preserving full message history only for the active issue.' é uma escolha insegura ou ineficiente.

Dica importante:
Mantenha os passos organizados, simples e sem complicações!

---

### CORRECT ANSWER

[ ] [D] - Implement sliding window context that retains the most recent 30 turns.