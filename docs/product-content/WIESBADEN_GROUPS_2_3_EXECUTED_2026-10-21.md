# Wiesbaden — cohorten 2 en 3, feitelijke Shopify-uitvoering — 21 oktober 2026

Status: **VERIFIED_SHOPIFY_ADMIN_WRITES / VERIFIED_STOREFRONT_SAMPLE / EXTERNAL_SEARCH_INDEX_NOT_VERIFIED**.

## In één oogopslag

- **Cohort 2 (50 bestaande Wiesbaden-producten):** 23 met aangepaste producttitel/omschrijving (3 vorige ronde + 20 nieuwe); 27 in quarantaine (19 automatische identiteits-/feitenblokkades plus 8 bronconflicten). Voor de 20 nieuwste zijn Admin SEO-title/description, eigen Nederlandse descriptionHtml, geordende custom.complete_specificaties, custom.card_title en bc_data.content_review klaar; voor de drie eerdere alleen native titel/omschrijving.
- **Cohort 3 (50 bestaande, unieke SKU's):** **27** nieuwe producten inhoudelijk gecontroleerd op officiële fabrikantpagina en in Shopify aangepast; **23** apart gehouden (19 uit offline validatie, 4 aangetroffen fabrikant-/categoriemismatches). Voor alle 27 zijn descriptionHtml, native Shopify SEO title+description, custom.complete_specificaties, custom.card_title en bc_data.content_review geschreven en onafhankelijk teruggelezen. Verschillende producttypes: fonteinkranen, opbouw wastafelkranen, badthermostaatkranen en douchethermostaten.
- **Gecumuleerd:** 9 eerdere wijzigingen (6 cohort1 + 3 cohort2) plus 20 aanvullende cohort2-wijzigingen plus 27 cohort3-wijzigingen = **56 live producten** bewerkt gedurende deze trajecten. Referentiekraan 24.3710 blijft beschermd. **Quarantaine: 93** (39 uitgesteld eerste cohort, 4 technische eerste cohort, 19 automatische tweede, 8 bronconflicten tweede, 19 automatische derde, 4 bronconflicten derde).
- Quarantaine is **uitsluitend verwerkingsblokkade**, niet Shopify DRAFT/archief. Canoniek register: `docs/product-content/wiesbaden/quarantine-register-2026-10-21.json` op actieve Git-branch.

## De 27 werkelijk bijgewerkte cohort-3 SKU's

22.3708, 22.3720, 22.3721, 22.3731, 22.3772, 22.3774, 22.5701, 22.6701;
29.1626, 29.2102, 29.3114, 29.4103, 29.4114, 29.4931, 29.5102, 29.5114,
29.5302, 29.5303, 29.5310, 29.5311, 29.5313, 29.5320,
29.5360, 29.5361, 29.5363, 29.5931, 29.7933.

Vier aanvullende quarantaine-items: 22.3750, 22.3761, 22.5760 (Sophia wandfonteinkraan in inbouwcollectie — taxonomy unclear) en 22.3770 (titel+tabel chroom, officiële omschrijving noemt geborsteld staal). Zie machineleesbaar register.

## Feitelijke schrijfacties en bewijs

- Alle 27 eerst **verse Shopify vendor/variant SKU** gecontroleerd en de nodige collecties daadwerkelijk als lidmaatschap gevonden. Fabrikant-SKU/variantkleur en essentiële gegevens apart op officiële Wiesbaden-productpagina opgezocht.
- EERST eigen pre-write-herstelbackup via `bc_rollback.pre_content_v1` aangemaakt voor elk nieuw cohort-3 product; hierin relevante oorspronkelijke productvelden, inclusief beschrijving en SEO. Daarna Shopify native `descriptionHtml` en `seo.title/seo.description` geschreven. Daarna met `metafieldsSet` met compareDigest getypeerde specificatiegroepen, korte titel en reviewmarker bijgewerkt. Ten slotte onafhankelijke Shopify-readback op inhoud, specs, review, prijs, documenten en backup uitgevoerd. Null/missing en onzekere waarden niet op gevoel ingevuld.
- Idem voor 19 van 20 nieuwe cohort-2 producten; **29.3930** is wel netjes teruggelezen en compleet bijgeschreven, maar mist een vooraf aangemaakte `bc_rollback.pre_content_v1` omdat de eerste proefwrite direct met productUpdate gebeurde. Maak bij terugzetten van dit artikel geen ongefundeerde automatische rollback.
- Prijzen, SKU's, voorraad, productstatus, handles, collectielidmaatschap en bestaande documenten/media zijn niet bewust gewijzigd. De nieuwe teksten bevatten geen verzonnen garantie, EAN, niet-geverifieerde uitloophoogten of leveringsclaims.
- **Publieke storefront steekproef** (4/4 producten met actuele title en relevante spec-rijen uit Shopify live): 29.3930,22.3708,29.4103,29.4115. Dit is GEEN 47-producten browser-test, geen mobielbedieningsproef.
- Oorspronkelijke 19-oktober bron-archief/cache hergebruikt, geen grootschalige scrape. Voor iedere toegepaste SKU afzonderlijke fabrikantpagina live opnieuw gelezen.
- **Niet getest / niet aangepast:** Typesense/VPS index writes en herindexering, publieke facetfilters en Search Console, volledige mobiele/desktop regressie. `bc_data.content_review.status=ready` is alleen de rendergoedkeuring voor de gecontroleerde gekozen productfeiten; niet een uitspraak over de externe index. Externe filters kunnen dus nog oude titels/waarden tonen.
- Het bestaande derde cohort met 50 SKU's plus alle 50 offline voorstellen en controles zit in het aan de eigenaar opgeleverde gesprekspakket, niet in publieke GitHub met volledige leveranciersinhoud.

## Praktische volgende uitvoering

Pak **groep 4** uit dezelfde bevroren 19-oktoberbron, sla alle verwerkte of in quarantaine geplaatste SKU's over, match fabrikant/Shopify opnieuw en schrijf alléén gecontroleerde voorstellen. Stop een onduidelijke set/inbouwdeel-, kleur- of installatiespecificatie in het centrale register. Los de externe zoek-/filterindexcontract-sync afzonderlijk gecontroleerd op, zonder prijzen/facetten uit een oude bron blind te overschrijven. Houd een duurzame voortgangscounter/status aan in Git.