---
name: gerar-cards-enriquecidos
description: Gera cartões enriquecidos e didáticos para flashcards SRS a partir de fotos no diretório, com explicações para múltiplos níveis de aprendizado
---

# Skill: Gerar Cards Enriquecidos com Explicações Didáticas

Automatiza o processo completo de criação de flashcards enriquecidos a partir de fotos, usando padrão de "professor de certificação" com explicações estruturadas para tech leads e aprendizes.

## Uso

```bash
/gerar-cards-enriquecidos
```

## Processo Automático

1. **Detectar e Renomear Fotos**
   - Encontra todas as imagens (*.png, *.jpg, *.jpeg) no diretório
   - Renomeia automaticamente para `foto-001.png`, `foto-002.png`, etc.
   - Ordena por data de modificação

2. **Extrair Conteúdo**
   - Lê cada foto e extrai:
     - Pergunta original (em inglês)
     - 4 opções de resposta (A, B, C, D)

3. **Gerar Card Simples** (`NNN-card.md`)
   ```
   [Pergunta original em inglês]
   ---
   [ ] A - [Opção A]
   [ ] B - [Opção B]
   [ ] C - [Opção C]
   [ ] D - [Opção D]
   ```

4. **Gerar Card Enriquecido** (`NNN-enriched-card.md`) com:
   - **TRANSLATED QUESTION**: Tradução fiel em português + opções traduzidas
   - **EXPLANATION (Tech Lead)**: Explicação técnica profunda
     * Conceito testado e padrão arquitetural
     * Por que a resposta correta é a melhor (análise detalhada)
     * Por que cada alternativa está errada (não apenas que está errada, MAS o motivo)
     * Dica importante e conexões com outros tópicos
   - ** 🚸 CHILDREN EXPLANATION**: Explicação acessível para aprendizes (como explicar para uma criança de 10 anos entenderia, mas apropriada para dev iniciante)
     * Conceito em linguagem simples
     * Por que a resposta correta funciona
     * O que torna as outras respostas problemáticas
   - **CORRECT ANSWER**: Letra da alternativa correta

## O que esperar

```
✅ Detectadas fotos:
   - Screenshot 2026-07-18 at 08.46.16.png → foto-001.png
   - Screenshot 2026-07-18 at 08.46.21.png → foto-002.png

📸 Processando foto-001.png...
[Pergunta extraída e exibida]

✅ Criados:
   - 001-card.md
   - 001-enriched-card.md
     (com explicação tech lead + explicação simples)

[Repete para as próximas fotos...]

✨ Concluído! 2 cards criados com sucesso.
```

## Estrutura de Output

```
desafio-fotos/
├── foto-001.png                # Foto renomeada
├── foto-002.png
├── 001-card.md                 # Card simples (pergunta + opções)
├── 001-enriched-card.md        # Card enriquecido (2 níveis de explicação)
├── 002-card.md
├── 002-enriched-card.md
└── ...
```

## Qualidade de Saída

### Explicação Tech Lead
- Tom técnico e preciso (similar aos exemplos em `templates/`)
- Conecta a pergunta a padrões de engenharia/arquitetura
- Análise detalhada de por que cada alternativa está certa/errada
- Insights sobre padrões recorrentes e best practices
- Português naturalizado com termos técnicos apropriados

### Explicação Simples
- Linguagem acessível para iniciantes
- Analogias práticas quando apropriado
- Quebra conceitos complexos em partes menores
- Explica não apenas "o quê" mas "por quê"
- Sem perder precisão técnica, mas sem jargão desnecessário

## Padrão da Certificação

As questões testam conceitos de:
- Claude Models e suas capacidades
- Prompt engineering avançado
- Agentic systems e tool use
- Vision capabilities e document handling
- Best practices para desenvolvedores
- Padrões de arquitetura e design
- Decisões de trade-offs em sistemas

Mantenha esse contexto ao gerar explicações.
