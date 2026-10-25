# Hotbath compacte keuzes — codecheckpoint 25 oktober 2026

Status: **IN_TEST / CODE_READY / PREVIEW_BASELINE_VERIFYING**. Deze zevenbestandenpatch is lokaal voorbereid en gereviewd. Op dit checkpoint wordt de bestaande ongepubliceerde kopie gelijkgetrokken met MAIN; de zevenbestandenpatch is **nog niet geüpload**.

Huidige MAIN, door eigenaar gepubliceerd: **195688890634 — BadkamerCity - Hotbath mobiel A afwerking**. Gebruikte UNPUBLISHED kopie: **195688694026 — BadkamerCity - Hotbath compacte keuzes**. Deze bestaande kopie had553 bestanden;551 waren gelijk aan MAIN en twee basisbestanden worden eerst exact gelijkgetrokken. Definitieve identieke-baselinecontrole volgt vóór de delta. De langzaam verwerkende extra kopie195691184394 heet nu **Backup - Hotbath afwerking 25 okt**, is niet als preview geverifieerd en wordt niet voor deze patch gebruikt.

## Wijziging

- De kleuruitklapper toont het werkelijke resterende aantal: `+4 kleuren`, `+1 kleur`, en uitgeklapt `Minder kleuren`; de knop is duidelijker vormgegeven.
- De mobiele inbouwdeelkeuze krijgt dezelfde compacte vorm als de overige keuzemenu’s: korte titel/uitleg en directe Ja/Nee-opties, zonder groot omliggend kader. De bestaande radio-inputs, exacte relaties, actuele prijs, verplicht kiezen en koopactie blijven behouden.
- Desktop en andere merken behouden bestaande bediening. Geen productdata-, prijs-, voorraad- of metafieldwijzigingen.

`before/` en `after/` bevatten uitsluitend de zeven manifestbestanden. De overige553-themebasis wordt niet opnieuw opgeslagen. Dit dossier mag niet als volledig thema worden gepusht.

## Checkpointbewijs

De uitgebreidere swatchtest is opnieuw uitgevoerd en geslaagd: correcte +4/+1-tekst, expand/collapse en aria-expanded, zes zichtbare keuzes met huidige kleur behouden, desktopherstel, onmogelijke keuzes, andere merken en exacte navigatie van drie proefgroepen. De fixture wordt hergebruikt uit het naastliggende `mobile-a/tests/test-data/hotbath-groups.json`.

Uitvoerder meldt onafhankelijke code-review PASS. Theme Check: zes bestanden PASS; bestaande ontbrekende datasetdependency in de partiële lokale tree bij het switcher-snippet blijft expliciet zichtbaar. Geen nieuwe codefout aangetroffen; geen foutloze volledige themacontrole geclaimd.

Nieuwe Shopify-upload, Admin-readback en visuele preview: **PENDING**. De eerdere totaalprijs-/cartbeperkingen blijven gelden; nieuwe volledige cartsubmit, fysieke telefoonbediening, bestelling en betaling zijn niet getest.

Test vanuit deze map: `node tests/hotbath-swatches-test.cjs`. Met afwijkende dossierlocatie kan `HOTBATH_TEST_FIXTURE` naar het bestaande fixturebestand wijzen.

Terugzetten: herstel uitsluitend de zeven `before/`-bestanden op een gecontroleerd ongepubliceerd thema. De bestaande kleurbeelden, mobiele totaalfunctie, inbouwdata en QA-redirect worden door deze delta niet vervangen.

**Exact volgende handeling:** de nieuwe preview na voltooide identieke kopie/upload valideren.

