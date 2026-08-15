Scenario: An agent is dropped into an unfamiliar repository and asked to add a feature. The best way to orient without burning context is to:

---

[ ] A - Load every file into context so nothing is missed.
[ ] B - Read the entry points and project structure, then search for the area the feature touches.
[ ] C - Start editing the first file that looks related.
[ ] D - Ask the user to explain every file.

---

### TRANSLATED QUESTION

Cenário: Um agente é inserido em um repositório desconhecido e solicitado a adicionar um recurso. A melhor forma de se orientar sem consumir contexto é:

A) Carregar todos os arquivos no contexto para que nada seja perdido.
B) Ler os pontos de entrada e a estrutura do projeto, depois procurar pela área que o recurso afeta.
C) Começar a editar o primeiro arquivo que pareça relacionado.
D) Pedir ao usuário para explicar cada arquivo.

---

### EXPLANATION (TECH LEAD)

**Explicação:**
Esta pergunta testa o princípio de Strategic Exploration e Context Efficiency — como navegar em um repositório desconhecido sem desperdício de contexto. A questão sonda compreensão sobre a ordem correta de atividades: visão geral antes de detalhes, estrutura antes de implementação.

**Por que a alternativa B é a correta:**
Esta alternativa é superior porque aplica o princípio de Least Privilege Informacional — começar com entry points (pontos de entrada naturais como main.py, __init__.py, routes/, config/) e estrutura de diretórios fornece compreensão de limites arquiteturais e dependências sem carregar todos os arquivos. Segue o padrão Progressive Disclosure: explora incrementalmente, localizando exatamente onde a feature toca o código. Permite decisões informadas sobre arquitetura, convenções e padrões existentes antes de qualquer modificação, reduzindo risco de violação de abstrações.

**Por que as outras estão erradas:**

A) Carregar todos os arquivos no contexto queima tokens rapidamente em repositórios grandes, deixando pouca memória/contexto justamente quando o agente precisa fazer análise profunda e integração de aprendizado. Ineficiente e desperdiçador.

C) Começar a editar o primeiro arquivo que pareça relacionado carrega risco de modificar código sem compreender padrões, dependências e convenções do projeto. Consequência: alterações podem quebrar abstrações, duplicar código existente ou violar convenções não documentadas.

D) Pedir ao usuário para explicar cada arquivo é impraticável e desconsidera que um repositório bem estruturado já fornece contexto via entry points, nomes descritivos e organização de diretórios. Desperdício de tempo do usuário.

**Dica importante:**
Lembre-se que este é um caso do padrão "Entry Point Discovery" — você encontrará situações similares ao investigar qualquer novo sistema: sempre comece pelos arquivos de configuração, rotas (routes/, controllers/), ou funções main(). Este padrão conecta-se ao conceito maior de Codebase Comprehension: estrutura informa design, design informa onde fazer mudanças.

---

### 🚸 CHILDREN EXPLANATION

**Explicação:**
Imagine que você chega em uma cidade desconhecida e precisa entregar um pacote em uma loja específica. A melhor estratégia não é explorar cada rua e beco (isso consome muito tempo e energia!). Em vez disso, você pergunta a um morador: "Onde fica o centro? Quais são as ruas principais?" Depois, você procura a loja no mapa que montou mentalmente. Um repositório de código funciona igual — você precisa do "mapa" antes de sair correndo por todas as "ruas".

**Por que a alternativa B é a correta:**
Esta é a melhor opção porque é como ler o mapa ANTES de explorar a cidade. Os "entry points" (arquivos como main.py, config/) são como as ruas principais e os sinais de trânsito. A estrutura do projeto é o mapa. Se você estuda isso primeiro, você descobre automaticamente aonde ir. Você entende onde estão os negócios (código), como tudo se conecta, e consegue encontrar exatamente o lugar que precisa modificar sem se perder.

**Por que as outras estão erradas:**

A) 🅰️ Carregar todos os arquivos queima sua energia (contexto). É como tentar memorizar cada rua, cada esquina e cada prédio da cidade de uma vez — você fica cansado e acaba não sabendo por onde começar a entregar o pacote.

C) 🅲️ Começar a editar sem entender o projeto é perigoso. É como entrar na primeira loja que você vê e começar a mexer nas coisas sem saber como a loja funciona — você pode quebrar algo importante ou duplicar o trabalho de alguém.

D) 🅳️ Pedir ao usuário para explicar cada arquivo não funciona bem porque repositórios bem organizados já contam a história por si: nomes descritivos, pastas estruturadas. Você aprende lendo sozinho — o usuário não precisa ser seu guia pessoal!

**Dica importante:**
Lembre-se: sempre que você chegar em um lugar novo (um repositório, um projeto, uma empresa), comece pelo MAPA — pergunte pela estrutura, pontos de entrada, limites principais. Este padrão funciona para tudo: aprender um novo videogame, entender como uma casa é organizada, ou navegar em um novo idioma. Estrutura primeiro, detalhes depois!

---

### CORRECT ANSWER

[ ] B - Read the entry points and project structure, then search for the area the feature touches.
