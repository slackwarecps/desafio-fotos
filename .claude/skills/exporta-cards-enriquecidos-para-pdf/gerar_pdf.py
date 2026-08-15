#!/usr/bin/env python3
"""
Gerador canônico do PDF do deck.

Implementa `templates/pdf-report-template.md`. Renderiza HTML e converte com Chrome
headless — único caminho testado nesta máquina que desenha emojis coloridos de verdade
(Apple Color Emoji) em vez de quadrados pretos (tofu).

Uso:
    python3 gerar_pdf.py [cards_dir] [outputs_dir]

Padrões:
    cards_dir   = outputs/cards-enriquecidos-forms/
    outputs_dir = outputs/

Saída: "Report dd-mm-yyyy hh:mm:ss.pdf" — imprime a última linha no formato
    REPORT <primeiro>-<último> OK <caminho>
"""

import html
import re
import subprocess
import sys
from datetime import datetime
from pathlib import Path

REPO = Path(__file__).resolve().parents[3]
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

# Ícone + rótulo de cada bloco, conforme templates/pdf-report-template.md
BLOCKS = [
    ("en", "📘", "PERGUNTA (ENGLISH)"),
    ("pt", "🇧🇷", "PERGUNTA (PORTUGUÊS)"),
    ("tech", "🧠", "ANÁLISE TÉCNICA (TECH LEAD)"),
    ("kids", "🚸", "EXPLICAÇÃO ACESSÍVEL (CRIANÇAS)"),
    ("answer", "✅", "RESPOSTA CORRETA"),
]


def parse_card(path: Path) -> dict:
    """Extrai as 5 seções de um NNN-enriched-card.md."""
    text = path.read_text(encoding="utf-8")

    def section(header: str) -> str:
        # Captura da linha "### HEADER" até o próximo "---" isolado ou próximo "###"
        pattern = rf"^###\s*{re.escape(header)}\s*\n(.*?)(?=^---\s*$|^###\s)"
        m = re.search(pattern, text, re.S | re.M)
        return m.group(1).strip() if m else ""

    head = text.split("\n---\n", 1)[0].strip()
    scenario = re.sub(r"^Scenario:\s*", "", head).strip()

    options_en = re.findall(r"^\[\s*\]\s*([A-D])\s*-\s*(.+)$", text, re.M)
    # A última ocorrência de "[ ] X - ..." é a resposta correta (seção CORRECT ANSWER)
    answer_raw = section("CORRECT ANSWER")
    answer_m = re.search(r"\[\s*\]\s*([A-D])\s*-\s*(.+)", answer_raw)

    return {
        "number": path.name[:3],
        "scenario": scenario,
        "options_en": options_en[:4],
        "pt": section("TRANSLATED QUESTION"),
        "tech": section("EXPLANATION (TECH LEAD)"),
        "kids": section("🚸 CHILDREN EXPLANATION"),
        "answer_letter": answer_m.group(1) if answer_m else "?",
        "answer_text": answer_m.group(2).strip() if answer_m else answer_raw,
    }


def md_inline(s: str) -> str:
    """Renderiza markdown inline: **negrito**, *itálico*, `código`."""
    s = html.escape(s)
    s = re.sub(r"`([^`]+)`", r"<code>\1</code>", s)
    s = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"(?<!\*)\*([^*\n]+)\*(?!\*)", r"<em>\1</em>", s)
    return s


def md_block(s: str) -> str:
    """Converte um bloco em parágrafos <p>, preservando quebras de linha internas.

    Linhas que são apenas um rótulo em negrito viram subtítulos, como no EPUB.
    """
    out = []
    for para in re.split(r"\n\s*\n", s.strip()):
        if not para.strip():
            continue
        label = re.fullmatch(r"\*\*(.+?):\*\*", para.strip())
        if label:
            out.append(f'<p class="label">{md_inline(label.group(1))}:</p>')
            continue
        # Rótulo em negrito seguido de texto na mesma linha/parágrafo
        m = re.match(r"\*\*(.+?):\*\*\s*\n(.*)", para.strip(), re.S)
        if m:
            out.append(f'<p class="label">{md_inline(m.group(1))}:</p>')
            para = m.group(2)
        lines = [md_inline(l) for l in para.strip().split("\n") if l.strip()]
        if lines:
            out.append("<p>" + "<br>".join(lines) + "</p>")
    return "\n".join(out)


CSS = """
@page { size: A4; margin: 18mm 16mm 20mm 16mm;
        @bottom-center { content: counter(page); } }
* { box-sizing: border-box; }
body { font-family: -apple-system, "Helvetica Neue", Helvetica, Arial, sans-serif;
       font-size: 11.5pt; line-height: 1.55; color: #1c1c1e; margin: 0; }
code { font-family: "SF Mono", Menlo, Consolas, monospace; font-size: 0.9em;
       background: #f2f2f7; padding: 1px 4px; border-radius: 3px; }
strong { color: #0b0b0c; }

/* Capa */
.cover { height: 247mm; display: flex; flex-direction: column;
         align-items: center; justify-content: center; text-align: center;
         page-break-after: always; }
.cover .mark { font-size: 54pt; line-height: 1; margin-bottom: 14mm; }
.cover h1 { font-size: 26pt; color: #1a4f9c; margin: 0 0 4mm; letter-spacing: .5px; }
.cover h2 { font-size: 13pt; font-weight: 500; color: #48484a; margin: 0 0 14mm; }
.cover .meta { font-size: 11pt; color: #636366; line-height: 1.9; }
.cover .rule { width: 46mm; height: 3px; background: #1a4f9c; margin: 0 0 12mm; }

/* Índice */
.toc { page-break-after: always; }
.toc h2, .card h2.section-title { font-size: 16pt; color: #1a4f9c; margin: 0 0 6mm; }
.toc ol { list-style: none; padding: 0; margin: 0; }
.toc li { display: flex; gap: 3mm; padding: 1.6mm 0;
          border-bottom: 1px solid #e5e5ea; font-size: 10.5pt; }
.toc .num { color: #1a4f9c; font-weight: 600; min-width: 12mm; }

/* Card */
.card { page-break-after: always; }
.card:last-child { page-break-after: auto; }
.card-head { display: flex; justify-content: space-between; align-items: center;
             background: #1a4f9c; color: #fff; padding: 3mm 5mm;
             border-radius: 5px; margin-bottom: 6mm; }
.card-head .id { font-weight: 700; font-size: 12pt; letter-spacing: .4px; }
.card-head .of { font-size: 10pt; opacity: .85; }

.block { margin: 0 0 6mm; }
.block h3 { display: flex; align-items: center; gap: 2.5mm;
            font-size: 12pt; color: #1a4f9c; margin: 0 0 2.5mm;
            padding-bottom: 1.5mm; border-bottom: 2px solid #d6e2f2; }
.block h3 .ico { font-size: 14pt; }
.block p { margin: 0 0 2.6mm; }
.block p.label { font-weight: 700; color: #1a4f9c; margin: 3.5mm 0 1.2mm; }
.options { list-style: none; padding: 0; margin: 2mm 0 0; }
.options li { padding: 1.4mm 0 1.4mm 9mm; text-indent: -9mm; }
.options .k { font-weight: 700; color: #1a4f9c; }

.answer { background: #eaf5ec; border-left: 4px solid #2e8b57;
          padding: 3.5mm 4.5mm; border-radius: 4px; }
.answer .letter { font-weight: 700; color: #2e8b57; font-size: 12.5pt; }

/* Página final */
.end { text-align: center; padding-top: 40mm; }
.end h2 { font-size: 18pt; color: #1a4f9c; margin-bottom: 8mm; }
.end ul { display: inline-block; text-align: left; list-style: none; padding: 0;
          margin: 6mm 0; color: #48484a; }
.end li { padding: 1mm 0; }
.end .meta { color: #636366; }
"""


def build_html(cards: list, generated: str) -> str:
    total = len(cards)
    parts = [
        "<!doctype html><html lang='pt-BR'><head><meta charset='utf-8'>",
        f"<title>Flashcards Deck</title><style>{CSS}</style></head><body>",
        # Capa
        "<section class='cover'>",
        "<div class='mark'>🧠</div>",
        "<h1>FLASHCARDS DECK</h1>",
        "<div class='rule'></div>",
        "<h2>Claude Certified Architect · Foundations Certification</h2>",
        f"<div class='meta'>Gerado em {generated}<br>Total de cards: <strong>{total}</strong></div>",
        "</section>",
        # Índice
        "<section class='toc'><h2>📑 Índice de Perguntas</h2><ol>",
    ]
    for c in cards:
        snippet = html.escape(c["scenario"][:95].rstrip() + ("…" if len(c["scenario"]) > 95 else ""))
        parts.append(f"<li><span class='num'>{c['number']}</span><span>{snippet}</span></li>")
    parts.append("</ol></section>")

    # Cards
    for pos, c in enumerate(cards, 1):
        parts.append("<section class='card'>")
        parts.append(
            f"<div class='card-head'><span class='id'>Card {pos:03d}/{total:03d}</span>"
            f"<span class='of'>arquivo {c['number']}</span></div>"
        )
        for key, ico, label in BLOCKS:
            parts.append(f"<div class='block'><h3><span class='ico'>{ico}</span>{label}</h3>")
            if key == "en":
                parts.append(f"<p>{md_inline(c['scenario'])}</p><ul class='options'>")
                for letter, txt in c["options_en"]:
                    parts.append(f"<li><span class='k'>{letter})</span> {md_inline(txt)}</li>")
                parts.append("</ul>")
            elif key == "answer":
                parts.append(
                    f"<div class='answer'><span class='letter'>✓ {c['answer_letter']}</span> "
                    f"{md_inline(c['answer_text'])}</div>"
                )
            else:
                parts.append(md_block(c[key]))
            parts.append("</div>")
        parts.append("</section>")

    # Página final
    parts.append(
        "<section class='end'><h2>🏁 Fim do Deck</h2>"
        f"<div class='meta'>Cards neste deck: <strong>{total}</strong><br>Gerado em {generated}</div>"
        "<ul>"
        + "".join(f"<li>{ico} {label}</li>" for _, ico, label in BLOCKS)
        + "</ul><div class='meta'>Para uso em Spaced Repetition Systems (SRS)</div></section>"
    )
    parts.append("</body></html>")
    return "\n".join(parts)


def main() -> int:
    cards_dir = Path(sys.argv[1]) if len(sys.argv) > 1 else REPO / "outputs/cards-enriquecidos-forms"
    out_dir = Path(sys.argv[2]) if len(sys.argv) > 2 else REPO / "outputs"

    files = sorted(cards_dir.glob("*-enriched-card.md"), key=lambda p: p.name)
    if not files:
        print(f"REPORT FAILED reason: nenhum *-enriched-card.md em {cards_dir}")
        return 1

    cards = [parse_card(f) for f in files]
    now = datetime.now()
    generated = now.strftime("%d/%m/%Y %H:%M:%S")
    stamp = now.strftime("%d-%m-%Y %H:%M:%S")

    out_dir.mkdir(parents=True, exist_ok=True)
    html_path = out_dir / f".deck-{now.strftime('%Y%m%d%H%M%S')}.html"
    pdf_path = out_dir / f"Report {stamp}.pdf"
    html_path.write_text(build_html(cards, generated), encoding="utf-8")

    if not Path(CHROME).exists():
        print(f"REPORT FAILED reason: Chrome não encontrado em {CHROME}")
        return 1

    proc = subprocess.run(
        [CHROME, "--headless", "--disable-gpu", "--no-pdf-header-footer",
         f"--print-to-pdf={pdf_path}", html_path.as_uri()],
        capture_output=True, text=True,
    )
    html_path.unlink(missing_ok=True)

    if not pdf_path.exists():
        print(f"REPORT FAILED reason: Chrome não gerou o PDF ({proc.stderr.strip()[:200]})")
        return 1

    print(f"REPORT {cards[0]['number']}-{cards[-1]['number']} OK {pdf_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
