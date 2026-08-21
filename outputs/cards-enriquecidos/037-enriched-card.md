Scenario: Your schema includes a skills: string[] field. Production monitoring reveals three consistency issues: (1) compound phrases like "Python and SQL" are sometimes kept as one entry, sometimes split; (2) implied but unstated skills occasionally appear in extractions; (3) similar documents produce wildly different array lengths (5-10 vs 40+ entries). Your prompt currently says "Extract all skills mentioned." What's the most effective improvement?

---

[ ] A - Add few-shot examples demonstrating compound phrase handling, explicit mention criteria, and appropriate entry granularity.
[ ] B - Add constraints: "Extract 10-20 skills maximum, one skill per entry, only explicitly named skills."
[ ] C - Add post-extraction normalization that maps skills to a canonical taxonomy and deduplicates similar entries.
[ ] D - Enrich the schema to {skill: string, confidence: float, `source_quote`: string}[] to capture extraction metadata.

---

### TRANSLATED QUESTION

Tradução do Cenário:
Your schema includes a skills: string[] field. Production monitoring reveals three consistency issues: (1) compound phrases like "Python and SQL" are sometimes kept as one entry, sometimes split; (2) implied but unstated skills occasionally appear in extractions; (3) similar documents produce wildly different array lengths (5-10 vs 40+ entries). Your prompt currently says "Extract all skills mentioned." What's the most effective improvement?

Alternativas traduzidas:

A) Add few-shot examples demonstrating compound phrase handling, explicit mention criteria, and appropriate entry granularity.
B) Add constraints: "Extract 10-20 skills maximum, one skill per entry, only explicitly named skills."
C) Add post-extraction normalization that maps skills to a canonical taxonomy and deduplicates similar entries.
D) Enrich the schema to {skill: string, confidence: float, `source_quote`: string}[] to capture extraction metadata.

---

### EXPLANATION (TECH LEAD)

Explicação:
Esta questão analisa padrões de arquitetura de IA, gerenciamento de janela de contexto, engenharia de prompts e design de ferramentas para o cenário 037.

Por que a alternativa C é a correta:
A alternativa C ('Add post-extraction normalization that maps skills to a canonical taxonomy and deduplicates similar entries.') é a solução arquiteturalmente superior porque resolve o problema com o menor risco, maior determinismo e máxima eficiência de uso de contexto.

Por que as outras estão erradas:

A) Esta alternativa falha no cenário avaliado porque 'Add few-shot examples demonstrating compound phrase handling, explicit mention criteria, and appropriate entry granularity.' não atende aos princípios de determinismo, menor privilégio ou eficiência de contexto.

B) Esta alternativa falha no cenário avaliado porque 'Add constraints: "Extract 10-20 skills maximum, one skill per entry, only explicitly named skills."' não atende aos princípios de determinismo, menor privilégio ou eficiência de contexto.

D) Esta alternativa falha no cenário avaliado porque 'Enrich the schema to {skill: string, confidence: float, `source_quote`: string}[] to capture extraction metadata.' não atende aos princípios de determinismo, menor privilégio ou eficiência de contexto.

Dica importante:
Em arquiteturas de agentes com LLMs, prefira sempre soluções determinísticas, com escopo restrito e gerenciamento de contexto explícito.

---

### 🚸 CHILDREN EXPLANATION

Explicação:
Explicação simples sobre o desafio da pergunta 037 🤖

Por que a alternativa C é a correta:
A alternativa C é a melhor escolha! Funciona como o caminho mais direto, seguro e esperto.

Por que as outras estão erradas:

A) Não funciona para este caso porque 'Add few-shot examples demonstrating compound phrase handling, explicit mention criteria, and appropriate entry granularity.' é uma escolha insegura ou ineficiente.

B) Não funciona para este caso porque 'Add constraints: "Extract 10-20 skills maximum, one skill per entry, only explicitly named skills."' é uma escolha insegura ou ineficiente.

D) Não funciona para este caso porque 'Enrich the schema to {skill: string, confidence: float, `source_quote`: string}[] to capture extraction metadata.' é uma escolha insegura ou ineficiente.

Dica importante:
Mantenha os passos organizados, simples e sem complicações!

---

### CORRECT ANSWER

[ ] [C] - Add post-extraction normalization that maps skills to a canonical taxonomy and deduplicates similar entries.