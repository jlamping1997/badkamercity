# Oneindige merkenbalk met slepen — 9 november 2026

**BRAND-MOTION-02 PREVIEW_VERIFIED / OWNER_PUBLICATION_PENDING.** Op expliciet eigenaarverzoek is het pauzeteken verwijderd, blijft de balk bewegen tijdens aanwijzen en aanraken, en is de rustige snelheid verhoogd van18 naar22px/s. Desktop én mobiel lopen nu oneindig naar rechts. Dit vervangt het eerdere pauze-/mobielcontract van BRAND-MOTION-01.

## Gedrag

De bestaande merkenrij blijft over de volle paginabreedte gevuld met herhalingen. Een muis- of vingerbeweging verplaatst de logo’s met de hand mee, in beide richtingen. Na loslaten loopt de extra snelheid kort uit en valt terug op22px/s. Ook een stilgehouden muisknop of vinger zet de gewone beweging niet stil. Pijlen geven een korte verplaatsing en laten de lus doorlopen.

Een horizontale beweging vanaf6px wordt slepen. Pointer capture houdt de beweging vast wanneer de hand de rij verlaat. Een verticale vingerbeweging blijft normaal paginaschuiven; `touch-action:pan-y pinch-zoom` behoudt ook zoomen. Na slepen wordt de bijbehorende onbedoelde merkklik geblokkeerd; een volgende gewone klik werkt normaal. Afgebroken bewegingen, meerdere vingers en oude snelheid bij lang vasthouden zijn afgedekt.

De bestaande reduced-motionvoorkeur blijft een stilstaande native rij geven. Toetsenbordfocus houdt doelen bedienbaar en hervat na verlaten van de rij; muisfocus pauzeert niet. Buiten beeld en in verborgen tabs wordt onzichtbaar animatiewerk opgeschort. Visuele kopieën hebben geen extra tabstops, dubbele ID’s of herhaalde schermlezerinhoud. Deze technische uitzonderingen zijn geen hover- of touchpauze.

## Bron en concept

- Actuele MAIN: **196416504074 — BadkamerCity - Doorlopende merkenbalk 9 nov**, door de eigenaar gepubliceerd sinds het vorige checkpoint.
- Hergebruikt concept: **196395073802 — BadkamerCity - Oneindige merkenbalk 9 nov**, UNPUBLISHED. Geen nieuwe themakopie gemaakt.
- De vijf achterlopende files van dit voormalige logoconcept zijn eerst exact uit MAIN overgenomen en teruggelezen. Met de volledige voorafgaande manifests en vijf checksumreadbacks zijn alle1.401 baselinefiles gelijk bewezen.
- Daarna precies drie featurefiles gewijzigd: `assets/bc-brand-slider.js`, `assets/bc-brands.css`, `sections/bc-homepage.liquid`. Alleen het pauzeknop-element is uit de homepage gehaald; de gedeelde merkenbron en directory zijn behouden.
- Codebaseline `55a7566ecc6130006ba02114fdc77e9f221a6484`, bestaande branch `fix/product-cards-2026-10-14`, bron `shopify/current/`.

Eindcontrole: **1.401 files per thema, 1.398 gelijk, exact drie featureverschillen**. Alle drie bodies en MD5’s teruggelezen. Alle1.401 MAIN-checksums ongewijzigd; settings_data-checksum aan beide kanten d6a5642b02e3b8773a5e4e37aed01256. De beschermde settings_data-body is niet gelezen of geschreven. Geen product-, prijs-, keuze-, filter-, URL- of publicatiewijziging. [Volledige bronvergelijking](theme-parity.json).

## Controles en grenzen

- **31 nieuwe gedragstests PASS** met echte component-JavaScript, synthetische geometrie, pointer events/capture en deterministische frames:320/390/750/989/1348/4000px, hover, vasthouden, muis/touch beide richtingen, momentum/terugval, verticale intentie, annuleren, klikbescherming, meerdere complete cycli, resize, reduced motion, toetsenbordmodaliteit, RTL, nul/één merk, legacy handmatige slider en editor-reconnect. [Uitvoer](checks.json).
- **20 bestaande merken-/slider- en13 logocontroles PASS.** De23 tests van het eerdere motiondossier zijn historische contracttests; de nieuwe31 toetsen het gewijzigde contract.
- Node-syntaxis en whitespacecontrole PASS. **Shopify-validator: drie featurefiles SUCCESS**, revisie1; officiële gecachete schemas na netwerk-timeout. [Uitvoer](theme-check.txt).
- **Echte Chrome-desktoppreview:** juiste Draft-naam, geen pauzeknop, railx0/breedte1.348px gelijk aan documentbreedte, acht geladen logo’s/negen oorspronkelijke links. Muisdrag800→1100px bracht de scrollpositie2208→1888; de homepage bleef open. Met muis erboven bleef moving=true en liep de positie verder naar1835 en1812. Geen fysiek mobiel/touch- of frame-ratebewijs geclaimd. [Meetgegevens](browser-check.json) · [Voorbeeld](homepage-preview.jpg).
- Fysieke telefoon/tablet en echte touchgebaren zijn NOT_TESTED; de touch- en mobiele checks zijn synthetisch. Screenshot toont opmaak, geen bewegingsopname. Windows/Codex-wrappers zijn niet uitgevoerd.

Tests herhalen via `npm test` met de vastgepinde dependencies in package.json; de sessie gebruikte dezelfde versie via BC_TEST_DEPENDENCIES.

## Volgende handeling en herstel

Eigenaar beoordeelt/publiceert **BadkamerCity - Oneindige merkenbalk 9 nov** in Shopify. De koppeling heeft niet gepubliceerd. Het concept bevat alle huidige MAIN-bestanden plus de drie gerichte wijzigingen.

`rollback/` bevat de drie exacte MAIN-bronfiles van vóór deze wijziging. Alleen in een UNPUBLISHED concept herstellen na controle op latere edits. Voor volledige terugkeer na eigenaarpublicatie is de eerdere live versie196416504074 beschikbaar. Historische rollen en publicatiewachtnotities in eerdere dossiers zijn geen actuele actie.
