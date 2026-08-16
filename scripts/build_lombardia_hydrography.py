#!/usr/bin/env python3
"""Build a lightweight Lombardia hydrography GeoJSON from the official ZIP."""
import argparse
import io
import json
import math
import zipfile
from pathlib import Path

import shapefile
from pyproj import Transformer

SOURCE_LAYERS = {
    "Corsi_acqua_RIP": {"network_type": "RIP", "name": "NOME_PRINC", "kind": "TIPOLOGIA_", "code": "IDT_N", "description": "DESCRIZION"},
    "Corsi_acqua_AIPO": {"network_type": "AIPO", "name": "NOME", "kind": "", "code": "COD_AIPO", "description": "DESCRIZION"},
}

def distance_sq(point, start, end):
    dx, dy = end[0] - start[0], end[1] - start[1]
    if dx == 0 and dy == 0:
        return (point[0] - start[0]) ** 2 + (point[1] - start[1]) ** 2
    t = max(0.0, min(1.0, ((point[0] - start[0]) * dx + (point[1] - start[1]) * dy) / (dx * dx + dy * dy)))
    px, py = start[0] + t * dx, start[1] + t * dy
    return (point[0] - px) ** 2 + (point[1] - py) ** 2

def simplify(points, tolerance):
    if len(points) <= 2:
        return points
    keep = {0, len(points) - 1}
    stack = [(0, len(points) - 1)]
    limit = tolerance * tolerance
    while stack:
        first, last = stack.pop()
        best_index, best_distance = None, -1.0
        for index in range(first + 1, last):
            current = distance_sq(points[index], points[first], points[last])
            if current > best_distance:
                best_index, best_distance = index, current
        if best_index is not None and best_distance > limit:
            keep.add(best_index)
            stack.extend(((first, best_index), (best_index, last)))
    return [points[index] for index in sorted(keep)]

def clean(value):
    return value.strip() if isinstance(value, str) else value

def build(source_zip, output, tolerance):
    transformer = Transformer.from_crs(32632, 4326, always_xy=True)
    features = []
    with zipfile.ZipFile(source_zip) as archive:
        for base, mapping in SOURCE_LAYERS.items():
            reader = shapefile.Reader(
                shp=io.BytesIO(archive.read(base + ".shp")),
                shx=io.BytesIO(archive.read(base + ".shx")),
                dbf=io.BytesIO(archive.read(base + ".dbf")),
                encoding="cp1252",
            )
            fields = [field[0] for field in reader.fields[1:]]
            for shape_record in reader.iterShapeRecords():
                record = dict(zip(fields, shape_record.record))
                points = [(float(x), float(y)) for x, y, *_ in shape_record.shape.points]
                starts = list(shape_record.shape.parts) + [len(points)]
                parts = []
                for start, end in zip(starts, starts[1:]):
                    segment = simplify(points[start:end], tolerance)
                    if len(segment) >= 2:
                        transformed = [transformer.transform(x, y) for x, y in segment]
                        if not all(7.5 <= lon <= 11.5 and 44.0 <= lat <= 47.5 for lon, lat in transformed):
                            raise ValueError(f"Coordinate fuori bounds in {base}")
                        parts.append([[round(lon, 6), round(lat, 6)] for lon, lat in transformed])
                if not parts:
                    continue
                geometry = {"type": "LineString", "coordinates": parts[0]} if len(parts) == 1 else {"type": "MultiLineString", "coordinates": parts}
                name = clean(record.get(mapping["name"])) or clean(record.get(mapping["description"])) or "Corso d'acqua senza nome"
                properties = {
                    "name": name, "network_type": mapping["network_type"],
                    "kind": clean(record.get(mapping["kind"])) if mapping["kind"] else None,
                    "source_code": clean(record.get(mapping["code"])),
                    "description": clean(record.get(mapping["description"])),
                    "source_date": "snapshot 2026-08-16",
                }
                features.append({"type": "Feature", "properties": properties, "geometry": geometry})
    collection = {"type": "FeatureCollection", "name": "Lombardia hydrography RIP and AIPO", "crs": {"type": "name", "properties": {"name": "urn:ogc:def:crs:OGC:1.3:CRS84"}}, "features": features}
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(collection, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
    return len(features)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--source-zip", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--tolerance-m", type=float, default=25.0)
    args = parser.parse_args()
    count = build(args.source_zip, args.output, args.tolerance_m)
    print(f"wrote {count} features to {args.output}")

if __name__ == "__main__":
    main()
