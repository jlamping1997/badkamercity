# BadkamerCity — START HIER bij een overdracht

**Laatste geverifieerde bronstand:** 7 oktober 2026. Dit document is het **eerste dat een nieuwe AI, freelancer, ICT'er of interne medewerker leest**. Doel: binnen 15 minuten weten wat live staat; binnen een uur veilig een taak kunnen oppakken; zonder gokken over ontbrekende toegang of data.

## 1. Wat is er werkelijk opgeleverd?

BadkamerCity is een Shopify Online Store 2.0-webshop met een custom Liquid/JSON-thema, meerdere categoriepagina-typen, homepage, productdetailpagina (PDP), product-switcher, handmatige exacte setrelaties, native filters en een optionele externe filterproef. Het **huidige live-thema** op de meetdatum is **BadkamerCity - SEO categoriehub** (`194864677130`) op `fpa9hu-i3.myshopify.com`.

Dit is een **werkende gepubliceerde themacodebasis** en een nauwkeurig gecontroleerde Git-snapshot, **geen verklaring dat webshoplancering, checkout, productdata of filters 100% gereed zijn**. De actuele code en de bekende datagrenzen staan in:

- [AI_HANDOFF_CURRENT.md](AI_HANDOFF_CURRENT.md) — volledige functionele uitleg.
- [THEME_COMPONENT_REFERENCE.md](THEME_COMPONENT_REFERENCE.md) — alle secties, instellingen, blocktypen en gekoppelde bestandsnamen; handig voor nieuwe codewijzigingen.
- [THEME_CODE_MAP_2026-10-07.json](THEME_CODE_MAP_2026-10-07.json) — machineleesbare afhankelijkheidskaart van alle **441** themabestanden.
- [SHOPIFY_ADMIN_STRUCTURE_2026-10-07.json](SHOPIFY_ADMIN_STRUCTURE_2026-10-07.json) — momentopname menu's, 204 collecties, 174 product-metafielddefinities, status-/producttellingen.
- [OPERATIONAL_RUNBOOK.md](OPERATIONAL_RUNBOOK.md) — veilige Windows/Git/Shopify-werkwijzen.
- [TROUBLESHOOTING.md](TROUBLESHOOTING.md) — concrete foutdiagnose en herstelroutes.
- [RELEASE_AND_QA.md](RELEASE_AND_QA.md) — wat getest/afgevinkt moet zijn vóór een publicatie.
- [SYSTEM_OWNERSHIP_AND_GAPS.md](SYSTEM_OWNERSHIP_AND_GAPS.md) — wat **niet** in de repo staat, welke toegang/bron nog nodig is.
- [PRODUCT_METAFIELD_MAPPING_AUDIT.md](PRODUCT_METAFIELD_MAPPING_AUDIT.md) — code-metafieldkoppelingen versus werkelijke definities.
- [HANDOFF_CHANGELOG.md](HANDOFF_CHANGELOG.md) — herkomst, bewijs en grenzen van deze overdrachtsronde.

### Bewijsniveaus

| Label | Betekenis | Voorbeeld |
| --- | --- | --- |
| **VERIFIED_THEME** | Bestand/dependency was werkelijk op live theme aanwezig en is met Git-baseline vergeleken | `sections/bc-meubelhub.liquid` |
| **VERIFIED_ADMIN** | Read-only GraphQL uit Shopify Admin op datum | `templateSuffix=bc-meubelhub` voor collectie Badkamermeubels |
| **USER_APPROVED_UI** | Gebruiker heeft uiterlijk/ervaring expliciet goedgekeurd | Mobiele rijnavigatie Badkamermeubels |
| **IMPLEMENTED_TEST_ONLY** | Code is aanwezig, maar achter schakelaar of pilotscope | Externe filters op `wastafelkranen?bcfilters=1` |
| **DOCUMENTED_NOT_VERIFIED** | Gedrag of afhankelijkheid bestaat volgens documentatie, niet recent end-to-end getest | VPS health, werkelijke checkout, Core Web Vitals |
| **HISTORICAL** | Oude stand; niet als productiestatus toepassen | Masterplan versie 0.26.3 met oude thema-ID's |

Gebruik deze labels bij elke toekomstige statusrapportage. **Een Shopify-template in Git is niet gelijk aan een ingeschakelde Shopify-collectie, en een ACTIVE product is niet automatisch online gepubliceerd.**

## 2. De eerste 15 minuten: controleer de werkelijke omgeving

1. Open de GitHub-repository `jlamping1997/badkamercity`, branch `main`.
2. Lees deze pagina, daarna `AI_HANDOFF_CURRENT.md` en `AGENTS.md`.
3. Controleer in Shopify welk thema NU rol `MAIN` heeft; vertrouw nooit blind het ID van 7 oktober.
4. Bepaal op de Windows-computer de **juiste** Git-repository en of lokale wijzigingen bestaan.
5. Identificeer de exacte template/sectie/data-eigenaar voor de taak. Als het om live verkoop gaat: controleer ook producten, checkout en beheertoegang.
6. Gebruik alleen een ongepubliceerd conceptthema voor codewijzigingen; vraag de merchant zelf te publiceren.

**Alleen read-only PowerShell-commando's om te beginnen:**

~~~powershell
# Kies de daadwerkelijk aanwezige map; historisch bestaan meerdere projecten.
cd C:\Projects\badkamercity-shopify-current
git rev-parse --show-toplevel
git remote -v
git branch --show-current
git status --short
git log -1 --oneline
shopify theme list --store fpa9hu-i3.myshopify.com
~~~

Als `git status --short` niet leeg is: **stop**, bekijk de verschillen en bewaar ze eerst. Geen `git reset --hard` of `git clean -fd`. Volg `OPERATIONAL_RUNBOOK.md`.

## 3. Wat gaat waar heen? (snelle taakroutering)

| Vraag/taak | Begin in | Admin/andere bron die óók gecontroleerd moet worden |
| --- | --- | --- |
| Homepage banners of headerhero | `templates/index.json`, `sections/home-hero.liquid` | Theme Editor, Shopify Files/CDN |
| Homepage categorieblokken | `home-category-grid.liquid` en `index.json` | Collections + Theme Editor |
| Mega-/mobiel menu of zoekbalk | `sections/header.liquid`, `snippets/bc-header-cart.liquid` | `main-menu` en Shopify search |
| Footer | `sections/footer.liquid` | Footer-blocks / menu's |
| Badkamermeubels categorie | `collection.bc-meubelhub.json` → `sections/bc-meubelhub.liquid` | Collectie `badkamermeubels`, inclusief drie **Admin-CSS**-patches |
| Andere hoofdcategorie | `collection.category-landing.json` → `sections/main-category-landing.liquid` | `main-menu` / specifieke A-Z-menu's |
| Productlijst, native filters | `collection.json` → `main-collection-product-grid.liquid` | Search & Discovery, echte producten |
| Externe filters | `bc-external-filters.js` + `bc-external-filters.liquid` | **Afzonderlijke VPS/index/API**; proefmodus |
| Productpagina ontwerp | `product.json` → `sections/main-product.liquid` | Product/variant/metafields |
| Productkleuren/keuzemenu's (switcher) | `bc-product-switcher.liquid` + `bc-product-switcher.js` | `custom.switch_group`, `product-switcher-data.json` en doel-URL's |
| Specificaties ontbreken | `bc-product-detail-specs.liquid` | **PRODUCT_METAFIELD_MAPPING_AUDIT.md**, echte Shopify-waarden |
| Setcomponenten of accessoires | `bc-product-set-data.liquid` / `bc-product-accessories-data.liquid` | Exacte compatibiliteit/SKU-verificatie |
| SEO title / description | Shopify collectie/product Admin | Theme canonical/meta, gerenderde HTML |
| Nieuwe categorie/subcategorie | Shopify Collecties + menu, toegewezen template | Publicatiestatus producten, SEO en links |
| Checkout/betalen/verzenden | Shopify Admin | Niet oplosbaar door alleen theme-code |

## 4. Architectuur in één oogopslag

~~~text
Bezoeker
  └─ Shopify Online Store / storefront
       ├─ layout/theme.liquid (header, head, CSS/JS, footer)
       ├─ templates/index.json (homepage)
       ├─ templates/collection.bc-meubelhub.json (speciale Badkamermeubels-hub)
       ├─ templates/collection.category-landing.json (categorie-overzicht)
       ├─ templates/collection.json (shoplijst/native filtering)
       ├─ templates/product.json (custom PDP)
       ├─ templates/search.json / cart.json / pages / customers
       └─ Shopify Admin en externe afhankelijke bronnen
           ├─ menu's, collecties, productstatus, SKU's, prijzen, media, metafields
           ├─ Shopify CDN, apps, checkout-instellingen
           └─ filter-VPS/Typesense en import/scraperprojecten (NIET in deze Git-repo)
~~~

Bekijk de **bestandenkaart** als een wijziging meerdere secties raakt. Een goede eerste opdracht is bijvoorbeeld “wijzig alleen de categorie-CTA op Badkamermeubels, op een ongepubliceerd thema, controleer 390px én 1440px”; een slechte opdracht is “vernieuw de hele webshop en zet live”.

## 5. De grootste valkuilen (lees voordat je iets doet)

**A. De mobiele categoriepagina is afhankelijk van Shopify Admin HTML.** In de Badkamermeubels-omschrijving staat na `[SPLIT]` drie keer een afgebakend `<style>`-blok:
`BCM_MOBILE_NAV_V2_START`, `BCM_DESKTOP_CTA_V1_START` en `BCM_HERO_COMPACT_V1_START`. Verwijderen kan het goedgekeurde mobiel/desktop-ontwerp direct breken. Snapshot in `docs/shopify-admin/collection-badkamermeubels-description-2026-10-07.html`.

**B. Er zijn verschillende templates voor verschillende collecties.** 204 collecties: **191 zonder alternate suffix (default), 12 met `category-landing`, 1 `bc-meubelhub`**. Alle collecties aanpassen via `templates/collection.json` zou onbedoeld veel meer beïnvloeden.

**C. Externe filters zijn niet overal actief.** Het frontend-script activeert pas bij `collection.handle == 'wastafelkranen'` én `bcfilters=1`. De VPS is een aparte dienst die nog actief getest moet worden.

**D. Productdata en codevelden zijn niet automatisch gelijk.** Shopify heeft **174 product-metafielddefinities**, maar de statisch gescande code noemt onder andere legacy `custom.*` keys, terwijl vele Admin-definities onder `specs.*` staan. Zie mapping-audit; niet automatisch waarden verzinnen of kopiëren.

**E. Gemakkelijk te missen:** `ACTIVE` ≠ aantoonbaar online verkoopbaar; een collectie bevat een product niet automatisch als publiek zichtbare listing. De GraphQL-snapshot telde **11.053 producten**, waarvan **11.051 ACTIVE, 1 DRAFT, 1 UNLISTED**; dit zijn Admin-statussen, **geen checkout- of publicatietest**.

**F. Git-geschiedenis en Shopify zijn apart.** De huidige `main` was op snapshotdatum een gecontroleerde kopie van live thema-code. Shopify thema-updates, Admin-mutaties en lokale ongetrackte bestanden kunnen later afwijken. Vergelijk altijd opnieuw.

## 6. Wanneer is iemand echt in staat zelfstandig door te werken?

**Code-taken:** ja, zodra GitHub/Shopify-accounttoegang, lokale Git/Shopify CLI en preview veilig werken. Alle code- en schema-verwijzingen staan in dit dossier.

**Productsynchronisatie/imports:** alleen na toegang tot bronbestanden, actuele importtools, Shopify-apprechten, datacontract, SKU-regels en importlog. Die zitten NIET allemaal in dit repo.

**VPS/externe filters:** alleen na toegang tot backend-repo/server/secretmanager, service health, indexstatus, deploymentworkflow en testplan. Het frontendbestand is niet de server.

**Complete webshoplancering:** pas na betaling/verzending/BTW, productdata, beschikbaarheid, privacy/legal, SEO en end-to-end orders te hebben gecontroleerd. Theme-snapshot is geen vrijgaveverklaring.

## 7. Concrete eerste dag voor opvolger

**0–15 min:** identiteit/thema/branch/documenten controleren.

**15–35 min:** naar functie die gewijzigd moet worden navigeren via taakroutering en componentreferentie; relevante Shopify Admin-resources read-only openen.

**35–60 min:** projectveiligheid controleren, werkzaamheden splitsen in kleine features, draft thema/backup klaarzetten, één minimaal reproduceerbare preview/test uitvoeren.

**Daarna:** alleen de expliciet goedgekeurde taak realiseren, screenshots/logs bewaren, correcte Git-commit, gebruiker laten beoordelen/publiceren en documentatie bijwerken.

Als een vraag niet met de beschikbare bronnen te beantwoorden is, gebruik **ONBEKEND/NOG TE VERIFIËREN** in plaats van een aanname.

## 8. Verantwoordelijkheid en veiligheid

Deze repository staat op GitHub en is **publiek**. Commit geen tokens, wachtwoorden, .env, privé-adressen, klant-/order-/betalingsgegevens, serverprivésleutels of gekopieerde complete leverancierscontracten. Leg *waar* een bevoegde beheerder veilige toegang aanvraagt vast, maar **niet de sleutel zelf**. Lees `SYSTEM_OWNERSHIP_AND_GAPS.md`.

**Korte instructie voor AI:** “Lees `docs/HANDOVER_START_HERE.md`, `AI_HANDOFF_CURRENT.md` en `AGENTS.md`; vergelijk actuele Shopify MAIN met Git; gebruik de codekaart en Admin-snapshot; maak in ongepubliceerde preview één gerichte wijziging en test zonder bestaande functionaliteit te slopen.”
