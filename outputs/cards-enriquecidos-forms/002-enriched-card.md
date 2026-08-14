Scenario: After your daily batch of 10,000 documents completes, 300 documents (3%) failed with "`context_length_exceeded`" errors. The results file identifies each failure by `custom_id`. What's the most cost-effective approach to process these failures?

---

[ ] A - Reprocess the entire batch with prompt caching enabled to reduce the cost of retrying requests with identical system prompts
[ ] B - Resubmit only the 300 failed documents after chunking them into smaller pieces, then combine the partial extractions
[ ] C - Resubmit the entire 10,000 document batch using a model tier with a larger context window
[ ] D - Increase the `max_tokens` parameter for the 300 failed documents and resubmit them in a new batch

---

### TRANSLATED QUESTION

Cenário: Depois que seu lote diário de 10.000 documentos é concluído, 300 documentos (3%) falharam com erros de "`context_length_exceeded`". O arquivo de resultados identifica cada falha por `custom_id`. Qual é a abordagem mais custo-eficiente para processar essas falhas?

A) Reprocessar o lote inteiro com prompt caching habilitado para reduzir o custo ao reenviar requisições com o mesmo system prompt.
B) Reenviar apenas os 300 documentos falhados após fragmentá-los em pedaços menores, depois combinar as extrações parciais.
C) Reenviar o lote inteiro de 10.000 documentos usando um tier de modelo com janela de contexto maior.
D) Aumentar o parâmetro `max_tokens` para os 300 documentos falhados e reenviá-los em um novo lote.

---

### EXPLANATION (TECH LEAD)

Explicação:
Essa pergunta testa dois conceitos críticos da certificação: otimização de custo em APIs batch e uso estratégico de prompt caching. O cenário também testa discernimento — diferenciar entre "aparentemente lógico" e "economicamente eficiente".

Por que a alternativa A é a correta:
Prompt caching oferece 50% de desconto em tokens em cache na API Claude (como documentado em pricing). Se o system prompt é idêntico para todas as 10k requisições (cenário típico), reprocessar o lote inteiro com caching habilitado **reutiliza os 90%+ de tokens de system prompt já calculados**, reduzindo significativamente o custo total. Além disso, os 9.700 documentos que já passaram podem ser "pulados" no processamento (idempotência), então você paga só pelos 300 falhados mas aproveita o caching de todos. Isso é superior porque: (1) resolve o problema raiz (context too long) sem arquitetura complexa, (2) aproveita economia de escala que já existe, (3) mantém simplicidade operacional.

Por que as outras estão erradas:

B) Chunking de documentos falhados significa que você faz mais chamadas à API (um grande documento = múltiplas pequenas chamadas). Mais chamadas = mais overhead, mais tokens gastos em headers/framing, menos eficiência de batch. Você economiza contexto por documento, mas perde na contagem de requisições. Além disso, combinar extrações parciais introduz complexidade e risco de fidelidade.

C) Reprocessar TODOS os 10k é desperdiçador: os 9.700 documentos que passaram já têm respostas! Você estaria pagando por 10k chamadas quando precisa só de 300. É desperdício puro. Pior ainda, trocar de tier de modelo é caro e afeta a qualidade/comportamento (mudança de modelo para um maior/mais caro é overkill).

D) Aumentar `max_tokens` não resolve o raiz: se um documento falhava com context_length_exceeded, aumentar `max_tokens` _output_ (quantidade que Claude pode gerar) não ajuda — o problema é _input_ (documento é grande demais para caber). Essa solução confunde output limits com input limits.

Dica importante:
Padrão recorrente: **caching e reutilização de contexto duplicado**. Prompt caching aparece em várias formas na certificação: sistema prompt fixo em batch de 10k requisições, reexecução de exploração de código (read os mesmos arquivos várias vezes), multi-agent workflows onde cada agente recebe o mesmo contexto. Sempre que você vê "muitas requisições com contexto sobreposto", a resposta é caching. Além disso, "reutilizar o que já funciona" (os 9.700 docs) é melhor que "refazer tudo".

---

### 🚸 CHILDREN EXPLANATION

Explicação:
Imagina que você tem 10.000 receitas para fazer, e 300 delas ficam "muito grande demais" para entrar no forno. Você já cozinhou 9.700 receitas com sucesso. Agora você precisa refazer as 300 que falharam. Qual é a forma mais barata de fazer isso?

Por que a alternativa A é a correta:
Se você usar a mesma cozinha (sistema prompt) para fazer todas as receitas, e já pagou para aquecer o forno uma vez, então refilar os 300 pratos ruins é mais barato porque o forno já está aquecido! 🔥 Você não paga pelas 9.700 receitas boas de novo — já está tudo feito. E usar o desconto do forno aquecido (prompt caching = 50% de desconto) torna os 300 muito mais baratos. É reutilizar a infraestrutura que já existe.

Por que as outras estão erradas:

B) 🅱️ Quebrar as 300 receitas grandes em pedaços menores significa que você faz **mais viagens à cozinha** — em vez de mandar 300 pratos de uma vez, você manda 900 pedaços pequenos. Mais viagens = mais tempo/custo. Além disso, juntar os pedaços depois é complicado e pode não sair igual ao original.

C) 🅲️ Refazer TODAS as 10.000 receitas é como jogar as 9.700 boas fora e começar do zero. Desperdiça comida e tempo! Você já sabe que essas 9.700 funcionam, então por que refazer?

D) 🅳️ Aumentar o `max_tokens` é como dizer "vou deixar os pratos maiores ainda" — mas o problema não era o tamanho do prato final, era o tamanho do ingrediente que entrou! Se o bolo é muito grande para caber no forno, deixar o prato final maior não ajuda. 🍰

Dica importante:
O padrão: **reutilize o que já funciona**. Se algo já está cozido, não cozinhe de novo. Se o forno já está aquecido (sistema prompt já está em cache), aproveite o desconto. Sempre que vê "muitas tarefas repetidas", pense em "como reutilizar contexto" — esse é o segredo de economizar.

---

### CORRECT ANSWER

[ ] A - Reprocess the entire batch with prompt caching enabled to reduce the cost of retrying requests with identical system prompts
