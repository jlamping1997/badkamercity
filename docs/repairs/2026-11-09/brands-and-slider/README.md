# Merkenoverzicht en homepage-slider — 9 november 2026

**BRANDS-01 — PREVIEW_VERIFIED / OWNER_REVIEW_PENDING.** Op eigenaarverzoek zijn de eerste twee stappen van het merkenplan voorbereid. Logo’s zijn nog niet aangeleverd; echte merknamen zijn de zichtbare terugval. Korte/lange producttitels, prijsvolgorde van productkleuren en afzonderlijke merklandingspagina’s blijven aparte geplande stappen.

## Review en actuele rollen

- **MAIN 196395073802 — BadkamerCity - Veilige kaartprijzen 9 nov** is behouden. Alle 1.390 oorspronkelijke checksums zijn bij de eindcontrole ongewijzigd.
- **UNPUBLISHED 196354474250 — BadkamerCity - Merkenoverzicht en slider 9 nov** is het enige reviewdoel. Bestaand concept hergebruikt; geen nieuwe themakopie.
- Codebaseline: `8eb51b59dbcd41e21cb0c6c443a676cf906e50b9`, branch `fix/product-cards-2026-10-14`, themabron `shopify/current/`. De eerdere lokale wijzigingen van de kaartprijsreparatie zijn behouden en niet opnieuw als merkfeature gecommit.
- Bij opening waren er 1.390 bestanden per thema: 1.386 gelijk en vier achterlopende kaartprijsfiles. Die vier zijn eerst exact uit MAIN gekopieerd en op checksum teruggelezen. Pas daarna zijn de merkfeatures toegevoegd.
- Finale vergelijking: MAIN 1.390 / concept 1.393; **1.383 gedeelde files identiek, zeven bestaande gewijzigd en drie nieuwe toegevoegd**. Alle tien featurebodies en MD5’s exact teruggelezen. [Volledige vergelijking](theme-parity.json).

## Nieuwe werking

Eén helper, `snippets/bc-brand-items.liquid`, voedt zowel de echte actieve homepage (`bc-homepage`) als het merkenoverzicht. De lijst komt uit storefront `shop.vendors`; alleen het expliciete testmerk BadkamerCity Test wordt uitgesloten. Negen bestaande echte merken zichtbaar: Cottoceramix, Hotbath, JEE-O, Lagoo, Porcelanosa, Sunshower, The Mosaic Factory, Verlavio en Wiesbaden. Nieuwe echte storefrontmerken krijgen automatisch een tekstlink.

Het overzicht is alfabetisch. De homepage houdt Hotbath, Wiesbaden, JEE-O en Sunshower vooraan; andere merken volgen alfabetisch. De merchant kan deze prioriteit wijzigen met een kommagescheiden namenlijst. Spaties, hoofdletterverschillen, herhaalde en onbekende namen veroorzaken geen dubbele of lege merklinks.

De slider gebruikt native horizontaal scrollen met scroll-snap; geen autoplay of externe bibliotheek. Pijlen en toetsenbord Home/End/links/rechts werken. Besturing verdwijnt als er niets te schuiven is. Verminderde beweging gebruikt direct scrollen. Zonder JavaScript blijven de lijst en links beschikbaar en is horizontaal scrollen mogelijk.

## Logo’s en toekomstige merklinks beheren

Ga in de thema-editor naar **Thema-instellingen → Merken**. Hier staan:

- De eerste merken op de homepage.
- Voor elk van de negen bekende merken één logo en één optionele merkpagina.
- Lege logo’s tonen de echte merknaam. Logo’s worden met behoud van verhouding ingepast; er worden geen productfoto’s als logo gebruikt.
- Een lege merkpagina behoudt de huidige vendorbestemming; Cottoceramix behoudt zijn bestaande collectie als die beschikbaar is. Een later gemaakte merklanding kan hier eenmaal worden gekoppeld en verschijnt dan op beide plekken.

Het thema-instellingenschema is uitgebreid; `config/settings_data.json` is niet gelezen of geschreven. Die file is wel met dezelfde checksum meegenomen in de manifestvergelijking. De oude vier merkblokken zijn alleen uit de actieve bc-homepage-instantie en het schema van die sectie verwijderd; banners, categorieën, instellingen en uitgeschakelde historische secties zijn in de test exact behouden.

## Featurefiles

Zeven bestaande paden:
- `assets/bc-homepage.css`
- `config/settings_schema.json`
- `locales/nl.json`
- `locales/en.default.json`
- `sections/bc-brand-directory.liquid`
- `sections/bc-homepage.liquid`
- `templates/index.json`

Drie nieuwe paden:
- `assets/bc-brand-slider.js`
- `assets/bc-brands.css`
- `snippets/bc-brand-items.liquid`

Alle paden zijn relatief aan shopify/current. Andere product-, keuze-, prijs- en filtercode blijft bytegelijk aan MAIN. Geen Shopify-productdata, prijzen, voorraad, menu’s, collectie-identiteiten, canonical, redirects, VPS of publicatie gewijzigd.

## Controles en bewijsgrenzen

**20 controles PASS** met de echte gedeelde Liquid-renderer en slider-JavaScript. Onder andere negen merken, testuitsluiting, alfabetische volgorde, homepageprioriteit, dubbele/onbekende namen, toekomstige merken, lege lijst, locale-/URL-/HTML-escaping, Cotto-terugval, gedeelde logo-/linkinstellingen, echte homepage-/directory-callers, behoud van overige homepagegegevens/instellingen/vertalingen, pijlen, toetsenbord, grenzen, resize, lege/korte lijst, reduced motion, RTL en opnieuw verbinden in de thema-editor.

`checks.json` bevat de afzonderlijke resultaten. Herhalen: installeer de vastgepinde devDependencies uit package.json en voer npm test uit. De implementatiesessie gebruikte dezelfde dependencyversies via BC_TEST_DEPENDENCIES. Geen onverklaarde skips.

**Shopify-validator: alle tien featurefiles SUCCESS**, revisie 1. De manifestverversing via netwerk gaf een proxytimeout; de officiële lokaal gecachete schemas zijn geladen en alle bestanden zijn daarop gecontroleerd. [Volledige validatoruitvoer](theme-check.txt). Node-syntax en git diff --check PASS.

**Echte Cloud Chrome-desktoppreview:** homepage bevat alle negen merknamen, behoudt de eerste vier en schuift 0 → 652px → 0 met correcte disabled-grenzen. De link Alle merken opent het overzicht met precies negen alfabetische merklinks en één H1. Op beide pagina’s documentbreedte 1.348px gelijk aan de beschikbare paginabreedte; geen horizontale documentoverloop. Previewbalk bevestigt het juiste concept en Draft. [Homepagebeeld](homepage-preview.jpg) · [Overzichtsbeeld](directory-preview.jpg).

Dit bewijst desktopinteractie en echte Liquid-weergave. Smalle vensters, fysieke telefoon/tablet, echte touch-swipe, daadwerkelijk ingestelde nieuwe logo’s en volledige koop-/betaalflow zijn **NOT_TESTED**. Het responsive gedrag en de scrollrichting zijn daarnaast met synthetische afmetingen getest; dit is geen fysieke telefoontest. Er zijn geen order-, mail-, tracking- of rankingclaims.

## Publicatie en herstel

**Volgende handeling:** eigenaar bekijkt het genoemde concept op eigen desktop/telefoon en publiceert het via Shopify als de basis gewenst is. De echte logo’s kunnen vervolgens in dezelfde centrale instellingen worden toegevoegd. Publicatie is niet door deze uitvoering verricht; de koppeling ondersteunt die stap hier niet.

Voor individuele terugzetting: herstel alleen de zeven gewijzigde bestanden uit `rollback/` en verwijder alleen de drie nieuwe featurefiles, nadat de actuele hashes op latere wijzigingen zijn gecontroleerd. Alleen het bedoelde UNPUBLISHED-concept schrijven. Voor volledige winkelterugkeer na eigenaarpublicatie blijft de ongewijzigde vorige versie 196395073802 beschikbaar; eigenaar kan die opnieuw publiceren. Geen oud tegelprijsbestand terugzetten buiten dit dossier.

De bestaande vendorlinks en hun filterbeperkingen zijn behouden. Een losse vendorlijst is nog geen ingerichte campagne-/SEO-landing. Daarvoor blijft Hotbath de eerste geplande proef. Wiesbaden-onderzoek en de andere werkstromen zijn niet gewijzigd.

