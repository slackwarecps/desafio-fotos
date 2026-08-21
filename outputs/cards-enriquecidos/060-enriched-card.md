Scenario: Your pipeline uses a tool called `extract_metadata` with a JSON schema for paper details. You've also defined `lookup_citations` and `verify_doi` tools for enrichment. During testing, you notice that when users include requests like "extract the metadata and tell me how cited it is," Claude sometimes calls `lookup_citations` first, which fails because it needs the DOI that `extract_metadata` would provide. What's the most effective way to ensure structured metadata extraction happens first?

---

[ ] A - Set `tool_choice` to "any" so Claude must use a tool, combined with system prompt instructions prioritizing `extract_metadata`.
[ ] B - Set `tool_choice` to "auto" and reorder the tool definitions so `extract_metadata` appears first in the tools array, since Claude prioritizes earlier-listed tools.
[ ] C - Set `tool_choice` to {"type": "tool", "name": "`extract_metadata`"} and process the enrichment requests in subsequent turns after receiving the extracted metadata.
[ ] D - Set `tool_choice` to {"type": "tool", "name": "`extract_metadata`"} for every API call in the pipeline, ensuring Claude always extracts metadata before any enrichment can occur.

---

### TRANSLATED QUESTION

Tradução do Cenário:
Your pipeline uses a tool called `extract_metadata` with a JSON schema for paper details. You've also defined `lookup_citations` and `verify_doi` tools for enrichment. During testing, you notice that when users include requests like "extract the metadata and tell me how cited it is," Claude sometimes calls `lookup_citations` first, which fails because it needs the DOI that `extract_metadata` would provide. What's the most effective way to ensure structured metadata extraction happens first?

Alternativas traduzidas:

A) Set `tool_choice` to "any" so Claude must use a tool, combined with system prompt instructions prioritizing `extract_metadata`.
B) Set `tool_choice` to "auto" and reorder the tool definitions so `extract_metadata` appears first in the tools array, since Claude prioritizes earlier-listed tools.
C) Set `tool_choice` to {"type": "tool", "name": "`extract_metadata`"} and process the enrichment requests in subsequent turns after receiving the extracted metadata.
D) Set `tool_choice` to {"type": "tool", "name": "`extract_metadata`"} for every API call in the pipeline, ensuring Claude always extracts metadata before any enrichment can occur.

---

### EXPLANATION (TECH LEAD)

Explicação:
Esta questão analisa padrões de arquitetura de IA, gerenciamento de janela de contexto, engenharia de prompts e design de ferramentas para o cenário 060.

Por que a alternativa C é a correta:
A alternativa C ('Set `tool_choice` to {"type": "tool", "name": "`extract_metadata`"} and process the enrichment requests in subsequent turns after receiving the extracted metadata.') é a solução arquiteturalmente superior porque resolve o problema com o menor risco, maior determinismo e máxima eficiência de uso de contexto.

Por que as outras estão erradas:

A) Esta alternativa falha no cenário avaliado porque 'Set `tool_choice` to "any" so Claude must use a tool, combined with system prompt instructions prioritizing `extract_metadata`.' não atende aos princípios de determinismo, menor privilégio ou eficiência de contexto.

B) Esta alternativa falha no cenário avaliado porque 'Set `tool_choice` to "auto" and reorder the tool definitions so `extract_metadata` appears first in the tools array, since Claude prioritizes earlier-listed tools.' não atende aos princípios de determinismo, menor privilégio ou eficiência de contexto.

D) Esta alternativa falha no cenário avaliado porque 'Set `tool_choice` to {"type": "tool", "name": "`extract_metadata`"} for every API call in the pipeline, ensuring Claude always extracts metadata before any enrichment can occur.' não atende aos princípios de determinismo, menor privilégio ou eficiência de contexto.

Dica importante:
Em arquiteturas de agentes com LLMs, prefira sempre soluções determinísticas, com escopo restrito e gerenciamento de contexto explícito.

---

### 🚸 CHILDREN EXPLANATION

Explicação:
Explicação simples sobre o desafio da pergunta 060 🤖

Por que a alternativa C é a correta:
A alternativa C é a melhor escolha! Funciona como o caminho mais direto, seguro e esperto.

Por que as outras estão erradas:

A) Não funciona para este caso porque 'Set `tool_choice` to "any" so Claude must use a tool, combined with system prompt instructions prioritizing `extract_metadata`.' é uma escolha insegura ou ineficiente.

B) Não funciona para este caso porque 'Set `tool_choice` to "auto" and reorder the tool definitions so `extract_metadata` appears first in the tools array, since Claude prioritizes earlier-listed tools.' é uma escolha insegura ou ineficiente.

D) Não funciona para este caso porque 'Set `tool_choice` to {"type": "tool", "name": "`extract_metadata`"} for every API call in the pipeline, ensuring Claude always extracts metadata before any enrichment can occur.' é uma escolha insegura ou ineficiente.

Dica importante:
Mantenha os passos organizados, simples e sem complicações!

---

### CORRECT ANSWER

[ ] [C] - Set `tool_choice` to {"type": "tool", "name": "`extract_metadata`"} and process the enrichment requests in subsequent turns after receiving the extracted metadata.