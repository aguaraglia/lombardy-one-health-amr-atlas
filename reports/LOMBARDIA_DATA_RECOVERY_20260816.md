# Recupero dati Lombardia - 16 agosto 2026

## Esito

La base ufficiale pubblicabile comprende ora geografia ISTAT 2026, AR-ISS 2024, OsMed 2024, MICROBIO 2023, AWaRe 2025, PPS-3, una sintesi regionale SIRe 2025 e il reticolo idrografico principale. Nessun dato individuale, clinico puntuale o riservato e stato acquisito o pubblicato.

## Nuove evidenze sanitarie

- AWaRe 2025: quote Access/Watch/Reserve per 25 ASST, con popolazione generale, under 14 e over 65. Il dato riguarda consumi territoriali dei residenti e non include l'uso ospedaliero.
- PPS-3: 28 strutture per acuti, 39 presidi e 12.412 pazienti rilevati tra novembre e dicembre 2022. Pubblicati aggregati su ICA, uso di antimicrobici e sette pattern di resistenza, con copertura e limiti del report.
- I valori presenti solo nei grafici regionali AWaRe non sono stati trascritti: le tabelle ASST sono state estratte senza ambiguita dal PDF ufficiale.

## Contesto ambientale

- SIRe 2025: acquisiti due ZIP ufficiali ARPA. Il foglio completo contiene 1.513 righe dati e 73 colonne; il sito pubblica solo aggregati regionali (18.844.231 AE di carico generato sommato, 5.524 controlli previsti, 7.014 eseguiti e 33 righe marcate non regolamentari per numero/modalita di controllo). Non sono misure AMR.
- Reticolo idrografico: archivio ufficiale da 60 MB, EPSG:32632. La build usa soltanto RIP (899 linee) e AIPO (76 linee), trasformati in WGS84 e semplificati; RIB e RIM restano esclusi.

## Fonti ancora da recuperare

- evidenze veterinarie lombarde separabili da IZSLER, non sole linee guida;
- consistenze zootecniche regionali BDN/VetInfo con licenza e data verificabili;
- studi peer-reviewed lombardi su filiera alimentare, fauna e ambiente con dati misurati.

## QA e limiti tecnici

- PDF AWaRe e PPS-3 acquisiti in snapshot raw con SHA-256 e verificati tramite estrazione testuale locale e fonte ufficiale online.
- Il rendering locale dei grafici AWaRe e stato prodotto con Poppler, ma la visualizzazione nell'app e fallita per helper_unknown_error; per prudenza sono stati esclusi i valori non presenti come testo.
- L'XLSX SIRe e stato importato in sola lettura con artifact-tool; nessuna riga impianto viene redistribuita.
- I venv creati dentro Google Drive sono risultati incompleti/corrotti durante la sincronizzazione; la trasformazione GIS usa uv con ambiente effimero in cache.
