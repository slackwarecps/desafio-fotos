Scenario: A contract is too long to fit in one context window, and you need fields from across the whole document. The dependable approach is to:

---

[ ] A - Truncate the document to what fits and extract from the first part.
[ ] B - Chunk the document with slight overlap, extract per chunk, then merge and reconcile the fields.
[ ] C - Summarize the document first, then extract from the summary.
[ ] D - Raise the temperature so the model fills in the missing parts.

---

### TRANSLATED QUESTION

Tradução do Cenário:
A contract is too long to fit in one context window, and you need fields from across the whole document. The dependable approach is to:

Alternativas traduzidas:

A) Truncate the document to what fits and extract from the first part.
B) Chunk the document with slight overlap, extract per chunk, then merge and reconcile the fields.
C) Summarize the document first, then extract from the summary.
D) Raise the temperature so the model fills in the missing parts.

---

### EXPLANATION (TECH LEAD)

Explicação:
Esta questão analisa padrões de arquitetura de IA, gerenciamento de janela de contexto, engenharia de prompts e design de ferramentas para o cenário 027.

Por que a alternativa B é a correta:
A alternativa B ('Chunk the document with slight overlap, extract per chunk, then merge and reconcile the fields.') é a solução arquiteturalmente superior porque resolve o problema com o menor risco, maior determinismo e máxima eficiência de uso de contexto.

Por que as outras estão erradas:

A) Esta alternativa falha no cenário avaliado porque 'Truncate the document to what fits and extract from the first part.' não atende aos princípios de determinismo, menor privilégio ou eficiência de contexto.

C) Esta alternativa falha no cenário avaliado porque 'Summarize the document first, then extract from the summary.' não atende aos princípios de determinismo, menor privilégio ou eficiência de contexto.

D) Esta alternativa falha no cenário avaliado porque 'Raise the temperature so the model fills in the missing parts.' não atende aos princípios de determinismo, menor privilégio ou eficiência de contexto.

Dica importante:
Em arquiteturas de agentes com LLMs, prefira sempre soluções determinísticas, com escopo restrito e gerenciamento de contexto explícito.

---

### 🚸 CHILDREN EXPLANATION

Explicação:
Explicação simples sobre o desafio da pergunta 027 🤖

Por que a alternativa B é a correta:
A alternativa B é a melhor escolha! Funciona como o caminho mais direto, seguro e esperto.

Por que as outras estão erradas:

A) Não funciona para este caso porque 'Truncate the document to what fits and extract from the first part.' é uma escolha insegura ou ineficiente.

C) Não funciona para este caso porque 'Summarize the document first, then extract from the summary.' é uma escolha insegura ou ineficiente.

D) Não funciona para este caso porque 'Raise the temperature so the model fills in the missing parts.' é uma escolha insegura ou ineficiente.

Dica importante:
Mantenha os passos organizados, simples e sem complicações!

---

### CORRECT ANSWER

[ ] [B] - Chunk the document with slight overlap, extract per chunk, then merge and reconcile the fields.