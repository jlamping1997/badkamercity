# Doorlopende merkenbalk — 9 november 2026

**BRAND-MOTION-01 LOCAL_VERIFIED / PREVIEW_COPY_PENDING.** Op eigenaarverzoek wordt de homepagebalk een langzaam naar rechts lopende, doorlopende rij over de volle paginabreedte. De bestaande gedeelde merkenlijst en officiële logo’s blijven de bron voor homepage en merkenoverzicht.

## Gedrag

- Desktop vanaf 990px: 18 pixels per seconde naar rechts, met voldoende herhalingen voor een gevulde lus, ook op een breed scherm. De kop blijft met de overige homepage-inhoud uitgelijnd.
- Onder 990px: een stilstaande rij met leesbare logo’s van 150px breed; native horizontaal vegen, pijlen en toetsenbord blijven beschikbaar.
- Pauze bij muisaanwijzen, toetsenbordfocus, buiten beeld of verborgen tab. Een zichtbare pauze-/afspeelknop laat bezoekers de beweging blijvend stoppen. Handmatige pijlen of aanraken stoppen automatisch bewegen tot opnieuw afspelen.
- Bij `prefers-reduced-motion: reduce` staat de rij stil en scrollt de bediening zonder animatie. Zonder JavaScript blijft de rij bruikbaar via native scroll.
- Visuele herhalingen behouden de echte merklinks, maar krijgen geen extra tabstops, dubbele ID’s of herhaalde schermlezerinhoud.

## Bron en afbakening

Actuele MAIN **196395073802 — BadkamerCity - Merklogos 9 nov** is door de eigenaar gepubliceerd. Codebaseline `4bf736c87e95323f5b15cb6e9f471767f8a6ce79`, branch `fix/product-cards-2026-10-14`, themabron `shopify/current/`. Omdat het eerdere reserveconcept niet meer bestaat, is de huidige MAIN via server-side `themeDuplicate` gekopieerd naar nieuw UNPUBLISHED **196416504074 — BadkamerCity - Doorlopende merkenbalk 9 nov**. Geen wijziging aan MAIN of publicatie.

Exact vijf productiefiles: `assets/bc-brand-slider.js`, `assets/bc-brands.css`, `sections/bc-homepage.liquid`, `locales/nl.json`, `locales/en.default.json`. De beschermde settings_data-body is niet gelezen of geschreven; alleen de checksum wordt vergeleken. Geen product-, prijs-, keuze-, categorie-, filter- of URL-wijzigingen. Merkenoverzicht behoudt zijn bestaande raster. Verlavio blijft tekst zolang de eigenaar geen eigen logo instelt.

## Controles

- **22 nieuwe gedragscontroles PASS:** echt component-JavaScript met synthetische geometrie, deterministische animatieframes, viewport-, voorkeur-, focus- en zichtbaarheidsgebeurtenissen. Inclusief 320/390/750/989px, desktop, ultrawide, RTL, stoppen/hervatten, native links, kopieën en editor-reconnect. [Resultaat](checks.json).
- **20 bestaande merken-/slidercontroles en 13 logocontroles PASS.** Alleen de bestaande testzoeker voor de homepage-section is aangepast aan de extra class.
- Node-syntaxis en whitespacecontrole PASS. **Shopify-validator: vijf featurefiles SUCCESS**, revisie1; na een netwerk-timeout zijn officiële gecachete schemas gebruikt. [Uitvoer](theme-check.txt).
- Browsercontrole en volledige conceptpariteit volgen na voltooiing van Shopify’s achtergrondkopie. Dit checkpoint is geen preview- of livevrijgave.
- Fysieke telefoon/tablet, echt aanraken en aangepaste merchantlogo-uploads zijn NOT_TESTED. De viewporttests zijn geen fysieke mobiele browsercontrole. Windows/Codex-wrappers zijn niet uitgevoerd.

Tests herhalen met de dependencies in package.json en `npm test`; deze sessie gebruikte dezelfde versies via `BC_TEST_DEPENDENCIES`.

## Vervolg en herstel

Volgende handeling: na voltooiing van de kopie alle bestandschecksums vergelijken, uitsluitend de vijf featurefiles in het concept plaatsen, exact teruglezen en de desktoppreview controleren.

`rollback/` bevat de vijf exacte MAIN-bronfiles van vóór de wijziging. Gericht herstellen in UNPUBLISHED na controle op latere wijzigingen; MAIN niet overschrijven. De bestaande live versie blijft beschikbaar voor terugkeer na eventuele eigenaarpublicatie. Oude themanamen en rollen in eerdere dossiers zijn gedateerde historie.
