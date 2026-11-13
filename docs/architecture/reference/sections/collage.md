# collage

**Bron:** `sections/collage.liquid`. Bronstatus: BYTE_MATCH.

[Functioneel dossier](../../components/FOUNDATIONS_AND_TOOLING.md) · [Bronhashes](../source-index.json) · [Alle secties](../SECTIONS.md)

Dit is de bronreferentie. Het dossier geeft de bedoeling, data-eigenaar, toestanden en onderhoudsgrenzen.

## Koppelingen

Letterlijke callers: —.

Letterlijke uitgaande refs: `assets/collage.css`, `assets/component-card.css`, `assets/component-deferred-media.css`, `assets/component-modal-video.css`, `assets/icon-close.svg`, `assets/icon-play.svg`, `snippets/card-collection.liquid`, `snippets/card-product.liquid`.

Geen caller gevonden betekent niet ongebruikt: Theme Editor, platformsections en dynamische aanroepen vallen buiten deze parser.

## Schema-instellingen

| ID | Type | Label / opties |
| --- | --- | --- |
| `heading` | `inline_richtext` | t:sections.collage.settings.heading.label |
| `heading_size` | `select` | t:sections.all.heading_size.label: h2: t:sections.all.heading_size.options__1.label; h1: t:sections.all.heading_size.options__2.label; h0: t:sections.all.heading_size.options__3.label; hxl: t:sections.all.heading_size.options__4.label; hxxl: t:sections.all.heading_size.options__5.label |
| `desktop_layout` | `select` | t:sections.collage.settings.desktop_layout.label: left: t:sections.collage.settings.desktop_layout.options__1.label; right: t:sections.collage.settings.desktop_layout.options__2.label |
| `mobile_layout` | `select` | t:sections.collage.settings.mobile_layout.label: collage: t:sections.collage.settings.mobile_layout.options__1.label; column: t:sections.collage.settings.mobile_layout.options__2.label |
| `card_styles` | `select` | t:sections.collage.settings.card_styles.label: none: t:sections.collage.settings.card_styles.options__1.label; product-card-wrapper: t:sections.collage.settings.card_styles.options__2.label |
| `color_scheme` | `color_scheme` | t:sections.all.colors.label |
| `padding_top` | `range` | t:sections.all.padding.padding_top |
| `padding_bottom` | `range` | t:sections.all.padding.padding_bottom |

## Blocktype image

| ID | Type | Label / opties |
| --- | --- | --- |
| `image` | `image_picker` | t:sections.collage.blocks.image.settings.image.label |

## Blocktype product

| ID | Type | Label / opties |
| --- | --- | --- |
| `product` | `product` | t:sections.collage.blocks.product.settings.product.label |
| `second_image` | `checkbox` | t:sections.collage.blocks.product.settings.second_image.label |

## Blocktype collection

| ID | Type | Label / opties |
| --- | --- | --- |
| `collection` | `collection` | t:sections.collage.blocks.collection.settings.collection.label |

## Blocktype video

| ID | Type | Label / opties |
| --- | --- | --- |
| `cover_image` | `image_picker` | t:sections.collage.blocks.video.settings.cover_image.label |
| `video_url` | `video_url` | t:sections.collage.blocks.video.settings.video_url.label |
| `description` | `text` | t:sections.collage.blocks.video.settings.description.label |

## Technische ingangen

Formtypen: —.

Letterlijke events in deze bron: —.

Letterlijke metafieldkeys: —.

DOM-hooks: `data-media-id`, `data-modal`.

Geen vermelding sluit dynamische keys, externe handlers of platformwerking niet uit. Inhoud/defaults en huidige product-/contact-/settingswaarden worden niet door deze tool gepubliceerd.
