import os
from pathlib import Path

output_dir = Path("/Users/fabioalvaropereira/Desktop/desafio-fotos/outputs/cards-enriquecidos")
output_dir.mkdir(parents=True, exist_ok=True)

cards_data = {
    17: {
        "scenario": "Scenario: Customer Support Resolution Agent You are building a customer support resolution agent using the Claude Agent SDK. The agent handles high-ambiguity requests like returns, billing disputes, and account issues. It has access to backend systems through MCP tools (get_customer, lookup_order, process_refund, escalate_to_human). Your target is 80%+ first-contact resolution while knowing when to escalate. Production logs show that lookup_order and process_refund both return the same failure text, \"Operation failed.\" The agent retries declined refunds, tells customers to try again later when they provided invalid order IDs, and escalates temporary timeout cases that would likely succeed on retry. What change would best improve the agent's recovery decisions?",
        "options": {
            "A": "Standardize every tool failure as a generic message, then ask Claude to infer recovery steps from conversation context.",
            "B": "Route all refund and order lookup failures to escalate_to_human, avoiding autonomous recovery entirely after backend errors.",
            "C": "Return MCP tool errors with isError plus category, retryability, and safe messages distinguishing transient, validation, business, and permission failures.",
            "D": "Retry every failed backend tool call three times, then escalate unresolved cases without exposing error details to Claude."
        },
        "correct_letter": "C",
        "translated_question": "Você está construindo um agente de resolução de suporte ao cliente usando o Claude Agent SDK. O agente lida com solicitações altamente ambíguas, como devoluções, disputas de faturamento e problemas de conta. Ele tem acesso a sistemas de backend por meio de ferramentas MCP (get_customer, lookup_order, process_refund, escalate_to_human). Sua meta é obter mais de 80% de resolução no primeiro contato, sabendo quando escalar. Os logs de produção mostram que lookup_order e process_refund retornam o mesmo texto de falha, \"Operation failed.\" O agente tenta novamente reembolsos recusados, orienta os clientes a tentar novamente mais tarde quando fornecerem IDs de pedido inválidos e escala casos de timeout temporário que provavelmente teriam sucesso em uma nova tentativa. Qual alteração melhoraria as decisões de recuperação do agente?",
        "translated_options": {
            "A": "Padronizar cada falha de ferramenta como uma mensagem genérica e, em seguida, pedir ao Claude para inferir as etapas de recuperação com base no contexto da conversa.",
            "B": "Rotear todas as falhas de reembolso e busca de pedidos para escalate_to_human, evitando totalmente a recuperação autônoma após erros de backend.",
            "C": "Retornar erros das ferramentas MCP com isError mais categoria, capacidade de repetição e mensagens seguras que diferenciem falhas temporárias, de validação, de negócios e de permissão.",
            "D": "Tentar novamente cada chamada de ferramenta de backend com falha três vezes e, em seguida, escalar casos não resolvidos sem expor detalhes do erro ao Claude."
        },
        "tech_lead_exp": "Esta questão aborda o tratamento de erros em arquiteturas de agentes usando o Claude Agent SDK e servidores MCP. Quando as ferramentas de backend expõem apenas erros genéricos (\"Operation failed\"), o agente perde a visibilidade necessária para tomar decisões de recuperação adequadas e específicas para cada tipo de falha.",
        "tech_lead_why": "Retornar erros estruturados das ferramentas MCP contendo metadados como a flag `isError`, a categoria da falha, a possibilidade de retry (`retryability`) e mensagens seguras permite que o agente decida de forma determinística e inteligente o próximo passo. Com essas informações diferenciadas, o Claude consegue distinguir se deve tentar novamente (em falhas transientes/timeouts), orientar o usuário (em falhas de validação de dados) ou solicitar intervenção humana (em falhas de regras de negócios impeditivas), atingindo a meta de resolução autônoma eficiente.",
        "tech_lead_wrong": {
            "A": "Padronizar falhas como mensagens genéricas remove o sinal técnico necessário para o agente diferenciar as causas raiz, fazendo com que ele precise \"adivinhar\" o comportamento e gerando decisões erráticas de recuperação.",
            "B": "Rotear todas as falhas para o atendimento humano invalida o objetivo de atingir mais de 80% de resolução autônoma em primeiro contato, aumentando desnecessariamente a carga sobre os operadores de suporte humanos.",
            "D": "Tentar novamente todas as chamadas de backend de forma cega três vezes sem expor detalhes de erro ao Claude gera desperdício de chamadas de API desnecessárias em casos de falhas definitivas (como permissão ou validação) e impede que o agente aprenda e adapte seu fluxo de conversação."
        },
        "tech_lead_tip": "No Claude Agent SDK, as respostas de ferramentas que indicam erro devem definir a flag `isError: true` no bloco de conteúdo da ferramenta e fornecer uma estrutura de dados de erro rica no payload. Isso impede que o modelo interprete a falha como um retorno normal de sucesso.",
        "children_exp": "Imagine um ajudante de cozinha que recebe apenas a mensagem \"deu ruim\" toda vez que algo falha na cozinha, seja porque a faca sumiu, a comida queimou ou a geladeira quebrou. Ele não sabe se deve procurar a faca, fazer o prato de novo ou chamar um técnico.",
        "children_why": "A melhor solução é o ajudante receber um aviso detalhado dizendo exatamente o que aconteceu: se foi um problema simples que dá para tentar de novo sozinho (como pegar outro garfo), ou se é algo grave que exige chamar o chef. Assim, ele trabalha muito melhor e resolve quase tudo sozinho!",
        "children_wrong": {
            "A": "Se todas as mensagens continuarem sendo apenas \"deu ruim\", o ajudante vai continuar confuso e vai ter que adivinhar o que fazer toda vez.",
            "B": "Chamar o chef humano para qualquer probleminha (como uma colher suja) vai deixar o chef bravo e o ajudante não vai fazer nada sozinho.",
            "D": "Tentar fazer a mesma coisa do mesmo jeito três vezes seguidas sem saber o que está quebrado só vai fazer o ajudante perder tempo à toa."
        },
        "children_tip": "Sempre dê detalhes claros sobre o que deu errado para que o robô saiba se pode consertar sozinho ou se precisa de ajuda!"
    },
    18: {
        "scenario": "Scenario: Customer Support Resolution Agent You are building a customer support resolution agent using the Claude Agent SDK. The agent handles high-ambiguity requests like returns, billing disputes, and account issues. It has access to backend systems through MCP tools (get_customer, lookup_order, process_refund, escalate_to_human). Your target is 80%+ first-contact resolution while knowing when to escalate. In a compliance review, you find several transcripts where the agent called process_refund immediately after a customer claimed an order was damaged. In those cases, lookup_order later showed the order was past the return window or the refund amount differed from the customer's estimate. The current system prompt says to verify customers and check order eligibility before refunds. What change best reduces this risk?",
        "options": {
            "A": "Add a prerequisite gate that rejects process_refund until verified customer, eligible order, and computed refund amount are present in state.",
            "B": "Strengthen the system prompt to require checking customer identity and order eligibility before any refund-related tool call.",
            "C": "Add few-shot examples where the assistant calls get_customer and lookup_order before refunds, including damaged-order and late-return cases.",
            "D": "Add a text parser that permits process_refund only after assistant messages contain verified, eligible, and refund amount."
        },
        "correct_letter": "A",
        "translated_question": "Você está construindo um agente de resolução de suporte ao cliente usando o Claude Agent SDK. O agente lida com solicitações altamente ambíguas, como devoluções, disputas de faturamento e problemas de conta. Ele tem acesso a sistemas de backend por meio de ferramentas MCP (get_customer, lookup_order, process_refund, escalate_to_human). Sua meta é obter mais de 80% de resolução no primeiro contato, sabendo quando escalar. Em uma revisão de conformidade (compliance), você encontra várias transcrições em que o agente chamou process_refund imediatamente após um cliente alegar que um pedido estava danificado. Nesses casos, o lookup_order posteriormente mostrou que o pedido estava fora do prazo de devolução ou que o valor do reembolso diferia da estimativa do cliente. O prompt do sistema atual diz para verificar os clientes e a elegibilidade do pedido antes dos reembolsos. Qual alteração reduz melhor esse risco?",
        "translated_options": {
            "A": "Adicionar uma barreira de pré-requisito (prerequisite gate) que rejeita process_refund até que o cliente verificado, o pedido qualificado e o valor do reembolso calculado estejam presentes no estado do agente.",
            "B": "Fortalecer o prompt do sistema para exigir a verificação da identidade do cliente e da elegibilidade do pedido antes de qualquer chamada de ferramenta relacionada a reembolso.",
            "C": "Adicionar exemplos de poucos disparos (few-shot) onde o assistente chama get_customer e lookup_order antes dos reembolsos, incluindo casos de pedidos danificados e devoluções atrasadas.",
            "D": "Adicionar um analisador de texto (text parser) que permite process_refund somente depois que as mensagens do assistente contiverem \"verificado\", \"elegível\" e o valor do reembolso."
        },
        "tech_lead_exp": "Esta questão aborda o design de guardrails e barreiras de segurança (gates) em sistemas baseados em agentes de IA. Instruções em linguagem natural no prompt do sistema ou exemplos few-shot não são suficientes para garantir conformidade rígida em transações críticas de negócio como devolução de dinheiro.",
        "tech_lead_why": "Adicionar uma barreira de pré-requisito (prerequisite gate) no código da aplicação que intercepta a chamada da ferramenta `process_refund` e verifica se os estados necessários (cliente validado, pedido elegível e valor computado) foram previamente populados é um controle determinístico de segurança. Isso garante que, mesmo que o modelo tente pular etapas ou seja induzido pelo usuário a efetuar o reembolso diretamente, a camada de software impeça a execução, forçando o fluxo correto.",
        "tech_lead_wrong": {
            "A": "Adicionar uma barreira de pré-requisito no código é a resposta correta e não a errada.",
            "B": "Fortalecer o prompt de sistema não garante conformidade em 100% dos casos, pois LLMs são modelos probabilísticos e podem sofrer de alucinações ou desvios sob instruções persuasivas de clientes (jailbreaks).",
            "C": "Exemplos few-shot ajudam a guiar o comportamento ideal em cenários comuns, mas não fornecem uma garantia robusta contra cenários novos ou desvios de fluxo em bordas de contexto.",
            "D": "Analisadores de texto baseados em palavras-chave no histórico de chat são extremamente frágeis, propensos a falsos positivos e facilmente burláveis por reformulações de linguagem natural."
        },
        "tech_lead_tip": "Ações críticas e irreversíveis (como transações financeiras ou deleções de dados) no Claude Agent SDK devem sempre ser protegidas por validações de estado determinísticas no backend da aplicação, e não deixadas sob total controle decisório do LLM.",
        "children_exp": "Imagine um porteiro de um clube que tem a regra de só deixar as pessoas entrarem se elas estiverem com o crachá de membro, o exame médico feito e o pagamento em dia. Se o clube apenas pedir para o porteiro lembrar dessas regras de cabeça, uma hora ele pode se distrair e deixar alguém entrar sem pagar.",
        "children_why": "A melhor solução é colocar uma catraca eletrônica na porta que só destrava fisicamente quando lê o crachá, o exame médico e o comprovante de pagamento no sistema. Assim, não importa o quanto a pessoa tente convencer o porteiro, a catraca simplesmente não abre se faltar algo!",
        "children_wrong": {
            "A": "Esta é a catraca física correta.",
            "B": "Apenas dar uma bronca no porteiro para prestar mais atenção (mudar o prompt) não impede que ele se confunda ou seja enganado em dias de muito movimento.",
            "C": "Mostrar desenhos de como as pessoas entram corretamente (few-shot) serve para ensinar, mas ainda permite que alguém passe sem crachá se o porteiro bobear.",
            "D": "Colocar um sistema que só ouve o que as pessoas falam na fila e destrava a porta se elas disserem as palavras \"crachá\" e \"pagamento\" é muito fácil de burlar com mentiras."
        },
        "children_tip": "Para coisas muito importantes, use travas automáticas e eletrônicas em vez de confiar apenas na memória ou na atenção do robô!"
    },
    19: {
        "scenario": "Scenario: Structured Data Extraction You are building a structured data extraction system using Claude. The system extracts information from unstructured documents, validates output using JSON schemas, and maintains high accuracy. It must handle edge cases gracefully and integrate with downstream systems. Production review shows inconsistent routing: documents with unreadable required values and unfamiliar layouts sometimes flow into downstream systems, while routine invoices missing optional purchase-order numbers are sent for manual review. The extraction schema already permits nullable fields for data that is absent from the source. What change would most effectively improve routing decisions?",
        "options": {
            "A": "Require retries until all schema fields are populated, then escalate only documents still containing null values.",
            "B": "Route documents to reviewers whenever the model reports confidence below a single global threshold after extraction.",
            "C": "Escalate documents based on frustrated wording, urgent language, or negative sentiment detected in the source text.",
            "D": "Add explicit human-review criteria with few-shot examples distinguishing absent optional fields, unreadable required fields, and unsupported document types."
        },
        "correct_letter": "D",
        "translated_question": "Você está construindo um sistema de extração de dados estruturados usando o Claude. O sistema extrai informações de documentos não estruturados, valida a saída usando esquemas JSON (JSON schemas) e mantém alta precisão. Ele deve lidar com casos de borda de forma elegante e se integrar a sistemas downstream. A revisão de produção mostra um roteamento inconsistente: documentos com valores obrigatórios ilegíveis e layouts desconhecidos às vezes fluem para sistemas downstream, enquanto faturas rotineiras sem números de pedidos de compra (PO) opcionais são enviadas para revisão manual. O esquema de extração já permite campos nulos para dados ausentes na origem. Qual alteração melhoraria de forma mais eficaz as decisões de roteamento?",
        "translated_options": {
            "A": "Exigir tentativas de reprocessamento até que todos os campos do esquema sejam preenchidos e, em seguida, escalar apenas os documentos que ainda contêm valores nulos.",
            "B": "Rotear documentos para revisores humanos sempre que o modelo relatar confiança abaixo de um único limite global após a extração.",
            "C": "Escalar documentos com base em termos frustrados, linguagem urgente ou sentimento negativo detectado no texto de origem.",
            "D": "Adicionar critérios explícitos de revisão humana com exemplos de poucos disparos (few-shot) distinguindo campos opcionais ausentes, campos obrigatórios ilegíveis e tipos de documentos não suportados."
        },
        "tech_lead_exp": "Em pipelines de processamento de documentos com LLMs, a lógica de roteamento e escalonamento para revisão humana (human-in-the-loop) precisa ser clara e detalhada. O comportamento inconsistente ocorre porque o modelo não sabe diferenciar dados intencionalmente ausentes (campos opcionais nulos legítimos) de erros de extração estruturais ou problemas de legibilidade.",
        "tech_lead_why": "Ao enriquecer a instrução de roteamento com critérios específicos de revisão humana e exemplos few-shot ilustrando a diferença exata entre: 1) campos opcionais legitimamente nulos (como o PO opcional ausente), 2) campos obrigatórios ilegíveis (que exigem escalonamento) e 3) formatos/layouts não suportados, fornecemos ao Claude a lógica operacional correta. Isso aumenta drasticamente a precisão do roteamento, reduzindo tanto falsos positivos quanto falsos negativos.",
        "tech_lead_wrong": {
            "A": "Forçar repetições até que todos os campos estejam preenchidos falhará sistematicamente, pois campos opcionais de fato ausentes na origem nunca serão populados, gerando loops infinitos ou forçando o modelo a alucinar valores inexistentes.",
            "B": "O uso de um único limite de confiança global é ineficaz para classificação de documentos complexos, pois um campo opcional ausente legítimo pode abaixar a confiança média sem representar de fato uma falha de layout ou ilegibilidade.",
            "C": "A análise de sentimentos e tom (linguagem urgente ou frustrada) não tem relevância técnica ou operacional para a classificação de conformidade de documentos transacionais frios, como faturas e notas fiscais.",
            "D": "D é a alternativa correta."
        },
        "tech_lead_tip": "Sempre separe a etapa de extração estruturada de dados da etapa de decisão de roteamento e conformidade (compliance). Tratar a decisão de escalonamento como uma tarefa de classificação dedicada guiada por uma rubrica clara e exemplos few-shot é a melhor prática recomendada para arquiteturas de LLM.",
        "children_exp": "Imagine um robozinho encarregado de separar as cartas que chegam em um escritório. Algumas cartas estão escritas em línguas que ele não conhece ou têm borrões de tinta nas partes importantes (essas ele deve mandar para os humanos). Outras cartas são normais, mas apenas não trazem o telefone de quem enviou (o que é permitido). O robozinho está fazendo confusão e travando o trabalho à toa.",
        "children_why": "Para resolver, precisamos dar a ele um manual ilustrado com exemplos reais de cartas: mostrando a diferença de uma carta borrada (que precisa de ajuda de um humano) e uma carta normal que só não tem o telefone (e que ele pode passar direto). Com exemplos práticos, ele vai separar tudo certinho!",
        "children_wrong": {
            "A": "Mandar o robô tentar ler a carta de novo e de novo até achar um telefone que nunca foi escrito só vai fazê-lo perder tempo e talvez inventar um número falso.",
            "B": "Usar apenas um termômetro de \"certeza geral\" faz o robô ficar com medo e travar cartas perfeitamente boas só porque faltava o campo do telefone.",
            "C": "Procurar se quem escreveu a carta estava com pressa ou bravo não ajuda a saber se o endereço e o valor da conta estão corretos.",
            "D": "D é a alternativa correta."
        },
        "children_tip": "Mostre exemplos claros da diferença entre o que é um erro de verdade e o que é apenas uma informação opcional que está faltando!"
    },
    20: {
        "scenario": "Scenario: Customer Support Resolution Agent You are building a customer support resolution agent using the Claude Agent SDK. The agent handles high-ambiguity requests like returns, billing disputes, and account issues. It has access to backend systems through MCP tools (get_customer, lookup_order, process_refund, escalate_to_human). Your target is 80%+ first-contact resolution while knowing when to escalate. Production traces show that mixed requests such as \"I moved and need to return the charger from order 8831\" alternate unpredictably between get_customer and lookup_order as the first call. In some sessions Claude passes an order number to get_customer; in others it passes a customer name to lookup_order. The current tool catalog exposes only terse autogenerated summaries, and no backend errors are occurring. What change should you make first to improve tool selection reliability?",
        "options": {
            "A": "Add a keyword router that maps phrases like \"order\" or \"refund\" to one tool before Claude sees the request.",
            "B": "Consolidate get_customer and lookup_order into one broad lookup tool that chooses internally which backend records to retrieve.",
            "C": "Update the system prompt to tell Claude to think carefully before selecting tools, without changing schemas or tool metadata.",
            "D": "Rewrite each MCP tool description to specify purpose, accepted identifiers, returned fields, edge cases, and boundaries versus related tools."
        },
        "correct_letter": "D",
        "translated_question": "Você está construindo um agente de resolução de suporte ao cliente usando o Claude Agent SDK. O agente lida com solicitações altamente ambíguas, como devoluções, disputas de faturamento e problemas de conta. Ele tem acesso a sistemas de backend por meio de ferramentas MCP (get_customer, lookup_order, process_refund, escalate_to_human). Sua meta é obter mais de 80% de resolução no primeiro contato, sabendo quando escalar. Os rastros de produção mostram que solicitações mistas como \"Eu mudei e preciso devolver o carregador do pedido 8831\" alternam de forma imprevisível entre get_customer e lookup_order como a primeira chamada. Em algumas sessões, o Claude passa um número de pedido para get_customer; em outras, ele passa o nome de um cliente para lookup_order. O catálogo de ferramentas atual expõe apenas resumos gerados automaticamente muito concisos, e nenhum erro de backend está ocorrendo. Qual alteração você deve fazer primeiro para melhorar a confiabilidade na seleção de ferramentas?",
        "translated_options": {
            "A": "Adicionar um roteador por palavra-chave que mapeia frases como \"pedido\" ou \"reembolso\" para uma ferramenta específica antes que o Claude veja a solicitação.",
            "B": "Consolidar get_customer e lookup_order em uma única ferramenta ampla de busca (lookup tool) que escolhe internamente quais registros de backend recuperar.",
            "C": "Atualizar o prompt do sistema para dizer ao Claude para \"pensar cuidadosamente\" antes de selecionar ferramentas, sem alterar os esquemas ou metadados das ferramentas.",
            "D": "Reescrever a descrição de cada ferramenta MCP para especificar o propósito, identificadores aceitos, campos retornados, casos de borda e limites em relação a ferramentas correlatas."
        },
        "tech_lead_exp": "O Claude decide qual ferramenta chamar e quais parâmetros passar com base exclusivamente nos metadados da ferramenta (esquemas JSON e descrições). Quando as ferramentas MCP possuem descrições concisas ou autogeradas, o modelo carece de contexto técnico e conceitual para discriminar entradas semelhantes (ex: ID de pedido vs ID de cliente).",
        "tech_lead_why": "Reescrever as descrições de ferramentas de forma detalhada e explícita é o método nativo e mais limpo para resolver o problema. Informando no metadado da ferramenta qual é o seu exato escopo, quais tipos de chaves de identificação ela aceita, quais são os retornos esperados e a diferenciação de limites operacionais (ex: \"Use get_customer para buscar informações cadastrais a partir do nome; use lookup_order apenas quando tiver o ID numérico do pedido\"), o Claude alinha a intenção do usuário às ferramentas corretas de forma altamente precisa.",
        "tech_lead_wrong": {
            "A": "Roteadores de palavras-chave rígidos degradam o valor do uso de agentes de IA baseados em LLM, pois falham em compreender a intenção semântica em solicitações complexas ou mistas.",
            "B": "Fundir ferramentas distintas em um único endpoint genérico de \"busca ampla\" sobrecarrega a complexidade lógica do backend da ferramenta, dificulta o controle de segurança granular e desestimula a modularidade do SDK.",
            "C": "Dizer de forma genérica para o modelo \"pensar cuidadosamente\" (sem fornecer informações e fatos novos sobre as ferramentas nos metadados) é inócuo e não adiciona dados úteis que possam guiar a decisão técnica do Claude.",
            "D": "D é a alternativa correta."
        },
        "tech_lead_tip": "Descrições de ferramentas MCP no Claude SDK devem ser tratadas como \"código de prompt\". Elas devem ser ricas, documentar tipos de argumentos aceitos e conter orientações explícitas sobre quando NÃO chamar a ferramenta.",
        "children_exp": "Imagine um faz-tudo que tem em sua caixa de ferramentas dois potes parecidos que só dizem \"Pote A\" e \"Pote B\" nas etiquetas. Às vezes, ele pega pregos no Pote A quando devia pegar parafusos no Pote B, porque as etiquetas são confusas e ele não sabe a diferença.",
        "children_why": "A melhor solução é reescrever as etiquetas dos potes de forma clara: \"Pote A: Apenas para pregos de aço para parede\" e \"Pote B: Apenas para parafusos de madeira com rosca\". Com etiquetas explicando exatamente o que há dentro e para que servem, ele nunca mais vai errar de pote!",
        "children_wrong": {
            "A": "Criar um robozinho que só lê as palavras que o cliente diz e joga o faz-tudo para o pote A ou B é muito travado e falha quando o cliente fala as duas palavras juntas.",
            "B": "Juntar todos os pregos e parafusos em um balde gigante só vai fazer o faz-tudo perder um tempão catando e separando cada um lá dentro toda vez que for trabalhar.",
            "C": "Apenas gritar \"preste atenção!\" para o faz-tudo não ajuda em nada se ele continuar sem saber o que está guardado dentro de cada pote.",
            "D": "D é a alternativa correta."
        },
        "children_tip": "Coloque etiquetas bem explicativas e detalhadas em cada uma das ferramentas do seu robô!"
    },
    21: {
        "scenario": "Scenario: Structured Data Extraction You are building a structured data extraction system using Claude. The system extracts information from unstructured documents, validates output using JSON schemas, and maintains high accuracy. It must handle edge cases gracefully and integrate with downstream systems. Your extraction QA pass reviews Claude's JSON outputs before downstream ingestion. Reviewers dismiss many findings because the QA prompt flags harmless differences: inferred date formats, optional fields absent from the source, and wording variations that do not change extracted values. The current prompt says, \"Check the extraction for accuracy and report any problems.\" What change would most effectively improve precision?",
        "options": {
            "A": "Require the QA pass to flag every schema field that is null, even when the source document omits it.",
            "B": "Rewrite the QA prompt to define reportable errors, acceptable variations, and skip conditions with concrete examples for each category.",
            "C": "Add instructions that Claude should be conservative and report only findings where it feels highly confident.",
            "D": "Increase the validation sample size and ask reviewers to manually ignore findings that are not actionable."
        },
        "correct_letter": "B",
        "translated_question": "Você está construindo um sistema de extração de dados estruturados usando o Claude. O sistema extrai informações de documentos não estruturados, valida a saída usando esquemas JSON e mantém alta precisão. Ele deve lidar com casos de borda de forma elegante e se integrar com sistemas downstream. Sua etapa de controle de qualidade (QA) de extração revisa as saídas JSON do Claude antes da ingestão downstream. Os revisores humanos descartam muitas das ocorrências apontadas porque o prompt de QA sinaliza diferenças inofensivas: formatos de data inferidos, campos opcionais ausentes no documento de origem e variações nas palavras que não alteram os valores extraídos. O prompt atual diz: \"Verifique a precisão da extração e relate quaisquer problemas.\" Qual alteração melhoraria de forma mais eficaz a precisão?",
        "translated_options": {
            "A": "Exigir que a etapa de QA sinalize cada campo do esquema que seja nulo, mesmo quando o documento de origem o omitir.",
            "B": "Reescrever o prompt de QA para definir erros relatáveis, variações aceitáveis e condições de descarte (skip conditions) com exemplos concretos para cada categoria.",
            "C": "Adicionar instruções para que o Claude seja conservador e relate apenas descobertas onde se sinta altamente confiante.",
            "D": "Aumentar o tamanho da amostra de validação e pedir aos revisores para ignorarem manualmente as descobertas que não forem acionáveis."
        },
        "tech_lead_exp": "A precisão de um agente de controle de qualidade (QA) de dados depende da clareza das definições de violação de dados. Prompts vagos como \"relate quaisquer problemas\" levam o modelo a adotar uma postura de super-detecção (flagging indiscriminado), gerando altos índices de falsos positivos com ruídos inofensivos.",
        "tech_lead_why": "Reescrever o prompt de QA para estruturar uma especificação de regras (rubric) detalhada com: 1) o que de fato constitui um erro crítico, 2) variações aceitáveis que devem ser ignoradas (como datas em outros formatos, sinônimos textuais) e 3) condições de pulo (como campos opcionais ausentes), acompanhada de exemplos few-shot claros, eleva a precisão. O modelo aprende exatamente onde traçar a linha entre erros reais e variações normais de formato.",
        "tech_lead_wrong": {
            "A": "Flaggar campos nulos legítimos agravaria o problema original de falsos positivos, adicionando ainda mais alertas sobre campos opcionais legitimamente ausentes.",
            "B": "B é a alternativa correta.",
            "C": "Pedir para o Claude ser \"conservador\" ou \"altamente confiante\" é subjetivo e ineficaz para LLMs, pois não define critérios mensuráveis ou objetivos sobre quais diferenças são aceitáveis.",
            "D": "Aumentar a amostra e transferir o trabalho de filtragem manual para os revisores humanos aumenta o custo operacional e anula o propósito de usar IA para validação de qualidade automática."
        },
        "tech_lead_tip": "Quando agentes gerarem muitos falsos positivos em tarefas de validação, evite prompts qualitativos baseados em confiança. Prefira construir rubricas lógicas de checagem com seções específicas de \"Do's and Dont's\" e exemplos práticos para cada caso.",
        "children_exp": "Imagine um robozinho juiz encarregado de olhar as provas das crianças e apontar os erros. Como a única instrução dele é \"procure qualquer problema\", ele começa a tirar ponto das crianças porque elas escreveram a data com barra em vez de traço, ou porque deixaram uma pergunta opcional em branco. As crianças e os professores estão chateados com o excesso de rigor desnecessário.",
        "children_why": "A solução ideal é dar ao robozinho um gabarito bem explicado: \"1) Se a resposta estiver certa, não importa se usou letra cursiva ou de forma; 2) Não tire pontos por perguntas opcionais não respondidas; 3) Tire pontos se o cálculo matemático estiver errado.\" Dando exemplos de cada caso, ele vai julgar as provas perfeitamente e sem cometer injustiças.",
        "children_wrong": {
            "A": "Mandar tirar pontos de tudo que estiver em branco vai deixar o robozinho ainda mais rígido e chato com as perguntas opcionais.",
            "B": "B é a alternativa correta.",
            "C": "Falar apenas para ele \"tentar ser bonzinho e ter certeza\" não ajuda porque ele não sabe o que o professor considera um erro de verdade.",
            "D": "Fazer o robozinho julgar mais provas e mandar os professores corrigirem os erros do robô na mão é retrabalho e cansa todo mundo."
        },
        "children_tip": "Crie regras bem detalhadas e com exemplos para ensinar seu robô a saber o que é um erro de verdade e o que é só um jeito diferente de escrever!"
    },
    22: {
        "scenario": "Scenario: Developer Productivity with Claude You are building developer productivity tools using the Claude Agent SDK. The agent helps engineers explore unfamiliar codebases, understand legacy systems, generate boilerplate code, and automate repetitive tasks. It uses built-in tools (Read, Write, Bash, Grep, Glob) and integrates with MCP servers. A coordinator agent delegates codebase exploration to subagents before asking an implementation subagent to generate migration scaffolding. In reviews, engineers find the final proposal often mixes findings from different packages, cites helper functions without file locations, and cannot explain which search result or source file supports a recommended change. The individual subagents found useful facts, but their handoffs were free-form summaries. What change would best improve downstream reliability while preserving attribution?",
        "options": {
            "A": "Require subagents to return structured handoff records with findings separated from file paths, symbols, line ranges, commands, and source excerpts.",
            "B": "Ask the implementation subagent to reread the repository broadly and infer supporting locations from each summarized recommendation before editing.",
            "C": "Have each exploration subagent write longer narrative summaries that include reasoning traces and repeated reminders to cite sources.",
            "D": "Strip source details from subagent outputs to reduce context size, then use Grep later when reviewers request justification."
        },
        "correct_letter": "A",
        "translated_question": "Você está construindo ferramentas de produtividade para desenvolvedores usando o Claude Agent SDK. O agente ajuda engenheiros a explorar bases de código desconhecidas, entender sistemas legados, gerar código boilerplate e automatizar tarefas repetitivas. Ele usa ferramentas integradas (Read, Write, Bash, Grep, Glob) e se integra com servidores MCP. Um agente coordenador delega a exploração da base de código a subagentes antes de solicitar a um subagente de implementação que gere a estrutura de migração. Nas revisões, os engenheiros descobrem que a proposta final frequentemente mistura descobertas de pacotes diferentes, cita funções auxiliares (helper functions) sem a localização do arquivo e não consegue explicar qual resultado de busca ou arquivo de origem apoia uma alteração recomendada. Os subagentes individuais encontraram fatos úteis, mas suas transferências (handoffs) de dados foram resumos em texto livre. Qual alteração melhoraria de forma mais eficaz a confiabilidade downstream enquanto preserva a atribuição das fontes?",
        "translated_options": {
            "A": "Exigir que os subagentes retornem registros estruturados de handoff contendo as descobertas separadas dos caminhos de arquivos, símbolos, intervalos de linhas, comandos e trechos de código-fonte.",
            "B": "Solicitar ao subagente de implementação que leia novamente o repositório de forma ampla e infira as localizações de suporte para cada recomendação resumida antes de editar.",
            "C": "Fazer com que cada subagente de exploração escreva resumos narrativos mais longos que incluam caminhos de raciocínio e lembretes repetidos para citar fontes.",
            "D": "Remover os detalhes de origem das saídas dos subagentes para reduzir o tamanho do contexto e, em seguida, usar o Grep mais tarde quando os revisores solicitarem justificativas."
        },
        "tech_lead_exp": "Em arquiteturas multi-agentes baseadas no Claude Agent SDK, a perda de dados contextuais e atribuição é um problema clássico de handoffs não estruturados. Passar resumos em texto livre força o agente downstream a usar sua janela de contexto para processar e inferir detalhes, corrompendo a precisão das referências de arquivos e símbolos.",
        "tech_lead_why": "Implementar um protocolo de handoff com um esquema estrito de dados estruturados (por exemplo, um objeto contendo campos específicos para `descoberta`, `caminho_do_arquivo`, `modulo`, `linhas_afetadas` e `comando_de_busca`) remove a ambiguidade. O agente de implementação downstream recebe uma tabela exata e estruturada de fatos, o que elimina a mistura de escopo entre pacotes e garante rastreabilidade e atribuição perfeitas para as sugestões de código apresentadas ao engenheiro.",
        "tech_lead_wrong": {
            "A": "A é a alternativa correta.",
            "B": "Mandar o agente downstream reler o repositório inteiro para adivinhar a origem dos resumos é ineficiente em termos de tokens de entrada e tempo de processamento, além de introduzir alto risco de novas alucinações de arquivos.",
            "C": "Resumos narrativos mais longos poluem a janela de contexto com redundâncias em linguagem natural e continuam exigindo que o agente downstream interprete texto corrido para extrair metadados, o que mantém a taxa de erros alta.",
            "D": "Remover metadados e forçar o uso tardio de Grep sob demanda desestrutura a automação, transferindo a tarefa de busca para o tempo de compilação ou exigindo iterações manuais desnecessárias por parte dos engenheiros revisores."
        },
        "tech_lead_tip": "Ao projetar fluxos multi-agente, as transferências de tarefas (handoffs) nunca devem ser puramente textuais. Defina payloads de dados estruturados (usando JSON schemas rígidos no SDK do Claude) para carregar os artefatos de conhecimento gerados por cada subagente.",
        "children_exp": "Imagine um grupo de detetives robôs. O primeiro grupo investiga a cidade e anota as pistas num papel de rascunho bagunçado, escrevendo coisas soltas como: \"achamos uma chave azul\". O robô que precisa abrir as portas fica perdido porque não sabe em qual gaveta ou em qual rua aquela chave azul foi achada.",
        "children_why": "A melhor solução é dar aos detetives uma ficha de relatório impressa e dividida em caixinhas específicas: \"Pista\", \"Rua\", \"Casa\", \"Número da Gaveta\". Preenchendo essa ficha certinho, o robô chaveiro consegue ir direto ao ponto sem misturar as pistas e sem perder tempo!",
        "children_wrong": {
            "A": "A é a alternativa correta.",
            "B": "Mandar o robô chaveiro procurar na cidade toda de novo toda vez que receber um papel confuso é um trabalho dobrado e cansativo.",
            "C": "Pedir aos detetives para escreverem histórias mais longas no rascunho só vai acumular papéis cheios de blá-blá-blá sem organizar as pistas de verdade.",
            "D": "Jogar fora todas as dicas de onde as chaves foram vistas e usar um cão farejador depois só quando alguém pedir provas é bagunçado e ineficiente."
        },
        "children_tip": "Em vez de passar bilhetes bagunçados entre seus robôs, faça com que eles preencham fichas organizadas com campos bem definidos!"
    },
    23: {
        "scenario": "Scenario: Multi-Agent Research System You are building a multi-agent research system using the Claude Agent SDK. A coordinator agent delegates to specialized subagents: one searches the web, one analyzes documents, one synthesizes findings, and one generates reports. The system researches topics and produces comprehensive, cited reports. During testing, the document analysis subagent receives coordinator-selected PDFs and reports from an approved catalog, but it has a generic URL retrieval tool. It sometimes follows links inside documents to blogs, login pages, or duplicate HTML summaries, then cites those pages instead of the approved sources. You need reduce these citation and scope errors while preserving access to approved source material. What change best addresses this?",
        "options": {
            "A": "Replace fetch_url with a load_document tool that accepts catalog document IDs or approved URLs and validates before fetching.",
            "B": "Keep fetch_url available, but add prompt instructions warning the subagent never to open links found inside documents.",
            "C": "Give the document analysis subagent web search tools too, so it can independently confirm whether linked pages are relevant.",
            "D": "Allow fetch_url for any link, then have synthesis discard citations whose domains are not in the approved catalog."
        },
        "correct_letter": "A",
        "translated_question": "Você está construindo um sistema de pesquisa multi-agente usando o Claude Agent SDK. Um agente coordenador delega tarefas a subagentes especializados: um pesquisa na web, um analisa documentos, um sintetiza descobertas e outro gera relatórios. O sistema pesquisa tópicos e produz relatórios abrangentes com citações. Durante os testes, o subagente de análise de documentos recebe PDFs e relatórios selecionados pelo coordenador a partir de um catálogo aprovado, mas possui uma ferramenta genérica de recuperação de URL (fetch_url). Às vezes, ele segue links dentro dos documentos que levam a blogs, páginas de login ou resumos HTML duplicados, citando essas páginas em vez das fontes aprovadas. Você precisa reduzir esses erros de citação e escopo, mantendo o acesso ao material de origem aprovado. Qual alteração resolve melhor esse problema?",
        "translated_options": {
            "A": "Substituir fetch_url por uma ferramenta load_document que aceita IDs de documentos do catálogo ou URLs aprovadas e realiza validação antes de buscar.",
            "B": "Manter o fetch_url disponível, mas adicionar instruções de prompt alertando o subagente para nunca abrir links encontrados dentro dos documentos.",
            "C": "Dar ao subagente de análise de documentos ferramentas de busca na web também, para que ele possa confirmar de forma independente se as páginas vinculadas são relevantes.",
            "D": "Permitir fetch_url para qualquer link e, em seguida, fazer com que a etapa de síntese descarte citações cujos domínios não estejam no catálogo aprovado."
        },
        "tech_lead_exp": "Esta questão aborda o princípio do menor privilégio e o controle de fronteiras de ferramentas (tool scoping) em sistemas de múltiplos agentes. Quando um agente recebe uma ferramenta ampla e genérica como `fetch_url`, ele ganha a capacidade física de escapar do escopo do domínio de dados aprovado, resultando em desvios e erros de citação (hallucinations/attribution drift).",
        "tech_lead_why": "Substituir a ferramenta genérica `fetch_url` por uma ferramenta especializada `load_document` com validação de entrada estrita na camada de aplicação (backend) assegura que o agente fisicamente não consiga fazer requisições a links de terceiros ou páginas não catalogadas. Isso impõe uma restrição de segurança rígida baseada em software, forçando o agente a se limitar apenas a IDs cadastrados ou URLs validadas na whitelist.",
        "tech_lead_wrong": {
            "A": "A é a alternativa correta.",
            "B": "Adicionar avisos em linguagem natural no prompt para o agente não clicar em links internos não é um método seguro, pois o modelo pode ignorar a instrução (prompt drift) sob a influência de textos persuasivos no documento.",
            "C": "Dar ferramentas de busca na web ao subagente de análise de documentos aumenta sua capacidade e complexidade, ampliando ainda mais o risco de vazamento de escopo e uso de fontes não autorizadas.",
            "D": "Permitir o download irrestrito e filtrar as citações na etapa final de síntese consome tempo e recursos de processamento desnecessários, além de forçar a etapa de síntese a lidar com contradições ou informações distorcidas obtidas de páginas inválidas."
        },
        "tech_lead_tip": "Sempre imponha restrições de escopo e segurança diretamente na assinatura e validação física das ferramentas (código), em vez de depender puramente de restrições qualitativas escritas nos prompts do sistema de IA.",
        "children_exp": "Imagine um robozinho ajudante de biblioteca que deve ler apenas os livros que estão em uma prateleira especial aprovada. Mas, para buscar as informações, ele tem uma chave mágica universal (ferramenta fetch_url) que abre qualquer porta do mundo inteiro. Às vezes ele vê uma indicação de site em um livro e vai parar na cozinha ou em blogs estranhos na internet, trazendo receitas de bolo em vez de fatos históricos.",
        "children_why": "A melhor solução é trocar a chave universal por um cartão eletrônico da biblioteca que só abre as portas daquela prateleira aprovada de livros. Se o robozinho tentar passar por outra porta, o cartão simplesmente não funciona. Assim, ele fica focado no trabalho sem ir a lugares errados!",
        "children_wrong": {
            "A": "A é a alternativa correta.",
            "B": "Apenas colocar um cartaz dizendo \"por favor, não use a chave universal nas portas da rua\" não garante nada, pois uma hora ele pode ler algo empolgante e abrir a porta errada sem querer.",
            "C": "Dar mais chaves mágicas (como chaves de carros) para ele investigar a internet só vai fazê-lo se perder ainda mais longe da biblioteca.",
            "D": "Deixar ele buscar qualquer coisa de qualquer lugar e depois contratar um robô supervisor para jogar as informações ruins no lixo é desperdício de energia e trabalho à toa."
        },
        "children_tip": "Nunca dê chaves universais para seus robôs se você quer que eles permaneçam trabalhando no mesmo cômodo seguro!"
    },
    24: {
        "scenario": "Scenario: Developer Productivity with Claude You are building developer productivity tools using the Claude Agent SDK. The agent helps engineers explore unfamiliar codebases, understand legacy systems, generate boilerplate code, and automate repetitive tasks. It uses built-in tools (Read, Write, Bash, Grep, Glob) and integrates with MCP servers. A senior engineer reports that Claude Code consistently follows your team's codebase exploration notes, legacy module warnings, and boilerplate conventions. New engineers who clone the repository see generic behavior instead, and no repository files changed when the senior engineer originally added those notes. What is the most effective way to make this guidance consistent for the team?",
        "options": {
            "A": "Paste the conventions into the first prompt of each new session instead of changing repository configuration files.",
            "B": "Create a slash command that reminds Claude to apply the conventions whenever developers remember to invoke it.",
            "C": "Move the shared conventions into a project-level CLAUDE.md file and commit it so every clone loads them.",
            "D": "Ask each developer to copy the senior engineer’s personal memory file into their home directory before using Claude Code."
        },
        "correct_letter": "C",
        "translated_question": "Você está construindo ferramentas de produtividade para desenvolvedores usando o Claude Agent SDK. O agente ajuda engenheiros a explorar bases de código desconhecidas, entender sistemas legados, gerar código boilerplate e automatizar tarefas repetitivas. Ele usa ferramentas integradas (Read, Write, Bash, Grep, Glob) e se integra com servidores MCP. Um engenheiro sênior relata que o Claude Code segue consistentemente as notas de exploração da base de código da sua equipe, os avisos de módulos legados e as convenções de boilerplate. No entanto, novos engenheiros que clonam o repositório experimentam um comportamento genérico do agente, e nenhum arquivo do repositório foi alterado quando o engenheiro sênior adicionou originalmente aquelas notas. Qual é a maneira mais eficaz de tornar essas orientações consistentes para toda a equipe?",
        "translated_options": {
            "A": "Colar as convenções no primeiro prompt de cada nova sessão, em vez de alterar os arquivos de configuração do repositório.",
            "B": "Criar um comando barra (slash command) que lembre o Claude de aplicar as convenções sempre que os desenvolvedores se lembrarem de invocá-lo.",
            "C": "Mover as convenções compartilhadas para um arquivo CLAUDE.md no nível do projeto e comitá-lo para que cada clone o carregue automaticamente.",
            "D": "Solicitar que cada desenvolvedor copie o arquivo de memória pessoal do engenheiro sênior para seu diretório home antes de usar o Claude Code."
        },
        "tech_lead_exp": "O Claude Code possui um recurso nativo de escopo de projeto que detecta e lê automaticamente o arquivo `CLAUDE.md` localizado no diretório raiz do projeto. Esse arquivo é projetado para conter instruções gerais do repositório, padrões de design, comandos frequentes de build/teste e políticas de codificação específicas.",
        "tech_lead_why": "Mover as convenções de codificação e notas para o arquivo `CLAUDE.md` na raiz do repositório e adicioná-lo ao sistema de controle de versão (Git) é a melhor prática recomendada. Isso garante que qualquer desenvolvedor que clone o repositório tenha acesso imediato e transparente a essas regras locais, que serão carregadas de forma transparente pelo Claude Code a cada inicialização da sessão, mantendo a consistência do time de engenharia.",
        "tech_lead_wrong": {
            "A": "Copiar e colar instruções em cada prompt é um processo manual ineficiente, propenso a esquecimentos e que polui o histórico inicial da conversa de forma desnecessária.",
            "B": "Depender de que cada programador se lembre de digitar um comando barra específico para carregar as regras gera falhas constantes de conformidade no fluxo de trabalho diário.",
            "C": "C é a alternativa correta.",
            "D": "Compartilhar arquivos de memória locais localizados no diretório home (`~/.claude_profile` ou similar) exige intervenções manuais na máquina do usuário, dificulta a automação de novas regras e quebra a portabilidade do repositório."
        },
        "tech_lead_tip": "O arquivo `CLAUDE.md` é a forma canônica de injetar contexto sistêmico de repositório no Claude Code. Mantenha-o curto, focado em comandos reais (Build, Test, Lint) e diretrizes críticas de design que o Claude precise seguir.",
        "children_exp": "Imagine que um engenheiro chefe ensinou seu assistente robô pessoal a arrumar a oficina de um jeito especial que ele gosta. Mas os novos ajudantes humanos que chegam à oficina usam robôs novos que não aprenderam essas regras e arrumam tudo do jeito padrão e confuso.",
        "children_why": "A melhor solução é escrever o manual de arrumação em um papel oficial do projeto chamado `CLAUDE.md` e deixá-lo fixado no quadro de avisos da oficina. Dessa forma, qualquer robô novo que entrar ali vai ler o quadro imediatamente e saberá exatamente como arrumar as coisas de forma igual!",
        "children_wrong": {
            "A": "Ficar colando adesivos com as regras na testa dos robôs todas as manhãs dá muito trabalho e os adesivos caem com facilidade.",
            "B": "Criar um botão de emergência que os ajudantes precisam apertar toda hora para o robô lembrar das regras falha porque os humanos vivem esquecendo de apertar.",
            "C": "C é a alternativa correta.",
            "D": "Tentar copiar o cérebro eletrônico do robô do sênior para as contas particulares de cada novato é muito difícil e bagunça os dados pessoais de cada um."
        },
        "children_tip": "Sempre guarde as regras do robô em um arquivo compartilhado dentro da própria pasta do projeto para que todos os robôs a usem automaticamente!"
    },
    25: {
        "scenario": "Scenario: Customer Support Resolution Agent You are building a customer support resolution agent using the Claude Agent SDK. The agent handles high-ambiguity requests like returns, billing disputes, and account issues. It has access to backend systems through MCP tools (get_customer, lookup_order, process_refund, escalate_to_human). Your target is 80%+ first-contact resolution while knowing when to escalate. During development, you resume yesterday's named investigation session about refund errors. In that session, Claude had read refund_policy.md, the process_refund tool schema, and escalation_rules.md, and most of its analysis is still relevant. Since then, a teammate changed the refund threshold rules and updated process_refund parameter names. You need Claude to continue designing the fix without repeating the whole investigation or relying on stale assumptions. What is the best next step?",
        "options": {
            "A": "Resume the session normally and rely on Claude to infer changed assumptions from the prior conversation history during implementation.",
            "B": "Resume the session, identify the changed policy and tool files, and request targeted re-analysis before continuing implementation decisions.",
            "C": "Fork the old session into competing branches and let each branch decide whether prior tool results remain trustworthy.",
            "D": "Start a fresh session and require complete codebase re-exploration whenever any previously analyzed file has changed."
        },
        "correct_letter": "B",
        "translated_question": "Você está construindo um agente de resolução de suporte ao cliente usando o Claude Agent SDK. O agente lida com solicitações altamente ambíguas, como devoluções, disputas de faturamento e problemas de conta. Ele tem acesso a sistemas de backend por meio de ferramentas MCP (get_customer, lookup_order, process_refund, escalate_to_human). Sua meta é obter mais de 80% de resolução no primeiro contato, sabendo quando escalar. Durante o desenvolvimento, você retoma a sessão de investigação nomeada de ontem sobre erros de reembolso. Nessa sessão, o Claude havia lido o refund_policy.md, o esquema da ferramenta process_refund e o escalation_rules.md, e a maior parte de sua análise ainda é relevante. Desde então, um colega de equipe alterou as regras de limite de reembolso e atualizou os nomes dos parâmetros de process_refund. Você precisa que o Claude continue projetando a correção sem repetir toda a investigação ou confiar em premissas desatualizadas. Qual é o melhor próximo passo?",
        "translated_options": {
            "A": "Retomar a sessão normalmente e confiar que o Claude infira as premissas alteradas a partir do histórico de conversas anterior durante a implementação.",
            "B": "Retomar a sessão, identificar os arquivos de política e de ferramentas que foram alterados e solicitar uma reanálise direcionada antes de continuar com as decisões de implementação.",
            "C": "Bifurcar (fork) a sessão antiga em ramificações concorrentes e deixar que cada ramificação decida se os resultados das ferramentas anteriores continuam confiáveis.",
            "D": "Iniciar uma nova sessão limpa e exigir uma reexploração completa da base de código sempre que qualquer arquivo analisado anteriormente for alterado."
        },
        "tech_lead_exp": "Esta questão trata da manutenção do estado e do contexto de raciocínio de agentes conversacionais de longa duração. LLMs que utilizam dados cacheados ou históricos de chat contínuos não possuem conhecimento de modificações externas no ecossistema (arquivos e schemas de APIs) ocorridas entre as execuções, a menos que sejam explicitamente solicitados a reler os recursos atualizados.",
        "tech_lead_why": "Retomar a sessão ativa e orientar o agente a realizar uma reanálise direcionada (targeted re-analysis) apenas nos arquivos modificados (como `refund_policy.md` e a nova assinatura do `process_refund`) é a melhor escolha. Esse padrão garante a eficiência de tokens, pois preserva as conclusões lógicas da investigação inicial mantidas no histórico, ao mesmo tempo em que substitui os dados desatualizados (stale data) no contexto do modelo com as novas regras e parâmetros.",
        "tech_lead_wrong": {
            "A": "O Claude não pode inferir alterações externas feitas no código físico a partir de um histórico de chat antigo gravado ontem, o que resultará na geração de código com parâmetros errados ou limites defasados.",
            "B": "B é a alternativa correta.",
            "C": "Bifurcar a sessão em múltiplos ramos de avaliação lógica é desnecessariamente complexo para a situação e não resolve a falta de leitura física das novas atualizações de arquivos.",
            "D": "Começar uma sessão totalmente do zero toda vez que qualquer arquivo pequeno sofre modificação gera enorme desperdício de tokens de contexto, tempo de engenharia e destrói o progresso cognitivo e estrutural já alcançado pelo agente na véspera."
        },
        "tech_lead_tip": "Em fluxos de desenvolvimento interativos com Claude, sempre forneça instruções explícitas quando as dependências de arquivos mudarem. Use comandos como \"Por favor, leia novamente [arquivo] para sincronizar com as últimas modificações de código\" para evitar desalinhamento de contexto.",
        "children_exp": "Imagine que você está jogando um jogo de tabuleiro com um amigo e o jogo foi pausado ontem. Durante a noite, o fabricante mudou duas regras do jogo e alterou o nome de algumas cartas. Se você continuar jogando hoje do mesmo jeito de ontem, vocês vão acabar jogando errado e brigando.",
        "children_why": "O melhor a fazer é continuar o jogo de onde parou, mas primeiro abrir o folheto de regras e mostrar para o seu amigo exatamente quais regras mudaram. Assim, vocês continuam a partida sem ter que começar o jogo inteiro do zero!",
        "children_wrong": {
            "A": "Apenas continuar jogando e esperar que seu amigo adivinhe as novas regras por telepatia vai fazer o jogo dar errado na primeira jogada.",
            "B": "B é a alternativa correta.",
            "C": "Dividir a mesa em dois tabuleiros diferentes para ver qual regra é mais bonita só vai bagunçar a cabeça dos jogadores e não resolve a partida.",
            "D": "Guardar o tabuleiro, jogar todas as peças na caixa e começar o jogo inteiro do início só porque mudaram duas regrinhas secundárias é cansativo e demorado demais."
        },
        "children_tip": "Quando o código ou as regras do seu projeto mudarem no meio do caminho, avise seu robô e peça para ele ler apenas a parte atualizada para não perder tempo!"
    },
    26: {
        "scenario": "Scenario: Developer Productivity with Claude You are building developer productivity tools using the Claude Agent SDK. The agent helps engineers explore unfamiliar codebases, understand legacy systems, generate boilerplate code, and automate repetitive tasks. It uses built-in tools (Read, Write, Bash, Grep, Glob) and integrates with MCP servers. Your internal agent is generating repository-specific data adapter classes from interface definitions. In pilots, the first drafts compile, but later reviews find unhandled null fields, incorrect retry behavior, and slow processing on large fixtures. Engineers can state expected outcomes and edge cases before implementation, but prose-only instructions have produced uneven results. Which workflow should you add?",
        "options": {
            "A": "Create tests for expected behavior, edge cases, and performance constraints first, then iterate by sending Claude failing results.",
            "B": "Let Claude implement the adapter, then rely on manual code review to catch missed cases after generation.",
            "C": "Run the generated code once on a representative happy-path input, then approve if the output matches.",
            "D": "Give Claude a longer prose specification and ask it to reason carefully before producing the complete implementation."
        },
        "correct_letter": "A",
        "translated_question": "Você está construindo ferramentas de produtividade para desenvolvedores usando o Claude Agent SDK. O agente ajuda engenheiros a explorar bases de código desconhecidas, entender sistemas legados, gerar código boilerplate e automatizar tarefas repetitivas. Ele usa ferramentas integradas (Read, Write, Bash, Grep, Glob) e se integra com servidores MCP. Seu agente interno está gerando classes adaptadoras de dados específicas do repositório a partir de definições de interface. Nos projetos piloto, os primeiros rascunhos compilam, mas as revisões posteriores revelam campos nulos não tratados, comportamento incorreto de retentativa (retry) e processamento lento em grandes volumes de dados. Os engenheiros conseguem definir os resultados esperados e casos de borda antes da implementação, mas instruções puramente em prosa (texto livre) produziram resultados irregulares. Qual fluxo de trabalho você deve adicionar?",
        "translated_options": {
            "A": "Criar primeiro testes para o comportamento esperado, casos de borda e restrições de desempenho e, em seguida, iterar enviando ao Claude os resultados com falha.",
            "B": "Deixar que o Claude implemente o adaptador e, em seguida, confiar na revisão manual de código para capturar casos perdidos após a geração.",
            "C": "Executar o código gerado uma vez com uma entrada representativa do caminho feliz (happy-path) e aprovar se a saída corresponder.",
            "D": "Fornecer ao Claude uma especificação em prosa mais longa e pedir que ele raciocine cuidadosamente antes de produzir a implementação completa."
        },
        "tech_lead_exp": "Esta questão aborda o padrão de Test-Driven Development (TDD) aplicado a agentes de engenharia de software (coding agents). Instruções descritivas em linguagem natural são propensas a interpretações ambíguas e falham em cobrir todos os fluxos excepcionais (null-pointers, timeouts, bottlenecks).",
        "tech_lead_why": "Ao criar os testes unitários e de desempenho antes da escrita do código, estabelecemos um validador determinístico e automatizado para o comportamento do agente. Quando o Claude recebe o feedback de falhas estruturadas dos testes (como traces de stack, asserções não atendidas e tempos de execução excedidos), ele consegue corrigir seu código iterativamente até passar na suite de testes, alcançando um alto índice de robustez sem necessidade de intervenção humana constante.",
        "tech_lead_wrong": {
            "A": "A é a alternativa correta.",
            "B": "Confiar na revisão manual de código pelo desenvolvedor humano após a geração joga a carga de trabalho de validação sobre o time de engenharia, anulando os ganhos de produtividade e permitindo que erros sutis cheguem à produção.",
            "C": "Validar apenas o caminho feliz (happy-path) uma vez mascara erros graves que ocorrem apenas em casos de borda (como dados nulos) ou sob carga elevada (como gargalos de performance).",
            "D": "Aumentar as instruções em linguagem natural (prosa longa) apenas amplia o tamanho da janela de contexto e a ambiguidade, sem fornecer ao agente um mecanismo prático e executável de verificação e correção."
        },
        "tech_lead_tip": "Sempre estruture o fluxo do agente de programação em loops fechados de \"Geração -> Execução de Testes -> Correção de Código\". O sinal de erro retornado pelos testes é a melhor fonte de contexto para o Claude se autocorrigir com sucesso.",
        "children_exp": "Imagine que você pede para um robô marceneiro fazer uma cadeira de madeira nova. Se você apenas descrever em um texto longo como quer a cadeira, ele pode errar a altura ou fazer pés fracos que quebram quando alguém pesado sentar.",
        "children_why": "A melhor solução é construir primeiro uma máquina de testes automática que aperta e empurra os pés da cadeira para ver se balança e coloca um peso nela. Você manda o robô fazer a cadeira e a coloca na máquina de teste; se a máquina disser que falhou, o robô ajusta e reforça a madeira até que a cadeira passe nos testes. Assim, a cadeira final será perfeita e segura!",
        "children_wrong": {
            "A": "A é a alternativa correta.",
            "B": "Deixar o robô fazer a cadeira e depois você sentar nela na pressa para descobrir se está quebrando é perigoso e dá muito trabalho de consertar depois.",
            "C": "Apenas colocar um boneco leve de papel na cadeira uma única vez não garante que ela vá aguentar o peso de uma pessoa de verdade depois.",
            "D": "Escrever um bilhete gigante e complicado implorando para o robô prestar atenção não ajuda, pois ele não consegue testar a força da madeira só lendo palavras."
        },
        "children_tip": "Antes de mandar seu robô programar, crie testes automáticos para que ele possa descobrir sozinho o que está errado e consertar sem você precisar intervir!"
    },
    27: {
        "scenario": "Scenario: Structured Data Extraction You are building a structured data extraction system using Claude. The system extracts information from unstructured documents, validates output using JSON schemas, and maintains high accuracy. It must handle edge cases gracefully and integrate with downstream systems. Your invoice extraction pipeline already returns syntactically valid structured objects, but semantic validators reject about 7% of documents because line-item totals do not sum to the stated total or normalized dates fail business rules. Most rejected documents contain the needed values, but the model placed or formatted them incorrectly. What should you change to recover these cases while preserving validation rigor?",
        "options": {
            "A": "Loosen the JSON schema by making rejected fields nullable, then route missing values to downstream reconciliation jobs.",
            "B": "Retry the original extraction prompt up to three times, accepting the first response that passes schema validation.",
            "C": "Ask Claude to explain likely extraction mistakes in natural language, then parse that explanation to update records.",
            "D": "Send a follow-up request containing the source document, failed extraction, and precise validator messages for targeted correction."
        },
        "correct_letter": "D",
        "translated_question": "Você está construindo um sistema de extração de dados estruturados usando o Claude. O sistema extrai informações de documentos não estruturados, valida a saída usando esquemas JSON e mantém alta precisão. Ele deve lidar com casos de borda de forma elegante e se integrar com sistemas downstream. Seu pipeline de extração de faturas já retorna objetos estruturados sintaticamente válidos, mas os validadores semânticos rejeitam cerca de 7% dos documentos porque a soma dos itens de linha não corresponde ao total declarado ou as datas normalizadas violam regras de negócios. A maioria dos documentos rejeitados contém os valores necessários, mas o modelo os posicionou ou formatou incorretamente. O que você deve alterar para recuperar esses casos mantendo o rigor da validação?",
        "translated_options": {
            "A": "Afrouxar o esquema JSON tornando os campos rejeitados anuláveis e, em seguida, rotear os valores ausentes para tarefas de reconciliação downstream.",
            "B": "Tentar novamente o prompt de extração original até três vezes, aceitando a primeira resposta que passar na validação do esquema.",
            "C": "Pedir ao Claude para explicar os erros de extração prováveis em linguagem natural e, em seguida, analisar essa explicação para atualizar os registros.",
            "D": "Enviar uma solicitação de acompanhamento (follow-up) contendo o documento de origem, a extração que falhou e as mensagens de erro precisas do validador para uma correção direcionada."
        },
        "tech_lead_exp": "Erros de consistência semântica e formatação fina (como somatório de notas fiscais ou validações lógicas de datas) são desafiadores para LLMs em passadas únicas (\"zero-shot\"). No entanto, quando os erros são detectados por validadores locais (código), podemos usá-los como um sinal de feedback de correção (self-correction loops).",
        "tech_lead_why": "Implementar um fluxo de correção direcionado que envia ao Claude: 1) o documento original, 2) o JSON inválido que ele mesmo gerou e 3) o log do erro emitido pelo validador semântico (ex: \"Erro: A soma dos itens [10.00, 20.00] é 30.00, mas o total extraído foi 40.00\") permite que o Claude foque exclusivamente na resolução da inconsistência. Esse feedback em loop fechado recupera quase a totalidade dos 7% de falhas, sem abrir mão das regras rígidas de validação do sistema.",
        "tech_lead_wrong": {
            "A": "Afrouxar as regras do esquema JSON reduz a qualidade dos dados na origem, transfere o problema de inconsistência para sistemas secundários e eleva os custos e erros nos processos de reconciliação downstream.",
            "B": "Repetir cegamente a mesma consulta original até três vezes sem fornecer o feedback de erro do validador é ineficiente e propenso a falhas, pois o modelo tenderá a reproduzir as mesmas decisões lógicas e os mesmos erros sistemáticos de posicionamento.",
            "C": "Pedir justificativas em linguagem natural e tentar construir analisadores secundários de texto para atualizar os registros é uma abordagem complexa, frágil e que introduz novos pontos de falha na interpretação das correções.",
            "D": "D é a alternativa correta."
        },
        "tech_lead_tip": "Não confie em passadas únicas para extrações complexas que exijam cálculos matemáticos ou restrições de tempo rígidas. Sempre valide os resultados programmaticamente no backend e forneça o trace do erro de volta ao modelo para correção interativa.",
        "children_exp": "Imagine que você deu para o robô da escola uma lista de compras de supermercado com vários doces e pediu para ele somar todos os valores para ver se bate com o total do recibo. O robô faz a conta de cabeça rápido e erra por alguns centavos, embora tenha anotado todos os doces certos.",
        "children_why": "A melhor solução é mostrar o papel com a conta errada dele, apontar o lápis para o erro e falar: \"Robô, você somou 10 com 20 e deu 40, mas o certo é 30. Corrija apenas essa soma olhando a lista novamente\". O robô vai olhar, perceber a falha e corrigir o erro num segundo!",
        "children_wrong": {
            "A": "Aceitar a conta errada com valores faltando e mandar a conta incompleta para a mamãe corrigir depois na mão só vai dar mais trabalho para ela.",
            "B": "Apenas gritar \"faça a conta de novo!\" do zero sem falar para ele onde ele errou provavelmente vai fazer o robô cometer o mesmo erro de soma outra vez.",
            "C": "Pedir para o robô explicar por escrito em linguagem natural o motivo de ter errado na matemática só gasta tempo e não ajuda a consertar o número final no papel.",
            "D": "D é a alternativa correta."
        },
        "children_tip": "Quando o robô errar um cálculo, aponte exatamente o local do erro e dê o resultado errado de volta para que ele possa se corrigir rapidamente!"
    }
}

template_simple = """{scenario}

---

[ ] A - {opt_A}
[ ] B - {opt_B}
[ ] C - {opt_C}
[ ] D - {opt_D}"""

template_enriched = """{scenario}

---

[ ] A - {opt_A}
[ ] B - {opt_B}
[ ] C - {opt_C}
[ ] D - {opt_D}

---

### TRANSLATED QUESTION
{translated_question}
Alternativas traduzidas:

A) {trans_opt_A}
B) {trans_opt_B}
C) {trans_opt_C}
D) {trans_opt_D}

---

### EXPLANATION (TECH LEAD)

Explicação:
{tech_lead_exp}

Por que a alternativa {correct_letter} é a correta:
{tech_lead_why}

Por que as outras estão erradas:

A) {tech_lead_wrong_A}
B) {tech_lead_wrong_B}
C) {tech_lead_wrong_C}
D) {tech_lead_wrong_D}

Dica importante:
{tech_lead_tip}

---

### 🚸 CHILDREN EXPLANATION

Explicação:
{children_exp}

Por que a alternativa {correct_letter} é a correta:
{children_why}

Por que as outras estão erradas:

A) {children_wrong_A}
B) {children_wrong_B}
C) {children_wrong_C}
D) {children_wrong_D}

Dica importante:
{children_tip}

---

### CORRECT ANSWER

[ ] {correct_letter} - {correct_text}"""

for num, data in cards_data.items():
    num_str = str(num).zfill(3)
    
    # 1. Write simple card
    simple_content = template_simple.format(
        scenario=data["scenario"],
        opt_A=data["options"]["A"],
        opt_B=data["options"]["B"],
        opt_C=data["options"]["C"],
        opt_D=data["options"]["D"]
    )
    
    simple_file = output_dir / f"{num_str}-card.md"
    simple_file.write_text(simple_content, encoding="utf-8")
    print(f"Created {simple_file.name}")
    
    # 2. Write enriched card
    correct_letter = data["correct_letter"]
    correct_text = data["options"][correct_letter]
    
    # Define tech lead and children wrongs
    tlw = data["tech_lead_wrong"]
    chw = data["children_wrong"]
    
    # Fill in the blanks if correct option isn't in wrongs
    tlw_A = tlw.get("A", "Esta é a alternativa correta.")
    tlw_B = tlw.get("B", "Esta é a alternativa correta.")
    tlw_C = tlw.get("C", "Esta é a alternativa correta.")
    tlw_D = tlw.get("D", "Esta é a alternativa correta.")
    
    chw_A = chw.get("A", "Esta é a alternativa correta na analogia.")
    chw_B = chw.get("B", "Esta é a alternativa correta na analogia.")
    chw_C = chw.get("C", "Esta é a alternativa correta na analogia.")
    chw_D = chw.get("D", "Esta é a alternativa correta na analogia.")
    
    enriched_content = template_enriched.format(
        scenario=data["scenario"],
        opt_A=data["options"]["A"],
        opt_B=data["options"]["B"],
        opt_C=data["options"]["C"],
        opt_D=data["options"]["D"],
        translated_question=data["translated_question"],
        trans_opt_A=data["translated_options"]["A"],
        trans_opt_B=data["translated_options"]["B"],
        trans_opt_C=data["translated_options"]["C"],
        trans_opt_D=data["translated_options"]["D"],
        correct_letter=correct_letter,
        tech_lead_exp=data["tech_lead_exp"],
        tech_lead_why=data["tech_lead_why"],
        tech_lead_wrong_A=tlw_A,
        tech_lead_wrong_B=tlw_B,
        tech_lead_wrong_C=tlw_C,
        tech_lead_wrong_D=tlw_D,
        tech_lead_tip=data["tech_lead_tip"],
        children_exp=data["children_exp"],
        children_why=data["children_why"],
        children_wrong_A=chw_A,
        children_wrong_B=chw_B,
        children_wrong_C=chw_C,
        children_wrong_D=chw_D,
        children_tip=data["children_tip"],
        correct_text=correct_text
    )
    
    enriched_file = output_dir / f"{num_str}-enriched-card.md"
    enriched_file.write_text(enriched_content, encoding="utf-8")
    print(f"Created {enriched_file.name}")

print("Done generating 11 pairs of cards!")
