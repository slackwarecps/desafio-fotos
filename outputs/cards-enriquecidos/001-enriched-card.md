Scenario: Your agent needs to insert a new helper function into the middle of a 150-line utility module, between two existing functions. The Edit tool fails because its `old_string` parameter cannot find unique text to match — the file has repetitive docstrings, variable names, and structural patterns. What's the most reliable way to complete this insertion?

---

[ ] A - Use Edit with an extremely long `old_string` capturing 30+ lines of context to guarantee uniqueness
[ ] B - Use Edit's `replace_all` parameter to target a common pattern and embed the new function in the replacement text
[ ] C - Use Bash to append the function definition to the end of the file using heredoc syntax
[ ] D - Use Read to load the file, add the function at the appropriate location, then Write the updated file

---

### TRANSLATED QUESTION

Tradução do Cenário:
Your agent needs to insert a new helper function into the middle of a 150-line utility module, between two existing functions. The Edit tool fails because its `old_string` parameter cannot find unique text to match — the file has repetitive docstrings, variable names, and structural patterns. What's the most reliable way to complete this insertion?

Alternativas traduzidas:

A) Use Edit with an extremely long `old_string` capturing 30+ lines of context to guarantee uniqueness
B) Use Edit's `replace_all` parameter to target a common pattern and embed the new function in the replacement text
C) Use Bash to append the function definition to the end of the file using heredoc syntax
D) Use Read to load the file, add the function at the appropriate location, then Write the updated file

---

### EXPLANATION (TECH LEAD)

Explicação:
Esta questão analisa padrões de arquitetura de IA, gerenciamento de janela de contexto, engenharia de prompts e design de ferramentas para o cenário 001.

Por que a alternativa D é a correta:
A alternativa D ('Use Read to load the file, add the function at the appropriate location, then Write the updated file') é a solução arquiteturalmente superior porque resolve o problema com o menor risco, maior determinismo e máxima eficiência de uso de contexto.

Por que as outras estão erradas:

A) Esta alternativa falha no cenário avaliado porque 'Use Edit with an extremely long `old_string` capturing 30+ lines of context to guarantee uniqueness' não atende aos princípios de determinismo, menor privilégio ou eficiência de contexto.

B) Esta alternativa falha no cenário avaliado porque 'Use Edit's `replace_all` parameter to target a common pattern and embed the new function in the replacement text' não atende aos princípios de determinismo, menor privilégio ou eficiência de contexto.

C) Esta alternativa falha no cenário avaliado porque 'Use Bash to append the function definition to the end of the file using heredoc syntax' não atende aos princípios de determinismo, menor privilégio ou eficiência de contexto.

Dica importante:
Em arquiteturas de agentes com LLMs, prefira sempre soluções determinísticas, com escopo restrito e gerenciamento de contexto explícito.

---

### 🚸 CHILDREN EXPLANATION

Explicação:
Explicação simples sobre o desafio da pergunta 001 🤖

Por que a alternativa D é a correta:
A alternativa D é a melhor escolha! Funciona como o caminho mais direto, seguro e esperto.

Por que as outras estão erradas:

A) Não funciona para este caso porque 'Use Edit with an extremely long `old_string` capturing 30+ lines of context to guarantee uniqueness' é uma escolha insegura ou ineficiente.

B) Não funciona para este caso porque 'Use Edit's `replace_all` parameter to target a common pattern and embed the new function in the replacement text' é uma escolha insegura ou ineficiente.

C) Não funciona para este caso porque 'Use Bash to append the function definition to the end of the file using heredoc syntax' é uma escolha insegura ou ineficiente.

Dica importante:
Mantenha os passos organizados, simples e sem complicações!

---

### CORRECT ANSWER

[ ] [D] - Use Read to load the file, add the function at the appropriate location, then Write the updated file