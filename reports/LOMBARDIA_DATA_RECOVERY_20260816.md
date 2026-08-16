# Recupero dati Lombardia - 16 agosto 2026

## Esito

Integrata una prima base ufficiale e pubblicabile: geografia ISTAT 2026, AR-ISS 2024, OsMed 2024 e MICROBIO 2023. Nessun dato puntuale o riservato e stato acquisito o pubblicato.

## Geografia

- Scartata come base corrente la serie regionale 2020: 1.506 comuni.
- Adottato ISTAT 1 gennaio 2026, versione generalizzata: 1.502 comuni, 12 province/citta metropolitana, 1 regione.
- Conversione riproducibile da EPSG:32632 a EPSG:4326 con `scripts/build_istat_geography.py`.
- Il pacchetto dichiara UTF-8 ma non contiene file CPG e almeno un record nazionale non e decodificabile come CP1252. Per i record lombardi Latin-1 non produce caratteri di controllo; la scelta e registrata nello script.

## Evidenze sanitarie

- AR-ISS: sei combinazioni regionali da sangue/liquor, con copertura 53,7%. Nessun downscaling.
- OsMed: antibiotici 14,7 DDD/1.000 abitanti/die; indicatore di consumo, non resistenza.
- MICROBIO: 31 presidi pubblici selezionati per qualita del dato, 22.388 eventi BSI adulti; conservati i limiti su definizione degli eventi e distinzione comunitario/nosocomiale.

## Fonti non integrate

- SIRe Acque: nessun export/licenza verificato; resta candidato.
- BDN, agricoltura e veterinaria IZSLER: da acquisire in una fase successiva con la stessa procedura di snapshot, licenza, aggregazione e QA.

## QA

- Tutti i JSON/GeoJSON sono parseabili.
- Conteggi e bounds geografici verificati.
- Hash raw registrati in `metadata/SNAPSHOTS.tsv`.
- AR-ISS e OsMed verificati con estrazione testuale e rendering delle pagine; il visualizzatore PNG dell'app non era disponibile per `helper_unknown_error`.
- Il PDF MICROBIO e leggibile via fonte ufficiale nel browser, ma il server restituisce HTML ai download scriptati; il PDF non e redistribuito localmente.