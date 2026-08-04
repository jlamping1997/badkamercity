# Shopify Admin Inventory

Onderzoeksdatum: 2026-08-04
Taak: `BC-ADM-001`
Store: `fpa9hu-i3.myshopify.com`
Uitkomst: `REVIEW`
Scope: uitsluitend read-only Shopify Admin-onderzoek; geen klanten-, order- of persoonsdata opgevraagd

## 1. Managementsamenvatting

De projecteigenaar heeft de officiële Shopify CLI `store auth`-route aangewezen en dertien read-scopes goedgekeurd. Shopify CLI `4.6.0` heeft deze scopes verleend. Alle uitgevoerde store-operaties waren GraphQL-query's via `shopify store execute`, zonder `--allow-mutations`.

De kerninventaris is nu uitvoerbaar en afgerond binnen de verleende bronnen. De store bevat 7.827 actieve producten, 7.827 varianten, 201 collecties, 117 pagina's, vijf menu's, één productmetafielddefinitie, één metaobjectdefinitie, één actieve markt, één gepubliceerde taal, één locatie en één delivery profile. Er zijn vier themes, waaronder het live theme en drie unpublished themes.

De belangrijkste datakwaliteitsbevindingen zijn:

- 17 varianten hebben geen SKU en 72 niet-lege SKU-waarden komen in meer dan één SKU-groep voor;
- alle producten hebben precies één variant en alle producten staan `ACTIVE`;
- er zijn 649 verschillende producttypewaarden, waaronder 69 keer letterlijk `undefined` en meerdere waarden die op producttitels lijken;
- 199 van de 201 collecties zijn leeg;
- alleen `custom.switch_group` heeft een definitie en meetbare productdekking: 3.658 van 7.827 producten (46,74%);
- `custom.switch_options`, de legacygroep/menuvelden, pluspunten en aandachtspunten hebben geen definitie en kwamen op geen enkel product voor;
- één metaobjectdefinitie `homepage_banner` bestaat, maar heeft nul entries;
- slechts 259 van 7.827 inventory items hebben tracking ingeschakeld;
- het live theme bevat in de actieve JSON-configuratie geen aantoonbare app blocks of app embeds;
- een volledige lijst van geïnstalleerde apps blijft met de verleende scopes **NIET TOEGANKELIJK**.

Deze uitkomst verwijdert de oude algemene Admin-toegangsblokkade, maar is geen implementatie-, datawijzigings-, theme- of publicatietoestemming. `BC-ADM-001` staat op `REVIEW`; `BC-DISC-001` blijft `NOT_STARTED` tot expliciete menselijke goedkeuring.

## 2. Statuslabels

- **BEWEZEN:** rechtstreeks vastgesteld met een genoemde read-only bron op 2026-08-04.
- **NIET TOEGANKELIJK:** niet beschikbaar via de verleende scopes of de gebruikte Shopify-route.
- **NOG ONDERZOEKEN:** aanvullende bronvalidatie, inhoudelijke beoordeling of menselijk eigenaarschap ontbreekt.
- **OPEN BESLISSING:** vereist een expliciete keuze van de projecteigenaar of bevoegde beheerder.

Afwezigheid in theme-code of een beperkte query wordt niet als algemene afwezigheid in Shopify geïnterpreteerd.

## 3. Randvoorwaarden en integriteit

Tijdens dit onderzoek is:

- geen GraphQL-mutatie uitgevoerd;
- `--allow-mutations` nooit gebruikt;
- geen Shopify Admin-data gewijzigd;
- geen theme-code gewijzigd;
- geen theme gepusht, gepulld, gepubliceerd, hernoemd of verwijderd;
- geen aanvullende scope aangevraagd buiten de expliciet goedgekeurde lijst;
- geen credential, token of configuratiewaarde getoond;
- geen klant-, order- of persoonsdata opgevraagd;
- geen volledige productdump opgeslagen;
- geen commit gemaakt en niets naar GitHub gepusht.

De repository was schoon vóór het onderzoek. Alleen dit rapport en `docs/MASTERPLAN.md` worden als taakdocumentatie gewijzigd.

## 4. Toegang en tooling

### 4.1 Shopify CLI

| Onderdeel | Resultaat |
| --- | --- |
| Shopify CLI | `4.6.0` |
| Autorisatieroute | `shopify store auth` |
| Store | `fpa9hu-i3.myshopify.com` |
| Uitvoering | `shopify store execute` met `--json` |
| Mutatietoestemming | Niet verleend en niet gebruikt |

### 4.2 Toegekende scopes

De query `currentAppInstallation { accessScopes { handle } }` bewees exact deze read-scopes:

- `read_products`
- `read_metaobject_definitions`
- `read_metaobjects`
- `read_online_store_navigation`
- `read_online_store_pages`
- `read_content`
- `read_themes`
- `read_markets`
- `read_locales`
- `read_locations`
- `read_inventory`
- `read_shipping`
- `read_checkout_and_accounts_configurations`

**BEWEZEN:** er stond geen write-scope in `currentAppInstallation.accessScopes`.

### 4.3 Gebruikte queryfamilies

| Domein | Queryfamilie | Paginatie/gebruik |
| --- | --- | --- |
| Scopes | `currentAppInstallation` | Eenmalige scopecontrole |
| Producten | `products` | 32 pagina's van maximaal 250 |
| Varianten/SKU | `productVariants` | 32 pagina's van maximaal 250 |
| Collecties | `collections` | Eén volledige pagina |
| Metafielddefinities | `metafieldDefinitions` | `PRODUCT`, `PRODUCTVARIANT`, `COLLECTION`, `PAGE`, `SHOP` |
| Metafielddekking | `products` plus gerichte `metafield`-velden | 87 pagina's van maximaal 90; exact over alle producten |
| Specificatiesteekproef | `products` plus `metafields(namespace: "custom")` | 40 unieke producten via vijf sorteerassen en beide richtingen |
| Metaobjects | `metaobjectDefinitions`, `metaobjects` | Alle definities en entries per type |
| Navigatie | `menus` | Alle menu's en items tot de volledige aanwezige diepte |
| Pagina's | `pages` | Eén volledige pagina |
| Themes/configuratie | `themes`, `theme.files` | Alle themes; 396 live bestanden in twee pagina's; gerichte JSON-inhoud |
| Markets/talen | `markets`, `shopLocales` | Volledig binnen de aanwezige aantallen |
| Accounts | `shop.customerAccountsV2`, `checkoutAndAccountsConfigurations` | Actief model en gepubliceerde configuratie |
| Locaties/voorraad | `locations`, `inventoryItems`, `inventoryLevels` | Exacte itemtelling plus niveausteekproef |
| Verzending | `deliveryProfiles`, `carrierServices` | Alle profiles, zones, methoden en carrier services |

De Shopify-plugin is gebruikt om de queryfamilies tegen het Admin GraphQL-schema te zoeken en te valideren. Een te ruime delivery-profilequery werd vóór datalezing afgewezen op querykost 2.609; dezelfde read-only query is daarna met kleinere pagina's uitgevoerd. Tijdelijke lege CLI-fouten tijdens lange paginaties zijn uitsluitend met dezelfde query, vertraging en beperkte retries herhaald.

## 5. Producten en varianten

### 5.1 Totalen en status

| Kenmerk | Aantal |
| --- | ---: |
| Producten | 7.827 |
| `ACTIVE` | 7.827 |
| `DRAFT` | 0 |
| `ARCHIVED` | 0 |
| Varianten | 7.827 |
| Producten met precies één variant | 7.827 |
| Producten met meer dan één variant | 0 |
| Producten met default/leeg template suffix | 7.827 |

**BEWEZEN:** de actuele data volgt voor alle bestaande producten het gekozen zelfstandig-productmodel met één technische variant.

### 5.2 Vendors

| Vendor | Producten |
| --- | ---: |
| `Hotbath` | 7.550 |
| `THE MOSAIC FACTORY` | 277 |

Er zijn geen lege vendorwaarden aangetroffen.

### 5.3 Producttypes

Er zijn 649 verschillende niet-lege producttypewaarden. De grootste groepen zijn:

| Producttype | Producten |
| --- | ---: |
| `Inbouw douchesets` | 2.783 |
| `Kraanonderdelen` | 774 |
| `Inbouw badkranen` | 449 |
| `Mozaiektegel` | 277 |
| `Inbouwdoucheset` | 259 |
| `Opbouw wastafelkranen` | 254 |
| `Hoofddouches` | 219 |
| `Badkamerspiegels` | 189 |
| `Inbouw wastafelkranen` | 169 |
| `Inbouw/opbouw nissen` | 154 |
| `Stortdouches` | 150 |
| `Handdouches` | 115 |

**BEWEZEN:** `undefined` komt 69 keer voor. Daarnaast komen producttitelachtige waarden slechts één keer voor. Dit wijst op een niet-genormaliseerde producttypetaxonomie en vereist vervolgvalidatie in `BC-DATA-001` en `BC-IA-001`.

### 5.4 SKU-dekking

| Kenmerk | Aantal |
| --- | ---: |
| Varianten met niet-lege SKU | 7.810 |
| Varianten zonder SKU | 17 |
| SKU-dekking | 99,78% |
| Groepen met een dubbele niet-lege SKU | 72 |

De 72 dubbele groepen zijn een telling van gegroepeerde SKU-waarden, niet van alle betrokken varianten. De betrokken producten en herstelregels zijn `[NOG ONDERZOEKEN]`; deze read-only taak wijzigt geen SKU.

### 5.5 Representatieve voorbeelden

| Product | Handle | Vendor | Producttype | Varianten |
| --- | --- | --- | --- | ---: |
| Hotbath Cobber IBS70 inbouw regendoucheset, geborsteld messing, 25 cm, wandarm, geen glijstang | `hotbath-cobber-ibs70-inbouw-doucheset-geborsteld-messing-staafmodel-25cm-wandarm-glijstang-nee` | Hotbath | Inbouwdoucheset | 1 |
| Hotbath SPOM357 HB Schroefje perlator F004/3c F7 | `hotbath-spom357-hb-schroefje-perlator-f004-3c-f7` | Hotbath | Kraanonderdelen | 1 |
| Hotbath Archie SDS32 opbouw regendouche RVS 316 | `hotbath-archie-sds32-opbouw-regendoucheset-20cm-hoofddouche-8mm-staafhanddouche-geborsteld-koper-pvd` | Hotbath | Stortdouches | 1 |
| The Mosaic Factory Venice Pennyround Red Glossy | `the-mosaic-factory-venice-pennyround-red-glossy-mozaiektegel-vkn010` | THE MOSAIC FACTORY | Mozaiektegel | 1 |

Dit is een beperkte steekproef; er is geen volledige productdump in Git opgeslagen.

## 6. Collecties

| Kenmerk | Aantal |
| --- | ---: |
| Collecties totaal | 201 |
| Handmatig | 200 |
| Automatisch | 1 |
| Leeg | 199 |
| Default/leeg template suffix | 188 |
| `category-landing` suffix | 13 |

De twee niet-lege collecties zijn:

| Collectie | Type | Producten | Voorwaarde |
| --- | --- | ---: | --- |
| `IBS70 cobber doucheset` (`ibs70-cobber-doucheset`) | Automatisch | 259 | `ANY`; `TAG EQUALS ibs70-cobber-doucheset` |
| `Hotbath Ace AC003 wastafelkraan` (`hotbath-ace-ac003-wastafelkraan`) | Handmatig | 12 | N.v.t. |

**BEWEZEN:** 99,00% van de collecties is leeg. De 13 category-landingcollecties bestaan en zijn toegewezen, maar hun assortimentdekking is grotendeels nul.

Meerdere titel/handlecombinaties zijn semantisch opvallend, bijvoorbeeld `Baden` met handle `douche`, `Accessoires` met handle `spiegels` en `Verwarming` met handle `badkamerverlichting`. De technische targets bestaan; de bedoelde commerciële betekenis is `[NOG ONDERZOEKEN]`.

## 7. Metafields

### 7.1 Definities

De definitiequery's leverden op:

| Owner type | Definities | `custom` |
| --- | ---: | ---: |
| `PRODUCT` | 1 | 1 |
| `PRODUCTVARIANT` | 0 | 0 |
| `COLLECTION` | 0 | 0 |
| `PAGE` | 0 | 0 |
| `SHOP` | 0 | 0 |

De enige definitie is:

| Namespace | Key | Naam | Type | Validaties |
| --- | --- | --- | --- | --- |
| `custom` | `switch_group` | `switch_group` | `single_line_text_field` | Geen |

Er zijn geen metafielddefinities gevonden die naar metaobjects verwijzen.

### 7.2 Exacte dekking van prioriteitsvelden

De volgende dekking is exact gemeten over alle 7.827 producten:

| Veld | Gevuld | Leeg/afwezig | Dekking | Waargenomen type |
| --- | ---: | ---: | ---: | --- |
| `custom.switch_group` | 3.658 | 4.169 | 46,74% | `single_line_text_field` |
| `custom.switch_options` | 0 | 7.827 | 0% | N.v.t. |
| `custom.group` | 0 | 7.827 | 0% | N.v.t. |
| `custom.menu_1` | 0 | 7.827 | 0% | N.v.t. |
| `custom.menu_2` | 0 | 7.827 | 0% | N.v.t. |
| `custom.menu_3` | 0 | 7.827 | 0% | N.v.t. |
| `custom.menu_4` | 0 | 7.827 | 0% | N.v.t. |
| `custom.menu_5` | 0 | 7.827 | 0% | N.v.t. |
| `custom.pluspunten` | 0 | 7.827 | 0% | N.v.t. |
| `custom.aandachtspunten` | 0 | 7.827 | 0% | N.v.t. |

**BEWEZEN:** de V2-trigger wordt gebruikt; de onderzochte legacyvelden en contentvelden hebben geen actuele productwaarden. Dit bewijst niet dat gelijknamige velden op een ander owner type of in een externe bron bestaan.

### 7.3 Specificaties

De theme-snapshot bevat de eerder vastgelegde statische specificatiereferenties, maar Shopify Admin bevat daarvoor geen definities. De 32 onderzochte `custom`-keys zijn:

- `afmeting`, `afwerking`, `basiskleur`, `frame`, `handdouche`, `hoofddouche`, `hoogte`, `led`, `lengte`, `met_glijstang`, `montage`, `plaatsing`, `type`, `type_bevestiging_hoofddouche`, `type_handdouche`, `vorm`;
- `artikelnummer`, `fabrikantnummer`, `ean`, `serie`;
- `vormgeving_stijlgroep`, `kleurgroep`, `glansgraad`, `materiaal_kraan`, `montagewijze`, `afwerking_greep`;
- `belgaqua_keurmerk`, `met_hoofddouche`, `breedte_diameter_hoofddouche`, `dikte_hoofddouche`, `aantal_straalsoorten_hoofddouche`, `lengte_douchearm`.

Een deterministische steekproef van 40 unieke producten is samengesteld via `ID`, `TITLE`, `PRODUCT_TYPE`, `CREATED_AT` en `UPDATED_AT`, telkens oplopend en aflopend. Geen van deze 32 keys kwam in de steekproef voor; alleen `custom.switch_group` werd aangetroffen, op 24 van de 40 producten.

**Beperking:** dit is geen exact dekkingsbewijs voor alle specificatiekeys over alle 7.827 producten. Een exacte meting via gewone gepagineerde query's zou een bredere aparte 32-veldenrun vereisen; Shopify Bulk Operations starten via een mutatie en waren expliciet verboden. Die bredere run is niet uitgevoerd. De conclusie blijft daarom:

- definities voor de specificatiekeys: **BEWEZEN afwezig** voor de onderzochte owner types;
- waarden in de 40-productsteekproef: **BEWEZEN niet aangetroffen**;
- volledige waardedekking buiten de steekproef: **NOG ONDERZOEKEN**.

Het bestaande risico rond `product.metafields.vendor` is aangescherpt: `product.vendor` is op alle producten gevuld, maar er bestaat geen productmetafielddefinitie `vendor`.

## 8. Metaobjects

Er bestaat één metaobjectdefinitie:

| Type | Velden | Entries | Capabilities |
| --- | --- | ---: | --- |
| `homepage_banner` | `title` (single line), `subtitle` (multi line), `image` (file reference), `button_text` (single line), `button_link` (single line), `position` (single line; lege choices-validatie) | 0 | Publishable en translatable aan; renderable en online store uit |

Alle velden zijn optioneel. Er zijn geen entries en geen metafielddefinities die naar dit type verwijzen. Eventuele indirecte app- of externe referenties zijn `[NOG ONDERZOEKEN]`.

## 9. Navigatie

### 9.1 Menu's en structuur

| Handle | Titel | Items inclusief afstammelingen |
| --- | --- | ---: |
| `main-menu` | Hoofdmenu | 234 |
| `footer` | Voettekstmenu | 1 |
| `customer-account-main-menu` | Hoofdmenu klantaccount | 2 |
| `assortiment` | Assortiment | 9 |
| `badkamermeubels-b` | Badkamermeubels - B | 1 |

Totaal zijn 247 menu-items aangetroffen met maximaal drie niveaus. De typen zijn 243 `COLLECTION`, twee `CUSTOMER_ACCOUNT_PAGE`, één `CATALOG` en één `SEARCH`.

#### Volledige structuur en linkdoelen

Notatie: `label` → `TYPE` `URL`. Inspringing toont het Shopify-parent/childniveau. De resource-ID-validatie staat in paragraaf 9.2.

**Hoofdmenu (`main-menu`)**

- `Badkamermeubels` → `COLLECTION` `/collections/badkamermeubels`
  - `Badmeubel sets` → `COLLECTION` `/collections/badmeubel-sets`
    - `Badmeubel met wastafel` → `COLLECTION` `/collections/badmeubel-met-wastafel-1`
    - `Badmeubel met waskom` → `COLLECTION` `/collections/badmeubel-met-wastafel`
    - `Badmeubel zonder spiegel` → `COLLECTION` `/collections/badmeubel-zonder-spiegel`
    - `Badmeubel met spiegel` → `COLLECTION` `/collections/badmeubel-met-spiegel`
    - `Badmeubel met spiegelkast` → `COLLECTION` `/collections/badmeubel-met-spiegelkast`
  - `Toiletmeubels` → `COLLECTION` `/collections/toiletmeubels`
  - `Kolom & Zijkasten` → `COLLECTION` `/collections/kolom-zijkasten`
    - `Hoge kasten` → `COLLECTION` `/collections/hoge-kasten`
    - `Halfhoge kasten` → `COLLECTION` `/collections/halfhoge-kasten`
  - `Losse onderkasten` → `COLLECTION` `/collections/losse-onderkasten`
  - `Wastafelbladen` → `COLLECTION` `/collections/wastafelbladen`
  - `Spiegels` → `COLLECTION` `/collections/spiegels-2`
    - `Badkamerspiegels` → `COLLECTION` `/collections/badkamerspiegels`
    - `Spiegelkasten` → `COLLECTION` `/collections/spiegelkasten`
  - `Toebehoren` → `COLLECTION` `/collections/toebehoren`
    - `Wastafelkranen` → `COLLECTION` `/collections/wastafelkranen`
    - `Sifons` → `COLLECTION` `/collections/sifons`
    - `Afvoerpluggen` → `COLLECTION` `/collections/afvoerpluggen`
- `Kranen` → `COLLECTION` `/collections/kranen`
  - `Douchekranen` → `COLLECTION` `/collections/douchekranen`
    - `Douchesets` → `COLLECTION` `/collections/douchesets`
    - `Douche thermostaatkranen` → `COLLECTION` `/collections/douche-thermostaatkranen`
    - `Inbouw douchekranen` → `COLLECTION` `/collections/inbouw-douchekranen`
    - `Handdouches` → `COLLECTION` `/collections/handdouches`
    - `Hoofddouches` → `COLLECTION` `/collections/hoofddouches`
  - `Badkranen` → `COLLECTION` `/collections/badkranen`
    - `Bad thermostaatkranen` → `COLLECTION` `/collections/bad-thermostaatkranen`
    - `Inbouw badkranen` → `COLLECTION` `/collections/inbouw-badkranen`
    - `Vrijstaande badkranen` → `COLLECTION` `/collections/vrijstaande-badkranen`
    - `Badrandkranen` → `COLLECTION` `/collections/badrandkranen`
    - `Badsets` → `COLLECTION` `/collections/badsets`
  - `Wastafelkranen` → `COLLECTION` `/collections/wastafelkranen`
    - `Opbouw wastafelkranen` → `COLLECTION` `/collections/opbouw-wastafelkranen`
    - `Inbouw wastafelkranen` → `COLLECTION` `/collections/inbouw-wastafelkranen`
  - `Fonteinkranen` → `COLLECTION` `/collections/fonteinkranen`
    - `Opbouw fonteinkranen` → `COLLECTION` `/collections/opbouw-fonteinkranen`
    - `Inbouw fonteinkranen` → `COLLECTION` `/collections/inbouw-fonteinkranen`
  - `Keukenkranen` → `COLLECTION` `/collections/keukenkranen`
  - `Bidetkranen` → `COLLECTION` `/collections/bidetkranen`
  - `Urinoirspoelers` → `COLLECTION` `/collections/urinoirspoelers`
  - `Buitendouches` → `COLLECTION` `/collections/buitendouches`
  - `Toebehoren` → `COLLECTION` `/collections/toebehoren`
    - `Universele uitlopen` → `COLLECTION` `/collections/universele-uitlopen`
    - `Hoekstopkranen` → `COLLECTION` `/collections/hoekstopkranen`
    - `Doucheslangen` → `COLLECTION` `/collections/doucheslangen`
    - `Handdouchehouders` → `COLLECTION` `/collections/handdouchehouders`
    - `Hoofddouchehouders` → `COLLECTION` `/collections/hoofddouchehouders`
- `Toiletten` → `COLLECTION` `/collections/toiletten`
  - `Complete toiletsets` → `COLLECTION` `/collections/complete-toiletsets`
  - `Hangtoiletten` → `COLLECTION` `/collections/hangtoiletten`
    - `Toilet zonder spoelrand` → `COLLECTION` `/collections/toilet-zonder-spoelrand`
    - `Compacte toiletten` → `COLLECTION` `/collections/compacte-toiletten`
  - `Staande toiletten` → `COLLECTION` `/collections/staande-toiletten`
    - `Duoblok toilet` → `COLLECTION` `/collections/duoblok-toilet`
    - `Toilet met losse stortbak` → `COLLECTION` `/collections/toilet-met-losse-stortbak`
  - `Douche wc's` → `COLLECTION` `/collections/douche-wcs`
  - `Bidetten` → `COLLECTION` `/collections/bidetten`
  - `Urinoirs` → `COLLECTION` `/collections/urinoirs`
  - `Fonteinen` → `COLLECTION` `/collections/fonteinen`
    - `Losse fonteinen` → `COLLECTION` `/collections/losse-fonteinen`
    - `Fonteinsets` → `COLLECTION` `/collections/fonteinsets`
    - `Fonteinmeubels` → `COLLECTION` `/collections/fonteinmeubels`
  - `Reservoirs` → `COLLECTION` `/collections/reservoirs`
    - `Inbouwreservoirs` → `COLLECTION` `/collections/inbouwreservoirs`
    - `Hangende reservoirs` → `COLLECTION` `/collections/hangende-reservoirs`
  - `Toilet accessoires` → `COLLECTION` `/collections/toilet-accessoires`
    - `Accessoires sets` → `COLLECTION` `/collections/toilet-accessoires-sets`
    - `Toiletborstels` → `COLLECTION` `/collections/toiletborstels`
    - `Toiletrolhouders` → `COLLECTION` `/collections/toiletrolhouders`
  - `Toebehoren & Overig` → `COLLECTION` `/collections/toebehoren-overig`
    - `Bedieningspanelen` → `COLLECTION` `/collections/bedieningspanelen`
    - `Toiletzittingen` → `COLLECTION` `/collections/toiletzittingen`
    - `Toiletblokhouder` → `COLLECTION` `/collections/toiletblokhouder`
- `Wastafels` → `COLLECTION` `/collections/wastafels`
  - `Vrijhangende wastafels` → `COLLECTION` `/collections/vrijhangende-wastafels`
  - `Meubelwastafels` → `COLLECTION` `/collections/meubelwastafels`
  - `Opzetwastafels` → `COLLECTION` `/collections/opzetwastafels`
  - `Fonteinen` → `COLLECTION` `/collections/fonteinen`
    - `Fonteinsets` → `COLLECTION` `/collections/fonteinsets`
    - `Fonteinmeubels` → `COLLECTION` `/collections/fonteinmeubels`
    - `Standaard fonteinen` → `COLLECTION` `/collections/standaard-fonteinen`
    - `Hoekfonteinen` → `COLLECTION` `/collections/hoekfonteinen`
    - `Opzetfonteinen` → `COLLECTION` `/collections/opzetfonteinen`
  - `Gootstenen` → `COLLECTION` `/collections/gootstenen`
  - `Wastafelkranen` → `COLLECTION` `/collections/wastafelkranen`
    - `Inbouw` → `COLLECTION` `/collections/inbouw-wastafelkranen`
    - `Opbouw` → `COLLECTION` `/collections/opbouw-wastafelkranen`
  - `Wastafel accessoires` → `COLLECTION` `/collections/zeep-accessoires`
    - `Planchetten` → `COLLECTION` `/collections/planchetten`
    - `Handdoekhouders` → `COLLECTION` `/collections/handdoekhouders`
    - `Zeep accessoires` → `COLLECTION` `/collections/zeep-accessoires-1`
  - `Toebehoren` → `COLLECTION` `/collections/toebehoren`
    - `Sifons` → `COLLECTION` `/collections/sifons`
    - `Wastafelpluggen` → `COLLECTION` `/collections/afvoerpluggen`
    - `Overloopringen` → `COLLECTION` `/collections/overloopringen`
- `Douche` → `COLLECTION` `/collections/douche-1`
  - `Douchecabines` → `COLLECTION` `/collections/douchecabines`
    - `Vierkant` → `COLLECTION` `/collections/vierkant`
    - `Rechthoek` → `COLLECTION` `/collections/rechthoek`
    - `Kwartrond` → `COLLECTION` `/collections/kwartrond`
    - `Vijfhoek` → `COLLECTION` `/collections/vijfhoek`
  - `Douchewanden` → `COLLECTION` `/collections/douchewanden`
    - `Inloopdouches` → `COLLECTION` `/collections/inloopdouches`
    - `Badwanden` → `COLLECTION` `/collections/badwanden`
  - `Douchedeuren` → `COLLECTION` `/collections/douchedeuren`
    - `Draaideuren` → `COLLECTION` `/collections/draaideuren`
    - `Schuifdeuren` → `COLLECTION` `/collections/schuifdeuren`
    - `Pendeldeuren` → `COLLECTION` `/collections/pendeldeuren`
    - `Vouwdeuren` → `COLLECTION` `/collections/vouwdeuren`
  - `Douchebakken` → `COLLECTION` `/collections/douchebakken`
  - `Douchegoten` → `COLLECTION` `/collections/douchegoten`
  - `Doucheputten` → `COLLECTION` `/collections/doucheputten`
  - `Douchekranen` → `COLLECTION` `/collections/douchekranen`
    - `Douchesets` → `COLLECTION` `/collections/douchesets`
    - `Douche thermostaatkranen` → `COLLECTION` `/collections/douche-thermostaatkranen`
    - `Inbouw douchekranen` → `COLLECTION` `/collections/inbouw-douchekranen`
    - `Handdouches` → `COLLECTION` `/collections/handdouches`
    - `Hoofddouches` → `COLLECTION` `/collections/hoofddouches`
  - `Sunshower` → `COLLECTION` `/collections/sunshower`
  - `Douche accessoires` → `COLLECTION` `/collections/douche-accessoires`
    - `Wissers` → `COLLECTION` `/collections/wissers`
    - `Doucherekken` → `COLLECTION` `/collections/doucherekken`
    - `Douchezitjes` → `COLLECTION` `/collections/douchezitjes`
- `Baden` → `COLLECTION` `/collections/douche`
  - `Inbouwbaden` → `COLLECTION` `/collections/inbouwbaden`
  - `Halfvrijstaande baden` → `COLLECTION` `/collections/halfvrijstaande-baden`
  - `Vrijstaande baden` → `COLLECTION` `/collections/vrijstaande-baden`
  - `Whirlpool baden` → `COLLECTION` `/collections/whirlpool-baden`
  - `Badkranen` → `COLLECTION` `/collections/badkranen`
    - `Bad thermostaatkranen` → `COLLECTION` `/collections/bad-thermostaatkranen`
    - `Inbouw badkranen` → `COLLECTION` `/collections/inbouw-badkranen`
    - `Vrijstaande badkranen` → `COLLECTION` `/collections/vrijstaande-badkranen`
    - `Badrandkranen` → `COLLECTION` `/collections/badrandkranen`
    - `Badsets` → `COLLECTION` `/collections/badsets`
  - `Badafvoeren & vulsystemen` → `COLLECTION` `/collections/badafvoeren-vulsystemen`
  - `Badwanden` → `COLLECTION` `/collections/badwanden`
    - `1-Delig` → `COLLECTION` `/collections/1-delig`
    - `2-Delig` → `COLLECTION` `/collections/2-delig`
  - `Bad accessoires` → `COLLECTION` `/collections/bad-accessoires`
    - `Badbruggen & badplanken` → `COLLECTION` `/collections/badbruggen-badplanken`
    - `Badkrukjes` → `COLLECTION` `/collections/badkrukjes`
    - `Badgrepen` → `COLLECTION` `/collections/badgrepen`
- `Spiegels` → `COLLECTION` `/collections/spiegels-1`
  - `Badkamerspiegels` → `COLLECTION` `/collections/badkamerspiegels`
    - `Rechthoekige spiegels` → `COLLECTION` `/collections/rechthoekige-spiegels`
    - `Ronde spiegels` → `COLLECTION` `/collections/ronde-spiegels`
    - `Toiletspiegels` → `COLLECTION` `/collections/toiletspiegels`
    - `Spiegels met verlichting` → `COLLECTION` `/collections/spiegels-met-verlichting`
    - `Spiegels zonder verlichting` → `COLLECTION` `/collections/spiegels-zonder-verlichting`
    - `Spiegels met verwarming` → `COLLECTION` `/collections/spiegels-met-verwarming`
  - `Spiegelkasten` → `COLLECTION` `/collections/spiegelkasten`
    - `Spiegelkast met verlichting` → `COLLECTION` `/collections/spiegelkast-met-verlichting`
    - `Spiegelkast zonder verlichting` → `COLLECTION` `/collections/spiegelkast-zonder-verlichting`
  - `Spiegelverlichting` → `COLLECTION` `/collections/spiegelverlichting`
  - `Scheer / make-up spiegels` → `COLLECTION` `/collections/scheer-make-up-spiegels`
  - `Spiegelbevestiging` → `COLLECTION` `/collections/spiegelbevestiging`
- `Accessoires` → `COLLECTION` `/collections/spiegels`
  - `Decoratie & Vintage` → `COLLECTION` `/collections/decoratie-vintage`
  - `Toilet accessoires` → `COLLECTION` `/collections/toilet-accessoires`
    - `Toilet accessoires sets` → `COLLECTION` `/collections/toilet-accessoires-sets`
    - `Toiletrolhouders` → `COLLECTION` `/collections/toiletrolhouders`
    - `Toiletborstelhouders` → `COLLECTION` `/collections/toiletborstelhouders`
    - `Reserverolhouders` → `COLLECTION` `/collections/reserverolhouders`
  - `Inbouw/opbouw nissen` → `COLLECTION` `/collections/inbouw-opbouw-nissen`
  - `Handdoekhouders` → `COLLECTION` `/collections/handdoekhouders`
    - `Handdoekstangen` → `COLLECTION` `/collections/handdoekstangen`
    - `Handdoekrekken` → `COLLECTION` `/collections/handdoekrekken`
    - `Handdoekhaken` → `COLLECTION` `/collections/handdoekhaken`
    - `Handdoekringen` → `COLLECTION` `/collections/handdoekringen`
  - `Zeep accessoires` → `COLLECTION` `/collections/zeep-accessoires-1`
    - `Zeepdispensers` → `COLLECTION` `/collections/zeepdispensers`
    - `Zeephouders` → `COLLECTION` `/collections/zeephouders`
  - `Wastafel accessoires` → `COLLECTION` `/collections/zeep-accessoires`
    - `Planchetten` → `COLLECTION` `/collections/planchetten`
  - `Bad accessoires` → `COLLECTION` `/collections/bad-accessoires`
    - `Badbruggen & badplanken` → `COLLECTION` `/collections/glashouders`
    - `Badkrukjes` → `COLLECTION` `/collections/badkrukjes`
    - `Badgrepen` → `COLLECTION` `/collections/badgrepen`
  - `Textiel` → `COLLECTION` `/collections/textiel`
  - `Stoelen & krukjes` → `COLLECTION` `/collections/stoelen-krukjes`
  - `Afvalemmers` → `COLLECTION` `/collections/afvalemmers`
  - `Sanitaire veiligheid` → `COLLECTION` `/collections/sanitaire-veiligheid`
  - `Onderhouds- en schoonmaakmiddelen` → `COLLECTION` `/collections/onderhouds-en-schoonmaakmiddelen`
- `Tegels` → `COLLECTION` `/collections/tegels`
  - `Vloertegels` → `COLLECTION` `/collections/vloertegels`
  - `Wandtegels` → `COLLECTION` `/collections/wandtegels`
  - `Decortegels` → `COLLECTION` `/collections/decortegels`
  - `Tegelstroken` → `COLLECTION` `/collections/tegelstroken`
  - `Mozaïek tegels` → `COLLECTION` `/collections/mozaiek-tegels`
  - `Keramisch parket` → `COLLECTION` `/collections/keramisch-parket`
  - `Populair` → `COLLECTION` `/collections/populair`
    - `Betonlook tegels` → `COLLECTION` `/collections/betonlook-tegels`
    - `Stonelook tegels` → `COLLECTION` `/collections/stonelook-tegels`
    - `Marmerlook tegels` → `COLLECTION` `/collections/marmerlook-tegels`
    - `Houtlook tegels` → `COLLECTION` `/collections/houtlook-tegels`
    - `Metaallook tegels` → `COLLECTION` `/collections/metaallook-tegels`
    - `Terrazzo tegels` → `COLLECTION` `/collections/terrazzo-tegels`
  - `Toebehoren` → `COLLECTION` `/collections/toebehoren`
    - `Tegellijm` → `COLLECTION` `/collections/tegellijm`
    - `Voorstrijkmiddel` → `COLLECTION` `/collections/voorstrijkmiddel`
    - `Voegmortel` → `COLLECTION` `/collections/voegmortel`
    - `Silicone kit` → `COLLECTION` `/collections/silicone-kit`
    - `Leveling systeem` → `COLLECTION` `/collections/leveling-systeem`
- `Badkamerverlichting` → `COLLECTION` `/collections/spiegels-1`
  - `Spots` → `COLLECTION` `/collections/spots`
    - `Inbouwspots` → `COLLECTION` `/collections/inbouwspots`
    - `Opbouwspots` → `COLLECTION` `/collections/opbouwspots`
  - `Hanglampen` → `COLLECTION` `/collections/hanglampen`
  - `Wandlampen` → `COLLECTION` `/collections/wandlampen`
  - `Plafondlampen` → `COLLECTION` `/collections/plafondlampen`
  - `Spiegellampen` → `COLLECTION` `/collections/spiegellampen`
- `Verwarming` → `COLLECTION` `/collections/badkamerverlichting`
  - `Radiatoren` → `COLLECTION` `/collections/radiatoren`
    - `Handdoekradiatoren` → `COLLECTION` `/collections/handdoekradiatoren`
    - `Designradiatoren` → `COLLECTION` `/collections/designradiatoren`
    - `Elektrische radiatoren` → `COLLECTION` `/collections/elektrische-radiatoren`
    - `Paneelradiatoren` → `COLLECTION` `/collections/paneelradiatoren`
    - `Lage temperatuur radiatoren` → `COLLECTION` `/collections/lage-temperatuur-radiatoren`
  - `Handdoekwarmers` → `COLLECTION` `/collections/handdoekwarmers`
  - `Elektrische vloerverwarming` → `COLLECTION` `/collections/elektrische-vloerverwarming`
  - `Spiegelverwarming` → `COLLECTION` `/collections/spiegelverwarming`
  - `Radiator aansluitmateriaal` → `COLLECTION` `/collections/radiator-aansluitmateriaal`
    - `Onderblokken` → `COLLECTION` `/collections/onderblokken`
    - `Radiatorkranen` → `COLLECTION` `/collections/radiatorkranen`
    - `Voetventielen` → `COLLECTION` `/collections/voetventielen`
    - `Thermostaatknoppen` → `COLLECTION` `/collections/thermostaatknoppen`
    - `Knelsets` → `COLLECTION` `/collections/knelsets`
- `Meer` → `COLLECTION` `/collections/meer`
  - `Waterontharders` → `COLLECTION` `/collections/waterontharders`
  - `Schakelmateriaal` → `COLLECTION` `/collections/schakelmateriaal`
  - `Badkamerventilatie` → `COLLECTION` `/collections/badkamerventilatie`
- `Outlet` → `COLLECTION` `/collections/outlet`

**Voettekstmenu (`footer`)**

- `Zoeken` → `SEARCH` `/search`

**Hoofdmenu klantaccount (`customer-account-main-menu`)**

- `Bestellingen` → `CUSTOMER_ACCOUNT_PAGE` `https://shopify.com/94179590410/account/orders`
- `Profiel` → `CUSTOMER_ACCOUNT_PAGE` `https://shopify.com/94179590410/account/profile`

**Assortiment (`assortiment`)**

- `Accessoires` → `COLLECTION` `/collections/spiegels`
- `Baden` → `COLLECTION` `/collections/douche`
- `Badkamermeubels` → `COLLECTION` `/collections/badkamermeubels`
- `Homepage` → `COLLECTION` `/collections/kranen`
- `Meer` → `COLLECTION` `/collections/meer`
- `Tegels` → `COLLECTION` `/collections/tegels`
- `Toiletten` → `COLLECTION` `/collections/toiletten`
- `Verwarming` → `COLLECTION` `/collections/badkamerverlichting`
- `Wastafels` → `COLLECTION` `/collections/wastafels`

**Badkamermeubels - B (`badkamermeubels-b`)**

- `Alle producten` → `CATALOG` `/collections/all`

### 9.2 Targets en afwijkingen

**BEWEZEN:** geen item heeft een lege titel, lege URL of `#`-URL. Alle 243 collection-items hebben een Shopify collection resource-ID. De account-, catalogus- en searchlinks hebben geldige Shopify-URL-vormen voor hun type.

De volgende zichtbare titel/targetcombinaties zijn inhoudelijk opvallend:

- `Baden` → `/collections/douche`;
- `Accessoires` → `/collections/spiegels`;
- `Badkamerverlichting` → `/collections/spiegels-1`;
- `Verwarming` → `/collections/badkamerverlichting`;
- `Homepage` in menu `assortiment` → `/collections/kranen`.

De targets bestaan technisch; of labels en doelen bewust zo zijn gekoppeld is `[NOG ONDERZOEKEN]` en hoort bij `BC-DISC-001`/`BC-IA-001`.

## 10. Templates en actieve themeconfiguratie

### 10.1 Objecttoewijzingen

| Objecttype | Toewijzing |
| --- | --- |
| Producten | Alle 7.827 hebben een leeg/default suffix en gebruiken de default producttemplate |
| Collecties | 188 default/leeg; 13 `category-landing` |
| Pagina's | 109 `begrip`; 6 `page`; 1 `contact`; 1 `begrippenlijst` |

Van de 117 pagina's zijn 116 gepubliceerd en één ongepubliceerd (`Merken`). De live themebestanden bevatten `page.json`, `page.contact.json`, `page.begrip.json` en `page.begrippenlijst.json`, maar geen `page.page.json`. Zes pagina's rapporteren toch suffix `page`; de runtimefallback en bedoelde toewijzing zijn `[NOG ONDERZOEKEN]`.

### 10.2 Themes

| Theme | ID | Rol | Status van doel/eigenaarschap |
| --- | ---: | --- | --- |
| `Categoriepagina_v1.0` | `189463068938` | `MAIN` | Live theme; wijzigen verboden zonder afzonderlijke toestemming |
| `BadkamerCity V1.0` | `189117628682` | `UNPUBLISHED` | Bestaande oudere unpublished omgeving |
| `BadkamerCity Development` | `192770375946` | `UNPUBLISHED` | Goedgekeurde previewomgeving voor latere expliciete taken |
| `badkamercity-phase-c-paris-rectangle-test-v2` | `192796786954` | `UNPUBLISHED` | **BEWEZEN bestaand**; eigenaar, exact doel en ontstaansreden `[NOG ONDERZOEKEN]`; niet wijzigen, verwijderen, publiceren, pushen of pullen |

Het live theme bevat 396 bestanden, gelijk aan de 396 lokale bestanden. Een aanvankelijke afwijking tussen Shopify's `checksumMd5` en de lokale MD5 voor `config/settings_data.json` bleek geen inhoudsverschil: API-body en lokaal bestand zijn bytegelijk en hebben dezelfde SHA-256.

### 10.3 Actieve JSON-configuratie en apps

De 15 JSON-templates, twee section groups en `config/settings_data.json` zijn live read-only opgehaald en succesvol geparseerd. Daarin staan:

- 26 sections;
- 157 blocks;
- nul disabled sections;
- nul disabled blocks;
- nul `shopify://apps/...`-referenties;
- nul app embeds in `settings_data.json`.

**BEWEZEN:** de actieve live JSON-configuratie bevat geen geconfigureerd theme app block of app embed. **Niet bewezen:** dat er geen apps, pixels, scripts of buiten deze JSON-configuratie werkende integraties bestaan.

## 11. Markets, talen en accounts

### 11.1 Markets en talen

| Onderdeel | Resultaat |
| --- | --- |
| Markets | Eén actieve markt: `Nederland`, handle `nl` |
| Talen | Eén taal: `nl` / Nederlands; primair en gepubliceerd |

### 11.2 Klantaccounts en checkoutconfiguratie

| Instelling | Resultaat |
| --- | --- |
| Accountmodel | `NEW_CUSTOMER_ACCOUNTS` |
| Loginlinks zichtbaar op storefront en checkout | Ja |
| Login verplicht bij checkout | Nee |
| Checkout/accounts configuraties | Eén |
| Configuratienaam | `Mijn winkel-configuratie` |
| Gepubliceerd | Ja |
| Laatst bijgewerkt/bewerkt | 2026-06-04 16:34:56 UTC |

Er zijn geen klantaccounts, klanten of orders gelezen.

## 12. Locaties en voorraadstructuur

### 12.1 Locaties

Er is één locatie:

| Naam | Actief | Fulfilment online orders | Land | Plaats/provincie |
| --- | --- | --- | --- | --- |
| `Winkellocatie` | Ja | Ja | NL | Niet ingevuld |

### 12.2 Inventory items

| Kenmerk | Aantal |
| --- | ---: |
| Inventory items | 7.827 |
| Tracking aan | 259 |
| Tracking uit | 7.568 |
| SKU gevuld | 7.810 |
| SKU leeg | 17 |

Een beperkte steekproef van tien getrackte inventory items had ieder één inventory level op `Winkellocatie`, zonder geneste paginatie. In die steekproef stonden `available` en `on_hand` beide op 10 en `committed`/`incoming` op 0. Dit is **geen** volledige voorraadniveaudump en mag niet als algemene voorraadbelofte worden gebruikt.

**NOG ONDERZOEKEN:** operationele betekenis, actualiteit, bronhouder en leverancierrelatie van tracking en hoeveelheden.

## 13. Shipping en delivery profiles

Er is één default delivery profile `Algemeen profiel`:

- één originlocatie: `Winkellocatie`;
- nul locaties zonder rates;
- vier actieve merchant-defined methoden;
- nul participant-defined methoden;
- productvarianttelling `AT_LEAST 500`; de query geeft geen exact totaal boven deze drempel;
- geen carrier services.

| Zone | Landen | Actieve methoden |
| --- | ---: | --- |
| `Domestic` | NL | Twee methoden met naam `Standaard` |
| `EU (Europeese Unie)` | 26 EU-landen | Eén methode `Standard` |
| `International` | 14 landen | Eén methode `Standard` |

De exacte tarieven, voorwaarden, gewichts-/prijsgrenzen en operationele geschiktheid zijn `[NOG ONDERZOEKEN]`. Dat er een rate bestaat bewijst niet dat de lanceringsregels uit `BC-LOG-001` en `BC-LOG-002` zijn vastgesteld.

## 14. Apps en resterende toegangsgrenzen

### 14.1 Bewezen

- De huidige Shopify CLI-installatie en exact verleende read-scopes zijn via `currentAppInstallation` aantoonbaar.
- Live JSON-templates, section groups en settings bevatten geen app blocks of app embeds.
- `content_for_header` blijft in theme-code aanwezig en kan runtime-inhoud injecteren.
- De `reviews.*`-themeverwijzingen bestaan statisch, maar er is geen bewijs welke app of welk proces ze beheert.

### 14.2 Niet toegankelijk

**NIET TOEGANKELIJK:** een volledige lijst van geïnstalleerde apps, sales channels, web pixels, script tags, app-abonnementen, externe dashboards en niet-themegebonden appconfiguratie. De verleende scopes bevatten geen algemene app-inventarisscope en er wordt geen aanvullende scope aangevraagd.

Daarom wordt niet geconcludeerd dat er geen apps actief zijn.

## 15. Volledigheid en beperkingen

### Volledig onderzocht binnen de toegestane route

- exacte product-, variant-, status-, vendor-, producttype-, template- en SKU-totalen;
- exacte collectieaantallen, typen, regels, suffixes en productaantallen;
- metafielddefinities voor vijf relevante owner types;
- exacte dekking van tien prioriteitsmetafields;
- alle metaobjectdefinities en entrytotalen;
- alle menu's, items, diepte, URL's en resource-ID's;
- product-, collectie- en paginatemplate suffixes;
- alle themes en de actieve live JSON-configuratie;
- markets, talen, customer-accountmodel, checkoutconfiguratie, locaties en inventory-itemstructuur;
- delivery profiles, zones, methoden en carrier services.

### Niet volledig onderzocht of niet toegankelijk

- volledige waarden/dekking van alle specificatiemetafields buiten de 40-productsteekproef: **NOG ONDERZOEKEN**;
- inhoudelijke juistheid van alle 247 navigatielabels tegenover hun targets: **NOG ONDERZOEKEN**;
- exacte productvarianttoewijzing aan het delivery profile boven de `AT_LEAST 500`-grens: **NOG ONDERZOEKEN**;
- tarieven en operationele verzendregels: **NOG ONDERZOEKEN**;
- volledige app-, pixel-, script- en externe integratielijst: **NIET TOEGANKELIJK**;
- eigenaar, exact doel en ontstaansreden van theme `192796786954`: **NOG ONDERZOEKEN**;
- leverancierbronnen, importbestanden en data-eigenaarschap: **NOG ONDERZOEKEN**.

## 16. Gevolgen voor vervolgtaken

- `BC-ADM-001` gaat naar `REVIEW`; de projecteigenaar beoordeelt de volledigheid en conclusies.
- `BC-DISC-001` blijft `NOT_STARTED` totdat die menselijke beoordeling expliciet is vastgelegd.
- `BC-DISC-001` kan daarna de 247 menukoppelingen, zes `page`-suffixes, themegebruik, niet-JSON appinjectie en het vierde testtheme nader duiden.
- `BC-DATA-001` krijgt harde input over één bestaande productmetafielddefinitie, ontbrekende specificatiedefinities, 17 lege SKU's, 72 dubbele SKU-groepen en 649 producttypen.
- `BC-SWITCH-001` krijgt exact bewijs dat `custom.switch_group` op 46,74% staat en de legacygroep/menuvelden op 0%.
- `BC-IA-001` krijgt bewijs dat 199 collecties leeg zijn en dat enkele titels, handles en menu-targets semantisch niet aansluiten.
- `BC-LOG-001` en `BC-LOG-002` krijgen één locatie, 259 getrackte items, één profile en drie brede verzendzones als actuele basis; operationele regels blijven open.
- `BC-ACC-001` kan uitgaan van nieuwe customer accounts en niet-verplichte login bij checkout, onder voorbehoud van functionele validatie.
- `BC-SEC-001` en `BC-ANA-001` blijven beperkt door de ontbrekende volledige app-/pixelinventaris.

## 17. Open vragen en beslissingen

1. **NOG ONDERZOEKEN:** wie beheert productdata en normaliseert SKU's, producttypen en metafields?
2. **NOG ONDERZOEKEN:** waarom zijn 199 collecties leeg en welke zijn bedoeld voor lancering?
3. **NOG ONDERZOEKEN:** zijn de opvallende collectiehandles en menu-targets bewust gekoppeld?
4. **NOG ONDERZOEKEN:** hoe moeten de zes pagina's met suffix `page` zich gedragen zonder `page.page.json`?
5. **NOG ONDERZOEKEN:** welke bron vult specificaties, pluspunten en aandachtspunten?
6. **NOG ONDERZOEKEN:** welke app of welk proces beheert eventuele `reviews.*`-velden?
7. **NOG ONDERZOEKEN:** eigenaar, exact doel en ontstaansreden van theme `192796786954`.
8. **OPEN BESLISSING:** welke bevoegde read-only bron mag later de volledige app-/pixel-/scriptinventaris leveren?
9. **OPEN BESLISSING:** keurt de projecteigenaar deze inventaris goed zodat `BC-ADM-001` `DONE` en `BC-DISC-001` actief kan worden?

## 18. Aanbevolen vervolgstap

1. De projecteigenaar beoordeelt dit rapport en de nieuwe datakwaliteitsrisico's.
2. Leg expliciet vast of `BC-ADM-001` is goedgekeurd; tot die tijd blijft de taak `REVIEW`.
3. Activeer pas daarna `BC-DISC-001` voor de gebruiksmatrix van templates, themeonderdelen, appafhankelijkheden en opvallende navigatiekoppelingen.
4. Wijzig geen product-, collectie-, metafield-, menu-, shipping- of themegegevens binnen deze review.

## 19. Eindconclusie

- **BEWEZEN:** de kern van Shopify Admin is binnen de dertien read-scopes geïnventariseerd met gepagineerde queries.
- **BEWEZEN:** het live theme is niet gewijzigd; de live inhoud van `config/settings_data.json` is gelijk aan de lokale inhoud.
- **BEWEZEN:** theme `192796786954` bestaat als unpublished testtheme; doel en eigenaarschap zijn niet bevestigd.
- **BEWEZEN:** er zijn geen write-scopes, mutaties of Shopify-wijzigingen gebruikt.
- **NIET TOEGANKELIJK:** de volledige geïnstalleerde-app-, pixel- en externe-integratielijst.
- **NOG ONDERZOEKEN:** datakwaliteitsherstel, operationele regels, app-eigenaarschap en inhoudelijke validatie van opvallende koppelingen.

Daarom is `BC-ADM-001` gereed voor menselijke `REVIEW`, niet voor implementatie of publicatie.
