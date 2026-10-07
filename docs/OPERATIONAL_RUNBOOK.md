# BadkamerCity — operationeel runbook

**Bronstand:** 7 oktober 2026. Dit is een werkhandleiding voor een nieuwe beheerder. Shopify MAIN op dit meetmoment: `BadkamerCity - SEO categoriehub`, ID `194864677130`. Controleer de actuele MAIN-ID altijd opnieuw. Git en Shopify zijn verschillende systemen. Publiceren doet alleen de bevoegde merchant.

## 1. Starten op een bestaande Windows-werkplek

~~~powershell
cd C:\Projects\badkamercity-shopify-current
git rev-parse --show-toplevel
git remote -v
git branch --show-current
git status --short
git log -1 --oneline
git --version
node --version
shopify version
shopify theme list --store fpa9hu-i3.myshopify.com
~~~

Een lege `git status --short` betekent lokaal schoon. Als de branch `main` is en de origin correct is:

~~~powershell
git fetch origin
git pull --ff-only origin main
git status --porcelain=v1
~~~

**Stop als `git status` bestanden noemt.** Lees `git diff` en controleer untracked bestanden. Maak bewust een checkpointcommit of stash. Geen `git reset --hard`, `git clean -fd`, blind overschrijven of force-push. Het script `scripts/git-align-worktree.ps1` is bedoeld om deze procedure voorzichtig te ondersteunen, maar is in deze documentatieronde niet lokaal uitgevoerd.

Nieuwe, lege pc: installeer Git, Node.js, Shopify CLI en een browser. Clone `https://github.com/jlamping1997/badkamercity` uitsluitend naar een lege map. Maak geen clone over bestaand werk. Volg bij `shopify theme list` de interactieve Shopify-authenticatie. Tokens nooit delen of committen.

## 2. Waar moet een wijziging worden gemaakt?

| Vraag | Begin in code | Ook controleren |
| --- | --- | --- |
| Homepage banners | `templates/index.json` en `sections/home-hero.liquid` | Theme Editor en Shopify Files |
| Header of mobiele drawer | `sections/header.liquid` | Shopify `main-menu` |
| Footer | `sections/footer.liquid` | Footer-menu en blokinstellingen |
| Badkamermeubels | `sections/bc-meubelhub.liquid`, `assets/bc-meubelhub.css` | Collectieomschrijving met 3 custom CSS-patches |
| Andere hoofdcategorie | `collection.category-landing.json`, `main-category-landing.liquid` | Collection suffix en menu's |
| Productlisting | `collection.json`, `main-collection-product-grid.liquid` | Search & Discovery en productstatus |
| Productpagina | `product.json`, `main-product.liquid` | Variant/SKU, prijs, metafields |
| Productkeuzemenu | `bc-product-switcher.js` en switcher-JSON | `custom.switch_group` en bestaande product-URLs |
| Productdetails ontbreken | `bc-product-detail-specs.liquid` | Metafield mapping-audit en echte waarden |
| Set/accessoire-koppeling | `bc-product-set-data.liquid`, `bc-product-accessories-data.liquid` | Exacte SKU en compatibiliteit |
| Externe filters | `bc-external-filters.js` | VPS, API/CORS/index; proefmodus |
| SEO title, handle of content | Vaak Shopify Admin, niet CSS | Meta/canonical/redirects/indexatie |
| BTW, verzendkosten, checkout | Shopify Admin | Theme-code is geen financieel bronsysteem |

Gebruik `THEME_COMPONENT_REFERENCE.md` voor de exacte setting-ID's/blokken en `THEME_CODE_MAP_2026-10-07.json` voor alle statische bronverwijzingen.

## 3. Veilig nieuwe themacode opleveren

**Fase A:** Controleer actuele Git-HEAD, Shopify MAIN, betrokken paginatype, alle afhankelijke bestanden en Admin-instellingen. Noteer verwachte werking, niet-te-veranderen gedrag, testvensters en rollback. Maak een featurebranch vanaf schone `main`.

**Fase B:** Dupliceer via Shopify Admin het actuele MAIN-thema of kies een bewezen identieke `UNPUBLISHED`-kopie. Test dat de draft huidige instellingen en templates bevat. Push ALLEEN gekozen bestanden naar deze ongepubliceerde kopie:

~~~powershell
# 123456789012 is een VOORBEELD, vervang door het echte UNPUBLISHED-ID.
shopify theme push --store fpa9hu-i3.myshopify.com --theme 123456789012 --only "sections/bc-meubelhub.liquid" --only "assets/bc-meubelhub.css"
~~~

**Fase C:** Theme Check uitvoeren, `git diff --check`, mobiele en desktopvoorschouw, cart/product/data/SEO en andere regressies. Bewijs noteren met URL, viewport, commit en datum. De CLI-melding “success” alleen bewijst niet dat de juiste pagina verandert.

**Fase D:** Code review + commit + GitHub branch/PR. Alleen de merchant laat het conceptthema publiceren. Daarna opnieuw MAIN-ID, storefront-URL en regressies controleren. `collection.templateSuffix` is Shopify Admin-data: verander dit niet voordat het nieuwe template op toekomstige MAIN bestaat.

## 4. Shopify-code alleen lezen en vergelijken

~~~powershell
$store = 'fpa9hu-i3.myshopify.com'
shopify theme list --store $store
$target = Join-Path $env:TEMP ('BadkamerCity_Audit_' + (Get-Date -Format yyyyMMdd_HHmmss))
New-Item -ItemType Directory -Force -Path $target | Out-Null
# Vervang 194864677130 na controle door het actuele MAIN-ID.
shopify theme pull --store $store --theme 194864677130 --path $target --nodelete
Write-Host $target
~~~

Download naar een aparte map, nooit als eerste stap over de Git-repository. Vergelijk de zeven theme-mappen. Pas op met Shopify CRLF versus Git LF bij hashes.

## 5. Veilig herstellen

- Theme/Liquid/CSS-probleem: huidig MAIN + Git commit vastleggen, één gerichte fix op UNPUBLISHED-kopie, merchant publiceert pas na review. Niet blind terug naar een maandenoud thema met verouderde settings.
- Verkeerde collectie-template: controleer Shopify `templateSuffix` en of het doeltemplate op MAIN bestaat; herstel alleen die collectie.
- Onjuiste prijs, voorraad of import: herstel uit Shopify Admin/leveranciersbron/data-backup. Git-theme rollback verandert geen productrecords.
- Externe filters stuk: test native Shopify-route zonder `bcfilters=1` en onderzoek afzonderlijke VPS. Zet proef niet sitebreed aan.

## 6. Eindrapport voor een volgende collega

Leg vast: Git branch + commit + schone/afwijkende worktree, Shopify MAIN en draft ID, exact gewijzigde files én Admin-data, test-URLs/viewport, bewijs, wat niet getest is, externe afhankelijkheden en rollback. Bewaar geen secrets of klantgegevens in logs.

**Voor detailtests:** [RELEASE_AND_QA.md](RELEASE_AND_QA.md). **Bij problemen:** [TROUBLESHOOTING.md](TROUBLESHOOTING.md). **Huidige functies:** [AI_HANDOFF_CURRENT.md](AI_HANDOFF_CURRENT.md).
