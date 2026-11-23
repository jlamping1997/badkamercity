# Rustigere onderkant homepage — 10 november 2026

**HOME-BOTTOM-01 CONCEPT_PREVIEW_VERIFIED / OWNER_DESIGN_REVIEW_PENDING.** Op verzoek van de eigenaar is een nieuw ontwerp voorbereid voor de onderste homepageblokken. De opgestapelde inspiratie-/3D-banners en de twee brede serviceaccordions zijn vervangen door twee naast elkaar geplaatste kaarten: tegelinspiratie en een compact hulpblok. Op smalle schermen stapelen ze. Het bestaande beeld en de inspiratiebestemming blijven de bron; er zijn geen nieuwe beelden of productclaims verzonnen.

‘Even overleggen?’ leidt naar contact. Bezorgen en retouren zijn kleine, directe links naar de bestaande informatiepagina’s, met native policy-/contactterugval. Het grote 3D-beeld en de showroomkop verschijnen niet meer; aanvragen blijft beschikbaar via de bescheiden uitklaplink ‘3D-advies op afspraak’. Een ingestelde externe boekingslink behoudt voorrang. Alle bestaande anchor-ID’s en het native Shopify-contactformulier zijn behouden; de form-body is bytegelijk. Vier optionele hulpinstellingen en zes vertaalde standaardteksten zijn toegevoegd. Oude merchantinstellingen zijn behouden; de editor licht de compacte opmaak toe.

## Bron en afbakening

- MAIN **196416504074 — BadkamerCity - Merkenbalk zonder pijlen**, door de eigenaar gepubliceerd sinds het vorige checkpoint.
- Bestaand UNPUBLISHED **196395073802 — BadkamerCity - Rustige homepage 10 nov** hergebruikt; geen extra kopie. De drie achterlopende merkenfiles zijn eerst uit MAIN gelijkgemaakt en exact teruggelezen. Samen met de volledige voorafgaande manifests zijn alle1.401 baselinefiles gelijk bewezen.
- Codebaseline `a6169d799bfac1185f0fa0851016ce6bb31fa2b5`, branch `fix/product-cards-2026-10-14`, bron `shopify/current/`.
- Vier featurefiles: `sections/bc-homepage.liquid`, `assets/bc-homepage.css`, `locales/nl.json`, `locales/en.default.json`. Kop/acties/categorieën/merkenmarkup zijn bytegelijk behouden. De bestaande homepage-JavaScript en index-template zijn niet aangepast. Nieuwe localeverschillen beperken zich tot bc_home.support; bestaande SEO-/prijsvertalingen blijven gelijk.

Eindcontrole: **1.401 files per thema, 1.397 gelijk en exact vier featureverschillen**. Vier bodies en checksums exact teruggelezen; alle1.401 MAIN-checksums ongewijzigd. Beschermde settings_data-body niet gelezen of geschreven; checksum aan beide kanten d6a5642b02e3b8773a5e4e37aed01256. [Volledige vergelijking](theme-parity.json).

## Controles en grenzen

- **15 nieuwe render-/contractcontroles PASS**: bestaande bovenkant/form-body/settings behouden, alleen nieuwe vertaalnamespace, twee kaarten en geldige anchors, hash-openen van het verplaatste formulier, boekingsvoorrang, ontbrekende pagina’s/policies, merchantoverride/escaping, Engelse nieuwe kopie, fout-/succesmelding die de disclosure opent. Native Shopify-formwrapper is offline gesimuleerd; dit is geen verzendtest. [Resultaat](checks.json).
- **20 bestaande merken-/slider- en13 logocontroles PASS.** De bestaande localevergelijking sluit uitsluitend de expliciet toegevoegde supportnamespace uit; de rest blijft streng vergeleken.
- **Shopify-validator: vier featurefiles SUCCESS**, revisie1. Whitespacecontrole PASS. [Uitvoer](theme-check.txt).
- **Echte Chrome-preview1348×936:** twee even hoge kaarten van390px, geladen inspiratiebeeld, juiste drie linkdoelen en geen documentoverloop. Kleine 3D-optie opent met muisklik en sluit met Enter; native formulier heeft post-/contactaction en drie bestaande verplichte velden. Formulier niet verstuurd. [Meetgegevens](browser-check.json) · [Ontwerpbeeld](desktop-preview.jpg).
- Fysiek mobiel/tablet, daadwerkelijke formulier-/mailaflevering, Lighthouse en lokale Windows/Codex-wrappers zijn NOT_TESTED. Geen bijbehorende vrijgave geclaimd.

## Volgende handeling en herstel

Eigenaar bekijkt **BadkamerCity - Rustige homepage 10 nov** en geeft ontwerpfeedback. Publicatie blijft bij de eigenaar; de koppeling heeft niet gepubliceerd. De grote 3D-promotie is bewust teruggebracht, de aanvraagfunctie blijft bruikbaar.

`rollback/` bevat de vier exacte MAIN-bronfiles vóór de wijziging. Alleen gericht in UNPUBLISHED herstellen na controle op latere edits. Voor volledige terugkeer na eigenaarpublicatie blijft thema196416504074 beschikbaar. Eerdere rollen en publicatiewachtnotities zijn historie.
