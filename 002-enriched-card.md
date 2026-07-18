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
Explicação Técnica:

Esta pergunta testa um padrão crítico em observabilidade de sistemas ML: **estruture dados para análise antes de tentar otimizar**. O cenário descreve um problema bem específico — há um padrão claro em feedback (aceitam renovação, rejeitam preço informal) — mas o sistema é cego porque os dados não estão estruturados para detectar e analisar esse padrão.

O conceito fundamental é **"You can't improve what you can't measure"**. Logs atuais têm sinais brutos (confidence score, texto), mas não categorização semântica. Sem categorização, é impossível: (1) detectar padrões de variação, (2) medir taxa de sucesso por tipo, (3) priorizar melhorias de forma baseada em dados.

Por que a alternativa B é a correta:

A alternativa B introduz **estrutura de dados** via campo `detected_pattern` (ex: "missing_clause", "informal_pricing", "date_mismatch"). Com isso, você consegue fazer análise real:
- Segmentar: "Qual taxa de aceitação para 'missing_clause' vs. 'informal_pricing'?"
- Descobrir: "Ah, 'informal_pricing' tem 15% aceitação enquanto 'missing_clause' tem 95%"
- Priorizar: "Vou otimizar a heurística para 'informal_pricing' porque é o problema real"

Isso transforma dados brutos em sinais acionáveis que guiam otimização sistemática.

Por que as outras estão erradas:

**A) Aumentar threshold globalmente**: É uma solução cega. Você suprime falsos positivos mas também falsos negativos válidos. Além disso, não resolve o padrão — se "informal_pricing" é intrinsecamente subjetivo, aumentar threshold global não ajuda; você precisa entender POR QUÊ e talvez aceitar baixa confiança apenas para esse padrão.

**C) Adicionar instrução de prompt**: Tenta usar prompt engineering para resolver um problema de dados/arquitetura. O modelo pode prever o que analistas querem, mas sem feedback estruturado e métricas, você não consegue validar. Além disso, diferentes padrões têm diferentes aceitabilidades — uma instrução global é inflexível.

**D) Guardar decisões e amostrar**: É útil para auditoria retrospectiva, mas não resolve o problema AGORA. Você continua cego em relação a padrões. Sampling aleatório de rejeitados não identifica sistematicamente por que determinados padrões falham.

Dica importante:

Em sistemas com feedback humano, **estruture dados para segmentação ANTES de otimizar**. Capture não apenas "resultado", mas "categoria de resultado" (padrão, tipo, contexto). Isso permite análise segmentada que revela os verdadeiros problemas em vez de sintomas genéricos.

---
### SIMPLE EXPLANATION
Explicação para Aprendizes:

O que está acontecendo:

Você tem um sistema que gera avisos sobre documentos. Alguns avisos as pessoas aceitam (renovação ausente), outros rejeitam (preço informal). Mas seus logs não dizem que tipo de aviso é cada um — só dizem "confidence score X, texto Y". Você não consegue entender por quê alguns são aceitos e outros não.

Por que a alternativa B é a melhor:

B diz: "Adicione um campo que categorize qual tipo de aviso é cada um, depois analise quais tipos as pessoas aceitam."

Assim você descobre:
- "Tipo 'missing_clause': 95% aceito"
- "Tipo 'informal_pricing': 15% aceito"

Com essa informação, você sabe exatamente o que melhorar.

Por que as outras não funcionam:

**A) Aumentar filtro global**: Você perde avisos que seriam úteis. Não resolve porque o problema não é "confiança", é "informal_pricing é confuso".

**C) Instruir o sistema**: Você tenta fazer o sistema "adivinhar" o que as pessoas querem. Mas sem dados estruturados, você não consegue validar se funciona.

**D) Guardar decisões e amostrar**: Você ainda não sabe o padrão. "Alguém rejeitou isso" não é suficiente — você precisa saber "tipo X é rejeitado porque...".

Lembrar:

**Para melhorar, precisa medir. Para medir, precisa categorizar:**

Em vez de "aviso rejeitado", tenha "tipo 'informal_pricing' rejeitado 85% do tempo". Isso é informação acionável.

---
### CORRECT ANSWER
Alternativa Correta: B
