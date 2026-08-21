Scenario: The agent verifies customer identity through a multi-step process before resetting passwords. During testing, you notice that after the customer answers the third verification question, the agent asks them to provide their name again, as if the earlier exchange never happened. What's the most likely cause of this behavior?

---

[ ] A - The verification tool is clearing the agent's internal state after each successful validation step.
[ ] B - The prompt lacks instructions telling Claude to remember information across multiple exchanges.
[ ] C - The conversation history isn't being passed in subsequent API requests.
[ ] D - Claude's memory retention is limited to two conversational turns by default, requiring explicit configuration to extend it.

---

### TRANSLATED QUESTION

Tradução do Cenário:
The agent verifies customer identity through a multi-step process before resetting passwords. During testing, you notice that after the customer answers the third verification question, the agent asks them to provide their name again, as if the earlier exchange never happened. What's the most likely cause of this behavior?

Alternativas traduzidas:

A) The verification tool is clearing the agent's internal state after each successful validation step.
B) The prompt lacks instructions telling Claude to remember information across multiple exchanges.
C) The conversation history isn't being passed in subsequent API requests.
D) Claude's memory retention is limited to two conversational turns by default, requiring explicit configuration to extend it.

---

### EXPLANATION (TECH LEAD)

Explicação:
Esta questão analisa padrões de arquitetura de IA, gerenciamento de janela de contexto, engenharia de prompts e design de ferramentas para o cenário 022.

Por que a alternativa C é a correta:
A alternativa C ('The conversation history isn't being passed in subsequent API requests.') é a solução arquiteturalmente superior porque resolve o problema com o menor risco, maior determinismo e máxima eficiência de uso de contexto.

Por que as outras estão erradas:

A) Esta alternativa falha no cenário avaliado porque 'The verification tool is clearing the agent's internal state after each successful validation step.' não atende aos princípios de determinismo, menor privilégio ou eficiência de contexto.

B) Esta alternativa falha no cenário avaliado porque 'The prompt lacks instructions telling Claude to remember information across multiple exchanges.' não atende aos princípios de determinismo, menor privilégio ou eficiência de contexto.

D) Esta alternativa falha no cenário avaliado porque 'Claude's memory retention is limited to two conversational turns by default, requiring explicit configuration to extend it.' não atende aos princípios de determinismo, menor privilégio ou eficiência de contexto.

Dica importante:
Em arquiteturas de agentes com LLMs, prefira sempre soluções determinísticas, com escopo restrito e gerenciamento de contexto explícito.

---

### 🚸 CHILDREN EXPLANATION

Explicação:
Explicação simples sobre o desafio da pergunta 022 🤖

Por que a alternativa C é a correta:
A alternativa C é a melhor escolha! Funciona como o caminho mais direto, seguro e esperto.

Por que as outras estão erradas:

A) Não funciona para este caso porque 'The verification tool is clearing the agent's internal state after each successful validation step.' é uma escolha insegura ou ineficiente.

B) Não funciona para este caso porque 'The prompt lacks instructions telling Claude to remember information across multiple exchanges.' é uma escolha insegura ou ineficiente.

D) Não funciona para este caso porque 'Claude's memory retention is limited to two conversational turns by default, requiring explicit configuration to extend it.' é uma escolha insegura ou ineficiente.

Dica importante:
Mantenha os passos organizados, simples e sem complicações!

---

### CORRECT ANSWER

[ ] [C] - The conversation history isn't being passed in subsequent API requests.