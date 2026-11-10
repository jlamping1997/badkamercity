# Wiesbaden batch 7 — 10 november 2026

Status: IMPLEMENTED_TEST_ONLY. Concept196416504074 blijft UNPUBLISHED; MAIN196441932042. Geen publicatie of MAIN-themefilewrite. Broncodebranch fix/product-cards-2026-10-14, shopify/current/.

## Scope
112 nieuwe artikelen in vijf groepen; cumulatief526artikelen/35groepen (voorheen414/30). Actuele exacte vendor-telling2451;1925overige artikelen nog inhoudelijk te beoordelen, niet allemaal vragen een menu.

| Groep | Artikelen | Keuzes | Vast |
|---|---:|---|---|
| Douchegoot flens + rooster |18|4afwerkingen;lengte50–100cm|7cm breed|
| Douchegoot flens + tegelrooster |24|5afwerkingen;lengte50–120cm|7cm breed|
| Less nisdeur helder |28|7afwerkingen;breedte70/80/90/100cm|200cm hoog;8mm glas|
| Less nisdeur rook |21|7afwerkingen;breedte70/80/90cm|200cm hoog;8mm glas|
| Less nisdeur vintage brons |21|7afwerkingen;breedte70/80/90cm|200cm hoog;8mm glas|

Glassoorten en roostertypen blijven gescheiden. Geen links/rechtsmenu voor omkeerbare standaardLess-deuren; spiegelrook/helder-richtingsproducten niet meegenomen. Geen losse glasplaten, scharnieronderdelen of 3e-generatiegoten aan deze groepen toegevoegd. Gootmatrices zijn niet volledig: alleen exact bestaande combinaties kunnen navigeren; geen ongewenste automatische kleur-/maatwissel.

## Bronnen
Bestaande officiële wiesbaden.nl-records (19oktober), leverancier-SKU-identiteit en actuele volledige Shopifytitels voor112artikelen exact gecontroleerd. Officiële Less20.3200 webbron opnieuw opgevraagd (cache10maanden): model en omkeerbare uitvoering bevestigd. Goot33.4272bron429; geen brede verse fabrikantcontroleclaim.
Less20.3200webbron noemt liftscharnierJa versus oud specificatierecordNee. Specificatieverschil blijft een hold: geen specificaties gewijzigd, geen liftscharnierkeuze/claim toegevoegd. Eerdere Alvara-materiaal- en technische inbouwonderdeelholds blijven behouden. badkamervoorjou.nl niet gebruikt.

## Admin-effect en herstel
112create-only custom.switch_group velden plus70ontbrekende custom.color_variants referentielijsten, alle compareDigest:null.42bestaande referentielijsten exact passend bevonden en behouden. Elke referentielijst bevat uitsluitend dezelfde glassoort/roostertype en maat; een maat met één afwerking krijgt één exacte verwijzing. Alle182velden na schrijven exact teruggelezen; geselecteerde overige velden ongewijzigd.
Deze Admin-data zijn winkelbreed:70nieuwe kleurverwijzingen kunnen direct door het bestaande MAIN-kleurmenu worden gebruikt. De uitgebreide maatkeuzes en nieuwe JSONrouters zitten uitsluitend in het ongepubliceerde concept. Geen claim dat alle wijzigingen alleen in een themadraft bestaan.
Geen prijs-, voorraad-, specificatie-, productpublicatie- of indexeringsmutaties.

Rollback: herstel section/router uit parent93c8d99aac9abaf08353e2825ce7f1fd330e9041. Verwijder alleen de112nieuw gecreëerde groepsvelden en70nieuw gecreëerde kleurverwijzingsvelden nadat actuele waarden overeenkomen met deze groepsassets en compatibele maatgenoten. Verwijder geen42vooraf bestaande verwijzingslijsten. ProductIDs en exacte combinaties staan in de vijf assets. De182nieuw gecreëerde velden (inclusief exact welke70referentielijsten) staan in [BATCH7_ADMIN_CHANGES.json](BATCH7_ADMIN_CHANGES.json); gebruik uitsluitend die lijst voor rollback. Nieuwe ongebruikte assets mogen blijven.

## Bewijs
- Zeven conceptbodies exact teruggelezen: vijf begrensdeJSONassets plus section/router. Sectiondiff: één regel vervangen; router: tien regels toegevoegd. Bestaande JSrenderer ongewijzigd.
- Drie MAIN-codechecksums exact gelijk aan baseline; MAIN-rol behouden.
- Lokale strikte Liquid-AST: baseline en beide gewijzigde bestanden PASS. Geen externe validatie-/telemetriehelpers opnieuw uitgevoerd.
- Werkelijke JSrenderer met DOMsubstitutie:112startstanden,886geldige aswissels,110ontbrekende combinaties afgewezen,660exacte kandidaatafbeeldingen,112prijsorders en112dubbele-combinatie-/identiteitsproeven PASS. Geen echtecartclaim.
- Echte desktopbrowser1363px: Less20.3200 (100cm/geborsteldstaal) →20.3388 (80cm/geborsteldstaal) →20.3389 (80cm/matzwart). Eindtitel en actieve80cm/matzwart bevestigd, geen horizontale documentoverflow.
- Publieke HTMLcontrole112/112 PASS:106rechtstreeks en6enkelkleurige goten na correctie van de oude harness-aanname >1kleurreferentie. SKU’s33.4192/33.4191/33.4271/33.4277/33.4270/33.4276 hadden elk exact één compatibel runtimefeit, één referentie en één maatgenoot; alle overige checks waren al PASS. Geen productwijziging voor deze harnesscorrectie. Ruwe resultaten en gecontroleerde correcties lokaal apart bewaard. Vijf MAIN-kleursteekproeven PASS, inclusief112nieuwe groepvelden die MAIN niet via de conceptmaatrouter gebruikt.
- NOT_TESTED: native mobiel, echte cartregels voor dezebatch, browserwissels voor rook/brons/roosters, volledige oudegroepenregressie/checkout. Geen Windowslokale clean/statusclaim.

Vijf assets: assets/bc-choice-data-21aac6303c3a8022.json, assets/bc-choice-data-689fa1add423a2c1.json, assets/bc-choice-data-9de83fc984e162b7.json, assets/bc-choice-data-1fa4b8d80b8d7724.json, assets/bc-choice-data-b2a215c3b1677cfe.json.
Lokale bewijsbestanden bevatten uitsluitend productdata en testmetingen; geen credentials/klantdata/inkoopprijzen in publieke documentatie.

Volgende handeling: gerichte mobiele/cart-QA op hetzelfde concept vóór eigenaarpublicatie; verdere gecontroleerde producttypepartijen binnen eigenaaropdracht toegestaan. Geen actieve schrijver na overdracht. Geen publicatie.

Codecheckpoint: [c3f0468](https://github.com/jlamping1997/badkamercity/commit/c3f046861e35713034395af40dca32069fdb91c1) op fix/product-cards-2026-10-14; shopify/current is conceptbron, geen MAIN-publicatie.

