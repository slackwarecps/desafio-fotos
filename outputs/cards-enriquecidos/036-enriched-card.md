Scenario: After deployment, you find that 12% of extractions contain semantic errors that pass JSON schema validation (e.g., a duration like "30 minutes" incorrectly placed in an ingredient quantity field). Human reviewers have capacity to check only 20% of extractions. Which approach most effectively allocates reviewer attention?

---

[ ] A - Have the model output field-level confidence scores, then calibrate review thresholds using a labeled validation set.
[ ] B - Randomly sample 20% of extractions for review, using corrections to track accuracy and identify error patterns.
[ ] C - Prioritize review of all extractions where required fields are empty or explicitly marked as not found.
[ ] D - Review all extractions from documents with formatting anomalies such as unusual layouts or mixed content types.

---

### TRANSLATED QUESTION

Tradução do Cenário:
After deployment, you find that 12% of extractions contain semantic errors that pass JSON schema validation (e.g., a duration like "30 minutes" incorrectly placed in an ingredient quantity field). Human reviewers have capacity to check only 20% of extractions. Which approach most effectively allocates reviewer attention?

Alternativas traduzidas:

A) Have the model output field-level confidence scores, then calibrate review thresholds using a labeled validation set.
B) Randomly sample 20% of extractions for review, using corrections to track accuracy and identify error patterns.
C) Prioritize review of all extractions where required fields are empty or explicitly marked as not found.
D) Review all extractions from documents with formatting anomalies such as unusual layouts or mixed content types.

---

### EXPLANATION (TECH LEAD)

Explicação:
Esta questão analisa padrões de arquitetura de IA, gerenciamento de janela de contexto, engenharia de prompts e design de ferramentas para o cenário 036.

Por que a alternativa B é a correta:
A alternativa B ('Randomly sample 20% of extractions for review, using corrections to track accuracy and identify error patterns.') é a solução arquiteturalmente superior porque resolve o problema com o menor risco, maior determinismo e máxima eficiência de uso de contexto.

Por que as outras estão erradas:

A) Esta alternativa falha no cenário avaliado porque 'Have the model output field-level confidence scores, then calibrate review thresholds using a labeled validation set.' não atende aos princípios de determinismo, menor privilégio ou eficiência de contexto.

C) Esta alternativa falha no cenário avaliado porque 'Prioritize review of all extractions where required fields are empty or explicitly marked as not found.' não atende aos princípios de determinismo, menor privilégio ou eficiência de contexto.

D) Esta alternativa falha no cenário avaliado porque 'Review all extractions from documents with formatting anomalies such as unusual layouts or mixed content types.' não atende aos princípios de determinismo, menor privilégio ou eficiência de contexto.

Dica importante:
Em arquiteturas de agentes com LLMs, prefira sempre soluções determinísticas, com escopo restrito e gerenciamento de contexto explícito.

---

### 🚸 CHILDREN EXPLANATION

Explicação:
Explicação simples sobre o desafio da pergunta 036 🤖

Por que a alternativa B é a correta:
A alternativa B é a melhor escolha! Funciona como o caminho mais direto, seguro e esperto.

Por que as outras estão erradas:

A) Não funciona para este caso porque 'Have the model output field-level confidence scores, then calibrate review thresholds using a labeled validation set.' é uma escolha insegura ou ineficiente.

C) Não funciona para este caso porque 'Prioritize review of all extractions where required fields are empty or explicitly marked as not found.' é uma escolha insegura ou ineficiente.

D) Não funciona para este caso porque 'Review all extractions from documents with formatting anomalies such as unusual layouts or mixed content types.' é uma escolha insegura ou ineficiente.

Dica importante:
Mantenha os passos organizados, simples e sem complicações!

---

### CORRECT ANSWER

[ ] [B] - Randomly sample 20% of extractions for review, using corrections to track accuracy and identify error patterns.