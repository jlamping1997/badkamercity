> **8 november 2026 — FILTER-COTTO-COLOR-01 READY_FOR_OWNER_EXECUTION; nog niet live:** 207 visueel beoordeelde Cottoceramix-serie/kleurcombinaties (202 genormaliseerde sleutels) staan klaar. Volledige vergelijking van 3.496 tegels: **353 kleurwijzigingen**, waarvan 315 vanuit Overige kleuren en 38 correcties. Overige bij Cotto daalt 414 → 99; 2.499 van 3.159 krijgen een bruikbare basiskleur, 561 zonder kleurbron blijven ongewijzigd. **50 tests PASS met echte fixtures, geen skips**; overige velden, andere merken, 47 eigenaarregelproducten, 27 Acero-tegels, 132 formaatcodes en volledige API gelijk. Code onder `scripts/filter-sync/simplification/cotto-colors/`; installerhash in manifest. Nieuwe regels zijn visuele afleidingen per exacte serie/bronwaarde, geen algemene titelafleiding of afzonderlijke eigenaarbevestiging. **Eén volgende handeling:** eigenaar voert het vastgepinde Cotto-installatieblok uit en deelt de volledige uitvoer; daarna publieke nacontrole. Echte serverstaging/activering/publieke controle van deze batch zijn nog niet uitgevoerd. Bestaande Acero-release blijft de laatst bewezen liveversie; Cottoceramix-formaatprofiel en overige holds behouden. [Dossier](filters/cotto-colors-2026-11-08/README.md).

> **8 november 2026 — DOC-LIVE-01 / actuele documentatie:** MAIN 196328685834; 119 gepubliceerde Pages, 227 collecties, 364 HTTP-responses en 1.387 live bestanden gecontroleerd. Twee footerrenderers, twee policies met zichtbare HTML-tags, ontbrekend verzendbeleid, onvolledige contactgegevens, het btw-idformaat en 15 Git/live-verschillen blijven open. Homepage-SEO, retourbeleid en tagconfiguratie zijn inmiddels live. [Actueel auditdossier](audits/2026-11-08/README.md), [masterindex](MASTER_SITE_REFERENCE.md). Geen Shopify-, thema- of serverwrite. Het afzonderlijke filtertraject volgt zijn nieuwste centrale checkpoint; eerdere installatieblokken niet herhalen. Oudere rollen en volgende handelingen zijn historische checkpoints.

> **8 november 2026 — FILTER-ACERO-01 APPLIED_VERIFIED / PUBLIC_API_VERIFIED:** eigenaar heeft code `ea0d0cdb5887f9881e83b23baaca0272458bc897` uitgevoerd. **238 GOED, nul FOUT**, 15.897 producten en 227 profielen. Actieve collectie `bc_sync_20261108t154938_a5477c`; alle vier vereiste vlaggen true, inclusief `acero_gray_v1`, met 27 Acero-tegels. Worker- en API-hashes komen overeen met het manifest; API ongewijzigd. Publieke nacontrole vindt precies de 27 verwachte Acero-product-ID's onder Grijs en nul daarvan onder Zilver. Oorspronkelijke Acero-namen blijven in de titels; formaten 60 × 60 / 60 × 120 / 60 × 150 geven 159 / 58 / 92 producten. Back-up `20261108T154937-6ec4e2`; timer volgens eigenaaruitvoer hervat. **Niet opnieuw installeren. Eén volgende handeling:** eigenaar test de vereenvoudigde filters op de live productlijsten en noteert gerichte productcorrecties. Het Cottoceramix-merkprofiel mist nog het tegelformaatfilter en blijft apart vervolgwerk. Overige holds behouden. [Dossier](filters/acero-correction-2026-11-08/README.md).

> **8 november 2026 — FILTER-SIMPLE-02 v2 LIVE / VERIFIED:** eigenaarinstallatie applied_verified opbc_sync_20261108t152018_664bbe,15.897producten/227profielen;237serverchecksPASSincl132formaten. OnafhankelijkAPI159/58/92formats,OF309,60×60ENBeige27;Goud93. EchteChrome1348×936Wastafelkranen615→Goud93→wissen615;Betonlook46→60×60negen→Beigetwee,herladenbehoudtkeuzes. Exactespecsbehouden. **Niet opnieuw installeren.** RestpuntCottoceramix-merkprofielmistformaatfilter; mobiel/reboot/volgendetimerNOT_TESTED. **Volgende handeling:** eigenaarpraktijkreviewmetproductlinksvoorcorrecties. [Bewijs](filters/simplification-release-2026-11-08/README.md). Overigeholdsbehouden.

> **8 november 2026 — FILTER-SIMPLE-02 STAGING_FAILED_SAFE:** eigenaarinstallatie stopte bij één echte APIcontrole: tegels/60 × 60 cm; volledige indexreadback en formaatfacettellingen PASS. Vorige liveversie volgens uitvoer behouden/hersteld, timer hervat; publieke health bevestigt nog de oude collectie bc_sync_20261108t130100_bc1233. Nieuwe filters NIET live. Geen bewezen oorzaak of vrijgave. **Volgende handeling:** [read-only diagnoseblok](filters/simplification-release-2026-11-08/README.md) uitvoeren en uitvoer delen; geen controle versoepelen of oude installer opnieuw laten draaien. Geen nieuw inhoudelijk kleurakkoord nodig.

> **8 november 2026 — FILTER-SIMPLE-02:** eigenaar autoriseert zelfstandige filtervereenvoudiging zonder nieuwe bevestigingen. Serverrelease klaar op 135ada92366349cbc29ea080894a8e0f5e434fad: 18 basiskleuren plus Overige, meerdere kleuren, gepaarde nominale tegelformaten, soort-/materiaal-/plaatsingsaliases; exacte specs en technische maten behouden. 41 release-/API-/workertests +6 kleurtests PASS; 3.496 tegels als fixture, 3.490 geldige formaten/132labels. Geen server-/Shopify-/themawrite; SSH niet bereikbaar vanuit deze omgeving. Geen themapublicatie nodig. **Volgende handeling:** eigenaar voert [het vastgezette installatieblok](filters/simplification-release-2026-11-08/README.md) uit en deelt uitvoer; daarna runtime/UI controleren. Geen nieuw kleurakkoord vragen. Alle overige holds behouden.

> **8 november 2026 — TILE-FILTER-01 bijgewerkt:** eigenaar heeft alle **15 getoonde kleurvoorstellen** expliciet goedgekeurd, inclusief hoofd- en aanvullende kleuren. Geen algemeen akkoord op alle 807 tegelkleurnamen. Privéoverzicht versie 1 vereenvoudigd tot kleine foto met kleur eronder (15 beelden, 545.791 bytes); versie 0 bewaart de volledige voorbereidingssnapshot. Exacte specs/calculators behouden. Geen productie-/index-/themawrite. **Volgende handeling:** bevoegde VPS-bronread uitvoeren voor schema, actieve allowlist, API-planner en syncworker; daarna de begrensde tegelpilot voorbereiden met verse live-pariteit en staging/UNPUBLISHED-tests. [Uitwerking](filters/tile-pilot-2026-11-08/README.md). Overige holds en restartpolicybewijs behouden.

> **8 november 2026 — FILTER-SIMPLE-01:** volledige alleen-lezen filteranalyse227/227profielen,34velden,1.002kleurnamen. Voorstel18basiskleuren met exacte productafwerking behouden;495naamvoorstellen/507open. Bestaande13groepen/36namen worden niet door de livekleurfilter gebruikt. MAIN196328685834; drie filterfiles wijken af van Git, dus vóór pilot verse live-pariteit. Geen productie-/index-/themawrite. **Volgende handeling:**18kleurenvoorstel beoordelen; daarna vier Wastafelkranen-twijfelgevallen classificeren. [Analyse/testgrenzen](filters/simplification-2026-11-08/README.md). Restartbeleid-/timerbewijs blijft apart; overige holds behouden.

> **8 november 2026 — FILTER-RESTORE-01 hersteld/getest:** verified-dienst weer HTTP 200 / ok=true, 227 profielen, generatie 20261107T080100_ca321b. Echte Chrome op MAIN 196328685834: Wastafelkranen 615 → Inbouw 200 → + Chroom 26 → Alles wissen 615. API-/nativecounts 615/615 en 358/358; CORS-preflight 200. Eigenaar toonde de gestopte kandidaatcontainer aan; geen server-/themawrite door uitvoerder. Restartbeleid/timer/reboot nog niet op server bevestigd; eigenaar deelde alleen het herstelcommando. **Volgende handeling:** uitvoer van dat bestaande blok delen; daarna Wastafelkranen als verbeterpilot. [Dossier](filters/recovery-2026-11-08/README.md). Andere overdrachten en holds behouden.

> **8 november 2026 — SEO-HOME-01:** homepageconcept **UNPUBLISHED196328685834 — BadkamerCity - Homepage SEO 8 nov** gecontroleerd. Titel/beschrijving, één H1 en deelafbeelding gereed; MAIN196341825802 behouden1.387/1.387. Zes gecontroleerde featurepaden,14HTTP-responses en desktoppreview; telefoonreview nog nodig. [Dossier](livegang-seo/seo/homepage-2026-11-08/README.md), codecheckpoint b10cb844eedc75817f66054f4d897b19d04f30e0. **Volgende handeling: eigenaar bekijkt laptop/telefoon en publiceert zelf bij akkoord.** Reservekopie196354474250 is niet het reviewdoel; BRAUER-/import-holds blijven apart.

> **8 november 2026 — BESTEL-01 LIVE:** 767 DENY → CONTINUE, 73 voorraadblokkades opgeheven; alle 851 gevolgde varianten beschikbaar, CONTINUE en exact teruggelezen. De 15.070 niet-gevolgde producten waren qua voorraad al onbeperkt bestelbaar. BC_2009 en Cotto RR6001 via echte koopknop naar de winkelwagen getest; eigen proefartikelen opgeruimd. Voorraadstanden, tracking en status behouden; geen DRAFT-, import-, foto-, prijs- of themawrite. Menurelease 196341825802 is nu MAIN en 5/5 files zijn exact gelijk. [Vaste bestelafspraak](orderability/POLICY.md) / [uitvoering](orderability/2026-11-08/README.md). Nieuwe imports mogen geen DENY terugzetten wegens N of nulvoorraad; geen automatische bewaker geïnstalleerd. Eerdere voorraadadviezen zijn hiervoor vervangen door de expliciete eigenaarafspraak. Andere import-holds blijven gelden.

> **7 november 2026 — VERLAVIO-MENU-02:** 481 menuvelden toegepast en exact teruggelezen; 494 fotoreferenties, 30 vervallen keuzes en 15 numerieke lijsten hersteld. Nieuwe UI staat gecontroleerd in **UNPUBLISHED 196341825802 — BadkamerCity - Verlavio keuzemenus 7 nov**; eigenaarpublicatie nog nodig, connector kan niet publiceren. MAIN **196246372618** onveranderd. 19 JS-tests, 5 validatorchecks, drie browserroutes en componentbreedtes 320/390 px gecontroleerd. Vijf productiefiles plus geneutraliseerd, niet door deze taak toegewezen QA-resttemplate; delete werd door connectorbeleid geblokkeerd. Voorraad/verkoopbeleid ongewijzigd, tijdelijke voorraadtekst blijft apart aandachtspunt. [Dossier](fabriecio/2026-11-07/menu-improvements/README.md) / [eindbewijs](fabriecio/2026-11-07/menu-improvements/final-verification.json). Codebranch fix/product-cards-2026-10-14; main alleen docs. Andere merktrajecten hieronder behouden hun eigen afspraken.

> **6 november 2026 - BRAUER-03:** alle Shopify-import, ookDRAFT-pilots, wacht op ontvangst/inventarisatie van alle aangekondigde afbeeldingen/PDF's/bestanden.31offlineproductinhouden met646bronverwijzingen gecontroleerd, titels/tekst/specs/rollen/uitsluitingen gereed ter beoordeling. [Productinhoud/aanlevering](brauer/2026-11-06/PRODUCTINHOUD.md) en [taken](brauer/2026-11-06/TAKEN.md). Geen Shopify-writes. Volgende handeling: offlineinhoud beoordelen en gerichte informatie aanvullen; media afwachten. Volledige bron-/inhoudsexports privé. Eerdere vroege-DRAFT-route is vervangen door deze eigenaarafspraak.

> **6 november 2026 - BRAUER-02:** btw in prijs bevestigd;13.161prijs-/typevoorstellen en31proefartikelen uitgewerkt. taxesIncluded=true;26.322Excelprijzen/469halvecentgevallen gecontroleerd.227collecties/258definities gelezen; Brauer-specs/leveradapter nog previewwerk. Geen Shopify-writes of import/publicatie. [Uitwerking](brauer/2026-11-06/UITWERKING.md), [velden](brauer/2026-11-06/VELDEN_EN_COLLECTIES.md), [taken](brauer/2026-11-06/TAKEN.md). Volgende handeling: officiële productdata/media voor31pilots koppelen; prijskeuze blokkeert niet meer. BRAUER-01 hieronder is het eerdere checkpoint.

> **6 november 2026 - BRAUER-01:** brononderzoek en plan gereed;13.757bronregels,13.161unieke SKU's;372gedeelde SKU's,578veldverschillen/371SKU's. Adviesprijs ex btw;163toekomstige artikelen. Geen Shopify-writes/import/publicatie. [Plan](brauer/2026-11-06/PLAN_VAN_AANPAK.md) en [taken](brauer/2026-11-06/TAKEN.md). Volgende handeling: prijs-/publicatieafspraken voor de proef vastleggen. MAIN bij verse rolmeting196246372618; Cottoceramix-unitvrijgave blijft apart te testen. Ruwe bronnen/exports niet in publieke Git.

> **5 november 2026 — COTTO-03 PUBLISHED_VERIFIED:** 832 nieuwe Cottoceramix-artikelen verwerkt: **824 live, acht DRAFT-bronconflicten**, volledige publicatie-readback nul fouten. Samen met 22 behouden Re-Bel-artikelen **846 actief**. 126 nieuwe kleurmenu-families, 2.705 READY-beelden, 15 originele JPEG-herstelbeelden, 64.900 veld-/groeps-/mediacontroles en 29 tests PASS. Funky en Monaco-R live gecontroleerd; echte Funky-cartproef PASS, eigen regel opgeruimd. MAIN196238639370, geen themawrite. **2.916 bronartikelen nog niet aangemaakt; feed niet ingericht.** Code `fdac6c95fbfbb751c9f18bffe5b35531acb8aca0`. Volgende COTTO-03-handeling: juiste stuks-/m¹-route voorbereiden voor de volgende batch. [Batch en herstel](cottoceramix/2026-11-05/rollout/README.md). Geen actieve COTTO-03-schrijver. Oudere COTTO-publicatieblokken hieronder zijn historie.

> **5 november 2026 — VERLAVIO-SET-01 live:**78 douchesets (Milaan36/Palermo36/Porlezza6) tonen462 bevestigde inbegrepen onderdelen in het bestaande Hotbath-setblok.156 bestaande metafieldwaarden toegevoegd en exact teruggelezen; alle78 live pagina's PASS. MAIN196238639370 ongewijzigd, geen theme-write/publicatie. Twaalf Venetie-sets blijven op bron-HOLD. [Dossier en herstel](fabriecio/2026-11-05/set-components/README.md). COTTO-/LAUNCH-werk hieronder behouden.

> **5 november 2026 — actuele publicatie bevestigd:** de eigenaar heeft **BadkamerCity - Re-Bel tegelkeuze (196238639370)** gepubliceerd; dit is nu MAIN. Voormalig MAIN 196227170570 is UNPUBLISHED. Zoekindex en nieuwe kaartprijsweergave zijn live gecontroleerd; SEARCH-01 is afgerond. De gedateerde COTTO-/SEARCH-publicatieverzoeken hieronder beschrijven eerdere checkpoints en zijn geen resterende actie.

> **5 november 2026 — LAUNCH-02:** [bedrijfsgegevens](livegang-seo/BEDRIJFSGEGEVENS.md), een [eigen30dagenretourconcept](livegang-seo/retouren/RETOURBELEID_CONCEPT.md), [twee-persoonsbestel-/mailchecks](livegang-seo/CONTROLES.md) en het [hergebruikplan voor één footer](livegang-seo/FOOTER_EN_BELEID.md) zijn voorbereid. Btw-idformaat/telefoon/retouradres en grote-retourkosten nog aanvullen; geen algemene “speciaal besteld”-uitsluiting. Geen winkelmutaties of publicatie; MAIN is bij laatste read196238639370. [Taken](livegang-seo/TAKEN.md) en centrale status bewaren het vervolg. COTTO/SEARCH blijven intact.

> **5 november 2026 — COTTO-02 ADMIN_APPLIED / PREVIEW_VERIFIED:** alle 22 Re-Bel-artikelen nu Cottoceramix als merk en titelvoorvoegsel; prijzen/identiteiten behouden. Vier echte vierkante tegelfoto's met gekozen kleur altijd zichtbaar en uitklappen naar elf. Browser- en 320/390px-componentcontrole PASS; fysieke mobiel/checkout niet opnieuw getest. MAIN196227170570 behouden 1381/1381; bestaand UNPUBLISHED196238639370 bevat dit menu, eerdere cartfixes én laatste parallelle SEARCH-01-code. Codecheckpoint `cb55eb45f1e32f9044a3b91279e0c41aa1b7c410`. **Volgende handeling voor COTTO-02: eigenaar beoordeelt/publiceert BadkamerCity - Re-Bel tegelkeuze**, daarna verse MAIN/publieke kleuren controleren. Geen actieve COTTO-02-schrijver. [Contract, bewijs en herstel](cottoceramix/2026-11-05/rebel/brand-colors.md). Oudere COTTO-01-merk-/menustatus hieronder is geschiedenis.

> **5 november 2026 — COTTO-01 PRODUCTS_LIVE / CART_PREVIEW_VERIFIED:** Re-Bel: 22 artikelen live, 11 kleuren × twee maten, gedeeld keuzemenu en bewezen m²-/doosprijzen. Echte live en previewcart PASS; eigen testregels verwijderd. MAIN196227170570 behouden1381/1381. UNPUBLISHED196238639370 — **BadkamerCity - Re-Bel tegelkeuze** bevat vier winkelwagencorrecties plus de bewezen zoekbescherming uit SEARCH-01 na bewezen volledige kopie. **Volgende handeling: eigenaar beoordeelt/publiceert dit concept**, daarna actuele MAIN en cartlabels teruglezen. Geen actieve schrijver; geen automatische Cottoceramix-feedverversing. Oudere FAB-04-publicatiestatussen hieronder zijn historische overdrachten. [Uitvoering en herstel](cottoceramix/2026-11-05/rebel/README.md).

> **5 november 2026 — SEARCH-01 OWNER_PUBLISHED / INDEX_LIVE_VERIFIED / UI_LIVE_VERIFIED:** MAIN **196238639370** gepubliceerd door eigenaar, drie prijsbestanden live checksum-exact. Index12.760/226profielen, Verlavio851; live Chrome Verlavio851/24externe kaarten en N8271TC één Nesso-kaart met **“Vanaf € 78,00”**, zonder foutbanner. **Afgerond; geen server- of publicatieactie nodig, installer niet herhalen.** Uurlijkse timer hervat; volgende toekomstige uitvoering nog niet waargenomen. [Eindbewijs](search-index/2026-11-05/README.md). COTTO-historie behouden; geen nieuwe automatisering of leveranciersfeedclaim.

> **5 november 2026 — FAB-04 historisch checkpoint vóór eigenaarspublicatie:** Nederlandse Market-verzending gericht hersteld; bestaande tarieven en andere Markets behouden. Alle 861 artikelen teruggelezen, exact 29 echte voorraadaantallen met CAS bijgewerkt, lege aantallen niet verzonnen; zes conflicten op aanvraag. Echte Chrome-winkelwagenproef PASS, eigen testregel verwijderd. **Voorraadtekst wacht op eigenaarspublicatie van BadkamerCity - Verlavio voorraad en levertijd (196227170570)**; MAIN 196116087050 ongeschreven, concept exact drie bestanden gewijzigd na 1.381/1.381-pariteit. De 1–2 werkdagen is winkelbeleid voor bevestigde voorraad en komt niet uit een CSV-levertijdveld. [Uitvoering, herstel en bewijsgrenzen](fabriecio/2026-11-05/stock/README.md). Geen actieve FAB-04-schrijver of feedworker; aparte actuele werkprioriteit in de centrale status behouden. Oudere FAB-03/FAB-02/FAB-01-blokken zijn gedateerde checkpoints.

> **5 november 2026 — FAB-03 historisch rebrandcheckpoint, APPLIED_VERIFIED:** eigenaar heeft **BadkamerCity - Verlavio merknaam** gepubliceerd; actuele MAIN **196116087050**, drie compatibiliteitsbestanden checksum-exact. Alle **861 producten**, **665 menutitels** en **1.665 altwaarden** omgezet en volledig teruggelezen: nul afwijkingen. Drie publieke productpagina's tonen Verlavio en intacte menu's. Prijzen, voorraad, SKU's, URL's, status, mediareferenties en levering behouden; interne Fabriecio-bronkoppeling blijft. Uitverkocht-probleem en 53 bronuitzonderingen open; feedautomatisering uitgesteld. Volgende handeling: bestaande koopbaarheidsafwijking gericht onderzoeken. [Uitvoering, herstel en testgrenzen](fabriecio/2026-11-05/verlavio/README.md). Geen actieve schrijver. Oudere FAB-01/FAB-02-blokken hieronder zijn geschiedenis.

> **5 november 2026 — FAB-02 historisch checkpoint:** Verlavio-compatibel concept **196116087050 — BadkamerCity - Verlavio merknaam** gereed. Huidige MAIN196227170570 ongewijzigd. Nog861Fabriecio/0Verlavio; eerst eigenaarspublicatie, daarna merk/titels/menu-/afbeeldingsteksten omzetten. [Hervatten](fabriecio/2026-11-05/verlavio/README.md). Geen actieve schrijver.

> **5 november 2026 — FAB-01 historisch checkpoint:** 665 Fabriecio-keuzemenu's en leverinformatie voor 851 actieve artikelen opgeslagen/teruggelezen. Concept **196227170570**, MAIN **196116087050** ongewijzigd; codecheckpoint **ab312b8f3685de23fb34166c307d680d284869e4**. Malmö in echte Chrome en 320/390-pixelcomponenten gecontroleerd. 53 bronafwijkingen en publieke Uitverkocht-blokkade open; geen publicatie of feedautomatisering. [Uitvoering en eigenaarreview](fabriecio/2026-11-05/product-choices/README.md). Geen actieve schrijver na overdracht.

> **5 november 2026 — LAUNCH-01:** voor winkelgereedheid, Google, Search Console, Merchant Center, metingen en SEO-groei begin bij [Livegang & SEO](livegang-seo/README.md) en de [takenlijst](livegang-seo/TAKEN.md). Nulmeting en documentatiestructuur zijn voorbereid; Google-inrichting en ontbrekende winkelinformatie nog niet uitgevoerd. De eerdere Lagoo-foto-instructie blijft gelden. Zie de centrale status voor exact één volgende handeling.

> **3 november 2026 — GIT-SYNC-01 / JEE-O LIVE:** actuele MAIN196110090506; alle24JEE-O-featurepaden komen overeen met Git en de nieuwe bronkopie `shopify/current/` op `fix/product-cards-2026-10-14`. Legacy root:507files/451gelijk/56afwijkend/867ontbrekend. Bronkopie:1366actuelethemafiles; acht oude QA/debugbackups alleen in manifest/historie. Eén expliciete API-bodyuitzondering: config/settings_data.json; beschermd door .shopifyignore. [Actuele broncontrole](git-sync/2026-11-03/README.md) en [centrale status](LIVE_STATUS_AND_NEXT_STEPS.md) gaan vóór oudere rollen/bronpaden hieronder. Geen Shopify-write of publicatie in deze Git-taak.

> **31 oktober 2026 — NAV-03 / TILE-02 reviewgereed:** eigenaar publiceerde FIX-01 als MAIN195974824202. Nieuw reviewconcept **UNPUBLISHED195947036938 — BadkamerCity - Compact menu en tegelinformatie** bevat exact7bedoeldefeaturepaden na1355/1355basispariteit. Eén passende categorierij met Meer, calculatorstart1m²/10% en native informatiepopup. 13breedteframes, menu/Escape/resize en echte tegel-PDP gecontroleerd;10lokaleregressies enThemeCheckPASS. Codecheckpoint b7a5308038965bf874e06ed5115aa9431eb381d3. QAhersteld,MAINongewijzigd,geenactieveschrijver. [Actuele status](LIVE_STATUS_AND_NEXT_STEPS.md) · [bewijs/rollback](navigation-and-tiles/2026-10-31/README.md). Oudere rollen en calculatorcontracten hieronder zijn geschiedenis.

> **31 oktober 2026 — FIX-01 concept hersteld:** oud concept195948839178 verwijderd door eigenaar; nieuw **UNPUBLISHED195974824202 — BadkamerCity - Betrouwbaar bestellen en filters** volledig opgebouwd vanuit MAIN195947036938. Voor writes1354/1354manifestpariteit; daarna exact21bedoelde featurepaden en alle21readbackchecksums correct. 126herhaalde checks, geen nieuw gereproduceerd defect; eerdere browser-/ThemeCheckbevindingen behouden hun datum. MAIN ongewijzigd; geen publicatie. Geen actieve schrijver. [Actuele status](LIVE_STATUS_AND_NEXT_STEPS.md) · [herstelbewijs](repairs/2026-10-31/recovery/README.md). Oudere concept-ID's hieronder zijn geschiedenis.

> **31 oktober 2026 — FIX-01 reviewgereed:** MAIN195947036938 ongewijzigd; UNPUBLISHED195948839178 “Betrouwbaar bestellen en filters” bevat exact21bedoelde featurepaden. 126lokale gevallen/checks, Theme Check en begrensde echte browsercontrole. Cart/Sunshower/filter/wishlist/tegel-/presentatiecontracten hersteld; Hygrometerredirects live200. QA-template exact hersteld. Geen actieve schrijver; eigenaarreview/publicatie en retourmailboxbewijs open, offerteactivatie uit. [Status](LIVE_STATUS_AND_NEXT_STEPS.md) · [herstel en testgrenzen](repairs/2026-10-31/README.md). Oudere rollen hieronder zijn gedateerde geschiedenis.

> **31 oktober 2026 — DOC-04 naslagwerk versie 2.0:** 80 hoofdstukken, 32 nieuwe praktische verdiepingen, 50 taken met takenzoeker, 40 diagnosepaden en 50 acceptatiescenario’s. Verse MAIN 195948839178; NAV-02-concept 195947036938 nog UNPUBLISHED; retourpagina live, mailboxbewijs open. 409 bronrecords/407 bytegelijk/twee expliciete uitzonderingen, 18 GETs en offline HTML-controle PASS. Geen winkelwrite of publicatie. [Naslagwerk](MASTER_SITE_REFERENCE.md) · [status](LIVE_STATUS_AND_NEXT_STEPS.md) · [bewijs](site-reference/2026-10-31/README.md). Oudere standen hieronder zijn gedateerde geschiedenis.

> **31 oktober2026 — NAV-02 preview gecontroleerd:** alle11categorieën zonder horizontaal schuiven; twee rijen op smalle desktop/laptop, één rij op breed scherm. UNPUBLISHED195947036938 heet nu Categorieen zonder schuiven;1354/1354pariteit vóór wijziging en finaalexactéénheaderpad. MAIN195948839178behouden. Twaalf breedtes, menu/focus/resize en Merken-doorklik gecontroleerd; QAhersteld. Eigenaar beoordeelt/publiceert. [Status](LIVE_STATUS_AND_NEXT_STEPS.md) · [dossier](laptop-navigation/2026-10-31/README.md).

> **30 oktober2026 — RET-03 live hersteld:** eigenaar publiceerde MAIN195948839178; de retour-Page was nog verborgen. Alleen Page166668894474 zichtbaar gemaakt. Live knop naast Verlanglijst en echte retourpagina zonder preview gecontroleerd. Geen themefilewrite of themapublicatie door uitvoerder; mailboxproef open. [Status](LIVE_STATUS_AND_NEXT_STEPS.md) · [vrijgave](returns/2026-10-30/PUBLICATION.md). Oudere standen hieronder zijn geschiedenis.

> **30 oktober2026 — RET-02 preview gecontroleerd:** retourknop op desktop direct naast Verlanglijst in UNPUBLISHED195948839178. MAIN195947036938 behouden1354/1354; concept exactéénheaderpadgewijzigd. Echte klik→formulier; zeven breedteframes zonderoverloop, QA-templatehersteld. Retour-Page nogverborgen; eigenaarstest en vrijgave open. [Status](LIVE_STATUS_AND_NEXT_STEPS.md) · [dossier](returns/2026-10-30/HEADER.md). Oudere themarollen hieronder zijn geschiedenis.

> **30 oktober2026 — RET-01 preview gecontroleerd:** native retouraanmelding en footer zonder Zichtenburglaan150 in UNPUBLISHED195947036938. MAIN195932061962 behouden1351/1351; concept1354/exact8featurepaden. Page166668894474verborgen. Eigenaar test mailboxontvangst vóór Page/themavrijgave. [Status](LIVE_STATUS_AND_NEXT_STEPS.md) · [dossier](returns/2026-10-30/README.md). HDR-01 is inmiddels door eigenaar gepubliceerd; oudere rollen zijn geschiedenis.

> **30 oktober 2026 — HDR-01 reviewgereed:** vaste mobiele bovenrij/logopositie, inklappende zoekrij en pointerfocus zonder grijs Terug-kader in UNPUBLISHED195932061962. MAIN195915448586 behouden. [Actuele status](LIVE_STATUS_AND_NEXT_STEPS.md) · [ontwerp/test/herstel](mobile-header/2026-10-30/README.md). Eigenaar-iPhone/publicatie open; oudere vervolgstappen zijn geschiedenis.

> **30 oktober 2026 — nieuwe volledige ingang:** lees [het naslagwerk](MASTER_SITE_REFERENCE.md) en [de actuele status](LIVE_STATUS_AND_NEXT_STEPS.md). Verse MAIN195915448586, Offerteconcept195916628234UNPUBLISHED. De oudere opleverrollen hieronder blijven geschiedenis.

> **30 oktober2026 — reclame in offerteformulier verborgen:** alleen de aparte Jotform-reclamecontainer via CSS; publieke formulierread na herladen en Phone-preview zonder balk, verplichte-veldenfouten zichtbaar. Geen nieuwe inzending, geen Shopify-write/publicatie. Verse rollen: MAIN195916628234;195915448586UNPUBLISHED. Uploadactivatie blijft uit; eigenaar controleert verificatie-/testmail. Zie [bewijs en herstel](quote/2026-10-30/BRANDING.md).

> **30 oktober2026 — eenvoudiger offertedesign:** één gecentreerde uploadkaart, minder tekst, compacte Jotform-velden en uitklapbare garantie-uitleg. UNPUBLISHED195916628234; MAIN195915448586 behouden. Vier ThemeCheck-files en17rendercases PASS;320/390component geen overflow. Alleen presentatie gewijzigd; klantactivatie uit. Volgende handeling: eigenaar controleert verificatie-/testmail. Zie [ontwerp](quote/2026-10-30/DESIGN.md) en [status](LIVE_STATUS_AND_NEXT_STEPS.md).

> **30 oktober2026 — Jotform-koppeling:** formulier263018521531044 aangemaakt, echte fictieve testupload/opslag/bevoegde download PASS; in UNPUBLISHED195916628234 gekoppeld met aparte previewgate. MAIN195915448586 behouden. Eigenaar controleert verificatie-/testmail; klantmail en publieke activatie uit. Zie [status](LIVE_STATUS_AND_NEXT_STEPS.md) en [integratie](quote/2026-10-30/INTEGRATION.md).

> **30 oktober2026 — offertefooter:** link onder Klantenservice in beide footers, klantactivatie uit; geen mobiele headerbalk. MAIN195915448586; reviewconcept195916628234. Zie [actuele status](LIVE_STATUS_AND_NEXT_STEPS.md) en [footerbewijs](quote/2026-10-30/FOOTER.md). Uploadaccount nog nodig.

> **30 oktober2026 — correctie offerteheader:** geen mobiele offertebalk; desktop behouden. Actuele MAIN195916628234; reviewconcept195915448586 — Offerteknop alleen desktop. Upload nog uit. Zie [actuele status](LIVE_STATUS_AND_NEXT_STEPS.md) en [besluit/plaatsingsadvies](quote/2026-10-30/HEADER.md). Oudere rollen hieronder zijn geschiedenis.

> **30 oktober2026 — BC-QUOTE-001:** offertepagina-ontwerp en providerkoppeling voorbereid in UNPUBLISHED195916628234 — BadkamerCity - Offerte vergelijken. MAIN195915448586 behouden. Pagina166573539594 ongepubliceerd, upload uit, homepageverwijzing disabled. ThemeCheck/14lokaletests en componentpreview PASS; echte ontvangst PRIVACY/ACCOUNT/TEST_PENDING. Volgende handeling: bestaande formulieraccounttoegang bepalen. [Actuele status](LIVE_STATUS_AND_NEXT_STEPS.md) · [dossier](quote/2026-10-30/README.md).

> **30 oktober 2026 — ASSORT-02 REVIEWGEREED:** mobiele uitklaplijst in UNPUBLISHED195915448586 — BadkamerCity - Mobiel assortiment. MAIN195916628234/1.344files behouden. Vijf featurebestanden, ThemeCheck en39lokalecases PASS;320/390/1024componentbrowsercontrole en gewone categorielink PASS. Native telefoonreview/publicatie bij eigenaar. Reserve195917644042 is niet het reviewconcept. Zie [actuele status](LIVE_STATUS_AND_NEXT_STEPS.md) en [dossier](assortment/2026-10-30/README.md).

> **29 oktober 2026 — ASSORT-01 REVIEWGEREED:** compact assortimentoverzicht uitgevoerd in UNPUBLISHED195916628234. MAIN195915448586/1.338files ongewijzigd; concept1.344files met exact tien bedoelde paden. ThemeCheck R8, twintig lokale cases, echte desktoplinks/zoeker en320/390/1024componenttests geslaagd. Native telefoonreview en merchant-publicatie open. Zie [actuele status](LIVE_STATUS_AND_NEXT_STEPS.md) en [dossier](assortment/2026-10-29/README.md).

> **29 oktober 2026 — FLASH-01:** MAIN195913482506 behouden. Concept195915448586 met stabiele startopmaak/icoonmaten is reviewgereed. Gecontroleerde browservergelijking en zoek-/navigatietest geslaagd; iPhone/eigenaarspublicatie open. Zie [actuele werkstatus](LIVE_STATUS_AND_NEXT_STEPS.md).

> **29 oktober 2026 — NAV-01:** homepage inmiddels MAIN195910795530. Menuconcept195913482506 is reviewgereed: inline uitklappers, rechte vervolgrijen en geen accountlinks. Zie [actuele werkstatus](LIVE_STATUS_AND_NEXT_STEPS.md); Shopify-componentbrowsercontrole320/390 geslaagd; native telefoon en eigenaarspublicatie open.

# BadkamerCity — START HIER bij een overdracht

**Vervolg 28 oktober 2026 — UI-01:** eigenaar kiest nu inconsistenties en productfotopijlen. [UI-vergelijking en conceptwerk](ui-consistency/2026-10-28/README.md); volg [actuele status](LIVE_STATUS_AND_NEXT_STEPS.md) voor exact concept-/test-/publicatiepunt. DOC-03E is geparkeerd; checkout buiten scope. Oudere volgende stappen hieronder zijn geschiedenis.

**Vervolg 28 oktober 2026 — DOC-03D:** [wishlistmethodedossiers](architecture/components/micro/README.md), 43 lokale cases, twee begrensde defectreproducties en vijftien verse metadata-/bytecontroles. Geen live fix of echte bezoekersopslag-/cartactie. Checkout buiten scope. Lees [actuele status](LIVE_STATUS_AND_NEXT_STEPS.md); oudere volgende stappen hieronder zijn geschiedenis.

**Vervolg 28 oktober 2026 — DOC-03C:** [filtermethodedossiers](architecture/components/micro/README.md), 41 lokale cases en twee begrensde defectreproducties; geen live fix. Checkout buiten scope. Lees [actuele status](LIVE_STATUS_AND_NEXT_STEPS.md); oudere volgende stappen hieronder zijn geschiedenis.

**Vervolg 28 oktober 2026 — DOC-03B:** [vier methodedossiers](architecture/components/micro/README.md), 39 extra geïsoleerde scenario’s en verse mapping-/contentstructuurcontrole. Checkout op eigenaarsverzoek buiten scope. Lees [actuele status](LIVE_STATUS_AND_NEXT_STEPS.md); oudere volgende stappen hieronder zijn geschiedenis.

**Vervolg 28 oktober 2026 — DOC-02C:** brede winkeldocumentatie met negen aanvullende dossiers en [naslag](architecture/reference/README.md) voor alle templates/secties/settings/snippets/assets. Lees [actuele status](LIVE_STATUS_AND_NEXT_STEPS.md) en [dekking](architecture/COVERAGE.md); 100% is niet vrijgegeven. Oudere volgende stappen hieronder zijn geschiedenis.


**Vervolg 28 oktober 2026 — DOC-03A:** de [microdossiers](architecture/components/micro/README.md) analyseren afzonderlijke functies en overgangsstaten. Vijftien geïsoleerde cases reproduceren twee problemen en bevestigen normale guards; geen echte cartactie of productiecorrectie. Lees de [actuele werkstatus](LIVE_STATUS_AND_NEXT_STEPS.md). Desktopbewijs is beperkt; mobiel en settings-bytepariteit blijven open. Oudere volgende stappen hieronder zijn geschiedenis.


> **Actuele documentatie-ingang — 28 oktober 2026:** lees [architectuur, onderzoeksboom en componentafspraken](architecture/README.md) en de centrale werkstatus. Oudere statusblokken hieronder zijn gedateerde achtergrond. De Git-root is niet gelijk aan de actuele Shopify MAIN; gebruik de bronvergelijking in het nieuwe dossier.

> **Wiesbaden — afgeronde Shopify-uitvoering, 21 oktober 2026: `SHOPIFY_COMPLETE_INDEX_BLOCKED`.** Volg [het vaste plan](product-content/WIESBADEN_EXECUTION_PLAN.md), [de actuele machine-status](product-content/wiesbaden/execution-state.json) en [het uitvoeringsresultaat](product-content/WIESBADEN_EXECUTION_RESULTS_2026-10-21.md). **2.299 prijswijzigingen zijn teruggelezen; 33.6000 en 75.3510 zijn ACTIVE én Online Store-gepubliceerd.** Oorspronkelijke queue: **186 online / 28 zonder positieve prijs / 3 historische safetyblocks**, niet opnieuw geprobeerd.
>
> **COMPLETE en teruggelezen:** verrijking van **2.273 producten / 12.259 metafields / 33.186 feiten / 6.345 filters / 1.368 documentlijsten**, met **0 uitzonderingen**. Zichtbare afwerking van **187 unieke producten: 3 gerichte correcties + 184 eerder lege SEO-records**, met **0 uitzonderingen**. **87 hoofdcategorietoevoegingen** via `productUpdate.collectionsToJoin` aan **5 bevestigde handmatige collecties**, met behoud van alle bestaande lidmaatschappen; **46 gevallen zonder voldoende bron niet gewijzigd**. Shopify normaliseert **14 identieke SEO-titels naar `null`**; effectieve producttitel en exacte SEO-description zijn teruggelezen. **18184 openbare headcheck PASS**.
>
> **Definitieve Admin-tellingen:** **2.451 totaal / 2.451 ACTIVE / 2.451 Online Store-gepubliceerd**, alle precisie **EXACT**; **EUR**, `taxesIncluded=true`, **MAIN 195491168522 ongewijzigd**. 151 bestaande contentreviews en 25 producten zonder bron behouden; volledige galerijen niet bewezen.
>
> **Exact volgende stap:** bestaande SSH-authenticatie voor de externe index beschikbaar maken, daarna synchroniseren en controleren. Indexstatus **BLOCKED_NO_EXISTING_SESSION_AUTH**; geen syncclaim. Er is geen Shopify-schrijver of achtergrondworker actief na afronding. Actieve branch `fix/product-cards-2026-10-14`; `main` alleen documentatie. Herhaal afgeronde Shopify-operaties niet. Oudere vervolgacties hieronder zijn historische checkpoints.

> **Vaste dagstart sinds 15 oktober 2026:** lees eerst de [centrale werkstatus op GitHub main](https://github.com/jlamping1997/badkamercity/blob/main/docs/LIVE_STATUS_AND_NEXT_STEPS.md). Daar staan de actuele taak, werkbranch, Shopify MAIN en volgende handeling. De oudere themarollen en werkvoorbeelden hieronder zijn gedateerde achtergrond. Er is maximaal één actieve uitvoering; een nieuwe chat maakt geen nieuw plan of nieuwe codebranch.

**Laatste geverifieerde bronstand:** 7 oktober 2026. Dit document is het **eerste dat een nieuwe AI, freelancer, ICT'er of interne medewerker leest**. Doel: binnen 15 minuten weten wat live staat; binnen een uur veilig een taak kunnen oppakken; zonder gokken over ontbrekende toegang of data.

## 1. Wat is er werkelijk opgeleverd?

BadkamerCity is een Shopify Online Store 2.0-webshop met een custom Liquid/JSON-thema, meerdere categoriepagina-typen, homepage, productdetailpagina (PDP), product-switcher, handmatige exacte setrelaties, native filters en een optionele externe filterproef. Het **huidige live-thema** op de meetdatum is **BadkamerCity - SEO categoriehub** (`194864677130`) op `fpa9hu-i3.myshopify.com`.

Dit is een **werkende gepubliceerde themacodebasis** en een nauwkeurig gecontroleerde Git-snapshot, **geen verklaring dat webshoplancering, checkout, productdata of filters 100% gereed zijn**. De actuele code en de bekende datagrenzen staan in:

- [AI_HANDOFF_CURRENT.md](AI_HANDOFF_CURRENT.md) — volledige functionele uitleg.
- [THEME_COMPONENT_REFERENCE.md](THEME_COMPONENT_REFERENCE.md) — alle secties, instellingen, blocktypen en gekoppelde bestandsnamen; handig voor nieuwe codewijzigingen.
- [THEME_CODE_MAP_2026-10-07.json](THEME_CODE_MAP_2026-10-07.json) — machineleesbare afhankelijkheidskaart van alle **441** themabestanden.
- [SHOPIFY_ADMIN_STRUCTURE_2026-10-07.json](SHOPIFY_ADMIN_STRUCTURE_2026-10-07.json) — momentopname menu's, 204 collecties, 174 product-metafielddefinities, status-/producttellingen.
- [OPERATIONAL_RUNBOOK.md](OPERATIONAL_RUNBOOK.md) — veilige Windows/Git/Shopify-werkwijzen.
- [TROUBLESHOOTING.md](TROUBLESHOOTING.md) — concrete foutdiagnose en herstelroutes.
- [RELEASE_AND_QA.md](RELEASE_AND_QA.md) — wat getest/afgevinkt moet zijn vóór een publicatie.
- [SYSTEM_OWNERSHIP_AND_GAPS.md](SYSTEM_OWNERSHIP_AND_GAPS.md) — wat **niet** in de repo staat, welke toegang/bron nog nodig is.
- [PRODUCT_METAFIELD_MAPPING_AUDIT.md](PRODUCT_METAFIELD_MAPPING_AUDIT.md) — code-metafieldkoppelingen versus werkelijke definities.
- [HANDOFF_CHANGELOG.md](HANDOFF_CHANGELOG.md) — herkomst, bewijs en grenzen van deze overdrachtsronde.

### Bewijsniveaus

| Label | Betekenis | Voorbeeld |
| --- | --- | --- |
| **VERIFIED_THEME** | Bestand/dependency was werkelijk op live theme aanwezig en is met Git-baseline vergeleken | `sections/bc-meubelhub.liquid` |
| **VERIFIED_ADMIN** | Read-only GraphQL uit Shopify Admin op datum | `templateSuffix=bc-meubelhub` voor collectie Badkamermeubels |
| **USER_APPROVED_UI** | Gebruiker heeft uiterlijk/ervaring expliciet goedgekeurd | Mobiele rijnavigatie Badkamermeubels |
| **IMPLEMENTED_TEST_ONLY** | Code is aanwezig, maar achter schakelaar of pilotscope | Externe filters op `wastafelkranen?bcfilters=1` |
| **DOCUMENTED_NOT_VERIFIED** | Gedrag of afhankelijkheid bestaat volgens documentatie, niet recent end-to-end getest | VPS health, werkelijke checkout, Core Web Vitals |
| **HISTORICAL** | Oude stand; niet als productiestatus toepassen | Masterplan versie 0.26.3 met oude thema-ID's |

Gebruik deze labels bij elke toekomstige statusrapportage. **Een Shopify-template in Git is niet gelijk aan een ingeschakelde Shopify-collectie, en een ACTIVE product is niet automatisch online gepubliceerd.**

## 2. De eerste 15 minuten: controleer de werkelijke omgeving

1. Open de centrale werkstatus op GitHub `main`; gebruik daarna de daar geregistreerde actieve codebranch. Onderstaande bronstand van 7 oktober is historisch.
2. Lees deze pagina, daarna `AI_HANDOFF_CURRENT.md` en `AGENTS.md`.
3. Controleer in Shopify welk thema NU rol `MAIN` heeft; vertrouw nooit blind het ID van 7 oktober.
4. Bepaal op de Windows-computer de **juiste** Git-repository en of lokale wijzigingen bestaan.
5. Identificeer de exacte template/sectie/data-eigenaar voor de taak. Als het om live verkoop gaat: controleer ook producten, checkout en beheertoegang.
6. Gebruik alleen een ongepubliceerd conceptthema voor codewijzigingen; vraag de merchant zelf te publiceren.

**Alleen read-only PowerShell-commando's om te beginnen:**

~~~powershell
# Kies de daadwerkelijk aanwezige map; historisch bestaan meerdere projecten.
cd C:\Projects\badkamercity-shopify-current
git rev-parse --show-toplevel
git remote -v
git branch --show-current
git status --short
git log -1 --oneline
shopify theme list --store fpa9hu-i3.myshopify.com
~~~

Als `git status --short` niet leeg is: **stop**, bekijk de verschillen en bewaar ze eerst. Geen `git reset --hard` of `git clean -fd`. Volg `OPERATIONAL_RUNBOOK.md`.

## 3. Wat gaat waar heen? (snelle taakroutering)

| Vraag/taak | Begin in | Admin/andere bron die óók gecontroleerd moet worden |
| --- | --- | --- |
| Homepage banners of headerhero | `templates/index.json`, `sections/home-hero.liquid` | Theme Editor, Shopify Files/CDN |
| Homepage categorieblokken | `home-category-grid.liquid` en `index.json` | Collections + Theme Editor |
| Mega-/mobiel menu of zoekbalk | `sections/header.liquid`, `snippets/bc-header-cart.liquid` | `main-menu` en Shopify search |
| Footer | `sections/footer.liquid` | Footer-blocks / menu's |
| Badkamermeubels categorie | `collection.bc-meubelhub.json` → `sections/bc-meubelhub.liquid` | Collectie `badkamermeubels`, inclusief drie **Admin-CSS**-patches |
| Andere hoofdcategorie | `collection.category-landing.json` → `sections/main-category-landing.liquid` | `main-menu` / specifieke A-Z-menu's |
| Productlijst, native filters | `collection.json` → `main-collection-product-grid.liquid` | Search & Discovery, echte producten |
| Externe filters | `bc-external-filters.js` + `bc-external-filters.liquid` | **Afzonderlijke VPS/index/API**; proefmodus |
| Productpagina ontwerp | `product.json` → `sections/main-product.liquid` | Product/variant/metafields |
| Productkleuren/keuzemenu's (switcher) | `bc-product-switcher.liquid` + `bc-product-switcher.js` | `custom.switch_group`, `product-switcher-data.json` en doel-URL's |
| Specificaties ontbreken | `bc-product-detail-specs.liquid` | **PRODUCT_METAFIELD_MAPPING_AUDIT.md**, echte Shopify-waarden |
| Setcomponenten of accessoires | `bc-product-set-data.liquid` / `bc-product-accessories-data.liquid` | Exacte compatibiliteit/SKU-verificatie |
| SEO title / description | Shopify collectie/product Admin | Theme canonical/meta, gerenderde HTML |
| Nieuwe categorie/subcategorie | Shopify Collecties + menu, toegewezen template | Publicatiestatus producten, SEO en links |
| Checkout/betalen/verzenden | Shopify Admin | Niet oplosbaar door alleen theme-code |

## 4. Architectuur in één oogopslag

~~~text
Bezoeker
  └─ Shopify Online Store / storefront
       ├─ layout/theme.liquid (header, head, CSS/JS, footer)
       ├─ templates/index.json (homepage)
       ├─ templates/collection.bc-meubelhub.json (speciale Badkamermeubels-hub)
       ├─ templates/collection.category-landing.json (categorie-overzicht)
       ├─ templates/collection.json (shoplijst/native filtering)
       ├─ templates/product.json (custom PDP)
       ├─ templates/search.json / cart.json / pages / customers
       └─ Shopify Admin en externe afhankelijke bronnen
           ├─ menu's, collecties, productstatus, SKU's, prijzen, media, metafields
           ├─ Shopify CDN, apps, checkout-instellingen
           └─ filter-VPS/Typesense en import/scraperprojecten (NIET in deze Git-repo)
~~~

Bekijk de **bestandenkaart** als een wijziging meerdere secties raakt. Een goede eerste opdracht is bijvoorbeeld “wijzig alleen de categorie-CTA op Badkamermeubels, op een ongepubliceerd thema, controleer 390px én 1440px”; een slechte opdracht is “vernieuw de hele webshop en zet live”.

## 5. De grootste valkuilen (lees voordat je iets doet)

**A. De mobiele categoriepagina is afhankelijk van Shopify Admin HTML.** In de Badkamermeubels-omschrijving staat na `[SPLIT]` drie keer een afgebakend `<style>`-blok:
`BCM_MOBILE_NAV_V2_START`, `BCM_DESKTOP_CTA_V1_START` en `BCM_HERO_COMPACT_V1_START`. Verwijderen kan het goedgekeurde mobiel/desktop-ontwerp direct breken. Snapshot in `docs/shopify-admin/collection-badkamermeubels-description-2026-10-07.html`.

**B. Er zijn verschillende templates voor verschillende collecties.** 204 collecties: **191 zonder alternate suffix (default), 12 met `category-landing`, 1 `bc-meubelhub`**. Alle collecties aanpassen via `templates/collection.json` zou onbedoeld veel meer beïnvloeden.

**C. Externe filters zijn niet overal actief.** Het frontend-script activeert pas bij `collection.handle == 'wastafelkranen'` én `bcfilters=1`. De VPS is een aparte dienst die nog actief getest moet worden.

**D. Productdata en codevelden zijn niet automatisch gelijk.** Shopify heeft **174 product-metafielddefinities**, maar de statisch gescande code noemt onder andere legacy `custom.*` keys, terwijl vele Admin-definities onder `specs.*` staan. Zie mapping-audit; niet automatisch waarden verzinnen of kopiëren.

**E. Gemakkelijk te missen:** `ACTIVE` ≠ aantoonbaar online verkoopbaar; een collectie bevat een product niet automatisch als publiek zichtbare listing. De GraphQL-snapshot telde **11.053 producten**, waarvan **11.051 ACTIVE, 1 DRAFT, 1 UNLISTED**; dit zijn Admin-statussen, **geen checkout- of publicatietest**.

**F. Git-geschiedenis en Shopify zijn apart.** De huidige `main` was op snapshotdatum een gecontroleerde kopie van live thema-code. Shopify thema-updates, Admin-mutaties en lokale ongetrackte bestanden kunnen later afwijken. Vergelijk altijd opnieuw.

## 6. Wanneer is iemand echt in staat zelfstandig door te werken?

**Code-taken:** ja, zodra GitHub/Shopify-accounttoegang, lokale Git/Shopify CLI en preview veilig werken. Alle code- en schema-verwijzingen staan in dit dossier.

**Productsynchronisatie/imports:** alleen na toegang tot bronbestanden, actuele importtools, Shopify-apprechten, datacontract, SKU-regels en importlog. Die zitten NIET allemaal in dit repo.

**VPS/externe filters:** alleen na toegang tot backend-repo/server/secretmanager, service health, indexstatus, deploymentworkflow en testplan. Het frontendbestand is niet de server.

**Complete webshoplancering:** pas na betaling/verzending/BTW, productdata, beschikbaarheid, privacy/legal, SEO en end-to-end orders te hebben gecontroleerd. Theme-snapshot is geen vrijgaveverklaring.

## 7. Concrete eerste dag voor opvolger

**0–15 min:** identiteit/thema/branch/documenten controleren.

**15–35 min:** naar functie die gewijzigd moet worden navigeren via taakroutering en componentreferentie; relevante Shopify Admin-resources read-only openen.

**35–60 min:** projectveiligheid controleren, werkzaamheden splitsen in kleine features, draft thema/backup klaarzetten, één minimaal reproduceerbare preview/test uitvoeren.

**Daarna:** alleen de expliciet goedgekeurde taak realiseren, screenshots/logs bewaren, correcte Git-commit, gebruiker laten beoordelen/publiceren en documentatie bijwerken.

Als een vraag niet met de beschikbare bronnen te beantwoorden is, gebruik **ONBEKEND/NOG TE VERIFIËREN** in plaats van een aanname.

## 8. Verantwoordelijkheid en veiligheid

Deze repository staat op GitHub en is **publiek**. Commit geen tokens, wachtwoorden, .env, privé-adressen, klant-/order-/betalingsgegevens, serverprivésleutels of gekopieerde complete leverancierscontracten. Leg *waar* een bevoegde beheerder veilige toegang aanvraagt vast, maar **niet de sleutel zelf**. Lees `SYSTEM_OWNERSHIP_AND_GAPS.md`.

**Korte instructie voor AI:** “Lees `docs/HANDOVER_START_HERE.md`, `AI_HANDOFF_CURRENT.md` en `AGENTS.md`; vergelijk actuele Shopify MAIN met Git; gebruik de codekaart en Admin-snapshot; maak in ongepubliceerde preview één gerichte wijziging en test zonder bestaande functionaliteit te slopen.”
