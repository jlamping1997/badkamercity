# main-list-collections

**Bron:** `sections/main-list-collections.liquid`. Bronstatus: BYTE_MATCH.

[Functioneel dossier](../../components/COLLECTIONS_AND_HUBS.md) · [Bronhashes](../source-index.json) · [Alle secties](../SECTIONS.md)

Dit is de bronreferentie. Het dossier geeft de bedoeling, data-eigenaar, toestanden en onderhoudsgrenzen.

## Koppelingen

Letterlijke callers: `templates/list-collections.json`.

Letterlijke uitgaande refs: `assets/component-card.css`, `assets/section-collection-list.css`, `snippets/card-collection.liquid`, `snippets/pagination.liquid`.

Geen caller gevonden betekent niet ongebruikt: Theme Editor, platformsections en dynamische aanroepen vallen buiten deze parser.

## Schema-instellingen

| ID | Type | Label / opties |
| --- | --- | --- |
| `title` | `inline_richtext` | t:sections.main-list-collections.settings.title.label |
| `sort` | `select` | t:sections.main-list-collections.settings.sort.label: alphabetical: t:sections.main-list-collections.settings.sort.options__1.label; alphabetical_reversed: t:sections.main-list-collections.settings.sort.options__2.label; date_reversed: t:sections.main-list-collections.settings.sort.options__3.label; date: t:sections.main-list-collections.settings.sort.options__4.label; products_high: t:sections.main-list-collections.settings.sort.options__5.label; products_low: t:sections.main-list-collections.settings.sort.options__6.label |
| `image_ratio` | `select` | t:sections.main-list-collections.settings.image_ratio.label: adapt: t:sections.main-list-collections.settings.image_ratio.options__1.label; portrait: t:sections.main-list-collections.settings.image_ratio.options__2.label; square: t:sections.main-list-collections.settings.image_ratio.options__3.label |
| `columns_desktop` | `range` | t:sections.main-list-collections.settings.columns_desktop.label |
| `columns_mobile` | `select` | t:sections.main-list-collections.settings.columns_mobile.label: 1: t:sections.main-list-collections.settings.columns_mobile.options__1.label; 2: t:sections.main-list-collections.settings.columns_mobile.options__2.label |

## Technische ingangen

Formtypen: —.

Letterlijke events in deze bron: —.

Letterlijke metafieldkeys: —.

DOM-hooks: —.

Geen vermelding sluit dynamische keys, externe handlers of platformwerking niet uit. Inhoud/defaults en huidige product-/contact-/settingswaarden worden niet door deze tool gepubliceerd.
