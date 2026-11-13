# rich-text

**Bron:** `sections/rich-text.liquid`. Bronstatus: BYTE_MATCH.

[Functioneel dossier](../../components/FOUNDATIONS_AND_TOOLING.md) · [Bronhashes](../source-index.json) · [Alle secties](../SECTIONS.md)

Dit is de bronreferentie. Het dossier geeft de bedoeling, data-eigenaar, toestanden en onderhoudsgrenzen.

## Koppelingen

Letterlijke callers: `templates/page.bc-sunshower.json`.

Letterlijke uitgaande refs: `assets/section-rich-text.css`.

Geen caller gevonden betekent niet ongebruikt: Theme Editor, platformsections en dynamische aanroepen vallen buiten deze parser.

## Schema-instellingen

| ID | Type | Label / opties |
| --- | --- | --- |
| `desktop_content_position` | `select` | t:sections.rich-text.settings.desktop_content_position.label: left: t:sections.rich-text.settings.desktop_content_position.options__1.label; center: t:sections.rich-text.settings.desktop_content_position.options__2.label; right: t:sections.rich-text.settings.desktop_content_position.options__3.label |
| `content_alignment` | `select` | t:sections.rich-text.settings.content_alignment.label: left: t:sections.rich-text.settings.content_alignment.options__1.label; center: t:sections.rich-text.settings.content_alignment.options__2.label; right: t:sections.rich-text.settings.content_alignment.options__3.label |
| `color_scheme` | `color_scheme` | t:sections.all.colors.label |
| `full_width` | `checkbox` | t:sections.rich-text.settings.full_width.label |
| `padding_top` | `range` | t:sections.all.padding.padding_top |
| `padding_bottom` | `range` | t:sections.all.padding.padding_bottom |

## Blocktype heading

| ID | Type | Label / opties |
| --- | --- | --- |
| `heading` | `inline_richtext` | t:sections.rich-text.blocks.heading.settings.heading.label |
| `heading_size` | `select` | t:sections.all.heading_size.label: h2: t:sections.all.heading_size.options__1.label; h1: t:sections.all.heading_size.options__2.label; h0: t:sections.all.heading_size.options__3.label; hxl: t:sections.all.heading_size.options__4.label; hxxl: t:sections.all.heading_size.options__5.label |

## Blocktype caption

| ID | Type | Label / opties |
| --- | --- | --- |
| `caption` | `text` | t:sections.rich-text.blocks.caption.settings.text.label |
| `text_style` | `select` | t:sections.rich-text.blocks.caption.settings.text_style.label: subtitle: t:sections.rich-text.blocks.caption.settings.text_style.options__1.label; caption-with-letter-spacing: t:sections.rich-text.blocks.caption.settings.text_style.options__2.label |
| `text_size` | `select` | t:sections.rich-text.blocks.caption.settings.caption_size.label: small: t:sections.rich-text.blocks.caption.settings.caption_size.options__1.label; medium: t:sections.rich-text.blocks.caption.settings.caption_size.options__2.label; large: t:sections.rich-text.blocks.caption.settings.caption_size.options__3.label |

## Blocktype text

| ID | Type | Label / opties |
| --- | --- | --- |
| `text` | `richtext` | t:sections.rich-text.blocks.text.settings.text.label |

## Blocktype button

| ID | Type | Label / opties |
| --- | --- | --- |
| `button_label` | `text` | t:sections.rich-text.blocks.buttons.settings.button_label_1.label |
| `button_link` | `url` | t:sections.rich-text.blocks.buttons.settings.button_link_1.label |
| `button_style_secondary` | `checkbox` | t:sections.rich-text.blocks.buttons.settings.button_style_secondary_1.label |
| `button_label_2` | `text` | t:sections.rich-text.blocks.buttons.settings.button_label_2.label |
| `button_link_2` | `url` | t:sections.rich-text.blocks.buttons.settings.button_link_2.label |
| `button_style_secondary_2` | `checkbox` | t:sections.rich-text.blocks.buttons.settings.button_style_secondary_2.label |

## Technische ingangen

Formtypen: —.

Letterlijke events in deze bron: —.

Letterlijke metafieldkeys: —.

DOM-hooks: —.

Geen vermelding sluit dynamische keys, externe handlers of platformwerking niet uit. Inhoud/defaults en huidige product-/contact-/settingswaarden worden niet door deze tool gepubliceerd.
