# Merklogo’s — 9 november 2026

**BRAND-LOGOS-01 PREVIEW_VERIFIED / OWNER_REVIEW_PENDING.** Acht fabrikantlogo’s gevonden op de eigen merkwebsites en toegevoegd aan de gedeelde merkenweergave. Verlavio blijft een leesbare tekstlink: bij gerichte web-, repository-, Shopify Files- en Library-controle is geen bestaand Verlavio-logo gevonden. Geen logo voor dit eigen merk verzonnen.

## Rollen en bron

- MAIN **196354474250 — BadkamerCity - Merkenoverzicht en slider 9 nov** is behouden; alle 1.393 checksums zijn aan het einde ongewijzigd.
- Reviewconcept: bestaand UNPUBLISHED **196395073802 — BadkamerCity - Merklogos 9 nov**. Geen extra themakopie gemaakt.
- Het bestaande concept had tien achterlopende merkfeaturepaden. Eerst alle tien exact uit de huidige MAIN gekopieerd en op checksum teruggelezen; daarna alleen de logo-aanvulling.
- Codebaseline: `1b8a402e6d0e6e62e5739fc6f3a410cd6c60823a`, branch `fix/product-cards-2026-10-14`, themabron `shopify/current/`.
- Eindmeting MAIN1.393 / concept1.401: **1.391 gedeelde files gelijk, twee bestaande verschillen en acht nieuwe assets**. Alle tien featurebodies en MD5’s exact uit het concept teruggelezen. [Bronvergelijking](theme-parity.json).

## Logo’s en weergave

De officiële bronnen, verwerking en bestandschecksums staan in [logo-sources.json](logo-sources.json). Hotbath is het originele PNG-bestand; de overige zeven zijn SVG. JEE-O en The Mosaic Factory zijn exact uit de inline header-SVG overgenomen; voor Sunshower zijn de bestaande symboolpaden met een zelfstandig SVG-omhulsel opgeslagen. Geen vormen, kleuren of merknaam aangepast.

Alle bestanden staan in theme-assets en laden via Shopify CDN; geen externe hotlinks. De acht logo’s verschijnen zowel op de homepage als op het alfabetische merkenoverzicht. Vaste afbeeldingsruimte en object-fit:contain behouden de verhouding. De compacte officiële TMF-headerlogo-uitvoering blijft leesbaar binnen de kaart.

De bestaande logo-imagepickers onder **Thema-instellingen → Merken** hebben voorrang op de meegeleverde standaardlogo’s. Verlavio kan daar één keer worden ingevuld zodra de eigenaar het logo aanlevert. Een onbekend nieuw merk houdt eveneens een tekstlink. Het helptekstje van de instellingengroep is hierop aangepast.

Twee bestaande codepaden gewijzigd:
- `snippets/bc-brand-items.liquid`: standaardlogo’s na een eventuele merchantoverride, vóór de tekstterugval.
- `config/settings_schema.json`: uitsluitend uitleg over de standaardlogo’s.

Acht nieuwe `assets/bc-brand-logo-*`-bestanden. Geen wijziging aan config/settings_data.json, productmedia, prijzen, titels, kleurkeuzes, filters, URL’s of publicatie.

## Controles

- **13 nieuwe controles PASS:** bronhashes/signatures van acht assets, dezelfde acht afbeeldingen/negen links in beide weergaven, aangepaste merchantlogo-/linkvoorrang, onbekend merk en Verlavio zonder defecte afbeelding, behoud van alle bestaande instellingendefinities.
- **20 bestaande merken-/slidercontroles PASS.** Prioriteit, alfabetisering, deduplicatie, links, escaping, behoud homepagegegevens, toetsenbord, resize, reduced motion, RTL en editor-reconnect blijven werken.
- Alle SVG’s geparseerd; geen scripts, foreignObject, eventhandlers of externe afbeeldingsreferenties. Het originele PNG geverifieerd. Alle acht bestanden met Sharp gerenderd en visueel bekeken vóór plaatsing.
- **Shopify-validator: negen tekst-/SVG-featurefiles SUCCESS**, revisie1. Het ongewijzigde binaire PNG is via signature/hash en browserload gecontroleerd. Validator gebruikte na netwerk-timeout de officiële gecachete schemas. [Uitvoer](theme-check.txt).
- **Echte Cloud Chrome-desktoppreview:** acht afbeeldingen in beide weergaven volledig geladen met naturalWidth > 0, negen merklinks, Verlavio als tekst, juiste Draft-naam. Slider 0 → 652px → 0 met correcte knoppen. Documentbreedte1.348px gelijk aan paginabreedte; geen horizontale documentoverloop.
- [Overzichtsbeeld](directory-preview.jpg) · [Homepagebeeld](homepage-preview.jpg).
- Fysieke telefoon/tablet/touch en een echte nieuw ingestelde merchantlogo-upload in de thema-editor zijn niet opnieuw getest. Geen koop-, mail-, meet- of rankingvrijgave.

Tests herhalen met de vastgepinde dependencies in package.json en npm test. De implementatiesessie gebruikte dezelfde versies via BC_TEST_DEPENDENCIES. De bestaande sliderchecks staan in ../brands-and-slider/checks.mjs.

## Vervolg en herstel

**Volgende handeling:** eigenaar beoordeelt/publiceert **BadkamerCity - Merklogos 9 nov** via Shopify. De koppeling heeft niet gepubliceerd. Voor Verlavio is daarna nog het eigen logobestand nodig; de merklink blijft intussen volledig bruikbaar.

Voor gericht herstel alleen de twee gewijzigde files uit rollback/ herstellen en de acht nieuwe logo-assets weghalen, na controle op latere wijzigingen. Niet in MAIN schrijven. Voor volledige terugkeer na eigenaarpublicatie blijft thema196354474250 ongewijzigd beschikbaar om opnieuw te publiceren. Andere werkstromen en eerdere tegel-/kaartprijsaanpassingen zijn behouden.

