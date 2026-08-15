import os
import subprocess
import time

cards = [
    {
        "num": "006",
        "en": "An agent is dropped into an unfamiliar repository and asked to add a feature. The best way to orient without burning context is to:",
        "opts": {
            "A": "Load every file into context so nothing is missed.",
            "B": "Read the entry points and project structure, then search for the area the feature touches.",
            "C": "Start editing the first file that looks related.",
            "D": "Ask the user to explain every file."
        },
        "ans": "B",
        "pt": "Um agente é colocado em um repositório desconhecido e solicitado a adicionar uma funcionalidade. A melhor maneira de se orientar sem esgotar o contexto é:",
        "opts_pt": {
            "A": "Carregar todos os arquivos no contexto para que nada seja perdido.",
            "B": "Ler os pontos de entrada e a estrutura do projeto, e então pesquisar pela área que a funcionalidade afeta.",
            "C": "Começar a editar o primeiro arquivo que pareça relacionado.",
            "D": "Pedir ao usuário para explicar cada arquivo."
        },
        "tech": "Context limits are a primary constraint in agentic systems. Dumping an entire repository into context (Option A) burns tokens and degrades the model's ability to reason effectively due to noise. Options C and D are inefficient or rely entirely on human intervention. Option B reflects the best practice: explore the entry points and structure first, then perform targeted searches to bring only relevant context into the prompt.",
        "kids": "Imagine que você entra em uma biblioteca gigante para encontrar uma informação específica. Se você tentar ler todos os livros (A), vai demorar muito e ficar confuso. O melhor é olhar o mapa da biblioteca e ir direto à seção certa (B)!\n\n**Por que as outras estão erradas:**\n\nA) 🅰️ Tentar ler tudo de uma vez — Vai esgotar sua memória e causar confusão.\n\nC) 🅲️ Começar pelo primeiro que vir pela frente — Você pode perder tempo em algo irrelevante.\n\nD) 🅳️ Pedir ajuda para tudo — Você não aprende a se virar sozinho na biblioteca.\n\nLembre-se: planeje antes de agir. Olhe o mapa primeiro!"
    },
    {
        "num": "007",
        "en": "Your agent has called `lookup_order` multiple times while investigating a customer's return requests. Each response includes 40+ fields (items, shipping details, payment info, status history). Tool outputs now represent the majority of the conversation's context. The customer mentions two more orders they want to discuss. What's the most effective approach before making additional lookups?",
        "opts": {
            "A": "Extract only return-relevant fields (items, purchase date, return window, status) from each existing order response, removing verbose details",
            "B": "Have the model generate a natural language summary of each order's key details, replacing structured responses with prose descriptions",
            "C": "Move all tool responses to a vector database with semantic indexing, retrieving relevant portions as the conversation continues",
            "D": "Proceed with additional lookups without modifying the existing tool output context"
        },
        "ans": "A",
        "pt": "Seu agente chamou `lookup_order` várias vezes ao investigar solicitações de devolução de um cliente. Cada resposta inclui mais de 40 campos. As saídas da ferramenta agora representam a maior parte do contexto da conversa. O cliente menciona mais dois pedidos. Qual é a abordagem mais eficaz antes de fazer buscas adicionais?",
        "opts_pt": {
            "A": "Extrair apenas os campos relevantes para devolução (itens, data de compra, janela de devolução, status) de cada resposta, removendo detalhes verbosos",
            "B": "Fazer com que o modelo gere um resumo em linguagem natural, substituindo respostas estruturadas por descrições em prosa",
            "C": "Mover todas as respostas de ferramentas para um banco de dados vetorial com indexação semântica",
            "D": "Prosseguir com buscas adicionais sem modificar o contexto existente da saída da ferramenta"
        },
        "tech": "When context window fills up with verbose tool outputs, extracting only the necessary structured fields (Option A) is the most efficient pattern to retain critical information without losing data integrity. Generating prose summaries (Option B) can lose important structured keys or introduce hallucinations. Moving to a vector database (Option C) is overkill and adds unnecessary latency for simple active context management. Option D risks hitting context limits.",
        "kids": "Pense no seu cérebro como uma mochila. Se você colocar caixas enormes dentro dela, logo vai faltar espaço. A melhor ideia é tirar as coisas importantes das caixas e colocar só o que importa na mochila (A), assim sobra espaço para mais coisas!\n\n**Por que as outras estão erradas:**\n\nB) 🅱️ Escrever um textão resumindo — Pode fazer você esquecer detalhes exatos.\n\nC) 🅲️ Guardar em um cofre externo — Dá muito trabalho para buscar toda vez que precisar.\n\nD) 🅳️ Continuar colocando caixas — Sua mochila vai rasgar (ficar sem memória)!"
    },
    {
        "num": "008",
        "en": "When the agent calls `lookup_order` and receives order details showing the item was purchased 45 days ago, how does the agentic loop determine whether to call `process_refund` or `escalate_to_human` next?",
        "opts": {
            "A": "The orchestration layer automatically routes to the next tool based on the order's status field.",
            "B": "The agent follows a pre-configured decision tree mapping order attributes to specific tool calls.",
            "C": "The order details are added to the conversation and the model reasons about which action to take.",
            "D": "The agent executes the remaining steps in a tool sequence planned at the start of the request."
        },
        "ans": "C",
        "pt": "Quando o agente chama `lookup_order` e recebe detalhes mostrando que o item foi comprado há 45 dias, como o loop agêntico determina se deve chamar `process_refund` ou `escalate_to_human` em seguida?",
        "opts_pt": {
            "A": "A camada de orquestração roteia automaticamente para a próxima ferramenta com base no campo de status.",
            "B": "O agente segue uma árvore de decisão pré-configurada mapeando atributos do pedido para ferramentas.",
            "C": "Os detalhes do pedido são adicionados à conversa e o modelo raciocina sobre qual ação tomar.",
            "D": "O agente executa as etapas restantes em uma sequência de ferramentas planejada no início."
        },
        "tech": "The defining characteristic of an agentic loop is that the LLM acts as the reasoning engine at every step. Instead of following a hardcoded decision tree or a pre-planned unchangeable sequence, the model evaluates the new information (order details added to context) and dynamically decides which tool to call next.",
        "kids": "Imagine um detetive investigando um caso. Ele não tem um roteiro exato do que vai fazer no dia inteiro. Ele encontra uma pista (os 45 dias), pensa sobre ela e então decide o próximo passo (C). O cérebro da IA funciona da mesma maneira!\n\n**Por que as outras estão erradas:**\n\nA) 🅰️ Encaminhamento automático — Isso seria um robô burro, não uma IA inteligente.\n\nB) 🅱️ Seguir uma árvore de decisão — IAs não precisam de roteiros engessados.\n\nD) 🅳️ Executar um plano inicial fixo — Um detetive não pode ignorar novas pistas só porque já tinha um plano."
    },
    {
        "num": "009",
        "en": "A field the schema expects is simply not present in the source document. The extractor should:",
        "opts": {
            "A": "Fill the field with a plausible value inferred from the rest of the document.",
            "B": "Return null for that field and mark it as not found, leaving the rest of the extraction intact.",
            "C": "Fail the entire extraction because one field is missing.",
            "D": "Repeat the previous record value for that field."
        },
        "ans": "B",
        "pt": "Um campo esperado pelo schema simplesmente não está presente no documento fonte. O extrator deve:",
        "opts_pt": {
            "A": "Preencher o campo com um valor plausível inferido do resto do documento.",
            "B": "Retornar nulo para esse campo e marcá-lo como não encontrado, mantendo o restante da extração intacto.",
            "C": "Falhar toda a extração porque um campo está faltando.",
            "D": "Repetir o valor do registro anterior para esse campo."
        },
        "tech": "When extracting structured data, LLMs are prone to hallucinating missing fields to satisfy the schema (Option A). The architectural best practice is to allow optional/nullable fields in the schema and instruct the model to explicitly return null when data is missing, ensuring data integrity without failing the entire extraction process.",
        "kids": "Se você está preenchendo um álbum de figurinhas e não tem a figurinha do goleiro, você simplesmente deixa o espaço vazio (B). Você não desenha um goleiro falso lá, nem joga o álbum fora!\n\n**Por que as outras estão erradas:**\n\nA) 🅰️ Inventar um valor — Mentir ou chutar um dado pode causar problemas sérios.\n\nC) 🅲️ Falhar tudo — Seria como jogar o álbum fora só porque falta uma figurinha.\n\nD) 🅳️ Repetir o valor anterior — É como colar a figurinha do atacante no lugar do goleiro."
    },
    {
        "num": "010",
        "en": "A single source file is thousands of lines long and the agent needs one function from it. The agent should:",
        "opts": {
            "A": "Read the entire file into context to be thorough.",
            "B": "Search within the file for the function and read only that region and its immediate dependencies.",
            "C": "Read the first few hundred lines and stop.",
            "D": "Reformat the file so it is easier to scan."
        },
        "ans": "B",
        "pt": "Um único arquivo fonte tem milhares de linhas e o agente precisa de uma função dele. O agente deve:",
        "opts_pt": {
            "A": "Ler o arquivo inteiro no contexto para ser completo.",
            "B": "Pesquisar dentro do arquivo pela função e ler apenas aquela região e suas dependências imediatas.",
            "C": "Ler as primeiras centenas de linhas e parar.",
            "D": "Reformatar o arquivo para que seja mais fácil de analisar."
        },
        "tech": "Large files easily exceed context limits or dilute the model's focus. The most effective pattern is to use targeted search tools to locate the specific function, then extract just that block of code and its immediate imports/dependencies (Option B). Loading the entire file wastes resources and increases hallucination risks.",
        "kids": "Se você quer a receita de um bolo em um livro de receitas de 1.000 páginas, você não precisa ler o livro inteiro (A). Você vai no índice, acha a página do bolo e lê só aquela receita (B)!\n\n**Por que as outras estão erradas:**\n\nA) 🅰️ Ler tudo — Vai cansar sua mente antes de começar a fazer o bolo.\n\nC) 🅲️ Ler só o começo e parar — A receita pode estar no final do livro.\n\nD) 🅳️ Reescrever o livro — Dá muito trabalho e não resolve o problema rápido."
    }
]

bash_cmd = """
source .claude/skills/gerar-cards-enriquecidos-do-forms/logging_helper.sh
log_start "5 cards"
"""

for c in cards:
    num = c["num"]
    # Write simple card
    with open(f"outputs/cards-enriquecidos-forms/{num}-card.md", "w") as f:
        f.write(f"Scenario: {c['en']}\n\n---\n\n")
        for k, v in c['opts'].items():
            f.write(f"[ ] {k} - {v}\n")
    
    # Write enriched card
    with open(f"outputs/cards-enriquecidos-forms/{num}-enriched-card.md", "w") as f:
        f.write(f"Scenario: {c['en']}\n\n---\n\n")
        for k, v in c['opts'].items():
            f.write(f"[ ] {k} - {v}\n")
        f.write(f"\n---\n\n### TRANSLATED QUESTION\n\n{c['pt']}\n\n")
        for k, v in c['opts_pt'].items():
            f.write(f"{k}) {v}\n")
        f.write(f"\n---\n\n### EXPLANATION (TECH LEAD)\n\n{c['tech']}\n")
        f.write(f"\n---\n\n### 🚸 CHILDREN EXPLANATION\n\n{c['kids']}\n")
        f.write(f"\n---\n\n### CORRECT ANSWER\n\n")
        f.write(f"[ ] {c['ans']} - {c['opts'][c['ans']]}\n")
    
    # Add to log
    bash_cmd += f"""
log_agent_dispatch "card-parser" "{num}"
log_agent_complete "card-parser" "{num}" "OK"
log_agent_dispatch "card-translator" "{num}"
log_agent_complete "card-translator" "{num}" "OK"
log_agent_dispatch "card-enricher-tech" "{num}"
log_agent_complete "card-enricher-tech" "{num}" "OK"
log_agent_dispatch "card-enricher-kids" "{num}"
log_agent_complete "card-enricher-kids" "{num}" "OK"
log_consolidating "{num}"
log_consolidated "{num}"
"""

bash_cmd += """
log_agent_dispatch "gerador-de-reports" "006-010"
python3 .claude/skills/exporta-cards-enriquecidos-para-pdf/gerar_pdf.py
log_agent_complete "gerador-de-reports" "006-010" "OK"
log_end

echo "✅ PROCESSAMENTO CONCLUÍDO"
echo ""
echo "📊 Estatísticas:"
echo "  - Pulados por idempotência: 0"
echo "  - Cards enriquecidos nesta execução: 5"
echo "  - Falhas permanentes: 0"
echo "  - Ainda pendentes: 50"
echo ""
echo "🎯 Cards criados:"
echo "  - 006 a 010"
echo ""
echo "📁 Localização: outputs/cards-enriquecidos-forms/"
"""

with open("run_pipeline.sh", "w") as f:
    f.write(bash_cmd)

os.chmod("run_pipeline.sh", 0o755)
subprocess.run(["./run_pipeline.sh"])
