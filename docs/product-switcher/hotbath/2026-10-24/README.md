# Hotbath menu-uitbreiding, 24 oktober 2026

Dit dossier bevat de volledige read-only inventarisatie en een begrensde, geteste eerste uitbreiding. Actieve branch: `fix/product-cards-2026-10-14`. De scope en tellingen staan in PLAN.md; snapshots en voorstellen zijn afzonderlijke gebruikersdata, niet in deze publieke repository opgeslagen.

## Preview en bron

- MAIN bij aanvang/einde: 195611492618; 512/512 bestanden ongewijzigd.
- Bronconcept: 195611197706, met nog niet gepubliceerde Sunshower-correcties.
- Nieuwe preview: 195649929482; eerst 514/514 identiek aan de bron, daarna 519 bestanden waarvan tien scoped wijzigingen en 509 gelijk.
- Alleen theme-bestanden gewijzigd. Geen productmetafields, prijzen, voorraad, index, betaalinstellingen of publicatie gewijzigd.

## Bestanden

- `patch/`: de tien daadwerkelijk teruggelezen conceptbestanden, geen root-theme-push.
- `rollback/`: vijf oorspronkelijke bestanden; bewaar byte-inhoud en controleer MD5 tegen bronmanifest.
- `tools/`: generator, analyse en betekenisvolle mapping-/scrolltests.
- `preview-manifest.json`, `final-file-readback.json`, `final-theme-verification.json`: scope, hashes en verse controles.
- `analysis-validation.json`, `preview-tests.json`, `scroll-tests.json`, `browser-verification.md`: bewijs en grenzen.
- `book-rules.json`: feiten en paginaverwijzingen uit Hotbath Catalogus Editie18, geen vervanging voor actuele fabrikantvalidatie.

## Reproduceren

Benodigde private taakinputs: `catalog_snapshot.json` en `current_menu_data.json` uit het afzonderlijke gegevensdossier. De productcatalogus is een momentopname, geen live sync. Gebruik geen willekeurige toekomstige export alsof deze dezelfde bronversie is.

De generatorinput werd bij deze sessie als tekst genormaliseerd. Maak vanuit de exact opgeslagen rollbackbestanden een aparte inputmap: lees als UTF-8 met universele newline-normalisatie en voeg precies één LF toe. De bron-MD5's in het manifest verwijzen naar de oorspronkelijke bytes; generator-SHA256's naar die genormaliseerde inputs. `source_sha256` in de audit is canonical JSON met sort_keys; `catalog_sha256` van de preview is de SHA256 van het ruwe snapshotbestand. Vergelijk die twee vormen niet als dezelfde hash.

Voorbeeld: `python3 tools/build_preview.py --source-dir <genormaliseerde-bronmap> --catalog <catalog_snapshot.json> --shared-data <current_menu_data.json> --output-dir <nieuwe-uitvoermap>`. Bewaar scroll_position.js naast de generator. De NL/EN-headingaliases zijn afzonderlijk toegepast en staan in patch/locales; de generator overschrijft ze niet. Gebruik finale manifesten voor de complete tien-file scope.

## Rollback en uitrol

Zet alleen de vijf bestaande bestanden uit rollback terug naar hetzelfde ongepubliceerde concept. De nieuwe helper en vier assets zijn daarna niet meer aangeroepen en kunnen blijven staan. MAIN en het oudere Sunshower-concept zijn behouden. Geen root-theme-sync gebruiken en niet naar MAIN schrijven.

Volgende batch: 34 bestaande groepen / 77 sterke aanvullingen; de eerdere baseline35/81 bevatte BAA03+4 uit deze proef. Fysieke telefooncontrole en eigenaarspublicatie zijn nog niet uitgevoerd. BAA03BGP en BAA09BGP hebben een bestaande ontbrekende productfoto; geen foutieve kleurfoto gebruiken.
