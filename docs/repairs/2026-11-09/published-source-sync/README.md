# Gepubliceerde prijs-/zoekrelease en gerichte Git-bronreconciliatie

9 november 2026 · GIT-SYNC-02 · OWNER_PUBLISHED_VERIFIED / SOURCE_RECONCILED

De eigenaar publiceerde **BadkamerCity - Hele europrijzen 8 nov (196368531722)** en meldde dat de visuele controle goed was. De verse MAIN-read bevat 1.390 bestanden. Alle 1.390 checksums zijn gelijk aan het eerder geteste eindconcept: de oorspronkelijke 24 prijs-/pictogrampaden plus de drie latere zoek-/LiquidDoc-paden zijn live bevestigd. Het vorige thema 196354474250 is nu UNPUBLISHED; het is niet automatisch een nieuwe actuele preview.

## Concreet opgelost

Git bevatte nog tien oudere gedeelde bestanden. Die zijn afzonderlijk inhoudelijk vergeleken met MAIN en exact overgenomen. Zo kan een volgende gerichte wijziging de al gepubliceerde klikbare productkaarten, groene tijdelijke voorraadpresentatie en bijbehorende tegelkoopbox niet onbedoeld door deze oudere Git-bron vervangen. [Review per bestand](file-review.json).

Dit is een correctie van de ontwikkelbron, geen nieuwe storefrontwijziging. Er is geen thema-, product-, prijs-, voorraad-, publicatie- of instellingenwrite uitgevoerd. De bestaande tijdelijke voorraadinstelling blijft uitsluitend presentatie; deze taak bewijst of wijzigt geen leveranciersvoorraad of bestelbaarheid. Het grote settings_schema-diff bestaat semantisch uit precies één bestaande checkboxgroep plus bronopmaak. settings_data is beschermd gebleven.

Tijdens opslag kwam een afgeronde BRAUER31-update binnen. Die scripts en documenten zijn volledig behouden; alleen het gedeelde statusdocument is additief samengevoegd. De tien themapaden waren door dat andere werk niet gewijzigd.

## Bron en pariteit

- Codebranch: fix/product-cards-2026-10-14; basis `02cdd42d18c3da1d87493758265a9466a6ec9fb6`; codecheckpoint `a12bb9433cf30bc355cca7d6ef029cde35dd8622`.
- Main-documentatiebasis: `84e7bf4cc50157f1387c20580e69e0949ae52a0b`; alleen documentatie op main bijwerken.
- Gedeelde files: 1.381, waarvan 1.380 vergeleken na uitsluiting van config/settings_data.json. **1.380 exact gelijk; nul resterende gedeelde verschillen.**
- Negen live-only backup-/reviewfiles zijn bewust niet geïmporteerd of verwijderd; de aparte .shopifyignore blijft een lokale deployguard.
- Geen claim dat de Windows-werkmap schoon is of dat een volledige Git-root mag worden gedeployed.

[Volledig vers MAIN-manifest](published-main-manifest.json) · [Publicatiecontrole](publication-check.json) · [Voor/na-bronpariteit](source-parity.json) · [Volledige live-eindcontrole](closure-check.json).

## Verificatie en grenzen

De tien opgehaalde bodies zijn afzonderlijk tegen de Admin-MD5 gecontroleerd. De bestaande regressies draaien opnieuw op de bijgewerkte bron: **31 prijscontroles, 26 kaartcontractcontroles, 17 voorspellende-zoekcontroles: 74 PASS**. De officiële Shopify-validator controleert alle tien files: VALID, nul errors; gebruikt de gecachte officiële schema's nadat netwerkverversing time-out gaf. [Controleverslag](checks.json) · [Validatoruitvoer](theme-check.txt).

Dit bewijst bronpariteit en de genoemde offline contractcontroles. Deze taak bevat geen nieuwe browser-, fysieke telefoon-, checkout-, betaal-, mail-, consent- of purchase-eventtest. Eerdere previewbrowserbewijzen blijven gekoppeld aan het vorige dossier. Native policies, juiste btw-identiteit en andere operationele gates blijven open.

## Terugzetten en vervolg

Live terugzetten is voor deze Git-taak niet nodig: er zijn geen Shopify-writes geweest. Bij een bewezen bronfout kan een gewone revert van het tienbestanden-codecheckpoint de eerdere Git-bytes herstellen; verifieer dan opnieuw de actuele MAIN, want een revert maakt de bron doelbewust afwijkend. Geen force-push, reset, clean of blind root-deploy.

**Eén volgende handeling:** technisch consentgedrag op de live site controleren bij weigeren, toestaan en heropenen. Er is voor deze taak niets opnieuw te publiceren. Geen actieve schrijver na overdracht.
