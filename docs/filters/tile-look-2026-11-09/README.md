# Tegels indelen op uitstraling

9 november 2026 · TILE-LOOK-01 · **ADMIN_APPLIED_VERIFIED / FILTER_READY_FOR_OWNER_EXECUTION**.

De eigenaar wil herkenbare uitstralingkeuzes zoals steenlook, marmerlook en houtlook. De bestaande Shopify-categorieën zijn aangevuld; het nieuwe generieke filterpakket staat klaar. De installatie van dat filter op de VPS is nog niet uitgevoerd.

## Gecontroleerd resultaat

Van de bestaande gepubliceerde tegelset van 3.496 artikelen zijn nu **3.495 ingedeeld**.3.137 ontbrekende `tiles.look`-velden zijn met compareDigest:null gevuld; alle 358 bestaande waarden, metafield-ID's, types en digests zijnbehouden. Iedere nieuweinvulling is vooraf op echte SKU, handle, titel en vendor gecontroleerd en daarna teruggelezen. Nieuwe tags zijn met tagsAdd toegevoegd; geen oude taglijst is vervangen.

De admin-hoofdcollectie bevat 4.100 artikelen. De 604 eerder als niet gepubliceerd uitgesloten records zijn niet geactiveerd of meegenomen in deze scope. Dat verklaart het verschil met de gepubliceerde filterset; er zijn geen producten verwijderd.

| Primaire uitstraling | Producten |
| --- | ---: |
| Betonlook | 146 |
| Decoratief | 828 |
| Effen | 661 |
| Handvormlook | 1022 |
| Houtlook | 74 |
| Marmerlook | 150 |
| Metaallook | 68 |
| Steenlook | 216 |
| Terracottalook | 150 |
| Terrazzo | 180 |

Eén bewuste uitzondering: **WM2600 — A Piedi White 100 × 100** blijft zonder look. Eén zachte productfoto en de beschikbare tekst geven onvoldoende onderscheid tussen steen, beton en effen. Het artikel blijft vindbaar zonder uitstralingselectie. CottageWhiteWC0701 kon na een verse featuredMedia-read en beeldcontrole alsnog begrensd als Steenlook worden ingedeeld(82% redactionele zekerheid); bronkleur en specificaties bleven onaangeraakt.

## Bestaande categorieën, volledige IDcontrole

| Bestaande route | Producten |
| --- | ---: |
| [stonelook-tegels](https://badkamercity.nl/collections/stonelook-tegels) | 216 |
| [marmerlook-tegels](https://badkamercity.nl/collections/marmerlook-tegels) | 150 |
| [houtlook-tegels](https://badkamercity.nl/collections/houtlook-tegels) | 74 |
| [betonlook-tegels](https://badkamercity.nl/collections/betonlook-tegels) | 146 |
| [metaallook-tegels](https://badkamercity.nl/collections/metaallook-tegels) | 68 |
| [terrazzo-tegels](https://badkamercity.nl/collections/terrazzo-tegels) | 180 |
| [decortegels](https://badkamercity.nl/collections/decortegels) | 839 |

Alle zeven volledige native product-IDsets komen exact overeen met de behouden bestaande leden plus de bedoelde toevoegingen; paginering volledig, geen dubbelen of extra/missende IDs. Iedere primaire look met een bestaande lookcategorie heeft nu zijn juiste plaats. Decortegels 839 omvat 828 primaire Decoratief-producten plus 11 behouden secundaireleden(marmer 4, hout 6, effen 1). Vijf oude Design-records kregen uitsluitend de ontbrekende Decortegel-tag; hun oorspronkelijke look bleef Design.

Terrazzo behoudt de oude handmatige bron 42669539594 en exact dezelfde 22 ID's. Daarnaast is bron 42862936330 toegevoegd met **ALL: tag Tegels EN tag Terrazzo**. Zo blijven bestaande handmatige keuzes intact en worden nieuwe toewijzingen automatisch meegenomen. Alle andere bestaande broncondities zijn teruggelezen. Native collectietoewijzingen liepen tijdelijk achter op de tagwrite; de eindcontrole wachtte op de feitelijke volledige productlijsten.

Er zijn 3.142 semantische tags toegevoegd: één per nieuwe lookinvulling plus de vijf bestaandeDesign-koppelingen. Geen productprijzen, voorraad, status, publicaties, kleur-/maat-/materiaal-/serievelden of Shopify-themafiles zijn geschreven. De MAIN-rol werd read-only aangetroffen als196354474250 — BadkamerCity - Tegelprijzen per m2 9 nov; dit is geen nieuwe integrale bronpariteitscontrole van dat afzonderlijke prijsdossier.

## Onderbouwing en afbakening

Hergebruik van bestaand merchantveld **tiles.look**, single_line_text_field, definitie 610289287434. Een primaire uitstraling per artikel; toepassing, mozaïektype, afwerking, kleur en werkelijke materiaalsoort blijven onderscheiden. Bestaande Terrazzolook→Terrazzo en Patroontegels/Design→Decoratief worden uitsluitend voor de consumentkeuze genormaliseerd; bestaande bronwaarden zijn niet herschreven. Zellige valt onder Handvormlook.

Bronnen: [officiële Cotto-catalogus](https://cottoceramix.nl/i/catalogus.html), openbare CX_Catalogus_2627 met 209 pagina's, officiële november2026artikellijst, productinformatie van Cotto en werkelijke fabrikanten, aangevuld met gerichte actuele productfoto's. De bronkoppeling gebruikt echte Shopify-variant-SKU's en waar nodig exacte handle-/titelhashes. Op eigenaarinstructie zijn goed onderbouwde visuele keuzes vanaf ongeveer 70% zekerheid toegestaan; niet iedere keuze is een letterlijk fabrikantlabel. Er is geen algemene titel-/kleur-/BMNUni-classifier gebruikt.

Gemengde reeksen zijn SKU-gebonden behandeld, onder meer AlterEgo(hout/beton), Studio (twee fabrikanten), Pop Tile (Sixties-basis/decor), Farnese, Si-Bel, Oltre, BelHistoire, Neri en Argillae. De catalogus-OCR-collisie VP1534 is niet als BelHistoire gebruikt. Een look is geen nieuwe materiaal- of productspecificatieclaim. Volledige catalogus, doel-ID's, foto's en voor/na-journals blijven privé; alleen geaggregeerd bewijs wordt gepubliceerd.

## Filterpakket en transportpin

De API en themacode blijven identiek; de worker leest tiles.look vers uit Shopify en levert `f_tegel_uitstraling` als gesloten generieke checkbox. Alleen de tegelprofielen en Cottoceramix krijgen de keuze. Cotto blijft general; het uitgestelde formaatfilter wordt niet toegevoegd. Maximaal twee groepen blijven open. Een pure lookcategorie met één waarde krijgt geen nutteloze zichtbare lookkeuze.

**91 lokale tests PASS, nul skips**:26 workercontroles en 65 releasecontroles, onafhankelijk bevestigd. De testset gebruikt echte private runtime-/API-/catalogusfixtures plus gerichte lifecyclegevallen. De oude kleuren en 132 formaatcodes zijn behouden; een menselijke active.json-swap tijdens de livecheck wordt niet overschreven. Deze tests zijn geen bewijs van serverinstallatie of browser-/telefooncontrole.

Codecheckpoint **ff1c7c13d9ce5ef3aeec9408aa9e9dc1ff4db183**. [Vastgepinde standalone](https://raw.githubusercontent.com/jlamping1997/badkamercity/ff1c7c13d9ce5ef3aeec9408aa9e9dc1ff4db183/scripts/filter-sync/simplification/tile-looks/release/repair_tile_look_filter.py) — 49.441 bytes, SHA256 `73088a72cafbfa895a047214e085eea5d0c2727749e6c63bf34f401c00ed30d5`.

Vereiste baseworker `ecfc142a4fb15e66df297ec20884826be1bd4e8c491fb20bdb3e17cc281ba69a`; target `79f676d035fdd6d250e2daec51b886d1aa54c117707718d7ea9695300c21c43d`. API blijft bytegelijk `3a7701134be7ac55b0a83436ceb16ebb19ac0a88aba17c283490f90047f02094`. Alle zeven bestaande flags vereist; nieuw is tile_looks_v1, samen acht. Installer gebruikt private backup, slot, timerpauze, volledigeverseexport, staging, volledigeindexreadback, lokale/publiekechecks vóórworkeropslag en owned-generationrollback. Geen vaste actuele productaantallen of doel-ID's in de installer.

De Shopify-indeling is voltooid. De zichtbare nieuwe lookfilter en gelijktijdige volledige VPS-verversing wachten op eigenaaruitvoering van deze standalone. Geen VPS-staging, activatie, nieuwe browser-, mobiele of rebootproef in deze sessie. De oudere serverkleurrelease blijft de geverifieerde productieversie totdat dit pakket succesvol is uitgevoerd.

## Herstel, rapport en vervolg

De private herstelkopie bevat de oorspronkelijke 3.496 records, alle 126 batches van maximaal 25 producten, pilot, bronwijziging, na-controles, frozenregels en herstelplan. Herstel uitsluitend eigen look-/tagtoevoegingen na verse waardevergelijking; behoud latere handmatige wijzigingen. Bij terugdraaien van de Terrazzo-autobron uitsluitend de exacte nieuwe bron verwijderen, nooit de bestaande handmatige bron. Het VPS-pakket heeft zijn eigen afzonderlijke back-up/herstel.

Compact foto-overzicht: 387 voorbeelden, 24 per pagina, 17 pagina's; kleine foto's van 160 × 100 pixels met look eronder, zoeken opnaam/SKU en filter perlook. Alle 387 actuele media-URLs gelezen;24 statische kaarten, JS-syntaxis en paginering/zoeken/legeuitkomst/reset zijn gecontroleerd. Geen echte browserrendering van dit rapport geclaimd.

**DEFERRED op eigenaarverzoek:** 143 nog kleurloze producten en het Cotto-merkformaatfilter. **OPEN:** het ene twijfelgeval WM2600. Overige werkstromen/holds behouden. Geen actieve lookschrijver na deze overdracht.

**Eén volgende handeling:** eigenaar voert het nieuwe vastgepinde PowerShell-blok uit en deelt de volledige uitvoer; daarna uitvoer plus publieke lookprofielen, productsets, kleur-/formaatcombinaties en actieve hashes/flags controleren. Niet als live lookfilter markeren vóór die nacontrole.
