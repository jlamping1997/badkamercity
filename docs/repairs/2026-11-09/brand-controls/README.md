# Merkenbalk zonder pijlen — 9 november 2026

**BRAND-CONTROLS-01 PREVIEW_VERIFIED / OWNER_PUBLICATION_PENDING.** Op eigenaarverzoek zijn de twee pijlknoppen en het pijltje achter ‘Alle merken’ verwijderd. De overzichtslink is nu een compacte donkerblauwe knop met witte tekst, afgeronde hoeken, hoverkleur en zichtbare toetsenbordfocus. De klikruimte blijft minimaal44px hoog.

De homepage rendert geen bedieningsknoppen meer. De slider initialiseert nu op basis van de track; eventuele knoppen zijn optioneel gemaakt. Daarmee blijven de bestaande oneindige beweging op22px/s en de sleep-/swipebediening werken zonder knoppen. De vroegere handmatige slider blijft bruikbaar waar die wél met knoppen wordt gerenderd.

## Bron en concept

- MAIN **196395073802 — BadkamerCity - Oneindige merkenbalk 9 nov** is sinds het vorige checkpoint door de eigenaar gepubliceerd.
- Bestaand UNPUBLISHED **196416504074 — BadkamerCity - Merkenbalk zonder pijlen** is hergebruikt. De drie achterlopende featurefiles zijn eerst uit de actuele MAIN gelijkgemaakt en op checksum teruggelezen. Met de volledige voorafgaande manifests zijn alle1.401 baselinefiles gelijk bewezen. Geen extra kopie.
- Codebaseline `9dd9f8f8423407dabd707dca56be4cc3eedfab77`; branch `fix/product-cards-2026-10-14`; bron `shopify/current/`.
- Exact drie productiefiles: `sections/bc-homepage.liquid`, `assets/bc-brands.css`, `assets/bc-brand-slider.js`.

Eindstand: **1.401 files per thema, 1.398 gelijk en exact drie featureverschillen**. Alle drie bodies en MD5’s exact teruggelezen; alle1.401 MAIN-checksums ongewijzigd. Beschermde settings_data-body niet gelezen of geschreven; checksum aan beide kanten d6a5642b02e3b8773a5e4e37aed01256. [Volledige bronvergelijking](theme-parity.json).

## Controle

- **31 bestaande motion-/pointerchecks PASS**, met zes fixtures zonder controls op320/390/750/989/1348/4000px. De fixtures en de bestaande homerender-acceptatie zijn aan de gewijzigde opmaak aangepast; geen nieuwe tests voor alleen CSS-opmaak toegevoegd.
- **20 bestaande merken-/sliderchecks en13 logochecks PASS.** Handmatige legacybediening blijft getest.
- Node-syntaxis, whitespacecontrole en **Shopify-validator op drie featurefiles PASS**. [Validatoruitvoer](theme-check.txt).
- **Echte Chrome-desktoppreview:** nul knoppen in de balk, juiste Draft-naam, volle1348px breedte zonder documentoverloop, acht geladen logo’s. Knop131×44px, witte tekst op donkerblauw en ronde hoeken. Echte klik opent `/collections?view=merken` met H1 ‘Onze merken’. Na teruggaan blijven beweging en muisdrag werken:2150→1830px, moving=true, geen onbedoelde navigatie. [Meetgegevens](browser-check.json) · [Screenshot](homepage-preview.jpg).
- Fysiek mobiel/tablet en echte touch zijn NOT_TESTED. De viewport-/pointerchecks zijn synthetisch. Geen FPS-benchmark of lokale Windows/Codex-wrappercontrole geclaimd.

## Volgende handeling en herstel

Eigenaar beoordeelt/publiceert **BadkamerCity - Merkenbalk zonder pijlen** in Shopify. De koppeling heeft niet gepubliceerd. Eerdere rollen en publicatiewachtnotities zijn historie.

`rollback/` bevat de drie exacte MAIN-bronfiles vóór de wijziging. Alleen in UNPUBLISHED gericht herstellen na controle op latere edits. Na eigenaarpublicatie blijft de eerdere live versie196395073802 beschikbaar voor volledige terugkeer.
