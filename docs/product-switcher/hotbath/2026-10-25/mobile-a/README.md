# Hotbath mobiel A — gecontroleerde afwerking, 25 oktober 2026

Status: **LIVE_USER_PUBLISHED / POLISH_PREVIEW_READY**.

De eigenaar heeft tijdens het werk **195688694026 — BadkamerCity - Hotbath mobiel A 25 okt** gepubliceerd. De ontvangen telefoonscreenshot toont de nieuwe live CB7072-weergave. De laatste afwerking staat afzonderlijk in **UNPUBLISHED 195688890634 — BadkamerCity - Hotbath mobiel A afwerking**. De uitvoerder heeft niet gepubliceerd en de live versie tijdens de afwerking niet gewijzigd.

## Patch en bewijs

Dit dossier bevat uitsluitend 23 gerichte bestanden in `after/`: zes gewijzigde bestanden, drie nieuwe JS/CSS, dertien officiële Hotbath-finishbeelden en één veilig afgevangen voormalige QA-route. `before/` bevat alleen de zes vervangen bestanden. Dit is geen volledige theme-export.

Finale Shopify-readback: **23/23 MD5 exact**, **530 overige bestanden ongewijzigd**, **553 totaal**; alle manifestpagina’s volledig. Zie `source-manifest.json` en `evidence/admin-final-readback-summary.json`.

Mobiel Hotbath: zes zichtbare kleurstalen met huidige kleur behouden, uitklapbare overige kleuren, volledige naam, compacte maten, actuele totaalprijs op basis van aantal en optioneel inbouwdeel. Onder360px drie kleurkolommen; plusknop blijft binnen het aantalveld. Desktop en andere merken behouden de bestaande bediening. Exacte product-/inbouwrelaties en bestaande winkelwagenactie blijven behouden; geen betaalde voorselectie of nieuwe automatische POST-herhaling. Geen product-/prijs-/voorraad-/metafieldwijzigingen.

## Controles

- Werkelijke totaalberekening:18/18 PASS; geen misleidende bedragen bij ongeldige hoeveelheden, prijzen, variant/valutamismatch, onbeschikbaarheid of onzekere cartstatus.
- Swatch/navigatieregressies PASS: zes zichtbaar, huidig behouden, naam, uitklappen, desktopherstel, onmogelijke opties, andere merken en drie proefgroepen.
- Observer ready/pending-scenario’s PASS: geen renderlus bij rust, scroll, aantal, keuze of desktopwissel.
- CB105 aantal2: Ja€778,00 / Nee€430,00; tien officiële swatches geladen.
- CB7072 aantal2 + inbouw:€3.234,02. Aantalveld142px; plusknop eindigt331px binnen container334px.
- IBS70 zonder add-on:€1.541,01→€3.082,02 bij aantal2.
- Smal frame320px nominaal/305px werkelijk: geen overflow; drie swatchkolommen69px.
- Desktop: mobiele functie inactief, geen mobiel totaal, aantal op oorspronkelijke plaats buiten formulier, oorspronkelijke dropdown.
- Theme Check vóór/na: dezelfde ontbrekende datasetdependency in de partiële lokale tree; geen nieuwe errors. Complexity227→229 waarschuwing. Geen foutloze volledige theme-check geclaimd.

## QA-route en beperkingen

Een tijdelijke alternatieve iframe-route hielp de smalle weergave inspecteren omdat de browser geen viewport-API biedt. Die route werd meegepubliceerd toen de eigenaar het concept live zette. Verwijderen werd door connectorbeleid geblokkeerd. In het afwerkingsconcept is alleen de eigen `templates/product.bc-mobile-review.liquid` daarom vervangen door een eenvoudige noindexredirect naar de normale productpagina, zonder iframe/testcode. Validator PASS/exit0 met cached schema na docs-timeout; browserredirect naar gewone CB105 zonder view bevestigd.

De huidige live versie bevat de eerdere helper nog totdat de eigenaar de afwerking publiceert. Gewone productroutes worden door de alternatieve route niet gewijzigd.

De agent heeft geen fysieke iPhone bediend; de eigenaarsscreenshot bevestigt weergave. De nieuwe harness heeft geen volledige winkelwagensubmit uitgevoerd; berekeningen en DOM/formbinding wel. Checkout, betaling, bestelling en alle Hotbath-pagina’s afzonderlijk: NOT_TESTED.

## Reproduceren, bronnen en terugzetten

Vanuit deze map: `npm install`, daarna `npm test`; happy-dom21.0.4 staat vastgelegd. Testpaden zijn aangepast aan deze dossierstructuur, productiecode is exact gekopieerd. De laatste CSS-afwerking wijzigt de geteste berekeningscode niet.

`swatch-sources.json` bevat officiële bronnen en beeldhashes. Geen screenshots of persoonlijke cartgegevens opgeslagen. Werkbranch `fix/product-cards-2026-10-14`; geen root-theme-sync vanwege onbekende deployintegratie, geen branchmerge; main alleen documentatie. Geen Windows-checkoutcontrole geclaimd.

Functioneel herstellen: op een gecontroleerd ongepubliceerd thema de zes bestanden uit `before/` terugzetten; de nieuwe assets worden dan niet meer actief aangeroepen. Laat de veilige QA-redirect behouden.

**Exact volgende handeling:** eigenaar beoordeelt/publiceert **BadkamerCity - Hotbath mobiel A afwerking (195688890634)**; daarna rollen, normale productpagina en aantalveld opnieuw controleren.
