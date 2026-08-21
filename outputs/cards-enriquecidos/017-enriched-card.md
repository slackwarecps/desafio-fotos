Scenario: The synthesis agent receives summarized findings from the web search and document analysis agents, then passes a consolidated summary to the report generator. During testing, you discover the generated reports make factual claims without proper citations—the report generator cannot attribute statements to their original sources because that metadata was lost during the summarization steps. What's the most effective approach to ensure proper source attribution in the final reports?

---

[ ] A - Have each agent output structured data separating content summaries from source metadata (URLs, document names, page numbers).
[ ] B - Have the report generator query the web search agent to re-locate sources for claims in the final report.
[ ] C - Instruct the synthesis agent to embed source references inline within its summary text using a consistent citation format.
[ ] D - Skip summarization and pass full raw outputs from web search and document analysis directly to the report generator.

---

### TRANSLATED QUESTION

Tradução do Cenário:
The synthesis agent receives summarized findings from the web search and document analysis agents, then passes a consolidated summary to the report generator. During testing, you discover the generated reports make factual claims without proper citations—the report generator cannot attribute statements to their original sources because that metadata was lost during the summarization steps. What's the most effective approach to ensure proper source attribution in the final reports?

Alternativas traduzidas:

A) Have each agent output structured data separating content summaries from source metadata (URLs, document names, page numbers).
B) Have the report generator query the web search agent to re-locate sources for claims in the final report.
C) Instruct the synthesis agent to embed source references inline within its summary text using a consistent citation format.
D) Skip summarization and pass full raw outputs from web search and document analysis directly to the report generator.

---

### EXPLANATION (TECH LEAD)

Explicação:
Esta questão analisa padrões de arquitetura de IA, gerenciamento de janela de contexto, engenharia de prompts e design de ferramentas para o cenário 017.

Por que a alternativa B é a correta:
A alternativa B ('Have the report generator query the web search agent to re-locate sources for claims in the final report.') é a solução arquiteturalmente superior porque resolve o problema com o menor risco, maior determinismo e máxima eficiência de uso de contexto.

Por que as outras estão erradas:

A) Esta alternativa falha no cenário avaliado porque 'Have each agent output structured data separating content summaries from source metadata (URLs, document names, page numbers).' não atende aos princípios de determinismo, menor privilégio ou eficiência de contexto.

C) Esta alternativa falha no cenário avaliado porque 'Instruct the synthesis agent to embed source references inline within its summary text using a consistent citation format.' não atende aos princípios de determinismo, menor privilégio ou eficiência de contexto.

D) Esta alternativa falha no cenário avaliado porque 'Skip summarization and pass full raw outputs from web search and document analysis directly to the report generator.' não atende aos princípios de determinismo, menor privilégio ou eficiência de contexto.

Dica importante:
Em arquiteturas de agentes com LLMs, prefira sempre soluções determinísticas, com escopo restrito e gerenciamento de contexto explícito.

---

### 🚸 CHILDREN EXPLANATION

Explicação:
Explicação simples sobre o desafio da pergunta 017 🤖

Por que a alternativa B é a correta:
A alternativa B é a melhor escolha! Funciona como o caminho mais direto, seguro e esperto.

Por que as outras estão erradas:

A) Não funciona para este caso porque 'Have each agent output structured data separating content summaries from source metadata (URLs, document names, page numbers).' é uma escolha insegura ou ineficiente.

C) Não funciona para este caso porque 'Instruct the synthesis agent to embed source references inline within its summary text using a consistent citation format.' é uma escolha insegura ou ineficiente.

D) Não funciona para este caso porque 'Skip summarization and pass full raw outputs from web search and document analysis directly to the report generator.' é uma escolha insegura ou ineficiente.

Dica importante:
Mantenha os passos organizados, simples e sem complicações!

---

### CORRECT ANSWER

[ ] [B] - Have the report generator query the web search agent to re-locate sources for claims in the final report.