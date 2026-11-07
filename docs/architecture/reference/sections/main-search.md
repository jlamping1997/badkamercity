# main-search

**Bron:** `sections/main-search.liquid`. Bronstatus: BYTE_MATCH.

[Functioneel dossier](../../components/PRODUCT_CARDS_AND_FILTERS.md) · [Bronhashes](../source-index.json) · [Alle secties](../SECTIONS.md)

Dit is de bronreferentie. Het dossier geeft de bedoeling, data-eigenaar, toestanden en onderhoudsgrenzen.

## Koppelingen

Letterlijke callers: `templates/search.bc-mobile-review.liquid`, `templates/search.json`.

Letterlijke uitgaande refs: `assets/component-card.css`, `assets/component-facets.css`, `assets/facets.js`, `assets/icon-caret.svg`, `assets/main-search.js`, `assets/mask-arch.svg`, `assets/mask-blobs.css`, `assets/template-collection.css`, `snippets/article-card.liquid`, `snippets/bc-card-product-search.liquid`, `snippets/bc-external-filters.liquid`, `snippets/bc-mobile-listing.liquid`, `snippets/bc-search-usp-strip.liquid`, `snippets/facets.liquid`, `snippets/loading-spinner.liquid`, `snippets/pagination.liquid`.

Geen caller gevonden betekent niet ongebruikt: Theme Editor, platformsections en dynamische aanroepen vallen buiten deze parser.

## Schema-instellingen

| ID | Type | Label / opties |
| --- | --- | --- |
| `columns_desktop` | `range` | t:sections.main-search.settings.columns_desktop.label |
| `columns_mobile` | `select` | t:sections.main-search.settings.columns_mobile.label: 1: t:sections.main-search.settings.columns_mobile.options__1.label; 2: t:sections.main-search.settings.columns_mobile.options__2.label |
| `image_ratio` | `select` | t:sections.main-search.settings.image_ratio.label: adapt: t:sections.main-search.settings.image_ratio.options__1.label; portrait: t:sections.main-search.settings.image_ratio.options__2.label; square: t:sections.main-search.settings.image_ratio.options__3.label |
| `image_shape` | `select` | t:sections.all.image_shape.label: default: t:sections.all.image_shape.options__1.label; arch: t:sections.all.image_shape.options__2.label; blob: t:sections.all.image_shape.options__3.label; chevronleft: t:sections.all.image_shape.options__4.label; chevronright: t:sections.all.image_shape.options__5.label; diamond: t:sections.all.image_shape.options__6.label; parallelogram: t:sections.all.image_shape.options__7.label; round: t:sections.all.image_shape.options__8.label |
| `show_secondary_image` | `checkbox` | t:sections.main-search.settings.show_secondary_image.label |
| `show_vendor` | `checkbox` | t:sections.main-search.settings.show_vendor.label |
| `show_rating` | `checkbox` | t:sections.main-search.settings.show_rating.label |
| `enable_filtering` | `checkbox` | t:sections.main-collection-product-grid.settings.enable_filtering.label |
| `filter_type` | `select` | t:sections.main-collection-product-grid.settings.filter_type.label: horizontal: t:sections.main-collection-product-grid.settings.filter_type.options__1.label; vertical: t:sections.main-collection-product-grid.settings.filter_type.options__2.label; drawer: t:sections.main-collection-product-grid.settings.filter_type.options__3.label |
| `enable_sorting` | `checkbox` | t:sections.main-collection-product-grid.settings.enable_sorting.label |
| `article_show_date` | `checkbox` | t:sections.main-search.settings.article_show_date.label |
| `article_show_author` | `checkbox` | t:sections.main-search.settings.article_show_author.label |
| `padding_top` | `range` | t:sections.all.padding.padding_top |
| `padding_bottom` | `range` | t:sections.all.padding.padding_bottom |

## Technische ingangen

Formtypen: —.

Letterlijke events in deze bron: —.

Letterlijke metafieldkeys: —.

DOM-hooks: `data-id`.

Geen vermelding sluit dynamische keys, externe handlers of platformwerking niet uit. Inhoud/defaults en huidige product-/contact-/settingswaarden worden niet door deze tool gepubliceerd.
