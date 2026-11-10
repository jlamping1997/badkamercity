# Wiesbaden batch 10 — 10 november 2026

Status IMPLEMENTED_TEST_ONLY. MAIN196416504074 behouden; vervolgconcept196441932042 UNPUBLISHED (BadkamerCity - Wiesbaden vervolg concept). Reserve196395073802 behouden. Geen publicatie of MAIN-filewrite.

## Resultaat
139kandidaatartikelen onderzocht;100toegevoegd in26groepen.39artikelen apart wegens meerdere SKU’s met dezelfde maat/uitvoering. Cumulatief831/2451uitgebreideartikelen en88groepen;1620overige artikelen nog te beoordelen/open. Niet ieder artikel vraagt een menu. Vendor-telling2451EXACT.

| Partij | Artikelen | Groepen |
|---|---:|---:|
| Inloopdouches, nisdeuren, zijwanden en Pento-cabine |62|15|
| Wastafels en Raw-waskommen |38|11|

77artikelen hebben alleen een maatmenu.23artikelen in4groepen hebben ook kleur (Graffic7, Bajo4, Laro1kraangat6, Larozonderkraangat6).
Cabineformaat bevat twee zijden; wastafels tonen het volledige bronformaat inclusief diepte/hoogte waar vermeld. Een vaste glashoogte/dikte wordt niet als extra keuze aangeboden. Kleur-/formaatcombinaties blijven exacte individuele verkoopartikelen.
Douchedeur/cabine/inloopwand/zijwand blijven gescheiden. Curvea helder/rook/vintagebrons, gewone/geribbelde Square, verschillende Side-compatibiliteitsfamilies, wastafels1/2/geen kraangat, Rawgezoet/hamerslag blijven aparte groepen. Geen nieuwe onbewezen compatibiliteit of setcomponent toegevoegd.

## Bronnen en holds
100actuele SKU’s, variantIDs, OnlineStore-publicatie/enkelvariant en leverancieridentiteit gecontroleerd tegen bestaande officiële wiesbaden.nl-records (19oktober).
98titels exact volledig;20.3755/20.3756hebben bestaande kortere titels80×200cm/90×200cm. SKU-identiteit en maten zijn gelijk aan officiële800/900×2000mm-bron; expliciet toegelaten en niet gewijzigd. Geen algemene vrijstelling voor afwijkende titels.
Verse fabrikantpagina20.3755opgevraagd maar429; geen claim van100nieuw gelezen fabrikantpagina’s. badkamervoorjou.nl niet gebruikt.

Nieuwehold39artikelen: Double4, Pared4, Salone1deur8, Salone2deuren6, Skyline-hoekinstap6, Sita11. Verschillende SKU’s hebben binnen deze kandidaten hetzelfde bronformaat/finish. Mogelijke generaties of onderdelenverschillen eerst uitzoeken; geen willekeurige eneSKU als doel gekozen, niets verwijderd of samengevoegd.
Eerdere Slide-duplicate-, Caral/inbouwdeel-, Alvara-materiaal-, Less-liftscharnier-, Comfort20000mm- en MAIN41.3665lege-kleurlabelholds behouden.

## Admin en code
100create-only custom.switch_group velden plus één ontbrekende custom.color_variants lijst (20.3755, uitsluitend eigen product bij80cm); alle compareDigest:null.101velden exact teruggelezen.99andere kleurreferentielijsten/-waarden en geselecteerde overige productvelden exact behouden. Geen kleur-/spec-tekst gewijzigd.
De Admin-data zijn winkelbreed. MAIN toont op dit80cmartikel geen nieuw meerkleurmenu; de volledige kleur/maatgroep is in vervolgconcept. Bestaande90cm-tweekleurkoppeling behouden.
28conceptbodies exact teruggelezen:26begrensdeJSONassets en section/router. Alleen26groepIDs op bestaande sectionregel en52routerregels toegevoegd. JSrenderer ongewijzigd. DrieMAIN-checksums bij start/einde gelijk.
Geen prijs-, voorraad-, specificatie-, titel-, productpublicatie- of indexeringsmutaties.

## Verificatie
-Lokale strikte Liquid-AST baseline+beidegewijzigdebestanden PASS. Geen externe validatie-/telemetriehelper uitgevoerd.
-100rendererstartstanden,294geldigeaswissels,4ontbrekendecombinaties afgewezen,100dubbelecombinatie-/navigatiefouten PASS.23exacte kleurreferentiesets,45kandidaatafbeeldingen,23prijsorders en23identiteits-/fotofoutproeven PASS.
-Dezelfde proeven ook op werkelijk publiek CDN-geserveerde JS uitgevoerd: dezelfde aantallen PASS (DOMsubstitutie; geen mobiele/cartclaim).
-Publiek31/31previewpagina’s over alle26groepen PASS; extra kleuren in alle4kleurfamilies en120cmGraffic-randgeval. De eersteGraffic-pagina80cm dekt deontbrekendezwartcombinatie. Identiteit/prijs/foto/cartformuliervariant/router/runtimefeiten exact.
-Publiek26/26JSONassets volledige inhoud enSHA256exact.
-MAIN2productformulieren intact (Pento/Curvea); bestaand90cmGraffic2kleurenmenu exact intact. Eerste MAIN-harness verwachtte onterecht een bestaand meerkleurmenu op80cm, waar baselinekleurreferentie ontbrak. Identiteit/prijs/cart waren daar al goed. Originele meetresultaten bewaard; juiste90cmcontrole als afzonderlijke opvolgingPASS. Geen productwijziging om de test passend te maken.
-Echte desktopbrowser20.3759(120cm/chroom): matzwartterecht beschikbaar. Breedte80cmgekozen→20.3755, chroombehouden, matzwartdisabledbevestigd; actuele titel/actievebreedte en geen horizontale documentoverflow bevestigd. Aanvankelijke aanname dat120cmdeontbrekendecombinatie was, gecorrigeerd naar80cm; geen JS-wijziging.
-NOT_TESTED: volledige100HTTP-paginaronde, native mobiel, echte cartregels, andere25groepen browserwissels, volledigeouderegroepenregressie/checkout. Geen Windowslokale clean/statusclaim.

## Herstel
[BATCH10_ADMIN_CHANGES.json](BATCH10_ADMIN_CHANGES.json) bevat uitsluitend101nieuw gecreëerde velden met before:null. Alleen verwijderen na actuele exacte vergelijking met after. Bestaande kleurverwijzingen nooit verwijderen.
Section/router in vervolgconcept herstellen uit parent568794c400c684adf10db5951143634c785b12c5.26nieuweongebruikteassets mogen blijven. Andere groepen behouden; MAIN en reserve niet schrijven.
Actieve codebranch fix/product-cards-2026-10-14; shopify/current. Geen credentials, klantgegevens, inkoopprijzen of settings_data-body in publieke bestanden.

Volgende handeling: gerichte mobiele/cart-QA op vervolgconcept vóór eigenaarpublicatie; verdere gecontroleerde producttypepartijen binnen eigenaaropdracht toegestaan. Geen actieve schrijver na overdracht.

Codecheckpoint: [c4115ba](https://github.com/jlamping1997/badkamercity/commit/c4115ba741cf7621b3c4e3f1308f689d962a478d) op fix/product-cards-2026-10-14; shopify/current is vervolgconceptbron, geen MAIN-publicatie.

