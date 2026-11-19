# Wiesbaden batch 12 — 10 november 2026

Status: CONCEPT_1239 / BATCH12_VERIFIED. Alleen vervolgconcept 196441932042 (UNPUBLISHED) valt binnen deze uitbreiding. MAIN 196416504074 en reserve 196395073802 behouden; geen publicatie.

## Resultaat en telling

203 nieuwe artikelen in 42 groepen. Cumulatief 1239/2451 uitgebreide artikelen en 159 groepen; 1212 overige artikelen nog te beoordelen/open. Dit is een uitbreidingsteller: niet ieder resterend artikel heeft een menu nodig. Bestaande bruikbare kleurmenu’s zijn niet als nieuwe toevoeging geteld. Bij Rhea M voegt Links/Rechts een relevante keuze toe aan de bestaande kleurkeuze.

| Partij | Artikelen | Groepen | Keuzes |
|---|---:|---:|---|
| Fonteinen en exacte fonteinsets | 40 | 12 | Links/Rechts; kleur waar variabel |
| Douchebak, doucheputten, planchet, profiel, paneel, Larx en Marmaris | 17 | 8 | Volledig formaat of Links/Rechts |
| Doblar-badafvoer en Caral-badplug | 16 | 2 | Kleur/afwerking |
| UniMatch clickwaste/open afvoerpluggen | 29 | 4 | Kleur; open/clickwaste en standaard/verlengd apart |
| UniMatch fontein-/wastafelsifons | 14 | 2 | Kleur; beide modellen apart |
| UniMatch handdouches en wandhouders/-bochten | 37 | 6 | Kleur; vaste, kantelbare en overige modellen apart |
| UniMatch sifonverlengbuis en vloerbuis | 13 | 2 | Kleur; producttypen apart |
| Oriona-lampen en Callista-radiatoren | 13 | 2 | Kleur; vaste eigenschappen niet als keuze |
| Tivaro-bidetsets | 6 | 1 | Kleur/afwerking |
| Alonzo toiletrolhouders | 18 | 3 | Kleur; planchet, vrijstaand met reserve en vaste arm apart |

Geen extra keuzes voor vaste eigenschappen. Quartz, Carrara, gewone keramiek en solid surface blijven afzonderlijke bronfamilies; losse fonteinen en complete sets blijven gescheiden. De bron noemt Quartz keramiek: geen onbewezen mineraal-/materiaalclaim toegevoegd. Er is geen nieuw passendheids-, montage- of componentenadvies toegevoegd.

## Identiteit, bronnen en technische controle

Alle 203 artikelen: officieel wiesbaden.nl-bronrecord, exacte leveranciersidentiteit en verse actieve/gepubliceerde/enkelvariant-Adminidentiteit gecontroleerd. De bronrecords dateren van 19 oktober; leverancieridentiteit van 21 oktober. Geen claim dat alle fabrikantpagina’s opnieuw zijn opgehaald. 202 leverancier-EAN’s matchen de winkel; bij 33.4422 ontbreekt de winkel-EAN maar bestaat een exacte leveranciers-SKU/merkmatch met leverancier-EAN. De bestaande titel van 33.4422 gebruikt `5/4 × 32` waar de bron `5/4" x 32` schrijft; gecontroleerde typografische normalisatie, geen titelwijziging.

UniMatch-fonteinsifons hebben inconsistente bronclassificaties Bekersifon/P-sifon/Overig. Alle zeven officiële, vanuit wiesbaden.nl gelinkte Compano-lijntekeningen bevestigen dezelfde flesvorm en maten: lichaam Ø50 × 90 mm, G1¼-inlaat verstelbaar 15–80 mm, uitlaat Ø31,75 × 330 mm, rozet Ø65 mm. Foto’s van vier afwerkingen stemmen daarmee overeen. Dit ondersteunt kleurnavigatie; oorspronkelijke specificaties niet herschreven en geen hydraulische gelijkwaardigheid geclaimd. Bewijs: [primaire tekeningen en geometriecontrole](BATCH12_SOURCE_CHECKS.json).

Lotte is één gesloten matrix van drie kleuren × twee kraangatzijden. Vier bestaande onvolledige kleurverwijzingen krijgen uitsluitend de ontbrekende variant aan dezelfde zijde erbij; alle oude product-ID’s blijven behouden. De twee overige Lotte-kleurvelden worden aangemaakt. Rhea M en Quartz-set behouden hun tien bestaande, al volledige kleurverwijzingen.

## Buiten deze uitbreiding

Veertien intake-artikelen blijven apart:

- Vier Slim-uitlopen: bestaande verwijzingen naar twee producten buiten de gecontroleerde intake; geen verwijzingen verwijderd.
- 33.4494: bron noemt Pop-up en overloop Ja waar gewone open-plugvarianten Nee/Nee vermelden.
- 33.4451: bron noemt hefstang Ja tegenover Nee bij peers.
- 33.4492: bron noemt volledig sluitend Ja tegenover Nee bij de andere open witte plug.
- 29.6900: kunststof en antikalk Nee tegenover messing/Ja bij de gewone staafhanddouches; tweekleurige uitvoering apart gehouden.
- Zes UniMatch-glijstangen: tekeningen ondersteunen gelijke geometrie, maar bronverschil Met slang Ja/Nee bewijst niet dezelfde verpakkingsinhoud. Hele cohort aangehouden.

Eerdere holds voor dubbele cabine-/Slide-identiteiten, Comfort 20000 mm, Alvara-materiaal, Less-liftscharnier, Caral-inbouwdelen/foreign refs, gemengde kunststofslangen, ontbrekende bronnen/leveranciers en MAIN 41.3665 blijven gelden. Bestaande verschillen in bronspecificaties, zoals Rhea-bevestigingsmateriaal en hoekmontage, zijn niet omgezet in nieuwe claims.

## Writes en bewijs

Toegepast en exact teruggelezen: 363 velden, bestaande uit 203 nieuwe `custom.switch_group`-velden, 156 nieuwe `custom.color_variants`-velden en vier append-only CAS-uitbreidingen van Lotte-kleurvelden. Tien bestaande gevulde kleurvelden blijven exact behouden. 170 producten hebben een kleurmenu in 26 groepen; 33 hebben alleen formaat/richting. 44 conceptfiles: 42 begrensde JSON-assets plus section/router. De bestaande JS-renderer blijft ongewijzigd.

- Onafhankelijke lokale review PASS: 203 bron-/leverancier-/Adminidentiteiten, 227 optiewaarden rechtstreeks vergeleken met bronafwerking, bronmaten of bronrichting, 42 unieke combinatiesets, 170 exacte kleurreferentiesluitingen, 42 payload-/SHA256-matches en alle 363 mutatievoorwaarden. Geen oude referentie verwijderd.
- Bestaande renderer met DOM-substitutie PASS: 203 startstanden en 948 geldige aswissels; 203 dubbele-combinatie- en navigatiefouten afgewezen. Alle matrices zijn volledig na de gekozen holds; daarom nul ontbrekende combinaties in deze batch. 1058 exacte kandidaatafbeeldingen, 170 compatibele prijsvolgordes en referentiesets; identiteits- en afbeeldingsfouten vallen veilig terug.
- Strikte lokale Liquidparser PASS op baseline en beide gewijzigde bestanden. Dit is geen Shopify Theme Check of runtimevalidatie; geen externe validatie-/telemetriehelper uitgevoerd.

Admin-readback PASS: alle 363 geschreven waarden exact, alle 203 geselecteerde productidentiteiten en overige opgehaalde velden ongewijzigd. De tien niet-gewijzigde gevulde kleurvelden zijn inclusief hun metadata behouden. Alle 44 conceptbodies exact teruggelezen; verwijdering van alleen de bedoelde groeps-/routertoevoegingen levert de vorige code terug, afgezien van eindwitruimte. JS-checksum behouden. Verse eindcontrole: catalogus 2451 EXACT, MAIN-rol en drie codechecksums ongewijzigd, vervolgconcept UNPUBLISHED.

Publieke servermarkup PASS: 58/58 previewpagina’s over alle 42 groepen. Productidentiteit, SKU, prijs, foto, formulier-variant en de begrensde JSON-route gecontroleerd. Alle 42/42 openbare JSON-assets volledig gelijk aan de voorbereide inhoud en SHA256. Twee MAIN-formulieren, de bestaande Rhea M-kleuren en de uitgebreide Lotte-kleurkoppeling zijn intact. Deze steekproef is geen volledige HTTP-ronde van 203 artikelen.

Desktopbrowser PASS: Lotte 36.4039 (mat wit, Rechts, €145) toont drie kleuren en twee zijden. Klik Mat zwart opent 36.4046 (Rechts, €179); klik Links opent 36.4047 (mat zwart, €179). Andere keuze en juiste productidentiteit blijven behouden. Previewbalk bevestigt het vervolgconcept.

NOT_TESTED: volledige 203 HTTP-paginaronde, native mobiel, echte winkelwagenregels en checkout, browserwissels in alle 42 nieuwe groepen, volledige regressie van oudere groepen. Gesimuleerde DOM- of schermbreedtecontrole bewijst geen native mobiele werking. Geen lokale Windows clean/statusclaim. Geen prijs-, voorraad-, specificatie-, titel-, productpublicatie- of indexeringsmutaties uitgevoerd.

## Herstel en overdracht

[BATCH12_ADMIN_CHANGES.json](BATCH12_ADMIN_CHANGES.json) bevat de exacte 363 before/after-waarden. Verwijder de 359 nieuw aangemaakte velden alleen na een verse exacte vergelijking met after. Herstel de vier bestaande Lotte-kleurvelden naar hun eigen before-waarden met een verse compareDigest; verwijder deze velden nooit. De tien ongewijzigde bestaande kleurvelden behouden.

Section/router in het vervolgconcept herstellen uit batch-11-parent `074df250228df7dda6be6c666d428574838841b4`. De 42 nieuwe ongebruikte JSON-assets mogen blijven. MAIN en reserve niet schrijven; overige groepen behouden. Codebranch `fix/product-cards-2026-10-14`, themabron `shopify/current`. Geen credentials, klantgegevens, inkoopprijzen of settings_data-body in publieke bestanden.

Gerichte mobiele/cart-QA op het vervolgconcept blijft nodig vóór eigenaarpublicatie. Verdere gecontroleerde producttypepartijen blijven binnen de eigenaaropdracht toegestaan; na overdracht geen actieve schrijver achterlaten.
