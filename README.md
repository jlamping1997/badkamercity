# BadkamerCity — Shopify Online Store 2.0

Deze Git-repository bevat de **theme-code** van BadkamerCity (Liquid, JSON-templates, CSS, JavaScript), plus een gecontroleerde technische overdracht. **De complete Shopify-catalogus, menu's, Admin-productwaarden en externe VPS/backend zitten niet in de Git-theme-code.**

## Neem je het project over? Begin hier.

**[HANDOVER_START_HERE.md](docs/HANDOVER_START_HERE.md)** — in 15 minuten begrijpen wat live staat en waar je veilig kunt beginnen.

Daarna, afhankelijk van je taak:

| Document | Doel |
| --- | --- |
| [AI_HANDOFF_CURRENT.md](docs/AI_HANDOFF_CURRENT.md) | Architectuur, werking, productpagina's, homepage, SEO, filters en uitzonderingen |
| [LIVE_STATUS_AND_NEXT_STEPS.md](docs/LIVE_STATUS_AND_NEXT_STEPS.md) | Wat bewezen live is, wat test-only/unknown is en werkprioriteiten |
| [THEME_COMPONENT_REFERENCE.md](docs/THEME_COMPONENT_REFERENCE.md) | Per sectie alle instellingen/blocktypen en Liquid-/asset-afhankelijkheden |
| [THEME_CODE_MAP_2026-10-07.json](docs/THEME_CODE_MAP_2026-10-07.json) | Machineleesbare dependencykaart van alle 441 Shopify-theme-bestanden |
| [SHOPIFY_ADMIN_STRUCTURE_2026-10-07.json](docs/SHOPIFY_ADMIN_STRUCTURE_2026-10-07.json) | Read-only momentopname van 204 collecties, 9 menu's en metafielddefinities |
| [PRODUCT_METAFIELD_MAPPING_AUDIT.md](docs/PRODUCT_METAFIELD_MAPPING_AUDIT.md) | Waar productvelden in code en Admin van elkaar kunnen afwijken |
| [OPERATIONAL_RUNBOOK.md](docs/OPERATIONAL_RUNBOOK.md) | Dagstart, Git synchroniseren, conceptthema, terugzetten en veilig opleveren |
| [TROUBLESHOOTING.md](docs/TROUBLESHOOTING.md) | Symptoom → controle → code/Admin-locatie → herstelroute |
| [RELEASE_AND_QA.md](docs/RELEASE_AND_QA.md) | Regressietesten, SEO, responsive, commerce, review, rollback |
| [WORKED_EXAMPLES_AND_HANDOFF_TEST.md](docs/WORKED_EXAMPLES_AND_HANDOFF_TEST.md) | Negen praktische voorbeelden en een concrete overnametest |
| [SYSTEM_OWNERSHIP_AND_GAPS.md](docs/SYSTEM_OWNERSHIP_AND_GAPS.md) | Wat buiten Git blijft en welke toegang/bronnen echt overgedragen moeten worden |
| [HANDOFF_CHANGELOG.md](docs/HANDOFF_CHANGELOG.md) | Datum, bewijs en scope van de uitgebreide overdracht | 
| [BASELINE_MANIFEST_2026-10-07.json](docs/BASELINE_MANIFEST_2026-10-07.json) | 441 bestanden met Shopify MD5/size/mediatype |
| [AGENTS.md](AGENTS.md) | Verplichte AI/Codex veiligheids- en brondocumentatie-instructies |

## Actuele snapshot

Gemeten op **7 oktober 2026**:

- Store: `fpa9hu-i3.myshopify.com`.
- Shopify MAIN theme: `BadkamerCity - SEO categoriehub`, ID `194864677130`.
- 441/441 live theme-bestanden inhoudelijk vergeleken met Git.
- Shopify Admin: 11.053 producten, 204 collecties en 9 menu's; een PRODUCT ACTIVE-status bewijst **geen** Online Store-publicatie.
- Eén speciale `bc-meubelhub`-collectie: Badkamermeubels. De mobiel goedgekeurde weergave gebruikt óók drie inline CSS-patches in de Shopify-collectieomschrijving. Een nieuwe Git-clone alléén kan dat verborgen Admin-aspect niet veranderen.
- Externe filters zijn een **opt-in-proef** op `wastafelkranen?bcfilters=1`, niet de standaard filterervaring.

Dit zijn gedateerde feiten, **geen permanente garantie**; begin elk werk met live Theme-role/Git-status opnieuw lezen.

## Projectveiligheid

- Verander alleen expliciet bedoelde code in een ongepubliceerd Shopify-conceptthema. De merchant publiceert na review.
- Geen destructieve Git-commando's om een werkmap “schoon” te maken; controleer/stash bestaande wijzigingen bewust.
- Voor productdata en imports: Shopify Admin + officiële bron, geen aannames vanuit titels.
- Geen geheimen, leveranciercontracten, persoonsgegevens, orders of betalingsgegevens in deze publieke repo.
- Historisch `docs/MASTERPLAN.md` (september 2026) blijft leesbaar als besluitgeschiedenis, maar bevat verouderde theme-ID's en projectstatussen. Gebruik de actuele handoff voor feitelijke huidige toestand.

### Werkplekinspectie

~~~powershell
git status --short
git branch --show-current
git remote -v
shopify theme list --store fpa9hu-i3.myshopify.com
~~~

**Eerst lezen → dan meten → dan een kleine veilige wijziging in draft → testen → review → publicatie door de eigenaar → documentatie vernieuwen.**
