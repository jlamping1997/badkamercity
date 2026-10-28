# DOC-01 — actuele bronkaart en productgegevens

**28 oktober 2026 · VERIFIED_THEME / VERIFIED_ADMIN, met één open bytepariteit-uitzondering.** Bronbranch bij aanvang: `fix/product-cards-2026-10-14` op `6aacab029dcfcaec79eb425a2f7859db62f4942d`. MAIN bleef `195818389770 — BadkamerCity - Smooth winkelwagen pop-up`. Geen winkel- of servergegevens gewijzigd.

## Dekking en bronhiërarchie

Alle 1.262 themebestanden zijn naast de Git-root opgehaald en statisch geïnventariseerd. Het manifest vóór en na de uitlezing bevat dezelfde paden en checksums; de MAIN-rol bleef gelijk. **1.261 bestanden zijn exact bytegelijk.** Voor `config/settings_data.json` geeft Shopify metadata MD5 `56d82e286a3ff41931816a95b614a5cf` en 8.651 bytes terug, terwijl de ontvangen tekst 11.923 bytes / MD5 `9fd7717c3e9eb0ab55c679cc1a753361` oplevert. De oorzaak is niet vastgesteld. De ontvangen tekst is behouden, niet aangepast om een hash te laten slagen. De harde pariteitscontrole stopt terecht met exitcode 2.

Daarom is DOC-01 **inhoudelijk vastgelegd, pariteitsvrijgave OPEN**. De snapshot is geen gecertificeerde identieke deploybron. De oude root van 441 bestanden blijft intact. De byteherkomst is vergeleken met alle gevolgde bestanden op het broncommit: 384 exact op het rootpad, 84 exact elders (onder meer releasedossiers), 794 zonder bytegelijke gevolgde kandidaat. Zie [source-provenance.json](evidence/2026-10-28-doc01/source-provenance.json). Dit is geen semantische herkomstverklaring; generated data, fonts en een gewijzigde codeversie kunnen verschillend tellen. Recente releasedossiers zijn niet automatisch geïntegreerd; featuregerichte verklaring blijft vervolgwerk. Geen root-sync of publicatie uitvoeren op basis van dit dossier.

De volledige snapshot en ruwe Admin-waarden worden niet in publieke Git gezet. Het [bewijsdossier](evidence/2026-10-28-doc01/README.md) bevat veilige hashes, paden, tellingen en statische afhankelijkheden. Het private productpakket is apart aan de eigenaar geleverd; toegang voor opvolgers loopt via de eigenaar.

## Bestandgroepen en afhankelijkheden

| Groep volgens scanner | Aantal | Interpretatie |
| --- | ---: | --- |
| Themebron | 423 | Liquid, JS, CSS, templates, settings en vertalingen |
| Gegenereerde keuzegegevenskandidaat | 656 | `bc-choice-data-*.json`; generator en actueel gebruik nog per pad traceren |
| Overige data-assets | 16 | JSON-data buiten bovenstaande groep |
| Media/font | 159 | Binaire en SVG-assets |
| Back-upkandidaat | 8 | Naam bevat backup; geen verwijderbesluit |

Er zijn **955** letterlijke Liquid-/JSON-verwijzingen: 952 doelen aanwezig in de snapshot, 3 niet opgelost. Nul JSON-/UTF-8-parsefouten. De 3 signalen gaan over `assets/icon-error` in `sections/main-password-header.liquid:84` en `assets/icon-3d-model` in `snippets/product-media.liquid:57` en `:113`. Controleer eerst de volledige expressie en functie; de regex lost geen samengestelde assetnamen op. Dit zijn kandidaten, geen bewezen ontbrekende assets.

Gebruik [theme-inventory.json](evidence/2026-10-28-doc01/theme-inventory.json) voor paden, hashes, regels, signalen en uitgaande edges; [reverse-dependencies.json](evidence/2026-10-28-doc01/reverse-dependencies.json) voor alle gevonden callers per doel. De kaart bevat geen volledige JS-importgraaf, CSS-URL-resolutie, dynamische Liquid, app-runtime of conditionele uitvoeringsanalyse.

## Echte Admin-toewijzingen → templates → secties

| Routefamilie | Toewijzingen | Theme-ingang | Directe secties |
| --- | ---: | --- | --- |
| Algemene PDP | 11.270 producten | `templates/product.json` | `main-product`, `related-products` |
| Sunshower PDP | 72 producten | `templates/product.sunshower.json` | `main-sunshower` |
| Hotbath pilot PDP | 1 product | `templates/product.bc-hotbath-pilot.json` | `main-product` |
| Algemene collectie | 209 collecties | `templates/collection.json` | `main-collection-banner`, `main-collection-product-grid`, `bc-collection-advice` |
| Meubelhub | 1 collectie | `templates/collection.bc-meubelhub.json` | `bc-meubelhub` |
| Categoriepagina | 16 collecties | `templates/collection.category-landing.json` | `main-category-landing`, `bc-collection-advice` |

Dit zijn Admin-toewijzingen, inclusief concepten, geen telling van alle publiek bereikbare URL's. ACTIVE en templateSuffix bewijzen geen kanaalpublicatie of routeactivatie. Er zijn 37 templatebestanden in de snapshot. Volledige route-/renderer-/viewportverificatie volgt in DOC-02. Pagina-/blog-/artikeltoewijzingen en Theme Editor-runtime zijn hier niet geïnventariseerd.

Alle **9 menu's** zijn tot de drie aanwezige niveaus gelezen; de openbare handletelling staat in [admin-assignment-counts.json](evidence/2026-10-28-doc01/admin-assignment-counts.json). Volledige items en bestemmingen staan privé bij de ruwe responses. Een bestaand menu is niet automatisch het geselecteerde header-/footermenu. De daadwerkelijke settings-consumptie, mobiele renderer en linkbereikbaarheid zijn nog te volgen.

Alle 226 collecties zijn gelezen, inclusief HTML, metafields, sortOrder en bronnen. In de aangetroffen collectievoorwaarden kwam alleen het type ProductTag voor; daarvan zijn matchType, relation en values vastgelegd. Product-collectielidmaatschappen tellen 39.064. Handmatige volgorde van producten binnen iedere collectie is niet apart geëxporteerd. Inline collectie-CSS blijft een mogelijke runtimeafhankelijkheid die bij de gerelateerde route onderzocht moet worden.

## Productdata en definities

Zie [PRODUCT_DATA.md](PRODUCT_DATA.md) voor pakketstructuur, datamodel, toegankelijkheid en beperkingen. De telling voor en na het venster is exact **11.343 producten / 11.343 varianten**: 11.342 ACTIVE, 1 DRAFT. Alle core-, metafield-, relatie- en variantdetaillagen sluiten op dezelfde IDs aan. Alle productvariant- en media-aantallen sluiten per product aan; geen onbehandelde geneste vervolgpagina's. Voor abonnementsgroepen en native productcomponenten is de producttelling overal nul.

Er zijn 250 bereikbare PRODUCT-metafielddefinities, 0 PRODUCTVARIANT-definities en 0 COLLECTION-definities opgehaald. Daarnaast zijn er 4 metaobjectdefinities. Waargenomen records: 241.042 productmetafields, 22 collectiemetafields, geen variantmetafields. Het [veldregister](evidence/2026-10-28-doc01/metafield-register.json) bevat 253 eigenaar/key/typecombinaties. Een definitie is niet hetzelfde als een aanwezige waarde; ongedefinieerde velden en ongebruikte definities blijven mogelijk.

## Wat de volgende onderzoeksstap moet oplossen

DOC-02 start met de open settings-pariteit en de featuregerichte herkomst van live code tegenover releasedossiers. Daarna de route-/componentmatrix: renderer, datavelden, keuzegegevensloader, events, staatmatrix en stijlcontract. Begin bij algemene PDP en Sunshower, vervolg met Hotbath/Wiesbaden, kaart/zoeken/filter, mobiel en cart. Het voorbeeld van Sunshower-pijlen blijft USER_REPORTED totdat functie en staat op de bedoelde route zijn gereproduceerd. Deze ronde heeft geen UI-, a11y-, performance-, checkout- of VPS-runtimevrijgave uitgevoerd.
