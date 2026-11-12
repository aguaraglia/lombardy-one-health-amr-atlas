# Verifica e rimozione di Ferrara et al. 2024

PMID 38789634. DOI 10.1007/s00210-024-03117-4. *Naunyn-Schmiedeberg's Archives of Pharmacology*, 2024. Verifica su PubMed (efetch del record completo) e su Europe PMC (core). Il full text non è in PMC (`inPMC` N, `isOpenAccess` N, nessun PMCID). Unpaywall segnala accesso chiuso e nessuna copia aperta. Il PDF Springer (`link.springer.com/content/pdf/10.1007/s00210-024-03117-4.pdf`) da questa rete restituisce una pagina di controllo, non il testo. Metodi e sede di arruolamento non sono quindi citabili oltre abstract, titolo e afferenze.

## Perché era nel catalogo

Il 16 agosto 2026 il commit `e8b8b49` («Expand curated Lombardy AMR literature») ha inserito il PMID nella selezione di `scripts/refresh_literature_from_pubmed.py` con questa nota, scritta a mano e non estratta dai metodi:

> Studio real-world in un ospedale lombardo su nuovi antibiotici per Gram-negativi multiresistenti

La nota ripete il titolo, che dice «an Italian real-world evidence study in a Lombardy hospital», senza nominare l'ospedale.

## Titolo e abstract

Titolo:

> The use of new antibacterial drugs against infections caused by multidrug-resistant Gram-negative bacteria: an Italian real-world evidence study in a Lombardy hospital.

L'abstract descrive 104 pazienti, schede AIFA e cartelle cliniche, e non nomina una città o un ospedale. Non compaiono Lombardia, Milano, Monza, Pavia, Bergamo o Brescia. La frase sui dati è:

> All data have been collected retrospectively from patient's medical records and entered into an electronic case report form (CRF). Among the 104 treated patients, Klebsiella spp. accounted for 50.1% of infections...

## Afferenze, tutte

1. Francesco Ferrara, corresponding author: «Pharmaceutical Department, Asl Napoli 3 Sud, Dell'amicizia Street 22, 80035, Nola, Naples, Italy.»
2. Roberta Pasquinucci: «Pharmaceutical Department, Asl Napoli 3 Sud, Dell'amicizia Street 22, 80035, Nola, Naples, Italy.»
3. Anna Chiara Aloisi: «Fondazione IRCCS San Gerardo dei Tintori di Monza, G.B. Pergolesi Street 33, 2900, Monza, Italy.»
4. Giacomo Polito: «Pharmacy Unit, Policlinico Umberto I Hospital, del Policlinico Street 155, 00161, Rome, Italy.»
5. Gabriele Bagaglini: «Pharmacy Unit, ASL Latina, Pier Luigi Nervi Street, 04100, Latina, Italy.»
6. Maurizio Capuozzo: «Pharmaceutical Department, Asl Napoli 3 Sud, Marittima Street 3, 80056, Ercolano, Naples, Italy.»
7. Andrea Zovi: «Ministry of Health, Viale Giorgio Ribotta 5, 00144, Rome, Italy.»

L'unica afferenza in Lombardia è quella di Aloisi, a Monza. Non è detto che i 104 pazienti siano stati arruolati al San Gerardo. L'autore corrispondente e altri due autori sono all'ASL Napoli 3 Sud. Gli altri sono a Roma e a Latina.

## Decisione

Non c'è una sede di campionamento documentata in Lombardia. Il titolo afferma un ospedale lombardo e non lo nomina. L'afferenza di Monza non basta a collocare lo studio. La voce è tolta dal catalogo e dallo script di aggiornamento, e non è messa su un layer. Il catalogo resta di 52 studi.
