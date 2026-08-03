# Development Theme

Datum: 2026-08-03  
Store: `fpa9hu-i3.myshopify.com`

## Resultaat

Vanuit de huidige repository is een nieuw Shopify-theme aangemaakt en geupload als unpublished theme.

- Naam: `BadkamerCity Development`
- Theme-ID: `192770375946`
- Status: `unpublished`
- Previewlink: <https://fpa9hu-i3.myshopify.com?preview_theme_id=192770375946>
- Theme Editor: <https://fpa9hu-i3.myshopify.com/admin/themes/192770375946/editor>

Het theme is niet gepubliceerd en heeft het live theme of een bestaand unpublished theme niet overschreven.

## Uitgevoerde upload

De upload is uitgevoerd met:

```text
shopify theme push --unpublished --theme "BadkamerCity Development" --store fpa9hu-i3.myshopify.com --json --no-color
```

Shopify bevestigde na de upload:

```text
id: 192770375946
name: BadkamerCity Development
role: unpublished
shop: fpa9hu-i3.myshopify.com
```

## Controle themelijst

Na de upload is `shopify theme list` uitgevoerd. De vastgestelde situatie is:

| Theme | ID | Status |
| --- | ---: | --- |
| `Categoriepagina_v1.0` | `189463068938` | `live` |
| `BadkamerCity V1.0` | `189117628682` | `unpublished` |
| `BadkamerCity Development` | `192770375946` | `unpublished` |

Daarmee is bevestigd dat:

- `Categoriepagina_v1.0` nog steeds het live theme is;
- `BadkamerCity Development` een afzonderlijk nieuw unpublished theme is;
- `BadkamerCity V1.0` niet is overschreven en unpublished is gebleven;
- geen theme is gepubliceerd of verwijderd.

## Git-status

Voorafgaand aan de Shopify-upload is alleen `docs/LIVE_THEME_COMPARISON.md` gecommit en naar de huidige GitHub-branch `main` gepusht.

- Commit: `badd5cf`
- Commitbericht: `docs: verify live theme parity`

Dit document is bewust nog niet gecommit.

## Lokale wijzigingen

- Geen theme-code gewijzigd.
- Aangemaakt: `docs/DEVELOPMENT_THEME.md`
