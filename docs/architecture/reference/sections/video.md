# video

**Bron:** `sections/video.liquid`. Bronstatus: BYTE_MATCH.

[Functioneel dossier](../../components/PRODUCT_PAGES.md) · [Bronhashes](../source-index.json) · [Alle secties](../SECTIONS.md)

Dit is de bronreferentie. Het dossier geeft de bedoeling, data-eigenaar, toestanden en onderhoudsgrenzen.

## Koppelingen

Letterlijke callers: —.

Letterlijke uitgaande refs: `assets/component-deferred-media.css`, `assets/icon-play.svg`, `assets/video-section.css`.

Geen caller gevonden betekent niet ongebruikt: Theme Editor, platformsections en dynamische aanroepen vallen buiten deze parser.

## Schema-instellingen

| ID | Type | Label / opties |
| --- | --- | --- |
| `heading` | `inline_richtext` | t:sections.video.settings.heading.label |
| `heading_size` | `select` | t:sections.all.heading_size.label: h2: t:sections.all.heading_size.options__1.label; h1: t:sections.all.heading_size.options__2.label; h0: t:sections.all.heading_size.options__3.label; hxl: t:sections.all.heading_size.options__4.label; hxxl: t:sections.all.heading_size.options__5.label |
| `enable_video_looping` | `checkbox` | t:sections.video.settings.enable_video_looping.label |
| `video` | `video` | t:sections.video.settings.video.label |
| `video_url` | `video_url` | t:sections.video.settings.video_url.label |
| `cover_image` | `image_picker` | t:sections.video.settings.cover_image.label |
| `description` | `text` | t:sections.video.settings.description.label |
| `full_width` | `checkbox` | t:sections.video.settings.full_width.label |
| `color_scheme` | `color_scheme` | t:sections.all.colors.label |
| `padding_top` | `range` | t:sections.all.padding.padding_top |
| `padding_bottom` | `range` | t:sections.all.padding.padding_bottom |

## Technische ingangen

Formtypen: —.

Letterlijke events in deze bron: —.

Letterlijke metafieldkeys: —.

DOM-hooks: `data-media-id`.

Geen vermelding sluit dynamische keys, externe handlers of platformwerking niet uit. Inhoud/defaults en huidige product-/contact-/settingswaarden worden niet door deze tool gepubliceerd.
