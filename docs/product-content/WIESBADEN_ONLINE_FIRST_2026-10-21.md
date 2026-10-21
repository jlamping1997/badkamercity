# Wiesbaden — eerst online, verrijken daarna (21 oktober 2026)

**VERIFIED_SHOPIFY_ADMIN / VERIFIED_STORE_FRONT_SAMPLE / REVIEW_LATER_IS_NOT_UNPUBLISH.**

## Nieuwe merchantbeslissing (hoogste prioriteit)

De eigenaar wil éérst alle beschikbare Wiesbaden-artikelen verkoopbaar ONLINE. Bestaande leveranciersteksten mogen voorlopig onvolledig zijn; latere correcties, technische documenten, ALT-teksten, filters, SEO, voorraad-/levertijdkoppelingen en mobiele wijzigingen worden in aparte verbeter-rondes uitgevoerd. **Quarantaine is een afvink-/reviewlijst en heeft geen Shopify statusactie.** Stop niet langer een gezond, positief geprijsd product wegens onbelangrijke ontbrekende specs. **Nooit** fictieve prijs, artikelidentiteit of niet-bestaande pakketcomponenten verkopen.

## Live geverifieerde resultaten

- Bevroren bronexport 19 oktober (vergeleken met Shopify toen): **2.457 Wiesbaden leveranciersproducten** = 2.240 exact gematchte bestaande Shopify-SKU's + **217 niet eerder gevonden fabrikant-SKU's**. Daarnaast 25 destijds bestaande producten zonder leveranciermatch; overlap/freshness blijft beheerpunt.
- Direct vóór nieuwe Shopify-writes gaf de Admin GraphQL count **2.265 ACTIVE Wiesbaden-producten** (alle Wiesbaden actief, 0 DRAFT). Bestaande 106 verwerkingsquarantaines waren niet gearchiveerd en blijven online.
- **24 totaal nieuwe producten** in Shopify aangemaakt met juiste vendor, SKU=fabrikantnummer, actuele fabrikantidentiteit/titel, prijs uit de reeds gehanteerde fabrikantadviesprijs *1,21, één variant met voorraadtracking UIT, productomschrijving, echte leverancier-productfoto (uitzondering hieronder), passende primaire collectie, en daarna **expliciet gepusht naar Online Store publication `283427864842`**. *ACTIVE alleen is niet voldoende*, feitelijke product-URL én publicatiereadback waren verplicht.
- **24/24 afzonderlijk uit Shopify herlezen:** `status=ACTIVE`, Online Store `isPublished=true`, product-URL bestaat, juiste SKU/prijs, niet-getrackte voorraad, minstens één `MediaImage READY` en minimaal één passende collectie. Nieuw getelde Wiesbaden ACTIVE = **2.289 exact** (+24).
- Onder meer: 36.4028 en 36.4030 Laro dubbele meubelwastafels, 38.4047 Novira onderkast, 20.3404 Sita inloopdouche, 41.3558 Elara WiFi radiator, 33.4422 UniMatch fonteinsifon, en alle WiFi vloerverwarmingssets **41.3640 t/m 41.3657** (18 SKUs). Voor deze reeks door SKU exact fabrikantdatabron bevestigd: oppervlakte 1–5 m², 150 W/m², wit/zwart WiFi-thermostaat. Voor elk positieve productprijs, 1 READY-image.
- Zeven overkoepelende collectiewrites voor nieuwe producten geverifieerd: wastafels, badkamermeubels, verwarming, douches, douchewanden, radiatoren en toebehoren, naast hun primaire collecties.
- Vijf publieke storefront-productpagina's live HTML gelezen: fabrikantnummer, EUR-prijs, omschrijving en media. Na beeldfix via Admin-status READBACK bevestiging.

### Bijzondere beeldcorrectie

- **33.4422**: leverancier-productfoto met >25 MP was door Shopify daadwerkelijk `FAILED`; product had een lege gallery ondanks de mediarecord. De mislukte media is verwijderd en vervangen door de correcte **fabrikant-technische lijntekening** via Shopify CDN. Daarna Admin `MediaImage READY` bevestigd. Product online; later een geoptimaliseerde echte productfoto gebruiken. Niet claimen dat dit SKU al een commerciële hero-foto heeft.

### Openstaande bronartikelen

- Uit originele 217 kandidaten nu **24 online**, **165 andere kandidaten met een positieve fabrieksadviesprijs en afbeeldingsbron wachten op basispublicatie**.
- **28 nieuwe bron-SKU's zonder bruikbare positieve prijs** zijn aan het centrale quarantaineregister toegevoegd (`new_source_candidates_missing_price_28`). Veelal 'bestaande uit'-sets zonder zelfstandige complete verkoopprijs. Deze 28 zijn **nooit aangemaakt**; worden pas online gezet na betrouwbaar prijs-/onderdeelbewijs. Dit is onderscheiden van de eerdere 106 reeds online bestaande, alleen voor review uitgezonderde artikelen.
- Centrale quarantine is nu **134 checklistitems (106 bestaande ONLINE, 28 nog NIET AANGEMAAKT wegens ontbrekende prijs)**. De eerdere 143 bestaande verbeterde producten + 24 nieuwe = 167 eerder daadwerkelijk gemodificeerde/aangemaakte Shopify-objecten; tel niet dubbel als 250 reeds bezochte SKU's.
- Er is **geen** bulkupdate gedaan van andere 2.265 oorspronkelijke artikelen. Geen themawijziging of VPS-indexupdate, geen voorraad/levertijdclaim, geen zoek-/filterafronding.

### Prijsdiscipline

De nieuwe 24 volgen de tot nu toe gehanteerde winkelprijsregel **adviesprijs component EXCL_TAX_SELECTED_BY_MANUFACTURER_COMPONENT → ×1,21 naar Shopify EUR bruto**. Administratief is die consistent met de oorspronkelijke Wiesbaden-prijsfeed, maar het markt- en BTW-basisbeleid is hiermee niet onafhankelijk fiscaal gevalideerd. Geen willekeurig ingevoerde of €0-bedragen; prijsberekening en commerciële adviesprijsvergelijking later apart controleren voordat de resterende 165 grootschalig worden gepubliceerd.

## Machineleesbaar + bronprivacy

- `docs/product-content/wiesbaden/ONLINE_FIRST_PUBLISHED_2026-10-21.json`: **24** geverifieerde SKU's met daadwerkelijke Shopify object-ID, URL, prijs, collectie en gerede afbeeldings-URL.
- `docs/product-content/wiesbaden/quarantine-register-2026-10-21.json`: 134 pending later-review SKUs gesplitst ONLINE/existent en NIEUW/niet aangemaakt.
- Lokale export buiten publieke Git: `/mnt/data/wiesbaden_online_first/Wiesbaden_online_eerst_20261021.html` = doorzoekbaar 217-artikelenoverzicht. De offline Pythonverwerker `wiesbaden-online-first-plan.py` en private volledige leveranciersplan bevatten bron-/adviesdata en blijven buiten de publieke repo en kunnen uit de gesprekbijlagen worden overgenomen.

## Volgende uitvoerhandeling

**Importeer de 165 overige positief geprijsde, niet eerder gematchte SKU's in gecontroleerde groepen** vanuit de bevroren bronlijst. Voor iedere SKU opnieuw live bevestigen dat deze niet al in Shopify bestaat; maak een enkele variant (SKU=fabrikant), voeg productfoto/collecties toe, publiceer expliciet naar Online Store, toets `READY`-beeldverwerking + positieve prijs en publieke URL. Review-opmerkingen blijven bij import bewaard; verwijder niets uit verkoop wegens bijzaken. Fouten/ontbrekende foto/prijswerking in de centraal samengestelde reviewlijst opnemen. Pas daarna bestaande productteksten in 500+ cohorten verder verrijken; Search/Typesense eerst later in aparte fase.

**Handeling eigenaar nu:** niets nodig om door te werken. Geen nieuwe API-sleutel of leveranciersexport vereist.
