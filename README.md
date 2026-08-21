# Lombardy One Health AMR Atlas

Edizione regionale `lom_amr_atlas`, costruita sulla base condivisa
`amr_atlas_common`.

Sito pubblico: <https://aguaraglia.github.io/lombardy-one-health-amr-atlas/>

## Stato

La base pubblica verificata al 22 agosto 2026 comprende AMR umana (AR-ISS 2024, MICROBIO 2023, PPS-3), uso di antibiotici (OsMed 2024, AWaRe 2025), contesto zootecnico BDN giugno 2026, evidenze IZSLER su Salmonella da latte CR/MN e MRSA suini, AMR ambientale (Oltrepo Pavese, acque di Pavia), fauna (cinghiali Brescia, uccelli Vanzago, ricci) e un primo paper food (C. jejuni Lodi). La mappa ha confini ISTAT 2026, reticolo idrografico principale, 480 depuratori georiferiti e aggregati SIRe 2025 per provincia. Il runtime carica soltanto le fonti public_approved. Restano candidate ClassyFarm, licenze Cambridge/Elsevier (Cortimiglia, Addis, Turolla) e AMR su carne al dettaglio con split lombardo.

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
