---
name: exporta-cards-enriquecidos-para-epub
description: Exporta cards enriquecidos para EPUB (e-book) compatível com Google Play Books para leitura no celular
---

# Skill: Exportar Cards Enriquecidos para EPUB

Converte todos os cards enriquecidos (`*-enriched-card.md`) em um arquivo EPUB formatado e pronto para ler no seu celular via Google Play Books.

## Uso

Existem **3 formas** de usar a skill:

### **1. Interativo (Recomendado)** 🎯
```bash
/exporta-cards-enriquecidos-para-epub
```
A skill **perguntará o título** do livro. Se deixar em branco, usa o padrão.

### **2. Via Argumento de Linha de Comando**
```bash
python3 .claude/skills/exporta-cards-enriquecidos-para-epub/exporta.py "Meu Livro de Flashcards"
```

### **3. Via Variável de Ambiente**
```bash
BOOK_TITLE="Meu Livro de Flashcards" /exporta-cards-enriquecidos-para-epub
```

### **Padrão (se não informar nada)**
```
"Flashcards - Claude Certified Architect"
```

O título será aplicado em:
- ✅ Capa (Cover)
- ✅ Metadados (content.opf)
- ✅ Índice (toc.ncx)

## Processo Automático

1. **Detectar Cards**
   - Encontra todos os arquivos `*-enriched-card.md` na pasta `/Users/fabioalvaropereira/Desktop/desafio-fotos/outputs/cards-enriquecidos/` (com fallback para caminhos relativos e raiz)
   - Ordena numericamente (001, 002, 003, etc.)

2. **Parse do Conteúdo**
   - Extrai de cada card:
     - Pergunta original (English)
     - Opções (A, B, C, D)
     - Tradução em português
     - Explicação Tech Lead
     - Explicação Simples
     - Resposta correta

3. **Gerar EPUB**
   - Cria estrutura válida de EPUB 3.0
   - **Idioma padrão: English (en-US)**
   - Seções em português marcadas com `lang="pt-BR"`
   - Formata cada card como 2 capítulos: pergunta + resposta
   - Inclui índice navegável (Table of Contents)
   - Otimiza para leitura móvel

4. **Output**
   - Arquivo: `flashcards-deck-[DATA].epub`
   - Compatível com: Google Play Books, Kindle, Apple Books, Kobo, etc.
   - **Idioma:** English (US) com seções em Portuguese (BR)

## O que esperar

```
============================================================
📚 Exportador de Cards Enriquecidos para EPUB
============================================================

📖 Qual é o título do livro? (padrão: 'Flashcards - Claude Certified Architect'): 
> My Custom Flashcards Book

✅ Título configurado: My Custom Flashcards Book

✅ Detectados cards enriquecidos em 'outputs/cards-enriquecidos':
   - 001-enriched-card.md
   - 002-enriched-card.md
   - 003-enriched-card.md

📖 Estruturando EPUB...
   ✓ Estrutura EPUB criada (EPUB 3.0 com nav.xhtml)
   ✓ Processando 3 cards (pergunta + resposta)...

📦 Compilando EPUB...

✅ Validando estrutura EPUB...
   ✓ Estrutura EPUB válida e compatível com Google Play Books

✨ EPUB gerado com sucesso!

📱 Arquivo: outputs/flashcards-deck-2026-07-19.epub
   Tamanho: 14.0 KB
   Cards: 3
   Formato: EPUB 3.0 (nav.xhtml + toc.ncx)
   Compatibilidade: ✅ Google Play Books, Apple Books, Kindle, Kobo

📥 Para ler no celular:
   1. Acesse: Google Play Books (https://play.google.com/books/publish)
   2. Faça upload: outputs/flashcards-deck-2026-07-19.epub
   3. Pronto! Leia no app do celular ou web
```

## Estrutura do EPUB

```
flashcards-deck-2026-07-19.epub
├── mimetype                           # Tipo MIME
├── META-INF/
│   └── container.xml                  # Referência ao OPF
├── OEBPS/
│   ├── content.opf                    # Metadados e estrutura
│   ├── nav.xhtml                      # Navegação EPUB 3.0 (obrigatório)
│   ├── toc.ncx                        # Índice de navegação (compatibilidade)
│   ├── styles.css                     # Estilização
│   └── chapters/
│       ├── cover.xhtml                # Capa
│       ├── q001.xhtml                 # Pergunta 001
│       ├── a001.xhtml                 # Resposta 001
│       ├── q002.xhtml                 # Pergunta 002
│       ├── a002.xhtml                 # Resposta 002
│       └── ...
```

**Nota:** Cada card é dividido em **2 páginas**:
- Página par: Pergunta (q001, q002, q003...)
- Página ímpar: Resposta (a001, a002, a003...)

## Qualidade do EPUB

- **Responsivo**: Adapta-se a qualquer tamanho de tela (celular, tablet, e-reader)
- **Navegável**: Índice clicável para pular entre cards
- **Formatado**: Tipografia legível, espaçamento adequado
- **Rápido**: Arquivo compacto, carrega rapidamente
- **Offline**: Funciona completamente sem internet

## Cards no EPUB

Cada card é dividido em **2 páginas separadas com quebra de página automática**:

### **Página 1: Pergunta** (q001.xhtml, q002.xhtml, ...) — [English]
1. **Título**: Question X/Total
2. **Seção Original**: Pergunta em inglês + 4 opções (A, B, C, D)

### **Página 2: Resposta** (a001.xhtml, a002.xhtml, ...) — [English + Portuguese sections]
1. **Título**: Question X - Answer [en-US]
2. **Tradução**: Pergunta e opções em português [pt-BR] 🇧🇷
3. **Explicação Tech Lead**: Análise técnica detalhada com padrões arquiteturais [pt-BR] 🇧🇷
4. **Explicação Simples**: Versão acessível para aprendizes [pt-BR] 🇧🇷
5. **Resposta Correta**: Letra correta destacada em verde [pt-BR] 🇧🇷

**Estrutura de páginas:**
- Página 1: Cover [en-US]
- Página 2: Question 001 [en-US]
- Página 3: Answer 001 [en-US com pt-BR nas seções de resposta]
- Página 4: Question 002 [en-US]
- Página 5: Answer 002 [en-US com pt-BR nas seções de resposta]
- etc.

**Configuração de Idiomas:**
- Idioma padrão do EPUB: **English (United States)**
- Seções de resposta: **Portuguese (Brazil)**
- Leitores como Google Play Books respeitam as marcações `lang` para:
  - Renderização de fontes apropriadas
  - Ajuste de hifenação
  - Pronúncia em leitura automática

## Leitura no Google Play Books

1. Baixe o EPUB para seu dispositivo
2. Abra Google Play Books
3. Toque em "Uploads"
4. Selecione `flashcards-deck-[DATA].epub`
5. Comece a estudar! 📚

Você pode:
- Marcar páginas favoritas
- Fazer notas
- Ajustar tamanho da fonte
- Sincronizar progresso entre dispositivos
