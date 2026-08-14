#!/usr/bin/env python3
"""
Skill: Exporta Cards Enriquecidos para EPUB
Consolida todos os cards enriquecidos (NNN-enriched-card.md) em um único arquivo EPUB
compatível com Google Play Books, Apple Books, Kindle, etc.
"""

import os
import re
import sys
import uuid
import shutil
import zipfile
import tempfile
from datetime import datetime
from pathlib import Path
from xml.etree import ElementTree as ET

def escape_xml(text):
    """Escapa caracteres especiais XML preservando UTF-8"""
    return (text
            .replace('&', '&amp;')
            .replace('<', '&lt;')
            .replace('>', '&gt;')
            .replace('"', '&quot;')
            .replace("'", '&#39;'))

def sanitize_filename(filename):
    """Sanitiza string para ser usada como nome de arquivo válido"""
    # Remove/substitui caracteres inválidos em nomes de arquivo
    filename = re.sub(r'[<>:"/\\|?*]', '-', filename)
    # Remove espaços múltiplos
    filename = re.sub(r'\s+', ' ', filename).strip()
    # Limita o tamanho
    filename = filename[:100]
    return filename

def remove_section_headers(text):
    """Remove headers como ### TRANSLATED QUESTION, ### EXPLANATION, etc"""
    text = re.sub(r'^### TRANSLATED QUESTION\s*\n', '', text, flags=re.MULTILINE)
    text = re.sub(r'^### EXPLANATION \(TECH LEAD\)\s*\n', '', text, flags=re.MULTILINE)
    text = re.sub(r'^### SIMPLE EXPLANATION\s*\n', '', text, flags=re.MULTILINE)
    text = re.sub(r'^Explicação Técnica:\s*\n', '', text, flags=re.MULTILINE)
    text = re.sub(r'^Explicação para Aprendizes:\s*\n', '', text, flags=re.MULTILINE)
    return text.strip()

def markdown_to_html(text):
    """Converte markdown básico para HTML com suporte a UTF-8"""
    # Bold
    text = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', text)
    # Itálico
    text = re.sub(r'\*(.+?)\*', r'<em>\1</em>', text)
    return text

def generate_styles_css():
    """Gera CSS otimizado para EPUB móvel com fontes menores"""
    return """/* Estilos para Flashcards EPUB - Otimizado para dispositivos móveis com fontes compactas */

* {
    margin: 0;
    padding: 0;
}

html, body {
    font-family: 'Georgia', 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    font-size: 0.95em;
    line-height: 1.5;
    color: #333;
    background-color: #fff;
}

body {
    margin: 0.6em;
    padding: 0;
}

h1 {
    font-size: 1.3em;
    margin-top: 0.2em;
    margin-bottom: 0.4em;
    border-bottom: 2px solid #1f4788;
    padding-bottom: 0.3em;
    color: #1f4788;
    page-break-after: avoid;
}

h2 {
    font-size: 1.1em;
    margin-top: 0.5em;
    margin-bottom: 0.3em;
    color: #2c5aa0;
    page-break-after: avoid;
}

h3 {
    font-size: 1em;
    margin-top: 0.4em;
    margin-bottom: 0.2em;
    color: #34495e;
    page-break-after: avoid;
}

.question {
    background-color: #ecf0f1;
    padding: 0.6em;
    border-left: 4px solid #1f4788;
    margin: 0.5em 0;
    font-weight: normal;
    font-size: 0.9em;
    page-break-inside: avoid;
}

.options {
    margin-top: 0.4em;
    line-height: 1.5;
    font-size: 0.9em;
}

.option {
    margin-bottom: 0.3em;
    margin-left: 0;
    padding-left: 0;
}

.correct-answer {
    background-color: #d5f4e6;
    padding: 0.6em;
    border-left: 4px solid #27ae60;
    margin-top: 0.6em;
    font-weight: bold;
    color: #27ae60;
    font-size: 0.9em;
    page-break-inside: avoid;
}

.explanation {
    background-color: #fef9e7;
    padding: 0.6em;
    border-left: 4px solid #f39c12;
    margin: 0.5em 0;
    line-height: 1.5;
    font-size: 0.9em;
}

.simple-explanation {
    background-color: #fdeaea;
    padding: 0.6em;
    border-left: 4px solid #e74c3c;
    margin: 0.5em 0;
    line-height: 1.5;
    font-size: 0.9em;
}

.section-title {
    font-weight: bold;
    color: #2c3e50;
    margin-top: 0.6em;
    margin-bottom: 0.3em;
    text-transform: uppercase;
    font-size: 0.8em;
    letter-spacing: 0.5px;
    page-break-after: avoid;
}

.translated-section {
    background-color: #f0f8ff;
    padding: 0.6em;
    border-left: 4px solid #3498db;
    margin: 0.5em 0;
    line-height: 1.5;
    font-size: 0.9em;
}

p {
    margin-bottom: 0.5em;
    text-align: justify;
}

strong {
    font-weight: bold;
}

em {
    font-style: italic;
}

.page-break {
    page-break-after: always;
}

.cover {
    text-align: center;
    padding: 1.5em 0.8em;
}

.cover h1 {
    border: none;
    margin-top: 1em;
    margin-bottom: 0.8em;
    font-size: 1.6em;
}

.cover p {
    font-size: 0.95em;
    margin-bottom: 0.4em;
    text-align: center;
    line-height: 1.4;
}
"""

def generate_xhtml_question(card_number, total_cards, sections):
    """Gera XHTML apenas da pergunta (página 1 de cada card) - Inglês como padrão"""
    try:
        original_question = sections[0].strip() if len(sections) > 0 else ""
        english_options = sections[1].strip() if len(sections) > 1 else ""
    except IndexError:
        return None

    # Processar opções em inglês
    english_lines = english_options.split('\n')
    english_options_html = []
    for line in english_lines:
        if line.strip().startswith('[ ]'):
            # Remove [ ] e adiciona ☐
            option_text = line.strip()[3:].strip()
            english_options_html.append(f'        <div class="option">☐ {escape_xml(option_text)}</div>')

    # Montar XHTML
    xhtml = f"""<?xml version="1.0" encoding="UTF-8"?>
<html xmlns="http://www.w3.org/1999/xhtml" lang="en-US">
<head>
    <meta charset="UTF-8"/>
    <title>Question {card_number:03d}</title>
    <link rel="stylesheet" href="../styles.css"/>
</head>
<body>
    <h1>Question {card_number:03d}/{total_cards}</h1>

    <h2>Original Question (English)</h2>
    <div class="question">
        {escape_xml(original_question)}
    </div>
    <div class="options">
{chr(10).join(english_options_html)}
    </div>
</body>
</html>
"""
    return xhtml

def generate_xhtml_answer(card_number, total_cards, sections):
    """Gera XHTML apenas da resposta (página 2 de cada card) - Inglês padrão, português marcado"""
    try:
        translated_section = remove_section_headers(sections[2].strip() if len(sections) > 2 else "")
        explanation_section = remove_section_headers(sections[3].strip() if len(sections) > 3 else "")
        simple_section = remove_section_headers(sections[4].strip() if len(sections) > 4 else "")
        correct_answer_section = sections[5].strip() if len(sections) > 5 else ""
    except IndexError:
        return None

    # Processar seções de tradução
    translated_html = markdown_to_html(escape_xml(translated_section))
    explanation_html = markdown_to_html(escape_xml(explanation_section))
    simple_html = markdown_to_html(escape_xml(simple_section))

    # Montar XHTML
    xhtml = f"""<?xml version="1.0" encoding="UTF-8"?>
<html xmlns="http://www.w3.org/1999/xhtml" lang="en-US">
<head>
    <meta charset="UTF-8"/>
    <title>Answer {card_number:03d}</title>
    <link rel="stylesheet" href="../styles.css"/>
</head>
<body>
    <h1>Question {card_number:03d} - Answer</h1>

    <h2 lang="pt-BR">Pergunta Traduzida (Português)</h2>
    <div class="translated-section" lang="pt-BR">
        {translated_html}
    </div>

    <div class="explanation" lang="pt-BR">
        <div class="section-title">Explicação (Tech Lead)</div>
        {explanation_html}
    </div>

    <div class="simple-explanation" lang="pt-BR">
        <div class="section-title">Explicação Simples</div>
        {simple_html}
    </div>

    <div class="correct-answer" lang="pt-BR">
        ✅ Resposta Correta: <strong>{escape_xml(correct_answer_section.replace('### CORRECT ANSWER', '').strip())}</strong>
    </div>
</body>
</html>
"""
    return xhtml

def generate_cover_xhtml(book_title):
    """Gera página de capa XHTML - Inglês padrão"""
    today = datetime.now().strftime("%d de %B de %Y")
    return f"""<?xml version="1.0" encoding="UTF-8"?>
<html xmlns="http://www.w3.org/1999/xhtml" lang="en-US">
<head>
    <meta charset="UTF-8"/>
    <title>Cover</title>
    <link rel="stylesheet" href="../styles.css"/>
</head>
<body>
    <div class="cover">
        <h1>{escape_xml(book_title)}</h1>
        <p style="margin-top: 2em;" lang="pt-BR">Preparado para estudar arquitetura de sistemas e design patterns</p>
        <p style="margin-top: 2em; font-size: 0.9em;" lang="pt-BR">Gerado em {today}</p>
        <p style="margin-top: 3em; font-size: 0.85em; color: #666;">Compatible with Google Play Books, Apple Books, Kindle and other EPUB readers</p>
        <div class="page-break"></div>
    </div>
</body>
</html>
"""

def generate_nav_xhtml(total_cards, book_title):
    """Gera OEBPS/nav.xhtml - Navegação EPUB 3.0 obrigatória - Inglês padrão"""
    nav_items = """        <li><a href="chapters/cover.xhtml">Cover</a></li>
"""

    for i in range(1, total_cards + 1):
        nav_items += f'        <li><a href="chapters/q{i:03d}.xhtml">Question {i:03d}</a></li>\n'
        nav_items += f'        <li><a href="chapters/a{i:03d}.xhtml">Answer {i:03d}</a></li>\n'

    return f"""<?xml version="1.0" encoding="UTF-8"?>
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops" lang="en-US">
<head>
    <meta charset="UTF-8"/>
    <title>Table of Contents</title>
    <link rel="stylesheet" href="styles.css"/>
</head>
<body>
    <nav epub:type="toc" id="toc">
        <h1>Table of Contents</h1>
        <ol>
{nav_items}        </ol>
    </nav>
    <nav epub:type="landmarks" id="landmarks" hidden="">
        <h1>Landmarks</h1>
        <ol>
            <li><a epub:type="bodymatter" href="chapters/cover.xhtml">Start</a></li>
        </ol>
    </nav>
</body>
</html>
"""

def generate_container_xml():
    """Gera META-INF/container.xml"""
    return """<?xml version="1.0" encoding="UTF-8"?>
<container version="1.0" xmlns="urn:oasis:names:tc:opendocument:xmlns:container">
    <rootfiles>
        <rootfile full-path="OEBPS/content.opf" media-type="application/oebps-package+xml"/>
    </rootfiles>
</container>
"""

def generate_toc_ncx(epub_uuid, total_cards, book_title):
    """Gera OEBPS/toc.ncx com índice navegável"""
    uuid_str = str(epub_uuid)

    nav_points = """        <navPoint id="navpoint-1" playOrder="1">
            <navLabel><text>Cover</text></navLabel>
            <content src="chapters/cover.xhtml"/>
        </navPoint>
"""

    play_order = 2
    for i in range(1, total_cards + 1):
        nav_points += f"""        <navPoint id="navpoint-{play_order}" playOrder="{play_order}">
            <navLabel><text>Question {i:03d}</text></navLabel>
            <content src="chapters/q{i:03d}.xhtml"/>
        </navPoint>
"""
        play_order += 1
        nav_points += f"""        <navPoint id="navpoint-{play_order}" playOrder="{play_order}">
            <navLabel><text>Answer {i:03d}</text></navLabel>
            <content src="chapters/a{i:03d}.xhtml"/>
        </navPoint>
"""
        play_order += 1

    return f"""<?xml version="1.0" encoding="UTF-8"?>
<ncx xmlns="http://www.daisy.org/z3986/2005/ncx/" version="2005-1">
    <head>
        <meta name="dtb:uid" content="uuid:{uuid_str}"/>
        <meta name="dtb:depth" content="1"/>
        <meta name="dtb:totalPageCount" content="0"/>
        <meta name="dtb:maxPageNumber" content="0"/>
    </head>
    <docTitle xml:lang="en-US">
        <text>{escape_xml(book_title)}</text>
    </docTitle>
    <navMap>
{nav_points}    </navMap>
</ncx>
"""

def generate_content_opf(epub_uuid, total_cards, today_iso, book_title):
    """Gera OEBPS/content.opf com metadados e estrutura - EPUB 3.0 compatível Google Play Books - Inglês padrão"""
    uuid_str = str(epub_uuid)

    manifest_items = """        <item id="ncx" href="toc.ncx" media-type="application/x-dtbncx+xml"/>
        <item id="nav" href="nav.xhtml" media-type="application/xhtml+xml" properties="nav"/>
        <item id="styles" href="styles.css" media-type="text/css"/>
        <item id="cover" href="chapters/cover.xhtml" media-type="application/xhtml+xml"/>
"""

    for i in range(1, total_cards + 1):
        manifest_items += f'        <item id="q{i:03d}" href="chapters/q{i:03d}.xhtml" media-type="application/xhtml+xml"/>\n'
        manifest_items += f'        <item id="a{i:03d}" href="chapters/a{i:03d}.xhtml" media-type="application/xhtml+xml"/>\n'

    spine_items = """        <itemref idref="cover"/>
"""

    for i in range(1, total_cards + 1):
        spine_items += f'        <itemref idref="q{i:03d}"/>\n'
        spine_items += f'        <itemref idref="a{i:03d}"/>\n'

    return f"""<?xml version="1.0" encoding="UTF-8"?>
<package xmlns="http://www.idpf.org/2007/opf"
         xmlns:dc="http://purl.org/dc/elements/1.1/"
         unique-identifier="uuid_id"
         version="3.0"
         xml:lang="en-US">
    <metadata>
        <dc:identifier id="uuid_id">uuid:{uuid_str}</dc:identifier>
        <dc:title>{escape_xml(book_title)}</dc:title>
        <dc:creator>Fabião - Claude Code</dc:creator>
        <dc:language>en-US</dc:language>
        <dc:rights>© 2026 - All rights reserved</dc:rights>
        <dc:publisher>Claude Code</dc:publisher>
        <dc:date>{today_iso}</dc:date>
        <meta property="dcterms:modified">{today_iso}</meta>
        <meta name="cover" content="cover"/>
    </metadata>
    <manifest>
{manifest_items}    </manifest>
    <spine toc="ncx">
{spine_items}    </spine>
</package>
"""

def validate_epub_structure(epub_path):
    """Valida estrutura do EPUB para garantir compatibilidade com Google Play Books"""
    issues = []
    with tempfile.TemporaryDirectory() as tmpdir:
        with zipfile.ZipFile(epub_path, 'r') as zip_ref:
            zip_ref.extractall(tmpdir)

        # Verificar mimetype
        mimetype_path = os.path.join(tmpdir, 'mimetype')
        if not os.path.exists(mimetype_path):
            issues.append("❌ mimetype não encontrado")
        else:
            with open(mimetype_path) as f:
                if f.read().strip() != "application/epub+zip":
                    issues.append("❌ mimetype incorreto")

        # Verificar container.xml
        if not os.path.exists(os.path.join(tmpdir, 'META-INF/container.xml')):
            issues.append("❌ container.xml não encontrado")

        # Verificar content.opf
        opf_path = os.path.join(tmpdir, 'OEBPS/content.opf')
        if not os.path.exists(opf_path):
            issues.append("❌ content.opf não encontrado")

        # Verificar nav.xhtml (CRÍTICO para EPUB 3.0 e Google Play Books)
        nav_path = os.path.join(tmpdir, 'OEBPS/nav.xhtml')
        if not os.path.exists(nav_path):
            issues.append("❌ CRÍTICO: nav.xhtml não encontrado (obrigatório EPUB 3.0)")

        # Verificar toc.ncx (compatibilidade)
        toc_path = os.path.join(tmpdir, 'OEBPS/toc.ncx')
        if not os.path.exists(toc_path):
            issues.append("⚠️  toc.ncx não encontrado (recomendado)")

    return issues

def main():
    """Função principal"""
    # Criar diretório outputs se não existir
    os.makedirs("outputs", exist_ok=True)

    # Perguntar título do livro (com suporte a stdin e variável de ambiente)
    print("=" * 60)
    print("📚 Exportador de Cards Enriquecidos para EPUB")
    print("=" * 60)

    # Tentar obter título de: argumento CLI > variável de ambiente > input interativo > padrão
    book_title = None

    # Verificar argumentos de linha de comando
    if len(sys.argv) > 1:
        book_title = " ".join(sys.argv[1:]).strip()

    # Verificar variável de ambiente
    if not book_title:
        book_title = os.environ.get("BOOK_TITLE", "").strip()

    # Tentar input interativo (se disponível)
    if not book_title:
        try:
            book_title = input("\n📖 Qual é o título do livro? (padrão: 'Flashcards - Claude Certified Architect'): ").strip()
        except EOFError:
            # Sem stdin disponível
            book_title = ""

    # Usar padrão se vazio
    if not book_title:
        book_title = "Flashcards - Claude Certified Architect"

    print(f"\n✅ Título configurado: {book_title}\n")

    # Data para nomes de arquivo
    today = datetime.now()
    today_str = today.strftime("%Y-%m-%d")
    today_iso = today.strftime("%Y-%m-%dT%H:%M:%SZ")

    # UUID único para este EPUB
    epub_uuid = uuid.uuid4()

    # Sanitizar título para usar no nome do arquivo
    filename_safe_title = sanitize_filename(book_title)
    output_epub = f"outputs/{filename_safe_title}-{today_str}.epub"
    temp_dir = "/tmp/epub_build"

    # Encontrar cards enriquecidos (busca em absoluto > relativo > raiz)
    cards_dir = "/Users/fabioalvaropereira/Desktop/desafio-fotos/outputs/cards-enriquecidos"
    if not os.path.exists(cards_dir):
        cards_dir = "outputs/cards-enriquecidos"
    if not os.path.exists(cards_dir):
        cards_dir = "."
    
    cards = sorted([os.path.join(cards_dir, f) for f in os.listdir(cards_dir) if re.match(r"\d{3}-enriched-card\.md$", f)])

    print(f"✅ Detectados cards enriquecidos em '{cards_dir}':")
    for card in cards:
        print(f"   - {os.path.basename(card)}")

    if not cards:
        print(f"❌ Nenhum card enriquecido encontrado em '{cards_dir}'!")
        return

    # Limpar diretório temporário anterior
    if os.path.exists(temp_dir):
        shutil.rmtree(temp_dir)

    # Criar estrutura de diretórios
    os.makedirs(f"{temp_dir}/META-INF", exist_ok=True)
    os.makedirs(f"{temp_dir}/OEBPS/chapters", exist_ok=True)

    print(f"\n📖 Estruturando EPUB...")

    # 1. Criar mimetype (sem compressão)
    with open(f"{temp_dir}/mimetype", "w", encoding="utf-8") as f:
        f.write("application/epub+zip")

    # 2. Criar META-INF/container.xml
    with open(f"{temp_dir}/META-INF/container.xml", "w", encoding="utf-8") as f:
        f.write(generate_container_xml())

    # 3. Criar OEBPS/styles.css
    with open(f"{temp_dir}/OEBPS/styles.css", "w", encoding="utf-8") as f:
        f.write(generate_styles_css())

    # 4. Criar OEBPS/toc.ncx
    with open(f"{temp_dir}/OEBPS/toc.ncx", "w", encoding="utf-8") as f:
        f.write(generate_toc_ncx(epub_uuid, len(cards), book_title))

    # 5. Criar OEBPS/nav.xhtml (EPUB 3.0 obrigatório)
    with open(f"{temp_dir}/OEBPS/nav.xhtml", "w", encoding="utf-8") as f:
        f.write(generate_nav_xhtml(len(cards), book_title))

    # 6. Criar OEBPS/content.opf
    with open(f"{temp_dir}/OEBPS/content.opf", "w", encoding="utf-8") as f:
        f.write(generate_content_opf(epub_uuid, len(cards), today_iso, book_title))

    # 7. Criar capa
    with open(f"{temp_dir}/OEBPS/chapters/cover.xhtml", "w", encoding="utf-8") as f:
        f.write(generate_cover_xhtml(book_title))

    print("   ✓ Estrutura EPUB criada (EPUB 3.0 com nav.xhtml)")

    # 8. Processar cada card (pergunta + resposta em arquivos separados)
    print(f"   ✓ Processando {len(cards)} cards (pergunta + resposta)...")
    for idx, card_file in enumerate(cards, 1):
        try:
            with open(card_file, 'r', encoding='utf-8') as f:
                full_content = f.read()

            # Extrair seções pelo padrão ---
            sections = re.split(r'^---\s*$', full_content, flags=re.MULTILINE)

            # Gerar XHTML da pergunta
            question_xhtml = generate_xhtml_question(idx, len(cards), sections)
            if question_xhtml:
                with open(f"{temp_dir}/OEBPS/chapters/q{idx:03d}.xhtml", "w", encoding="utf-8") as f:
                    f.write(question_xhtml)

            # Gerar XHTML da resposta
            answer_xhtml = generate_xhtml_answer(idx, len(cards), sections)
            if answer_xhtml:
                with open(f"{temp_dir}/OEBPS/chapters/a{idx:03d}.xhtml", "w", encoding="utf-8") as f:
                    f.write(answer_xhtml)
        except Exception as e:
            print(f"   ⚠️  Erro ao processar {card_file}: {e}")

    # 9. Compilar EPUB (arquivo ZIP especial)
    print(f"\n📦 Compilando EPUB...")

    if os.path.exists(output_epub):
        os.remove(output_epub)

    with zipfile.ZipFile(output_epub, 'w', zipfile.ZIP_DEFLATED) as epub:
        # Adicionar mimetype sem compressão
        epub.write(f"{temp_dir}/mimetype", "mimetype", compress_type=zipfile.ZIP_STORED)

        # Adicionar META-INF e OEBPS com compressão
        for root, dirs, files in os.walk(f"{temp_dir}"):
            for file in files:
                if file == "mimetype":
                    continue
                file_path = os.path.join(root, file)
                arcname = file_path.replace(f"{temp_dir}/", "")
                epub.write(file_path, arcname, compress_type=zipfile.ZIP_DEFLATED)

    # 10. Validação da estrutura EPUB
    print(f"\n✅ Validando estrutura EPUB...")
    validation_issues = validate_epub_structure(output_epub)

    if validation_issues:
        print("   ❌ Problemas encontrados na validação:")
        for issue in validation_issues:
            print(f"   {issue}")
        return
    else:
        print("   ✓ Estrutura EPUB válida e compatível com Google Play Books")

    # 11. Limpeza
    shutil.rmtree(temp_dir)

    # 12. Resumo final
    epub_size = os.path.getsize(output_epub) / 1024

    print(f"\n✨ EPUB gerado com sucesso!")
    print(f"\n📱 Arquivo: {output_epub}")
    print(f"   Tamanho: {epub_size:.1f} KB")
    print(f"   Cards: {len(cards)}")
    print(f"   Formato: EPUB 3.0 (nav.xhtml + toc.ncx)")
    print(f"   Compatibilidade: ✅ Google Play Books, Apple Books, Kindle, Kobo")
    print(f"\n📥 Para ler no celular:")
    print(f"   1. Acesse: Google Play Books (https://play.google.com/books/publish)")
    print(f"   2. Faça upload: {output_epub}")
    print(f"   3. Pronto! Leia no app do celular ou web")

if __name__ == "__main__":
    main()
