"""PubMed search via E-utilities; saves CSV with PMID, title, journal, year, pubtypes, DOI, abstract."""
import sys, csv, json, time, urllib.parse, urllib.request, xml.etree.ElementTree as ET
sys.stdout.reconfigure(encoding="utf-8")
BASE = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/"

def get(url):
    for _ in range(3):
        try:
            with urllib.request.urlopen(url, timeout=60) as r:
                return r.read()
        except Exception as e:
            time.sleep(2)
    raise RuntimeError(url)

def search(term, retmax=2000):
    q = urllib.parse.urlencode({"db": "pubmed", "term": term, "retmax": retmax, "retmode": "json", "tool": "monografia"})
    d = json.loads(get(BASE + "esearch.fcgi?" + q))
    return int(d["esearchresult"]["count"]), d["esearchresult"]["idlist"]

def fetch(ids):
    rows = []
    for i in range(0, len(ids), 150):
        q = urllib.parse.urlencode({"db": "pubmed", "id": ",".join(ids[i:i+150]), "retmode": "xml", "tool": "monografia"})
        root = ET.fromstring(get(BASE + "efetch.fcgi?" + q))
        for art in root.findall(".//PubmedArticle"):
            pmid = art.findtext(".//PMID")
            title = "".join(art.find(".//ArticleTitle").itertext()) if art.find(".//ArticleTitle") is not None else ""
            journal = art.findtext(".//Journal/ISOAbbreviation") or art.findtext(".//Journal/Title") or ""
            year = art.findtext(".//PubDate/Year") or (art.findtext(".//PubDate/MedlineDate") or "")[:4]
            auths = art.findall("MedlineCitation/Article/AuthorList/Author")
            vol = art.findtext(".//JournalIssue/Volume") or ""; iss = art.findtext(".//JournalIssue/Issue") or ""; pg = art.findtext(".//Pagination/MedlinePgn") or ""
            jfull = art.findtext(".//Journal/Title") or ""
            authors = "; ".join(((a.findtext("LastName") or a.findtext("CollectiveName") or "") + " " + (a.findtext("Initials") or "")).strip() for a in auths)
            first = (auths[0].findtext("LastName") or auths[0].findtext("CollectiveName") or "") if auths else ""
            ptypes = "; ".join(p.text for p in art.findall(".//PublicationType"))
            doi = ""
            for a in art.findall("PubmedData/ArticleIdList/ArticleId"):
                if a.get("IdType") == "doi": doi = a.text
            pmc = ""
            for a in art.findall("PubmedData/ArticleIdList/ArticleId"):
                if a.get("IdType") == "pmc": pmc = a.text
            abst = " ".join("".join(x.itertext()) for x in art.findall(".//Abstract/AbstractText"))
            rows.append({"pmid": pmid, "first_author": first, "authors": authors, "journal_full": jfull, "volume": vol, "issue": iss, "pages": pg, "year": year, "journal": journal, "title": title,
                         "pubtypes": ptypes, "doi": doi, "pmcid": pmc, "abstract": abst})
        time.sleep(0.4)
    return rows

if __name__ == "__main__":
    term, out = sys.argv[1], sys.argv[2]
    n, ids = search(term)
    rows = fetch(ids)
    with open(out, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()) if rows else ["pmid"])
        w.writeheader(); w.writerows(rows)
    print(f"count={n} fetched={len(rows)} -> {out}")
