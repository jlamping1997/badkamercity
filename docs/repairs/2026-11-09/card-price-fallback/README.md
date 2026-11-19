# Veilige kaartprijzen bij een mislukte productaanvraag

9 november 2026 · CARD-PRICE-FALLBACK-01 · PREVIEW_VERIFIED / OWNER_PUBLICATION_PENDING

De eigenaar heeft herstel van stap1 uit de read-only Git-review gevraagd. De andere chat werkt niet aan thema’s. De geïsoleerde foutproef met de actuele bron gaf bij een mislukte Shopify-kaartaanvraag de zoekindexprijs €69,07 zonder eenheid; bij een geslaagde aanvraag stond de juiste €63,95 per m². De indexprijs is de koopbare doosprijs en kan dus niet veilig als leidende kaartprijs dienen zonder de verkoopeenheid.

## Gewijzigd gedrag

De externe collectie-/zoekkaart toont nu **Prijs laden…** totdat de actuele Shopify-kaartgegevens binnen zijn. Dan verschijnt de bestaande juiste m²-, stuk-, pak- of setprijs. Verschillende variantprijzen behouden Vanaf; gewone hele EUR-prijzen houden de bestaande geldopmaak. Deze wachttijd geldt voor alle externe kaarten, omdat de index alleen onvoldoende bewijs van de prijseenheid levert. Native serverkaarten behouden hun bestaande correcte weergave.

Bij HTTP-fout, netwerkfout, time-out, lege section, ongeldige JSON of een andere productidentiteit staat **Bekijk prijs**. De productlink blijft bruikbaar; de snelle bestelknop blijft dan uitgeschakeld zoals in de eerdere gegevensfoutsituatie. Een ontbrekend section-contract blijft niet eindeloos laden. Ook ontbrekende/ongeldige prijs- of tegelgegevens tonen geen schijnbedrag. Er is geen nulprijs, kale doosprijs of nieuw financieel bedrag als terugval ingevoerd. Echte gratis prijzen van nul blijven toegestaan.

De prijskeuze staat eenmaal in productPrice: controle op getal/centen, eventuele geverifieerde tegeloppervlakte en m²-prijs, dan formattering. Dezelfde route geldt na kaartverrijking en kleurwissel. Nieuwe NL/EN-labels komen via bc_listing uit de bestaande filtersnippet. aria-busy wordt afgesloten bij succes én fout. Filters, sorteren, paginering, cache, vier gelijktijdige kaartaanvragen, kleurrelaties en native API-terugval blijven in hun bestaande controller.

## Bron en concept

MAIN bij start/einde: **196354474250 — Tegelprijzen per m2 9 nov**. Bestaande reserve196395073802 eerst read-only volledig vergeleken:1.390files per thema, precies de vijf eerdere prijsfiles achterlopend. Die vijf zijn exact uit de bevestigde huidige Git/live-bron overgenomen; overige1.385files, inclusief settings-checksum, waren al gelijk. Geen extra themakopie gemaakt en config/settings_data.json niet geschreven of als body gelezen.

Hetzelfde bestaande UNPUBLISHED concept196395073802 heet nu **BadkamerCity - Veilige kaartprijzen 9 nov**. Daar zijn uitsluitend deze vier functiepaden gewijzigd:

- assets/bc-external-filters.js
- snippets/bc-external-filters.liquid
- locales/nl.json
- locales/en.default.json

Finale integrale read: **1.390files per thema,1.386gelijk en precies vier bedoelde verschillen; alle1.390MAIN-checksums ongewijzigd.** Alle vier geschreven bodies en MD5’s exact teruggelezen. [Volledige vergelijking](theme-parity.json). De overige eerdere tegelprijswijzigingen en alle gedeelde categorie-/uitstralinggegevens blijven behouden. Geen product-, prijs-, voorraad-, server- of publicatiewrite.

## Controle

- **31 nieuwe controles PASS** met de echte filtercontroller in Happy DOM en de echte Liquid-labelroute. Inclusief eerst uitgestelde aanvraag zonder doosprijsflits, daarna juiste m²-prijs; HTTP/netwerk/time-out/JSON/null/identiteitsfouten op zoeken én collectie; ongeldige geld-/oppervlaktedata; gewone bedragen, stuksproducten, variatieprijzen, echte nulprijs, NL/EN, ontbrekende configuratie en totale indexuitval met native kaartbehoud. [Testbron](checks.mjs) · [Resultaat](checks.json).
- Bestaande tegel-,26kaart-,31prijs- en17voorspellende-zoekregressies opnieuw PASS. De oude dossiers en hun beperkingen zijn behouden. Er is geen bestaande testverwachting aangepast voor deze patch.
- Officiële Shopify-validator op alle vier functiepaden: **VALID**, nul errors of waarschuwingen; officiële gecachte schema’s na een time-out bij netwerkverversing. [Uitvoer](theme-check.txt).
- Echte Chrome-desktoppreview1348×926, conceptnaam zichtbaar: Cottoceramix met Marmerlookfilter geeft90producten, alle24kaartprijzen op de getoonde pagina hebben state ready en aria-busy=false; bedragen met alleen per m². Nieuwe NL-labels in de DOM bevestigd. [Browserbeeld](browser-preview.jpg). Geen browsernetwerkfout geïnjecteerd; foutpaden zijn offline met de echte controller gecontroleerd. Geen nieuwe fysieke telefoon-, koop-, mail- of meetproef.

Herhalen: installeer de vastgelegde testdependencies en voer node checks.mjs uit in dit dossier. De bredere bestaande suites staan in ../tile-area-prices/ en ../predictive-search-prices/. De uitbreiding van automatische testuitvoering uit de eerdere adviestabel is niet uitgevoerd.

## Publiceren en herstel

**Eén volgende handeling:** eigenaar beoordeelt/publiceert **196395073802 — Veilige kaartprijzen 9 nov** in Shopify; daarna verse MAIN-read en de vier checksums controleren. De koppeling ondersteunt geen publicatie door de agent. Het huidige live thema is deze ronde volledig ongewijzigd gebleven.

Voor herstel vóór publicatie kunnen uitsluitend de vier paden uit rollback/ worden teruggezet in dit concept, na vergelijking met de actuele MAIN. Er is geen serverupdate nodig. Werkcode op fix/product-cards-2026-10-14, uitgangspunt d0be39296dae99c0ffece39a6bbdb3ba2ab84ffd; themabron uitsluitend shopify/current/. Lokale Windows-werkmap niet gecontroleerd. Overige Wiesbaden-/BRAUER-/beleids-/mobiele-/meetwerkstromen en uitgestelde kleur-/formaatpunten behouden. Geen actieve schrijver na overdracht.
