# Repository Audit

Datum: 2026-08-03  
Scope: volledige Shopify-theme repository in `CITY_MASTER`  
Belangrijke randvoorwaarde: geen theme-code aangepast, niets gepusht naar Shopify, geen commit gemaakt.

## 1. Technische opbouw

Deze repository is een Shopify Online Store 2.0 theme met de standaard mappen:

- `layout/`: hoofd-layouts `theme.liquid` en `password.liquid`.
- `templates/`: JSON/JSONC templates voor home, product, collectie, zoekpagina, cart, blog, klantenaccount en custom page templates.
- `sections/`: herbruikbare OS 2.0 sections, met veel Dawn-achtige basissecties plus BadkamerCity custom sections.
- `snippets/`: kleinere Liquid-fragmenten voor kaarten, cart, facetten, media, productinformatie en BadkamerCity maatwerk.
- `assets/`: CSS, JS, SVG iconen, een GIF en product-switcher data.
- `config/`: theme settings schema en settings data.
- `locales/`: vertalingen en schema-vertalingen.

De basis lijkt sterk op Shopify Dawn, met forse maatwerklaag erbovenop. `layout/theme.liquid` laadt globaal `constants.js`, `pubsub.js`, `global.js`, disclosure/modal/search scripts, `base.css`, cart assets indien nodig en conditionele predictive-search/localization assets.

De grootste technische zwaartepunten zitten in:

- `sections/main-product.liquid`: circa 143 KB, bevat layout, CSS, product buybox, switcher fallback-data, specificaties en inline JS.
- `assets/global.js`: bevat Dawn-achtige globale componenten plus de oudere `BCProductSwitcher`.
- `assets/product-switcher-data.json`: circa 1,85 MB, bevat de nieuwe product-switcher dataset.
- `sections/header.liquid`: circa 67 KB, bevat veel header/subnav/mega-menu maatwerk.
- `assets/base.css`: circa 93 KB, bevat Dawn-basis plus BadkamerCity tokens en styling.

## 2. Custom functionaliteiten

Aanwezige BadkamerCity custom functionaliteiten:

- Homepagina componenten:
  - `sections/home-hero.liquid`
  - `sections/home-category-grid.liquid`
  - `sections/home-shop-by-style.liquid`
  - `sections/home-mijn-badkamercity.liquid`
  - `sections/home-brand-rail.liquid`
- Category landing pages:
  - `templates/collection.category-landing.json`
  - `sections/main-category-landing.liquid`
  - `sections/main-collection-category-landing.liquid`
  - `snippets/bc-category-icon.liquid`
- Productpagina maatwerk:
  - custom buybox styling in `sections/main-product.liquid` en `assets/section-main-product.css`
  - nieuwe product switcher via `snippets/bc-product-switcher.liquid`, `assets/bc-product-switcher.js` en `assets/product-switcher-data.json`
  - oudere/fallback product switcher in `sections/main-product.liquid` plus `assets/global.js`
  - korte en volledige specificaties via `bc-product-spec-*`, `short-specs.liquid`, `product-specs.liquid`
  - plus-/aandachtspunten snippet `snippets/product-pros-cons.liquid`
  - aangepaste media modal/gallery controls
- Zoekpagina maatwerk:
  - `sections/main-search.liquid`
  - `snippets/bc-card-product-search.liquid`
  - `snippets/bc-search-usp-strip.liquid`
- Begrippenlijst:
  - `templates/page.begrippenlijst.json`
  - `templates/page.begrip.json`
  - `sections/main-glossary.liquid`
  - `sections/main-glossary-page.liquid`
- Header/footer shell:
  - BadkamerCity footer styling in `sections/footer.liquid` en `assets/base.css`
  - custom header/subnav/wishlist/showroom links in `sections/header.liquid` en `snippets/header-drawer.liquid`

## 3. Af, onaf of mogelijk defect

Waarschijnlijk af of grotendeels bruikbaar:

- Dawn-basisfunctionaliteit voor cart, customer accounts, collections, search, product form, predictive search en localization is aanwezig.
- Nieuwe product switcher heeft een duidelijke dataset, root-snippet en JS renderer.
- Zoekresultaatkaart en USP-strip zijn concreet uitgewerkt.
- Home sections zijn uitgebreid en via `templates/index.json` gekoppeld.
- Category landing template is ingericht met blokken voor subcategorieen.

Onaf, experimenteel of verouderd:

- `sections/product-info.liquid`, `sections/product-media.liquid`, `sections/product-description.liquid`, `sections/product-specs.liquid`, `sections/bc-related-products.liquid` lijken losse/oudere productsecties naast de grote geïntegreerde `main-product.liquid`.
- `snippets/bc-product-short-specs.liquid` bevat alleen `<!-- Short specs blok verwijderd. -->`.
- `snippets/product-pros-cons.liquid` bestaat, maar ik vond geen render-verwijzing ernaar.
- `templates/index.json` bevat meerdere lege links/collecties in home-blokken.
- `templates/collection.category-landing.json` bevat placeholdertekst zoals "Voeg hier een korte omschrijving toe...".
- `sections/header.liquid` bevat hardcoded `href="#"` links voor onder andere Inspiratie, Advies, Showrooms, Afspraak maken en Zakelijk.
- Specificatie-uitleg gebruikt placeholder-links via `uitleg_url: '#'`.

Mogelijk defect:

- `sections/bc-related-products.liquid` gebruikt `{% section 'related-products' %}` binnen een section. Dat is in Shopify themes doorgaans niet toegestaan; sections worden normaal via templates/groups geplaatst, niet genest met `{% section %}` in een section.
- `sections/product-media.liquid` rendert `variant_images`, maar definieert die variabele niet. Theme Check meldt dit ook.
- `sections/product-info.liquid` rendert `product-variant-picker` en `buy-buttons` zonder dezelfde context als `main-product.liquid` verwacht, zoals `block`, `product_form_id` en `section_id`. Dit kan breken als deze losse sectie gebruikt wordt.
- `sections/main-product.liquid` gebruikt zowel een nieuwe switcher als een oude fallback. Dubbele logica vergroot de kans op afwijkend gedrag per product/metafield.
- `assets/global.js` bevat in de oude switcher een verkeerd weergegeven vinkje `âœ“`, waarschijnlijk encoding-schade.

## 4. Product switcher

Er zijn twee implementaties.

Nieuwe switcher:

- Snippet: `snippets/bc-product-switcher.liquid`
- Script: `assets/bc-product-switcher.js`
- Data: `assets/product-switcher-data.json`
- Trigger: product metafield `product.metafields.custom.switch_group`
- Root attribute: `data-bc-product-switcher-v2`

Werking:

1. Liquid leest `product.metafields.custom.switch_group`.
2. Als die gevuld is, rendert de snippet een lege container met:
   - `data-switch-group`
   - `data-product-handle`
   - `data-product-url`
   - `data-switcher-data-url`
3. `bc-product-switcher.js` laadt eenmalig `product-switcher-data.json`.
4. Het script zoekt de juiste group op `group.id`.
5. Het script zoekt het huidige product op handle of URL.
6. `menus` worden gesorteerd op `order`.
7. `products` worden gesorteerd op `sort_order`.
8. Per menu worden buttons of dropdowns gerenderd:
   - expliciet via `display_type`
   - automatisch dropdown bij meer dan 5 waarden
9. Bij selectie wordt een partial-match check gedaan; onmogelijke keuzes worden disabled.
10. Bij exacte match navigeert het script naar `matchedProduct.url`.

Datasetstatus:

- `assets/product-switcher-data.json` bevat 433 groepen, 3383 producten en 560 menu-definities.
- De dataset is groot voor een asset die op productpagina's client-side wordt geladen: circa 1,85 MB ongecomprimeerd.

Oude/fallback switcher:

- Liquid-data wordt inline opgebouwd in `sections/main-product.liquid` wanneer `switch_group` leeg is maar `custom.group` bestaat.
- Oude JS staat in `assets/global.js` als `BCProductSwitcher`.
- Deze variant gebruikt `data-bc-product-switcher`, inline `ProductGroupData-{{ section.id }}` JSON en kan extra productpagina's ophalen met `section_id` en `page`.
- Menuvelden komen uit `custom.menu_1` t/m `custom.menu_5`, of uit legacy defaults.

Risico's in de switcher:

- Twee codepaden voor vergelijkbaar gedrag.
- Grote globale JSON payload.
- Console debug output staat aan in productiecode.
- Data-asset en metafields moeten exact synchroon zijn; ontbrekende group/current product verbergt de switcher.
- Fallback switcher telt en rendert maximaal per collectiepagina en heeft paginering-workarounds.
- Backupversies van data en JS staan nog in `assets/` en kunnen per ongeluk worden gepubliceerd.

## 5. Test-, oude en backupbestanden

Verdachte backup/oude bestanden:

- `assets/bc-product-switcher.backup-debug.js`
- `assets/bc-product-switcher.js.backup-qa-round-1-20260706-214223`
- `assets/bc-product-switcher.js.backup-qa-round-1-rerun-20260707-110751`
- `assets/product-switcher-data.backup.json`
- `assets/product-switcher-data.backup-before-production.json`
- `assets/product-switcher-data.json.backup-qa-round-1-20260706-214223`
- `assets/product-switcher-data.json.backup-qa-round-1-rerun-20260707-110751`
- `assets/product-switcher-data.json.backup-qa-round-2-20260707-111611`

Waarschijnlijk oud/experimenteel:

- `sections/product-info.liquid`
- `sections/product-media.liquid`
- `sections/product-description.liquid`
- `sections/product-specs.liquid`
- `sections/bc-related-products.liquid`
- `snippets/bc-product-short-specs.liquid`
- `snippets/product-pros-cons.liquid`

Opmerking: `assets/icon-copy.svg`, `assets/template-collection.css` en `assets/template-giftcard.css` matchen deels op zoekwoorden zoals `copy` of standaard Dawn-namen, maar zijn niet automatisch backup/testbestanden.

## 6. Fouten, risico's en performanceproblemen

Theme Check resultaat:

- `shopify theme check` inspecteerde 196 bestanden.
- Resultaat: 12 offenses in 10 bestanden, waarvan 1 error en 11 warnings.
- De CLI eindigde daarna met een Windows assertion failure, wat op een lokale Shopify CLI/tooling-bug kan wijzen.

Theme Check meldingen:

- Error in `config/settings_schema.json`: `ValidJSON`, doordat Theme Check een remote schema-reference niet kon parsen. Dit lijkt mogelijk een tooling/network/cache issue, omdat het over een Shopify docs URL gaat.
- `layout/theme.liquid` en `layout/password.liquid`: `scheme_classes` als onbekend object.
- `sections/featured-product.liquid` en `sections/main-product.liquid`: `seo_media` assigned but unused.
- `sections/main-article.liquid`: `anchorId` variabelenaam.
- `sections/main-list-collections.liquid`: `moduloResult` variabelenaam.
- `sections/main-product.liquid`: `offset: continue` gemeld als onbekend object.
- `sections/main-search.liquid`: `skip_card_product_styles` assigned but unused.
- `sections/product-media.liquid`: `variant_images` onbekend.
- `snippets/bc-product-spec-row.liquid`: deprecated `img_tag`, gebruik liever `image_tag`.

Functionele risico's:

- De productpagina is zeer groot en bevat veel inline CSS/JS en dubbele switcher-logica.
- `bc-related-products.liquid` bevat vermoedelijk ongeldige section nesting.
- Header bevat meerdere `href="#"` links die gebruikers nergens heen sturen.
- Specificatie-uitleg bevat placeholder `#` links.
- `product.metafields.vendor` wordt gebruikt voor Merk in specificaties; dat lijkt verdacht, omdat Shopify vendor normaal `product.vendor` is.
- JSON/JSONC bestanden bevatten Shopify comment-headers. Dat is normaal in themes, maar gewone JSON tooling faalt hierop.
- Er is geen zichtbare testinrichting, CI-configuratie of lintconfiguratie in de repo.

Performance risico's:

- `product-switcher-data.json` is circa 1,85 MB en wordt op productpagina's client-side geladen wanneer de nieuwe switcher actief is.
- Er staan meerdere 1,8 MB backup-datasets in `assets/`; als deze naar Shopify meegaan vergroten ze theme omvang en beheerlast.
- `main-product.liquid` bevat veel inline CSS, waardoor caching/hergebruik minder gunstig is dan aparte assets.
- `main-search.liquid` bevat veel inline CSS voor zoekkaarten en USP-strip.
- De oude fallback switcher kan extra section fetches doen voor gepagineerde collecties.
- Debug logging in switcher scripts geeft ruis en kleine runtime overhead.
- Veel locale-bestanden en SVG iconen zijn standaard voor Dawn, maar vergroten de repository en moeten bewust beheerd worden.

## 7. Ontbrekende documentatie

Ontbreekt of is niet zichtbaar:

- `README.md` met projectdoel, branchstrategie en lokale setup.
- Shopify store/theme koppeling: store URL, theme ID's, staging/production flow.
- Uitleg welke files Dawn-basis zijn en welke BadkamerCity maatwerk zijn.
- Product switcher datamodel:
  - hoe `product-switcher-data.json` gegenereerd wordt;
  - eigenaar van de dataset;
  - bron van waarheid;
  - validatieregels;
  - relatie met metafields `switch_group`, `group`, `menu_1` t/m `menu_5`.
- Metafield-definities en typeverwachtingen voor alle gebruikte `custom.*` velden.
- Contentbeheer-instructies voor homepage, category landing pages, begrippenlijst en zoek-USP's.
- Testplan voor productpagina, cart, search, filters, switcher en mobile header.
- Performance budget en meetmethode.
- Release checklist: theme check, preview review, backup, publish-procedure, rollback.
- Overzicht van oude/te verwijderen bestanden.

## 8. Onderdelen voor toekomstig masterplan

Aanbevolen masterplan-onderdelen:

1. Stabilisatie en inventarisatie
   - Vastleggen welke sections/snippets actief gebruikt worden.
   - Backup/testbestanden uit publiceerbare theme-assets halen.
   - Theme Check en JSONC tooling betrouwbaar maken.

2. Product switcher hardening
   - Een bron van waarheid kiezen: asset-dataset, metafields/metaobjects of Shopify data.
   - Oude fallback en nieuwe switcher functioneel vergelijken.
   - Datavalidatie bouwen voor ontbrekende groepen, handles, URL's, menu-values en dubbele combinaties.
   - Payloadstrategie bepalen: splitsen per groep, genereren per product, metaobject-query, of lazy endpoint.

3. Productpagina vereenvoudigen
   - `main-product.liquid` opsplitsen waar veilig.
   - Inline CSS/JS reduceren.
   - Specificaties, summary, buybox en media duidelijk afbakenen.

4. Content en navigatie afronden
   - Header placeholder-links vervangen.
   - Homepage lege links/collecties vullen of conditioneel verbergen.
   - Category landing placeholdertekst vervangen.
   - Uitleg-links voor specificaties koppelen aan echte begrippenlijstpagina's.

5. Kwaliteit en tests
   - Theme Check in CI of lokale checklist.
   - Smoke test matrix voor producttypes, switcher-groepen, cart, search/filtering, mobile/desktop.
   - Performance metingen voor productpagina en zoekpagina.

6. Documentatie en overdracht
   - README, metafield catalogus, switcher datamodel, release checklist, contentbeheerhandleiding.

## 9. Nog benodigde informatie voor veilig ontwikkelen

Nodig voordat er veilig doorontwikkeld wordt:

- Welke Shopify store en welk theme is productie, staging en development?
- Is deze repo exact gelijk aan het live theme?
- Welke branch is leidend?
- Wie beheert `product-switcher-data.json` en hoe wordt die gegenereerd?
- Welke product metafields bestaan in Shopify Admin, inclusief types en validaties?
- Welke producten moeten de nieuwe `switch_group` gebruiken en welke nog de oude `group` fallback?
- Moet de oude fallback switcher blijven bestaan?
- Welke backupbestanden mogen verwijderd of buiten het theme geplaatst worden?
- Welke custom sections worden echt gebruikt in templates of in de Theme Editor?
- Welke homepage/category/header links zijn definitief?
- Welke apps zijn actief en afhankelijk van theme markup?
- Welke performancegrenzen gelden voor productpagina, collection en search?
- Welke browsers/devices moeten ondersteund worden?
- Wie keurt visuele en functionele wijzigingen goed?

## Belangrijkste bevindingen

- De theme is Dawn-gebaseerd met een grote BadkamerCity maatwerklaag.
- De productpagina is het complexste en risicovolste onderdeel.
- De product switcher bestaat dubbel: nieuwe asset-based V2 en oude Liquid/global.js fallback.
- De nieuwe switcherdataset is groot: 433 groepen, 3383 producten, circa 1,85 MB.
- Er staan meerdere grote backupbestanden in `assets/`.
- Er zijn geen ontbrekende snippet- of asset-referenties gevonden.
- Theme Check vindt 1 error en 11 warnings; sommige meldingen lijken tooling-gerelateerd, andere zijn echte aandachtspunten.

## Grootste risico's

- Switcher-regressies door dubbele logica en datakoppeling aan metafields/assets.
- Performance-impact door grote switcher JSON en grote inline product/search code.
- Per ongeluk publiceren van backup/debug assets.
- Placeholder-links en onafgemaakte content in header, category landing en specificatie-uitleg.
- Losse oude productsections kunnen defect zijn als iemand ze in de Theme Editor activeert.
- Ontbrekende documentatie maakt wijzigingen afhankelijk van impliciete kennis.

## Aanbevolen volgorde volgende stappen

1. Bevestig live/staging/development workflow en bron van waarheid.
2. Maak een inventaris van actief gebruikte templates, sections en snippets in de live Theme Editor.
3. Documenteer metafields en product-switcher datamodel.
4. Valideer de switcherdata tegen Shopify producten en metafields.
5. Beslis of de oude fallback switcher blijft of uitgefaseerd wordt.
6. Ruim backup/debug assets op in een aparte, veilige change.
7. Los Theme Check warnings/errors op of documenteer bewuste uitzonderingen.
8. Vul placeholder-links/content en koppel specificatie-uitleg aan echte begrippenlijstpagina's.
9. Daarna pas productpagina/performance refactoren met testplan en preview review.

## Aangemaakte of gewijzigde bestanden

- Aangemaakt: `docs/REPOSITORY_AUDIT.md`
- Verder geen bestanden gewijzigd.

