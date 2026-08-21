Scenario: A research agent keeps spawning follow-up searches and the run is not converging. The most reliable way to prevent an endless loop is to:

---

[ ] A - Let it continue until it naturally stops.
[ ] B - Give the task an explicit budget and a coverage check, and stop once the questions are answered or the budget is spent.
[ ] C - Cut the run off at a random time.
[ ] D - Add more sub-agents so it finishes sooner.

---

### TRANSLATED QUESTION

Tradução do Cenário:
A research agent keeps spawning follow-up searches and the run is not converging. The most reliable way to prevent an endless loop is to:

Alternativas traduzidas:

A) Let it continue until it naturally stops.
B) Give the task an explicit budget and a coverage check, and stop once the questions are answered or the budget is spent.
C) Cut the run off at a random time.
D) Add more sub-agents so it finishes sooner.

---

### EXPLANATION (TECH LEAD)

Explicação:
Esta questão analisa padrões de arquitetura de IA, gerenciamento de janela de contexto, engenharia de prompts e design de ferramentas para o cenário 054.

Por que a alternativa B é a correta:
A alternativa B ('Give the task an explicit budget and a coverage check, and stop once the questions are answered or the budget is spent.') é a solução arquiteturalmente superior porque resolve o problema com o menor risco, maior determinismo e máxima eficiência de uso de contexto.

Por que as outras estão erradas:

A) Esta alternativa falha no cenário avaliado porque 'Let it continue until it naturally stops.' não atende aos princípios de determinismo, menor privilégio ou eficiência de contexto.

C) Esta alternativa falha no cenário avaliado porque 'Cut the run off at a random time.' não atende aos princípios de determinismo, menor privilégio ou eficiência de contexto.

D) Esta alternativa falha no cenário avaliado porque 'Add more sub-agents so it finishes sooner.' não atende aos princípios de determinismo, menor privilégio ou eficiência de contexto.

Dica importante:
Em arquiteturas de agentes com LLMs, prefira sempre soluções determinísticas, com escopo restrito e gerenciamento de contexto explícito.

---

### 🚸 CHILDREN EXPLANATION

Explicação:
Explicação simples sobre o desafio da pergunta 054 🤖

Por que a alternativa B é a correta:
A alternativa B é a melhor escolha! Funciona como o caminho mais direto, seguro e esperto.

Por que as outras estão erradas:

A) Não funciona para este caso porque 'Let it continue until it naturally stops.' é uma escolha insegura ou ineficiente.

C) Não funciona para este caso porque 'Cut the run off at a random time.' é uma escolha insegura ou ineficiente.

D) Não funciona para este caso porque 'Add more sub-agents so it finishes sooner.' é uma escolha insegura ou ineficiente.

Dica importante:
Mantenha os passos organizados, simples e sem complicações!

---

### CORRECT ANSWER

[ ] [B] - Give the task an explicit budget and a coverage check, and stop once the questions are answered or the budget is spent.