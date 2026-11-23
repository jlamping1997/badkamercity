# image-banner

**Bron:** `sections/image-banner.liquid`. Bronstatus: BYTE_MATCH.

[Functioneel dossier](../../components/FOUNDATIONS_AND_TOOLING.md) · [Bronhashes](../source-index.json) · [Alle secties](../SECTIONS.md)

Dit is de bronreferentie. Het dossier geeft de bedoeling, data-eigenaar, toestanden en onderhoudsgrenzen.

## Koppelingen

Letterlijke callers: —.

Letterlijke uitgaande refs: `assets/section-image-banner.css`.

Geen caller gevonden betekent niet ongebruikt: Theme Editor, platformsections en dynamische aanroepen vallen buiten deze parser.

## Schema-instellingen

| ID | Type | Label / opties |
| --- | --- | --- |
| `image` | `image_picker` | t:sections.image-banner.settings.image.label |
| `image_2` | `image_picker` | t:sections.image-banner.settings.image_2.label |
| `image_overlay_opacity` | `range` | t:sections.image-banner.settings.image_overlay_opacity.label |
| `image_height` | `select` | t:sections.image-banner.settings.image_height.label: adapt: t:sections.image-banner.settings.image_height.options__1.label; small: t:sections.image-banner.settings.image_height.options__2.label; medium: t:sections.image-banner.settings.image_height.options__3.label; large: t:sections.image-banner.settings.image_height.options__4.label |
| `image_behavior` | `select` | t:sections.all.animation.image_behavior.label: none: t:sections.all.animation.image_behavior.options__1.label; ambient: t:sections.all.animation.image_behavior.options__2.label; fixed: t:sections.all.animation.image_behavior.options__3.label; zoom-in: t:sections.all.animation.image_behavior.options__4.label |
| `desktop_content_position` | `select` | t:sections.image-banner.settings.desktop_content_position.label: top-left: t:sections.image-banner.settings.desktop_content_position.options__1.label; top-center: t:sections.image-banner.settings.desktop_content_position.options__2.label; top-right: t:sections.image-banner.settings.desktop_content_position.options__3.label; middle-left: t:sections.image-banner.settings.desktop_content_position.options__4.label; middle-center: t:sections.image-banner.settings.desktop_content_position.options__5.label; middle-right: t:sections.image-banner.settings.desktop_content_position.options__6.label; bottom-left: t:sections.image-banner.settings.desktop_content_position.options__7.label; bottom-center: t:sections.image-banner.settings.desktop_content_position.options__8.label; bottom-right: t:sections.image-banner.settings.desktop_content_position.options__9.label |
| `desktop_content_alignment` | `select` | t:sections.image-banner.settings.desktop_content_alignment.label: left: t:sections.image-banner.settings.desktop_content_alignment.options__1.label; center: t:sections.image-banner.settings.desktop_content_alignment.options__2.label; right: t:sections.image-banner.settings.desktop_content_alignment.options__3.label |
| `show_text_box` | `checkbox` | t:sections.image-banner.settings.show_text_box.label |
| `color_scheme` | `color_scheme` | t:sections.all.colors.label |
| `stack_images_on_mobile` | `checkbox` | t:sections.image-banner.settings.stack_images_on_mobile.label |
| `mobile_content_alignment` | `select` | t:sections.image-banner.settings.mobile_content_alignment.label: left: t:sections.image-banner.settings.mobile_content_alignment.options__1.label; center: t:sections.image-banner.settings.mobile_content_alignment.options__2.label; right: t:sections.image-banner.settings.mobile_content_alignment.options__3.label |
| `show_text_below` | `checkbox` | t:sections.image-banner.settings.show_text_below.label |

## Blocktype heading

| ID | Type | Label / opties |
| --- | --- | --- |
| `heading` | `inline_richtext` | t:sections.image-banner.blocks.heading.settings.heading.label |
| `heading_size` | `select` | t:sections.all.heading_size.label: h2: t:sections.all.heading_size.options__1.label; h1: t:sections.all.heading_size.options__2.label; h0: t:sections.all.heading_size.options__3.label; hxl: t:sections.all.heading_size.options__4.label; hxxl: t:sections.all.heading_size.options__5.label |

## Blocktype text

| ID | Type | Label / opties |
| --- | --- | --- |
| `text` | `inline_richtext` | t:sections.image-banner.blocks.text.settings.text.label |
| `text_style` | `select` | t:sections.image-banner.blocks.text.settings.text_style.label: body: t:sections.image-banner.blocks.text.settings.text_style.options__1.label; subtitle: t:sections.image-banner.blocks.text.settings.text_style.options__2.label; caption-with-letter-spacing: t:sections.image-banner.blocks.text.settings.text_style.options__3.label |

## Blocktype buttons

| ID | Type | Label / opties |
| --- | --- | --- |
| `button_label_1` | `text` | t:sections.image-banner.blocks.buttons.settings.button_label_1.label |
| `button_link_1` | `url` | t:sections.image-banner.blocks.buttons.settings.button_link_1.label |
| `button_style_secondary_1` | `checkbox` | t:sections.image-banner.blocks.buttons.settings.button_style_secondary_1.label |
| `button_label_2` | `text` | t:sections.image-banner.blocks.buttons.settings.button_label_2.label |
| `button_link_2` | `url` | t:sections.image-banner.blocks.buttons.settings.button_link_2.label |
| `button_style_secondary_2` | `checkbox` | t:sections.image-banner.blocks.buttons.settings.button_style_secondary_2.label |

## Technische ingangen

Formtypen: —.

Letterlijke events in deze bron: —.

Letterlijke metafieldkeys: —.

DOM-hooks: —.

Geen vermelding sluit dynamische keys, externe handlers of platformwerking niet uit. Inhoud/defaults en huidige product-/contact-/settingswaarden worden niet door deze tool gepubliceerd.
