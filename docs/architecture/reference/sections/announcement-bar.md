# announcement-bar

**Bron:** `sections/announcement-bar.liquid`. Bronstatus: BYTE_MATCH.

[Functioneel dossier](../../components/FOUNDATIONS_AND_TOOLING.md) · [Bronhashes](../source-index.json) · [Alle secties](../SECTIONS.md)

Dit is de bronreferentie. Het dossier geeft de bedoeling, data-eigenaar, toestanden en onderhoudsgrenzen.

## Koppelingen

Letterlijke callers: —.

Letterlijke uitgaande refs: `assets/component-list-social.css`, `assets/component-slider.css`, `assets/component-slideshow.css`, `assets/icon-arrow.svg`, `assets/icon-caret.svg`, `assets/theme-editor.js`, `snippets/country-localization.liquid`, `snippets/language-localization.liquid`, `snippets/social-icons.liquid`.

Geen caller gevonden betekent niet ongebruikt: Theme Editor, platformsections en dynamische aanroepen vallen buiten deze parser.

## Schema-instellingen

| ID | Type | Label / opties |
| --- | --- | --- |
| `auto_rotate` | `checkbox` | t:sections.announcement-bar.settings.auto_rotate.label |
| `change_slides_speed` | `range` | t:sections.announcement-bar.settings.change_slides_speed.label |
| `color_scheme` | `color_scheme` | t:sections.all.colors.label |
| `show_line_separator` | `checkbox` | t:sections.header.settings.show_line_separator.label |
| `show_social` | `checkbox` | t:sections.announcement-bar.settings.show_social.label |
| `enable_country_selector` | `checkbox` | t:sections.announcement-bar.settings.enable_country_selector.label |
| `enable_language_selector` | `checkbox` | t:sections.announcement-bar.settings.enable_language_selector.label |

## Blocktype announcement

| ID | Type | Label / opties |
| --- | --- | --- |
| `text` | `text` | t:sections.announcement-bar.blocks.announcement.settings.text.label |
| `link` | `url` | t:sections.announcement-bar.blocks.announcement.settings.link.label |

## Technische ingangen

Formtypen: `localization`.

Letterlijke events in deze bron: —.

Letterlijke metafieldkeys: —.

DOM-hooks: `data-autoplay`, `data-speed`.

Geen vermelding sluit dynamische keys, externe handlers of platformwerking niet uit. Inhoud/defaults en huidige product-/contact-/settingswaarden worden niet door deze tool gepubliceerd.
