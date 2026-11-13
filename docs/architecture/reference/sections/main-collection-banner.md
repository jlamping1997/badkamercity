# main-collection-banner

**Bron:** `sections/main-collection-banner.liquid`. Bronstatus: BYTE_MATCH.

[Functioneel dossier](../../components/FOUNDATIONS_AND_TOOLING.md) · [Bronhashes](../source-index.json) · [Alle secties](../SECTIONS.md)

Dit is de bronreferentie. Het dossier geeft de bedoeling, data-eigenaar, toestanden en onderhoudsgrenzen.

## Koppelingen

Letterlijke callers: `templates/collection.json`.

Letterlijke uitgaande refs: `assets/bc-category-directory.css`, `assets/bc-collection.css`, `assets/component-bc-category-navigation.css`, `assets/component-collection-hero.css`, `snippets/bc-category-breadcrumbs.liquid`, `snippets/bc-category-children.liquid`, `snippets/bc-category-link-index.liquid`, `snippets/bc-collection-intro.liquid`.

Geen caller gevonden betekent niet ongebruikt: Theme Editor, platformsections en dynamische aanroepen vallen buiten deze parser.

## Schema-instellingen

| ID | Type | Label / opties |
| --- | --- | --- |
| `navigation_menu` | `link_list` | Menu voor de categorieboom |
| `show_collection_description` | `checkbox` | t:sections.main-collection-banner.settings.show_collection_description.label |
| `show_collection_image` | `checkbox` | t:sections.main-collection-banner.settings.show_collection_image.label |
| `color_scheme` | `color_scheme` | t:sections.all.colors.label |
| `show_related_links` | `checkbox` | Toon alfabetische links |
| `related_links_menu` | `link_list` | Menu voor alfabetische links |

## Blocktype category_menu

| ID | Type | Label / opties |
| --- | --- | --- |
| `source_collection` | `collection` | Voor welke collectie? |
| `cards_menu` | `link_list` | Menu voor de categorieplaatjes |
| `links_menu` | `link_list` | Menu voor de alfabetische links |

## Technische ingangen

Formtypen: —.

Letterlijke events in deze bron: —.

Letterlijke metafieldkeys: —.

DOM-hooks: —.

Geen vermelding sluit dynamische keys, externe handlers of platformwerking niet uit. Inhoud/defaults en huidige product-/contact-/settingswaarden worden niet door deze tool gepubliceerd.
