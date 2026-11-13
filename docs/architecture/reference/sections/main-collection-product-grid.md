# main-collection-product-grid

**Bron:** `sections/main-collection-product-grid.liquid`. Bronstatus: BYTE_MATCH.

[Functioneel dossier](../../components/PRODUCT_CARDS_AND_FILTERS.md) · [Bronhashes](../source-index.json) · [Alle secties](../SECTIONS.md)

Dit is de bronreferentie. Het dossier geeft de bedoeling, data-eigenaar, toestanden en onderhoudsgrenzen.

## Koppelingen

Letterlijke callers: `templates/collection.json`.

Letterlijke uitgaande refs: `assets/bc-collection.css`, `assets/component-card.css`, `assets/component-facets.css`, `assets/facets.js`, `assets/icon-caret.svg`, `assets/mask-arch.svg`, `assets/mask-blobs.css`, `assets/price-per-item.js`, `assets/product-form.js`, `assets/quantity-popover.js`, `assets/quick-add-bulk.js`, `assets/quick-add.css`, `assets/quick-add.js`, `assets/quick-order-list.js`, `assets/template-collection.css`, `snippets/bc-collection-active-filters.liquid`, `snippets/bc-external-filters.liquid`, `snippets/bc-mobile-listing.liquid`, `snippets/card-product.liquid`, `snippets/facets.liquid`, `snippets/loading-spinner.liquid`, `snippets/pagination.liquid`.

Geen caller gevonden betekent niet ongebruikt: Theme Editor, platformsections en dynamische aanroepen vallen buiten deze parser.

## Schema-instellingen

| ID | Type | Label / opties |
| --- | --- | --- |
| `products_per_page` | `range` | t:sections.main-collection-product-grid.settings.products_per_page.label |
| `columns_desktop` | `range` | t:sections.main-collection-product-grid.settings.columns_desktop.label |
| `columns_mobile` | `select` | t:sections.main-collection-product-grid.settings.columns_mobile.label: 1: t:sections.main-collection-product-grid.settings.columns_mobile.options__1.label; 2: t:sections.main-collection-product-grid.settings.columns_mobile.options__2.label |
| `color_scheme` | `color_scheme` | t:sections.all.colors.label |
| `image_ratio` | `select` | t:sections.main-collection-product-grid.settings.image_ratio.label: adapt: t:sections.main-collection-product-grid.settings.image_ratio.options__1.label; portrait: t:sections.main-collection-product-grid.settings.image_ratio.options__2.label; square: t:sections.main-collection-product-grid.settings.image_ratio.options__3.label |
| `image_shape` | `select` | t:sections.all.image_shape.label: default: t:sections.all.image_shape.options__1.label; arch: t:sections.all.image_shape.options__2.label; blob: t:sections.all.image_shape.options__3.label; chevronleft: t:sections.all.image_shape.options__4.label; chevronright: t:sections.all.image_shape.options__5.label; diamond: t:sections.all.image_shape.options__6.label; parallelogram: t:sections.all.image_shape.options__7.label; round: t:sections.all.image_shape.options__8.label |
| `show_secondary_image` | `checkbox` | t:sections.main-collection-product-grid.settings.show_secondary_image.label |
| `show_vendor` | `checkbox` | t:sections.main-collection-product-grid.settings.show_vendor.label |
| `show_rating` | `checkbox` | t:sections.main-collection-product-grid.settings.show_rating.label |
| `quick_add` | `select` | t:sections.main-collection-product-grid.settings.quick_add.label: none: t:sections.main-collection-product-grid.settings.quick_add.options.option_1; standard: t:sections.main-collection-product-grid.settings.quick_add.options.option_2; bulk: t:sections.main-collection-product-grid.settings.quick_add.options.option_3 |
| `enable_filtering` | `checkbox` | t:sections.main-collection-product-grid.settings.enable_filtering.label |
| `filter_type` | `select` | t:sections.main-collection-product-grid.settings.filter_type.label: horizontal: t:sections.main-collection-product-grid.settings.filter_type.options__1.label; vertical: t:sections.main-collection-product-grid.settings.filter_type.options__2.label; drawer: t:sections.main-collection-product-grid.settings.filter_type.options__3.label |
| `enable_sorting` | `checkbox` | t:sections.main-collection-product-grid.settings.enable_sorting.label |
| `padding_top` | `range` | t:sections.all.padding.padding_top |
| `padding_bottom` | `range` | t:sections.all.padding.padding_bottom |

## Technische ingangen

Formtypen: —.

Letterlijke events in deze bron: —.

Letterlijke metafieldkeys: —.

DOM-hooks: `data-id`.

Geen vermelding sluit dynamische keys, externe handlers of platformwerking niet uit. Inhoud/defaults en huidige product-/contact-/settingswaarden worden niet door deze tool gepubliceerd.
