# BadkamerCity: vaste basis voor het homepage-redesign

## Vastgelegde oorspronkelijke versie

- Project: `C:\Projects\badkamercity-shopify-current`
- Branch voor vervolgwerk: `homepage-redesign-top3`
- Baseline-commit: `6e7d803d4d145bcc9175b29ee1ac7572d6dd29e2`
- Baseline-commitbericht: `Baseline before homepage redesign`
- ZIP-back-up, gemaakt voordat Git of beveiligingsbestanden werden toegevoegd:
  `C:\Projects\badkamercity-shopify-backups\badkamercity-before-homepage-redesign-20261005-024025.zip`
- Back-up gemaakt op 5 oktober 2026, 02:40:25 (Europe/Berlin).
- SHA-256 van de ZIP: `05fab0b7cf799ad639027089235a3e97fdf2208acaf92e5949e8346e29a6e589`
- Alle 396 oorspronkelijke bestanden zijn byte voor byte tegen de ZIP gecontroleerd.
- De lokale Git-instelling `core.autocrlf=false` voorkomt automatische conversie van regeleindes bij staging. Globale Git-instellingen zijn niet gewijzigd.

Deze exacte lokale versie is de vaste basis. De voorbereiding verandert geen webshopcode.

## ABSOLUUT BESCHERMD

Deze bestanden mogen tijdens het homepage-redesign NIET gewijzigd, verwijderd of hernoemd worden:

- `layout/theme.liquid`
- `sections/header-group.json`
- `sections/header.liquid`
- `snippets/header-drawer.liquid`
- `snippets/header-search.liquid`
- `snippets/header-dropdown-menu.liquid`
- `snippets/header-mega-menu.liquid`
- `assets/component-list-menu.css`
- `assets/component-menu-drawer.css`
- `assets/component-mega-menu.css`
- `assets/component-search.css`
- `assets/base.css`
- `sections/footer.liquid`
- `sections/footer-group.json`
- `snippets/bc-category-icon.liquid`

Het gedeelde snippet `snippets/bc-category-icon.liquid` wordt ook door de navigatie gebruikt. Wijzig dit snippet NIET.

Ook de bestaande USP-code blijft beschermd, ook waar deze momenteel niet op de homepage wordt ingeladen:

- `sections/announcement-bar.liquid`
- `sections/usps.liquid`
- `snippets/bc-search-usp-strip.liquid`

Voor behoud van de footer zijn de volgende bestaande afhankelijkheden eveneens beschermd:

- `assets/section-footer.css`
- `assets/component-newsletter.css`
- `assets/component-list-payment.css`
- `assets/component-list-social.css`
- `snippets/social-icons.liquid`
- `snippets/country-localization.liquid`
- `snippets/language-localization.liquid`
- `assets/component-localization-form.css`
- `assets/localization-form.js`
- `assets/icon-truck.svg`
- `assets/icon-return.svg`
- `assets/icon-success.svg`
- `assets/icon-star.svg`
- `assets/icon-error.svg`
- `assets/icon-facebook.svg`
- `assets/icon-instagram.svg`
- `assets/icon-youtube.svg`
- `assets/icon-tiktok.svg`
- `assets/icon-twitter.svg`
- `assets/icon-pinterest.svg`
- `assets/icon-snapchat.svg`
- `assets/icon-tumblr.svg`
- `assets/icon-vimeo.svg`
- `assets/icon-caret.svg`
- `assets/icon-checkmark.svg`
- `assets/icon-reset.svg`
- `assets/icon-search.svg`
- `assets/icon-close.svg`

De SHA-256-controle omvat alle bovenstaande bestanden.

## Regels voor iedere vervolgopdracht

- Werk uitsluitend aan de gevraagde homepage-content onder de bestaande header.
- Wijzig de header, navigatie, bovenste USP-balk en footer niet.
- Wijzig productpagina's, collectiepagina's en de bestaande categorieboom niet.
- Verwijder geen bestaande functionaliteit.
- Wijzig alleen bestanden die nodig zijn voor de concrete vervolgopdracht.
- Gebruik geen globale CSS-wijzigingen. Geef nieuwe homepage-CSS een eigen namespace en begrens selectors tot de homepage-sectie.
- Behoud Shopify Liquid-functionaliteit, theme-editorinstellingen en dynamische data.
- Hardcode geen productprijzen of productgegevens die uit Shopify kunnen komen.
- Gebruik geen nep-reviews of verzonnen klantenaantallen. Neem bestaande claims niet zonder onderbouwing over in nieuwe homepage-content.
- Zorg voor desktop, tablet en mobiel; houd JavaScript minimaal en let op performance, lazy loading en accessibility.
- Controleer de beschermde bestanden met `HOMEPAGE_PROTECTED_FILES.sha256` voor en na iedere latere opdracht en rapporteer het resultaat.
- Wijzig het checksum-bestand niet om een afwijking te accepteren. Het bevat de originele hashes uit de ZIP-back-up.
- Stop bij een afwijking aan een beschermd bestand en onderzoek die voordat vervolgwerk wordt uitgevoerd. Neem geen bestaande wijzigingen van anderen weg.
- Controleer iedere diff vóór een commit. Commit uitsluitend de bestanden die bij de opdracht horen.
- Voer in deze voorbereidingsopdracht geen `shopify theme push`, publish of live theme-wijzigingen uit.
- Start na deze voorbereiding pas met redesignwerk na de volgende gebruikersopdracht.

## Homepage-baseline

`templates/index.json` bevat vijf ingeschakelde secties in onderstaande volgorde:

| Volgorde | Sectie-ID | Type | Liquid-bestand |
| --- | --- | --- | --- |
| 1 | `home_hero_gDkwi8` | `home-hero` | `sections/home-hero.liquid` |
| 2 | `home_category_grid_FgNMtn` | `home-category-grid` | `sections/home-category-grid.liquid` |
| 3 | `home_shop_by_style_BK9a6q` | `home-shop-by-style` | `sections/home-shop-by-style.liquid` |
| 4 | `home_mijn_badkamercity_3wELah` | `home-mijn-badkamercity` | `sections/home-mijn-badkamercity.liquid` |
| 5 | `home_brand_rail_aUrAmK` | `home-brand-rail` | `sections/home-brand-rail.liquid` |

Header en footer worden buiten deze lijst geladen via `layout/theme.liquid`.
De header en het homepage-categoriegrid gebruiken beide het Shopify-menu `main-menu`; wijzig dat menu of de categorieboom niet.
De Shopify-commentaarheader van `index.json` hoort bij het oorspronkelijke bestand. Verwijder die alleen in het geheugen bij het parsen voor een controle.

## Controle van beschermde bestanden

Voer dit PowerShell-fragment uit vanuit de projectroot. Ontbrekende bestanden of gewijzigde bytes laten de controle falen:

```powershell
$ErrorActionPreference = 'Stop'
$expectedProjectPath = 'C:\Projects\badkamercity-shopify-current'
if (-not [string]::Equals((Get-Location).ProviderPath, $expectedProjectPath, [StringComparison]::OrdinalIgnoreCase)) {
    throw 'De controle moet vanuit de vaste projectroot worden uitgevoerd.'
}
$protectedCount = 0
foreach ($hashLine in Get-Content -LiteralPath 'HOMEPAGE_PROTECTED_FILES.sha256') {
    if ($hashLine -notmatch '^([0-9a-f]{64})  (.+)$') {
        throw "Ongeldige checksumregel: $hashLine"
    }
    $expectedDigest = $Matches[1]
    $protectedRelativePath = $Matches[2]
    $actualDigest = (Get-FileHash -LiteralPath $protectedRelativePath -Algorithm SHA256).Hash.ToLowerInvariant()
    if ($actualDigest -ne $expectedDigest) {
        throw "Beschermd bestand gewijzigd: $protectedRelativePath"
    }
    $protectedCount++
}
if ($protectedCount -ne 46) { throw "Onverwacht aantal beschermde bestanden: $protectedCount" }
Write-Output "PASS: alle $protectedCount beschermde bestanden zijn byte voor byte ongewijzigd."
```

## Theme-check van de oorspronkelijke versie

- Uitgevoerd: `shopify theme check --path C:\Projects\badkamercity-shopify-current --output json --no-color`
- Geen automatische correcties uitgevoerd.
- Exitcode: `1`; 2 bestaande fouten en 19 waarschuwingen in 16 bestanden.
- Beide fouten zijn `ValidSchemaTranslations` in `sections/featured-product.liquid`, regels 743 en 744.
- Ontbrekende sleutels in `locales/en.default.schema.json`:
  `t:sections.main-product.blocks.icon_with_text.settings.content.label` en
  `t:sections.main-product.blocks.icon_with_text.settings.content.info`.
- De homepage heeft een waarschuwing voor 47 instellingen in `sections/home-hero.liquid` (`ExcessiveSettingsCount`).
- Deze bestaande meldingen zijn vastgelegd en niet gerepareerd in de voorbereiding.
- Volledig rapport buiten de projectmap:
  `C:\Projects\badkamercity-shopify-backups\badkamercity-theme-check-20261005-024025.json`.

Git-metadata blijft in `.git`; de tweede commit bevat uitsluitend dit regelsbestand en het checksum-overzicht.
