# Globale instellingen en talen

Bronmoment 28 oktober 2026. Gegenereerde letterlijke zoekkaart; geen volledige parser, runtimebewijs of handmatige review. Dynamische refs, CSS-cascade en platforminjecties apart volgen. Paden/regelnummers horen bij [bronhashes](source-index.json), niet automatisch bij Git-root.

Geen huidige settings_data.json-waarden gepubliceerd. Die body wijkt nog van de Shopify-metadata af.

## t:settings_schema.logo.name

| ID | Type | Label / opties |
| --- | --- | --- |
| `logo` | `image_picker` | t:settings_schema.logo.settings.logo_image.label |
| `logo_width` | `range` | t:settings_schema.logo.settings.logo_width.label |
| `favicon` | `image_picker` | t:settings_schema.logo.settings.favicon.label |

## t:settings_schema.colors.name

| ID | Type | Label / opties |
| --- | --- | --- |
| `color_schemes` | `color_scheme_group` | — |

## t:settings_schema.typography.name

| ID | Type | Label / opties |
| --- | --- | --- |
| `type_header_font` | `font_picker` | t:settings_schema.typography.settings.type_header_font.label |
| `heading_scale` | `range` | t:settings_schema.typography.settings.heading_scale.label |
| `type_body_font` | `font_picker` | t:settings_schema.typography.settings.type_body_font.label |
| `body_scale` | `range` | t:settings_schema.typography.settings.body_scale.label |

## t:settings_schema.layout.name

| ID | Type | Label / opties |
| --- | --- | --- |
| `page_width` | `range` | t:settings_schema.layout.settings.page_width.label |
| `spacing_sections` | `range` | t:settings_schema.layout.settings.spacing_sections.label |
| `spacing_grid_horizontal` | `range` | t:settings_schema.layout.settings.spacing_grid_horizontal.label |
| `spacing_grid_vertical` | `range` | t:settings_schema.layout.settings.spacing_grid_vertical.label |

## t:settings_schema.animations.name

| ID | Type | Label / opties |
| --- | --- | --- |
| `animations_reveal_on_scroll` | `checkbox` | t:settings_schema.animations.settings.animations_reveal_on_scroll.label |
| `animations_hover_elements` | `select` | t:settings_schema.animations.settings.animations_hover_elements.label: default: t:settings_schema.animations.settings.animations_hover_elements.options__1.label; vertical-lift: t:settings_schema.animations.settings.animations_hover_elements.options__2.label; 3d-lift: t:settings_schema.animations.settings.animations_hover_elements.options__3.label |

## t:settings_schema.buttons.name

| ID | Type | Label / opties |
| --- | --- | --- |
| `buttons_border_thickness` | `range` | t:settings_schema.global.settings.thickness.label |
| `buttons_border_opacity` | `range` | t:settings_schema.global.settings.opacity.label |
| `buttons_radius` | `range` | t:settings_schema.global.settings.corner_radius.label |
| `buttons_shadow_opacity` | `range` | t:settings_schema.global.settings.opacity.label |
| `buttons_shadow_horizontal_offset` | `range` | t:settings_schema.global.settings.horizontal_offset.label |
| `buttons_shadow_vertical_offset` | `range` | t:settings_schema.global.settings.vertical_offset.label |
| `buttons_shadow_blur` | `range` | t:settings_schema.global.settings.blur.label |

## t:settings_schema.variant_pills.name

| ID | Type | Label / opties |
| --- | --- | --- |
| `variant_pills_border_thickness` | `range` | t:settings_schema.global.settings.thickness.label |
| `variant_pills_border_opacity` | `range` | t:settings_schema.global.settings.opacity.label |
| `variant_pills_radius` | `range` | t:settings_schema.global.settings.corner_radius.label |
| `variant_pills_shadow_opacity` | `range` | t:settings_schema.global.settings.opacity.label |
| `variant_pills_shadow_horizontal_offset` | `range` | t:settings_schema.global.settings.horizontal_offset.label |
| `variant_pills_shadow_vertical_offset` | `range` | t:settings_schema.global.settings.vertical_offset.label |
| `variant_pills_shadow_blur` | `range` | t:settings_schema.global.settings.blur.label |

## t:settings_schema.inputs.name

| ID | Type | Label / opties |
| --- | --- | --- |
| `inputs_border_thickness` | `range` | t:settings_schema.global.settings.thickness.label |
| `inputs_border_opacity` | `range` | t:settings_schema.global.settings.opacity.label |
| `inputs_radius` | `range` | t:settings_schema.global.settings.corner_radius.label |
| `inputs_shadow_opacity` | `range` | t:settings_schema.global.settings.opacity.label |
| `inputs_shadow_horizontal_offset` | `range` | t:settings_schema.global.settings.horizontal_offset.label |
| `inputs_shadow_vertical_offset` | `range` | t:settings_schema.global.settings.vertical_offset.label |
| `inputs_shadow_blur` | `range` | t:settings_schema.global.settings.blur.label |

## t:settings_schema.cards.name

| ID | Type | Label / opties |
| --- | --- | --- |
| `card_style` | `select` | t:settings_schema.cards.settings.style.label: standard: t:settings_schema.cards.settings.style.options__1.label; card: t:settings_schema.cards.settings.style.options__2.label |
| `card_image_padding` | `range` | t:settings_schema.global.settings.image_padding.label |
| `card_text_alignment` | `select` | t:settings_schema.global.settings.text_alignment.label: left: t:settings_schema.global.settings.text_alignment.options__1.label; center: t:settings_schema.global.settings.text_alignment.options__2.label; right: t:settings_schema.global.settings.text_alignment.options__3.label |
| `card_color_scheme` | `color_scheme` | t:sections.all.colors.label |
| `card_border_thickness` | `range` | t:settings_schema.global.settings.thickness.label |
| `card_border_opacity` | `range` | t:settings_schema.global.settings.opacity.label |
| `card_corner_radius` | `range` | t:settings_schema.global.settings.corner_radius.label |
| `card_shadow_opacity` | `range` | t:settings_schema.global.settings.opacity.label |
| `card_shadow_horizontal_offset` | `range` | t:settings_schema.global.settings.horizontal_offset.label |
| `card_shadow_vertical_offset` | `range` | t:settings_schema.global.settings.vertical_offset.label |
| `card_shadow_blur` | `range` | t:settings_schema.global.settings.blur.label |

## t:settings_schema.collection_cards.name

| ID | Type | Label / opties |
| --- | --- | --- |
| `collection_card_style` | `select` | t:settings_schema.collection_cards.settings.style.label: standard: t:settings_schema.collection_cards.settings.style.options__1.label; card: t:settings_schema.collection_cards.settings.style.options__2.label |
| `collection_card_image_padding` | `range` | t:settings_schema.global.settings.image_padding.label |
| `collection_card_text_alignment` | `select` | t:settings_schema.global.settings.text_alignment.label: left: t:settings_schema.global.settings.text_alignment.options__1.label; center: t:settings_schema.global.settings.text_alignment.options__2.label; right: t:settings_schema.global.settings.text_alignment.options__3.label |
| `collection_card_color_scheme` | `color_scheme` | t:sections.all.colors.label |
| `collection_card_border_thickness` | `range` | t:settings_schema.global.settings.thickness.label |
| `collection_card_border_opacity` | `range` | t:settings_schema.global.settings.opacity.label |
| `collection_card_corner_radius` | `range` | t:settings_schema.global.settings.corner_radius.label |
| `collection_card_shadow_opacity` | `range` | t:settings_schema.global.settings.opacity.label |
| `collection_card_shadow_horizontal_offset` | `range` | t:settings_schema.global.settings.horizontal_offset.label |
| `collection_card_shadow_vertical_offset` | `range` | t:settings_schema.global.settings.vertical_offset.label |
| `collection_card_shadow_blur` | `range` | t:settings_schema.global.settings.blur.label |

## t:settings_schema.blog_cards.name

| ID | Type | Label / opties |
| --- | --- | --- |
| `blog_card_style` | `select` | t:settings_schema.blog_cards.settings.style.label: standard: t:settings_schema.blog_cards.settings.style.options__1.label; card: t:settings_schema.blog_cards.settings.style.options__2.label |
| `blog_card_image_padding` | `range` | t:settings_schema.global.settings.image_padding.label |
| `blog_card_text_alignment` | `select` | t:settings_schema.global.settings.text_alignment.label: left: t:settings_schema.global.settings.text_alignment.options__1.label; center: t:settings_schema.global.settings.text_alignment.options__2.label; right: t:settings_schema.global.settings.text_alignment.options__3.label |
| `blog_card_color_scheme` | `color_scheme` | t:sections.all.colors.label |
| `blog_card_border_thickness` | `range` | t:settings_schema.global.settings.thickness.label |
| `blog_card_border_opacity` | `range` | t:settings_schema.global.settings.opacity.label |
| `blog_card_corner_radius` | `range` | t:settings_schema.global.settings.corner_radius.label |
| `blog_card_shadow_opacity` | `range` | t:settings_schema.global.settings.opacity.label |
| `blog_card_shadow_horizontal_offset` | `range` | t:settings_schema.global.settings.horizontal_offset.label |
| `blog_card_shadow_vertical_offset` | `range` | t:settings_schema.global.settings.vertical_offset.label |
| `blog_card_shadow_blur` | `range` | t:settings_schema.global.settings.blur.label |

## t:settings_schema.content_containers.name

| ID | Type | Label / opties |
| --- | --- | --- |
| `text_boxes_border_thickness` | `range` | t:settings_schema.global.settings.thickness.label |
| `text_boxes_border_opacity` | `range` | t:settings_schema.global.settings.opacity.label |
| `text_boxes_radius` | `range` | t:settings_schema.global.settings.corner_radius.label |
| `text_boxes_shadow_opacity` | `range` | t:settings_schema.global.settings.opacity.label |
| `text_boxes_shadow_horizontal_offset` | `range` | t:settings_schema.global.settings.horizontal_offset.label |
| `text_boxes_shadow_vertical_offset` | `range` | t:settings_schema.global.settings.vertical_offset.label |
| `text_boxes_shadow_blur` | `range` | t:settings_schema.global.settings.blur.label |

## t:settings_schema.media.name

| ID | Type | Label / opties |
| --- | --- | --- |
| `media_border_thickness` | `range` | t:settings_schema.global.settings.thickness.label |
| `media_border_opacity` | `range` | t:settings_schema.global.settings.opacity.label |
| `media_radius` | `range` | t:settings_schema.global.settings.corner_radius.label |
| `media_shadow_opacity` | `range` | t:settings_schema.global.settings.opacity.label |
| `media_shadow_horizontal_offset` | `range` | t:settings_schema.global.settings.horizontal_offset.label |
| `media_shadow_vertical_offset` | `range` | t:settings_schema.global.settings.vertical_offset.label |
| `media_shadow_blur` | `range` | t:settings_schema.global.settings.blur.label |

## t:settings_schema.popups.name

| ID | Type | Label / opties |
| --- | --- | --- |
| `popup_border_thickness` | `range` | t:settings_schema.global.settings.thickness.label |
| `popup_border_opacity` | `range` | t:settings_schema.global.settings.opacity.label |
| `popup_corner_radius` | `range` | t:settings_schema.global.settings.corner_radius.label |
| `popup_shadow_opacity` | `range` | t:settings_schema.global.settings.opacity.label |
| `popup_shadow_horizontal_offset` | `range` | t:settings_schema.global.settings.horizontal_offset.label |
| `popup_shadow_vertical_offset` | `range` | t:settings_schema.global.settings.vertical_offset.label |
| `popup_shadow_blur` | `range` | t:settings_schema.global.settings.blur.label |

## t:settings_schema.drawers.name

| ID | Type | Label / opties |
| --- | --- | --- |
| `drawer_border_thickness` | `range` | t:settings_schema.global.settings.thickness.label |
| `drawer_border_opacity` | `range` | t:settings_schema.global.settings.opacity.label |
| `drawer_shadow_opacity` | `range` | t:settings_schema.global.settings.opacity.label |
| `drawer_shadow_horizontal_offset` | `range` | t:settings_schema.global.settings.horizontal_offset.label |
| `drawer_shadow_vertical_offset` | `range` | t:settings_schema.global.settings.vertical_offset.label |
| `drawer_shadow_blur` | `range` | t:settings_schema.global.settings.blur.label |

## t:settings_schema.badges.name

| ID | Type | Label / opties |
| --- | --- | --- |
| `badge_position` | `select` | t:settings_schema.badges.settings.position.label: bottom left: t:settings_schema.badges.settings.position.options__1.label; bottom right: t:settings_schema.badges.settings.position.options__2.label; top left: t:settings_schema.badges.settings.position.options__3.label; top right: t:settings_schema.badges.settings.position.options__4.label |
| `badge_corner_radius` | `range` | t:settings_schema.global.settings.corner_radius.label |
| `sale_badge_color_scheme` | `color_scheme` | t:settings_schema.badges.settings.sale_badge_color_scheme.label |
| `sold_out_badge_color_scheme` | `color_scheme` | t:settings_schema.badges.settings.sold_out_badge_color_scheme.label |

## t:settings_schema.brand_information.name

| ID | Type | Label / opties |
| --- | --- | --- |
| `brand_headline` | `inline_richtext` | t:settings_schema.brand_information.settings.brand_headline.label |
| `brand_description` | `richtext` | t:settings_schema.brand_information.settings.brand_description.label |
| `brand_image` | `image_picker` | t:settings_schema.brand_information.settings.brand_image.label |
| `brand_image_width` | `range` | t:settings_schema.brand_information.settings.brand_image_width.label |

## t:settings_schema.social-media.name

| ID | Type | Label / opties |
| --- | --- | --- |
| `social_facebook_link` | `text` | t:settings_schema.social-media.settings.social_facebook_link.label |
| `social_instagram_link` | `text` | t:settings_schema.social-media.settings.social_instagram_link.label |
| `social_youtube_link` | `text` | t:settings_schema.social-media.settings.social_youtube_link.label |
| `social_tiktok_link` | `text` | t:settings_schema.social-media.settings.social_tiktok_link.label |
| `social_twitter_link` | `text` | t:settings_schema.social-media.settings.social_twitter_link.label |
| `social_snapchat_link` | `text` | t:settings_schema.social-media.settings.social_snapchat_link.label |
| `social_pinterest_link` | `text` | t:settings_schema.social-media.settings.social_pinterest_link.label |
| `social_tumblr_link` | `text` | t:settings_schema.social-media.settings.social_tumblr_link.label |
| `social_vimeo_link` | `text` | t:settings_schema.social-media.settings.social_vimeo_link.label |

## t:settings_schema.search_input.name

| ID | Type | Label / opties |
| --- | --- | --- |
| `predictive_search_enabled` | `checkbox` | t:settings_schema.search_input.settings.predictive_search_enabled.label |
| `predictive_search_show_vendor` | `checkbox` | t:settings_schema.search_input.settings.predictive_search_show_vendor.label |
| `predictive_search_show_price` | `checkbox` | t:settings_schema.search_input.settings.predictive_search_show_price.label |

## t:settings_schema.currency_format.name

| ID | Type | Label / opties |
| --- | --- | --- |
| `currency_code_enabled` | `checkbox` | t:settings_schema.currency_format.settings.currency_code_enabled.label |

## t:settings_schema.cart.name

| ID | Type | Label / opties |
| --- | --- | --- |
| `cart_type` | `select` | t:settings_schema.cart.settings.cart_type.label: drawer: t:settings_schema.cart.settings.cart_type.drawer.label; page: t:settings_schema.cart.settings.cart_type.page.label; notification: t:settings_schema.cart.settings.cart_type.notification.label |
| `show_vendor` | `checkbox` | t:settings_schema.cart.settings.show_vendor.label |
| `show_cart_note` | `checkbox` | t:settings_schema.cart.settings.show_cart_note.label |
| `cart_drawer_collection` | `collection` | t:settings_schema.cart.settings.cart_drawer.collection.label |
| `cart_color_scheme` | `color_scheme` | t:sections.all.colors.label |

## Locale-assets

Er zijn 51 locale-assets inclusief editor-schema’s. Dit is niet het aantal gepubliceerde winkeltalen. De actuele Admin-taal is `nl` (primair/gepubliceerd).
