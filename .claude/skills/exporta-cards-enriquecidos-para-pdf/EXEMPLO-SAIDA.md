# Exemplo de Saída PDF (Markdown Consolidado)

Este arquivo mostra como a skill formata o documento PDF consolidado.

---

## FLASHCARDS DECK - CLAUDE CERTIFIED ARCHITECT                    pag1

**Flashcards - Claude Certified Architect – Foundations Certification**

Data de Geração: 18 de Julho de 2026, 09:45 BRT
Total de Questões: 10
Versão: 1.0

{QUEBRA_DE_PAGINA_AQUI}

---

### Question 1/10                                        pag2

Scenario: Structured Data Extraction You are building a structured data extraction system using Claude. The system extracts information from unstructured documents, validates output using JSON schemas, and maintains high accuracy. It must handle edge cases gracefully and integrate with downstream systems. Your product has two document queues: customer onboarding forms that must populate an eligibility screen while an operations specialist is waiting, and 40,000 archived contracts used for a dashboard due next week. Finance asks whether the lower-cost processing path should replace the current real-time calls for both queues. What should you recommend?

---

[ ] A - Route onboarding forms to batches first, then fall back to synchronous calls whenever pending jobs exceed a threshold.
[ ] B - Move both queues to the Message Batches API, polling frequently so urgent onboarding jobs usually finish quickly.
[ ] C - Keep both queues on synchronous calls, since batch responses cannot be reliably matched back to submitted documents.
[ ] D - Keep synchronous calls for onboarding forms, and use the Message Batches API for historical contracts with latency-tolerant processing.

---
{QUEBRA_DE_PAGINA_AQUI}

### QUESTION 1 ANSWER                                    pag3

**Translated question**

Você está construindo um sistema de extração de dados estruturados usando Claude. O sistema extrai informações de documentos não estruturados, valida a saída usando esquemas JSON e mantém alta precisão. Deve lidar com casos extremos de forma graciosa e integrar-se com sistemas downstream. Seu produto tem duas filas de documentos: formulários de onboarding de clientes que devem preencher uma tela de elegibilidade enquanto um especialista operacional aguarda, e 40.000 contratos arquivados usados para um dashboard devido na próxima semana. Finanças pergunta se o caminho de processamento de menor custo deve substituir as chamadas em tempo real para ambas as filas. O que você recomenda?

Alternativas traduzidas:

A) Rotear formulários de onboarding para batches primeiro, depois fazer fallback para chamadas síncronas sempre que trabalhos pendentes excedem um limite.
B) Mover ambas as filas para a Message Batches API, fazendo polling frequentemente para que trabalhos urgentes de onboarding geralmente terminem rapidamente.
C) Manter ambas as filas em chamadas síncronas, pois respostas em batch não podem ser confiávelmente combinadas de volta aos documentos submetidos.
D) Manter chamadas síncronas para formulários de onboarding, e usar a Message Batches API para contratos históricos com processamento tolerante a latência.

---

**Tech Lead Explanation:**

Esta pergunta testa um conceito crítico em arquitetura de sistemas: a necessidade de **casamento entre o padrão de processamento e as características do requisito**. Nem todos os dados têm os mesmos requisitos de latência — é essencial diferenciar entre operações críticas ao tempo real (que pagam mais por sincronismo) e operações onde a latência é tolerável (que podem economizar custo).

A chave aqui é reconhecer que há **dois contextos diferentes** com requisitos completamente opostos: (1) onboarding de clientes requer respostas **imediatas** porque um humano está esperando interativamente, e (2) contratos históricos são um relatório batch que pode tolerar horas de latência.

Por que a alternativa D é a correta:

A alternativa D aplica o princípio de **"right tool for the right job"** na sua forma mais pura. Mantém sincronismo para onboarding (porque a latência impacta a experiência do usuário em tempo real) e move contratos históricos para Batches API (porque 40.000 documentos históricos não precisam respostas imediatas — o dashboard "é para próxima semana"). Isso otimiza custo sem comprometer requisitos críticos.

Por que as outras estão erradas:

A) Rotear onboarding para batch primeiro é conceitualmente errado. Um especialista operacional esperando fica bloqueado indefinidamente.

B) Mover ambas para Batches API com polling frequente tenta simular sincronismo — você não consegue eliminar latência inerente de batch apenas com polling rápido.

C) Manter tudo em sincronismo é desperdiçar dinheiro — 40.000 documentos históricos não precisam de premium de latência.

---

** 🧒 Children  Explanation:**

O que está acontecendo:

Você tem dois trabalhos diferentes: um que precisa ser feito AGORA (enquanto alguém espera), outro que pode ser feito depois (um relatório que ninguém precisa hoje). A pergunta: qual é a forma inteligente de fazer esses dois?

Por que a alternativa D é a melhor:

D diz: "Faça o trabalho urgente de forma rápida, e o trabalho que pode esperar de forma barata." Isso é inteligente porque: (1) a pessoa esperando fica feliz, (2) os 40.000 documentos são baratos, (3) você economiza dinheiro sem deixar ninguém esperando.

Por que as outras não funcionam:

A) Tenta batch primeiro — pessoa esperando fica muito tempo esperando.
B) Usa batch para ambos com polling rápido — você não consegue fazer batch ser tão rápido quanto síncrono.
C) Manter tudo rápido — você economiza tempo mas gasta MUITO dinheiro.

---

**✅ CORRECT ANSWER**
[ ] D - Keep synchronous calls for onboarding forms, and use the Message Batches API for historical contracts with latency-tolerant processing.

---
{QUEBRA_DE_PAGINA_AQUI}


### Question 2/10                                        pag4

Scenario: Structured Data Extraction You are building a structured data extraction system using Claude. The system extracts information from unstructured documents, validates output using JSON schemas, and maintains high accuracy. It must handle edge cases gracefully and integrate with downstream systems. Your extraction pipeline includes a QA pass that flags possible mistakes in supplier contract records before they enter the downstream procurement system. Over the last month, procurement analysts accepted many findings about missing renewal clauses but overturned most findings involving informal pricing language. Current logs store only document ID, field name, confidence, and finding text, making it difficult to prioritize prompt and validator improvements. What change should you make first?
---
[ ] A - Increase the QA confidence threshold globally, suppressing all lower-confidence findings before analysts review extracted contract records.
[ ] B - Add a structured detected_pattern field to each QA finding, then analyze acceptance rates by pattern and document type.
[ ] C - Add a system prompt instruction telling Claude to report only findings that procurement analysts would likely accept.
[ ] D - Store only analyst accept or reject decisions per document, then randomly sample overturned findings for manual discussion.

---
{QUEBRA_DE_PAGINA_AQUI}

### QUESTION 2 ANSWER                                    pag5

**Translated question**

Você está construindo um sistema de extração de dados estruturados usando Claude. O sistema extrai informações de documentos não estruturados, valida a saída usando esquemas JSON e mantém alta precisão. Deve lidar com casos extremos de forma graciosa e integrar-se com sistemas downstream. Seu pipeline de extração inclui uma passagem de QA que sinaliza possíveis erros em registros de contratos de fornecedores antes de entrarem no sistema de procurement downstream. No último mês, analistas de procurement aceitaram muitos findings sobre cláusulas de renovação ausentes mas rejeitaram a maioria dos findings envolvendo linguagem de preço informal. Os logs atuais armazenam apenas document ID, field name, confidence e finding text, tornando difícil priorizar melhorias de prompt e validator. Qual mudança você deveria fazer primeiro?

Alternativas traduzidas:

A) Aumentar o limiar de confiança de QA globalmente, suprimindo todos os findings de menor confiança antes que os analistas revisem registros de contrato extraídos.
B) Adicionar um campo estruturado detected_pattern a cada QA finding, depois analisar taxas de aceitação por padrão e tipo de documento.
C) Adicionar uma instrução de system prompt dizendo a Claude para reportar apenas findings que analistas de procurement provavelmente aceitariam.
D) Armazenar apenas decisões de aceitar/rejeitar dos analistas por documento, depois amostrar aleatoriamente findings rejeitados para discussão manual.

---

**Tech Lead Explanation:**

Esta pergunta testa um conceito fundamental em ML systems: **você não pode melhorar o que não consegue medir**. O cenário apresenta um problema bem específico — há um padrão consistente no feedback dos analistas (aceitam findings sobre renovação, rejeitam sobre preço informal) — mas o sistema não tem informações estruturadas para **entender por que** esse padrão existe.

A raiz do problema é a falta de visibilidade analítica. Os logs atuais armazenam dados brutos (confidence score, texto do finding), mas não capturam **que tipo de finding** é cada um. Sem categorização, é impossível detectar padrões, medir taxa de aceite por padrão, ou direcionar melhorias.

Por que a alternativa B é a correta:

A alternativa B usa estruturação de dados — adiciona um campo `detected_pattern` (ex: "missing_clause", "informal_pricing") a cada finding. Com isso, você consegue fazer análise real e descobrir que "informal_pricing" tem baixa taxa de aceite. Depois você otimiza especificamente para esse padrão.

Por que as outras estão erradas:

A) Aumentar threshold globalmente é cego — você suprime findings válidos junto com falsos positivos.
C) Confiar em prompt para filtrar é frágil — sem feedback estruturado, você não consegue validar.
D) Armazenar decisões é útil para auditoria, mas não resolve o problema de entender padrões.

---

**🧒 Children  Explanation:**

O que está acontecendo:

Você tem um sistema que gera avisos sobre documentos. Alguns avisos as pessoas aceitam (renovação ausente), outros rejeitam (preço informal). Mas você não consegue entender por quê — seus logs não dizem que tipo de aviso é cada um.

Por que a alternativa B é a melhor:

B diz: "Adicione um campo que diga qual tipo de aviso é cada um, depois analise quais tipos as pessoas aceitam." Assim você descobre: "Ah, tipo 'preço informal' tem baixa aceitação, preciso melhorar isso."

Por que as outras não funcionam:

A) Aumentar filtro global — você perde avisos válidos.
C) Instruir o sistema a prever o que as pessoas querem — você não consegue validar sem dados estruturados.
D) Só guardar decisões — você ainda não sabe por quê as pessoas rejeitam.

---

**✅ CORRECT ANSWER**
[ ] B - Add a structured detected_pattern field to each QA finding, then analyze acceptance rates by pattern and document type.

---
{QUEBRA_DE_PAGINA_AQUI}

[... E assim por diante para Questions 3-10 ...]

---

## Notas Sobre Formatação

- Cada página é numerada (pag1, pag2, etc.)
- Questões em páginas pares, respostas em páginas ímpares
- Counter "Question X/10" mostra progresso
- Seções claramente delineadas com `---`
- Explicações estruturadas em dois níveis (Tech Lead + children)
- Cada card é auto-contido e pode ser lido independentemente
