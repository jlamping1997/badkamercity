# Active Theme Usage

> **BC-DISC-001 - DONE - menselijk goedgekeurd read-only onderzoeksrapport.** Dit document beschrijft wat in het live theme direct is geconfigureerd, statisch bereikbaar is, alleen beschikbaar is, kandidaat-legacy is, backup/debug is of niet statisch bewezen kan worden. De classificaties zijn onderzoeksbevindingen en geven geen toestemming om bestanden, themes, apps of Shopify-data te wijzigen of verwijderen.

## 1. Onderzoeksgegevens

| Onderdeel | Waarde |
| --- | --- |
| Onderzoeksdatum | 2026-08-04 |
| Menselijke goedkeuring | 2026-08-05 - projecteigenaar heeft `BC-DISC-001` als afgerond read-only onderzoek goedgekeurd |
| Store | `fpa9hu-i3.myshopify.com` |
| Shopify CLI | `4.6.0` |
| Live theme | `Categoriepagina_v1.0` (`189463068938`, `MAIN`) |
| Repositorybasis | `main`; vooraf schoon en `HEAD` gelijk aan `origin/main` op `2150ca54abb15aa0f75be196b3dfa7d2c7ddff8a` |
| Lokale themesnapshot | 396 bestanden in `assets`, `config`, `layout`, `locales`, `sections`, `snippets` en `templates` |
| Taakstatus na menselijke beoordeling | `BC-DISC-001` `DONE`; `BC-DISC-002` is de actieve volgende read-only taak op `READY`, maar is niet inhoudelijk gestart |

## 2. Bronnen, methode en grenzen

### 2.1 Gebruikte bronnen

- `AGENTS.md`, `docs/MASTERPLAN.md`, `docs/SHOPIFY_ADMIN_INVENTORY.md` en `docs/REPOSITORY_AUDIT.md` zijn volledig gelezen.
- De lokale repository is read-only onderzocht met bestandslijsten, JSON-parsing, gerichte tekstzoekacties, inkomende/uitgaande referenties en hashes.
- De reeds toegestane Shopify Admin-route is alleen read-only gebruikt met `shopify store execute`.
- Via `themes` en gerichte `theme.files`-queries zijn de live bestandsnamen en de bodies van de 15 JSON-templates, twee section groups, `config/settings_data.json`, zeven customer-templates en `templates/gift_card.liquid` gecontroleerd.
- De 18 live JSON-configuratiebestanden zijn opnieuw geparseerd. Hun inhoud is bytegelijk aan de lokale bestanden.
- Bestaand Admin-bewijs uit `docs/SHOPIFY_ADMIN_INVENTORY.md` is gebruikt voor object-to-template-toewijzingen, metafielddekking, menu's, themes, markets, talen en accountconfiguratie.

### 2.2 Statische referentiemethode

Voor alle 396 bestanden is gezocht naar:

- JSON `sections[].type`-koppelingen;
- Liquid `render`, `include`, `section` en `sections`;
- `asset_url`, `asset_img_url`, `stylesheet_tag` en statische `/assets/...`-paden;
- JavaScript section-rendering-URL's en vaste section-ID's;
- CSS-, JavaScript- en JSON-koppelingen;
- app-blocktypen, app-embeds, `content_for_header`, `content_for_layout` en aanvullende checkoutcontent;
- lege links, placeholdercontent en menu-, pagina- en collectie-instellingen.

De syntactische transitive closure vanaf `layout/theme.liquid`, de live JSON-configuratie en `config/settings_data.json` omvat 167 bestanden: 15 templates, 27 sections/section groups, 36 snippets, 87 assets, een layout en een configuratiebestand. Daarnaast zijn vaste dynamische section-endpoints afzonderlijk beoordeeld.

### 2.3 Beperkingen

- **BEWEZEN:** live JSON en lokale JSON zijn op onderzoeksdatum inhoudelijk gelijk.
- **BEWEZEN:** de actieve JSON bevat nul disabled sections, nul disabled blocks, nul `shopify://apps/...`-blokken en nul app embeds.
- **NIET TOEGANKELIJK:** de volledige lijst van apps, web pixels, script tags, externe dashboards en niet-themegebonden integraties.
- **NOG ONDERZOEKEN:** werkelijk browsergedrag per route, device, product, cartactie en Theme Editor-conditie. Deze taak heeft geen storefront-runtime- of visuele test uitgevoerd.
- **NOG ONDERZOEKEN:** dynamische Liquid-bestandsnamen, Shopify-injectie en appcode kunnen buiten statische letterlijke referenties vallen.
- Afwezigheid van een statische inkomende referentie is nadrukkelijk geen bewijs dat een bestand veilig kan worden verwijderd.

## 3. Classificatiedefinities

| Classificatie | Betekenis |
| --- | --- |
| `ACTIVE_LIVE` | Staat direct in de live JSON-configuratie, is de globale live layout/configuratie of is door actuele instellingen/objecttoewijzingen direct actief bewezen. |
| `REACHABLE_FROM_ACTIVE` | Heeft een statisch of vast dynamisch codepad vanaf een `ACTIVE_LIVE`-bestand; voorwaarden kunnen het pad per route of object uitschakelen. |
| `AVAILABLE_NOT_ACTIVE` | Bestaat in het live theme/repository, maar komt niet in de huidige live JSON voor of een actuele instelling maakt het pad niet actief. |
| `LEGACY_OR_ORPHAN_CANDIDATE` | Heeft geen gevonden externe inkomende referentie en/of bevat aantoonbare oude of risicovolle code. Dit is alleen een onderzoekskandidaat, nooit verwijderbewijs. |
| `BACKUP_OR_DEBUG` | Bestandsnaam en inhoud wijzen aantoonbaar op backup-, QA- of debuggebruik; het bestand is geen actieve primaire assetreferentie. |
| `DYNAMIC_OR_NOT_PROVEN` | Gebruik hangt af van Shopify-runtime, een niet onderzochte route, Theme Editor, appinjectie of andere niet statisch bewijsbare toestand. |

Wanneer meerdere labels mogelijk zijn, prevaleert het concrete livebewijs. Een syntactisch bereikbare asset kan bijvoorbeeld door `cart_type != 'drawer'` huidig niet worden geladen; die voorwaarde staat dan expliciet in de matrix.

## 4. Samenvatting

- **BEWEZEN:** het live theme bevat 396 bestanden: 203 assets, 2 configbestanden, 2 layouts, 51 locales, 70 sections/section groups, 45 snippets en 23 templates.
- **BEWEZEN:** de 15 live JSON-templates en twee section groups configureren 26 section-instanties en 157 blocks. Geen section of block is disabled.
- **BEWEZEN:** alle 7.827 producten gebruiken `templates/product.json`; dit activeert `sections/main-product.liquid` en `sections/related-products.liquid`.
- **BEWEZEN:** de homepage gebruikt vijf BadkamerCity-sections met 24 blocks; `page.begrippenlijst.json` bevat 109 actieve term-blocks.
- **BEWEZEN:** `settings.cart_type` is `notification` en predictive search staat aan. De drawerbranch is daardoor niet huidig actief.
- **BEWEZEN:** de V2-switcher wordt voor 3.658 producten door `custom.switch_group` geactiveerd. De legacy-UI vereist `custom.group`; dat veld is bij alle 7.827 producten leeg/afwezig.
- **BEWEZEN:** acht backup/debugbestanden staan in `assets/`; geen daarvan heeft een actieve primaire inkomende referentie.
- **NOG ONDERZOEKEN:** runtimevolledigheid van de V2-dataset, alle app-/pixelinjectie en de businessbedoeling van kandidaat-legacybestanden.

## 5. Actieve template- en sectionmatrix

### 5.1 Live JSON-templates

Alle onderstaande bestanden bestaan in het live theme en zijn lokaal/live bytegelijk.

| Template | Classificatie | Directe sections en blocks | Object- of routebewijs |
| --- | --- | --- | --- |
| `templates/404.json` | `ACTIVE_LIVE` | `main-404`; 0 blocks | Shopify-systeemroute; concrete runtimehit niet uitgevoerd |
| `templates/article.json` | `ACTIVE_LIVE` configuratie / `DYNAMIC_OR_NOT_PROVEN` runtime | `main-article`; 4 blocks: `featured_image`, `title`, `share`, `content` | Blog-/articleobjecten niet in Admin-inventaris geteld |
| `templates/blog.json` | `ACTIVE_LIVE` configuratie / `DYNAMIC_OR_NOT_PROVEN` runtime | `main-blog`; 0 blocks | Blog-/articleobjecten niet in Admin-inventaris geteld |
| `templates/cart.json` | `ACTIVE_LIVE` | `main-cart-items`, `main-cart-footer`, `featured-collection`; 2 blocks: `subtotal`, `buttons` | Shopify-cartsysteemroute |
| `templates/collection.category-landing.json` | `ACTIVE_LIVE` | `main-category-landing`; 4 `subcategory`-blocks | Toegewezen aan 13 collecties |
| `templates/collection.json` | `ACTIVE_LIVE` | `main-collection-banner`, `main-collection-product-grid`; 0 blocks | Toegewezen aan 188 collecties |
| `templates/index.json` | `ACTIVE_LIVE` | Vijf home-sections; 24 blocks | Actieve homepageconfiguratie |
| `templates/list-collections.json` | `ACTIVE_LIVE` | `main-list-collections`; 0 blocks | Shopify-collectie-indexroute |
| `templates/page.begrip.json` | `ACTIVE_LIVE` | `main-glossary-page`; 0 blocks | Toegewezen aan 109 pagina's |
| `templates/page.begrippenlijst.json` | `ACTIVE_LIVE` | `main-glossary`; 109 `term`-blocks | Toegewezen aan 1 pagina |
| `templates/page.contact.json` | `ACTIVE_LIVE` | `main-page`, `contact-form`; 0 blocks | Toegewezen aan 1 pagina |
| `templates/page.json` | `ACTIVE_LIVE` configuratie / `DYNAMIC_OR_NOT_PROVEN` toewijzing | `main-page`; 0 blocks | Geen pagina met leeg/default suffix; 6 pagina's melden suffix `page`, maar `page.page.json` ontbreekt |
| `templates/password.json` | `ACTIVE_LIVE` configuratie / `DYNAMIC_OR_NOT_PROVEN` runtime | `email-signup-banner`; 3 blocks: `heading`, `paragraph`, `email_form` | Passwordmodus is niet als actief vastgesteld |
| `templates/product.json` | `ACTIVE_LIVE` | `main-product`, `related-products`; 8 blocks | Toegewezen aan alle 7.827 producten |
| `templates/search.json` | `ACTIVE_LIVE` | `main-search`; 0 blocks | Shopify-zoekroute; predictive search staat aan |

### 5.2 Section groups

| Bestand | Classificatie | Configuratie |
| --- | --- | --- |
| `sections/header-group.json` | `ACTIVE_LIVE` | `header`; 0 blocks; menu `main-menu`; desktoptype `dropdown` |
| `sections/footer-group.json` | `ACTIVE_LIVE` | `footer`; 3 blocks: twee `link_list` en een `text`; beide linklijsten gebruiken menu `footer` |

### 5.3 Niet-JSON templates en layouts

| Bestanden | Classificatie | Bewijs |
| --- | --- | --- |
| `layout/theme.liquid` | `ACTIVE_LIVE` | Globale storefrontlayout; laadt header/footer groups, globale scripts/styles en `content_for_header`/`content_for_layout` |
| `layout/password.liquid` | `DYNAMIC_OR_NOT_PROVEN` | Bestaat live; passwordmodus niet vastgesteld; bevat eigen header/footer sections en dynamische injectie |
| Zeven `templates/customers/*.json` | `AVAILABLE_NOT_ACTIVE` | Bestaan live, maar accountmodel is `NEW_CUSTOMER_ACCOUNTS`; klassiek theme-accountpad is daardoor niet het bewezen actieve model |
| `templates/gift_card.liquid` | `DYNAMIC_OR_NOT_PROVEN` | Bestaat live; gift-cardruntime en uitgegeven giftcards zijn niet onderzocht |

### 5.4 Actieve instellingen en conditionele paden

| Pad | Actuele toestand | Classificatie/conclusie |
| --- | --- | --- |
| Cart notification | `cart_type = notification`; header rendert `cart-notification` en laadt `cart-notification.js` | `ACTIVE_LIVE` / dynamische sectionresponses `REACHABLE_FROM_ACTIVE` |
| Cart drawer | Layout rendert drawer alleen bij `cart_type = drawer` | `AVAILABLE_NOT_ACTIVE` in de huidige configuratie |
| Predictive search | `predictive_search_enabled = true` | `ACTIVE_LIVE`; `sections/predictive-search.liquid` is dynamisch bereikbaar |
| Scroll reveal | `animations_reveal_on_scroll` is leeg | `animations.js` is syntactisch gekoppeld maar huidig niet als geladen bewezen |
| Collection quick add | Instelling ontbreekt in actieve collectie/cartsection en schemadefault is `none` | Standard/bulk quick-addcode is beschikbaar, huidig niet actief bewezen |
| Pickup availability | Actieve `main-product` geeft `show_pickup_availability: false` door | Section/script beschikbaar, huidig niet actief |
| Theme editor | `theme-editor.js` wordt alleen onder design-modecondities geladen | `DYNAMIC_OR_NOT_PROVEN` buiten de storefront |

## 6. Volledige onderzochte bestandenmatrix

De onderstaande indeling is sluitend voor alle 396 bestanden. Exact benoemde groepen plus de expliciete complementregels voorkomen dat een niet-opgesomd bestand stilzwijgend als ongebruikt wordt beschouwd.

### 6.1 Config en layouts - 4 bestanden

| Bestanden | Aantal | Classificatie |
| --- | ---: | --- |
| `config/settings_data.json`, `layout/theme.liquid` | 2 | `ACTIVE_LIVE` |
| `config/settings_schema.json` | 1 | `AVAILABLE_NOT_ACTIVE`; Theme Editor-schema, geen storefrontrenderbestand |
| `layout/password.liquid` | 1 | `DYNAMIC_OR_NOT_PROVEN` |

### 6.2 Templates - 23 bestanden

| Bestanden | Aantal | Classificatie |
| --- | ---: | --- |
| De 15 JSON-templates uit paragraaf 5.1 | 15 | `ACTIVE_LIVE` als live configuratie; runtimebeperkingen per rij |
| `templates/customers/account.json`, `activate_account.json`, `addresses.json`, `login.json`, `order.json`, `register.json`, `reset_password.json` | 7 | `AVAILABLE_NOT_ACTIVE` onder `NEW_CUSTOMER_ACCOUNTS` |
| `templates/gift_card.liquid` | 1 | `DYNAMIC_OR_NOT_PROVEN` |

### 6.3 Sections en section groups - 70 bestanden

| Groep | Aantal | Bestanden |
| --- | ---: | --- |
| `ACTIVE_LIVE` groups | 2 | `header-group.json`, `footer-group.json` |
| `ACTIVE_LIVE` direct uit live JSON | 25 | `contact-form`, `email-signup-banner`, `featured-collection`, `footer`, `header`, `home-brand-rail`, `home-category-grid`, `home-hero`, `home-mijn-badkamercity`, `home-shop-by-style`, `main-404`, `main-article`, `main-blog`, `main-cart-footer`, `main-cart-items`, `main-category-landing`, `main-collection-banner`, `main-collection-product-grid`, `main-glossary`, `main-glossary-page`, `main-list-collections`, `main-page`, `main-product`, `main-search`, `related-products` |
| `REACHABLE_FROM_ACTIVE` via vaste sectionresponses | 5 | `cart-icon-bubble`, `cart-live-region-text`, `cart-notification-button`, `cart-notification-product`, `predictive-search` |
| `LEGACY_OR_ORPHAN_CANDIDATE` | 6 | `bc-related-products`, `main-collection-category-landing`, `product-description`, `product-info`, `product-media`, `product-specs` |
| `DYNAMIC_OR_NOT_PROVEN` | 2 | `main-password-header`, `main-password-footer` |
| `AVAILABLE_NOT_ACTIVE` | 30 | `announcement-bar`, `apps`, `bulk-quick-order-list`, `cart-drawer`, `collage`, `collapsible-content`, `collection-list`, `custom-liquid`, `featured-blog`, `featured-product`, `image-banner`, `image-with-text`, `main-account`, `main-activate-account`, `main-addresses`, `main-login`, `main-order`, `main-register`, `main-reset-password`, `multicolumn`, `multirow`, `newsletter`, `page`, `pickup-availability`, `quick-order-list`, `rich-text`, `short-specs`, `slideshow`, `usps`, `video` |

Alle namen in deze tabel onder `sections/` eindigen op `.liquid`, behalve de twee expliciet genoemde `.json`-groups.

### 6.4 Snippets - 45 bestanden

| Groep | Aantal | Bestanden |
| --- | ---: | --- |
| `REACHABLE_FROM_ACTIVE` | 36 | `article-card`, `bc-card-product-search`, `bc-product-spec-header`, `bc-product-spec-row`, `bc-product-switcher`, `bc-search-usp-strip`, `buy-buttons`, `card-collection`, `card-product`, `cart-drawer`, `cart-notification`, `country-localization`, `facets`, `gift-card-recipient-form`, `header-drawer`, `header-search`, `icon-accordion`, `icon-with-text`, `language-localization`, `loading-spinner`, `meta-tags`, `pagination`, `price`, `price-facet`, `product-media-gallery`, `product-media-modal`, `product-thumbnail`, `product-variant-options`, `product-variant-picker`, `progress-bar`, `quantity-input`, `share-button`, `social-icons`, `swatch`, `swatch-input`, `unit-price` |
| `LEGACY_OR_ORPHAN_CANDIDATE` | 6 | `bc-category-icon`, `bc-product-short-specs`, `header-dropdown-menu`, `header-mega-menu`, `product-media`, `product-pros-cons` |
| `AVAILABLE_NOT_ACTIVE` | 3 | `quick-order-list`, `quick-order-list-row`, `quick-order-product-row` |

Alle namen in deze tabel staan onder `snippets/` en eindigen op `.liquid`.

### 6.5 Assets - 203 bestanden

| Groep | Aantal | Definitie |
| --- | ---: | --- |
| `REACHABLE_FROM_ACTIVE` | 87 | Statisch bereikbaar vanaf live layout/JSON; exacte lijst hieronder |
| `BACKUP_OR_DEBUG` | 8 | Exacte lijst in paragraaf 9 |
| `LEGACY_OR_ORPHAN_CANDIDATE` | 1 | `component-product-pros-cons.css`; alleen bedoeld voor het niet aangeroepen `product-pros-cons`-snippet en zelf nergens gerefereerd |
| `DYNAMIC_OR_NOT_PROVEN` | 5 | `customer.css`, `customer.js`, `password-modal.js`, `section-password.css`, `template-giftcard.css` |
| `AVAILABLE_NOT_ACTIVE` | 102 | Alle overige bestanden onder `assets/`: het complement van de vier exact gedefinieerde groepen hierboven |

De 87 statisch bereikbare assets zijn:

```text
animations.js
base.css
bc-product-switcher.js
cart.js
cart-drawer.js
cart-notification.js
component-accordion.css
component-article-card.css
component-card.css
component-cart.css
component-cart-drawer.css
component-cart-items.css
component-cart-notification.css
component-collection-hero.css
component-complementary-products.css
component-deferred-media.css
component-discounts.css
component-facets.css
component-list-menu.css
component-list-payment.css
component-list-social.css
component-localization-form.css
component-mega-menu.css
component-menu-drawer.css
component-model-viewer-ui.css
component-newsletter.css
component-pagination.css
component-pickup-availability.css
component-predictive-search.css
component-price.css
component-product-model.css
component-product-variant-picker.css
component-rating.css
component-search.css
component-show-more.css
component-slider.css
component-swatch.css
component-swatch-input.css
component-totals.css
component-volume-pricing.css
constants.js
details-disclosure.js
details-modal.js
facets.js
global.js
icon-false.svg
icon-true.svg
localization-form.js
magnify.js
main-search.js
mask-blobs.css
media-gallery.js
newsletter-section.css
pickup-availability.js
predictive-search.js
price-per-item.js
product-form.js
product-info.js
product-modal.js
product-model.js
product-switcher-data.json
pubsub.js
quantity-popover.css
quantity-popover.js
quick-add.css
quick-add.js
quick-add-bulk.js
quick-order-list.css
quick-order-list.js
recipient-form.js
search-form.js
section-blog-post.css
section-collection-list.css
section-contact-form.css
section-email-signup-banner.css
section-footer.css
section-image-banner.css
section-main-blog.css
section-main-glossary.css
section-main-glossary-page.css
section-main-page.css
section-main-product.css
section-related-products.css
share.js
show-more.js
template-collection.css
theme-editor.js
```

`REACHABLE_FROM_ACTIVE` is geen claim dat elk bestand op iedere request wordt geladen. De bekende false/conditionele paden staan in paragraaf 5.4.

### 6.6 Locales - 51 bestanden

Alle 51 bestanden onder `locales/` zijn `DYNAMIC_OR_NOT_PROVEN`: Liquid `t`-filters en Shopify-locale-resolutie kiezen keys runtime. De enige gepubliceerde taal is Nederlands, maar fallback-, schema- en Theme Editor-gebruik maken een statische bestandsverwijderconclusie onverantwoord.

## 7. Auditverdachten

| Bestand | Classificatie | Inkomend | Uitgaand | Relatie met actieve templates | Bekend risico / bewijs | Aanbevolen vervolgcategorie |
| --- | --- | --- | --- | --- | --- | --- |
| `sections/product-info.liquid` | `LEGACY_OR_ORPHAN_CANDIDATE` | Geen externe referentie gevonden | `price`, `product-variant-picker`, `buy-buttons` | Niet in `product.json`; geïntegreerde functie zit in `main-product` | Mist aantoonbaar dezelfde `block`, `product_form_id` en `section_id`-context als de actieve implementatie | Gerichte runtimevalidatie, daarna menselijke behoud-/opruimbeslissing |
| `sections/product-media.liquid` | `LEGACY_OR_ORPHAN_CANDIDATE` | Geen | `product-media-gallery` | Niet in actief producttemplate | Geeft ongedefinieerde `variant_images` door; eerder door Theme Check gemeld | Niet activeren; apart valideren voor eventuele opruimtaak |
| `sections/product-description.liquid` | `LEGACY_OR_ORPHAN_CANDIDATE` | Geen | Geen bestandreferenties; leest `product.description` | Niet in actief producttemplate | Dubbele losse productbeschrijving naast actieve `description`-block | Business-/runtimevalidatie voor behoudbesluit |
| `sections/product-specs.liquid` | `LEGACY_OR_ORPHAN_CANDIDATE` | Geen | `bc-product-spec-header`, `bc-product-spec-row` | Niet in actief producttemplate; dezelfde snippets zijn wel actief vanuit `main-product` | Bevat `product.metafields.vendor` en `#`-uitleglinks; Admin bewees geen `vendor`-metafielddefinitie | Niet activeren; datamodelbesluit in latere taak |
| `sections/bc-related-products.liquid` | `LEGACY_OR_ORPHAN_CANDIDATE` | Geen | `{% section 'related-products' %}` | Niet in `product.json`; `related-products` staat daar al direct | Section-in-section is vermoedelijk ongeldig; dubbele wrapper | Gerichte Theme Check/runtimevalidatie, daarna opruimbeslissing |
| `snippets/bc-product-short-specs.liquid` | `LEGACY_OR_ORPHAN_CANDIDATE` | Geen | Geen | Niet bereikbaar vanuit actieve producttemplate | Bevat alleen `<!-- Short specs blok verwijderd. -->` | Kandidaat voor latere expliciete opruimtaak |
| `snippets/product-pros-cons.liquid` | `LEGACY_OR_ORPHAN_CANDIDATE` | Geen | Leest `custom.pluspunten` en `custom.aandachtspunten` | Niet aangeroepen; stylesheet evenmin | Beide metafields hebben exact 0/7.827 dekking en geen onderzochte definitie | Databron en businessdoel vaststellen voor behoudbesluit |
| `sections/main-product.liquid` | `ACTIVE_LIVE` | `templates/product.json` | 20 snippets/assets, inclusief beide switcherpaden | Alle 7.827 producten; variant-pickerblock actief | 3.223 regels/146.809 bytes; twee switcherarchitecturen, inline code, `product.metafields.vendor` en twee `#`-uitleglinks | Behouden; gerichte runtime- en regressietests vóór latere wijziging |
| `assets/global.js` | `REACHABLE_FROM_ACTIVE` | `layout/theme.liquid` | Vaste DOM/sectionroutes; legacy `BCProductSwitcher` | Globaal op storefront | Legacy switcher initialiseert op `[data-bc-product-switcher]`; bevat debugwaarschuwingen en een fout gecodeerd vinkje (`âœ“`) in een aanvullend codepad | Behouden; later isoleren/testen, geen architectuurbesluit in deze taak |
| `snippets/bc-product-switcher.liquid` | `REACHABLE_FROM_ACTIVE` | `main-product` bij niet-lege `custom.switch_group` | `bc-product-switcher.js`, `product-switcher-data.json` | V2-pad op maximaal de 3.658 producten met triggerdata | Script wordt per gerenderde switcher toegevoegd; datasetdekking niet tegen alle Admin-handles gevalideerd | Behouden en representatief runtime testen |
| `assets/bc-product-switcher.js` | `REACHABLE_FROM_ACTIVE` | V2-snippet | Fetch van `product-switcher-data.json`; navigatie naar bestaand product | Alleen wanneer V2-root bestaat | Logt `console.info` bij initialisatie/rendering; runtimefouten en matchvolledigheid niet getest | Behouden; logging/performance later apart beoordelen |
| `assets/product-switcher-data.json` | `REACHABLE_FROM_ACTIVE` | V2-snippet en V2-JavaScript | Geen bestandsreferenties | V2-databron | 1.894.030 bytes; 433 unieke groepen, 560 menu's en 3.383 unieke producthandles; Admin heeft 3.658 producten met `switch_group`, dus gelijkheid/volledigheid is niet bewezen | Data-eigenaar, generatieproces en volledige vergelijking vaststellen |

**OPEN BESLISSING:** geen van de kandidaatbestanden mag op basis van deze matrix worden verwijderd. Eigenaarschap, businessbedoeling, runtimebewijs en een aparte implementatie-/opruimopdracht zijn vereist.

## 8. Bereikbaarheid van beide switchers

### 8.1 V2-switcher

1. `templates/product.json` is aan alle 7.827 producten toegewezen en bevat een actief `variant_picker`-block.
2. `sections/main-product.liquid` leest `product.metafields.custom.switch_group`.
3. Bij een niet-lege waarde rendert de actieve variant-pickerbranch `snippets/bc-product-switcher.liquid`.
4. Het snippet maakt `[data-bc-product-switcher-v2]`, geeft groep/handle/URL door en laadt `bc-product-switcher.js` plus `product-switcher-data.json`.
5. Admin-bewijs: `custom.switch_group` is gevuld op 3.658 van 7.827 producten (46,74%).

**BEWEZEN:** het V2-codepad en de trigger zijn actief bereikbaar op 3.658 producten.

**NOG ONDERZOEKEN:** de asset bevat 3.383 unieke handles, 275 minder dan het aantal producten met een trigger. Dat verschil is geen automatisch foutbewijs: een volledige setvergelijking tussen Admin-groepen, handles en assetdata is niet uitgevoerd. Runtime-match, ontbrekende groepen, beschikbaarheid en navigatiecorrectheid moeten apart worden getest.

### 8.2 Legacyfallback

1. `main-product` leest `custom.group` en bouwt bij een lege V2-trigger legacygroepdata uit een collectie.
2. De legacy-UI wordt alleen gerenderd bij `current_switch_group == blank` én `current_group != blank`.
3. `global.js` initialiseert `BCProductSwitcher` alleen op een daadwerkelijk gerenderde `[data-bc-product-switcher]`-root.
4. `custom.menu_1` tot en met `custom.menu_5` bepalen optioneel de legacyvelden; anders gebruikt de code vijf hardcoded veldnamen.
5. Admin-bewijs: `custom.group` en alle vijf menuvelden zijn exact op 0 van 7.827 producten gevuld.

**BEWEZEN:** legacycode is onderdeel van de actieve `main-product`/`global.js`-keten.

**BEWEZEN:** met de op 2026-08-04 gemeten Admin-productdata wordt de legacy-UI voor geen product geactiveerd, omdat `custom.group` overal leeg/afwezig is.

**DYNAMIC_OR_NOT_PROVEN:** externe runtime-injectie, ongeïnventariseerde owner types of toekomstige data kunnen niet statisch worden uitgesloten. Dit onderzoek neemt geen architectuurbesluit over behoud of uitfasering.

## 9. Backup- en debugbestanden

| Bestand | Bytes | Relatie met primaire asset | Classificatie |
| --- | ---: | --- | --- |
| `bc-product-switcher.backup-debug.js` | 10.036 | Verschilt van primaire JS | `BACKUP_OR_DEBUG` |
| `bc-product-switcher.js.backup-qa-round-1-20260706-214223` | 11.742 | Verschilt van primaire JS | `BACKUP_OR_DEBUG` |
| `bc-product-switcher.js.backup-qa-round-1-rerun-20260707-110751` | 11.902 | SHA-256 is bytegelijk aan huidige `bc-product-switcher.js` | `BACKUP_OR_DEBUG` |
| `product-switcher-data.backup.json` | 3.731 | Kleine oude dataset; verschilt | `BACKUP_OR_DEBUG` |
| `product-switcher-data.backup-before-production.json` | 6.889 | Kleine pre-productiedataset; verschilt | `BACKUP_OR_DEBUG` |
| `product-switcher-data.json.backup-qa-round-1-20260706-214223` | 1.807.052 | Verschilt van primaire dataset | `BACKUP_OR_DEBUG` |
| `product-switcher-data.json.backup-qa-round-1-rerun-20260707-110751` | 1.894.070 | Verschilt van primaire dataset | `BACKUP_OR_DEBUG` |
| `product-switcher-data.json.backup-qa-round-2-20260707-111611` | 1.894.070 | Verschilt van primaire dataset | `BACKUP_OR_DEBUG` |

**BEWEZEN:** geen actief Liquid-, JSON-, CSS- of JavaScriptbestand verwijst naar deze backupnamen.

**RISICO:** de bestanden staan wel in het live theme en vergroten omvang en verwarringskans. Verwijdering blijft een afzonderlijke, expliciet goedgekeurde taak met runtimebewijs en herstelplan.

## 10. Apps en dynamische injectie

### 10.1 Bewezen

- De 15 live JSON-templates, twee section groups en `settings_data.json` bevatten nul app-blockreferenties en nul app embeds.
- De huidige actieve blockconfiguratie bevat geen `shopify://apps/...`-type.
- De volgende sections ondersteunen schema-/rendertechnisch `@app`: `apps`, `featured-product`, `footer`, `header`, `main-article`, `main-cart-footer`, `main-product`, `newsletter`.
- Van die lijst staan `footer`, `header`, `main-article`, `main-cart-footer` en `main-product` in live JSON; daarin is geen actief `@app`-block geconfigureerd.
- `layout/theme.liquid`, `layout/password.liquid` en `templates/gift_card.liquid` bevatten `content_for_header`.
- `layout/theme.liquid` en `layout/password.liquid` bevatten `content_for_layout`.
- `main-cart-footer` bevat `content_for_additional_checkout_buttons`.
- `card-product`, `main-product` en `featured-product` bevatten statische `reviews.*`-metafieldpaden; daaruit blijkt niet welke app of welk proces eigenaar is.

### 10.2 Niet toegankelijk

**NIET TOEGANKELIJK:** een volledige lijst van geïnstalleerde apps, sales channels, web pixels, script tags, checkout-extensies, app-abonnementen, consenttools, externe dashboards en buiten theme-JSON werkende injectie.

Daarom is de juiste conclusie: **geen app blocks of embeds bewezen in de actieve JSON**, niet: “er bestaan geen apps”. Er zijn geen aanvullende scopes aangevraagd.

## 11. Content- en navigatiekoppelingen

| Onderdeel | Themegebruik | Admin-/configbewijs | Status |
| --- | --- | --- | --- |
| Header | `header-group.json` geeft `main-menu` aan `header.liquid`; custom desktop/mobilemenu loopt over maximaal drie menuniveaus | `main-menu` bestaat en volledige structuur staat in Admin-inventaris | `ACTIVE_LIVE` |
| Footer | Twee actieve `link_list`-blocks gebruiken beide menu `footer` | Menu bestaat; volledige structuur staat in Admin-inventaris | `ACTIVE_LIVE` |
| Homepage categorieën | `home-category-grid` gebruikt `source_mode: menu` en menu `main-menu` | Acht block-collectionvelden zijn leeg, maar de actieve bronmodus is menu | `ACTIVE_LIVE` met lege alternatieve velden |
| Homepage overige links | Hero/banner/stijl/content/brandsections | 17 linkinstellingen en 14 collectioninstellingen zijn leeg | **BEWEZEN placeholder/leeg**; bedoeling `[NOG ONDERZOEKEN]` |
| Header secundaire links | Zes hardcoded `href="#"`: Inspiratie, Advies, #MijnBadkamercity, Showrooms, Afspraak maken, Zakelijk | Geen doelresource gekoppeld | **BEWEZEN ongeldige placeholderdoelen** |
| Wishlist | Header linkt hardcoded naar `/pages/verlanglijst` | Paginabestaan/-publicatie is in dit rapport niet afzonderlijk bewezen | `DYNAMIC_OR_NOT_PROVEN` |
| Category landing | Vier subcategoryblocks linken naar `badmeubel-sets`, `losse-onderkasten`, `toebehoren`, `toiletmeubels` | Deze collectiehandles bestaan in Admin-navigatiebewijs; het template is aan 13 collecties toegewezen | `ACTIVE_LIVE` |
| Category landing tekst | Dezelfde vier blocks bevatten “Voeg hier een korte omschrijving...” | Actief gedeeld template | **BEWEZEN placeholdercontent** |
| Begrippen | 109 pagina's gebruiken `page.begrip`; één pagina gebruikt `page.begrippenlijst`; detailtemplate linkt naar `/pages/begrippenlijst` | Toewijzingen bewezen | `ACTIVE_LIVE` |
| Zes pagina's met suffix `page` | Live bevat `page.json`, niet `page.page.json` | Admin meldt zes keer suffix `page` | `DYNAMIC_OR_NOT_PROVEN`; fallback/bedoeling `[NOG ONDERZOEKEN]` |
| Product specificatie-uitleg | Actieve `main-product` bevat twee `uitleg_url: '#'`-waarden | Geen echte begrippenpagina gekoppeld | **BEWEZEN placeholderdoelen** |

Deze taak heeft geen labels, menu-items, collectie-inhoud, pagina's of links hersteld.

## 12. Vierde theme

| Theme | ID | Status |
| --- | ---: | --- |
| `badkamercity-phase-c-paris-rectangle-test-v2` | `192796786954` | **BEWEZEN bestaand** en `UNPUBLISHED` |

- Eigenaar: **NOG ONDERZOEKEN**.
- Exact doel: **NOG ONDERZOEKEN**.
- Reden van ontstaan en relatie met Phase C Paris Rectangle: **NOG ONDERZOEKEN**.
- Het theme is niet gepulld, gepusht, gewijzigd, hernoemd, verwijderd of gepubliceerd.

## 13. Onbewezen en open beslissingen

### Niet toegankelijk

- Volledige app-, pixel-, script- en externe-integratielijst.
- Runtime-inhoud die Shopify of apps uitsluitend via `content_for_header`, checkoutcontent of externe configuratie injecteren.

### Nog onderzoeken

- Browserruntime per actieve template, inclusief de routes artikel, blog, password en gift card.
- Exacte afhandeling van zes pagina's met suffix `page` zonder `page.page.json`.
- Volledige één-op-éénvergelijking tussen 3.658 Admin-producten met `switch_group` en de 3.383 handles in de V2-asset.
- Eigenaarschap en generatieproces van `product-switcher-data.json`.
- Eigenaarschap, doel en ontstaansreden van theme `192796786954`.
- Bestaan/publicatiestatus en businessbedoeling van hardcoded paginadoelen zoals `/pages/verlanglijst`.
- Betekenis van lege homepagevelden wanneer een section een alternatieve databron gebruikt.

### Open beslissing

- Of de legacyfallback blijft, wordt gemigreerd of later wordt verwijderd.
- Of kandidaat-legacy en backup/debugbestanden na aanvullend runtimebewijs behouden of in een aparte taak verwijderd worden.
- Welke bevoegde read-only bron de ontbrekende volledige app-/pixelinventaris mag leveren.
- Welke placeholderlinks en content zakelijke doelwaarden krijgen.

## 14. Risico's

| Risico | Bewijs | Gevolg |
| --- | --- | --- |
| Dubbele switcherarchitectuur | V2 in eigen snippet/assets; legacy in `main-product`/`global.js` | Regressie- en onderhoudsrisico bij productwijzigingen |
| Dataset/triggeraantal verschilt | 3.658 Admin-triggers versus 3.383 assethandles | Mogelijk ontbrekende, afwijkende of historische datasetkoppelingen; nog geen foutbewijs |
| Grote actieve productketen | `main-product` 146.809 bytes; dataset 1.894.030 bytes | Performance- en wijzigingsrisico |
| Kandidaatsecties kunnen defect zijn | Geen inkomende refs; ongedefinieerde context en section-nesting | Theme Editor kan defect gedrag activeren |
| Backup/debug in live theme | Acht benoemde bestanden; V2 logt `console.info` | Verwarring, omvang en runtime-logruis |
| Placeholdercontent | Zes headerhashlinks, twee producthashlinks, 17 lege home-links en vier categorybeschrijvingen | Dode journeys en onvolledige content |
| Verborgen integraties | Geen actieve JSON-apprefs, maar dynamische injectie bestaat en volledige lijst is niet toegankelijk | Onzichtbare afhankelijkheden kunnen later breken |
| Statische false negatives | Dynamische namen en Shopify section rendering | Een “geen referentie”-conclusie kan onterecht als verwijderbewijs worden gebruikt |

## 15. Aanbevolen veilige vervolgstappen

1. De projecteigenaar heeft dit rapport en de onderzoeksclassificaties op 2026-08-05 goedgekeurd; `BC-DISC-001` is `DONE`. Deze goedkeuring is geen verwijder-, wijzigings-, runtime- of implementatietoestemming.
2. `BC-DISC-002` is uitsluitend projectadministratief de actieve volgende read-only taak op `READY`; inhoudelijke uitvoering vereist een afzonderlijke expliciete startopdracht.
3. Plan afzonderlijk read-only runtimeonderzoek op representatieve routes en producten: V2-product, product zonder switchgroep, cart notification, predictive search, categorie, begrip en de zes `page`-suffixgevallen.
4. Vergelijk in een aparte read-only datataak alle Admin-`switch_group`-waarden en producthandles met de V2-dataset; leg bronhouder en generatieproces vast.
5. Neem pas daarna een menselijk architectuurbesluit over de legacyfallback en een afzonderlijk opruimbesluit over kandidaat- en backupbestanden.
6. Houd implementatie, themebeheer, Shopify-mutaties en aanvullende scopes geblokkeerd.

## 16. Menselijke goedkeuring

De BadkamerCity-projecteigenaar heeft `docs/ACTIVE_THEME_USAGE.md` en masterplan versie 0.5 op 2026-08-05 menselijk beoordeeld en `BC-DISC-001` als afgerond read-only onderzoek goedgekeurd.

De goedkeuring bevestigt uitsluitend:

- de classificaties zijn onderzoeksbevindingen;
- `LEGACY_OR_ORPHAN_CANDIDATE` is geen verwijdertoestemming;
- `BACKUP_OR_DEBUG` is geen verwijdertoestemming;
- alle runtime-, app-, pixel- en switcherdatabeperkingen blijven bestaan;
- geen themebestand mag worden gewijzigd of verwijderd;
- `BC-DISC-001` mag naar `DONE`;
- `BC-DISC-002` mag als actieve volgende read-only taak naar `READY`, zonder inhoudelijke uitvoering binnen deze administratieve opdracht.

De goedkeuring geeft buiten deze twee projectadministratiedocumenten geen toestemming voor Shopify-datawijzigingen, theme-code- of repositorybestandswijzigingen, bestandsverwijderingen, themebeheer, aanvullende scopes, appwijzigingen of implementatiewerk. Alle risico's en open beslissingen uit dit rapport blijven gelden.

## 17. Integriteitsbevestiging

Tijdens `BC-DISC-001` is:

- geen GraphQL-mutatie uitgevoerd;
- `--allow-mutations` nooit gebruikt;
- geen Shopify-data gewijzigd;
- geen theme-code gewijzigd;
- geen theme gepusht, gepulld, gepubliceerd, verwijderd, hernoemd of aangepast;
- geen app geïnstalleerd of geconfigureerd;
- geen aanvullende scope aangevraagd;
- geen token of credential getoond;
- tijdens de inhoudelijke onderzoeksuitvoering geen commit gemaakt en niets gepusht.

Alleen `docs/ACTIVE_THEME_USAGE.md` en `docs/MASTERPLAN.md` zijn gewijzigd en worden na de menselijke goedkeuring als projectadministratie gecommit. Shopify-data, themes en theme-code blijven ongewijzigd.
