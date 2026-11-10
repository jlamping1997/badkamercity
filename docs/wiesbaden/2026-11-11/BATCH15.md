# Wiesbaden batch 15 — 11 november 2026

Status: VERIFIED_CONCEPT_AND_RESOLVED_MENU_REVIEWS. Exact 300 artikelen afgehandeld in de bron-/menucontrole: 63 krijgen een nieuw menu in 17 groepen, 169 bestaande goede kleurmenu’s blijven behouden en 68 exacte modellen/onderdeelrollen hebben geen menu nodig. Aangehouden artikelen tellen niet als afgehandeld.

De nieuwe configuratiemenu’s staan alleen in vervolgconcept196441932042 (UNPUBLISHED). Productmetafields zijn winkelbreed: bestaande Barco-/Julia-kleurmenu’s op MAIN zijn daardoor aangevuld en apart gecontroleerd. MAIN196416504074-bestanden en reserve196395073802 niet geschreven. Geen publicatie.

| Teller na geverifieerde toepassing | Aantal |
|---|---:|
| Nieuw uitgebreid | 63 |
| Cumulatief met uitgebreid menu | 1636/2451 |
| Uitgebreide groepen | 219 |
| Afgehandeld beoordeeld | 2139/2451 |
| Nog af te handelen, inclusief bekende holds | 312 |

De 237 ongewijzigde beoordelingen verhogen de uitbreidingsteller niet. De exacte300-ID-ledger bevat alle63 nieuwe,169 bestaande en68 unieke ID’s plus afzonderlijke hashes: `BATCH15_REVIEW_LEDGER.json`. De bevroren reviewplan-SHA256 is `3d913f44a814e3ff8bb7010f975049a96c4496eb4d70e6c7357cc5a7d34b66c6`.

## Nieuwe menu’s

| Familie | Artikelen | Groepen | Keuzes |
|---|---:|---:|---|
| Slim losse uitlopen | 6 | 1 | Kleur + lengte25/30cm; Ø18mm vast |
| Barco-waskommen | 4 | 1 | Kleur, inclusief ontbrekende Beige |
| Caral complete2-wegsets met3-standenhanddouche | 12 | 1 | Kleur + hoofddouchediameter25/30cm |
| Tower-bevestigingssets | 2 | 1 | Wit/Mat zwart |
| Libero-baden | 2 | 1 | Glans/Mat wit |
| Julia-fonteinen30×28cm | 3 | 1 | Kleur, inclusief ontbrekende Beige |
| Double/Pared/Salone/Skyline/Curf-cabines | 16 | 6 | Formaat, kleur of draairichting waar variabel |
| Sita-inloopdouches met handdoekhouder | 6 | 1 | Breedte80/90/100/110/120/140cm |
| Ribbd-badmengkranen | 4 | 1 | Kleur; hartafstand15cm vast |
| Style-inbouwkranen, vier bewezen varianten | 4 | 1 | Kleur |
| Brush dubbele toiletrolhouders | 2 | 1 | Kleur |
| 304 wastafelkranen met coldstart | 2 | 1 | Uitvoering Standaard/Hoog |

Cabines gebruiken een onderbouwde selectie van actuele canonieke fabrikant-SKU’s; 21 oude/andere commerciële tegenhangers blijven apart. Geen generatiekeuze bedacht om dubbele combinaties passend te maken. Ontbrekende geldige combinaties blijven uitgeschakeld. Bij Caral is de voormalige vreemde kleurpeer29.3095 nu exact geverifieerd; de enige naamafwijking is een dubbel handdouche-woord. Geen inbouwdeeladvies toegevoegd.

De304-keuze betreft twee complete modellen, geen claim dat alleen de hoogte verschilt: lichaamsdiameter, uitloophoogte/reikwijdte, bevestiging en bronvermelding van de aanvoer verschillen. Alle specificaties blijven behouden; geen gelijke aansluiting, passing of uitwisselbaarheid geclaimd. Bij Barco blijven verschillen in bevestigingsmateriaal behouden; geen gelijke doosinhoud beloofd. Tower Mat zwart volgt de officiële titel; het bestaande kleurveld Zwart blijft ongewijzigd. Sita20.3405 behoudt de tegenstrijdige oude onderdeelmetadata; naam en primaire afbeelding/tekening ondersteunen de hele SKU, het nieuwe menu kiest alleen breedte. Style29.1635 blijft buiten de groep wegens een afwijkende tweede tekening.

## Ongewijzigde beoordelingen en holds

169 artikelen in39 volledige kleurcohorten zijn gecontroleerd op verse zichtbare labels, ankers, volledige referentiesluiting, bronafwerking/-functie en exacte leverancieridentiteit. De twee bestaande Julia-artikelen zijn hiervan verwijderd omdat ze tot de nieuwe Julia3 behoren. De eerdere171/40-HTTP-controle is uitsluitend ondersteunende superset; de finale ongewijzigde scope is169/39.

68 modellen/rollen zijn afzonderlijk onafhankelijk beoordeeld aan de hand van de2451-artikelcatalogus, bronidentiteit, huidige lege keuzeroutes en concrete functie-/montage-/onderdeelrol. Geen echte kleur-, maat- of richtingsvarianten als uniek weggeschreven. Dit is een begrensde menubeoordeling, geen algemene claim dat verschillende functies nooit samen navigeerbaar zijn.

Entra/Bajo met ontbrekende exacte leverancieridentiteit, Caral Cadans7 met onopgeloste functie-/materiaalvelden, Ribbd29.5310 als uitbreiding van een bestaande groep en alle overige onopgeloste bron-/compatibiliteits-/generatieholds blijven buiten deze300. Er is niet doorgegroepeerd om een teller te halen.

## Mutaties en verificatie

Toegepast en exact teruggelezen:91 velden —63 nieuwe `custom.switch_group`,23 nieuwe `custom.color_variants` en5 append-only CAS-uitbreidingen (Barco3,Julia2). Alle oude ID’s en ankers behouden.18 bestaande ingevulde kleurvelden en17 overige lege velden blijven exact behouden.46 artikelen hebben een kleurmenu;17 begrensde JSON-assets plus section/router maken19 conceptfiles. Bestaande JS-renderer ongewijzigd.

- Onafhankelijke nieuwe-datareview PASS:1353 controles,63 SKU-/bron-/leverancier-/Adminidentiteiten, alle optiewaarden en referenties,14 gecontroleerde bestaande winkeltitels,17 payload-/SHA256-matches en91 mutatievoorwaarden. Bestaande titels niet gewijzigd.
- Bestaande renderer met DOM-substitutie PASS:63 startstanden,194 geldige aswissels,2 onmogelijke combinaties geblokkeerd,63 dubbele-combinatie-/navigatiefouten afgewezen;172 exacte kandidaatafbeeldingen en46 referentie-/prijssets. Dit is geen echte browser-/cartclaim.
- Strikte lokale Liquidparser PASS op baseline en beide gewijzigde bestanden; geen externe validatie-/telemetriehelper of Shopify Theme Check uitgevoerd.

Admin-readback PASS voor alle300 producten: alle91 bedoelde velden exact,86create-only en5append-onlyCAS. Alle237 ongewijzigde producten en overige gelezen velden van63 nieuwe menuartikelen behouden.19 conceptbodies exact; alleen17 groepsnamen en17 routerparen toegevoegd, overige inhoud gelijk op eindwitruimte na. JS en drie MAIN-codechecksums behouden; MAIN blijft MAIN en vervolgconcept UNPUBLISHED.

Publiek PASS:31/31 nieuwe previewpagina’s over alle17 groepen en17/17 volledige JSON-assets exact. Twee MAIN-formulieren en bestaande Slim-kleuren intact; Barco4/Julia3 op MAIN exact gecontroleerd na de referentieaanvullingen. Ongewijzigde scope:75/75 ondersteunende HTTP-steekproeven PASS,39 previewkleurcohorten plus2 MAIN en34 producttypen uit68 artikelen zonder menu. De eerdere42-steekproefsuperset behoudt één Julia-baselinemeting; die telt niet als ongewijzigde finale controle. Geen volledige300-HTTP-ronde.

Desktopbrowser PASS: Slim29.4036,25cm,geborsteldstaalPVD,€95 →29.4037,30cm,dezelfdeafwerking,€109. Juiste lengtecheckbox, titel, artikelnummer en afbeeldingsbijschrift; winkelwagenknop beschikbaar. Alleen navigatie gecontroleerd; geen echte winkelwagenmutatie in deze ronde.

Broncache19oktober en exacte leverancieridentiteit21oktober; officiële gekoppelde tekeningen/foto’s aanvullend gecontroleerd.41 van de nieuwe winkel-EAN’s matchen;22 canonieke douche-/Curf-SKU’s hebben geen winkel-EAN maar wel een exacte leverancier-SKU/merkmatch met leverancier-EAN. Niet alle fabrikantpagina’s opnieuw opgehaald; onder meer429-responses begrenzen de controle. Veilige bron-/assetcontroles en scopes: `BATCH15_SOURCE_CHECKS.json`.

NOT_TESTED: volledige63 HTTP-paginaronde, native mobiel, echte winkelwagenregels/checkout, browserwissels in alle17 groepen en volledige regressie van oudere groepen. Geen prijs-, voorraad-, specificatie-, titel-, productpublicatie- of indexeringsmutaties uitgevoerd.

## Herstel

`BATCH15_ADMIN_CHANGES.json` bevat de exacte91 before/after-mutaties. Verwijder de86 nieuw aangemaakte velden alleen na verse exacte vergelijking met after. Herstel de5 bestaande Barco-/Julia-kleurvelden naar hun eigen before-waarden met verse compareDigest; verwijder ze nooit. De237 ongewijzigde beoordelingen en overige bestaande kleurvelden niet muteren.

Section/router herstellen uit batch-14-parent `b6946616e3f85e15e28b86a7ac38a69302354b42`;17 ongebruikte nieuwe JSON-assets mogen blijven. MAIN, reserve en overige groepen behouden. Codebranch `fix/product-cards-2026-10-14`, themabron `shopify/current`. Geen credentials, klantgegevens, inkoopprijzen of settings_data-body in publieke bestanden. Mobiele/cart-QA blijft nodig vóór eigenaarpublicatie; na overdracht geen actieve schrijver achterlaten.

De312 resterende beoordelingen betreffen menu’s. Afgehandelde menu’s lossen geen afzonderlijke specificatie-/materiaaldataholds op, waaronder de beschreven Sita-/Alvara-gegevens.
