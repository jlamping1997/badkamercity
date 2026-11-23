# related-products

**Bron:** `sections/related-products.liquid`. Bronstatus: BYTE_MATCH.

[Functioneel dossier](../../components/PRODUCT_PAGES.md) · [Bronhashes](../source-index.json) · [Alle secties](../SECTIONS.md)

Dit is de bronreferentie. Het dossier geeft de bedoeling, data-eigenaar, toestanden en onderhoudsgrenzen.

## Koppelingen

Letterlijke callers: `sections/bc-related-products.liquid`, `templates/product.json`.

Letterlijke uitgaande refs: `assets/component-card.css`, `assets/mask-arch.svg`, `assets/mask-blobs.css`, `assets/section-related-products.css`, `snippets/card-product.liquid`.

Geen caller gevonden betekent niet ongebruikt: Theme Editor, platformsections en dynamische aanroepen vallen buiten deze parser.

## Schema-instellingen

| ID | Type | Label / opties |
| --- | --- | --- |
| `heading` | `inline_richtext` | t:sections.related-products.settings.heading.label |
| `heading_size` | `select` | t:sections.all.heading_size.label: h2: t:sections.all.heading_size.options__1.label; h1: t:sections.all.heading_size.options__2.label; h0: t:sections.all.heading_size.options__3.label; hxl: t:sections.all.heading_size.options__4.label; hxxl: t:sections.all.heading_size.options__5.label |
| `products_to_show` | `range` | t:sections.related-products.settings.products_to_show.label |
| `columns_desktop` | `range` | t:sections.related-products.settings.columns_desktop.label |
| `columns_mobile` | `select` | t:sections.related-products.settings.columns_mobile.label: 1: t:sections.related-products.settings.columns_mobile.options__1.label; 2: t:sections.related-products.settings.columns_mobile.options__2.label |
| `color_scheme` | `color_scheme` | t:sections.all.colors.label |
| `image_ratio` | `select` | t:sections.related-products.settings.image_ratio.label: adapt: t:sections.related-products.settings.image_ratio.options__1.label; portrait: t:sections.related-products.settings.image_ratio.options__2.label; square: t:sections.related-products.settings.image_ratio.options__3.label |
| `image_shape` | `select` | t:sections.all.image_shape.label: default: t:sections.all.image_shape.options__1.label; arch: t:sections.all.image_shape.options__2.label; blob: t:sections.all.image_shape.options__3.label; chevronleft: t:sections.all.image_shape.options__4.label; chevronright: t:sections.all.image_shape.options__5.label; diamond: t:sections.all.image_shape.options__6.label; parallelogram: t:sections.all.image_shape.options__7.label; round: t:sections.all.image_shape.options__8.label |
| `show_secondary_image` | `checkbox` | t:sections.related-products.settings.show_secondary_image.label |
| `show_vendor` | `checkbox` | t:sections.related-products.settings.show_vendor.label |
| `show_rating` | `checkbox` | t:sections.related-products.settings.show_rating.label |
| `padding_top` | `range` | t:sections.all.padding.padding_top |
| `padding_bottom` | `range` | t:sections.all.padding.padding_bottom |

## Technische ingangen

Formtypen: —.

Letterlijke events in deze bron: —.

Letterlijke metafieldkeys: —.

DOM-hooks: `data-product-id`, `data-section-id`, `data-url`.

Geen vermelding sluit dynamische keys, externe handlers of platformwerking niet uit. Inhoud/defaults en huidige product-/contact-/settingswaarden worden niet door deze tool gepubliceerd.
