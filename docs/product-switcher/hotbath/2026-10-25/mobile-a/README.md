# Hotbath mobiel ontwerp A — uploadcheckpoint 25 oktober 2026

Status: **UPLOADED_NOT_PUBLISHED / IN_TEST**.

De 22 permanente bestanden in `after/` zijn een gerichte patch voor het mobiele Hotbath-bestelblok. Zes bestaande bestanden zijn gewijzigd; zestien zijn nieuw (drie JS/CSS-bestanden en dertien officiële Hotbath-finishafbeeldingen). `before/` bewaart uitsluitend de zes vervangen bestanden. Dit is geen volledige theme-export en mag niet als volledig thema worden gepusht.

## Scope en publicatie

- Gecontroleerde basis en huidige MAIN: **195688890634 — WERKCONCEPT - Hotbath mobiel A - nog in test**.
- Uploaddoel: **UNPUBLISHED 195688694026 — BadkamerCity - Hotbath mobiel A 25 okt**.
- Voor de patch waren alle 536 bestanden van beide thema’s checksum-identiek.
- Uitvoerder heeft gemeld dat de 22 permanente bestanden werkelijk zijn geüpload en alle 536 MAIN-bestanden ongewijzigd zijn. Finale Admin-checksums worden na visuele QA opnieuw vastgelegd.
- Geen product-, prijs-, voorraad-, metafield-, bestel- of betaalinstellingen gewijzigd. Geen thema gepubliceerd.
- Bestaande werkbranch: `fix/product-cards-2026-10-14`; geen root-theme-sync zolang de Git→Shopify-integratie onbekend is.

## Gedrag

Op smalle Hotbath-productpagina’s: officiële kleurstalen, aanvankelijk zes zichtbare keuzes (huidige kleur blijft zichtbaar), uitklappen van overige kleuren, leesbare volledige kleurnaam, compacte maatknoppen en een compact bestelblok. Totaalprijs volgt aantal en de bestaande expliciete inbouwdeelkeuze. De bestaande exacte productnavigatie, inbouwrelaties en winkelwagenactie blijven behouden. Andere merken en desktop behouden hun bestaande bediening.

De totaalberekening weigert misleidende bedragen bij ongeldige aantallen, variant-/valutamismatch, ontbrekende of onveilige prijzen, onbeschikbare geselecteerde inbouwdelen, onzekere winkelwagenstatus en niet-ondersteunde verkoopplannen. Er is geen betaalde voorselectie en geen nieuwe automatische POST-herhaling.

## Bewijs op dit checkpoint

- `tests/hotbath-mobile-total-test.cjs`: **18/18 PASS**, werkelijk productie-`calculate()` met geïsoleerde fixtures.
- `tests/hotbath-swatches-test.cjs`: **PASS** voor zes zichtbare kleuren, behoud geselecteerde kleur, volledige naam, uit-/inklappen, desktopherstel, selectiestatus, onmogelijke optie, andere merken en exacte productnavigatie in drie proefgroepen.
- `tests/hotbath-mobile-observer-test.mjs`: **2 scenario’s PASS**, ready en pending; geen observer-/requestAnimationFrame-lus bij rust, scrollen, aantal, keuze en desktopwissel.
- Theme Check vóór/na: dezelfde ontbrekende `assets/product-switcher-data.json`-dependency in de partiële lokale testboom; **geen nieuwe errors**. Bestaande complexitywaarschuwing 227→229 en andere bestaande waarschuwingen blijven zichtbaar. Geen claim van een foutloze volledige theme-check.
- Mobiele/desktop visuele eindcontrole en definitieve Admin-readback zijn **IN_TEST**.
- Fysieke iPhone, betaling en alle Hotbath-productpagina’s afzonderlijk: **NOT_TESTED**.

Een tijdelijk Shopify-template met een smal iframe is uitsluitend gebruikt als renderhulp omdat de beschikbare browser geen viewport-API biedt. Het maakt geen deel uit van deze patch, is hier niet opgeslagen en wordt voor oplevering verwijderd of, als verwijderen door platformbeleid geblokkeerd is, door een veilige inactieve alias vervangen en expliciet gemeld.

## Reproduceren

Vanuit deze map:

```sh
npm install
npm test
```

`happy-dom` is vastgelegd op 21.0.4. Testpaden zijn alleen aangepast voor deze dossierstructuur; de in `after/` opgeslagen productiecode is ongewijzigd overgenomen uit de uploadwerkmap.

## Bronnen en terugzetten

`source-manifest.json` bevat MD5/SHA-256 per gewijzigd bestand; `swatch-sources.json` bevat de officiële Hotbath-bron-URL en SHA-256 van elk finishbeeld. `evidence/` bevat lokale testresultaten.

Terugzetten vóór publicatie: overschrijf alleen de zes gewijzigde bestanden vanuit `before/` op een gecontroleerd ongepubliceerd thema. De zestien nieuwe assets hebben daarna geen actieve referenties. Verwijdering is geen vereiste voor functioneel herstel. Publicatie/omwisselen blijft een afzonderlijke eigenaarshandeling.

**Exact volgende handeling:** visuele preview afronden, tijdelijke QA-renderhulp opruimen en 22 permanente bestanden plus ongewijzigde MAIN opnieuw via Admin verifiëren.

