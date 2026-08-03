# Live Theme Comparison

Datum: 2026-08-03  
Lokale repository: `CITY_MASTER`  
Tijdelijke live-download: `C:\Users\LauraHarrySuiker\OneDrive - Harry Suiker\Bureaublad\CITY_LIVE_COMPARE_20260803`  
Store: `fpa9hu-i3.myshopify.com`  
Live theme: `Categoriepagina_v1.0`  
Live theme ID: `189463068938`

## Randvoorwaarden

- Geen theme-code gewijzigd.
- Niets naar Shopify gepusht.
- Niets gepubliceerd.
- Het live theme is niet over `CITY_MASTER` heen getrokken.
- De live theme-code is gedownload naar een aparte tijdelijke map buiten `CITY_MASTER`.
- Dit vergelijkingsrapport is nog niet gecommit.

## Uitgevoerde stappen

Stap 1 is uitgevoerd:

- Gecommit: `docs/SHOPIFY_ENVIRONMENT.md`
- Commitbericht: `docs: document Shopify environment`
- Commit hash: `ff8ceaf`
- Gepusht naar huidige GitHub-branch: `main`

Stap 2 is uitgevoerd:

```text
shopify theme pull --store fpa9hu-i3.myshopify.com --theme 189463068938 --path "C:\Users\LauraHarrySuiker\OneDrive - Harry Suiker\Bureaublad\CITY_LIVE_COMPARE_20260803" --nodelete --no-color
```

Daarna zijn alleen deze Shopify-theme-mappen vergeleken:

- `assets`
- `config`
- `layout`
- `locales`
- `sections`
- `snippets`
- `templates`

Genegeerd:

- `.git`
- `docs`
- andere bestanden of mappen buiten de Shopify-theme-mappen

## Vergelijkingsmethode

Voor beide locaties is per bestand binnen de zeven theme-mappen een relatieve padlijst gemaakt. Daarna is per bestand een SHA-256 hash berekend en vergeleken.

## Samenvatting

```text
LocalFileCount : 396
LiveFileCount  : 396
LocalOnlyCount : 0
LiveOnlyCount  : 0
DifferingCount : 0
```

## 1. Is de lokale theme-code gelijk aan het live theme?

Ja. Binnen de vergeleken Shopify-theme-mappen is de lokale theme-code gelijk aan het live Shopify-theme `Categoriepagina_v1.0` met ID `189463068938`.

Er zijn geen ontbrekende bestanden en geen inhoudelijke verschillen gevonden.

## 2. Bestanden die alleen lokaal bestaan

Geen.

## 3. Bestanden die alleen live bestaan

Geen.

## 4. Bestanden die inhoudelijk verschillen

Geen.

## 5. Kan `CITY_MASTER` veilig als uitgangssituatie gebruikt worden?

Ja, voor de Shopify theme-code kan `CITY_MASTER` veilig als uitgangssituatie worden gebruikt.

De lokale bestanden in `assets`, `config`, `layout`, `locales`, `sections`, `snippets` en `templates` zijn gelijk aan het live theme. Daarmee is de lokale codebasis een correcte technische snapshot van het live theme op het moment van deze vergelijking.

Belangrijke nuance: dit bewijst alleen gelijkheid van theme-bestanden. Het zegt niets over externe Shopify-data zoals producten, collecties, metafield-definities, metaobjects, menus, markets, apps, shop settings of content die niet als theme-bestand in deze mappen staat.

## 6. Aanbevolen vervolgstap

Gebruik `CITY_MASTER` als technische basis, maar ontwikkel niet direct tegen live.

Aanbevolen volgorde:

1. Commit dit vergelijkingsrapport apart wanneer akkoord.
2. Richt een development of unpublished Shopify theme in voor toekomstige wijzigingen.
3. Documenteer de externe afhankelijkheden: metafields, product switcher databron, menus, collecties en actieve apps.
4. Voer toekomstige wijzigingen via GitHub en een Shopify preview/development theme uit, niet rechtstreeks op het live theme.

## Aangemaakte of gewijzigde bestanden in `CITY_MASTER`

- Aangemaakt: `docs/LIVE_THEME_COMPARISON.md`

