# bc-sunshower-landing

**Bron:** `sections/bc-sunshower-landing.liquid`. Bronstatus: BYTE_MATCH.

[Functioneel dossier](../../components/PRODUCT_PAGES.md) · [Bronhashes](../source-index.json) · [Alle secties](../SECTIONS.md)

Dit is de bronreferentie. Het dossier geeft de bedoeling, data-eigenaar, toestanden en onderhoudsgrenzen.

## Koppelingen

Letterlijke callers: `templates/page.bc-sunshower.json`.

Letterlijke uitgaande refs: `assets/bc-sunshower-landing.css`, `assets/bc-sunshower-mobile.js`, `assets/bc-sunshower-shop.js`, `snippets/bc-sunshower-shop-card.liquid`.

Geen caller gevonden betekent niet ongebruikt: Theme Editor, platformsections en dynamische aanroepen vallen buiten deze parser.

## Schema-instellingen

| ID | Type | Label / opties |
| --- | --- | --- |
| `hero_image` | `image_picker` | t:ss_experience.settings.hero_image |
| `hero_mobile_image` | `image_picker` | t:ss_experience.settings.hero_mobile_image |
| `configurator_url` | `url` | t:ss_experience.settings.configurator_url |
| `one_product` | `product` | t:ss_experience.settings.one_product |
| `plus_product` | `product` | t:ss_experience.settings.plus_product |
| `one_image` | `image_picker` | t:ss_experience.settings.one_image |
| `plus_image` | `image_picker` | t:ss_experience.settings.plus_image |
| `installation_image` | `image_picker` | t:ss_experience.settings.installation_image |
| `inbouw_image` | `image_picker` | t:ss_experience.settings.inbouw_image |
| `opbouw_image` | `image_picker` | t:ss_experience.settings.opbouw_image |
| `advice_url` | `url` | t:ss_experience.settings.advice_url |

## Blocktype accessory

| ID | Type | Label / opties |
| --- | --- | --- |
| `kind` | `select` | t:ss_experience.accessory.kind: cleaning: t:ss_experience.accessory.cleaning; seat: t:ss_experience.accessory.seat; wiper: t:ss_experience.accessory.wiper |
| `product` | `product` | t:ss_experience.accessory.product |
| `image_override` | `image_picker` | t:ss_experience.accessory.image_override |
| `product_white` | `product` | t:ss_experience.accessory.product_white |
| `product_black` | `product` | t:ss_experience.accessory.product_black |
| `product_grey` | `product` | t:ss_experience.accessory.product_grey |
| `product_sand` | `product` | t:ss_experience.accessory.product_sand |

## Technische ingangen

Formtypen: —.

Letterlijke events in deze bron: —.

Letterlijke metafieldkeys: —.

DOM-hooks: `data-bcsse-configurator-url`, `data-bcsse-section-id`, `data-bcsse-uv-url`.

Geen vermelding sluit dynamische keys, externe handlers of platformwerking niet uit. Inhoud/defaults en huidige product-/contact-/settingswaarden worden niet door deze tool gepubliceerd.
