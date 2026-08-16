#!/usr/bin/env python3
import argparse
import json
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser(description="Join public SIRe province aggregates to ISTAT province geometries.")
    parser.add_argument("--provinces", default="public/geography/atlas_provinces.geojson")
    parser.add_argument("--summary", default="public/data/sire_wastewater_province_summary_2025.json")
    parser.add_argument("--output", default="public/geography/atlas_wastewater_provinces.geojson")
    args = parser.parse_args()
    provinces = json.loads(Path(args.provinces).read_text(encoding="utf-8"))
    summary = json.loads(Path(args.summary).read_text(encoding="utf-8"))
    by_code = {row["province"]: row for row in summary["records"]}
    seen = set()
    for feature in provinces["features"]:
        props = feature.get("properties", {})
        code = props.get("abbreviation")
        if code not in by_code:
            raise ValueError(f"Missing SIRe aggregate for province {code}")
        row = by_code[code]
        feature["properties"] = {
            "name": props.get("name"),
            "abbreviation": code,
            "plants_major": row["plants_major"],
            "plants_minor": row["plants_minor"],
            "plants_total": row["plants_total"],
            "aggregation_note": "Conteggi distinti nei consuntivi provinciali SIRe 2025; contesto depurativo, non dato AMR."
        }
        seen.add(code)
    missing = set(by_code) - seen
    if missing:
        raise ValueError(f"Unmatched province aggregates: {sorted(missing)}")
    provinces["name"] = "Lombardy SIRe wastewater province aggregates 2025"
    Path(args.output).write_text(json.dumps(provinces, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
    print(f"WROTE={args.output}")
    print(f"FEATURES={len(provinces['features'])}")


if __name__ == "__main__":
    main()
