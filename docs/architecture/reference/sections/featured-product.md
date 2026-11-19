# featured-product

**Bron:** `sections/featured-product.liquid`. Bronstatus: BYTE_MATCH.

[Functioneel dossier](../../components/PRODUCT_PAGES.md) · [Bronhashes](../source-index.json) · [Alle secties](../SECTIONS.md)

Dit is de bronreferentie. Het dossier geeft de bedoeling, data-eigenaar, toestanden en onderhoudsgrenzen.

## Koppelingen

Letterlijke callers: —.

Letterlijke uitgaande refs: `assets/component-accordion.css`, `assets/component-deferred-media.css`, `assets/component-model-viewer-ui.css`, `assets/component-product-model.css`, `assets/component-product-variant-picker.css`, `assets/component-rating.css`, `assets/component-swatch-input.css`, `assets/component-swatch.css`, `assets/component-volume-pricing.css`, `assets/icon-arrow.svg`, `assets/icon-minus.svg`, `assets/icon-plus.svg`, `assets/magnify.js`, `assets/media-gallery.js`, `assets/price-per-item.js`, `assets/product-form.js`, `assets/product-info.js`, `assets/product-modal.js`, `assets/product-model.js`, `assets/section-featured-product.css`, `assets/section-main-product.css`, `assets/show-more.js`, `assets/theme-editor.js`, `snippets/buy-buttons.liquid`, `snippets/icon-with-text.liquid`, `snippets/loading-spinner.liquid`, `snippets/price.liquid`, `snippets/product-media-gallery.liquid`, `snippets/product-media-modal.liquid`, `snippets/product-variant-picker.liquid`.

Geen caller gevonden betekent niet ongebruikt: Theme Editor, platformsections en dynamische aanroepen vallen buiten deze parser.

## Schema-instellingen

| ID | Type | Label / opties |
| --- | --- | --- |
| `product` | `product` | t:sections.featured-product.settings.product.label |
| `color_scheme` | `color_scheme` | t:sections.all.colors.label |
| `secondary_background` | `checkbox` | t:sections.featured-product.settings.secondary_background.label |
| `media_size` | `select` | t:sections.main-product.settings.media_size.label: small: t:sections.main-product.settings.media_size.options__1.label; medium: t:sections.main-product.settings.media_size.options__2.label; large: t:sections.main-product.settings.media_size.options__3.label |
| `constrain_to_viewport` | `checkbox` | t:sections.main-product.settings.constrain_to_viewport.label |
| `media_fit` | `select` | t:sections.main-product.settings.media_fit.label: contain: t:sections.main-product.settings.media_fit.options__1.label; cover: t:sections.main-product.settings.media_fit.options__2.label |
| `media_position` | `select` | t:sections.featured-product.settings.media_position.label: left: t:sections.featured-product.settings.media_position.options__1.label; right: t:sections.featured-product.settings.media_position.options__2.label |
| `image_zoom` | `select` | t:sections.main-product.settings.image_zoom.label: lightbox: t:sections.main-product.settings.image_zoom.options__1.label; hover: t:sections.main-product.settings.image_zoom.options__2.label; none: t:sections.main-product.settings.image_zoom.options__3.label |
| `hide_variants` | `checkbox` | t:sections.main-product.settings.hide_variants.label |
| `enable_video_looping` | `checkbox` | t:sections.featured-product.settings.enable_video_looping.label |
| `padding_top` | `range` | t:sections.all.padding.padding_top |
| `padding_bottom` | `range` | t:sections.all.padding.padding_bottom |

## Blocktype @app

| ID | Type | Label / opties |
| --- | --- | --- |

## Blocktype text

| ID | Type | Label / opties |
| --- | --- | --- |
| `text` | `inline_richtext` | t:sections.featured-product.blocks.text.settings.text.label |
| `text_style` | `select` | t:sections.featured-product.blocks.text.settings.text_style.label: body: t:sections.featured-product.blocks.text.settings.text_style.options__1.label; subtitle: t:sections.featured-product.blocks.text.settings.text_style.options__2.label; uppercase: t:sections.featured-product.blocks.text.settings.text_style.options__3.label |

## Blocktype title

| ID | Type | Label / opties |
| --- | --- | --- |
| `heading_size` | `select` | t:sections.all.heading_size.label: h2: t:sections.all.heading_size.options__1.label; h1: t:sections.all.heading_size.options__2.label; h0: t:sections.all.heading_size.options__3.label; hxl: t:sections.all.heading_size.options__4.label; hxxl: t:sections.all.heading_size.options__5.label |

## Blocktype price

| ID | Type | Label / opties |
| --- | --- | --- |

## Blocktype sku

| ID | Type | Label / opties |
| --- | --- | --- |
| `text_style` | `select` | t:sections.featured-product.blocks.sku.settings.text_style.label: body: t:sections.featured-product.blocks.sku.settings.text_style.options__1.label; subtitle: t:sections.featured-product.blocks.sku.settings.text_style.options__2.label; uppercase: t:sections.featured-product.blocks.sku.settings.text_style.options__3.label |

## Blocktype quantity_selector

| ID | Type | Label / opties |
| --- | --- | --- |

## Blocktype variant_picker

| ID | Type | Label / opties |
| --- | --- | --- |
| `picker_type` | `select` | t:sections.featured-product.blocks.variant_picker.settings.picker_type.label: dropdown: t:sections.featured-product.blocks.variant_picker.settings.picker_type.options__1.label; button: t:sections.featured-product.blocks.variant_picker.settings.picker_type.options__2.label |
| `swatch_shape` | `select` | t:sections.featured-product.blocks.variant_picker.settings.swatch_shape.label: circle: t:sections.featured-product.blocks.variant_picker.settings.swatch_shape.options__1.label; square: t:sections.featured-product.blocks.variant_picker.settings.swatch_shape.options__2.label; none: t:sections.main-product.blocks.variant_picker.settings.swatch_shape.options__3.label |

## Blocktype buy_buttons

| ID | Type | Label / opties |
| --- | --- | --- |
| `show_dynamic_checkout` | `checkbox` | t:sections.featured-product.blocks.buy_buttons.settings.show_dynamic_checkout.label |
| `show_gift_card_recipient` | `checkbox` | t:sections.main-product.blocks.buy_buttons.settings.show_gift_card_recipient.label |

## Blocktype share

| ID | Type | Label / opties |
| --- | --- | --- |
| `share_label` | `text` | t:sections.featured-product.blocks.share.settings.text.label |

## Blocktype custom_liquid

| ID | Type | Label / opties |
| --- | --- | --- |
| `custom_liquid` | `liquid` | t:sections.custom-liquid.settings.custom_liquid.label |

## Blocktype rating

| ID | Type | Label / opties |
| --- | --- | --- |

## Blocktype icon-with-text

| ID | Type | Label / opties |
| --- | --- | --- |
| `layout` | `select` | t:sections.main-product.blocks.icon_with_text.settings.layout.label: horizontal: t:sections.main-product.blocks.icon_with_text.settings.layout.options__1.label; vertical: t:sections.main-product.blocks.icon_with_text.settings.layout.options__2.label |
| `icon_1` | `select` | t:sections.main-product.blocks.icon_with_text.settings.icon_1.label: none: t:sections.main-product.blocks.collapsible_tab.settings.icon.options__1.label; apple: t:sections.main-product.blocks.collapsible_tab.settings.icon.options__2.label; banana: t:sections.main-product.blocks.collapsible_tab.settings.icon.options__3.label; bottle: t:sections.main-product.blocks.collapsible_tab.settings.icon.options__4.label; box: t:sections.main-product.blocks.collapsible_tab.settings.icon.options__5.label; carrot: t:sections.main-product.blocks.collapsible_tab.settings.icon.options__6.label; chat_bubble: t:sections.main-product.blocks.collapsible_tab.settings.icon.options__7.label; check_mark: t:sections.main-product.blocks.collapsible_tab.settings.icon.options__8.label; clipboard: t:sections.main-product.blocks.collapsible_tab.settings.icon.options__9.label; dairy: t:sections.main-product.blocks.collapsible_tab.settings.icon.options__10.label; dairy_free: t:sections.main-product.blocks.collapsible_tab.settings.icon.options__11.label; dryer: t:sections.main-product.blocks.collapsible_tab.settings.icon.options__12.label; eye: t:sections.main-product.blocks.collapsible_tab.settings.icon.options__13.label; fire: t:sections.main-product.blocks.collapsible_tab.settings.icon.options__14.label; gluten_free: t:sections.main-product.blocks.collapsible_tab.settings.icon.options__15.label; heart: t:sections.main-product.blocks.collapsible_tab.settings.icon.options__16.label; iron: t:sections.main-product.blocks.collapsible_tab.settings.icon.options__17.label; leaf: t:sections.main-product.blocks.collapsible_tab.settings.icon.options__18.label; leather: t:sections.main-product.blocks.collapsible_tab.settings.icon.options__19.label; lightning_bolt: t:sections.main-product.blocks.collapsible_tab.settings.icon.options__20.label; lipstick: t:sections.main-product.blocks.collapsible_tab.settings.icon.options__21.label; lock: t:sections.main-product.blocks.collapsible_tab.settings.icon.options__22.label; map_pin: t:sections.main-product.blocks.collapsible_tab.settings.icon.options__23.label; nut_free: t:sections.main-product.blocks.collapsible_tab.settings.icon.options__24.label; pants: t:sections.main-product.blocks.collapsible_tab.settings.icon.options__25.label; paw_print: t:sections.main-product.blocks.collapsible_tab.settings.icon.options__26.label; pepper: t:sections.main-product.blocks.collapsible_tab.settings.icon.options__27.label; perfume: t:sections.main-product.blocks.collapsible_tab.settings.icon.options__28.label; plane: t:sections.main-product.blocks.collapsible_tab.settings.icon.options__29.label; plant: t:sections.main-product.blocks.collapsible_tab.settings.icon.options__30.label; price_tag: t:sections.main-product.blocks.collapsible_tab.settings.icon.options__31.label; question_mark: t:sections.main-product.blocks.collapsible_tab.settings.icon.options__32.label; recycle: t:sections.main-product.blocks.collapsible_tab.settings.icon.options__33.label; return: t:sections.main-product.blocks.collapsible_tab.settings.icon.options__34.label; ruler: t:sections.main-product.blocks.collapsible_tab.settings.icon.options__35.label; serving_dish: t:sections.main-product.blocks.collapsible_tab.settings.icon.options__36.label; shirt: t:sections.main-product.blocks.collapsible_tab.settings.icon.options__37.label; shoe: t:sections.main-product.blocks.collapsible_tab.settings.icon.options__38.label; silhouette: t:sections.main-product.blocks.collapsible_tab.settings.icon.options__39.label; snowflake: t:sections.main-product.blocks.collapsible_tab.settings.icon.options__40.label; star: t:sections.main-product.blocks.collapsible_tab.settings.icon.options__41.label; stopwatch: t:sections.main-product.blocks.collapsible_tab.settings.icon.options__42.label; truck: t:sections.main-product.blocks.collapsible_tab.settings.icon.options__43.label; washing: t:sections.main-product.blocks.collapsible_tab.settings.icon.options__44.label |
| `image_1` | `image_picker` | t:sections.main-product.blocks.icon_with_text.settings.image_1.label |
| `heading_1` | `inline_richtext` | t:sections.main-product.blocks.icon_with_text.settings.heading_1.label |
| `icon_2` | `select` | t:sections.main-product.blocks.icon_with_text.settings.icon_2.label: none: t:sections.main-product.blocks.collapsible_tab.settings.icon.options__1.label; apple: t:sections.main-product.blocks.collapsible_tab.settings.icon.options__2.label; banana: t:sections.main-product.blocks.collapsible_tab.settings.icon.options__3.label; bottle: t:sections.main-product.blocks.collapsible_tab.settings.icon.options__4.label; box: t:sections.main-product.blocks.collapsible_tab.settings.icon.options__5.label; carrot: t:sections.main-product.blocks.collapsible_tab.settings.icon.options__6.label; chat_bubble: t:sections.main-product.blocks.collapsible_tab.settings.icon.options__7.label; check_mark: t:sections.main-product.blocks.collapsible_tab.settings.icon.options__8.label; clipboard: t:sections.main-product.blocks.collapsible_tab.settings.icon.options__9.label; dairy: t:sections.main-product.blocks.collapsible_tab.settings.icon.options__10.label; dairy_free: t:sections.main-product.blocks.collapsible_tab.settings.icon.options__11.label; dryer: t:sections.main-product.blocks.collapsible_tab.settings.icon.options__12.label; eye: t:sections.main-product.blocks.collapsible_tab.settings.icon.options__13.label; fire: t:sections.main-product.blocks.collapsible_tab.settings.icon.options__14.label; gluten_free: t:sections.main-product.blocks.collapsible_tab.settings.icon.options__15.label; heart: t:sections.main-product.blocks.collapsible_tab.settings.icon.options__16.label; iron: t:sections.main-product.blocks.collapsible_tab.settings.icon.options__17.label; leaf: t:sections.main-product.blocks.collapsible_tab.settings.icon.options__18.label; leather: t:sections.main-product.blocks.collapsible_tab.settings.icon.options__19.label; lightning_bolt: t:sections.main-product.blocks.collapsible_tab.settings.icon.options__20.label; lipstick: t:sections.main-product.blocks.collapsible_tab.settings.icon.options__21.label; lock: t:sections.main-product.blocks.collapsible_tab.settings.icon.options__22.label; map_pin: t:sections.main-product.blocks.collapsible_tab.settings.icon.options__23.label; nut_free: t:sections.main-product.blocks.collapsible_tab.settings.icon.options__24.label; pants: t:sections.main-product.blocks.collapsible_tab.settings.icon.options__25.label; paw_print: t:sections.main-product.blocks.collapsible_tab.settings.icon.options__26.label; pepper: t:sections.main-product.blocks.collapsible_tab.settings.icon.options__27.label; perfume: t:sections.main-product.blocks.collapsible_tab.settings.icon.options__28.label; plane: t:sections.main-product.blocks.collapsible_tab.settings.icon.options__29.label; plant: t:sections.main-product.blocks.collapsible_tab.settings.icon.options__30.label; price_tag: t:sections.main-product.blocks.collapsible_tab.settings.icon.options__31.label; question_mark: t:sections.main-product.blocks.collapsible_tab.settings.icon.options__32.label; recycle: t:sections.main-product.blocks.collapsible_tab.settings.icon.options__33.label; return: t:sections.main-product.blocks.collapsible_tab.settings.icon.options__34.label; ruler: t:sections.main-product.blocks.collapsible_tab.settings.icon.options__35.label; serving_dish: t:sections.main-product.blocks.collapsible_tab.settings.icon.options__36.label; shirt: t:sections.main-product.blocks.collapsible_tab.settings.icon.options__37.label; shoe: t:sections.main-product.blocks.collapsible_tab.settings.icon.options__38.label; silhouette: t:sections.main-product.blocks.collapsible_tab.settings.icon.options__39.label; snowflake: t:sections.main-product.blocks.collapsible_tab.settings.icon.options__40.label; star: t:sections.main-product.blocks.collapsible_tab.settings.icon.options__41.label; stopwatch: t:sections.main-product.blocks.collapsible_tab.settings.icon.options__42.label; truck: t:sections.main-product.blocks.collapsible_tab.settings.icon.options__43.label; washing: t:sections.main-product.blocks.collapsible_tab.settings.icon.options__44.label |
| `image_2` | `image_picker` | t:sections.main-product.blocks.icon_with_text.settings.image_2.label |
| `heading_2` | `inline_richtext` | t:sections.main-product.blocks.icon_with_text.settings.heading_2.label |
| `icon_3` | `select` | t:sections.main-product.blocks.icon_with_text.settings.icon_3.label: none: t:sections.main-product.blocks.collapsible_tab.settings.icon.options__1.label; apple: t:sections.main-product.blocks.collapsible_tab.settings.icon.options__2.label; banana: t:sections.main-product.blocks.collapsible_tab.settings.icon.options__3.label; bottle: t:sections.main-product.blocks.collapsible_tab.settings.icon.options__4.label; box: t:sections.main-product.blocks.collapsible_tab.settings.icon.options__5.label; carrot: t:sections.main-product.blocks.collapsible_tab.settings.icon.options__6.label; chat_bubble: t:sections.main-product.blocks.collapsible_tab.settings.icon.options__7.label; check_mark: t:sections.main-product.blocks.collapsible_tab.settings.icon.options__8.label; clipboard: t:sections.main-product.blocks.collapsible_tab.settings.icon.options__9.label; dairy: t:sections.main-product.blocks.collapsible_tab.settings.icon.options__10.label; dairy_free: t:sections.main-product.blocks.collapsible_tab.settings.icon.options__11.label; dryer: t:sections.main-product.blocks.collapsible_tab.settings.icon.options__12.label; eye: t:sections.main-product.blocks.collapsible_tab.settings.icon.options__13.label; fire: t:sections.main-product.blocks.collapsible_tab.settings.icon.options__14.label; gluten_free: t:sections.main-product.blocks.collapsible_tab.settings.icon.options__15.label; heart: t:sections.main-product.blocks.collapsible_tab.settings.icon.options__16.label; iron: t:sections.main-product.blocks.collapsible_tab.settings.icon.options__17.label; leaf: t:sections.main-product.blocks.collapsible_tab.settings.icon.options__18.label; leather: t:sections.main-product.blocks.collapsible_tab.settings.icon.options__19.label; lightning_bolt: t:sections.main-product.blocks.collapsible_tab.settings.icon.options__20.label; lipstick: t:sections.main-product.blocks.collapsible_tab.settings.icon.options__21.label; lock: t:sections.main-product.blocks.collapsible_tab.settings.icon.options__22.label; map_pin: t:sections.main-product.blocks.collapsible_tab.settings.icon.options__23.label; nut_free: t:sections.main-product.blocks.collapsible_tab.settings.icon.options__24.label; pants: t:sections.main-product.blocks.collapsible_tab.settings.icon.options__25.label; paw_print: t:sections.main-product.blocks.collapsible_tab.settings.icon.options__26.label; pepper: t:sections.main-product.blocks.collapsible_tab.settings.icon.options__27.label; perfume: t:sections.main-product.blocks.collapsible_tab.settings.icon.options__28.label; plane: t:sections.main-product.blocks.collapsible_tab.settings.icon.options__29.label; plant: t:sections.main-product.blocks.collapsible_tab.settings.icon.options__30.label; price_tag: t:sections.main-product.blocks.collapsible_tab.settings.icon.options__31.label; question_mark: t:sections.main-product.blocks.collapsible_tab.settings.icon.options__32.label; recycle: t:sections.main-product.blocks.collapsible_tab.settings.icon.options__33.label; return: t:sections.main-product.blocks.collapsible_tab.settings.icon.options__34.label; ruler: t:sections.main-product.blocks.collapsible_tab.settings.icon.options__35.label; serving_dish: t:sections.main-product.blocks.collapsible_tab.settings.icon.options__36.label; shirt: t:sections.main-product.blocks.collapsible_tab.settings.icon.options__37.label; shoe: t:sections.main-product.blocks.collapsible_tab.settings.icon.options__38.label; silhouette: t:sections.main-product.blocks.collapsible_tab.settings.icon.options__39.label; snowflake: t:sections.main-product.blocks.collapsible_tab.settings.icon.options__40.label; star: t:sections.main-product.blocks.collapsible_tab.settings.icon.options__41.label; stopwatch: t:sections.main-product.blocks.collapsible_tab.settings.icon.options__42.label; truck: t:sections.main-product.blocks.collapsible_tab.settings.icon.options__43.label; washing: t:sections.main-product.blocks.collapsible_tab.settings.icon.options__44.label |
| `image_3` | `image_picker` | t:sections.main-product.blocks.icon_with_text.settings.image_3.label |
| `heading_3` | `inline_richtext` | t:sections.main-product.blocks.icon_with_text.settings.heading_3.label |

## Technische ingangen

Formtypen: `product`.

Letterlijke events in deze bron: —.

Letterlijke metafieldkeys: `reviews.rating`, `reviews.rating_count`.

DOM-hooks: `data-cart-quantity`, `data-max`, `data-min`, `data-product-id`, `data-section`, `data-section-id`, `data-text`, `data-update-url`, `data-url`, `data-variant-id`.

Geen vermelding sluit dynamische keys, externe handlers of platformwerking niet uit. Inhoud/defaults en huidige product-/contact-/settingswaarden worden niet door deze tool gepubliceerd.
