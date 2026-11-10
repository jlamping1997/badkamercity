# Wiesbaden batch 13 — 10 november 2026

Status: CONCEPT_1539 / BATCH13_VERIFIED. Exact 300 nieuwe menu-artikelen in 34 volledige cohorten, uitsluitend voor vervolgconcept 196441932042 (UNPUBLISHED). MAIN 196416504074 en reserve 196395073802 behouden; geen publicatie.

Cumulatief 1539/2451 uitgebreide artikelen, 193 groepen en 912 overige artikelen nog te beoordelen. Deze teller betekent niet dat ieder resterend artikel een menu nodig heeft. De partij bestaat uit 128 artikelen die oorspronkelijk geen menu hadden en 172 artikelen met een nieuwe relevante configuratiekeuze naast hun bestaande kleurkeuze. Bestaande goede kleurmenu’s zijn niet zonder extra keuze opnieuw geteld.

| Familie | Artikelen | Groepen | Nieuwe keuzes |
|---|---:|---:|---|
| Style / Caral Victoria kranen | 25 | 2 | Standaard of XL (hoog) |
| UniMatch complete handdouchesets | 50 | 3 | Staaf 1 stand of rond Ø12 cm 3 standen |
| Alonzo accessoires | 48 | 4 | Groot/klein, type rek, wand/vrijstaand of met/zonder klep |
| Spotz inbouwspots | 14 | 1 | Enkel/dubbel |
| Vesta rimless hangtoiletten | 35 | 3 | Toiletzitting; normaal, bidet koud en bidet warm/koud apart |
| Less losse glazen en glaskoppelingen | 40 | 7 | Breedte, Links/Rechts of kleur waar variabel |
| Slim profielen en stabilisatie | 28 | 4 | Kleur/afwerking; producttypen apart |
| Magnum WiFi-vloerverwarming | 18 | 1 | Oppervlakte/vermogen en thermostaatkleur |
| Stonea inkortbare voorzetpanelen | 9 | 1 | Volledig maatbereik en kleur |
| UniMatch buisverbinders | 7 | 2 | Kleur; recht en T-stuk apart |
| UniMatch Cadans-glijstangsets | 6 | 1 | Kleur |
| Caral Beam-complete sets en verlengsets | 12 | 2 | Kleur; beide producttypen apart |
| Laro / Novira meubels | 5 | 2 | Kleur; beide producttypen apart |
| Ultimo 3.0 toiletzittingen | 3 | 1 | Kleur |

## Bronnen en begrijpelijke keuzes

Alle 300 SKU-/merkidentiteiten sluiten exact aan op officiële wiesbaden.nl-bronrecords en leverancieridentiteit. Verse Admin bevestigt actieve, gepubliceerde producten met één variant en nog geen switch_group. Fabrikantrecords: 19 oktober; leverancieridentiteit: 21 oktober. 271 winkel-EAN’s matchen; bij 29 ontbreekt de winkel-EAN maar bestaat een exacte leveranciers-SKU/merkmatch met leverancier-EAN. Geen claim dat alle fabrikantpagina’s opnieuw zijn opgehaald. De 23 bestaande afwijkende winkeltitels blijven behouden; concrete configuraties en SKU’s zijn gecontroleerd, geen titelmutaties.

- Los Less-glas blijft los glas: vast 2000 mm hoog en 8 mm dik, alleen Breedte zichtbaar waar die varieert. Geen samengesteld deur-/hardwareadvies.
- Stonea toont de volledige bronbereiken in oplopende volgorde: 80–90 × 70–100 / 110–140 / 150–180 cm. De losse, door de oorspronkelijke parser gevonden eindmaat is niet als volledig formaat gebruikt.
- Magnum koppelt elk bronoppervlak aan het bijbehorende vermogen; de kleur betreft expliciet de WiFi-thermostaat. Geen dimensioneringsadvies.
- De drie UniMatch-basisassemblages blijven apart. Negen representatieve officiële tekening-/fotoparen bevestigen de vaste bases. Letterlijke tweekleurige afwerkingen blijven zichtbaar; ontbrekende combinaties blijven uitgeschakeld. Geen claim over gelijke handdouchematerialen of uitwisselbare componenten.
- Vesta gebruikt drie afzonderlijke lichaams-/functiegroepen; de concrete meegeleverde zitting is zichtbaar. Alonzo wand/vrijstaand is door de betreffende bronmontagevelden bevestigd. Standaard/XL-kranen zijn met bron-/tekeningbewijs beoordeeld. Geen nieuw passendheids- of installatieadvies toegevoegd.

## Aangehouden en doorgeschoven

39 artikelen uit de intake blijven aangehouden: Caral-afbouwdelen 12 (model-/functieverschillen), Style-inbouwkranen 5 (1-/2-gats), Caral-opbouwsets 6 (cooltouch/KIWA), Ribbd-badmengkranen 4 (binnen-/buitendraad), Style-watervalbadkranen 5 (afwijkende functievelden), Brush dubbele houders 2 (klep), Less vintage nisdeurglas 3 (deurtype) en Comfort-zijwanden 2 (bestaande hold). Inconsistente fabrikantmetadata is niet zonder bewijs gecorrigeerd.

20 overige artikelen zijn uitsluitend doorgeschoven om exact 300 via hele cohorten te verwerken: Caral-glijstukken 2, thermostaatkranen 2, rozetten 2, Amador-schuimstraalbrekers 2, tegelroosterafstandhouders 3, sifonrozetten 2, schroevensets 3 en Less vintage glasplaten 4. Dit zijn geen nieuwe technische holds. Amador-/Ribbd-hoogtecohorten en alle eerdere holds zijn vooraf buiten de selectie gebleven.

## Mutaties en verificatie

Toegepast en exact teruggelezen: 396 create-only velden, bestaande uit 300 nieuwe `custom.switch_group` en 96 nieuwe `custom.color_variants`; alle compareDigest: null. Alle 172 bestaande gevulde kleurreferentielijsten blijven exact behouden, evenals 32 andere lege kleurvelden. 268 artikelen hebben een kleurmenu in 28 groepen. 36 conceptfiles: 34 begrensde JSON-assets plus section/router; bestaande JS-renderer ongewijzigd.

- Onafhankelijke review PASS: 300 bron-/leverancier-/Adminidentiteiten, 513 rechtstreeks uit bronafwerking, -maten, -richting of -functie herberekende optiewaarden; 34 unieke combinatiesets, 268 exacte referentiesluitingen, 172 ongewijzigde oude lijsten, 34 payload-/SHA256-matches en alle 396 create-only mutatievoorwaarden.
- Bestaande renderer met DOM-substitutie PASS: 300 startstanden, 1822 geldige aswissels en 118 ontbrekende combinaties afgewezen; 300 dubbele-combinatie-/navigatiefouten afgewezen. 1584 exacte kandidaatafbeeldingen, 268 prijsvolgordes en referentiesets; veilige terugval bij identiteits- en afbeeldingsfouten.
- Strikte lokale Liquidparser PASS op baseline en beide gewijzigde bestanden. Geen Shopify Theme Check of externe validatie-/telemetriehelper uitgevoerd.

Admin-readback PASS: alle 396 geschreven waarden exact. Alle 300 geselecteerde productidentiteiten en overige opgehaalde velden ongewijzigd; 172 bestaande gevulde kleurreferenties en 32 lege kleurvelden inclusief metadata behouden. Alle 36 conceptbodies exact teruggelezen; de bedoelde groep-/routertoevoegingen terugnemen levert de vorige code terug, afgezien van eindwitruimte. JS-checksum behouden. Verse eindcontrole: catalogus 2451 EXACT; MAIN-rol en drie codechecksums ongewijzigd; vervolgconcept blijft UNPUBLISHED.

Publieke servermarkup PASS: 58/58 previewpagina’s over alle 34 groepen, met exacte SKU, titel, prijs, foto, formulier-variant, runtimekleurfeiten en juiste begrensde keuzedata. Alle 34/34 openbare JSON-assets zijn volledig gelijk aan de voorbereide inhoud en SHA256. Twee MAIN-formulieren en de bestaande Style-/Vesta-kleurmenu’s zijn intact. Dit is een groepssteekproef, geen volledige HTTP-ronde van 300 artikelen.

Desktopbrowser PASS: Vesta 32.3418 (mat wit, zonder toiletzitting, €319) blokkeert Vesta-zitting. Klik Glans wit opent 32.3450 (zonder toiletzitting, €279); klik Vesta opent 32.3454 (glans wit, Vesta-zitting, €379). Mat wit is bij die zitting terecht uitgeschakeld. De andere keuze en de juiste productidentiteit blijven behouden; de previewbalk bevestigt het vervolgconcept.

NOT_TESTED: volledige 300 HTTP-paginaronde, native mobiel, echte winkelwagenregels en checkout, browserwissels in alle 34 nieuwe groepen en volledige regressie van oudere groepen. Gesimuleerde DOM-/schermbreedtecontrole bewijst geen native mobiele werking. Geen lokale Windows clean/statusclaim. Geen prijs-, voorraad-, specificatie-, titel-, productpublicatie- of indexeringsmutaties uitgevoerd.

## Herstel

[BATCH13_ADMIN_CHANGES.json](BATCH13_ADMIN_CHANGES.json) bevat uitsluitend de exacte 396 nieuwe velden met before: null. Verwijder alleen deze velden na een verse exacte vergelijking met after; bestaande kleurvelden nooit verwijderen of wijzigen. Section/router in het vervolgconcept herstellen uit batch-12-parent `b6c4680115b5a647bc874ad5c381e73eab559243`. De 34 ongebruikte nieuwe JSON-assets mogen blijven; MAIN, reserve en overige groepen behouden.

Codebranch `fix/product-cards-2026-10-14`, themabron `shopify/current`. Geen credentials, klantgegevens, inkoopprijzen of settings_data-body in publieke bestanden. Mobiele/cart-QA blijft nodig vóór eigenaarpublicatie; na overdracht geen actieve schrijver achterlaten.

Primaire bron-/tekeningcontroles en beslissingen: [BATCH13_SOURCE_CHECKS.json](BATCH13_SOURCE_CHECKS.json).
