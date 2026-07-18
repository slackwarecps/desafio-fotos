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
C) Manter ambas as filas em chamadas síncronas, pois respostas em batch não podem ser confiávelmente combinadas de volta aos documentos submetidos.
D) Manter chamadas síncronas para formulários de onboarding, e usar a Message Batches API para contratos históricos com processamento tolerante a latência.

---
### EXPLANATION (TECH LEAD)
Explicação Técnica:

Esta pergunta testa um conceito crítico em arquitetura de sistemas: **segmentação de requisitos por SLA (Service Level Agreement)**. O padrão fundamental é reconhecer que nem todos os dados têm os mesmos requisitos de latência ou throughput — misturar padrões de processamento leva a ineficiência de custo e complexidade operacional desnecessária.

O cenário apresenta dois contextos com requisitos opostos: (1) **Onboarding** é **síncrono-crítico** (humano esperando interativamente, SLA de segundos), (2) **Histórico** é **batch-tolerante** (relatório que será visto amanhã, SLA de horas).

Por que a alternativa D é a correta:

A alternativa D aplica **"right tool for the job"** com precisão cirúrgica:
- **Sincronismo para onboarding**: Porque latência impacta UX interativa. Operador aguardando pela tela de elegibilidade não pode ficar em retry loop.
- **Batch para histórico**: Porque 40k documentos não precisam respostas imediatas. Batch tem throughput superior e custo inferior por transação.

Resultado: custo otimizado sem comprometer requisitos críticos ao negócio. Você paga premium apenas onde é comercialmente justificado.

Por que as outras estão erradas:

**A) Batch-first com fallback**: Conceitualmente confunde prioridades. Onboarding é síncrono-crítico — não é "tente batch primeiro". O fallback apenas adiciona latência antes do sincronismo. Além disso, ainda desperdicia custo em sincronismo para histórico.

**B) Batch para ambos com polling rápido**: Tenta usar heurística (polling frequente) para simular sincronismo que batch não oferece inerentemente. Você não elimina latência estrutural de batch apenas fazendo polling rápido. E desperdiça potencial de economia de custo que batch ofereceria para histórico.

**C) Syncronismo para ambos**: É o status quo que Finance questiona. Deixar 40k documentos históricos em processamento síncrono é economicamente injustificável — você paga premium de latência para um caso de uso onde latência não gera valor.

Dica importante:

Em arquitetura de sistemas, sempre segmente por SLA/requisito de latência. Esse padrão aparece constantemente: requisitos síncronos (com humano esperando) vs. batch (processamento background). Não misture. Use o padrão mais simples que satisfaz cada requisito. Esse é um trade-off fundamental entre costo (batch é mais barato) e latência (sincronismo é mais rápido).

---
### SIMPLE EXPLANATION
Explicação para Aprendizes:

O que está acontecendo:

Imagine dois tipos de trabalho na sua casa: (1) lavar a louça que você vai usar no jantar de hoje (urgente!), (2) limpar a garagem que você vai pintar no fim de semana (pode esperar).

Você não faria os dois da mesma forma, né? Você lava a louça rápido (mão quente, água correndo), mas a garagem você pode fazer devagar, economizando tempo e energia.

A pergunta aqui é a mesma: você tem dois tipos de processamento — um que precisa ser RÁPIDO (onboarding que alguém está esperando) e outro que pode ser BARATO (40k contratos que ninguém precisa hoje).

Por que a alternativa D é a melhor:

D diz: "Faça o onboarding rápido (síncrono), faça o histórico barato (batch)."

Isso funciona porque:
- Onboarding é rápido quando você precisa
- Histórico é barato quando custa menos
- Você não desperdiça dinheiro fazendo histórico rápido
- Você não deixa ninguém esperando

Por que as outras não funcionam:

**A) Tenta batch primeiro**: A pessoa esperando o onboarding fica esperando mais que devia.

**B) Batch para ambos com polling rápido**: Você não consegue fazer batch ser tão rápido quanto síncrono. E você não economiza dinheiro tentando fazer isso.

**C) Syncronismo para ambos**: Você economiza tempo no histórico (que já ia rápido demais), mas GASTA muito dinheiro desnecessariamente.

Lembrar:

**Use o padrão certo para cada trabalho:**
- **Trabalho urgente** (alguém esperando) → Rápido (síncrono)
- **Trabalho que pode esperar** → Barato (batch)
- Não tente fazer ambos iguais — é desperdiçar recursos

---
### CORRECT ANSWER
Alternativa Correta: D
