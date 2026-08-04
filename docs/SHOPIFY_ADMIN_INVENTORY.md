# Shopify Admin Inventory

Onderzoeksdatum: 2026-08-04
Taak: `BC-ADM-001`
Store: `fpa9hu-i3.myshopify.com`
Uitkomst: `BLOCKED` door ontbrekende Shopify Admin API-readtoegang
Scope: uitsluitend read-only onderzoek; geen klanten- of orderinhoud opgevraagd

## 1. Managementsamenvatting

De bestaande Shopify CLI-sessie kan de theme-omgeving van de juiste store lezen. Op 2026-08-04 bevestigde `shopify theme list` opnieuw dat `Categoriepagina_v1.0` (`189463068938`) live staat en dat `BadkamerCity Development` (`192770375946`) unpublished is.

Er is in deze repository echter geen Shopify-appconfiguratie, geen zichtbare Admin API-tokenvariabele en geen beschikbare Shopify Admin-connector. Een minimale read-only Admin GraphQL-query via `shopify app execute` kon daardoor niet worden uitgevoerd: de CLI stopte omdat `shopify.app.toml` ontbreekt. Er is geen app aangemaakt of gekoppeld, er zijn geen rechten of scopes aangevraagd en er is geen alternatieve toegang geconstrueerd.

Daarom zijn de werkelijke Admin-aantallen, definities, waarden, toewijzingen en instellingen niet verantwoord vast te stellen. De taak blijft `BLOCKED`. De tijdgebonden live-theme-snapshot levert wel bruikbaar ondersteunend bewijs over verwachte metafields, templatebestanden, menu-handles en afwezigheid van geconfigureerde app-block-URL's, maar bewijst niet dat de bijbehorende Admin-objecten bestaan of actief zijn.

## 2. Statuslabels

- **BEWEZEN:** rechtstreeks vastgesteld met een genoemde bron en datum.
- **NIET TOEGANKELIJK:** de benodigde read-only Admin-bron was in deze uitvoeringscontext niet beschikbaar.
- **NOG ONDERZOEKEN:** kan pas na geldige read-only toegang of aanvullend bewijs worden vastgesteld.
- **OPEN BESLISSING:** vereist een expliciete keuze van de projecteigenaar of bevoegde beheerder.

Afwezigheid in theme-code of CLI-uitvoer wordt nergens als afwezigheid in Shopify Admin geïnterpreteerd.

## 3. Randvoorwaarden en uitgevoerde controles

### 3.1 Randvoorwaarden

Tijdens dit onderzoek is:

- geen Shopify Admin-data gewijzigd;
- geen theme-code gewijzigd;
- geen theme gepusht, gepulld, gepubliceerd, hernoemd of verwijderd;
- geen app geïnstalleerd, aangemaakt, gekoppeld of geconfigureerd;
- geen recht of scope aangevraagd;
- geen credential, token of configuratiewaarde getoond;
- geen klant- of orderinhoud opgevraagd;
- geen commit gemaakt en niets naar GitHub gepusht.

### 3.2 Bronnen en methoden

| Bron of controle | Datum | Resultaat | Beperking |
| --- | --- | --- | --- |
| `git status --short --branch` | 2026-08-04 | **BEWEZEN:** startstatus was schoon op `main`, gelijk aan `origin/main` | Alleen Git-werkboom |
| `shopify version` | 2026-08-04 | **BEWEZEN:** Shopify CLI `3.92.1` | Geen bewijs van Admin-scopes |
| `shopify theme info --store fpa9hu-i3.myshopify.com` | 2026-08-04 | **BEWEZEN:** storecontext leesbaar; Development Theme ID niet lokaal ingesteld | Theme-context, geen Admin-inventaris |
| `shopify theme list --store fpa9hu-i3.myshopify.com` | 2026-08-04 | **BEWEZEN:** drie themes en hun rollen leesbaar | Alleen themes en rollen |
| Werkruimtecontrole op `.env*`, `shopify*.toml` en Shopify-configbestanden | 2026-08-04 | **BEWEZEN:** geen toepasselijke bestanden gevonden | Zegt niets over handmatige Admin-toegang van personen |
| Controle van uitsluitend omgevingsvariabelnamen | 2026-08-04 | **BEWEZEN:** geen namen gevonden voor Shopify/Admin/Storefront access tokens | Waarden zijn bewust niet gelezen of getoond |
| `shopify app info --path . --json --no-color` | 2026-08-04 | **BEWEZEN:** faalt omdat de repository geen app-TOML bevat | Geen app gekoppeld om dit te omzeilen |
| Minimale query `shop { id name }` via `shopify app execute --path .` | 2026-08-04 | **BEWEZEN:** vóór uitvoering gestopt wegens ontbrekende app-TOML | Er is geen Admin-data teruggekomen |
| `docs/LIVE_THEME_COMPARISON.md` | 2026-08-03 | **BEWEZEN:** 396 lokale/live themebestanden waren hashgelijk | Tijdgebonden; geen Admin-data |
| Lokale parsing van JSON-themeconfiguratie en statische bronverwijzingen | 2026-08-04 | **BEWEZEN:** hieronder vermelde template-, menu- en metafieldverwachtingen | Bewijst gebruik in de snapshot, niet bestaan/dekking in Admin |
| Officiële Shopify GraphQL Admin API-documentatie | geraadpleegd 2026-08-04 | **BEWEZEN:** benodigde queryfamilies en scopes hieronder | Documentatie bewijst geen verleende storetoegang |

## 4. Beschikbare en ontbrekende toegang

| Domein | Status | Vaststelling |
| --- | --- | --- |
| Shopify CLI theme-identiteit en rollen | **BEWEZEN** | Store en themelijst zijn read-only opvraagbaar |
| Lokale live-theme-snapshot van 2026-08-03 | **BEWEZEN** | Zeven theme-mappen waren toen gelijk aan live theme `189463068938` |
| GraphQL Admin API | **NIET TOEGANKELIJK** | Geen bruikbare Admin-appcontext of zichtbare Admin-tokenvariabele; testquery stopte vóór uitvoering |
| Shopify Admin in een geauthenticeerde browser | **NIET TOEGANKELIJK** | Geen browser-/Admin-connector beschikbaar in deze uitvoeringscontext |
| Producten en collecties | **NIET TOEGANKELIJK** | Geen Admin-query of Admin-export beschikbaar |
| Metafield- en metaobjectdefinities/waarden | **NIET TOEGANKELIJK** | Theme-referenties zijn geen definities of dekkingsbewijs |
| Menu-objecten en linkvaliditeit | **NIET TOEGANKELIJK** | Alleen gebruikte handles zijn lokaal zichtbaar |
| Geïnstalleerde apps, pixels en externe appconfiguratie | **NIET TOEGANKELIJK** | Theme-snapshot kan verborgen Admin-/appafhankelijkheden niet uitsluiten |
| Actieve object-to-template-toewijzingen | **NIET TOEGANKELIJK** | Templatebestanden zijn zichtbaar; toewijzingen aan producten/collecties/pagina's niet |
| Markets, talen, accounts, locaties, voorraad en verzending | **NIET TOEGANKELIJK** | Geen geschikte Admin-readbron aanwezig |

## 5. Bewezen Shopify-omgeving

De actuele read-only themelijst op 2026-08-04 is:

| Theme | ID | Rol |
| --- | ---: | --- |
| `Categoriepagina_v1.0` | `189463068938` | `live` |
| `BadkamerCity V1.0` | `189117628682` | `unpublished` |
| `BadkamerCity Development` | `192770375946` | `unpublished` |

**BEWEZEN:** de repository is gekoppeld aan `fpa9hu-i3.myshopify.com`; deze opdracht heeft live theme `189463068938` niet gewijzigd en de role bleef `live`.
**NOG ONDERZOEKEN:** of iemand na de hashvergelijking van 2026-08-03 via Shopify Admin theme-instellingen of bestanden heeft aangepast. Er is in deze opdracht bewust geen theme-pull of nieuwe parity-check uitgevoerd.

## 6. Producten

**NIET TOEGANKELIJK:** de volgende gevraagde gegevens konden niet uit Shopify Admin worden gelezen:

- totaal aantal producten;
- aantallen per status `ACTIVE`, `DRAFT` en `ARCHIVED`;
- vendors, producttypes en verdeling daarvan;
- gebruikte productsjablonen en aantallen per template suffix;
- aantal producten met alleen de technische standaardvariant versus meerdere varianten;
- totaal aantal varianten en SKU-dekking;
- representatieve productsteekproeven;
- publicatie-/verkoopkanaalstatus;
- dekking van de switcher- en specificatiemetafields.

**BEWEZEN uit het theme, niet uit Admin:** er bestaat alleen `templates/product.json`; er is lokaal geen alternatief `product.*.json`-template. Dit bewijst niet hoeveel producten dit template werkelijk gebruiken.

**BEWEZEN uit bestaand repositoryonderzoek:** `assets/product-switcher-data.json` bevatte op 2026-08-03 433 groepen, 3.383 productrecords en 560 menudefinities. Deze asset is geen Shopify-productexport en mag niet worden gebruikt als Admin-producttelling of dekkingsbewijs.

## 7. Collecties

**NIET TOEGANKELIJK:** niet vastgesteld zijn:

- totaal aantal collecties;
- verdeling handmatig versus geautomatiseerd;
- regels en voorwaarden van geautomatiseerde collecties;
- aantallen producten per collectie;
- publicatiestatus;
- werkelijk toegewezen collectie-template suffixes;
- lege, tijdelijke of overlappende collecties.

**BEWEZEN uit het theme, niet uit Admin:** beschikbaar zijn `collection.json` en alternatief `collection.category-landing.json`. Werkelijk gebruik van het alternatieve template is **NOG ONDERZOEKEN**.

## 8. Metafields

### 8.1 Definities, typen, validaties en dekking

**NIET TOEGANKELIJK:** geen enkele Admin-metafielddefinitie, eigenaar, type, validatie, waarde of productdekking kon worden opgevraagd. Daardoor kan niet worden bevestigd of een theme-referentie:

- als definitie bestaat;
- het door de code verwachte type heeft;
- verplicht of optioneel is;
- geldige validaties heeft;
- op nul, enkele of alle relevante producten is gevuld;
- door een app, medewerker, import of ander systeem wordt beheerd.

### 8.2 Bewezen theme-referenties

De live-theme-snapshot bevat 61 unieke statische `namespace.key`-referenties: 58 onder `custom`, één onder `descriptors` en twee onder `reviews`.

Switcher en productrelaties:

- `custom.switch_group`
- `custom.group` (legacy fallback)
- `custom.switch_key`
- `custom.menu_1` tot en met `custom.menu_5`
- `custom.afmeting`, `custom.afwerking`, `custom.basiskleur`, `custom.frame`, `custom.handdouche`, `custom.hoofddouche`, `custom.hoogte`, `custom.led`, `custom.lengte`, `custom.met_glijstang`, `custom.montage`, `custom.plaatsing`, `custom.type`, `custom.type_bevestiging_hoofddouche`, `custom.type_handdouche` en `custom.vorm`

Productidentiteit en specificaties:

- `custom.artikelnummer`, `custom.fabrikantnummer`, `custom.ean`, `custom.serie`
- `custom.vormgeving_stijlgroep`, `custom.kleurgroep`, `custom.glansgraad`, `custom.materiaal_kraan`, `custom.montagewijze`, `custom.afwerking_greep`
- `custom.belgaqua_keurmerk`, `custom.met_hoofddouche`, `custom.breedte_diameter_hoofddouche`, `custom.dikte_hoofddouche`, `custom.aantal_straalsoorten_hoofddouche`, `custom.lengte_douchearm`
- `custom.met_handdouche`, `custom.breedte_diameter_douchekop`, `custom.aantal_straalsoorten_handdouche`, `custom.met_doucheslang`, `custom.lengte_doucheslang`
- `custom.vorm_thermostaat`, `custom.thermostatisch`, `custom.met_inbouwdeel`, `custom.aantal_uitgangen_tegelijk_bedienbaar`, `custom.bediening_voor_aan_uit`
- `custom.hotbath_ecoair_system`, `custom.hotbath_shower_power_system`, `custom.hotbath_fluhs`, `custom.hotbath_plumber_friendly`

Kaarten, inhoud en standaarden:

- `custom.search_card_spec_1`, `custom.search_card_spec_2`
- `custom.pluspunten`, `custom.aandachtspunten`
- `descriptors.subtitle`
- `reviews.rating`, `reviews.rating_count`

Daarnaast geeft `product.metafields.vendor` in de theme-code alleen een namespace zonder key door als merkveld. Dit is het bestaande risico `BC-R-015`; zonder Admin-data kan niet worden vastgesteld wat hier werkelijk wordt gerenderd.

### 8.3 Specifieke gevraagde velden

| Veld | Theme-snapshot | Admin-definitie/type/dekking |
| --- | --- | --- |
| `custom.switch_group` | **BEWEZEN:** actieve referentie voor de V2-switcher | **NIET TOEGANKELIJK** |
| `custom.switch_options` | **BEWEZEN:** geen statische referentie aangetroffen in de zeven theme-mappen | **NIET TOEGANKELIJK:** bestaan in Admin kan niet worden uitgesloten |
| `custom.group` | **BEWEZEN:** legacy fallbackreferentie | **NIET TOEGANKELIJK** |
| `custom.menu_1` tot en met `custom.menu_5` | **BEWEZEN:** legacy menu-/keuzevelden | **NIET TOEGANKELIJK** |
| overige 51 statische `custom.*`-velden | **BEWEZEN:** theme-referenties zoals hierboven | **NIET TOEGANKELIJK** |

## 9. Metaobjects

**NIET TOEGANKELIJK:** niet vastgesteld zijn:

- aantal metaobjectdefinities;
- definitienamen, types, velden, validaties en capabilities;
- aantallen entries per definitie;
- draft/active of publishable status;
- referenties vanuit producten, collecties, pagina's, menu's of theme-instellingen;
- eigenaarschap door apps of medewerkers.

De afwezigheid van duidelijke statische metaobjectreferenties in het theme is geen bewijs dat metaobjects niet bestaan of niet indirect worden gebruikt.

## 10. Navigatiemenu's

**BEWEZEN uit de live-theme-snapshot:** de configuratie verwijst naar:

- `main-menu` in `sections/header-group.json`;
- `main-menu` in `templates/index.json` voor de homepage-categoriegrid;
- `footer` in twee footerblokken van `sections/footer-group.json`.

**NIET TOEGANKELIJK:** menu-ID's, titels, volledige boomstructuur, diepte, linktypen, resource targets, redirects, tijdelijke URL's, `#`-links en ongeldige doelen konden niet worden gecontroleerd. Het bestaan en de inhoud van de genoemde handles blijven **NOG ONDERZOEKEN**.

## 11. Apps en appafhankelijkheden

**BEWEZEN uit de snapshot van 2026-08-03:** er zijn geen `shopify://apps/...`-referenties gevonden in `assets`, `config`, `layout`, `locales`, `sections`, `snippets` en `templates`. De 15 JSON-templates en beide section groups bevatten geen geconfigureerde app-block-URL.

**BEWEZEN:** acht sections ondersteunen wel `@app`-blokken, waaronder header, footer, product, featured product, article, cart footer en newsletter. `layout/theme.liquid` rendert `content_for_header`, waardoor Shopify of apps scripts kunnen injecteren zonder statische `shopify://apps/...`-referentie.

**NIET TOEGANKELIJK:** een volledige lijst van geïnstalleerde apps, sales channels, app embeds, web pixels, script tags, theme app extensions, abonnementen en externe storefrontafhankelijkheden. Er wordt daarom nadrukkelijk niet geconcludeerd dat er geen apps actief zijn.

De `reviews.*`-metafieldreferenties kunnen op een reviewintegratie wijzen, maar dat is zonder Admin-bewijs slechts **NOG ONDERZOEKEN**.

## 12. Templates en Theme Editor-configuratie

### 12.1 Beschikbare templatebestanden

**BEWEZEN:** de snapshot bevat 16 templatebestanden: 15 JSON-templates en `gift_card.liquid`.

| Templategroep | Beschikbare bestanden |
| --- | --- |
| Product | `product.json` |
| Collectie | `collection.json`, `collection.category-landing.json` |
| Pagina | `page.json`, `page.contact.json`, `page.begrip.json`, `page.begrippenlijst.json` |
| Overig | `404.json`, `article.json`, `blog.json`, `cart.json`, `index.json`, `list-collections.json`, `password.json`, `search.json`, `gift_card.liquid` |

Alle sections in de 15 JSON-templates staan in de snapshot enabled; er zijn geen `disabled: true`-sections aangetroffen. Dit zegt niets over objecttoewijzingen of runtimezichtbaarheid.

### 12.2 Werkelijk gebruik

**NIET TOEGANKELIJK:** niet vastgesteld zijn:

- hoeveel producten, collecties en pagina's ieder template gebruiken;
- of `collection.category-landing`, `page.contact`, `page.begrip` en `page.begrippenlijst` werkelijk aan objecten zijn toegewezen;
- welke sections of blocks via Admin-content zichtbaar/gevuld zijn;
- of app embeds na 2026-08-03 zijn geactiveerd;
- of actuele Theme Editor-instellingen na de live-pariteitssnapshot zijn gewijzigd.

## 13. Markets, talen, accounts, locaties, voorraad, verzending en shopinstellingen

| Onderdeel | Status | Beperking |
| --- | --- | --- |
| Markets en domeinen | **NIET TOEGANKELIJK** | Geen marketnamen, statussen, regio's, valuta of web presences bekend |
| Actieve talen | **NIET TOEGANKELIJK** | Het theme bevat 31 vertaalbestanden, maar dat bewijst geen gepubliceerde shoplocales |
| Klantaccounts/checkoutconfiguratie | **NIET TOEGANKELIJK** | Accountmodel en gepubliceerde configuratie onbekend |
| Locaties | **NIET TOEGANKELIJK** | Aantallen, typen, fulfilmentrol en adressen niet opgevraagd |
| Voorraad | **NIET TOEGANKELIJK** | Inventory items, tracking en niveaus per locatie onbekend |
| Verzending | **NIET TOEGANKELIJK** | Delivery profiles, zones, tarieven, pickup/local delivery en carrier services onbekend |
| Algemene shopinstellingen | **NIET TOEGANKELIJK** | Alleen de myshopify-storecontext is bewezen; relevante configuratie niet |

Geen klant-, order- of persoonsdata is nodig of opgevraagd voor deze inventaris.

## 14. Benodigde read-only toegang

De veilige vervolgstap gebruikt uitsluitend een al bestaande, door de projecteigenaar goedgekeurde read-only route. Tijdens deze taak mag geen app worden gemaakt, geïnstalleerd of uitgebreid.

### 14.1 Voorkeursroute

**OPEN BESLISSING:** de projecteigenaar kiest één van deze bestaande routes:

1. een reeds geïnstalleerde Shopify-app met een Admin API-token en alleen de benodigde read-scopes; of
2. begeleide read-only Shopify Admin-toegang voor de relevante beheeronderdelen; of
3. door een bevoegde beheerder gemaakte Admin-exports en schermafbeeldingen met datum, filters en totalen.

Credentials horen nooit in Git, documentatie, chatuitvoer of commandologs. Bij API-toegang moet eerst met `currentAppInstallation { accessScopes { handle } }` worden bewezen welke scopes al zijn verleend.

### 14.2 Minimale queryfamilies en scopes

| Onderzoek | GraphQL-queryfamilie of Admin-onderdeel | Benodigde read-toegang |
| --- | --- | --- |
| Producten, varianten, SKU's, vendors, types, statussen, collectieleden en template suffixes | `products`, product/variant connections, `collections` | `read_products` |
| Product-/variant-/collectiemetafielddefinities en waarden | `metafieldDefinitions`, resource-metafields | Scope van het owner type; voor deze kernobjecten minimaal `read_products` |
| Metaobjectdefinities | `metaobjectDefinitions` | `read_metaobject_definitions` |
| Metaobjectentries en referenties | `metaobjects` en resource references | `read_metaobjects`, plus scope van verwijzende owner types |
| Navigatiemenu's | `menus` met geneste items en targets | `read_online_store_navigation` |
| Pagina-/blogtargets vanuit navigatie | pages, blogs en articles | `read_online_store_pages` en waar nodig `read_content` |
| Themes, actuele settings en theme app blocks | online store themes/theme files of Admin Theme Editor | `read_themes` of gelijkwaardige read-only Admin-toegang |
| Markets | `markets` | `read_markets` |
| Gepubliceerde talen | `shopLocales` | `read_locales` |
| Locaties | `locations` | `read_locations`; voor volledige inventarisgegevens ook `read_inventory` |
| Voorraad | inventory items en levels | `read_inventory` en `read_locations` |
| Carrier services | shipping/carrier resources | `read_shipping` |
| Delivery profiles, zones en methoden | `deliveryProfiles` plus geneste zones/methoden | geauthenticeerde Admin GraphQL-toegang; benodigde nested resource- en staffrechten eerst met read-only query valideren |
| Checkout- en accountconfiguratie | `checkoutAndAccountsConfigurations` | `read_checkout_and_accounts_configurations` en vereiste staff permission `manage_checkout_settings` |
| Apps, app extensions, embeds en pixels | Admin Apps/sales channels plus relevante installatie-/theme-/pixeloverzichten | expliciete read-only Admin-toegang; zonder zo'n bron geen volledige app-lijst claimen |

Officiële referenties:

- [Shopify API access scopes](https://shopify.dev/docs/api/usage/access-scopes)
- [Productenquery](https://shopify.dev/docs/api/admin-graphql/latest/queries/products)
- [Metafielddefinities](https://shopify.dev/docs/api/admin-graphql/latest/queries/metafieldDefinitions)
- [Metaobjectdefinitie](https://shopify.dev/docs/api/admin-graphql/latest/queries/metaobjectDefinition)
- [Navigatiemenu's](https://shopify.dev/docs/api/admin-graphql/latest/queries/menus)
- [Markets](https://shopify.dev/docs/api/admin-graphql/latest/queries/markets)
- [Shoplocales](https://shopify.dev/docs/api/admin-graphql/latest/queries/shopLocales)
- [Locaties](https://shopify.dev/docs/api/admin-graphql/latest/queries/locations)
- [Delivery profiles](https://shopify.dev/docs/api/admin-graphql/latest/queries/deliveryProfiles)
- [Checkout- en accountconfiguratie](https://shopify.dev/docs/api/admin-graphql/latest/objects/CheckoutAndAccountsConfiguration)

## 15. Gevolgen voor het masterplan

- `BC-ADM-001` blijft actief maar krijgt eindstatus `BLOCKED`; essentiële Admin-bronnen ontbreken.
- `BC-DISC-001` wordt niet geactiveerd en blijft `NOT_STARTED` tot menselijke beoordeling en hervatting/afronding van `BC-ADM-001`.
- `BC-DISC-002` blijft daarna de derde taak in de vaste volgorde.
- `BC-DATA-001` en `BC-SWITCH-001` kunnen metafieldtypes, dekking en migratie niet veilig besluiten.
- `BC-IA-001` kan de werkelijke collectie- en navigatiestructuur niet valideren.
- `BC-LOG-001` en `BC-LOG-002` missen locaties, voorraad en delivery profiles.
- `BC-ACC-001`, `BC-SEC-001` en `BC-ANA-001` missen account-, app-, pixel- en consentconfiguratie.
- `BC-R-008` is nu bewezen geblokkeerd door ontbrekende read-only Admin-toegang, in plaats van alleen algemeen onbekend.

## 16. Open vragen en onzekerheden

1. **OPEN BESLISSING:** welke bestaande read-only route stelt de projecteigenaar beschikbaar?
2. **NOG ONDERZOEKEN:** bestaat er al een geïnstalleerde app met de vereiste scopes die zonder rechtenwijziging mag worden gebruikt?
3. **NOG ONDERZOEKEN:** wie is bevoegd om Admin-totalen, exports en instellingen als leidend te bevestigen?
4. **NOG ONDERZOEKEN:** zijn live theme-instellingen sinds de parity-snapshot van 2026-08-03 gewijzigd?
5. **NOG ONDERZOEKEN:** bestaat `custom.switch_options` in Admin ondanks afwezigheid van een theme-referentie?
6. **NOG ONDERZOEKEN:** welke app of welk proces beheert eventuele `reviews.*`-velden?
7. **NOG ONDERZOEKEN:** welke alternate templates zijn werkelijk toegewezen?
8. **NOG ONDERZOEKEN:** bestaan en werken de menu-handles `main-menu` en `footer` met geldige doelen?

## 17. Veilige vervolgstap

1. Laat de projecteigenaar dit blokkaderapport beoordelen.
2. Laat een bevoegde Shopify-beheerder een reeds bestaande read-only route aanwijzen; maak in deze stap geen app en breid geen scopes uit.
3. Bewijs bij API-gebruik eerst de reeds verleende scopes zonder tokens te tonen.
4. Hervat `BC-ADM-001` met gepagineerde tellingen, definities, representatieve niet-persoonsgebonden samples en een domein-voor-domein querylog.
5. Laat de projecteigenaar de volledige inventaris beoordelen voordat `BC-DISC-001` actief wordt.

## 18. Eindconclusie

- **BEWEZEN:** de theme-CLI-context werkt voor de juiste store; deze opdracht heeft het live theme niet gewijzigd en de role bleef `live`.
- **BEWEZEN:** de tijdgebonden theme-snapshot toont verwachte metafields, templates en menu-handles, maar geen Admin-dekking of toewijzingen.
- **NIET TOEGANKELIJK:** de essentiële Shopify Admin API- en browsergegevens voor alle gevraagde Admin-domeinen.
- **NOG ONDERZOEKEN:** alle werkelijke aantallen, definities, waarden, apps, objecttoewijzingen en instellingen.
- **OPEN BESLISSING:** welke bestaande read-only toegangsroute de projecteigenaar veilig beschikbaar stelt.

Daarom is `BC-ADM-001` `BLOCKED`. Er zijn tijdens het onderzoek geen Shopify-data, theme-code, themes, apps, rechten of publicatiestatussen gewijzigd.
