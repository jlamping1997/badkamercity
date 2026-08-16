# BadkamerCity smoke- en regressiebaseline

> **UNEXECUTED DESIGN BASELINE**  
> Dit document is een menselijk goedgekeurde testontwerpbasis in status `DONE`. Het bevat geen bewijs dat een storefrontreis functioneel werkt.

## 1. Documentstatus

`DONE` — menselijk goedgekeurd binnen de niet-runtime/documentatiescope. Alle ontworpen runtimecases staan `UNEXECUTED`; `PASS` is nergens functioneel toegekend.

Menselijk goedgekeurd: 2026-08-16.

## 2. Taak en datum

- Taak: `BC-TECH-005` — Minimale smoke- en regressiebasis vastleggen.
- Onderzoeksdatum: 2026-08-16.
- Algemene projectstatus: `ACTIVE FOR DISCOVERY - IMPLEMENTATION BLOCKED`.
- Uitvoeringsvorm: uitsluitend lokale read-only analyse plus documentatie.

## 3. Doel

Een kleine maar voldoende brede, herhaalbare en privacyveilige smoke-/regressiematrix ontwerpen waarmee een later expliciet toegestane technische wijziging aantoonbaar kan worden beoordeeld vóór preview, merge en release.

## 4. Scope

De scope omvat bestaande actieve theme-paden, lokale bewijsdocumenten, routeklassen, responsive width-breakpoints, fixtureklassen, L0/L1/L2-testlagen, testcases, stopvoorwaarden, bewijsvelden en een proportionele change-impactmatrix. Theme-code is alleen gelezen.

## 5. Buiten scope

Geen browser- of storefronttest, Shopify-query, preview, cartmutatie, login, account-/orderinzage, checkout, formulierverzending, screenshot, package-installatie, CI-wijziging, theme-codewijziging, defectoplossing of performancebudget. De matrix autoriseert geen latere uitvoering.

## 6. Bewijsbronnen

- `docs/ACTIVE_THEME_USAGE.md`: primaire route-, template-, section-, account- en switcherclassificatie.
- `docs/REPOSITORY_AUDIT.md`: lokale code- en toolinggrens.
- `docs/THEME_CHECK_BASELINE.md`: statische kwaliteitsbaseline en fingerprints.
- `docs/TECHNICAL_CHANGE_WORKFLOW.md`: gates, branch-, preview-, merge- en rollbackregels.
- `docs/TECHNICAL_STABILIZATION_PLAN.md`: herkomst `PROPOSED-TECH-02` en grens met `PROPOSED-TECH-12`.
- `docs/SHOPIFY_ADMIN_INVENTORY.md`, `docs/DEVELOPMENT_THEME.md`, `docs/LIVE_THEME_COMPARISON.md` en `docs/SHOPIFY_ENVIRONMENT.md`: uitsluitend bestaande lokale snapshots; niet opnieuw bevraagd.
- Gerichte lokale code-read van relevante actieve CSS, Liquid, templates en snippets; bewijs staat in de run `BC-TECH-005_20260816-113636`.

## 7. Bewijslabels

- `BEWEZEN IN LOKALE CODE`: statisch aangetroffen in een lokaal themebestand.
- `BEWEZEN IN BESTAAND SNAPSHOT`: afkomstig uit een reeds bestaand bewijsdocument; actualiteit moet vóór runtime worden herbevestigd.
- `VOORGESTELD`: testontwerp, viewport of selectieregel; geen runtimefeit.
- `DYNAMIC_OR_NOT_PROVEN`: bereikbaarheid of gedrag hangt van runtime/configuratie af en is niet bewezen.
- `UNEXECUTED`: ontworpen maar niet uitgevoerd.
- `BLOCKED`: uitvoering kon niet verantwoord starten of afronden; dit is nooit `PASS`.

## 8. Huidige functionele bewijsgrens

Deze taak heeft nul functionele smoke- of regressietests uitgevoerd. Een statisch bewezen template-, section- of codereferentie bewijst geen render, interactie, netwerkgedrag, toegankelijkheid, structured-data-uitvoer of performance. Historische snapshotkandidaten vereisen read-only hervalidatie vlak vóór een afzonderlijk geautoriseerde runtime-uitvoering.

## 9. Route- en templatebasis

De matrix telt 16 kernrouteklassen. Prioriteit betekent toekomstige smokeprioriteit, niet huidige uitvoeringsstatus.

| Routeklasse | Actieve template of grens | Primaire sections/componenten | Bereikbaarheid | Prioriteit | Bewijsbron |
| --- | --- | --- | --- | --- | --- |
| Homepage | `templates/index.json` | vijf `home-*`-sections en header | `ACTIVE_LIVE` | L1 | `ACTIVE_THEME_USAGE.md`; lokale template-read |
| Standaard collectie | `templates/collection.json` | `main-collection-banner`, `main-collection-product-grid` | `ACTIVE_LIVE` | L1 | `ACTIVE_THEME_USAGE.md` |
| Category-landing collectie | `templates/collection.category-landing.json` | `main-category-landing` | `ACTIVE_LIVE` | L1 | `ACTIVE_THEME_USAGE.md` |
| Zoekpagina | `templates/search.json` | `main-search` | `ACTIVE_LIVE` | L2, of L1 bij search-impact | `ACTIVE_THEME_USAGE.md` |
| Predictive search | header + dynamische predictive endpoint/section | `header-search`, `predictive-search` | `REACHABLE_FROM_ACTIVE` | L2 | lokale header/theme-read; actieve instelling in bestaand bewijs |
| Productpagina | `templates/product.json` | `main-product` | `ACTIVE_LIVE` | L1 | `ACTIVE_THEME_USAGE.md` |
| Related products | producttemplate | `related-products` | `REACHABLE_FROM_ACTIVE` | L2 | lokale producttemplate-read |
| Cart notification | header bij `cart_type=notification` | `cart-notification` | `REACHABLE_FROM_ACTIVE` | L1 | bestaande config en lokale header-read |
| Cart page | `templates/cart.json` | `main-cart-items`, `main-cart-footer`, `featured-collection` | `ACTIVE_LIVE` | L1 | `ACTIVE_THEME_USAGE.md` |
| 404 | `templates/404.json` | `main-404` | `ACTIVE_LIVE` | L2 | `ACTIVE_THEME_USAGE.md` |
| Begrippenlijst | `templates/page.begrippenlijst.json` | `main-glossary` | `ACTIVE_LIVE` | L2 | `ACTIVE_THEME_USAGE.md` |
| Begrippendetail | `templates/page.begrip.json` | `main-glossary-page` | `ACTIVE_LIVE` | L2 | `ACTIVE_THEME_USAGE.md` |
| Contactpagina | `templates/page.contact.json` | `main-page`, `contact-form` | `ACTIVE_LIVE` | L2 | `ACTIVE_THEME_USAGE.md`; verzenden buiten scope |
| Nieuwe customer-account entry/linkgrens | header/drawer-link naar account-login; nieuwe accounts | header en `header-drawer` | `REACHABLE_FROM_ACTIVE` | L2 | bestaand accountsnapshot plus lokale link-read |
| Password | `layout/password.liquid`, `templates/password.json` | `email-signup-banner` | `DYNAMIC_OR_NOT_PROVEN` | L2 indien impact | lokaal bestand; geen runtimebewijs |
| Gift-card | `templates/gift_card.liquid` | gift-cardtemplate | `DYNAMIC_OR_NOT_PROVEN` | L2 indien impact | lokaal bestand; geen actieve fixture bewezen |

`AVAILABLE_NOT_ACTIVE` blijft van toepassing op klassieke customer-accounttemplates; de bestaande snapshot classificeert de shop als nieuwe customer accounts. Voor account, password en gift-card wordt geen runtimeclaim gedaan.

## 10. Breakpointinventaris

`BEWEZEN BREAKPOINT IN CODE`: een gerichte read-only scan van 27 voor actieve routes relevante CSS-/Liquidbestanden vond 183 `@media`-headers, 172 width-breakpointvermeldingen en exact 7 unieke width-waarden. Zeventien overige mediaheaders betroffen alleen reduced motion, forced colors of hover en zijn geen width-breakpoint. Frequentie is het aantal vermeldingen, niet het aantal ondersteunde apparaten.

| Width-waarde | Frequentie | Richting(en) | Relevante actieve bestanden/componenten |
| --- | ---: | --- | --- |
| `479px` | 1 | max | `sections/home-category-grid.liquid`; home |
| `749px` | 29 | min/max | `base.css`, header/menu, product, collectie/search, home |
| `750px` | 81 | min | globaal, header/menu, product, collectie/search, cart en home; dominant |
| `900px` | 1 | min | `assets/section-main-product.css`; product |
| `989px` | 19 | max | globaal, header/menu, product, collectie/search |
| `990px` | 40 | min/max | globaal, header/menu, product, collectie/search, cart en home; dominant |
| `1199px` | 1 | max | `sections/header.liquid`; header |

De 749/750- en 989/990-paren zijn dominante lokale omslagpunten. De scan bewijst code-aanwezigheid, niet dat ieder component visueel correct omschakelt.

## 11. Voorgestelde referentieviewports

Dit zijn `VOORGESTELDE REFERENTIEVIEWPORTS`, afgeleid van lokale code; zij claimen geen volledige browser- of apparaatondersteuning.

| Viewportklasse | Voorgestelde pixels | Afleiding | Gebruik later |
| --- | --- | --- | --- |
| `VP-MOBILE` | `375 × 812` | duidelijk onder 479px en het dominante desktopbegin 750px | mobiele header, grid, PDP en cart |
| `VP-DESKTOP` | `1280 × 900` | duidelijk boven 990px en de headergrens 1199px | desktopheader, brede grids, PDP en cart |
| `VP-BOUNDARY-750` | gepaard `749 × 900` en `750 × 900` | lokale aangrenzende max/min-grens | optionele gerichte grenscontrole bij responsive impact |

Een latere menselijke gate bepaalt of deze voorstellen, de hoogte en eventueel de 989/990-grens worden gebruikt.

## 12. Fixturemodel

Een fixture is een herhaalbare teststate of selectieregel, geen verzonnen productrecord. Iedere kandidaat uit een historisch snapshot blijft ongeldig voor uitvoering totdat route, status, template, benodigde metafields en veilige beschikbaarheid opnieuw read-only zijn bevestigd. Persoonsgegevens zijn voor alle fixtures verboden.

## 13. Fixturecatalogus

De catalogus bevat exact 12 unieke fixtureklassen.

| Fixture-ID | Doel | Benodigde eigenschappen | Bewijsbron / concrete kandidaat | Hervalidatie vóór uitvoering | Latere mutatiecategorie | Persoonsgegevens toegestaan |
| --- | --- | --- | --- | --- | --- | --- |
| `FIX-PDP-V2` | V2-switcherpad | actief product, niet-lege `custom.switch_group`, handle in V2-assetgroep | snapshot bewijst 3.658/7.827 niet-lege velden; assetgroep `hotbath-ace-ac003-wastafelkraan` met producthandlekandidaten | productstatus, veldwaarde, groeps- en handle-overlap, publicatie en veilige variant | `READ_ONLY`; add-to-cart apart | NEE |
| `FIX-PDP-NO-V2` | regulier PDP-pad zonder V2 | actief product met lege `custom.switch_group` en zonder bewezen legacytrigger | snapshot impliceert 4.169 lege V2-velden; geen individueel product wordt verzonnen | concrete kandidaat selecteren en lege V2/legacyvelden bewijzen | `READ_ONLY`; add-to-cart apart | NEE |
| `FIX-PDP-TILE` | bestaand tegelproduct zonder calculatorclaim | actief producttype tegel/mozaïek; regulier PDP-pad | snapshotkandidaat `the-mosaic-factory-venice-pennyround-red-glossy-mozaiektegel-vkn010` | status, type, route, template en ontbreken van geautoriseerde calculatorfixture | `READ_ONLY` | NEE |
| `FIX-COLLECTION-DEFAULT` | standaard collectie | default template, bereikbaar, bij voorkeur niet-leeg | snapshotkandidaat `ibs70-cobber-doucheset`; suffix per kandidaat nog te herbevestigen | template, productcount, publicatie en route | `READ_ONLY` | NEE |
| `FIX-COLLECTION-LANDING` | category landing | `category-landing`-template en bereikbare bloktargets | bestaand bewijs noemt onder meer handle `badmeubel-sets` | template, publicatie, bloktargets en lege-state | `READ_ONLY` | NEE |
| `FIX-SEARCH-RESULTS` | publieke zoekresultaten | niet-persoonlijke term met onderbouwde assortimentkans | voorgestelde term `wastafelkraan`, onderbouwd door snapshotproduct-/collectietitels | term levert op testmoment resultaten; geen klantinput | `READ_ONLY` | NEE |
| `FIX-SEARCH-ZERO` | nulresultaatstate | synthetische niet-persoonlijke term | voorgesteld `bc-smoke-geen-resultaat-20260816` | vóór bewijs vaststellen dat resultaat echt nul is | `READ_ONLY` | NEE |
| `FIX-CART-EMPTY` | lege cart | nieuwe geïsoleerde storefrontsessie zonder regels | ontwerpstate; geen Admin- of klantdata nodig | cart leeg en sessie niet hergebruikt | `EPHEMERAL_STOREFRONT_STATE` | NEE |
| `FIX-CART-ONE-ITEM` | één veilige cartregel | tijdelijk één herbevestigd niet-persoonlijk testproduct | hergebruik later een geldige PDP-fixture; geen specifiek variant-ID vastgelegd | product/variant beschikbaar, geen bestelling of checkout | `EPHEMERAL_STOREFRONT_STATE` | NEE |
| `FIX-ACCOUNT-ANON` | account-entry/linkgrens | anonieme sessie, alleen zichtbare link en bestemming | bestaand bewijs: nieuwe customer accounts en header-/drawerlink | accountmodel en link read-only herbevestigen | `READ_ONLY`; login verboden | NEE |
| `FIX-404` | foutpagina | synthetische niet-bestaande publieke route | voorgestelde willekeurige slug zonder klantdata | bevestig vooraf geen bestaande route te raken | `READ_ONLY` | NEE |
| `FIX-GLOSSARY` | index plus één detailtype | actieve begrippenlijst en bestaand `page.begrip`-item | snapshot bewijst één index en 109 detailtemplates; geen detailhandle verzonnen | concrete publieke detailroute selecteren en template bewijzen | `READ_ONLY` | NEE |

## 14. Testlagen L0/L1/L2

- `L0 — STATIC GATE`: branch/basis, diff-whitelist, Theme Check vóór/na, fingerprintdelta, parser-/syntaxischecks en `git diff --check`.
- `L1 — CRITICAL SMOKE`: kritieke route- en interactieoppervlakken die door de wijziging geraakt kunnen zijn.
- `L2 — IMPACT REGRESSION`: proportionele aanvullende dekking voor search, landing, kaarten, PDP-details, switchers, cart, content, keyboard, structured data, performancebewijs en extra responsive states.

Alle drie lagen zijn in deze taak uitsluitend `ONTWERP`. Er is geen browser- of functionele test uitgevoerd.

## 15. Testcase-ID-conventie

Formaat: `SMK-<DOMEIN>-NNN`, met hoofdletters, één functioneel domein en een binnen dat domein oplopend driecijferig nummer. ID's zijn uniek in de centrale matrix; latere verwijzingen naar hetzelfde ID maken geen nieuwe testcase.

## 16. Centrale testcasematrix

Alle 53 cases zijn `UNEXECUTED`. `M`, `D`, `K`, `SD` en `Perf` betekenen mobiel, desktop, toetsenbord, structured data en performance-relevantie. Voor iedere rij geldt `Persoonsgegevens = NEE`.

| Test-ID | Titel | Laag | Wijzigingsoppervlak | Route/component | Fixture | Precondities | Stappen later | Verwacht resultaat | Failureclassificatie | Bewijsvereiste | M | D | K | SD | Perf | Persoonsgegevens | Toekomstige menselijke gate | Huidige status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `SMK-STATIC-001` | Branch en basis | L0 | alle codewijzigingen | Git | n.v.t. | officiële taak, toestemming, exacte basis | vergelijk branch, HEAD en goedgekeurde basis | exact toegestaan branchmodel en basis | `FAIL/ENVIRONMENT_MISMATCH` | commandlog en hashes | N | N | N | N | N | NEE | GATE A/B | UNEXECUTED |
| `SMK-STATIC-002` | Diff-whitelist | L0 | alle wijzigingen | Git diff | n.v.t. | exacte bestandswhitelist | vergelijk changed/staged files met whitelist | geen bestand buiten scope | `FAIL/REGRESSION` | filelist, diffstat, volledige diff | N | N | N | N | N | NEE | GATE B/F | UNEXECUTED |
| `SMK-STATIC-003` | Theme Check vóór | L0 | theme-code | statische tooling | n.v.t. | goedgekeurde wrapper en basis | voer baselinecheck volgens BC-TECH-003 uit | bekende baseline reproduceerbaar | `BLOCKED/TOOLING_FAILURE` of `FAIL/REGRESSION` | runlog, versie, fingerprints | N | N | N | N | N | NEE | GATE B | UNEXECUTED |
| `SMK-STATIC-004` | Parser en syntaxis | L0 | gewijzigd codeformaat | betrokken bestanden | n.v.t. | parser reeds toegestaan en beschikbaar | parse alleen gewijzigde ondersteunde bestanden | geen nieuwe parse-/syntaxfout | `FAIL/REGRESSION` | commando, versie, foutlocaties | N | N | N | mogelijk | N | NEE | GATE B | UNEXECUTED |
| `SMK-STATIC-005` | Theme Check na | L0 | theme-code | statische tooling | n.v.t. | implementatie gereed | voer identieke wrapper na wijziging uit | resultaat volledig vastgelegd | `BLOCKED/TOOLING_FAILURE` of `FAIL/REGRESSION` | runlog, versie, fingerprints | N | N | N | N | N | NEE | GATE B/F | UNEXECUTED |
| `SMK-STATIC-006` | Fingerprintdelta | L0 | theme-code | Theme Check-uitvoer | n.v.t. | voor- en naresultaat beschikbaar | vergelijk unieke fingerprints en ernst | geen nieuwe, bredere of ernstigere offense zonder besluit | `FAIL/REGRESSION`; bestaand alleen met bewijs | delta en classificatie | N | N | N | N | N | NEE | GATE B/F | UNEXECUTED |
| `SMK-STATIC-007` | Git diff check | L0 | alle wijzigingen | Git | n.v.t. | werkdiff gereed | voer `git diff --check` uit | exitcode 0 | `FAIL/REGRESSION` | raw stdout/stderr/exitcode | N | N | N | N | N | NEE | GATE B/F | UNEXECUTED |
| `SMK-HOME-001` | Homepage basisrender | L1 | homepage/globaal | `/` | n.v.t. | geautoriseerde preview en actieve homepage | open route op vereiste viewports | geen crash; hoofdcontent zichtbaar | `FAIL/REGRESSION` | route, commit, viewport, screenshot/log | J | J | N | N | J | NEE | GATE D/E | UNEXECUTED |
| `SMK-HOME-002` | Primaire zichtbare navigatie-ingangen | L1 | homepage/header | homepage-ingangen | n.v.t. | links zichtbaar | inspecteer en activeer alleen veilige GET-links | relevante zichtbare ingang heeft geldige bestemming | `FAIL/REGRESSION`; leeg optioneel volgens bewijs | linklijst en bestemmingen | J | J | J | N | N | NEE | GATE D/E | UNEXECUTED |
| `SMK-HOME-003` | Lege of optionele home-targets | L1 | homepage | vijf home-sections | n.v.t. | bestaande optionele/lege targets bekend | render zonder datawijziging en inspecteer betreffende blokken | geen templatecrash; leegte veilig afgehandeld | `FAIL/REGRESSION` of `PRE_EXISTING` met basisbewijs | blok, configbewijs, screenshot/log | J | J | N | N | N | NEE | GATE D/E | UNEXECUTED |
| `SMK-HEADER-001` | Desktopheader | L1 | header/navigation | desktopheader | n.v.t. | `VP-DESKTOP`; menu aanwezig | open pagina en inspecteer logo, menu, search, account/cartlinks | header bruikbaar zonder overlap of ontbrekende primaire control | `FAIL/REGRESSION` | viewport en screenshot/log | N | J | N | N | J | NEE | GATE D/E | UNEXECUTED |
| `SMK-HEADER-002` | Mobile drawer | L1 | header/navigation | mobile drawer | n.v.t. | `VP-MOBILE`; anoniem | open/sluit drawer en navigeer één niveau zonder formulier | drawer opent, focus/labels zichtbaar, veilige link bereikbaar | `FAIL/REGRESSION` | stappen, viewport, screenshot/log | J | N | J | N | J | NEE | GATE D/E | UNEXECUTED |
| `SMK-HEADER-003` | Toetsenbord primaire navigatie | L2 | header/navigation | header/menu | n.v.t. | toetsenbordinput | tab, activeer en sluit waar van toepassing | logische bereikbaarheid en zichtbare focus | `FAIL/REGRESSION` | focusvolgorde en control-ID's | J | J | J | N | N | NEE | GATE D/E | UNEXECUTED |
| `SMK-HEADER-004` | Geen dode focusroute | L2 | header/navigation | getest headeroppervlak | n.v.t. | drawer/menu geopend indien van toepassing | doorloop controls voor- en achterwaarts | geen onverwachte focusval of onbereikbare sluitactie | `FAIL/REGRESSION` | focusroute en afwijkingslog | J | J | J | N | N | NEE | GATE D/E | UNEXECUTED |
| `SMK-COLL-001` | Default collection | L1 | collectie | `collection.json` | `FIX-COLLECTION-DEFAULT` | fixture hervalideerd | open route, inspecteer titel/grid/paginastate | route rendert met correcte standaardstructuur | `FAIL/REGRESSION` | fixture, route, viewport, screenshot/log | J | J | N | N | J | NEE | GATE D/E | UNEXECUTED |
| `SMK-COLL-002` | Category landing | L1 | collectie/landing | `collection.category-landing.json` | `FIX-COLLECTION-LANDING` | template en targets hervalideerd | open landing en volg één veilige targetlink | landing en aanwezige targets renderen zonder crash | `FAIL/REGRESSION`; leeg bewijsbaar classificeren | config, route en screenshot/log | J | J | J | N | J | NEE | GATE D/E | UNEXECUTED |
| `SMK-COLL-003` | Productgrid en productkaart | L1 | collectie/product card | productgrid | `FIX-COLLECTION-DEFAULT` | niet-lege fixture | inspecteer eerste representatieve kaart en open PDP | identiteit, prijs indien aanwezig en link blijven coherent | `FAIL/REGRESSION` | kaart/PDP-identiteit en screenshot/log | J | J | J | N | J | NEE | GATE D/E | UNEXECUTED |
| `SMK-COLL-004` | Filter- en sorteringsbasis | L2 | collectie/search | facets/sort | `FIX-COLLECTION-DEFAULT` | runtimefacets werkelijk beschikbaar | wijzig één veilige filter/sortering en herstel | state verandert zonder crash en route blijft coherent | `BLOCKED/FIXTURE_INVALID` of `FAIL/REGRESSION` | URL/state/resultaatlog | J | J | J | N | J | NEE | GATE D/E | UNEXECUTED |
| `SMK-SEARCH-001` | Search met resultaat | L1 | search | `/search` | `FIX-SEARCH-RESULTS` | term hervalideerd | voer publieke term in en open resultaatpagina | resultatenstate zonder fout; relevante kaart bruikbaar | `FAIL/REGRESSION` | term, route, count/state, screenshot/log | J | J | J | N | J | NEE | GATE D/E | UNEXECUTED |
| `SMK-SEARCH-002` | Search nulresultaat | L2 | search/empty | `/search` | `FIX-SEARCH-ZERO` | term vooraf nul | voer synthetische term in | begrijpelijke nulstate, geen crash of oude resultaten | `FAIL/REGRESSION` of `FIXTURE_INVALID` | term, nulbewijs, screenshot/log | J | J | J | N | N | NEE | GATE D/E | UNEXECUTED |
| `SMK-SEARCH-003` | Predictive search | L2 | predictive search | header search | `FIX-SEARCH-RESULTS` | feature actief en endpoint bereikbaar | typ term zonder persoonsgegevens; inspecteer suggesties | dynamische state/labels coherent of expliciet geblokkeerd | `FAIL/REGRESSION` of `BLOCKED/ENVIRONMENT_MISMATCH` | request/resultaatstate en screenshot/log | J | J | J | N | J | NEE | GATE D/E | UNEXECUTED |
| `SMK-SEARCH-004` | Search toetsenbordinteractie | L2 | search | input/listbox/resultaat | `FIX-SEARCH-RESULTS` | toetsenbord; predictive indien actief | focus input, typ, navigeer suggesties, escape/submit | focus en selectie voorspelbaar; geen dode route | `FAIL/REGRESSION` | focus-/keylog en controlstate | J | J | J | N | N | NEE | GATE D/E | UNEXECUTED |
| `SMK-PDP-001` | PDP basisrender | L1 | product/PDP | `product.json` | `FIX-PDP-NO-V2` | fixture hervalideerd | open PDP op beide hoofdviewports | hoofdpagina rendert zonder crash | `FAIL/REGRESSION` | route, commit, viewport, screenshot/log | J | J | N | N | J | NEE | GATE D/E | UNEXECUTED |
| `SMK-PDP-002` | Titel prijs merkidentiteit | L1 | product/PDP | buybox | `FIX-PDP-NO-V2` | snapshotidentiteit beschikbaar | vergelijk zichtbare identiteit binnen dezelfde route | titel/merk en werkelijk aanwezige prijsvelden zijn intern coherent | `FAIL/REGRESSION`; ontbrekende bron niet invullen | veldbewijs en screenshot/log | J | J | N | N | N | NEE | GATE D/E | UNEXECUTED |
| `SMK-PDP-003` | PDP media | L2 | product/media | gallery/modal | `FIX-PDP-NO-V2` | media aanwezig | navigeer zichtbare media zonder download/upload | controls en geselecteerde media werken binnen oppervlak | `FAIL/REGRESSION` of `FIXTURE_INVALID` | media-aantal, controls, screenshot/log | J | J | J | N | J | NEE | GATE D/E | UNEXECUTED |
| `SMK-PDP-004` | Productformulier en buy action | L1 | product/PDP/cart | product form | `FIX-CART-ONE-ITEM` | veilige beschikbare variant en lege cart | selecteer zo nodig variant; voeg één item toe | geldige request en cartfeedback; geen checkout | `FAIL/REGRESSION` of `FIXTURE_INVALID` | variant, response, cartstate, screenshot/log | J | J | J | N | J | NEE | GATE D/E plus mutatietoestemming | UNEXECUTED |
| `SMK-PDP-005` | V2-switcher | L1 | switcher/PDP | `bc-product-switcher` | `FIX-PDP-V2` | veld en asset-overlap hervalideerd | inspecteer groepen; activeer één veilige navigatieoptie | huidige productstatus en doelroute coherent; geen cartmutatie | `FAIL/REGRESSION` of `FIXTURE_INVALID` | groep, handles, route, screenshot/log | J | J | J | N | J | NEE | GATE D/E | UNEXECUTED |
| `SMK-PDP-006` | Product zonder V2 | L2 | switcher/PDP | reguliere buybox | `FIX-PDP-NO-V2` | V2 en legacytrigger leeg bewezen | open product en inspecteer buybox | geen V2-UI; reguliere PDP blijft bruikbaar | `FAIL/REGRESSION` of `FIXTURE_INVALID` | metafieldbewijs, route, screenshot/log | J | J | J | N | N | NEE | GATE D/E | UNEXECUTED |
| `SMK-PDP-007` | Specificatiegebied | L2 | product/PDP | specificaties/accordions | `FIX-PDP-NO-V2` | product met daadwerkelijk aanwezige specificatievelden | inspecteer/bedien zichtbare specificatiecontrols | aanwezige labels/waarden en controls renderen zonder crash | `FAIL/REGRESSION` of `FIXTURE_INVALID` | veldpresence en screenshot/log | J | J | J | N | N | NEE | GATE D/E | UNEXECUTED |
| `SMK-PDP-008` | Related products | L2 | product/recommendations | `related-products` | `FIX-PDP-NO-V2` | aanbevelingen bereikbaar of lege state toegestaan | observeer response en open één veilige kaart indien aanwezig | aanwezige kaarten coherent; lege state veilig | `FAIL/REGRESSION`, `BLOCKED/ENVIRONMENT_MISMATCH` | request/state en screenshot/log | J | J | J | N | J | NEE | GATE D/E | UNEXECUTED |
| `SMK-PDP-009` | Product structured data | L2 | structured data | Product JSON-LD | `FIX-PDP-NO-V2` | PDP geladen in geautoriseerde runtime | lees JSON-LD, parse en vergelijk identiteit/URL/aanwezige prijs | geldige JSON; identiteit en URL coherent; geen onbewezen voorraadclaim | `FAIL/REGRESSION` of `NEEDS_HUMAN_REVIEW` | raw object/hash, parse-uitvoer, basisdelta | J | J | N | J | N | NEE | GATE D/E/F | UNEXECUTED |
| `SMK-SWITCH-001` | V2 asset en navigatiecoherentie | L2 | switcher | V2-data/links | `FIX-PDP-V2` | exacte assetgroep en productset hervalideerd | vergelijk gerenderde keuzes met groep; volg één GET-link | geen onverwachte ontbrekende/onjuiste keuze binnen fixture | `FAIL/REGRESSION` of `FIXTURE_INVALID` | asset-/veldhash, keuze- en routelog | J | J | J | N | J | NEE | GATE D/E | UNEXECUTED |
| `SMK-SWITCH-002` | Legacy-switchergrens | L2 | legacy switcher | legacy `custom.group`-pad | geen geldige fixture | aparte veilige fixture ontbreekt | niet uitvoeren totdat fixture expliciet is geautoriseerd | toekomstig resultaat blijft `BLOCKED/FIXTURE_INVALID`; geen activatie | `BLOCKED/FIXTURE_INVALID` | bewijs 0/7.827 plus stoplog | J | J | J | N | N | NEE | nieuwe taak/gate vereist | UNEXECUTED |
| `SMK-CART-001` | Lege cart | L1 | cart | `/cart` | `FIX-CART-EMPTY` | geïsoleerde lege sessie | open cart zonder wijziging | lege state en navigatie renderen zonder crash | `FAIL/REGRESSION` | sessiestate, route, screenshot/log | J | J | J | N | J | NEE | GATE D/E | UNEXECUTED |
| `SMK-CART-002` | Add-to-cart naar notification | L1 | PDP/cartfeedback | product form/notification | `FIX-CART-ONE-ITEM` | expliciete ephemeral-mutatie toegestaan | voeg exact één veilig item toe; open geen checkout | notification toont coherente itemstatus en cartlink | `FAIL/REGRESSION` of `FIXTURE_INVALID` | request/response, notification, cartcount | J | J | J | N | J | NEE | GATE D/E plus mutatietoestemming | UNEXECUTED |
| `SMK-CART-003` | Cart met één item | L1 | cart | `/cart` | `FIX-CART-ONE-ITEM` | één tijdelijke regel | open cart en vergelijk product/variant/hoeveelheid | exact één coherente regel; checkout niet activeren | `FAIL/REGRESSION` | cartstate en screenshot/log | J | J | J | N | J | NEE | GATE D/E plus mutatietoestemming | UNEXECUTED |
| `SMK-CART-004` | Hoeveelheid wijzigen en verwijderen | L1 | cart controls | cart item | `FIX-CART-ONE-ITEM` | één tijdelijke regel en toestemming | wijzig hoeveelheid binnen veilige grens; verwijder; eindig leeg | totals/state verversen; tijdelijke state opgeruimd | `FAIL/REGRESSION` of `BLOCKED/ENVIRONMENT_MISMATCH` | request/statevolgorde en eindstate | J | J | J | N | J | NEE | GATE D/E plus mutatietoestemming | UNEXECUTED |
| `SMK-TILE-001` | Bestaand tegelproduct zonder calculator | L2 | tegel/PDP | reguliere PDP | `FIX-PDP-TILE` | tile-fixture hervalideerd | open product zonder calculatoractie | reguliere PDP rendert; geen calculator wordt verwacht of verzonnen | `FAIL/REGRESSION` of `FIXTURE_INVALID` | type, route, screenshot/log | J | J | N | N | N | NEE | GATE D/E | UNEXECUTED |
| `SMK-TILE-002` | Reguliere PDP blijft onafhankelijk | L2 | tegel/PDP | buybox en media | `FIX-PDP-TILE` | geen geautoriseerde calculatorfunctie | inspecteer bestaande zichtbare PDP-controls | ontbreken calculator breekt bestaande PDP niet | `FAIL/REGRESSION`; geen featureclaim | controlinventaris en screenshot/log | J | J | J | N | N | NEE | GATE D/E | UNEXECUTED |
| `SMK-CONTENT-001` | Glossary index | L2 | content | begrippenlijst | `FIX-GLOSSARY` | indexroute hervalideerd | open index en inspecteer termlinks | index rendert en aanwezige links zijn veilige GET-routes | `FAIL/REGRESSION` | route, linksteekproef, screenshot/log | J | J | J | N | N | NEE | GATE D/E | UNEXECUTED |
| `SMK-CONTENT-002` | Glossary detail | L2 | content | begrippendetail | `FIX-GLOSSARY` | concrete bestaande detailroute geselecteerd | open detail vanaf index | detailtemplate en terug-/navroute coherent | `FAIL/REGRESSION` of `FIXTURE_INVALID` | route/template en screenshot/log | J | J | J | N | N | NEE | GATE D/E | UNEXECUTED |
| `SMK-CONTENT-003` | Contact zonder verzending | L2 | content/formuliergrens | contactpagina | n.v.t. | anonieme sessie | open pagina; inspecteer labels/controls; verstuur niets | pagina en formcontrols renderen; nul write | `FAIL/REGRESSION` | screenshot/controlinventaris; geen payload | J | J | J | N | N | NEE | GATE D/E | UNEXECUTED |
| `SMK-CONTENT-004` | 404 | L2 | content/error | 404 | `FIX-404` | slug als niet-bestaand hervalideerd | open synthetische route | 404-template rendert zonder gevoelige data of crash | `FAIL/REGRESSION` of `FIXTURE_INVALID` | URL/status/template/screenshot | J | J | J | N | N | NEE | GATE D/E | UNEXECUTED |
| `SMK-ACCOUNT-001` | Anonieme account-entry | L2 | accountgrens/header | accountlink | `FIX-ACCOUNT-ANON` | anoniem; nieuwe-accountmodel hervalideerd | inspecteer link en volg alleen publieke entryroute | linkbestemming bereikbaar of verklaard; geen login/klantdata | `FAIL/REGRESSION` of `BLOCKED/ENVIRONMENT_MISMATCH` | link, redirect/status, geen accountinhoud | J | J | J | N | N | NEE | GATE D/E | UNEXECUTED |
| `SMK-RESP-001` | Mobiele referentie | L2 | CSS/responsive | geraakt oppervlak | passende fixture | `VP-MOBILE` toegestaan | voer verplichte impactgroep op 375px uit | geen regressie binnen getest oppervlak; geen supportclaim | `FAIL/REGRESSION` | viewport, route, screenshot/log | J | N | volgens case | N | J | NEE | GATE D/E | UNEXECUTED |
| `SMK-RESP-002` | Desktopreferentie | L2 | CSS/responsive | geraakt oppervlak | passende fixture | `VP-DESKTOP` toegestaan | voer verplichte impactgroep op 1280px uit | geen regressie binnen getest oppervlak; geen supportclaim | `FAIL/REGRESSION` | viewport, route, screenshot/log | N | J | volgens case | N | J | NEE | GATE D/E | UNEXECUTED |
| `SMK-RESP-003` | Breakpointgrens 749/750 | L2 | CSS/responsive | geraakt oppervlak | passende fixture | grensset proportioneel vereist | vergelijk dezelfde state op 749px en 750px | bedoelde omslag zonder verborgen primaire control/overlap | `FAIL/REGRESSION` | beide viewports en visuele/logdelta | J | J | volgens case | N | J | NEE | GATE D/E | UNEXECUTED |
| `SMK-KEYBOARD-001` | Header keyboard | L2 | toegankelijkheid | header/menu | n.v.t. | toetsenbordinput | doorloop primaire headercontrols | logische volgorde, zichtbare focus, sluiting bereikbaar | `FAIL/REGRESSION` | focusroute en screenshot/log | J | J | J | N | N | NEE | GATE D/E | UNEXECUTED |
| `SMK-KEYBOARD-002` | Search keyboard | L2 | toegankelijkheid | search/predictive | `FIX-SEARCH-RESULTS` | term en feature hervalideerd | bedien input, suggesties en submit zonder muis | controlstate en focus blijven coherent | `FAIL/REGRESSION` | keys, focusroute, state | J | J | J | N | N | NEE | GATE D/E | UNEXECUTED |
| `SMK-KEYBOARD-003` | PDP-controls keyboard | L2 | toegankelijkheid | PDP media/options/buy | `FIX-PDP-NO-V2` | controls zichtbaar | tab en activeer read-only controls; buy alleen met aparte toestemming | geen onbereikbare zichtbare control binnen scope | `FAIL/REGRESSION` | controllijst/focusroute | J | J | J | N | N | NEE | GATE D/E | UNEXECUTED |
| `SMK-KEYBOARD-004` | Cart-controls keyboard | L2 | toegankelijkheid | notification/cart | `FIX-CART-ONE-ITEM` | ephemeral-state toegestaan | open/close notification en bedien cartcontrols | focus herstelt/logisch; controls bereikbaar | `FAIL/REGRESSION` | focus- en statelog | J | J | J | N | N | NEE | GATE D/E plus mutatietoestemming | UNEXECUTED |
| `SMK-KEYBOARD-005` | Zichtbare interactieve wijziging | L2 | taakspecifieke UI | gewijzigd component | passende fixture | wijzigingsoppervlak heeft zichtbare controls | inventariseer en bedien alleen die controls met toetsenbord | nieuwe/gewijzigde controls bereikbaar en focus zichtbaar | `FAIL/REGRESSION` | impactlijst, focusroute, screenshot/log | J | J | J | N | N | NEE | GATE D/E | UNEXECUTED |
| `SMK-PERF-001` | Minimaal performancebewijs | L2 | performance-impact | geraakte route | passende fixture | meettool later goedgekeurd | meet cold/warm waar relevant zonder budgetclaim | velden volledig; verschillen gerapporteerd, geen verzonnen norm | `BLOCKED/TOOLING_FAILURE` of `NEEDS_HUMAN_REVIEW` | velden uit sectie 31 | J | J | N | N | J | NEE | GATE D/E/F | UNEXECUTED |

Laagverdeling: L0 = 7, L1 = 17, L2 = 29; totaal = 53.

## 17. Homepage

`SMK-HOME-001` t/m `003` scheiden basisrender, zichtbare navigatie-ingangen en lege/optionele targets. Lege ingestelde links of collectievelden worden niet stil als defect of succes geclassificeerd: eerst basisbewijs, daarna `PRE_EXISTING` of `NEEDS_HUMAN_REVIEW`.

## 18. Header en navigation

`SMK-HEADER-001` t/m `004` dekken desktopheader, mobile drawer, primaire toetsenbordroute en dode-focuscontrole. Account en cart blijven binnen hun eigen privacy-/mutatiegrenzen.

## 19. Collection en product cards

`SMK-COLL-001` t/m `004` dekken default, category landing, grid/kaart en de conditionele filter-/sorteringsbasis. Filter/sort wordt `BLOCKED/FIXTURE_INVALID` wanneer de gekozen fixture geen bruikbare facets heeft.

## 20. Search en predictive search

`SMK-SEARCH-001` t/m `004` gebruiken uitsluitend niet-persoonlijke termen. Predictive search is statisch bereikbaar bewezen, maar responsegedrag blijft `UNEXECUTED`.

## 21. Productpagina

`SMK-PDP-001` t/m `009` dekken render, identiteit, media, buy action, V2, geen-V2, specificaties, related products en structured data. Prijs, voorraad en levertijd worden alleen getoetst tegen werkelijk aanwezige en bevoegde bronnen; deze baseline verzint geen waarheid.

## 22. V2-switcher

Lokale code bewijst het pad `custom.switch_group` → `bc-product-switcher`; het bestaande snapshot bewijst 3.658 niet-lege velden en een V2-asset met groepen/handles. Geen concrete product-metafield/asset-overlap is in deze taak runtime bewezen. `FIX-PDP-V2` en `SMK-PDP-005`/`SMK-SWITCH-001` vereisen daarom hervalidatie.

## 23. Legacy-switchergrens

Legacycode bestaat en is statisch vanuit `main-product` bereikbaar, maar het bestaande Adminsnapshot rapporteert `custom.group = 0/7.827`; huidige legacy-UI-activatie is niet bewezen. Er wordt geen legacyfixture verzonnen, geen productdata aangepast en niets geactiveerd. `SMK-SWITCH-002` blijft bij toekomstige uitvoering `BLOCKED` en/of `FIXTURE_INVALID` totdat een aparte expliciet geautoriseerde veilige fixture bestaat.

## 24. Cart

`SMK-CART-001` is read-only bij een lege geïsoleerde sessie. `SMK-CART-002` t/m `004` vereisen later afzonderlijke toestemming voor `EPHEMERAL_STOREFRONT_STATE`, gebruiken één niet-persoonlijk hervalideerd product en eindigen zonder checkout of bestelling.

## 25. Tegelproduct

De snapshot bewijst een bestaand mozaïektegelproductkandidaat. De twee tilecases toetsen alleen dat het reguliere PDP-pad niet breekt; zij specificeren, activeren of simuleren geen tegelcalculator en verzinnen geen m²-regels.

## 26. Accountgrens

Alleen de anonieme publieke account-entry/linkstatus valt binnen het ontwerp. Geen login, accountaanmaak, klantprofiel, orderhistorie, adres, e-mail of andere persoonsdata wordt gebruikt of gelezen.

## 27. Content glossary contact en 404

Glossary index/detail en 404 zijn veilige GET-ontwerpen. De contactpagina mag later alleen worden bekeken en met toetsenbord worden geïnventariseerd; invullen of verzenden is `WRITE_OR_TRANSACTIONAL` en blijft buiten scope.

## 28. Responsive

Responsive cases gebruiken alleen de drie voorgestelde viewportklassen wanneer hun wijzigingsoppervlak dit vereist. De 749/750-grens is optioneel en proportioneel; 989/990 kan later bij concrete code-impact aanvullend worden gekozen. Geen matrixrij beweert volledige device-, OS- of browserdekking.

## 29. Toetsenbord

Header, search, PDP, cart en ieder zichtbaar gewijzigd interactief oppervlak hebben een afzonderlijke keyboardcase. Minimaal bewijs omvat inputmethode, focusvolgorde, zichtbare focus, openen/sluiten en iedere dode route binnen het geteste oppervlak.

## 30. Structured data

Lokale code bewijst `{{ product | structured_data }}` binnen `application/ld+json` in `sections/main-product.liquid` en `canonical_url` in `layout/theme.liquid`. Een latere read-only storefrontcontrole moet minimaal JSON geldig parsen, productidentiteit en URL/canonicalrelatie vergelijken, prijsvelden alleen toetsen indien werkelijk aanwezig en de output tegen de basis vergelijken. Voorraad of levertijd wordt zonder aparte databron niet juist verklaard. De storefrontcontrole is niet uitgevoerd.

## 31. Performancebewijs

Er is geen budget of milliseconden-/Core Web Vitals-doel gekozen. Later minimaal vastleggen: route, basiscommit, viewportklasse, cold/warm state waar relevant, requestcount, transferred/resource size waar tooling betrouwbaar meet, grote switcherasset geladen ja/nee, console errors, meettool, toolversie en datum. Afwijkingen vragen menselijke interpretatie.

## 32. Failureclassificatie

Resultaatstaten:

- `PASS`: alleen na werkelijk uitgevoerde, volledig bewezen testcase.
- `FAIL`: verwacht resultaat niet gehaald.
- `BLOCKED`: uitvoering of beoordeling kon niet geldig plaatsvinden; nooit `PASS`.
- `NOT_RUN`: niet uitgevoerd; nooit `PASS`.
- `NOT_APPLICABLE`: aantoonbaar niet relevant voor het goedgekeurde wijzigingsoppervlak.

Technische oorzaaklabels: `REGRESSION`, `PRE_EXISTING`, `TOOLING_FAILURE`, `FIXTURE_INVALID`, `ENVIRONMENT_MISMATCH`, `NEEDS_HUMAN_REVIEW`. `PRE_EXISTING` vereist bestaand basisbewijs; een onbekende fixture of onverwachte afwijking wordt nooit stil als baseline of succes geaccepteerd. Binnen BC-TECH-005 zijn alle functionele runtimecases `UNEXECUTED`/`NOT_RUN`, niet `PASS`.

## 33. Mutatie- en privacymatrix

| Toekomstige actie | Classificatie | Regel |
| --- | --- | --- |
| Gewone publieke pagina-GET | `READ_ONLY` | toegestaan alleen in later geautoriseerde runtime |
| Publieke search | `READ_ONLY` | uitsluitend niet-persoonlijke term |
| Switchernavigatie | `READ_ONLY` | alleen veilige GET en hervalideerde fixture |
| Add-to-cart | `EPHEMERAL_STOREFRONT_STATE` | aparte toestemming; geïsoleerde sessie; geen checkout |
| Cart quantity/verwijderen | `EPHEMERAL_STOREFRONT_STATE` | tijdelijke state herstellen naar leeg |
| Contactformulier verzenden | `WRITE_OR_TRANSACTIONAL` | buiten scope |
| Checkout/order | `WRITE_OR_TRANSACTIONAL` | verboden binnen deze baseline en uitvoering |
| Login/customer/order history | `PERSONAL_DATA` | verboden |
| Offerteupload | `WRITE_OR_TRANSACTIONAL` plus mogelijk `PERSONAL_DATA` | verboden zonder afzonderlijke taak en privacykader |

BC-TECH-005 zelf voerde uitsluitend lokale read-only analyse en documentatie uit.

## 34. Change-impactmatrix

| Wijzigingscategorie | Verplichte testcasegroepen | Proportionele uitbreiding |
| --- | --- | --- |
| Header/navigation | L0; HEADER-L1; HOME-navigatie | relevante keyboard, mobile/desktop en account-entry L2 |
| Homepage | L0; HOME-L1 | header, responsive, keyboard en performance alleen bij impact |
| Collection/product card | L0; COLL default/grid L1 | landing, filter/sort, search, responsive, keyboard |
| Search | L0; SEARCH result L1 | zero, predictive, keyboard, cards, responsive |
| Product/PDP | L0; PDP render/identiteit/buy L1 | media, specs, related, structured data, cart en responsive volgens diff |
| Switcher | L0; PDP V2 L1 | V2-coherentie, geen-V2; legacy alleen met geldige fixture |
| Cart | L0; CART-L1 | keyboard/responsive/performance volgens diff; nooit checkout |
| CSS/responsive | L0; geraakte kritieke L1 op mobiel en desktop | grensviewport en keyboard voor geraakte controls |
| Structured data | L0; relevante route-L1 | `SMK-PDP-009`, parser/delta en menselijke review |
| Globale layout | L0; brede relevante HOME/HEADER/COLL/PDP/CART L1 | responsive, keyboard, search en performance volgens impact |
| Locale/content | L0; geraakte route/contentcase | keyboard bij controltekst; geen volledige site zonder reden |
| Tooling-only | L0 | geen browserclaim; L1/L2 alleen als tooling runtimegedrag beïnvloedt |
| Documentatie-only | documentvalidator, whitelist en `git diff --check` | geen browserclaim en geen functionele `PASS` |

Een kleine PDP-codewijziging vereist L0 plus relevante PDP-L1/L2, niet automatisch de hele site. Een globale layout-/CSS-wijziging vereist een bredere kritieke L1 en gerichte responsive/keyboard-L2.

## 35. Minimaal bewijs per uitgevoerde testcase

Later minimaal: resultaat `PASS/FAIL/BLOCKED/NOT_RUN/NOT_APPLICABLE`, basiscommit, testcase-ID, fixture-ID, route, viewportklasse, inputmethode, feitelijk resultaat, screenshot-/logverwijzing waar van toepassing, datum en reviewer. Aanvullend worden tool/versie en technische oorzaak vastgelegd. Een screenshot alleen is geen volledig bewijs.

## 36. Relatie met Theme Check

BC-TECH-003 blijft de verplichte L0 pre-/postgate voor theme-code. Nieuwe, uitgebreidere of ernstigere fingerprints zijn regressiesignalen. Geen suppressie of stille rebaseline zonder afzonderlijke menselijke goedkeuring; functionele cases vervangen Theme Check niet en Theme Check vervangt runtimebewijs niet.

## 37. Relatie met technical change workflow

Iedere latere uitvoering erft het goedgekeurde branchmodel, de exacte basiscommit, whitelist, rollback en afzonderlijke gates A-G uit `docs/TECHNICAL_CHANGE_WORKFLOW.md`. Deze baseline verleent geen GATE A, B, C, D, E, F of G en autoriseert geen branch, push, preview, merge of release.

## 38. Relatie met PROPOSED-TECH-12

`PROPOSED-TECH-12` blijft afzonderlijk en niet-officieel. BC-TECH-005 definieert alleen minimale bewijsvelden. Het beslist niet over opslagarchitectuur voor grote artefacten, bewaartermijn, binary-retentie, screenshotrepository, centrale testdatabase of CI-artifactopslag.

## 39. Toekomstige runtime-uitvoeringsvoorwaarden

Voor runtime zijn minimaal nodig: officiële taak-ID en `READY`, exacte scope/whitelist, menselijke GATE A/B, bekende basiscommit, geldige fixtures, goedgekeurde tool en viewports, actuele read-only targetcontrole vóór eventuele preview, privacy-/mutatietoestemming, L0-pregate en stop-/rollbackplan. Developmentpreview vraagt afzonderlijk GATE C/D; acceptatie vraagt GATE E. Live en verboden themes blijven uitgesloten.

Stop onmiddellijk bij verkeerde branch/basis/target, ongeldige fixture, persoonsgegevens, onverwachte write/transaction, checkout-/orderrisico, nieuwe Theme Check-regressie, onverwachte remote drift, gevoelige logdata, environment mismatch of niet-geautoriseerde scope-uitbreiding.

## 40. Open beslissingen

- Exact runtimeframework/tool: open; gerichte lokale inventaris vond geen betrouwbaar aanwezige browser-/test-/CI-tooling. Niets is geïnstalleerd.
- Menselijke goedkeuring van matrix, fixtureselectie, viewportvoorstellen, browsermatrix, testlagen en runtimegrenzen.
- Concrete V2-, geen-V2-, default-collection- en glossary-detailfixtures na actuele read-only hervalidatie.
- Wanneer 989/990 als extra grensset verplicht wordt.
- Artefactopslag en retentie blijven bij het afzonderlijke `PROPOSED-TECH-12`.

## 41. Risico's

- Een ontwerpmatrix kan ten onrechte als functioneel bewijs worden gelezen; daarom staat overal `UNEXECUTED`.
- Historische snapshots kunnen verouderen; fixturehervalidatie is verplicht.
- Statische bereikbaarheid bewijst geen render of interactie.
- V2-fieldcoverage en assetgroepen bewijzen zonder overlapcontrole geen geldige productfixture.
- Legacy kan onveilig worden geactiveerd als het nulbewijs wordt genegeerd.
- Referentieviewports kunnen ten onrechte als supportmatrix of performancebudget worden gebruikt.
- Tijdelijke cartstate kan mutatief worden; afzonderlijke toestemming en opruiming zijn vereist.

## 42. Aanbevolen volgende stap

De projecteigenaar beoordeelt deze `REVIEW`-baseline, met name de 12 fixtureklassen, drie viewportklassen, L0/L1/L2-verdeling, 53 testcases, change-impactmatrix en toekomstige privacy-/mutatiegrenzen. Pas na expliciete goedkeuring kan BC-TECH-005 naar `DONE`; runtime-uitvoering vereist daarna een afzonderlijke officiële taak en toestemming.

## 43. Veiligheidsbevestiging

Binnen BC-TECH-005 is geen browser, developmentserver, preview, Shopify Admin, Shopify CLI store-/themecommando, product/cart/account-runtime, package-installatie, branch, theme push/pull/publicatie of theme-codewijziging uitgevoerd. Geen persoonsgegevensfixture is gemaakt. Alle runtimecases blijven `UNEXECUTED`; fase B blijft lokaal, ongecommit en ongepusht.

## 44. Menselijke goedkeuring

De BadkamerCity-projecteigenaar heeft `BC-TECH-005` en deze smoke-/regressiebaseline op 2026-08-16 definitief goedgekeurd binnen de vastgelegde niet-runtime/documentatiescope.

De goedkeuring omvat de 16 routeklassen; 7 lokaal bewezen width-breakpoints (`479px`, `749px`, `750px`, `900px`, `989px`, `990px` en `1199px`); 3 voorgestelde referentieviewportklassen; 12 privacyveilige fixtureklassen; 53 unieke testcases met verdeling L0=7, L1=17 en L2=29; de proportionele change-impactmatrix; en de failure-, privacy- en mutatiegrenzen. De drie viewports blijven testreferenties en vormen geen volledige browser- of apparaatsupportmatrix. Iedere concrete fixture vereist voor toekomstige uitvoering nieuwe read-only hervalidatie en persoonsgegevens blijven verboden.

De legacy-switcher krijgt geen verzonnen fixture en blijft voor runtime `BLOCKED`/`FIXTURE_INVALID` totdat een veilige fixture afzonderlijk is geautoriseerd. De structured-data-controles zijn niet uitgevoerd; voorraad- of levertijdjuistheid wordt daaruit niet zonder aparte betrouwbare databron afgeleid. De performancebewijsvelden zijn goedgekeurd zonder performancebudget, Core Web Vitals-doel of millisecondennorm. De exacte browser-/runtime-tool blijft een open beslissing.

Er is geen functionele test uitgevoerd en alle eerdere runtimecases bleven `UNEXECUTED`. Deze goedkeuring accepteert het ontwerp; zij bewijst niet dat een storefrontjourney functioneert. Iedere toekomstige runtime-, browser-, preview- of mutatiehandeling vereist een afzonderlijke officiële taak en expliciete menselijke toestemming. Zij geeft evenmin algemene branch-, merge-, release-, Shopify- of theme-codebevoegdheid.
