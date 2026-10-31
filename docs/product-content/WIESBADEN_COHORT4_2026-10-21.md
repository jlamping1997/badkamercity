# Wiesbaden cohort 4 — Shopify-updates geverifieerd, 21 oktober 2026

**APPLIED_ADMIN_VERIFIED (43) / QUARANTINED (7) / PUBLIC_STOREFRONT_SAMPLED (7) / VPS_INDEX_NOT_SYNCED.**

Doel: snelheid zonder blind een gestructureerde bronfeed door te schrijven. Door de eigenaar goedgekeurde werkwijze: valideer de makkelijk onderbouwbare producten, zet alle uitzonderingen tot de laatste ronde apart.

## Concrete uitkomst

- **50 unieke, nieuwe Wiesbaden-SKU’s:** 20 doucheslangen, 30 douchearmen. Geen overlap met 150 eerder behandelde artikelidentiteiten.
- **43** producten in Shopify bijgewerkt, bij elk SKU/merk/één variant/producttype/collectiepad vóór schrijven gecontroleerd. Voor elk artikel gecontroleerde leveranciergegevens uit de officiële 19-oktoberbron.
- **43 private herstelkopieën** vóór mutatie opgeslagen als `bc_rollback.pre_content_v1`.
- Bij alle 43: nieuw eigen `descriptionHtml`, aparte Shopify SEO-titel en metabeschrijving, `custom.complete_specificaties` (gegroepeerde geverifieerde feiten), `custom.card_title`, `bc_data.content_review`. Beschrijving heeft geen extra dubbele oude specificatietabel en geen EAN.
- **43/43 onafhankelijke Shopify Admin-readbacks geslaagd**: beschrijving, SEO, maat-/aansluitregels, reviewstatus, backup, variantprijs, status, URL-handle, technische-documentenmetafield en bestaande filtermanifesten.
- **7** artikelen aan centrale quarantaine toegevoegd. SKU 24.3812 heeft tegenstrijdige montagemodellen; zes overige douchearmen missen bevestigde aansluitmaat in hun originele fabrikantgegevens. Geen wijziging van hun Shopify-status.
- **7 publieke HTML-productpagina’s nagelezen**: twee pilotproducten plus vijf verschillende uitvoeringen; zichtbaar SEO-title, fabrikantnummer, tekst en productspecificaties.
- **Geen** aanpassing van voorraad, prijs, handles, media, variant-ID, oorspronkelijke Shopify-producttitels of bestaande technische documenten.

## Quarantaine (allemaal centraal geregistreerd)

| SKU | Reden |
| --- | --- |
| 24.3812 | Muurbevestiging in titel, maar fabrikantveld model = plafondmontage |
| 29.2862, 29.2863 | Officiële bron geeft geen aansluitdraaddiameter op |
| 29.3852, 29.3863 | Officiële bron geeft geen aansluitdraaddiameter op |
| 29.5884, 29.5885 | Officiële bron geeft geen aansluitdraaddiameter op |

Canoniek register: `docs/product-content/wiesbaden/quarantine-register-2026-10-21.json`. Totale merkstatus na vier batches: **99 toegepast / 100 in quarantaine / 1 eerder beschermd = 200 behandelde SKU’s** uit de gedateerde groep exact gematchte leveranciersproducten.

## Onderbouwing / grenzen

- De op 19 oktober gecachte fabrikantpagina's hebben bij collectie het bewijs HTTP 200 en leverancier-SKU, naam, type en specificaties. Op 21 oktober gaf een nieuwe live fabrikantprobe HTTP 503, via openbare zoekresultaten waren o.a. 24.3807 en 24.3811 wel herkenbaar. Geen claim van een complete live hercrawl.
- Uitzondering 24.3807: fabrikant noemt een kunststof binnenkern met RVS/metalige omvlechting; in tekst expliciet genuanceerd, geen onjuiste massieve-metalen slang beloofd.
- Geen fysieke mobiele browser-/checkouttest, PDF-tekeninganalyse per product, Search Console-rankingclaim of actuele externe Typesense/VPS-indexwrite. De nu live Shopify-producttitels/zoekfacetten op externe service kunnen achterlopen.
- Het review-statusveld zegt dat het goedgekeurde feitensubset mag renderen; niet dat voorraad of het volledige assortiment klaar is.
- **Verdere productupdates alleen met volledige backup/readback**; uitgesloten/gerede producten nooit opnieuw overschrijven.

## Efficiënt vervolg

Nieuw read-only script `scripts/wiesbaden-next-cohort.py` selecteert exact een nieuwe groep via bronarchief + hetzelfde quarantaine-register en slaat alle reeds toegepaste of beschermde SKU's over. **Zes offline unit tests geslaagd; op de lokale testfixture twee keer dezelfde selectie zonder drift.** Volgende 50 kandidaten zijn offline voorbereid als 31 hoofddouches + 19 handdouches. Voor die groep zijn nog **nul** productmutaties uitgevoerd.

Exact volgende uitvoerhandeling: valideren van dat volgende cohort op fabrikantfeiten/technische toebehoren en opnieuw een veilige apply-batch draaien; parallel de externe zoekindexsynchronisatie afzonderlijk afmaken.
