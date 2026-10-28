# BadkamerCity — actuele werkstatus

**Bijgewerkt: 28 oktober 2026, na DOC-01 / productexport.** Vaste actuele ingang. De [status van vóór het documentatieonderzoek](LIVE_STATUS_ARCHIVE_BEFORE_2026-10-28.md) blijft geschiedenis.

## Huidige opdracht en uitkomst

De eigenaar vraagt diepe documentatie in Git, een graaf van systemen/code/data en later onderbouwde UI-consistentie en kleine verbeteringen. Aanvullend: databestanden met alle bereikbare gegevens per product. Geen productmutaties of brede refactor.

**DOC-00 vastgelegd; DOC-01 inhoudelijk CAPTURED, pariteitsvrijgave OPEN.** Begin bij [architectuur](architecture/README.md), [actuele bronkaart](architecture/DOC01_SOURCE_MAP.md) en [productdata](architecture/PRODUCT_DATA.md). Het private productpakket is apart geleverd; de publieke repo bevat alleen veilige schema's, aantallen en kaarten.

## Gecontroleerde bronstand

| Bron | Stand op meetmoment |
| --- | --- |
| Repository | jlamping1997/badkamercity, publiek |
| Actieve codebranch | fix/product-cards-2026-10-14 |
| Broncommit bij aanvang | 6aacab029dcfcaec79eb425a2f7859db62f4942d |
| main bij aanvang | 48e73f3805ef9306bf18c90b47a7b9a645e2a332; documentatie-ingang |
| Shopify MAIN, voor/na | 195818389770 — BadkamerCity - Smooth winkelwagen pop-up |
| Vorige MAIN | 195805085962 — Winkelwagen compact - 27 okt; UNPUBLISHED |
| Live snapshot | Alle 1.262 bestanden ontvangen; metadata voor/na gelijk |
| Bytecontrole | 1.261 exact; settings_data.json wijkt af van teruggegeven metadata |
| Statische kaart | 955 refs: 952 in snapshot, 3 niet opgelost; 0 parsefouten |
| Byteherkomst tegenover alle gevolgde bestanden | 384 root, 84 elders, 794 geen match; geen semantische herkomstclaim |
| Admin | 226 collecties, 9 menu's, product-/collectietemplates, veld-/metaobjectdefinities gelezen |
| Productpakket | 11.343 producten / 11.343 varianten; 241.064 metafields; 32.065 mediarecords |
| Windows / VPS | Niet gecontroleerd; geen synchronisatie of servermutaties geclaimd |

Nieuwe publicatie kan rollen veranderen. De root blijft 441 themabestanden en is niet automatisch de actuele productiecode. Geen root overschreven of live code gepubliceerd.

## Controles en grenzen

Voor-/natellingen producten/varianten zijn EXACT en sluiten aan. Geen dubbele IDs/verweesde varianten/onbehandelde geneste paginering. Variant-/media-aantallen sluiten per product aan. SQLite integrity_check ok; foreign_key_check nul fouten. Vier gerichte builderchecks en vijf scannerchecks geslaagd. De harde themepariteitscontrole faalt terecht met exitcode 2 op de ene settings-uitzondering; geen volledige bronvrijgave.

Productdata is privé JSONL + SQLite + ruwe responses + veldregister, met media-/document-URL's en 674 JSON-themeassets. Geen binaire media, app-private/externe leveranciers-/VPS-data, volledig markt-/B2B-prijsmodel of atomair herstelpunt. Publicatiekoppelingen zijn de ontvangen standaard APP-catalogusselectie. Zie de volledige grenzen in PRODUCT_DATA.md. Een constante telling bewijst geen ongewijzigde voorraad gedurende het exportvenster.

Geen browser-/UI-/checkout-/a11y-/performancevrijgave uitgevoerd. Het gemelde Sunshower-pijltjesverschil blijft USER_REPORTED; de functie moet in DOC-02 worden gereproduceerd. Korte titels/filteroptimalisatie blijven geparkeerd. Geen writer of achtergrondworker blijft actief na oplevering; de eenmalige read-only bulkexportjob is COMPLETED, de daadwerkelijke bestanden zijn via gewone gepagineerde reads verkregen.

## Exact één volgende handeling

**DOC-01 pariteitsuitzondering read-only afbakenen:** bij een opnieuw gecontroleerde MAIN de ontvangen config/settings_data.json vergelijken met een zelfstandig exact bronbestand uit een toegestane theme-export, zonder productie/root te wijzigen. Vastleggen of het een representatieverschil of bronverschil is; geen hashvrijgave zonder bewijs. Daarna DOC-02: de bron-/Admin-kaart tot route-/renderer-/componentmatrix verdiepen, beginnend bij algemene PDP en Sunshower.

## Hervatten

Lees deze status → AGENTS.md → architecture/DOC01_SOURCE_MAP.md → PRODUCT_DATA.md. Controleer eigen werkmap/rollen/toegang en bewaar bestaande wijzigingen. Actuele checkpoint is te vinden met git log -1 -- docs/architecture/DOC01_SOURCE_MAP.md; main bevat uitsluitend documentatie-updates, tooling staat op de actieve branch. Geen oude imports/publicaties uit archief opnieuw starten.
