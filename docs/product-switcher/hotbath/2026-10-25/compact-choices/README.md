# Hotbath compacte keuzes — 25 oktober 2026

Status: **PREVIEW_READY / NIET_GEPUBLICEERD**.

MAIN blijft **195688890634 — BadkamerCity - Hotbath mobiel A afwerking**, tijdens deze wijziging ongewijzigd. De nieuwe weergave staat in **UNPUBLISHED 195688694026 — BadkamerCity - Hotbath compacte keuzes**.

## Wijziging

De kleuruitklapper toont het werkelijke resterende aantal: **+4 kleuren**, **+1 kleur**, en uitgeklapt **Minder kleuren**. De knop is duidelijker vormgegeven. De mobiele inbouwkeuze gebruikt een compacte titel/uitleg en directe Ja/Nee-keuzeknoppen in dezelfde stijl als de overige menu’s, zonder groot kader. De echte radio-inputs, vereiste keuze, actuele meerprijs, exacte productrelaties en bestaande koopactie zijn behouden. Geen betaalde voorselectie.

Desktop en andere merken behouden de eerdere bediening. Geen product-, prijs-, voorraad- of metafieldwijzigingen. Alleen de zeven bestanden in `after/` zijn gewijzigd; `before/` bewaart de zeven vorige bestanden. Niet als volledig thema pushen.

## Gecontroleerd

- Vóór de patch: alle553 previewbestanden identiek aan MAIN na herstel van twee basisbestanden.
- Finale Admin-readback: **553 bestanden =7 exacte gewijzigde bestanden +546 ongewijzigd**; preview UNPUBLISHED, MAIN ongewijzigd.
- Tijdelijke QA-renderroute na testen exact teruggezet naar de bestaande veilige noindexredirect; geen iframe/testcode op de opgeleverde route.
- Uitgebreide swatchtest PASS: +4/+1-telling en enkelvoud, uit-/inklappen, aria-expanded, zes zichtbare kleuren met huidige kleur behouden, desktopherstel, onmogelijke opties, andere merken en drie exacte proefgroeproutes.
- Echte Shopify-preview in smal frame: **+4 kleuren → Minder kleuren → +4 kleuren** werkt.
- Inbouwkeuze: geen initiële selectie, required behouden; compacte labels. CB7072 aantal2: Ja **€3.234,02**, Nee **€1.408,00**.
- Frame320px nominaal/305px inhoud: scrollbreedte305px, geen overflow; keuzeknoppen107,5×56,375px.
- Desktop: mobiele functie inactief, bestaande kleurdropdown, oorspronkelijke inbouwlabels en verborgen mobiele labels.
- Onafhankelijke code-review PASS. Theme Check zes bestanden PASS plus dezelfde ontbrekende datasetdependency bij het switcher-snippet in de partiële lokale tree; geen nieuwe codefout. Geen foutloze volledige theme-check geclaimd.

De visuele controle gebruikte390/320px iframes omdat de browser geen viewport-API biedt. Geen fysieke telefoonbediening en geen nieuwe winkelwagen-submit, checkout, bestelling of betaling uitgevoerd. Berekeningen en DOM/formulierkoppeling zijn wel gecontroleerd. Screenshots zijn niet in de publieke repository opgeslagen.

## Overige themakopie

De extra serverkopie **195691184394 — Backup - Hotbath afwerking 25 okt** was te langzaam voor de actieve uitvoering; daarom is de bestaande preview hergebruikt. De extra kopie is inmiddels klaar en **553/553 checksums gelijk aan de huidige MAIN-basis**. Dit is een geverifieerde ongewijzigde back-up, niet het concept met de nieuwe compacte keuzes.

## Reproduceren en terugzetten

Test vanuit deze map: `node tests/hotbath-swatches-test.cjs`. De fixture wordt hergebruikt uit het naastliggende `mobile-a/tests/test-data/hotbath-groups.json`; met andere dossierlocatie kan `HOTBATH_TEST_FIXTURE` naar dat bestand wijzen.

`source-manifest.json` legt MD5/SHA-256 vast; `evidence/` bevat readback, browserresultaten en testresultaten. Functioneel herstel: alleen de zeven `before/`-bestanden op een gecontroleerd ongepubliceerd thema terugzetten. De oorspronkelijke mobiele totaalfunctie, kleurbeelden, inbouwdata en veilige QA-redirect blijven behouden.

Werkbranch: `fix/product-cards-2026-10-14`. Alleen scoped dossier; geen root-theme-sync of branchmerge. Main bevat uitsluitend documentatie. Geen Windows-checkoutcontrole geclaimd.

**Exact volgende handeling:** eigenaar beoordeelt/publiceert **BadkamerCity - Hotbath compacte keuzes (195688694026)**; daarna actuele rollen en de kleur-/inbouwkeuze op normale productpagina controleren.
