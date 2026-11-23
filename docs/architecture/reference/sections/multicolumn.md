# multicolumn

**Bron:** `sections/multicolumn.liquid`. Bronstatus: BYTE_MATCH.

[Functioneel dossier](../../components/FOUNDATIONS_AND_TOOLING.md) · [Bronhashes](../source-index.json) · [Alle secties](../SECTIONS.md)

Dit is de bronreferentie. Het dossier geeft de bedoeling, data-eigenaar, toestanden en onderhoudsgrenzen.

## Koppelingen

Letterlijke callers: —.

Letterlijke uitgaande refs: `assets/component-slider.css`, `assets/icon-arrow.svg`, `assets/icon-caret.svg`, `assets/section-multicolumn.css`.

Geen caller gevonden betekent niet ongebruikt: Theme Editor, platformsections en dynamische aanroepen vallen buiten deze parser.

## Schema-instellingen

| ID | Type | Label / opties |
| --- | --- | --- |
| `title` | `inline_richtext` | t:sections.multicolumn.settings.title.label |
| `heading_size` | `select` | t:sections.all.heading_size.label: h2: t:sections.all.heading_size.options__1.label; h1: t:sections.all.heading_size.options__2.label; h0: t:sections.all.heading_size.options__3.label; hxl: t:sections.all.heading_size.options__4.label; hxxl: t:sections.all.heading_size.options__5.label |
| `image_width` | `select` | t:sections.multicolumn.settings.image_width.label: third: t:sections.multicolumn.settings.image_width.options__1.label; half: t:sections.multicolumn.settings.image_width.options__2.label; full: t:sections.multicolumn.settings.image_width.options__3.label |
| `image_ratio` | `select` | t:sections.multicolumn.settings.image_ratio.label: adapt: t:sections.multicolumn.settings.image_ratio.options__1.label; portrait: t:sections.multicolumn.settings.image_ratio.options__2.label; square: t:sections.multicolumn.settings.image_ratio.options__3.label; circle: t:sections.multicolumn.settings.image_ratio.options__4.label |
| `button_label` | `text` | t:sections.multicolumn.settings.button_label.label |
| `button_link` | `url` | t:sections.multicolumn.settings.button_link.label |
| `columns_desktop` | `range` | t:sections.multicolumn.settings.columns_desktop.label |
| `column_alignment` | `select` | t:sections.multicolumn.settings.column_alignment.label: left: t:sections.multicolumn.settings.column_alignment.options__1.label; center: t:sections.multicolumn.settings.column_alignment.options__2.label |
| `background_style` | `select` | t:sections.multicolumn.settings.background_style.label: none: t:sections.multicolumn.settings.background_style.options__1.label; primary: t:sections.multicolumn.settings.background_style.options__2.label |
| `color_scheme` | `color_scheme` | t:sections.all.colors.label |
| `columns_mobile` | `select` | t:sections.multicolumn.settings.columns_mobile.label: 1: t:sections.multicolumn.settings.columns_mobile.options__1.label; 2: t:sections.multicolumn.settings.columns_mobile.options__2.label |
| `swipe_on_mobile` | `checkbox` | t:sections.multicolumn.settings.swipe_on_mobile.label |
| `padding_top` | `range` | t:sections.all.padding.padding_top |
| `padding_bottom` | `range` | t:sections.all.padding.padding_bottom |

## Blocktype column

| ID | Type | Label / opties |
| --- | --- | --- |
| `image` | `image_picker` | t:sections.multicolumn.blocks.column.settings.image.label |
| `title` | `inline_richtext` | t:sections.multicolumn.blocks.column.settings.title.label |
| `text` | `richtext` | t:sections.multicolumn.blocks.column.settings.text.label |
| `link_label` | `text` | t:sections.multicolumn.blocks.column.settings.link_label.label |
| `link` | `url` | t:sections.multicolumn.blocks.column.settings.link.label |

## Technische ingangen

Formtypen: —.

Letterlijke events in deze bron: —.

Letterlijke metafieldkeys: —.

DOM-hooks: —.

Geen vermelding sluit dynamische keys, externe handlers of platformwerking niet uit. Inhoud/defaults en huidige product-/contact-/settingswaarden worden niet door deze tool gepubliceerd.
