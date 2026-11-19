"""Convert article PDFs (entrada/artigos) and PMC XMLs (trabalho/textos) into page-tagged plain text in trabalho/textos."""
import sys, glob, os, xml.etree.ElementTree as ET
import pymupdf
root = sys.argv[1]
for f in glob.glob(os.path.join(root, "entrada", "artigos", "*.pdf")):
    out = os.path.join(root, "trabalho", "textos", os.path.basename(f)[:-4] + ".txt")
    d = pymupdf.open(f)
    with open(out, "w", encoding="utf-8") as o:
        for i, p in enumerate(d, 1):
            o.write(f"\n=== [p.{i}] ===\n" + p.get_text())
for f in glob.glob(os.path.join(root, "trabalho", "textos", "PMC*.xml")):
    r = ET.parse(f).getroot()
    out = f[:-4] + ".txt"
    parts = []
    for sec in r.iter():
        if sec.tag == "title" and sec.text: parts.append("\n## " + "".join(sec.itertext()))
        elif sec.tag == "p": parts.append("".join(sec.itertext()))
        elif sec.tag == "table-wrap":
            parts.append("\n[TABLE] " + " ".join((sec.findtext("label") or "", "".join(sec.find("caption").itertext()) if sec.find("caption") is not None else "")))
            for tr in sec.iter("tr"):
                parts.append(" | ".join("".join(c.itertext()).strip() for c in tr))
    open(out, "w", encoding="utf-8").write("\n".join(parts))
print("ok")
