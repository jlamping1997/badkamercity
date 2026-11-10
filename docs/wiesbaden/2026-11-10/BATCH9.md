# Wiesbaden batch 9 — 10 november 2026

Status: IMPLEMENTED_TEST_ONLY. MAIN196416504074 behouden. Vervolgconcept196441932042 (BadkamerCity - Wiesbaden vervolg concept) blijft UNPUBLISHED. Reserve196395073802 behouden. Geen publicatie of MAIN-filewrite.

## Resultaat
104artikelen onderzocht;102toegevoegd in23groepen. Twee Comfort-hoekprofielzijwanden vastgehouden. Cumulatief731/2451artikelen met uitgebreide keuzemenu’s en62groepen. Actuele vendor-telling2451EXACT;1720overige artikelen nog te beoordelen/open, niet allemaal vragen een menu. De teller is een uitbreidingsteller, geen claim dat elke resterende SKU een menu moet krijgen.

| Partij | Artikelen | Groepen | Keuzes |
|---|---:|---:|---|
| Spiegels |49|14|Formaat of diameter; alleen Novi ook kleur|
| Slim losse glasplaten |38|6|Breedte; glassoort/melkglas per groep vast|
| Comfort inloopdouche |11|1|Breedte / glasdikte in één keuze|
| Comfort zijwand draaibaar / muurprofiel |4|2|Breedte|

96artikelen hebben slechts één maatmenu;6Novi-spiegels kleur+diameter. Geen overbodige vaste kleur-/hoogteknoppen. Tigris met scheerspiegel en met stopcontact blijven afzonderlijk van basisuitvoering en elkaar. Ronde/rechthoekige/organische spiegels niet samengevoegd. Slim glasplaten blijven losse glasplaten, geen complete-setclaim; profielset/stabilisatiestang niet aan de keuze toegevoegd.
Comfort50–130cm heeft10mmglas;140/160cm heeft8mmglas. Eén menu met expliciete waarden zoals70cm/10mm en140cm/8mm voorkomt dat een breedtekeuze de glasdikte verbergt.

## Bronnen en holds
Voor alle102 actuele SKU/variant/leverancieridentiteit en volledige titel exact gematcht met bestaande officiële wiesbaden.nl-bronrecords (19oktober); geen titel-normalisaties nodig. Slim20.3452fabrikantbron opnieuw opgehaald (cachevorigemaand): losse8mmglasplaat, profielset apart. Geen brede claim van102verse fabrikantpagina’s. badkamervoorjou.nl niet gebruikt.
Nieuwe hold:20.3819 versus20.3820 Comfort-zijwand hoekprofiel. Titel/dimensie van20.3820noemt400×20000×10mm tegenover300×2000×10mm. Niet stil naar2000gecorrigeerd of in één eenvoudig breedtemenu gezet; beide blijven buiten deze uitbreiding tot broncontrole.
Eerdere Caral/inbouwdeel-, Slide-duplicate-, Alvara-materiaal-, Less-liftscharnier- en MAIN41.3665lege-kleur-labelholds behouden. Bestaande correcte kleurmenu’s zoals Nomi/Renk niet opnieuw opgebouwd.

## Snellere controlewijze
De bestaande renderer blijft identiek. Elke nieuwe SKU en elke mogelijke aswissel wordt lokaal geverifieerd; publieke pagina’s worden per nieuwe groep bemonsterd, plus extra risicogevallen. Elke nieuwe JSONasset wordt publiek éénmaal exact op hash en volledige inhoud gecontroleerd. Zo hoeven we de identieke producttemplate niet voor alle102SKU’s volledig opnieuw te downloaden. Dit is een afgebakende steekproefaanpak, geen claim van102HTTP-paginatests.
Nodige batchgates blijven: exacte bronidentiteit, technische uitvoering/groepsgrens, unieke combinatie, gepubliceerd/actief/enkelvariant, geen bestaande switch_group overschrijven, bestaande prijs en SKU behouden. Een afwijking gaat in hold in plaats van onbewezen normalisatie.

## Testbewijs
-102create-only custom.switch_group velden compareDigest:null. Alle102exact teruggelezen; alle geselecteerde overige velden en alle kleurverwijzingen exact behouden. Geen custom.color_variants-writes.
-25conceptbodies exact teruggelezen:23beperkteJSONassets, section/router. Bestaande JSrenderer checksumgelijk. Section alleen23groepIDs toegevoegd; router46regels toegevoegd.
-Drie MAIN-codechecksums bij start/einde gelijk; rollen onveranderd. Geen prijs-, voorraad-, specificatie-, productpublicatie- of indexeringsmutaties.
-Strikte lokale Liquid-AST baseline en beide gewijzigde bestanden PASS. Geen externe validatie-/telemetriehelper opnieuw uitgevoerd.
-Bestaande JSrenderer met DOMsubstitutie:102startstanden,524geldigeaswissels en102dubbelecombinatie-/navigatiefouten PASS. Novi6bestaande exacte kleurreferentiesets,12kandidaatafbeeldingen,6prijsorders en6identiteits-/afbeeldingfouten PASS. Geen werkelijke mobiele/browser-/cartclaim voor deze simulatie.
-Publiek26/26previewpagina’s PASS, alle23groepen gedekt. Extra andere Novi-kleur, beide Comfort-glasdiktes en Slim160cm. Identiteit/prijs/foto/cartformuliervariant/router/compactkleurenfeiten waar van toepassing exact.
-Publiek23/23JSONassets volledige inhoud enSHA256exact.
-MAIN2bestaande productformulieren/identiteiten intact (Slim/Comfort); Novi-bestaand2kleurenmenu intact. Geen claim van een nieuw werkend maatmenu opMAIN.
-Echte desktopbrowserComfort20.3807(70cm/10mm)→20.3813(140cm/8mm): titel, actievekeuze en geen horizontale documentoverflow bevestigd.
-NOT_TESTED: complete102HTTP-paginaronde, native mobiel, echte cartregels, browserwissels in andere22groepen, volledigeouderegroepenregressie/checkout. Geen Windowslokale clean/statusclaim.

## Herstel en overdracht
[BATCH9_ADMIN_CHANGES.json](BATCH9_ADMIN_CHANGES.json) bevat uitsluitend de102nieuw gecreëerde groepsvelden; before is null. Verwijder alleen deze velden na actuele vergelijking met after, geen bestaande kleurverwijzing wijzigen/verwijderen.
Section/router herstellen uit parentb81fa0d4eee2ee383cf08da2b19f94db8de6bd09 in hetzelfde vervolgconcept. Nieuwe23ongebruikteassets mogen blijven. Andere product-/themagroepen behouden; MAIN en reserve niet schrijven.
Broncode: fix/product-cards-2026-10-14, shopify/current. Geen credentials, klantgegevens, inkoopprijzen of settings_data-body in publieke bestanden.

Volgende handeling: gerichte mobiele/cart-QA op vervolgconcept vóór eigenaarpublicatie; verdere gecontroleerde producttypepartijen binnen eigenaaropdracht toegestaan. Geen actieve schrijver na overdracht.
