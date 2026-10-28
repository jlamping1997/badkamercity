# Productpagina's, specificaties en documenten

**Verdieping:** zie [de actierace-analyse voor Sunshower](micro/SUNSHOWER_ACTIONS.md). Het gedateerde bron-/HTML-bewijs hieronder blijft behouden; nieuwe replays zijn apart gelabeld.

**Eigenaarrol:** storefrontontwikkeling voor rendering; assortiment/datahouder voor feiten en productrelaties. **Bronstatus:** VERIFIED_THEME, drie representatieve PDP's VERIFIED_HTML; interactieve/visuele staten NOT_TESTED. Zie [bronregels](README.md) en [routebeslissing](../ROUTE_RENDERER_MATRIX.md).

## Twee hoofdopbouwen

| Onderdeel | Algemene PDP | Sunshower PDP |
| --- | --- | --- |
| Ingang | product.json of Hotbath-pilottemplate → main-product | product.sunshower.json → main-sunshower |
| Identiteit | product-info: product ID, URL, section ID; H1, merk, SKU | data-ss-page: bron-ID, variant, prijs, valuta; H1 en SKU |
| Media | product-media-gallery + media-gallery.js; media-modal; instellingen voor layout en variantmedia | Alleen images uit product.media; eigen viewport, thumbnails, pijlen; PhotoSwipe-module op aanvraag |
| Keuze | Geordende serverbeslissing; gedeelde switcher of native variantpicker | bc_sunshower.configuration + catalogusasset; wisselt product-URL |
| Kopen | buy-buttons → product-form; optioneel inbouwinterceptor | Native productformulier voor hoofdartikel; aparte multi-item setfunctie |
| Inhoud | Beschrijving, documenten, specsrouter, setcomponenten en accessoires | Gegevens uit bc_sunshower; guide-/highlights-/value-snippets |
| Stijl | section-main-product, bc-product-page en componentstyles | bc-sunshower-page + configurator + PhotoSwipe-stijl |

Belangrijkste bronnen: main-product:1–82 (root/load), :315–327 (identiteit/media), :762–877 (keuze/koop), :1093–1184 (inhoud); main-sunshower:8–19 (gegevens), :24–82 (galerij/keuze/koop), :93–134 (inhoud/set/schema). Hashes en exact bytegelijke Git-kandidaten staan in de [bronindex](../evidence/2026-10-28-doc02/source-index.json).

## Algemene PDP: data door de renderketen

De server rendert hoofdidentiteit vanuit Shopify-product/selected_or_first_available_variant. De buybox wordt vanuit sectionblocks opgebouwd; een block dat in een schema bestaat maar niet in de template staat, is niet automatisch zichtbaar. De keuzebeslissing staat apart beschreven bij [PRODUCT_CHOICES](PRODUCT_CHOICES.md).

`product-info.js` ontvangt optionValueSelectionChange, kan een eerdere fetch afbreken, haalt sectie-HTML op en werkt variant, media, form-ID, prijs en URL bij. De native route gebruikt history.replaceState met variant-ID; de cross-product switchers gebruiken location.assign. Verwissel die twee mechanismen niet bij een wijziging aan “keuzes”.

### Specificaties: de echte prioriteit

`snippets/bc-product-detail-specs.liquid:6–24` beslist:

| Voorwaarde | Renderer | Waarheid en terugval |
| --- | --- | --- |
| bc_sunshower.specifications gevuld | bc-sunshower-panel, mode specifications | Sunshower JSON-structuur |
| Hotbath normal-scope geeft ready | bc-hotbath-public-specs | custom.complete_specificaties; identiteit en importscope; held_source_claims uitsluiten |
| Merk Wiesbaden of JEE-O | Eerst bc-wiesbaden-reviewed-specs | Alleen geldig beoordeelde broninhoud; bij leeg resultaat mapped renderer |
| Mapped renderer | bc-product-detail-specs-mapped → mapped-spec-row | Wiesbaden gebruikt custom; JEE-O gebruikt specs; de veldnamen worden dynamisch doorgegeven |
| Overige producten | bc-product-detail-specs-legacy | Bestaande oudere mapping; geen automatische namespaceverhuizing |

Hotbath normal-scope controleert vendor, toegestane importbatch, één defaultvariant, SKU = custom.artikelnummer en gevuld JSON-type. Pilot-/TEST-/exclude-/no-sync-gevallen vallen erbuiten. De naam “ready” is een **codeguard** en geen nieuwe commerciële goedkeuring van iedere waarde. Het public-specssnippet bewaart bronlabels, eenheden en volgorde en houdt claims apart. Pas een veldnaam niet globaal aan omdat dezelfde naam ook onder specs voorkomt.

Wiesbaden reviewed-scope vereist onder andere de fabrikantnummer/SKU-match, het juiste JSON-schema en status, overeenkomende product-ID/SKU en aanwezige spec_keys. Er bestaat daarnaast een expliciete pilotuitzondering voor 24.3710. Behoud deze scope bij een stijlwijziging. Een niet passend reviewobject kan leiden tot mapped terugval; dat betekent niet automatisch “alle specificaties ontbreken”.

### Beschrijving en dubbelingen

`bc-product-description.liquid:5–77` kan de bekende geïmporteerde Wiesbaden-tabel uit de **weergave** halen. Alleen de exacte marker/structuur wordt herkend; iedere rij moet passen op aanwezige data en er moet een artikelnummermatch zijn. Anders blijft de originele omschrijving staan. Deze rendering muteert Shopify descriptionHtml niet.

De algemene PDP normaliseert in de weergegeven omschrijving H1/H2 naar H3. Het disclosurecomponent klapt beschrijving na vier berekende regels in; op mobiel kan het specificaties na tien rijen inklappen. Het houdt verborgen links buiten de tabvolgorde en herstelt die bij openen. Dit is sourcegedrag, nog geen uitgevoerde a11yvrijgave. Sunshower heeft een afzonderlijke omschrijvingsuitklapper; zie [stijl en beweging](MOTION_AND_STYLES.md).

### Documenten

`bc-product-documents.liquid:7–49` gebruikt custom.technische_documenten met type list.url. De renderer vereist reviewed Wiesbaden-scope óf Hotbath met bc_data.documents_visible == true. Hij dedupliceert URL's, laat alleen https:// door en bepaalt het label uit het pad/extensie; handleidingen-PDF's worden anders benoemd dan tekeningen. Externe links krijgen noopener/noreferrer.

Een document kan dus aanwezig zijn in de database en toch bewust niet door deze renderer worden getoond. Voor Sunshower geldt de andere route via bc_sunshower.documents en bc-ss-guide. Een bugmelding “PDF ontbreekt” begint bij veldtype, scopeguard en exacte gebruikte sectie, niet bij het willekeurig zichtbaar maken van alle URL's. Bereikbaarheid, rechten en inhoud van de binaire documenten zijn niet in deze ronde gecontroleerd.

### Set en accessoires

`bc-product-set-components` kiest eerst Sunshower, vervolgens beoordeelde setdata met de benoemde VERIFIED-statussen en anders de bestaande mapping/testproductroute. `bc-product-accessories` kiest eveneens eerst Sunshower; de Hotbath-terugval controleert merk, SKU en productidentiteit, beperkt de gelezen relatierijen en dedupliceert varianten. “Inbegrepen”, “apart nodig” en “optioneel” zijn verschillende betekenisgroepen. Een informatieve setcomponent is geen toestemming om die variant nogmaals betaald toe te voegen.

## Velddekking uit het private exportvenster

| Veld | Type | Productrecords met het veld |
| --- | --- | ---: |
| custom.complete_specificaties | json | 9.420 |
| custom.technische_documenten | list.url | 4.070 |
| bc_data.content_review | json | 2.416 |
| bc_data.documents_visible | boolean | 7.012 |
| bc_sunshower.configuration | json | 72 |
| bc_sunshower.specifications / source / documents / components | json | Elk 104 |
| bc_sunshower.accessories | json | 72 |

Dit zijn aantallen **aanwezige velden**, geen aantallen zichtbare rijen, true-booleans of goedgekeurde producten. De 104 Sunshower-datarecords en 72 configuratorproducten vormen verschillende scopes. Zie [PRODUCT_DATA](../PRODUCT_DATA.md) voor het exportvenster en [field-consumers.json](../evidence/2026-10-28-doc02/field-consumers.json) voor gevonden letterlijke consumers. Dynamische mapping kan meer keys gebruiken dan de regex vindt.

## Onderhoud en gerichte regressie

| Wijziging | Eerst volgen | Controleren vóór een fix als afgerond geldt |
| --- | --- | --- |
| Eén spec ontbreekt | Bronwaarde → type → scopeguard → renderer → rijhelper → label/unit | Null, false, 0, held claim, verkeerde SKU; oude omschrijving blijft veilig |
| Bijlagenblok | documents/list.url + reviewed/documents_visible → https-filter → label | Lege/duplicaat/http/https-URL; Sunshower-route apart; geen Admin-write door CSS-fix |
| Galerij | Templateinstelling → mediafilter → DOM IDs → media-script/viewer | 0/1/meerdere beelden, video/3D alleen waar ondersteund, variantmedia, pijlen/zoom/focus |
| Omschrijving | Vendor/markercontrole → getoonde HTML → disclosure | Korte/lange tekst, resize, ingeklapte links, terugknop, reduced motion |
| Set/accessoire | Exacte relatie + inbegrepen/vereist/optioneel → beschikbaarheid → koophandler | Geen dubbel betaald onderdeel; onjuiste relatie blokkeert; totaal en aantal volgen het juiste contract |

Deze scenario's zijn een acceptatiematrix, niet deze ronde uitgevoerde tests. Wijzig rendering eerst in een bewezen passend conceptthema; bewaar exacte oude bestanden en gegevens. De huidige documentatiewijziging is terug te zetten met de relevante Git-commit en heeft geen storefrontrollback nodig. Productdataherstel is een afzonderlijke operatie met oorspronkelijke private waarden en expliciete opdracht.
