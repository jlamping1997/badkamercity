# main-category-landing

**Bron:** `sections/main-category-landing.liquid`. Bronstatus: BYTE_MATCH.

[Functioneel dossier](../../components/COLLECTIONS_AND_HUBS.md) · [Bronhashes](../source-index.json) · [Alle secties](../SECTIONS.md)

Dit is de bronreferentie. Het dossier geeft de bedoeling, data-eigenaar, toestanden en onderhoudsgrenzen.

## Koppelingen

Letterlijke callers: `templates/collection.category-landing.json`.

Letterlijke uitgaande refs: `assets/bc-category-directory.css`, `assets/bc-collection.css`, `assets/component-bc-category-navigation.css`, `assets/component-card.css`, `assets/template-collection.css`, `snippets/bc-category-breadcrumbs.liquid`, `snippets/bc-category-children.liquid`, `snippets/bc-category-link-index.liquid`, `snippets/bc-collection-intro.liquid`, `snippets/card-product.liquid`.

Geen caller gevonden betekent niet ongebruikt: Theme Editor, platformsections en dynamische aanroepen vallen buiten deze parser.

## Schema-instellingen

| ID | Type | Label / opties |
| --- | --- | --- |
| `navigation_menu` | `link_list` | Menu voor de categorieboom |
| `subcategory_source` | `select` | Bron voor subcategorieën: menu: Huidige categorieboom uit menu; manual: Handmatige blokken |
| `color_scheme` | `color_scheme` | Kleurschema |
| `show_collection_title` | `checkbox` | Toon collectietitel |
| `show_collection_description` | `checkbox` | Toon collectieomschrijving |
| `show_seo_content` | `checkbox` | Toon SEO content met split |
| `seo_content` | `richtext` | SEO content |
| `show_extra_content` | `checkbox` | Toon extra contentblok |
| `extra_text_title` | `text` | Titel extra content |
| `extra_text_content` | `richtext` | Extra content |
| `show_subcategory_grid` | `checkbox` | Toon subcategorie-overzicht |
| `subcategory_grid_heading` | `text` | Titel subcategorie-overzicht |
| `subcategory_grid_columns_desktop` | `range` | Kolommen desktop |
| `subcategory_image_ratio` | `select` | Beeldverhouding subcategorie-afbeelding: adapt: Aangepast aan afbeelding; square: Vierkant; landscape: Liggend; portrait: Staand |
| `show_related_links` | `checkbox` | Toon gerelateerde links |
| `related_links_heading` | `text` | Titel gerelateerde links |
| `related_links_columns_desktop` | `range` | Kolommen gerelateerde links desktop |
| `show_advice_bar` | `checkbox` | Toon adviesbalk boven onderste SEO-tekst |
| `advice_bar_title` | `text` | Titel adviesbalk |
| `show_product_grid` | `checkbox` | Toon productgrid onder subcategorieën |
| `product_grid_heading` | `text` | Titel productgrid |
| `product_grid_intro` | `richtext` | Intro productgrid |
| `max_products` | `range` | Maximaal aantal producten |
| `product_grid_columns_desktop` | `range` | Kolommen productgrid desktop |
| `product_image_ratio` | `select` | Beeldverhouding productafbeelding: adapt: Aangepast aan afbeelding; square: Vierkant; portrait: Staand |
| `padding_top` | `range` | Padding boven |
| `padding_bottom` | `range` | Padding onder |
| `show_subcategory_heading` | `checkbox` | Toon titel boven de categorieplaatjes |
| `show_advice_link` | `checkbox` | Toon link naar het keuzeadvies |
| `related_links_menu` | `link_list` | Algemeen menu voor alfabetische links |

## Blocktype subcategory

| ID | Type | Label / opties |
| --- | --- | --- |
| `block_title` | `text` | Titel |
| `block_image` | `image_picker` | Afbeelding |
| `block_link` | `url` | Link |
| `block_description` | `textarea` | Korte omschrijving |

## Blocktype related_group

| ID | Type | Label / opties |
| --- | --- | --- |
| `group_label` | `text` | Label |
| `group_menu` | `link_list` | Menu |

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
