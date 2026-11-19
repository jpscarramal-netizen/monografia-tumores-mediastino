# -*- coding: utf-8 -*-
"""Build the monograph .docx following the course norms (ABNT, TNR 12, 1.5 spacing, margins 3/3/2/2)."""
import os
import sys

from docx import Document
from docx.enum.section import WD_SECTION
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_BREAK, WD_LINE_SPACING
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Cm, Pt, RGBColor

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import conteudo as C  # noqa: E402

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
OUT = os.path.join(ROOT, "saida", "monografia_tumores_mediastino.docx")
FONT = "Times New Roman"
BLACK = RGBColor(0, 0, 0)


def set_margins(section):
    section.top_margin, section.left_margin = Cm(3), Cm(3)
    section.bottom_margin, section.right_margin = Cm(2), Cm(2)
    section.page_height, section.page_width = Cm(29.7), Cm(21.0)


def para(doc, text="", align=WD_ALIGN_PARAGRAPH.JUSTIFY, bold=False, size=12, indent=True,
         spacing=1.5, after=6, before=0, italic=False, upper=False):
    p = doc.add_paragraph()
    pf = p.paragraph_format
    pf.alignment = align
    pf.first_line_indent = Cm(1.25) if indent else Cm(0)
    pf.line_spacing = spacing
    pf.space_after = Pt(after)
    pf.space_before = Pt(before)
    if text:
        r = p.add_run(text.upper() if upper else text)
        r.bold, r.italic = bold, italic
        r.font.size, r.font.name, r.font.color.rgb = Pt(size), FONT, BLACK
    return p


def heading(doc, text, level):
    p = doc.add_paragraph(style=f"Heading {level}")
    pf = p.paragraph_format
    pf.alignment = WD_ALIGN_PARAGRAPH.LEFT
    pf.first_line_indent = Cm(0)
    pf.line_spacing = 1.5
    pf.space_before = Pt(18 if level == 1 else 12)
    pf.space_after = Pt(12)
    pf.keep_with_next = True
    r = p.add_run(text.upper() if level == 1 else text)
    r.bold = True
    r.font.size, r.font.name, r.font.color.rgb = Pt(12), FONT, BLACK
    return p


def centered_title(doc, text, before=0, after=12):
    return para(doc, text, align=WD_ALIGN_PARAGRAPH.CENTER, bold=True, indent=False, spacing=1.0,
                before=before, after=after)


def page_break(doc):
    doc.add_paragraph().add_run().add_break(WD_BREAK.PAGE)


def add_field(run, instr):
    for kind, text in (("begin", None), ("instr", instr), ("separate", None), ("text", "1"), ("end", None)):
        if kind == "instr":
            el = OxmlElement("w:instrText")
            el.set(qn("xml:space"), "preserve")
            el.text = text
        elif kind == "text":
            el = OxmlElement("w:t")
            el.text = text
        else:
            el = OxmlElement("w:fldChar")
            el.set(qn("w:fldCharType"), kind)
        run._r.append(el)


def setup_styles(doc):
    st = doc.styles["Normal"]
    st.font.name, st.font.size = FONT, Pt(12)
    st.element.rPr.rFonts.set(qn("w:eastAsia"), FONT)
    for lvl in (1, 2):
        h = doc.styles[f"Heading {lvl}"]
        h.font.name, h.font.size, h.font.bold, h.font.color.rgb = FONT, Pt(12), True, BLACK
        h.element.rPr.rFonts.set(qn("w:asciiTheme"), "") if False else None
        rfonts = h.element.rPr.find(qn("w:rFonts"))
        if rfonts is None:
            rfonts = OxmlElement("w:rFonts")
            h.element.rPr.append(rfonts)
        for a in ("w:ascii", "w:hAnsi", "w:cs", "w:eastAsia"):
            rfonts.set(qn(a), FONT)
        for a in ("w:asciiTheme", "w:hAnsiTheme", "w:cstheme", "w:eastAsiaTheme"):
            if rfonts.get(qn(a)) is not None:
                del rfonts.attrib[qn(a)]
    for name in ("TOC 1", "TOC 2"):
        try:
            s = doc.styles[name]
        except KeyError:
            s = doc.styles.add_style(name, 1)
        s.font.name, s.font.size = FONT, Pt(12)
    # ask Word to refresh the TOC on open
    upd = OxmlElement("w:updateFields")
    upd.set(qn("w:val"), "true")
    doc.settings.element.append(upd)


def cell_text(cell, text, bold=False, size=10, align=WD_ALIGN_PARAGRAPH.LEFT):
    cell.text = ""
    p = cell.paragraphs[0]
    p.paragraph_format.alignment = align
    p.paragraph_format.line_spacing = 1.0
    p.paragraph_format.space_after = Pt(0)
    p.paragraph_format.first_line_indent = Cm(0)
    r = p.add_run(text)
    r.bold = bold
    r.font.size, r.font.name, r.font.color.rgb = Pt(size), FONT, BLACK


def set_borders(table, inner_vertical=True, outer_sides=True):
    tbl = table._tbl
    tblPr = tbl.tblPr
    b = OxmlElement("w:tblBorders")
    spec = {"top": True, "bottom": True, "insideH": True,
            "left": outer_sides, "right": outer_sides, "insideV": inner_vertical}
    for edge, on in spec.items():
        e = OxmlElement(f"w:{edge}")
        e.set(qn("w:val"), "single" if on else "nil")
        e.set(qn("w:sz"), "4")
        e.set(qn("w:color"), "000000")
        b.append(e)
    tblPr.append(b)


def repeat_header(table):
    trPr = table.rows[0]._tr.get_or_add_trPr()
    h = OxmlElement("w:tblHeader")
    h.set(qn("w:val"), "true")
    trPr.append(h)


def caption(doc, text):
    return para(doc, text, align=WD_ALIGN_PARAGRAPH.CENTER, bold=True, indent=False, spacing=1.0, after=6, size=12)


def source(doc, text):
    return para(doc, text, align=WD_ALIGN_PARAGRAPH.LEFT, indent=False, spacing=1.0, after=12, size=10)


def build():
    doc = Document()
    setup_styles(doc)
    sec = doc.sections[0]
    set_margins(sec)

    # ---------- CAPA ----------
    for line in ("UNIVERSIDADE FEDERAL DE OURO PRETO", "ESCOLA DE MEDICINA",
                 "DEPARTAMENTO DE CIRURGIA, GINECOLOGIA, OBSTETRÍCIA E PROPEDÊUTICA", "GRADUAÇÃO EM MEDICINA"):
        centered_title(doc, line, after=0)
    for _ in range(5):
        para(doc, indent=False, spacing=1.0)
    centered_title(doc, C.AUTORES, after=0)
    for _ in range(5):
        para(doc, indent=False, spacing=1.0)
    centered_title(doc, C.TITULO + ":", after=0)
    para(doc, C.SUBTITULO, align=WD_ALIGN_PARAGRAPH.CENTER, indent=False, spacing=1.0)
    for _ in range(4):
        para(doc, indent=False, spacing=1.0)
    centered_title(doc, "TRABALHO DE GRADUAÇÃO")
    for _ in range(7):
        para(doc, indent=False, spacing=1.0)
    centered_title(doc, "Ouro Preto", after=0)
    centered_title(doc, "2026", after=0)
    page_break(doc)

    # ---------- FOLHA DE ROSTO ----------
    centered_title(doc, C.AUTORES, after=0)
    for _ in range(6):
        para(doc, indent=False, spacing=1.0)
    centered_title(doc, C.TITULO + ":", after=0)
    para(doc, C.SUBTITULO, align=WD_ALIGN_PARAGRAPH.CENTER, indent=False, spacing=1.0)
    for _ in range(4):
        para(doc, indent=False, spacing=1.0)
    p = para(doc, "Trabalho apresentado à disciplina CGP012, Clínica Cirúrgica II, do Curso de Medicina da Universidade "
                  "Federal de Ouro Preto (UFOP), ministrada pelo Prof. Iure Kalinine Ferraz de Souza, como requisito "
                  "parcial para aprovação na disciplina.", align=WD_ALIGN_PARAGRAPH.JUSTIFY, indent=False, spacing=1.0)
    p.paragraph_format.left_indent = Cm(8)
    for _ in range(9):
        para(doc, indent=False, spacing=1.0)
    centered_title(doc, "Ouro Preto", after=0)
    centered_title(doc, "2026", after=0)
    page_break(doc)

    # ---------- FOLHA DE APROVAÇÃO ----------
    centered_title(doc, C.AUTORES, after=24)
    centered_title(doc, C.TITULO + ":", after=0)
    para(doc, C.SUBTITULO, align=WD_ALIGN_PARAGRAPH.CENTER, indent=False, spacing=1.0, after=24)
    p = para(doc, "Trabalho apresentado à disciplina CGP012, Clínica Cirúrgica II, do Curso de Medicina da Universidade "
                  "Federal de Ouro Preto, como requisito parcial para aprovação na disciplina.",
             indent=False, spacing=1.0, after=24)
    p.paragraph_format.left_indent = Cm(8)
    para(doc, "Aprovado em: ____/____/2026", indent=False, spacing=1.0, after=36)
    centered_title(doc, "BANCA EXAMINADORA", after=36)
    for nome in ("Prof. Iure Kalinine Ferraz de Souza", "Universidade Federal de Ouro Preto"):
        pass
    for linha in ("______________________________________________",
                  "Prof. Iure Kalinine Ferraz de Souza (Orientador)", "Universidade Federal de Ouro Preto", "",
                  "______________________________________________", "[Nome do avaliador]",
                  "Universidade Federal de Ouro Preto"):
        para(doc, linha, align=WD_ALIGN_PARAGRAPH.CENTER, indent=False, spacing=1.0, after=0)
    page_break(doc)

    # ---------- RESUMO ----------
    centered_title(doc, "RESUMO", after=18)
    para(doc, C.RESUMO, indent=False, spacing=1.0, after=12)
    p = para(doc, "", indent=False, spacing=1.0)
    r = p.add_run("Palavras-chave: ")
    r.bold, r.font.name, r.font.size = True, FONT, Pt(12)
    r = p.add_run(C.PALAVRAS_CHAVE)
    r.font.name, r.font.size = FONT, Pt(12)
    page_break(doc)

    # ---------- ABSTRACT ----------
    centered_title(doc, "ABSTRACT", after=18)
    para(doc, C.ABSTRACT, indent=False, spacing=1.0, after=12)
    p = para(doc, "", indent=False, spacing=1.0)
    r = p.add_run("Keywords: ")
    r.bold, r.font.name, r.font.size = True, FONT, Pt(12)
    r = p.add_run(C.KEYWORDS)
    r.font.name, r.font.size = FONT, Pt(12)
    page_break(doc)

    # ---------- LISTAS ----------
    centered_title(doc, "LISTA DE QUADROS", after=18)
    para(doc, "Quadro 1 - Síntese dos estudos incluídos na revisão", indent=False, spacing=1.0)
    for _ in range(2):
        para(doc, indent=False, spacing=1.0)
    centered_title(doc, "LISTA DE TABELAS", after=18)
    para(doc, "Tabela 1 - Principais resultados numéricos dos estudos incluídos", indent=False, spacing=1.0)
    page_break(doc)

    centered_title(doc, "LISTA DE ABREVIATURAS E SIGLAS", after=18)
    t = doc.add_table(rows=0, cols=2)
    for sigla, sig in C.SIGLAS:
        row = t.add_row().cells
        cell_text(row[0], sigla, size=12)
        cell_text(row[1], sig, size=12)
        row[0].width, row[1].width = Cm(3), Cm(13)
    page_break(doc)

    # ---------- SUMÁRIO ----------
    centered_title(doc, "SUMÁRIO", after=18)
    p = doc.add_paragraph()
    add_field(p.add_run(), 'TOC \\o "1-2" \\h \\z \\u')

    # ---------- TEXTO: nova seção com numeração ----------
    new = doc.add_section(WD_SECTION.NEW_PAGE)
    set_margins(new)
    new.header.is_linked_to_previous = False
    hp = new.header.paragraphs[0]
    hp.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    hr = hp.add_run()
    hr.font.name, hr.font.size = FONT, Pt(10)
    add_field(hr, "PAGE")
    sec.header.is_linked_to_previous = False

    heading(doc, "1 Introdução", 1)
    for t_ in C.INTRODUCAO:
        para(doc, t_)

    heading(doc, "2 Objetivos", 1)
    heading(doc, "2.1 Objetivo geral", 2)
    para(doc, C.OBJ_GERAL)
    heading(doc, "2.2 Objetivos específicos", 2)
    for o in C.OBJ_ESPECIFICOS:
        p = para(doc, "• " + o, indent=False)
        p.paragraph_format.left_indent = Cm(1.25)

    heading(doc, "3 Metodologia", 1)
    for t_ in C.METODOLOGIA:
        para(doc, t_)

    heading(doc, "4 Resultados e discussão", 1)
    para(doc, C.RESULTADOS_ABERTURA)

    # Quadro 1
    caption(doc, "Quadro 1 - Síntese dos estudos incluídos na revisão")
    q = doc.add_table(rows=1, cols=5)
    q.alignment = WD_TABLE_ALIGNMENT.CENTER
    widths = (Cm(1.0), Cm(2.8), Cm(3.4), Cm(3.6), Cm(5.2))
    for c, h, w in zip(q.rows[0].cells, ("Nº", "Autor (ano) / País", "Delineamento / Nível de evidência",
                                        "Objetivo", "Principais achados"), widths):
        cell_text(c, h, bold=True, size=9, align=WD_ALIGN_PARAGRAPH.CENTER)
        c.width = w
    for row in C.QUADRO1:
        cells = q.add_row().cells
        for c, v, w in zip(cells, row, widths):
            cell_text(c, v, size=9)
            c.width = w
    set_borders(q, inner_vertical=True, outer_sides=True)
    repeat_header(q)
    source(doc, "Fonte: elaboração própria com base nos estudos incluídos (2026). Nível de evidência segundo o Oxford "
                "Centre for Evidence-Based Medicine (2011).")

    # Tabela 1
    caption(doc, "Tabela 1 - Principais resultados numéricos dos estudos incluídos")
    tb = doc.add_table(rows=1, cols=6)
    tb.alignment = WD_TABLE_ALIGNMENT.CENTER
    widths = (Cm(2.4), Cm(2.6), Cm(1.6), Cm(2.8), Cm(3.4), Cm(3.2))
    for c, h, w in zip(tb.rows[0].cells, C.TABELA1_CAB, widths):
        cell_text(c, h, bold=True, size=8, align=WD_ALIGN_PARAGRAPH.CENTER)
        c.width = w
    for row in C.TABELA1:
        cells = tb.add_row().cells
        for c, v, w in zip(cells, row, widths):
            cell_text(c, v, size=8)
            c.width = w
    set_borders(tb, inner_vertical=False, outer_sides=False)
    repeat_header(tb)
    source(doc, "Fonte: elaboração própria com base nos estudos incluídos (2026). " + C.TABELA1_NOTA)

    for titulo, paragrafos in C.SECOES:
        heading(doc, titulo, 2)
        for t_ in paragrafos:
            para(doc, t_)

    heading(doc, "5 Considerações finais", 1)
    for t_ in C.CONSIDERACOES:
        para(doc, t_)

    # Referências: alinhadas à esquerda, espaço simples, 1 linha entre elas
    page_break(doc)
    heading(doc, "Referências", 1)
    for ref in C.REFERENCIAS:
        para(doc, ref, align=WD_ALIGN_PARAGRAPH.LEFT, indent=False, spacing=1.0, after=12)

    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    doc.save(OUT)
    print(OUT)


if __name__ == "__main__":
    build()
