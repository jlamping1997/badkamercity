# BRAUER-23 — beschikbare leveranciersgegevens verder benut

7 november 2026. De eigenaar vraagt toe te voegen wat nog kan, na verduidelijking dat de drie oorspronkelijke bestanden al geleverd en verwerkt zijn. Offline vervolg op BRAUER-22; geen Shopify-writes, DRAFT-import, media-upload, themawrite of publicatie. MAIN read-only bevestigd196246372618.

## Toegevoegd

Alle13.161artikelen opnieuw beoordeeld op nog onbenutte, letterlijk aanwezige gegevens in de aangeleverde kranen-, glas- en meubelbestanden.4.300extra klantvelden bij4.186artikelen uit die leveranciersgegevens. Daarnaast434extra velden uit de al gecontroleerde openbare technische tabellen; geen nieuwe websitecrawl nodig voor deze batch. Samen4.734extra specificaties bij4.380artikelen. Geen bestaande specificatiewaarde gewijzigd of verwijderd.

Leveranciersaanvullingen:2.696letterlijke uitvoeringsnamen,1.001expliciet genoemde aantallen straalstanden handdouche,414expliciete uitsluitingen van grepen,30draaibare uitlopen,30platte uitloopdoorsneden,28dimfuncties,28lichtkleurfuncties,28afstandsbedieningen,11wasbak-aantallen,9klokken,7uitsluitingen van vulfunctie,7verborgen opbergruimtes,6afgeronde glashoeken en5expliciete links/rechts-plaatsingen van fonteinen. Uitvoeringsnamen zoals Slim/Medium/Wavy worden letterlijk bewaard; geen dikte in millimeters of oppervlaktestructuur uit die naam afgeleid. De plaatsingsrichting van een fontein krijgt een eigen veld en vervangt niet de montageplaats op een onderkast.

Retailtabellen leveren onder andere bediening aan/uit, plaats bediening, hartafstand, vorm/aantal rozetten, plugdiameter en sifonaansluiting. Alleen expliciete eenheden, aantallen en leesbare Ja/Nee-waarden gebruikt. Een sifonaansluiting wordt geen wateraanvoer; ontbrekende iconen leveren geen Nee op. Rozettenkenmerken worden niet zonder context op een afdekplaat toegepast. Met achterplaat en Afdekplaat vergelijken als hetzelfde begrip, zonder bestaande klantwaarden te herschrijven. Doorsnede uitloop en geometrische uitloopvorm blijven verschillende begrippen.

## Bewijs en grenzen

Elke leveranciersaanvulling bewaart exacte SKU/EAN, bronveld, letterlijke bronpassage, bronregels en extractieregel. Retail blijft exact merk+fabrikant-SKU+EAN vereisen; eenzelfde kleur/model of codesuffix is onvoldoende. Nog steeds905productpagina’s,892bron-SKU’s,902exacte merk-SKU-EAN-pagina’s. Drie pagina’s zonderEAN uitsluitend aanvullend bewijs. Cumulatief4.419retailvelden plus4.300nieuwe leveranciersvelden in de aanvullende herkomstlijst. Totaal144.078feiten in de catalogus.

De oorspronkelijke42gegevensblokkades,28open retailveldverschillen bij24artikelen,14verdachte slangwaarden en84concrete vragen bij80artikelen zijn behouden. Eerdere tegenstrijdige maten blijven bewijs, ook nadat de betwiste klantwaarde is weggehaald: opnieuw verwerken mag die waarde niet ongemerkt alsnog invullen. De twee004-B4-maatvelden blijven daarom leeg. Cumulatieve herkomst wordt nu opgebouwd uit actuele veldherkomst; opnieuw uitvoeren wist eerdere aanvullingen niet. Een herhaalcontrole bewijst identieke catalogus, identieke veldherkomst, identieke aanvullende herkomstlijst en28behouden open verschillen.

10.089artikelen missen nog één of meer gekozen kernvelden. Dat aantal is geen aantal ontbrekende producten of een foutpercentage. Een deel van de nieuwe nuttige kenmerken valt buiten die kernveldselectie.4.968onbeoordeelde bronkandidaten blijven op de werklijst; geen achtergrondtaak of volledige cataloguscrawl geclaimd. Officiële afbeeldingen/PDF-aanlevering nog niet compleet ontvangen. Geen derdenmedia als officiële aanlevering aangemerkt.

## Bestanden en controles

De privébundel bewaart de actuele volledige catalogus, veldherkomst, leveranciersaanvullingen, bronobservaties, vragen, oorspronkelijke bestanden en gebruikersnotities. Publieke Git bevat code, tests en geaggregeerde overdracht. De vijf Excelbladen blijven behouden; Aanvullingen toont nu zowel bronbestand/bronregels voor leveranciersgegevens als bron-URL voor retailgegevens. Geen volledige prijslijsten of gebruikersinhoud in publieke Git.

23specificatie-/retail-/leverancierstests en9voorbereidingstests PASS. Alle13.161businessrecords buiten specificaties en controlenotities exact gelijk aan BRAUER-22. Geen prijs/BTW-, SKU/EAN-, titel-, familie-, optie-, notitie- of mediawijziging;163toekomstige artikelen behouden. Preflight terecht exit2, alle vrijgavevlaggenfalse. Geen Windows/Excel-app- of live winkeltest uitgevoerd; lokale scratch is geen Git-checkout. Definitieve nativeXLSX: alle13.161artikelregels,4.419retailaanvullingen,4.300leveranciersaanvullingen en84vragen exact vergeleken met de definitieve gegevens. Twaalf EAN-voorbeelden blijven strings; nul native foutcellen. Recalc13.161/10.089correct. Vijf bladen gerenderd/gecontroleerd en de nieuwe leveranciersregels afzonderlijk bekeken.

**Eén volgende handeling:** verdere openbare bronkandidaten exact op artikelidentiteit onderzoeken voor ontbrekende kerngegevens; uitzonderingsvragen apart laten bevestigen. Na volledige officiële mediaontvangst eerst inventarisatie/exacte koppeling en complete representatieve pagina-/keuzeproef. Iedere Shopify-import blijft geblokkeerd tot die voorwaarden en het akkoord zijn vervuld.
