Scenario: During testing, you observe that in extended exploration sessions (30+ minutes), the agent starts giving inconsistent answers about code structure it discussed earlier. Engineers report having to repeat context about modules they've already explored. What's the most effective approach to address this?

---

[ ] A - Have the agent maintain a scratchpad file that records key findings, referencing it for subsequent questions.
[ ] B - Switch to a higher-capacity model tier to provide more context window space for accumulated exploration data.
[ ] C - Implement automatic context clearing every 15 minutes to ensure the agent starts with fresh, uncontaminated context.
[ ] D - Create summaries of all source files before exploration begins, loading only these compressed representations into context.

---

### TRANSLATED QUESTION

Tradução do Cenário:
During testing, you observe that in extended exploration sessions (30+ minutes), the agent starts giving inconsistent answers about code structure it discussed earlier. Engineers report having to repeat context about modules they've already explored. What's the most effective approach to address this?

Alternativas traduzidas:

A) Have the agent maintain a scratchpad file that records key findings, referencing it for subsequent questions.
B) Switch to a higher-capacity model tier to provide more context window space for accumulated exploration data.
C) Implement automatic context clearing every 15 minutes to ensure the agent starts with fresh, uncontaminated context.
D) Create summaries of all source files before exploration begins, loading only these compressed representations into context.

---

### EXPLANATION (TECH LEAD)

Explicação:
Esta questão analisa padrões de arquitetura de IA, gerenciamento de janela de contexto, engenharia de prompts e design de ferramentas para o cenário 041.

Por que a alternativa B é a correta:
A alternativa B ('Switch to a higher-capacity model tier to provide more context window space for accumulated exploration data.') é a solução arquiteturalmente superior porque resolve o problema com o menor risco, maior determinismo e máxima eficiência de uso de contexto.

Por que as outras estão erradas:

A) Esta alternativa falha no cenário avaliado porque 'Have the agent maintain a scratchpad file that records key findings, referencing it for subsequent questions.' não atende aos princípios de determinismo, menor privilégio ou eficiência de contexto.

C) Esta alternativa falha no cenário avaliado porque 'Implement automatic context clearing every 15 minutes to ensure the agent starts with fresh, uncontaminated context.' não atende aos princípios de determinismo, menor privilégio ou eficiência de contexto.

D) Esta alternativa falha no cenário avaliado porque 'Create summaries of all source files before exploration begins, loading only these compressed representations into context.' não atende aos princípios de determinismo, menor privilégio ou eficiência de contexto.

Dica importante:
Em arquiteturas de agentes com LLMs, prefira sempre soluções determinísticas, com escopo restrito e gerenciamento de contexto explícito.

---

### 🚸 CHILDREN EXPLANATION

Explicação:
Explicação simples sobre o desafio da pergunta 041 🤖

Por que a alternativa B é a correta:
A alternativa B é a melhor escolha! Funciona como o caminho mais direto, seguro e esperto.

Por que as outras estão erradas:

A) Não funciona para este caso porque 'Have the agent maintain a scratchpad file that records key findings, referencing it for subsequent questions.' é uma escolha insegura ou ineficiente.

C) Não funciona para este caso porque 'Implement automatic context clearing every 15 minutes to ensure the agent starts with fresh, uncontaminated context.' é uma escolha insegura ou ineficiente.

D) Não funciona para este caso porque 'Create summaries of all source files before exploration begins, loading only these compressed representations into context.' é uma escolha insegura ou ineficiente.

Dica importante:
Mantenha os passos organizados, simples e sem complicações!

---

### CORRECT ANSWER

[ ] [B] - Switch to a higher-capacity model tier to provide more context window space for accumulated exploration data.