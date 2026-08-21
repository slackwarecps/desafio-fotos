Scenario: An engineer asks your agent to identify untested code paths in a legacy payment processing module spanning 45 files. After reading the first 8 source files, the agent's responses are becoming noticeably less accurate—it's forgetting previously discussed code patterns and hasn't yet located all test files or traced critical payment flows. What's the most effective approach to complete this investigation?

---

[ ] A - Document all current findings in a summary report, clear context completely, then use that report as the sole reference for continuing the investigation.
[ ] B - Spawn subagents to investigate specific questions (e.g., "find all test files for payment processing", "trace refund flow dependencies") while the main agent coordinates findings and preserves high-level understanding.
[ ] C - Clear context with /clear, then selectively re-read only the most critical files discovered so far, writing key findings to a scratchpad file that persists between context resets.
[ ] D - Switch to using Grep to search for specific function names instead of reading full files, reducing the content loaded into context for remaining exploration.

---

### TRANSLATED QUESTION

Tradução do Cenário:
An engineer asks your agent to identify untested code paths in a legacy payment processing module spanning 45 files. After reading the first 8 source files, the agent's responses are becoming noticeably less accurate—it's forgetting previously discussed code patterns and hasn't yet located all test files or traced critical payment flows. What's the most effective approach to complete this investigation?

Alternativas traduzidas:

A) Document all current findings in a summary report, clear context completely, then use that report as the sole reference for continuing the investigation.
B) Spawn subagents to investigate specific questions (e.g., "find all test files for payment processing", "trace refund flow dependencies") while the main agent coordinates findings and preserves high-level understanding.
C) Clear context with /clear, then selectively re-read only the most critical files discovered so far, writing key findings to a scratchpad file that persists between context resets.
D) Switch to using Grep to search for specific function names instead of reading full files, reducing the content loaded into context for remaining exploration.

---

### EXPLANATION (TECH LEAD)

Explicação:
Esta questão analisa padrões de arquitetura de IA, gerenciamento de janela de contexto, engenharia de prompts e design de ferramentas para o cenário 024.

Por que a alternativa B é a correta:
A alternativa B ('Spawn subagents to investigate specific questions (e.g., "find all test files for payment processing", "trace refund flow dependencies") while the main agent coordinates findings and preserves high-level understanding.') é a solução arquiteturalmente superior porque resolve o problema com o menor risco, maior determinismo e máxima eficiência de uso de contexto.

Por que as outras estão erradas:

A) Esta alternativa falha no cenário avaliado porque 'Document all current findings in a summary report, clear context completely, then use that report as the sole reference for continuing the investigation.' não atende aos princípios de determinismo, menor privilégio ou eficiência de contexto.

C) Esta alternativa falha no cenário avaliado porque 'Clear context with /clear, then selectively re-read only the most critical files discovered so far, writing key findings to a scratchpad file that persists between context resets.' não atende aos princípios de determinismo, menor privilégio ou eficiência de contexto.

D) Esta alternativa falha no cenário avaliado porque 'Switch to using Grep to search for specific function names instead of reading full files, reducing the content loaded into context for remaining exploration.' não atende aos princípios de determinismo, menor privilégio ou eficiência de contexto.

Dica importante:
Em arquiteturas de agentes com LLMs, prefira sempre soluções determinísticas, com escopo restrito e gerenciamento de contexto explícito.

---

### 🚸 CHILDREN EXPLANATION

Explicação:
Explicação simples sobre o desafio da pergunta 024 🤖

Por que a alternativa B é a correta:
A alternativa B é a melhor escolha! Funciona como o caminho mais direto, seguro e esperto.

Por que as outras estão erradas:

A) Não funciona para este caso porque 'Document all current findings in a summary report, clear context completely, then use that report as the sole reference for continuing the investigation.' é uma escolha insegura ou ineficiente.

C) Não funciona para este caso porque 'Clear context with /clear, then selectively re-read only the most critical files discovered so far, writing key findings to a scratchpad file that persists between context resets.' é uma escolha insegura ou ineficiente.

D) Não funciona para este caso porque 'Switch to using Grep to search for specific function names instead of reading full files, reducing the content loaded into context for remaining exploration.' é uma escolha insegura ou ineficiente.

Dica importante:
Mantenha os passos organizados, simples e sem complicações!

---

### CORRECT ANSWER

[ ] [B] - Spawn subagents to investigate specific questions (e.g., "find all test files for payment processing", "trace refund flow dependencies") while the main agent coordinates findings and preserves high-level understanding.