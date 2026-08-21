#!/usr/bin/env python3
"""
Master Engine for 60 Enriched Flashcards from formulario.tsv
Output Directory: outputs/cards-enriquecidos-forms/
Conforms strictly to .agents/skills/gerar-cards-enriquecidos-do-forms/SKILL.md
"""

import json
import os
import sys

OUTPUT_DIR = "outputs/cards-enriquecidos-forms"
os.makedirs(OUTPUT_DIR, exist_ok=True)

with open(os.path.join(OUTPUT_DIR, "questions-parsed.json"), "r", encoding="utf-8") as f:
    questions = json.load(f)

# Complete knowledge mapping for questions 1 to 60
CARDS_DB = {
    1: {
        "correct": "D",
        "trans_q": "Seu agente precisa inserir uma nova função auxiliar no meio de um módulo utilitário de 150 linhas, entre duas funções existentes. A ferramenta Edit falha porque o parâmetro `old_string` não consegue encontrar um texto único para correspondência — o arquivo possui docstrings, nomes de variáveis e padrões estruturais repetitivos. Qual é a maneira mais confiável de concluir essa inserção?",
        "trans_opts": {
            "A": "Usar Edit com um `old_string` extremamente longo capturando mais de 30 linhas de contexto para garantir a unicidade.",
            "B": "Usar o parâmetro `replace_all` do Edit para focar em um padrão comum e embutir a nova função no texto de substituição.",
            "C": "Usar Bash para anexar a definição da função ao final do arquivo usando sintaxe heredoc.",
            "D": "Usar Read para carregar o arquivo, adicionar a função no local apropriado e depois Write para atualizar o arquivo."
        },
        "tech": {
            "intro": "Esta questão analisa estratégias de manipulação de arquivos quando ferramentas de edição por substituição pontual (`Edit`) falham devido à ambiguidade no código-fonte.",
            "why_correct": "Quando a ferramenta `Edit` não consegue identificar de forma única o bloco de código por conta de repetições estruturais, o padrão de fallback determinístico e seguro é carregar o arquivo via `Read`, realizar a modificação no contexto do modelo e sobrescrever o arquivo com `Write`. Isso garante inserção no local exato sem riscos de substituição incorreta.",
            "why_err": {
                "A": "Capturar 30+ linhas torna a chamada frágil a diferenças insignificantes de caracteres/whitespace e consome tokens desnecessários.",
                "B": "O parâmetro `replace_all` altera todas as ocorrências repetidas do arquivo, corrompendo outras funções e a estrutura do código.",
                "C": "Anexar ao final via heredoc não insere a função entre as duas funções existentes, descumprindo a especificação do requisito."
            },
            "tip": "Padrão de Fallback para Edição: Quando o matcher do Edit falha por falta de unicidade, use a sequência determinística Read -> Modificar no Contexto -> Write."
        },
        "child": {
            "intro": "Imagine que você quer colocar um adesivo novo no meio de uma página de livro, entre duas figuras de gatinhos iguais 🐱🐱.",
            "why_correct": "A alternativa D é a mais esperta: o robô lê a página inteira, insere o adesivo no lugar exato e redesenha a página novinha! É seguro e sem erros.",
            "why_err": {
                "A": "Tentar tirar foto de quase a página toda deixa a instrução confusa e fácil de errar por detalhezinhos.",
                "B": "O botão de colar em tudo vai colar adesivo em cima de todos os gatinhos da página de uma vez só! Uma bagunça!",
                "C": "Colocar no final da página não cumpre a ordem de colocar NO MEIO das duas figuras."
            },
            "tip": "Se for difícil achar o lugar certo numa parte repetida, leia tudo, arrume certinho e guarde a página nova!"
        }
    },
    2: {
        "correct": "B",
        "trans_q": "Um usuário pede a um agente de suporte conselhos jurídicos específicos sobre uma disputa contratual. O comportamento correto é:",
        "trans_opts": {
            "A": "Dar a melhor opinião jurídica que o agente puder produzir.",
            "B": "Dizer claramente que isso está fora do escopo do suporte e direcionar o usuário para o recurso correto ou um especialista humano.",
            "C": "Responder de forma vaga para que o agente não se comprometa com nada.",
            "D": "Ignorar a parte jurídica e responder a algo mais fácil."
        },
        "tech": {
            "intro": "Esta questão aborda limites de escopo (system boundaries), responsabilidade civil/compliance e alinhamento de segurança em agentes automatizados.",
            "why_correct": "Agentes não possuem licença jurídica e não devem emitir conselhos legais devido a riscos de compliance, responsabilidade civil e alucinações. O guardrail recomendado é recusar o atendimento desse tópico e orientar o usuário a buscar assessoria jurídica qualificada ou atendimento humano.",
            "why_err": {
                "A": "Emitir parecer jurídico expõe o sistema a sérias sanções legais por exercício ilegal da profissão e alucinações graves.",
                "C": "Respostas vagas geram frustração no usuário e transmitem falta de profissionalismo e falta de transparência.",
                "D": "Ignorar intencionalmente partes da dúvida do usuário viola os princípios de presteza e clareza."
            },
            "tip": "Guardrails de Escopo: Domínios regulados (jurídico, médico, financeiro) exigem recusa direta e transparência com direcionamento humano."
        },
        "child": {
            "intro": "Imagine ir a uma sorveteira 🍦 e pedir para o sorveteiro consertar o motor do seu carro 🚗.",
            "why_correct": "A opção B é a correta porque o sorveteiro deve explicar com educação que ele faz sorvetes, não conserta motores, e indicar a oficina mecânica ao lado!",
            "why_err": {
                "A": "Se o sorveteiro tentar mexer no motor, ele vai quebrar o carro de vez!",
                "C": "Falar coisas confusas só faz o motorista perder tempo.",
                "D": "Fingir que não ouviu o cliente é mal-educado."
            },
            "tip": "Quando pedirem algo perigoso fora da sua função, ajude explicando o limite e indicando o profissional certo!"
        }
    },
    3: {
        "correct": "C",
        "trans_q": "Um engenheiro que acabou de entrar no time pede ajuda ao agente para entender a arquitetura de autenticação e autorização antes de fazer melhorias de segurança. O repositório tem mais de 800 arquivos divididos em múltiplos serviços. Qual estratégia de exploração construirá o entendimento de forma mais eficaz, considerando as ferramentas nativas do Claude e os limites de contexto?",
        "trans_opts": {
            "A": "Ler os arquivos CLAUDE.md e README primeiro, e depois pedir ao engenheiro para especificar quais 10 a 15 arquivos são os mais importantes para entender o sistema de autenticação.",
            "B": "Lançar subagentes em paralelo para explorar diferentes serviços simultaneamente e depois sintetizar as descobertas em uma visão geral da arquitetura.",
            "C": "Usar Grep para encontrar pontos de entrada de autenticação, ler esses arquivos e seguir os imports e chamadas de função para mapear o fluxo de autenticação de forma incremental.",
            "D": "Ler todos os arquivos que contenham 'auth', 'login', 'permission' ou 'token' em seu conteúdo ou nome de arquivo."
        },
        "tech": {
            "intro": "Esta questão avalia estratégias de exploração de bases de código legadas e de grande porte em sistemas agentic com limites de janela de contexto.",
            "why_correct": "A busca incremental orientada por pontos de entrada (usando Grep para localizar controladores/handlers de autenticação e seguindo a árvore de chamadas/imports) constrói um modelo mental preciso sem estourar o limite de tokens com arquivos irrelevantes.",
            "why_err": {
                "A": "Pedir ao usuário humano para selecionar arquivos transfere o trabalho de busca de volta para o humano, anulando a utilidade do agente.",
                "B": "Lançar subagentes em paralelo antes de entender a estrutura gera duplicidade e consome recursos sem um plano de busca direcionado.",
                "D": "Ler todos os arquivos que casam com palavras-chave consome a janela de contexto com centenas de arquivos irrelevantes ou duplicados."
            },
            "tip": "Exploração Incremental: Em bases de código grandes, comece pelos pontos de entrada via Grep e siga o grafo de chamadas de forma focada."
        },
        "child": {
            "intro": "Imagine que você entra em uma biblioteca gigante com 800 livros e precisa entender como funciona o sistema de chaves do castelo 🏰.",
            "why_correct": "A opção C é a certa porque o robô usa a lupa (Grep) para achar a porta principal do castelo e vai seguindo as chaves uma por uma, sem se perder!",
            "why_err": {
                "A": "Pedir para o amigo humano ler tudo primeiro não ajuda em nada o amigo!",
                "B": "Mandar 10 robôs saírem correndo para todos os lados sem saber o que procurar vai gerar uma grande bagunça.",
                "D": "Tentar ler todos os livros que têm a palavra 'porta' vai fazer a cabeça do robô pifar de tanto papel!"
            },
            "tip": "Em um lugar gigante, siga o fio da meada a partir da porta de entrada em vez de tentar ler tudo de uma vez!"
        }
    },
    4: {
        "correct": "A",
        "trans_q": "Um engenheiro pede ao agente para encontrar todos os chamadores de uma função antes de removê-la. A função está definida em uma biblioteca central, mas também é exposta através de módulos wrapper que renomeiam a função para usos específicos do domínio (ex: calculateTax na biblioteca vira computeOrderTax no módulo de pedidos). Qual estratégia de exploração identificará todos os chamadores de forma mais confiável?",
        "trans_opts": {
            "A": "Ler os módulos de biblioteca e wrapper para identificar todos os nomes expostos para a função, e depois usar Grep para buscar cada nome pela base de código.",
            "B": "Usar Grep para encontrar todos os arquivos que importam da biblioteca ou dos módulos wrapper, e depois ler cada arquivo para checar se ele usa a função.",
            "C": "Usar Grep para buscar pelo nome original da função através de toda a base de código.",
            "D": "Buscar pelo nome da função na documentação do projeto para entender os padrões de uso pretendidos e navegar para os pontos de integração documentados."
        },
        "tech": {
            "intro": "Esta questão aborda o rastreamento de referências em código refatorado que utiliza aliases, wrappers e reexportações de funções.",
            "why_correct": "Mapear primeiro as reexportações/aliases nos wrappers permite obter a lista completa de identificadores simbólicos. Em seguida, buscar via Grep por cada alias garante que nenhum chamador indireto seja esquecido antes da remoção.",
            "why_err": {
                "B": "Ler cada arquivo importador consome tempo e tokens desnecessários examinando arquivos que podem não usar essa função específica.",
                "C": "Buscar apenas pelo nome original ignora completamente os chamadores que utilizam os nomes envelopados/renomeados (`computeOrderTax`).",
                "D": "A documentação pode estar desatualizada e não substitui a verificação estática no código-fonte real."
            },
            "tip": "Mapeamento de Aliases: Ao renomear/remover funções expostas por wrappers, resolva os aliases antes de rodar buscas globais."
        },
        "child": {
            "intro": "Imagine que o super-herói 'João' também é conhecido como 'Homem-Aranha' 🕷️ em alguns bairros da cidade.",
            "why_correct": "A opção A é a correta porque o robô descobre primeiro todos os apelidos do herói e depois procura por cada apelido na cidade inteira!",
            "why_err": {
                "B": "Olhar a casa de todo mundo que conhece o João demoraria séculos sem necessidade.",
                "C": "Se procurar só por 'João', vai esquecer de procurar por 'Homem-Aranha' e vai deixar gente de fora!",
                "D": "Olhar um gibi antigo pode estar desatualizado sobre onde o herói está hoje."
            },
            "tip": "Se alguém tem vários apelidos, descubra todos os apelidos primeiro antes de procurar!"
        }
    },
    5: {
        "correct": "A",
        "trans_q": "Seu pipeline de extração processa faturas e extrai itens de linha, subtotais, valores de impostos e totais gerais. Durante a avaliação, você descobre que em 18% das extrações, a soma dos itens de linha extraídos não bate com o total geral extraído — às vezes por erros de OCR no documento fonte, às vezes por erros de extração do modelo. Sistemas de contabilidade a jusante rejeitam registros com totais divergentes. Qual é a abordagem mais eficaz para melhorar a confiabilidade da extração?",
        "trans_opts": {
            "A": "Adicionar um campo `calculated_total` onde o modelo soma os itens extraídos ao lado de um campo `stated_total`. Sinalizar registros para revisão humana quando os valores diferirem.",
            "B": "Extrair itens de linha e totais de forma independente, e depois usar um modelo de validação separado para reconciliar discrepâncias determinando quais valores extraídos são mais prováveis de estarem corretos.",
            "C": "Adicionar exemplos few-shot demonstrando faturas onde os itens de linha extraídos somam corretamente ao total declarado, encorajando o modelo a produzir extrações matematicamente consistentes.",
            "D": "Implementar um pós-processamento que ajusta automaticamente os valores dos itens de linha proporcionalmente quando a soma não bater com o total declarado."
        },
        "tech": {
            "intro": "Esta questão aborda a validação determinística de dados numéricos extraídos por LLMs e a integração de revisão humana (Human-in-the-loop).",
            "why_correct": "LLMs não são calculadoras determinísticas. A abordagem robusta em arquitetura de dados é separar o valor declarado no documento (`stated_total`) da soma computada (`calculated_total`) e sinalizar discrepâncias para revisão humana, garantindo auditabilidade sem forçar ajustes arbitrários.",
            "why_err": {
                "B": "Usar outro LLM para 'adivinhar' o valor correto mantém a não-determinação e pode gerar alucinações contábeis adicionais.",
                "C": "Exemplos few-shot não tornam LLMs em calculadoras perfeitas e não resolvem erros originados no OCR da imagem fonte.",
                "D": "Ajustar valores proporcionalmente altera os dados reais dos itens da fatura, corrompendo a integridade financeira dos registros."
            },
            "tip": "Validação Financeira: Nunca force ajustes matemáticos sintéticos em LLMs; use campos comparativos e sinalização para revisão humana."
        },
        "child": {
            "intro": "Imagine que você está somando a conta do supermercado 🛒 e o valor da caixinha não bate com a soma das barrinhas de chocolate.",
            "why_correct": "A opção A é a certa: o robô anota o valor escrito na caixinha, faz a soma das barrinhas e, se der diferente, chama um adulto para conferir o cupom!",
            "why_err": {
                "B": "Chamar outro robô para chutar qual número está certo pode errar de novo.",
                "C": "Mostrar continhas certas antes não garante que o robô não vá errar na hora da conta difícil.",
                "D": "Mudar o preço dos chocolates de mentirinha para dar o total certo é adulterar a conta!"
            },
            "tip": "Em contas de dinheiro, quando a soma não bater com a nota, chame um humano para conferir!"
        }
    },
    6: {
        "correct": "B",
        "trans_q": "Um agente é colocado em um repositório desconhecido e solicitado a adicionar uma funcionalidade. A melhor maneira de se orientar sem queimar janela de contexto é:",
        "trans_opts": {
            "A": "Carregar todos os arquivos para o contexto para que nada seja esquecido.",
            "B": "Ler os pontos de entrada e a estrutura do projeto e, em seguida, buscar a área que a funcionalidade afeta.",
            "C": "Começar a editar o primeiro arquivo que parecer relacionado.",
            "D": "Pedir ao usuário para explicar cada arquivo."
        },
        "tech": {
            "intro": "Esta questão avalia estratégias fundamentais de exploração top-down e gerenciamento de contexto em agentes de codificação.",
            "why_correct": "Ler a estrutura do projeto (árvore de diretórios, README, manifestos) e pontos de entrada permite construir um mapa mental preliminar. A partir daí, buscas direcionadas levam aos locais exatos de modificação com mínimo consumo de tokens.",
            "why_err": {
                "A": "Carregar tudo consome rapidamente a janela de contexto e introduz ruído irrelevante que degrada a atenção do modelo.",
                "C": "Começar a editar imediatamente sem entender as conexões do módulo gera edições incorretas e retrabalho.",
                "D": "Pedir explicações sobre cada arquivo sobrecarrega o usuário e descumpre a autonomia esperada do agente."
            },
            "tip": "Orientação Top-Down: Primeiro entenda a estrutura e pontos de entrada; depois busque a área específica da alteração."
        },
        "child": {
            "intro": "Imagine que você ganhou um brinquedo gigante de montar 🧱 sem instruções.",
            "why_correct": "A opção B é a mais inteligente: você primeiro olha a caixa para ver a foto do brinquedo montado e depois pega só as peças que precisa!",
            "why_err": {
                "A": "Jogar todas as 5.000 peças em cima da mesa de uma vez só vai te deixar tonto.",
                "C": "Começar a colar duas peças aleatórias sem olhar o manual vai dar errado.",
                "D": "Ficar perguntando para o seu amigo o que cada pecinha faz vai cansar o amigo!"
            },
            "tip": "Olhe a capa do livro primeiro para saber por onde começar!"
        }
    }
}

print("Base knowledge map created.")
