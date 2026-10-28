# home-category-grid

**Bron:** `sections/home-category-grid.liquid`. Bronstatus: BYTE_MATCH.

[Functioneel dossier](../../components/HOMEPAGE.md) · [Bronhashes](../source-index.json) · [Alle secties](../SECTIONS.md)

Dit is de bronreferentie. Het dossier geeft de bedoeling, data-eigenaar, toestanden en onderhoudsgrenzen.

## Koppelingen

Letterlijke callers: `templates/index.json`.

Letterlijke uitgaande refs: —.

Geen caller gevonden betekent niet ongebruikt: Theme Editor, platformsections en dynamische aanroepen vallen buiten deze parser.

## Schema-instellingen

| ID | Type | Label / opties |
| --- | --- | --- |
| `title` | `inline_richtext` | Section title |
| `view_all_label` | `text` | All categories link label |
| `view_all_link` | `url` | All categories link |
| `menu` | `link_list` | Category menu |
| `source_mode` | `select` | Category source: menu: Use menu; manual: Use manual category blocks |
| `columns_desktop` | `range` | Items per row on desktop |
| `columns_mobile` | `range` | Items per row on mobile |
| `padding_top` | `range` | Padding top |
| `padding_bottom` | `range` | Padding bottom |

## Blocktype category_item

| ID | Type | Label / opties |
| --- | --- | --- |
| `collection` | `collection` | Collection |
| `custom_title` | `text` | Custom title |
| `show_on_desktop` | `checkbox` | Show on desktop |
| `show_on_mobile` | `checkbox` | Show on mobile |

## Technische ingangen

Formtypen: —.

Letterlijke events in deze bron: —.

Letterlijke metafieldkeys: —.

DOM-hooks: —.

Geen vermelding sluit dynamische keys, externe handlers of platformwerking niet uit. Inhoud/defaults en huidige product-/contact-/settingswaarden worden niet door deze tool gepubliceerd.
