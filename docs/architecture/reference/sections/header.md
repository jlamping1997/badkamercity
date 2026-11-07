# header

**Bron:** `sections/header.liquid`. Bronstatus: BYTE_MATCH.

[Functioneel dossier](../../components/NAVIGATION_AND_STORAGE.md) · [Bronhashes](../source-index.json) · [Alle secties](../SECTIONS.md)

Dit is de bronreferentie. Het dossier geeft de bedoeling, data-eigenaar, toestanden en onderhoudsgrenzen.

## Koppelingen

Letterlijke callers: `sections/header-group.json`.

Letterlijke uitgaande refs: `assets/cart-notification.js`, `assets/component-cart-notification.css`, `assets/component-list-menu.css`, `assets/component-mega-menu.css`, `assets/component-menu-drawer.css`, `assets/component-search.css`, `assets/icon-account-bc.svg`, `assets/icon-wishlist-bc.svg`, `snippets/bc-header-cart.liquid`, `snippets/cart-notification.liquid`, `snippets/country-localization.liquid`, `snippets/header-drawer.liquid`, `snippets/header-search.liquid`, `snippets/language-localization.liquid`.

Geen caller gevonden betekent niet ongebruikt: Theme Editor, platformsections en dynamische aanroepen vallen buiten deze parser.

## Schema-instellingen

| ID | Type | Label / opties |
| --- | --- | --- |
| `logo_position` | `select` | t:sections.header.settings.logo_position.label: top-left: t:sections.header.settings.logo_position.options__2.label; top-center: t:sections.header.settings.logo_position.options__3.label; middle-left: t:sections.header.settings.logo_position.options__1.label; middle-center: t:sections.header.settings.logo_position.options__4.label |
| `mobile_logo_position` | `select` | t:sections.header.settings.mobile_logo_position.label: center: t:sections.header.settings.mobile_logo_position.options__1.label; left: t:sections.header.settings.mobile_logo_position.options__2.label |
| `menu` | `link_list` | t:sections.header.settings.menu.label |
| `category_nav_label` | `text` | Toegankelijke naam categoriebalk |
| `category_submenu_label` | `text` | Toegankelijke naam submenu |
| `category_all_label` | `text` | Link naar volledige categorie |
| `category_close_label` | `text` | Toegankelijke naam sluiten |
| `category_previous_label` | `text` | Toegankelijke naam terugscrollen |
| `category_next_label` | `text` | Toegankelijke naam verder scrollen |
| `menu_type_desktop` | `select` | t:sections.header.settings.menu_type_desktop.label: dropdown: t:sections.header.settings.menu_type_desktop.options__1.label; mega: t:sections.header.settings.menu_type_desktop.options__2.label; drawer: t:sections.header.settings.menu_type_desktop.options__3.label |
| `sticky_header_type` | `select` | t:sections.header.settings.sticky_header_type.label: none: t:sections.header.settings.sticky_header_type.options__1.label; on-scroll-up: t:sections.header.settings.sticky_header_type.options__2.label; always: t:sections.header.settings.sticky_header_type.options__3.label; reduce-logo-size: t:sections.header.settings.sticky_header_type.options__4.label |
| `show_line_separator` | `checkbox` | t:sections.header.settings.show_line_separator.label |
| `color_scheme` | `color_scheme` | t:sections.all.colors.label |
| `menu_color_scheme` | `color_scheme` | t:sections.header.settings.menu_color_scheme.label |
| `enable_country_selector` | `checkbox` | t:sections.header.settings.enable_country_selector.label |
| `enable_language_selector` | `checkbox` | t:sections.header.settings.enable_language_selector.label |
| `enable_customer_avatar` | `checkbox` | t:sections.header.settings.enable_customer_avatar.label |
| `search_placeholder` | `text` | Search placeholder |
| `margin_bottom` | `range` | t:sections.header.settings.margin_bottom.label |
| `padding_top` | `range` | t:sections.all.padding.padding_top |
| `padding_bottom` | `range` | t:sections.all.padding.padding_bottom |

## Blocktype @app

| ID | Type | Label / opties |
| --- | --- | --- |

## Technische ingangen

Formtypen: `localization`.

Letterlijke events in deze bron: `DOMContentLoaded`, `change`, `click`, `focusin`, `focusout`, `keydown`, `mouseenter`, `mouseleave`, `pointerdown`, `preventHeaderReveal`, `resize`, `scroll`, `shopify:section:load`, `shopify:section:unload`, `toggle`.

Letterlijke metafieldkeys: —.

DOM-hooks: `data-sticky-type`.

Geen vermelding sluit dynamische keys, externe handlers of platformwerking niet uit. Inhoud/defaults en huidige product-/contact-/settingswaarden worden niet door deze tool gepubliceerd.
