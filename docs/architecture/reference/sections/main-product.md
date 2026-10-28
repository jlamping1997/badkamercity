# main-product

**Bron:** `sections/main-product.liquid`. Bronstatus: BYTE_MATCH.

[Functioneel dossier](../../components/PRODUCT_PAGES.md) · [Bronhashes](../source-index.json) · [Alle secties](../SECTIONS.md)

Dit is de bronreferentie. Het dossier geeft de bedoeling, data-eigenaar, toestanden en onderhoudsgrenzen.

## Koppelingen

Letterlijke callers: `templates/product.bc-disclosure-check.liquid`, `templates/product.bc-hotbath-data.json`, `templates/product.bc-hotbath-pilot.json`, `templates/product.json`.

Letterlijke uitgaande refs: `assets/bc-choice-position.js`, `assets/bc-hotbath-mobile.css`, `assets/bc-hotbath-mobile.js`, `assets/bc-hotbath-swatches.css`, `assets/bc-product-accessories.js`, `assets/bc-product-disclosure.js`, `assets/bc-product-page.css`, `assets/bc-product-sticky.js`, `assets/component-accordion.css`, `assets/component-card.css`, `assets/component-complementary-products.css`, `assets/component-deferred-media.css`, `assets/component-model-viewer-ui.css`, `assets/component-product-accessories.css`, `assets/component-product-model.css`, `assets/component-product-pros-cons.css`, `assets/component-product-set.css`, `assets/component-product-variant-picker.css`, `assets/component-rating.css`, `assets/component-slider.css`, `assets/component-swatch-input.css`, `assets/component-swatch.css`, `assets/component-volume-pricing.css`, `assets/icon-caret.svg`, `assets/icon-cart-bc.svg`, `assets/icon-close.svg`, `assets/icon-inventory-status.svg`, `assets/icon-minus.svg`, `assets/icon-plus.svg`, `assets/magnify.js`, `assets/media-gallery.js`, `assets/price-per-item.js`, `assets/product-form.js`, `assets/product-info.js`, `assets/product-modal.js`, `assets/product-model.js`, `assets/quick-add.css`, `assets/quick-add.js`, `assets/section-main-product.css`, `assets/show-more.js`, `assets/theme-editor.js`, `snippets/bc-hotbath-normal-scope.liquid`, `snippets/bc-product-accessories.liquid`, `snippets/bc-product-breadcrumbs.liquid`, `snippets/bc-product-description.liquid`, `snippets/bc-product-detail-specs.liquid`, `snippets/bc-product-documents.liquid`, `snippets/bc-product-set-components.liquid`, `snippets/bc-product-switcher.liquid`, `snippets/bc-sunshower-choices.liquid`, `snippets/bc-wiesbaden-colors.liquid`, `snippets/buy-buttons.liquid`, `snippets/card-product.liquid`, `snippets/icon-accordion.liquid`, `snippets/icon-with-text.liquid`, `snippets/loading-spinner.liquid`, `snippets/product-media-gallery.liquid`, `snippets/product-media-modal.liquid`, `snippets/product-pros-cons.liquid`, `snippets/product-variant-picker.liquid`.

Geen caller gevonden betekent niet ongebruikt: Theme Editor, platformsections en dynamische aanroepen vallen buiten deze parser.

## Schema-instellingen

| ID | Type | Label / opties |
| --- | --- | --- |
| `enable_sticky_info` | `checkbox` | t:sections.main-product.settings.enable_sticky_info.label |
| `color_scheme` | `color_scheme` | t:sections.all.colors.label |
| `media_size` | `select` | t:sections.main-product.settings.media_size.label: small: t:sections.main-product.settings.media_size.options__1.label; medium: t:sections.main-product.settings.media_size.options__2.label; large: t:sections.main-product.settings.media_size.options__3.label |
| `constrain_to_viewport` | `checkbox` | t:sections.main-product.settings.constrain_to_viewport.label |
| `media_fit` | `select` | t:sections.main-product.settings.media_fit.label: contain: t:sections.main-product.settings.media_fit.options__1.label; cover: t:sections.main-product.settings.media_fit.options__2.label |
| `gallery_layout` | `select` | t:sections.main-product.settings.gallery_layout.label: stacked: t:sections.main-product.settings.gallery_layout.options__1.label; columns: t:sections.main-product.settings.gallery_layout.options__2.label; thumbnail: t:sections.main-product.settings.gallery_layout.options__3.label; thumbnail_slider: t:sections.main-product.settings.gallery_layout.options__4.label |
| `mobile_thumbnails` | `select` | t:sections.main-product.settings.mobile_thumbnails.label: columns: t:sections.main-product.settings.mobile_thumbnails.options__1.label; show: t:sections.main-product.settings.mobile_thumbnails.options__2.label; hide: t:sections.main-product.settings.mobile_thumbnails.options__3.label |
| `media_position` | `select` | t:sections.main-product.settings.media_position.label: left: t:sections.main-product.settings.media_position.options__1.label; right: t:sections.main-product.settings.media_position.options__2.label |
| `image_zoom` | `select` | t:sections.main-product.settings.image_zoom.label: lightbox: t:sections.main-product.settings.image_zoom.options__1.label; hover: t:sections.main-product.settings.image_zoom.options__2.label; none: t:sections.main-product.settings.image_zoom.options__3.label |
| `hide_variants` | `checkbox` | t:sections.main-product.settings.hide_variants.label |
| `enable_video_looping` | `checkbox` | t:sections.main-product.settings.enable_video_looping.label |
| `padding_top` | `range` | t:sections.all.padding.padding_top |
| `padding_bottom` | `range` | t:sections.all.padding.padding_bottom |

## Blocktype @app

| ID | Type | Label / opties |
| --- | --- | --- |

## Blocktype text

| ID | Type | Label / opties |
| --- | --- | --- |
| `text` | `inline_richtext` | t:sections.main-product.blocks.text.settings.text.label |
| `text_style` | `select` | t:sections.main-product.blocks.text.settings.text_style.label: body: t:sections.main-product.blocks.text.settings.text_style.options__1.label; subtitle: t:sections.main-product.blocks.text.settings.text_style.options__2.label; uppercase: t:sections.main-product.blocks.text.settings.text_style.options__3.label |

## Blocktype title

| ID | Type | Label / opties |
| --- | --- | --- |

## Blocktype price

| ID | Type | Label / opties |
| --- | --- | --- |

## Blocktype sku

| ID | Type | Label / opties |
| --- | --- | --- |
| `text_style` | `select` | t:sections.main-product.blocks.sku.settings.text_style.label: body: t:sections.main-product.blocks.sku.settings.text_style.options__1.label; subtitle: t:sections.main-product.blocks.sku.settings.text_style.options__2.label; uppercase: t:sections.main-product.blocks.sku.settings.text_style.options__3.label |

## Blocktype inventory

| ID | Type | Label / opties |
| --- | --- | --- |
| `text_style` | `select` | t:sections.main-product.blocks.inventory.settings.text_style.label: body: t:sections.main-product.blocks.inventory.settings.text_style.options__1.label; subtitle: t:sections.main-product.blocks.inventory.settings.text_style.options__2.label; uppercase: t:sections.main-product.blocks.inventory.settings.text_style.options__3.label |
| `inventory_threshold` | `range` | t:sections.main-product.blocks.inventory.settings.inventory_threshold.label |
| `show_inventory_quantity` | `checkbox` | t:sections.main-product.blocks.inventory.settings.show_inventory_quantity.label |

## Blocktype quantity_selector

| ID | Type | Label / opties |
| --- | --- | --- |

## Blocktype variant_picker

| ID | Type | Label / opties |
| --- | --- | --- |
| `picker_type` | `select` | t:sections.main-product.blocks.variant_picker.settings.picker_type.label: dropdown: t:sections.main-product.blocks.variant_picker.settings.picker_type.options__1.label; button: t:sections.main-product.blocks.variant_picker.settings.picker_type.options__2.label |
| `swatch_shape` | `select` | t:sections.main-product.blocks.variant_picker.settings.swatch_shape.label: circle: t:sections.main-product.blocks.variant_picker.settings.swatch_shape.options__1.label; square: t:sections.main-product.blocks.variant_picker.settings.swatch_shape.options__2.label; none: t:sections.main-product.blocks.variant_picker.settings.swatch_shape.options__3.label |

## Blocktype buy_buttons

| ID | Type | Label / opties |
| --- | --- | --- |
| `show_dynamic_checkout` | `checkbox` | t:sections.main-product.blocks.buy_buttons.settings.show_dynamic_checkout.label |
| `show_gift_card_recipient` | `checkbox` | t:sections.main-product.blocks.buy_buttons.settings.show_gift_card_recipient.label |

## Blocktype description

| ID | Type | Label / opties |
| --- | --- | --- |

## Blocktype share

| ID | Type | Label / opties |
| --- | --- | --- |
| `share_label` | `text` | t:sections.main-product.blocks.share.settings.text.label |

## Blocktype custom_liquid

| ID | Type | Label / opties |
| --- | --- | --- |
| `custom_liquid` | `liquid` | t:sections.custom-liquid.settings.custom_liquid.label |

## Blocktype collapsible_tab

| ID | Type | Label / opties |
| --- | --- | --- |
| `heading` | `text` | t:sections.main-product.blocks.collapsible_tab.settings.heading.label |
| `icon` | `select` | t:sections.main-product.blocks.collapsible_tab.settings.icon.label: none: t:sections.main-product.blocks.collapsible_tab.settings.icon.options__1.label; apple: t:sections.main-product.blocks.collapsible_tab.settings.icon.options__2.label; banana: t:sections.main-product.blocks.collapsible_tab.settings.icon.options__3.label; bottle: t:sections.main-product.blocks.collapsible_tab.settings.icon.options__4.label; box: t:sections.main-product.blocks.collapsible_tab.settings.icon.options__5.label; carrot: t:sections.main-product.blocks.collapsible_tab.settings.icon.options__6.label; chat_bubble: t:sections.main-product.blocks.collapsible_tab.settings.icon.options__7.label; check_mark: t:sections.main-product.blocks.collapsible_tab.settings.icon.options__8.label; clipboard: t:sections.main-product.blocks.collapsible_tab.settings.icon.options__9.label; dairy: t:sections.main-product.blocks.collapsible_tab.settings.icon.options__10.label; dairy_free: t:sections.main-product.blocks.collapsible_tab.settings.icon.options__11.label; dryer: t:sections.main-product.blocks.collapsible_tab.settings.icon.options__12.label; eye: t:sections.main-product.blocks.collapsible_tab.settings.icon.options__13.label; fire: t:sections.main-product.blocks.collapsible_tab.settings.icon.options__14.label; gluten_free: t:sections.main-product.blocks.collapsible_tab.settings.icon.options__15.label; heart: t:sections.main-product.blocks.collapsible_tab.settings.icon.options__16.label; iron: t:sections.main-product.blocks.collapsible_tab.settings.icon.options__17.label; leaf: t:sections.main-product.blocks.collapsible_tab.settings.icon.options__18.label; leather: t:sections.main-product.blocks.collapsible_tab.settings.icon.options__19.label; lightning_bolt: t:sections.main-product.blocks.collapsible_tab.settings.icon.options__20.label; lipstick: t:sections.main-product.blocks.collapsible_tab.settings.icon.options__21.label; lock: t:sections.main-product.blocks.collapsible_tab.settings.icon.options__22.label; map_pin: t:sections.main-product.blocks.collapsible_tab.settings.icon.options__23.label; nut_free: t:sections.main-product.blocks.collapsible_tab.settings.icon.options__24.label; pants: t:sections.main-product.blocks.collapsible_tab.settings.icon.options__25.label; paw_print: t:sections.main-product.blocks.collapsible_tab.settings.icon.options__26.label; pepper: t:sections.main-product.blocks.collapsible_tab.settings.icon.options__27.label; perfume: t:sections.main-product.blocks.collapsible_tab.settings.icon.options__28.label; plane: t:sections.main-product.blocks.collapsible_tab.settings.icon.options__29.label; plant: t:sections.main-product.blocks.collapsible_tab.settings.icon.options__30.label; price_tag: t:sections.main-product.blocks.collapsible_tab.settings.icon.options__31.label; question_mark: t:sections.main-product.blocks.collapsible_tab.settings.icon.options__32.label; recycle: t:sections.main-product.blocks.collapsible_tab.settings.icon.options__33.label; return: t:sections.main-product.blocks.collapsible_tab.settings.icon.options__34.label; ruler: t:sections.main-product.blocks.collapsible_tab.settings.icon.options__35.label; serving_dish: t:sections.main-product.blocks.collapsible_tab.settings.icon.options__36.label; shirt: t:sections.main-product.blocks.collapsible_tab.settings.icon.options__37.label; shoe: t:sections.main-product.blocks.collapsible_tab.settings.icon.options__38.label; silhouette: t:sections.main-product.blocks.collapsible_tab.settings.icon.options__39.label; snowflake: t:sections.main-product.blocks.collapsible_tab.settings.icon.options__40.label; star: t:sections.main-product.blocks.collapsible_tab.settings.icon.options__41.label; stopwatch: t:sections.main-product.blocks.collapsible_tab.settings.icon.options__42.label; truck: t:sections.main-product.blocks.collapsible_tab.settings.icon.options__43.label; washing: t:sections.main-product.blocks.collapsible_tab.settings.icon.options__44.label |
| `content` | `richtext` | t:sections.main-product.blocks.collapsible_tab.settings.content.label |
| `page` | `page` | t:sections.main-product.blocks.collapsible_tab.settings.page.label |

## Blocktype popup

| ID | Type | Label / opties |
| --- | --- | --- |
| `text` | `text` | t:sections.main-product.blocks.popup.settings.link_label.label |
| `page` | `page` | t:sections.main-product.blocks.popup.settings.page.label |

## Blocktype rating

| ID | Type | Label / opties |
| --- | --- | --- |

## Blocktype complementary

| ID | Type | Label / opties |
| --- | --- | --- |
| `block_heading` | `text` | t:sections.main-product.blocks.complementary_products.settings.heading.label |
| `make_collapsible_row` | `checkbox` | t:sections.main-product.blocks.complementary_products.settings.make_collapsible_row.label |
| `icon` | `select` | t:sections.main-product.blocks.collapsible_tab.settings.icon.label: none: t:sections.main-product.blocks.collapsible_tab.settings.icon.options__1.label; apple: t:sections.main-product.blocks.collapsible_tab.settings.icon.options__2.label; banana: t:sections.main-product.blocks.collapsible_tab.settings.icon.options__3.label; bottle: t:sections.main-product.blocks.collapsible_tab.settings.icon.options__4.label; box: t:sections.main-product.blocks.collapsible_tab.settings.icon.options__5.label; carrot: t:sections.main-product.blocks.collapsible_tab.settings.icon.options__6.label; chat_bubble: t:sections.main-product.blocks.collapsible_tab.settings.icon.options__7.label; check_mark: t:sections.main-product.blocks.collapsible_tab.settings.icon.options__8.label; clipboard: t:sections.main-product.blocks.collapsible_tab.settings.icon.options__9.label; dairy: t:sections.main-product.blocks.collapsible_tab.settings.icon.options__10.label; dairy_free: t:sections.main-product.blocks.collapsible_tab.settings.icon.options__11.label; dryer: t:sections.main-product.blocks.collapsible_tab.settings.icon.options__12.label; eye: t:sections.main-product.blocks.collapsible_tab.settings.icon.options__13.label; fire: t:sections.main-product.blocks.collapsible_tab.settings.icon.options__14.label; gluten_free: t:sections.main-product.blocks.collapsible_tab.settings.icon.options__15.label; heart: t:sections.main-product.blocks.collapsible_tab.settings.icon.options__16.label; iron: t:sections.main-product.blocks.collapsible_tab.settings.icon.options__17.label; leaf: t:sections.main-product.blocks.collapsible_tab.settings.icon.options__18.label; leather: t:sections.main-product.blocks.collapsible_tab.settings.icon.options__19.label; lightning_bolt: t:sections.main-product.blocks.collapsible_tab.settings.icon.options__20.label; lipstick: t:sections.main-product.blocks.collapsible_tab.settings.icon.options__21.label; lock: t:sections.main-product.blocks.collapsible_tab.settings.icon.options__22.label; map_pin: t:sections.main-product.blocks.collapsible_tab.settings.icon.options__23.label; nut_free: t:sections.main-product.blocks.collapsible_tab.settings.icon.options__24.label; pants: t:sections.main-product.blocks.collapsible_tab.settings.icon.options__25.label; paw_print: t:sections.main-product.blocks.collapsible_tab.settings.icon.options__26.label; pepper: t:sections.main-product.blocks.collapsible_tab.settings.icon.options__27.label; perfume: t:sections.main-product.blocks.collapsible_tab.settings.icon.options__28.label; plane: t:sections.main-product.blocks.collapsible_tab.settings.icon.options__29.label; plant: t:sections.main-product.blocks.collapsible_tab.settings.icon.options__30.label; price_tag: t:sections.main-product.blocks.collapsible_tab.settings.icon.options__31.label; question_mark: t:sections.main-product.blocks.collapsible_tab.settings.icon.options__32.label; recycle: t:sections.main-product.blocks.collapsible_tab.settings.icon.options__33.label; return: t:sections.main-product.blocks.collapsible_tab.settings.icon.options__34.label; ruler: t:sections.main-product.blocks.collapsible_tab.settings.icon.options__35.label; serving_dish: t:sections.main-product.blocks.collapsible_tab.settings.icon.options__36.label; shirt: t:sections.main-product.blocks.collapsible_tab.settings.icon.options__37.label; shoe: t:sections.main-product.blocks.collapsible_tab.settings.icon.options__38.label; silhouette: t:sections.main-product.blocks.collapsible_tab.settings.icon.options__39.label; snowflake: t:sections.main-product.blocks.collapsible_tab.settings.icon.options__40.label; star: t:sections.main-product.blocks.collapsible_tab.settings.icon.options__41.label; stopwatch: t:sections.main-product.blocks.collapsible_tab.settings.icon.options__42.label; truck: t:sections.main-product.blocks.collapsible_tab.settings.icon.options__43.label; washing: t:sections.main-product.blocks.collapsible_tab.settings.icon.options__44.label |
| `product_list_limit` | `range` | t:sections.main-product.blocks.complementary_products.settings.product_list_limit.label |
| `products_per_page` | `range` | t:sections.main-product.blocks.complementary_products.settings.products_per_page.label |
| `pagination_style` | `select` | t:sections.main-product.blocks.complementary_products.settings.pagination_style.label: dots: t:sections.main-product.blocks.complementary_products.settings.pagination_style.options.option_1; counter: t:sections.main-product.blocks.complementary_products.settings.pagination_style.options.option_2; numbers: t:sections.main-product.blocks.complementary_products.settings.pagination_style.options.option_3 |
| `image_ratio` | `select` | t:sections.main-product.blocks.complementary_products.settings.image_ratio.label: portrait: t:sections.main-product.blocks.complementary_products.settings.image_ratio.options.option_1; square: t:sections.main-product.blocks.complementary_products.settings.image_ratio.options.option_2 |
| `enable_quick_add` | `checkbox` | t:sections.main-product.blocks.complementary_products.settings.enable_quick_add.label |

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

Formtypen: —.

Letterlijke events in deze bron: —.

Letterlijke metafieldkeys: `bc_sunshower.configuration`, `bc_sunshower.source`, `custom.afmeting`, `custom.afwerking`, `custom.basiskleur`, `custom.breedte_diameter_hoofddouche`, `custom.color_variants`, `custom.frame`, `custom.group`, `custom.handdouche`, `custom.hoofddouche`, `custom.hoogte`, `custom.led`, `custom.lengte`, `custom.leverancier_verwachte_datum`, `custom.leverancier_voorraad`, `custom.menu_1`, `custom.menu_2`, `custom.menu_3`, `custom.menu_4`, `custom.menu_5`, `custom.met_glijstang`, `custom.montage`, `custom.plaatsing`, `custom.switch_group`, `custom.switch_key`, `custom.type`, `custom.type_bevestiging_hoofddouche`, `custom.type_handdouche`, `custom.vorm`, `reviews.rating`, `reviews.rating_count`.

DOM-hooks: `data-cart-quantity`, `data-currency`, `data-current-url`, `data-disclosure-mode`, `data-hotbath-mobile-a`, `data-max`, `data-min`, `data-mobile-choose-inbouw-label`, `data-mobile-total-label`, `data-mobile-vat-label`, `data-modal`, `data-product-id`, `data-product-price`, `data-product-variant`, `data-section`, `data-section-id`, `data-sunshower-product`, `data-switch-field`, `data-switch-value`, `data-switcher-group`, `data-text`, `data-update-url`, `data-url`, `data-variant-id`.

Geen vermelding sluit dynamische keys, externe handlers of platformwerking niet uit. Inhoud/defaults en huidige product-/contact-/settingswaarden worden niet door deze tool gepubliceerd.
