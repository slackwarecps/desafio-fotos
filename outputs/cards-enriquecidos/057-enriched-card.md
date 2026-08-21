Scenario: Your system extracts event metadata (date, location, organizer, `attendee_count`) from news articles using a JSON schema with all nullable fields. During evaluation, you observe the model frequently generates plausible but incorrect values for fields not mentioned in the article—for example, outputting "500" for `attendee_count` when the source contains no attendance information. What's the most effective way to reduce these false extractions?

---

[ ] A - Add a post-processing step using a second LLM call to verify each extracted value exists in the source document.
[ ] B - Add prompt instructions to return null for any field where information is not directly stated in the source.
[ ] C - Make all schema fields required (non-nullable) with strict validation rules to ensure the model only outputs verifiable data.
[ ] D - Upgrade to a more capable model tier with improved instruction-following to reduce hallucination tendencies.

---

### TRANSLATED QUESTION

Tradução do Cenário:
Your system extracts event metadata (date, location, organizer, `attendee_count`) from news articles using a JSON schema with all nullable fields. During evaluation, you observe the model frequently generates plausible but incorrect values for fields not mentioned in the article—for example, outputting "500" for `attendee_count` when the source contains no attendance information. What's the most effective way to reduce these false extractions?

Alternativas traduzidas:

A) Add a post-processing step using a second LLM call to verify each extracted value exists in the source document.
B) Add prompt instructions to return null for any field where information is not directly stated in the source.
C) Make all schema fields required (non-nullable) with strict validation rules to ensure the model only outputs verifiable data.
D) Upgrade to a more capable model tier with improved instruction-following to reduce hallucination tendencies.

---

### EXPLANATION (TECH LEAD)

Explicação:
Esta questão analisa padrões de arquitetura de IA, gerenciamento de janela de contexto, engenharia de prompts e design de ferramentas para o cenário 057.

Por que a alternativa B é a correta:
A alternativa B ('Add prompt instructions to return null for any field where information is not directly stated in the source.') é a solução arquiteturalmente superior porque resolve o problema com o menor risco, maior determinismo e máxima eficiência de uso de contexto.

Por que as outras estão erradas:

A) Esta alternativa falha no cenário avaliado porque 'Add a post-processing step using a second LLM call to verify each extracted value exists in the source document.' não atende aos princípios de determinismo, menor privilégio ou eficiência de contexto.

C) Esta alternativa falha no cenário avaliado porque 'Make all schema fields required (non-nullable) with strict validation rules to ensure the model only outputs verifiable data.' não atende aos princípios de determinismo, menor privilégio ou eficiência de contexto.

D) Esta alternativa falha no cenário avaliado porque 'Upgrade to a more capable model tier with improved instruction-following to reduce hallucination tendencies.' não atende aos princípios de determinismo, menor privilégio ou eficiência de contexto.

Dica importante:
Em arquiteturas de agentes com LLMs, prefira sempre soluções determinísticas, com escopo restrito e gerenciamento de contexto explícito.

---

### 🚸 CHILDREN EXPLANATION

Explicação:
Explicação simples sobre o desafio da pergunta 057 🤖

Por que a alternativa B é a correta:
A alternativa B é a melhor escolha! Funciona como o caminho mais direto, seguro e esperto.

Por que as outras estão erradas:

A) Não funciona para este caso porque 'Add a post-processing step using a second LLM call to verify each extracted value exists in the source document.' é uma escolha insegura ou ineficiente.

C) Não funciona para este caso porque 'Make all schema fields required (non-nullable) with strict validation rules to ensure the model only outputs verifiable data.' é uma escolha insegura ou ineficiente.

D) Não funciona para este caso porque 'Upgrade to a more capable model tier with improved instruction-following to reduce hallucination tendencies.' é uma escolha insegura ou ineficiente.

Dica importante:
Mantenha os passos organizados, simples e sem complicações!

---

### CORRECT ANSWER

[ ] [B] - Add prompt instructions to return null for any field where information is not directly stated in the source.