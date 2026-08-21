Scenario: A developer asks the agent to investigate why a specific API endpoint intermittently returns 500 errors. The codebase has 200+ files and the developer doesn't know which components are involved. The agent must trace the error through routing, middleware, business logic, and database layers. What task decomposition approach would be most effective?

---

[ ] A - Have the agent first create a comprehensive plan mapping all code paths through the endpoint before beginning any file exploration or code reading.
[ ] B - Have the agent dynamically generate investigation subtasks based on what it discovers at each step, adapting its exploration plan as new information about the error path emerges.
[ ] C - Define a fixed sequence of investigation steps upfront—grep for error patterns, then read error handlers, then check database queries, then examine middleware—executing each step regardless of intermediate findings.
[ ] D - Run parallel worker agents that simultaneously investigate all four layers, then synthesize their findings to identify where the error originates.

---

### TRANSLATED QUESTION

Tradução do Cenário:
A developer asks the agent to investigate why a specific API endpoint intermittently returns 500 errors. The codebase has 200+ files and the developer doesn't know which components are involved. The agent must trace the error through routing, middleware, business logic, and database layers. What task decomposition approach would be most effective?

Alternativas traduzidas:

A) Have the agent first create a comprehensive plan mapping all code paths through the endpoint before beginning any file exploration or code reading.
B) Have the agent dynamically generate investigation subtasks based on what it discovers at each step, adapting its exploration plan as new information about the error path emerges.
C) Define a fixed sequence of investigation steps upfront—grep for error patterns, then read error handlers, then check database queries, then examine middleware—executing each step regardless of intermediate findings.
D) Run parallel worker agents that simultaneously investigate all four layers, then synthesize their findings to identify where the error originates.

---

### EXPLANATION (TECH LEAD)

Explicação:
Esta questão analisa padrões de arquitetura de IA, gerenciamento de janela de contexto, engenharia de prompts e design de ferramentas para o cenário 012.

Por que a alternativa D é a correta:
A alternativa D ('Run parallel worker agents that simultaneously investigate all four layers, then synthesize their findings to identify where the error originates.') é a solução arquiteturalmente superior porque resolve o problema com o menor risco, maior determinismo e máxima eficiência de uso de contexto.

Por que as outras estão erradas:

A) Esta alternativa falha no cenário avaliado porque 'Have the agent first create a comprehensive plan mapping all code paths through the endpoint before beginning any file exploration or code reading.' não atende aos princípios de determinismo, menor privilégio ou eficiência de contexto.

B) Esta alternativa falha no cenário avaliado porque 'Have the agent dynamically generate investigation subtasks based on what it discovers at each step, adapting its exploration plan as new information about the error path emerges.' não atende aos princípios de determinismo, menor privilégio ou eficiência de contexto.

C) Esta alternativa falha no cenário avaliado porque 'Define a fixed sequence of investigation steps upfront—grep for error patterns, then read error handlers, then check database queries, then examine middleware—executing each step regardless of intermediate findings.' não atende aos princípios de determinismo, menor privilégio ou eficiência de contexto.

Dica importante:
Em arquiteturas de agentes com LLMs, prefira sempre soluções determinísticas, com escopo restrito e gerenciamento de contexto explícito.

---

### 🚸 CHILDREN EXPLANATION

Explicação:
Explicação simples sobre o desafio da pergunta 012 🤖

Por que a alternativa D é a correta:
A alternativa D é a melhor escolha! Funciona como o caminho mais direto, seguro e esperto.

Por que as outras estão erradas:

A) Não funciona para este caso porque 'Have the agent first create a comprehensive plan mapping all code paths through the endpoint before beginning any file exploration or code reading.' é uma escolha insegura ou ineficiente.

B) Não funciona para este caso porque 'Have the agent dynamically generate investigation subtasks based on what it discovers at each step, adapting its exploration plan as new information about the error path emerges.' é uma escolha insegura ou ineficiente.

C) Não funciona para este caso porque 'Define a fixed sequence of investigation steps upfront—grep for error patterns, then read error handlers, then check database queries, then examine middleware—executing each step regardless of intermediate findings.' é uma escolha insegura ou ineficiente.

Dica importante:
Mantenha os passos organizados, simples e sem complicações!

---

### CORRECT ANSWER

[ ] [D] - Run parallel worker agents that simultaneously investigate all four layers, then synthesize their findings to identify where the error originates.