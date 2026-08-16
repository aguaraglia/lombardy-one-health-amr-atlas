# Sardinia AMR Atlas - audit dei dati effettivamente usati

Data audit: 2026-08-16  
Edizione: `srd_amr_atlas`  
Commit pubblico di riferimento: `e3d5640f4a3b5b22a03c15b420547f784dd99f09`  
Superficie pubblicata: root del repository GitHub Pages

## Verdetto

Il sito pubblicato dalla root referenzia 26 asset JSON/GeoJSON per circa 66,35 MB. Tutti i 26 file sono sintatticamente validi; i GeoJSON caricati hanno geometrie non nulle. La cartella `web/` e' una copia storica e non e' la superficie canonica servita da GitHub Pages.

Il controllo `scripts/check_public_privacy.ps1` passa sui 126 file tracciati. Questo controllo verifica i nomi e i percorsi Git, non sostituisce la revisione scientifica, di licenza e di granularita'.

## Asset caricati dalla dashboard e dalle schede evidenza

| Ambito | File | Unita' validate | Ruolo |
|---|---|---:|---|
| Consumo umano | `public/data/aifa_osmed_2024_antibiotics.json` | 10 | contesto AIFA/OsMed |
| Sorveglianza umana | `public/data/ar_iss_2024_coverage.json` | 1 | copertura AR-ISS |
| Sorveglianza umana | `public/data/ar_iss_2024_sardinia_resistance.json` | 6 | fenotipi regionali |
| Sorveglianza umana | `public/data/ar_iss_2024_sardinia_sites.geojson` | 8 feature | sedi dei laboratori, non prevalenza locale |
| Contesto veterinario | `public/data/bdn_bovini_sardegna_2025.json` | 2 | consistenza regionale |
| Contesto veterinario | `public/data/bdn_ovicaprini_sardegna_2025.json` | 2 | consistenza regionale |
| Contesto veterinario | `public/data/bdn_suini_sardegna_2025.json` | 1 | consistenza regionale |
| Idrografia | `public/data/dbgt_corsi_principali.geojson` | 16.269 feature | contesto cartografico, non rete idrologica validata |
| AMR ambientale | `public/data/environmental_amr_water_bodies_2024.json` | 1 | evidenza aggregata |
| AMR ambientale | `public/data/environmental_amr_water_bodies.geojson` | 2 feature | localizzazione pubblica generalizzata |
| Filiera alimentare | `public/data/food_chain_amr_berchidda.json` | 1 | studio storico |
| Filiera alimentare | `public/data/food_chain_amr_berchidda.geojson` | 1 feature | poligono comunale, non ubicazione aziendale |
| AMR umana | `public/data/human_amr_facility_sassari_studies.json` | 8 | studi aggregati di struttura |
| AMR umana | `public/data/human_amr_facility_evidence.geojson` | 3 feature | strutture pubbliche, non residenza dei pazienti |
| AMR umana | `public/data/human_amr_local_studies_sardinia.json` | 4 | studi locali/area vasta |
| AMR veterinaria | `public/data/izs_sa07_02_north_sardinia_amr.json` | 1 | coorte storica di area |
| Letteratura | `public/data/literature_curated_sardinia.json` | 36 record | registro bibliografico curato |
| Letteratura | `public/data/literature_curated_summary.json` | 1 | riepilogo del registro |
| AMR veterinaria | `public/data/pig_ecoli_sardinia_2024_amr.json` | 1 | studio di filiera |
| PNCAR | `public/data/pncar_env_panel.json` | 1 | pannello/target metodologico, non osservazioni |
| Impianti | `public/data/sira_depuratori_points.geojson` | 788 feature | layer contestuale SIRA |
| AMR veterinaria | `public/data/veterinary_amr_municipal_evidence.geojson` | 40 feature | evidenze aggregate per comune |
| AMR veterinaria | `public/data/veterinary_amr_municipal_evidence.json` | 1 | metadati del layer aggregato |
| Wildlife | `public/data/wild_boar_ecoli_sardinia_2024_amr.json` | 1 | studio su cinghiali |
| Geografia | `public/geography/atlas_municipalities.geojson` | 377 feature | comuni DBGT 10K V05 |
| Geografia | `public/geography/atlas_provinces.geojson` | 6 feature | province DBGT 10K V05 |

## File presenti ma non caricati dalla superficie canonica

- `public/geography/atlas_regions.geojson` e' usato soltanto dalla vecchia copia `web/`;
- `dbgt_asta_percorso.geojson`, `dbgt_fiumi_summary.json`, `sira_corsi_acqua.geojson` e `sira_depuratori_nearest_river.csv` sono prodotti idrografici/intermedi;
- `izs_bioresource_amr_municipal.*` e `streptococcus_uberis_amr_municipal.*` alimentano o documentano prodotti aggregati, ma non sono caricati direttamente;
- `istat_censimento_agricoltura_2020_sardegna.json` e' presente ma non visualizzato;
- `test_direct.geojson` e `test_hydro.geojson` sono file di test e non devono entrare in una release;
- i due grandi file amministrativi nella radice di `public/` non sono referenziati dal runtime.

## Fonti principali ricostruite

- Regione Autonoma della Sardegna DBGT 10K V05 per confini e idrografia cartografica;
- ISS AR-ISS, dati 2024, per copertura e resistenze regionali;
- AIFA/OsMed 2024 per consumi di antibiotici;
- BDN/VetInfo 2025 per consistenze zootecniche aggregate;
- PubMed, articoli e relativi supplementi per le evidenze umane, veterinarie, alimentari, wildlife e ambientali;
- IZS Sardegna Bioresource e progetto SA 07/02 per evidenze veterinarie;
- Geoportale/SIRA per impianti di depurazione e contesto idrografico;
- ENA/NCBI per accessioni e metadati genomici, mantenendo fuori dal pubblico il dettaglio puntuale;
- PNCAR e organismi internazionali come fonti metodologiche e benchmark, non come osservazioni locali.

Le descrizioni complete, lo stato di accesso e i limiti interpretativi sono registrati in `metadata/SOURCES.tsv`, `metadata/SOURCE_LAYER_REPORT_PRIVACY.tsv`, `metadata/SNAPSHOTS.tsv` e `metadata/LITERATURE_CURATED.tsv`.

## Disallineamenti da correggere prima della prossima release Sardegna

1. `metadata/PUBLIC_SCOPE.md` descrive ancora la prima preview amministrativa, ma il runtime pubblica molti dataset AMR e contestuali.
2. Il layer `sira_depuratori_points.geojson` contiene 788 impianti ed e' tracciato/pubblicato, mentre `metadata/SOURCES.tsv` documenta ancora snapshot precedenti da 267/274 record e copertura parziale. Provenienza, data, licenza e copertura del file corrente devono essere riallineate.
3. `reports/PROJECT_AUDIT.txt` e' datato 2026-07-15, punta al vecchio percorso e conta soltanto sei file: non e' piu' utilizzabile come audit corrente.
4. `metadata/RELEASE_MANIFEST.tsv` fotografa la release 0.2.0 e non deve essere interpretato come inventario dinamico del working tree.
5. I file di test e gli output intermedi devono restare esclusi da qualunque build comune o lombarda.

## Regola per la nuova edizione Lombardia

Nessun dataset sardo viene copiato nell'edizione `lom_amr_atlas`. La base comune comprende soltanto codice, stile, schemi e procedure. Ogni fonte lombarda deve attraversare gli stati `candidate`, `verified`, `public_approved`; soltanto l'ultimo stato puo' essere caricato dal runtime pubblico.
