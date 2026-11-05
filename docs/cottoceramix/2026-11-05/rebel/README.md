# COTTO-01 — Revoir Paris Re-Bel pilot

5 november 2026. Producten: **LIVE_VERIFIED**. Winkelwagencorrectie: **PREVIEW_VERIFIED / AWAITING_MERCHANT_PUBLICATION**, nog geen themapublicatie.

De eigenaar vroeg één complete Cottoceramix-serie online te zetten als voorbeeld voor de verdere import. Re-Bel heeft een gecontroleerde matrix van 11 kleuren × twee vierkante formaten. Casablanca bevat daarnaast vormen en randstukken met een andere verkoopeenheid; dat vraagt een afzonderlijke beoordeling.

## Live resultaat

- [Blanc 60×60](https://badkamercity.nl/products/revoir-paris-re-bel-blanc-vloertegel-mat-60x60-cm) is de ingangs-URL. Elke uitvoering heeft hetzelfde gezamenlijke kleur-/formaatmenu.
- Exact 22 nieuwe producten, één verkochte variant per artikel; ACTIVE én expliciet gepubliceerd op de Webshop.
- [Productregister](products.json): vaste SKU, product-/variant-ID, handle, kleur, maat, verkoopprijs, verpakking, gewicht en openbare bron-URL.
- 70 afbeeldingen verwerkt en READY. Browserproef: tegelbeeld en sfeerbeeld laden; kleurwissel verandert artikel, foto's en leverinformatie.
- Bestaande collecties Tegels, Vloertegels en Terrazzo tegels hergebruikt. Geen nieuwe categorie-, serie- of SEO-landing aangemaakt.

| Formaat | m²-prijs incl. btw | Doosinhoud | Tegels/doos | Doosprijs incl. btw | Gewicht/doos |
| --- | ---: | ---: | ---: | ---: | ---: |
| 60×60 cm | €68,95 | 1,44 m² | 4 | €99,29 | 29,81 kg |
| 100×100 cm | €79,95 | 2 m² | 2 | €159,90 | 44,26 kg |

## Data- en keuzemenucontract

1. Een exact leveranciersartikel blijft een exact Shopify-artikel met één variant. De variantprijs is de **doosprijs**; cart quantity is het gehele aantal dozen. Leveranciersvoorraad is geen eigen magazijnvoorraad.
2. De bestaande `tegels`-template en generieke `bc-porcelanosa-buybox` worden hergebruikt. De naam van die code beperkt de werking niet tot Porcelanosa.
3. `custom.bron_toelichtingen_json.tiles` bevat m²/doos, stuks/doos, m²-/doosprijs, gewicht, leverinformatie en bronbewijs. Native unit pricing is ingesteld op 1 m² en de werkelijke m²-inhoud per verkochte doos.
4. `tiles.group_id` is `COTTO-REVOIR-PARIS-RE-BEL`; `tiles.group_label` is Re-Bel. Elk artikel verwijst met `tiles.group_products` naar alle 22 gepubliceerde producten. Kleur- en maattermen hebben exact dezelfde schrijfwijze binnen de groep.
5. `tiles.color`, `tiles.size`, `tiles.execution`, `tiles.application` en `tiles.look` voeden de keuzes. `custom.complete_specificaties` voedt de tabel; bestaande `bc_filters`-velden leggen maatvoering, kleur, serie en afwerking vast.
6. Bij de volgende serie eerst een complete keuzematrix maken en gaten/verschillende verkoopeenheden beoordelen. Stuksartikelen niet met een verzonnen m²-inhoud in de tegelcalculator stoppen. De huidige groepslus kan maximaal 50 producten betrouwbaar verwerken; grotere groepen vragen een eigen laadstrategie.
7. Voor nieuwe artikelen: eerst SKU/handle-deduplicatie, concepten, readback van prijzen/beelden/specificaties, wederzijdse groepsreferenties, daarna expliciete Webshoppublicatie. Bestaande artikelen gericht bijwerken; `productSet`-lijstvelden niet blind vervangen omdat ontbrekende lijstleden worden verwijderd.

## Voorraad, levering en bronuitzonderingen

De XML is opnieuw rechtstreeks opgehaald op 5 november; prijs, verpakking en gewicht van alle 22 sloten aan op het gecontroleerde werkbestand. Vijf voorraden waren inmiddels gewijzigd. Positieve voorraad toont “Op voorraad bij leverancier”; nulvoorraad blijft bestelbaar met de bronterm “Ongeveer 12 werkdagen”. Er is geen bezorgbelofte van 1–2 werkdagen overgenomen van een ander merk.

De voorraad is een momentopname. Er is **geen automatische feedverversing** ingericht. Voor structurele uitbreiding moet een vervolgopdracht veranderingen gecontroleerd laten bijwerken en handmatige correcties beschermen.

RR6006 mist Mat/Glans in XML maar heeft expliciet `Matt` in de officiële leveranciersexcel. Alle 22 zijn Mat. De EAN van RR6011, `5407007481834`, heeft een onjuist controlecijfer en is bewust niet als barcode gepubliceerd; de bronwaarde blijft in het bronbewijs bewaard. De andere 21 EAN's zijn gecontroleerd en teruggelezen.

Gewichten gelden per verkochte doos. Varianten vereisen verzending, hebben dezelfde bestaande algemene verzendprofielkoppeling als de gecontroleerde Porcelanosa-tegels en zijn niet als eigen winkelvoorraad geteld. Bestaande verzendkosten, Markets, btw en betaalinstellingen zijn niet gewijzigd.

## Winkelwagenaanpassing

Live bleek de bestaande winkelwagen overal een stuklabel te gebruiken en voor deze tegels terug te vallen op een onbekende levertijd. De berekende aantallen en bedragen waren juist, maar de eenheid was onduidelijk.

Vier bestanden lossen dit generiek op voor producten met het bestaande positieve m²/doos-contract:

- `snippets/bc-cart-unit-label.liquid`: “per doos” voor tegels; bestaande vertaling “per stuk” voor overige artikelen.
- `sections/cart-notification-product.liquid`: hetzelfde juiste label in de toevoegbevestiging.
- `sections/main-cart-items.liquid`: hetzelfde label bij normale en afgeprijsde eenheidsprijzen.
- `snippets/bc-cart-delivery.liquid`: dezelfde bewezen tegel-levertijd als op de productpagina; bestaande overige fallback-/Wiesbadenlogica blijft werken.

Er zijn geen nieuwe scripts, stylesheets of vertaalwaarden toegevoegd. MAIN bij deze proef: **196227170570 — BadkamerCity - Verlavio voorraad en levertijd**. Nieuw concept: **196238639370 — BadkamerCity - Re-Bel tegelkeuze**. Dit concept is gebaseerd op die actuele MAIN, zodat de eerder gepubliceerde Verlavio-correctie meegaat.

## Controle en grenzen

- Admin-readback: 22/22 veldsets, prijzen, native eenheidsprijzen, verpakkingen, gewichten en brongegevens gelijk; 22/22 groepslijsten met 22 referenties; 22/22 Webshoppublicatie; 70/70 media READY.
- Echte Chrome, zonder preview: 11 kleuren en twee maten zichtbaar; Blanc 60→100 en Blanc→Caramel behouden de passende andere keuze. Foto's, specificaties en levering wisselen mee.
- 10 m² + 10%: 60 cm geeft 8 dozen, 11,52 m² en €794,32; 100 cm geeft 6 dozen, 12 m² en €959,40. Oppervlakte 0 blokkeert de koopknop. Drie handmatige dozen geven 4,32 m² en €297,87, zonder extra snijverlies.
- Drie dozen RR6002 via de echte productknop toegevoegd, winkelwagenbedrag €297,87 en artikelidentiteit correct; alleen de eigen testregel verwijderd, winkelwagen weer leeg.
- `node scripts/component-audit/cottoceramix-pilot.mjs`: zeven semantische render-/matrixchecks PASS, inclusief alle 286 kleur-/maatwissels, normale artikelen, afgeprijsde prijzen, ontbrekende metadata en ge-escapete leveringstekst.
- Shopify Liquid-validatie: 5/5 bestanden SUCCESS in gecombineerde revisie 2, met meegeleverde documentatiefallback omdat de live documentatiecache niet bereikbaar was.
- Echte previewcart na upload: **PASS** — drie dozen RR6001 voor €297,87; melding én cart tonen “per doos”, de bevestigde leveranciersvoorraad en €68,95/m². Eigen testregel verwijderd; cart leeg. Fysieke telefoon, verzendberekening met afleveradres, checkout en betaling: **NOT_TESTED**.

Herstelpad: alleen de 22 in het productregister genoemde artikelen uit de Webshop halen en op DRAFT zetten; er bestonden geen eerdere Re-Bel-artikelen met die SKU's/handles. Het conceptthema kan ongepubliceerd blijven; er is geen themapublicatie door de uitvoerder. Na eventuele publicatie kan de bewaarde vorige MAIN teruggezet worden. Geen andere producten terugrollen.

De volledige kopie was vooraf 1381/1381 identiek aan MAIN. Na upload heeft het concept 1382 bestanden met exact de vier bedoelde afwijkingen; MAIN bleef 1381/1381 behouden. Echte previewcart en afbeeldingen PASS.

Volgende handeling: eigenaar bekijkt Re-Bel en publiceert **BadkamerCity - Re-Bel tegelkeuze** in Shopify. Daarna uitsluitend de actuele MAIN-rol en de gepubliceerde winkelwagenlabels teruglezen. Tot dat moment zijn de 22 producten live en de winkelwagencorrecties alleen in het concept beschikbaar.

## Gelijktijdige zoekcorrectie behouden

De bestaande zoekbescherming uit SEARCH-01 is byte-exact overgenomen uit concept196116087050 (MD5 `e0783b4ed15e1acc70ff1518cf2b5f20`). Eigen 23 runtimechecks PASS; de vier winkelwagenbestanden zijn ongewijzigd en alle vijf bronbodies exact teruggelezen. Publiceer uitsluitend het gecombineerde **BadkamerCity - Re-Bel tegelkeuze**. Het losse zoekconcept mist de winkelwagenaanpassing en mag daarna niet terug gepubliceerd worden.

**Zoekvindbaarheid OPEN:** de browserproeven op `RR6001` en `Re-Bel` leveren nog nul op. De directe artikelpagina, menu's en bestellen werken. Er is geen oorzaak verondersteld en geen backendindex gewijzigd; vervolg via het afzonderlijke SEARCH-01-onderzoek. Dit is geen verklaring dat Re-Bel al via de algemene zoekfunctie vindbaar is.
