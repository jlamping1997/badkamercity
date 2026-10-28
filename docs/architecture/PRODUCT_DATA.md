# Productdata — privé-export en openbaar datamodel

**Exportvenster 28 oktober 2026 circa 02:10–02:43 UTC.** De eigenaar heeft een export gevraagd van alle gegevens die we per product hebben. Uitvoer: alle 11.343 via de huidige Shopify-verbinding bereikbare producten en 11.343 varianten, zonder status-/namespacefilter, met de geselecteerde productoppervlakken hieronder. Dat is geen claim dat ieder extern systeem of elk API-veld is geëxporteerd.

## Waar zoeken

Het private pakket heet `badkamercity-productdata-2026-10-28.zip`. Vraag de eigenaar om toegang; de publiek toegankelijke Git-repository bevat geen ruwe productwaarden, kostprijzen, voorraadregels, leveranciersinformatie of privé-downloadlink. In het pakket staat een Nederlandse `LEESMIJ.md` met zoekvoorbeelden.

| Pakketonderdeel | Inhoud |
| --- | --- |
| `products.jsonl` | Eén samengesteld product per regel, met varianten, metafields, media, collecties en publicatiekoppelingen |
| `products.sqlite` | Volledige records als JSON plus relationele zoektabellen |
| `field-dictionary.json` | 447 waargenomen veldpaden, typen, nulls en aantallen |
| `metafield-register.json` | 253 eigenaar/namespace/key/typecombinaties en vulling |
| `raw-api/` | Oorspronkelijke responses, schema's, collectievoorwaarden, 9 menu's en voor-/nacontroles |
| `queries/` | Selecties en grenzen van de gebruikte query's |
| `theme-runtime-data/assets/` | 674 JSON-assets uit MAIN; inclusief gegenereerde keuzes en back-upkandidaten |
| `validation.json`, `SHA256SUMS.txt` | Tellingen, integriteitsresultaten en bestandshashes |

## Model en sleutels

| Entiteit / SQLite-tabel | Sleutel / relatie | Telling |
| --- | --- | ---: |
| products | Shopify Product GID | 11.343 |
| variants | Variant GID → product_id | 11.343 |
| metafields | Metafield GID + owner_id/owner_type; namespace + key + type | 241.064 |
| media | Media GID + raw_json | 32.065 |
| product_media | product_id + media_id + position | 32.065 |
| collections | Collection GID | 226 |
| product_collections | product_id + collection_id | 39.064 |
| inventory_levels | InventoryLevel GID → variant, inventory item, locatie | 11.343 |
| references_data | GenericFile of Metaobject GID | 19 |

Productrecords bewaren identiteit, tekst/HTML, merk/type/status/tags, template, categorie/SEO, datums, opties, prijsbereiken en de variantdetails. Variantrecords bewaren SKU/barcodes, prijzen, inventaris/verkoopstatus, belasting/verzending, gewicht, oorsprong/douane, toegankelijk kostenveld, voorraadstaten per locatie, metafields, mediaverwijzingen, deliveryProfile en componentkoppelingen. De uitgebreide selected-fieldstructuur is navolgbaar via query's en veldregister; raw_json voorkomt verlies door alleen een smalle tabel te leveren.

ID's, SKU's, barcodes en geldbedragen blijven strings. Een ontbrekende waarde, null, lege string, false en nul zijn verschillend. Kosten null betekent niet kosten nul. `metafields.value` is de oorspronkelijke serialisatie; `jsonValue` bewaart de door Shopify geïnterpreteerde waarde. Geen lege specificaties aangevuld of eenheden/leveranciersregels verzonnen.

## Controle en beperkingen

[data-validation.json](evidence/2026-10-28-doc01/data-validation.json) bevat alleen veilige aantallen. Begin-/eindtellingen zijn EXACT en sluiten aan; IDs zijn uniek; lagen sluiten aan; geen verweesde varianten; aantallen varianten/media kloppen per product; geen onbehandelde geneste vervolgpagina's; SQLite integrity_check is ok en foreign_key_check heeft nul fouten. De vier offline builderchecks testen dat onvolledige joins/paginering falen en stringidentiteit/bedragen/nulls behouden blijven. De vijf scannerchecks blijven slagen.

De export is niet atomair. Constante tellingen bewijzen geen constante prijzen of voorraad gedurende het venster. Media/documenten zijn metadata en URL's: 32.065 mediarecords, 17 GenericFile-records en 2 gekoppelde metaobjects; binaire bestanden zijn niet gedownload. URL's kunnen later wijzigen of verlopen. De enkele aanwezige winkeltaal is nl.

Publicatiekoppelingen zijn de ontvangen resourcePublicationsV2-selectie met standaard APP-catalogus. Markt-/B2B-contextprijzen en volledige kanaalinrichting vallen buiten deze export. Niet bereikbare app-private velden, externe leveranciers-/VPS-bronnen, niet gekoppelde bestanden, historische productversies en niet geselecteerde API-oppervlakken zijn niet inbegrepen. De 674 JSON-themeassets bevatten ook afgeleide/back-updata en gelden niet automatisch als actuele bronwaarheid. Dit is geen import-/herstelbestand of toestemming voor bulkmutaties.

## Opnieuw samenstellen

Op de actieve branch: `scripts/build_product_data_package.py`. Alleen Python-standaardbibliotheek; geen netwerk of mutaties. Het script combineert opgeslagen responses, weigert onvolledige joins en geneste paginering, maakt JSONL/SQLite/veldregister en kopieert de private herkomstlaag. De output moet buiten de publieke repo staan en de doelmap mag nog niet bestaan.

```bash
python3 scripts/build_product_data_package.py --source /pad/naar/opgehaalde-bronnen --output /privaat/nieuw-productpakket
python3 -m unittest discover -s scripts -p 'test_product_data_package.py' -v
```

Dit is een **offline builder**, geen autonome volledige Shopify-downloader. Voor een nieuwe export moeten MAIN, actuele schema's, rechten, alle pagina's en voor-/nacontroles opnieuw gelezen worden. Start geen automatische import of externe synchronisatie op basis van dit pakket.
