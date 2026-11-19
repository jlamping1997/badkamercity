# Wiesbaden batch 8 — 10 november 2026

Status: IMPLEMENTED_TEST_ONLY. Actieve MAIN is nu196416504074 (voorheen concept). Geen publicatie door deze sessie. Vervolgconcept196441932042 UNPUBLISHED, hernoemd naar BadkamerCity - Wiesbaden vervolg concept. Reserve196395073802 behouden.

## Nieuwe conceptbasis
Volledige checksuminventaris beide thema’s: MAIN1436bestanden, oud concept1401.1397bestaande bestanden exact gelijk;35ontbrekende JSONassets en4verschillende codebestanden vanuit huidige MAIN naar vervolgconcept overgenomen,39bodies exact teruggelezen. Geen extra doelbestanden. Settings_data.json checksumgelijk, niet geschreven; geen beschermde body geraadpleegd. Zo behoudt vervolgconcept alle voorgaande526artikelen/35groepen en actuele SEO-code. MAIN-codebodies komen overeen met Gitcheckpointc120d204e6e87ac82bbbef2174b6f468189906ee.

## Nieuwe partij
103nieuwe artikelen /4groepen; cumulatief629/2451artikelen en39groepen.1822overige artikelen nog te beoordelen; niet allemaal vragen een menu.2451actuele vendortelling EXACT.

| Groep | Artikelen | Menu’s |
|---|---:|---|
| Elara sierradiator |15|Kleur; exact hoogte × breedte (5formaten)|
| Elara elektrisch Smart WiFi |35|Kleur (6); exact hoogte × breedte (6formaten, één ontbrekende combinatie)|
| Less nisdeur spiegelrook naar helder |42|Kleur (7); breedte70/80/90; uitvoeringLinks/Rechts|
| Square inloopdouche helder |11|Kleur (3); breedte80/90/100/110/120 (alleen bestaande combinaties)|

CV- en elektrische radiatoren blijven afzonderlijk. Maten76,6/118,5/181,7cm behouden decimalen. Geen los hoogtemenu/breedtemenu met niet-bestaande combinaties. Geen verzonnen wattages of vermogensmenu. Less200cmhoog/8mmglas; Square200cmhoog/8mmglas. Links/Rechts is neutraal Uitvoering, geen onbewezen draairichtingsclaim.

## Bewijs en bronnen
Alle103actuele SKU’s/leverancieridentiteit, officiële wiesbaden.nl-bronrecords en volledige titels inhoudelijk exact gematcht. Twee cosmetische titelafwijkingen toegelaten na exacte normalisatie:41.3558 gebruikt×,41.3686 gebruikt×en suffix –41.3686. Titels niet gewijzigd.
Elara41.3566officiële bron opnieuw opgehaald (cache3weken), model/formaat/elektrische uitvoering bevestigd. Spiegelrook20.3219webbron via zoektool niet toegankelijk; bestaande officiële records gebruikt, geen brede verse fabrikantclaim. badkamervoorjou.nl niet gebruikt.
Slide-kandidaat niet meegenomen: meerdere verschillende artikelnummers met identieke maat/kleur, die zonder nader onderzoek dubbele navigatiedoelen geven. Comfort-maten niet blind samengevoegd:8mm/10mmglasverschil. Eerdere technische bronholds blijven staan.

## Admin en teststatus
103nieuwe custom.switch_group velden (create-only) en39kleurverwijzingslijsten:19nieuwe create-only lijsten,20bestaande lijsten uitsluitend uitgebreid met exact passende kleurgenoten onder compareDigest-CAS.64bestaande lijsten behouden. Geen referentie verwijderd; kleurgenoten blijven exact dezelfde maat en uitvoering. Alle142velden exact teruggelezen; geselecteerde overige velden ongewijzigd.
Admin-data zijn winkelbreed: extra kleurverwijzingen worden ook door bestaand MAIN-kleurmenu gebruikt. Uitgebreide maat-/uitvoeringsmenu’s en viernieuweJSONassets uitsluitend vervolgconcept.
Zes nieuwe/gewijzigde conceptbodies exact teruggelezen. Bestaande JSrenderer hergebruikt; sectionwijziging alleen viergroepIDs toegevoegd, router achtregels toegevoegd. Drie MAIN-checksums behouden; geen MAIN-write, prijs-, voorraad-, specificatie-, productpublicatie- of indexeringsmutaties.
Lokale strikte Liquidparser baseline+beidegewijzigdebestanden PASS. Geen externe validatie-/telemetriehelpers opnieuw uitgevoerd.
Bestaande JSrenderer met DOMsubstitutie:103startstanden,858geldigeaswissels,26ontbrekendecombinaties afgewezen,573exactekandidaatafbeeldingen,103prijsorders,103dubbelecombinatie- en identiteitsproeven PASS.
Echte desktopbrowser:41.3566 (118,5×60cm glanswit) →41.3559 (76,6×45cm glanswit); actuele titel, actievekleur en exacte maat bevestigd; geen horizontale documentoverflow.
Publieke103-paginacontrole103/103PASS: exact conceptthema, titel, SKU, prijs, eerste foto, cartformuliervariant, begrensdeasset en alle runtimekandidaatfeiten. Lokale nieuwe harness laat exact éénkleurgenoot toe indien dat het volledige bestaande maatsetje is; geen achteraf wijziging van productdata voor testuitslagen.
MAIN:3/4kleursteekproeven exact naar nieuwe verwijzingenPASS. Elektrisch41.3566renderde5van6referenties; deextra41.3665heeft custom.kleur leeg (verse Adminread bevestigd) en bestaand MAIN-snippet slaat lege labels over. Gerichte nieuwe MAINcontrole tegen de5oorspronkelijke kleurartikelenPASS: bestaande titels/prijs/cart/kleuren intact. Dit is een zichtbare beperking van het bestaande MAIN-kleurmenu, geen claim dat daar6kleuren staan. Het nieuwe concept gebruikt expliciete JSONkleurlabels en toont de6kleuren correct; volledige103previewcontrole bevestigt runtimefeiten, desktop6kleurknoppen gezien. Geen custom.kleur-specificatievelden gewijzigd.
NOT_TESTED: native mobiel, echte cart voor deze103, browserwissels van deandere3families en kleur/uitvoering binnen dezebatch, volledigeouderegroepenregressie/checkout. Geen Windowslokale clean/statusclaim.

## Herstel
[BATCH8_ADMIN_CHANGES.json](BATCH8_ADMIN_CHANGES.json) bevat voor142velden exact voor/na. Verwijder uitsluitend de122nieuwgecreëerde velden nadat huidige waarde nog exact gelijk is aan after. Herstel de20uitgebreide lijsten naar before met een vers gelezen compareDigest, zonder andere sessiewijzigingen te overschrijven.64ongewijzigde lijsten nooit verwijderen.
Section/router uit parentc120d204e6e87ac82bbbef2174b6f468189906ee terugzetten in vervolgconcept; viernieuweassets mogen ongebruikt blijven. De synchronisatie naar de huidige MAIN-basis hoeft niet teruggedraaid te worden. MAIN en reserve niet schrijven.
Nieuweassets: assets/bc-choice-data-3c21f5131341220f.json, assets/bc-choice-data-dad38812c183acba.json, assets/bc-choice-data-019324864dc27fc2.json, assets/bc-choice-data-01fe2176e73e6c8a.json.
Geen klantdata, credentials, inkoopprijzen of settingsbody in publieke bestanden.

Volgende handeling: gerichte mobiele/cart-QA op vervolgconcept196441932042 vóór eigenaarpublicatie; verdere gecontroleerde producttypepartijen binnen bestaande eigenaaropdracht toegestaan. Geen actieve schrijver na overdracht. Geen publicatie.

Codecheckpoint: [714e354](https://github.com/jlamping1997/badkamercity/commit/714e35438fb9610c8c146e7a4ea3c669181b436a) op fix/product-cards-2026-10-14; shopify/current is vervolgconceptbron, niet gelijk aan MAIN na batch8.

