# Lagoo — echte productlinks en begrensde foto's

## LAGOO-17 — Hotbath-stijl en rustige offerteknop · 3 november 2026

Eigenaar accepteert de productnavigatie en vraagt exact de Hotbath-keuzestijl met eigen Lagoo-opties. De Lagoo-adapter gebruikt nu dezelfde bestaande bc-hotbath-swatches.css en hetzelfde bc-product-switcher.js: vier kleurbolletjes, geselecteerde kleur zichtbaar, selectierand/vinkje en Bekijk alle 8 kleuren / +4. Hoogte blijft Regular/Medium/High. Bestaande compacte afbeeldingsregels worden hergebruikt; geen gedeelde Hotbath-code aangepast. Zes bestaande illustratieve afwerkingsassets hergebruikt, aparte illustratieve Tuscany/champagne-SVG's toegevoegd. Deze bolletjes zijn een kleuraanduiding, geen nieuwe fabrikantkleurmeting; echte productfoto's en productdata zijn ongewijzigd.

De grote offertebalk is vervangen door hetzelfde icoon-/labelpatroon als Retour, Verlanglijst en Winkelwagen. Geen extra subtitel of blauw vlak. Laagsteprijsgarantie blijft als tooltip; bestaande bestemmingen en activeringsinstellingen behouden. Op mobiel blijft deze desktopactie verborgen. De huidige conceptbestemming is nog het bestaande offertevoorbeeld; geen nieuwe claim over werkende formulierontvangst.

Alleen bestaand UNPUBLISHED196116087050 aangepast: header.liquid, bc-header-quote.liquid, bc-lagoo-choices.liquid, nieuwe bc-lagoo-swatch-url.liquid en twee nieuwe kleur-SVG's onder shopify/current/. Deze zes bestanden identiek teruggelezen. MAIN196110090506 en gedeelde Hotbath-CSS/JavaScript ongewijzigd geverifieerd. Producten, prijzen, foto's en publicatiestatus niet gemuteerd; LVS blijft later.

**Tests:** ThemeCheck 6/6 PASS; bijgewerkte bestaande DOM-test 216/216 kleur-/hoogtewissels, vier zichtbare kleuren met selectie altijd zichtbaar, uitklappen voor verborgen keuzes, alle 24 renderbestemmingen met bestaande kleurasset, validatiegrenzen PASS. Echte Chrome-browser op 1363 CSS-pixels: nieuwe header zonder horizontale overloop, offerteactie transparant/compact; acht swatchafbeeldingen geladen. Uitklappen → koper High G1104BK (€570) → Medium G1102BK (€440), juiste URL, titel, selectie en foto; koper en uitgeklapte staat behouden. Desktop visueel gecontroleerd. Fysieke telefoon, aparte mobiele viewport, cart/checkout en offerteontvangst niet opnieuw getest. Geen browser-screenshots in publieke Git of Library opgeslagen.

**Volgende handeling:** eigenaar bekijkt de bijgewerkte stijl in hetzelfde concept; daarna gecontroleerde Lagoo-uitrol voortzetten. Geen themapublicatie. Herstel: alleen deze zes conceptbestanden terugzetten vanaf de vorige codecommit; nieuwe helper/assets zo nodig ongebruikt laten. Oorspronkelijke LAGOO-16-proef en catalogusbrede fotocorrectie blijven hieronder afgebakend.

3 november 2026 · LAGOO-16 · IMPLEMENTED_TEST_ONLY

## Scope

De eigenaar wil kleur-/uitvoeringsknoppen zoals Hotbath: een andere echte product-URL met eigen foto en prijs. De oude Lagoo-import heeft208groepen/1772SKU-varianten, waardoor modellen/kleuren in gedeelde galerijen terechtkwamen. Geen uitrol naar alle groepen of afronding van de fotocorrectie claimen.

**LVS1/LVS2/LVS3 blijven nu ongemoeid.** To-do na de fotocorrectie: zelf samen te stellen sets zoals Hotbath IBS70, met type handdouche en met/zonder glijstang. Compatibiliteit, overige keuzes en prijzen eerst bewijzen; geen nieuwe LVS-producten nu.

## Concrete proef

-24nieuwe enkelvoudige producten voor G1100/G1102/G1104, ieder8kleuren. Elk heeft één eigen fabrikantfoto, de gekopieerde actuele SKU-prijs/BTW/verzend- en trackingwaarden, artikelgerichte fabrikanttekst en uitsluitend bevestigde, in eigen beheer opgeslagen PDF's. Voorgestelde/ongerelateerde PDF's uitgesloten.
- Status **UNLISTED**, uitsluitend gepubliceerd op Webshop283427864842. Niet in zoekresultaten, collecties of aanbevelingen; directe productlinks zijn bereikbaar en koopbaar. Deze24SKU's bestaan tijdelijk ook in de oude groep. Voor definitieve uitrol zijn een gecontroleerde omzetting en historische ID-/URL-afhandeling nodig.
- De bestaande proefoudergroep is exact ongewijzigd teruggelezen: ACTIVE,24varianten,37foto's. Geen oude product-/variant-ID's verwijderd, geen bestaande prijzen veranderd. De overige207bestaande groepen zijn niet gemuteerd.
- Foto-identiteit: expliciete fabrikant-SKU waar beschikbaar; overige proefbeelden via sterke volledige/genormaliseerde beeldidentiteit met benoemde referentie en visuele controle. Legacyfoto's dienen alleen als referentie; alle gekoppelde bestanden zijn de eigen lagoo-official-fabrikantkopieën. Geen galerijvolgorde/hashnaam als kleurbewijs.

## Thema

MAIN196110090506 blijft ongewijzigd. UNPUBLISHED **196116087050 — BadkamerCity - Lagoo foto's en productkeuzes** is eerst volledig1374/1374checksums identiek bevonden. Na wijziging:1375bestanden, geen ontbrekende bestanden, exact twee bedoelde afwijkingen:

| Bestand | Functie | MD5 concept |
|---|---|---|
| shopify/current/sections/main-product.liquid | Lagoo-adapter vóór generieke variantkeuze |4f129067bb4190c90774baca8deb7aec|
| shopify/current/snippets/bc-lagoo-choices.liquid | expliciete productbestemmingen via bestaande V2-switcher |66f73b47a98d49b5e92de260a2f94ff9|

De adapter leest custom.lagoo_choices(JSON), gebruikt dezelfde bestaande bc-product-switcher.js als Hotbath en behoudt de andere gekozen eigenschappen bij een wissel. Kleur én hoogte zijn benoemde knoppen. Alleen Lagoo, één SKU per product, bestaande groepsidentiteit en exacte /products/{handle}-bestemmingen. Native links als JavaScript ontbreekt. Geen wijzigingen in gedeelde JavaScript/CSS of andere merken.

[Proef High/geborsteld nikkel](https://badkamercity.nl/products/lagoo-g1104bn?preview_theme_id=196116087050)

## Validatie

- Shopify read-after-write:24/24juiste producten, één variant/één correcte media-ID, actuele prijs/compareAtPrice/BTW/verzend-/trackingwaarden, kleur/hoogte en identieke navigatiegegevens. Beschrijving en PDF-links gelijk na uitsluitend normalisatie van Shopify's witruimte tussen HTML-tags.
- Bestaande echte V2-JavaScript in Happy DOM:216/216kleur-/hoogtewissels naar exact de bedoelde andere product-URL, geen variant-query. Op bestemmingen juiste kleur en één bijbehorende foto.
- Liquid-rendering:correcte JSON; andere merken, meerdere varianten, onbekend groepslid en externe URL worden geweigerd.
-24/24publieke conceptpagina's HTTP200; juiste24bestemmingen in inline menu en precies één juiste fabrikantfoto-ID in de afbeeldingmarkup.
- Toolkit ThemeCheck:nieuwe snippet PASS; main-product PASS met twee bestaande waarschuwingen(ongebruikte seo_media en offset:continue). Python compile en git diff --check PASS.
- Finale MAIN-controle:1374/1374originele checksums ongewijzigd. Concept alleen genoemde2verschillen.
- **NOT_TESTED:** echte browser/mobiele bediening, visuele eigenaarreview, cart/checkout, volledige catalogusmigratie en SEO-/redirectafhandeling. Happy DOM/HTTP zijn geen browservrijgave.

## Voorbereiden en herstellen

scripts/lagoo/prepare-product-links.py maakt uitsluitend DRAFT-invoer uit verse privébron+werkset+expliciete fotobewijzen; geen Shopify-writes. Het stopt bij ontbrekend bewijs, LVS, dubbele keuzes, onvolledige variantpaginering of verkeerde fabrikantbron. scripts/lagoo/test-product-links.mjs gebruikt de bestaande component-audit-devDependencies en een privé-invoerpad. Catalogus, originele400reviews en volledige receipts blijven buiten publieke Git.

Terugzetten: nieuwe24producten op DRAFT en zo nodig uitsluitend hun Webshop-publicatie ontkoppelen; oud product blijft intact. Concept niet publiceren of de twee bestanden vanaf MAIN terugzetten, uitsluitend op UNPUBLISHED. Geen bestaande producten/varianten verwijderen.

**Volgende handeling:** eigenaar beoordeelt deze24uitvoeringen in het concept; daarna resterende groepen met bewezen foto-/kleurkoppelingen en een behoudende ID-/URL-omzetting voorbereiden. Concept pas door eigenaar publiceren als de afgesproken scope is gecontroleerd. Geen actieve schrijver na deze overdracht.

