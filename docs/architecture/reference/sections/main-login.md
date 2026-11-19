# main-login

**Bron:** `sections/main-login.liquid`. Bronstatus: BYTE_MATCH.

[Functioneel dossier](../../components/ACCOUNTS_AND_SYSTEM_PAGES.md) · [Bronhashes](../source-index.json) · [Alle secties](../SECTIONS.md)

Dit is de bronreferentie. Het dossier geeft de bedoeling, data-eigenaar, toestanden en onderhoudsgrenzen.

## Koppelingen

Letterlijke callers: `templates/customers/login.json`.

Letterlijke uitgaande refs: `assets/customer.css`, `assets/icon-error.svg`, `assets/icon-success.svg`.

Geen caller gevonden betekent niet ongebruikt: Theme Editor, platformsections en dynamische aanroepen vallen buiten deze parser.

## Schema-instellingen

| ID | Type | Label / opties |
| --- | --- | --- |
| `enable_shop_login_button` | `checkbox` | t:sections.main-login.shop_login_button.enable |
| `padding_top` | `range` | t:sections.all.padding.padding_top |
| `padding_bottom` | `range` | t:sections.all.padding.padding_bottom |

## Technische ingangen

Formtypen: `customer_login`, `guest_login`, `recover_customer_password`.

Letterlijke events in deze bron: —.

Letterlijke metafieldkeys: —.

DOM-hooks: —.

Geen vermelding sluit dynamische keys, externe handlers of platformwerking niet uit. Inhoud/defaults en huidige product-/contact-/settingswaarden worden niet door deze tool gepubliceerd.
