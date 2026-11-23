# bc-meubelhub

**Bron:** `sections/bc-meubelhub.liquid`. Bronstatus: BYTE_MATCH.

[Functioneel dossier](../../components/COLLECTIONS_AND_HUBS.md) · [Bronhashes](../source-index.json) · [Alle secties](../SECTIONS.md)

Dit is de bronreferentie. Het dossier geeft de bedoeling, data-eigenaar, toestanden en onderhoudsgrenzen.

## Koppelingen

Letterlijke callers: `templates/collection.bc-meubelhub.json`.

Letterlijke uitgaande refs: `assets/bc-meubelhub.css`, `assets/bc-meubelhub.js`, `snippets/bc-meubelhub-icon.liquid`.

Geen caller gevonden betekent niet ongebruikt: Theme Editor, platformsections en dynamische aanroepen vallen buiten deze parser.

## Schema-instellingen

| ID | Type | Label / opties |
| --- | --- | --- |
| `heading` | `text` | Paginatitel (leeg = collectietitel) |
| `eyebrow` | `text` | Bovenregel |
| `intro` | `richtext` | Korte introductie |
| `hero_image` | `image_picker` | Hero afbeelding (vervangbaar) |
| `hero_url` | `url` | Hero afbeelding URL |
| `hero_alt` | `text` | Beschrijving hero afbeelding |
| `hero_usp_1` | `text` | Voordeel 1 |
| `hero_usp_2` | `text` | Voordeel 2 |
| `hero_usp_3` | `text` | Voordeel 3 |
| `shop_heading` | `text` | Titel keuzehulp |
| `type_menu` | `link_list` | Menu: op type |
| `maat_menu` | `link_list` | Menu: op maat |
| `stijl_menu` | `link_list` | Menu: op stijl |
| `merk_menu` | `link_list` | Menu: op merk |
| `show_pending` | `checkbox` | Toon niet-klikbare maat/stijlvoorbeelden tot menu’s gekoppeld zijn |
| `show_brands` | `checkbox` | Merkenblok tonen |
| `brands_heading` | `text` | Titel merkenblok |
| `brands_intro` | `text` | Ondertitel merkenblok |
| `brands_url` | `url` | Bestemming Alle merken (optioneel) |
| `inspiration_image` | `image_picker` | Inspiratieafbeelding (vervangbaar) |
| `inspiration_url` | `url` | Inspiratieafbeelding URL |
| `inspiration_link` | `url` | Stijlenpagina (leeg = keuzeadvies op deze pagina) |
| `service_title_1` | `text` | Servicetitel 1 |
| `service_text_1` | `text` | Serviceuitleg 1 |
| `service_title_2` | `text` | Servicetitel 2 |
| `service_text_2` | `text` | Serviceuitleg 2 |
| `service_title_3` | `text` | Servicetitel 3 |
| `service_text_3` | `text` | Serviceuitleg 3 |
| `service_title_4` | `text` | Servicetitel 4 |
| `service_text_4` | `text` | Serviceuitleg 4 |
| `advice_fallback` | `richtext` | Advies als [SPLIT]-tekst ontbreekt |

## Blocktype category

| ID | Type | Label / opties |
| --- | --- | --- |
| `category` | `collection` | Bestaande collectie |
| `label` | `text` | Titel |
| `caption` | `text` | Korte ondertitel |
| `photo` | `image_picker` | Afbeelding (vervangbaar) |
| `photo_url` | `url` | Afbeelding URL |
| `photo_alt` | `text` | Afbeeldingbeschrijving |
| `allow_empty` | `checkbox` | Lege collectie toch klikbaar (alleen zinvolle navigatiepagina’s) |

## Blocktype brand

| ID | Type | Label / opties |
| --- | --- | --- |
| `label` | `text` | Merknaam |
| `destination` | `url` | Bestaande merkselectie |
| `logo` | `image_picker` | Officieel merklogo |

## Technische ingangen

Formtypen: —.

Letterlijke events in deze bron: —.

Letterlijke metafieldkeys: —.

DOM-hooks: —.

Geen vermelding sluit dynamische keys, externe handlers of platformwerking niet uit. Inhoud/defaults en huidige product-/contact-/settingswaarden worden niet door deze tool gepubliceerd.
