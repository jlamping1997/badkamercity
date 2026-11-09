# Git-broncontrole — 3 november 2026

> **Vervolg 9 november 2026 — GIT-SYNC-02:** voor de huidige bron geldt [de nieuwe volledige publicatie-/broncontrole](../../repairs/2026-11-09/published-source-sync/README.md): MAIN196368531722, 1.390 files, 1.380 gedeelde files exact na tien gerichte Git-overames. settings_data-bodyuitzondering, .shopifyignore en negen live-only files blijven beschermd. De rollen en tellingen van 3 november hieronder zijn historische nulmetingen.

Status: **CURRENT_SOURCE_CAPTURED / JEEO_LIVE_CONFIRMED / ONE_PROTECTED_API_EXCEPTION**.

Broncodecheckpoint: **d4cc4bcf360d1f91d5a6ab8270a0ad7a188f0434**. De volledige sourcecommit is opnieuw uit Git opgehaald;1366/1366bronfiles exact gelijk aan de gecontroleerde capture, nul ontbrekende paden. [Git-verificatie](git-verification.json).

## Resultaat

Actuele Shopify MAIN **196110090506 — BadkamerCity - JEE-O kleurkeuzes**. Vorig MAIN196052189450 is nu UNPUBLISHED. Alle24JEE-O-featurefiles stonden al exact op de codebranch en zijn ongewijzigd in live aangetroffen. De eerdere themapublicatieblokkade is historische uitvoeringsstatus; deze Git-taak heeft niets gepubliceerd.

De algemene Git-root liep achter. Deze volledige vergelijking vervangt de oude steekproef voor het bronmoment van deze taak:

| Controle | Aantal |
| --- | ---: |
| Live themabestanden | 1374 |
| Oude root-themabestanden | 507 |
| Root bytegelijk | 451 |
| Root afwijkend | 56 |
| Ontbrekend in root | 867 |
| Alleen in root | 0 |

## Actuele bronmap

**Gebruik shopify/current/ op branch fix/product-cards-2026-10-14.** Dit is de actuele werkbron; logische paden zoals sections/main-product.liquid horen binnen die map. De oude themamappen op repositoryniveau en gedateerde releasedossiers blijven historie. Geen bestaande rootcode verwijderd of als één blinde consolidatie overschreven.

Alle1374livepaden zijn opgehaald. De bronmap bevat1366actuelethemafiles; acht oude QA/debugbackups zijn uitsluitend in het manifest geregistreerd. Deze zijn al uitgesloten door het bestaande backupbeleid. De extra .shopifyignore is een deploybescherming en telt niet als Shopify-themafile.

1365van1366actuele bronfiles zijn bytegelijk aan Shopify. De volledige [manifestcontrole](live-theme-manifest.json) vermeldt per pad bronhash, capturehash, legacy-rootstatus en Git-locatie. De manifest-only acht backupfiles zijn geen ontbrekende actuele feature.

De codebranch draagt deze bronmap. Main blijft uitsluitend documentatie-ingang en krijgt hetzelfde dossier/manifest en de actuele overdracht. Er is geen branch aangemaakt. De quality-control-branch en overige producttrajecten zijn niet samengevoegd.

## API-uitzondering en guard

config/settings_data.json heeft in Shopify MD5 **56d82e286a3ff41931816a95b614a5cf**/8651bytes; de API-body heeft MD5 **9fd7717c3e9eb0ab55c679cc1a753361**/11923bytes. De ontvangen JSONC is opgeslagen zonder onverklaarde inhoud te reconstrueren. De oorzaak is niet vastgesteld; dit is dezelfde historische settings-pariteitsgrens.

**Geen bytegelijke settingsback-up of volledige herstelvrijgave claimen.** shopify/current/.shopifyignore sluit config/settings_data.json uit van uploads. Voor een latere overdracht/export dit ene bestand onafhankelijk opnieuw ophalen en de bronchecksum sluiten; pas daarna de guard bewust aanpassen.

templates/page.retour-aanmelden.json bevatte in de API een gegenereerde commentheader. Uitsluitend die header verwijderd; de overblijvende122bytes hebben exact de opgegeven Shopify-MD52e5141a5c097bfb87ccc21e92fa51d66. Deze oude uitzondering is daarmee voor deze broncapture gesloten.

## Meting en grenzen

- Bronmoment eindcontrole: 2026-11-03T12:28:54.707Z.
- Thema en alle1374manifestpaden voor/na capture gelijk; geen wijzigingen tijdens ophalen.
- Alle24JEE-O-featurefiles exact gelijk aan de vorige geteste implementatie.
- Alle804JSON/JSONC-files uit de actieve bron parsebaar.
- Credentialpatronen voor leveranciers-/GitHub-tokens, private sleutels en letterlijke secrets niet aangetroffen. Geen ruwe Admin-productexport, klant-, order- of leverancierscontractdata toegevoegd.
- JSON-assets zijn bestaande storefrontkeuzedata uit het Shopify-thema, geen nieuwe private catalogusexport.
- Geen .github-workflow, shopify.theme.toml of .shopifyignore in de oude root aangetroffen. Een Shopify-GitHub-binding is niet onafhankelijk bewezen; daarom de oude root niet omgezet en geen automatische deployment ingericht.
- Kopie van bestaande bron: geen nieuwe gedragswijziging. Geen nieuwe browser-, mobiele, winkelwagen-, checkout-, ranking- of performancetest geclaimd.
- Geen Windows-werkmap, lokale pc-synchronisatie of PowerShell-runprotocol gecontroleerd.

## Gebruik en herstel

Start met centrale status en AGENTS.md, checkout de bestaande codebranch en gebruik shopify/current/. Controleer bij nieuw werk eerst verse Shopify-rollen en bronchecksums. Werk met een bewezen gelijk UNPUBLISHED-concept en alleen bedoelde paden. .shopifyignore blijft van kracht. Nooit blind de oude root of de volledige sourcecapture naar MAIN uploaden.

Deze Git-commit verandert geen live Shopify-file of product. Git-herstel kan als gewone revert van de nieuwe bronkopie/overdrachtswijziging; de eerdere code en dossiers blijven in de geschiedenis. Shopify-herstel gebruikt het bestaande vorige thema of een gericht beoordeeld concept volgens het releasebeleid.

Catalogus, metafieldwaarden, menu-/collectie-instellingen, Shopify Files-media, order-/klantgegevens en externe VPS/backend worden niet door deze themebron gereproduceerd. Hun afzonderlijke actuele status blijft leidend.
