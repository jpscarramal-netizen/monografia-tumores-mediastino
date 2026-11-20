# -*- coding: utf-8 -*-
"""Build the monograph .docx in the structure of the author's meta-analysis paper (article format),
keeping the pre-textual elements required by the course norms (ABNT, TNR 12, 1.5 spacing, margins 3/3/2/2)."""
import csv
import os
import re
import sys

from docx.enum.section import WD_SECTION
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.shared import Cm, Pt
from docx import Document

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import gera_docx as G  # noqa: E402  (reuse helpers: para, heading, centered_title, page_break, add_field, ...)

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
SEC = os.path.join(ROOT, "trabalho", "secoes")
OUT = os.path.join(ROOT, "saida", "monografia_tumores_mediastino.docx")
FIG1 = os.path.join(ROOT, "trabalho", "figuras", "figura1_prisma.png")

AUTORES = "[NOMES DOS INTEGRANTES DO GRUPO 6]"
TITULO = "ESTADO ATUAL DO TRATAMENTO CIRÚRGICO DOS TUMORES DO MEDIASTINO ANTERIOR"
SUBTITULO = "revisão sistemática das abordagens aberta, videotoracoscópica e robótica"

SIGLAS = [
    ("ChART", "Chinese Alliance for Research in Thymomas"),
    ("ECR", "Ensaio clínico randomizado"),
    ("ESTS", "European Society of Thoracic Surgeons"),
    ("HR", "Hazard ratio (razão de riscos)"),
    ("IASLC", "International Association for the Study of Lung Cancer"),
    ("IC 95%", "Intervalo de confiança de 95%"),
    ("IPTW", "Ponderação pelo inverso da probabilidade de tratamento"),
    ("ITMIG", "International Thymic Malignancy Interest Group"),
    ("JART", "Japanese Association for Research on the Thymus"),
    ("KART", "Korean Association for Research on the Thymus"),
    ("MD", "Diferença de médias"),
    ("MG", "Miastenia gravis"),
    ("MIS", "Cirurgia minimamente invasiva"),
    ("NCCN", "National Comprehensive Cancer Network"),
    ("NCDB", "National Cancer Database"),
    ("OCEBM", "Oxford Centre for Evidence-Based Medicine"),
    ("OR", "Odds ratio (razão de chances)"),
    ("PICO", "População, intervenção, comparação e desfecho"),
    ("PRISMA", "Preferred Reporting Items for Systematic Reviews and Meta-Analyses"),
    ("PSM", "Pareamento por escore de propensão"),
    ("R0", "Ressecção completa, com margens microscópicas livres"),
    ("RATS", "Cirurgia torácica robótica"),
    ("RR", "Risco relativo"),
    ("STS", "Society of Thoracic Surgeons"),
    ("TET", "Tumor epitelial tímico"),
    ("TNM", "Classificação tumor, linfonodo e metástase"),
    ("VATS", "Cirurgia torácica videoassistida"),
]


def read(name):
    with open(os.path.join(SEC, name), encoding="utf-8") as f:
        return f.read().strip()


def add_runs(p, text, size=12):
    """Add text to paragraph p, rendering **bold** and *italic* spans."""
    for part in re.split(r"(\*\*[^*]+\*\*|\*[^*]+\*)", text):
        if not part:
            continue
        r = p.add_run(part.strip("*") if part.startswith("*") else part)
        r.bold = part.startswith("**")
        r.italic = part.startswith("*") and not part.startswith("**")
        r.font.name, r.font.size, r.font.color.rgb = G.FONT, Pt(size), G.BLACK


def md_body(doc, md, prefix):
    """Render markdown body: '### ' -> numbered level-2 heading, '1. ' lists, paragraphs."""
    sub = 0
    for block in re.split(r"\n\s*\n", md.strip()):
        block = block.strip()
        if not block or block.startswith("# ") or block.startswith("## "):
            continue
        if block.startswith("### "):
            sub += 1
            G.heading(doc, f"{prefix}.{sub} {block[4:].strip()}", 2)
            continue
        lines = block.split("\n")
        if all(re.match(r"^\d+\.\s", ln) for ln in lines):
            for ln in lines:
                p = G.para(doc, "", indent=False)
                p.paragraph_format.left_indent = Cm(1.25)
                add_runs(p, ln)
            continue
        p = G.para(doc, "")
        add_runs(p, " ".join(ln.strip() for ln in lines))


def table_from_csv(doc, path, headers, widths, size, vertical):
    with open(path, encoding="utf-8-sig") as f:
        rows = list(csv.reader(f))[1:]
    t = doc.add_table(rows=1, cols=len(headers))
    t.alignment = WD_TABLE_ALIGNMENT.CENTER
    for c, h, w in zip(t.rows[0].cells, headers, widths):
        G.cell_text(c, h, bold=True, size=size, align=WD_ALIGN_PARAGRAPH.CENTER)
        c.width = w
    for row in rows:
        cells = t.add_row().cells
        for c, v, w in zip(cells, row, widths):
            G.cell_text(c, v, size=size)
            c.width = w
    G.set_borders(t, inner_vertical=vertical, outer_sides=vertical)
    G.repeat_header(t)
    return len(rows)


def resumo_part(doc, md, titulo, kw_label):
    G.centered_title(doc, titulo, after=18)
    for ln in [x.strip() for x in md.split("\n") if x.strip()]:
        if ln.startswith("#"):
            continue
        p = G.para(doc, "", indent=False, spacing=1.0, after=6)
        m = re.match(r"^([A-ZÀ-Ý ,]+|[A-Z][a-z]+(?:-[a-z]+)?):\s*(.*)$", ln)
        if m:
            r = p.add_run(m.group(1) + ": ")
            r.bold, r.font.name, r.font.size = True, G.FONT, Pt(12)
            add_runs(p, m.group(2))
        else:
            add_runs(p, ln)
    G.page_break(doc)


def sort_key(ref):
    head = ref.split(".")[0].upper()
    year = re.findall(r"\b(19|20)\d{2}\b", ref)
    y = re.findall(r"(?:, |\b)((?:19|20)\d{2})\. DOI|, ((?:19|20)\d{2})\.", ref)
    yr = next((a or b for a, b in y), "") if y else (year[-1] if year else "")
    return (head, yr)


def build():
    doc = Document()
    G.setup_styles(doc)
    sec = doc.sections[0]
    G.set_margins(sec)

    # ---------- CAPA ----------
    for line in ("UNIVERSIDADE FEDERAL DE OURO PRETO", "ESCOLA DE MEDICINA",
                 "DEPARTAMENTO DE CIRURGIA, GINECOLOGIA, OBSTETRÍCIA E PROPEDÊUTICA", "GRADUAÇÃO EM MEDICINA"):
        G.centered_title(doc, line, after=0)
    for _ in range(5):
        G.para(doc, indent=False, spacing=1.0)
    G.centered_title(doc, AUTORES, after=0)
    for _ in range(5):
        G.para(doc, indent=False, spacing=1.0)
    G.centered_title(doc, TITULO + ":", after=0)
    G.para(doc, SUBTITULO, align=WD_ALIGN_PARAGRAPH.CENTER, indent=False, spacing=1.0)
    for _ in range(4):
        G.para(doc, indent=False, spacing=1.0)
    G.centered_title(doc, "TRABALHO DE GRADUAÇÃO")
    for _ in range(7):
        G.para(doc, indent=False, spacing=1.0)
    G.centered_title(doc, "Ouro Preto", after=0)
    G.centered_title(doc, "2026", after=0)
    G.page_break(doc)

    # ---------- FOLHA DE ROSTO ----------
    G.centered_title(doc, AUTORES, after=0)
    for _ in range(6):
        G.para(doc, indent=False, spacing=1.0)
    G.centered_title(doc, TITULO + ":", after=0)
    G.para(doc, SUBTITULO, align=WD_ALIGN_PARAGRAPH.CENTER, indent=False, spacing=1.0)
    for _ in range(4):
        G.para(doc, indent=False, spacing=1.0)
    p = G.para(doc, "Trabalho apresentado à disciplina CGP012, Clínica Cirúrgica II, do Curso de Medicina da "
                    "Universidade Federal de Ouro Preto (UFOP), ministrada pelo Prof. Iure Kalinine Ferraz de Souza, "
                    "como requisito parcial para aprovação na disciplina. Formato de artigo científico, conforme "
                    "previsto nas normas da disciplina.", indent=False, spacing=1.0)
    p.paragraph_format.left_indent = Cm(8)
    for _ in range(9):
        G.para(doc, indent=False, spacing=1.0)
    G.centered_title(doc, "Ouro Preto", after=0)
    G.centered_title(doc, "2026", after=0)
    G.page_break(doc)

    # ---------- FOLHA DE APROVAÇÃO ----------
    G.centered_title(doc, AUTORES, after=24)
    G.centered_title(doc, TITULO + ":", after=0)
    G.para(doc, SUBTITULO, align=WD_ALIGN_PARAGRAPH.CENTER, indent=False, spacing=1.0, after=24)
    p = G.para(doc, "Trabalho apresentado à disciplina CGP012, Clínica Cirúrgica II, do Curso de Medicina da "
                    "Universidade Federal de Ouro Preto, como requisito parcial para aprovação na disciplina.",
               indent=False, spacing=1.0, after=24)
    p.paragraph_format.left_indent = Cm(8)
    G.para(doc, "Aprovado em: ____/____/2026", indent=False, spacing=1.0, after=36)
    G.centered_title(doc, "BANCA EXAMINADORA", after=36)
    for linha in ("______________________________________________",
                  "Prof. Iure Kalinine Ferraz de Souza (Orientador)", "Universidade Federal de Ouro Preto", "",
                  "______________________________________________", "[Nome do avaliador]",
                  "Universidade Federal de Ouro Preto"):
        G.para(doc, linha, align=WD_ALIGN_PARAGRAPH.CENTER, indent=False, spacing=1.0, after=0)
    G.page_break(doc)

    # ---------- RESUMO / ABSTRACT ----------
    res = read("resumo.md")
    pt, en = re.split(r"^##\s*ABSTRACT\s*$", res, flags=re.M)
    resumo_part(doc, pt, "RESUMO", "Palavras-chave")
    resumo_part(doc, en, "ABSTRACT", "Keywords")

    # ---------- LISTAS ----------
    G.centered_title(doc, "LISTA DE FIGURAS", after=18)
    G.para(doc, "Figura 1 - Fluxograma PRISMA 2020 da seleção dos estudos", indent=False, spacing=1.0)
    G.para(doc, indent=False, spacing=1.0)
    G.centered_title(doc, "LISTA DE QUADROS", after=18)
    G.para(doc, "Quadro 1 - Características dos estudos incluídos", indent=False, spacing=1.0)
    G.para(doc, indent=False, spacing=1.0)
    G.centered_title(doc, "LISTA DE TABELAS", after=18)
    G.para(doc, "Tabela 1 - Principais resultados dos estudos incluídos", indent=False, spacing=1.0)
    G.page_break(doc)

    G.centered_title(doc, "LISTA DE ABREVIATURAS E SIGLAS", after=18)
    t = doc.add_table(rows=0, cols=2)
    for sigla, sig in SIGLAS:
        row = t.add_row().cells
        G.cell_text(row[0], sigla, size=12)
        G.cell_text(row[1], sig, size=12)
        row[0].width, row[1].width = Cm(3), Cm(13)
    G.page_break(doc)

    # ---------- SUMÁRIO ----------
    G.centered_title(doc, "SUMÁRIO", after=18)
    G.add_field(doc.add_paragraph().add_run(), 'TOC \\o "1-2" \\h \\z \\u')

    # ---------- TEXTO ----------
    new = doc.add_section(WD_SECTION.NEW_PAGE)
    G.set_margins(new)
    new.header.is_linked_to_previous = False
    hp = new.header.paragraphs[0]
    hp.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    hr = hp.add_run()
    hr.font.name, hr.font.size = G.FONT, Pt(10)
    G.add_field(hr, "PAGE")
    sec.header.is_linked_to_previous = False

    G.heading(doc, "1 Introdução", 1)
    md_body(doc, read("introducao.md"), "1")

    G.heading(doc, "2 Métodos", 1)
    md_body(doc, read("metodos.md"), "2")

    G.heading(doc, "3 Resultados", 1)
    md_body(doc, read("resultados.md"), "3")

    # Figure and tables are placed at the end of section 3 (ABNT allows after first mention)
    G.caption(doc, "Figura 1 - Fluxograma PRISMA 2020 da seleção dos estudos")
    pic = doc.add_paragraph()
    pic.alignment = WD_ALIGN_PARAGRAPH.CENTER
    pic.add_run().add_picture(FIG1, width=Cm(14.5))
    G.source(doc, "Fonte: elaboração própria (2026), segundo o modelo PRISMA 2020 (PAGE et al., 2021).")

    G.caption(doc, "Quadro 1 - Características dos estudos incluídos")
    table_from_csv(doc, os.path.join(SEC, "quadro1.csv"),
                   ("Estudo", "País / fonte", "Desenho / nível", "Comparação", "n", "População", "Principais achados"),
                   (Cm(2.0), Cm(2.2), Cm(2.2), Cm(1.8), Cm(1.4), Cm(2.2), Cm(4.2)), 7, True)
    G.source(doc, "Fonte: elaboração própria com base nos estudos incluídos (2026). Nível de evidência segundo o "
                  "Oxford Centre for Evidence-Based Medicine (2011).")

    G.caption(doc, "Tabela 1 - Principais resultados dos estudos incluídos")
    table_from_csv(doc, os.path.join(SEC, "tabela1.csv"),
                   ("Estudo", "Comparação", "R0 / margem", "Perioperatório", "Oncológico"),
                   (Cm(2.4), Cm(2.6), Cm(3.0), Cm(4.0), Cm(4.0)), 7, False)
    G.source(doc, "Fonte: elaboração própria com base nos estudos incluídos (2026). Valores na ordem da comparação "
                  "indicada. NR: não relatado.")

    G.heading(doc, "4 Discussão", 1)
    md_body(doc, read("discussao.md").replace("### Limitações", "### Limitações"), "4")

    G.heading(doc, "5 Conclusão", 1)
    md_body(doc, read("conclusao.md"), "5")

    # ---------- REFERÊNCIAS ----------
    G.page_break(doc)
    G.heading(doc, "Referências", 1)
    refs = []
    for name in ("referencias_estudos.md", "referencias_apoio.md"):
        refs += [r.strip() for r in re.split(r"\n\s*\n", read(name)) if r.strip() and not r.startswith("#")]
    seen, uniq = set(), []
    for r in refs:
        k = re.sub(r"\W", "", r.lower())[:80]
        if k not in seen:
            seen.add(k)
            uniq.append(r)
    for ref in sorted(uniq, key=sort_key):
        p = G.para(doc, "", align=WD_ALIGN_PARAGRAPH.LEFT, indent=False, spacing=1.0, after=12)
        add_runs(p, ref)

    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    doc.save(OUT)
    print(OUT, "| referências:", len(uniq))


if __name__ == "__main__":
    build()
