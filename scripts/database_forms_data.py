#!/usr/bin/env python3
import json
import os
import sys

# Script to build database of cards for forms
# Reads questions-parsed.json and writes 001 to 060 cards

OUTPUT_DIR = "outputs/cards-enriquecidos-forms"
os.makedirs(OUTPUT_DIR, exist_ok=True)

with open(os.path.join(OUTPUT_DIR, "questions-parsed.json"), "r", encoding="utf-8") as f:
    questions = json.load(f)

# Dictionary of detailed card data
DATA = {
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
            "intro": "Esta questão analisa estratégias de manipulação de arquivos quando ferramentas de edição por correspondência pontual (`Edit`) falham devido a falta de unicidade no código.",
            "why_correct": "Quando a ferramenta `Edit` não consegue identificar de forma única o bloco de código por conta de repetições estruturais, o padrão de fallback determinístico e seguro é carregar o arquivo via `Read`, realizar a modificação no contexto do modelo e sobrescrever o arquivo com `Write`. Isso garante inserção no local exato sem riscos de substituição incorreta.",
            "why_err": {
                "A": "Capturar 30+ linhas torna a chamada frágil a diferenças insignificantes de caracteres e consome tokens desnecessários.",
                "B": "O parâmetro `replace_all` altera todas as ocorrências repetidas do arquivo, corrompendo outras funções e a estrutura do código.",
                "C": "Anexar ao final via heredoc não insere a função entre as duas funções existentes, descumprindo a especificação."
            },
            "tip": "Padrão de Fallback para Edição: Quando o matcher do Edit falha por falta de unicidade, use a sequência determinística Read -> Modificar no Contexto -> Write."
        },
        "child": {
            "intro": "Imagine que você quer colocar um adesivo novo no meio de uma página de livro, entre duas figuras de gatinhos iguais 🐱🐱.",
            "why_correct": "A alternativa D é a mais esperta: o robô lê a página inteira, insere o adesivo no lugar exato e redesenha a página novinha! É seguro e sem erros.",
            "why_err": {
                "A": "Tentar tirar foto de quase a página toda deixa a instrução confusa e fácil de errar.",
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
    }
}

print("Base generator template initialised.")
