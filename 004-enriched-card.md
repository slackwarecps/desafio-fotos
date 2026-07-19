Scenario: Multi-Model Orchestration Strategy You are architecting a system that needs to handle both high-latency, highly-accurate tasks (research synthesis) and low-latency, cost-sensitive tasks (content moderation). A single unified model can handle both but costs 3x more than using two specialized models. The research team strongly prefers unified experiences, but operations is concerned about budget impact. What should you recommend?

---

[ ] A - Use the unified model for both workloads; the better accuracy for moderation justifies the cost.
[ ] B - Split into two models, use the expensive one only for research, route moderation to a cheaper alternative.
[ ] C - Use the unified model but add a caching layer to reduce duplicate queries across workloads.
[ ] D - Implement a cost-aware router: direct to unified model when latency permits, fall back to cheaper model under load.

---

### TRANSLATED QUESTION

Cenário: Estratégia de Orquestração Multi-Modelo Você está arquitetando um sistema que precisa lidar com tarefas de alta latência e alta precisão (síntese de pesquisa) e tarefas de baixa latência e custo-sensível (moderação de conteúdo). Um único modelo unificado pode lidar com ambos, mas custa 3x mais do que usar dois modelos especializados. O time de pesquisa prefere fortemente experiências unificadas, mas operações está preocupada com impacto no orçamento. O que você deveria recomendar?

Alternativas traduzidas:

A) Use o modelo unificado para ambos os workloads; a precisão melhor para moderação justifica o custo.
B) Divida em dois modelos, use o caro apenas para pesquisa, rotearize moderação para uma alternativa mais barata.
C) Use o modelo unificado mas adicione uma camada de cache para reduzir queries duplicadas entre workloads.
D) Implemente um roteador ciente de custo: dirija para modelo unificado quando latência permitir, recue para modelo mais barato sob carga.

---

### EXPLANATION (TECH LEAD)

Esta pergunta testa um conceito crítico em engenharia de sistemas: **otimização multi-dimensional sob restrições**. Você raramente tem a liberdade de otimizar para um único objetivo (custo, latência, precisão, simplicidade). Sistemas reais exigem trade-offs.

A chave aqui é reconhecer que **diferentes workloads têm diferentes requisitos**, e tentar forçar uma solução única é uma anti-pattern clássica. Pesquisa pode tolerar latência (ela não precisa de resposta em tempo real), enquanto moderação de conteúdo é tipicamente time-critical.

Por que a alternativa D é a correta:

A alternativa D reconhece a realidade operacional: você não escolhe entre "caro" ou "barato", você escolhe **quando usar cada um**. Cria um roteador inteligente que:
- Usa o modelo caro (unificado) para pesquisa onde precisão é crítica
- Cai para modelo barato sob carga, quando sistema está estressado
- Não tenta ser "tudo para todos", mas ser o melhor possível dentro de restrições

Este é o padrão "staged fallback" — comumente usado em arquiteturas de produção.

Por que as outras estão erradas:

**A)** Assume que custo não importa — operações sempre importa em sistemas reais. "Melhor" não justifica 3x de gasto sem análise de impacto.

**B)** Funciona do ponto de vista técnico, mas ignora o feedback da pesquisa. Criar dois sistemas separados também aumenta complexidade operacional — agora você tem manutenção de dois modelos, roteamento adicional, monitoramento duplicado.

**C)** Caching é uma otimização tática válida, mas não resolve o problema fundamental de custo. É uma otimização **secundária** — você implementaria caching **em conjunto com** qualquer estratégia de roteamento.

Dica importante: **Trade-offs arquiteturais raramente têm respostas "perfeitas"**. A alternativa D não é "melhor" em todas as dimensões — é melhor porque reconhece múltiplas restrições e cria um sistema que degrada graciosamente sob pressão, não apenas otimiza para um caso feliz.

---

### SIMPLE EXPLANATION

O que está acontecendo:

Você tem dois tipos de trabalho: um que é importante mas pode esperar (pesquisa), outro que precisa ser feito rápido (moderação). Um sistema caro faz os dois bem, um barato faz os dois pior. A pergunta: qual você usa?

Por que a alternativa D é a melhor:

D diz: "Use o caro quando possível, mas tenha um plano B barato para quando as coisas ficarem apressadas." Isso é inteligente porque:
1. Pesquisadores ficam felizes (sistema robusto para eles)
2. Operações fica feliz (custos controlados)
3. Você não está preso — pode adaptar conforme aprende

Por que as outras não funcionam:

**A)** Caro o tempo todo — você gasta muito dinheiro sem necessidade.
**B)** Dois sistemas separados — mais complexo de manter, mais chances de diferenças aparecerem.
**C)** Caching ajuda, mas não resolve — você ainda está pagando 3x pela maioria das queries.

Lembrar: **Sistemas reais precisam de planos B. A boa arquitetura permite flexibilidade.**

---

### CORRECT ANSWER

Alternativa Correta: D
