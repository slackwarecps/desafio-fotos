#!/usr/bin/env python3
"""
Skill: Exporta Cards Enriquecidos para EPUB
Converte todos os cards enriquecidos (NNN-enriched-card.md) em um arquivo EPUB compatível com leitores de e-book.
"""

import os
import re
import uuid
import shutil
import zipfile
from datetime import datetime

def remove_section_headers(text):
    """Remove headers markdown comuns da seção"""
    text = re.sub(r'^### TRANSLATED QUESTION\s*\n', '', text, flags=re.MULTILINE)
    text = re.sub(r'^### EXPLANATION \(TECH LEAD\)\s*\n', '', text, flags=re.MULTILINE)
    text = re.sub(r'^### SIMPLE EXPLANATION\s*\n', '', text, flags=re.MULTILINE)
    text = re.sub(r'^### CORRECT ANSWER\s*\n', '', text, flags=re.MULTILINE)
    return text.strip()

def markdown_to_html(md_text):
    """Conversão simples de Markdown para HTML básico compatível com EPUB/XHTML"""
    # Escape XML básico
    html = md_text.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
    
    # Negritos: **texto** -> <strong>texto</strong>
    html = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', html)
    
    # Itálicos: *texto* -> <em>texto</em>
    html = re.sub(r'\*(.*?)\*', r'<em>\1</em>', html)
    
    # Código inline: `texto` -> <code>texto</code>
    html = re.sub(r'`(.*?)`', r'<code>\1</code>', html)
    
    # Dividir em parágrafos por linhas em branco
    paragraphs = re.split(r'\n\s*\n', html)
    html_paragraphs = []
    
    for p in paragraphs:
        p = p.strip()
        if not p:
            continue
        
        # Tratar listas (linhas começando com - ou *)
        lines = p.split('\n')
        in_list = False
        list_items = []
        normal_lines = []
        
        for line in lines:
            line_strip = line.strip()
            if line_strip.startswith('- ') or line_strip.startswith('* '):
                if not in_list:
                    # Se havia linhas normais antes, adiciona como parágrafo
                    if normal_lines:
                        html_paragraphs.append(f"<p>{'<br/>'.join(normal_lines)}</p>")
                        normal_lines = []
                    in_list = True
                content = line_strip[2:]
                list_items.append(f"<li>{content}</li>")
            else:
                if in_list:
                    # Fecha a lista atual
                    html_paragraphs.append(f"<ul>{''.join(list_items)}</ul>")
                    list_items = []
                    in_list = False
                normal_lines.append(line)
        
        if in_list:
            html_paragraphs.append(f"<ul>{''.join(list_items)}</ul>")
        elif normal_lines:
            html_paragraphs.append(f"<p>{'<br/>'.join(normal_lines)}</p>")
            
    return '\n'.join(html_paragraphs)

def parse_card(card_file):
    """Faz o parse de um card enriquecido markdown para extrair as seções estruturadas"""
    with open(card_file, 'r', encoding='utf-8') as f:
        full_content = f.read()
    
    # Separar seções baseando-se no delimitador '---'
    sections = re.split(r'^---\s*$', full_content, flags=re.MULTILINE)
    
    original_question = sections[0].strip() if len(sections) > 0 else ""
    english_options = sections[1].strip() if len(sections) > 1 else ""
    
    # Limpar cabeçalhos das outras seções
    translated_section = remove_section_headers(sections[2].strip() if len(sections) > 2 else "")
    explanation_section = remove_section_headers(sections[3].strip() if len(sections) > 3 else "")
    simple_section = remove_section_headers(sections[4].strip() if len(sections) > 4 else "")
    correct_answer_section = remove_section_headers(sections[5].strip() if len(sections) > 5 else "")
    
    # Formatar opções em inglês
    options_html = []
    for line in english_options.split('\n'):
        line = line.strip()
        if line.startswith('[ ]'):
            options_html.append(f'<div class="option">☐ {line[3:].strip()}</div>')
        elif line:
            options_html.append(f'<div class="option">{line}</div>')
            
    # Obter preview da pergunta original para o índice (primeiras palavras)
    preview = re.sub(r'^(Scenario:\s*|Question:\s*)', '', original_question)
    preview = preview.split('.')[0] # pega a primeira frase
    if len(preview) > 50:
        preview = preview[:47] + "..."
        
    return {
        "original_question": markdown_to_html(original_question),
        "english_options": '\n'.join(options_html),
        "translated_question": markdown_to_html(translated_section),
        "explanation": markdown_to_html(explanation_section),
        "simple_explanation": markdown_to_html(simple_section),
        "correct_answer": correct_answer_section.replace("Alternativa Correta:", "").strip(),
        "preview": preview
    }

def build_epub(cards, output_epub_path):
    """Gera o arquivo EPUB com a estrutura correta"""
    # Criar estrutura temporária
    temp_dir = "outputs/epub_temp"
    os.makedirs(temp_dir, exist_ok=True)
    os.makedirs(f"{temp_dir}/META-INF", exist_ok=True)
    os.makedirs(f"{temp_dir}/OEBPS", exist_ok=True)
    os.makedirs(f"{temp_dir}/OEBPS/chapters", exist_ok=True)
    
    # 1. Arquivo mimetype (Sem compressão)
    with open(f"{temp_dir}/mimetype", "w", encoding="utf-8") as f:
        f.write("application/epub+zip")
        
    # 2. Arquivo META-INF/container.xml
    container_xml = """<?xml version="1.0" encoding="UTF-8"?>
<container version="1.0" xmlns="urn:oasis:names:tc:opendocument:xmlns:container">
    <rootfiles>
        <rootfile full-path="OEBPS/content.opf" media-type="application/oebps-package+xml"/>
    </rootfiles>
</container>"""
    with open(f"{temp_dir}/META-INF/container.xml", "w", encoding="utf-8") as f:
        f.write(container_xml)
        
    # 3. Arquivo OEBPS/styles.css
    styles_css = """body {
    font-family: Georgia, serif;
    line-height: 1.6;
    margin: 1em;
    color: #333;
}

h1 {
    font-size: 1.6em;
    margin-top: 0.5em;
    margin-bottom: 0.5em;
    border-bottom: 2px solid #3498db;
    padding-bottom: 0.3em;
    color: #1f4788;
}

h2 {
    font-size: 1.2em;
    margin-top: 0.8em;
    margin-bottom: 0.4em;
    color: #2c3e50;
    border-bottom: 1px solid #ddd;
    padding-bottom: 0.2em;
}

.question {
    background-color: #f8f9fa;
    padding: 1em;
    border-left: 4px solid #3498db;
    margin: 0.8em 0;
    font-style: italic;
}

.options {
    margin-left: 1em;
    margin-top: 0.6em;
    margin-bottom: 1em;
}

.option {
    margin-bottom: 0.5em;
}

.explanation {
    background-color: #fdf6e3;
    padding: 1em;
    border-left: 4px solid #b58900;
    margin: 0.8em 0;
}

.simple-explanation {
    background-color: #f4f9f4;
    padding: 1em;
    border-left: 4px solid #2ea44f;
    margin: 0.8em 0;
}

.correct-answer {
    background-color: #e6f4ea;
    padding: 0.8em;
    border-left: 4px solid #137333;
    margin-top: 1em;
    font-weight: bold;
    color: #137333;
}

.section-title {
    font-weight: bold;
    color: #2c3e50;
    margin-bottom: 0.5em;
    text-transform: uppercase;
    font-size: 0.85em;
    letter-spacing: 1px;
}

p {
    margin-bottom: 0.8em;
}

ul {
    margin-top: 0.4em;
    margin-bottom: 0.6em;
    padding-left: 1.5em;
}

li {
    margin-bottom: 0.3em;
}
"""
    with open(f"{temp_dir}/OEBPS/styles.css", "w", encoding="utf-8") as f:
        f.write(styles_css)
        
    # Processar cada card
    parsed_cards = []
    for idx, card_file in enumerate(cards, 1):
        num_str = f"{idx:03d}"
        card_data = parse_card(card_file)
        card_data["num"] = num_str
        parsed_cards.append(card_data)
        
        # Gerar XHTML do capítulo
        chapter_xhtml = f"""<?xml version="1.0" encoding="UTF-8"?>
<html xmlns="http://www.w3.org/1999/xhtml" lang="pt-BR">
<head>
    <meta charset="UTF-8"/>
    <title>Questão {num_str}</title>
    <link rel="stylesheet" href="../styles.css" type="text/css"/>
</head>
<body>
    <h1>Questão {num_str}</h1>
    
    <h2>Original Question (English)</h2>
    <div class="question">
        {card_data["original_question"]}
    </div>
    <div class="options">
        {card_data["english_options"]}
    </div>

    <h2>Pergunta Traduzida (Português)</h2>
    <div class="question">
        {card_data["translated_question"]}
    </div>

    <div class="explanation">
        <div class="section-title">Explicação (Tech Lead)</div>
        {card_data["explanation"]}
    </div>

    <div class="simple-explanation">
        <div class="section-title">🧒 Explicação Simples</div>
        {card_data["simple_explanation"]}
    </div>

    <div class="correct-answer">
        Resposta Correta: {card_data["correct_answer"]}
    </div>
</body>
</html>"""
        with open(f"{temp_dir}/OEBPS/chapters/{num_str}.xhtml", "w", encoding="utf-8") as f:
            f.write(chapter_xhtml)
            
    # Capa
    cover_xhtml = f"""<?xml version="1.0" encoding="UTF-8"?>
<html xmlns="http://www.w3.org/1999/xhtml" lang="pt-BR">
<head>
    <meta charset="UTF-8"/>
    <title>Capa</title>
    <link rel="stylesheet" href="../styles.css" type="text/css"/>
    <style>
        .cover-container {{
            text-align: center;
            margin-top: 3em;
        }}
        .cover-title {{
            font-size: 2.2em;
            color: #1f4788;
            margin-bottom: 0.5em;
            border: none;
            padding: 0;
        }}
        .cover-subtitle {{
            font-size: 1.2em;
            color: #555;
            margin-bottom: 2em;
        }}
        .cover-meta {{
            margin-top: 4em;
            font-size: 0.9em;
            color: #777;
        }}
    </style>
</head>
<body>
    <div class="cover-container">
        <h1 class="cover-title">Flashcards Deck</h1>
        <div class="cover-subtitle">Claude Certified Architect - Foundations</div>
        
        <div class="cover-meta">
            <p><strong>Total de Questões:</strong> {len(cards)}</p>
            <p><strong>Data de Geração:</strong> {datetime.now().strftime('%d/%m/%Y')}</p>
            <p><strong>Criado por:</strong> Antigravity &amp; Fabão</p>
        </div>
    </div>
</body>
</html>"""
    with open(f"{temp_dir}/OEBPS/chapters/cover.xhtml", "w", encoding="utf-8") as f:
        f.write(cover_xhtml)
        
    # 4. Arquivo OEBPS/content.opf
    book_uuid = str(uuid.uuid4())
    datetime_iso = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
    
    # Manifest
    manifest_items = [
        '<item id="styles" href="styles.css" media-type="text/css"/>',
        '<item id="toc" href="toc.ncx" media-type="application/x-dtbncx+xml"/>',
        '<item id="cover" href="chapters/cover.xhtml" media-type="application/xhtml+xml"/>'
    ]
    for c in parsed_cards:
        manifest_items.append(f'<item id="ch{c["num"]}" href="chapters/{c["num"]}.xhtml" media-type="application/xhtml+xml"/>')
        
    # Spine
    spine_items = [
        '<itemref idref="cover"/>'
    ]
    for c in parsed_cards:
        spine_items.append(f'<itemref idref="ch{c["num"]}"/>')
        
    content_opf = f"""<?xml version="1.0" encoding="UTF-8"?>
<package xmlns="http://www.idpf.org/2007/opf" version="3.0" unique-identifier="uuid">
    <metadata xmlns:dc="http://purl.org/dc/elements/1.1/">
        <dc:title>Flashcards - Certificação Claude</dc:title>
        <dc:creator>Fabiao</dc:creator>
        <dc:language>pt-BR</dc:language>
        <dc:date>{datetime.now().strftime('%Y-%m-%d')}</dc:date>
        <dc:identifier id="uuid">uuid:{book_uuid}</dc:identifier>
        <meta property="dcterms:modified">{datetime_iso}</meta>
    </metadata>
    <manifest>
        {"\n        ".join(manifest_items)}
    </manifest>
    <spine toc="toc">
        {"\n        ".join(spine_items)}
    </spine>
</package>"""
    with open(f"{temp_dir}/OEBPS/content.opf", "w", encoding="utf-8") as f:
        f.write(content_opf)
        
    # 5. Arquivo OEBPS/toc.ncx
    nav_points = [
        f"""<navPoint id="navpoint-cover" playOrder="1">
            <navLabel><text>Capa</text></navLabel>
            <content src="chapters/cover.xhtml"/>
        </navPoint>"""
    ]
    for idx, c in enumerate(parsed_cards, 2):
        nav_points.append(f"""<navPoint id="navpoint-{c["num"]}" playOrder="{idx}">
            <navLabel><text>Questão {c["num"]}: {c["preview"]}</text></navLabel>
            <content src="chapters/{c["num"]}.xhtml"/>
        </navPoint>""")
        
    toc_ncx = f"""<?xml version="1.0" encoding="UTF-8"?>
<ncx xmlns="http://www.daisy.org/z3986/2005/ncx/" version="2005-1">
    <head>
        <meta name="dtb:uid" content="uuid:{book_uuid}"/>
        <meta name="dtb:depth" content="1"/>
        <meta name="dtb:totalPageCount" content="0"/>
        <meta name="dtb:maxPageNumber" content="0"/>
    </head>
    <docTitle>
        <text>Flashcards - Certificação Claude</text>
    </docTitle>
    <navMap>
        {"\n        ".join(nav_points)}
    </navMap>
</ncx>"""
    with open(f"{temp_dir}/OEBPS/toc.ncx", "w", encoding="utf-8") as f:
        f.write(toc_ncx)
        
    # 6. Criar ZIP / EPUB
    with zipfile.ZipFile(output_epub_path, 'w', zipfile.ZIP_DEFLATED) as epub:
        # Escrever mimetype sem compressão
        epub.write(f"{temp_dir}/mimetype", "mimetype", compress_type=zipfile.ZIP_STORED)
        
        # Adicionar os outros diretórios recursivamente
        for root, _, files in os.walk(f"{temp_dir}"):
            for file in files:
                full_path = os.path.join(root, file)
                rel_path = os.path.relpath(full_path, temp_dir)
                if rel_path == "mimetype":
                    continue
                epub.write(full_path, rel_path, compress_type=zipfile.ZIP_DEFLATED)
                
    # Limpeza
    shutil.rmtree(temp_dir)

def main():
    """Ponto de entrada do script"""
    os.makedirs("outputs", exist_ok=True)
    today = datetime.now().strftime("%Y-%m-%d")
    output_epub = f"outputs/flashcards-deck-{today}.epub"
    
    # Encontrar cards enriquecidos apenas no diretório raiz
    cards = sorted([f for f in os.listdir(".") if re.match(r"\d{3}-enriched-card\.md$", f)])
    
    print("📚 Gerando EPUB...")
    
    if not cards:
        print("❌ Nenhum card enriquecido (*-enriched-card.md) encontrado no diretório raiz!")
        return
        
    print(f"✅ Cards encontrados: {len(cards)}")
    for card in cards:
        print(f"   - {card}")
        
    print("\n📖 Estruturando EPUB...")
    print("✅ Formatando cards como capítulos")
    print("✅ Criando índice navegável")
    
    try:
        build_epub(cards, output_epub)
        print("✅ Compilando arquivo EPUB")
        
        # Criar uma cópia do arquivo EPUB na raiz para o usuário também
        root_epub = f"flashcards-deck-{today}.epub"
        shutil.copy2(output_epub, root_epub)
        
        epub_size = os.path.getsize(root_epub) / 1024
        
        print("\n✨ Concluído!")
        print(f"Arquivos gerados:")
        print(f"- {output_epub} (na pasta outputs)")
        print(f"- {root_epub} (na raiz do projeto, {epub_size:.1f} KB)")
        
        print("\n📱 Próximos passos:")
        print("   1. Copie o arquivo para seu celular")
        print("   2. Abra no Google Play Books")
        print("   3. Estude offline em qualquer lugar")
        
    except Exception as e:
        print(f"❌ Erro ao compilar EPUB: {e}")

if __name__ == "__main__":
    main()
