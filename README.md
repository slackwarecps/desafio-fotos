# Desafio Fotos - Sistema de Flashcards Enriquecidos

Sistema para criar flashcards educacionais enriquecidos a partir de fotos, estruturados para apps de repetição espaçada (SRS).

## Workflow

### Fase 1: Preparação de Fotos
Coloque as novas fotos (screenshots) no diretório raiz, em qualquer formato:
- `Screenshot 2026-07-18 at 08.46.16.png`
- `Captura de Tela...png`
- Qualquer arquivo `.png` ou `.jpg`

A skill cuidará da renomeação automaticamente.

### Fase 2: Gerar Cards Enriquecidos
Use a skill `/gerar-cards-enriquecidos` para automatizar todo o processo:

```bash
/gerar-cards-enriquecidos
```

#### O que a skill faz:

1. **Detecta fotos**: Encontra todas as fotos `foto-NNN.png`
2. **Extrai conteúdo**: Lê cada foto e identifica:
   - Pergunta/Cenário
   - Opções de resposta (A, B, C, D)
3. **Cria card simples**: Arquivo `NNN-card.md` com:
   - Pergunta original (inglês)
   - Separador ---
   - 4 opções de resposta
4. **Enriquece card**: Arquivo `NNN-enriched-card.md` com:
   - Pergunta original em inglês
   - Tradução completa para português
   - Explicação técnica detalhada:
     * Contexto do conceito testado
     * Por que a resposta correta é correta
     * Por que cada alternativa errada está errada
     * Dica importante sobre o padrão
   - Indicação da resposta correta

## Estrutura de Arquivos

```
desafio-fotos/
├── foto-001.png              # Foto original capturada
├── foto-002.png
├── foto-003.png
│
├── 001-card.md               # Card simples (básico)
├── 002-card.md
├── 003-card.md
│
├── 001-enriched-card.md      # Card enriquecido (com tradução + explicação)
├── 002-enriched-card.md
├── 003-enriched-card.md
│
├── templates/                # Templates de referência
│   ├── 001-card.md
│   └── 001-enriched-card.md
│
└── .claude/
    └── skills/
        └── gerar-cards-enriquecidos.md
```

## Formato dos Cards

### Card Simples (NNN-card.md)
```markdown
Scenario: [Contexto]
[Pergunta completa]
---
[ ] A - [Opção A]
[ ] B - [Opção B]
[ ] C - [Opção C]
[ ] D - [Opção D]
```

### Card Enriquecido (NNN-enriched-card.md)
```markdown
[Pergunta original em inglês]
---
[ ] A - [Opção A]
...
---
### TRANSLATED QUESTION
[Tradução para português]

Alternativas traduzidas:

A) [Opção A traduzida]
...

---
### EXPLANATION
Explicação:

[Explicação técnica detalhada]

Por que a alternativa [X] é a correta:
[Análise detalhada]

Por que as outras estão erradas:

[Análise de cada alternativa incorreta]

Dica importante:
[Padrão ou conceito geral]

---
### CORRECT ANSWER
Alternativa Correta: [A/B/C/D]
```

## Fluxo Completo para Novas Perguntas

1. **Capture as fotos** de novas perguntas
2. **Coloque no diretório** raiz do projeto
3. **Execute**: `/gerar-cards-enriquecidos`
4. **Para cada foto**, o Claude vai:
   - Extrair a pergunta e opções
   - Criar o card simples
   - Perguntar qual é a resposta correta
   - Criar o card enriquecido com tradução e explicação

## Uso em Apps SRS

Os cards enriquecidos (com tradução e explicação) são projetados para:
- **Frente do card**: Pergunta em português (da seção TRANSLATED QUESTION)
- **Verso do card**: Resposta + Explicação (seção EXPLANATION + CORRECT ANSWER)

Isso permite:
- Estudar em português
- Entender não só a resposta, mas também o conceito
- Reforçar padrões de engenharia e arquitetura

## Exemplos

Veja os cards de exemplo já criados:
- `001-enriched-card.md` - Developer Productivity com Plan Mode
- `002-enriched-card.md` - Structured Data Extraction com requisitos de latência
- `003-enriched-card.md` - QA patterns e observabilidade de dados

## Skills Disponíveis

### 1. `/gerar-cards-enriquecidos`
Gera cards simples e enriquecidos a partir de fotos automaticamente.
- Detecta fotos com qualquer nome
- Renomeia para `foto-001.png`, `foto-002.png`, etc.
- Cria `NNN-card.md` (simples)
- Cria `NNN-enriched-card.md` (com 2 níveis de explicação)

### 2. `/exporta-cards-enriquecidos-para-pdf`
Exporta todos os cards enriquecidos para um único PDF.
- Consolida todos os `NNN-enriched-card.md`
- Formata como deck didático
- Gera `flashcards-deck-[DATA].pdf`
- Pronto para estudar ou compartilhar

### 3. `/exporta-cards-enriquecidos-para-epub`
Exporta todos os cards enriquecidos para o formato EPUB de e-book (compatível com Google Play Books).
- Consolida todos os `NNN-enriched-card.md` em XHTMLs estruturados
- Otimiza tipografia e estilos para visualização em celulares
- Gera `flashcards-deck-[DATA].epub`
- Executável através do script [scripts/exporta_epub.py](file:///Users/fabioalvaropereira/Desktop/desafio-fotos/scripts/exporta_epub.py)

## Próximas Fases

- [ ] Integrar com app SRS externo (Anki, Quizlet)
- [ ] Adicionar categorização automática por tópico
- [ ] Sincronizar com repositório remoto
- [ ] Gerar estatísticas de aprendizado
- [ ] Suporte para múltiplos idiomas
