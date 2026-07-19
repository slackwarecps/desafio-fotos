Scenario: Structured Data Extraction You are building a structured data extraction system using Claude. The system extracts information from unstructured documents, validates output using JSON schemas, and maintains high accuracy. It must handle edge cases gracefully and integrate with downstream systems. Your product has two document queues: customer onboarding forms that must populate an eligibility screen while an operations specialist is waiting, and 40,000 archived contracts used for a dashboard due next week. Finance asks whether the lower-cost processing path should replace the current real-time calls for both queues. What should you recommend?
---
[ ] A - Route onboarding forms to batches first, then fall back to synchronous calls whenever pending jobs exceed a threshold.
[ ] B - Move both queues to the Message Batches API, polling frequently so urgent onboarding jobs usually finish quickly.
[ ] C - Keep both queues on synchronous calls, since batch responses cannot be reliably matched back to submitted documents.
[ ] D - Keep synchronous calls for onboarding forms, and use the Message Batches API for historical contracts with latency-tolerant processing.
---
### TRANSLATED QUESTION
Você está construindo um sistema de extração de dados estruturados usando Claude. O sistema extrai informações de documentos não estruturados, valida a saída usando esquemas JSON e mantém alta precisão. Deve lidar com casos extremos de forma graciosa e integrar-se com sistemas downstream. Seu produto tem duas filas de documentos: formulários de onboarding de clientes que devem preencher uma tela de elegibilidade enquanto um especialista operacional aguarda, e 40.000 contratos arquivados usados para um dashboard devido na próxima semana. Finanças pergunta se o caminho de processamento de menor custo deve substituir as chamadas em tempo real para ambas as filas. O que você recomenda?

Alternativas traduzidas:

A) Rotear formulários de onboarding para batches primeiro, depois fazer fallback para chamadas síncronas sempre que trabalhos pendentes excedem um limite.
B) Mover ambas as filas para a Message Batches API, fazendo polling frequentemente para que trabalhos urgentes de onboarding geralmente terminem rapidamente.
C) Manter ambas as filas em chamadas síncronas, pois respostas em batch não podem ser confiavelmente combinadas de volta aos documentos submetidos.
D) Manter chamadas síncronas para formulários de onboarding, e usar a Message Batches API para contratos históricos com processamento tolerante a latência.

---
### EXPLANATION (TECH LEAD)

Esta pergunta testa um conceito fundamental em arquitetura de sistemas: a necessidade de **casamento entre o padrão de processamento e os requisitos de latência**. Nem todos os dados têm os mesmos requisitos — é essencial diferenciar entre operações críticas ao tempo real (que pagam mais por sincronismo) e operações onde a latência é tolerável (que podem economizar custo).

A chave aqui é reconhecer que há **dois contextos diferentes** com requisitos completamente opostos: (1) onboarding de clientes requer respostas **imediatas** porque um humano está esperando interativamente, e (2) contratos históricos são um relatório batch que pode tolerar horas de latência.

Por que a alternativa D é a correta:

Aplica o princípio de **"right tool for the right job"** na sua forma mais pura. Mantém sincronismo para onboarding (a latência impacta a experiência do usuário em tempo real) e move contratos históricos para Batches API (40.000 documentos não precisam respostas imediatas — o dashboard "é para próxima semana"). Otimiza custo sem comprometer requisitos críticos.

Por que as outras estão erradas:

**A)** Rotear onboarding para batch primeiro é conceitualmente errado — um especialista operacional esperando fica bloqueado indefinidamente. O fallback para síncrono só ocorre após o threshold ser atingido, adicionando latência desnecessária mesmo em casos urgentes.

**B)** Mover ambas para Batches API com polling frequente tenta simular sincronismo — você não elimina a latência inerente de batch apenas com polling rápido. O batch foi desenhado para throughput, não para baixa latência.

**C)** Manter tudo em sincronismo é tecnicamente correto do ponto de vista de latência, mas financeiramente ineficiente — 40.000 documentos históricos não precisam de premium de latência, gerando custo desnecessário.

Dica importante: **Sistemas multi-fila são comuns em arquiteturas reais.** Sempre avalie: (1) requisito de latência de cada workload, (2) custo de cada abordagem, (3) se faz sentido unificar ou separar os caminhos de processamento. A resposta mais cara nem sempre é a melhor — a resposta certa depende do trade-off entre latência e custo para cada caso.

---
### SIMPLE EXPLANATION

O que está acontecendo:

Você tem dois trabalhos diferentes: um que precisa ser feito AGORA (enquanto alguém espera), outro que pode ser feito depois (um relatório que ninguém precisa hoje). A pergunta: qual é a forma inteligente de fazer esses dois?

Por que a alternativa D é a melhor:

D diz: "Faça o trabalho urgente de forma rápida, e o trabalho que pode esperar de forma barata." Isso é inteligente porque: (1) a pessoa esperando fica feliz, (2) os 40.000 documentos custam menos para processar, (3) você economiza dinheiro sem deixar ninguém esperando.

Por que as outras não funcionam:

**A)** Tenta batch primeiro para tudo — a pessoa esperando fica muito tempo esperando o batch terminar.

**B)** Usa batch para ambos com polling rápido — não adianta: batch é inerentemente mais lento que chamada síncrona.

**C)** Manter tudo rápido — você economiza tempo mas gasta MUITO mais dinheiro do que o necessário.

Lembrar: **Processamento síncrono é rápido e caro; batch é lento e barato. Use cada um onde faz sentido.**

---
### CORRECT ANSWER

Alternativa Correta: D
