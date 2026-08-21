Scenario: Your extraction pipeline processes contracts that frequently include amendments. When a contract contains both original terms and later amendments (e.g., original clause specifies "30-day payment terms" while Amendment 1 changes this to "45 days"), the model inconsistently extracts one value or the other with no indication of which applies. What's the most effective approach to improve extraction accuracy for documents with amendments?

---

[ ] A - Redesign the schema so amended fields capture multiple values, each with source location and effective date.
[ ] B - Add prompt instructions to always extract the most recent amendment value and ignore superseded original terms.
[ ] C - Preprocess documents with a classifier that identifies and removes superseded sections before the main extraction step.
[ ] D - Implement post-extraction validation using pattern matching to detect amendments and flag those extractions for manual review.

---

### TRANSLATED QUESTION

Tradução do Cenário:
Your extraction pipeline processes contracts that frequently include amendments. When a contract contains both original terms and later amendments (e.g., original clause specifies "30-day payment terms" while Amendment 1 changes this to "45 days"), the model inconsistently extracts one value or the other with no indication of which applies. What's the most effective approach to improve extraction accuracy for documents with amendments?

Alternativas traduzidas:

A) Redesign the schema so amended fields capture multiple values, each with source location and effective date.
B) Add prompt instructions to always extract the most recent amendment value and ignore superseded original terms.
C) Preprocess documents with a classifier that identifies and removes superseded sections before the main extraction step.
D) Implement post-extraction validation using pattern matching to detect amendments and flag those extractions for manual review.

---

### EXPLANATION (TECH LEAD)

Explicação:
Esta questão analisa padrões de arquitetura de IA, gerenciamento de janela de contexto, engenharia de prompts e design de ferramentas para o cenário 011.

Por que a alternativa A é a correta:
A alternativa A ('Redesign the schema so amended fields capture multiple values, each with source location and effective date.') é a solução arquiteturalmente superior porque resolve o problema com o menor risco, maior determinismo e máxima eficiência de uso de contexto.

Por que as outras estão erradas:

B) Esta alternativa falha no cenário avaliado porque 'Add prompt instructions to always extract the most recent amendment value and ignore superseded original terms.' não atende aos princípios de determinismo, menor privilégio ou eficiência de contexto.

C) Esta alternativa falha no cenário avaliado porque 'Preprocess documents with a classifier that identifies and removes superseded sections before the main extraction step.' não atende aos princípios de determinismo, menor privilégio ou eficiência de contexto.

D) Esta alternativa falha no cenário avaliado porque 'Implement post-extraction validation using pattern matching to detect amendments and flag those extractions for manual review.' não atende aos princípios de determinismo, menor privilégio ou eficiência de contexto.

Dica importante:
Em arquiteturas de agentes com LLMs, prefira sempre soluções determinísticas, com escopo restrito e gerenciamento de contexto explícito.

---

### 🚸 CHILDREN EXPLANATION

Explicação:
Explicação simples sobre o desafio da pergunta 011 🤖

Por que a alternativa A é a correta:
A alternativa A é a melhor escolha! Funciona como o caminho mais direto, seguro e esperto.

Por que as outras estão erradas:

B) Não funciona para este caso porque 'Add prompt instructions to always extract the most recent amendment value and ignore superseded original terms.' é uma escolha insegura ou ineficiente.

C) Não funciona para este caso porque 'Preprocess documents with a classifier that identifies and removes superseded sections before the main extraction step.' é uma escolha insegura ou ineficiente.

D) Não funciona para este caso porque 'Implement post-extraction validation using pattern matching to detect amendments and flag those extractions for manual review.' é uma escolha insegura ou ineficiente.

Dica importante:
Mantenha os passos organizados, simples e sem complicações!

---

### CORRECT ANSWER

[ ] [A] - Redesign the schema so amended fields capture multiple values, each with source location and effective date.