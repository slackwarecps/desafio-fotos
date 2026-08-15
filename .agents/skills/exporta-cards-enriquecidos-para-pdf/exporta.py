#!/usr/bin/env python3
"""
Skill: Exporta Cards Enriquecidos para PDF
Consolida todos os cards enriquecidos (NNN-enriched-card.md) em um único arquivo PDF formatado como deck didático.
"""

import os
import re
import sys
from datetime import datetime

def sanitize_filename(filename):
    """Sanitiza string para ser usada como nome de arquivo válido"""
    filename = re.sub(r'[<>:"/\\|?*]', '-', filename)
    filename = re.sub(r'\s+', ' ', filename).strip()
    filename = filename[:100]
    return filename

def remove_section_headers(text):
    """Remove headers como ### TRANSLATED QUESTION, ### EXPLANATION, ### SIMPLE EXPLANATION"""
    text = re.sub(r'^### TRANSLATED QUESTION\s*\n', '', text, flags=re.MULTILINE)
    text = re.sub(r'^### EXPLANATION \(TECH LEAD\)\s*\n', '', text, flags=re.MULTILINE)
    text = re.sub(r'^### SIMPLE EXPLANATION\s*\n', '', text, flags=re.MULTILINE)
    text = re.sub(r'^Explicação Técnica:\s*\n', '', text, flags=re.MULTILINE)
    text = re.sub(r'^Explicação para Aprendizes:\s*\n', '', text, flags=re.MULTILINE)
    return text.strip()

def generate_markdown_deck(cards, output_md, book_title):
    """Gera arquivo Markdown consolidado com estrutura de deck"""
    os.makedirs("outputs", exist_ok=True)

    deck_content = []
    total_cards = len(cards)

    # Capa
    deck_content.append(f"# {book_title.upper()}")
    deck_content.append("")
    deck_content.append(f"**{book_title}**")
    deck_content.append("")
    deck_content.append(f"Data de Geração: {datetime.now().strftime('%d de %B de %Y, %H:%M %Z')}")
    deck_content.append(f"Total de Questões: {total_cards}")
    deck_content.append("Versão: 1.0")
    deck_content.append("")
    deck_content.append("{QUEBRA_DE_PAGINA_AQUI}")
    deck_content.append("")
    deck_content.append("---")
    deck_content.append("")

    # Processar cada card
    for idx, card_file in enumerate(cards, 1):
        try:
            with open(card_file, 'r', encoding='utf-8') as f:
                full_content = f.read()

            # Extrair seções pelo padrão ---
            sections = re.split(r'^---\s*$', full_content, flags=re.MULTILINE)

            original_question = sections[0].strip() if len(sections) > 0 else ""
            english_options = sections[1].strip() if len(sections) > 1 else ""
            translated_section = remove_section_headers(sections[2].strip() if len(sections) > 2 else "")
            explanation_section = remove_section_headers(sections[3].strip() if len(sections) > 3 else "")
            simple_section = remove_section_headers(sections[4].strip() if len(sections) > 4 else "")
            correct_answer_section = sections[5].strip() if len(sections) > 5 else ""

            # ===== PÁGINA DE QUESTÃO =====
            deck_content.append(f"### Question {idx}/{total_cards}")
            deck_content.append("")
            deck_content.append(original_question)
            deck_content.append("")
            deck_content.append("---")
            deck_content.append("")
            deck_content.append(english_options)
            deck_content.append("")
            deck_content.append("---")
            deck_content.append("{QUEBRA_DE_PAGINA_AQUI}")
            deck_content.append("")

            # ===== PÁGINA DE RESPOSTA =====
            deck_content.append(f"### Question {idx} Answer")
            deck_content.append("")

            # Tradução
            if translated_section:
                deck_content.append("**TRANSLATED QUESTION**")
                deck_content.append("")
                deck_content.append(translated_section)
                deck_content.append("")
                deck_content.append("---")
                deck_content.append("")

            # Explicação Técnica
            if explanation_section:
                deck_content.append("**Tech Lead Explanation:**")
                deck_content.append("")
                deck_content.append(explanation_section)
                deck_content.append("")
                deck_content.append("---")
                deck_content.append("")

            # Explicação Simples
            if simple_section:
                deck_content.append("**🧒 Children Explanation:**")
                deck_content.append("")
                deck_content.append(simple_section)
                deck_content.append("")
                deck_content.append("---")
                deck_content.append("")

            # Resposta Correta
            if correct_answer_section:
                deck_content.append("**✅ CORRECT ANSWER**")
                deck_content.append(correct_answer_section)
                deck_content.append("")

            deck_content.append("---")
            deck_content.append("{QUEBRA_DE_PAGINA_AQUI}")
            deck_content.append("")

        except Exception as e:
            print(f"   ❌ Erro ao processar {card_file}: {e}")
            continue

    # Salvar Markdown
    with open(output_md, 'w', encoding='utf-8') as f:
        f.write('\n'.join(deck_content))

    return len(cards)

def generate_pdf(output_md, output_pdf):
    """Converte Markdown para PDF usando weasyprint (suporte completo a UTF-8), com fallback para reportlab"""
    try:
        try:
            from weasyprint import HTML, CSS
        except ImportError:
            print("⚠️  weasyprint não encontrado. Instalando...")
            os.system(f"{sys.executable} -m pip install weasyprint -q")
            from weasyprint import HTML, CSS
    except (ImportError, OSError) as e:
        print(f"   ⚠️  weasyprint indisponível ({e}).")
        print("   Tentando fallback com reportlab...")
        generate_pdf_fallback(output_md, output_pdf)
        return

    # Ler arquivo Markdown
    with open(output_md, 'r', encoding='utf-8') as f:
        markdown_content = f.read()

    # Converter Markdown para HTML básico
    html_content = markdown_to_html(markdown_content)

    # Gerar PDF usando weasyprint
    try:
        HTML(string=html_content).write_pdf(output_pdf)
    except Exception as e:
        print(f"   ❌ Erro com weasyprint: {e}")
        print("   Tentando fallback com reportlab...")
        generate_pdf_fallback(output_md, output_pdf)

def markdown_to_html(markdown_content):
    """Converte Markdown simples para HTML com suporte completo a UTF-8"""
    html_lines = [
        '<!DOCTYPE html>',
        '<html lang="pt-BR">',
        '<head>',
        '  <meta charset="UTF-8">',
        '  <meta name="viewport" content="width=device-width, initial-scale=1.0">',
        '  <title>Flashcards Deck</title>',
        '  <style>',
        '    body { font-family: "Segoe UI", Tahoma, Geneva, Verdana, sans-serif; line-height: 1.5; color: #333; margin: 20px; }',
        '    h1 { font-size: 36px; color: #1f4788; margin: 20px 0 10px; }',
        '    h3 { font-size: 23px; color: #2c5aa0; margin: 15px 0 10px; }',
        '    .title { font-size: 31px; font-weight: bold; color: #1f4788; text-align: center; margin: 20px 0; }',
        '    .heading { font-size: 18px; font-weight: bold; color: #2c5aa0; margin: 12px 0; }',
        '    .body { font-size: 14px; line-height: 1.5; margin: 6px 0; }',
        '    .options { font-size: 14px; margin: 6px 0 6px 0; padding: 0; }',
        '    hr { border: none; border-top: 1px solid #ddd; margin: 12px 0; }',
        '    .page-break { page-break-after: always; }',
        '    p { margin: 6px 0; }',
        '    b { font-weight: bold; }',
        '  </style>',
        '</head>',
        '<body>'
    ]

    lines = markdown_content.split('\n')
    for line in lines:
        if line.startswith('# '):
            text = line.replace('# ', '')
            html_lines.append(f'  <h1>{escape_html(text)}</h1>')
        elif line.startswith('### '):
            text = line.replace('### ', '')
            html_lines.append(f'  <h3>{escape_html(text)}</h3>')
        elif line.startswith('**') and line.endswith('**'):
            text = line.replace('**', '')
            html_lines.append(f'  <div class="heading"><b>{escape_html(text)}</b></div>')
        elif line == '{QUEBRA_DE_PAGINA_AQUI}':
            html_lines.append('  <div class="page-break"></div>')
        elif line.startswith('---'):
            html_lines.append('  <hr>')
        elif line.strip().startswith('[ ]'):
            html_lines.append(f'  <div class="options">{escape_html(line.strip())}</div>')
        elif line.strip():
            html_lines.append(f'  <p class="body">{escape_html(line.strip())}</p>')
        else:
            html_lines.append('  <p></p>')

    html_lines.extend(['</body>', '</html>'])
    return '\n'.join(html_lines)

def escape_html(text):
    """Escapa caracteres especiais HTML preservando UTF-8"""
    return (text
            .replace('&', '&amp;')
            .replace('<', '&lt;')
            .replace('>', '&gt;')
            .replace('"', '&quot;')
            .replace("'", '&#39;'))

def generate_pdf_fallback(output_md, output_pdf):
    """Fallback usando reportlab com suporte Unicode registrado"""
    try:
        from reportlab.lib.pagesizes import letter
        from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
        from reportlab.lib.units import inch
        from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, HRFlowable
        from reportlab.lib import colors
        from reportlab.pdfbase import pdfmetrics
        from reportlab.pdfbase.ttfonts import TTFont
    except ImportError:
        print("❌ Falha ao importar reportlab")
        return

    # Registrar fontes Unicode (DejaVu)
    try:
        pdfmetrics.registerFont(TTFont('DejaVuSans', '/System/Library/Fonts/DejaVuSans.ttf'))
        pdfmetrics.registerFont(TTFont('DejaVuSans-Bold', '/System/Library/Fonts/DejaVuSans-Bold.ttf'))
        default_font = 'DejaVuSans'
    except:
        default_font = 'Helvetica'

    # Ler arquivo Markdown
    with open(output_md, 'r', encoding='utf-8') as f:
        markdown_content = f.read()

    # Criar PDF
    doc = SimpleDocTemplate(output_pdf, pagesize=letter)
    story = []
    styles = getSampleStyleSheet()

    # Custom styles
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=26,
        textColor=colors.HexColor('#1f4788'),
        spaceAfter=10,
        spaceBefore=10,
        alignment=1,
        fontName=default_font
    )

    heading_style = ParagraphStyle(
        'CustomHeading',
        parent=styles['Heading2'],
        fontSize=18,
        textColor=colors.HexColor('#2c5aa0'),
        spaceAfter=12,
        spaceBefore=12,
        fontName=default_font
    )

    heading3_style = ParagraphStyle(
        'CustomHeading3',
        parent=styles['Heading3'],
        fontSize=16,
        textColor=colors.HexColor('#333333'),
        spaceAfter=10,
        spaceBefore=10,
        fontName=default_font
    )

    body_style = ParagraphStyle(
        'CustomBody',
        parent=styles['Normal'],
        fontSize=13,
        leading=17,
        spaceAfter=6,
        alignment=4,
        fontName=default_font
    )

    # Estilo para opções (com checkbox)
    options_style = ParagraphStyle(
        'OptionsStyle',
        parent=styles['Normal'],
        fontSize=13,
        leading=18,
        spaceAfter=6,
        leftIndent=10,
        alignment=4,
        fontName=default_font
    )

    # Processar conteúdo
    lines = markdown_content.split('\n')
    current_preformatted = []

    for line in lines:
        # Se é um checkbox/opção, trata especialmente
        if line.strip().startswith('[ ]'):
            current_preformatted.append(line)
        else:
            # Se tem linhas acumuladas (opções), adiciona como Paragraph
            if current_preformatted:
                for preformatted_line in current_preformatted:
                    story.append(Paragraph(preformatted_line, options_style))
                current_preformatted = []

            # Processa linha normal
            if line.startswith('# '):
                text = line.replace('# ', '')
                story.append(Paragraph(text, title_style))
            elif line.startswith('### '):
                text = line.replace('### ', '')
                story.append(Paragraph(text, heading3_style))
            elif line.startswith('**') and line.endswith('**'):
                bold_text = line.replace('**', '')
                story.append(Paragraph(f"<b>{bold_text}</b>", heading_style))
            elif line == '{QUEBRA_DE_PAGINA_AQUI}':
                story.append(PageBreak())
            elif line.startswith('---'):
                story.append(HRFlowable(width="100%", thickness=1, lineCap='round', color=colors.HexColor('#dddddd')))
                story.append(Spacer(1, 0.08*inch))
            elif line.strip() and not line.startswith('#'):
                story.append(Paragraph(line, body_style))
            elif line.strip() == '':
                story.append(Spacer(1, 0.04*inch))

    # Adiciona opções restantes
    if current_preformatted:
        for preformatted_line in current_preformatted:
            story.append(Paragraph(preformatted_line, options_style))

    # Gerar PDF
    try:
        doc.build(story)
    except Exception as e:
        print(f"   ❌ Erro ao gerar PDF com fallback: {e}")

def main():
    """Função principal"""
    os.makedirs("outputs", exist_ok=True)

    # Título do deck: argumento de linha de comando > variável de ambiente > padrão
    book_title = None
    if len(sys.argv) > 1:
        book_title = " ".join(sys.argv[1:]).strip()
    if not book_title:
        book_title = os.environ.get("BOOK_TITLE", "").strip()
    if not book_title:
        book_title = "Flashcards Deck - Claude Certified Architect"

    print(f"✅ Título configurado: {book_title}\n")

    # Data para o nome do arquivo
    today = datetime.now().strftime("%Y-%m-%d")
    filename_safe_title = sanitize_filename(book_title)
    output_md = f"outputs/{filename_safe_title}-{today}.md"
    output_pdf = f"outputs/{filename_safe_title}-{today}.pdf"

    # Encontrar cards enriquecidos (CARDS_DIR env > relativo > absoluto > raiz)
    cards_dir = os.environ.get("CARDS_DIR")
    if not cards_dir or not os.path.exists(cards_dir):
        cards_dir = "outputs/cards-enriquecidos"
    if not os.path.exists(cards_dir):
        cards_dir = "/Users/fabioalvaropereira/Desktop/desafio-fotos/outputs/cards-enriquecidos"
    if not os.path.exists(cards_dir):
        cards_dir = "."
    
    cards = sorted([os.path.join(cards_dir, f) for f in os.listdir(cards_dir) if re.match(r"\d{3}-enriched-card\.md$", f)])

    print(f"✅ Detectados cards enriquecidos em '{cards_dir}':")
    for card in cards:
        print(f"   - {os.path.basename(card)}")

    if not cards:
        print(f"❌ Nenhum card enriquecido encontrado em '{cards_dir}'!")
        return

    # Processar cards
    print(f"\n📝 Processando {len(cards)} cards...")
    total = generate_markdown_deck(cards, output_md, book_title)

    file_size = os.path.getsize(output_md) / 1024
    print(f"   ✓ {output_md} criado ({file_size:.1f} KB)")

    # Converter para PDF
    print(f"\n🔄 Convertendo para PDF...")
    try:
        generate_pdf(output_md, output_pdf)
        pdf_size = os.path.getsize(output_pdf) / 1024
        print(f"   ✓ {output_pdf} criado ({pdf_size:.1f} KB)")
    except Exception as e:
        print(f"   ❌ Erro ao gerar PDF: {e}")
        return

    print(f"\n✨ Pronto! Deck exportado com sucesso.")
    print(f"   Arquivos:")
    print(f"   - {output_md} (raw, editável)")
    print(f"   - {output_pdf} (formatado, pronto para compartilhar)")
    print(f"   Total: {total} questões")

if __name__ == "__main__":
    main()
