# Lombardia One Health AMR Atlas

Edizione regionale `lom_amr_atlas`, costruita sulla base condivisa
`amr_atlas_common`.

## Stato

La struttura applicativa e' pronta, ma non contiene ancora dataset AMR
lombardi pubblicati. Le fonti candidate sono registrate nei metadati e nel
catalogo; il runtime le ignora finche' non diventano `public_approved`.

## Build locale

```powershell
powershell.exe -NoProfile -ExecutionPolicy Bypass -File scripts/build.ps1
python -m http.server 8000 --directory site
```

Aprire `http://localhost:8000/`.

## Directory

- `public/`: esclusivamente dati e asset candidati alla superficie pubblica;
- `private/`: dati riservati o granulari, mai copiati nella build;
- `raw/`: puntatore/convenzione per fonti originali immutabili;
- `metadata/`: fonti, equivalenze con Sardegna e decisioni di pubblicazione;
- `schema/`: schemi condivisi versionati;
- `reports/`: audit e verifiche;
- `releases/`: pacchetti congelati;
- `site/`: output generato, non sorgente canonica.
