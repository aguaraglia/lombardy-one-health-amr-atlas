#!/usr/bin/env python3
"""Build Lombardy study evidence layers from the curated literature catalog.

Geometries come from the ISTAT boundaries already in this edition, or from a
named facility geocoded on OpenStreetMap. The script does not geocode farms
and does not invent a site the catalog does not name.
"""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
NOTE = (
    "Il segnaposto indica dove è stato condotto lo studio, non una prevalenza."
)
SECTOR = {
    "healthcare_amr": "AMR clinica",
    "human_antimicrobial_use": "Consumo di antimicrobici",
    "antimicrobial_use": "Uso di antimicrobici",
    "companion_animal_amr": "AMR negli animali d'affezione",
    "wildlife_amr": "AMR nella fauna selvatica",
    "veterinary_amr": "AMR veterinaria",
    "foodborne_amr": "AMR alimentare",
    "dairy_amr": "AMR nel comparto lattiero",
    "dairy_one_health": "One Health nel comparto lattiero",
    "swine_amr": "AMR nella filiera suinicola",
    "wastewater_amr": "AMR ambientale",
    "infection_prevention": "Infezioni correlate all'assistenza",
    "antimicrobial_stewardship": "Stewardship antimicrobica",
    "regional_surveillance": "Sorveglianza regionale",
    "healthcare_one_health_amr": "One Health clinica",
}
# Nominatim results checked on 2026-11-12. Coordinates are the facility or campus
# returned for the named institution, not a sample and not a farm.
POINTS = {
    "san_raffaele": (9.26548, 45.50620, "IRCCS San Raffaele, Milano", "OpenStreetMap Nominatim: IRCCS San Raffaele, Via Olgettina, Milano"),
    "san_matteo": (9.14742, 45.19746, "Fondazione IRCCS Policlinico San Matteo, Pavia", "OpenStreetMap Nominatim: Fondazione IRCCS Policlinico San Matteo, Viale Golgi, Pavia"),
    "humanitas": (9.16497, 45.37363, "IRCCS Humanitas, Rozzano", "OpenStreetMap Nominatim: Istituto Clinico Humanitas, Via Manzoni 56, Rozzano"),
    "multimedica": (9.21909, 45.53648, "IRCCS MultiMedica", "OpenStreetMap Nominatim: Ospedale IRCCS Multimedica, Via Milanese, Sesto San Giovanni. L'abstract indica Milano; il punto è la sede OSM dell'ente nominato."),
    "sacco": (9.12355, 45.52016, "Ospedale Luigi Sacco, Milano", "OpenStreetMap Nominatim: Ospedale Luigi Sacco, Via Grassi, Milano"),
    "desio": (9.19656, 45.62688, "Ospedale di Desio", "OpenStreetMap Nominatim: Ospedale di Desio, Via Mazzini, Desio"),
    "policlinico": (9.19675, 45.45790, "Fondazione IRCCS Ca' Granda Ospedale Maggiore Policlinico, Milano", "OpenStreetMap Nominatim: Policlinico di Milano, Via Francesco Sforza"),
    "spedali": (10.23126, 45.55746, "Spedali Civili di Brescia", "OpenStreetMap Nominatim: Spedali Civili di Brescia, Piazzale Spedali Civili"),
    "lodi_campus": (9.47245, 45.30518, "Polo universitario di Lodi, ospedale veterinario didattico", "OpenStreetMap Nominatim: Polo universitario di Lodi. Il civico di Via dell'Università 6 non è risolto; il punto è il polo UNIMI di Lodi, non un allevamento."),
    "vanzago": (8.97237, 45.52012, "Riserva naturale Bosco WWF di Vanzago", "OpenStreetMap Nominatim: Riserva naturale Bosco WWF di Vanzago. Sede del centro recupero, non un punto di fauna libera."),
    "unimi": (9.19439, 45.46020, "Università degli Studi di Milano, sede centrale", "OpenStreetMap Nominatim: sede centrale, Via Festa del Perdono 7. Sede dell'ente, non un punto di campionamento dell'aria."),
    "insubria": (9.09526, 45.80194, "Università degli Studi dell'Insubria, Como", "OpenStreetMap Nominatim: Università dell'Insubria, Via Francesco Anzani, Como. Sede dell'ente, non un punto di campionamento."),
}
ORGANISM = {
    "pubmed_41938218": "S. aureus, P. aeruginosa, K. pneumoniae, E. coli",
    "pubmed_42223260": "K. pneumoniae ST6668, blaNDM-1",
    "pubmed_42217672": "Neisseria gonorrhoeae",
    "pubmed_42702569": "consumo ospedaliero di antibiotici (AWaRe)",
    "pubmed_42071966": "uso di antimicrobici (DDDAit), bovine da latte",
    "pubmed_42650660": "K. pneumoniae complex ESBL, blaCTX-M-15, blaSHV, blaTEM",
    "pubmed_42644089": "Gram-positivi, soprattutto Enterococcus spp.",
    "pubmed_39858317": "E. coli e K. pneumoniae, blaCTX-M gruppo 1",
    "pubmed_41304232": "micobatteri non tubercolari, complesso M. avium",
    "pubmed_39805348": "E. coli, anche ESBL, e S. aureus",
    "pubmed_39889451": "E. coli ESBL, AmpC e carbapenemasi",
    "pubmed_40890421": "KPC, NDM, VRE, CRAB",
    "pubmed_39923562": "geni di resistenza ad ampio spettro nel particolato",
    "pubmed_25026083": "Campylobacter jejuni",
    "pubmed_34206498": "E. coli ESBL/AmpC",
    "pubmed_29180991": "Enterobacteriaceae ESBL, KPC, mcr-1.2",
    "pubmed_39061505": "Salmonella enterica",
    "pubmed_42203922": "prescrizioni antibiotiche territoriali (AWaRe)",
    "pubmed_42511134": "Streptococcus agalactiae",
    "pubmed_42578762": "K. pneumoniae ST147 NDM-14",
    "pubmed_41750509": "E. coli da piometra",
    "pubmed_42322447": "E. coli resistente alle cefalosporine di terza generazione",
    "pubmed_42515098": "Salmonella enterica",
    "pennisi_hai_milan_2026": "infezioni correlate all'assistenza",
    "pubmed_40805079": "Gram-negativi da uccelli selvatici",
    "saluzzo_vim_bergamo_2025": "patogeni con blaVIM-1",
    "active_cre_surveillance_milan_2024": "Enterobacterales resistenti ai carbapenemi",
    "pubmed_39200700": "scelte antibiotiche in pediatria",
    "antonelli_pps3_lombardy_2024": "infezioni correlate all'assistenza e uso di antimicrobici",
    "comelli_microbio_2024": "sorveglianza MICRO-BIO",
    "pubmed_39612737": "S. aureus e stafilococchi meticillino-resistenti",
    "pubmed_36976013": "Acinetobacter baumannii resistente ai carbapenemi",
    "pubmed_36882761": "stewardship antimicrobica",
    "pubmed_35644436": "S. aureus associato agli allevamenti",
    "pubmed_35743817": "residui antimicrobici e indicatori nel latte di massa",
    "pubmed_35756019": "E. coli OXA-244 ST131",
    "pubmed_34664793": "uso territoriale di antibiotici",
    "pubmed_32825203": "S. aureus meticillino-resistente",
    "pubmed_32763372": "K. pneumoniae NDM-5 e OXA-48",
    "pubmed_32913720": "S. aureus meticillino-resistente",
    "turolla_urban_sewage_milan_2018": "batteri resistenti agli antibiotici nei reflui",
    "principe_colistin_lombardy_2018": "E. coli, mcr-1",
    "pubmed_28770191": "Streptococcus pneumoniae",
    "pubmed_29017452": "K. pneumoniae resistente ai carbapenemi",
    "zanotto_ecoli_wwtp_milan_2016": "E. coli resistente agli antibiotici",
    "pubmed_27457497": "S. aureus e MRSA",
    "pubmed_24858644": "K. pneumoniae KPC-3",
    "pubmed_23731504": "S. aureus meticillino-resistente associato agli allevamenti",
    "pubmed_21706227": "prescrizione territoriale di antibiotici",
    "pubmed_20735332": "S. aureus meticillino-resistente",
    "pubmed_17534228": "uropatogeni",
    "luzzaro_bloodstream_lombardy_2002": "patogeni da emocoltura",
}


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def municipality(name: str, municipalities: dict) -> dict:
    return municipalities[name]["geometry"]


def provinces(names: list[str], provinces_by_name: dict) -> dict:
    parts = []
    for name in names:
        geometry = provinces_by_name[name]["geometry"]
        if geometry["type"] == "Polygon":
            parts.append(geometry["coordinates"])
        elif geometry["type"] == "MultiPolygon":
            parts.extend(geometry["coordinates"])
        else:
            raise ValueError(name)
    if len(parts) == 1:
        return {"type": "Polygon", "coordinates": parts[0]}
    return {"type": "MultiPolygon", "coordinates": parts}


def feature(geometry: dict, place: str, level: str, basis: str, studies: list[dict], extra_note: str = "") -> dict:
    note = NOTE if not extra_note else f"{NOTE} {extra_note}"
    return {
        "type": "Feature",
        "geometry": geometry,
        "properties": {
            "place": place,
            "geography_level": level,
            "geography_basis": basis,
            "study_count": len(studies),
            "study_ids": "; ".join(item["id"] for item in studies),
            "authors": " | ".join(item["authors"] for item in studies),
            "year": " | ".join(item["year"] for item in studies),
            "title": " | ".join(item["title"] for item in studies),
            "sector": " | ".join(item["sector"] for item in studies),
            "organism": " | ".join(item["organism"] for item in studies),
            "doi": " | ".join(item["doi"] for item in studies),
            "geography_note": note,
        },
    }


def point(key: str) -> dict:
    lon, lat, _label, _source = POINTS[key]
    return {"type": "Point", "coordinates": [round(lon, 6), round(lat, 6)]}


def place_label(key: str) -> str:
    return POINTS[key][2]


def place_basis(key: str, text: str) -> str:
    return f"{text} {POINTS[key][3]}"


def main() -> None:
    catalog = load_json(ROOT / "public/data/literature-catalog.json")
    by_id = {item["id"]: item for item in catalog["records"]}
    missing_organism = set(by_id) - set(ORGANISM)
    if missing_organism:
        raise SystemExit("Organismo mancante: " + ", ".join(sorted(missing_organism)))

    def card(study_id: str) -> dict:
        record = by_id[study_id]
        doi = record.get("doi") or ""
        return {
            "id": study_id,
            "authors": record["authors"],
            "year": str(record["year"]),
            "title": record["title"].rstrip("."),
            "sector": SECTOR[record["scope"]],
            "organism": ORGANISM[study_id],
            "doi": f"https://doi.org/{doi}" if doi else record["source_url"],
        }

    municipalities = {
        feature["properties"]["name"]: feature
        for feature in load_json(ROOT / "public/geography/atlas_municipalities.geojson")["features"]
    }
    province_features = {
        feature["properties"]["name"]: feature
        for feature in load_json(ROOT / "public/geography/atlas_provinces.geojson")["features"]
    }
    region = load_json(ROOT / "public/geography/atlas_region.geojson")["features"][0]["geometry"]

    layers: dict[str, list] = {
        "human": [],
        "veterinary": [],
        "food": [],
        "environment": [],
        "wildlife": [],
        "regional": [],
    }
    placed: dict[str, str] = {}

    def add(layer: str, study_ids: list[str], geometry: dict, place: str, level: str, basis: str, extra_note: str = "") -> None:
        for study_id in study_ids:
            if study_id in placed:
                placed[study_id] += f"; {level}: {place}"
            else:
                placed[study_id] = f"{level}: {place}"
        layers[layer].append(feature(geometry, place, level, basis, [card(study_id) for study_id in study_ids], extra_note))

    add("human", ["pubmed_42217672", "pubmed_42223260"], point("san_raffaele"), place_label("san_raffaele"), "struttura",
        place_basis("san_raffaele", "Ospedale nominato nell'abstract."))
    add("human", ["pubmed_42223260"], municipality("Pavia", municipalities), "Pavia", "comune",
        "L'abstract colloca 52 genomi a Pavia e non nomina l'ospedale pavese. Il terzo ospedale del titolo non è nominato e non riceve un punto.")
    add("human", ["pubmed_41938218"], point("multimedica"), place_label("multimedica"), "struttura",
        place_basis("multimedica", "Ente nominato: IRCCS MultiMedica."))
    add("human", ["pubmed_41304232", "pubmed_40890421", "pubmed_36882761", "pubmed_35644436"], point("san_matteo"), place_label("san_matteo"), "struttura",
        place_basis("san_matteo", "Ospedale universitario di Pavia nominato nell'abstract o nell'afferenza."))
    add("human", ["pubmed_39805348"], point("humanitas"), place_label("humanitas"), "struttura",
        place_basis("humanitas", "IRCCS Humanitas a Rozzano, nominato nell'abstract."))
    add("human", ["pubmed_36976013", "active_cre_surveillance_milan_2024"], point("policlinico"), place_label("policlinico"), "struttura",
        place_basis("policlinico", "Fondazione IRCCS Ca' Granda nominata nell'afferenza o nel gruppo autore."))
    add("human", ["pubmed_32763372", "pubmed_17534228"], point("spedali"), place_label("spedali"), "struttura",
        place_basis("spedali", "Spedali Civili nominati nell'afferenza."))
    add("human", ["pubmed_29017452"], point("sacco"), place_label("sacco"), "struttura",
        place_basis("sacco", "Ospedale Sacco nominato nel collegamento territoriale."))
    add("human", ["pubmed_28770191"], point("desio"), place_label("desio"), "struttura",
        place_basis("desio", "Desio Hospital nominato nel titolo e nell'afferenza."))
    add("human", ["saluzzo_vim_bergamo_2025"], municipality("Bergamo", municipalities), "Bergamo", "comune",
        "L'abstract indica un ospedale terziario di Bergamo e non ne riporta il nome. Nessun punto di struttura.")
    add("human", ["pennisi_hai_milan_2026", "pubmed_20735332"], municipality("Milano", municipalities), "Milano", "comune",
        "Gli articoli indicano un ospedale di Milano senza nominarlo. Nessun punto di struttura.")
    add("human", ["pubmed_24858644"], municipality("Brescia", municipalities), "Brescia", "comune",
        "Il titolo indica Brescia Hospital e l'afferenza è l'Università di Brescia, senza il nome legale della struttura. Si usa il comune, non un ospedale presunto.")

    add("veterinary", ["pubmed_39889451", "pubmed_42650660"], point("lodi_campus"), place_label("lodi_campus"), "struttura",
        place_basis("lodi_campus", "Ospedale veterinario didattico di Lodi, o di Milano con indirizzo di dipartimento a Lodi."))
    add("veterinary", ["pubmed_39858317"], municipality("Milano", municipalities), "Milano", "comune",
        "L'abstract del 2025 indica l'ospedale veterinario didattico di Milano e non un indirizzo. Non è stato spostato sulla sede di Lodi.")
    add("veterinary", ["pubmed_42071966"], provinces(["Lodi"], province_features), "Provincia di Lodi", "provincia",
        "210 allevamenti della provincia di Lodi. Nessuna azienda è localizzata.")
    add("veterinary", ["pubmed_39061505"], provinces(["Cremona", "Mantova"], province_features), "Province di Cremona e Mantova", "provincia",
        "Isolati diagnostici IZSLER da stalle delle due province. Nessuna azienda è localizzata.")

    add("food", ["pubmed_25026083", "pubmed_39612737"], provinces(["Lodi"], province_features), "Provincia di Lodi", "provincia",
        "Stalle da latte della provincia di Lodi. Nessuna azienda è localizzata.")

    add("environment", ["pubmed_39923562"], point("unimi"), place_label("unimi"), "struttura",
        place_basis("unimi", "Una delle due sedi nominate per il particolato."))
    add("environment", ["pubmed_39923562"], point("insubria"), place_label("insubria"), "struttura",
        place_basis("insubria", "Seconda sede nominata per il particolato."))
    add("environment", ["pubmed_29180991"], provinces(["Pavia"], province_features), "Provincia di Pavia", "provincia",
        "L'area dichiarata è l'Oltrepò Pavese. L'atlante non ha un poligono dell'Oltrepò: si usa il confine provinciale, più ampio dell'area dello studio. Nessun pozzo o depuratore è localizzato.")
    add("environment", ["pubmed_35756019"], municipality("Pavia", municipalities), "Pavia", "comune",
        "Acque dell'area urbana di Pavia. Nessuna coordinata di campionamento è ripubblicata.")
    add("environment", ["turolla_urban_sewage_milan_2018", "zanotto_ecoli_wwtp_milan_2016"], municipality("Milano", municipalities), "Milano", "comune",
        "Impianti dell'area urbana di Milano non nominati. Nessun depuratore è localizzato.")

    add("wildlife", ["pubmed_42644089", "pubmed_40805079"], point("vanzago"), place_label("vanzago"), "struttura",
        place_basis("vanzago", "Centro recupero di Vanzago nominato nei due lavori."))
    add("wildlife", ["pubmed_34206498"], provinces(["Brescia"], province_features), "Provincia di Brescia", "provincia",
        "Cinghiali cacciati in provincia di Brescia. Nessun sito di caccia è localizzato.")
    add("wildlife", ["pubmed_42322447"], provinces(["Milano", "Varese", "Como", "Monza e della Brianza"], province_features),
        "Province di Milano, Varese, Como e Monza e Brianza", "provincia",
        "Province già registrate nella scheda Raineri dell'atlante. Il centro di recupero non è un punto distinto da queste province nel collegamento usato qui.")

    regional_ids = [
        "pubmed_42702569", "pubmed_42203922", "pubmed_42578762", "pubmed_42511134",
        "pubmed_41750509", "pubmed_42515098", "pubmed_39200700", "antonelli_pps3_lombardy_2024",
        "comelli_microbio_2024", "pubmed_35743817", "pubmed_34664793", "pubmed_32825203",
        "pubmed_32913720", "principe_colistin_lombardy_2018", "pubmed_27457497",
        "pubmed_23731504", "pubmed_21706227", "luzzaro_bloodstream_lombardy_2002",
    ]
    add("regional", regional_ids, region, "Lombardia", "regione",
        "Gli autori dichiarano la Lombardia, più ospedali non nominati, o una filiera regionale. Il contorno regionale non è un punto di misura.")

    expected = set(by_id)
    got = set(placed)
    if got != expected:
        raise SystemExit(f"Copertura incompleta. Mancanti: {sorted(expected - got)}. Extra: {sorted(got - expected)}")

    names = {
        "human": "human_amr_evidence.geojson",
        "veterinary": "veterinary_amr_evidence.geojson",
        "food": "food_chain_amr_evidence.geojson",
        "environment": "environmental_amr_evidence.geojson",
        "wildlife": "wildlife_amr_evidence.geojson",
        "regional": "regional_study_outline.geojson",
    }
    for key, filename in names.items():
        collection = {"type": "FeatureCollection", "features": layers[key]}
        path = ROOT / "public/data" / filename
        path.write_text(json.dumps(collection, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(f"{filename}: {len(layers[key])} features")

    print("PLACED", len(placed))
    for study_id in sorted(placed):
        print(f"{study_id}\t{placed[study_id]}")


if __name__ == "__main__":
    main()
