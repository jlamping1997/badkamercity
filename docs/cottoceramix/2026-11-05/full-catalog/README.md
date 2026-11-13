# COTTO-05 — assortiment gepubliceerd, unitvrijgave en zoekindex nog open

5 november 2026. **PARTIALLY_PUBLISHED / BLOCKED_MERCHANT_THEME_AND_INDEX_LAG.**

Er staan **3.159 Cottoceramix-artikelen ACTIVE én gepubliceerd op Webshop**. Daarnaast staan **597 gecontroleerde stuks-/pak-/setartikelen DRAFT**, evenals acht bestaande bronconflicten. De productgegevens zijn teruggelezen; de nieuwe unitbediening is nog niet werkelijk in de browser of winkelwagen getest. Het gecontroleerde conceptthema is nog UNPUBLISHED en de externe zoekindex loopt achter. Dit checkpoint is geen volledige vrijgave van het assortiment.

## Bevestigde aantallen

De verse meting van **5 november 2026, 21:38 UTC** sluit op 3.764 unieke Shopify-producten:

| Onderdeel | Aantal | Bewezen stand |
| --- | ---: | --- |
| Bestaande actieve artikelen | 846 | ACTIVE en Webshop-publicatie behouden |
| Nieuwe strict m²-artikelen | 1.127 | Volledige readback en publicatienacontrole PASS |
| Overige nieuwe m²-artikelen | 1.186 | Volledige v2-readback en publicatienacontrole PASS |
| **Actief en Webshop-gepubliceerd totaal** | **3.159** | Drie afzonderlijk gecontroleerde, niet-overlappende groepen |
| Native stuks-/pak-/setartikelen | 597 | Volledige Admin-controle PASS; DRAFT, geen storefrontvrijgave |
| Bestaande bron-HOLDs | 8 | DRAFT, ongepubliceerd en zonder publieke product-URL |
| **DRAFT totaal** | **605** | 597 unitartikelen plus acht bestaande HOLDs |
| **Shopify-producten totaal** | **3.764** | Unieke product-ID's bevestigd |

De bron bevat 3.771 exacte SKU's. Er zijn vijftien bron-HOLDs: acht bestaan al als DRAFT; zes afwerkingsconflicten en één artikel zonder bruikbare productfoto zijn niet aangemaakt. De tellingen en veldcontroles zijn gefaseerd uitgevoerd, niet als één atomaire Shopify-snapshot. De bronvoorraad is geen nieuw geverifieerde livevoorraad.

## Gegevens- en keuzecontract

Eén leveranciers-SKU blijft één product met één verkochte variant. Winkelmerk en vendor zijn **Cottoceramix**; oorspronkelijke fabrikant en bronserie blijven herleidbaar. Exacte SKU's, inclusief terminale punten, blijven behouden. Bestaande producten worden niet blind opnieuw aangemaakt of generiek overschreven.

Bij m²-artikelen is de native variantprijs de doosprijs inclusief btw, de eenheidsprijs per m² en het bestelaantal een geheel aantal dozen. Bevestigde doosinhoud en gekozen exacte maat/dikte zijn leidend. Onbekende optionele kleur, afwerking, maat, dikte, stuksinhoud of fysiek gewicht wordt weggelaten. Er wordt geen aanname of fictief gewicht van 0 kg gepubliceerd. Onvolledige artikelen blijven afzonderlijk in plaats van een onbewezen familiecombinatie te krijgen.

De unitroute gebruikt `order_mode=unit` binnen `custom.bron_toelichtingen_json.value.tiles`, met `sale_unit` en een bevestigd `unit_count` in hetzelfde JSON-object. Dit is geen afzonderlijk `tiles.order_mode`-metafield. De 597 artikelen bestaan uit **539 stuksartikelen, 23 vaste pakken en 35 vaste sets**. Eén native besteleenheid vertegenwoordigt het gehele stuk, pak of set tegen de bevestigde prijs. Alleen bij een bevestigde per-stukprijs wordt die met de vaste pakinhoud vermenigvuldigd. Geen stuk-EAN als afgeleide multipack-GTIN gebruiken; geen onbewezen m²- of strekkende-meterdekking tonen. Bij 134 unitartikelen is het native gewicht bevestigd; bij 463 blijft het onbekende gewicht weggelaten.

De nieuwe bediening hergebruikt vierkante tegelfoto's, uitklapbare kleurkeuze en technisch begrensde families. Dit bewijst geen volledige kopie van elk leveranciersmenu. De daadwerkelijke unitbediening moet nog worden vrijgegeven.

## Uitgevoerde gegevenscontroles

| Controle | Resultaat en grens |
| --- | --- |
| Strict m²-batch | 87.323 controles over 1.127 artikelen, nul fouten; afzonderlijke nacontrole bevestigt ACTIVE, Webshop-publicatie en publieke product-URL |
| Overige m²-batch | 91.398 volledige v2-controles over 1.186 artikelen, nul fouten; daarna 9.489 controles op exacte product-/variantidentiteit, SKU, ACTIVE, publicatie, overlayhandle en publieke URL, nul fouten |
| Unitbatch na categorisatiecorrectie | 41.740 volledige veldcontroles en 21.297 semantische controles over 597 DRAFT-artikelen, nul fouten; 497 families en 1.182 mediabestanden READY |
| Behoud bestaande 854 producten | 846 actieve producten behouden status, publicatie, handle en publieke URL; acht HOLDs blijven DRAFT en ongepubliceerd. Geen nieuwe volledige vergelijking van bestaande prijzen, voorraad, metafields of media |

De bron-SKU-paren `MA1003`/`MA1003.`, `MA1005`/`MA1005.` en `MA1017`/`MA1017.` blijven afzonderlijke bronidentiteiten. Vier gerichte handlecorrecties lossen de botsingen op: drie punt-SKU's krijgen `-dot`; de kale `MA1005`-handle is hersteld. Bron-SKU, prijs en bron-JSON zijn behouden; nul artikelen uitgesloten. De v2- en publicatienacontroles omvatten deze uitvoering.

`MC0031` is gericht als **Onderhoudsmiddelen** gecategoriseerd en aan de bestaande onderhoudscollectie gekoppeld; de onjuiste tegeltoepassing is verwijderd. Product-/variant-ID, native velden, bron-JSON, groepsreferenties en beelden zijn behouden. Alleen deze categorisatie is aangepast; de overige 596 unitinputs zijn ongewijzigd. Bovenstaande unitcijfers gelden voor de **definitieve controle na deze correctie**, niet voor de eerdere 41.742-controleversie.

## Thema en code

Het data-/importcheckpoint blijft [916a431e180e28672b70feebc574ca345c6fbe80](https://github.com/jlamping1997/badkamercity/commit/916a431e180e28672b70feebc574ca345c6fbe80). De aanvullende beschikbaarheidslabels staan in codecheckpoint [4976dd7ee56e9dd664e4e19198b6e2d852a46b2b](https://github.com/jlamping1997/badkamercity/commit/4976dd7ee56e9dd664e4e19198b6e2d852a46b2b), op dezelfde branch `fix/product-cards-2026-10-14`, bron `shopify/current/`. De labelcorrectie wijzigt geen importdata, prijzen, leveranciersvoorraad of publicatiestatus.

De verse rolcontrole van **21:38 UTC** bevestigt **MAIN 196238639370 — BadkamerCity - Re-Bel tegelkeuze** en **UNPUBLISHED 196246372618 — BadkamerCity - Cottoceramix volledig assortiment**. De volledige previewmanifestcontrole van 21:38:27 UTC slaagt: **1.385 bestanden, exact achttien featurepaden, zestien gewijzigde bestaande bestanden en twee nieuwe helpers**. Alle achttien featurepaden komen exact overeen met de gevalideerde lokale bytes; geen onverwachte verschillen. De vijf bestanden van de beschikbaarheidscorrectie zijn ook afzonderlijk per MD5 exact teruggelezen. De actuele MAIN-metadata is ongewijzigd; de eerdere volledige vergelijking van 1.383 MAIN-baselinebestanden blijft behouden. Deze laatste ronde heeft alle previewbestanden herlezen, niet opnieuw ieder MAIN-bestand. Geen themapublicatie door de uitvoerder.

| Previewbestanden | Aantal |
| --- | ---: |
| `assets/bc-porcelanosa-buybox.js`, `assets/bc-product-sticky.js` | 2 |
| `locales/en.default.json`, `locales/nl.json` | 2 |
| `sections/bc-brand-directory.liquid`, `sections/main-product.liquid` | 2 |
| `snippets/bc-card-delivery.liquid`, `snippets/bc-card-product-search.liquid`, `snippets/bc-card-tile-price.liquid`, `snippets/bc-cart-delivery.liquid`, `snippets/bc-cart-unit-label.liquid`, `snippets/bc-porcelanosa-buybox.liquid`, `snippets/bc-tile-choice-data.liquid`, `snippets/card-product.liquid` | 8 |
| Nieuwe `snippets/bc-cotto-unit-mode.liquid` | 1 |
| Aanvullend gewijzigde `snippets/facets.liquid`, `snippets/bc-collection-active-filters.liquid` | 2 |
| Nieuwe `snippets/bc-native-facet-value-label.liquid` | 1 |

De oorspronkelijke vijftien bestanden zijn officieel gevalideerd met bestaande niet-blokkerende waarschuwingen, per ronde vastgelegd. De vijf bestanden van de labelaanvulling zijn opnieuw officieel gevalideerd; één bestaande complexiteitswaarschuwing bij `facets.liquid` blijft niet-blokkerend. Acht gerichte rendertests voor de beschikbaarheidslabels slagen afzonderlijk. De 80 Python-tests en 36 render-/runtimechecks van het importcodecheckpoint blijven eerdere PASS-resultaten en zijn voor deze labelcorrectie niet herhaald. Die 36 bestaan uit twaalf unitroute-, zes kleurkeuze-, zeven bestaande pilot-, vier kaartleverings- en zeven bestaande kaartprijscontroles. Offline tests en Admin-readback vervangen geen echte unitkoopproef.

Alleen op de native collectie `cottoceramix` wordt `filter.v.availability=1` getoond als **Bestelbaar** en `0` als **Niet bestelbaar**. Dit past bij de Shopify-bestelbaarheid van ongetrackte artikelen met doorbestellen toegestaan; het is geen leveranciersvoorraadbelofte. Dezelfde tekst geldt op negen renderplekken: desktop, mobiel, schermlezertekst en actieve chips. Native filterwaarden, aantallen, selectiegedrag en verwijder-URL's blijven behouden. Search, andere collecties/merken en de externe API/index zijn niet gewijzigd. De echte Chrome-desktopcontrole van **21:40 UTC** in het juiste Cottoceramix Draft-thema slaagt: standaard **Bestelbaar (3159)** en **Niet bestelbaar (0)**; de nuloptie is uitgeschakeld. Aanvinken toont de zichtbare chip **Beschikbaarheid: Bestelbaar**. Wissen via die chip geeft na afloop van de native AJAX-update weer een uitgevinkt veld, nul actieve chips en 3.159 producten met 24 kaarten, geladen foto's en geen horizontale overloop. Native desktop-/mobiele facet-chips zijn tevens als verborgen, correct gerenderde DOM gecontroleerd; dit is geen werkelijke mobiele viewport- of telefoonproef. Er is geen winkelwagenactie uitgevoerd. De aparte leverancierslevertekst op productkaarten is geen beschikbaarheidsfilter en blijft broninformatie.

## Browserbewijs en open unitvrijgave

De bestaande echte Chrome-desktopcontrole van vóór de beschikbaarheidslabelaanvulling op 1.363 × 936 pixels bevestigt in het Cottoceramix-concept de native collectie met **3.159 producten**, 24 kaarten, geladen eerste drie productfoto's, zichtbare paginering tot pagina 132 en geen horizontale overloop. Pagina 132 is hiermee niet afzonderlijk bezocht en niet elke catalogusfoto visueel gecontroleerd. Eerdere echte navigatie naar pagina twee, tijdens de tussentelling van 1.973 producten, bevestigde 24 unieke bestemmingen per pagina en geen overlap. De melding over tijdelijk niet beschikbare uitgebreide filters blijft zichtbaar.

Bij Sweet Bars zijn alle acht kleurtegelfoto's en de geselecteerde Royal Green-hoofdfoto geladen. Deep White → Royal Green bewaart 2,5 m² en 10% snijverlies en geeft zeven dozen voor €398,44. Dit is m²-browserbewijs; geen winkelwagen- of unitbewijs.

De echte unitbrowser- en winkelwagenproef is **BLOCKED_PRODUCT_PREVIEW_THEME_BINDING**. Twee gerichte previewpogingen bleven het oude MAIN/Re-Bel-thema tonen; de zichtbare toolbaractie leverde geen bruikbare ondersteunde deel-URL op. Daardoor is de nieuwe unitbediening niet daadwerkelijk getest. Er is **geen unit-UI- of cart-PASS** en ook geen bewezen rendererdefect. Alle 597 unitartikelen blijven DRAFT. Fysieke telefoon, adresafhankelijke verzending, checkout en betaling zijn niet getest.

## Zoekindex en feed

De verse openbare indexcontrole van **21:39:41 UTC** is technisch gezond: beide HTTP-aanvragen geven 200, met consistente generatie **20261105T210044_bd0667**. De eerdere vier controles van 21:20 UTC blijven afzonderlijk behouden. De index telt nog **1.973 Cottoceramix-resultaten**, tegenover 3.159 gepubliceerde artikelen. Het telverschil is 1.186; dit is geen afzonderlijke audit van ontbrekende SKU's. De eerdere meting van slechts 22 artikelen is achterhaald. Er is geen actuele indexstoring bewezen en geen volledige zoekvindbaarheid vrijgegeven. De generatie bewijst niet of de verversing automatisch of handmatig liep.

Controleer na de unitvrijgave opnieuw of de bestaande synchronisatie al is bijgewerkt. Alleen indien nodig de reguliere synchronisatie verversen; geen oude eenmalige reparatie-installer opnieuw uitvoeren. Een automatische Cottoceramix-voorraad-/levertijdfeed is niet ingericht. Een latere feed moet op leverancier plus exact SKU koppelen, bestaande product-/variant-ID's behouden en winkelmerk, titels, SEO, groepen, referenties en handmatige correcties beschermen.

## Bron-HOLDs

| Reden | SKU's | Stand |
| --- | --- | --- |
| Acht bestaande bronconflicten | `MAR128L`, `MAR130L`, `MAR129L`, `MAR132L`, `MAR131L`, `VA3202`, `VA3201`, `VA3203` | Bestaande DRAFT-artikelen; bronidentiteit, maat/kleur of afwerking bevestigen |
| Zes afwerkingsconflicten | `GQR107M`, `MA1070`, `ES1271`, `EX1170`, `EX1171`, `MA1071` | Niet aangemaakt; tegenstrijdige afwerking oplossen |
| Geen bruikbare echte productfoto | `AD5917` | Niet aangemaakt; geen placeholder als productfoto publiceren |

## Eerstvolgende handeling en vervolgvolgorde

**De eigenaar publiceert het gecontroleerde thema “BadkamerCity - Cottoceramix volledig assortiment”.** Daarna:

1. Vers controleren welk thema MAIN is en bevestigen dat de gecontroleerde versie actief is.
2. Alleen de zes geregistreerde unitpilots activeren en hun echte kleurkeuze, aantallen, pak-/setprijzen, leverinformatie en winkelwagen controleren: `CB1801`, `CB1802`, `FGB323M`, `UM0104`, `KE4815`, `MC0031`.
3. Alleen bij PASS de overige 591 unitartikelen publiceren en de status/publicatie opnieuw teruglezen. Bij een fout de betrokken pilots gericht DRAFT herstellen; de 591 blijven DRAFT.
4. Zoekindexdekking opnieuw controleren en uitsluitend indien nodig de bestaande reguliere synchronisatie verversen.

De actuele tellingen, testgrenzen en blokkades staan in [verification-summary.json](verification-summary.json). Herstel alleen op exact geregistreerde nieuwe product-ID's: publicatie gericht verwijderen en zo nodig DRAFT herstellen. Bestaande artikelen en andere merken niet generiek terugrollen; MAIN niet overschrijven. Volledige bronbestanden, mutatiereceipts, herstelkopieën, screenshots, tijdelijke of ondertekende URL's en credentials worden niet openbaar gedeeld.
