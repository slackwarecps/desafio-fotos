# Skill: Exportar Cards Enriquecidos para EPUB

Implementação da skill que converte cards enriquecidos em um arquivo EPUB compatível com Google Play Books e outros leitores.

## Como Usar

### **Opção 1: Interativo (Recomendado)** 🎯
```bash
/exporta-cards-enriquecidos-para-epub
```
A skill perguntará pelo título do livro. Se deixar em branco (ENTER), usa o padrão.

### **Opção 2: Com Título via Argumento**
```bash
python3 .claude/skills/exporta-cards-enriquecidos-para-epub/exporta.py "Meu Livro Personalizado"
```

### **Opção 3: Com Título via Variável de Ambiente**
```bash
BOOK_TITLE="Meu Livro Personalizado" python3 .claude/skills/exporta-cards-enriquecidos-para-epub/exporta.py
```

### **Padrão (sem argumentos)**
Se nenhuma opção for fornecida, usa:
```
"Flashcards - Claude Certified Architect"
```

---

## Fluxo de Execução

### Fase 0: Solicitar Título (Interativo)

Se executado sem argumentos, a skill pergunta:
```
📖 Qual é o título do livro? 
(padrão: 'Flashcards - Claude Certified Architect'): 
```

### Fase 1: Detectar e Validar Cards

```bash
# Listar todos os cards enriquecidos
find . -maxdepth 1 -name "*-enriched-card.md" -type f | sort
```

Exemplo de output:
```
✅ Cards enriquecidos encontrados: 5
   - 001-enriched-card.md
   - 002-enriched-card.md
   - 003-enriched-card.md
   - 004-enriched-card.md
   - 005-enriched-card.md
```

### Fase 2: Parse de Cada Card

Para cada arquivo `NNN-enriched-card.md`:

1. **Ler o arquivo markdown**
2. **Extrair seções**:
   - Pergunta e opções (antes do primeiro `---`)
   - Seção TRANSLATED QUESTION
   - Seção EXPLANATION (TECH LEAD) 
   - Seção SIMPLE EXPLANATION
   - Seção CORRECT ANSWER

3. **Normalizar conteúdo**:
   - Converter markdown básico para HTML
   - Preservar formatação (negrito, itálico, listas)
   - Escapar caracteres especiais XML

### Fase 3: Criar Estrutura EPUB

O EPUB é um arquivo ZIP com estrutura específica. Você vai criar:

#### 1. Arquivo `mimetype` (sem compressão)
```
application/epub+zip
```

#### 2. Diretório `META-INF/`

**Arquivo: `META-INF/container.xml`**
```xml
<?xml version="1.0" encoding="UTF-8"?>
<container version="1.0" xmlns="urn:oasis:names:tc:opendocument:xmlns:container">
    <rootfiles>
        <rootfile full-path="OEBPS/content.opf" media-type="application/oebps-package+xml"/>
    </rootfiles>
</container>
```

#### 3. Diretório `OEBPS/`

**Arquivo: `OEBPS/content.opf`** (Metadados e Estrutura)
```xml
<?xml version="1.0" encoding="UTF-8"?>
<package xmlns="http://www.idpf.org/2007/opf" version="3.0" unique-identifier="uuid">
    <metadata xmlns:dc="http://purl.org/dc/elements/1.1/">
        <dc:title>Flashcards - Certificação Claude</dc:title>
        <dc:creator>Fabião - Claude Code</dc:creator>
        <dc:language>pt-BR</dc:language>
        <dc:date>[DATA_ATUAL]</dc:date>
        <dc:identifier id="uuid">uuid:[UUID_GERADO]</dc:identifier>
        <meta property="dcterms:modified">[ISO_8601_DATETIME]</meta>
    </metadata>
    <manifest>
        <item id="toc" href="toc.ncx" media-type="application/x-dtbncx+xml"/>
        <item id="styles" href="styles.css" media-type="text/css"/>
        <item id="cover" href="chapters/cover.xhtml" media-type="application/xhtml+xml"/>
        <item id="ch001" href="chapters/001.xhtml" media-type="application/xhtml+xml"/>
        <item id="ch002" href="chapters/002.xhtml" media-type="application/xhtml+xml"/>
        <!-- ... um item para cada capítulo ... -->
    </manifest>
    <spine toc="toc">
        <itemref idref="cover"/>
        <itemref idref="ch001"/>
        <itemref idref="ch002"/>
        <!-- ... referência para cada capítulo ... -->
    </spine>
</package>
```

**Arquivo: `OEBPS/toc.ncx`** (Índice de Navegação)
```xml
<?xml version="1.0" encoding="UTF-8"?>
<ncx xmlns="http://www.daisy.org/z3986/2005/ncx/" version="2005-1">
    <head>
        <meta name="dtb:uid" content="uuid:[UUID_MESMO_DO_OPF]"/>
        <meta name="dtb:depth" content="1"/>
        <meta name="dtb:totalPageCount" content="0"/>
        <meta name="dtb:maxPageNumber" content="0"/>
    </head>
    <docTitle>
        <text>Flashcards - Certificação Claude</text>
    </docTitle>
    <navMap>
        <navPoint id="navpoint-1" playOrder="1">
            <navLabel><text>Capa</text></navLabel>
            <content src="chapters/cover.xhtml"/>
        </navPoint>
        <navPoint id="navpoint-2" playOrder="2">
            <navLabel><text>Card 001: [Preview pergunta]</text></navLabel>
            <content src="chapters/001.xhtml"/>
        </navPoint>
        <!-- ... um navPoint para cada capítulo ... -->
    </navMap>
</ncx>
```

**Arquivo: `OEBPS/styles.css`**
```css
/* Estilos para legibilidade em devices móveis */
body {
    font-family: Georgia, serif;
    line-height: 1.6;
    margin: 1em;
    color: #333;
}

h1 {
    font-size: 1.8em;
    margin-top: 0.5em;
    margin-bottom: 0.5em;
    border-bottom: 2px solid #3498db;
    padding-bottom: 0.3em;
}

h2 {
    font-size: 1.4em;
    margin-top: 0.8em;
    margin-bottom: 0.4em;
    color: #2c3e50;
}

h3 {
    font-size: 1.2em;
    margin-top: 0.6em;
    margin-bottom: 0.3em;
    color: #34495e;
}

.question {
    background-color: #ecf0f1;
    padding: 1em;
    border-left: 4px solid #3498db;
    margin: 0.8em 0;
    font-weight: bold;
}

.options {
    margin-left: 1.5em;
    margin-top: 0.6em;
    line-height: 1.8;
}

.option {
    margin-bottom: 0.4em;
}

.correct-answer {
    background-color: #d5f4e6;
    padding: 0.8em;
    border-left: 4px solid #27ae60;
    margin-top: 1em;
    font-weight: bold;
    color: #27ae60;
}

.explanation {
    background-color: #fef9e7;
    padding: 1em;
    border-left: 4px solid #f39c12;
    margin: 0.8em 0;
    line-height: 1.7;
}

.simple-explanation {
    background-color: #fdeaea;
    padding: 1em;
    border-left: 4px solid #e74c3c;
    margin: 0.8em 0;
    line-height: 1.7;
}

.section-title {
    font-weight: bold;
    color: #2c3e50;
    margin-top: 1em;
    margin-bottom: 0.5em;
    text-transform: uppercase;
    font-size: 0.9em;
    letter-spacing: 1px;
}

p {
    text-align: justify;
    margin-bottom: 0.8em;
}

.page-break {
    page-break-after: always;
}
```

**Arquivos: `OEBPS/chapters/cover.xhtml`** e `OEBPS/chapters/NNN.xhtml`**

Cada capítulo é um arquivo XHTML. Exemplo estrutura:

```xhtml
<?xml version="1.0" encoding="UTF-8"?>
<html xmlns="http://www.w3.org/1999/xhtml" lang="pt-BR">
<head>
    <meta charset="UTF-8"/>
    <title>Card 001</title>
    <link rel="stylesheet" href="../styles.css"/>
</head>
<body>
    <h1>Card 001</h1>
    
    <h2>Original Question (English)</h2>
    <div class="question">
        [Pergunta original em inglês]
    </div>
    <div class="options">
        <div class="option">☐ A - [Opção A]</div>
        <div class="option">☐ B - [Opção B]</div>
        <div class="option">☐ C - [Opção C]</div>
        <div class="option">☐ D - [Opção D]</div>
    </div>

    <h2>Pergunta Traduzida (Português)</h2>
    <div class="question">
        [Pergunta traduzida em português]
    </div>
    <div class="options">
        <div class="option">A) [Opção A traduzida]</div>
        <div class="option">B) [Opção B traduzida]</div>
        <div class="option">C) [Opção C traduzida]</div>
        <div class="option">D) [Opção D traduzida]</div>
    </div>

    <div class="explanation">
        <div class="section-title">Explicação (Tech Lead)</div>
        <p>[Conteúdo da seção EXPLANATION do card markdown]</p>
    </div>

    <div class="simple-explanation">
        <div class="section-title">Explicação Simples</div>
        <p>[Conteúdo da seção SIMPLE EXPLANATION do card markdown]</p>
    </div>

    <div class="correct-answer">
        Resposta Correta: <strong>[LETRA]</strong>
    </div>

    <div class="page-break"></div>
</body>
</html>
```

### Fase 4: Compilar EPUB

O EPUB é um arquivo ZIP especial:

1. **Adicionar `mimetype`** (SEM compressão, UTF-8)
   ```bash
   echo "application/epub+zip" > mimetype
   zip -0 -X flashcards-deck-[DATA].epub mimetype
   ```

2. **Adicionar outros arquivos** (COM compressão)
   ```bash
   zip -r flashcards-deck-[DATA].epub META-INF/ OEBPS/
   ```

3. **Validar estrutura**
   ```bash
   unzip -t flashcards-deck-[DATA].epub
   ```

### Fase 5: Gerar Output

```
✨ EPUB gerado com sucesso!

📱 Arquivo: flashcards-deck-2026-07-18.epub
📊 Cards inclusos: 5
🎨 Tamanho: ~45 KB
📖 Formato: EPUB 3.0 (compatível com Google Play Books)

📥 Para usar no celular:
   1. Copie o arquivo para seu dispositivo
   2. Abra no Google Play Books
   3. Sincronize para ler offline em qualquer lugar
```

## Checklist de Implementação

- [ ] Detectar todos os `*-enriched-card.md`
- [ ] Ordenar numericamente
- [ ] Para cada card:
  - [ ] Ler o arquivo markdown
  - [ ] Extrair seções (pergunta, tradução, explicações, resposta)
  - [ ] Gerar arquivo XHTML formatado
- [ ] Criar diretório temporário para estrutura EPUB
  - [ ] Criar `mimetype`
  - [ ] Criar `META-INF/container.xml`
  - [ ] Criar `OEBPS/content.opf` com todos os metadados
  - [ ] Criar `OEBPS/toc.ncx` com índice navegável
  - [ ] Criar `OEBPS/styles.css`
  - [ ] Criar `OEBPS/chapters/cover.xhtml`
  - [ ] Criar `OEBPS/chapters/NNN.xhtml` para cada card
- [ ] Compilar ZIP especial:
  - [ ] Adicionar `mimetype` sem compressão
  - [ ] Adicionar `META-INF/` e `OEBPS/` com compressão
- [ ] Validar estrutura EPUB
- [ ] Mover arquivo EPUB para raiz do projeto
- [ ] Listar resumo final
- [ ] Confirmar sucesso

## Exemplo de UUID

Use um UUID válido, por exemplo:
```
uuid:12345678-1234-1234-1234-123456789abc
```

Ou gere dinamicamente no seu script (Python/Node.js tem geradores de UUID).

## Data no ISO 8601

Formato esperado: `YYYY-MM-DDTHH:mm:ssZ`

Exemplo: `2026-07-18T14:30:00Z`

## Validação EPUB

Para verificar se o EPUB foi criado corretamente:
```bash
# Ver estrutura interna
unzip -l flashcards-deck-2026-07-18.epub

# Validar (se tiver ferramentas de validação)
epubcheck flashcards-deck-2026-07-18.epub
```

## Validação Automática

A skill agora **valida automaticamente** o EPUB após a geração para garantir compatibilidade total com Google Play Books:

✅ **Verificações automatizadas:**
- ✓ Arquivo `mimetype` presente e correto
- ✓ `META-INF/container.xml` válido
- ✓ `OEBPS/content.opf` com metadados corretos
- ✓ `OEBPS/nav.xhtml` obrigatório (EPUB 3.0) ← **Critical**
- ✓ `OEBPS/toc.ncx` para compatibilidade

Se qualquer validação falhar, a skill **interrompe e exibe o erro** em vez de gerar um arquivo inválido.

## Suporte a Google Play Books

O EPUB 3.0 com estrutura correta é **100% compatível** com:
- ✅ Google Play Books (upload direto)
- ✅ Apple Books
- ✅ Kindle (via conversão)
- ✅ Kobo
- ✅ Calibre
- ✅ Qualquer leitor EPUB moderno

**Como fazer upload no Google Play Books:**
1. Acesse: [Google Play Books Partner Center](https://play.google.com/books/publish)
2. Clique em "Fazer upload de livro"
3. Selecione o arquivo EPUB gerado
4. Aguarde o processamento (geralmente minutos)
5. Pronto! Sincronize no app do celular e leia offline
