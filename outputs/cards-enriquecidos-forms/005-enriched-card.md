Scenario: Your agent is handling a billing dispute. After calling `get_customer` and `lookup_order`, it identifies that the dispute involves a promotional pricing error requiring manager approval—beyond the agent's authorization level. How should the workflow handle this mid-process escalation?

---

[ ] A - Call `escalate_to_human` passing only the customer's original message.
[ ] B - Compile a structured handoff with customer details, order info, and the identified issue before calling `escalate_to_human`.
[ ] C - Attempt the refund with `process_refund` anyway, escalating only if the system rejects the transaction.
[ ] D - Persist the complete conversation and tool response history to a database, then call `escalate_to_human` with a reference ID.

---

### TRANSLATED QUESTION

Cenário: Seu agente está lidando com uma disputa de cobrança. Após chamar `get_customer` e `lookup_order`, identifica que a disputa envolve erro de preço promocional exigindo aprovação de gerente—além do nível de autorização do agente. Como o workflow deve lidar com essa escalação mid-process?

Alternativas traduzidas:

A) Chamar `escalate_to_human` passando apenas a mensagem original do cliente.
B) Compilar um handoff estruturado com detalhes do cliente, info da ordem, e issue identificada antes de chamar `escalate_to_human`.
C) Tentar o refund com `process_refund` mesmo assim, escalando apenas se o sistema rejeitar a transação.
D) Persistir conversa completa e histórico de respostas de tools em um banco de dados, depois chamar `escalate_to_human` com um reference ID.

---

### EXPLANATION (TECH LEAD)

Explicação:
A pergunta testa **handoff pattern em workflows agentic**. Especificamente: quando escalar para humano, que contexto você deve passar? A diferença entre "escalação fria" (dump raw conversation) vs. "escalação estruturada" (resumo + contexto) é crítica para eficiência operacional.

Por que a alternativa B é a correta:
Compilar um handoff estruturado é superior porque: (1) **Reduz trabalho humano**: em vez de humano ler 20 turnos de conversa, recebe um resumo — "cliente X, ordem Y, problema Z". (2) **Contexto apropriado**: human já tem os dados relevantes (customer profile, order summary, identified issue) sem ruído. (3) **Evita re-discovery**: human não precisa chamar `get_customer` e `lookup_order` de novo — você já fez isso. (4) **Rastreabilidade**: handoff estruturado permite logging/auditing claro. Isto é padrão em operações profissionais: handoff estruturado > handoff caótico.

Por que as outras estão erradas:

A) Passar apenas mensagem original é escalação fria — human recebe cliente reclamando, sem contexto que você descobriu (error type, order eligibility, approval requirements). Força human a fazer re-investigation que o agent já fez.

C) Tentar `process_refund` mesmo sabendo que requer aprovação viola autorização. Além disso, "escalate só se fail" é reativo — você já SABE que precisa de aprovação (promotional pricing error), por que arriscar uma falha? Escalar depois que falhou custa tempo de customer.

D) Persistir "complete conversation and tool response history" em banco de dados é overhead — você não precisa armazenar tudo, só o resumo. Passar reference ID em vez de contexto força human a fazer lookup de database, ineficiente. "Complete history" também introduz problemas de privacidade/PII.

Dica importante:
Padrão recorrente: **structured handoff**. Sempre que escalando (de agent para human, de subagent para coordinator, de service A para service B), a melhor prática é compilar um "handoff packet" — um resumo estruturado, não uma dump bruta. Isto aparece em varios contextos: microservices (service mesh), customer support (case notes), incident response (runbooks).

---

### 🚸 CHILDREN EXPLANATION

Explicação:
Imagina que você está assistindo um colega em uma tarefa, mas descobriu algo que só o gerente pode aprovar. Como você avisa o gerente?

Por que a alternativa B é a correta:
Você não quer apenas dizer "ei gerente, leia toda essa conversa que tive com o cliente". Isso é preguiçoso! Em vez disso, você faz uma **anotação clara**: "Cliente X quer refund de $500 da ordem Y. Problema: preço promocional foi aplicado errado. Requer: aprovação de gerente. Cliente já confirmou estar na política de 30 dias." Assim o gerente tem EXATAMENTE o que precisa saber, sem ler 20 mensagens.

Por que as outras estão erradas:

A) 🅰️ Só passar a mensagem original do cliente é como chamar o gerente e dizer "tem um cliente irritado aqui". O gerente não sabe QUAL o problema, quanto é, nem por que você não resolveu. Gerente precisa fazer todo o trabalho de novo!

C) 🅲️ Tentar fazer o refund mesmo sabendo que precisa de aprovação é desobediência. É como um assistente tentar assinar um cheque de $500 quando ele só pode até $100 — quando isso falha, você desperdiça tempo e cliente fica mais irritado.

D) 🅳️ Guardar TUDO em um banco de dados e passar só um ID é falta de preparação. Quando você chama o gerente, deveria ter a informação pronta, não fazer ele procurar em um banco de dados. Handoff deve ser **auto-contido e claro**.

Dica importante:
Quando você passa uma tarefa para outro (seja gerente, colega, ou outro time), sempre resume: **quem, o quê, problema, próximo passo**. Isso poupa tempo de todo mundo!

---

### CORRECT ANSWER

[ ] B - Compile a structured handoff with customer details, order info, and the identified issue before calling `escalate_to_human`.
