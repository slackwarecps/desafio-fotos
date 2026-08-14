Scenario: An agent is dropped into an unfamiliar repository and asked to add a feature. The best way to orient without burning context is to:

---

[ ] A - Load every file into context so nothing is missed.
[ ] B - Read the entry points and project structure, then search for the area the feature touches.
[ ] C - Start editing the first file that looks related.
[ ] D - Ask the user to explain every file.

---

### TRANSLATED QUESTION

Cenário: Um agente é lançado em um repositório desconhecido e solicitado a adicionar uma funcionalidade. A melhor forma de se orientar sem desperdiçar contexto é:

A) Carregar todos os arquivos do repositório no contexto para não perder nada.
B) Ler os entry points e a estrutura do projeto, depois buscar a área que a funcionalidade toca.
C) Começar a editar o primeiro arquivo que parece relacionado.
D) Pedir ao usuário para explicar cada arquivo.

---

### EXPLANATION (TECH LEAD)

Explicação:
Essa pergunta testa o conceito de eficiência de contexto no Claude Code — como explorar um repositório desconhecido sem queimar a janela de contexto do LLM. É um padrão central da certificação: exploração direcionada vs. exploração exaustiva, e quando usar cada uma.

Por que a alternativa B é a correta:
A estratégia de "entry points first" é superior porque concentra a exploração nos pontos de entrada (main.py, __init__.py, package.json, CLAUDE.md, READMEs) e na estrutura geral do projeto. Isso permite mapear rapidamente quais módulos existem, como se relacionam e qual deles provavelmente será tocado pela feature. Depois, a busca direcionada (Grep, Read seletivo) localiza o código relevante. Isso consome muito menos contexto do que ler tudo: você obtém ~80% da compreensão com ~20% dos tokens. Essa é a regra de Pareto aplicada a exploração de código.

Por que as outras estão erradas:

A) Carregar todos os arquivos queimaria rapidamente a janela de contexto — especialmente em repositórios grandes (800+ arquivos mencionados em outras perguntas). Além disso, não resolve o problema: ler tudo não significa entender relações entre módulos ou onde a mudança deve ir. É uma abordagem brute-force que contradiz o princípio de queimar contexto eficientemente.

C) Editar o "primeiro arquivo que parece relacionado" é o erro oposto: implementação prematura sem planejamento. Já foi mencionado em contexto de certificação como o padrão que leva a falhas em tarefas complexas — você mexe na abstração errada e tem que reverter. Essa é a "hypothesis-free execution" que falha.

D) Perguntar ao usuário para explicar cada arquivo transfere o ônus da exploração para o usuário, o que não é escalável. Além disso, o agente já deveria ter ferramentas (Read, Grep, CLAUDE.md) para autodescoberta.

Dica importante:
O padrão recorrente é: **investigação antes da implementação**. Quando há incerteza estrutural (não sabe onde fazer a mudança, comportamento espalhado entre vários módulos, histórico de retrabalho), a resposta é: plan mode, ou pelo menos exploração estruturada (entry points → structure → targeted reads). Isso aparece em várias questões da certificação sob nomes diferentes (plan mode, iterative understanding, avoiding premature edits).

---

### 🚸 CHILDREN EXPLANATION

Explicação:
Imagina que você tem um grande videojogo com muitos níveis, personagens e cenas, e alguém te pede para "adicionar um novo poder ao personagem principal". Você não conhece o jogo ainda. Qual é a forma mais inteligente de descobrir como fazer isso sem gastar toda sua energia lendo cada detalhe do jogo?

Por que a alternativa B é a correta:
Você deveria começar olhando para os "mapas principais" do jogo — como o personagem é criado, onde os poderes vivem, qual é a estrutura geral. Depois, você busca especificamente **onde** os poderes são armazenados e como se conectam ao personagem. Assim você descobre em que arquivo mexer, sem ler o script de cada NPC ou cada textura de cenário. É rápido e focado!

Por que as outras estão erradas:

A) 🅰️ Ler TODOS os arquivos do jogo (cada script, cada imagem) é como estudar o manual inteiro de um videojogo — desperdiça muita energia em informações que não importam para sua tarefa. Você quer adicionar um poder, não aprender sobre física ou desenho de personagens!

C) 🅲️ Começar a mexer no primeiro arquivo que parece relacionado sem planejar é como editar o jogo na sorte — "vou mexer aqui e ver o que acontece". Muito arriscado, você pode quebrar algo que não entendia.

D) 🅳️ Pedir para o criador do jogo explicar cada arquivo para você não faz sentido — o agente já tem ferramentas para descobrir sozinho. Você quer ser independente, não ficar pedindo ajuda o tempo todo!

Dica importante:
O padrão é: **primeiro, mapa e estrutura; depois, busca focada**. Sempre que não sabe onde uma mudança deve ir, não comece a editar. Explore primeiro, entenda o layout, e depois mexa com confiança. É como viajar para uma cidade nova — você olha o mapa antes de sair dirigindo.

---

### CORRECT ANSWER

[ ] B - Read the entry points and project structure, then search for the area the feature touches.
