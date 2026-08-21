Scenario: An engineer who just joined the team asks the agent to help them understand the authentication and authorization architecture before making security improvements. The codebase has 800+ files across multiple services. What exploration strategy will most effectively build understanding, given Claude built-in tools and context limits?

---

[ ] A - Read any CLAUDE.md and README files first, then ask the engineer to specify which 10-15 files are most important for understanding the auth system.
[ ] B - Launch parallel subagents to explore different services simultaneously, then synthesize their findings into an architectural overview.
[ ] C - Use Grep to find authentication entry points, read those files, then follow imports and function calls to map the auth flow incrementally.
[ ] D - Read all files containing "auth", "login", "permission", or "token" in their content or filename.

---

### TRANSLATED QUESTION

Tradução do Cenário:
An engineer who just joined the team asks the agent to help them understand the authentication and authorization architecture before making security improvements. The codebase has 800+ files across multiple services. What exploration strategy will most effectively build understanding, given Claude built-in tools and context limits?

Alternativas traduzidas:

A) Read any CLAUDE.md and README files first, then ask the engineer to specify which 10-15 files are most important for understanding the auth system.
B) Launch parallel subagents to explore different services simultaneously, then synthesize their findings into an architectural overview.
C) Use Grep to find authentication entry points, read those files, then follow imports and function calls to map the auth flow incrementally.
D) Read all files containing "auth", "login", "permission", or "token" in their content or filename.

---

### EXPLANATION (TECH LEAD)

Explicação:
Esta questão analisa padrões de arquitetura de IA, gerenciamento de janela de contexto, engenharia de prompts e design de ferramentas para o cenário 003.

Por que a alternativa C é a correta:
A alternativa C ('Use Grep to find authentication entry points, read those files, then follow imports and function calls to map the auth flow incrementally.') é a solução arquiteturalmente superior porque resolve o problema com o menor risco, maior determinismo e máxima eficiência de uso de contexto.

Por que as outras estão erradas:

A) Esta alternativa falha no cenário avaliado porque 'Read any CLAUDE.md and README files first, then ask the engineer to specify which 10-15 files are most important for understanding the auth system.' não atende aos princípios de determinismo, menor privilégio ou eficiência de contexto.

B) Esta alternativa falha no cenário avaliado porque 'Launch parallel subagents to explore different services simultaneously, then synthesize their findings into an architectural overview.' não atende aos princípios de determinismo, menor privilégio ou eficiência de contexto.

D) Esta alternativa falha no cenário avaliado porque 'Read all files containing "auth", "login", "permission", or "token" in their content or filename.' não atende aos princípios de determinismo, menor privilégio ou eficiência de contexto.

Dica importante:
Em arquiteturas de agentes com LLMs, prefira sempre soluções determinísticas, com escopo restrito e gerenciamento de contexto explícito.

---

### 🚸 CHILDREN EXPLANATION

Explicação:
Explicação simples sobre o desafio da pergunta 003 🤖

Por que a alternativa C é a correta:
A alternativa C é a melhor escolha! Funciona como o caminho mais direto, seguro e esperto.

Por que as outras estão erradas:

A) Não funciona para este caso porque 'Read any CLAUDE.md and README files first, then ask the engineer to specify which 10-15 files are most important for understanding the auth system.' é uma escolha insegura ou ineficiente.

B) Não funciona para este caso porque 'Launch parallel subagents to explore different services simultaneously, then synthesize their findings into an architectural overview.' é uma escolha insegura ou ineficiente.

D) Não funciona para este caso porque 'Read all files containing "auth", "login", "permission", or "token" in their content or filename.' é uma escolha insegura ou ineficiente.

Dica importante:
Mantenha os passos organizados, simples e sem complicações!

---

### CORRECT ANSWER

[ ] [C] - Use Grep to find authentication entry points, read those files, then follow imports and function calls to map the auth flow incrementally.