# Skill Interna: Gerar Cards Enriquecidos

Implementação da skill que automatiza a geração de flashcards enriquecidos a partir de fotos.

## Fluxo de Execução

### Fase 1: Detectar e Renomear Fotos

```bash
# Listar todas as imagens no diretório
find . -maxdepth 1 \( -name "*.png" -o -name "*.jpg" -o -name "*.jpeg" \) -type f | sort
```

Para cada foto encontrada que não segue o padrão `foto-NNN.png`:
1. Ordene por data de modificação (`stat` ou `ls -lt`)
2. Renomeie para `foto-001.png`, `foto-002.png`, etc. usando `mv`
3. Informe ao Fabão sobre cada renomeação

Exemplo de output:
```
✅ Renomeando fotos encontradas:
   - "Screenshot 2026-07-18 at 08.46.16.png" → foto-001.png
   - "Screenshot 2026-07-18 at 08.46.21.png" → foto-002.png
```

### Fase 2: Processar Cada Foto

Para cada arquivo `foto-001.png`, `foto-002.png`, etc. (em ordem numérica):

#### Passo 1: Ler a Imagem
Use a ferramenta `Read` com o caminho absoluto:
```
/Users/fabioalvaropereira/Desktop/desafio-fotos/foto-001.png
```

#### Passo 2: Extrair Conteúdo
Leia a imagem e extraia:
- **Pergunta/Cenário**: Texto completo da pergunta (em inglês)
- **Opções**: As 4 alternativas rotuladas A, B, C, D

Exemplo de extração:
```
Pergunta: "You are building a multi-agent research system..."
A - Allow fetch_url for any link...
B - Replace fetch_url with a load_document tool...
C - Keep fetch_url available, but add prompt instructions...
D - Give the document analysis subagent web search tools...
```

#### Passo 3: Criar Card Simples
Crie o arquivo `001-card.md` com o conteúdo extraído:

```markdown
Scenario: [Cenário/Contexto]
[Pergunta completa em inglês]
---
[ ] A - [Opção A]
[ ] B - [Opção B]
[ ] C - [Opção C]
[ ] D - [Opção D]
```

#### Passo 4: Perguntar a Resposta Correta
Pergunte ao Fabão interativamente:
```
📸 Foto 001: "You are building a multi-agent research system..."
Qual é a resposta correta? (A/B/C/D): 
```

Aguarde a resposta (A, B, C ou D).

#### Passo 5: Criar Card Enriquecido
Crie o arquivo `001-enriched-card.md` com a estrutura completa:

```markdown
[Pergunta original em inglês - igual ao card simples]
---
[ ] A - [Opção A]
[ ] B - [Opção B]
[ ] C - [Opção C]
[ ] D - [Opção D]
---
### TRANSLATED QUESTION
[Pergunta completamente traduzida para português]

Alternativas traduzidas:

A) [Opção A traduzida]
B) [Opção B traduzida]
C) [Opção C traduzida]
D) [Opção D traduzida]

---
### EXPLANATION
Explicação:

[Introdução ao conceito testado - 1 parágrafo]

Por que a alternativa [X] é a correta:
[Análise detalhada de 3-4 linhas]

Por que as outras estão erradas:

[Análise de por que A está errada - 2-3 linhas]
[Análise de por que B está errada - 2-3 linhas]
[Análise de por que D está errada - 2-3 linhas]

Dica importante:
[Padrão geral ou conceito-chave a lembrar - 2-3 linhas]

---
### CORRECT ANSWER
Alternativa Correta: [X]
```

## Padrões de Qualidade

### Estrutura do Card Enriquecido

```markdown
[Pergunta original em inglês]
---
[ ] A - [Opção A]
[ ] B - [Opção B]
[ ] C - [Opção C]
[ ] D - [Opção D]
---
### TRANSLATED QUESTION
[Pergunta traduzida fielmente para português]

Alternativas traduzidas:
A) [Opção A traduzida]
B) [Opção B traduzida]
C) [Opção C traduzida]
D) [Opção D traduzida]

---
### EXPLANATION (TECH LEAD)
[Explicação técnica profunda para profissionais experientes]

---
### SIMPLE EXPLANATION
[Explicação acessível para aprendizes/iniciantes]

---
### CORRECT ANSWER
Alternativa Correta: [X]
```

### EXPLANATION (TECH LEAD) — Estrutura
- **Contexto**: O que a pergunta testa? Qual padrão/conceito?
- **Análise Detalhada**: Explicação do conceito em profundidade (1-2 parágrafos)
- **Por que [X] é a correta**: Análise técnica clara (3-4 linhas)
- **Por que as outras estão erradas**: Para CADA alternativa errada (2-3 linhas cada)
- **Dica Importante**: Padrão recorrente, conexão com outro tópico, insight geral

### SIMPLE EXPLANATION — Estrutura
- **O que é**: Conceito explicado em linguagem simples (1 parágrafo)
- **Por que [X] é a melhor**: Como um dev iniciante deveria pensar (2-3 linhas)
- **Por que as outras não funcionam**: Para CADA alternativa (1-2 linhas cada)
- **Lembrar**: Uma frase-chave que resume tudo

### Tradução
- Ser fiel ao significado, não literal
- Manter terminologia técnica em inglês quando apropriado (ex: "fetch_url", "tool design")
- Naturalizar a linguagem para PT-BR

### Análise de Alternativas
**Importante**: Nunca diga apenas "está errada"
- ❌ Ruim: "Essa alternativa está incorreta"
- ✅ Bom (Tech Lead): "Usa fetch_url genérica, continuando o problema original — não resolve na raiz"
- ✅ Bom (Simples): "Permite que o problema continue acontecendo, em vez de impedir"

## Exemplos de Estrutura

### Exemplo Tech Lead
```
Por que a alternativa B é a correta:

A abordagem B estrutura o erro semanticamente com `errorCategory: business`, 
sinalizando que é uma restrição comercial (não técnica) que não pode ser resolvida 
por retry. O coordenador consegue tomar uma decisão inteligente: pedir ao subagente 
que aceite summaries em vez de full text.

Por que as outras estão erradas:

A) Mascara o erro — downstream não consegue diferenciar "vazio real" de "falhou extrair"
C) Retry indefinido é arriscado — se a falha é persistente, fica preso em retry
D) Escalar para infraestrutura é equivocado — não é problema técnico
```

### Exemplo Simples
```
Por que a alternativa B é a melhor:

Quando a ferramenta não consegue fazer algo, é importante comunicar *por quê*. 
Se dizemos "erro de negócio, não tente novamente", o coordenador sabe: "Preciso 
pedir de forma diferente" em vez de ficar tentando a mesma coisa.

Por que as outras não funcionam:

A) Fingir que tudo correu bem confunde quem recebe a informação
C) Tentar de novo mil vezes se a razão é que "a licença não permite" não funciona
D) Culpar a infraestrutura quando o problema é na verdade "a licença não permite"
```

## Referências

Veja exemplos já criados:
- `/Users/fabioalvaropereira/Desktop/desafio-fotos/templates/001-enriched-card.md`
- `/Users/fabioalvaropereira/Desktop/desafio-fotos/001-enriched-card.md` (com novo padrão)
- `/Users/fabioalvaropereira/Desktop/desafio-fotos/002-enriched-card.md` (com novo padrão)

Esses exemplos mostram o tom, estrutura e profundidade esperados.

## Checklist de Execução

- [ ] Detectar todas as fotos no diretório
- [ ] Renomear fotos que não estão em padrão `foto-NNN.png`
- [ ] Informar Fabão sobre as renomeações
- [ ] Para cada foto:
  - [ ] Ler a imagem
  - [ ] Extrair pergunta + 4 opções
  - [ ] Criar `NNN-card.md`
  - [ ] Perguntar resposta correta ao Fabão
  - [ ] Traduzir conteúdo para português
  - [ ] Gerar explicação técnica (por que correta, por que erradas)
  - [ ] Criar `NNN-enriched-card.md`
- [ ] Listar todos os cards criados ao final
- [ ] Confirmar sucesso
