# slideshow

**Bron:** `sections/slideshow.liquid`. Bronstatus: BYTE_MATCH.

[Functioneel dossier](../../components/MOTION_AND_STYLES.md) · [Bronhashes](../source-index.json) · [Alle secties](../SECTIONS.md)

Dit is de bronreferentie. Het dossier geeft de bedoeling, data-eigenaar, toestanden en onderhoudsgrenzen.

## Koppelingen

Letterlijke callers: —.

Letterlijke uitgaande refs: `assets/component-slider.css`, `assets/component-slideshow.css`, `assets/icon-caret.svg`, `assets/icon-pause.svg`, `assets/icon-play.svg`, `assets/section-image-banner.css`, `assets/theme-editor.js`.

Geen caller gevonden betekent niet ongebruikt: Theme Editor, platformsections en dynamische aanroepen vallen buiten deze parser.

## Schema-instellingen

| ID | Type | Label / opties |
| --- | --- | --- |
| `layout` | `select` | t:sections.slideshow.settings.layout.label: full_bleed: t:sections.slideshow.settings.layout.options__1.label; grid: t:sections.slideshow.settings.layout.options__2.label |
| `slide_height` | `select` | t:sections.slideshow.settings.slide_height.label: adapt_image: t:sections.slideshow.settings.slide_height.options__1.label; small: t:sections.slideshow.settings.slide_height.options__2.label; medium: t:sections.slideshow.settings.slide_height.options__3.label; large: t:sections.slideshow.settings.slide_height.options__4.label |
| `slider_visual` | `select` | t:sections.slideshow.settings.slider_visual.label: dots: t:sections.slideshow.settings.slider_visual.options__2.label; counter: t:sections.slideshow.settings.slider_visual.options__1.label; numbers: t:sections.slideshow.settings.slider_visual.options__3.label |
| `auto_rotate` | `checkbox` | t:sections.slideshow.settings.auto_rotate.label |
| `change_slides_speed` | `range` | t:sections.slideshow.settings.change_slides_speed.label |
| `image_behavior` | `select` | t:sections.all.animation.image_behavior.label: none: t:sections.all.animation.image_behavior.options__1.label; ambient: t:sections.all.animation.image_behavior.options__2.label |
| `show_text_below` | `checkbox` | t:sections.slideshow.settings.show_text_below.label |
| `accessibility_info` | `text` | t:sections.slideshow.settings.accessibility.label |

## Blocktype slide

| ID | Type | Label / opties |
| --- | --- | --- |
| `image` | `image_picker` | t:sections.slideshow.blocks.slide.settings.image.label |
| `image_overlay_opacity` | `range` | t:sections.slideshow.blocks.slide.settings.image_overlay_opacity.label |
| `heading` | `inline_richtext` | t:sections.slideshow.blocks.slide.settings.heading.label |
| `heading_size` | `select` | t:sections.all.heading_size.label: h2: t:sections.all.heading_size.options__1.label; h1: t:sections.all.heading_size.options__2.label; h0: t:sections.all.heading_size.options__3.label; hxl: t:sections.all.heading_size.options__4.label; hxxl: t:sections.all.heading_size.options__5.label |
| `subheading` | `inline_richtext` | t:sections.slideshow.blocks.slide.settings.subheading.label |
| `button_label` | `text` | t:sections.slideshow.blocks.slide.settings.button_label.label |
| `link` | `url` | t:sections.slideshow.blocks.slide.settings.link.label |
| `button_style_secondary` | `checkbox` | t:sections.slideshow.blocks.slide.settings.secondary_style.label |
| `show_text_box` | `checkbox` | t:sections.slideshow.blocks.slide.settings.show_text_box.label |
| `box_align` | `select` | t:sections.slideshow.blocks.slide.settings.box_align.label: top-left: t:sections.slideshow.blocks.slide.settings.box_align.options__1.label; top-center: t:sections.slideshow.blocks.slide.settings.box_align.options__2.label; top-right: t:sections.slideshow.blocks.slide.settings.box_align.options__3.label; middle-left: t:sections.slideshow.blocks.slide.settings.box_align.options__4.label; middle-center: t:sections.slideshow.blocks.slide.settings.box_align.options__5.label; middle-right: t:sections.slideshow.blocks.slide.settings.box_align.options__6.label; bottom-left: t:sections.slideshow.blocks.slide.settings.box_align.options__7.label; bottom-center: t:sections.slideshow.blocks.slide.settings.box_align.options__8.label; bottom-right: t:sections.slideshow.blocks.slide.settings.box_align.options__9.label |
| `text_alignment` | `select` | t:sections.slideshow.blocks.slide.settings.text_alignment.label: left: t:sections.slideshow.blocks.slide.settings.text_alignment.option_1.label; center: t:sections.slideshow.blocks.slide.settings.text_alignment.option_2.label; right: t:sections.slideshow.blocks.slide.settings.text_alignment.option_3.label |
| `text_alignment_mobile` | `select` | t:sections.slideshow.blocks.slide.settings.text_alignment_mobile.label: left: t:sections.slideshow.blocks.slide.settings.text_alignment_mobile.options__1.label; center: t:sections.slideshow.blocks.slide.settings.text_alignment_mobile.options__2.label; right: t:sections.slideshow.blocks.slide.settings.text_alignment_mobile.options__3.label |
| `color_scheme` | `color_scheme` | t:sections.all.colors.label |

## Technische ingangen

Formtypen: —.

Letterlijke events in deze bron: —.

Letterlijke metafieldkeys: —.

DOM-hooks: `data-autoplay`, `data-speed`.

Geen vermelding sluit dynamische keys, externe handlers of platformwerking niet uit. Inhoud/defaults en huidige product-/contact-/settingswaarden worden niet door deze tool gepubliceerd.
