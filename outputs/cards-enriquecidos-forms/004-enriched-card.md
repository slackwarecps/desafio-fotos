Scenario: An engineer who just joined the team asks the agent to help them understand the authentication and authorization architecture before making security improvements. The codebase has 800+ files across multiple services. What exploration strategy will most effectively build understanding, given Claude built-in tools and context limits?

---

[ ] A - Read any CLAUDE.md and README files first, then ask the engineer to specify which 10-15 files are most important for understanding the auth system.
[ ] B - Launch parallel subagents to explore different services simultaneously, then synthesize their findings into an architectural overview.
[ ] C - Use Grep to find authentication entry points, read those files, then follow imports and function calls to map the auth flow incrementally.
[ ] D - Read all files containing "auth", "login", "permission", or "token" in their content or filename.

---

### TRANSLATED QUESTION

Cenário: Um engenheiro que acaba de se juntar ao time pede ao agente para ajudá-lo a entender a arquitetura de autenticação e autorização antes de fazer melhorias de segurança. A base de código tem 800+ arquivos em múltiplos serviços. Qual estratégia de exploração construirá entendimento mais efetivamente, considerando ferramentas nativas do Claude e limites de contexto?

Alternativas traduzidas:

A) Ler arquivos CLAUDE.md e README primeiro, depois pedir ao engenheiro que especifique quais 10-15 arquivos são mais importantes para entender o sistema de auth.
B) Lançar subagentes em paralelo para explorar diferentes serviços simultaneamente, depois sintetizar seus achados em uma visão arquitetural.
C) Usar Grep para encontrar entry points de autenticação, ler esses arquivos, depois seguir imports e chamadas de funções para mapear o fluxo de auth incrementalmente.
D) Ler todos os arquivos contendo "auth", "login", "permission", ou "token" no conteúdo ou nome de arquivo.

---

### EXPLANATION (TECH LEAD)

Explicação:
A pergunta testa **estratégia de exploração eficiente sob restrições de contexto**. O cenário apresenta um desafio real: 800+ arquivos, múltiplos serviços, contexto limitado, necessidade de construir compreensão arquitetural. Isto é um padrão central em tarefas agentic: exploração direcionada vs. brute-force.

Por que a alternativa C é a correta:
A estratégia de "Grep → imports → incremental mapping" é superior porque: (1) **Inicia com alta precisão**: Grep localiza entry points concretos (funções de auth, decoradores) em vez de confiar em convenção. (2) **Segue relacionamentos naturais**: imports e call chains revelam como os módulos se relacionam sem ler tudo. (3) **Controla crescimento do contexto**: você expande apenas para os arquivos conectados aos entry points descobertos, não carrega 800 arquivos inteiros. (4) **Detecta padrões rapidamente**: uma vez que você lê os entry points + seus imports diretos (10-15 arquivos), o padrão de arquitetura fica claro. Isto consome ~50KB de contexto em vez de 10MB.

Por que as outras estão erradas:

A) Depender de CLAUDE.md + pedir ao engenheiro deixa a exploração incompleta: CLAUDE.md pode estar desatualizado ou incompleto. Pedir ao engenheiro transfere o ônus da descoberta, além disso ele pode ter viés sobre quais arquivos "parecem" importantes sem uma estratégia sistemática.

B) Subagentes em paralelo parece paralelo mas introduz overhead: você precisa coordenar outputs desconexos, risco de cada subagente ler os mesmos arquivos (desperdício), difícil sintetizar "achados incompletos" sem contexto da integração entre serviços. Além disso, 800+ arquivos distribuídos entre subagentes continua sendo brute-force.

D) "Ler todos files contendo 'auth'..." é variação de brute-force: um grep por "auth" provavelmente retorna 100+ arquivos. Ler todos continua queimando contexto exponencialmente. Pior, alguns arquivo contêm "auth" em comentários ou logs, não em lógica de auth.

Dica importante:
Padrão recorrente: **investigação direcionada através de busca + seguindo relacionamentos**. Sempre que tem "muitos arquivos, contexto limitado", a resposta é: entrada específica (grep) → follow imports → read apenas a closure. Isto aparece em várias certificações: "search then read", não "read all".

---

### 🚸 CHILDREN EXPLANATION

Explicação:
Imagina que você tem uma biblioteca gigante com 800 livros sobre segurança, e precisa entender como o sistema de "acesso" funciona. Você não vai ler todos os 800 livros — seria impraticável! Em vez disso, você quer usar uma estratégia esperta.

Por que a alternativa C é a correta:
Você começa procurando (tipo com um índice remissivo) onde exatamente "autenticação" é mencionada. Encontra alguns capítulos-chave. Depois, você lê esses capítulos, e eles te apontam para outros capítulos relacionados ("veja também Capítulo X"). Você segue esses "veja também" e assim descobre a estrutura inteira sem ler 800 livros. É como explorar um mapa — você começa num ponto e segue os caminhos!

Por que as outras estão erradas:

A) 🅰️ Confiar só no índice (CLAUDE.md) e perguntar ao bibliotecário qual 10-15 livros ler é preguiçoso e incompleto — o índice pode estar desatualizado, e o bibliotecário pode esquecer algum livro importante.

B) 🅱️ Mandar vários ajudantes lerem livros diferentes e depois tentar juntar o aprendizado deles é complicado — eles vão ler os mesmos livros (desperdício), vão ter dúvidas um sobre o outro, e você vai ficar confuso tentando conectar o que cada um descobriu.

D) 🅳️ Ler TODOS os 800 livros que mencionam "segurança" é o pior — você vai gastar semanas lendo coisas irrelevantes, quando na verdade só precisava entender 10-15 capítulos-chave. É ineficiente demais!

Dica importante:
O padrão inteligente é: **busca focada → ler o essencial → seguir as pistas**. Como um detetive investigando um crime: você procura evidências específicas, lê os documentos relevantes, segue as conexões entre eles. Não lê toda a história da cidade!

---

### CORRECT ANSWER

[ ] C - Use Grep to find authentication entry points, read those files, then follow imports and function calls to map the auth flow incrementally.
