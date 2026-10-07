# BadkamerCity — release, acceptatie, QA en rollback

**Status:** dit is een **herhaalbaar testplan**, géén bewering dat alle vakjes nu groen zijn. Documentatiesnapshot 2026-10-07; alle genoemde URLs, productaantallen en theme-IDs moeten bij een nieuwe release opnieuw worden gecontroleerd.

## 1. Wat moet vóór elke theme-publicatie vaststaan?

| Gate | Verplicht bewijs | Wie bevestigt |
| --- | --- | --- |
| G0. Scope | Exacte taak, geraakte JSON/Liquid/CSS/JS en Admin-dependencies, wat onveranderd blijft | Ontwikkelaar |
| G1. Git | Correct origin/branch, `git status` schoon of wijzigingen verklaard, commit/PR | Ontwikkelaar |
| G2. Baseline | Huidige Shopify MAIN, ongepubliceerde conceptkopie, vergelijking met vorige versie | Ontwikkelaar |
| G3. Rendering | Relevante pagina's correct in preview (mobiel, tablet, desktop) | Test/reviewer |
| G4. Data | Links, prijzen, SKU, productstatus/publicatie, lege data en Admin-menu's correct | Data-eigenaar |
| G5. Toegankelijkheid | H1/landmarks, toetsenbord/focus, labels, alt, touch targets | Tester |
| G6. SEO | Title, meta, canonical, interne links, headings, JSON-LD, geen indexblokkade | SEO-review |
| G7. Performance | Geen onbedoelde grote JS/image-/API-requests, voor/na-metingen | Tester |
| G8. Commerce | PDP → cart en relevante bestelstroom zonder prijs-/variantverwarring | Merchant / tester |
| G9. Extern | Bij filterwijziging: VPS/API, CORS, index, foutfallback, mobiele drawer | Backend + frontend |
| G10. Publicatie | Merchant keurt de preview expliciet goed en publiceert zelf | Projecteigenaar |
| G11. Nazorg | Nieuwe MAIN, regressie-smoketests, changelog, Git-baseline en rollbackreferentie | Ontwikkelaar |

**Gates die niet getest konden worden zijn NIET “OK” maar `NOT_TESTED` of `BLOCKED`**, met reden en verantwoordelijke rol. Afwezigheid van consoleerrors is bijvoorbeeld geen bewijs van correcte checkout.

## 2. Route- en viewportmatrix

| Route / selectie | Template(s) in snapshot | Waarom testen |
| --- | --- | --- |
| `/` | `index.json` | Homepage met 8 actieve secties; banners, categorieën, merken, CTA |
| `/collections/badkamermeubels` | `collection.bc-meubelhub.json` | Goedgekeurde mobiel/desktop hub, SEO, 6 kaarten, Admin-CSS |
| `/collections/wastafels` | `collection.category-landing.json` | Menu-boom, categoriekaarten, adviestekst en A-Z |
| `/collections/accessoires` | `collection.category-landing.json` | Alternatieve A-Z-/categorie-menu's |
| `/collections/kranen` | `collection.category-landing.json` | Hoofdcategorie-landing, relatie naar Wastafelkranen |
| `/collections/wastafelkranen` | `collection.json` | Native productlijst/sorteren/filteren |
| `/collections/wastafelkranen?bcfilters=1` | `collection.json` + filterproef | Test alleen bij expliciete VPS-regressie, geen algemene launch |
| `/collections/toiletmeubels` | `collection.json` | Productlijst met beperkt assortiment / lege data |
| `/products/<bestaande-actieve-producthandle>` | `product.json` | Gallery, price, cart, switcher/specs volgens SKU |
| `/search?q=wastafel` | `search.json` | Native zoekresultaten en pagination |
| `/cart` | `cart.json` | Winkelwagen en aantallen |
| `/pages/contact` of actuele handle | `page.contact.json` indien gekoppeld | Formulier/CTA (route altijd eerst controleren) |

**Voordat een pad als testgeval geldt:** controleer of de collectie of het product daadwerkelijk gepubliceerd is. Een ADMIN-collectie met nul producten is niet automatisch een fout in het thema.

Minimale viewports: `320×700`, `375×812`, `390×844`, `430×932`, `768×1024`, `1024×768`, `1440×900`, `1920×1080`. Voeg landschap, toetsenbord/tabbing en touch toe bij menu-/drawerwijzigingen.

## 3. Aparte kwaliteitscriteria per pagina

### 3.1 Badkamermeubels (gevoelige pagina)

- [ ] Precies één zichtbare hoofd-H1 over Badkamermeubels.
- [ ] Echte H2 “Kies een categorie”; H3 kaarttitels, verdere H2/H3/H4 correct.
- [ ] Mobiel direct de compacte klikbare rijen; geen grote hero boven de categorieën.
- [ ] Desktop herkenbare luxe cards, CTA/pijl/hover, ingekorte hero.
- [ ] Geen horizontale scroll op 320–430 px.
- [ ] Zes kaarten zichtbaar; lege categorieën volgen bewust `can_link` en `allow_empty`.
- [ ] `[SPLIT]` levert onderste adviescontent zonder duplicaten op.
- [ ] Shopify Admin-omschrijving behoudt `bcm-mobile-nav-v2`, `bcm-desktop-cta-v1` en `bcm-hero-compact-v1` of er is een geteste code-equivalente migratie.
- [ ] `CollectionPage`/`BreadcrumbList`/`ItemList` schema valide en niet dubbel.
- [ ] Page title, meta description, canonical, interne links en FAQ-koppen logisch.
- [ ] Hero-afbeelding en lazy images hebben redelijke netwerkbelasting; meet werkelijke requests op mobiel.

### 3.2 Productdetailpagina

- [ ] Titel, merk, SKU, prijs, btw-/aflevertekst uit correcte bron.
- [ ] Add to cart kiest juiste productvariant en verhoogt juiste cart SKU/hoeveelheid.
- [ ] Galerij/thumbnails, productfoto's en modal reageren op touch/toetsenbord.
- [ ] Sticky koopactie overlapt geen drawer/footer.
- [ ] Zonder `custom.switch_group` geen lege of foutieve switcher.
- [ ] Met `switch_group` alleen bestaande uitvoerings-URL's en geldige combinaties.
- [ ] Specificatietabel toont alleen reële ingevulde metafields; datum/type/eenheid klopt.
- [ ] Pluspunten/aandachtspunten kloppen of component is bewust verborgen.
- [ ] Setonderdelen verwijzen naar exacte echte SKU, juiste inbegrepen/required/optional.
- [ ] Accessoires zijn expliciet geverifieerd en hun prijs/voorraad komen van Shopify.
- [ ] Gerelateerde producten/aanbevelingen worden niet als gegarandeerde curated relaties gepresenteerd.

### 3.3 Native collectielijst

- [ ] Filterchips, reset, sortering, paginering, producttellingen en lege resultaten.
- [ ] Op mobiel filterdrawer opent/sluit en houdt focus/scroll logisch.
- [ ] Geen producten uit DRAFT/UNLISTED op publieke productlijsten zonder bewust Shopify-beleid.
- [ ] Geen onbedoelde indexeerbare filterparametervarianten.
- [ ] Servergerenderde fallback aanwezig ook zonder externe filterproef.

### 3.4 Externe filterproef (alleen relevant bij aparte wijziging)

- [ ] `wastafelkranen?bcfilters=1` triggert uitsluitend testflow.
- [ ] `POST /v3/api/v1/search` bereikbaar via geconfigureerde base-URL.
- [ ] Filters/type/ranges/tellingen komen uit de juiste actuele index.
- [ ] CORS/preflight, timeouts, errors en lege responses zijn gecontroleerd.
- [ ] Fail-safe: bij serverfout blijft normale productweergave/navigatie echt bruikbaar (niet alleen fouttekst).
- [ ] Native `/collections/wastafelkranen` zonder parameter blijft onveranderd.
- [ ] Geen queryparams/secrets in publiek toegankelijke logging.

## 4. SEO-check op de echte HTML

- H1/H2/H3/H4 controleren met de DOM, niet alleen visuele lettergrootte.
- Document head: `<title>`, `meta name=description`, `canonical`; Shopify Admin SEO-velden en redirectbeleid verifiëren.
- Echte links met `<a href>`; geen niet-bestaande maat-/stijl-landings.
- JSON-LD broninspectie en Rich Results Test voor ondersteunde schematypen; `CollectionPage` op zichzelf is geen gegarandeerd Google rich result.
- Pagina's met zoek-HTTP-fallback in A-Z-menu's niet voorstellen als aparte indexeerbare collecties.
- Robots/sitemap/Search Console indexeerbaarheid en mogelijke schema-app-overlap.
- Geen rangschikking claimen op basis van headings alleen.

## 5. Performance- en toegankelijkheidsmeting

Meet vóór/na met dezelfde browser/netwerkprofielen, én controleer echt mobiel waar mogelijk:

- LCP: hero-/belangrijkste afbeelding, fonts, render-blocking CSS.
- CLS: afbeeldingsdimensies, sticky balken, fonts, latere CSS uit collectieomschrijving.
- INP/interactie: menu/drawer, slider, tabs, switcher, filters, add-to-cart.
- Network: `product-switcher-data.json` (circa 1,9 MB), CMS/CDN media, extra VPS-requests en externe apps.
- Accessibility: focus-visible, Escape/backdrop, semantische landmarks, alt, form labels, aria-status, voldoende doelgrootte.

Een aantrekkelijke pagina is niet automatisch snel; code op zichzelf bewijst geen Google-score. Noteer gemeten cijfers/metingen als bewijs.

## 6. Verplichte releasebewijzen

~~~text
Release-ID / change:
Bron Git commit en branch:
Shopify draft theme ID:
Shopify MAIN vooraf:
Shopify MAIN achteraf:
Lijst gewijzigde themafiles:
Shopify Admin-data gewijzigd? Welke velden en vorige waarden?
Externe dienst/data-index gewijzigd?
Geteste URLs + viewport + browser:
Tests: PASS / FAIL / BLOCKED / NOT_TESTED:
Prestaties voor/na indien relevant:
Review door eigenaar:
Publicatietijd, uitvoerder:
Laatste rooktest en resultaat:
Rollback-thema/commit/voorafgaande Admin-waarde:
Openstaande issues:
~~~

## 7. Incident-/rollbackplan

1. Stop verdere thema-/datawijzigingen bij impact.
2. Noteer huidige MAIN, laatste werkende theme, Git-HEAD en Admin-config vooraf.
3. Controleer of het UI-code of Admin-/serverdata is; niet automatisch theme rollback als dat niets oplost.
4. Bereid herstel op een draft-kopie voor, met gerichte wijziging.
5. Controleer minstens hoofdpagina, Badkamermeubels mobiel, PDP, native collectie en cart.
6. Laat merchant publiceren, bevestig nieuwe MAIN, werk changelog/baseline en documentatie bij.

## 8. Wat deze momentopname NIET bewijst

De code-/Admin-inventaris van 7 oktober zegt niets definitiefs over betaalgateway, real-live productbeschikbaarheid, servermonitoring, privacy/legal en Google-indexatie. Een opvolger moet deze disciplines apart laten accorderen. **VERIFIED_THEME is niet hetzelfde als RELEASE_APPROVED.**
