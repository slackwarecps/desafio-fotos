
## TITULO DO DECK DATA E HORA                                           pag1


### Question 1/3                                        pag2

Scenario: Structured Data Extraction You are building a structured data extraction system using Claude. The system extracts information from unstructured documents, validates output using JSON schemas, and maintains high accuracy. It must handle edge cases gracefully and integrate with downstream systems. Your product has two document queues: customer onboarding forms that must populate an eligibility screen while an operations specialist is waiting, and 40,000 archived contracts used for a dashboard due next week. Finance asks whether the lower-cost processing path should replace the current real-time calls for both queues. What should you recommend?

---

[ ] A - Route onboarding forms to batches first, then fall back to synchronous calls whenever pending jobs exceed a threshold.
[ ] B - Move both queues to the Message Batches API, polling frequently so urgent onboarding jobs usually finish quickly.
[ ] C - Keep both queues on synchronous calls, since batch responses cannot be reliably matched back to submitted documents.
[ ] D - Keep synchronous calls for onboarding forms, and use the Message Batches API for historical contracts with latency-tolerant processing.


### Question 1 Answer                                    pag3
**TRANSLATED QUESTION**
Você está construindo um sistema de extração de dados estruturados usando Claude. O sistema extrai informações de documentos não estruturados, valida a saída usando esquemas JSON e mantém alta precisão. Deve lidar com casos extremos de forma graciosa e integrar-se com sistemas downstream. Seu produto tem duas filas de documentos: formulários de onboarding de clientes que devem preencher uma tela de elegibilidade enquanto um especialista operacional aguarda, e 40.000 contratos arquivados usados para um dashboard devido na próxima semana. Finanças pergunta se o caminho de processamento de menor custo deve substituir as chamadas em tempo real para ambas as filas. O que você recomenda?

Alternativas traduzidas:

A) Rotear formulários de onboarding para batches primeiro, depois fazer fallback para chamadas síncronas sempre que trabalhos pendentes excedem um limite.
B) Mover ambas as filas para a Message Batches API, fazendo polling frequentemente para que trabalhos urgentes de onboarding geralmente terminem rapidamente.
C) Manter ambas as filas em chamadas síncronas, pois respostas em batch não podem ser confiávelmente combinadas de volta aos documentos submetidos.
D) Manter chamadas síncronas para formulários de onboarding, e usar a Message Batches API para contratos históricos com processamento tolerante a latência.

**Correct Answer**
[ ] D - Keep synchronous calls for onboarding forms, and use the Message Batches API for historical contracts with latency-tolerant processing.




