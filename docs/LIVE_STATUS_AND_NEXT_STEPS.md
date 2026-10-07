# BadkamerCity — bewezen live-status en volgende werkroute

**Meetdatum:** 7 oktober 2026. Dit overzicht scheidt wat bestaat van wat daadwerkelijk is getest of expliciet goedgekeurd. Nieuwe AI's mogen deze status niet stil upgraden; ze moeten nieuwe controles met datum en bron toevoegen.

## 1. Huidige status per onderdeel

| Onderdeel | Status | Wat is bewezen / wat niet |
| --- | --- | --- |
| Git-repository/theme-snapshot | **VERIFIED_THEME** | 441/441 Shopify-themebestanden inhoudelijk met Git vastgelegd, inclusief 4 grote switcher-JSON's |
| Shopify MAIN | **VERIFIED_ADMIN** | Thema `194864677130` “BadkamerCity - SEO categoriehub” MAIN op meetmoment |
| Homepage | **IMPLEMENTED_THEME** | 8 secties in `templates/index.json`; geen volledige browser/checkouttest in deze ronde |
| Header, mobiele drawer, footer | **IMPLEMENTED_THEME** | Code en Theme Editor-schema aanwezig; regressie per browser nog uitvoeren |
| Badkamermeubels desktop | **USER_APPROVED_UI / VERIFIED_THEME** | Hubsysteem, compacte hero en duidelijke categorie-CTA; Admin-description CSS dependency |
| Badkamermeubels mobiel | **USER_APPROVED_UI / VERIFIED_ADMIN** | Compacte rijnavigatie goedgekeurd; CSS deels in collectieomschrijving |
| Badkamermeubels SEO-basis | **IMPLEMENTED_THEME** | H1/H2/H3/H4, canonical/head, JSON-LD `CollectionPage`/`BreadcrumbList`/`ItemList`. GSC-rankings niet gemeten |
| Andere hoofdcategorieën | **IMPLEMENTED_THEME** | `category-landing` via 12 collectie-suffixes, menu's en adviserende inhoud |
| Native productlijsten/filtering | **IMPLEMENTED_THEME** | `collection.json` + Shopify facets/paginering; werkelijke filterdata hangt van Admin af |
| Productdetailpagina | **IMPLEMENTED_THEME** | Gallery, koopbox, options, specs, plus/min, sets, accessoires, aanbevelingen als code aanwezig |
| Product-switcher V2 | **IMPLEMENTED_THEME / DATA_DEPENDENCY** | Custom switcher + ca. 1,9 MB JSON; actuele productdekking niet integraal geverifieerd |
| Exacte Hotbath setonderdelen | **IMPLEMENTED_THEME / SOURCE_CHECK_NEEDED** | Exacte SKU-mapping in snippets; per SKU controleren |
| Accessoires / cross-sell | **IMPLEMENTED_THEME / SOURCE_CHECK_NEEDED** | Beperkte curated mappings; niet alle producten gedekt |
| Externe filterservice | **IMPLEMENTED_TEST_ONLY** | Alleen `wastafelkranen?bcfilters=1`; VPS-health en foutfallback niet bewezen |
| Productcatalogus Admin | **VERIFIED_ADMIN (counts only)** | 11.053 totaal, 11.051 ACTIVE, 1 DRAFT, 1 UNLISTED, exacte telling. Publicatie/kwaliteit niet bewezen |
| Categorieën | **VERIFIED_ADMIN (counts/assignment)** | 204 collecties: 191 default, 12 `category-landing`, 1 `bc-meubelhub` |
| Menu's | **VERIFIED_ADMIN** | 9 gedefinieerde menu's en hun boom/URLs opgeslagen |
| Productmetafield-schema | **VERIFIED_ADMIN (definitions only)** | 174 productdefinities; 54 in code letterlijk gebruikte keys niet als huidige PRODUCT-definitie teruggevonden, geen defectclaim |
| Betaal-/verzend-/BTW-regels | **NOT_VERIFIED** | Shopify Admin / testcheckout nodig |
| Core Web Vitals | **NOT_VERIFIED** | Alleen code-opbouw geaudit; geen actuele LCP/CLS/INP-meting |
| Google-indexatie/rankings | **NOT_VERIFIED** | GSC-gegevens niet in theme-repo |
| Externe VPS/leverancierimporters | **OUTSIDE_REPOSITORY** | Frontend/deelcontext bekend; backend/deployment/brondata moeten apart worden overgedragen |

## 2. Aanbevolen prioriteiten bij hervatting

### P0 — voorkom onjuiste klantdata / onverwachte uitval

1. **Productkwaliteit per merk valideren.** Maak een Shopify-export met SKU, vendor, titel, variantprijs, voorraad-/publicatiestatus, afbeelding, collectie, belangrijke metafields en SEO. Controleer ongepubliceerde, lege en verouderde gegevens. Geen massale correcties zonder bron.
2. **VPS/filter-gate correct afhandelen.** Test opt-in end-to-end (health, index, CORS, API, error fallback) voordat het sitebreed actief wordt. Native filter op publieksroutes intact houden.
3. **Shopify checkout, belasting, betaling, verzending en wettelijke teksten** laten controleren door bevoegde merchant. Theme/Git zeggen hier niets definitiefs over.

### P1 — maak onderhoud nog robuuster

4. **CSS-handoff neutraliseren:** drie beschreven inline CSS-blokken uit de Badkamermeubels-collectiebeschrijving gecontroleerd migreren naar `assets/bc-meubelhub.css`. Pas verwijderen uit Admin als mobiel/desktop exact hetzelfde blijft.
5. **Metafield-schema en rendercode harmoniseren:** echte `custom.*`/`specs.*` waarden per SKU vergelijken, contract/namespace beslissen en daarna kleine batch testen.
6. **Externe codeprojecten archiveren en overdragen** via veilige zakelijke opslag met een apart Git-repo/back-up waar passend. Vooral filterbackend, indexer, Hotbath/Wiesbaden/JEE-O importcode en bronschema's.
7. **Up-to-date browser/SEO/performance QA** uitvoeren voor homepage, hub, PDP, native listing, menu/cart.

### P2 — groei en onderhoud

8. Uitbouwen van echte, relevante subcategorie-/merk-/maatlandings met producten en unieke nuttige inhoud.
9. Documenteerde releaseprocedures automatiseren (read-only diff, regressie en theme-check) waar toepasbaar.
10. Pas na audit en rollbackplan test-/backupassets opruimen; schoon Git betekent **niet** alle oude bestanden verwijderen.

## 3. Open besluiten die iemand zonder originele ontwikkelaar niet moet raden

| Vraag | Wie moet kiezen / waarmee onderbouwen |
| --- | --- |
| Welke metafield namespace is definitief voor iedere productklasse? | Productdata-eigenaar, echte Shopify-waarden, bronmapping |
| Wanneer mogen lege categorieën klikbaar en indexeerbaar zijn? | SEO/merchandising-eigenaar met werkelijk assortiment |
| Mag externe filterindex standaard productlijsten vervangen? | Frontend/backend/commerce na foutfallback-, privacy- en loadtests |
| Wat zijn officiële levertijd-, voorraad- en garantieclaims? | Leveranciersregels en commerciële/juridische eigenaar |
| Welke importcode/CSV is per merk de laatste versie? | Oorspronkelijke datamappen, bronversie, SHA/batchlogs |
| Waar liggen serversecrets, backups, domein en Search Console? | Bevoegde IT/merchant; niet in openbare Git |
| Wat is meetbaar de huidige checkout- en bestelstatus? | Shopify Admin + veilige testbestelling en merchant akkoord |

## 4. Hoe dit document actueel houden

Na een goedgekeurde verandering: noteer datum, geraakte files/Admin-objecten, bron/commit, menselijk akkoord, verrichte test en eventuele prestatiecijfers. Trek een nieuwe Shopify MAIN-themasnapshot bij een themapublicatie. Actualiseer de menu-/metafield-/collectiedefinities zodra die wijzigen.

**Voorkom twee strijdige waarheden:** het september-masterplan blijft een historisch besluitdocument, deze actuele status en `AI_HANDOFF_CURRENT.md` beschrijven 7 oktober. Vraag altijd live Shopify/Git opnieuw op; een toekomstige bron kan beide documentmomenten achterhalen.
