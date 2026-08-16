#!/usr/bin/env python3
"""Build Lombardia public geography from the annual ISTAT boundary archive."""
from __future__ import annotations
import argparse, json
from pathlib import Path
import shapefile
from pyproj import Transformer

TRANSFORMER=Transformer.from_crs("EPSG:32632","EPSG:4326",always_xy=True)

def transform_coordinates(value):
    if value and isinstance(value[0],(int,float)):
        x,y=TRANSFORMER.transform(float(value[0]),float(value[1])); return [x,y]
    return [transform_coordinates(item) for item in value]

def build(shp_path,output,kind):
    reader=shapefile.Reader(str(shp_path),encoding="latin1",encodingErrors="strict")
    features=[]
    for sr in reader.iterShapeRecords():
        record=sr.record.as_dict()
        if int(record["COD_REG"])!=3: continue
        if kind=="municipalities":
            props={"name":record["COMUNE"],"istat_code":record["PRO_COM_T"],"province_code":str(record["COD_UTS"]).zfill(3),"region_code":"03","source_date":"2026-01-01"}
        elif kind=="provinces":
            props={"name":record["DEN_UTS"],"istat_code":str(record["COD_UTS"]).zfill(3),"abbreviation":record["SIGLA"],"unit_type":record["TIPO_UTS"],"region_code":"03","source_date":"2026-01-01"}
        else:
            props={"name":record["DEN_REG"],"istat_code":str(record["COD_REG"]).zfill(2),"source_date":"2026-01-01"}
        geometry=dict(sr.shape.__geo_interface__); geometry["coordinates"]=transform_coordinates(geometry["coordinates"])
        features.append({"type":"Feature","properties":props,"geometry":geometry})
    expected={"municipalities":1502,"provinces":12,"region":1}[kind]
    if len(features)!=expected: raise ValueError(f"{kind}: expected {expected}, found {len(features)}")
    output.parent.mkdir(parents=True,exist_ok=True); output.write_text(json.dumps({"type":"FeatureCollection","features":features},ensure_ascii=False,separators=(",",":")),encoding="utf-8")

def main():
    p=argparse.ArgumentParser(); p.add_argument("--source-root",type=Path,required=True); p.add_argument("--output-root",type=Path,required=True); a=p.parse_args()
    jobs=[("Com01012026_g/Com01012026_g_WGS84.shp","atlas_municipalities.geojson","municipalities"),("ProvCM01012026_g/ProvCM01012026_g_WGS84.shp","atlas_provinces.geojson","provinces"),("Reg01012026_g/Reg01012026_g_WGS84.shp","atlas_region.geojson","region")]
    for source,name,kind in jobs: build(a.source_root/source,a.output_root/name,kind)
if __name__=="__main__": main()