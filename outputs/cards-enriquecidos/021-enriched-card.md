Scenario: Your extraction system implements automatic retries when validation fails. On each retry, the specific validation error is appended to the prompt. This retry-with-error-feedback approach resolves most failures within 2-3 attempts. For which failure pattern would additional retries be LEAST effective?

---

[ ] A - The model extracts keywords as a nested object organized by category when the schema requires a flat array of strings
[ ] B - The model extracts citation counts as locale-formatted strings ("1,234") when the schema requires integers
[ ] C - The model extracts dates as ISO 8601 datetime strings ("2023-03-15T00:00:00Z") when the schema requires only the date portion (YYYY-MM-DD)
[ ] D - The model extracts "et al." for co-authors when the full list exists only in an external document not in the input

---

### TRANSLATED QUESTION

Tradução do Cenário:
Your extraction system implements automatic retries when validation fails. On each retry, the specific validation error is appended to the prompt. This retry-with-error-feedback approach resolves most failures within 2-3 attempts. For which failure pattern would additional retries be LEAST effective?

Alternativas traduzidas:

A) The model extracts keywords as a nested object organized by category when the schema requires a flat array of strings
B) The model extracts citation counts as locale-formatted strings ("1,234") when the schema requires integers
C) The model extracts dates as ISO 8601 datetime strings ("2023-03-15T00:00:00Z") when the schema requires only the date portion (YYYY-MM-DD)
D) The model extracts "et al." for co-authors when the full list exists only in an external document not in the input

---

### EXPLANATION (TECH LEAD)

Explicação:
Esta questão analisa padrões de arquitetura de IA, gerenciamento de janela de contexto, engenharia de prompts e design de ferramentas para o cenário 021.

Por que a alternativa C é a correta:
A alternativa C ('The model extracts dates as ISO 8601 datetime strings ("2023-03-15T00:00:00Z") when the schema requires only the date portion (YYYY-MM-DD)') é a solução arquiteturalmente superior porque resolve o problema com o menor risco, maior determinismo e máxima eficiência de uso de contexto.

Por que as outras estão erradas:

A) Esta alternativa falha no cenário avaliado porque 'The model extracts keywords as a nested object organized by category when the schema requires a flat array of strings' não atende aos princípios de determinismo, menor privilégio ou eficiência de contexto.

B) Esta alternativa falha no cenário avaliado porque 'The model extracts citation counts as locale-formatted strings ("1,234") when the schema requires integers' não atende aos princípios de determinismo, menor privilégio ou eficiência de contexto.

D) Esta alternativa falha no cenário avaliado porque 'The model extracts "et al." for co-authors when the full list exists only in an external document not in the input' não atende aos princípios de determinismo, menor privilégio ou eficiência de contexto.

Dica importante:
Em arquiteturas de agentes com LLMs, prefira sempre soluções determinísticas, com escopo restrito e gerenciamento de contexto explícito.

---

### 🚸 CHILDREN EXPLANATION

Explicação:
Explicação simples sobre o desafio da pergunta 021 🤖

Por que a alternativa C é a correta:
A alternativa C é a melhor escolha! Funciona como o caminho mais direto, seguro e esperto.

Por que as outras estão erradas:

A) Não funciona para este caso porque 'The model extracts keywords as a nested object organized by category when the schema requires a flat array of strings' é uma escolha insegura ou ineficiente.

B) Não funciona para este caso porque 'The model extracts citation counts as locale-formatted strings ("1,234") when the schema requires integers' é uma escolha insegura ou ineficiente.

D) Não funciona para este caso porque 'The model extracts "et al." for co-authors when the full list exists only in an external document not in the input' é uma escolha insegura ou ineficiente.

Dica importante:
Mantenha os passos organizados, simples e sem complicações!

---

### CORRECT ANSWER

[ ] [C] - The model extracts dates as ISO 8601 datetime strings ("2023-03-15T00:00:00Z") when the schema requires only the date portion (YYYY-MM-DD)