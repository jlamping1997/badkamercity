# Routes → renderers → data → interacties

**DOC-02A · 28 oktober 2026 · VERIFIED_THEME, deels VERIFIED_HTML.** Lees de [dossieringang](components/README.md) voor bron-/bewijsregels. Thema MAIN 195818389770; het complete manifest is gelijk aan DOC-01. De open settings-bytecontrole verhindert geen uitleg van checksumgelijke code, maar verhindert wel een volledige deployvrijgave.

## De routebeslissing

Een template bepaalt de eerste secties. Binnen een sectie kiezen productmetafields, merk, instellingen en JavaScript nog een renderer. De aanwezigheid van een scriptbestand of template bewijst daarom niet dat een bezoeker die bediening gebruikt.

| Ingang | Template / sectie | Verdere renderer / data | Werkelijk bewijs in deze ronde |
| --- | --- | --- | --- |
| `/` | `index.json` | Onder meer home-popular-products, home-sunshower; eigen sectiemarkup | Publieke HTML 200, verwachte Shopify.theme.id |
| Algemene PDP | `product.json` → main-product | Buybox met beslisvolgorde hieronder; product-info/product-form; specsrouter | Wiesbaden 24.3710 en Hotbath SDS1: HTML 200 + data-bc-product-page |
| Sunshower PDP | `product.sunshower.json` → main-sunshower | Vier configuratievelden in de onderzochte pagina; bc_sunshower JSON en catalogusasset | Round One Medium Inbouw White: HTML 200 + data-ss-page |
| Hotbath pilot | `product.bc-hotbath-pilot.json` → main-product | Dezelfde hoofdsectie, andere templatecontext mogelijk | Template-/Admin-toewijzing uit DOC-01; geen verse pilot-HTML |
| Standaard collectie | `collection.json` → banner + product-grid + advice | Eerst card-product; externe renderer kan daarna overnemen | Wastafelkranen: HTML 200, 24 native kaart-CTA-labels, filterroot aanwezig |
| Zoekresultaten | `search.json` → main-search | Eerst bc-card-product-search; externe renderer kan overnemen | q=sunshower&type=product: HTML 200, 36 native kaart-CTA-labels, filterroot aanwezig |
| Predictive search | Header → predictive-search component | Eigen searchrequest, eigen responsemarkup | Bronpad vastgesteld; geen suggestie-interactie getest |
| Sunshower landing | `page.bc-sunshower.json` → bc-sunshower-landing | Lichtkeuzekaarten, configuratorlinks en bc-sunshower-shop-card | `/pages/sunshower`: HTML 200; 3 shopkaartroots |
| Meubelhub | `collection.bc-meubelhub.json` → bc-meubelhub | Eigen categorie-/menublokken en Admin-description | Template/code + eerdere Admin-toewijzing; geen verse hub-HTML |
| Categoriepagina | `collection.category-landing.json` → main-category-landing | Eigen hubs/links, geen aanname dat standaard productgrid actief is | Template/code + eerdere Admin-toewijzingen |
| Winkelwagen | `cart.json` → main-cart-items + main-cart-footer | cart.js, bc-cart-page.js, bc-cart-tools.js | Lege cart via nieuwe anonieme GET: HTML 200; geen cartmutatie |
| Productaanbevelingen | related-products of andere oproepende sectie | card-product met callerparameters | Bronref vastgesteld; aanbevelingsrequest niet interactief getest |

De tellingen uit DOC-01: 11.270 standaard PDP-toewijzingen, 72 Sunshower, 1 Hotbath pilot; 209 standaard collecties, 1 meubelhub, 16 categoriepagina's. Dit zijn toewijzingen inclusief concepten, geen nieuwe telling van publiek bereikbare pagina's.

## Binnen main-product is de volgorde beslissend

`sections/main-product.liquid:762` behandelt het block `variant_picker` in deze volgorde:

1. bc_sunshower.configuration gevuld → bc-sunshower-choices.
2. Merk exact Wiesbaden + custom.color_variants gevuld → bc-wiesbaden-colors.
3. current_switch_group gevuld → V2 bc-product-switcher.
4. current_group gevuld → oudere collectiegestuurde switcher, met ProductGroupData in de pagina.
5. Anders → Dawn product-variant-picker.

Dit is een `if/elsif`-keten. De voorwaarden zijn geen onafhankelijk op te tellen doelgroepen. Een gevuld veld kan door een eerdere voorwaarde worden overschaduwd. Een V2-laadfout heractiveert niet automatisch de Liquid-variantpicker; de beslissing is dan al op de server gemaakt. Zie [keuzes](components/PRODUCT_CHOICES.md).

De Hotbath-router kan een ontbrekende groep invullen of expliciet `__NO_MENU__` teruggeven. SPOM in titel, handle of variant-SKU onderdrukt in deze code de productgroep. De oudere custom.group-route gebruikt collectiecontext en een begrensde productlijst; die route is niet hetzelfde datamodel als V2.

## Native lijst → externe lijst

De native kaart is de serverterugval. `bc-external-filters` voegt het endpoint/context toe; `bc-external-filters.js:12–34` vereist bestaande layout-, grid- en contextnodes. Daarna roept de huidige code **zonder bcfilters=1-opt-incheck** runSearch aan (`:171`). Alleen bij een geldig antwoord neemt de externe lijst over (`:267–328`). Een oude pilotbeschrijving met verplichte queryparameter is voor deze code geen activeringswaarheid.

Het externe script verstuurt een POST voor een **zoekopdracht**, niet voor een productwijziging. Deze ronde heeft dat endpoint niet rechtstreeks aangeroepen of servergezondheid bewezen. HTML bevat de native kaart, terwijl een echte browser later de JS-kaart kan tonen. Gebruik [kaarten en filters](components/PRODUCT_CARDS_AND_FILTERS.md) voor de twee contracten.

## Globale laag

`layout/theme.liquid` laadt onder meer gedeelde kaartstijl en wishlist. Headergroep → header → desktopcategorieën, mobiele drawer, zoekveld, cartbadge en conditionele cart-notification. Alle acht gecontroleerde responses bevatten het notification-dialog en Shopify.theme.id 195818389770. Dat is onafhankelijk HTML-bewijs voor de popupmarkup; de settings-file is daarmee niet bytegelijk verklaard.

`templates/index.json` heeft de hero uitgeschakeld en de huidige homeblokken ingeschakeld. `templates/cart.json` heeft de featured-collection uitgeschakeld. “Bestaat als bestand” is dus niet gelijk aan “staat op de actuele pagina”.

## Onderzoeksset en vervolg

[http-response-checks.json](evidence/2026-10-28-doc02/http-response-checks.json) bewaart URL, tijdvenster, status, responsgrootte, hash en theme-ID. [rendered-structure.json](evidence/2026-10-28-doc02/rendered-structure.json) bewaart alleen veilige structurele signalen en assetnamen, geen ruwe response of klantdata. Er is geen browser-JavaScript uitgevoerd in die controles.

Voor DOC-02B: volg dezelfde representatieve routes in een browser, leg viewport en staat vast en registreer welke renderer werkelijk zichtbaar blijft na laden/fout/terugknop. Begin met de mobiele productkaart/pijlvergelijking en de PDP-keuzes. Koopacties blijven buiten die read-only stap; tests met transportstubs of conceptdata vragen een expliciet benoemde testbron en mogen geen echte winkelwagen-/voorraadwerking claimen.
