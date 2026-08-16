#!/usr/bin/env python3
import argparse
import json
from pathlib import Path
from urllib.parse import urlencode
from urllib.request import Request, urlopen

SERVICE = "https://www.cartografia.servizirl.it/expo/rest/services/gpt/direttiva_alluvioni_2022/MapServer/6/query"
WHERE = "CatDist='Depuratori' AND Risorsa='Trattamento acque reflue urbane'"


def fetch_json(params):
    url = f"{SERVICE}?{urlencode(params)}"
    request = Request(url, headers={"User-Agent": "lom-amr-atlas/1.0"})
    with urlopen(request, timeout=90) as response:
        return json.load(response)


def main():
    parser = argparse.ArgumentParser(description="Fetch public Lombardy urban wastewater treatment points.")
    parser.add_argument("--output", default="public/geography/atlas_wastewater_plants.geojson")
    args = parser.parse_args()

    expected = fetch_json({"where": WHERE, "returnCountOnly": "true", "f": "json"})["count"]
    source = fetch_json({
        "where": WHERE,
        "outFields": "OBJECTID,DenOrig,Prov,CodCom,Annoril,Risorsa,PropDato",
        "returnGeometry": "true",
        "outSR": "4326",
        "orderByFields": "OBJECTID",
        "resultRecordCount": "1000",
        "f": "geojson",
    })
    if source.get("type") != "FeatureCollection":
        raise ValueError("The service did not return a GeoJSON FeatureCollection")

    features = []
    for feature in source.get("features", []):
        geometry = feature.get("geometry")
        props = feature.get("properties") or {}
        if not geometry or geometry.get("type") != "Point":
            continue
        coordinates = geometry.get("coordinates") or []
        if len(coordinates) < 2:
            continue
        features.append({
            "type": "Feature",
            "geometry": {"type": "Point", "coordinates": coordinates[:2]},
            "properties": {
                "name": props.get("DenOrig") or "Depuratore",
                "province": props.get("Prov"),
                "municipality_code": props.get("CodCom"),
                "survey_year": props.get("Annoril"),
                "source_owner": props.get("PropDato") or "Regione Lombardia",
                "context_note": "Posizione cartografica di un impianto di trattamento delle acque reflue urbane; non e' un punto di campionamento AMR.",
            },
        })

    if len(features) != expected:
        raise ValueError(f"Expected {expected} public points, obtained {len(features)}")

    output = {
        "type": "FeatureCollection",
        "name": "Lombardy urban wastewater treatment plants - regional cartographic service",
        "source": SERVICE.rsplit("/query", 1)[0],
        "source_filter": WHERE,
        "features": features,
    }
    path = Path(args.output)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(output, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
    print(f"WROTE={path}")
    print(f"FEATURES={len(features)}")


if __name__ == "__main__":
    main()
