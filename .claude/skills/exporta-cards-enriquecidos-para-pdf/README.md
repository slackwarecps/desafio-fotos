# Skill Interna: Exporta Cards Enriquecidos para PDF

Converte cards enriquecidos em um PDF formatado como deck didático para estudo.

## Fluxo de Execução

### Fase 1: Detectar Cards

```bash
# Listar todos os cards enriquecidos no diretório
find . -maxdepth 1 -name "*-enriched-card.md" -type f | sort -V
```

Exemplo de output:
```
001-enriched-card.md
002-enriched-card.md
003-enriched-card.md
...
010-enriched-card.md
```

### Fase 2: Extrair Conteúdo de Cada Card

Para cada arquivo `NNN-enriched-card.md`:

1. **Pergunta Original** (em inglês)
   - Extrair a primeira seção antes do `---`

2. **Pergunta Traduzida**
   - Seção `### TRANSLATED QUESTION`
   - Incluir alternativas traduzidas

3. **Explicação Tech Lead**
   - Seção `### EXPLANATION (TECH LEAD)`

4. **Explicação Simples**
   - Seção `### SIMPLE EXPLANATION`

5. **Resposta Correta**
   - Seção `### CORRECT ANSWER`

### Fase 3: Formatar Documento Consolidado

Estrutura do markdown consolidado:

```markdown
## TITULO DO DECK [DATA E HORA]                                    pag1

### Question 1/10                                        pag2
[Pergunta em inglês com opções]

### Question 1 Answer                                    pag3
#### TRANSLATED QUESTION
[Tradução + opções em português]

#### EXPLANATION
**Tech Lead:**
[Explicação profunda]

**Simple Explanation:**
[Explicação acessível]

#### CORRECT ANSWER
[Letra da resposta correta]

[Repete para Question 2, 3, ... 10]
```

### Fase 4: Gerar PDF com Pandoc

1. **Criar arquivo Markdown consolidado** (permanente)
   - Arquivo: `outputs/flashcards-deck-YYYY-MM-DD.md`
   - Tamanho típico: 10-15 KB
   - **MANTIDO para edição futura**

2. **Executar comando pandoc** para converter `.md` → `.pdf`
   ```bash
   pandoc flashcards-deck-YYYY-MM-DD.md \
     -o flashcards-deck-YYYY-MM-DD.pdf \
     --from markdown \
     --to pdf
   ```

3. **Resultado**
   - Arquivo: `outputs/flashcards-deck-YYYY-MM-DD.pdf`
   - Formatado para print/compartilhamento
   - **Ambos os arquivos são mantidos**

**Alternativas de Engine PDF:**
```bash
# Com wkhtmltopdf (melhor qualidade)
pandoc flashcards-deck-YYYY-MM-DD.md \
  -o flashcards-deck-YYYY-MM-DD.pdf \
  --pdf-engine=wkhtmltopdf

# Com xhtml2pdf (se wkhtmltopdf não estiver disponível)
pandoc flashcards-deck-YYYY-MM-DD.md -t html | \
  xhtml2pdf - -o flashcards-deck-YYYY-MM-DD.pdf
```

## Padrão de Formatação

### Capa (Página 1)

```
## TITULO DO DECK [DATA E HORA]                                    pag1

**Flashcards - Claude Certified Architect – Foundations**

Data de Geração: [data e hora]
Total de Questões: [número]
Versão: 1.0
```

### Questões (Páginas pares)

```
### Question N/[TOTAL]                                  pag[NÚMERO]

[Pergunta original em inglês com cenário]
---
[ ] A - [Opção A]
[ ] B - [Opção B]
[ ] C - [Opção C]
[ ] D - [Opção D]
```

### Respostas (Páginas ímpares)

```
### Question N Answer                                   pag[NÚMERO]

#### TRANSLATED QUESTION
[Pergunta traduzida em português]

Alternativas traduzidas:

A) [Opção A traduzida]
B) [Opção B traduzida]
C) [Opção C traduzida]
D) [Opção D traduzida]

#### EXPLANATION

**Tech Lead Explanation:**

[Explicação técnica completa]

**Simple Explanation:**

[Explicação acessível]

#### CORRECT ANSWER
Alternativa Correta: [X]
```

## Instruções para Claude

Quando o usuário chamar `/exporta-cards-enriquecidos-para-pdf`:

1. **Fase 1: Detectar**
   - Use Bash para encontrar todos os `*-enriched-card.md`
   - Informe quantos foram encontrados

2. **Fase 2: Extrair**
   - Use Read para ler cada card
   - Extraia as seções em ordem: pergunta, tradução, explicações, resposta
   - Mantenha formatação original

3. **Fase 3: Consolidar**
   - Crie documento Markdown único
   - Siga padrão de formatação acima
   - Adicione números de página e contadores (Question X/Y)

4. **Fase 4: Converter para PDF com Pandoc**
   - Execute comando pandoc para converter `.md` → `.pdf`
   - Comando:
     ```bash
     pandoc flashcards-deck-YYYY-MM-DD.md \
       -o flashcards-deck-YYYY-MM-DD.pdf \
       --from markdown \
       --to pdf
     ```
   - Mantenha o arquivo `.md` raw (não delete)
   - Ambos os arquivos (`.md` e `.pdf`) são gerados

5. **Fase 5: Resumo**
   - Informe nome dos arquivos gerados:
     - `.md` (raw, editável)
     - `.pdf` (formatado, pronto para compartilhar)
   - Quantidade de questões
   - Número de páginas
   - Sucesso!

## Tratamento de Erros

### Nenhum card encontrado
```
❌ Nenhum card enriquecido encontrado no diretório.
   Verifique se há arquivos no padrão: NNN-enriched-card.md
   Exemplo: 001-enriched-card.md, 002-enriched-card.md, etc.
```

### Card malformado
```
⚠️ Card [NNN] não segue o padrão esperado.
   Campos faltantes: [seções que faltam]
   Pulando para o próximo card...
```

### Erro na conversão PDF
```
❌ Erro ao converter Markdown para PDF.
   Arquivo Markdown foi gerado: flashcards-deck.md
   Você pode converter manualmente com:
   $ pandoc flashcards-deck.md -o flashcards-deck.pdf
```

## Exemplos

Veja o template de referência:
- `/Users/fabioalvaropereira/Desktop/desafio-fotos/templates/deck-exemplo.md`

Esse arquivo mostra exatamente a estrutura esperada no PDF.

## Checklist de Execução

- [ ] Detectar todos os cards enriquecidos
- [ ] Contar total de questões
- [ ] Extrair conteúdo de cada card
- [ ] Validar que cada card tem todas as seções
- [ ] Criar documento Markdown consolidado
- [ ] Adicionar capa com data/hora
- [ ] Numerar questões (Question X/[TOTAL])
- [ ] Formatar números de página
- [ ] Converter para PDF
- [ ] Validar PDF foi criado
- [ ] Reportar sucesso com nome do arquivo
