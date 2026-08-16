# Lombardy One Health AMR Atlas

Edizione regionale `lom_amr_atlas`, costruita sulla base condivisa
`amr_atlas_common`.

Sito pubblico: <https://aguaraglia.github.io/lombardy-one-health-amr-atlas/>

## Stato

La struttura applicativa contiene una base pubblica verificata di dati AMR
umani, uso di antibiotici e contesto One Health lombardo. La mappa comprende
confini ISTAT 2026, reticolo idrografico principale e indicatori SIRe 2025
aggregati per provincia. Il runtime carica soltanto le fonti marcate
`public_approved` nei cataloghi.

La pagina Pubblicazioni mantiene distinti rapporti istituzionali, dataset e
letteratura scientifica regionale o locale.

## Build locale

```powershell
powershell.exe -NoProfile -ExecutionPolicy Bypass -File scripts/build.ps1
python -m http.server 8000 --directory site
```

Aprire `http://localhost:8000/`.

## Directory

- `public/`: esclusivamente dati e asset approvati per la superficie pubblica;
- `private/`: dati riservati o granulari, mai copiati nella build;
- `raw/`: fonti originali immutabili, escluse dal sito;
- `metadata/`: fonti, equivalenze con Sardegna e decisioni di pubblicazione;
- `schema/`: schemi condivisi versionati;
- `reports/`: audit e verifiche;
- `releases/`: pacchetti congelati;
- `site/`: output generato, non sorgente canonica.
