# collection-list

**Bron:** `sections/collection-list.liquid`. Bronstatus: BYTE_MATCH.

[Functioneel dossier](../../components/FOUNDATIONS_AND_TOOLING.md) · [Bronhashes](../source-index.json) · [Alle secties](../SECTIONS.md)

Dit is de bronreferentie. Het dossier geeft de bedoeling, data-eigenaar, toestanden en onderhoudsgrenzen.

## Koppelingen

Letterlijke callers: —.

Letterlijke uitgaande refs: `assets/component-card.css`, `assets/component-slider.css`, `assets/icon-caret.svg`, `assets/section-collection-list.css`, `snippets/card-collection.liquid`.

Geen caller gevonden betekent niet ongebruikt: Theme Editor, platformsections en dynamische aanroepen vallen buiten deze parser.

## Schema-instellingen

| ID | Type | Label / opties |
| --- | --- | --- |
| `title` | `inline_richtext` | t:sections.collection-list.settings.title.label |
| `heading_size` | `select` | t:sections.all.heading_size.label: h2: t:sections.all.heading_size.options__1.label; h1: t:sections.all.heading_size.options__2.label; h0: t:sections.all.heading_size.options__3.label; hxl: t:sections.all.heading_size.options__4.label; hxxl: t:sections.all.heading_size.options__5.label |
| `image_ratio` | `select` | t:sections.collection-list.settings.image_ratio.label: adapt: t:sections.collection-list.settings.image_ratio.options__1.label; portrait: t:sections.collection-list.settings.image_ratio.options__2.label; square: t:sections.collection-list.settings.image_ratio.options__3.label |
| `columns_desktop` | `range` | t:sections.collection-list.settings.columns_desktop.label |
| `color_scheme` | `color_scheme` | t:sections.all.colors.label |
| `show_view_all` | `checkbox` | t:sections.collection-list.settings.show_view_all.label |
| `columns_mobile` | `select` | t:sections.collection-list.settings.columns_mobile.label: 1: t:sections.collection-list.settings.columns_mobile.options__1.label; 2: t:sections.collection-list.settings.columns_mobile.options__2.label |
| `swipe_on_mobile` | `checkbox` | t:sections.collection-list.settings.swipe_on_mobile.label |
| `padding_top` | `range` | t:sections.all.padding.padding_top |
| `padding_bottom` | `range` | t:sections.all.padding.padding_bottom |

## Blocktype featured_collection

| ID | Type | Label / opties |
| --- | --- | --- |
| `collection` | `collection` | t:sections.collection-list.blocks.featured_collection.settings.collection.label |

## Technische ingangen

Formtypen: —.

Letterlijke events in deze bron: —.

Letterlijke metafieldkeys: —.

DOM-hooks: —.

Geen vermelding sluit dynamische keys, externe handlers of platformwerking niet uit. Inhoud/defaults en huidige product-/contact-/settingswaarden worden niet door deze tool gepubliceerd.
