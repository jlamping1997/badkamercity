# BadkamerCity — praktijkvoorbeelden en overnametest voor nieuwe AI/ontwikkelaar

**Gebruik dit document als oefen- en uitvoerhandleiding.** Alle stappen zijn expliciet gescheiden in `READ_ONLY`, `DRAFT_CHANGE`, `ADMIN_CHANGE_NEEDS_APPROVAL` en `PUBLISH_NEEDS_MERCHANT`. Het doel is een nieuwe medewerker zelfstandig te laten beginnen zonder onzichtbare aannames.

## Voorbeeld 1: homepagebanner veranderen

**Vraag:** “Maak de banner lager en pas een afbeelding aan.”

1. `READ_ONLY`: Bekijk `templates/index.json`. Vind de actieve section van type `home-hero` en open `sections/home-hero.liquid`. Bekijk de settings vanuit `THEME_COMPONENT_REFERENCE.md`.
2. `READ_ONLY`: Controleer in Shopify Theme Editor welke hero-/banner-afbeeldingen en bestemmingslinks feitelijk ingesteld zijn; de template-JSON kan Shopify CDN-URL's bevatten.
3. `DRAFT_CHANGE`: Pas een concrete setting of CSS aan op een nieuw ongepubliceerd, actueel thema. Als afbeelding vervangen wordt: rechten, resolutie, alt en mobiel crop eerst controleren.
4. `TEST`: 390px en 1440px, LCP/beeldverhouding, CTA-link, menu-overlay, volgende sectie direct zichtbaar.
5. `PUBLISH_NEEDS_MERCHANT`: eigenaar beoordeelt de preview en publiceert. Daarna MAIN-ID en afbeeldingverzoeken read-only controleren.

**Niet doen:** homepage-layout opnieuw bouwen omdat één banner hoger/lager moet.

## Voorbeeld 2: een nieuwe subcategorie toevoegen

**Vraag:** “Maak Douche → Douchecabines → Kwartrond volledig bruikbaar.”

1. `READ_ONLY`: Zoek in `docs/SHOPIFY_ADMIN_STRUCTURE_2026-10-07.json` het `main-menu` en de bestaande collectiehandles (snapshot is historisch; actuele Shopify Admin leidend).
2. `READ_ONLY`: Controleer de echte collectie `kwartrond`, titel, assortiment, online-publicatie, producttype, collection image en SEO-velden. Een menu-naam is geen bestaand assortiment.
3. `ADMIN_CHANGE_NEEDS_APPROVAL`: Maak/actualiseer alleen indien nodig de bestaande Shopify-collectie en het menu-item onder `Douche → Douchecabines`. Een nieuw handle kan redirects vereisen.
4. `DRAFT_CHANGE`: Gebruik `collection.category-landing.json` voor een keuzehub of `collection.json` voor echte productlisting; pas geen drie templates tegelijk aan.
5. `TEST`: Hoofdmenu desktop, mobiele drawer, breadcrumbs, categoriekaart, listing/filter, canonical en linkdoel.
6. `PUBLISH_NEEDS_MERCHANT`: eigenaar publiceert theme-code; Admin-toewijzing mag pas worden gezet zodra juiste template ook in live bestaat.

**Niet doen:** twintig dunne nieuwe maat-/merkpagina's publiceren als er geen productaanbod of unieke nuttige inhoud is.

## Voorbeeld 3: Badkamermeubels is mobiel kapot na tekstedit

**Vraag:** “Op mijn telefoon staat weer een enorm sfeerbeeld vóór de categorieën.”

1. `READ_ONLY`: Vraag Shopify collectie `badkamermeubels` op (ID `gid://shopify/Collection/569428148490`). Kijk naar `templateSuffix` en `descriptionHtml`.
2. `READ_ONLY`: Controleer of marker `BCM_MOBILE_NAV_V2_START` en style-ID `bcm-mobile-nav-v2` aanwezig zijn. Vergelijk `docs/shopify-admin/collection-badkamermeubels-description-2026-10-07.html`.
3. `READ_ONLY`: Inspecteer in de browser `.bcm-hero__media`, `.bcm-card-grid` en de CSS-cascade; andere templates/overrides kunnen ook meespelen.
4. `DRAFT_CHANGE`: Herstel alleen de ontbrekende responsieve override of migreer alle drie patches netjes naar `assets/bc-meubelhub.css` — niet één halve patch.
5. `TEST`: 320, 375, 390, 430, 768 en 1440px; controleer de echte H2 “Kies een categorie”, geen dubbele pseudo-H2, CTA en links.
6. `PUBLISH_NEEDS_MERCHANT`: daarna pas goedkeuren. Bij Admin-mutatie: oude descriptionHtml veilig bewaren.

**Niet doen:** de hele collectieomschrijving vervangen door SEO-copy; daarmee kan de mobiele stylesheet verdwijnen.

## Voorbeeld 4: specs ontbreken bij een Wiesbaden/Hotbath/JEE-O product

**Vraag:** “Productspecificaties zijn leeg, maar ik heb ze wel geïmporteerd.”

1. `READ_ONLY`: Open het product in Shopify Admin en lees SKU, vendor, status, variant en echte metafieldwaarden.
2. `READ_ONLY`: Zoek de velden die `snippets/bc-product-detail-specs.liquid` leest. Sommige zijn `custom.*`. Vergelijk `docs/PRODUCT_METAFIELD_MAPPING_AUDIT.md` met werkelijk gedefinieerde `specs.*` en `custom.*`.
3. `READ_ONLY`: Controleer datatype (tekst/getal/boolean/lijst), eenheid, missende velden en of de actieve PDP-renderer deze sectie gebruikt.
4. `DRAFT_CHANGE` of `ADMIN_CHANGE_NEEDS_APPROVAL`: Beslis expliciet of bronimport naar de bestaande canonieke namespace wordt aangepast, of Liquid een andere bewezen namespace moet lezen.
5. `TEST`: minimaal één artikel met waarde, één zonder waarde en één met boolean `false`; controleer filters en productdetailtabel.
6. `PUBLISH_NEEDS_MERCHANT` indien theme veranderd is; Admin-datamutaties alleen via goedgekeurde batch.

**Niet doen:** ontbrekende specs uit de producttitel afleiden of massaal kopiëren zonder broncontrole.

## Voorbeeld 5: Hotbath kleur/uitvoering werkt niet

**Vraag:** “De switcher stuurt bij geborsteld nikkel naar het verkeerde artikel.”

1. `READ_ONLY`: Open `snippets/bc-product-switcher.liquid` en `assets/bc-product-switcher.js`. Lees `custom.switch_group`.
2. `READ_ONLY`: Zoek de groep in `assets/product-switcher-data.json` en exact gekozen uitvoering, handle, SKU, optiecombinatie en route.
3. `READ_ONLY`: Controleer dat het doelproduct bestaat en Online Store-gepubliceerd is en dat de gekozen SKU klopt.
4. `DRAFT_CHANGE`: Corrigeer uitsluitend de bewezen mapping/groep of JS-logica. Grote data-JSON (~1,9 MB) vraagt expliciete datakwaliteit-/performancecontrole.
5. `TEST`: variantenknoppen/select, onmogelijke combinatie disabled, terugnavigatie, geselecteerde uitvoering, prijs/cart.
6. Documenteer data-generatie-/herkomstbron; het oude JSON is geen automatische actuele leveranciersfeed.

**Niet doen:** alle uitvoeringen vervangen door één Shopify productvariant zonder architectuurbesluit.

## Voorbeeld 6: “Deze set bestaat uit” toont foutieve componenten

1. `READ_ONLY`: `bc-product-set-data.liquid`, `bc-product-set-components.liquid`, `bc-product-set-product-handle.liquid` en `bc-product-set-item.liquid`.
2. Controleer per regel `included|required|optional`, quantity, exacte SKU, vendor, doelproduct en de SKU van de echte variant.
3. Corrigeer alleen relaties uit officiële leverancierdata; geen automatische matching via productnaam.
4. Test zowel een set met complete onderdelen als een product zonder set en het demo-testproduct afzonderlijk.
5. Controleer dat verkoopprijzen/beschikbaarheid uit Shopify-productrecords komen.

## Voorbeeld 7: Externe filters werken niet

1. `READ_ONLY`: Test zonder parameter de normale Shopify-collectie `/collections/wastafelkranen`. Werkt deze? Zo nee: native filter/Shopify data eerst onderzoeken.
2. `READ_ONLY`: Test `/collections/wastafelkranen?bcfilters=1`. Alleen hier zou frontendcode de externe filtermodus mogen activeren.
3. Inspecteer publieke base-URL in `snippets/bc-external-filters.liquid` en `POST /api/v1/search` in `assets/bc-external-filters.js`.
4. `READ_ONLY`: In browser Network/Console: API-status, CORS, timeout, responsevorm, index/facet-data.
5. **Niet** aanzetten op alle collecties. Test error fallback: rootclass `bc-external-filters-active` kan native filters verbergen voordat API is geslaagd.
6. Als serverdefect: externe VPS/backendbeheerder nodig. Repo bevat die backend niet.

## Voorbeeld 8: “Maak Git schoon en leg een baseline vast”

1. `READ_ONLY`: Bepaal precieze lokale repo, origin, branch, `git status --short`, GitHub remote `main` en Shopify MAIN.
2. Vergelijk remote themabestanden met Git en let op LF/CRLF.
3. Leg afwijkingen vast voordat je kiest wat de bron van waarheid is.
4. Als lokale wijzigingen bestaan: eerst veilig stash/checkpoint, pas daarna fast-forward; geen reset of clean.
5. Nieuwe docs en code in een leesbare commit met bron/date/sha, verified versus unknown.
6. `git status --porcelain` eindigt leeg op de werkplek als alle wijzigingen bewust gecommit/stashed zijn. GitHub remote alleen kan lokale status niet bewijzen.
7. Git commit vervangt geen Shopify-data-export en verandert niet automatisch live theme.

## Voorbeeld 9: Klaarzetten voor Google

1. Lees echte `<head>` uit `layout/theme.liquid` en Shopify Admin SEO-velden van de collectie.
2. Inspecteer gerenderde H1/H2/H3/H4 op concrete URL en nav-links; kijk naar `CollectionPage`/`BreadcrumbList`/`ItemList` waar ze echt worden uitgegeven.
3. Controleer Google Search Console-indexing, robots, canonical, status 200, omleidingen en wat de gebruiker voor de zoekvraag wil.
4. Controleer product-/subcollectiedekking en interne-linkboom.
5. Meet werkelijke Core Web Vitals. Geen rankinggarantie op basis van headings of schema alleen.

## 10. Overnametest — kun je zonder oorspronkelijke eigenaar door?

Laat de volgende ontwikkelaar **alleen read-only** de onderstaande vragen beantwoorden, met code-/Admin-verwijzingen:

| Vraag | Verwacht antwoord / bewijsbron |
| --- | --- |
| Wat is MAIN? | Shopify `themes` rol `MAIN`; snapshot was `194864677130`, nieuwe stand kan verschillen |
| Wat is Git source of truth? | `jlamping1997/badkamercity` `main` plus livevergelijking; geen blinde oude branch |
| Welke 3 collectie-templates bestaan? | `collection.json`, `collection.category-landing.json`, `collection.bc-meubelhub.json` |
| Hoeveel zijn waar gekoppeld op snapshot? | 191 default, 12 `category-landing`, 1 `bc-meubelhub` |
| Waarom verandert Badkamermeubels mobiel na description-edit? | 3 inline stylesheetpatches in Shopify Admin-collectiebeschrijving |
| Welke metavelden gebruikt switcher? | `custom.switch_group` plus groep/producten in `product-switcher-data.json` |
| Welke code toont Hotbath exacte sets? | `bc-product-set-data.liquid` en renderers; status|quantity|SKU|name |
| Waar staan alle actieve homepage-secties? | `templates/index.json` + individuele `home-*` sections |
| Waar staat externe filterbackend? | Niet in deze repo; frontend naar VPS; alleen wastafelkranen + `bcfilters=1` |
| Wat is het namespace-risico voor productspecs? | Verschil code `custom.*` en 174 definitiekeys waaronder `specs.*`; waarden niet gemeten |
| Kun je vanuit Git een verdwenen order herstellen? | Nee, Shopify Admin/backup is een aparte databron |
| Wie publiceert? | Merchant/eigenaar na review; AI alleen concept en checks |

**Als één van deze antwoorden niet bevestigd kan worden, noteer `BLOCKED / NOG TE VERIFIËREN`**, niet “alles compleet”. De taak kan nog steeds doorgaan voor andere, wel gedocumenteerde onderdelen.
