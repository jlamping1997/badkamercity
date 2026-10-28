# featured-collection

**Bron:** `sections/featured-collection.liquid`. Bronstatus: BYTE_MATCH.

[Functioneel dossier](../../components/FOUNDATIONS_AND_TOOLING.md) · [Bronhashes](../source-index.json) · [Alle secties](../SECTIONS.md)

Dit is de bronreferentie. Het dossier geeft de bedoeling, data-eigenaar, toestanden en onderhoudsgrenzen.

## Koppelingen

Letterlijke callers: `templates/cart.json`.

Letterlijke uitgaande refs: `assets/component-card.css`, `assets/component-slider.css`, `assets/icon-caret.svg`, `assets/mask-arch.svg`, `assets/mask-blobs.css`, `assets/price-per-item.js`, `assets/product-form.js`, `assets/quantity-popover.js`, `assets/quick-add-bulk.js`, `assets/quick-add.css`, `assets/quick-add.js`, `assets/quick-order-list.js`, `assets/template-collection.css`, `snippets/card-product.liquid`.

Geen caller gevonden betekent niet ongebruikt: Theme Editor, platformsections en dynamische aanroepen vallen buiten deze parser.

## Schema-instellingen

| ID | Type | Label / opties |
| --- | --- | --- |
| `collection` | `collection` | t:sections.featured-collection.settings.collection.label |
| `products_to_show` | `range` | t:sections.featured-collection.settings.products_to_show.label |
| `title` | `inline_richtext` | t:sections.featured-collection.settings.title.label |
| `heading_size` | `select` | t:sections.all.heading_size.label: h2: t:sections.all.heading_size.options__1.label; h1: t:sections.all.heading_size.options__2.label; h0: t:sections.all.heading_size.options__3.label; hxl: t:sections.all.heading_size.options__4.label; hxxl: t:sections.all.heading_size.options__5.label |
| `description` | `richtext` | t:sections.featured-collection.settings.description.label |
| `show_description` | `checkbox` | t:sections.featured-collection.settings.show_description.label |
| `description_style` | `select` | t:sections.featured-collection.settings.description_style.label: body: t:sections.featured-collection.settings.description_style.options__1.label; subtitle: t:sections.featured-collection.settings.description_style.options__2.label; uppercase: t:sections.featured-collection.settings.description_style.options__3.label |
| `columns_desktop` | `range` | t:sections.featured-collection.settings.columns_desktop.label |
| `enable_desktop_slider` | `checkbox` | t:sections.featured-collection.settings.enable_desktop_slider.label |
| `full_width` | `checkbox` | t:sections.featured-collection.settings.full_width.label |
| `show_view_all` | `checkbox` | t:sections.featured-collection.settings.show_view_all.label |
| `view_all_style` | `select` | t:sections.featured-collection.settings.view_all_style.label: link: t:sections.featured-collection.settings.view_all_style.options__1.label; outline: t:sections.featured-collection.settings.view_all_style.options__2.label; solid: t:sections.featured-collection.settings.view_all_style.options__3.label |
| `color_scheme` | `color_scheme` | t:sections.all.colors.label |
| `image_ratio` | `select` | t:sections.featured-collection.settings.image_ratio.label: adapt: t:sections.featured-collection.settings.image_ratio.options__1.label; portrait: t:sections.featured-collection.settings.image_ratio.options__2.label; square: t:sections.featured-collection.settings.image_ratio.options__3.label |
| `image_shape` | `select` | t:sections.all.image_shape.label: default: t:sections.all.image_shape.options__1.label; arch: t:sections.all.image_shape.options__2.label; blob: t:sections.all.image_shape.options__3.label; chevronleft: t:sections.all.image_shape.options__4.label; chevronright: t:sections.all.image_shape.options__5.label; diamond: t:sections.all.image_shape.options__6.label; parallelogram: t:sections.all.image_shape.options__7.label; round: t:sections.all.image_shape.options__8.label |
| `show_secondary_image` | `checkbox` | t:sections.featured-collection.settings.show_secondary_image.label |
| `show_vendor` | `checkbox` | t:sections.featured-collection.settings.show_vendor.label |
| `show_rating` | `checkbox` | t:sections.featured-collection.settings.show_rating.label |
| `quick_add` | `select` | t:sections.main-collection-product-grid.settings.quick_add.label: none: t:sections.main-collection-product-grid.settings.quick_add.options.option_1; standard: t:sections.main-collection-product-grid.settings.quick_add.options.option_2; bulk: t:sections.main-collection-product-grid.settings.quick_add.options.option_3 |
| `columns_mobile` | `select` | t:sections.featured-collection.settings.columns_mobile.label: 1: t:sections.featured-collection.settings.columns_mobile.options__1.label; 2: t:sections.featured-collection.settings.columns_mobile.options__2.label |
| `swipe_on_mobile` | `checkbox` | t:sections.featured-collection.settings.swipe_on_mobile.label |
| `padding_top` | `range` | t:sections.all.padding.padding_top |
| `padding_bottom` | `range` | t:sections.all.padding.padding_bottom |

## Technische ingangen

Formtypen: —.

Letterlijke events in deze bron: —.

Letterlijke metafieldkeys: —.

DOM-hooks: `data-id`.

Geen vermelding sluit dynamische keys, externe handlers of platformwerking niet uit. Inhoud/defaults en huidige product-/contact-/settingswaarden worden niet door deze tool gepubliceerd.
