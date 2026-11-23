# Statische code-inventarisatie

Bron: `shopify-MAIN-195818389770-15-files`. Dekking: **partial_sample**.

Bestanden: **15**. Gevonden statische verwijzingen: **149**.

Dit is een gegenereerde zoekkaart, geen vrijgave of lijst met bewezen defects.

## Grenzen

- Static candidates only: no runtime, visual, accessibility, security or commercial correctness certification.
- Liquid references and JSON section types only; dynamic Liquid, JS imports, CSS URLs, app blocks and implicit layout execution are not fully resolved.
- No-reference and identical-byte groups do not prove unused code or justify removal.
- Coverage and source label are declared by the operator; hashes establish only scanned-file equality.

## Vergelijking met live manifest

| Categorie | Aantal |
| --- | ---: |
| equal | 15 |
| different | 0 |
| live_only | 1247 |
| scan_only | 0 |

## Ingangen per bestand

| Bestand | Type | Regels | Uitgaande verwijzingen |
| --- | --- | ---: | ---: |
| `assets/bc-cart-page.js` | theme_source | 336 | 0 |
| `assets/bc-external-filters.js` | theme_source | 947 | 0 |
| `assets/bc-product-switcher.js` | theme_source | 769 | 0 |
| `assets/bc-sunshower-page.css` | theme_source | 327 | 0 |
| `assets/bc-sunshower-page.js` | theme_source | 389 | 0 |
| `assets/bc-sunshower-shop.js` | theme_source | 344 | 0 |
| `layout/theme.liquid` | theme_source | 384 | 28 |
| `sections/main-product.liquid` | theme_source | 2891 | 69 |
| `sections/main-sunshower.liquid` | theme_source | 139 | 18 |
| `snippets/bc-card-product-search.liquid` | theme_source | 140 | 4 |
| `snippets/bc-external-filters.liquid` | theme_source | 39 | 2 |
| `snippets/bc-product-switcher.liquid` | theme_source | 63 | 2 |
| `snippets/card-product.liquid` | theme_source | 627 | 23 |
| `snippets/cart-notification.liquid` | theme_source | 23 | 2 |
| `templates/product.sunshower.json` | theme_source | 20 | 1 |

Volledige paden, hashes, afhankelijkheden en signalen staan in `inventory.json`.
