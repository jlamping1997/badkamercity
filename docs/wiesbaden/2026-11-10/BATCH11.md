# Wiesbaden batch 11 — 10 november 2026

Status: CONCEPT_1036 / BATCH11_VERIFIED. MAIN 196416504074 behouden. Vervolgconcept 196441932042 (BadkamerCity - Wiesbaden vervolg concept) blijft UNPUBLISHED; reserve 196395073802 behouden. Geen publicatie of MAIN-filewrite.

## Resultaat en telling

205 artikelen toegevoegd in 29 groepen. Cumulatief 1036/2451 uitgebreide artikelen en 117 groepen; 1415 overige artikelen nog te beoordelen/open. Deze uitbreidingsteller betekent niet dat ieder resterend artikel een menu nodig heeft.

| Partij | Artikelen | Groepen | Keuzes |
|---|---:|---:|---|
| Caral complete bad-/douchesets | 71 | 6 | Exacte afwerking + baduitlooplengte of hoofddouchediameter |
| Caral losse baduitlopen | 18 | 1 | Afwerking + lengte 20/25/30 cm |
| UniMatch / 304 hoofddouches | 19 | 2 | Diameter; UniMatch ook afwerking en expliciete dikte |
| Caral losse rozetten | 21 | 2 | Afwerking + diameter 65/75 mm; kraangedeelte/uitloop apart |
| Raw, Julia en Rhea XXS-fonteinen | 20 | 5 | Formaat waar variabel; afwerking en Links/Rechts waar variabel |
| Liora, Rivi, Zenn en Trapeze-baden | 22 | 5 | Formaat, glans/mat en Links/Rechts waar variabel |
| Demis ovale inbouwnissen | 4 | 1 | Kleur + diepte 7/10 cm; front 30 × 45 cm vast |
| Losse douchegootroosters | 28 | 6 | Lengte; type/generatie/flensuitvoering afzonderlijk |
| Tigris badkamer-LED | 2 | 1 | Lengte 300/500 mm |

Geen keuzes toegevoegd voor vaste eigenschappen. Raw rond en Julia betonlook hebben alleen een Links/Rechts-keuze. Complete sets blijven gescheiden naar 2 stopkranen/2-weg/overige uitvoering en naar staaf-/3-standenhanddouche; niet aan afbouwdelen gekoppeld. Er is geen nieuw inbouwdeeladvies of claim over meegeleverde componenten toegevoegd.

Bij UniMatch is 20 cm diameter 12 mm dik en 25/30 cm diameter 8 mm dik: het maatmenu vermeldt beide maten. Zwart en Mat zwart blijven de afzonderlijke bronlabels; geen onbewezen finishnormalisatie.

## Bronnen en gecontroleerde sluiting

Alle 205 artikelen hebben een bestaand officieel wiesbaden.nl-bronrecord, exacte leverancieridentiteit en een verse actieve/gepubliceerde/enkelvariant-Adminidentiteit. Namen, SKU’s en variant-ID’s zijn gecontroleerd; geen titelwijzigingen nodig. De fabrikantrecords dateren van 19 oktober. Verse pagina 29.4040 was niet toegankelijk en 29.3041 gaf HTTP 429; geen claim dat 205 fabrikantpagina’s opnieuw zijn gelezen. badkamervoorjou.nl niet gebruikt.

Twee matwitte 180 × 80 cm-halfbaden ontbraken als losse singleton in candidate-families maar zaten al in de bestaande kleurverwijzingen: Liora 21.3672 en Rivi 21.3679. Productregister, officiële bron, leverancier-EAN-match en verse Admin bevestigden beide. Toegevoegd aan hun eigen halfbadfamilie, zodat bestaande kleurkoppelingen behouden blijven. Rivi-hoekbad glans/mat (8) en Zenn-hoekbad glans/mat (6) zijn per identiek model samengebracht; half-/hoek-/vrijstaande baden niet gemengd. Ontbrekende maat/finishcombinaties blijven onbeschikbaar.

De technische Caral-inbouwdeelhold blijft bestaan. Sommige oorspronkelijke fabrieksspecificaties spreken de volledige setnaam tegen, zoals hoofddouche Nee bij een set met hoofddouche of Handbediend bij een thermostaattitel. Deze specificaties zijn niet gewijzigd of als extra productclaims gebruikt.

## Buiten deze uitbreiding

- 15 kunststofslangen blijven apart vanwege gemengde tweekleurige/inleguitvoeringen.
- 11 Caral-sets uit candidate-98a454578719 blijven apart wegens een bestaande kleurverwijzing buiten de gecontroleerde broncohort; geen verwijzing verwijderd om de groep passend te maken.
- 10 artikelen missen een officieel bronrecord en exacte leverancierslookup: onderkast-LED 38.3850/51/52/53 en roosters 33.4137, 33.4222, 33.4230/35, 33.4250/54.
- 29.4045 heeft wel een officieel record, maar geen exacte leverancierslookup/EAN-match. Dit is ontbrekend bewijs, geen vaststelling dat het artikel onjuist is. Ook dit artikel blijft apart.

Eerdere Slide-/cabineduplicaten, Comfort 20000 mm-, Alvara-materiaal-, Less-liftscharnier- en MAIN 41.3665 lege-kleurlabelholds behouden.

## Writes en bewijs

- 205 create-only custom.switch_group-velden en 106 nieuw aangemaakte custom.color_variants-lijsten; alle compareDigest: null. Alle 311 waarden exact teruggelezen. Vooraf waren 55 kleurvelden gevuld en 150 leeg. 106 lege velden gevuld; 99 overige waarden ongewijzigd (55 gevuld + 44 leeg). Geen bestaande lijst overschreven of verwijderd. Referenties bevatten uitsluitend dezelfde overige keuzes, inclusief formaat en Links/Rechts.
- 205 producten: geselecteerde overige waarden ongewijzigd. 31 conceptfiles exact teruggelezen: 29 begrensde JSON-assets plus section/router. Bestaande JS-renderer ongewijzigd. Definitieve MAIN-role en drie codehashes ongewijzigd; producttelling 2451 EXACT.
- Onafhankelijke tweede controle: 205 exacte bron-/leverancier-/Adminidentiteiten, 386 afzonderlijke optiewaarden, 161 referentiesluitingen, 29 asset-SHA256’s en 311 create-only inputs PASS. Dit is een datacontrole, geen browser-/cartclaim.
- Strikte lokale Liquidparser op baseline en beide gewijzigde bestanden PASS. Geen externe validatie-/telemetriehelper uitgevoerd.
- Bestaande renderer met DOM-substitutie: 205 startstanden, 992 geldige aswissels, 116 ontbrekende combinaties afgewezen en 205 dubbele-combinatie-/navigatiefouten PASS. 161 exacte kleurreferentiesets, 811 kandidaatafbeeldingen, 161 prijsorders en 161 identiteits-/afbeeldingfouten PASS.

Publieke controle: **52/52 previewpagina’s** geslaagd, verspreid over alle **29 groepen**, met controle van productidentiteit, prijs, foto’s, winkelwagenformulier en de juiste begrensde keuzedata. Alle **29/29 publieke JSON-assets** zijn volledig gelijk aan de voorbereide inhoud, inclusief SHA256. Twee MAIN-formuliersteekproeven en de bestaande UniMatch-kleurkeuze zijn intact. Dit is een groepssteekproef, geen volledige HTTP-ronde van alle 205 artikelen.

Desktopbrowser: Liora 21.3672 (mat wit, 180 × 80 cm) blokkeert 170 × 75 cm. Klik op Glans wit opent 21.3671 (180 × 80 cm, € 1.359) en maakt 170 × 75 cm beschikbaar. Klik daarop opent 21.3666 (glans wit, 170 × 75 cm, € 1.299); mat wit is daar terecht geblokkeerd. De previewbalk bevestigt het vervolgconcept. Verse Admin-controle: MAIN-rol en drie gecontroleerde codechecksums ongewijzigd; catalogusaantal 2451 EXACT.

NOT_TESTED: volledige 205 HTTP-paginaronde, native mobiel, echte cartregels en checkout, browserwissels in alle nieuwe groepen, volledige regressie van oudere groepen. Een gesimuleerde breedte van 390 px is geen native mobiele controle. Geen lokale Windows clean/statusclaim. Geen prijs-, voorraad-, specificatie-, titel-, productpublicatie- of indexeringsmutaties.

## Herstel en overdracht

BATCH11_ADMIN_CHANGES.json bevat uitsluitend 311 nieuw aangemaakte velden met before: null. Verwijder alleen die velden na een verse exacte vergelijking met after. De 99 ongewijzigde kleurvelden, waaronder alle 55 bestaande ingevulde lijsten, niet verwijderen of wijzigen.

Section/router in het vervolgconcept herstellen uit parent c4115ba741cf7621b3c4e3f1308f689d962a478d. 29 nieuwe ongebruikte JSON-assets mogen blijven. Andere groepen behouden; MAIN en reserve niet schrijven. Actieve codebranch fix/product-cards-2026-10-14, themabron shopify/current. Geen credentials, klantgegevens, inkoopprijzen of settings_data-body in publieke bestanden.

Volgende handeling: gerichte mobiele/cart-QA op het vervolgconcept vóór eigenaarpublicatie; verdere gecontroleerde producttypepartijen binnen eigenaaropdracht toegestaan. Geen actieve schrijver na overdracht.
