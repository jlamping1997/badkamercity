# BRAUER-24 — specificatieronde afgerond, 8 november 2026

De resterende bronverwerking is afgerond. Catalogus, vragenlijst en definitieve specificatie-Excel zijn nu op dezelfde gecontroleerde stand. **Geen Shopify-write of import, ook geen DRAFT.** Volledige officiële afbeeldingen en PDF’s zijn nog niet ontvangen. Er is geen actieve bronlezer of schrijver na deze overdracht.

| Onderdeel | Eindstand |
| --- | ---: |
| Unieke artikelen | 13.161 |
| Specificatievelden, inclusief artikelidentiteit | 173.785 |
| Extra velden sinds de overgedragen stage3 | 10.324 |
| Extra velden sinds BRAUER-23 | 29.707 |
| Cumulatieve aanvullende herkomst | 38.426 |
| Daarvan externe exacte artikelbronnen | 34.126 |
| Daarvan letterlijke leveranciersgegevens | 4.300 |
| Artikelen met ontbrekende gekozen kernvelden | 7.005 |
| Open retailveldverschillen | 31 |
| Verdachte slangwaarden, ingehouden | 288 |
| Concrete vragen / betrokken artikelen | 361 / 357 |
| Oorspronkelijke gegevensblokkades, behouden | 42 |
| Toekomstige artikelen, behouden | 163 |

De tellingen overlappen. Ontbrekende kernvelden zijn geen ontbrekende producten. Ingevulde kernvelden betekenen geen volledige technische vrijgave.

## Bronverwerking

De 4.748 bewaarde nieuwe technische records zijn gebruikt zonder de pagina’s opnieuw te lezen. Bestaande en pending bronrecords zijn op bron-URL samengevoegd; pending gaat bij dezelfde URL voor. Alle 220 resterende SKU/EAN/URL-aanvragen zijn opnieuw anoniem gelezen. Elke aanvraag leverde een technische tabel met exact merk BRAUER, fabrikantartikelnummer én EAN op. Geen leesfouten in deze hervatting, dus geen extra herhaalverzoeken nodig. De gepubliceerde limiet van 150 URL’s/minuut bleef gelden; het ophaalproces gebruikte een lagere grens. Geen blokkade omzeild of betaalde uitbreiding ingeschakeld.

De oorspronkelijke primaire werklijst van 4.968 kandidaten is daarmee volledig behandeld. In totaal 5.873 bronrecords, 5.860 bron-SKU’s en 5.870 exacte merk/SKU/EAN-pagina’s. De drie oudere pagina’s zonder EAN blijven uitsluitend vergelijkingsbewijs. Dit is geen onderzoek van iedere artikelpagina voor de gehele catalogus van 13.161 artikelen.

De eerdere 28 open retailverschillen en alle 233 eerder ingehouden slangwaarden zijn behouden; de eindstand is respectievelijk 31 en 288. Geen oude specificatie gewijzigd of verwijderd. Historische verschillen, waaronder verworpen winkelwaarden, blijven aanwezig. Geen afmetingen uit unitloze modelcodes, ontbrekende iconen als Nee, overerving naar andere uitvoeringen of omzetting van 15 naar 150 cm.

`retail_extract.py` weigert nu een lege research-map en voegt gedeeltelijke extracten samen met bestaande getypeerde records. De hervattingscode kan ook de bewaarde getypeerde hervattingsrecords hergebruiken wanneer de ruwe fetchresponses niet aanwezig zijn. De oorspronkelijke duizenden ruwe pagina’s blijven buiten het herstelpakket. De getypeerde bronrecords zijn de gezaghebbende overdracht.

## Controles

- 23 specificatie-, retail- en leverancierstests, negen voorbereidingstests en zes hervattingstests: **38/38 PASS**.
- Herhaalde verrijking: catalogus, veldherkomst, samenvatting, cumulatieve aanvullingen en historische verschillen exact behouden; nul extra velden op de herhaalrun.
- Native XLSX-vergelijking: alle 13.161 artikelregels, 34.126 retailaanvullingen, 4.300 leveranciersaanvullingen en 361 vragen exact gelijk aan de eindgegevens. Twaalf EAN-voorbeelden zijn strings; nul native foutcellen.
- Vijf bladen gerenderd en visueel gecontroleerd. Overzichtformules en opgeslagen uitkomsten 13.161 / 7.005 gecontroleerd.
- Alle businessrecords buiten specificaties/controlenotities gelijk aan het aangeleverde pakket. Prijzen inclusief 21% btw, SKU/EAN, titels, goedgekeurde families/keuzes, eigen aanvullingen, bronbestanden en media behouden.
- Preflight met de correcte catalogus-/gate-argumenten geeft **exitcode 2** en een geldig JSON-blokkeerresultaat. Alle vrijgavevlaggen blijven false.

De Excel-export overschreed eerst de standaard Node-heaplimiet. Dezelfde bouwer is met meer heap en behoud van de al geslaagde renders opnieuw geëxporteerd; de eindexport en native vergelijking zijn geslaagd. Dit is geen claim van een Windows-/Excel-desktopcontrole.

Shopify is alleen voor de MAIN-rol gelezen: voor en na **196341825802**. Geen product-, prijs-, voorraad-, media-, thema- of publicatiewrites. Geen live winkel-, checkout-, Windows-Git- of fysieke Excel-app-test uitgevoerd.

## Herstel en vervolg

De bestaande privé-ZIP en specificatie-XLSX behouden hun identiteit. Begin bij `prepared/HANDOFF_BRAUER24.json`. De samengevoegde `retail-observations.json` bevat de volledige toegepaste bronset; de oorspronkelijke pendingrecords en werklijst blijven bewaard. `retail-lookup-pending.json` en de oorspronkelijke next-batch-queue zijn leeg. `retail-lookup-resume-targets.json` is de historische inputlijst van 220 aanvragen, geen nieuwe werklijst.

Codecheckpoint: **419b9104e0d699f739a58cb39c60e5dcc50db13c** op `fix/product-cards-2026-10-14`; zes codepaden remote exact geverifieerd. Main blijft alleen de documentatie-ingang. De scratchomgeving is geen lokale Windows-Git-worktree.

**Eén volgende taak:** de 361 concrete vragen op actuele officiële artikelbladen/tekeningen controleren zodra die worden aangeleverd. Daarna blijven de volledige officiële mediainventarisatie, exacte koppeling en beoordeelde representatieve product-/keuzeproef verplicht vóór enige import. Geen volledige technische vrijgave of importgereedheid geclaimd.
