# Wiesbaden gecontroleerde productinhoud — contract v1

Ingevoerd20oktober2026 voor zeven volgende producten in concept195491168522. Zie [batchdossier](WIESBADEN_PROEFGROEP_2_2026-10-20.md) en actuele centrale status voor publicatie. MAIN195488317706 is in deze uitvoering niet veranderd.

## Gegevens en eigenaar

| Metafield | Type | Functie |
| --- | --- | --- |
| custom.complete_specificaties | json | Gegroepeerde eigenschappen met stabiele key, Nederlands label en feitelijke value |
| custom.card_title | single_line_text_field | Actuele korte titel voor bestaande Shopify/API-kaartkoppeling |
| custom.technische_documenten | list.url | Alleen bevestigde HTTPS-documentlinks; geen fictieve bijlagen |
| bc_data.content_review | json | Controlemarker en toegestane specs/categoriepad voor deze productidentiteit |

De nieuwe PRODUCT-definitie bc_data.content_review heeft ID435276939530. Geen extra storefronttoegangsinstelling aangezet. Andere definities bestaan al; geen migratie van specs.* of oude filtermanifesten. De marker wordt door de merchant-owned Liquidcontext gelezen.

Voorbeeldstructuur (waarden illustratief, geen uitvoerplan):

```json
{
  "schema": "wiesbaden-content-v1",
  "status": "ready",
  "product_id": "10657255489802",
  "sku": "32.3411",
  "spec_keys": ["fabrikantnummer", "merk", "productsoort"],
  "category_handles": ["wastafels", "opzetwastafels"],
  "source_urls": ["https://www.wiesbaden.nl/"],
  "reviewed_date": "2026-10-20",
  "omitted_facts": []
}
```

product_id is een numerieke ID als string, geen ShopifyGID. Alleen toegestane spec_keys verschijnen in de gecontroleerde tabel. Source_urls/datum/omitted_facts dienen als overdracht; zij zijn geen automatische claim dat alles door Liquid wordt gevalideerd.

## Scope en fallback

bc-wiesbaden-reviewed-scope controleert vendorwiesbaden, slechts één defaultvariant, JSON-specificaties en daarin fabrikantnummer exact gelijk aan de huidige SKU. Nieuwe gecontroleerde scope vereist schemawiesbaden-content-v1, statusready, exact dezelfde SKU én stringproduct-ID, plus minstens één spec_key. Anders geen nieuwe scope.

Originele24.3710 is een expliciete bestaande pilotuitzondering en behoudt de oude whitelisted33specificaties. Bij niet-passende reviewdata geeft de ongewijzigde specsrouter de bestaande mapped fallback weer. Dit is geen automatische goedkeuring van andere Wiesbaden-/JEE-O-data. Multi-variantproducten zijn buiten dit contract en vereisen apart ontwerp.

bc-product-breadcrumbs leest de gecontroleerde category_handles, gebruikt native collections en controleert werkelijk lidmaatschap vóór een link. Het pad selecteert bestaande categorieën; dit schrijft geen collectielidmaatschap of Shopify-taxonomie. De eerste pilot behoudt zijn goedgekeurde drie links.

bc-product-documents gebruikt dezelfde scope en alleen list.url. Dubbele URL’s worden samengenomen, niet-HTTPS wordt overgeslagen, echte bestandsextensie bepaalt zichtbaar type. Tekeningen kunnen JPG zijn; noem ze geen PDF. Bestaande Sunshower-rijvormgeving wordt hergebruikt. Geen onjuiste generieke beloftes over documentbeschikbaarheid.

ready betekent dat deze controleerbare inhoud in deze route mag renderen; onbekende maten, historische filterwaarden, voorraad, prijsstrategie en commerciële lancering worden daarmee niet compleet verklaard.

## Schrijf- en bewijsprocedure voor een volgende batch

Controleer eerst actuele centrale status, MAIN, Adminidentiteit/varianten/collecties/metafielddefinities en fabrikantbewijzen. Maak een private originele herstelkopie. Bewaar alleen eigen tekst, feiten en bronprovenance in publieke documentatie. Gekopieerd fabrikantproza/volledige Admin-snapshots blijven privé.

Bereid complete_specificaties, eigen titel/proza/SEO, kaarttitel en documentlinks voor. Onzekere/conflicterende facts weglaten en apart registreren; producten met een onopgelost kernconflict apart houden. Reviewmarker bindt dit aan de exacte productidentiteit en gekozen bestaande categorieën. Schrijf met actuele compareDigest of expliciet null voor aantoonbaar afwezige metavelden; stop bij fout/conflict. Lees alle gewijzigde velden en beschermde product-/variant-/collectie-/mediawaarden onafhankelijk terug.

Controleer echte Shopify-HTML, reguliere browser, titelbrug en externe SKU-/tekst-/filterzoekroute. Een goede korte kaarttitel is geen bewijs dat de zoekindex is vernieuwd. Deze batch heeft de index niet geschreven; [titelcorrectie](wiesbaden/proefgroep2/INDEX_TITLES_RUN.md) staat nog open.

## Bestanden en rollback

Gewijzigde snippets: bc-product-breadcrumbs, bc-product-documents, bc-wiesbaden-reviewed-specs; nieuw bc-wiesbaden-reviewed-scope. De ongewijzigde bc-product-detail-specs-router vangt lege gecontroleerde output op. Geen nieuwe CSS, router, hoofdsectie of Sunshowercode. Exacte before/afterhashes staan bij het batchbewijs en de toepasbare patch.

Verwijderen/opschorten van content_review bij een nieuw product schakelt de nieuwe scope uit en laat de bestaande mapped fallback over; het maakt geen Admintekst-/SEO-mutatie ongedaan. Rollback van het thema is afzonderlijk van productdata. Herstel productvelden alleen uit de private originele backup na verse vergelijking met de toegepaste situatie; niet blind een later bewerkte productinhoud overschrijven. De VPS heeft een eigen aparte titelsbackup/restore als het script later wordt uitgevoerd.
