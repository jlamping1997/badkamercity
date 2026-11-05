# BadkamerCity — actuele werkstatus

## COTTO-05 — m²-assortiment gepubliceerd; native units wachten op eigenaar · 5 november 2026

**IN_PROGRESS — aanvullende native filtercorrectie.** De Cottoceramix-beschikbaarheidsfilter gebruikte Shopify-bestelbaarheid als label ‘Op voorraad’. Alleen deze native filterwaarden worden ‘Bestelbaar’ / ‘Niet bestelbaar’, inclusief mobiel, schermlezertekst en actieve filters. Vijf themabestanden officieel gevalideerd, acht gerichte renderchecks en onafhankelijke review PASS; codecheckpoint **4976dd7ee56e9dd664e4e19198b6e2d852a46b2b** op de actieve codebranch. Preview-upsert, manifest- en browsernacontrole nog afronden; product-/voorraadgegevens en onderstaande tellingen ongewijzigd.

**PARTIALLY_PUBLISHED / BLOCKED_MERCHANT_THEME_AND_INDEX_LAG.** Verse eindcontrole bevestigt **3.159 ACTIVE en Webshop-gepubliceerde Cottoceramix-artikelen**. Er zijn 3.764 unieke Shopify-producten/varianten: 3.159 ACTIVE en 605 DRAFT, waarvan 597 native stuks-/pak-/setartikelen en acht bestaande bron-HOLDs. De broncheckpointset bevat 3.771 exacte SKU's; zes nieuwe afwerkingsconflicten en AD5917 zonder bruikbare foto zijn niet aangemaakt. Totaal 15 bron-HOLDs, geen extra unit-HOLD.

De 1.127 nieuwe strict-m²-artikelen slagen met 87.323 veld-/groep-/mediacontroles; alle 1.127 publicaties en publieke URL's teruggelezen. De 1.186 overige m²-artikelen slagen met 91.398 controles en daarna 9.489 nacontroles op exacte SKU-/product-/variantidentiteit, ACTIVE, Webshop en URL. Vier gerichte Malaga-handlecorrecties behouden de afzonderlijke punt-SKU's; nul uitsluitingen. De 854 bestaande producten zijn apart teruggelezen: 846 blijven ACTIVE/gepubliceerd met behouden handles/URL's; acht HOLDs blijven ongepubliceerd DRAFT.

Alle **597 native unitartikelen blijven DRAFT**. De actuele gecombineerde readback na de ene MC0031-onderhoudscorrectie slaagt: 41.740 hoofdcontroles en 21.297 onafhankelijke semantische controles, nul fouten; 1.182 beelden READY en 497 groepen exact. 134 gewichten bevestigd, 463 onbekende gewichten bewust weggelaten; geen m²-claims op de unitroute. MC0031 gebruikt de bestaande onderhoudscollectie; SKU, variant, prijs €39,95, bron-JSON, foto's en referenties behouden. De overige 596 unitrecords zijn exact ongewijzigd.

**Themapublicatie door eigenaar vereist:** MAIN **196238639370** blijft ongeschreven, alle 1.383 baselinebestanden checksumgelijk. Alleen **UNPUBLISHED196246372618 — BadkamerCity - Cottoceramix volledig assortiment** bevat de 15 gevalideerde bestanden: exact 14 wijzigingen en één nieuwe helper, 1.384 bestanden totaal. Codecheckpoint **916a431e180e28672b70feebc574ca345c6fbe80**, bron `shopify/current/`, vaste branch `fix/product-cards-2026-10-14`; geen broncodewijziging sinds dit checkpoint.

Echte conceptbrowser: Cottoceramix-collectie toont 3.159 producten, 24 kaarten per pagina en paginalink132, de eerste drie foto's geladen en geen overloop; bestaande melding over uitgebreide filters blijft zichtbaar. Sweet Bars heeft acht geladen kleurkeuzen; Deep White→Royal Green bewaart 2,5m²+10% en rekent zeven dozen/€398,44. De echte unit-UI/cartproef blijft **BLOCKED** doordat de gebruikte DRAFT-productpreview aan het oude MAIN-thema bleef gebonden; geen unit-koopbewijs of rendererfout geclaimd.

De openbare zoekdienst is gezond (HTTP200), consistente generatie **20261105T210044_bd0667**, inmiddels 1.973 Cottoceramix-resultaten; CF3009 en AH6571 elk één. Het telverschil met het gepubliceerde totaal is 1.186; geen individuele ontbrekende-SKU-audit uitgevoerd. Geen timerstoring of verplichte reparatie bewezen; volledige zoekopname van 3.159 nog niet bevestigd. SSH/VPS-route vanuit deze uitvoering niet bereikbaar.

[Definitieve beperkte overdracht en publicatiegrens](cottoceramix/2026-11-05/full-catalog/README.md) · [Openbare verificatiesamenvatting](cottoceramix/2026-11-05/full-catalog/verification-summary.json). Geen automatische Cottoceramix-feed ingericht. Fysieke telefoon, adresafhankelijke verzending, checkout en betaling niet uit de Admin-/offlinetests afgeleid.

**Exact één volgende handeling:** eigenaar publiceert **BadkamerCity - Cottoceramix volledig assortiment (196246372618)**. Daarna verse MAIN-rol/hashcontrole, zes unitproefartikelen activeren en echte unit-/cartproef uitvoeren; alleen na PASS de overige 591 unitartikelen publiceren. Vervolgens indexopname opnieuw controleren en uitsluitend indien nodig de bestaande reguliere synchronisatie uitvoeren.

## COTTO-04 — tweede controle productkeuzes · 5 november 2026

**REVIEW_COMPLETE / VERIFIED_BROWSER / NO_STORE_WRITES.** Zeven live series getest: Funky, Re-Bel, Croccante, Zelij, Magnetism, Lula en Marea Alta Mat. In 26 vastgelegde browsertoestanden kloppen doosafronding en totaalbedrag; geen horizontale overloop bij desktopviewport1363×936. Kleur-, formaat-, foto-, titel-, verpakkings- en prijswissels werken in de geteste routes. In m²-modus blijven gewenste m² en snijverlies behouden; na handmatig dozen invoeren blijven juist de dozen behouden. Uit-/inklappen bewaart de gekozen kleur, ook bij Zelij met24kleuren.

Onafhankelijke selectiecontrole op824 gepubliceerde nieuwe producten/126families: **11.314 kernwissels**, geen ongewenste technische verandering door alleen een kleurwissel. Dit is een bron-/runtimecontrole, geen live browserklik op elk artikel. Veertig formaat→dikte-koppelingen zijn verwacht; Croccante60→80cm met9→10mm ook live bevestigd. De vier relevante componentbestanden zijn checksumgelijk aan MAIN **196238639370**;846 actieve Cottoceramix-artikelen bij begin en einde.

Geen functionele blokkade gevonden in deze steekproef. Verbeteringen geparkeerd: expliciete vormnamen bij onder meer Magnetism/Cottage, aparte uitvoeringnavigatie tussen model-/afwerkingsfamilies, bronkleurnamen bij Croccante normaliseren. Afrondingsverschillen van maximaal één cent in de afgeleide m²-prijs vragen geen prijsbatch. Eén laag geprioriteerde lifecycle-kwestie alleen in een verwijdertest gereproduceerd; geen fout in de normale productwissel bewezen. Geen product-/prijs-/voorraad-/theme-mutatie of publicatie.

[Uitgevoerde scenario's, beoordeling en grenzen](cottoceramix/2026-11-05/menu-review/README.md) · [Beperkte openbare verificatie](cottoceramix/2026-11-05/menu-review/verification.json). Fysieke telefoon, nieuwe cartactie, verzending, checkout/betaling en livefeed deze ronde **NOT_TESTED**. Geen actieve COTTO-04-schrijver na overdracht.

**Exact één volgende handeling binnen het cataloguswerk:** de al openstaande aparte stuks-/m¹-route voor onder meer Casablanca-randstukken en Enso als kleine volgende batch voorbereiden; bovenstaande UX-ideeën blijven apart van die import.

## LAUNCH-03 — eenmanszaakadres en retourlocatie apart bevestigd · 5 november 2026

**OWNER_CONFIRMED / DOCS_UPDATED / NOT_PUBLISHED.** Bedrijfsadres van de eenmanszaak blijft **Hengelolaan70,2545JR 's-Gravenhage**. Werk-/retourontvangstlocatie is **bij Harry Suiker, Zichtenburglaan150,2544EB 's-Gravenhage**. Eigenaar bevestigt de retourafspraak; postcode via officiële contactpagina gecontroleerd. Harry Suiker wordt niet de verkoper.

[Bedrijfsgegevens](livegang-seo/BEDRIJFSGEGEVENS.md), [retourconcept](livegang-seo/retouren/RETOURBELEID_CONCEPT.md), modelformulier, footerplan en taken bijgewerkt. **BC-LIVE-001A DONE**; eigen zakelijk telefoonnummer volgt later, geen Harry Suiker-nummer overnemen. Geen algemene vrije-inloop-/afhaalbelofte. Oudere LAUNCH-02-opmerkingen dat retouradres nog onbekend is, zijn hiermee historisch.

**Volgende handeling voor livegang:** volledig btw-id/juridische identiteit en retourkosten/raming voor grote goederen aanvullen; telefoon later zodra beschikbaar. Retourfunctie/mail-/publicatiecontroles blijven open. Geen Shopify- of Google-mutatie; andere actuele taken behouden.

## VERLAVIO-SET-01 — inbegrepen onderdelen douchesets · 5 november 2026

**APPLIED_VERIFIED / 78 SETS LIVE / 12 SOURCE_HOLDS.** De eigenaar vroeg dezelfde onderdelenweergave als Hotbath IBS70. 36 Milaan-,36 Palermo- en6 Porlezza-sets hebben nu462 bevestigde inbegrepen onderdelenregels uit108 losse Verlavio-artikelen. Uitsluitend156 waarden in de bestaande `bc_data.set_components` en `bc_data.component_products` toegevoegd; geen theme-writes of publicatie. MAIN blijft196238639370.

Alle78 bronpagina's exact opnieuw gecontroleerd; alle156 waarden teruggelezen in de volledige861-productinventaris, overige vastgelegde velden gelijk. Alle78 live productpagina's/462 regels PASS op aantallen, namen, SKU's, exacte variantlinks en prijzen. Desktopbrowser1363px bevestigt pilotCKK_2015. IBS70CR347 bleef exact gelijk met8 onderdelen; herhaling geeft0 writes. Mobiele browser en aankoop niet uitgevoerd.

[Uitvoering, grenzen en herstel](fabriecio/2026-11-05/set-components/README.md) · [Beperkte openbare verificatie](fabriecio/2026-11-05/set-components/verification.json). Twaalf Venetie-sets blijven zonder lijst wegens ontbrekend leveranciersbewijs. Volgende inhoudelijke handeling binnen deze scope: expliciete samenstelling voor deze twaalf opvragen/verkrijgen; niet raden. COTTO-03,LAUNCH-02 en overige lopende werkzaamheden hieronder blijven van kracht.

## LAUNCH-02 — bedrijfsgegevens,30dagenretourconcept en praktische controles · 5 november 2026

**OWNER_INPUT_RECORDED / DRAFT_READY / NOT_PUBLISHED.** Jackson levert bedrijfsadres/KvK/IBAN en kiest jaarrond30dagen retour. Opgenomen in [bedrijfsgegevens](livegang-seo/BEDRIJFSGEGEVENS.md); btw-id **NL00548932B64** mist in het opgegeven formaat één cijfer vóór B, telefoon/juridische handelsnaam en fysiek retouradres nog niet compleet. Geen cijfer of oude showroomgegevens gegokt. IBAN-checksum geldig, geen rekeninghouderschap of officiële KvK/VIES-koppeling geclaimd.

Eigen [retourconcept](livegang-seo/retouren/RETOURBELEID_CONCEPT.md) en leeg modelformulier voorbereid:30dagen melden, daarna14dagen terugsturen, geen novemberverlenging. Algemene uitsluiting “speciaal besteld” niet overgenomen; echt individueel maatwerk apart toetsen. Referentie is geen juridische bron; geen automatische50%-aftrek of algemene tegel-/douchewanduitsluiting. Retouradres en vooraf kenbare grote-retourkosten/raming nog aanvullen.

[Bestel-/contact-/retourchecks](livegang-seo/CONTROLES.md) maken het werk voor Jackson en uitvoering afzonderlijk afvinkbaar. Het native retourformulier toont paginasucces, maar een eigen directe bewaarbare klantmail is niet in de bron aangetroffen; werkelijke mailbox-/platformafhandeling nog testen. Herroepingsfunctie/ontvangstbevestiging en publicatie van het modelformulier staan expliciet open. Geen formulierinzending, order of betaling in deze taak uitgevoerd.

[Google-productcontrole in gewone taal](livegang-seo/GOOGLE_PRODUCTCONTROLE.md): bestaande data automatisch controleren, alleen uitzonderingen aan eigenaar voorleggen, geschikt assortiment niet laten wachten op ontbrekende beelden. Verlavio is publieke merknaam, Fabriecio blijft interne bron. Latere FAB-03/04-bewijzen vervangen het oude algemene koopbaarheidsprobleem; foto-/Google-vrijgave niet uit die proeven afleiden. Jackson werkt verder aan levertijden en foto’s; die taken niet als volledig getest afgevinkt. Lagoo-fotoverbod behouden.

[Universele-footerplan](livegang-seo/FOOTER_EN_BELEID.md): bestaande standaardfooter hergebruiken via footer-group/compact_homepage, volledige navigatiedekking bewaren; beide renderers tonen al shop.policies. Tijdens de read-only controle veranderde MAIN van196227170570 naar **196238639370 — BadkamerCity - Re-Bel tegelkeuze** door publicatie buiten deze uitvoering. Dit is geen schrijfbaar concept meer. Geen themefilewrite, policy-/product-/Google-instelling gewijzigd of thema gepubliceerd; COTTO/SEARCH-werk behouden.

**Exact één volgende handeling voor LAUNCH-02:** ontbrekend [gegevenspakket](livegang-seo/BEDRIJFSGEGEVENS.md) aanvullen: volledig btw-id/telefoon/juridische naam, bevestigd Nederlands retouradres en grote-retourkosten/raming. Daarna het al voorbereide beleid en de bestaande footerroute gericht afronden. [Bijgewerkte taken](livegang-seo/TAKEN.md) · [logboek](livegang-seo/LOGBOEK.md). Geen actieve LAUNCH-02-schrijver na overdracht.

## COTTO-03 — eerste grote catalogusbatch gepubliceerd · 5 november 2026

**PUBLISHED_VERIFIED / NEXT_BATCHES_OPEN.** Op expliciete opdracht 832 nieuwe Cottoceramix-artikelen aangemaakt; exact **824 ACTIVE én op Webshop gepubliceerd**, acht bronconflicten DRAFT/niet gepubliceerd. Alle 832 status-/kanaalwaarden onafhankelijk teruggelezen: nul afwijkingen. De 22 Re-Bel-artikelen zijn op ID/titel/vendor/handle/status/variant/prijs/mediareferenties onveranderd. Shopify telt nu **846 actieve Cottoceramix-artikelen**. Uit de gecorrigeerde werkset van 3.770 resteren **2.916 nog niet aangemaakte** artikelen; samples/vervallen artikelen en drie extra nieuwe feedrecords blijven apart.

126 nieuwe coherente kleurfamilies gebruiken de bestaande vierkante keuze. Bronmodellen/afwerkingen/formaten zijn waar nodig gesplitst; geen claim dat elk leveranciersmenu exact is gekopieerd of alle families één gezamenlijke selector hebben. Groepsreferenties volledig gelezen en correct. De gekozen Z/AA-maat en AF-dikte gaan vóór oude AB/AC/AE-waarden; een gevonden mapperfout is vóór verdere publicatie hersteld. Vijftien originele bronfoto's met octet-stream-header ongewijzigd als JPEG aangeleverd en gekoppeld; **2.705 beelden READY** over de 832 nieuwe artikelen.

**Bewijs:** gefaseerde volledige veld-/groeps-/fotoreadback, **64.900 controles PASS**; 29 script-/regressietests PASS. Live Chrome Funky: twaalf kleuren, Amber→Seaport, juiste prijs en 10m²+10%=14dozen/€1.234,24. Twee dozen daadwerkelijk toegevoegd: 1,68m²/€176,32, juiste per-dooslabels; eigen regel verwijderd, cart leeg. Monaco-R: vijf kleuren, Beige→Verde, €79,95/m² en €102,34/doos/1,28m². Fysieke telefoon, adresafhankelijke verzending, checkout/betaling en Google-/zoekindexopname deze ronde NOT_TESTED.

De eigenaar heeft het vorige concept gepubliceerd: **MAIN196238639370 — BadkamerCity - Re-Bel tegelkeuze**. De drie kleurcomponenthashes ongewijzigd bevestigd. Geen themabestand geschreven of thema gepubliceerd in COTTO-03; andere merken behouden. Algemene bulkmutaties geblokkeerd door de connector; begrensde toegestane API-batches gebruikt. Geen automatische Cottoceramix-feed of importworker ingericht.

Codecheckpoint **fdac6c95fbfbb751c9f18bffe5b35531acb8aca0**, bron `shopify/current/`, vaste branch `fix/product-cards-2026-10-14`. [Batch, gegevenscontract, bewijs en herstel](cottoceramix/2026-11-05/rollout/README.md). Geen actieve COTTO-03-schrijver na overdracht.

**Exact één volgende handeling voor COTTO-03:** aparte stuks-/m¹-route voor onder meer Casablanca-randstukken en Enso als volgende kleine batch voorbereiden; daarna bronconflicten/ontbrekende waarden gericht oplossen. Geen huidige batch opnieuw aanmaken of bestaande SKU's blind upserten. Oudere COTTO-02-publicatiestatus hieronder is geschiedenis.
## COTTO-02 — Cottoceramix en uitklapbare tegelkleuren gereed · 5 november 2026

**ADMIN_APPLIED_VERIFIED / PREVIEW_VERIFIED / AWAITING_MERCHANT_PUBLICATION.** Alle 22 bestaande Re-Bel-artikelen hebben Cottoceramix als vendor, titelvoorvoegsel en zichtbaar Merk; beschrijving, SEO en 70 afbeeldings-altwaarden aangepast. Volledige voor-/navergelijking: nul afwijkingen van plan; identiteiten, URL's, publicaties, doos-/m²-prijzen, verpakking, gewicht, voorraadbeleid en fotoreferenties behouden.

Het bestaande concept toont vier vierkante tegelfoto's inclusief de gekozen kleur; “Bekijk alle 11 kleuren” / +7 opent de volledige vierkolomskeuze. Open toestand blijft bij productwissels bewaard. Opt-in via `tiles.color_picker_layout="expandable_grid"`; overige tegelgroepen behouden de rail. Zes nieuwe semantische kleurchecks en zeven bestaande pilotchecks PASS; drie productbestanden en de neutrale QA-template door Liquid-validator goedgekeurd. Echte Chrome: uit-/inklappen, alle elf foto's, Blanc→Perle en 60→100 cm met behoud van de andere keuze; componentkaders 320/390 CSS-pixels zonder overloop. Fysieke telefoon, volledige mobiele PDP en checkout/betaling deze ronde NOT_TESTED.

**Thema's:** MAIN **196227170570** is volledig 1381/1381 checksumgelijk gebleven. Alleen **UNPUBLISHED196238639370 — BadkamerCity - Re-Bel tegelkeuze** bevat het nieuwe menu. Finale inventaris: 1383 bestanden, elf verschillen tegenover MAIN — vier eerdere cartfiles, drie nieuwe productcomponentfiles, één inactieve neutrale QA-template en drie laatste SEARCH-01-files. De parallelle zoekpatch `05a54c8d8b7df8c41644eec7abd5bd812a3cb6d5` behouden; oude COTTO-01-zoekhash is niet langer de huidige zoekbaseline. COTTO-02 heeft geen backendindex gewijzigd en publiceert geen thema.

Codecheckpoint **cb55eb45f1e32f9044a3b91279e0c41aa1b7c410**, vaste branch `fix/product-cards-2026-10-14`, bron `shopify/current/`. [Gegevens, menucontract, bewijs en herstel](cottoceramix/2026-11-05/rebel/brand-colors.md). Geen actieve COTTO-02-schrijver na overdracht.

**Exact één volgende handeling voor COTTO-02:** eigenaar beoordeelt en publiceert **BadkamerCity - Re-Bel tegelkeuze**; daarna verse MAIN-rol en publieke merk-/kleurenweergave controleren. SEARCH-01 en verdere import blijven afzonderlijk. De COTTO-01-merk-/menubeschrijving hieronder is het vorige checkpoint.
## COTTO-01 — Re-Bel live; winkelwagencorrectie gereed voor eigenaarspublicatie · 5 november 2026

**PRODUCTS_LIVE_VERIFIED / CART_PREVIEW_VERIFIED / AWAITING_MERCHANT_PUBLICATION.** Exact 22 nieuwe Revoir Paris Re-Bel-artikelen ACTIVE en gepubliceerd op de Webshop: 11 kleuren × 60×60/100×100 cm. Gedeeld kleur-/formaatmenu, native m²-eenheidsprijzen, juiste doosprijzen, dozen als bestelaantal, 70 afbeeldingen READY, volledige specificaties en gewichten gecontroleerd. Actuele XML gebruikt; vijf voorraadverschillen tegenover Excel verwerkt. EAN RR6011 heeft een onjuist controlecijfer en is niet als barcode gepubliceerd. [Uitvoering, productregister, hergebruik en herstel](cottoceramix/2026-11-05/rebel/README.md).

**VERIFIED_ADMIN / VERIFIED_BROWSER.** Alle 22 productveldsets, 22 groepslijsten met elk 22 referenties en Webshoppublicaties teruggelezen. Live kleur/maat wisselt met behoud van de andere keuze; 10 m² + 10% geeft 8 dozen/11,52 m²/€794,32 bij 60 cm of 6 dozen/12 m²/€959,40 bij 100 cm. Ongeldige invoer blokkeert bestellen. Live en preview elk drie dozen werkelijk toegevoegd voor €297,87; alleen eigen testregel verwijderd, cart leeg. Previewbevestiging én cart tonen nu “per doos”, de juiste leveranciersleverinformatie en €68,95/m². Toolkit 5/5 (gecombineerde revisie 2) en zeven lokale render-/matrixchecks PASS. Fysieke mobiel, adresafhankelijke verzending, checkout en betaling NOT_TESTED. Automatische Cottoceramix-feedverversing is niet ingericht. Echte zoekproef op RR6001 en Re-Bel geeft nog nul; zoekvindbaarheid van deze nieuwe serie blijft OPEN bij het aparte indexherstel, zonder veronderstelde oorzaak.

**Rollen en scope:** MAIN **196227170570 — BadkamerCity - Verlavio voorraad en levertijd** is 1381/1381 behouden. Nieuw UNPUBLISHED **196238639370 — BadkamerCity - Re-Bel tegelkeuze** was vooraf 1381/1381 identiek en heeft finaal 1382 bestanden met exact vijf bedoelde afwijkingen: de vier winkelwagenbestanden en de al gecontroleerde zoekbescherming uit SEARCH-01. Geen themapublicatie door uitvoerder; producten zijn al live, winkelwagencorrectie alleen in dit concept. Branch `fix/product-cards-2026-10-14`, bron `shopify/current/`. Andere merken, instellingen en de Lagoo-foto-instructie behouden. De oudere FAB-04-overdracht hieronder dateert van vóór de inmiddels waargenomen eigenaarspublicatie van het Verlavio-voorraadthema.

**Integratie SEARCH-01:** het byte-identieke zoekbestand (MD5 `e0783b4ed15e1acc70ff1518cf2b5f20`) uit concept196116087050 is in dit COTTO-concept overgenomen. De bestaande 23 runtimechecks slagen ook hier. Publiceer alleen het gecombineerde COTTO-concept; het losse zoekconcept mist de vier winkelwagenbestanden en mag daarna niet als latere release gebruikt worden. Backendindex/SSH zijn niet gewijzigd.

**Geen actieve COTTO-01-schrijver of feedworker. Exact één volgende handeling:** eigenaar beoordeelt Re-Bel en publiceert **BadkamerCity - Re-Bel tegelkeuze** in Shopify. Daarna verse MAIN-rol en de gepubliceerde winkelwagenlabels controleren, vóór verdere import.

## SEARCH-01 — index en prijsweergave live; afgerond · 5 november 2026

**OWNER_PUBLISHED / INDEX_LIVE_VERIFIED / UI_LIVE_VERIFIED.** Eigenaar heeft het gecombineerde thema gepubliceerd: **MAIN 196238639370 — BadkamerCity - Re-Bel tegelkeuze**; voorraadthema 196227170570 is UNPUBLISHED. Alle drie live prijsbestanden zijn checksum-exact teruggelezen. De eerdere COTTO-publicatieverzoeken zijn gedateerde checkpoints; geen resterende publicatiestap.

Momentopname van de gecontroleerde indexgeneratie op 5 november rond 18:07 UTC; latere COTTO-03-imports vallen buiten deze meting en vereisen een volgende geslaagde reguliere synchronisatieronde.

De volledige index `bc_sync_20261105t180750_9caf43` is live: 226 profielen, 12.760 globaal / 12.018 shopping, Verlavio 851, Re-Bel 22, RR6001 exact Cottoceramix, beide Nesso-SKU's exact op hetzelfde product met minimum 7800 / price_varies=true/geen Lagoo-afbeelding, Hotbath 7.540 en echte nul voor onzin. Generatieheader gelijk in alle gecontroleerde antwoorden; installercontroles en onafhankelijke publieke nacontrole PASS.

Echte Chrome zonder preview: Verlavio 851 producten / 24 externe kaarten / 0 native / geen foutbanner. Ná themapublicatie via echte header N8271TC + Enter: **één product/één externe Nesso-kaart, “Vanaf € 78,00”, geen foutbanner**. De SKU-alias en nieuwe kaartprijsweergave werken op MAIN.

**SEARCH-01 afgerond; geen server- of publicatiehandeling nodig. Installer niet opnieuw uitvoeren.** De bestaande uurlijkse timer is hervat; een volgende toekomstige uitvoering is nog niet waargenomen. Geen nieuwe automatisering, leveranciersfeedclaim of Shopify-datawijziging. [Eindbewijs en grenzen](search-index/2026-11-05/README.md). COTTO-historie behouden; geen actieve SEARCH-01-schrijver.

**Publicatie-afstemming COTTO-01:** de oorspronkelijke zoekbescherming (historisch controlepunt MD5 `e0783b4ed15e1acc70ff1518cf2b5f20`, vóór de prijsuitbreiding met concept-JS `11de150d3e2797a6f35742a813281fcb`) is meegenomen in **UNPUBLISHED 196238639370 — BadkamerCity - Re-Bel tegelkeuze**, samen met de vier COTTO-winkelwagenbestanden. Eigen 23 runtimechecks en gecombineerde 5/5 validatie PASS. Publiceer alleen dit gecombineerde concept. Het losse zoekconcept 196116087050 mist de winkelwagenwijzigingen en mag daarna niet als latere release worden gebruikt. De nieuwe publieke index vindt Re-Bel 22 en RR6001 als exact Cottoceramix-artikel.

## FAB-04 — historisch checkpoint vóór eigenaarspublicatie: koopbaarheid hersteld · 5 november 2026

**BACKEND_APPLIED_VERIFIED / PREVIEW_VERIFIED / COPY_AWAITING_MERCHANT_PUBLICATION.** De winkel gebruikt Market-driven verzending. De werkelijke Nederlandse verzendoptie bevatte alleen de winkellocatie. Uitsluitend de Verlavio-leverancierslocatie is als oorsprong toegevoegd. Volledige voor-/navergelijking: alleen die toevoeging; bestaande tarief-ID's, €6,95, gratis-verzendingdrempel €100,01 en andere Markets gelijk.

**Volledige readback PASS, 16:37:57 UTC:** alle 861 producten, nul afwijkingen. Exact 29 gewijzigde echte aantallen met CAS uit de feed bijgewerkt; 118 lege aantallen niet verzonnen. De 84 actieve Y-artikelen met leeg aantal behouden CONTINUE/nul; overige voorraadregels DENY. ID's, titels, handles, SKU's, prijzen, tracking, beleid, status en overige locatievoorraad/-velden behouden; 851 ACTIVE / 10 ARCHIVED. Zes bronconflicten op aanvraag; bestaande portalweek 50 behouden waar de feed week 28 meldt.

Publieke eindcontrole 16:31:19 UTC: drie voorraadproducten beschikbaar/InStock met actieve koopknop; nulvoorraadvoorbeeld niet beschikbaar/OutOfStock met week 50; conflict zonder bevestigde voorraadbelofte. Echte Chrome-preview: VSB_2001 met “Op voorraad / Levertijd: 1–2 werkdagen” succesvol toegevoegd via de winkelwagenknop; alleen eigen testregel verwijderd, eindcart nul. Mat Wit navigeert naar VSB_2003 met week 50 en uitgeschakelde knop; GM_3001 toont “Voorraad en levertijd op aanvraag”. Geen checkout-/betalingstest of fysieke telefoon.

MAIN **196116087050** blijft ongeschreven. **UNPUBLISHED196227170570 — BadkamerCity - Verlavio voorraad en levertijd**: vóór wijziging 1.381/1.381 identiek aan MAIN, finaal exact drie bestanden gewijzigd (leveringssnippet en NL/EN-vertaling), alle hashes teruggelezen. 23 leveringsgevallen, 16 menu-/URL-overgangen en drie Liquidvalidaties geldig. De 1–2 werkdagen is winkelbeleid voor de 774 bevestigde actieve Y-artikelen zonder conflict; dit staat niet als apart levertijdveld in de feed. De 71 N-artikelen en zes conflicten volgen hun eigen status.

**Exact één volgende handeling:** eigenaar publiceert **BadkamerCity - Verlavio voorraad en levertijd (196227170570)**; daarna MAIN-rol en drie publieke leverstatussen teruglezen. Geen actieve FAB-04-schrijver of feedworker na overdracht; de aparte COTTO-01-prioriteit hierboven blijft behouden. [Voorraad, oorzaak, herstel en bewijsgrenzen](fabriecio/2026-11-05/stock/README.md). Zes leveranciersconflicten, 53 bronmenu-uitzonderingen en merkenoverzicht blijven open; geen automatische feed of vijfminutenverversing ingericht. FAB-03 hieronder is het gedateerde rebrandcheckpoint; het toenmalige koopbaarheidsonderzoek is door FAB-04 afgerond.

## FAB-03 — historisch rebrandcheckpoint: Verlavio live en volledig gecontroleerd · 5 november 2026

**APPLIED_VERIFIED / MERCHANT_PUBLISHED.** De eigenaar heeft **BadkamerCity - Verlavio merknaam** gepubliceerd. Verse Shopify-controle bevestigt **MAIN 196116087050**; voormalig MAIN 196227170570 is UNPUBLISHED. Alle drie gepubliceerde compatibiliteitsbestanden zijn checksum-exact gecontroleerd. Geen MAIN-filewrite of publicatie door de uitvoerder.

Alle **861 bestaande producten** hebben nu merk Verlavio, de bijbehorende producttitel en exacte merk-tag. **665 keuzemenutitels** en **1.665 afbeeldings-altwaarden** zijn omgezet. Volledige read-after-writecontrole op 15:51:12 UTC: exact gelijk aan het uitvoerplan, nul afwijkingen; eindtelling **861 Verlavio / 0 Fabriecio**. Status blijft 851 ACTIVE / 10 ARCHIVED. Product-/variant-ID's, handles/URL's, SKU's, prijzen, voorraad/-beleid, mediareferenties/-URL's, omschrijvingen, SEO en levering zijn gelijk aan de nulmeting. Menuopbouw, opties en bestemmingen blijven behouden; interne leveranciersvelden en bron-/importtags blijven Fabriecio.

**PASS:** eerst vier Malmö-producten als proef; daarna de volledige catalogusvergelijking. Publieke eindcontrole op 15:49:20 UTC: VSB_2001, VSB_2004 en BKK_1001 geven HTTP 200 met Verlavio in H1, JSON-LD Brand, alle menutitels en productafbeelding-alt; menu's aanwezig. Vooraf alle 665 menu's onder Verlavio getest: 5.425 keuzecontroles / 4.096 URL-wissels / nul fouten. Geen nieuwe fysieke telefoon-, cart-, checkout- of betalingstest.

Het bestaande Uitverkocht-probleem en 53 bronuitzonderingen blijven open; automatische feedkoppeling blijft uitgesteld. De merknaamwijziging bewijst geen koopbaarheid. Verlavio ontbreekt nog in het merkenoverzicht, net zoals Fabriecio daar voordien ontbrak; een eventuele toevoeging is afzonderlijk themawerk.

**Exact één volgende handeling:** de bestaande Uitverkocht-/koopbaarheidsafwijking gericht onderzoeken met een product dat volgens Admin voorraad heeft. Geen merkdatabatches of publicatie meer nodig. Geen actieve schrijver of feedworker na overdracht. [Uitvoering, herstel en testgrenzen](fabriecio/2026-11-05/verlavio/README.md). De FAB-01/FAB-02-blokken hieronder zijn historische checkpoints; hun publicatie-/nulproductclaims zijn niet de huidige status.

## FAB-02 — historisch checkpoint: Verlavio private label voorbereid · 5 november 2026

**AWAITING_MERCHANT_PUBLICATION / PRODUCT_REBRAND_NOT_APPLIED.** Eigenaar wil merk **Verlavio**. Fabriecio blijft intern de leverancier. Verse rollen: **196227170570 is nu MAIN**; eigenaar heeft het vorige concept gepubliceerd. Alleen vendor wijzigen zou de665menu's verbergen. Daarom compatibel concept **UNPUBLISHED196116087050 — BadkamerCity - Verlavio merknaam** gereedgemaakt: eerst zes verschillen exact vanuit MAIN overgenomen, daarna drie files ondersteunen beide merknamen. Alle drie hashes teruggelezen; MAIN niet geschreven.

**PASS:**18Python-tests,16brand/productwissels,12leveringsgevallen,5425keuzecontroles/4096URL-wissels met Verlavio,3Liquidfiles geldig. Privéplan:861merk/titelwijzigingen,665menutitels,1665imagealtwaarden. Actueel nog **861Fabriecio / 0Verlavio**; niets als gewijzigd claimen. Leverancierssleutels en bestaandeURL's/SKU's blijven behouden. De53bronuitzonderingenenhetbestaandeUitverkocht-probleemblijvenopen.

**Exact één volgende handeling:** eigenaar publiceert **BadkamerCity - Verlavio merknaam**. Daarna actueleMAIN/hashcontrole en de voorbereide merkdatamutaties met teruglezing uitvoeren. De Shopify-koppeling staat codewrites alleen in concept toe. Geen actieve schrijver na overdracht. [Uitvoering en hervatten](fabriecio/2026-11-05/verlavio/README.md).

## FAB-01 — historisch checkpoint: Fabriecio productkeuzes en levering in concept · 5 november 2026

**VERIFIED_ADMIN / PREVIEW_VERIFIED / OWNER_REVIEW_PENDING / NOT_PUBLISHED.** Alle 861 Fabriecio-bronartikelen exact aan bestaande Shopify-SKU's gekoppeld. Op 851 actieve artikelen zijn 1.516 nieuwe velden opgeslagen en exact teruggelezen: 665 keuzemenu's en 851 leverinformatie. Prijs, voorraad, status, SKU/variant-ID, handle en featuredMedia onveranderd. Tien gearchiveerde artikelen overgeslagen; 132 actieve artikelen hebben geen bronmenu, één heeft alleen een gearchiveerde tegenhanger. Twee families/53 artikelen blijven op HOLD wegens 26 bronlinks die ongemerkt ook een andere maat/kleur wijzigen.

UNPUBLISHED **196227170570 — BadkamerCity - Fabriecio productkeuzes** is eerst 1.378/1.378 identiek aan MAIN **196116087050** gemaakt. Daarna exact zes featurepaden: twee snippets, main-product, twee locales en een geneutraliseerde ongebruikte QA-template. MAIN 1.378/1.378 ongewijzigd. Geen publicatie. Actuele bron: **shopify/current/** op **fix/product-cards-2026-10-14**, codecheckpoint **ab312b8f3685de23fb34166c307d680d284869e4**.

**PASS:** 17 Python-tests, 5.425 werkelijke Liquid/JS-keuzecontroles/4.096 URL-wissels; native Chrome Malmö-wissels met behoud van kleur/maat, juiste prijs/Week50 en geladen swatches; 320/390 CSS-pixelcomponenten zonder overloop; zes ThemeCheck-files geldig. Fysieke telefoon/cart/checkout niet vrijgegeven. De bestaande publieke Uitverkocht-blokkade blijft open; automatische feedkoppeling is uitgesteld. Limiet256metafielddefinities behouden; twee nieuwe ongestructureerde JSON-velden zonder bestaande definities te verwijderen.

[Uitvoering, herstel en grenzen](fabriecio/2026-11-05/product-choices/README.md) · [getelde verificatie](fabriecio/2026-11-05/product-choices/verification.json).

**Exact één volgende handeling:** Jackson bekijkt het concept **BadkamerCity - Fabriecio productkeuzes**, te beginnen bij Malmö. Geen actieve schrijver na overdracht. Andere dossiers en het Lagoo-fotoverbod blijven behouden.

## LAUNCH-01 — vast dossier voor livegang, Google en SEO · 5 november 2026

**DOCUMENTATION_READY / READ_ONLY_BASELINE / SETUP_NOT_EXECUTED.** Eigenaar wil bestaande verkoopklare producten nu vindbaar maken en het assortiment daarna uitbreiden. Vast dossier [Livegang & SEO](livegang-seo/README.md) aangemaakt: [taken/acceptatie](livegang-seo/TAKEN.md), webshopbasis, account-/gegevensstromen, Search Console, Merchant Center, GA4/privacy, SEO-roadmap, paginaregister, volledig niet-product-URL-register en logboek.

Verse Shopify-read: MAIN **196116087050**, hoofdadres HTTPS badkamercity.nl, NL, taxesIncluded=true; zeven app-installaties volledig gelezen, Google & YouTube niet aangetroffen. Alleen standaard privacybeleid ingevuld; standaard refund/terms/shipping-URL's geven404. Retourformulier en Contact zijn publiek200; ontvangst en volledige bedrijfsinformatie niet bewezen. Homepage mist meta description. Alle17kind-sitemaps gelezen: **11.887unieke product-URL's**,225collecties,119Pages,éénblog,éénartikel; dit is geen indexatie-/koopbaarheidsmeting. Zes productvoorbeelden met head/schema onderzocht. FabriecioGM_1002 meldt schemaOutOfStock en ontbreekt in deze product-sitemapcapture; oorzaak open.

Route: bestaand Merchant Center **5898992928** hergebruiken (account/status alleen eerder door eigenaar gemeld), standaard Google & YouTube-koppeling, gratis vermeldingen eerst; Ads later afzonderlijk. Google-login, domeinverificatie, Search Console-indexatie en GA4 niet gecontroleerd. **Lagoo-fotoverbod behouden**: geen foto's terugzetten; beeldloze artikelen afzonderlijk uit de Google-productbestemming houden zolang ze niet aan de beeldvereiste voldoen. Bestaande catalogus-/kleur-/LVS-/offerteafspraken blijven gelden.

Uitsluitend documentatie op main en de bestaande codebranch **fix/product-cards-2026-10-14**; themabron blijft **shopify/current/**. Geen Shopify-write, appinstallatie, feedactivering, advertentiebudget, formulierinzending of publicatie. Geen browser-/mobiel-/checkout-/betalingstest of Windows-controle. [Nulmeting en grenzen](livegang-seo/bewijs/2026-11-05-nulmeting.json) · [logboek/herstel](livegang-seo/LOGBOEK.md).

**Exact één volgende handeling:** **BC-LIVE-001** — de werkelijke verkopersgegevens en bezorg-/retourafspraken vaststellen om ontbrekende winkelinformatie gericht af te ronden. Andere dossiers blijven behouden; geen actieve schrijver na overdracht.

## LAGOO-19 — alle productafbeeldingen verwijderd · 4 november 2026

**VERIFIED_ADMIN / LIVE_PRODUCT_CHECK.** Op expliciete eigenaaropdracht alle Lagoo-productafbeeldingen onmiddellijk verwijderd. Verse inventaris: **232 Lagoo-producten**, waarvan 175 met samen **1.788 afbeeldingskoppelingen** naar 1.763 unieke bestanden. Eén proefverwijdering met readback, daarna acht opeenvolgende batches via `fileUpdate.referencesToRemove`; alle antwoorden zonder userErrors. Alleen relaties met gecontroleerde vendor Lagoo verwijderd. Bestanden blijven beschikbaar voor herstel; variantafbeeldingen worden door dezelfde Shopify-operatie leeggemaakt.

Volledige eindcontrole: **232/232 producten, nul media** en geen volgende pagina. Titels, handles, vendor, status en descriptionHtml gelijk aan de nulmeting. MAIN **196116087050** ongewijzigd; geen themefilewrite/publicatie. Openbare Garda-productpagina zonder preview: nul product-`img` in main en visueel geen productfoto. Native zoekmarkup bevat Lagoo-kaarten zonder foto's; de latere externe zoeklaag toont vier Wiesbaden Lagos-producten met hun eigen foto's. Deze afzonderlijke zoekafwijking is niet aangepast. Geen Windows-, fysieke telefoon-, cart- of checkouttest.

**Nieuwe foto-instructie gaat vóór eerdere foto-uitrol:** Lagoo blijft zonder productfoto's. Niet automatisch opnieuw importeren/herkoppelen of de oude foto-uitrol hervatten. LVS1/2/3 en overige eerdere grenzen behouden. [Bewijs en herstel](lagoo/2026-11-04/no-product-images/README.md).

**Exact één volgende handeling voor Lagoo:** wacht op een nieuwe expliciete eigenaaropdracht voordat foto's opnieuw worden gekoppeld. Geen actieve schrijver na overdracht.

## LAGOO-18 — goedgekeurde Lagoo-stijl live bevestigd; offerteactie nog uit · 3 november 2026

Eigenaar keurt LAGOO-17 goed met “Ja dit is goed voeg toe”. Verse Shopify-controle toont dat thema **196116087050 — BadkamerCity - Lagoo foto's en productkeuzes** inmiddels al **MAIN** is; voormalig MAIN196110090506 is UNPUBLISHED. Deze uitvoering heeft niets gepubliceerd en geen Shopify-code/data/instellingen gemuteerd.

Volledige live-inventaris: 1378 bestanden. Alle zeven LAGOO-featurebestanden komen exact overeen met de eerder gecontroleerde code (checkpoint e8939e96d9aebd4f7338f29cba0ff17fd3a3d649). Publieke G1104BN-pagina zonder previewcookie/-parameter HTTP200 met compacte kleurenadapter en 24 echte productbestemmingen. De Hotbath-keuzestijl is dus live; eerdere NOT_PUBLISHED voor het thema is historisch.

**Concrete resterende afwijking offerteknop:** live header-group heeft quote_cta_enabled=false / quote_cta_preview=true. De offerte-Page166573539594 (offerte-vergelijken) is nog isPublished=false en de klant-URL geeft404. Op de live productpagina is de offerteactie daarom afwezig. De alternatieve contact?view-route geeft200 maar bevat live geen Jotform-iframe. Het goedgekeurde rustige ontwerp staat in de code; geen kapotte klantlink geactiveerd en geen claim dat offerte-upload al live werkt.

Bestaande productstatussen, foto's, 400 reviews en LVS-uitstel niet gewijzigd. Volledige Lagoo-catalogusomzetting blijft open volgens LAGOO-16. CONTENT-01 en andere taken hieronder behouden.

**Exact één volgende handeling voor offerteactivatie:** bestaande uploadpagina/koppeling en ontvangst aantoonbaar afronden, daarna de Page en klantactie gericht activeren via de bestaande preview-/publicatiewerkwijze. Geen actieve schrijver na overdracht.

## CONTENT-01 — plus- en aandachtspunten beoordeeld; niets toegepast · 3 november 2026

**READ_ONLY_AUDIT / PROPOSALS_READY / NOT_APPLIED.** Op verzoek van de eigenaar de bestaande punten inhoudelijk beoordeeld. Volledige inventaris11.887ACTIVE producten/48pagina's;148verschillende veldteksten, waarvan67bij273JEE-O-producten.6.318producten hebben minstens één gevuld veld. Twee gecontroleerde JEE-O-lijsten overlappen woordelijk met BadkamerXXL; geen algemene herkomstclaim voor alle producten. Bij48JEE-O-waskommen staat geen overloop zowel bij plus als aandacht.

Privéreview bevat alle148teksten met voorstel, reden en verificatievoorwaarde; standaardJEE-O-filter. Geen verplicht aantal punten; specificaties/setinhoud apart, geen stijl- of veiligheidsclaims verzinnen. Temperatuur, onderhoud, universele passing en ontbrekende eenheden eerst controleren. Sunshower heeft daarnaast een aparte configuratieroute buiten deze veldinventaris.

**PASS:** inventaris/148van148beoordelingen en filterlogica67/148/81/18 plus lege zoekstatus; geen visuele browser-, telefoon- of checkouttest. Geen Shopify-product-/thema-/publicatiemutatie. Verse eindcontrole MAIN196110090506; Lagoo-concept196116087050 UNPUBLISHED. Bestaande Lagoo-code/status behouden. [Scope, broncontrole en overdracht](product-content/PROS_CONS_REVIEW_2026-11-03.md).

**Exact één volgende handeling voor CONTENT-01:** Jackson beoordeelt de JEE-O-termvoorstellen. Daarna pas een kleine fabrikantbevestigde productgroep voorbereiden; geen automatische catalogusbrede vervanging. Geen actieve schrijver na overdracht.

## LAGOO-17 — Hotbath-keuzestijl en subtiele offerteactie in concept · 3 november 2026

Eigenaar accepteert de productnavigatie en vraagt exact de Hotbath-stijl met eigen Lagoo-opties. Bestaand UNPUBLISHED **196116087050** aangepast: dezelfde Hotbath-CSS/JavaScript voor vier ronde kleurbolletjes, geselecteerde kleur altijd zichtbaar, selectierand/vinkje en Bekijk alle 8 kleuren / +4. Eigen Lagoo-kleurnamen en Regular/Medium/High behouden. Bestaande illustratieve afwerkingsassets hergebruikt, aparte illustratieve Tuscany/champagne-SVG's; echte productfoto's blijven ongewijzigd. De grote blauwe offertebalk is nu een rustig icoon met label bij Retour/Verlanglijst/Winkelwagen. Bestemming, instellingen en mobiele verberging blijven behouden; geen nieuwe formulierontvangsttest geclaimd.

Zes conceptfiles bijgewerkt/toegevoegd en exact teruggelezen. Gedeelde Hotbath-CSS/JavaScript en MAIN-header/snippet ongewijzigd. Finale volledige vergelijking: MAIN 1374 bestanden, concept 1378, exact zeven bedoelde verschillen inclusief vorige Lagoo-adapter/main-product-wijziging; geen ontbrekende bestanden. Geen product-/prijs-/foto-/publicatiedatamutaties en geen themapublicatie; LVS blijft later.

**Bewezen:** ThemeCheck 6/6 PASS; bijgewerkte bestaande DOM-test 216/216 wissels, juiste vier zichtbare kleuren met selectie, uitklappen en bestaande kleurassets, Liquid-grensgevallen PASS. Echte Chrome op 1363 CSS-pixels: transparante compacte offerteactie, geen horizontale overloop, 8/8 swatchafbeeldingen geladen. Uitklappen en kleurwissel naar G1104BK (€570), daarna Medium naar G1102BK (€440): echte nieuwe URL, koper behouden, juiste foto/selectie/titel/prijs. **NOT_TESTED:** fysieke telefoon/aparte mobiele viewport, cart/checkout en offerteontvangst. Browserbeelden buiten publieke Git/Library gehouden.

Codecheckpoint **e8939e96d9aebd4f7338f29cba0ff17fd3a3d649** op **fix/product-cards-2026-10-14**, bron **shopify/current/**. [Details en herstel](lagoo/2026-11-03/product-links/README.md). Alleen het bestaande concept aangepast; volledige Lagoo-catalogusomzetting blijft open volgens LAGOO-16.

**Exact één volgende handeling:** eigenaar bekijkt de bijgewerkte stijl in hetzelfde concept, daarna gecontroleerde Lagoo-uitrol voortzetten. Publicatie door eigenaar volgens bestaande werkwijze. Herstel via vorige codecommit voor de zes gewijzigde conceptpaden; nieuwe ongebruikte assets/helper mogen blijven. Geen actieve schrijver na overdracht.

## LAGOO-16 — proef met juiste foto's en echte productlinks klaar; uitrol nog open · 3 november 2026

**LVS1/LVS2/LVS3 nu ongemoeid laten. To-do voor na de fotocorrectie:** zelf samen te stellen sets zoals Hotbath IBS70, met type handdouche en met/zonder glijstang. Andere setkeuzes, technische compatibiliteit, prijzen en productrelaties eerst controleren. De 20 beschikbare LVS-beelden en 4 fotogaten blijven in de privéwerkset. Geen nieuwe LVS-producten/configurator nu.

De huidige Lagoo-import heeft 208 groepen / 1772 SKU-varianten en te brede gezamenlijke galerijen. Eigenaar wil aparte echte product-URL's zoals Hotbath. **Eerste concrete proef:** 24 nieuwe producten voor G1100/G1102/G1104, elk één SKU, één aantoonbaar bijbehorende eigen Lagoo-foto, actuele bestaande prijs/BTW/verzend-/trackingwaarden, artikelgerichte fabrikanttekst en bevestigde eigen PDF's. Status UNLISTED; alleen Webshop gepubliceerd en via directe link bereikbaar/koopbaar, buiten zoeken/collecties/aanbevelingen. Dezelfde SKU's bestaan tijdelijk ook nog in de oude groep. Geen catalogusbrede omzetting claimen: bestaande proefouder exact intact (ACTIVE / 24 varianten / 37 foto's); overige 207 groepen niet gemuteerd.

UNPUBLISHED **196116087050 — BadkamerCity - Lagoo foto's en productkeuzes**, eerst volledig 1374/1374 checksums identiek aan verse MAIN **196110090506**. Nu 1375 conceptbestanden met exact twee bedoelde afwijkingen: main-product.liquid en nieuwe bc-lagoo-choices.liquid onder shopify/current/. De adapter gebruikt de bestaande Hotbath V2-navigatie met expliciete productbestemmingen; kleur/hoogte blijven bij wisselen behouden. Andere merken en gedeelde JavaScript/CSS niet gewijzigd. MAIN na afloop 1374/1374 checksums ongewijzigd, niet gepubliceerd.

**Bewezen:** 24/24 Admin-readbacks op foto, SKU, prijs, opties, publicatie, tekst/PDF's en voorraad-/verzendinstellingen; 216/216 kleur-/hoogtewissels in bestaande echte JavaScript via Happy DOM; Liquid-rendering en grensgevallen PASS; 24/24 conceptpagina's HTTP200 met juiste inline navigatie en exact één juiste fabrikantfoto-ID. ThemeCheck PASS met twee bestaande main-product-waarschuwingen; git diff --check en Python compile PASS. **NOT_TESTED:** echte browser/mobiel/visuele eigenaarreview, cart/checkout, volledige migratie en SEO-/historische URL-afhandeling.

Codecheckpoint **433ee10324a29fa755f9b4aff484ba57eb9a8f9a** op bestaande branch **fix/product-cards-2026-10-14**. [Proefpagina High/nikkel](https://badkamercity.nl/products/lagoo-g1104bn?preview_theme_id=196116087050) · [uitvoering en herstel](lagoo/2026-11-03/product-links/README.md). Volledige catalogus, oorspronkelijke 400 reviews en API-receipts niet publiek opgeslagen; privéfabrikantwerkset bijgewerkt naar versie 7 met fotobewijs en readbacks.

**Exact één volgende handeling:** eigenaar beoordeelt deze 24 uitvoeringen in het concept; daarna de resterende groepen met bewezen foto-/kleurkoppelingen en behoudende ID-/URL-omzetting voorbereiden. Publiceren door eigenaar na controle, volgens de bestaande Git-werkwijze. Herstel: nieuwe proefproducten terug naar DRAFT / uitsluitend hun Webshop-publicatie ontkoppelen; oorspronkelijke groep intact. Geen actieve schrijver na overdracht.

## QC-15 — fotogalerijprobleem vastgesteld; LVS-foto’s voorbereid · 3 november 2026

Eigenaar constateert dat kraangalerijen te veel modellen/kleuren bevatten. Bevestigd: de QC-11-fabrikantgalerijen zijn te breed samengevoegd; bronherkomst/READY en eerdere API-verificaties bewijzen geen juiste klantgalerij per gekozenkleur/model. De208publicaties uitQC-14 blijven uitgevoerd, maar de galerijpresentatie is nog niet hersteld. Geen nieuwe brede fotovervanging uitvoeren. Eerst één model/kleur aantoonbaar correct maken en bestaande gegevens behouden.

G1104 gebruikt publiek een VulpStudio3D/AR-viewer met één3D-model en materiaalpalet ch/bn/mb/tc/bb/bk/gm/pg; kleurbolletjes daar leveren niet automatisch acht losse2D-foto’s. Geen AR in Badkamercity ingebouwd. Advies: eerst correcte2D-variantfoto’s; externe viewerintegratie later afzonderlijk toetsen.

Nieuwe eigenaarsopdracht omvat LVS1/2/3-foto’s.20fabrikantkleurbeelden voorbereid:7LVS1/5LVS2/8LVS3, éénbeeldperkleur;4exacte fabrikantcodekoppelingen en16sterke beeldidentiteiten met eerder door eigenaar geaccepteerde LVS-foto’s metkleurcode (genormaliseerdeRMSEmax0,602/255, duidelijkeafstandtotanderekleuren). Legacybestanden uitsluitend referentie, alle nieuwe beeldURL’s eigen fabrikantkopieën. Extra/niet-gematchte beelden niet alskleurfoto opgenomen. Ontbreekt:LVS1PG,LVS2CH,LVS2TC,LVS2PG; geenanderekleurfallback.

LiveShopify-zoekopdracht vendorLagoo+LVS1*/LVS2*/LVS3* gaf0producten. Alleenfoto’s/CSV/bronbewijzenaangevuld in privéfabrikantwerkset, inclusief20echteJPG’s. Productimportbescherming blijft; geen drie nieuwe producten/prijzen/publicatie, geen themamutatie of QC-reviewwijziging. VolgendeLagoo-stap: G1104-fotokoppeling en zichtbare galerij per uitvoering corrigeren op bewezen bronnen; LVS-productimport eventueel gericht uitvoeren met de vier open fotogaten zichtbaar.

## GIT-SYNC-01 — actuele themabron en JEE-O-publicatie bevestigd · 3 november 2026

Shopify MAIN is inmiddels **196110090506 — BadkamerCity - JEE-O kleurkeuzes**; vorig MAIN196052189450 is UNPUBLISHED. De24JEE-O-codefiles stonden al exact in Git en zijn ongewijzigd live aangetroffen. Eerdere PUBLICATION_BLOCKED-status hieronder is hiermee historisch; deze Git-taak heeft zelf niet gepubliceerd.

Volledige vergelijking: live1374bestanden; oude Git-root507, waarvan451bytegelijk en56afwijkend;867livepaden ontbraken in de root. Daarom een aparte actuele bronkopie **shopify/current/** op bestaande branch **fix/product-cards-2026-10-14**. Geen onzekere root-/deploykoppeling omgezet. Main ontvangt uitsluitend documentatie/manifest.

Alle1374livepaden gelezen:1373inhoudelijk bytegelijk vastgesteld. Acht historische QA/debugbackups niet als actieve code opgenomen: de actuele bronmap bevat1366themafiles, waarvan1365bytegelijk. Enige API-bodyuitzondering config/settings_data.json expliciet vastgelegd en tegen upload beschermd. Retourtemplate hersteld naar exact de Shopify-checksum door uitsluitend de gegenereerde API-header weg te nemen.804JSON/JSONC-bestanden parsebaar; geen credentialpatroon gevonden. Bronmanifest opnieuw gelezen:1374paden/geen wijzigingen tijdens de capture. Geen nieuwe browser-/mobiel-/checkoutvrijgave.

Broncodecheckpoint **d4cc4bcf360d1f91d5a6ab8270a0ad7a188f0434**; Git-readback1366/1366exact aan de gecontroleerde capture.

[Actuele bron, gebruik en herstel](git-sync/2026-11-03/README.md) · [volledige bestandscontrole](git-sync/2026-11-03/live-theme-manifest.json). Catalogus, metafields, menu-inhoud, orders en externe backend blijven afzonderlijke systemen. QC-/Lagoo-status hieronder behouden. Geen actieve Git-schrijver na overdracht.

**Volgende Git-handeling:** bij nieuw themawerk de codebranch met **shopify/current/** als bron openen en de actuele MAIN opnieuw controleren; settings_data pas meenemen nadat de checksumuitzondering onafhankelijk is gesloten.

## QC-14 — Lagoo online op Webshop · 3 november 2026

Op expliciete opdracht de208geïmporteerdeLagoo-productgroepen gepubliceerd op de bewezen OnlineStore/Webshop-publicatie283427864842, geïdentificeerd via apphandle online_store. Eerst éénpilot gepubliceerd en teruggelezen, daarna207groepen in begrensde aliasbatches.208geslaagd/0fouten. Finale onafhankelijke paginering: alle208ACTIVE, publishedOnPublication=true op exactditkanaal en publishedAtingevuld. LVS1/LVS2/LVS3 uitgesloten. Andereverkoopkanalen/marktpublicaties, productdata, thema en reviews niet gewijzigd.

OpenbareNesso-productpagina op badkamercity.nl HTTP200 met juisteproductnaam. Verdere publiekeproductsteekproeven volgen in privéverslag. Geen echtecart/checkout of fysieke telefoon getest. Privépublicatieverslag bevat exactebefore/afterID’s en herstel: uitsluitend ditkanaal ontkoppelen na expliciete opdracht. Bestaande57beeldlozegroepen en eerder gedocumenteerde datagaten blijven kwaliteitswerk; publicatie is geen nieuwe inhoudelijke datavrijgave.

**Volgende Lagoo-stap:** eigenaar bekijkt de gepubliceerdeproducten en vult ontbrekende fabrikantbeelden/technischeinformatie gericht aan. Publicatie afgerond; geen actieve schrijver.

## QC-13 — Lagoo-status ACTIVE · 3 november 2026

Op expliciete opdracht “Zet ze op actief” exact de208eerder geïmporteerdeLagoo-productgroepen vanDRAFTnaarACTIVEgezet. Vijf native statusbatches50/50/50/50/8:208geslaagd/0mislukt. Alle208daarna opnieuw uitShopify gelezen: juisteID/handle/vendor enACTIVE. LVS1/LVS2/LVS3 en andereproducten buiten scope. Alleenproductstatus gewijzigd; geen prijs-,optie-,media-,voorraad-,review- ofthemawijziging. PublishedAtblijftvooralle208null; geenverkoopkanaalpublicatiegeclaimd. [Importscope en herstel](https://github.com/jlamping1997/badkamercity/blob/quality-control/quality-control/LAGOO_IMPORT_EXECUTED_2026-11-03.md). Privéactivatieverslag bevat before/after enexacteID’s. VolgendeLagoo-stap: verkoopkanaalpublicatie en ontbrekendegegevens gericht beoordelen; geen actieve schrijver.

## QC-12 — Lagoo geïmporteerd als concept · 3 november 2026

Op expliciete opdracht208groepen/1772varianten geïmporteerd:202nieuweDRAFT-groepen,6bestaandeproefgroepenopbestaandeIDbijgewerkt. Alle208groepen direct vergeleken en finale vendorinventaris208uniekehandles/alleDRAFT/publishedAtnull.105bestaandevariant-ID’s behouden; prijzen, opties, SKU’s en fotorelaties gecontroleerd.151groepenmetfabrikantfoto’s,57zonder;1764galerijreferenties/1763uniekefabrikantbestandenREADY,612exactevariantfoto’s.156seriewaarden geverifieerd,390PDF-linksnaar eigenopslag. LVS1/2/3 uitgesloten.

Geen publicatie/thema-/voorraadhoeveelheid-/review-/D1-mutatie; MAINvóór/na196052189450. Browser/telefoon/checkout niet getest. Volledige input/before/readbacks/importverslag uitsluitend privé in bijgewerkte fabrikantwerkset; nieuwe producten blijven concept tot gegevens en verkoopprijzen zijn gecontroleerd. [Scope, bewijs en herstel](https://github.com/jlamping1997/badkamercity/blob/quality-control/quality-control/LAGOO_IMPORT_EXECUTED_2026-11-03.md).

**Volgende Lagoo-stap:** eigenaar bekijkt de concepten en vult alleen de ontbrekende fabrikantbeelden/technische gegevens aan vóór gerichte publicatie. Import afgerond; geen actieve Lagoo-schrijver.

## JEEO-03 — 228 kleurkoppelingen en kleurbolletjes LIVE bevestigd · 3 november 2026

**VERIFIED_ADMIN / LIVE_THEME_CONFIRMED / DESKTOP_PREVIEW_TESTED.** Bij deze nieuwe controle is196110090506 MAIN; alle24eerder geleverde JEE-O-codefiles zijn exact gelijk gebleven. Alle65groepen/228producten,456metafields en273behouden titels horen bij de eerder gecontroleerde uitvoering; deze Git-taak heeft geen productdata opnieuw geschreven.

De eerdere29PDP-/29kaartdata-, prijs-/foto-/SKU-/link- en desktopcontroles behouden hun bronmoment. Mobiele interactie/fysieke telefoon en checkout niet als nieuw getest opgevoerd. SWMBAS71/2producten en43producten zonder kleurtegenhanger behouden hun eerdere uitzondering.

Publiceren was tijdens implementatie door de Shopify-koppeling geblokkeerd; het thema is daarna buiten deze uitvoering gepubliceerd. Geen nieuwe publicatie nodig. [Kleurcontract, tests en herstel](product-content/JEEO_COLOURS_2026-11-03.md) · [24featurepaden](product-content/JEEO_COLOURS_THEME_FILES_2026-11-03.json). Voor actuele Git-bron: GIT-SYNC-01 hierboven.

## QC-11 — uitsluitend officiële Lagoo-foto’s in import en proefproducten · 3 november 2026

Op expliciete eigenaarsopdracht fabrikantgalerijen toegestaan in importv5, zonder terugval op Badkamervoorjou. 1.562 van1.772niet-beschermde varianten hebben fabrikantbeelden;210zonder gevonden fabrikantfoto. Productgalerij en vaste variantfoto gescheiden:612exacte artikel-/kleurkoppelingen. Het eerdere getal1.558 telde alleen kandidaatgalerijen; vier exacte varianten zonder kandidaatgalerij komen erbij. LVS1/2/3 ongewijzigd.

Zes bestaande Shopify-DRAFT-proefgroepen aangepast en volledig teruggelezen:168eigen fabrikantfoto’s in vijf galerijen,102oude referenties uit zes galerijen ontkoppeld. RE9012zonder fabrikantfoto nu beeldloos. Alle105variantrelaties gecontroleerd:48exactgekoppeld/57zondervastefoto. Bestanden behouden voor herstel. Geen productcreatie/publicatie of prijs-,titel-,optie-,voorraad- of themamutatie. Verse MAIN196052189450; andere taken hieronder behouden hun status.

Sites-versie14 succeeded, bron dff37cd29558b345be7d1bd9b7411bfbbe3db61e, deployment appgdep_6ae9c6a0f6c481918766f09ec4f3de90. TypeScript/15Lagoo- en10fabrikantcontractgroepen PASS. HostedimportHTTP200:1772/1562metfoto/210leeg/612exact, allebeeldURLs eigen fabrikantbestanden. Authclient/toegangsbeleid identiek. Eerste deployment faalde op oude buildchunks; schone tweede build33.697.516bytes geslaagd. Alleen onbereikbare gegenereerde chunks opgeschoond, brondata behouden. Browser/telefoon niet opnieuw getest.

Privéwerkset bijgewerkt met Shopify-concept-CSV208groepen/1772varianten. OpenbareGit uitsluitend code/dossier; brondata/reviews/herstel privé. [Scope en herstel](https://github.com/jlamping1997/badkamercity/blob/quality-control/quality-control/LAGOO_PHOTO_POLICY_2026-11-03.md). **Volgende Lagoo-stap:** bijgewerkte fabrikantconceptimport gebruiken en alleen ontbrekende beelden/technische gegevens behandelen. Geen automatische volledige publicatie.

## JEEO-02 — titels bevestigd en kleurkoppelingen uitgewerkt · 3 november 2026

Alle273JEE-O-titels/handles opnieuw uit Shopify gelezen: exact gelijk aan JEEO-01. Geen herhaalde productwrite.66mogelijke kleurgroepen/230producten en43zonder kleurtegenhanger voorbereid;8groepen/28producten ook op fabrikantartikelcode bevestigd,57catalogusgevalideerd en1SWMBAS71-HOLDgroep/2producten. Volledige koppellijst privé; geen kleurrelatie geactiveerd.

Huidige MAIN196052189450 read-only onderzocht. Bestaande kleuradapter en bc-card-data begrenzen color_variants tot Wiesbaden; alleen productrefs invullen toont JEE-O nog niet. V2 kan worden hergebruikt. Manifestprecedentie voor kaartkleur bij implementatie expliciet oplossen. [Details en testgrenzen](product-content/JEEO_TITLES_2026-11-03.md).

**Volgende JEE-O-actie:** in een identiek UNPUBLISHED-concept de JEE-O-product- en kaartkoppeling voorbereiden; eerst3groepen van5Slimline-plafondarmen per lengte15/25/35cm testen. Geen theme-write/publicatie of metafieldmutatie in deze controle; geen actieve JEE-O-schrijver. Andere trajecten hieronder behouden hun status.

## JEEO-01 — 273 klantvriendelijke producttitels afgerond · 3 november 2026

Op expliciete eigenaarsopdracht alle273JEE-O-producttitels aangepast naar natuurlijke namen, bijvoorbeeld **JEE-O flow hoge wastafelkraan Geborsteld RVS**. Merk/serie/product/afwerking; geen lange technische omschrijvingen. Maat behouden waar uitvoeringen anders niet herkenbaar zijn. Korte/lange Soho-uitlopen apart; nul dubbele nieuwe titels.

Drie proefproducten + vijf groepen van50 + één van20 vooraf gecontroleerd en exact teruggelezen. Volledige eindinventaris273/273titels exact; nul onverwachte wijzigingen in vergeleken overige velden, waaronder URL/handle, omschrijving, status, opties en varianten met SKU/prijs. Drie oorspronkelijke openbare URL's HTTP200 met juiste nieuweH1. Geen theme-write/publicatie, keuzemenu-, SEO-, metafield- of mediabatch. Voor/na-overzicht en herstelgegevens privé bewaard; geen actieve JEE-O-schrijver. [Scope, bewijs en herstel](product-content/JEEO_TITLES_2026-11-03.md).

**Volgende JEE-O-stap:** keuzemenu's per exacte modelfamilie uitwerken; eerst15Slimline-plafondarmen met lengte15/25/35cm en vijf afwerkingen. Huidige storefrontbron vóór implementatie controleren. Lagoo-QC en de bestaande themareview hieronder behouden hun eigen status.

## QC-10 — officiële Lagoo-bron en klantdocumenten · 3 november2026

Alle199productpagina's en27mediapagina's gelezen;2.629mediarecords tegenover2.679headercount,50verschil expliciet open. Nieuwe werkset met1.823eigen fabrikantfoto's en372PDF-kopieën READY. Geen3D/CAD-bestandsdownload.254PDF-records in actuele paginalinks; overige alleen kandidaat.48pagina's/314bestaande varianten noemen inbouwdelen met originele voorwaarden/alternatieven.616varianten met expliciete artikel-/kleurcode,612niet beschermd voor importfoto's. Andere kleurkoppelingen blijven onzeker; ook fabrikant hergebruikt seriebeelden.

Dezelfde privé-QC gebruikt nieuwe fabrikantfoto-ID's, duidelijke bronlabels en huidige/kandidaat-PDF's;24LVS1/2/3varianten en alle andere merken exact behouden. Oude400beoordelingen blijven historie, geen automatische goedkeuring van nieuwe bestanden. Checkpoints blijven per SKU. Importv4:1772niet-beschermde varianten,612photoImportReady; alle andere importfoto's leeg/hold. Prijzen/opties/EAN's niet uit groepsclaims overschreven. Geen Shopify-productmutatie/publicatie; uitsluitend eigen bestandskopieën. [Scope en herstel](https://github.com/jlamping1997/badkamercity/blob/quality-control/quality-control/LAGOO_OFFICIAL_SOURCE_2026-11-03.md).

Sites-versie12 succeeded; bron627aafcae4508977066e13e68ef7ab8e1341b2c2, deployment appgdep_6ae9b9ea19488191a5816154ba3b1387. Schone build33MiB, originele brondata privé behouden. TypeScript/build/45bestaande API-SQLite-Lagoo-groepen+8nieuwe fabrikantcontractgroepen PASS. Hosted reviewcatalogus1796/1772official/24protected HTTP200; G1100BN juiste eigen fabrikant-URL HTTP200; import1772/612photoReady HTTP200; review zonder visitor401. Authclient/toegangsbeleid gelijk. Browsergoedkeuring faalde door capaciteit, geen browseromweg; fysieke telefoon/visitor-write niet getest. Twee bronbeelden onverwerkbaar;24PDF-kopieën lokaal signature/EOF/SHA gecontroleerd, overige READY maar lokale verificatie door proxy403onvolledig. Volledige data/reviews uitsluitend privé; downloadbare werkset geleverd. Eigenaar herlaadt en behandelt alleen resterende onzekere fabrikantkoppelingen.

## QC-09 — eerste400Lagoo-fotoselecties verwerkt, LVS1/2/3 overgeslagen · 3 november 2026

Checkpoint400 bevestigd: vervolg N8100CH.24LVS1/2/3varianten uitgesloten van galerie, brondata/Shopify daarvoor ongemoeid.400bekeken varianten verwerkt in private importwerkkopie:366met selectie/367beelden,34zonder keuze blijven open. Alle oorspronkelijke kandidaten, specificaties, prijzen, opties en eigen PDF's behouden. Export bevat approvedLagooImport. Geen automatische goedkeuring/afkeur of D1-reset.

Actuele Shopifyinventaris6DRAFT-proefgroepen; binnen eerste400bestaan3groepen/25varianten. Vijf Nesso-variantkoppelingen gecorrigeerd en drie niet-geselecteerde productgalerijreferenties verwijderd; eigen bestanden behouden. Alle25koppelingen en drie galerijen exact teruggelezen; geen nieuwe producten/publicatie. De overige30groepen zijn alleen voorbereid in importdata, niet geïmporteerd. [Scope/rollback/testgrenzen](https://github.com/jlamping1997/badkamercity/blob/quality-control/quality-control/LAGOO_400_APPLIED_2026-11-03.md).

Sites-versie10 succeeded, bron1b7fabbd6840ec8d2c91511fd1b8fc38776eea66, deployment appgdep_6ae9a3a5712c81918b0638ebdd0bb148. TypeScript/build/45API-SQLite-Lagoo-groepen+6selectie-integriteitstests PASS. Authclient/toegangsbeleid gelijk. Browser/telefoon/hosted visitor-write niet getest. Reviews/checkpoints/volledige catalogus/receipt uitsluitend privé. Eigenaar herlaadt de bestaande privétool en vervolgt met N8100CH.

## QC-08 — alleen goede foto's, vaste kleur, checkpoints per20 · 3 november 2026

Galerie toont één selecteerknop per foto, geen fout-/twijfelactie. Deselecteren=unchecked; niet geselecteerd is geen afkeur. Kleur/SKU blijven sticky bovenaan. Foto-oordelen direct opgeslagen; bij20/40/60etc en laatste groep eerst online checkpoint, dan volgende product. Herladen hervat op nextSku van laatste galeriecheckpoint; tussentijdse bevestigde selecties blijven behouden. Zelfde eigenaargebonden API/schema, geen Shopify-write. TypeScript/build/45API-SQLite-Lagoo-groepen PASS. Browser/telefoon/hosted visitor-write niet getest. Versie9 succeeded, bron c5a4ee8dea2043da36db698505cb19bfc06893a2, deployment appgdep_6ae98d0bef948191831ff2ad92f3b432. Authclient/toegangsbeleid identiek. [Dossier](https://github.com/jlamping1997/badkamercity/blob/quality-control/quality-control/LAGOO_SELECTION_2026-11-03.md). Eigenaar herlaadt en controleert selectie/hervatten na20producten.

## QC-07 — Lagoo-galerie per SKU · 3 november 2026

Dezelfde privétool toont producttitel, kleur en alle kandidaatfoto’s; per foto Goed/Niet goed/Twijfel. Meerdere goede foto’s per variant, productwissel handmatig. Individuele foto-oordelen via bestaande D1-review-API, geen automatische hoofdfotokeuze/Shopify-write. TypeScript/build en44API/SQLite/Lagoo-contractgroepen PASS, inclusief twee onafhankelijke oordelen binnen één SKU. Browser/telefoon niet getest. Sites-bron71e835d774cdca06467f685e9286ed0fc0c8feb8, deployment appgdep_6ae98b7954fc8191b5ce72dfe703f0a0 succeeded. [Werkwijze](https://github.com/jlamping1997/badkamercity/blob/quality-control/quality-control/LAGOO_GALLERY_2026-11-03.md). Eigenaar herlaadt privétool en beoordeelt foto’s per kleurvariant. Bij herladen start galerie op eerste product; bevestigde oordelen blijven zichtbaar.

## QC-06 — Lagoo: directe kleurcontrole · 2 november 2026

Dezelfde privétool opent nu standaard alleen Lagoo: kleur uit titel groot boven één foto, Ja/Nee/Twijfel en automatisch volgende SKU na bevestigde opslag. Andere foto wisselt kandidaat direct. Geen ronde-start of algemene merk-/PDF-menu's in de eenvoudige weergave; Uitgebreid behoudt de bestaande QC en voortgang. [Actuele werkwijze op quality-control](https://github.com/jlamping1997/badkamercity/blob/quality-control/quality-control/LAGOO_FAST_REVIEW_2026-11-02.md).

Sites-versie7 succeeded; broncommit e21a5308e2d4867fc702a0bd73d13b8ec7de6177, deployment appgdep_6ae897e9677c81918bd7fe9efee75b7f. TypeScript/build,43bestaande API/SQLite/Lagoo-groepen en6gerenderde kleurcontrolecontracten PASS. Hosted Lagoo1796kaarten en SKU-gallery HTTP200; review zonder visitor401. Native begrensde24reviews+1checkpoint identiek vóór/na, authclient/toegangsbeleid gelijk. Geen Shopify-write, catalogus- of databaseschemamutatie. Browser/telefoon/hosted visitor-write niet opnieuw getest; eerdere previewinfrastructuur niet aantoonbaar hersteld. Volgende QC-actie: eigenaar herlaadt privélink en controleert kleur/foto met directe knoppen. Andere storefronttaken hieronder blijven afzonderlijk.

**31 oktober 2026 · NAV-03 / TILE-02 PREVIEW_VERIFIED / OWNER_REVIEW_PENDING.** Compact menu, startwaarde1m² en tegelinformatie staan in het gecontroleerde concept. Geen actieve schrijver na overdracht.

## QC-05 — Lagoo in dezelfde privécontrole · 2 november 2026

Afzonderlijk van het NAV-03-themaconcept: branch `quality-control` bevat nu 211 Lagoo-brongroepen als 1.796 SKU/kleurkaarten in [dezelfde privétool](https://badkamercity-quality.jason015.chatgpt.site), versie6. Per SKU hoofdfoto kiezen/expliciet goedkeuren; Aanleverlijst met ontbrekende PDF, technische documentatie, foto, kenmerken en EAN. 1.229 afbeeldingen en251PDF-bestanden in eigen Shopify Files; PDF-kopieën volledig op SHA256/grootte gecontroleerd. 92groepen zonder directe PDF; koppelsuggesties blijven ongeverifieerd. Geen automatische goedkeuring of fotocorrectie.

Sites-broncommit `5634119673735eb88cce104c51e2b4f8fe7a8d2a`, deployment `appgdep_6ae894b87f3c8191b8f1ce1d6894e20c` succeeded. TypeScript/build/43contractgroepen PASS. Hosted Lagoo1796kaarten en lazySKU-gallery HTTP200; review zonder visitor401. Bounded native24reviewrijen+1checkpoint identiek vóór/na, authclient/toegangsbeleid ongewijzigd. Browser/telefoon/hosted-visitorwrite niet getest in deze taak. Volledige catalogus en reviews blijven privé; publieke Git alleen code en scope.

Vijf bestaande DRAFT-proefomschrijvingen gebruiken nu eigen PDF-links. Geen volledige import/publicatie van overige205groepen. Volgende QC-actie: eigenaar kiest Lagoo en controleert foto's en ontbrekende gegevens per SKU. [QC-dossier op quality-control](https://github.com/jlamping1997/badkamercity/blob/quality-control/quality-control/LAGOO_QC_2026-11-02.md). NAV-03-status en vervolghandeling hieronder blijven van kracht voor het storefrontthema.

## Begin hier: actuele rollen en code

- **MAIN195974824202 — BadkamerCity - Betrouwbaar bestellen en filters.** De eigenaar heeft de herstelde FIX-01 gepubliceerd. Verse eindmeting:1.355bestanden, nul gewijzigde paden tegenover opening van deze taak. Geen MAIN-filewrite of publicatie door deze uitvoering.
- **UNPUBLISHED195947036938 — BadkamerCity - Compact menu en tegelinformatie.** Eerst alle21FIX-01-paden vanuit MAIN overgenomen; vóór nieuwe features1355/1355checksumpariteit. Finaal1.356bestanden, exactzesgewijzigdebestaandepaden +éénnieuweoverflow-snippet. Alle zeven checksums correct teruggelezen. QA-template exact hersteld.
- Repository **jlamping1997/badkamercity**, bestaande branch **fix/product-cards-2026-10-14**. Runtimecheckpoint **b7a5308038965bf874e06ed5115aa9431eb381d3**. Alleen de zeven expliciete featurepaden uploaden; Git-root is geen volledige actuele MAIN-snapshot. Main ontvangt dezelfde overdracht/testdocumentatie, geen themacode.

[Actuele wijziging, bewijs en rollback](navigation-and-tiles/2026-10-31/README.md) · [einddiff](navigation-and-tiles/2026-10-31/final-verification.json).

## Nieuwe werking

| Onderdeel | Gedrag in het concept |
| --- | --- |
| Desktop/laptopcategorieën | Eén rij; werkelijk passende categorieën direct zichtbaar. Rest met volledige sublinks onder Meer categorieën. Geen horizontaal schuiven of tweede rij. |
| Tablet/telefoon | Onder990CSS-px bestaand menu. Brede tablet/laptop kan de passende enkele rij gebruiken; apparaatnaam is geen vaste layoutkeuze. |
| Zonder scripts | Native Alle categorieën-details met bestaande bestemmingen. |
| Tegelcalculator | Verse start1m², 10% snijverlies behouden; opgeslagen expliciete keuzes en handmatige dozen blijven werken. Ongeldige invoer blijft blokkeren. |
| Informatieknop | Native popup naast Bereken je bestelling met vloer-/wanduitleg, Sluiten/Escape/focusterugkeer; NL/EN. |

## Verificatie en grenzen

**Dertien CSS-breedtes 320–1920px:** geen document- of categorierail-overloop; vanaf990px één48pxrij. In de gebruikte fixtures990/1024:7direct+4Meer;1180/1280:9+2;1366enbreder11direct. Deze aantallen zijn meetresultaten, geen vaste limieten. Meer opent binnen viewport, ArrowDown/Escape/focus getest. Tablet820:Menu→Douche→Terug→Escape. Open mobiel menu sluit bij resize naar1366zonderbodylock.

**Tien lokale regressies PASS**, Theme Checkrevisie3 allezevenfiles geldig. Echte tegel-PDP begint1m²/10%;10m²→8dozen/11,44m²;0m² geeft fout/geblokkeerd/geen oud totaal. Native informatiepopup en Escape/focus/body-scroll gecontroleerd. Echte concept-homepage visueel bekeken. Tijdelijke QA-template exact teruggezet.

Dit is Cloud Chrome en componentframes met echte conceptcode, geen fysieke telefoon/tablet/Windows-, touch-hardware-, volledige checkout-, mailbox-, ranking- of performancevrijgave. Geen echte cart-, order- of formulieractie. Settings_data/retourtemplate-bodyuitzonderingen behouden; beide niet geüpload.

## Exact één volgende handeling

**Eigenaar opent bij Webshop→Thema’s het Voorbeeld van BadkamerCity - Compact menu en tegelinformatie, controleert eigen laptop/tablet/telefoon en publiceert daarna zelf.** Geen publicatie door uitvoerder.

## Bestaande reparaties en open taken behouden

FIX-01 is nu LIVE door eigenaarspublicatie: cartbevestiging, Sunshower pending/onzekere add, definitieve native filterterugval, Toon minder, zoektelling, tegelprijseenheden, wishlist-intents en echte footerlinks/SEO. De eerdere lege calculatorstart is door de nieuwe expliciete opdracht vervangen door1m². [Oorspronkelijke FIX-01](repairs/2026-10-31/README.md) · [herstel verwijderd concept](repairs/2026-10-31/recovery/README.md).

- **Retouraanmelding:** bestaande live Page166668894474, handmatige native contactaanvraag. Mailontvangst/spam/antwoord en labellevering nog onbewezen; geen automatisch RMA/label/refund gebouwd. [Publicatie](returns/2026-10-30/PUBLICATION.md).
- **Offerte:** deze taak wijzigt geen activatie of account/verificatie. Het bestaande verificatie-/ontvangst-/opslag-/verwijderbewijs blijft open; geen privéaccountpoging. [Integratie](quote/2026-10-30/INTEGRATION.md).
- **Hygrometer:** eerdere twee redirects naar bestaande /pages/hygro-meter behouden; in deze taak niet opnieuw alle redirects getest.
- **Filters/wishlist:** eerdere grenzen voor omgekeerd bereik/APIbeleid, URLdialecten, responseidentity, facetzoeker, oudere/no-Locks-tabversies, opgeslagen corrupte/dubbele arrays en productread-timeout/TTL blijven open. Niet als nieuwe productie-incidenten opgevoerd.
- **QC-04:** afzonderlijke privétool op quality-control; geen privébeoordelingen gelezen of Shopify-productmutatie uitgevoerd.

[Het naslagwerk](MASTER_SITE_REFERENCE.md) blijft het gedateerde DOC-04-boek met80hoofdstukken. Oude NAV-02-rijen/publicatierollen zijn historisch en vervangen door deze actuele status en NAV-03. De registers behouden hun eigen peildatum. Geen Windows-controle geclaimd.
