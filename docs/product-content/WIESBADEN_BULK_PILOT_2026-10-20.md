# Wiesbaden — uitvoering eerste 50-SKU bulkproef, 20 oktober 2026

**Status: BULK_CODE_ON_ACTIVE_GIT_BRANCH / LOCAL_DRY_RUN_COMPLETED / NO_ADMIN_WRITES.**

De eerder afgesproken alleen-lezen bulkproef is **uitgevoerd**. Geen nieuwe scrape of nieuw ontwerptraject. Behouden bron: private BadkamerCity_Wiesbaden_datarun_20261019.zip.

## Geïmplementeerd

- Werkbranch: fix/product-cards-2026-10-14 in jlamping1997/badkamercity.
- Python-verwerker: scripts/wiesbaden-bulk-preview.py. Standaardbibliotheek, geen Shopify/VPS-credentials of write-API's.
- Regressietests: scripts/test_wiesbaden_bulk_preview.py (13 offline tests).
- Input uit bestaande product-master.jsonl, category-import-proposal.json, complete-specifications-proposal.json en filter-field-proposal.json in de datarun-ZIP.
- Product-JSON per SKU: bron-SHA256, URL, bronmoment, getypeerde feiten, identiteit, gegroepeerde specificaties, SEO/tekstvoorstel, categorie-/breadcrumbvoorstel, getypeerde filters, harde blokkades en redactionele waarschuwingen.
- Eerder beoordeelde items worden niet opnieuw toegepast; geen EAN, privé inkoopdata, garantie/levertijd of verzonnen setinhoud.
- Idempotente write-if-changed: tweede run met identieke input hergebruikt alle 50 productbestanden.

## Offline resultaat uit bestaande broncache

| Status | Aantal |
| --- | ---: |
| EDITORIAL_REVIEW_REQUIRED | 31 |
| BLOCKED_FACTS_OR_IDENTITY | 18 |
| EXISTING_REVIEWED_DO_NOT_REPLACE | 1 |
| **Totaal** | **50** |

Er zijn 9 productprofielen, 736 getypeerde bronfeiten (waaronder echte false) en 193 getypeerde filterkandidaten. De filters zijn nog niet live toegepast.

Belangrijkste gevonden blokkades: 10 onverenigbare categorietoewijzingen, 8 onbewezen onderdeelcompatibiliteiten, 3 breadcrumb-identiteitsissues, 2 sets met onzekere inhoud. SKU 29.8007 bevat een echte kleur-/producttype-tegenstrijdigheid; 24.3710 blijft de goedgekeurde referentie. Controletypen overlappen, dus deze aantallen zijn niet optelbaar als unieke geblokkeerde producten.

**Testbewijs:** 13 lokale tests geslaagd op de stand-alone verwerker met originele datarun ZIP. Tweede offline run: 0 opnieuw gegenereerd, 50 hergebruikt. De actieve GitHub-branch bevat de verwerker en regressietest, met readback van het bestand. Een aparte Windows-run van de committed variant is NOT_TESTED. Er zijn geen Shopify-, theme- of VPS-mutaties uitgevoerd.

## Uitvoering op Windows

Controleer eerst de werkrepo en lokale wijzigingen; doe geen reset/clean. Het eigen source-ZIP-pad is afhankelijk van waar de gebruiker het bestand heeft neergezet.

~~~powershell
python scripts/wiesbaden-bulk-preview.py --input "C:\Users\LauraHarrySuiker\Downloads\BadkamerCity_Wiesbaden_datarun_20261019.zip" --output "C:\Users\LauraHarrySuiker\Downloads\Wiesbaden_bulkproef"
python scripts/test_wiesbaden_bulk_preview.py "C:\Users\LauraHarrySuiker\Downloads\BadkamerCity_Wiesbaden_datarun_20261019.zip"
~~~

Het voorbeeldpad voor het ZIP is niet vanaf de Windows-pc vastgesteld. De uitvoer is alleen een eigen offline map. De extra private reviewbundel bevat een zoekbaar proef-review.html, review-50.csv, manifest.json en 50 individuele SKU-dossiers; deze worden NIET naar de openbare GitHub-repository gekopieerd.

## Wat nog openstaat

- Alle 31 inhoudelijke concepten vereisen menselijke redactie; er zijn dus niet 31 kant-en-klare gepubliceerde productteksten.
- De externe Typesense-/VPS-route, originele zeven titelcorrecties en Filter-Index-readback blijven ongetest voor deze batch.
- Bestaande collectie-ID's, feitelijk lidmaatschap en Shopify-filterdefinities moeten vers herbevestigd worden voordat enige nieuwe live write plaatsvindt.
- 29.8007 en 41.3540 blijven bekende holds; 41.3540 valt buiten de 50-kraanselectie.
- Er zijn geen product-/prijs-/voorraad-/afbeelding-/publicatiestatus-/handle-/collectie-/themamutaties.
- De brontelling van 2.240 exact gekoppelde bestaande Wiesbaden-producten betekent niet dat 2.240 teksten gevalideerd zijn.

**Eén volgende implementatiehandeling:** alle 50 voorstellen redactioneel kalibreren en de 18 blockers per foutgroep behandelen. Voer pas een kleine afgebakende echte batch uit nadat rollback en externe index-write/readback aantoonbaar werken.
