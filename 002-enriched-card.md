Scenario: Structured Data Extraction You are building a structured data extraction system using Claude. The system extracts information from unstructured documents, validates output using JSON schemas, and maintains high accuracy. It must handle edge cases gracefully and integrate with downstream systems. Your extraction pipeline includes a QA pass that flags possible mistakes in supplier contract records before they enter the downstream procurement system. Over the last month, procurement analysts accepted many findings about missing renewal clauses but overturned most findings involving informal pricing language. Current logs store only document ID, field name, confidence, and finding text, making it difficult to prioritize prompt and validator improvements. What change should you make first?
---
[ ] A - Increase the QA confidence threshold globally, suppressing all lower-confidence findings before analysts review extracted contract records.
[ ] B - Add a structured detected_pattern field to each QA finding, then analyze acceptance rates by pattern and document type.
[ ] C - Add a system prompt instruction telling Claude to report only findings that procurement analysts would likely accept.
[ ] D - Store only analyst accept or reject decisions per document, then randomly sample overturned findings for manual discussion.
---
### TRANSLATED QUESTION
Você está construindo um sistema de extração de dados estruturados usando Claude. O sistema extrai informações de documentos não estruturados, valida a saída usando esquemas JSON e mantém alta precisão. Deve lidar com casos extremos de forma graciosa e integrar-se com sistemas downstream. Seu pipeline de extração inclui uma passagem de QA que sinaliza possíveis erros em registros de contratos de fornecedores antes de entrarem no sistema de procurement downstream. No último mês, analistas de procurement aceitaram muitos findings sobre cláusulas de renovação ausentes mas rejeitaram a maioria dos findings envolvendo linguagem de preço informal. Os logs atuais armazenam apenas document ID, field name, confidence e finding text, tornando difícil priorizar melhorias de prompt e validator. Qual mudança você deveria fazer primeiro?

Alternativas traduzidas:

A) Aumentar o limiar de confiança de QA globalmente, suprimindo todos os findings de menor confiança antes que os analistas revisem registros de contrato extraídos.
B) Adicionar um campo estruturado detected_pattern a cada QA finding, depois analisar taxas de aceitação por padrão e tipo de documento.
C) Adicionar uma instrução de system prompt dizendo a Claude para reportar apenas findings que analistas de procurement provavelmente aceitariam.
D) Armazenar apenas decisões de aceitar/rejeitar dos analistas por documento, depois amostrar aleatoriamente findings rejeitados para discussão manual.

---
### EXPLANATION (TECH LEAD)

Esta pergunta testa um conceito fundamental em ML systems e data pipelines: **você não pode melhorar o que não consegue medir**. O cenário apresenta um problema bem específico — há um padrão consistente no feedback dos analistas (aceitam findings sobre renovação, rejeitam sobre preço informal) — mas o sistema não tem informações estruturadas para **entender por que** esse padrão existe.

A raiz do problema é a falta de visibilidade analítica. Os logs atuais armazenam dados brutos (confidence score, texto do finding), mas não capturam **que tipo de finding** é cada um. Sem categorização, é impossível detectar padrões, medir taxa de aceite por padrão, ou direcionar melhorias específicas.

Por que a alternativa B é a correta:

Adiciona um campo `detected_pattern` (ex: "missing_clause", "informal_pricing") a cada finding, permitindo análise real. Com isso, você descobre que "informal_pricing" tem baixa taxa de aceite e pode otimizar especificamente esse padrão — seja ajustando o prompt ou o validator. É a abordagem data-driven: estrutura os dados primeiro, depois toma decisões.

Por que as outras estão erradas:

**A)** Aumentar threshold globalmente é cego e indiscriminado — você suprime findings válidos junto com falsos positivos. Pior: se "informal_pricing" tem baixa confiança mas "missing_clause" tem alta, aumentar o threshold global pode matar findings úteis só porque um padrão é problemático.

**C)** Confiar em instrução de prompt para filtrar é frágil — sem feedback estruturado, você não consegue validar se o filtro está funcionando, e o modelo pode subjetivamente decidir o que "analysts would likely accept".

**D)** Armazenar decisões é útil para auditoria, mas isoladamente não ajuda a entender padrões. Amostragem aleatória de findings rejeitados é ineficiente e não escala.

Dica importante: **Sempre estruture dados de feedback do sistema antes de tentar otimizar.** A falta de dados categorizados é um anti-pattern comum — leads gastam tempo tentando melhorar cegamente em vez de primeiro entender onde estão os problemas reais. "Instrumentação primeiro, otimização depois."

---
### SIMPLE EXPLANATION

O que está acontecendo:

Você tem um sistema que gera avisos sobre documentos. Alguns avisos as pessoas aceitam (cláusula de renovação ausente), outros rejeitam (preço informal). Mas você não consegue entender por quê — seus logs só guardam o texto do aviso, não dizem que tipo de aviso é cada um.

Por que a alternativa B é a melhor:

B diz: "Adicione um campo que diga qual tipo de aviso é cada um, depois analise quais tipos as pessoas aceitam." Assim você descobre: "Ah, tipo 'preço informal' tem baixa aceitação — preciso melhorar isso." É como um médico que primeiro diagnostica antes de tratar.

Por que as outras não funcionam:

**A)** Aumentar o filtro geral — você joga fora avisos bons junto com os ruins.

**C)** Pedir para o sistema adivinhar o que as pessoas vão aceitar — você nunca sabe se ele está acertando ou errando.

**D)** Só guardar se aceitaram ou rejeitaram — você ainda não sabe por quê rejeitaram.

Lembrar: **Antes de consertar um problema, primeiro entenda qual é o problema.** Categorize os dados para enxergar padrões.

---
### CORRECT ANSWER

Alternativa Correta: B
