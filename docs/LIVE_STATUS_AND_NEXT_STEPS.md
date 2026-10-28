# BadkamerCity — actuele werkstatus

**28 oktober 2026 · DOC-02A componentverdieping vastgelegd.** Vaste huidige ingang. De [lange oude status](LIVE_STATUS_ARCHIVE_BEFORE_2026-10-28.md) en oudere releasehandelingen zijn geschiedenis, geen opdracht om import/publicatie te herhalen.

## Huidige opdracht en resultaat

De eigenaar vraagt sterke, diep doorzoekbare documentatie in Git: wat we gebruiken, hoe onderdelen zijn opgebouwd, hun code-/datakoppelingen en onderbouwde inconsistenties. Ook is een private export van bereikbare productgegevens gevraagd en geleverd. Geen live refactor, productmutatie of publicatieopdracht in deze documentatieronde.

**DOC-00:** onderzoeksboom/afspraken. **DOC-01:** volledige ontvangen bronkaart en private productexport; één settings-bytepariteitsuitzondering blijft OPEN. **DOC-02A:** nu de [routematrix](architecture/ROUTE_RENDERER_MATRIX.md) en [acht inhoudelijke componentdossiers](architecture/components/README.md): fundament/tooling, PDP-data, keuzes/inbouw, kaarten/filters, cartfeedback, navigatie/opslag, datapijplijnen en stijl/beweging. Samen negen inhoudelijke uitlegpagina's, met bronnen, staten, fouten/terugval, onderhoud en acceptatiegrenzen.

## Bronstand en meetgrenzen

| Bron | Waarneming |
| --- | --- |
| Repository | jlamping1997/badkamercity, publiek |
| Actieve branch / startcommit | fix/product-cards-2026-10-14 / c8f76eea2bf8a81ab0f54196e239e0b3930fe20a |
| main bij aanvang | 2f87039c2774e27010860a4ef5ccb29dcc7bf886; documentatie-ingang |
| Opnieuw gelezen MAIN | 195818389770 — BadkamerCity - Smooth winkelwagen pop-up |
| Compleet vers manifest | 1.262 bestanden; paden/checksums gelijk aan DOC-01 |
| DOC-01-pariteit | 1.261 exact; ontvangen settings_data.json blijft afwijkend van zijn metadata |
| Componentbronindex | 85 geselecteerde bestanden, alle bytes/groottes passend; geen claim van 85 volledige runtimeaudits |
| Metafieldconsumenten | 52 letterlijke keys + 4 dynamische locaties; typen/aantallen uit eerdere private export |
| Openbare responses | 8 GET's, alle HTTP 200 en Shopify.theme.id 195818389770; HTML-structuur, geen uitgevoerde JS |
| Afgeleide keuzedata | 656/656 groepsassets bytegelijk gereconstrueerd uit 9 werkelijke bronassets |
| Productexport uit DOC-01 | 11.343 producten/varianten, 241.064 metafields, 32.065 mediarecords; privé geleverd, geen nieuwe realtime voorraadtelling |
| Windows / VPS / deploymentkoppeling | Niet opnieuw vastgesteld; geen synchronisatie- of servergezondheidsclaim |

Zie [bewijs DOC-02A](architecture/evidence/2026-10-28-doc02/README.md), [bronkaart DOC-01](architecture/DOC01_SOURCE_MAP.md) en [productdata](architecture/PRODUCT_DATA.md). Tooling staat op de actieve branch; main krijgt alleen documentatie. Root-themacode is niet automatisch productiecode en is niet overschreven.

## Concrete inzichten voor vervolgonderzoek

- De gewone PDP, externe kaart, Sunshower-shopkaart, inbouw/set en wishlist gebruiken verschillende cartfeedbackpaden. De nieuwe popup wordt niet via iedere ingang aangeroepen; eerst gewenst contract bepalen, geen globale submitinterceptor toevoegen.
- Native mobiele lijst-CSS verbergt sommige Bekijk-product-labels/pijlen. Sunshower-linkkaarten hebben een eigen pijl; externe CSS/JS kan de lijst later veranderen. Dit geeft een te onderzoeken verklaring, geen afgeronde reproductie van de gemelde inconsistentie.
- Eén onderzochte Hotbath SDS1-response gebruikt de oorspronkelijke grote dataset wegens niet passende revisieguard. De groep bestaat en de afgeleide bytes zijn correct; geen algemene performance- of datacorruptieclaim.
- De historische generator staat in Git maar heeft geen gevolgde datasets/-invoer op het broncommit. De huidige oorspronkelijke assets zijn beschikbaar in het private pakket/read-only thema; invoer, controle en rebuild zijn nu beschreven.
- De huidige externe-filtercode probeert na DOM-guards automatisch runSearch, zonder bcfilters=1-guard. Oude opt-inbeschrijvingen zijn voor deze bron historisch; daadwerkelijke API-/index-/browserwerking blijft open.

## Uitgevoerd en niet uitgevoerd

Nieuwe controles: volledige manifestvergelijking, herhaalde drie bodyreads, exacte componenthashes, Git-blobkandidaten, veldconsumentenmetadata, acht HTML-responses, 656 afleidingsvergelijkingen, document-/JSON-/bronverwijzingscontroles en de offline componentbuilder op echte brondata. De oude vier productbuilder-/vijf scannerchecks blijven eerder bewijs; geen nieuwe featuretestclaim.

Geen browser-/touch-/focus-/computed-style-/performance-/checkouttest. Geen add/change/update-cart, product-/theme-/VPS-write, nieuw thema, publicatie, brede dependencyupgrade of dump van private productwaarden naar Git. De settings-body is opnieuw identiek ontvangen maar wijkt nog af van metadata; geen onafhankelijke exacte settingskopie beschikbaar in deze verbinding of gevolgde Git-bestanden. De oorzaak blijft onbekend; geen pariteitscontrole versoepeld. Na oplevering geen writer of achtergrondworker actief.

## Exact één volgende handeling

**DOC-02B — mobiele kaart-/pijlvergelijking read-only uitvoeren:** standaard collectie Wastafelkranen, zoekresultaten Sunshower en Sunshower-landing in dezelfde mobiele en desktopstaat bekijken; na JavaScript de werkelijke renderer, CTA-zichtbaarheid/cascade, linkfunctie en focus vastleggen. Daarna de bevinding classificeren met het bestaande componentcontract. Geen koopactie/productwijziging nodig; de settings-uitzondering blijft apart OPEN voor volledige bronvrijgave.

## Hervatten

Lees deze status → AGENTS.md → architecture/components/README.md → het betreffende dossier en gedateerde bronindex. Controleer eigen Gitwerkmap, actuele MAIN en hashes. Bron-/hand-offcheckpoint is vindbaar met git log -1 -- docs/architecture/components. De private productexport wordt via de eigenaar gedeeld, niet uit publieke Git gehaald. Oudere imports, previews en publicaties niet opnieuw starten op basis van historie.
