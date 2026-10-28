# image-with-text

**Bron:** `sections/image-with-text.liquid`. Bronstatus: BYTE_MATCH.

[Functioneel dossier](../../components/FOUNDATIONS_AND_TOOLING.md) · [Bronhashes](../source-index.json) · [Alle secties](../SECTIONS.md)

Dit is de bronreferentie. Het dossier geeft de bedoeling, data-eigenaar, toestanden en onderhoudsgrenzen.

## Koppelingen

Letterlijke callers: —.

Letterlijke uitgaande refs: `assets/component-image-with-text.css`.

Geen caller gevonden betekent niet ongebruikt: Theme Editor, platformsections en dynamische aanroepen vallen buiten deze parser.

## Schema-instellingen

| ID | Type | Label / opties |
| --- | --- | --- |
| `image` | `image_picker` | t:sections.image-with-text.settings.image.label |
| `height` | `select` | t:sections.image-with-text.settings.height.label: adapt: t:sections.image-with-text.settings.height.options__1.label; small: t:sections.image-with-text.settings.height.options__2.label; medium: t:sections.image-with-text.settings.height.options__3.label; large: t:sections.image-with-text.settings.height.options__4.label |
| `desktop_image_width` | `select` | t:sections.image-with-text.settings.desktop_image_width.label: small: t:sections.image-with-text.settings.desktop_image_width.options__1.label; medium: t:sections.image-with-text.settings.desktop_image_width.options__2.label; large: t:sections.image-with-text.settings.desktop_image_width.options__3.label |
| `layout` | `select` | t:sections.image-with-text.settings.layout.label: image_first: t:sections.image-with-text.settings.layout.options__1.label; text_first: t:sections.image-with-text.settings.layout.options__2.label |
| `image_behavior` | `select` | t:sections.all.animation.image_behavior.label: none: t:sections.all.animation.image_behavior.options__1.label; ambient: t:sections.all.animation.image_behavior.options__2.label; zoom-in: t:sections.all.animation.image_behavior.options__4.label |
| `content_layout` | `select` | t:sections.image-with-text.settings.content_layout.label: no-overlap: t:sections.image-with-text.settings.content_layout.options__1.label; overlap: t:sections.image-with-text.settings.content_layout.options__2.label |
| `desktop_content_position` | `select` | t:sections.image-with-text.settings.desktop_content_position.label: top: t:sections.image-with-text.settings.desktop_content_position.options__1.label; middle: t:sections.image-with-text.settings.desktop_content_position.options__2.label; bottom: t:sections.image-with-text.settings.desktop_content_position.options__3.label |
| `desktop_content_alignment` | `select` | t:sections.image-with-text.settings.desktop_content_alignment.label: left: t:sections.image-with-text.settings.desktop_content_alignment.options__1.label; center: t:sections.image-with-text.settings.desktop_content_alignment.options__2.label; right: t:sections.image-with-text.settings.desktop_content_alignment.options__3.label |
| `mobile_content_alignment` | `select` | t:sections.image-with-text.settings.mobile_content_alignment.label: left: t:sections.image-with-text.settings.mobile_content_alignment.options__1.label; center: t:sections.image-with-text.settings.mobile_content_alignment.options__2.label; right: t:sections.image-with-text.settings.mobile_content_alignment.options__3.label |
| `section_color_scheme` | `color_scheme` | t:sections.all.colors.label |
| `color_scheme` | `color_scheme` | t:sections.multirow.settings.container_color_scheme.label |
| `padding_top` | `range` | t:sections.all.padding.padding_top |
| `padding_bottom` | `range` | t:sections.all.padding.padding_bottom |

## Blocktype heading

| ID | Type | Label / opties |
| --- | --- | --- |
| `heading` | `inline_richtext` | t:sections.image-with-text.blocks.heading.settings.heading.label |
| `heading_size` | `select` | t:sections.all.heading_size.label: h2: t:sections.all.heading_size.options__1.label; h1: t:sections.all.heading_size.options__2.label; h0: t:sections.all.heading_size.options__3.label; hxl: t:sections.all.heading_size.options__4.label; hxxl: t:sections.all.heading_size.options__5.label |

## Blocktype caption

| ID | Type | Label / opties |
| --- | --- | --- |
| `caption` | `text` | t:sections.image-with-text.blocks.caption.settings.text.label |
| `text_style` | `select` | t:sections.image-with-text.blocks.caption.settings.text_style.label: subtitle: t:sections.image-with-text.blocks.caption.settings.text_style.options__1.label; caption-with-letter-spacing: t:sections.image-with-text.blocks.caption.settings.text_style.options__2.label |
| `text_size` | `select` | t:sections.image-with-text.blocks.caption.settings.caption_size.label: small: t:sections.image-with-text.blocks.caption.settings.caption_size.options__1.label; medium: t:sections.image-with-text.blocks.caption.settings.caption_size.options__2.label; large: t:sections.image-with-text.blocks.caption.settings.caption_size.options__3.label |

## Blocktype text

| ID | Type | Label / opties |
| --- | --- | --- |
| `text` | `richtext` | t:sections.image-with-text.blocks.text.settings.text.label |
| `text_style` | `select` | t:sections.image-with-text.blocks.text.settings.text_style.label: body: t:sections.image-with-text.blocks.text.settings.text_style.options__1.label; subtitle: t:sections.image-with-text.blocks.text.settings.text_style.options__2.label |

## Blocktype button

| ID | Type | Label / opties |
| --- | --- | --- |
| `button_label` | `text` | t:sections.image-with-text.blocks.button.settings.button_label.label |
| `button_link` | `url` | t:sections.image-with-text.blocks.button.settings.button_link.label |
| `button_style_secondary` | `checkbox` | t:sections.image-with-text.blocks.button.settings.outline_button.label |

## Technische ingangen

Formtypen: —.

Letterlijke events in deze bron: —.

Letterlijke metafieldkeys: —.

DOM-hooks: —.

Geen vermelding sluit dynamische keys, externe handlers of platformwerking niet uit. Inhoud/defaults en huidige product-/contact-/settingswaarden worden niet door deze tool gepubliceerd.
