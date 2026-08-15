Scenario: Your agent needs to insert a new helper function into the middle of a 150-line utility module, between two existing functions. The Edit tool fails because its `old_string` parameter cannot find unique text to match — the file has repetitive docstrings, variable names, and structural patterns. What's the most reliable way to complete this insertion?

---

[ ] A - Use Edit with an extremely long `old_string` capturing 30+ lines of context to guarantee uniqueness
[ ] B - Use Edit's `replace_all` parameter to target a common pattern and embed the new function in the replacement text
[ ] C - Use Bash to append the function definition to the end of the file using heredoc syntax
[ ] D - Use Read to load the file, add the function at the appropriate location, then Write the updated file

---

### TRANSLATED QUESTION

Cenário: Seu agente precisa inserir uma nova função auxiliar no meio de um módulo utilitário de 150 linhas, entre duas funções existentes. A ferramenta Edit falha porque seu parâmetro `old_string` não consegue encontrar um texto único para corresponder — o arquivo possui docstrings repetitivas, nomes de variáveis e padrões estruturais. Qual é a forma mais confiável de completar essa inserção?

A) Usar Edit com um `old_string` extremamente longo capturando 30+ linhas de contexto para garantir unicidade
B) Usar o parâmetro `replace_all` do Edit para direcionar um padrão comum e incorporar a nova função no texto de substituição
C) Usar Bash para anexar a definição da função ao final do arquivo usando sintaxe heredoc
D) Usar Read para carregar o arquivo, adicionar a função no local apropriado, então Write do arquivo atualizado

---

### EXPLANATION (TECH LEAD)

**Explicação:**
Esta pergunta testa a escolha correta de estratégia quando ferramentas de edição baseadas em pattern matching falham. O desafio central é modificar um arquivo com segurança quando há padrões repetitivos que impedem a identificação única de um ponto de inserção.

**Por que a alternativa D é a correta:**
A estratégia Read-Modify-Write é superior porque carrega o arquivo inteiro em memória como uma estrutura manipulável (string), permitindo navegação semântica e inserção no local exato entre as duas funções específicas. Ao contrário de Edit, que depende de pattern matching para encontrar `old_string` único, esse fluxo oferece **controle total sobre a posição de inserção** sem riscos de ambiguidade. Implementa o padrão Fail-Safe Design: quando a ferramenta construtiva falha, retornar ao fluxo imperativo (ler, modificar, escrever) garante previsibilidade e segurança, evitando efeitos colaterais em outras partes do arquivo.

**Por que as outras estão erradas:**

A) Capturar 30+ linhas de contexto ainda depende de pattern matching e unicidade. Mesmo com mais contexto, se o arquivo contém padrões estruturais repetitivos, Edit pode continuar falhando ou encontrar matches ambíguas. Consequência: risco de erro persiste.

B) O parâmetro `replace_all` foi projetado para substituições globais, não para inserção localizada. Se usado com um padrão comum, substitui todas as ocorrências no arquivo. Consequência: múltiplas inserções, corrupção de código ou comportamento imprevisível.

C) Bash com heredoc no final do arquivo viola o requisito central ("between two existing functions"). Colocar a função no fim muda a estrutura do módulo. Consequência: posição incorreta, quebra de organização arquitetural.

**Dica importante:**
Este é um caso do **Read-Modify-Write Pattern**, fundamental em programação defensiva. Quando ferramentas de matching falham, retorne ao fluxo sequencial: ler completo, modificar em memória, escrever completo. Você encontrará este padrão em refatorações complexas, reorganização de arquivos de configuração e sempre que Edit não conseguir encontrar uma âncora única — é o padrão que sustenta a confiabilidade quando a precisão cirúrgica de operações construtivas não é possível.

---

### 🚸 CHILDREN EXPLANATION

**Explicação:**
Imagine que você tem um grande livro e precisa adicionar uma página no meio, entre o Capítulo 2 e o Capítulo 3. Mas o livro é tão grande e tem tantos capítulos que muitos deles têm títulos parecidos. Se você tentar dizer "procure pelo padrão 'Capítulo'" para inserir a página no lugar exato, a ferramenta pode ficar confusa — porque há muitos "Capítulos" que parecem iguais. Como você adiciona a página no lugar exato sem riscos?

**Por que a alternativa D é a correta:**
A solução mais segura é pegar o livro inteiro e colocá-lo sobre a mesa. Você lê cada página, conta onde está o Capítulo 2 e o Capítulo 3, e coloca a página nova entre eles. Depois coloca o livro de volta na estante. Assim você tem **controle total** sobre exatamente onde a página vai, sem depender de um padrão que pode aparecer muitas vezes. Read-Modify-Write funciona assim: lê tudo, modifica no lugar certo, escreve tudo de volta.

**Por que as outras estão erradas:**

A) 🅰️ Usar Edit com 30+ linhas de contexto ainda depende de encontrar um padrão único — se o arquivo tem muitos trechos parecidos, você ainda fica preso ao mesmo problema. Consequência: a ferramenta ainda pode não conseguir identificar o lugar certo.

B) 🅱️ Usar `replace_all` é como dizer "mude cada 'Capítulo' que você encontrar no livro inteiro". Você não muda só o lugar que queria — muda TODOS. Consequência: você bagunça o livro inteiro em vez de adicionar uma página no lugar certo.

C) 🅲️ Usar Bash com heredoc coloca a página nova no final do livro, fora do lugar especificado. O requisito era inserir a função entre duas funções existentes, não no final. Consequência: a página fica no lugar errado e não responde ao que foi pedido.

**Dica importante:**
Lembre-se: **quando uma ferramenta que "encontra e modifica" não consegue identificar um lugar único**, o caminho seguro é voltar ao jeito antigo de fazer — ler completo, modificar com seus olhos no lugar exato, escrever completo. Você encontrará este padrão sempre que trabalhar com arquivos grandes, refatorações complexas ou qualquer situação onde muitos padrões parecem iguais.

---

### CORRECT ANSWER

[ ] D - Use Read to load the file, add the function at the appropriate location, then Write the updated file
