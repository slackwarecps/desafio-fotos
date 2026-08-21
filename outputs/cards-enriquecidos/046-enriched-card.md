Scenario: Your extraction pipeline processes restaurant menus and must output structured JSON with fields for item names, descriptions, prices, and dietary tags. Some menus use inconsistent formatting—prices as "$12" vs "12.00", dietary info as icons vs text. What's the most reliable approach?

---

[ ] A - Use separate extraction calls for each field to ensure consistent handling of each type.
[ ] B - Extract data as-is and normalize formats in post-processing code after Claude returns.
[ ] C - Request multiple extraction attempts per document and select the most common format.
[ ] D - Define a strict output schema and include format normalization rules in your prompt.

---

### TRANSLATED QUESTION

Tradução do Cenário:
Your extraction pipeline processes restaurant menus and must output structured JSON with fields for item names, descriptions, prices, and dietary tags. Some menus use inconsistent formatting—prices as "$12" vs "12.00", dietary info as icons vs text. What's the most reliable approach?

Alternativas traduzidas:

A) Use separate extraction calls for each field to ensure consistent handling of each type.
B) Extract data as-is and normalize formats in post-processing code after Claude returns.
C) Request multiple extraction attempts per document and select the most common format.
D) Define a strict output schema and include format normalization rules in your prompt.

---

### EXPLANATION (TECH LEAD)

Explicação:
Esta questão analisa padrões de arquitetura de IA, gerenciamento de janela de contexto, engenharia de prompts e design de ferramentas para o cenário 046.

Por que a alternativa B é a correta:
A alternativa B ('Extract data as-is and normalize formats in post-processing code after Claude returns.') é a solução arquiteturalmente superior porque resolve o problema com o menor risco, maior determinismo e máxima eficiência de uso de contexto.

Por que as outras estão erradas:

A) Esta alternativa falha no cenário avaliado porque 'Use separate extraction calls for each field to ensure consistent handling of each type.' não atende aos princípios de determinismo, menor privilégio ou eficiência de contexto.

C) Esta alternativa falha no cenário avaliado porque 'Request multiple extraction attempts per document and select the most common format.' não atende aos princípios de determinismo, menor privilégio ou eficiência de contexto.

D) Esta alternativa falha no cenário avaliado porque 'Define a strict output schema and include format normalization rules in your prompt.' não atende aos princípios de determinismo, menor privilégio ou eficiência de contexto.

Dica importante:
Em arquiteturas de agentes com LLMs, prefira sempre soluções determinísticas, com escopo restrito e gerenciamento de contexto explícito.

---

### 🚸 CHILDREN EXPLANATION

Explicação:
Explicação simples sobre o desafio da pergunta 046 🤖

Por que a alternativa B é a correta:
A alternativa B é a melhor escolha! Funciona como o caminho mais direto, seguro e esperto.

Por que as outras estão erradas:

A) Não funciona para este caso porque 'Use separate extraction calls for each field to ensure consistent handling of each type.' é uma escolha insegura ou ineficiente.

C) Não funciona para este caso porque 'Request multiple extraction attempts per document and select the most common format.' é uma escolha insegura ou ineficiente.

D) Não funciona para este caso porque 'Define a strict output schema and include format normalization rules in your prompt.' é uma escolha insegura ou ineficiente.

Dica importante:
Mantenha os passos organizados, simples e sem complicações!

---

### CORRECT ANSWER

[ ] [B] - Extract data as-is and normalize formats in post-processing code after Claude returns.