#!/usr/bin/env python3
"""Aggiorna il catalogo lombardo da una selezione curata di record PubMed."""

from __future__ import annotations

import json
import re
import sys
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path

CURATED = {
    "42578762": ("healthcare_amr", "Tre ospedali della Lombardia; diffusione di Klebsiella pneumoniae ST147 NDM-14"),
    "42515098": ("foodborne_amr", "Collezione storica di Salmonella da casi umani in Lombardia, 2001-2016"),
    "42511134": ("veterinary_amr", "Isolati bovini di Streptococcus agalactiae provenienti dalla Lombardia"),
    "42322447": ("wildlife_amr", "Ricci europei campionati in Lombardia per Escherichia coli resistenti alle cefalosporine"),
    "42203922": ("human_antimicrobial_use", "Prescrizioni antibiotiche territoriali in Lombardia, 2000-2024"),
    "41750509": ("companion_animal_amr", "Casi clinici veterinari di piometra osservati in Lombardia"),
    "40805079": ("wildlife_amr", "Uccelli selvatici ricoverati al Centro Recupero Animali Selvatici di Vanzago"),
    "39612737": ("dairy_amr", "Stafilococchi meticillino-resistenti in 88 allevamenti bovini da latte della provincia di Lodi"),
    "39200700": ("antimicrobial_stewardship", "Indagine sulle scelte antibiotiche dei pediatri di famiglia della Lombardia"),
    "38789634": ("healthcare_amr", "Studio real-world in un ospedale lombardo su nuovi antibiotici per Gram-negativi multiresistenti"),
    "36976013": ("healthcare_amr", "Pazienti COVID-19 ventilati in terapia intensiva a Milano con Acinetobacter baumannii resistente ai carbapenemi"),
    "36882761": ("antimicrobial_stewardship", "Programma di stewardship in un reparto di chirurgia vascolare di Pavia"),
    "35756019": ("wastewater_amr", "Escherichia coli OXA-244 isolato da acque superficiali e sotterranee in provincia di Pavia"),
    "35644436": ("healthcare_one_health_amr", "Staphylococcus aureus associato agli allevamenti in pazienti del Policlinico San Matteo di Pavia"),
    "35743817": ("dairy_one_health", "Latte di massa da 331 allevamenti bovini lombardi: qualità, residui antimicrobici e indicatori One Health"),
    "34664793": ("human_antimicrobial_use", "Uso territoriale di antibiotici in Lombardia, 2000-2019"),
    "32913720": ("swine_amr", "Staphylococcus aureus meticillino-resistente lungo la filiera suinicola lombarda"),
    "32825203": ("swine_amr", "Indagine su MRSA in 88 allevamenti suini della Lombardia"),
    "32763372": ("healthcare_amr", "Klebsiella pneumoniae ipermucoviscosa NDM-5 e OXA-48 in un ospedale di Brescia"),
    "29017452": ("healthcare_amr", "Sorveglianza genomica di Klebsiella pneumoniae KPC all'Ospedale Sacco di Milano, 2012-2014"),
    "28770191": ("healthcare_amr", "Resistenza antimicrobica di Streptococcus pneumoniae nell'area di Desio, 2008-2016"),
    "27457497": ("dairy_amr", "Ricerca di MRSA in 844 campioni di latte di massa raccolti in Lombardia"),
    "23731504": ("healthcare_one_health_amr", "Infezioni umane da MRSA associato agli allevamenti in un'area lombarda ad alta densità suinicola"),
    "21706227": ("human_antimicrobial_use", "Prescrizione territoriale di antibiotici in Lombardia"),
    "20735332": ("healthcare_amr", "Epidemiologia di MRSA in un ospedale universitario di Milano"),
    "17534228": ("healthcare_amr", "Resistenza degli uropatogeni in pazienti ambulatoriali nell'area di Brescia"),
    "24858644": ("healthcare_amr", "Klebsiella pneumoniae KPC-3 in un ospedale di Brescia"),
}


def text(node: ET.Element | None) -> str:
    return " ".join("".join(node.itertext()).split()) if node is not None else ""


def publication_year(article: ET.Element) -> int:
    candidates = [
        text(article.find("./Article/ArticleDate/Year")),
        text(article.find("./Article/Journal/JournalIssue/PubDate/Year")),
        text(article.find("./MedlineJournalInfo/MedlineTA")),
        text(article.find("./Article/Journal/JournalIssue/PubDate/MedlineDate")),
    ]
    for value in candidates:
        match = re.search(r"(19|20)\d{2}", value)
        if match:
            return int(match.group(0))
    return 0


def parse_record(article: ET.Element) -> dict:
    citation = article.find("./MedlineCitation")
    pubmed = article.find("./PubmedData")
    if citation is None or pubmed is None:
        raise ValueError("Record PubMed incompleto")
    pmid = text(citation.find("./PMID"))
    journal_article = citation.find("./Article")
    if journal_article is None:
        raise ValueError(f"Articolo mancante per PMID {pmid}")
    authors = journal_article.findall("./AuthorList/Author")
    if authors:
        first = authors[0]
        first_name = " ".join(filter(None, [text(first.find("./LastName")), text(first.find("./Initials"))]))
        author_label = f"{first_name} et al." if len(authors) > 1 else first_name
    else:
        author_label = text(journal_article.find("./AuthorList/CollectiveName"))
    doi = ""
    for identifier in pubmed.findall("./ArticleIdList/ArticleId"):
        if identifier.attrib.get("IdType") == "doi":
            doi = text(identifier)
            break
    scope, geographic_link = CURATED[pmid]
    return {
        "id": f"pubmed_{pmid}",
        "year": publication_year(citation),
        "title": text(journal_article.find("./ArticleTitle")),
        "authors": author_label,
        "journal": text(journal_article.find("./Journal/Title")),
        "scope": scope,
        "geographic_link": geographic_link,
        "pmid": pmid,
        "doi": doi,
        "source_url": f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/",
    }


def main() -> int:
    repo = Path(__file__).resolve().parents[1]
    catalog_path = repo / "public" / "data" / "literature-catalog.json"
    catalog = json.loads(catalog_path.read_text(encoding="utf-8-sig"))
    query = urllib.parse.urlencode({
        "db": "pubmed",
        "id": ",".join(CURATED),
        "retmode": "xml",
        "tool": "lom_amr_atlas",
        "email": "atlas-maintainer@example.invalid",
    })
    request = urllib.request.Request(
        f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?{query}",
        headers={"User-Agent": "lom-amr-atlas-literature-refresh/1.0"},
    )
    with urllib.request.urlopen(request, timeout=60) as response:
        root = ET.fromstring(response.read())
    fetched = {text(item.find("./MedlineCitation/PMID")): item for item in root.findall("./PubmedArticle")}
    missing = sorted(set(CURATED) - set(fetched))
    if missing:
        raise RuntimeError("PMID non restituiti da PubMed: " + ", ".join(missing))
    existing_pmids = {str(item.get("pmid", "")) for item in catalog.get("records", [])}
    additions = [parse_record(fetched[pmid]) for pmid in CURATED if pmid not in existing_pmids]
    records = list(catalog.get("records", [])) + additions
    records.sort(key=lambda item: (-int(item.get("year", 0)), str(item.get("title", "")).casefold()))
    catalog["selection_note"] = (
        "Selezione curata e aggiornata il 2026-08-16: studi regionali o locali con collegamento "
        "territoriale esplicito alla Lombardia. Non equivale a una revisione sistematica e gli "
        "studi locali non sono trasformati automaticamente in stime regionali."
    )
    catalog["records"] = records
    catalog_path.write_text(json.dumps(catalog, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"CATALOG_OK total={len(records)} added={len(additions)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

