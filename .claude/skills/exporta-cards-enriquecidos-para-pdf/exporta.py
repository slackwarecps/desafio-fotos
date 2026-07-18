#!/usr/bin/env python3
"""
Skill: Exporta Cards Enriquecidos para PDF
Consolida todos os cards enriquecidos (NNN-enriched-card.md) em um único arquivo PDF formatado como deck didático.
"""

import os
import re
from datetime import datetime

def remove_section_headers(text):
    """Remove headers como ### TRANSLATED QUESTION, ### EXPLANATION, ### SIMPLE EXPLANATION"""
    text = re.sub(r'^### TRANSLATED QUESTION\s*\n', '', text, flags=re.MULTILINE)
    text = re.sub(r'^### EXPLANATION \(TECH LEAD\)\s*\n', '', text, flags=re.MULTILINE)
    text = re.sub(r'^### SIMPLE EXPLANATION\s*\n', '', text, flags=re.MULTILINE)
    text = re.sub(r'^Explicação Técnica:\s*\n', '', text, flags=re.MULTILINE)
    text = re.sub(r'^Explicação para Aprendizes:\s*\n', '', text, flags=re.MULTILINE)
    return text.strip()

def generate_markdown_deck(cards, output_md):
    """Gera arquivo Markdown consolidado com estrutura de deck"""
    os.makedirs("outputs", exist_ok=True)

    deck_content = []
    total_cards = len(cards)

    # Capa
    deck_content.append("# FLASHCARDS DECK - CLAUDE CERTIFIED ARCHITECT")
    deck_content.append("")
    deck_content.append("**Flashcards - Claude Certified Architect – Foundations Certification**")
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
    """Converte Markdown para PDF usando reportlab"""
    try:
        from reportlab.lib.pagesizes import letter
        from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
        from reportlab.lib.units import inch
        from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Preformatted, HRFlowable
        from reportlab.lib import colors
    except ImportError:
        print("⚠️  reportlab não encontrado. Instalando...")
        os.system("pip install reportlab -q")
        from reportlab.lib.pagesizes import letter
        from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
        from reportlab.lib.units import inch
        from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Preformatted, HRFlowable
        from reportlab.lib import colors

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
        fontSize=20,
        textColor=colors.HexColor('#1f4788'),
        spaceAfter=10,
        spaceBefore=10,
        alignment=1
    )

    heading_style = ParagraphStyle(
        'CustomHeading',
        parent=styles['Heading2'],
        fontSize=14,
        textColor=colors.HexColor('#2c5aa0'),
        spaceAfter=12,
        spaceBefore=12
    )

    heading3_style = ParagraphStyle(
        'CustomHeading3',
        parent=styles['Heading3'],
        fontSize=12,
        textColor=colors.HexColor('#333333'),
        spaceAfter=10,
        spaceBefore=10
    )

    body_style = ParagraphStyle(
        'CustomBody',
        parent=styles['Normal'],
        fontSize=10,
        leading=13,
        spaceAfter=6,
        alignment=4  # justify
    )

    code_style = ParagraphStyle(
        'CodeStyle',
        parent=styles['Normal'],
        fontSize=9,
        leading=11,
        spaceAfter=4,
        leftIndent=15,
        fontName='Courier'
    )

    # Estilo para opções (com checkbox)
    options_style = ParagraphStyle(
        'OptionsStyle',
        parent=styles['Normal'],
        fontSize=10,
        leading=14,
        spaceAfter=6,
        leftIndent=10,
        alignment=4  # justify para wrap text
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
                    # Renderiza opção como Paragraph normal para permitir wrap
                    story.append(Paragraph(preformatted_line, options_style))
                current_preformatted = []

            # Processa linha normal
            if line.startswith('# '):
                story.append(Paragraph(line.replace('# ', ''), title_style))
            elif line.startswith('### '):
                story.append(Paragraph(line.replace('### ', ''), heading3_style))
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
    doc.build(story)

def main():
    """Função principal"""
    os.makedirs("outputs", exist_ok=True)

    # Data para o nome do arquivo
    today = datetime.now().strftime("%Y-%m-%d")
    output_md = f"outputs/flashcards-deck-{today}.md"
    output_pdf = f"outputs/flashcards-deck-{today}.pdf"

    # Encontrar cards enriquecidos apenas no diretório raiz
    cards = sorted([f for f in os.listdir(".") if re.match(r"\d{3}-enriched-card\.md$", f)])

    print(f"✅ Detectados cards enriquecidos:")
    for card in cards:
        print(f"   - {card}")

    if not cards:
        print("❌ Nenhum card enriquecido encontrado!")
        return

    # Processar cards
    print(f"\n📝 Processando {len(cards)} cards...")
    total = generate_markdown_deck(cards, output_md)

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
