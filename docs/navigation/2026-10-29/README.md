# NAV-01 — mobiel menu met inline uitklappers

29 oktober 2026. Eigenaar wil Mijn account verwijderen en onderliggende categorieën in hetzelfde scherm openen, met strakke rijen in plaats van afgeronde vakken. De eerste categorieën en de goedgekeurde homepage blijven behouden.

## Bronnen en doel

Verse Shopify-read: homepageconcept **195910795530 — BadkamerCity - Homepage rondjes en acties** is inmiddels **MAIN**. Dit is een door de eigenaar uitgevoerde publicatie; deze sessie heeft niet gepubliceerd. Vorige MAIN195876815114 is UNPUBLISHED. Actieve codebranch blijft `fix/product-cards-2026-10-14`, startcheckpoint `e37ce710aa108a126cdb8ce23ab8f7b76d3c62b0`; main alleen documentatie.

Concept **195913482506 — BadkamerCity - Menu openklappen en strakke rijen** is klaar voor review. Status: **PREVIEW_READY / SHOPIFY_COMPONENT_BROWSER_QA_PASSED / NATIVE_PHONE_NOT_TESTED / NOT_PUBLISHED**. Vóór schrijven waren alle 1.337 bestanden checksumgelijk aan MAIN; na afloop wijken alleen de twee bedoelde menubestanden af. MAIN is opnieuw volledig vergeleken: 1.337/1.337 ongewijzigd. De testtemplate is exact hersteld.

Codecheckpoint **9048bff16f540ef9ec7f0f3ff14e776ab4a31f2f** op de bestaande branch. Centrale documentatiecheckpoint **d2683980d30e9103aa178bca47127a3d3cfe61ef** op main. Dit afrondingsdossier volgt in een documentatiecommit; de code is sinds het checkpoint niet gewijzigd.

De actieve `header-group.json` selecteert `main-menu`. De verse Admin-boom heeft drie niveaus. Kranen → Wastafelkranen bevat echte collectielinks naar opbouw en inbouw. Een menubestemming/collectietemplate wijzigen is niet nodig.

## Gedrag en bestanden

- `sections/header.liquid`: accountlink weg; vervolgscherm zonder afgeronde container of gekleurde kaart; dunne scheidingslijnen. BcMobileDrawer behoudt root → categorie en terug. Inactieve panelen zijn inert/aria-hidden; vooruit/terug verplaatst focus. Sluiten/heropenen reset de uitklappers.
- `snippets/header-drawer.liquid`: account-CTA weg; tweede niveau met kinderen is native details/summary, met plus/minteken. Openen van Wastafelkranen blijft in Kranen en verandert de URL niet. Binnenin staan Bekijk alle wastafelkranen en alle bestaande derde-niveaulinks. Een keuze zonder kinderen is een normale link. Afzonderlijke derde panelen vervallen.
- `snippets/bc-mobile-category-icon.liquid`: bestaande ongewijzigde MAIN-afhankelijkheid opgenomen in Git; niet uploaden. De Git-root bevatte dit recentere live snippet nog niet.

Admin blijft de enige bron voor titels, volgorde en URL's. Geen accountfunctionaliteit of klantinstellingen gedeactiveerd; alleen de gevraagde links in de header/drawer verwijderd. Homepagecirkels blijven zoals goedgekeurd. Desktopnavigatie en collectiepagina's behouden hun eigen renderer.

## Uitgevoerde controles

JavaScript `node --check` geslaagd. Eerste ThemeCheck vond een ontbrekende, bestaande live-afhankelijkheid in de onvolledige lokale runtimekopie (`bc-mobile-category-icon`). Die is uit MAIN gelezen en toegevoegd. ThemeCheck R3 slaagt voor beide gewijzigde bestanden; zie validation-r3.log. Een afzonderlijke LiquidJS-rendercontrole met de verse Admin-menuboom behoudt alle 156 URL's en rendert 24 inline groepen zonder derde panelen. Dat is een lokale componentcontrole, geen Shopify-runtimebewijs.

Daarna is de gewijzigde **header door Shopify zelf gerenderd** via een tijdelijke noindex view op het concept. Twee srcdoc-frames geven echte CSS-mediabreedtes 320/390; de fixture gebruikt de gewijzigde headersectie en het exacte BcMobileDrawer-script. De statische headersectie gebruikt de schema-instellingen/main-menu; het is geen volledige mobiele homepage met sticky scroll. Browserresultaten:

- Kranen → Wastafelkranen blijft in hetzelfde Kranen-paneel; de framepagina blijft about:srcdoc en er is geen derde paneel. De drie links tonen de juiste /collections/wastafelkranen, /opbouw-wastafelkranen en /inbouw-wastafelkranen.
- Klik, Enter openen en Space sluiten; plus/min verandert mee. Geen horizontale overloop op 320/390. Computed radius vervolgcontainer/summary 0px.
- Terug zet root actief en focus op Kranen. Verborgen panelen hebben inert en aria-hidden=true. Escape sluit; heropenen start op root en reset de open groepen.
- Douche → Douchesets opent inline met alle drie echte onderliggende links, ook het lange label Inloopdouches en douchewanden past op 320px.
- In de echte desktop-homepage zijn 24 nieuwe uitklappers en nul derde panelen/accountlinks aanwezig; zoeken en cart blijven in de header. De doelcollectie Opbouw wastafelkranen is daarnaast in een echte hoofdbrowsertab geopend en toont de juiste h1. Dit is geen doorkliktest binnen het srcdoc-frame.

De tijdelijke fixture is exact teruggezet naar de oorspronkelijke inerte QA-view; er blijft geen testcontroller achter. Native telefoon/touch, volledige sticky-header-scroll, overlap met cart/search, resize 990px en een volledige focustrap-audit zijn **NOT_TESTED**. Zoeken/cart zijn deze ronde op aanwezigheid gecontroleerd; hun volledige eerdere testflow is niet herhaald. Geen checkout, bestelling, mail of Admin-menu mutatie.

## Terugzetten

De twee oorspronkelijke MAIN-bronnen staan met LF-genormaliseerde regeleinden onder `baseline/`; de originele Shopify-checksums staan in de verificatiemeting. Die archiefbestanden zijn bron voor inhoudelijk terugzetten, geen claim van bytepariteit van de archiefkopie. Alleen header.liquid en header-drawer.liquid horen in het deploymentmanifest. Gebruik een verse gecontroleerde conceptkopie; nooit de hele Git-root naar Shopify uploaden. Publicatie door eigenaar na review. De oorspronkelijke homepage-MAIN blijft beschikbaar als terugzetversie.

## Volgende handeling

Eigenaar beoordeelt concept **BadkamerCity - Menu openklappen en strakke rijen** op zijn telefoon: Menu → Kranen → Wastafelkranen open/dicht, Opbouw kiezen en terug. Daarna beslist de eigenaar over publicatie. De nieuwe menuversie is nog niet live. Zie `mobile-menu-preview.jpg`, `theme-verification.json`, `menu-render-check.json` en `deployment-manifest.json`.
