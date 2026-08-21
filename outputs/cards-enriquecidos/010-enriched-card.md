Scenario: A single source file is thousands of lines long and the agent needs one function from it. The agent should:

---

[ ] A - Read the entire file into context to be thorough.
[ ] B - Search within the file for the function and read only that region and its immediate dependencies.
[ ] C - Read the first few hundred lines and stop.
[ ] D - Reformat the file so it is easier to scan.

---

### TRANSLATED QUESTION

Tradução do Cenário:
A single source file is thousands of lines long and the agent needs one function from it. The agent should:

Alternativas traduzidas:

A) Read the entire file into context to be thorough.
B) Search within the file for the function and read only that region and its immediate dependencies.
C) Read the first few hundred lines and stop.
D) Reformat the file so it is easier to scan.

---

### EXPLANATION (TECH LEAD)

Explicação:
Esta questão analisa padrões de arquitetura de IA, gerenciamento de janela de contexto, engenharia de prompts e design de ferramentas para o cenário 010.

Por que a alternativa B é a correta:
A alternativa B ('Search within the file for the function and read only that region and its immediate dependencies.') é a solução arquiteturalmente superior porque resolve o problema com o menor risco, maior determinismo e máxima eficiência de uso de contexto.

Por que as outras estão erradas:

A) Esta alternativa falha no cenário avaliado porque 'Read the entire file into context to be thorough.' não atende aos princípios de determinismo, menor privilégio ou eficiência de contexto.

C) Esta alternativa falha no cenário avaliado porque 'Read the first few hundred lines and stop.' não atende aos princípios de determinismo, menor privilégio ou eficiência de contexto.

D) Esta alternativa falha no cenário avaliado porque 'Reformat the file so it is easier to scan.' não atende aos princípios de determinismo, menor privilégio ou eficiência de contexto.

Dica importante:
Em arquiteturas de agentes com LLMs, prefira sempre soluções determinísticas, com escopo restrito e gerenciamento de contexto explícito.

---

### 🚸 CHILDREN EXPLANATION

Explicação:
Explicação simples sobre o desafio da pergunta 010 🤖

Por que a alternativa B é a correta:
A alternativa B é a melhor escolha! Funciona como o caminho mais direto, seguro e esperto.

Por que as outras estão erradas:

A) Não funciona para este caso porque 'Read the entire file into context to be thorough.' é uma escolha insegura ou ineficiente.

C) Não funciona para este caso porque 'Read the first few hundred lines and stop.' é uma escolha insegura ou ineficiente.

D) Não funciona para este caso porque 'Reformat the file so it is easier to scan.' é uma escolha insegura ou ineficiente.

Dica importante:
Mantenha os passos organizados, simples e sem complicações!

---

### CORRECT ANSWER

[ ] [B] - Search within the file for the function and read only that region and its immediate dependencies.