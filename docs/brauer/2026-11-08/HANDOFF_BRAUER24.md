# BRAUER-24 — overdracht op verzoek eigenaar, 8 november 2026

De actieve leescel is gestopt; geen bronraadpleging of schrijver draait door. De eigenaar gaat verder in een nieuwe chat. Niets geïmporteerd, gepubliceerd of naar Shopify geschreven. Volledige officiële afbeeldingen/PDF’s nog niet ontvangen.

## Gegevensstand

- 13.161 unieke artikelen uit de drie al geleverde leveranciersbestanden.
- Actuele catalogus163.461feiten,19.383extra specificaties sinds BRAUER-23; bronverwerking toegepast tot4191pagina’s. Nog8515artikelen met minimaal één ontbrekend gekozen kernveld.
- 28open retailveldverschillen en233verdachte slangwaarden. Oorspronkelijke42dataholds en163toekomstige artikelen behouden.
- Primaire werklijst4968kandidaten. Eerste ronde tot4950;4748nieuwe technische tabellen bewaard. Voor220kandidaten geen tabel bewaard, waaronder de laatste18die niet afgerond zijn. Nog geen herhaalronde uitgevoerd.
- Excel en open-work.json lopen achter: gecontroleerde stage2,155887feiten,20528cumulatieve aanvullingen en178vragen. Native PASS toen; niet als definitieve nieuwste stand behandelen.32tests PASS op stage2, eindcontroles nog uitvoeren.

## Herstelbare bestanden

Het bestaande privébestand Brauer-importpakket-2026-11-07.zip bevat de overdracht. Lees prepared/HANDOFF_BRAUER24.json. De oorspronkelijke bronbestanden, gebruikersaanvullingen en gesloten vrijgave zijn behouden.

prepared/retail-observations-pending.json bevat4748getypeerde nieuwe bronrecords, deels al toegepast. Samenvoegen met prepared/retail-observations.json, dedupliceren op bron-URL en de nieuwe pendingrecord bij dubbele URL laten voorgaan. Niet opnieuw alle4748pagina’s lezen. prepared/retail-lookup-pending.json bevat de220concrete resterende SKU/EAN/URL-combinaties; prepared/retail-lookup-targets.json de volledige oorspronkelijke werklijst.

**retail_extract.py niet blind uitvoeren op het herstelpakket:** ruwe research-tabelextracten zijn daarin niet gebundeld; de getypeerde bronrecords zijn de overdrachtsbron. Een lege research-map mag retail-observations.json niet leeg overschrijven.

De oude retail-next-batch-queue.json is eveneens stage2; gebruik voor hervatten de nieuwe retail-lookup-pending.json.

## Eén volgende taak

De220nog onvoltooide kandidaten afronden: tijdelijke fouten éénmaal opnieuw, gepubliceerde leeslimiet150URLs/min respecteren; geen blokkade omzeilen of betaalde uitbreiding activeren. Alle bronrecords op URL samenvoegen, exacte merk/SKU/EAN-guards behouden en enrich_retail_specifications.py draaien. Daarna build_open_work.py, de32tests, preflight (bewust exit2), nieuwe Excel-export en nativevergelijking met de definitieve catalogus/aanvullingen/vragen. De nativecontrole staat ook onder controles/verify-retail-workbook.py; daarvoor analysis-map aanmaken.

Bestaande keuzegroepen, prijzen inclusief btw, SKU/EAN, titels, notities en media behouden. Geen fysieke maten uit unitloze modelcodes, ontbrekend Ja/Nee niet als Nee,15cm-slangbron niet automatisch150cm, historische tegenspraak niet laten verdwijnen op herhaalruns. Badkamervoorjou uitgesloten. Iedere Shopify-import, ookDRAFT, wacht op volledige officiële mediaontvangst/inventarisatie en latere beoordeelde proef.

Actieve codebranch fix/product-cards-2026-10-14; main is de documentatie-ingang. Broncode onder shopify/current/ raakt deze offline taak niet. Geen lokale Windows-/Excel-app- of live winkelcontrole geclaimd.
