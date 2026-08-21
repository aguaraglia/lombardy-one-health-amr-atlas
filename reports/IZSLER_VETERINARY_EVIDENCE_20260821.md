# Evidenze veterinarie IZSLER - 21 agosto 2026

## Esito

Prima evidenza AMR veterinaria **separabile per la Lombardia** e pubblicabile:

- Parolini et al., *Animals* 2024, 14(14):2043. DOI `10.3390/ani14142043`. PMID 39061505. PMC11273392. CC BY 4.0.
- Tutti gli autori affiliati IZSLER (laboratori di Cremona, Mantova, Brescia).
- Geografia: stalle da latte delle **province di Cremona e Mantova**, campioni diagnostici 2021-2022.
- Record: `izsler_salmonella_dairy_cr_mn_2021_2022` (`public_approved`).

## Numeri pubblicati (n/N dal paper)

- 120 casi in 118 stalle (59 nel 2021, 61 nel 2022); 2710 campioni.
- Prima isolamento da carcasse/organi di vitelli: 74/120 (61,67%).
- Sierotipi sui 120 casi: Dublin 46/120 (38,33%); Typhimurium 28/120 (23,33%); variante monofasica 17/120 (14,17%).
- AST su 51 isolati non ripetuti: ampicillina 38/51 (74,51%); sulfisoxazolo 31/51 (60,78%); tetraciclina 27/51 (52,94%); florfenicolo 19/51 (37,25%); colistina 16/51 (31,37%); cefotaxime 2/51 (3,92%).
- Resistenza a 5 o piu classi: 24/51 (47,06%).
- Per sierotipo (testo, sezione 3.6): Typhimurium ampicillina 14/14 e tetraciclina 14/14; monofasica ampicillina 10/10 e tetraciclina 9/10; Dublin colistina 16/18, ampicillina 6/18, tetraciclina 0/18.

Non sono stati interpolati i 14 farmaci della Figura 3: solo i valori dichiarati nel testo e nelle tabelle.

## Interpretazione

Coorte diagnostica, non prevalenza regionale. Nessun identificativo aziendale. Nessun layer geografico aggiunto.

## Scartato o ancora candidate

- Linee guida regionali coniglio/bovino/suino: gia in catalogo come stewardship, non dataset AMR.
- ClassyFarm (sistema IZSLER): cruscotti DDDAit regionali su VetInfo, accesso autenticato. Non redistribuibile senza export ufficiale. Lo stub `izsler_amr` resta `candidate`.
- Survey suini ESPHM 2025 (Emilia-Romagna **e** Lombardia): geografia mista, non staccabile.
- Progetti IZSLER in banca dati ricerca senza risultati pubblici (PRC2020004 e analoghi).

## File toccati

- `public/data/izsler_salmonella_dairy_cr_mn_2021_2022.json`
- `public/data/evidence-catalog.json`
- `public/data/literature-catalog.json`
- `metadata/SOURCES.tsv`
- `atlas.config.json`
- `README.md`
- questo report

Rebuild locale (`scripts/build.ps1`) per aggiornare `site/`.

## Aggiornamento (stesso giorno)

Seconda evidenza pubblica IZSLER, CC BY:

- Rodriguez-Lopez et al., *Foods* 2020, 9(9):1141. DOI `10.3390/foods9091141`. PMID 32825203. PMC7555242.
- 88 unita di ingrasso in Lombardia (2016-2018); 440 tamponi animali (77/440 MRSA, 17,50%); 150 ambientali (10/150, 6,67%); 87 isolati.
- Tetraciclina 85,05%; ceftiofur 48,28%; tiamulina 32/87 (36,78%); doxiciclina 32,18%; enrofloxacina 27,59%; gentamicina 25,29%; SxT 9/87 (10,34%); MDR 67/87 (77,01%).
- Penicilline: non-suscettibilita >91,95% (soglia testuale, senza n esatto).
- Non e stata ripubblicata la Table 2 isolate-level.

Cortimiglia et al. 2016 (PMID 27457497) resta `candidate`: testo libero su PMC ma licenza Cambridge non CC BY confermata. Gia presente in `literature-catalog.json`.

Guaita 2026 (mastiti MIC) e il survey suini ESPHM 2025 restano misti Lombardia+Emilia-Romagna: non caricati.
