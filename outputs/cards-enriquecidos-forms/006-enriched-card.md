Scenario: A customer raises three separate issues during one session: a refund inquiry (turns 1-15), a subscription question (turns 16-30), and a payment method update (turns 31-45). At turn 48, the customer asks "What happened with my refund?" The conversation is approaching context limits. What strategy best maintains the agent's ability to address all issues throughout the session?

---

[ ] A - Extract and persist structured issue data (order IDs, amounts, statuses) into a separate context layer.
[ ] B - Rely on MCP tools to re-fetch relevant information on demand when the customer references earlier issues.
[ ] C - Summarize earlier turns into a narrative description, preserving full message history only for the active issue.
[ ] D - Implement sliding window context that retains the most recent 30 turns.

---

### TRANSLATED QUESTION

Cenário: Um cliente levanta três issues separadas durante uma sessão: refund inquiry (turns 1-15), subscription question (turns 16-30), e payment method update (turns 31-45). No turn 48, cliente pergunta "E aí, o que aconteceu com meu refund?" A conversa está se aproximando dos limites de contexto. Qual estratégia melhor mantém a habilidade do agente de lidar com todas as issues durante a sessão?

Alternativas traduzidas:

A) Extrair e persistir dados estruturados de issues (order IDs, valores, status) em uma camada de contexto separada.
B) Confiar em MCP tools para re-buscar informação relevante sob demanda quando cliente referencia issues anteriores.
C) Resumir turns anteriores em descrição narrativa, preservando histórico completo de mensagens apenas para a issue ativa.
D) Implementar sliding window context que retém os últimos 30 turns.

---

### EXPLANATION (TECH LEAD)

Explicação:
A pergunta testa **context management em multi-issue conversations**. Cenário típico em customer support: contexto é limitado, mas você tem múltiplas issues não-relacionadas que o cliente menciona ao longo do tempo. Como você mantém rastreabilidade sem gastar tokens em histórico completo?

Por que a alternativa A é a correta:
Extrair e persistir structured issue data em camada separada é superior porque: (1) **Desacoplamento de conversação**: dados de issue (ID, status, contexto técnico) vivem independentemente da conversa — não competem por tokens com turn 48. (2) **Re-referência eficiente**: quando cliente pergunta "e meu refund?" no turn 48, você faz lookup estruturado (O(1) lookup: order ID → status) em vez de re-scanning histórico. (3) **Múltiplas issues simultaneamente**: você tem slots para refund, subscription, payment method — cada um independente. (4) **Escala**: padrão "structured data layer" permite lidar com 5, 10, 20 issues sem degradação de contexto. Isto é arquitetura padrão em sistemas reais: conversação é transitória, dados estruturados são fonte verdade.

Por que as outras estão erradas:

B) Confiar em MCP tools para re-fetch é reativo — você já chamou `get_customer`, `lookup_order` nos turns 1-15. Re-fetching no turn 48 é redescoberta custosa. Além disso, MCP tools têm latência — block no turn 48 esperando resposta.

C) Resumir turns em narrativa é lossy compression — narrativa "the customer's refund is being processed" é mais vago que dado estruturado "refund_status: pending, expected_date: 2026-08-16". Quando cliente pergunta "quando chega?" no turn 48, você não tem a data exata — só tem narrativa genérica.

D) Sliding window retaining últimos 30 turns perde issue #1 (refund, turns 1-15). Turn 48 pergunta sobre refund, mas turns 1-15 foram dropados. Você perdeu contexto crítico. Sliding window é pior aqui.

Dica importante:
Padrão recorrente: **structured state management outside conversation context**. Sempre que tem múltiplos issues, long conversations, ou re-referências, a resposta é "extrair estado estruturado para camada separada, não compressão lossy". Isto aparece em: CRM systems (customer data persists), incident management (issue registry), conversation bots (session state).

---

### 🚸 CHILDREN EXPLANATION

Explicação:
Imagina que você está ajudando um cliente que tem 3 problemas: quer refund de um produto, quer mudar a subscription, e quer atualizar forma de pagamento. Tudo numa longa conversa. Em algum ponto, você cansa de guardar TUDO na memória, quer esquecer o início pra lembrar só do agora. Como você não perde a informação?

Por que a alternativa A é a correta:
Em vez de tentar guardar toda a conversa na sua cabeça, você anota os dados importantes num **papel separado**: "Cliente X, refund ordem 123 → Status: em processamento. Subscription: plano pro. Payment: Visa terminado em 4321." Assim quando cliente pergunta "e meu refund?" mais tarde, você não precisa lembrar de 50 mensagens — só consulta o papel! Papel (dados estruturados) é pequeno e fácil de procurar.

Por que as outras estão erradas:

A) 🅰️ Pedir ao cliente pra chamar tools de novo é impraticável — cliente não pode chamar seu sistema, só você. E re-buscar é lento.

C) 🅲️ Resumir tudo em narrativa é como tentar condensar 50 mensagens num texto "o cliente tinha vários problemas". Muito vago! Quando pergunta "e meu refund?", você não tem número, status, nada concreto.

D) 🅳️ Lembrar só dos últimos 30 mensagens é como esquecer tudo que aconteceu nos primeiros 15 turns — e se a pergunta sobre refund aparece no turn 48? Você esqueceu tudo sobre refund!

Dica importante:
Quando você tem conversa longa com múltiplos assuntos, **anote os dados importantes num lugar à parte** — tipo planilha com status de cada coisa. Não tente guardar tudo na conversa!

---

### CORRECT ANSWER

[ ] A - Extract and persist structured issue data (order IDs, amounts, statuses) into a separate context layer.
