Scenario: A research agent must gather facts from eight independent web sources and produce one synthesis. None of the sources depend on each other. Which dispatch pattern stays fast without flooding the coordinator context?

---

[ ] A - Read all eight sources into the coordinator context, then write the synthesis in a single pass.
[ ] B - Dispatch eight sub-agents in parallel, each returning a short structured summary with citations, then synthesize from the summaries.
[ ] C - Process the sources one at a time in a single agent, appending each full page to the running prompt.
[ ] D - Pick the two sources that look most promising and ignore the rest to save tokens.

---

### TRANSLATED QUESTION

Tradução do Cenário:
A research agent must gather facts from eight independent web sources and produce one synthesis. None of the sources depend on each other. Which dispatch pattern stays fast without flooding the coordinator context?

Alternativas traduzidas:

A) Read all eight sources into the coordinator context, then write the synthesis in a single pass.
B) Dispatch eight sub-agents in parallel, each returning a short structured summary with citations, then synthesize from the summaries.
C) Process the sources one at a time in a single agent, appending each full page to the running prompt.
D) Pick the two sources that look most promising and ignore the rest to save tokens.

---

### EXPLANATION (TECH LEAD)

Explicação:
Esta questão analisa padrões de arquitetura de IA, gerenciamento de janela de contexto, engenharia de prompts e design de ferramentas para o cenário 050.

Por que a alternativa B é a correta:
A alternativa B ('Dispatch eight sub-agents in parallel, each returning a short structured summary with citations, then synthesize from the summaries.') é a solução arquiteturalmente superior porque resolve o problema com o menor risco, maior determinismo e máxima eficiência de uso de contexto.

Por que as outras estão erradas:

A) Esta alternativa falha no cenário avaliado porque 'Read all eight sources into the coordinator context, then write the synthesis in a single pass.' não atende aos princípios de determinismo, menor privilégio ou eficiência de contexto.

C) Esta alternativa falha no cenário avaliado porque 'Process the sources one at a time in a single agent, appending each full page to the running prompt.' não atende aos princípios de determinismo, menor privilégio ou eficiência de contexto.

D) Esta alternativa falha no cenário avaliado porque 'Pick the two sources that look most promising and ignore the rest to save tokens.' não atende aos princípios de determinismo, menor privilégio ou eficiência de contexto.

Dica importante:
Em arquiteturas de agentes com LLMs, prefira sempre soluções determinísticas, com escopo restrito e gerenciamento de contexto explícito.

---

### 🚸 CHILDREN EXPLANATION

Explicação:
Explicação simples sobre o desafio da pergunta 050 🤖

Por que a alternativa B é a correta:
A alternativa B é a melhor escolha! Funciona como o caminho mais direto, seguro e esperto.

Por que as outras estão erradas:

A) Não funciona para este caso porque 'Read all eight sources into the coordinator context, then write the synthesis in a single pass.' é uma escolha insegura ou ineficiente.

C) Não funciona para este caso porque 'Process the sources one at a time in a single agent, appending each full page to the running prompt.' é uma escolha insegura ou ineficiente.

D) Não funciona para este caso porque 'Pick the two sources that look most promising and ignore the rest to save tokens.' é uma escolha insegura ou ineficiente.

Dica importante:
Mantenha os passos organizados, simples e sem complicações!

---

### CORRECT ANSWER

[ ] [B] - Dispatch eight sub-agents in parallel, each returning a short structured summary with citations, then synthesize from the summaries.