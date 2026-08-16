# Geografia pubblica

La cartografia pubblica dell'edizione Lombardia comprende:

- `atlas_region.geojson`: confine regionale ISTAT 2026;
- `atlas_provinces.geojson`: 12 province/città metropolitana ISTAT 2026;
- `atlas_municipalities.geojson`: 1.502 comuni ISTAT 2026;
- `atlas_hydrography.geojson`: 975 elementi del reticolo principale RIP/AIPO;
- `atlas_wastewater_provinces.geojson`: 12 geometrie provinciali con soli conteggi aggregati SIRe 2025.

Il layer SIRe non contiene nomi, codici, coordinate, gestori o note dei singoli
impianti. I valori indicano la copertura documentale dei consuntivi provinciali
e non rappresentano misure di resistenza antimicrobica.

Le trasformazioni sono riproducibili con gli script in `scripts/`. Fonti,
snapshot, licenze e limiti sono registrati in `metadata/` e `reports/`.
