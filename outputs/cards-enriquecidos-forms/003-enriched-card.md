Scenario: Your pipeline uses a tool called `extract_metadata` with a JSON schema for paper details. You've also defined `lookup_citations` and `verify_doi` tools for enrichment. During testing, you notice that when users include requests like "extract the metadata and tell me how cited it is," Claude sometimes calls `lookup_citations` first, which fails because it needs the DOI that `extract_metadata` would provide. What's the most effective way to ensure structured metadata extraction happens first?

---

[ ] A - Set `tool_choice` to "any" so Claude must use a tool, combined with system prompt instructions prioritizing `extract_metadata`.
[ ] B - Set `tool_choice` to "auto" and reorder the tool definitions so `extract_metadata` appears first in the tools array, since Claude prioritizes earlier-listed tools.
[ ] C - Set `tool_choice` to {"type": "tool", "name": "`extract_metadata`"} and process the enrichment requests in subsequent turns after receiving the extracted metadata.
[ ] D - Set `tool_choice` to {"type": "tool", "name": "`extract_metadata`"} for every API call in the pipeline, ensuring Claude always extracts metadata before any enrichment can occur.

---

### TRANSLATED QUESTION

Cenário: Seu pipeline usa uma ferramenta chamada `extract_metadata` com um schema JSON para detalhes de artigos. Você também definiu ferramentas `lookup_citations` e `verify_doi` para enriquecimento. Durante os testes, você nota que quando usuários incluem requisições como "extraia os metadados e me diga como é citado", Claude às vezes chama `lookup_citations` primeiro, o que falha porque precisa do DOI que `extract_metadata` retornaria. Qual é a forma mais eficaz de garantir que a extração estruturada de metadados aconteça primeiro?

A) Definir `tool_choice` para "any" para que Claude use uma ferramenta, combinado com instruções no system prompt priorizando `extract_metadata`.
B) Definir `tool_choice` para "auto" e reordenar as definições de ferramentas para que `extract_metadata` apareça primeiro no array de ferramentas, pois Claude prioriza ferramentas listadas antes.
C) Definir `tool_choice` para {"type": "tool", "name": "`extract_metadata`"} e processar requisições de enriquecimento em turnos subsequentes após receber os metadados extraídos.
D) Definir `tool_choice` para {"type": "tool", "name": "`extract_metadata`"} em toda chamada à API do pipeline, garantindo que Claude sempre extraia metadados antes de qualquer enriquecimento.

---

### EXPLANATION (TECH LEAD)

Explicação:
Essa pergunta testa entendimento de **tool_choice constraints** (um dos tópicos centrais do Claude Certified Architect) e como gerenciar dependências entre ferramentas e dados. O problema apresentado é clássico em agentic systems: você tem múltiplas ferramentas, mas uma depende da saída da outra. A pergunta examina qual é a forma mais robusta de garantir a ordem de execução.

Por que a alternativa C é a correta:
O padrão mais eficaz para garantir ordem de execução com dependência de dados é **separar em turnos (multi-turn)**. No Turn 1, você define `tool_choice` com tipo "tool" e nome específico: `{"type": "tool", "name": "extract_metadata"}`, forçando Claude a chamar **apenas** extract_metadata. Ele retorna DOI, título, etc. No Turn 2, você passa a resposta anterior na conversation history, permite todas as ferramentas (ou define `tool_choice` para `lookup_citations`), e agora Claude tem o DOI em mão. Isso é robusto porque: (1) não se baseia em prompt instructions (que Claude pode ignorar), (2) não se baseia em ordem de lista (que não é garantida), (3) usa o mecanismo de constrain nativo da API (tool_choice = "hard guarantee"), (4) modelar intencionalmente o fluxo com turnos é como trabalham pipelines profissionais (separação de concerns, falha rápida se DOI estiver faltando).

Por que as outras estão erradas:

A) `tool_choice` "any" apenas força que Claude use **alguma** ferramenta, não especifica qual. Combinado com prompt instructions ("priorize extract_metadata"), parece lógico, mas é frágil: Claude pode ignorar instruções de prioridade e ainda chamar lookup_citations primeiro, depois detect falha. Isso é o cenário que já está acontecendo no problema ("sometimes calls lookup_citations first").

B) É uma falsidade que Claude prioriza ferramentas pela ordem na lista. Isso não é um comportamento documentado ou confiável da API. Claude escolhe ferramentas com base em relevância semântica da descrição, não posição na array. Além disso, mesmo que fosse verdade, depender dessa heurística é mais frágil que usar `tool_choice` hard constraint.

D) Definir `tool_choice` para extract_metadata em **toda** chamada é overkill e impede enriquecimento legítimo. Você trava tudo em extract_metadata quando só precisa garantir ordem durante aquele fluxo específico. É como trancar a porta de um quarto quando você só quer evitar que alguém entre por uma janela específica.

Dica importante:
Padrão recorrente: **orchestração de ferramentas com dependências**. Quando ferramentas têm relações de dependência (A precisa da saída de B), a forma robusta é usar `tool_choice` hard constraints + multi-turn flow, não prompt instructions. Outro padrão conexo é "failure modes" — se uma ferramenta falhar silenciosamente (lookup_citations com DOI vazio), o pipeline falha. Aqui, separar em turnos permite detectar essa falha rapidamente. Esse conceito aparece em várias formas na certificação: error handling, observability, tool orchestration.

---

### 🚸 CHILDREN EXPLANATION

Explicação:
Imagina que você está fazendo um sanduíche e precisa de dois passos específicos: primeiro, você tira o livro de receitas da cozinha (extract_metadata = pegar os ingredientes e modo de fazer); depois, você liga para um amigo que conhece a história daquele sanduíche (lookup_citations = perguntar como é famoso). Mas se você ligar para o amigo ANTES de pegar o livro, ele vai dizer "qual sanduíche?" porque você não mencionou nem sequer o nome! 🥪 Como garantir a ordem certa?

Por que a alternativa C é a correta:
Você usa um **checklist explícito com passos ordenados**. Passo 1: pegar o livro (extract_metadata). Só depois que tiver os ingredientes e o modo de fazer, Passo 2: ligar para o amigo (lookup_citations) com as informações em mão. Dessa forma, o amigo já sabe exatamente sobre qual sanduíche você está falando. É como ter uma lista de tarefas onde você marca "pronto" antes de ir pro próximo passo.

Por que as outras estão erradas:

A) 🅰️ Dizer "use uma ferramenta e dê prioridade a extract_metadata no seu pensamento" é como pedir educadamente ao seu amigo "por favor, espera eu pegar o livro antes de me perguntar sobre o sanduíche". Mas seu amigo pode ainda assim perguntar logo de cara porque não entendeu a ordem. Educação (prompt instruction) não é garantia.

B) 🅱️ Listar extract_metadata primeiro na lista de ferramentas e torcer que Claude escolha aquela é como colocar o livro de receitas na primeira prateleira da cozinha — pode ser que seu amigo vire para o outro lado e pergunte do jeito dele mesmo! Claude não "automaticamente prioriza" ferramentas pela ordem. Isso é um mito.

D) 🅳️ Forçar que Claude **sempre** use extract_metadata em toda ligação é excessivo. Você só precisa disso quando o usuário pede "extraia E me diga como é famoso" juntos. Se o usuário pedir só "extraia", você não precisa trancar tudo. É como dizer "em casa, você sempre deve pegar o livro de receitas primeiro antes de fazer qualquer coisa" — até antes de tostar pão? Não faz sentido.

Dica importante:
O padrão: **fluxos com ordem importam**. Sempre que uma ação depende do resultado de outra, use **passos claros e separados**, não apenas esperança e instruções. É como receitas: passo 1, depois passo 2 — não misture. Use mecanismos de "hard lock" (como `tool_choice` específico) para garantir, não instruções suaves. Quando há dependências de dados, separe em turnos.

---

### CORRECT ANSWER

[ ] C - Set `tool_choice` to {"type": "tool", "name": "`extract_metadata`"} and process the enrichment requests in subsequent turns after receiving the extracted metadata.
