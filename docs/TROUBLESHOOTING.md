# BadkamerCity — foutzoekgids met oorzaak, controles en herstel

**Bronstand 2026-10-07.** Diagnose vóór wijzigingen. Kijk altijd naar de **daadwerkelijke Shopify MAIN**, `templateSuffix`, Git-commit, preview of live-URL, browser viewport, Shopify Admin-data en browser Network/Console. Leg tijdstip en effect vast zonder tokens, klantgegevens of betalingsinformatie.

## 1. Snelle beslisboom

~~~text
1. Is het alleen in preview of ook in de actuele MAIN?
   → Shopify theme role/ID, werkelijke preview-link controleren.
2. Is de pagina via een ander template gekoppeld?
   → Shopify collectie.templateSuffix of product.templateSuffix controleren.
3. Wordt dezelfde code geladen maar is de inhoud anders?
   → Shopify Admin: menu's, collectie/product status, instellingen, metafields.
4. Is er JavaScript of een netwerk-/VPS-afhankelijkheid?
   → Console en Network, API-status, CORS en foutfallback.
5. Welke gebruikersflow wordt geraakt?
   → Alleen die flow patchen op UNPUBLISHED; daarna desktop/mobile regressie.
6. Wat is de terugzetroute?
   → Bestaande theme-backup/Git-commit en vorig Admin veld bewaren.
~~~

## 2. Symptomenmatrix

| Symptoom | Eerst read-only controleren | Bestand/bron | Veilige vervolgstap |
| --- | --- | --- | --- |
| Nieuwe collectie-template ontbreekt in dropdown | Bestaat `templates/collection.<suffix>.json` werkelijk in het nu LIVE thema? | Shopify Themes, collecties | Verkeerde push/doeltheme of bestand niet doorgekomen; read-after-write en een juiste draft maken |
| Nieuw design komt niet in beeld | MAIN versus preview, Shopify `templateSuffix`, cache | Collection Admin, JSON-template | Test met de bedoelde preview, geen herhaalde blinde push |
| Badkamermeubels mobiel heeft weer grote hero | Marker `BCM_MOBILE_NAV_V2_START` aanwezig in descriptionHtml? | Shopify collectieomschrijving | Vergelijk read-only snapshot; herstel onder gecontroleerde UI-review |
| Badkamermeubels hero is desktop te hoog | Marker `BCM_HERO_COMPACT_V1_START` aanwezig? | Admin description + `bc-meubelhub.css` | Override herstellen of bewust naar code migreren, daarna desktop vergelijken |
| “Kies een categorie” staat dubbel | H2 en pseudo-element `::before` in DOM/CSS | `bc-meubelhub.liquid`, CSS | De echte H2 behouden; pseudo-heading uitgeschakeld houden |
| Kaart is zichtbaar maar niet klikbaar | Doelcollectie/`all_products_count` en `allow_empty` | `bc-meubelhub.liquid`, JSON block | Geen link maken zonder geldige bestemming of bewust besluit voor lege hub |
| Een categorie verwijst verkeerd | Block `category`, handle, redirect, producttoewijzing | Theme Editor, collecties | Corrigeer toegewezen collectie; bewaar oude handle |
| A-Z/menu linkt naar zoekresultaat | Shopify menu-item type en url | `main-menu` / A-Z-menu's | Een zoekroute is niet automatisch een SEO-landingspagina |
| Header-/mobiele navigatie werkt niet | Menutoewijzing, browserconsole, overlay, keyboard | `sections/header.liquid` | Reproduceer op 320–430 px en desktop, patch minimale oorzaak in draft |
| Zoekbalk toont geen resultaten | `/search?q=...` rechtstreeks testen | `main-search.liquid`, predictive search JS | Native search versus autosuggest isoleren |
| Collectie toont nul producten | Productstatus, Online Store-publicatie, collectie-membership | Shopify Admin | Niet oplossen met CSS: data of toewijzing eerst herstellen |
| Native filterknoppen ontbreken | Search & Discovery, actuele filters, `bcfilters`-parameter | `main-collection-product-grid.liquid` | Externe proef uitsluiten, native Shopify filters apart testen |
| Extern filter doet niets | Exacte URL `/collections/wastafelkranen?bcfilters=1` | `bc-external-filters.js`, snippet, VPS | Alleen die collectie/parameter activeert de proef |
| Extern filter geeft HTTP/CORS-fout | Network naar `POST /api/v1/search`, responsevorm | Externe VPS/backend | Filterproef uit/geen verkeer sturen, backendbeheerder en fallbacktest |
| Na filterfout verdwijnen native controls | HTML klasse `bc-external-filters-active` | `bc-external-filters.css`/JS | Fallback is nog niet end-to-end bewezen; fix op draft, niet sitebreed uitrollen |
| Switcher toont geen opties | `custom.switch_group` en groep in data-JSON | `bc-product-switcher.liquid`/JS/JSON | Check group, handle, SKU en bestaande doelproduct-URL |
| Switchen gaat naar verkeerde productkleur | Gekozen opties → exacte JSON producthandle | Switcherdata en echte Shopify producten | Corrigeer bronmapping; niet een productnaam als SKU-combinatie interpreteren |
| PDP is langzaam | Networkgrootte `product-switcher-data.json`, afbeelding en JS | `assets/bc-product-switcher.js`, productmedia | Meet mobiele LCP/INP vóór bundel-/datastructuurwijziging |
| Productspecificaties leeg | Werkelijke namespace.key en waarde; type | `bc-product-detail-specs.liquid` en mapping-audit | `custom.*` versus `specs.*` onderzoeken, geen fictieve default |
| EAN/fabrikantcode ontbreken | Shopify metafields en bronidentifiers | PDP-snippet + Admin | Definitie is geen bewijs van waarde; valideer importbatch |
| Plus/minpunten zijn weg | Werkelijke `custom.pluspunten`/`custom.aandachtspunten` waarden en block | `product-pros-cons` | Data of block visibility controleren |
| Set bestaat uit onjuiste artikelen | Exacte variant-SKU, vendor, mappingregel | `bc-product-set-data.liquid` + mapping-snip | Alleen geverifieerde relaties aanpassen; prijs uit Shopify |
| “Maak je bestelling compleet” is leeg | Bestaat expliciete accessoireregel voor SKU? | `bc-product-accessories-data.liquid` | Niet alle producten hebben curated relaties: dit kan correct zijn |
| Productfoto is vervormd of leeg | Shopify media, afmeting, image-url, CSS object-fit | `main-product.liquid`/gallery | Bronmedia versus crop/layout onderscheiden |
| Winkelwagenbadge wordt niet bijgewerkt | Shopify cart na toevoegen, drawer events | `bc-header-cart.liquid`, `cart*.js` | Native cart correctheid afzonderlijk bewijzen |
| Checkoutprijzen, BTW of verzending kloppen niet | Shopify Admin / testcheckout | Checkout/Payments/Tax/Shipping | Niet oplossen in themestyles; merchant controleren |
| SEO-title of canonical klopt niet | Gerenderde `<head>` en Admin SEO-velden | `layout/theme.liquid`, `meta-tags.liquid` | Feitelijke URL inspecteren, redirects/canonical meenemen |
| Gestructureerde data dubbel | View Source en Google's Rich Results Test | `bc-meubelhub.liquid` + apps/snippets | Schema-producent identificeren, niet blind nog JSON-LD toevoegen |
| Menu ziet er goed uit maar link geeft 404 | Publieke Shopify collectiebestemming | Admin menu/collectie | Redirect/handle/publicatie herstellen of link herzien |
| Banners ontbreken | `templates/index.json` instellingen en CDN-url | `home-hero.liquid`, Shopify Files | CDN-/Theme Editor bron verifiëren |
| GitHub is schoon, werk-pc niet | `git status --short` en `git rev-parse --show-toplevel` | Git lokale map | Wrong clone, untracked files of branch; geen reset/clean |
| Shopify CLI “success”, maar template ontbreekt | Theme-ID, rol, file aanwezig, templateSuffix | Shopify API/Admin | Controleer doeltheme read-after-write; error uit eerdere ronde is bekend |
| Site traag na kleine wijziging | Network, wat nieuw geladen is, 3rd-party requests | Image/JS/CSS en externe apps | Eerst meten (LCP/CLS/INP); voorkom speculatieve “performancefixes” |

## 3. Praktische read-only checks

**Git:**

~~~powershell
git status --short
git branch --show-current
git log -5 --oneline
git grep -n "bc-meubelhub" -- sections snippets templates assets
git grep -n "bcfilters" -- assets snippets sections
git diff --stat
~~~

**Browser:** open de exacte live of preview-URL. Inspecteer Elements voor daadwerkelijke headings/links, Network voor statuscode en grootte van CSS/JS/JSON/API, Console voor JavaScript-fouten. Vergelijk breedtes 320, 375, 390, 430 en 1440 px. Masker privacygevoelige inhoud bij screenshots.

**Shopify Admin:** controleer actuele `MAIN`, `collection.templateSuffix`, productstatus én Online Store-publicatie, menu-handles, metafielddefinities en echte waarden; voer pas daarna mutaties uit.

## 4. Wanneer moet een AI stoppen en toestemming vragen?

- Productie publiceren, thema wisselen, oude back-ups overschrijven.
- Producten massaal aanmaken/verwijderen, prijzen/voorraad wijzigen, BTW/shipping instellen.
- Externe filters overal activeren terwijl VPS-fallback niet getest is.
- Een onbekende metafieldmapping “repareren” door waarden te verzinnen.
- Een groot asset of backup verwijderen om Git-status schoon te maken.
- Gedrag dat meerdere merken/productklassen raakt zonder regressietest.

## 5. Incidentrapportje

~~~text
Datum/tijd/tijdzone:
Symptoom en getroffen URL:
Preview of MAIN theme-ID:
Git branch/commit:
Browser en viewport:
Verwacht versus daadwerkelijk:
Reproduceerbare stappen:
Code- of Admin-oorzaak (bewezen/hypothese):
Network/console-resultaat zonder geheimen:
Omvang impact:
Wijziging op draft:
Tests uitgevoerd en nog ontbrekend:
Rollbackplan:
Gebruikersgoedkeuring:
~~~

Gebruik ook [OPERATIONAL_RUNBOOK.md](OPERATIONAL_RUNBOOK.md) en [RELEASE_AND_QA.md](RELEASE_AND_QA.md). Een symptoomlijst is een onderzoekshulp, **geen bewijs dat het genoemde defect nu daadwerkelijk speelt**.
