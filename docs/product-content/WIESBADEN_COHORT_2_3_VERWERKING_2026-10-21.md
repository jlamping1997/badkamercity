# Wiesbaden — uitvoering cohort 2 en 3, 21 oktober 2026

**PARTIAL_ADMIN_APPLIED / QUARANTINE_REGISTER_VERIFIED / VPS_INDEX_NOT_SYNCED / NOT_BRAND_COMPLETE.**

De gebruiker heeft opdracht gegeven betrouwbare Wiesbaden-producten te verrijken en twijfelgevallen in een centrale Git-quarantaine te zetten tot de eindronde.

## Gecontroleerde voortgang

- Cohort 1 (50): **6** producten eerder aangepast, **43** in quarantaine (39 uitgesteld + 4 technische uitzonderingen), **1** reeds goedgekeurd referentieproduct 24.3710 beschermd.
- Cohort 2 (volgende 50): **23** live productaanpassingen, **27** in verwerkingsquarantaine (19 bestaande blokkades + 8 extra).
- Cohort 3 (nieuwe 50): **27** live productaanpassingen, **23** in verwerkingsquarantaine (19 bestaande blokkades + 4 extra).
- Totaal over 150 behandelde posities: **56** live bijgewerkt, **93** apart gezet voor eindcontrole, **1** referentie beschermd. Geen nieuwe productaanmaak.
- Canonieke machineregistratie: `docs/product-content/wiesbaden/quarantine-register-2026-10-21.json` (93 unieke SKU's, 56 toegepaste SKU's). Mutatie bevestiging en readback op 21-10-2026.

## Welke updates?

Bij de twintig nieuw toegepaste artikelen in cohort 2 en zevenentwintig in cohort 3 zijn beschrijving-HTML en afzonderlijke Shopify SEO-titel/-omschrijving, `custom.complete_specificaties` (getypeerde en gegroepeerde kernfeiten), `custom.card_title` en `bc_data.content_review` gebruikt. Producttitel (native title), SKU, variantprijs, voorraad, productstatus, producthandle, technische document-metafields en collecties zijn daarbij niet aangepast. De drie eerder toegepaste cohort-2 artikelen en zes uit cohort 1 kregen oorspronkelijk vooral nieuwe titel en beschrijving; claim GEEN identieke volledigheid op alle 56.

Voor elk van de 47 nieuwe writes is vóór schrijven een leverancier-/SKU-/kleuren-/producttypecheck gedaan en Shopify identiteit/collections/varianten gelezen. Een afzonderlijk privé product-backup-metafield `bc_rollback.pre_content_v1` is vóór de nieuwe writes opgeslagen. Daarna zijn writes en basale Admin-readbacks uitgevoerd; bij een gedeeltelijke mutation-breuk is de laatste 29.7932 apart afgerond en geverifieerd. De bronmaat `8 mm` bij 29.4103 is letterlijk zo vermeld door de leverancier; geen zelfstandige fysieke maatmeting gedaan.

Vier publieke storefront-URL's zijn aanvullend tekstueel via live fetch nagekeken (29.3930, 22.3708, 29.4103, 29.4115): SEO-titel, SKU, zichtbare spec-rijen. **Niet** op elk product een mobiele browser-, PDF-dimensie- of onafhankelijke cataloguscontrole gedaan. Een fabrikantentabel kan aantoonbaar fouten bevatten en één bron is geen wiskundige 90%-zekerheid.

## Belangrijke beperkingen

- Externe Typesense/VPS zoek-/filterindex **niet gesynchroniseerd of geverifieerd**; korte zoekkaarttitels uit Shopify kunnen actueel zijn terwijl fulltext-index oud blijft. Niet als volledig SEO/filter-afgerond rapporteren.
- Geen collectielidmaatschapsaanpassing; bestaand categoriepad blijft indien ongeschikt in quarantaine.
- Alle bronversies, lange oorspronkelijke Shopify HTML en eventuele aanmeldgegevens buiten de publieke Git-repo houden. Product-backup bevat privacygevoelige broninhoud en is alleen in Shopify Admin terug te lezen.
- De 93 verwerkingsquarantaines zijn **GEEN Shopify DRAFT/ARCHIVE**; producten blijven in winkel zoals ze stonden.
- Na cohort 3 is de merkbrede verwerking van ruim 2.000 producten **niet klaar**.
- Beste eerstvolgende werk: cohort 4, niet opnieuw cohort 1–3 scrapen; gebruik bronrun van 19 oktober, sla 93 quarantaine-SKU's, alle 56 toegepaste SKU's en referentie 24.3710 over. Eerst exact 50 nieuwe, unieke bestaande producten selecteren; bron-check/Shopify-read/backup/apply/readback en onzekere apart zetten. Voor grote schaalwerking nog generieke search-index synchronisatie + facetverification uitrollen.

**Note:** Gedateerde gegevens en uitvoering via ChatGPT connectors; er is géén lokale Windows/SSH-sessie of klantcheckouttest uitgevoerd.
