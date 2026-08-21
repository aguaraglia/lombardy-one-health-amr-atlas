# Recupero dati Lombardia - 16 agosto 2026

## Esito

La base ufficiale pubblicabile comprende ora geografia ISTAT 2026, AR-ISS 2024, OsMed 2024, MICROBIO adulti e pediatrico 2023, AWaRe 2025, PPS-3, una sintesi regionale SIRe 2025 e il reticolo idrografico principale. Nessun dato individuale, clinico puntuale o riservato e stato acquisito o pubblicato.

## Nuove evidenze sanitarie

- AWaRe 2025: quote Access/Watch/Reserve per 25 ASST, con popolazione generale, under 14 e over 65. Il dato riguarda consumi territoriali dei residenti e non include l'uso ospedaliero.
- PPS-3: 28 strutture per acuti, 39 presidi e 12.412 pazienti rilevati tra novembre e dicembre 2022. Pubblicati aggregati su ICA, uso di antimicrobici e sette pattern di resistenza, con copertura e limiti del report.
- MICROBIO pediatrico 2023: 1.311 eventi BSI, 36 isolamenti da liquor e nove pattern selezionati dagli antibiogrammi cumulativi regionali. Sono escluse le tabelle per singola struttura.
- I valori presenti solo nei grafici regionali AWaRe non sono stati trascritti: le tabelle ASST sono state estratte senza ambiguita dal PDF ufficiale.

## Materiali veterinari recuperati

Sono stati acquisiti e registrati come riferimenti link-only i documenti regionali sull'uso prudente degli antibiotici in coniglio da carne (2022), bovino da latte (2023) e suino (2025). Sono materiali di stewardship e divulgazione, non dataset AMR.

## Contesto ambientale

- SIRe 2025: acquisiti due ZIP ufficiali ARPA. Il foglio completo contiene 1.513 righe dati e 73 colonne; il sito pubblica solo aggregati regionali (18.844.231 AE di carico generato sommato, 5.524 controlli previsti, 7.014 eseguiti e 33 righe marcate non regolamentari per numero/modalita di controllo). Non sono misure AMR.
- Reticolo idrografico: archivio ufficiale da 60 MB, EPSG:32632. La build usa soltanto RIP (899 linee) e AIPO (76 linee), trasformati in WGS84 e semplificati; RIB e RIM restano esclusi.

## Fonti ancora da recuperare

Aggiornato il 22 agosto 2026. IZSLER veterinario, BDN e studi peer-reviewed food/fauna/ambiente CC BY sono stati caricati.

Restano aperti:

- ClassyFarm: cruscotti DDDAit regionali su VetInfo, accesso autenticato; serve un export ufficiale;
- sorveglianza regionale delle acque reflue con geni AMR: annunciata, dataset ancora non pubblicabile;
- AMR su carne al dettaglio con geografia lombarda separabile e licenza CC BY;
- licenze da sbloccare prima di pubblicare numeri: Cortimiglia 2016 (Cambridge), Fusar Poli/Addis 2024 (Elsevier), Turolla 2018 (CC BY-NC-ND);
- DGR 4561/2025: gia in SOURCES.tsv come riferimento di governance, non come evidenza AMR.

## QA e limiti tecnici

- PDF AWaRe, PPS-3 e pediatrico acquisiti in snapshot raw con SHA-256 e verificati tramite estrazione testuale locale e fonte ufficiale online.
- Il rendering locale dei grafici e stato prodotto con Poppler, ma la visualizzazione nell'app e fallita per helper_unknown_error; per prudenza sono stati esclusi i valori non verificabili come testo.
- L'XLSX SIRe e stato importato in sola lettura con artifact-tool; nessuna riga impianto viene redistribuita.
- I venv creati dentro Google Drive sono risultati incompleti/corrotti durante la sincronizzazione; la trasformazione GIS usa uv con ambiente effimero in cache.
