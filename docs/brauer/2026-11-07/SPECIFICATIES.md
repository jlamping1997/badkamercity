# BRAUER-20 — duidelijke specificaties voor de volledige offline catalogus

7 november 2026. Uitvoering via connectors en tijdelijke Linux-werkruimte; geen lokale Windows-Gitcontrole. Geen Shopify-writes, conceptimport, media-upload of publicatie.

## Klantweergave

Alle 13.161 artikelen hebben een gestructureerde specificatietabel met maximaal vier groepen: Algemeen, Afmetingen, Uitvoering en Meegeleverd. Lege groepen verdwijnen. Artikelnummer en EAN zijn de fabrikantidentiteit. Kenmerken komen uit de drie originele BRAUER-prijslijsten, hun productomschrijvingen en de 64 eerder op exact SKU én EAN gecontroleerde artikelen. Elke zichtbare waarde heeft veldbewijs; controles worden niet uitgebreid naar vergelijkbare kleuren of serienummers.

Relevante kenmerken verschillen per producttype: kraanhoogte, uitloop, montage en wandafwerking bij kranen; lades, softclose, deurrichting en sifonuitsparingen bij kasten; glassoort, glascoating en deursysteem bij glas; kraangaten, spoelbakken en bakpositie bij wastafels. Verlichting en spiegelzijden worden apart beschreven. Edition wordt in consumententaal Standaard; de ruwe bron blijft behouden. Greepafwerking blijft Standaard/glad, Carving/gekarteld en Stripe/gestreept.

Onbekend is geen Nee. Expliciete nul kraangaten blijft nul. Meegeleverd wordt alleen ingevuld bij bronbewijs. Losse kast, wastafel voor onderkast, onderdeel en setgebonden glasdeel blijven herkenbaar. Afmetingen worden niet afgeleid uit een artikelnummertype of een nummer zonder bewezen eenheid. Joy maatcode120 en gecontroleerde fysieke breedte119cm zijn dus verschillende gegevens. De fabrikant-MDF/MFC-handleiding is alleen geraadpleegd als aanvullende context; geen seriebrede maat- of onderdelenovererving daaruit toegepast.

## Open technische gegevens

76 producttypen verwerkt. Voor 10.552 artikelen ontbreken nog één of meer gekozen kernvelden, vooral fysieke afmetingen en aansluitgegevens. Dit is een concrete werkvoorraad, geen foutpercentage. De overige 2.609 artikelen hebben de gekozen kernvelden; dat betekent geen volledige technische of commerciële vrijgave. Ook niet-verplichte extra gegevens kunnen ontbreken. Het Exceloverzicht toont ontbrekende kernvelden per artikel en aantallen per type. De volledige klanttabellen en veldherkomst staan in het privévoorbereidingspakket.

Alle bestaande holds blijven behouden: 27 materiaal-/afwerkingsconflicten, 12 niet-unieke keuzecombinaties, drie maatbronconflicten; samen42artikelen. Betwiste waarden worden nu geheel weggelaten uit de klanttabel; reden en bronconflict blijven intern bestaan. 163 toekomstig leverbare artikelen blijven apart; geen voorraadclaim.

## Formaat en aansluiting

`customer_specifications` gebruikt de bestaande gelezen tabelvorm `[{group,items:[{key,label,value}]}]`. Voor fabrikantnummer is de sleutel `fabrikantnummer`. Dit is offline gegevensvoorbereiding, geen API-writepayload. De huidige Brauer-router is nog niet op dit formaat aangesloten. Bij de latere vrijgave eerst actuele bestaande velddefinitie controleren, vervolgens waarden toepassen en exact teruglezen, daarna weergave in een UNPUBLISHED conceptthema controleren. Geen nieuwe app-owned definities of schemawijzigingen uitgevoerd.

`specifications` is nu de schone platte klantweergave. `specification_review` bevat ontbrekende kernvelden en interne nominale maten. `specification-evidence.json` bewaart per SKU/EAN elk bronveld, fragment, bestandsregel of eerdere exacte bron-URL. Identiteiten, BTW-prijzen, groepen, opties, media, eigen aanvullingen en dataholds zijn onveranderd; daarvoor is een fingerprintbaseline vastgelegd. `release-gate.json` verwijst naar de nieuwe catalogushash en houdt de import gesloten.

## Uitvoering en controles

Na `prepare_catalog.py` en `restore_verified_details.py`: `build_specifications.py`, daarna de bestaande voorbereidingstests en `test_specifications.py`. Zes nieuwe tests en negen voorbereidingstests PASS. Beide testsets bewaken identiteit, BTW, groepsregels, exacte beeldkoppeling, bronconflicten, eenheden, onbekend versus Nee en fabrikantnummer. Het specificatieoverzicht is gemaakt met Artifact Tool; drie bladen: Overzicht, Voorbeelden en Artikelen. Excel is een reviewoverzicht; alle volledige specificaties staan in de JSONcatalogus van het pakket. Geen claims over een fysieke Windows/Excel- of live winkeltest. De aparte voorbeeldtabel in het gesprek heeft twaalf echte artikelsets; geen browsercontrole uitgevoerd doordat de lokale Playwright-browser ontbreekt. Werkbladweergaven wel gerenderd en visueel gecontroleerd.

**Eén volgende handeling:** de ontbrekende fysieke maten en aansluitgegevens per exact artikel verrijken uit ontvangen officiële technische productdata. De complete aangekondigde afbeeldingen-/PDF-set moet nog worden ontvangen en geïnventariseerd; vóór die ontvangst geen Shopify-import, ook geen DRAFT-pilot.
