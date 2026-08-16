# Perimetro della release pubblica Lombardia

Stato iniziale: struttura tecnica senza dataset AMR regionali pubblicati.

La build pubblica include template, runtime, configurazione e cataloghi. I
record marcati `candidate`, `verified` o `restricted` non sono caricati dal
browser. Un file presente sotto `public/` non e' automaticamente pubblicabile:
deve essere referenziato da un catalogo con stato `public_approved`.

Sono sempre esclusi:

- coordinate di aziende, allevamenti, campioni o pazienti;
- identificativi individuali o di isolato non gia' pubblicati e necessari;
- dati clinici granulari;
- estratti ottenuti da servizi autenticati senza autorizzazione al riuso;
- inferenze comunali o provinciali non documentate dalla fonte;
- dati sardi usati come segnaposto.
