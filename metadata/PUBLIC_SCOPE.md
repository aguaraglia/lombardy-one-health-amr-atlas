# Ambito pubblico del Lombardy One Health AMR Atlas

La base pubblica verificata comprende:

- confini ISTAT generalizzati al 1 gennaio 2026: 1.502 comuni, 12 province/città metropolitana e regione;
- sei indicatori AR-ISS 2024 aggregati per la Lombardia, con numerosità, percentuale, IC 95% e copertura regionale del 53,7%;
- consumo e spesa complessiva di antibiotici OsMed 2024;
- sintesi MICROBIO 2023 per adulti, limitata ai 31 presidi pubblici inclusi dal report e accompagnata dai limiti metodologici;
- sintesi MICROBIO pediatrica 2023: 1.311 eventi BSI, 36 isolamenti da liquor e nove pattern selezionati da antibiogrammi cumulativi regionali;
- quote AWaRe 2025 di consumo territoriale per 25 ASST e tre fasce di popolazione;
- aggregati PPS-3 su ICA, uso di antimicrobici e pattern di resistenza in 28 strutture per acuti, raccolti nel 2022;
- sintesi regionale SIRe Acque 2025 su carichi e controlli, esclusivamente come contesto ambientale non-AMR;
- conteggi SIRe 2025 aggregati per provincia, ricavati dai 23 consuntivi ufficiali e pubblicati senza identificativi o coordinate di impianto;
- reticolo idrografico principale RIP/AIPO di Regione Lombardia, trasformato in WGS84 e semplificato per uso cartografico;
- 480 impianti di trattamento delle acque reflue urbane georiferiti dal servizio cartografico pubblico di Regione Lombardia, mantenuti distinti dai dati SIRe 2025 e dai punti di campionamento AMR;
- coorte diagnostica IZSLER su Salmonella enterica in stalle da latte delle province di Cremona e Mantova (2021-2022; 118 aziende, 51 isolati con MIC); evidenza di studio, non prevalenza regionale e senza identificativi aziendali;
- coorte IZSLER su MRSA in 88 unita di ingrasso suino lombarde (2016-2018; 87 isolati aggregati, CC BY); non prevalenza regionale corrente e senza identificativi aziendali;

- consistenze BDN giugno 2026 (aggregati regionali, non AMR): 1.492.937 bovini, 3.949.063 suini da ingrasso/riproduzione, 80.353 ovini e 62.001 caprini; nessun identificativo aziendale;
- letteratura scientifica con collegamento territoriale esplicito alla Lombardia, mantenuta distinta dai dataset.

Gli export SIRe 2025 sono conservati come snapshot raw esclusi da Git e non vengono redistribuiti a livello di singola riga. Il layer puntuale usa invece un servizio cartografico regionale pubblico separato, con soli campi essenziali e con l'anno del rilievo esplicitato. Il reticolo minore e di bonifica non è incluso nella build per evitare un layer sproporzionato e non necessario.

Non sono pubblicati record individuali, identificativi di paziente o campione, coordinate cliniche, dati aziendali o di allevamento, dataset autenticati, né fonti prive di condizioni d'uso e trasformazione verificabili. Le tabelle pediatriche per singola struttura non vengono ripubblicate. Gli indicatori regionali non vengono attribuiti a comuni o strutture e non sono combinati in un indice sintetico di rischio.
