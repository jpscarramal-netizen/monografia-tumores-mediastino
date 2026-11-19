"""Deduplicate PubMed, Scopus and WoS records by DOI and normalized title; list records new vs PubMed."""
import csv, re, sys
csv.field_size_limit(10**8)
sys.stdout.reconfigure(encoding="utf-8")
B = "trabalho/busca/"
def norm(t): return re.sub(r"[^a-z0-9]", "", (t or "").lower())[:120]
def load(f, doi, title, year, src):
    out = []
    for r in csv.DictReader(open(B + f, encoding="utf-8")):
        out.append({"src": src, "doi": (r.get(doi) or "").lower().strip(), "title": r.get(title, ""), "year": r.get(year, ""),
                    "journal": r.get("journal", ""), "author": r.get("first_author", ""), "abstract": r.get("abstract", "")})
    return out
pm = load("pubmed_2026-11-19.csv", "doi", "title", "year", "PubMed")
sc = load("scopus_2026-11-19.csv", "doi", "title", "year", "Scopus")
ws = load("wos_2026-11-19.csv", "doi", "title", "year", "WoS")
seen_doi, seen_t, uniq, dup = set(), set(), [], 0
for r in pm + sc + ws:
    k1, k2 = r["doi"], norm(r["title"])
    if (k1 and k1 in seen_doi) or (k2 and k2 in seen_t):
        dup += 1; continue
    if k1: seen_doi.add(k1)
    if k2: seen_t.add(k2)
    uniq.append(r)
print(f"PubMed {len(pm)} | Scopus {len(sc)} | WoS {len(ws)} | total {len(pm)+len(sc)+len(ws)} | duplicatas {dup} | únicos {len(uniq)}")
new = [r for r in uniq if r["src"] != "PubMed"]
with open(B + "novos_scopus_wos.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=["src", "year", "doi", "author", "journal", "title", "abstract"]); w.writeheader()
    for r in new: w.writerow({k: r[k] for k in w.fieldnames})
print("novos (não estavam no PubMed):", len(new))
