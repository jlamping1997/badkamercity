# newsletter

**Bron:** `sections/newsletter.liquid`. Bronstatus: BYTE_MATCH.

[Functioneel dossier](../../components/FOUNDATIONS_AND_TOOLING.md) · [Bronhashes](../source-index.json) · [Alle secties](../SECTIONS.md)

Dit is de bronreferentie. Het dossier geeft de bedoeling, data-eigenaar, toestanden en onderhoudsgrenzen.

## Koppelingen

Letterlijke callers: —.

Letterlijke uitgaande refs: `assets/component-newsletter.css`, `assets/icon-arrow.svg`, `assets/icon-error.svg`, `assets/icon-success.svg`, `assets/newsletter-section.css`.

Geen caller gevonden betekent niet ongebruikt: Theme Editor, platformsections en dynamische aanroepen vallen buiten deze parser.

## Schema-instellingen

| ID | Type | Label / opties |
| --- | --- | --- |
| `color_scheme` | `color_scheme` | t:sections.all.colors.label |
| `full_width` | `checkbox` | t:sections.newsletter.settings.full_width.label |
| `padding_top` | `range` | t:sections.all.padding.padding_top |
| `padding_bottom` | `range` | t:sections.all.padding.padding_bottom |

## Blocktype heading

| ID | Type | Label / opties |
| --- | --- | --- |
| `heading` | `inline_richtext` | t:sections.newsletter.blocks.heading.settings.heading.label |
| `heading_size` | `select` | t:sections.all.heading_size.label: h2: t:sections.all.heading_size.options__1.label; h1: t:sections.all.heading_size.options__2.label; h0: t:sections.all.heading_size.options__3.label; hxl: t:sections.all.heading_size.options__4.label; hxxl: t:sections.all.heading_size.options__5.label |

## Blocktype paragraph

| ID | Type | Label / opties |
| --- | --- | --- |
| `text` | `richtext` | t:sections.newsletter.blocks.paragraph.settings.paragraph.label |

## Blocktype email_form

| ID | Type | Label / opties |
| --- | --- | --- |

## Blocktype @app

| ID | Type | Label / opties |
| --- | --- | --- |

## Technische ingangen

Formtypen: `customer`.

Letterlijke events in deze bron: —.

Letterlijke metafieldkeys: —.

DOM-hooks: —.

Geen vermelding sluit dynamische keys, externe handlers of platformwerking niet uit. Inhoud/defaults en huidige product-/contact-/settingswaarden worden niet door deze tool gepubliceerd.
