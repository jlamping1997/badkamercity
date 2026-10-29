# NAV-01 — mobiel menu met inline uitklappers

29 oktober 2026. Eigenaar wil Mijn account verwijderen en onderliggende categorieën in hetzelfde scherm openen, met strakke rijen in plaats van afgeronde vakken. De eerste categorieën en de goedgekeurde homepage blijven behouden.

## Bronnen en doel

Verse Shopify-read: homepageconcept **195910795530 — BadkamerCity - Homepage rondjes en acties** is inmiddels **MAIN**. Dit is een door de eigenaar uitgevoerde publicatie; deze sessie heeft niet gepubliceerd. Vorige MAIN195876815114 is UNPUBLISHED. Actieve codebranch blijft `fix/product-cards-2026-10-14`, startcheckpoint `e37ce710aa108a126cdb8ce23ab8f7b76d3c62b0`; main alleen documentatie.

Nieuw concept **195913482506 — BadkamerCity - Menu openklappen en strakke rijen** wordt door Shopify gekopieerd van huidige MAIN. Status bij dit checkpoint: **COPY_PROCESSING / CODE_IMPLEMENTED / BROWSER_QA_PENDING / NOT_PUBLISHED**. Geen bestanden schrijven voordat de volledige kopie checksumgelijk is. De reviewlink is pas gereed na upload en browsercontrole.

De actieve `header-group.json` selecteert `main-menu`. De verse Admin-boom heeft drie niveaus. Kranen → Wastafelkranen bevat echte collectielinks naar opbouw en inbouw. Een menubestemming/collectietemplate wijzigen is niet nodig.

## Gedrag en bestanden

- `sections/header.liquid`: accountlink weg; vervolgscherm zonder afgeronde container of gekleurde kaart; dunne scheidingslijnen. BcMobileDrawer behoudt root → categorie en terug. Inactieve panelen zijn inert/aria-hidden; vooruit/terug verplaatst focus. Sluiten/heropenen reset de uitklappers.
- `snippets/header-drawer.liquid`: account-CTA weg; tweede niveau met kinderen is native details/summary, met plus/minteken. Openen van Wastafelkranen blijft in Kranen en verandert de URL niet. Binnenin staan Bekijk alle wastafelkranen en alle bestaande derde-niveaulinks. Een keuze zonder kinderen is een normale link. Afzonderlijke derde panelen vervallen.
- `snippets/bc-mobile-category-icon.liquid`: bestaande ongewijzigde MAIN-afhankelijkheid opgenomen in Git; niet uploaden. De Git-root bevatte dit recentere live snippet nog niet.

Admin blijft de enige bron voor titels, volgorde en URL's. Geen accountfunctionaliteit of klantinstellingen gedeactiveerd; alleen de gevraagde links in de header/drawer verwijderd. Homepagecirkels blijven zoals goedgekeurd. Desktopnavigatie en collectiepagina's behouden hun eigen renderer.

## Controle bij checkpoint

JavaScript `node --check` geslaagd. Eerste ThemeCheck vond een ontbrekende, bestaande live-afhankelijkheid in de onvolledige lokale runtimekopie (`bc-mobile-category-icon`). Die is uit MAIN gelezen en toegevoegd. ThemeCheck R3 slaagt voor beide gewijzigde bestanden; zie validation-r3.log. Browser-, touch- en echte telefoontests zijn nog niet uitgevoerd. Geen checkout, bestelling, mail of Admin-menu mutatie.

## Terugzetten

De twee originele MAIN-bronnen staan onder `baseline/`. Alleen header.liquid en header-drawer.liquid horen in het deploymentmanifest. Gebruik een verse gecontroleerde conceptkopie; nooit de hele Git-root naar Shopify uploaden. Publicatie door eigenaar na review. De oorspronkelijke homepage-MAIN blijft beschikbaar als terugzetversie.
