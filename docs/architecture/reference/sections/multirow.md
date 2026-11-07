# multirow

**Bron:** `sections/multirow.liquid`. Bronstatus: BYTE_MATCH.

[Functioneel dossier](../../components/FOUNDATIONS_AND_TOOLING.md) · [Bronhashes](../source-index.json) · [Alle secties](../SECTIONS.md)

Dit is de bronreferentie. Het dossier geeft de bedoeling, data-eigenaar, toestanden en onderhoudsgrenzen.

## Koppelingen

Letterlijke callers: —.

Letterlijke uitgaande refs: `assets/component-image-with-text.css`.

Geen caller gevonden betekent niet ongebruikt: Theme Editor, platformsections en dynamische aanroepen vallen buiten deze parser.

## Schema-instellingen

| ID | Type | Label / opties |
| --- | --- | --- |
| `image_height` | `select` | t:sections.multirow.settings.image_height.label: adapt: t:sections.multirow.settings.image_height.options__1.label; small: t:sections.multirow.settings.image_height.options__2.label; medium: t:sections.multirow.settings.image_height.options__3.label; large: t:sections.multirow.settings.image_height.options__4.label |
| `desktop_image_width` | `select` | t:sections.multirow.settings.desktop_image_width.label: small: t:sections.multirow.settings.desktop_image_width.options__1.label; medium: t:sections.multirow.settings.desktop_image_width.options__2.label; large: t:sections.multirow.settings.desktop_image_width.options__3.label |
| `image_layout` | `select` | t:sections.multirow.settings.image_layout.label: alternate-left: t:sections.multirow.settings.image_layout.options__1.label; alternate-right: t:sections.multirow.settings.image_layout.options__2.label; align-left: t:sections.multirow.settings.image_layout.options__3.label; align-right: t:sections.multirow.settings.image_layout.options__4.label |
| `heading_size` | `select` | t:sections.all.heading_size.label: h2: t:sections.all.heading_size.options__1.label; h1: t:sections.all.heading_size.options__2.label; h0: t:sections.all.heading_size.options__3.label; hxl: t:sections.all.heading_size.options__4.label; hxxl: t:sections.all.heading_size.options__5.label |
| `text_style` | `select` | t:sections.multirow.settings.text_style.label: body: t:sections.multirow.settings.text_style.options__1.label; subtitle: t:sections.multirow.settings.text_style.options__2.label |
| `button_style` | `select` | t:sections.multirow.settings.button_style.label: primary: t:sections.multirow.settings.button_style.options__1.label; secondary: t:sections.multirow.settings.button_style.options__2.label |
| `desktop_content_position` | `select` | t:sections.multirow.settings.desktop_content_position.label: top: t:sections.multirow.settings.desktop_content_position.options__1.label; middle: t:sections.multirow.settings.desktop_content_position.options__2.label; bottom: t:sections.multirow.settings.desktop_content_position.options__3.label |
| `desktop_content_alignment` | `select` | t:sections.multirow.settings.desktop_content_alignment.label: left: t:sections.multirow.settings.desktop_content_alignment.options__1.label; center: t:sections.multirow.settings.desktop_content_alignment.options__2.label; right: t:sections.multirow.settings.desktop_content_alignment.options__3.label |
| `mobile_content_alignment` | `select` | t:sections.multirow.settings.mobile_content_alignment.label: left: t:sections.multirow.settings.mobile_content_alignment.options__1.label; center: t:sections.multirow.settings.mobile_content_alignment.options__2.label; right: t:sections.multirow.settings.mobile_content_alignment.options__3.label |
| `section_color_scheme` | `color_scheme` | t:sections.all.colors.label |
| `row_color_scheme` | `color_scheme` | t:sections.multirow.settings.container_color_scheme.label |
| `padding_top` | `range` | t:sections.all.padding.padding_top |
| `padding_bottom` | `range` | t:sections.all.padding.padding_bottom |

## Blocktype row

| ID | Type | Label / opties |
| --- | --- | --- |
| `image` | `image_picker` | t:sections.multirow.blocks.row.settings.image.label |
| `caption` | `text` | t:sections.multirow.blocks.row.settings.caption.label |
| `heading` | `inline_richtext` | t:sections.multirow.blocks.row.settings.heading.label |
| `text` | `richtext` | t:sections.multirow.blocks.row.settings.text.label |
| `button_label` | `text` | t:sections.multirow.blocks.row.settings.button_label.label |
| `button_link` | `url` | t:sections.multirow.blocks.row.settings.button_link.label |

## Technische ingangen

Formtypen: —.

Letterlijke events in deze bron: —.

Letterlijke metafieldkeys: —.

DOM-hooks: —.

Geen vermelding sluit dynamische keys, externe handlers of platformwerking niet uit. Inhoud/defaults en huidige product-/contact-/settingswaarden worden niet door deze tool gepubliceerd.
