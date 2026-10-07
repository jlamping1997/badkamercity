# BadkamerCity — complete thema-component- en instellingenreferentie
> **Automatisch samengesteld op 7 oktober 2026 uit de werkelijk live Shopify-theme-code #194864677130.** Dit is een code-index, geen bewijs dat iedere sectie ingeschakeld is of alle instellingen ingevuld zijn. Raadpleeg voor feitelijke waarden van actieve JSON-templates, de Shopify Theme Editor en Admin. De broncode blijft leidend. Aangemaakte referenties zijn statisch uit Liquid gedetecteerd en kunnen aanroepen binnen comments bevatten.

## Zo gebruik je dit bestand
Zoek je een visuele functie, zoek dan op sectienaam of setting-ID. Open het corresponderende `sections/*.liquid`; controleer `templates/*.json` voor actieve configuratie en `snippets/` plus `assets/` voor werking. **De instellingen hieronder zijn de configureerbare mogelijkheden (schema), niet noodzakelijk de huidige waarden.** Gebruik [THEME_CODE_MAP_2026-10-07.json](THEME_CODE_MAP_2026-10-07.json) voor machine-readable dependencies en [SHOPIFY_ADMIN_STRUCTURE_2026-10-07.json](SHOPIFY_ADMIN_STRUCTURE_2026-10-07.json) voor Admin-menu's/collecties/metafield-definities.

### JSON-template-index

| Template | Geconfigureerde secties in volgorde | Aandachtspunt |
| --- | --- | --- |
| `templates/404.json` | `main-404` |  |
| `templates/article.json` | `main-article` |  |
| `templates/blog.json` | `main-blog` |  |
| `templates/cart.json` | `main-cart-items` → `main-cart-footer` → `featured-collection` |  |
| `templates/collection.bc-meubelhub.json` | `bc-meubelhub` | Badkamermeubels via Admin-suffix |
| `templates/collection.category-landing.json` | `main-category-landing` → `bc-collection-advice` | Navigatiehub |
| `templates/collection.json` | `main-collection-banner` → `main-collection-product-grid` → `bc-collection-advice` | Productlijst met native filtering |
| `templates/customers/account.json` | `main-account` |  |
| `templates/customers/activate_account.json` | `main-activate-account` |  |
| `templates/customers/addresses.json` | `main-addresses` |  |
| `templates/customers/login.json` | `main-login` |  |
| `templates/customers/order.json` | `main-order` |  |
| `templates/customers/register.json` | `main-register` |  |
| `templates/customers/reset_password.json` | `main-reset-password` |  |
| `templates/index.json` | `home-hero` → `home-category-grid` → `home-popular-products` → `home-complete-bathroom` → `home-shop-by-style` → `home-brand-rail` → `home-mijn-badkamercity` → `home-help-cta` |  |
| `templates/list-collections.json` | `main-list-collections` |  |
| `templates/page.begrip.json` | `main-glossary-page` |  |
| `templates/page.begrippenlijst.json` | `main-glossary` |  |
| `templates/page.contact.json` | `main-page` → `contact-form` |  |
| `templates/page.json` | `main-page` |  |
| `templates/password.json` | `email-signup-banner` |  |
| `templates/product.bc-hotbath-data.json` | `main-product` | Speciale pilot-/testtemplate; niet gelijkstellen aan standaard PDP |
| `templates/product.bc-hotbath-pilot.json` | `main-product` | Speciale pilot-/testtemplate; niet gelijkstellen aan standaard PDP |
| `templates/product.json` | `main-product` → `related-products` |  |
| `templates/search.json` | `main-search` |  |

## Sectie-index

Elke sectie hieronder heeft een bestand in `sections/`. Aanroepen via snippets/asset-URLs zijn alleen statisch gedetecteerd. Let op: het JSON-template **kan deze sectie niet gebruiken**, of een block/setting kan uitstaan.


### 1. `sections/announcement-bar.liquid`
**Shopify Theme Editor naam:** t:sections.announcement-bar.name. **Settings:** 7. **Blocktypen:** 1.
**Aangeroepen door JSON-template(s):** Geen directe JSON-template-match aangetroffen — mogelijk sectiegroup/dynamisch/niet actief.
**Statische code-afhankelijkheden:** `snippets/country-localization.liquid`, `snippets/language-localization.liquid`, `snippets/social-icons.liquid`, `assets/component-list-social.css`, `assets/component-slider.css`, `assets/component-slideshow.css`, `assets/icon-arrow.svg`, `assets/icon-caret.svg`, `assets/theme-editor.js`

| Setting-ID | Type | Label (uit schema) |
| --- | --- | --- |
| `auto_rotate` | `checkbox` | t:sections.announcement-bar.settings.auto_rotate.label |
| `change_slides_speed` | `range` | t:sections.announcement-bar.settings.change_slides_speed.label |
| `color_scheme` | `color_scheme` | t:sections.all.colors.label |
| `show_line_separator` | `checkbox` | t:sections.header.settings.show_line_separator.label |
| `show_social` | `checkbox` | t:sections.announcement-bar.settings.show_social.label |
| `enable_country_selector` | `checkbox` | t:sections.announcement-bar.settings.enable_country_selector.label |
| `enable_language_selector` | `checkbox` | t:sections.announcement-bar.settings.enable_language_selector.label |

**Blocktypen en instelbare velden:**
- `announcement` (t:sections.announcement-bar.blocks.announcement.name): `text`, `link`

### 2. `sections/apps.liquid`
**Shopify Theme Editor naam:** t:sections.apps.name. **Settings:** 1. **Blocktypen:** 1.
**Aangeroepen door JSON-template(s):** Geen directe JSON-template-match aangetroffen — mogelijk sectiegroup/dynamisch/niet actief.
**Statische code-afhankelijkheden:** Geen vaste render-/assetverwijzingen aangetroffen.

| Setting-ID | Type | Label (uit schema) |
| --- | --- | --- |
| `include_margins` | `checkbox` | t:sections.apps.settings.include_margins.label |

**Blocktypen en instelbare velden:**
- `@app` (): geen velden

### 3. `sections/bc-collection-advice.liquid`
**Shopify Theme Editor naam:** BadkamerCity keuzeadvies. **Settings:** 4. **Blocktypen:** 0.
**Aangeroepen door JSON-template(s):** `templates/collection.category-landing.json`, `templates/collection.json`
**Statische code-afhankelijkheden:** `assets/bc-collection.css`, `assets/icon-caret.svg`

| Setting-ID | Type | Label (uit schema) |
| --- | --- | --- |
| `navigation_menu` | `link_list` | Menu voor categorieboom |
| `extra_content` | `richtext` | Aanvullend advies |
| `show_faq` | `checkbox` | Toon veelgestelde vragen bij kranen |
| `show_contact` | `checkbox` | Toon contactblok |

### 4. `sections/bc-meubelhub.liquid`
**Shopify Theme Editor naam:** BadkamerCity meubelhub. **Settings:** 31. **Blocktypen:** 2.
**Aangeroepen door JSON-template(s):** `templates/collection.bc-meubelhub.json`
**Statische code-afhankelijkheden:** `snippets/bc-meubelhub-icon.liquid`, `assets/bc-meubelhub.css`, `assets/bc-meubelhub.js`

| Setting-ID | Type | Label (uit schema) |
| --- | --- | --- |
| `heading` | `text` | Paginatitel (leeg = collectietitel) |
| `eyebrow` | `text` | Bovenregel |
| `intro` | `richtext` | Korte introductie |
| `hero_image` | `image_picker` | Hero afbeelding (vervangbaar) |
| `hero_url` | `url` | Hero afbeelding URL |
| `hero_alt` | `text` | Beschrijving hero afbeelding |
| `hero_usp_1` | `text` | Voordeel 1 |
| `hero_usp_2` | `text` | Voordeel 2 |
| `hero_usp_3` | `text` | Voordeel 3 |
| `shop_heading` | `text` | Titel keuzehulp |
| `type_menu` | `link_list` | Menu: op type |
| `maat_menu` | `link_list` | Menu: op maat |
| `stijl_menu` | `link_list` | Menu: op stijl |
| `merk_menu` | `link_list` | Menu: op merk |
| `show_pending` | `checkbox` | Toon niet-klikbare maat/stijlvoorbeelden tot menu’s gekoppeld zijn |
| `show_brands` | `checkbox` | Merkenblok tonen |
| `brands_heading` | `text` | Titel merkenblok |
| `brands_intro` | `text` | Ondertitel merkenblok |
| `brands_url` | `url` | Bestemming Alle merken (optioneel) |
| `inspiration_image` | `image_picker` | Inspiratieafbeelding (vervangbaar) |
| `inspiration_url` | `url` | Inspiratieafbeelding URL |
| `inspiration_link` | `url` | Stijlenpagina (leeg = keuzeadvies op deze pagina) |
| `service_title_1` | `text` | Servicetitel 1 |
| `service_text_1` | `text` | Serviceuitleg 1 |
| `service_title_2` | `text` | Servicetitel 2 |
| `service_text_2` | `text` | Serviceuitleg 2 |
| `service_title_3` | `text` | Servicetitel 3 |
| `service_text_3` | `text` | Serviceuitleg 3 |
| `service_title_4` | `text` | Servicetitel 4 |
| `service_text_4` | `text` | Serviceuitleg 4 |
| `advice_fallback` | `richtext` | Advies als [SPLIT]-tekst ontbreekt |

**Blocktypen en instelbare velden:**
- `category` (Categoriekaart): `category`, `label`, `caption`, `photo`, `photo_url`, `photo_alt`, `allow_empty`
- `brand` (Merkkaart): `label`, `destination`, `logo`

### 5. `sections/bc-related-products.liquid`
**Shopify Theme Editor naam:** Related Products. **Settings:** 0. **Blocktypen:** 0.
**Aangeroepen door JSON-template(s):** Geen directe JSON-template-match aangetroffen — mogelijk sectiegroup/dynamisch/niet actief.
**Statische code-afhankelijkheden:** `sections/related-products.liquid`

### 6. `sections/bulk-quick-order-list.liquid`
**Shopify Theme Editor naam:** t:sections.quick-order-list.name. **Settings:** 0. **Blocktypen:** 0.
**Aangeroepen door JSON-template(s):** Geen directe JSON-template-match aangetroffen — mogelijk sectiegroup/dynamisch/niet actief.
**Statische code-afhankelijkheden:** `snippets/quick-order-list.liquid`, `assets/quick-order-list.css`, `assets/quick-order-list.js`

### 7. `sections/cart-drawer.liquid`
**Geen direct parsebaar Theme Editor-schema in dit bestand** (mogelijk via vaste sectiegroep of legacy-code).
**Aangeroepen door JSON-template(s):** Geen directe JSON-template-match aangetroffen — mogelijk sectiegroup/dynamisch/niet actief.
**Statische code-afhankelijkheden:** `snippets/cart-drawer.liquid`

### 8. `sections/cart-icon-bubble.liquid`
**Geen direct parsebaar Theme Editor-schema in dit bestand** (mogelijk via vaste sectiegroep of legacy-code).
**Aangeroepen door JSON-template(s):** Geen directe JSON-template-match aangetroffen — mogelijk sectiegroup/dynamisch/niet actief.
**Statische code-afhankelijkheden:** `snippets/bc-header-cart.liquid`

### 9. `sections/cart-live-region-text.liquid`
**Geen direct parsebaar Theme Editor-schema in dit bestand** (mogelijk via vaste sectiegroep of legacy-code).
**Aangeroepen door JSON-template(s):** Geen directe JSON-template-match aangetroffen — mogelijk sectiegroup/dynamisch/niet actief.
**Statische code-afhankelijkheden:** Geen vaste render-/assetverwijzingen aangetroffen.

### 10. `sections/cart-notification-button.liquid`
**Geen direct parsebaar Theme Editor-schema in dit bestand** (mogelijk via vaste sectiegroep of legacy-code).
**Aangeroepen door JSON-template(s):** Geen directe JSON-template-match aangetroffen — mogelijk sectiegroup/dynamisch/niet actief.
**Statische code-afhankelijkheden:** Geen vaste render-/assetverwijzingen aangetroffen.

### 11. `sections/cart-notification-product.liquid`
**Geen direct parsebaar Theme Editor-schema in dit bestand** (mogelijk via vaste sectiegroep of legacy-code).
**Aangeroepen door JSON-template(s):** Geen directe JSON-template-match aangetroffen — mogelijk sectiegroup/dynamisch/niet actief.
**Statische code-afhankelijkheden:** Geen vaste render-/assetverwijzingen aangetroffen.

### 12. `sections/collage.liquid`
**Shopify Theme Editor naam:** t:sections.collage.name. **Settings:** 8. **Blocktypen:** 4.
**Aangeroepen door JSON-template(s):** Geen directe JSON-template-match aangetroffen — mogelijk sectiegroup/dynamisch/niet actief.
**Statische code-afhankelijkheden:** `snippets/card-collection.liquid`, `snippets/card-product.liquid`, `assets/collage.css`, `assets/component-card.css`, `assets/component-deferred-media.css`, `assets/component-modal-video.css`, `assets/component-price.css`, `assets/icon-close.svg`, `assets/icon-play.svg`

| Setting-ID | Type | Label (uit schema) |
| --- | --- | --- |
| `heading` | `inline_richtext` | t:sections.collage.settings.heading.label |
| `heading_size` | `select` | t:sections.all.heading_size.label |
| `desktop_layout` | `select` | t:sections.collage.settings.desktop_layout.label |
| `mobile_layout` | `select` | t:sections.collage.settings.mobile_layout.label |
| `card_styles` | `select` | t:sections.collage.settings.card_styles.label |
| `color_scheme` | `color_scheme` | t:sections.all.colors.label |
| `padding_top` | `range` | t:sections.all.padding.padding_top |
| `padding_bottom` | `range` | t:sections.all.padding.padding_bottom |

**Blocktypen en instelbare velden:**
- `image` (t:sections.collage.blocks.image.name): `image`
- `product` (t:sections.collage.blocks.product.name): `product`, `second_image`
- `collection` (t:sections.collage.blocks.collection.name): `collection`
- `video` (t:sections.collage.blocks.video.name): `cover_image`, `video_url`, `description`

### 13. `sections/collapsible-content.liquid`
**Shopify Theme Editor naam:** t:sections.collapsible_content.name. **Settings:** 13. **Blocktypen:** 1.
**Aangeroepen door JSON-template(s):** Geen directe JSON-template-match aangetroffen — mogelijk sectiegroup/dynamisch/niet actief.
**Statische code-afhankelijkheden:** `snippets/icon-accordion.liquid`, `assets/collapsible-content.css`, `assets/component-accordion.css`, `assets/icon-caret.svg`

| Setting-ID | Type | Label (uit schema) |
| --- | --- | --- |
| `caption` | `text` | t:sections.collapsible_content.settings.caption.label |
| `heading` | `inline_richtext` | t:sections.collapsible_content.settings.heading.label |
| `heading_size` | `select` | t:sections.all.heading_size.label |
| `heading_alignment` | `select` | t:sections.collapsible_content.settings.heading_alignment.label |
| `layout` | `select` | t:sections.collapsible_content.settings.layout.label |
| `container_color_scheme` | `color_scheme` | t:sections.collapsible_content.settings.container_color_scheme.label |
| `color_scheme` | `color_scheme` | t:sections.collapsible_content.settings.section_color_scheme.label |
| `open_first_collapsible_row` | `checkbox` | t:sections.collapsible_content.settings.open_first_collapsible_row.label |
| `image` | `image_picker` | t:sections.collapsible_content.settings.image.label |
| `image_ratio` | `select` | t:sections.collapsible_content.settings.image_ratio.label |
| `desktop_layout` | `select` | t:sections.collapsible_content.settings.desktop_layout.label |
| `padding_top` | `range` | t:sections.all.padding.padding_top |
| `padding_bottom` | `range` | t:sections.all.padding.padding_bottom |

**Blocktypen en instelbare velden:**
- `collapsible_row` (t:sections.collapsible_content.blocks.collapsible_row.name): `heading`, `icon`, `row_content`, `page`

### 14. `sections/collection-list.liquid`
**Shopify Theme Editor naam:** t:sections.collection-list.name. **Settings:** 10. **Blocktypen:** 1.
**Aangeroepen door JSON-template(s):** Geen directe JSON-template-match aangetroffen — mogelijk sectiegroup/dynamisch/niet actief.
**Statische code-afhankelijkheden:** `snippets/card-collection.liquid`, `assets/component-card.css`, `assets/component-slider.css`, `assets/icon-caret.svg`, `assets/section-collection-list.css`

| Setting-ID | Type | Label (uit schema) |
| --- | --- | --- |
| `title` | `inline_richtext` | t:sections.collection-list.settings.title.label |
| `heading_size` | `select` | t:sections.all.heading_size.label |
| `image_ratio` | `select` | t:sections.collection-list.settings.image_ratio.label |
| `columns_desktop` | `range` | t:sections.collection-list.settings.columns_desktop.label |
| `color_scheme` | `color_scheme` | t:sections.all.colors.label |
| `show_view_all` | `checkbox` | t:sections.collection-list.settings.show_view_all.label |
| `columns_mobile` | `select` | t:sections.collection-list.settings.columns_mobile.label |
| `swipe_on_mobile` | `checkbox` | t:sections.collection-list.settings.swipe_on_mobile.label |
| `padding_top` | `range` | t:sections.all.padding.padding_top |
| `padding_bottom` | `range` | t:sections.all.padding.padding_bottom |

**Blocktypen en instelbare velden:**
- `featured_collection` (t:sections.collection-list.blocks.featured_collection.name): `collection`

### 15. `sections/contact-form.liquid`
**Shopify Theme Editor naam:** t:sections.contact-form.name. **Settings:** 5. **Blocktypen:** 0.
**Aangeroepen door JSON-template(s):** `templates/page.contact.json`
**Statische code-afhankelijkheden:** `assets/icon-error.svg`, `assets/icon-success.svg`, `assets/section-contact-form.css`

| Setting-ID | Type | Label (uit schema) |
| --- | --- | --- |
| `heading` | `inline_richtext` | t:sections.contact-form.settings.title.label |
| `heading_size` | `select` | t:sections.all.heading_size.label |
| `color_scheme` | `color_scheme` | t:sections.all.colors.label |
| `padding_top` | `range` | t:sections.all.padding.padding_top |
| `padding_bottom` | `range` | t:sections.all.padding.padding_bottom |

### 16. `sections/custom-liquid.liquid`
**Shopify Theme Editor naam:** t:sections.custom-liquid.name. **Settings:** 4. **Blocktypen:** 0.
**Aangeroepen door JSON-template(s):** Geen directe JSON-template-match aangetroffen — mogelijk sectiegroup/dynamisch/niet actief.
**Statische code-afhankelijkheden:** Geen vaste render-/assetverwijzingen aangetroffen.

| Setting-ID | Type | Label (uit schema) |
| --- | --- | --- |
| `custom_liquid` | `liquid` | t:sections.custom-liquid.settings.custom_liquid.label |
| `color_scheme` | `color_scheme` | t:sections.all.colors.label |
| `padding_top` | `range` | t:sections.all.padding.padding_top |
| `padding_bottom` | `range` | t:sections.all.padding.padding_bottom |

### 17. `sections/email-signup-banner.liquid`
**Shopify Theme Editor naam:** t:sections.email-signup-banner.name. **Settings:** 10. **Blocktypen:** 3.
**Aangeroepen door JSON-template(s):** `templates/password.json`
**Statische code-afhankelijkheden:** `assets/component-newsletter.css`, `assets/email-signup-banner-background-mobile.svg`, `assets/email-signup-banner-background.svg`, `assets/icon-arrow.svg`, `assets/icon-error.svg`, `assets/icon-success.svg`, `assets/newsletter-section.css`, `assets/section-email-signup-banner.css`, `assets/section-image-banner.css`

| Setting-ID | Type | Label (uit schema) |
| --- | --- | --- |
| `show_background_image` | `checkbox` | t:sections.email-signup-banner.settings.show_background_image.label |
| `image` | `image_picker` | t:sections.email-signup-banner.settings.image.label |
| `image_overlay_opacity` | `range` | t:sections.email-signup-banner.settings.image_overlay_opacity.label |
| `image_height` | `select` | t:sections.email-signup-banner.settings.image_height.label |
| `desktop_content_position` | `select` | t:sections.email-signup-banner.settings.desktop_content_position.label |
| `desktop_content_alignment` | `select` | t:sections.email-signup-banner.settings.desktop_content_alignment.label |
| `show_text_box` | `checkbox` | t:sections.email-signup-banner.settings.show_text_box.label |
| `color_scheme` | `color_scheme` | t:sections.all.colors.label |
| `mobile_content_alignment` | `select` | t:sections.email-signup-banner.settings.mobile_content_alignment.label |
| `show_text_below` | `checkbox` | t:sections.email-signup-banner.settings.show_text_below.label |

**Blocktypen en instelbare velden:**
- `heading` (t:sections.email-signup-banner.blocks.heading.name): `heading`, `heading_size`
- `paragraph` (t:sections.email-signup-banner.blocks.paragraph.name): `text`, `text_style`
- `email_form` (t:sections.email-signup-banner.blocks.email_form.name): geen velden

### 18. `sections/featured-blog.liquid`
**Shopify Theme Editor naam:** t:sections.featured-blog.name. **Settings:** 12. **Blocktypen:** 0.
**Aangeroepen door JSON-template(s):** Geen directe JSON-template-match aangetroffen — mogelijk sectiegroup/dynamisch/niet actief.
**Statische code-afhankelijkheden:** `snippets/article-card.liquid`, `assets/component-article-card.css`, `assets/component-card.css`, `assets/component-slider.css`, `assets/icon-caret.svg`, `assets/section-featured-blog.css`

| Setting-ID | Type | Label (uit schema) |
| --- | --- | --- |
| `blog` | `blog` | t:sections.featured-blog.settings.blog.label |
| `post_limit` | `range` | t:sections.featured-blog.settings.post_limit.label |
| `heading` | `inline_richtext` | t:sections.featured-blog.settings.heading.label |
| `heading_size` | `select` | t:sections.all.heading_size.label |
| `columns_desktop` | `range` | t:sections.featured-blog.settings.columns_desktop.label |
| `show_view_all` | `checkbox` | t:sections.featured-blog.settings.show_view_all.label |
| `show_image` | `checkbox` | t:sections.featured-blog.settings.show_image.label |
| `show_date` | `checkbox` | t:sections.featured-blog.settings.show_date.label |
| `show_author` | `checkbox` | t:sections.featured-blog.settings.show_author.label |
| `color_scheme` | `color_scheme` | t:sections.all.colors.label |
| `padding_top` | `range` | t:sections.all.padding.padding_top |
| `padding_bottom` | `range` | t:sections.all.padding.padding_bottom |

### 19. `sections/featured-collection.liquid`
**Shopify Theme Editor naam:** t:sections.featured-collection.name. **Settings:** 23. **Blocktypen:** 0.
**Aangeroepen door JSON-template(s):** `templates/cart.json`
**Statische code-afhankelijkheden:** `snippets/card-product.liquid`, `assets/component-card.css`, `assets/component-price.css`, `assets/component-slider.css`, `assets/icon-caret.svg`, `assets/mask-arch.svg`, `assets/mask-blobs.css`, `assets/price-per-item.js`, `assets/product-form.js`, `assets/quantity-popover.js`, `assets/quick-add-bulk.js`, `assets/quick-add.css`, `assets/quick-add.js`, `assets/quick-order-list.js`, `assets/template-collection.css`

| Setting-ID | Type | Label (uit schema) |
| --- | --- | --- |
| `collection` | `collection` | t:sections.featured-collection.settings.collection.label |
| `products_to_show` | `range` | t:sections.featured-collection.settings.products_to_show.label |
| `title` | `inline_richtext` | t:sections.featured-collection.settings.title.label |
| `heading_size` | `select` | t:sections.all.heading_size.label |
| `description` | `richtext` | t:sections.featured-collection.settings.description.label |
| `show_description` | `checkbox` | t:sections.featured-collection.settings.show_description.label |
| `description_style` | `select` | t:sections.featured-collection.settings.description_style.label |
| `columns_desktop` | `range` | t:sections.featured-collection.settings.columns_desktop.label |
| `enable_desktop_slider` | `checkbox` | t:sections.featured-collection.settings.enable_desktop_slider.label |
| `full_width` | `checkbox` | t:sections.featured-collection.settings.full_width.label |
| `show_view_all` | `checkbox` | t:sections.featured-collection.settings.show_view_all.label |
| `view_all_style` | `select` | t:sections.featured-collection.settings.view_all_style.label |
| `color_scheme` | `color_scheme` | t:sections.all.colors.label |
| `image_ratio` | `select` | t:sections.featured-collection.settings.image_ratio.label |
| `image_shape` | `select` | t:sections.all.image_shape.label |
| `show_secondary_image` | `checkbox` | t:sections.featured-collection.settings.show_secondary_image.label |
| `show_vendor` | `checkbox` | t:sections.featured-collection.settings.show_vendor.label |
| `show_rating` | `checkbox` | t:sections.featured-collection.settings.show_rating.label |
| `quick_add` | `select` | t:sections.main-collection-product-grid.settings.quick_add.label |
| `columns_mobile` | `select` | t:sections.featured-collection.settings.columns_mobile.label |
| `swipe_on_mobile` | `checkbox` | t:sections.featured-collection.settings.swipe_on_mobile.label |
| `padding_top` | `range` | t:sections.all.padding.padding_top |
| `padding_bottom` | `range` | t:sections.all.padding.padding_bottom |

### 20. `sections/featured-product.liquid`
**Shopify Theme Editor naam:** t:sections.featured-product.name. **Settings:** 12. **Blocktypen:** 12.
**Aangeroepen door JSON-template(s):** Geen directe JSON-template-match aangetroffen — mogelijk sectiegroup/dynamisch/niet actief.
**Statische code-afhankelijkheden:** `snippets/buy-buttons.liquid`, `snippets/icon-with-text.liquid`, `snippets/loading-spinner.liquid`, `snippets/price.liquid`, `snippets/product-media-gallery.liquid`, `snippets/product-media-modal.liquid`, `snippets/product-variant-picker.liquid`, `assets/component-accordion.css`, `assets/component-deferred-media.css`, `assets/component-model-viewer-ui.css`, `assets/component-price.css`, `assets/component-product-model.css`, `assets/component-product-variant-picker.css`, `assets/component-rating.css`, `assets/component-swatch-input.css`, `assets/component-swatch.css`, `assets/component-volume-pricing.css`, `assets/icon-arrow.svg`, `assets/icon-minus.svg`, `assets/icon-plus.svg`, `assets/magnify.js`, `assets/media-gallery.js`, `assets/price-per-item.js`, `assets/product-form.js`, `assets/product-info.js`, `assets/product-modal.js`, `assets/product-model.js`, `assets/section-featured-product.css`, `assets/section-main-product.css`, `assets/show-more.js`, `assets/theme-editor.js`
**Rechtstreeks genoemde metafields:** `reviews.rating`, `reviews.rating_count`. Let op: definitiebestaan/gevulde waarden apart controleren.

| Setting-ID | Type | Label (uit schema) |
| --- | --- | --- |
| `product` | `product` | t:sections.featured-product.settings.product.label |
| `color_scheme` | `color_scheme` | t:sections.all.colors.label |
| `secondary_background` | `checkbox` | t:sections.featured-product.settings.secondary_background.label |
| `media_size` | `select` | t:sections.main-product.settings.media_size.label |
| `constrain_to_viewport` | `checkbox` | t:sections.main-product.settings.constrain_to_viewport.label |
| `media_fit` | `select` | t:sections.main-product.settings.media_fit.label |
| `media_position` | `select` | t:sections.featured-product.settings.media_position.label |
| `image_zoom` | `select` | t:sections.main-product.settings.image_zoom.label |
| `hide_variants` | `checkbox` | t:sections.main-product.settings.hide_variants.label |
| `enable_video_looping` | `checkbox` | t:sections.featured-product.settings.enable_video_looping.label |
| `padding_top` | `range` | t:sections.all.padding.padding_top |
| `padding_bottom` | `range` | t:sections.all.padding.padding_bottom |

**Blocktypen en instelbare velden:**
- `@app` (): geen velden
- `text` (t:sections.featured-product.blocks.text.name): `text`, `text_style`
- `title` (t:sections.featured-product.blocks.title.name): `heading_size`
- `price` (t:sections.featured-product.blocks.price.name): geen velden
- `sku` (t:sections.featured-product.blocks.sku.name): `text_style`
- `quantity_selector` (t:sections.featured-product.blocks.quantity_selector.name): geen velden
- `variant_picker` (t:sections.featured-product.blocks.variant_picker.name): `picker_type`, `swatch_shape`
- `buy_buttons` (t:sections.featured-product.blocks.buy_buttons.name): `show_dynamic_checkout`, `show_gift_card_recipient`
- `share` (t:sections.featured-product.blocks.share.name): `share_label`
- `custom_liquid` (t:sections.custom-liquid.name): `custom_liquid`
- `rating` (t:sections.featured-product.blocks.rating.name): geen velden
- `icon-with-text` (t:sections.main-product.blocks.icon_with_text.name): `layout`, `icon_1`, `image_1`, `heading_1`, `icon_2`, `image_2`, `heading_2`, `icon_3`, `image_3`, `heading_3`

### 21. `sections/footer.liquid`
**Shopify Theme Editor naam:** Footer BadkamerCity. **Settings:** 33. **Blocktypen:** 3.
**Aangeroepen door JSON-template(s):** Geen directe JSON-template-match aangetroffen — mogelijk sectiegroup/dynamisch/niet actief.
**Statische code-afhankelijkheden:** Geen vaste render-/assetverwijzingen aangetroffen.

| Setting-ID | Type | Label (uit schema) |
| --- | --- | --- |
| `placeholder_mode` | `checkbox` | Voorbeeldcontact en social iconen tonen |
| `payment_examples` | `checkbox` | Voorbeeldbetaaliconen (alleen themaeditor) |
| `footer_label` | `text` | Toegankelijke naam |
| `example_label` | `text` | Voorbeeldlabel |
| `trust_title_1` | `text` | USP 1 titel |
| `trust_text_1` | `text` | USP 1 tekst |
| `trust_title_2` | `text` | USP 2 titel |
| `trust_text_2` | `text` | USP 2 tekst |
| `trust_title_3` | `text` | USP 3 titel |
| `trust_text_3` | `text` | USP 3 tekst |
| `trust_title_4` | `text` | USP 4 titel |
| `trust_text_4` | `text` | USP 4 tekst |
| `brand_tagline` | `text` | Tagline |
| `brand_text` | `richtext` | Introductie |
| `show_social` | `checkbox` | Social iconen tonen |
| `service_heading` | `text` | Kop service |
| `category_heading` | `text` | Kop assortiment |
| `info_heading` | `text` | Kop over BadkamerCity |
| `all_label` | `text` | Link volledig assortiment |
| `contact_heading` | `text` | Contactkop |
| `contact_subtitle` | `text` | Contact ondertitel |
| `contact_address` | `textarea` | Adres |
| `contact_phone` | `text` | Telefoon |
| `opening_hours` | `text` | Openingstijden |
| `contact_email` | `text` | E-mail |
| `contact_button_text` | `text` | Knoptekst |
| `contact_button_link` | `url` | Knoplink |
| `showroom_link_label` | `text` | Showroom linktekst |
| `showroom_link` | `url` | Showroom link |
| `payment_enable` | `checkbox` | Betaaliconen tonen |
| `show_policy` | `checkbox` | Beleidslinks tonen |
| `payment_label` | `text` | Toegankelijke naam betaaliconen |
| `bottom_text` | `text` | Copyrighttekst |

**Blocktypen en instelbare velden:**
- `service` (Servicelink): `label`, `url`
- `category` (Categorielink): `label`, `url`
- `info` (Informatielink): `label`, `url`

### 22. `sections/header.liquid`
**Shopify Theme Editor naam:** t:sections.header.name. **Settings:** 21. **Blocktypen:** 1.
**Aangeroepen door JSON-template(s):** Geen directe JSON-template-match aangetroffen — mogelijk sectiegroup/dynamisch/niet actief.
**Statische code-afhankelijkheden:** `snippets/bc-header-cart.liquid`, `snippets/cart-notification.liquid`, `snippets/country-localization.liquid`, `snippets/header-drawer.liquid`, `snippets/header-search.liquid`, `snippets/language-localization.liquid`, `assets/cart-notification.js`, `assets/component-cart-notification.css`, `assets/component-list-menu.css`, `assets/component-mega-menu.css`, `assets/component-menu-drawer.css`, `assets/component-price.css`, `assets/component-search.css`, `assets/icon-account-bc.svg`, `assets/icon-wishlist-bc.svg`

| Setting-ID | Type | Label (uit schema) |
| --- | --- | --- |
| `logo_position` | `select` | t:sections.header.settings.logo_position.label |
| `mobile_logo_position` | `select` | t:sections.header.settings.mobile_logo_position.label |
| `menu` | `link_list` | t:sections.header.settings.menu.label |
| `category_nav_label` | `text` | Toegankelijke naam categoriebalk |
| `category_submenu_label` | `text` | Toegankelijke naam submenu |
| `category_all_label` | `text` | Link naar volledige categorie |
| `category_close_label` | `text` | Toegankelijke naam sluiten |
| `category_previous_label` | `text` | Toegankelijke naam terugscrollen |
| `category_next_label` | `text` | Toegankelijke naam verder scrollen |
| `menu_type_desktop` | `select` | t:sections.header.settings.menu_type_desktop.label |
| `sticky_header_type` | `select` | t:sections.header.settings.sticky_header_type.label |
| `show_line_separator` | `checkbox` | t:sections.header.settings.show_line_separator.label |
| `color_scheme` | `color_scheme` | t:sections.all.colors.label |
| `menu_color_scheme` | `color_scheme` | t:sections.header.settings.menu_color_scheme.label |
| `enable_country_selector` | `checkbox` | t:sections.header.settings.enable_country_selector.label |
| `enable_language_selector` | `checkbox` | t:sections.header.settings.enable_language_selector.label |
| `enable_customer_avatar` | `checkbox` | t:sections.header.settings.enable_customer_avatar.label |
| `search_placeholder` | `text` | Search placeholder |
| `margin_bottom` | `range` | t:sections.header.settings.margin_bottom.label |
| `padding_top` | `range` | t:sections.all.padding.padding_top |
| `padding_bottom` | `range` | t:sections.all.padding.padding_bottom |

**Blocktypen en instelbare velden:**
- `@app` (): geen velden

### 23. `sections/home-brand-rail.liquid`
**Shopify Theme Editor naam:** Home brand rail. **Settings:** 8. **Blocktypen:** 1.
**Aangeroepen door JSON-template(s):** `templates/index.json`
**Statische code-afhankelijkheden:** Geen vaste render-/assetverwijzingen aangetroffen.

| Setting-ID | Type | Label (uit schema) |
| --- | --- | --- |
| `title` | `text` | Titel |
| `show_intro` | `checkbox` | Toon introductietekst |
| `intro` | `text` | Intro |
| `show_all_brands_link` | `checkbox` | Toon 'Alle merken' link |
| `all_brands_label` | `text` | 'Alle merken' label |
| `all_brands_link` | `url` | 'Alle merken' link |
| `padding_top` | `range` | Padding top |
| `padding_bottom` | `range` | Padding bottom |

**Blocktypen en instelbare velden:**
- `brand` (Merk): `collection`, `custom_image`, `custom_title`, `custom_link`

### 24. `sections/home-category-grid.liquid`
**Shopify Theme Editor naam:** Home category grid. **Settings:** 9. **Blocktypen:** 1.
**Aangeroepen door JSON-template(s):** `templates/index.json`
**Statische code-afhankelijkheden:** Geen vaste render-/assetverwijzingen aangetroffen.

| Setting-ID | Type | Label (uit schema) |
| --- | --- | --- |
| `title` | `inline_richtext` | Section title |
| `view_all_label` | `text` | All categories link label |
| `view_all_link` | `url` | All categories link |
| `menu` | `link_list` | Category menu |
| `source_mode` | `select` | Category source |
| `columns_desktop` | `range` | Items per row on desktop |
| `columns_mobile` | `range` | Items per row on mobile |
| `padding_top` | `range` | Padding top |
| `padding_bottom` | `range` | Padding bottom |

**Blocktypen en instelbare velden:**
- `category_item` (Category item): `collection`, `custom_title`, `show_on_desktop`, `show_on_mobile`

### 25. `sections/home-complete-bathroom.liquid`
**Shopify Theme Editor naam:** Complete badkamer advies. **Settings:** 13. **Blocktypen:** 0.
**Aangeroepen door JSON-template(s):** `templates/index.json`
**Statische code-afhankelijkheden:** Geen vaste render-/assetverwijzingen aangetroffen.

| Setting-ID | Type | Label (uit schema) |
| --- | --- | --- |
| `image` | `image_picker` | Badkamerfoto |
| `heading` | `textarea` | Titel |
| `body` | `textarea` | Introductie |
| `step_1_title` | `text` | Stap 1: titel |
| `step_1_text` | `textarea` | Stap 1: tekst |
| `step_2_title` | `text` | Stap 2: titel |
| `step_2_text` | `textarea` | Stap 2: tekst |
| `step_3_title` | `text` | Stap 3: titel |
| `step_3_text` | `textarea` | Stap 3: tekst |
| `cta_label` | `text` | Knoptekst |
| `cta_link` | `url` | Link adviesgesprek |
| `padding_top` | `range` | Ruimte boven |
| `padding_bottom` | `range` | Ruimte onder |

### 26. `sections/home-help-cta.liquid`
**Shopify Theme Editor naam:** Badkamer hulp CTA. **Settings:** 11. **Blocktypen:** 0.
**Aangeroepen door JSON-template(s):** `templates/index.json`
**Statische code-afhankelijkheden:** Geen vaste render-/assetverwijzingen aangetroffen.

| Setting-ID | Type | Label (uit schema) |
| --- | --- | --- |
| `heading` | `text` | Titel |
| `text` | `textarea` | Tekst |
| `primary_button_label` | `text` | Primaire knoptekst |
| `primary_button_link` | `url` | Primaire knoplink |
| `secondary_button_label` | `text` | Secundaire knoptekst |
| `secondary_button_link` | `url` | Secundaire knoplink |
| `service_1_label` | `textarea` | Servicepunt 1 |
| `service_2_label` | `textarea` | Servicepunt 2 |
| `service_3_label` | `textarea` | Servicepunt 3 |
| `padding_top` | `range` | Ruimte boven |
| `padding_bottom` | `range` | Ruimte onder |

### 27. `sections/home-hero.liquid`
**Shopify Theme Editor naam:** Home Hero. **Settings:** 47. **Blocktypen:** 0.
**Aangeroepen door JSON-template(s):** `templates/index.json`
**Statische code-afhankelijkheden:** Geen vaste render-/assetverwijzingen aangetroffen.

| Setting-ID | Type | Label (uit schema) |
| --- | --- | --- |
| `hero_title` | `text` | Hero title |
| `hero_subtitle` | `text` | Hero subtitle |
| `hero_button_text` | `text` | Hero button text |
| `hero_button_link` | `url` | Hero button link |
| `hero_title_color` | `color` | Hero title color |
| `hero_subtitle_color` | `color` | Hero subtitle color |
| `hero_title_position_mode` | `select` | Hero title placement mode |
| `hero_title_mobile_x` | `range` | Hero title mobile horizontal position |
| `hero_title_mobile_y` | `range` | Hero title mobile vertical position |
| `hero_title_desktop_x` | `range` | Hero title desktop horizontal position |
| `hero_title_desktop_y` | `range` | Hero title desktop vertical position |
| `hero_subtitle_position_mode` | `select` | Hero subtitle placement mode |
| `hero_subtitle_mobile_x` | `range` | Hero subtitle mobile horizontal position |
| `hero_subtitle_mobile_y` | `range` | Hero subtitle mobile vertical position |
| `hero_subtitle_desktop_x` | `range` | Hero subtitle desktop horizontal position |
| `hero_subtitle_desktop_y` | `range` | Hero subtitle desktop vertical position |
| `hero_button_text_color` | `color` | Hero button text color |
| `hero_button_background_color` | `color` | Hero button background color |
| `hero_button_alignment` | `select` | Hero button position |
| `hero_button_position_mode` | `select` | Hero button placement mode |
| `hero_button_mobile_x` | `range` | Hero button mobile horizontal position |
| `hero_button_mobile_y` | `range` | Hero button mobile vertical position |
| `hero_button_desktop_x` | `range` | Hero button desktop horizontal position |
| `hero_button_desktop_y` | `range` | Hero button desktop vertical position |
| `hero_image` | `image_picker` | Hero image |
| `banner_1_title` | `text` | Banner 2 title |
| `banner_1_subtitle` | `text` | Banner 2 subtitle |
| `banner_1_button` | `text` | Banner 2 button text |
| `banner_1_link` | `url` | Banner 2 link |
| `banner_1_title_color` | `color` | Banner 2 title color |
| `banner_1_subtitle_color` | `color` | Banner 2 subtitle color |
| `banner_1_button_text_color` | `color` | Banner 2 button text color |
| `banner_1_button_background_color` | `color` | Banner 2 button background color |
| `banner_1_button_alignment` | `select` | Banner 2 button position |
| `banner_1_image` | `image_picker` | Banner 2 image |
| `banner_2_title` | `text` | Banner 3 title |
| `banner_2_subtitle` | `text` | Banner 3 subtitle |
| `banner_2_button` | `text` | Banner 3 button text |
| `banner_2_link` | `url` | Banner 3 link |
| `banner_2_title_color` | `color` | Banner 3 title color |
| `banner_2_subtitle_color` | `color` | Banner 3 subtitle color |
| `banner_2_button_text_color` | `color` | Banner 3 button text color |
| `banner_2_button_background_color` | `color` | Banner 3 button background color |
| `banner_2_button_alignment` | `select` | Banner 3 button position |
| `banner_2_image` | `image_picker` | Banner 3 image |
| `padding_top` | `range` | Padding top |
| `padding_bottom` | `range` | Padding bottom |

### 28. `sections/home-mijn-badkamercity.liquid`
**Shopify Theme Editor naam:** Badkamerinspiratie. **Settings:** 8. **Blocktypen:** 1.
**Aangeroepen door JSON-template(s):** `templates/index.json`
**Statische code-afhankelijkheden:** `assets/icon-caret.svg`

| Setting-ID | Type | Label (uit schema) |
| --- | --- | --- |
| `title` | `text` | Titel |
| `show_intro` | `checkbox` | Toon introductietekst |
| `intro` | `richtext` | Intro |
| `hashtag_label` | `text` | Fallback kaarttitel |
| `button_label` | `text` | Knop label |
| `button_link` | `url` | Knop link |
| `padding_top` | `range` | Padding top |
| `padding_bottom` | `range` | Padding bottom |

**Blocktypen en instelbare velden:**
- `post` (Inspiratiekaart): `image`, `caption`, `link`

### 29. `sections/home-popular-products.liquid`
**Shopify Theme Editor naam:** Home popular products. **Settings:** 8. **Blocktypen:** 0.
**Aangeroepen door JSON-template(s):** `templates/index.json`
**Statische code-afhankelijkheden:** `snippets/loading-spinner.liquid`, `snippets/unit-price.liquid`, `assets/icon-box.svg`, `assets/icon-cart-bc.svg`, `assets/product-form.js`

| Setting-ID | Type | Label (uit schema) |
| --- | --- | --- |
| `heading` | `text` | Titel |
| `collection` | `collection` | Collectie |
| `product_count` | `range` | Aantal producten |
| `view_all_label` | `text` | Bekijk alle-label |
| `view_all_link` | `url` | Bekijk alle-link |
| `add_to_cart_label` | `text` | Tekst winkelwagenknop |
| `padding_top` | `range` | Ruimte boven |
| `padding_bottom` | `range` | Ruimte onder |

### 30. `sections/home-shop-by-style.liquid`
**Shopify Theme Editor naam:** Home shop by style. **Settings:** 17. **Blocktypen:** 1.
**Aangeroepen door JSON-template(s):** `templates/index.json`
**Statische code-afhankelijkheden:** Geen vaste render-/assetverwijzingen aangetroffen.

| Setting-ID | Type | Label (uit schema) |
| --- | --- | --- |
| `show_extended_content` | `checkbox` | Toon extra teksten |
| `card_cta_label` | `text` | Compacte kaarttekst |
| `eyebrow` | `text` | Eyebrow |
| `title` | `inline_richtext` | Titel |
| `intro` | `richtext` | Intro |
| `primary_button_label` | `text` | Primaire knop label |
| `primary_button_link` | `url` | Primaire knop link |
| `secondary_button_label` | `text` | Secundaire knop label |
| `secondary_button_link` | `url` | Secundaire knop link |
| `support_title_1` | `text` | Support kaart 1 titel |
| `support_text_1` | `text` | Support kaart 1 tekst |
| `support_title_2` | `text` | Support kaart 2 titel |
| `support_text_2` | `text` | Support kaart 2 tekst |
| `support_title_3` | `text` | Support kaart 3 titel |
| `support_text_3` | `text` | Support kaart 3 tekst |
| `padding_top` | `range` | Padding top |
| `padding_bottom` | `range` | Padding bottom |

**Blocktypen en instelbare velden:**
- `style_card` (Stijlkaart): `featured`, `image`, `kicker`, `secondary_kicker`, `title`, `text`, `link_label`, `link`

### 31. `sections/image-banner.liquid`
**Shopify Theme Editor naam:** t:sections.image-banner.name. **Settings:** 12. **Blocktypen:** 3.
**Aangeroepen door JSON-template(s):** Geen directe JSON-template-match aangetroffen — mogelijk sectiegroup/dynamisch/niet actief.
**Statische code-afhankelijkheden:** `assets/section-image-banner.css`

| Setting-ID | Type | Label (uit schema) |
| --- | --- | --- |
| `image` | `image_picker` | t:sections.image-banner.settings.image.label |
| `image_2` | `image_picker` | t:sections.image-banner.settings.image_2.label |
| `image_overlay_opacity` | `range` | t:sections.image-banner.settings.image_overlay_opacity.label |
| `image_height` | `select` | t:sections.image-banner.settings.image_height.label |
| `image_behavior` | `select` | t:sections.all.animation.image_behavior.label |
| `desktop_content_position` | `select` | t:sections.image-banner.settings.desktop_content_position.label |
| `desktop_content_alignment` | `select` | t:sections.image-banner.settings.desktop_content_alignment.label |
| `show_text_box` | `checkbox` | t:sections.image-banner.settings.show_text_box.label |
| `color_scheme` | `color_scheme` | t:sections.all.colors.label |
| `stack_images_on_mobile` | `checkbox` | t:sections.image-banner.settings.stack_images_on_mobile.label |
| `mobile_content_alignment` | `select` | t:sections.image-banner.settings.mobile_content_alignment.label |
| `show_text_below` | `checkbox` | t:sections.image-banner.settings.show_text_below.label |

**Blocktypen en instelbare velden:**
- `heading` (t:sections.image-banner.blocks.heading.name): `heading`, `heading_size`
- `text` (t:sections.image-banner.blocks.text.name): `text`, `text_style`
- `buttons` (t:sections.image-banner.blocks.buttons.name): `button_label_1`, `button_link_1`, `button_style_secondary_1`, `button_label_2`, `button_link_2`, `button_style_secondary_2`

### 32. `sections/image-with-text.liquid`
**Shopify Theme Editor naam:** t:sections.image-with-text.name. **Settings:** 13. **Blocktypen:** 4.
**Aangeroepen door JSON-template(s):** Geen directe JSON-template-match aangetroffen — mogelijk sectiegroup/dynamisch/niet actief.
**Statische code-afhankelijkheden:** `assets/component-image-with-text.css`

| Setting-ID | Type | Label (uit schema) |
| --- | --- | --- |
| `image` | `image_picker` | t:sections.image-with-text.settings.image.label |
| `height` | `select` | t:sections.image-with-text.settings.height.label |
| `desktop_image_width` | `select` | t:sections.image-with-text.settings.desktop_image_width.label |
| `layout` | `select` | t:sections.image-with-text.settings.layout.label |
| `image_behavior` | `select` | t:sections.all.animation.image_behavior.label |
| `content_layout` | `select` | t:sections.image-with-text.settings.content_layout.label |
| `desktop_content_position` | `select` | t:sections.image-with-text.settings.desktop_content_position.label |
| `desktop_content_alignment` | `select` | t:sections.image-with-text.settings.desktop_content_alignment.label |
| `mobile_content_alignment` | `select` | t:sections.image-with-text.settings.mobile_content_alignment.label |
| `section_color_scheme` | `color_scheme` | t:sections.all.colors.label |
| `color_scheme` | `color_scheme` | t:sections.multirow.settings.container_color_scheme.label |
| `padding_top` | `range` | t:sections.all.padding.padding_top |
| `padding_bottom` | `range` | t:sections.all.padding.padding_bottom |

**Blocktypen en instelbare velden:**
- `heading` (t:sections.image-with-text.blocks.heading.name): `heading`, `heading_size`
- `caption` (t:sections.image-with-text.blocks.caption.name): `caption`, `text_style`, `text_size`
- `text` (t:sections.image-with-text.blocks.text.name): `text`, `text_style`
- `button` (t:sections.image-with-text.blocks.button.name): `button_label`, `button_link`, `button_style_secondary`

### 33. `sections/main-404.liquid`
**Geen direct parsebaar Theme Editor-schema in dit bestand** (mogelijk via vaste sectiegroep of legacy-code).
**Aangeroepen door JSON-template(s):** `templates/404.json`
**Statische code-afhankelijkheden:** Geen vaste render-/assetverwijzingen aangetroffen.

### 34. `sections/main-account.liquid`
**Shopify Theme Editor naam:** t:sections.main-account.name. **Settings:** 2. **Blocktypen:** 0.
**Aangeroepen door JSON-template(s):** `templates/customers/account.json`
**Statische code-afhankelijkheden:** `assets/customer.css`, `assets/icon-account.svg`, `assets/icon-caret.svg`

| Setting-ID | Type | Label (uit schema) |
| --- | --- | --- |
| `padding_top` | `range` | t:sections.all.padding.padding_top |
| `padding_bottom` | `range` | t:sections.all.padding.padding_bottom |

### 35. `sections/main-activate-account.liquid`
**Shopify Theme Editor naam:** t:sections.main-activate-account.name. **Settings:** 2. **Blocktypen:** 0.
**Aangeroepen door JSON-template(s):** `templates/customers/activate_account.json`
**Statische code-afhankelijkheden:** `assets/customer.css`, `assets/icon-error.svg`

| Setting-ID | Type | Label (uit schema) |
| --- | --- | --- |
| `padding_top` | `range` | t:sections.all.padding.padding_top |
| `padding_bottom` | `range` | t:sections.all.padding.padding_bottom |

### 36. `sections/main-addresses.liquid`
**Shopify Theme Editor naam:** t:sections.main-addresses.name. **Settings:** 2. **Blocktypen:** 0.
**Aangeroepen door JSON-template(s):** `templates/customers/addresses.json`
**Statische code-afhankelijkheden:** `assets/customer.css`, `assets/customer.js`, `assets/icon-caret.svg`

| Setting-ID | Type | Label (uit schema) |
| --- | --- | --- |
| `padding_top` | `range` | t:sections.all.padding.padding_top |
| `padding_bottom` | `range` | t:sections.all.padding.padding_bottom |

### 37. `sections/main-article.liquid`
**Shopify Theme Editor naam:** t:sections.main-article.name. **Settings:** 0. **Blocktypen:** 5.
**Aangeroepen door JSON-template(s):** `templates/article.json`
**Statische code-afhankelijkheden:** `snippets/pagination.liquid`, `snippets/share-button.liquid`, `assets/icon-arrow.svg`, `assets/icon-error.svg`, `assets/icon-success.svg`, `assets/section-blog-post.css`

**Blocktypen en instelbare velden:**
- `@app` (): geen velden
- `featured_image` (t:sections.main-article.blocks.featured_image.name): `image_height`
- `title` (t:sections.main-article.blocks.title.name): `blog_show_date`, `blog_show_author`
- `content` (t:sections.main-article.blocks.content.name): geen velden
- `share` (t:sections.main-article.blocks.share.name): `share_label`

### 38. `sections/main-blog.liquid`
**Shopify Theme Editor naam:** t:sections.main-blog.name. **Settings:** 7. **Blocktypen:** 0.
**Aangeroepen door JSON-template(s):** `templates/blog.json`
**Statische code-afhankelijkheden:** `snippets/article-card.liquid`, `snippets/pagination.liquid`, `assets/component-article-card.css`, `assets/component-card.css`, `assets/section-main-blog.css`

| Setting-ID | Type | Label (uit schema) |
| --- | --- | --- |
| `layout` | `select` | t:sections.main-blog.settings.layout.label |
| `show_image` | `checkbox` | t:sections.main-blog.settings.show_image.label |
| `image_height` | `select` | t:sections.main-blog.settings.image_height.label |
| `show_date` | `checkbox` | t:sections.main-blog.settings.show_date.label |
| `show_author` | `checkbox` | t:sections.main-blog.settings.show_author.label |
| `padding_top` | `range` | t:sections.all.padding.padding_top |
| `padding_bottom` | `range` | t:sections.all.padding.padding_bottom |

### 39. `sections/main-cart-footer.liquid`
**Shopify Theme Editor naam:** t:sections.main-cart-footer.name. **Settings:** 3. **Blocktypen:** 3.
**Aangeroepen door JSON-template(s):** `templates/cart.json`
**Statische code-afhankelijkheden:** `assets/component-cart.css`, `assets/component-discounts.css`, `assets/component-price.css`, `assets/component-totals.css`, `assets/icon-discount.svg`

| Setting-ID | Type | Label (uit schema) |
| --- | --- | --- |
| `color_scheme` | `color_scheme` | t:sections.all.colors.label |
| `padding_top` | `range` | t:sections.all.padding.padding_top |
| `padding_bottom` | `range` | t:sections.all.padding.padding_bottom |

**Blocktypen en instelbare velden:**
- `subtotal` (t:sections.main-cart-footer.blocks.subtotal.name): geen velden
- `buttons` (t:sections.main-cart-footer.blocks.buttons.name): geen velden
- `@app` (): geen velden

### 40. `sections/main-cart-items.liquid`
**Shopify Theme Editor naam:** t:sections.main-cart-items.name. **Settings:** 3. **Blocktypen:** 0.
**Aangeroepen door JSON-template(s):** `templates/cart.json`
**Statische code-afhankelijkheden:** `snippets/loading-spinner.liquid`, `snippets/unit-price.liquid`, `assets/cart.js`, `assets/component-cart-items.css`, `assets/component-cart.css`, `assets/component-discounts.css`, `assets/component-price.css`, `assets/component-totals.css`, `assets/icon-close.svg`, `assets/icon-discount.svg`, `assets/icon-error.svg`, `assets/icon-info.svg`, `assets/icon-minus.svg`, `assets/icon-plus.svg`, `assets/icon-remove.svg`, `assets/quantity-popover.css`, `assets/quantity-popover.js`

| Setting-ID | Type | Label (uit schema) |
| --- | --- | --- |
| `color_scheme` | `color_scheme` | t:sections.all.colors.label |
| `padding_top` | `range` | t:sections.all.padding.padding_top |
| `padding_bottom` | `range` | t:sections.all.padding.padding_bottom |

### 41. `sections/main-category-landing.liquid`
**Shopify Theme Editor naam:** Category Landing. **Settings:** 30. **Blocktypen:** 3.
**Aangeroepen door JSON-template(s):** `templates/collection.category-landing.json`
**Statische code-afhankelijkheden:** `snippets/bc-category-breadcrumbs.liquid`, `snippets/bc-category-children.liquid`, `snippets/bc-category-link-index.liquid`, `snippets/bc-collection-intro.liquid`, `snippets/card-product.liquid`, `assets/bc-category-directory.css`, `assets/bc-collection.css`, `assets/component-bc-category-navigation.css`, `assets/component-card.css`, `assets/component-price.css`, `assets/template-collection.css`

| Setting-ID | Type | Label (uit schema) |
| --- | --- | --- |
| `navigation_menu` | `link_list` | Menu voor de categorieboom |
| `subcategory_source` | `select` | Bron voor subcategorieën |
| `color_scheme` | `color_scheme` | Kleurschema |
| `show_collection_title` | `checkbox` | Toon collectietitel |
| `show_collection_description` | `checkbox` | Toon collectieomschrijving |
| `show_seo_content` | `checkbox` | Toon SEO content met split |
| `seo_content` | `richtext` | SEO content |
| `show_extra_content` | `checkbox` | Toon extra contentblok |
| `extra_text_title` | `text` | Titel extra content |
| `extra_text_content` | `richtext` | Extra content |
| `show_subcategory_grid` | `checkbox` | Toon subcategorie-overzicht |
| `subcategory_grid_heading` | `text` | Titel subcategorie-overzicht |
| `subcategory_grid_columns_desktop` | `range` | Kolommen desktop |
| `subcategory_image_ratio` | `select` | Beeldverhouding subcategorie-afbeelding |
| `show_related_links` | `checkbox` | Toon gerelateerde links |
| `related_links_heading` | `text` | Titel gerelateerde links |
| `related_links_columns_desktop` | `range` | Kolommen gerelateerde links desktop |
| `show_advice_bar` | `checkbox` | Toon adviesbalk boven onderste SEO-tekst |
| `advice_bar_title` | `text` | Titel adviesbalk |
| `show_product_grid` | `checkbox` | Toon productgrid onder subcategorieën |
| `product_grid_heading` | `text` | Titel productgrid |
| `product_grid_intro` | `richtext` | Intro productgrid |
| `max_products` | `range` | Maximaal aantal producten |
| `product_grid_columns_desktop` | `range` | Kolommen productgrid desktop |
| `product_image_ratio` | `select` | Beeldverhouding productafbeelding |
| `padding_top` | `range` | Padding boven |
| `padding_bottom` | `range` | Padding onder |
| `show_subcategory_heading` | `checkbox` | Toon titel boven de categorieplaatjes |
| `show_advice_link` | `checkbox` | Toon link naar het keuzeadvies |
| `related_links_menu` | `link_list` | Algemeen menu voor alfabetische links |

**Blocktypen en instelbare velden:**
- `subcategory` (Subcategorie): `block_title`, `block_image`, `block_link`, `block_description`
- `related_group` (Gerelateerde linkgroep): `group_label`, `group_menu`
- `category_menu` (Categoriepagina-menu's): `source_collection`, `cards_menu`, `links_menu`

### 42. `sections/main-collection-banner.liquid`
**Shopify Theme Editor naam:** t:sections.main-collection-banner.name. **Settings:** 6. **Blocktypen:** 1.
**Aangeroepen door JSON-template(s):** `templates/collection.json`
**Statische code-afhankelijkheden:** `snippets/bc-category-breadcrumbs.liquid`, `snippets/bc-category-children.liquid`, `snippets/bc-category-link-index.liquid`, `snippets/bc-collection-intro.liquid`, `assets/bc-category-directory.css`, `assets/bc-collection.css`, `assets/component-bc-category-navigation.css`, `assets/component-collection-hero.css`

| Setting-ID | Type | Label (uit schema) |
| --- | --- | --- |
| `navigation_menu` | `link_list` | Menu voor de categorieboom |
| `show_collection_description` | `checkbox` | t:sections.main-collection-banner.settings.show_collection_description.label |
| `show_collection_image` | `checkbox` | t:sections.main-collection-banner.settings.show_collection_image.label |
| `color_scheme` | `color_scheme` | t:sections.all.colors.label |
| `show_related_links` | `checkbox` | Toon alfabetische links |
| `related_links_menu` | `link_list` | Menu voor alfabetische links |

**Blocktypen en instelbare velden:**
- `category_menu` (Categoriepagina-menu's): `source_collection`, `cards_menu`, `links_menu`

### 43. `sections/main-collection-category-landing.liquid`
**Shopify Theme Editor naam:** Category Landing. **Settings:** 20. **Blocktypen:** 1.
**Aangeroepen door JSON-template(s):** Geen directe JSON-template-match aangetroffen — mogelijk sectiegroup/dynamisch/niet actief.
**Statische code-afhankelijkheden:** `snippets/card-product.liquid`, `assets/component-card.css`, `assets/component-price.css`, `assets/icon-arrow.svg`, `assets/template-collection.css`

| Setting-ID | Type | Label (uit schema) |
| --- | --- | --- |
| `color_scheme` | `color_scheme` | Kleurschema |
| `show_collection_title` | `checkbox` | Toon collectietitel |
| `show_collection_description` | `checkbox` | Toon collectieomschrijving |
| `show_intro_text` | `checkbox` | Toon introtekst |
| `intro_text` | `richtext` | Introtekst |
| `show_extra_content` | `checkbox` | Toon extra contentblok |
| `extra_text_title` | `text` | Titel extra content |
| `extra_text_content` | `richtext` | Extra content |
| `show_subcategory_grid` | `checkbox` | Toon subcategorie-overzicht |
| `subcategory_grid_heading` | `text` | Titel subcategorie-overzicht |
| `subcategory_grid_columns_desktop` | `range` | Kolommen desktop |
| `subcategory_image_ratio` | `select` | Beeldverhouding subcategorie-afbeelding |
| `show_product_grid` | `checkbox` | Toon productgrid onder subcategorieën |
| `product_grid_heading` | `text` | Titel productgrid |
| `product_grid_intro` | `richtext` | Intro productgrid |
| `max_products` | `range` | Maximaal aantal producten |
| `product_grid_columns_desktop` | `range` | Kolommen productgrid desktop |
| `product_image_ratio` | `select` | Beeldverhouding productafbeelding |
| `padding_top` | `range` | Padding boven |
| `padding_bottom` | `range` | Padding onder |

**Blocktypen en instelbare velden:**
- `subcategory` (Subcategorie): `block_title`, `block_image`, `block_link`, `block_description`

### 44. `sections/main-collection-product-grid.liquid`
**Shopify Theme Editor naam:** t:sections.main-collection-product-grid.name. **Settings:** 15. **Blocktypen:** 0.
**Aangeroepen door JSON-template(s):** `templates/collection.json`
**Statische code-afhankelijkheden:** `snippets/bc-collection-active-filters.liquid`, `snippets/bc-external-filters.liquid`, `snippets/card-product.liquid`, `snippets/facets.liquid`, `snippets/loading-spinner.liquid`, `snippets/pagination.liquid`, `assets/bc-collection.css`, `assets/component-card.css`, `assets/component-facets.css`, `assets/component-price.css`, `assets/facets.js`, `assets/icon-caret.svg`, `assets/mask-arch.svg`, `assets/mask-blobs.css`, `assets/price-per-item.js`, `assets/product-form.js`, `assets/quantity-popover.js`, `assets/quick-add-bulk.js`, `assets/quick-add.css`, `assets/quick-add.js`, `assets/quick-order-list.js`, `assets/template-collection.css`

| Setting-ID | Type | Label (uit schema) |
| --- | --- | --- |
| `products_per_page` | `range` | t:sections.main-collection-product-grid.settings.products_per_page.label |
| `columns_desktop` | `range` | t:sections.main-collection-product-grid.settings.columns_desktop.label |
| `columns_mobile` | `select` | t:sections.main-collection-product-grid.settings.columns_mobile.label |
| `color_scheme` | `color_scheme` | t:sections.all.colors.label |
| `image_ratio` | `select` | t:sections.main-collection-product-grid.settings.image_ratio.label |
| `image_shape` | `select` | t:sections.all.image_shape.label |
| `show_secondary_image` | `checkbox` | t:sections.main-collection-product-grid.settings.show_secondary_image.label |
| `show_vendor` | `checkbox` | t:sections.main-collection-product-grid.settings.show_vendor.label |
| `show_rating` | `checkbox` | t:sections.main-collection-product-grid.settings.show_rating.label |
| `quick_add` | `select` | t:sections.main-collection-product-grid.settings.quick_add.label |
| `enable_filtering` | `checkbox` | t:sections.main-collection-product-grid.settings.enable_filtering.label |
| `filter_type` | `select` | t:sections.main-collection-product-grid.settings.filter_type.label |
| `enable_sorting` | `checkbox` | t:sections.main-collection-product-grid.settings.enable_sorting.label |
| `padding_top` | `range` | t:sections.all.padding.padding_top |
| `padding_bottom` | `range` | t:sections.all.padding.padding_bottom |

### 45. `sections/main-glossary-page.liquid`
**Shopify Theme Editor naam:** Begripspagina. **Settings:** 12. **Blocktypen:** 0.
**Aangeroepen door JSON-template(s):** `templates/page.begrip.json`
**Statische code-afhankelijkheden:** `assets/section-main-glossary-page.css`

| Setting-ID | Type | Label (uit schema) |
| --- | --- | --- |
| `heading_prefix` | `text` | Label boven titel |
| `show_back_link` | `checkbox` | Toon teruglink |
| `back_link_label` | `text` | Tekst teruglink |
| `back_link_url` | `url` | URL teruglink |
| `show_sidebar` | `checkbox` | Toon sidebar |
| `sidebar_heading` | `text` | Sidebar titel |
| `sidebar_text` | `textarea` | Sidebar tekst |
| `sidebar_button_label` | `text` | Sidebar knoptekst |
| `sidebar_button_url` | `url` | Sidebar knoplink |
| `color_scheme` | `color_scheme` | Kleurenschema |
| `padding_top` | `range` | Padding boven |
| `padding_bottom` | `range` | Padding onder |

### 46. `sections/main-glossary.liquid`
**Shopify Theme Editor naam:** Begrippenlijst. **Settings:** 9. **Blocktypen:** 1.
**Aangeroepen door JSON-template(s):** `templates/page.begrippenlijst.json`
**Statische code-afhankelijkheden:** `assets/section-main-glossary.css`

| Setting-ID | Type | Label (uit schema) |
| --- | --- | --- |
| `heading` | `text` | Titel |
| `intro` | `richtext` | Intro |
| `enable_search` | `checkbox` | Zoekfunctie tonen |
| `search_label` | `text` | Zoekveld label |
| `search_placeholder` | `text` | Zoekveld placeholder |
| `empty_text` | `richtext` | Tekst zonder resultaten |
| `color_scheme` | `color_scheme` | Kleurenschema |
| `padding_top` | `range` | Bovenruimte |
| `padding_bottom` | `range` | Onderruimte |

**Blocktypen en instelbare velden:**
- `term` (Begrip): `term`, `letter`, `keywords`

### 47. `sections/main-list-collections.liquid`
**Shopify Theme Editor naam:** t:sections.main-list-collections.name. **Settings:** 5. **Blocktypen:** 0.
**Aangeroepen door JSON-template(s):** `templates/list-collections.json`
**Statische code-afhankelijkheden:** `snippets/card-collection.liquid`, `snippets/pagination.liquid`, `assets/component-card.css`, `assets/section-collection-list.css`

| Setting-ID | Type | Label (uit schema) |
| --- | --- | --- |
| `title` | `inline_richtext` | t:sections.main-list-collections.settings.title.label |
| `sort` | `select` | t:sections.main-list-collections.settings.sort.label |
| `image_ratio` | `select` | t:sections.main-list-collections.settings.image_ratio.label |
| `columns_desktop` | `range` | t:sections.main-list-collections.settings.columns_desktop.label |
| `columns_mobile` | `select` | t:sections.main-list-collections.settings.columns_mobile.label |

### 48. `sections/main-login.liquid`
**Shopify Theme Editor naam:** t:sections.main-login.name. **Settings:** 3. **Blocktypen:** 0.
**Aangeroepen door JSON-template(s):** `templates/customers/login.json`
**Statische code-afhankelijkheden:** `assets/customer.css`, `assets/icon-error.svg`, `assets/icon-success.svg`

| Setting-ID | Type | Label (uit schema) |
| --- | --- | --- |
| `enable_shop_login_button` | `checkbox` | t:sections.main-login.shop_login_button.enable |
| `padding_top` | `range` | t:sections.all.padding.padding_top |
| `padding_bottom` | `range` | t:sections.all.padding.padding_bottom |

### 49. `sections/main-order.liquid`
**Shopify Theme Editor naam:** t:sections.main-order.name. **Settings:** 2. **Blocktypen:** 0.
**Aangeroepen door JSON-template(s):** `templates/customers/order.json`
**Statische code-afhankelijkheden:** `snippets/unit-price.liquid`, `assets/customer.css`, `assets/icon-discount.svg`

| Setting-ID | Type | Label (uit schema) |
| --- | --- | --- |
| `padding_top` | `range` | t:sections.all.padding.padding_top |
| `padding_bottom` | `range` | t:sections.all.padding.padding_bottom |

### 50. `sections/main-page.liquid`
**Shopify Theme Editor naam:** t:sections.main-page.name. **Settings:** 2. **Blocktypen:** 0.
**Aangeroepen door JSON-template(s):** `templates/page.contact.json`, `templates/page.json`
**Statische code-afhankelijkheden:** `assets/section-main-page.css`

| Setting-ID | Type | Label (uit schema) |
| --- | --- | --- |
| `padding_top` | `range` | t:sections.all.padding.padding_top |
| `padding_bottom` | `range` | t:sections.all.padding.padding_bottom |

### 51. `sections/main-password-footer.liquid`
**Shopify Theme Editor naam:** t:sections.main-password-footer.name. **Settings:** 1. **Blocktypen:** 0.
**Aangeroepen door JSON-template(s):** Geen directe JSON-template-match aangetroffen — mogelijk sectiegroup/dynamisch/niet actief.
**Statische code-afhankelijkheden:** `assets/icon-facebook.svg`, `assets/icon-instagram.svg`, `assets/icon-pinterest.svg`, `assets/icon-shopify.svg`, `assets/icon-snapchat.svg`, `assets/icon-tiktok.svg`, `assets/icon-tumblr.svg`, `assets/icon-twitter.svg`, `assets/icon-vimeo.svg`, `assets/icon-youtube.svg`

| Setting-ID | Type | Label (uit schema) |
| --- | --- | --- |
| `color_scheme` | `color_scheme` | t:sections.all.colors.label |

### 52. `sections/main-password-header.liquid`
**Shopify Theme Editor naam:** t:sections.main-password-header.name. **Settings:** 1. **Blocktypen:** 0.
**Aangeroepen door JSON-template(s):** Geen directe JSON-template-match aangetroffen — mogelijk sectiegroup/dynamisch/niet actief.
**Statische code-afhankelijkheden:** `assets/icon-close.svg`, `assets/icon-padlock.svg`

| Setting-ID | Type | Label (uit schema) |
| --- | --- | --- |
| `color_scheme` | `color_scheme` | t:sections.all.colors.label |

### 53. `sections/main-product.liquid`
**Shopify Theme Editor naam:** t:sections.main-product.name. **Settings:** 13. **Blocktypen:** 17.
**Aangeroepen door JSON-template(s):** `templates/product.bc-hotbath-data.json`, `templates/product.bc-hotbath-pilot.json`, `templates/product.json`
**Statische code-afhankelijkheden:** `snippets/bc-product-accessories.liquid`, `snippets/bc-product-detail-specs.liquid`, `snippets/bc-product-set-components.liquid`, `snippets/bc-product-switcher.liquid`, `snippets/buy-buttons.liquid`, `snippets/card-product.liquid`, `snippets/icon-accordion.liquid`, `snippets/icon-with-text.liquid`, `snippets/loading-spinner.liquid`, `snippets/product-media-gallery.liquid`, `snippets/product-media-modal.liquid`, `snippets/product-pros-cons.liquid`, `snippets/product-variant-picker.liquid`, `assets/bc-product-accessories.js`, `assets/bc-product-sticky.js`, `assets/component-accordion.css`, `assets/component-card.css`, `assets/component-complementary-products.css`, `assets/component-deferred-media.css`, `assets/component-model-viewer-ui.css`, `assets/component-price.css`, `assets/component-product-accessories.css`, `assets/component-product-model.css`, `assets/component-product-pros-cons.css`, `assets/component-product-set.css`, `assets/component-product-variant-picker.css`, `assets/component-rating.css`, `assets/component-slider.css`, `assets/component-swatch-input.css`, `assets/component-swatch.css`, `assets/component-volume-pricing.css`, `assets/icon-caret.svg`, `assets/icon-cart-bc.svg`, `assets/icon-close.svg`, `assets/icon-inventory-status.svg`, `assets/icon-minus.svg`, `assets/icon-plus.svg`, `assets/magnify.js`, `assets/media-gallery.js`, `assets/price-per-item.js`, `assets/product-form.js`, `assets/product-info.js`, `assets/product-modal.js`, `assets/product-model.js`, `assets/quick-add.css`, `assets/quick-add.js`, `assets/section-main-product.css`, `assets/show-more.js`, `assets/theme-editor.js`
**Rechtstreeks genoemde metafields:** `custom.afmeting`, `custom.afwerking`, `custom.basiskleur`, `custom.breedte_diameter_hoofddouche`, `custom.frame`, `custom.group`, `custom.handdouche`, `custom.hoofddouche`, `custom.hoogte`, `custom.led`, `custom.lengte`, `custom.leverancier_verwachte_datum`, `custom.leverancier_voorraad`, `custom.menu_1`, `custom.menu_2`, `custom.menu_3`, `custom.menu_4`, `custom.menu_5`, `custom.met_glijstang`, `custom.montage`, `custom.plaatsing`, `custom.switch_group`, `custom.switch_key`, `custom.type`, `custom.type_bevestiging_hoofddouche`, `custom.type_handdouche`, `custom.vorm`, `reviews.rating`, `reviews.rating_count`. Let op: definitiebestaan/gevulde waarden apart controleren.

| Setting-ID | Type | Label (uit schema) |
| --- | --- | --- |
| `enable_sticky_info` | `checkbox` | t:sections.main-product.settings.enable_sticky_info.label |
| `color_scheme` | `color_scheme` | t:sections.all.colors.label |
| `media_size` | `select` | t:sections.main-product.settings.media_size.label |
| `constrain_to_viewport` | `checkbox` | t:sections.main-product.settings.constrain_to_viewport.label |
| `media_fit` | `select` | t:sections.main-product.settings.media_fit.label |
| `gallery_layout` | `select` | t:sections.main-product.settings.gallery_layout.label |
| `mobile_thumbnails` | `select` | t:sections.main-product.settings.mobile_thumbnails.label |
| `media_position` | `select` | t:sections.main-product.settings.media_position.label |
| `image_zoom` | `select` | t:sections.main-product.settings.image_zoom.label |
| `hide_variants` | `checkbox` | t:sections.main-product.settings.hide_variants.label |
| `enable_video_looping` | `checkbox` | t:sections.main-product.settings.enable_video_looping.label |
| `padding_top` | `range` | t:sections.all.padding.padding_top |
| `padding_bottom` | `range` | t:sections.all.padding.padding_bottom |

**Blocktypen en instelbare velden:**
- `@app` (): geen velden
- `text` (t:sections.main-product.blocks.text.name): `text`, `text_style`
- `title` (t:sections.main-product.blocks.title.name): geen velden
- `price` (t:sections.main-product.blocks.price.name): geen velden
- `sku` (t:sections.main-product.blocks.sku.name): `text_style`
- `inventory` (t:sections.main-product.blocks.inventory.name): `text_style`, `inventory_threshold`, `show_inventory_quantity`
- `quantity_selector` (t:sections.main-product.blocks.quantity_selector.name): geen velden
- `variant_picker` (t:sections.main-product.blocks.variant_picker.name): `picker_type`, `swatch_shape`
- `buy_buttons` (t:sections.main-product.blocks.buy_buttons.name): `show_dynamic_checkout`, `show_gift_card_recipient`
- `description` (t:sections.main-product.blocks.description.name): geen velden
- `share` (t:sections.main-product.blocks.share.name): `share_label`
- `custom_liquid` (t:sections.custom-liquid.name): `custom_liquid`
- `collapsible_tab` (t:sections.main-product.blocks.collapsible_tab.name): `heading`, `icon`, `content`, `page`
- `popup` (t:sections.main-product.blocks.popup.name): `text`, `page`
- `rating` (t:sections.main-product.blocks.rating.name): geen velden
- `complementary` (t:sections.main-product.blocks.complementary_products.name): `block_heading`, `make_collapsible_row`, `icon`, `product_list_limit`, `products_per_page`, `pagination_style`, `image_ratio`, `enable_quick_add`
- `icon-with-text` (t:sections.main-product.blocks.icon_with_text.name): `layout`, `icon_1`, `image_1`, `heading_1`, `icon_2`, `image_2`, `heading_2`, `icon_3`, `image_3`, `heading_3`

### 54. `sections/main-register.liquid`
**Shopify Theme Editor naam:** t:sections.main-register.name. **Settings:** 2. **Blocktypen:** 0.
**Aangeroepen door JSON-template(s):** `templates/customers/register.json`
**Statische code-afhankelijkheden:** `assets/customer.css`, `assets/icon-error.svg`

| Setting-ID | Type | Label (uit schema) |
| --- | --- | --- |
| `padding_top` | `range` | t:sections.all.padding.padding_top |
| `padding_bottom` | `range` | t:sections.all.padding.padding_bottom |

### 55. `sections/main-reset-password.liquid`
**Shopify Theme Editor naam:** t:sections.main-reset-password.name. **Settings:** 2. **Blocktypen:** 0.
**Aangeroepen door JSON-template(s):** `templates/customers/reset_password.json`
**Statische code-afhankelijkheden:** `assets/customer.css`, `assets/icon-error.svg`

| Setting-ID | Type | Label (uit schema) |
| --- | --- | --- |
| `padding_top` | `range` | t:sections.all.padding.padding_top |
| `padding_bottom` | `range` | t:sections.all.padding.padding_bottom |

### 56. `sections/main-search.liquid`
**Shopify Theme Editor naam:** t:sections.main-search.name. **Settings:** 14. **Blocktypen:** 0.
**Aangeroepen door JSON-template(s):** `templates/search.json`
**Statische code-afhankelijkheden:** `snippets/article-card.liquid`, `snippets/bc-card-product-search.liquid`, `snippets/bc-search-usp-strip.liquid`, `snippets/facets.liquid`, `snippets/loading-spinner.liquid`, `snippets/pagination.liquid`, `assets/component-card.css`, `assets/component-facets.css`, `assets/component-price.css`, `assets/component-search.css`, `assets/facets.js`, `assets/icon-caret.svg`, `assets/main-search.js`, `assets/mask-arch.svg`, `assets/mask-blobs.css`, `assets/template-collection.css`

| Setting-ID | Type | Label (uit schema) |
| --- | --- | --- |
| `columns_desktop` | `range` | t:sections.main-search.settings.columns_desktop.label |
| `columns_mobile` | `select` | t:sections.main-search.settings.columns_mobile.label |
| `image_ratio` | `select` | t:sections.main-search.settings.image_ratio.label |
| `image_shape` | `select` | t:sections.all.image_shape.label |
| `show_secondary_image` | `checkbox` | t:sections.main-search.settings.show_secondary_image.label |
| `show_vendor` | `checkbox` | t:sections.main-search.settings.show_vendor.label |
| `show_rating` | `checkbox` | t:sections.main-search.settings.show_rating.label |
| `enable_filtering` | `checkbox` | t:sections.main-collection-product-grid.settings.enable_filtering.label |
| `filter_type` | `select` | t:sections.main-collection-product-grid.settings.filter_type.label |
| `enable_sorting` | `checkbox` | t:sections.main-collection-product-grid.settings.enable_sorting.label |
| `article_show_date` | `checkbox` | t:sections.main-search.settings.article_show_date.label |
| `article_show_author` | `checkbox` | t:sections.main-search.settings.article_show_author.label |
| `padding_top` | `range` | t:sections.all.padding.padding_top |
| `padding_bottom` | `range` | t:sections.all.padding.padding_bottom |

### 57. `sections/multicolumn.liquid`
**Shopify Theme Editor naam:** t:sections.multicolumn.name. **Settings:** 14. **Blocktypen:** 1.
**Aangeroepen door JSON-template(s):** Geen directe JSON-template-match aangetroffen — mogelijk sectiegroup/dynamisch/niet actief.
**Statische code-afhankelijkheden:** `assets/component-slider.css`, `assets/icon-arrow.svg`, `assets/icon-caret.svg`, `assets/section-multicolumn.css`

| Setting-ID | Type | Label (uit schema) |
| --- | --- | --- |
| `title` | `inline_richtext` | t:sections.multicolumn.settings.title.label |
| `heading_size` | `select` | t:sections.all.heading_size.label |
| `image_width` | `select` | t:sections.multicolumn.settings.image_width.label |
| `image_ratio` | `select` | t:sections.multicolumn.settings.image_ratio.label |
| `button_label` | `text` | t:sections.multicolumn.settings.button_label.label |
| `button_link` | `url` | t:sections.multicolumn.settings.button_link.label |
| `columns_desktop` | `range` | t:sections.multicolumn.settings.columns_desktop.label |
| `column_alignment` | `select` | t:sections.multicolumn.settings.column_alignment.label |
| `background_style` | `select` | t:sections.multicolumn.settings.background_style.label |
| `color_scheme` | `color_scheme` | t:sections.all.colors.label |
| `columns_mobile` | `select` | t:sections.multicolumn.settings.columns_mobile.label |
| `swipe_on_mobile` | `checkbox` | t:sections.multicolumn.settings.swipe_on_mobile.label |
| `padding_top` | `range` | t:sections.all.padding.padding_top |
| `padding_bottom` | `range` | t:sections.all.padding.padding_bottom |

**Blocktypen en instelbare velden:**
- `column` (t:sections.multicolumn.blocks.column.name): `image`, `title`, `text`, `link_label`, `link`

### 58. `sections/multirow.liquid`
**Shopify Theme Editor naam:** t:sections.multirow.name. **Settings:** 13. **Blocktypen:** 1.
**Aangeroepen door JSON-template(s):** Geen directe JSON-template-match aangetroffen — mogelijk sectiegroup/dynamisch/niet actief.
**Statische code-afhankelijkheden:** `assets/component-image-with-text.css`

| Setting-ID | Type | Label (uit schema) |
| --- | --- | --- |
| `image_height` | `select` | t:sections.multirow.settings.image_height.label |
| `desktop_image_width` | `select` | t:sections.multirow.settings.desktop_image_width.label |
| `image_layout` | `select` | t:sections.multirow.settings.image_layout.label |
| `heading_size` | `select` | t:sections.all.heading_size.label |
| `text_style` | `select` | t:sections.multirow.settings.text_style.label |
| `button_style` | `select` | t:sections.multirow.settings.button_style.label |
| `desktop_content_position` | `select` | t:sections.multirow.settings.desktop_content_position.label |
| `desktop_content_alignment` | `select` | t:sections.multirow.settings.desktop_content_alignment.label |
| `mobile_content_alignment` | `select` | t:sections.multirow.settings.mobile_content_alignment.label |
| `section_color_scheme` | `color_scheme` | t:sections.all.colors.label |
| `row_color_scheme` | `color_scheme` | t:sections.multirow.settings.container_color_scheme.label |
| `padding_top` | `range` | t:sections.all.padding.padding_top |
| `padding_bottom` | `range` | t:sections.all.padding.padding_bottom |

**Blocktypen en instelbare velden:**
- `row` (t:sections.multirow.blocks.row.name): `image`, `caption`, `heading`, `text`, `button_label`, `button_link`

### 59. `sections/newsletter.liquid`
**Shopify Theme Editor naam:** t:sections.newsletter.name. **Settings:** 4. **Blocktypen:** 4.
**Aangeroepen door JSON-template(s):** Geen directe JSON-template-match aangetroffen — mogelijk sectiegroup/dynamisch/niet actief.
**Statische code-afhankelijkheden:** `assets/component-newsletter.css`, `assets/icon-arrow.svg`, `assets/icon-error.svg`, `assets/icon-success.svg`, `assets/newsletter-section.css`

| Setting-ID | Type | Label (uit schema) |
| --- | --- | --- |
| `color_scheme` | `color_scheme` | t:sections.all.colors.label |
| `full_width` | `checkbox` | t:sections.newsletter.settings.full_width.label |
| `padding_top` | `range` | t:sections.all.padding.padding_top |
| `padding_bottom` | `range` | t:sections.all.padding.padding_bottom |

**Blocktypen en instelbare velden:**
- `heading` (t:sections.newsletter.blocks.heading.name): `heading`, `heading_size`
- `paragraph` (t:sections.newsletter.blocks.paragraph.name): `text`
- `email_form` (t:sections.newsletter.blocks.email_form.name): geen velden
- `@app` (): geen velden

### 60. `sections/page.liquid`
**Shopify Theme Editor naam:** t:sections.page.name. **Settings:** 5. **Blocktypen:** 0.
**Aangeroepen door JSON-template(s):** Geen directe JSON-template-match aangetroffen — mogelijk sectiegroup/dynamisch/niet actief.
**Statische code-afhankelijkheden:** `assets/section-main-page.css`

| Setting-ID | Type | Label (uit schema) |
| --- | --- | --- |
| `page` | `page` | t:sections.page.settings.page.label |
| `heading_size` | `select` | t:sections.all.heading_size.label |
| `color_scheme` | `color_scheme` | t:sections.all.colors.label |
| `padding_top` | `range` | t:sections.all.padding.padding_top |
| `padding_bottom` | `range` | t:sections.all.padding.padding_bottom |

### 61. `sections/pickup-availability.liquid`
**Geen direct parsebaar Theme Editor-schema in dit bestand** (mogelijk via vaste sectiegroep of legacy-code).
**Aangeroepen door JSON-template(s):** Geen directe JSON-template-match aangetroffen — mogelijk sectiegroup/dynamisch/niet actief.
**Statische code-afhankelijkheden:** `assets/icon-close.svg`, `assets/icon-tick.svg`

### 62. `sections/predictive-search.liquid`
**Geen direct parsebaar Theme Editor-schema in dit bestand** (mogelijk via vaste sectiegroep of legacy-code).
**Aangeroepen door JSON-template(s):** Geen directe JSON-template-match aangetroffen — mogelijk sectiegroup/dynamisch/niet actief.
**Statische code-afhankelijkheden:** `snippets/loading-spinner.liquid`

### 63. `sections/product-description.liquid`
**Shopify Theme Editor naam:** Product Description. **Settings:** 0. **Blocktypen:** 0.
**Aangeroepen door JSON-template(s):** Geen directe JSON-template-match aangetroffen — mogelijk sectiegroup/dynamisch/niet actief.
**Statische code-afhankelijkheden:** Geen vaste render-/assetverwijzingen aangetroffen.

### 64. `sections/product-info.liquid`
**Shopify Theme Editor naam:** Product Info. **Settings:** 0. **Blocktypen:** 0.
**Aangeroepen door JSON-template(s):** Geen directe JSON-template-match aangetroffen — mogelijk sectiegroup/dynamisch/niet actief.
**Statische code-afhankelijkheden:** `snippets/buy-buttons.liquid`, `snippets/price.liquid`, `snippets/product-variant-picker.liquid`

### 65. `sections/product-media.liquid`
**Shopify Theme Editor naam:** Product Media. **Settings:** 0. **Blocktypen:** 0.
**Aangeroepen door JSON-template(s):** Geen directe JSON-template-match aangetroffen — mogelijk sectiegroup/dynamisch/niet actief.
**Statische code-afhankelijkheden:** `snippets/product-media-gallery.liquid`

### 66. `sections/product-specs.liquid`
**Shopify Theme Editor naam:** Product Specs. **Settings:** 0. **Blocktypen:** 0.
**Aangeroepen door JSON-template(s):** Geen directe JSON-template-match aangetroffen — mogelijk sectiegroup/dynamisch/niet actief.
**Statische code-afhankelijkheden:** `snippets/bc-product-spec-header.liquid`, `snippets/bc-product-spec-row.liquid`
**Rechtstreeks genoemde metafields:** `custom.aantal_straalsoorten_handdouche`, `custom.aantal_straalsoorten_hoofddouche`, `custom.aantal_uitgangen_tegelijk_bedienbaar`, `custom.afwerking_greep`, `custom.artikelnummer`, `custom.basiskleur`, `custom.bediening_voor_aan_uit`, `custom.belgaqua_keurmerk`, `custom.breedte_diameter_douchekop`, `custom.breedte_diameter_hoofddouche`, `custom.dikte_hoofddouche`, `custom.ean`, `custom.fabrikantnummer`, `custom.glansgraad`, `custom.hotbath_ecoair_system`, `custom.hotbath_fluhs`, `custom.hotbath_plumber_friendly`, `custom.hotbath_shower_power_system`, `custom.kleurgroep`, `custom.lengte_douchearm`, `custom.lengte_doucheslang`, `custom.materiaal_kraan`, `custom.met_doucheslang`, `custom.met_glijstang`, `custom.met_handdouche`, `custom.met_hoofddouche`, `custom.met_inbouwdeel`, `custom.montagewijze`, `custom.serie`, `custom.thermostatisch`, `custom.type_bevestiging_hoofddouche`, `custom.type_handdouche`, `custom.vorm_thermostaat`, `custom.vormgeving_stijlgroep`. Let op: definitiebestaan/gevulde waarden apart controleren.

### 67. `sections/quick-order-list.liquid`
**Shopify Theme Editor naam:** t:sections.quick-order-list.name. **Settings:** 6. **Blocktypen:** 0.
**Aangeroepen door JSON-template(s):** Geen directe JSON-template-match aangetroffen — mogelijk sectiegroup/dynamisch/niet actief.
**Statische code-afhankelijkheden:** `snippets/quick-order-list.liquid`, `assets/component-price.css`, `assets/price-per-item.js`, `assets/quantity-popover.css`, `assets/quantity-popover.js`, `assets/quick-order-list.css`, `assets/quick-order-list.js`

| Setting-ID | Type | Label (uit schema) |
| --- | --- | --- |
| `variants_per_page` | `range` | t:sections.quick-order-list.settings.variants_per_page.label |
| `show_image` | `checkbox` | t:sections.quick-order-list.settings.show_image.label |
| `show_sku` | `checkbox` | t:sections.quick-order-list.settings.show_sku.label |
| `color_scheme` | `color_scheme` | t:sections.all.colors.label |
| `padding_top` | `range` | t:sections.all.padding.padding_top |
| `padding_bottom` | `range` | t:sections.all.padding.padding_bottom |

### 68. `sections/related-products.liquid`
**Shopify Theme Editor naam:** t:sections.related-products.name. **Settings:** 13. **Blocktypen:** 0.
**Aangeroepen door JSON-template(s):** `templates/product.json`
**Statische code-afhankelijkheden:** `snippets/card-product.liquid`, `assets/component-card.css`, `assets/component-price.css`, `assets/mask-arch.svg`, `assets/mask-blobs.css`, `assets/section-related-products.css`

| Setting-ID | Type | Label (uit schema) |
| --- | --- | --- |
| `heading` | `inline_richtext` | t:sections.related-products.settings.heading.label |
| `heading_size` | `select` | t:sections.all.heading_size.label |
| `products_to_show` | `range` | t:sections.related-products.settings.products_to_show.label |
| `columns_desktop` | `range` | t:sections.related-products.settings.columns_desktop.label |
| `columns_mobile` | `select` | t:sections.related-products.settings.columns_mobile.label |
| `color_scheme` | `color_scheme` | t:sections.all.colors.label |
| `image_ratio` | `select` | t:sections.related-products.settings.image_ratio.label |
| `image_shape` | `select` | t:sections.all.image_shape.label |
| `show_secondary_image` | `checkbox` | t:sections.related-products.settings.show_secondary_image.label |
| `show_vendor` | `checkbox` | t:sections.related-products.settings.show_vendor.label |
| `show_rating` | `checkbox` | t:sections.related-products.settings.show_rating.label |
| `padding_top` | `range` | t:sections.all.padding.padding_top |
| `padding_bottom` | `range` | t:sections.all.padding.padding_bottom |

### 69. `sections/rich-text.liquid`
**Shopify Theme Editor naam:** t:sections.rich-text.name. **Settings:** 6. **Blocktypen:** 4.
**Aangeroepen door JSON-template(s):** Geen directe JSON-template-match aangetroffen — mogelijk sectiegroup/dynamisch/niet actief.
**Statische code-afhankelijkheden:** `assets/section-rich-text.css`

| Setting-ID | Type | Label (uit schema) |
| --- | --- | --- |
| `desktop_content_position` | `select` | t:sections.rich-text.settings.desktop_content_position.label |
| `content_alignment` | `select` | t:sections.rich-text.settings.content_alignment.label |
| `color_scheme` | `color_scheme` | t:sections.all.colors.label |
| `full_width` | `checkbox` | t:sections.rich-text.settings.full_width.label |
| `padding_top` | `range` | t:sections.all.padding.padding_top |
| `padding_bottom` | `range` | t:sections.all.padding.padding_bottom |

**Blocktypen en instelbare velden:**
- `heading` (t:sections.rich-text.blocks.heading.name): `heading`, `heading_size`
- `caption` (t:sections.rich-text.blocks.caption.name): `caption`, `text_style`, `text_size`
- `text` (t:sections.rich-text.blocks.text.name): `text`
- `button` (t:sections.rich-text.blocks.buttons.name): `button_label`, `button_link`, `button_style_secondary`, `button_label_2`, `button_link_2`, `button_style_secondary_2`

### 70. `sections/short-specs.liquid`
**Shopify Theme Editor naam:** Short Specs. **Settings:** 1. **Blocktypen:** 0.
**Aangeroepen door JSON-template(s):** Geen directe JSON-template-match aangetroffen — mogelijk sectiegroup/dynamisch/niet actief.
**Statische code-afhankelijkheden:** `snippets/bc-product-spec-row.liquid`
**Rechtstreeks genoemde metafields:** `custom.aantal_straalsoorten_hoofddouche`, `custom.aantal_uitgangen_tegelijk_bedienbaar`, `custom.basiskleur`, `custom.breedte_diameter_hoofddouche`, `custom.thermostatisch`. Let op: definitiebestaan/gevulde waarden apart controleren.

| Setting-ID | Type | Label (uit schema) |
| --- | --- | --- |
| `title` | `text` | Titel |

### 71. `sections/slideshow.liquid`
**Shopify Theme Editor naam:** t:sections.slideshow.name. **Settings:** 8. **Blocktypen:** 1.
**Aangeroepen door JSON-template(s):** Geen directe JSON-template-match aangetroffen — mogelijk sectiegroup/dynamisch/niet actief.
**Statische code-afhankelijkheden:** `assets/component-slider.css`, `assets/component-slideshow.css`, `assets/icon-caret.svg`, `assets/icon-pause.svg`, `assets/icon-play.svg`, `assets/section-image-banner.css`, `assets/theme-editor.js`

| Setting-ID | Type | Label (uit schema) |
| --- | --- | --- |
| `layout` | `select` | t:sections.slideshow.settings.layout.label |
| `slide_height` | `select` | t:sections.slideshow.settings.slide_height.label |
| `slider_visual` | `select` | t:sections.slideshow.settings.slider_visual.label |
| `auto_rotate` | `checkbox` | t:sections.slideshow.settings.auto_rotate.label |
| `change_slides_speed` | `range` | t:sections.slideshow.settings.change_slides_speed.label |
| `image_behavior` | `select` | t:sections.all.animation.image_behavior.label |
| `show_text_below` | `checkbox` | t:sections.slideshow.settings.show_text_below.label |
| `accessibility_info` | `text` | t:sections.slideshow.settings.accessibility.label |

**Blocktypen en instelbare velden:**
- `slide` (t:sections.slideshow.blocks.slide.name): `image`, `image_overlay_opacity`, `heading`, `heading_size`, `subheading`, `button_label`, `link`, `button_style_secondary`, `show_text_box`, `box_align`, `text_alignment`, `text_alignment_mobile`, `color_scheme`

### 72. `sections/usps.liquid`
**Shopify Theme Editor naam:** USPs. **Settings:** 0. **Blocktypen:** 0.
**Aangeroepen door JSON-template(s):** Geen directe JSON-template-match aangetroffen — mogelijk sectiegroup/dynamisch/niet actief.
**Statische code-afhankelijkheden:** Geen vaste render-/assetverwijzingen aangetroffen.

### 73. `sections/video.liquid`
**Shopify Theme Editor naam:** t:sections.video.name. **Settings:** 11. **Blocktypen:** 0.
**Aangeroepen door JSON-template(s):** Geen directe JSON-template-match aangetroffen — mogelijk sectiegroup/dynamisch/niet actief.
**Statische code-afhankelijkheden:** `assets/component-deferred-media.css`, `assets/icon-play.svg`, `assets/video-section.css`

| Setting-ID | Type | Label (uit schema) |
| --- | --- | --- |
| `heading` | `inline_richtext` | t:sections.video.settings.heading.label |
| `heading_size` | `select` | t:sections.all.heading_size.label |
| `enable_video_looping` | `checkbox` | t:sections.video.settings.enable_video_looping.label |
| `video` | `video` | t:sections.video.settings.video.label |
| `video_url` | `video_url` | t:sections.video.settings.video_url.label |
| `cover_image` | `image_picker` | t:sections.video.settings.cover_image.label |
| `description` | `text` | t:sections.video.settings.description.label |
| `full_width` | `checkbox` | t:sections.video.settings.full_width.label |
| `color_scheme` | `color_scheme` | t:sections.all.colors.label |
| `padding_top` | `range` | t:sections.all.padding.padding_top |
| `padding_bottom` | `range` | t:sections.all.padding.padding_bottom |

## Referentiegrenzen

- Dit document claimt **niet** dat elk component bereikbaar of productief goedgekeurd is. Kijk in de daadwerkelijke actieve JSON-templates en Shopify Admin.
- `sections/main-product.liquid` bevat omvangrijke product-UI en interne CSS; een setting-ID zegt nog niets over het renderpad.
- `sections/bc-meubelhub.liquid` wordt via de collectie-`templateSuffix` geactiveerd. Cruciale extra CSS ligt óók in de Shopify-collectieomschrijving.
- Een snippet dat alleen in test- of backupbestanden voorkomt is geen bewezen actieve functie.
- Liquid `asset_url`-verwijzingen kunnen per template verschillen en zijn geen laadgarantie op alle pagina's.
- Vergelijk `docs/SHOPIFY_ADMIN_STRUCTURE_2026-10-07.json` met product.metafields en Shopify Admin voordat je import-schema's wijzigt.
- Wijzig settings/blokken via een conceptthema; publicatie en Admin-data-acties apart goedkeuren.

