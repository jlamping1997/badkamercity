# collapsible-content

**Bron:** `sections/collapsible-content.liquid`. Bronstatus: BYTE_MATCH.

[Functioneel dossier](../../components/FOUNDATIONS_AND_TOOLING.md) · [Bronhashes](../source-index.json) · [Alle secties](../SECTIONS.md)

Dit is de bronreferentie. Het dossier geeft de bedoeling, data-eigenaar, toestanden en onderhoudsgrenzen.

## Koppelingen

Letterlijke callers: —.

Letterlijke uitgaande refs: `assets/collapsible-content.css`, `assets/component-accordion.css`, `assets/icon-caret.svg`, `snippets/icon-accordion.liquid`.

Geen caller gevonden betekent niet ongebruikt: Theme Editor, platformsections en dynamische aanroepen vallen buiten deze parser.

## Schema-instellingen

| ID | Type | Label / opties |
| --- | --- | --- |
| `caption` | `text` | t:sections.collapsible_content.settings.caption.label |
| `heading` | `inline_richtext` | t:sections.collapsible_content.settings.heading.label |
| `heading_size` | `select` | t:sections.all.heading_size.label: h2: t:sections.all.heading_size.options__1.label; h1: t:sections.all.heading_size.options__2.label; h0: t:sections.all.heading_size.options__3.label; hxl: t:sections.all.heading_size.options__4.label; hxxl: t:sections.all.heading_size.options__5.label |
| `heading_alignment` | `select` | t:sections.collapsible_content.settings.heading_alignment.label: left: t:sections.collapsible_content.settings.heading_alignment.options__1.label; center: t:sections.collapsible_content.settings.heading_alignment.options__2.label; right: t:sections.collapsible_content.settings.heading_alignment.options__3.label |
| `layout` | `select` | t:sections.collapsible_content.settings.layout.label: none: t:sections.collapsible_content.settings.layout.options__1.label; row: t:sections.collapsible_content.settings.layout.options__2.label; section: t:sections.collapsible_content.settings.layout.options__3.label |
| `container_color_scheme` | `color_scheme` | t:sections.collapsible_content.settings.container_color_scheme.label |
| `color_scheme` | `color_scheme` | t:sections.collapsible_content.settings.section_color_scheme.label |
| `open_first_collapsible_row` | `checkbox` | t:sections.collapsible_content.settings.open_first_collapsible_row.label |
| `image` | `image_picker` | t:sections.collapsible_content.settings.image.label |
| `image_ratio` | `select` | t:sections.collapsible_content.settings.image_ratio.label: adapt: t:sections.collapsible_content.settings.image_ratio.options__1.label; small: t:sections.collapsible_content.settings.image_ratio.options__2.label; large: t:sections.collapsible_content.settings.image_ratio.options__3.label |
| `desktop_layout` | `select` | t:sections.collapsible_content.settings.desktop_layout.label: image_first: t:sections.collapsible_content.settings.desktop_layout.options__1.label; image_second: t:sections.collapsible_content.settings.desktop_layout.options__2.label |
| `padding_top` | `range` | t:sections.all.padding.padding_top |
| `padding_bottom` | `range` | t:sections.all.padding.padding_bottom |

## Blocktype collapsible_row

| ID | Type | Label / opties |
| --- | --- | --- |
| `heading` | `text` | t:sections.collapsible_content.blocks.collapsible_row.settings.heading.label |
| `icon` | `select` | t:sections.collapsible_content.blocks.collapsible_row.settings.icon.label: none: t:sections.collapsible_content.blocks.collapsible_row.settings.icon.options__1.label; apple: t:sections.collapsible_content.blocks.collapsible_row.settings.icon.options__2.label; banana: t:sections.collapsible_content.blocks.collapsible_row.settings.icon.options__3.label; bottle: t:sections.collapsible_content.blocks.collapsible_row.settings.icon.options__4.label; box: t:sections.collapsible_content.blocks.collapsible_row.settings.icon.options__5.label; carrot: t:sections.collapsible_content.blocks.collapsible_row.settings.icon.options__6.label; chat_bubble: t:sections.collapsible_content.blocks.collapsible_row.settings.icon.options__7.label; check_mark: t:sections.collapsible_content.blocks.collapsible_row.settings.icon.options__8.label; clipboard: t:sections.collapsible_content.blocks.collapsible_row.settings.icon.options__9.label; dairy: t:sections.collapsible_content.blocks.collapsible_row.settings.icon.options__10.label; dairy_free: t:sections.collapsible_content.blocks.collapsible_row.settings.icon.options__11.label; dryer: t:sections.collapsible_content.blocks.collapsible_row.settings.icon.options__12.label; eye: t:sections.collapsible_content.blocks.collapsible_row.settings.icon.options__13.label; fire: t:sections.collapsible_content.blocks.collapsible_row.settings.icon.options__14.label; gluten_free: t:sections.collapsible_content.blocks.collapsible_row.settings.icon.options__15.label; heart: t:sections.collapsible_content.blocks.collapsible_row.settings.icon.options__16.label; iron: t:sections.collapsible_content.blocks.collapsible_row.settings.icon.options__17.label; leaf: t:sections.collapsible_content.blocks.collapsible_row.settings.icon.options__18.label; leather: t:sections.collapsible_content.blocks.collapsible_row.settings.icon.options__19.label; lightning_bolt: t:sections.collapsible_content.blocks.collapsible_row.settings.icon.options__20.label; lipstick: t:sections.collapsible_content.blocks.collapsible_row.settings.icon.options__21.label; lock: t:sections.collapsible_content.blocks.collapsible_row.settings.icon.options__22.label; map_pin: t:sections.collapsible_content.blocks.collapsible_row.settings.icon.options__23.label; nut_free: t:sections.collapsible_content.blocks.collapsible_row.settings.icon.options__24.label; pants: t:sections.collapsible_content.blocks.collapsible_row.settings.icon.options__25.label; paw_print: t:sections.collapsible_content.blocks.collapsible_row.settings.icon.options__26.label; pepper: t:sections.collapsible_content.blocks.collapsible_row.settings.icon.options__27.label; perfume: t:sections.collapsible_content.blocks.collapsible_row.settings.icon.options__28.label; plane: t:sections.collapsible_content.blocks.collapsible_row.settings.icon.options__29.label; plant: t:sections.collapsible_content.blocks.collapsible_row.settings.icon.options__30.label; price_tag: t:sections.collapsible_content.blocks.collapsible_row.settings.icon.options__31.label; question_mark: t:sections.collapsible_content.blocks.collapsible_row.settings.icon.options__32.label; recycle: t:sections.collapsible_content.blocks.collapsible_row.settings.icon.options__33.label; return: t:sections.collapsible_content.blocks.collapsible_row.settings.icon.options__34.label; ruler: t:sections.collapsible_content.blocks.collapsible_row.settings.icon.options__35.label; serving_dish: t:sections.collapsible_content.blocks.collapsible_row.settings.icon.options__36.label; shirt: t:sections.collapsible_content.blocks.collapsible_row.settings.icon.options__37.label; shoe: t:sections.collapsible_content.blocks.collapsible_row.settings.icon.options__38.label; silhouette: t:sections.collapsible_content.blocks.collapsible_row.settings.icon.options__39.label; snowflake: t:sections.collapsible_content.blocks.collapsible_row.settings.icon.options__40.label; star: t:sections.collapsible_content.blocks.collapsible_row.settings.icon.options__41.label; stopwatch: t:sections.collapsible_content.blocks.collapsible_row.settings.icon.options__42.label; truck: t:sections.collapsible_content.blocks.collapsible_row.settings.icon.options__43.label; washing: t:sections.collapsible_content.blocks.collapsible_row.settings.icon.options__44.label |
| `row_content` | `richtext` | t:sections.collapsible_content.blocks.collapsible_row.settings.row_content.label |
| `page` | `page` | t:sections.collapsible_content.blocks.collapsible_row.settings.page.label |

## Technische ingangen

Formtypen: —.

Letterlijke events in deze bron: —.

Letterlijke metafieldkeys: —.

DOM-hooks: —.

Geen vermelding sluit dynamische keys, externe handlers of platformwerking niet uit. Inhoud/defaults en huidige product-/contact-/settingswaarden worden niet door deze tool gepubliceerd.
