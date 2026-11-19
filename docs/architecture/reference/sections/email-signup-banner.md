# email-signup-banner

**Bron:** `sections/email-signup-banner.liquid`. Bronstatus: BYTE_MATCH.

[Functioneel dossier](../../components/FOUNDATIONS_AND_TOOLING.md) · [Bronhashes](../source-index.json) · [Alle secties](../SECTIONS.md)

Dit is de bronreferentie. Het dossier geeft de bedoeling, data-eigenaar, toestanden en onderhoudsgrenzen.

## Koppelingen

Letterlijke callers: `templates/password.json`.

Letterlijke uitgaande refs: `assets/component-newsletter.css`, `assets/email-signup-banner-background-mobile.svg`, `assets/email-signup-banner-background.svg`, `assets/icon-arrow.svg`, `assets/icon-error.svg`, `assets/icon-success.svg`, `assets/newsletter-section.css`, `assets/section-email-signup-banner.css`, `assets/section-image-banner.css`.

Geen caller gevonden betekent niet ongebruikt: Theme Editor, platformsections en dynamische aanroepen vallen buiten deze parser.

## Schema-instellingen

| ID | Type | Label / opties |
| --- | --- | --- |
| `show_background_image` | `checkbox` | t:sections.email-signup-banner.settings.show_background_image.label |
| `image` | `image_picker` | t:sections.email-signup-banner.settings.image.label |
| `image_overlay_opacity` | `range` | t:sections.email-signup-banner.settings.image_overlay_opacity.label |
| `image_height` | `select` | t:sections.email-signup-banner.settings.image_height.label: adapt-image: t:sections.email-signup-banner.settings.image_height.options__1.label; small: t:sections.email-signup-banner.settings.image_height.options__2.label; medium: t:sections.email-signup-banner.settings.image_height.options__3.label; large: t:sections.email-signup-banner.settings.image_height.options__4.label |
| `desktop_content_position` | `select` | t:sections.email-signup-banner.settings.desktop_content_position.label: top-left: t:sections.email-signup-banner.settings.desktop_content_position.options__1.label; top-center: t:sections.email-signup-banner.settings.desktop_content_position.options__2.label; top-right: t:sections.email-signup-banner.settings.desktop_content_position.options__3.label; middle-left: t:sections.email-signup-banner.settings.desktop_content_position.options__4.label; middle-center: t:sections.email-signup-banner.settings.desktop_content_position.options__5.label; middle-right: t:sections.email-signup-banner.settings.desktop_content_position.options__6.label; bottom-left: t:sections.email-signup-banner.settings.desktop_content_position.options__7.label; bottom-center: t:sections.email-signup-banner.settings.desktop_content_position.options__8.label; bottom-right: t:sections.email-signup-banner.settings.desktop_content_position.options__9.label |
| `desktop_content_alignment` | `select` | t:sections.email-signup-banner.settings.desktop_content_alignment.label: left: t:sections.email-signup-banner.settings.desktop_content_alignment.options__1.label; center: t:sections.email-signup-banner.settings.desktop_content_alignment.options__2.label; right: t:sections.email-signup-banner.settings.desktop_content_alignment.options__3.label |
| `show_text_box` | `checkbox` | t:sections.email-signup-banner.settings.show_text_box.label |
| `color_scheme` | `color_scheme` | t:sections.all.colors.label |
| `mobile_content_alignment` | `select` | t:sections.email-signup-banner.settings.mobile_content_alignment.label: left: t:sections.email-signup-banner.settings.mobile_content_alignment.options__1.label; center: t:sections.email-signup-banner.settings.mobile_content_alignment.options__2.label; right: t:sections.email-signup-banner.settings.mobile_content_alignment.options__3.label |
| `show_text_below` | `checkbox` | t:sections.email-signup-banner.settings.show_text_below.label |

## Blocktype heading

| ID | Type | Label / opties |
| --- | --- | --- |
| `heading` | `text` | t:sections.email-signup-banner.blocks.heading.settings.heading.label |
| `heading_size` | `select` | t:sections.all.heading_size.label: h2: t:sections.all.heading_size.options__1.label; h1: t:sections.all.heading_size.options__2.label; h0: t:sections.all.heading_size.options__3.label; hxl: t:sections.all.heading_size.options__4.label; hxxl: t:sections.all.heading_size.options__5.label |

## Blocktype paragraph

| ID | Type | Label / opties |
| --- | --- | --- |
| `text` | `richtext` | t:sections.email-signup-banner.blocks.paragraph.settings.paragraph.label |
| `text_style` | `select` | t:sections.email-signup-banner.blocks.paragraph.settings.text_style.label: body: t:sections.email-signup-banner.blocks.paragraph.settings.text_style.options__1.label; subtitle: t:sections.email-signup-banner.blocks.paragraph.settings.text_style.options__2.label |

## Blocktype email_form

| ID | Type | Label / opties |
| --- | --- | --- |

## Technische ingangen

Formtypen: `customer`.

Letterlijke events in deze bron: —.

Letterlijke metafieldkeys: —.

DOM-hooks: —.

Geen vermelding sluit dynamische keys, externe handlers of platformwerking niet uit. Inhoud/defaults en huidige product-/contact-/settingswaarden worden niet door deze tool gepubliceerd.
