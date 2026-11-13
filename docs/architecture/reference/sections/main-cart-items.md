# main-cart-items

**Bron:** `sections/main-cart-items.liquid`. Bronstatus: BYTE_MATCH.

[Functioneel dossier](../../components/CART_AND_FEEDBACK.md) · [Bronhashes](../source-index.json) · [Alle secties](../SECTIONS.md)

Dit is de bronreferentie. Het dossier geeft de bedoeling, data-eigenaar, toestanden en onderhoudsgrenzen.

## Koppelingen

Letterlijke callers: `templates/cart.bc-mobile.liquid`, `templates/cart.json`.

Letterlijke uitgaande refs: `assets/bc-cart-page.css`, `assets/cart.js`, `assets/component-cart-items.css`, `assets/component-cart.css`, `assets/component-discounts.css`, `assets/component-totals.css`, `assets/icon-close.svg`, `assets/icon-discount.svg`, `assets/icon-error.svg`, `assets/icon-info.svg`, `assets/icon-minus.svg`, `assets/icon-plus.svg`, `assets/icon-remove.svg`, `assets/quantity-popover.css`, `assets/quantity-popover.js`, `snippets/bc-cart-delivery.liquid`, `snippets/loading-spinner.liquid`, `snippets/unit-price.liquid`.

Geen caller gevonden betekent niet ongebruikt: Theme Editor, platformsections en dynamische aanroepen vallen buiten deze parser.

## Schema-instellingen

| ID | Type | Label / opties |
| --- | --- | --- |
| `quote_email` | `text` | E-mailadres voor offerteaanvragen |
| `color_scheme` | `color_scheme` | t:sections.all.colors.label |
| `padding_top` | `range` | t:sections.all.padding.padding_top |
| `padding_bottom` | `range` | t:sections.all.padding.padding_bottom |

## Technische ingangen

Formtypen: —.

Letterlijke events in deze bron: —.

Letterlijke metafieldkeys: —.

DOM-hooks: `data-cart-quantity`, `data-currency`, `data-id`, `data-index`, `data-locale`, `data-min`, `data-per-item`, `data-quantity-variant-id`, `data-quote-email`, `data-quote-error`, `data-quote-intro`, `data-quote-subject`, `data-restore-error`, `data-restoring`, `data-save-error`, `data-saved`.

Geen vermelding sluit dynamische keys, externe handlers of platformwerking niet uit. Inhoud/defaults en huidige product-/contact-/settingswaarden worden niet door deze tool gepubliceerd.
