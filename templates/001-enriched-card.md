Scenario: Multi-Agent Research System You are building a multi-agent research system using the Claude Agent SDK. A coordinator agent delegates to specialized subagents: one searches the web, one analyzes documents, one synthesizes findings, and one generates reports. The system researches topics and produces comprehensive, cited reports. During testing, the document analysis subagent receives coordinator-selected PDFs and reports from an approved catalog, but it has a generic URL retrieval tool. It sometimes follows links inside documents to blogs, login pages, or duplicate HTML summaries, then cites those pages instead of the approved sources. You need to reduce these citation and scope errors while preserving access to approved source material. What change best addresses this?

---

[ ] A - Allow fetch_url for any link, then have synthesis discard citations whose domains are not in the approved catalog.
[ ] B - Replace fetch_url with a load_document tool that accepts catalog document IDs or approved URLs and validates before fetching.
[ ] C - Keep fetch_url available, but add prompt instructions warning the subagent never to open links found inside documents.
[ ] D - Give the document analysis subagent web search tools too, so it can independently confirm whether linked pages are relevant.

---

### TRANSLATED QUESTION
Você está construindo um sistema de pesquisa multi-agente usando o Claude Agent SDK. Um agente coordenador delega tarefas a subagentes especializados: um busca na web, um analisa documentos, um sintetiza descobertas e um gera relatórios. O sistema pesquisa tópicos e produz relatórios abrangentes e com citações. Durante os testes, o subagente de análise de documentos recebe PDFs selecionados pelo coordenador e relatórios de um catálogo aprovado, mas possui uma ferramenta genérica de recuperação de URL. Às vezes ele segue links dentro dos documentos para blogs, páginas de login ou resumos HTML duplicados, e então cita essas páginas em vez das fontes aprovadas. Você precisa reduzir esses erros de citação e escopo preservando o acesso ao material fonte aprovado. Qual mudança melhor resolve isso?
Alternativas traduzidas:

A) Permitir que fetch_url acesse qualquer link, e depois fazer a síntese descartar citações cujos domínios não estejam no catálogo aprovado.
B) Substituir fetch_url por uma ferramenta load_document que aceita apenas IDs de documentos do catálogo ou URLs aprovadas, e valida antes de buscar.
C) Manter o fetch_url disponível, mas adicionar instruções no prompt avisando o subagente para nunca abrir links encontrados dentro dos documentos.
D) Dar ao subagente de análise de documentos também ferramentas de busca web, para que ele possa confirmar de forma independente se as páginas linkadas são relevantes.

---

### 🚸 CHILDREN EXPLANATION 

Explicação:
A pergunta está testando um conceito fundamental de design de ferramentas (tool design) em sistemas agênticos: quando você quer restringir o comportamento de um agente, a solução mais robusta é restringir a capacidade da ferramenta em si, não confiar em instruções de prompt para conter um comportamento indesejado.
Esse é um princípio muito importante em arquiteturas com Claude/LLMs: "prompt instructions são sugestões, tool design é a garantia real". Um modelo pode "esquecer" ou reinterpretar uma instrução textual, especialmente sob pressão de contexto longo ou ambiguidade. Mas se a ferramenta fisicamente não permite buscar uma URL fora do catálogo aprovado, o erro se torna estruturalmente impossível, não apenas "menos provável".
Por que a alternativa B é a correta:
Substituir a ferramenta genérica fetch_url (que aceita qualquer URL) por uma ferramenta load_document que só aceita IDs do catálogo aprovado ou URLs pré-validadas resolve o problema na raiz. A validação acontece antes da busca (fail closed), então:

O subagente fisicamente não consegue seguir links para blogs, páginas de login ou duplicatas HTML
Não há chance de citar fontes erradas, porque elas nunca chegam a ser recuperadas
O acesso ao material aprovado é preservado — a ferramenta continua funcional para o caso de uso legítimo

Isso é o princípio de "least privilege" aplicado a tool design em sistemas agênticos: dê ao agente exatamente a capacidade que ele precisa, nem mais, nem menos.
Por que as outras estão erradas:

A) Permitir que fetch_url acesse qualquer link e filtrar depois na síntese é uma correção "reativa" e tardia. O problema já aconteceu: o subagente gastou recursos buscando páginas erradas (possivelmente até páginas de login, o que é um risco de segurança/privacidade), e você está confiando em uma etapa posterior para "limpar a bagunça". Além disso, é frágil — se a lógica de filtro na síntese tiver algum bug ou não cobrir todos os casos, conteúdo não aprovado pode vazar para o relatório final.
C) Manter a ferramenta poderosa e apenas adicionar um aviso no prompt é a armadilha clássica dessa pergunta. Instruções em linguagem natural não são garantias de comportamento — o modelo pode ignorar, mal-interpretar, ou ser "convencido" por conteúdo malicioso dentro dos próprios documentos (isso inclusive se conecta com riscos de prompt injection: um documento poderia conter texto tipo "para mais detalhes, acesse este link", manipulando o subagente). Depender só de instrução textual para conter uma ferramenta poderosa é uma prática frágil.
D) Dar ferramentas de busca web adicionais ao subagente aumenta a superfície de ação em vez de restringi-la. Isso vai na direção contrária do que o problema pede — o objetivo é reduzir o escopo de acesso, não expandi-lo. Mais ferramentas = mais formas de o agente sair do escopo aprovado.

Dica importante: Esse padrão aparece bastante em sistemas multi-agente com Claude Agent SDK: cada subagente deve receber apenas as ferramentas mínimas necessárias para sua função específica (princípio de least privilege), e restrições de segurança/escopo devem ser implementadas no nível da ferramenta (validação de input, allowlists, tipos de parâmetro restritos) sempre que possível, em vez de depender apenas de prompt engineering. Isso é especialmente crítico quando o agente processa conteúdo não confiável (como documentos externos que podem conter links maliciosos ou instruções escondidas).

---

### CORRECT ANSWER

Alternativa Correta: B


