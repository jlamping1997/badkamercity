# Korte kaarttitels en duidelijke producttitels

10 november 2026. Voorstel, nog geen Shopify-titelwrite. Uitwerking van [PRODUCT_CONTENT_PLAN](../../PRODUCT_CONTENT_PLAN.md); geen nieuw parallel titelsysteem.

## Vaste vorm

| Gebruik | Bron | Schrijfregel |
| --- | --- | --- |
| Productkaart | Bestaand custom.card_title, met product.title als terugval | Begin met het producttype. Voeg alleen een relevante maat, montage of onderscheidend model toe. Merk staat al apart op de kaart. Een serienaam zoals &More is geen bruikbare eerste uitleg. |
| Productpagina | Bestaand product.title / H1 | Merk, relevante serie/model, producttype, onderscheidende bevestigde maat/montage en exacte afwerking. Leesbaar, geen hele specificatietabel. |
| Google-title | Bestaand Shopify SEO-veld | Afzonderlijke zoekresultaattitel; niet automatisch gelijkmaken aan de H1. In afstemming met de actieve SEO-chat. |

Geen hard afkappen op een woordlimiet. Korte titel moet op een telefoon snel te begrijpen zijn. Geen artikelnummer/EAN of kleurreeks in de korte titel; behoud essentieel onderscheid tussen complete set, afbouwdeel en los onderdeel. Product-URL’s, SKU’s en bestaande keuzegroepen blijven dezelfde identiteit houden.

## Eerste echte proef: Hotbath BAA16

Alle 12 actuele Hotbath-badgrepen uitgelezen, paginering afgerond. Eén modelfamilie, 12 afwerkingen. Geen ervan heeft custom.card_title. De externe kaart haalt merk en afwerking uit de producttitel; daardoor blijft ‘&More badgreep’ over. De native kaart en andere terugvalroutes tonen de oorspronkelijke langere titel zonder merk. Dit verklaart het verschil in presentatie.

| Veld | Huidig voorbeeld | Voorstel |
| --- | --- | --- |
| Kaart | &More badgreep | Badgreep 30 cm |
| Productpagina | Hotbath &More badgreep – chroom | Hotbath &More BAA16 rechte badgreep, hartmaat 30 cm – chroom |
| Andere uitvoering | Hotbath &More badgreep – geborsteld gunmetal PVD | Hotbath &More BAA16 rechte badgreep, hartmaat 30 cm – geborsteld gunmetal PVD |

30 cm en de rechte vorm staan in de actuele SKU-gebonden complete_specificaties; de filter_manifest bevestigt lengte 300 mm. De officiële fabrikantcontrole van de maatbetekenis is nog open. Dus de tabel is een controleerbaar voorstel, geen nieuw bewezen fabrikantgegeven of uitgevoerde wijziging. [Alle 12 voor/na-voorstellen en gestructureerd bronbewijs](hotbath-title-pilot.json).

## Batches

1. Eerst 5 artikelen uit deze familie: chroom, gunmetal PVD, geborsteld messing, Tuscan bronze en mat wit. Beoordeel productsoort, lengte versus hartmaat, vorm en exacte afwerking. Geen ontbrekende eigenschap raden.
2. Na controle de resterende 7 afwerkingen van dezelfde familie. Geen winkelbrede opdracht afleiden uit één geslaagde familie.
3. Daarna circa 25 artikelen verdeeld over andere Hotbath-functies: wastafelkraan, inbouw-afbouwdeel, complete doucheset, losse douchekop en accessoire. De setinhoud moet uit de SKU-bron blijken.
4. Daarna per merk en productfamilie batches tot circa 100 artikelen, kleiner bij twijfel. Wiesbaden-keuzedata blijven bij de andere werkstroom; geen familie-ID’s of opties tegelijk aanpassen.
5. Alleen geslaagde, opnieuw uitgelezen records afronden. Onvolledige of tegenstrijdige gegevens krijgen HOLD met reden; geen eindeloos opnieuw onderzoek van al afgeronde artikelen.

Per record: product-ID, variant-ID/SKU, merk, huidige title/card_title met versie/digest, voorstel, bron, reden, status en herstelgegevens. Bestaande definities hergebruiken na type-/toegangscontrole; geen extra long-title-veld aanmaken.

## Controle vóór en na een write

Verse identiteit en huidige waarde lezen; gewijzigde records sinds het voorstel niet overschrijven. Voor kortetekstvelden compareDigest gebruiken waar ondersteund. Alleen title en card_title wijzigen binnen de goedgekeurde batch; geen handles, prijzen, omschrijvingen, voorraad of SEO-velden meenemen.

Controleer native collectiekaart, externe filterkaart na actuele data-hydratatie, zoeken, PDP, sticky koopbalk en winkelwagennaam. Kleur-/maatwissel moet hetzelfde juiste artikel met bijbehorende foto, SKU en prijs blijven tonen. Titelafhankelijke groepsmatching eerst onderzoeken. Geen titelbatch publiceren zolang een relevante keuze daardoor verkeerd schakelt.

**Volgende handeling:** broncontrole en eigenaarreview van de vijf concrete BAA16-voorbeelden; daarna pas toepassen en teruglezen. Deze documentatie is geen uitgevoerde productbatch.
