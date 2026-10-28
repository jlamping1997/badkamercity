# BadkamerCity — actuele technische AI-handoff

**Vervolgmeting 28 oktober 2026 — DOC-02A:** de [componentdossiers](architecture/components/README.md) en [routematrix](architecture/ROUTE_RENDERER_MATRIX.md) verdiepen nu de bron-/data-/interactiecontracten. Lees eerst de [actuele werkstatus](LIVE_STATUS_AND_NEXT_STEPS.md). De private productexport blijft apart; settings-bytepariteit is OPEN en browserinteracties zijn nog niet als nieuw bewijs getest. Oudere volgende stappen hieronder zijn geschiedenis.


> **Actuele documentatie-ingang — 28 oktober 2026:** lees [architectuur, onderzoeksboom en componentafspraken](architecture/README.md) en de centrale werkstatus. Oudere statusblokken hieronder zijn gedateerde achtergrond. De Git-root is niet gelijk aan de actuele Shopify MAIN; gebruik de bronvergelijking in het nieuwe dossier.

## Code opschoning en gedeelde keuzes — 25 oktober 2026 (PREVIEW_READY / NIET_GEPUBLICEERD)

De eigenaar heeft de eerdere compacte desktopkeuzes gepubliceerd: actuele **MAIN195704848650**. De gevraagde opschoning staat in **UNPUBLISHED195706257674 — BadkamerCity - code opschoning en gedeelde keuzes**. Korte producttitels en bijbehorende filteroptimalisatie blijven op verzoek geparkeerd.

Hotbath en Sunshower delen één begrensde scrollfunctie; Sunshower voorkomt concurrerende hash-scroll bij bewaarde positie. Product-CSS uit het centrale Liquid-bestand gehaald met behoud van instelling/specifiteit. Prijs-/categorieopmaak eenmaal laden. Drie Badkamermeubels-styles naar het thema, zonder wijziging van gedeelde Admin-inhoud. Menudata per productgroep: CB105EXT 227.754→8.424 ongecomprimeerde bytes, met terugval op de originele bron bij een nieuwe revisie of netwerkfout. Geen algemene snelheids-/Lighthouse-scoreclaim.

**Bewijs:** kopie vooraf553/553 identiek; finaal23 bestaande files gewijzigd,4 nieuwe codefiles en656 gegenereerde JSON-data-assets (geen aparte scripts).683 bestanden checksum-exact en27 codefiles inhoudelijk teruggelezen. MAIN553/553 ongewijzigd, QA-template exact hersteld, Admin-description exact gelijk. Shopify-validatie en gerichte regressies slagen; echte desktopkeuzes/totaalbedrag getest, responsive320/390/1024-frames zonder overloop,8 HTTP-paginatypen200. Geen fysieke iPhone, echte winkelwagen/checkout of CrUX/Lighthouse-meting.

**Beperking:**8 niet-verwezen back-upassets behouden: themeFilesDelete is door de Shopify-veiligheidsregel geweigerd vanwege risico voor live storefront. Geen omweg gebruikt. Alle code, brondata, herstelbestanden, screenshots, checksums, onderhoudspipeline en grenzen staan in [het release-dossier](https://github.com/jlamping1997/badkamercity/tree/fix/product-cards-2026-10-14/docs/code-cleanup/2026-10-25). Actieve branch blijft fix/product-cards-2026-10-14; main alleen documentatie. Bestaande lokale dirty bestanden niet aangeraakt; Windows niet gecontroleerd.

**Exact volgende stap:** eigenaar beoordeelt en publiceert het concept **BadkamerCity - code opschoning en gedeelde keuzes** via Shopify → Webshop → Thema's. Daarna MAIN-rol en actieve menudatabron opnieuw controleren. Terugval is het huidige MAIN195704848650. Geen schrijver of achtergrondworker actief na oplevering.

---


## Hotbath compacte keuzes — desktop en mobiel, 25 oktober 2026

PREVIEW_READY: **195704848650 — BadkamerCity - compacte keuzes desktop**; huidige MAIN195704357130 blijft ongewijzigd. [Actueel dossier en bewijs](https://github.com/jlamping1997/badkamercity/blob/c8f76eea2bf8a81ab0f54196e239e0b3930fe20a/docs/product-switcher/2026-10-25/desktop-options/README.md). De eigenaar heeft gevraagd de bestaande mobiele bediening ook op desktop te gebruiken. De eerdere alleen-desktop verplichte Ja/Nee-keuze is voor dezelfde Hotbath-scope vervangen door de compacte checkbox **Inbouwdeel toevoegen** (uit = afbouwdeel alleen; expliciet aan = exact gekoppeld inbouwdeel). Geen betaalde voorselectie. Kleurcirkelmenu, uitklapper, bewaarde kleur-/inbouwkeuze en totaalberekening gelden nu op alle schermbreedtes. Andere merken en volumeproducten behouden hun oorspronkelijke bediening.

Vijf assets: bc-product-switcher.js, bc-product-inbouw.js, bc-hotbath-mobile.js, bc-hotbath-mobile.css en bc-hotbath-swatches.css. De bestaande mobile-namen blijven om bestaande CSS/JS-koppelingen te behouden; actieve scope is nu alle breedtes. Geen nieuwe componentkopie, data-/mapping-/prijswijziging of root-theme-sync. De eerder gepubliceerde scrollfix is behouden.

Vooraf553/553 gelijk; finaal5 gewijzigd/548 gelijk; MAIN553/553 ongewijzigd. Functietests en echte desktopbrowser PASS; iframe320/390/1024 gecontroleerd, tijdelijke QA-template hersteld. Cart-handler met transportstub getest; geen echte winkelwagen/checkout, fysieke iPhone of Windowscontrole. Volgende stap: eigenaar beoordeelt/publiceert dit concept, daarna actuele MAIN opnieuw controleren. Volledige grenzen en rollback staan in het dossier. Oudere desktop-contracten hieronder zijn historisch.

> **Wiesbaden — afgeronde Shopify-uitvoering, 21 oktober 2026: `SHOPIFY_COMPLETE_INDEX_BLOCKED`.** Volg [het vaste plan](product-content/WIESBADEN_EXECUTION_PLAN.md), [de actuele machine-status](product-content/wiesbaden/execution-state.json) en [het uitvoeringsresultaat](product-content/WIESBADEN_EXECUTION_RESULTS_2026-10-21.md). **2.299 prijswijzigingen zijn teruggelezen; 33.6000 en 75.3510 zijn ACTIVE én Online Store-gepubliceerd.** Oorspronkelijke queue: **186 online / 28 zonder positieve prijs / 3 historische safetyblocks**, niet opnieuw geprobeerd.
>
> **COMPLETE en teruggelezen:** verrijking van **2.273 producten / 12.259 metafields / 33.186 feiten / 6.345 filters / 1.368 documentlijsten**, met **0 uitzonderingen**. Zichtbare afwerking van **187 unieke producten: 3 gerichte correcties + 184 eerder lege SEO-records**, met **0 uitzonderingen**. **87 hoofdcategorietoevoegingen** via `productUpdate.collectionsToJoin` aan **5 bevestigde handmatige collecties**, met behoud van alle bestaande lidmaatschappen; **46 gevallen zonder voldoende bron niet gewijzigd**. Shopify normaliseert **14 identieke SEO-titels naar `null`**; effectieve producttitel en exacte SEO-description zijn teruggelezen. **18184 openbare headcheck PASS**.
>
> **Definitieve Admin-tellingen:** **2.451 totaal / 2.451 ACTIVE / 2.451 Online Store-gepubliceerd**, alle precisie **EXACT**; **EUR**, `taxesIncluded=true`, **MAIN 195491168522 ongewijzigd**. 151 bestaande contentreviews en 25 producten zonder bron behouden; volledige galerijen niet bewezen.
>
> **Exact volgende stap:** bestaande SSH-authenticatie voor de externe index beschikbaar maken, daarna synchroniseren en controleren. Indexstatus **BLOCKED_NO_EXISTING_SESSION_AUTH**; geen syncclaim. Er is geen Shopify-schrijver of achtergrondworker actief na afronding. Actieve branch `fix/product-cards-2026-10-14`; `main` alleen documentatie. Herhaal afgeronde Shopify-operaties niet. Oudere vervolgacties hieronder zijn historische checkpoints.

> **WIESBADEN — MAIN195491168522 / BULKONTWERP,20oktober:** eigenaar heeft de proefgroep gepubliceerd en het resultaat algemeen goedgekeurd. Verse Admin-rol plus512/512 checksums gelijk aan eerder geteste preview; vorigeMAIN195488317706 UNPUBLISHED. Geen nieuwe agenttelefoontest of product-/theme-/indexwrite. [Bulkwerkwijze](product-content/WIESBADEN_BULK_WORKFLOW_2026-10-20.md) legt hergebruik van de bestaande bron-/mappingtools en centrale breadcrumbs/specs/bijlagen vast, plus typeprofielen, feitenherkomst, AI-claimcontrole, automatische controle van ieder product en menselijke kalibratie/steekproef/uitzonderingen. De bulkverwerker is NIET gebouwd; er is geen50of2k-bulkproef uitgevoerd. **Volgende implementatiestap:** alleen-lezen50kranenproef op bestaande tools, met expliciete gereed/reviewuitvoer. Voor livebulk eerst Shopify+VPS/indexcontract bewijzen; publicatie lost het oude zoekindexverschil niet automatisch op.25bestaande zonderbronmatch en217nieuwekandidaten blijven aparte stromen, twee bronconflicten open. Eerdere notities “conceptUNPUBLISHED/publiceren” hieronder zijn historische fasebeschrijvingen.


> **WIESBADEN PROEFGROEP2 — ADMIN TOEGEPAST / CONCEPT KLAAR / INDEXSYNC OPEN, 20 oktober:** eigenaar heeft24.3710 mobiel goedgekeurd en doorgaan gevraagd. Zeven producten (20.3755,20.3756,32.3411,32.3594,32.2510,32.3670,38.4125) nu met eigen tekst/titels/SEO,151 specificatieregels en13 documentlinks in Shopify; onafhankelijke volledige readback PASS, prijzen/voorraad/varianten/collecties/media/filtermanifesten behouden. 29.8007 en41.3540 bewust ongewijzigd wegens bronconflicten. MAIN195488317706 behouden511/511; concept **195491168522 — BadkamerCity - Wiesbaden proefgroep 2**, vóór511/511 identiek, na512/drie gewijzigd/één nieuw/508 gelijk. Theme Check4/4SUCCESS, echte preview-HTML7/7, referentie24.3710 behoudt33rijen. Desktop1363×936 Marmaris en zoekkaart gecontroleerd; nieuwe fysieke mobiel en koopacties NOT_TESTED. [Batchdossier](product-content/WIESBADEN_PROEFGROEP_2_2026-10-20.md), [nieuw metadatacontract](product-content/WIESBADEN_REVIEWED_CONTENT_CONTRACT.md).
>
> **Zoekindex is nog oud:** exacte SKU7/7, korte kaarttitel7/7 via bestaande bc-card-data, vier tekstproeven3PASS/1FAIL (“Barco ovale waskom”0). [Zeven-title-only correctie](product-content/wiesbaden/proefgroep2/INDEX_TITLES_RUN.md) met private backup/readback/restore en12 offline veiligheidstests klaar, **niet uitgevoerd op VPS**: SSH-netwerk onbereikbaar. **Volgende handeling:** uitvoeren vanuit bestaande lokale Windows/SSH-sessie en output registreren. Daarna eigenaarconceptreview/publicatie. Laat onbevestigde fonteinmaten, FSC-filterwaarde32.3670 en twee bronconflicten expliciet open. Alleen docs/patch opgeslagen, geen root-theme-push; private Admin-herstelzip is buiten publieke Git bewaard. Onderstaande “mobiele review volgt” voor24.3710 is door gebruikersgoedkeuring ingehaald; eerdere previewthema's niet opnieuw publiceren.


> **PDP LIVE / MOBIELE REVIEW — 20 oktober:** eigenaar heeft concept **195488317706** gepubliceerd; verse Admin-read bevestigt MAIN en openbare HTTP 200-HTML zonder preview bevestigt dit thema, één breadcrumb vóór H1, 33 specificatieregels, beide bijlagen en geen Liquid-fouten. Vorig MAIN 195486253322 is UNPUBLISHED. Geen Shopify-/product-/indexwrite in deze verificatieronde. **Niet heel Wiesbaden afgerond:** volledige productverrijking en nieuw breadcrumb-/bijlagenblok zijn nog pilotscope **24.3710**; publicatie is geen automatische uitrol van brondata naar andere producten. Volgende handeling: eigenaar beoordeelt mobiel vanaf zoeken op24.3710; daarna andere representatieve producttypen in batches. Mobiele visuele/actiecontrole blijft USER_REVIEW_PENDING. [Actuele status](LIVE_STATUS_AND_NEXT_STEPS.md). Onderstaande previewstatus is historisch na deze publicatie.

> **PDP BREADCRUMBS EN BIJLAGEN — PREVIEW READY, 20 oktober:** [centrale status](LIVE_STATUS_AND_NEXT_STEPS.md), [verslag](PDP_BREADCRUMB_DOCUMENTS_2026-10-20.md). Concept **195488317706** blijft UNPUBLISHED, MAIN **195486253322** behouden. Voor **24.3710** staan de breadcrumbs boven H1 en de lijntekening/PDF in een bijlagenblok zoals bij Sunshower; 33 specificaties en de eerdere 750–989 px-correctie behouden. Nieuwste eigenaarinstructie vervangt de eerdere verborgen-documentenkeuze. Alleen de bestaande list.url-metafield aangevuld met de geverifieerde handleiding, compareDigest en readback. Concept 509 → 511, vijf gewijzigd/twee nieuw/504 gelijk; MAIN 508 gelijk. Theme Check zonder errors; negen conditionele cases PASS; normale browser 1363 px en Bijlagen-anchor gecontroleerd. Nieuwe mobiel/smal-proef NOT_TESTED wegens geblokkeerd data-URL-protocol; geen omweg of QA-templatewrite. Patch, backup en beelden onder docs; geen root-theme-push. Volgende handeling: eigenaar bekijkt 24.3710 in dit bestaande concept en publiceert indien akkoord. Onderstaande eerdere previewnotitie is aangevuld.

> **PDP950PX — PREVIEW READY20okt:** [actuele centrale status](LIVE_STATUS_AND_NEXT_STEPS.md) en [verslag](PDP_RESPONSIVE_2026-10-20.md). MAIN195486253322 behouden; concept195488317706 krijgt uitsluitend750–989px CSS-layoutcorrectie. Nulmeting508/508gelijk; finale509: éénCSS+éénneutraleongebruikteQA-redirecttemplate, overige507gelijk. De connector blokkeerde verwijderen van de eigen testtemplate; testinhoud veilig vervangen, geen verwijderomweg. Zesviewporten geïsoleerde actueleShopifymarkup/styles zonderJS: geen overloop/33rijen,950pxfoto893→390pxhoog enkoopblok ernaast. Mobiel320/390 en990pxunchanged. Native1363pxgelezen, geenactietests/echtephone. ThemeCheckSUCCESS. Eigenaarreview/publicatie in Shopify is de volgende handeling; geen productdata of livebestanden gewijzigd.

> **WIESBADEN 24.3710 — SHOPIFY PREVIEW READY, 20 oktober:** [actuele centrale status](LIVE_STATUS_AND_NEXT_STEPS.md) en [nieuwe preview](https://badkamercity.nl/products/wiesbaden-304-wastafelkraan-met-coldstart-geborsteld-rvs-24-3710?preview_theme_id=195486253322). Concept195486253322 van MAIN195449651466; vóór507/507 gelijk, na508 bestanden/4wijzigingen, overige504 gelijk, MAIN507ongewijzigd. ThemeCheck4/4SUCCESS; echte Shopify-HTML33rijen, driecategorielinks; drieandereproducten titel/rijengelijk. Geen nieuwe visuele browser-/mobieltest. Eigenaar heeft filterapply+verify-uitvoer gedeeld: éénkraangatgevonden/tweeuitgesloten; geen SSH door deze ronde. Connector verbiedt MAIN-writes/publicatie; eigenaarreview/publicatie of oorspronkelijke handmatige patch blijft laatste stap. Geen root-themacode pushen naar een onbekende live-integratie.

> **WIESBADEN 24.3710 — FILTERCORRECTIE VOORBEREID, 20 oktober:** eigenaar bevestigt interactieve SSH/sudo/index lezen. Alleen index `bc_verified_full_20261013_874e415c15`, document `10657256210698`; geen herimport of ander product. [Actuele uitvoerinstructie](product-content/wiesbaden/24.3710-filter-correction.md). Gerichte PATCH zet uitsluitend `f_aantal_kraangaten` op1; optioneel int32, API verwerkt numerieke ranges min=max. Script controleert live schema, SKU/collecties, lokale en publieke API; private volledige back-up vóór write, herstel alleen dit veld, volledige readback/conflictcontrole.17 offline tests PASS; serveruitvoering NOT_EXECUTED. Manifesthash is geen voorwaarde voor deze directe correctie; niet verzinnen/wijzigen. Latere volledige bronopbouw moet de waarde meenemen. Verse Shopifyread: vier handmatige collecties inclusief Wastafels, behouden; MAIN195449651466 ongewijzigd. Publieke nulmeting baseline1, bereik1..1=0,2..2=0. Beide post-correctiecriteria wachten op uitvoering; geen live succes claimen. Volgende handeling: eigenaar voert gekoppelde PowerShell-stappen uit en deelt geschoonde JSON; daarna storefrontcontrole. De hieronder genoemde SSH-authenticatieblokkade is historisch. Specificatieweergave blijft afzonderlijk geparkeerd.

> **WIESBADEN 24.3710 — 20 oktober, BLOCKED / oorzaak bewezen:** producttoestemming blijft geldig; geen import herhalen. App heeft read_themes/write_themes, maar connectorinstructie verbiedt MAIN-bestandswrites. Geen Shopify-writefout of approval-rejection ontvangen; geen omweg. MAIN195449651466/elf verse bestanden ongewijzigd. SSH-log `Permission denied (publickey,password).`, exit255: authenticatie faalt na bereikte server; BatchMode vroeg geen wachtwoord, sudo-/Dockerrechten onbekend. Bestaande lokale code importeert vaste11050-documentexport; geen één-SKU-sync/values_sha256-berekening gevonden in33 archieven. Exporthash klopt, manifesthashcontract blijft onbekend. Laatste twee echte browsercontroles: **8/33 specificaties** en **0 resultaten bij één kraangat**, beide BLOCKED. [Concrete vierbestandsinstructie en twee VPS-commando's](product-content/wiesbaden/24.3710.unblock.md); twee gereviewde snippets byte-exact klaargezet en read-only diagnostisch script met vijf offline tests, nog niet op server uitgevoerd. Geen Shopify/indexwrite in deze vervolgronde. Volgende handeling: eigenaar voert gekoppelde Admin-/VPS-stappen uit en meldt veilige uitvoer. Eerdere productwrites/backups blijven in toepassingsrapport; geen ander product of thema publiceren.

> **PUBLICATIE GOEDGEKEURD — 19 oktober, 12:02 CEST:** eigenaar vraagt de getoonde winkelwagen door te voeren. Dit is toestemming voor publicatie van het concrete concept; niet opnieuw om akkoord vragen. Verse read-only controle: MAIN blijft **195388080394**; **195392143626 — BadkamerCity - Winkelwagen helder** blijft UNPUBLISHED, processing=false, 502 bestanden, alle zeven goedgekeurde checksums exact. De Shopify-connector beschrijft themapublicatie expliciet als geblokkeerde handeling. Geen publicatiemutatie geprobeerd en geen alternatieve route gebruikt om die grens te omzeilen. **Laatste stap:** eigenaar publiceert dit bestaande concept in Shopify Admin; daarna MAIN en de storefront opnieuw controleren.

> **WINKELWAGEN HELDER 19 OKTOBER — IMPLEMENTED_PREVIEW:** nieuwe eigenaarsscope is uitsluitend de cart; checkoutvormgeving/betaalflow blijven staan. Verse MAIN **195388080394** (oude cart gepubliceerd), concept **195392143626 — BadkamerCity - Winkelwagen helder**. Vóór feature 501/501 identiek; finale 502 files, zes bestaande/één nieuwe JS, zeven inhouden exact, overige495 gelijk en QA exact hersteld; MAIN501/501 ongewijzigd. Compacte productrijen, echte kortingen, codeformulier buiten cart-items, prijsopbouw altijd onder producten, groene native CTA. Controller ververst vier Dawn-secties, bewaart codes, controleert applicable, beschermt aantal/code-races en herstelt via GET; geen POST-retry. Onzekere codes beloven geen verzendkorting. **Live Admin-regel apart al aangepast: NL €6,95 t/m100; gratis vanaf100,01 na korting; andere zones behouden.** Cart toont bestemmingsschatting. 16 controllergroepen +13beleid/+13render PASS, ThemeCheckR2 SUCCESS. Werkelijke desktopcouponfout/aantallen/verwijderen en verzendoffertes gecontroleerd; testcart leeg. Mobiel alleen statische productiecomponent320/390/430frames, geen fysieke telefoon/volledige header/footer of geldige winkelcode end-to-end. Codecheckpoint 296068add50d01e9e8ed80666d37e59177ef2c71; zie centrale status en CART_CLEAR_2026-10-19.md. Patch/tests/bewijs opgeslagen, geen theme-source-push zolang Gitintegratie NOT_VERIFIED. Eigenaar beoordeelt/publiceert; agent niet. Oudere cartnotitie hieronder is historisch.

> **WINKELWAGEN 19 OKTOBER — IMPLEMENTED_PREVIEW:** actuele MAIN is nu 195392143626 (fotogalerij gepubliceerd). Concept 195388080394 heet BadkamerCity - Winkelwagen vernieuwd. Eerst 500/500 checksum-identiek gemaakt; finale readback 501 bestanden, vier bestaande gewijzigd/één CSS nieuw en overige 496 gelijk, MAIN 500/500 ongewijzigd. Alleen twee native cart-secties, bc-cart-page.css en nieuwe bc_cart_page-localegroep gewijzigd. Native cart.js en form-/AJAX-contracten behouden; nieuwe aantallen/subtotaal/totaal binnen bestaande .js-contents. CSS op cart-prefix en #MainContent:has(.bc-cart-items), geen globale zoek-/PDP-wijzigingen. Desktop twee kolommen vanaf1100px; ≤360px regelprijs eigen rij; totaalflex mag ombreken. De bestaande echte Shopify-checkout staat al op één pagina; deze release maakt alleen de winkelwagen mooi en wijzigt geen checkoutbranding, adres/payment UI of instellingen. Browserbewijzen en grenzen in LIVE_STATUS_AND_NEXT_STEPS.md en cart-page-verification-2026-10-19.json. Eigen testcart via1→2→1→leeg gecontroleerd; geen bestelling/betaling. Mobiel alleen geïsoleerde component320/390/430px, volledige mobiele site/telefoon nog NOT_TESTED. QA-template exact hersteld. Git alleen vijf-file-productiepatch/bewijs, geen theme-bronpaden zolang integratie NOT_VERIFIED. Eigenaar beoordeelt/publiceert; agent heeft niet gepubliceerd.


> **SUNSHOWER FOTOCARROUSEL 19 OKTOBER — IMPLEMENTED_PREVIEW:** de vorige PointerEvent-fotowissel en éénfoto-dialog zijn vervangen door een native horizontale scroll-snap-reeks met alle foto’s als eigen slides. De browser verzorgt touchbeweging en momentum; geen pointerup-handler die de volgende foto ineens inwisselt. De bestaande algemene themaslider is niet gebruikt: deze ondersteunt vooral bedienknoppen; de galerij krijgt een kleine eigen indexcontroller boven native scroll. Tijdens scroll volgt de enige miniatuurselectie/fototeller het werkelijk dichtstbijzijnde beeld; een pending knopdoel houdt snel herhaalde pijlen coherent. Een late scrollend/fallbacktimer mag dat doel pas wissen als de bestemming werkelijk bereikt is; pointerdown/horizontale wheel mag het wel bewust annuleren. 44px pijlen, begrensde uiteinden, geen loop; thumbnailreveal uitsluitend horizontaal. Native touch-action:auto laat horizontaal/verticaal scrollen en browserpinch toe; PointerEvents onderdrukken alleen een onbedoelde zoomklik na beweging. Elke slide is een echte fullimage-link als JS/modulefallback. Afbeeldingsfout heeft NL/EN-melding. PhotoSwipe 5.4.4 wordt lokaal dynamisch geïmporteerd bij openen; vendor-CSS alleen op Sunshower-PDP. Viewer heeft dezelfde media-index, zichtbare 44px pijlen ook op touch, teller, sluit/zoomknoppen, focus/keyboardbediening, reduced motion en veilige schermranden. Scoped CSS moet pswp__bg en pswp__img--placeholder display:block houden: Dawn verbergt anders lege divs en de donkere backdrop verdwijnt. Viewerchange synchroniseert de paginacarrousel onmiddellijk; destroy behoudt foto en geeft focus terug. allowPanToNext:false voorkomt fotowissel tijdens ingezoomd pannen. ESM-importfout valt terug op de echte afbeeldingslink. Native iPhone-touch/pinch moet afzonderlijk getest worden. Werk alleen in UNPUBLISHED 195392143626 — BadkamerCity - Sunshower fotogalerij; MAIN 195388080394 is de gepubliceerde vorige swipeversie. Actuele bewijs/readback/testgrenzen eerst in LIVE_STATUS_AND_NEXT_STEPS.md. De 18-okt pointer/nodewisselcontracten hieronder zijn historisch. Finale readback: concept 500 files, vijf gewijzigd/drie nieuw, overige 492 identiek; alle acht productie-inhouden exact, QA-template hersteld, MAIN 497/497 ongewijzigd. 39 regressiegroepen + Theme Check R3/R4 en browserpijl/scroll/viewercontroles geslaagd. Fysieke onder-de-duim/inertie/pinch en continue viewer-swipe nog NOT_TESTED; zie expliciete browserbeperkingen in releaseverificatie. Niet publiceren zonder merchantbesluit.

> **HISTORICAL — SUNSHOWER SWIPEN 18 OKTOBER (vervangen in preview 19 oktober):** de vaste grote-fotoknop verwerkt PointerEvents. Hergebruik requestPhoto voor thumbnails en swipes; gewenste cursor los van gecommitteerde selectie is nodig voor snel vegen tijdens laden. Bestaande decode/node/intentguards behouden. Scope touch-action:pan-y pinch-zoom alleen fotoknop; verticale beweging, multi-pointer en cancel mogen geen foto of vergroting activeren. Swipeklik onderdrukken maar volgende tap/keyboardzoom toelaten. Miniatuurreveal alleen horizontale stripscroll, nooit scrollIntoView. Actuele rollen/testgrenzen in LIVE_STATUS_AND_NEXT_STEPS.md.

> **HISTORICAL — SUNSHOWER FOTOSELECTIE 18 OKTOBER (vorig mechanisme):** galerij in bc-sunshower-page.js wisselt nu de daadwerkelijk geladen én gedecodeerde afbeeldingsnode en miniatuurselectie samen; alleen src wijzigen is onvoldoende. mainPhoto is een actuele let-referentie voor zoom/volgende wissels; oude srcset/sizes niet overnemen. Laatste intentie vóór én na decode bewaken; geselecteerde klik annuleert lopende keuze. Herstelde init/load/persisted-pageshow matcht zichtbaar currentSrc zonder breedtequery en haalt geen netwerkdata op. Actuele rollen/bewijs/beperkingen eerst in LIVE_STATUS_AND_NEXT_STEPS.md.

> **SUNSHOWER DIRECT EN SNELLER 18 OKTOBER:** IR/UV-fotokaarten zijn native directe ONE/PLUS-links naar #sunshower-configurator. Tussenpanelen/detailstatus verwijderd; oude detailhash mag kaarten niet verbergen. Beeldbron is nu regioncrop 0,9×hoogte met hetzelfde focalpunt. sizes volgt coverbreedte op basis van kaarthoogte (261px/77,4vw/360px); vervang dit niet simpelweg door 50vw. Accessoire- en aankoopcode ongewijzigd. Actuele rollen, bewijs en beperkingen: LIVE_STATUS_AND_NEXT_STEPS.md en sunshower-direct-speed-verification-2026-10-18.json.

> **SUNSHOWER DIRECT SHOPPEN 18 OKTOBER:** actuele rollen/testgrenzen staan eerst in LIVE_STATUS_AND_NEXT_STEPS.md. Landingaccessoires gebruiken nu eigen snippet bc-sunshower-shop-card en bc-sunshower-shop.js: afzonderlijke kleurproducten leveren servervariant/prijs/foto/beschikbaarheid, native links/forms fallback. Huidige notification-modus bevestigt inline en ververst alleen cart-icon-bubble; native popup zou de pagina naar boven trekken. Per-kaart lock+gedeelde mutatiewachtrij; nooit automatisch opnieuw POSTen na onzekere reactie. Zie sunshower-quickshop-verification-2026-10-18.json en de productiepatch. SunSwipe heeft alleen een eerlijk gelabeld kleurenoverzicht, geen afzonderlijke kleurfoto’s.


> **Vaste dagstart sinds 15 oktober 2026:** lees eerst de [centrale werkstatus op GitHub main](https://github.com/jlamping1997/badkamercity/blob/main/docs/LIVE_STATUS_AND_NEXT_STEPS.md). Daar staan de actuele taak, werkbranch, Shopify MAIN en volgende handeling. De oudere themarollen en werkvoorbeelden hieronder zijn gedateerde achtergrond. Er is maximaal één actieve uitvoering; een nieuwe chat maakt geen nieuw plan of nieuwe codebranch.

> **ZOEKFILTERS EN KORTE TITELS 14 OKTOBER:** verse MAIN `195216048394`; concept `195218047242` voegt zoekfilterprofiel `__all__` en merchantveld `custom.card_title` toe. Veld aangemaakt en nog leeg. Zie [zoek- en titelcontract](https://github.com/jlamping1997/badkamercity/blob/c8f76eea2bf8a81ab0f54196e239e0b3930fe20a/docs/SEARCH_AND_SHORT_TITLES_2026-10-14.md). Publicatie en visuele/live zoekcontrole open; hieronder oudere release-momentopnamen.

> **PRODUCTKAARTEN VERFIJND:** bij laatste read is `195213656330` MAIN. De verdere presentatieverfijning staat in kopie `195216048394` (Productkaarten verfijnd); zie [kaartstatus](https://github.com/jlamping1997/badkamercity/blob/c8f76eea2bf8a81ab0f54196e239e0b3930fe20a/docs/PRODUCT_CARDS_2026-10-14.md). Geen header-/productdatamutatie. Tien kaart-rendercontroles en tien filtertests geslaagd. Visuele eindcontrole en merchant-publicatie blijven open; connector kan geen MAIN schrijven of publiceren.

> **GOEDGEKEURDE PRODUCTKAARTEN:** MAIN is bij de laatste read `195211919626`. Het goedgekeurde ontwerp met productkenmerken en ‘Bekijk product’ staat volledig in kopie `195213656330` (Goedgekeurde productkaarten); zie [actuele kaartstatus](https://github.com/jlamping1997/badkamercity/blob/c8f76eea2bf8a81ab0f54196e239e0b3930fe20a/docs/PRODUCT_CARDS_2026-10-14.md). Merchant heeft live toepassing geautoriseerd, maar de connector kan MAIN niet schrijven/publiceren. Alleen merchant-publicatie en visuele eindcontrole blijven nodig voor deze release. Header behouden; oudere thema-status hieronder is historisch.

> **NIEUW ONTWERPCONCEPT 14 OKTOBER:** een verse Admin-read toont `195038216458` als MAIN. Productkaartwijzigingen staan daarom in nieuwe UNPUBLISHED kopie `195211919626` (Productkaarten 14 okt). Zie [productkaarten](https://github.com/jlamping1997/badkamercity/blob/c8f76eea2bf8a81ab0f54196e239e0b3930fe20a/docs/PRODUCT_CARDS_2026-10-14.md). Browserpreview geblokkeerd; visuele desktop/mobiele review open. Oudere aanwijzingen hieronder dat Afronding basis nog concept is, zijn historisch.

> **LATERE UPDATE 14 OKTOBER:** op verzoek van de merchant zijn de filters in concept `195038216458` standaard zichtbaar gemaakt, zonder `bcfilters=1`. Wastafelkranen zonder parameter gecontroleerd: 454 producten en externe filters actief. Zie de aanvulling bovenaan [filterpreview](https://github.com/jlamping1997/badkamercity/blob/c8f76eea2bf8a81ab0f54196e239e0b3930fe20a/docs/FILTER_PREVIEW_2026-10-14.md). MAIN is niet gewijzigd.

> **ACTUELE AANVULLING 14 OKTOBER 2026:** lees eerst [gecontroleerde filterpreview](https://github.com/jlamping1997/badkamercity/blob/c8f76eea2bf8a81ab0f54196e239e0b3930fe20a/docs/FILTER_PREVIEW_2026-10-14.md). De merchant heeft index-, API- en HTTPS/CORS-proeven op de VPS succesvol uitgevoerd. Concept `195038216458` gebruikt de nieuwe route opt-in via `bcfilters=1`; desktopcontroles en 10 regressietests zijn geslaagd. Mobiele visuele controle, verdere familiecontrole en standaard activering/publicatie staan open. MAIN blijft `194981003530`.

> **ACTUELE AANVULLING 10 OKTOBER 2026:** lees eerst [Afronding basis 10 oktober](https://github.com/jlamping1997/badkamercity/blob/c8f76eea2bf8a81ab0f54196e239e0b3930fe20a/docs/AFRONDING_BASIS_2026-10-10.md). MAIN is nu `194981003530`; het samengebrachte concept `195038216458` is ongepubliceerd en staat op REVIEW. De onderstaande architectuur en aantallen beschrijven de historische momentopname van 7 oktober. Nieuwe previewtests en open mobiele controle staan in de aanvulling.

> **UITGEBREIDE OVERDRACHT (2026-10-07):** Begin als nieuwe AI/ontwikkelaar bij **[HANDOVER_START_HERE.md](HANDOVER_START_HERE.md)**. Dit document blijft de volledige functionele basis. De volgende aanvullende documenten maken de overdracht operationeel en controleerbaar:
>
> - [Live-status en volgende prioriteiten](LIVE_STATUS_AND_NEXT_STEPS.md)
> - [Alle theme-componenten/instellingen](THEME_COMPONENT_REFERENCE.md)
> - [Machineleesbare code-/dependencykaart van 441 files](THEME_CODE_MAP_2026-10-07.json)
> - [Shopify Admin-structuur: 204 collecties, 9 menu's, metafields](SHOPIFY_ADMIN_STRUCTURE_2026-10-07.json)
> - [Metafield-audit code versus Shopify](PRODUCT_METAFIELD_MAPPING_AUDIT.md)
> - [Operationeel runbook](OPERATIONAL_RUNBOOK.md), [storingsgids](TROUBLESHOOTING.md), [release & QA](RELEASE_AND_QA.md)
> - [Praktijkvoorbeelden en overnametest](WORKED_EXAMPLES_AND_HANDOFF_TEST.md)
> - [Systemen, ontbrekende overdrachtsstukken en toegang](SYSTEM_OWNERSHIP_AND_GAPS.md)
>
> **Extra geverifieerde Admin-data:** 11.053 producten (11.051 ACTIVE, 1 DRAFT, 1 UNLISTED), 204 collecties (191 default, 12 `category-landing`, 1 `bc-meubelhub`), 9 menu's, 174 PRODUCT-metafielddefinities. Dit zijn read-only snapshots, geen bewezen publicatie-/kwaliteitsdekking. Onbekende externe VPS-, checkout- en leverancierscomponenten worden niet als “af” voorgesteld.


**Momentopname:** 7 oktober 2026  
**Doel:** Een volgende ChatGPT/Codex/andere AI of ontwikkelaar moet de huidige code, schermen, datastromen, afhankelijkheden, beperkingen en veilige werkwijze begrijpen zonder opnieuw te beginnen.

> **LEES DIT EERST.** Oude documenten in `docs/` beschrijven soms oude Shopify-theme-ID's en de vroegere fase “implementation blocked”. Die gelden niet als actuele productie-inventaris. Dit document legt vast wat daadwerkelijk in het live thema is aangetroffen; waar gegevens alleen in Shopify Admin of een externe VPS bestaan, staat dat expliciet vermeld. Voer nooit ongeautoriseerde productiepublicaties of destructieve Git-commando's uit.

## Inhoud

1. Huidige omgeving en bewijs
2. Algemene architectuur en mappen
3. Bronnen van waarheid
4. Thema, header, navigatie en footer
5. Homepage
6. Collectiearchitectuur
7. Badkamermeubels-hub, mobiel ontwerp en SEO
8. Productdetailpagina
9. Product-switcher V2
10. Setonderdelen en aanvullende accessoires
11. Filterarchitectuur en VPS-proef
12. Zoek-, winkelwagen- en overige pagina's
13. SEO en performance
14. Databeheer en imports
15. Git- en Shopify-ontwikkelworkflow
16. Test- en reviewmatrix
17. Bekende aandachtspunten en open zaken
18. Eerste opdracht voor een nieuwe AI
19. Bestandswijzer

---

## 1. Huidige omgeving en bewijs

| Eigenschap | Verifieerbare momentopname |
| --- | --- |
| Webshop | BadkamerCity (sanitair, badkamers, tegels) |
| Shopify-store | `fpa9hu-i3.myshopify.com` |
| Live thema op 2026-10-07 | **BadkamerCity - SEO categoriehub** |
| Shopify OnlineStoreTheme-ID | `gid://shopify/OnlineStoreTheme/194864677130` |
| Theme role | `MAIN` |
| Theme laatste update | `2026-10-06T21:14:23Z` |
| GitHub-repository | `https://github.com/jlamping1997/badkamercity` |
| Standaardbranch | `main` |
| Snapshot-/herstelbranch | `sync/live-shopify-2026-10-07` |
| Oude main vóór synchronisatie | `fbaef4d812d96e794d94eedd4613d7abb53ebc08` |
| Lokaal gebruikt projectpad | `C:\Projects\badkamercity-shopify-current`; eerder ook `C:\Projects\badkamercity` |
| Exacte bron van UI in Git | `assets/`, `config/`, `layout/`, `locales/`, `sections/`, `snippets/`, `templates/` |
| Admin-voorbeeldcollectie | `gid://shopify/Collection/569428148490` — Badkamermeubels |
| Machine-readable bestandsregister | `docs/BASELINE_MANIFEST_2026-10-07.json` |

### 1.1 Volledige theme-snapshot, inclusief vier grote bestanden

Shopify bevatte op het meetmoment **441 theme-bestanden**. De Git-snapshot is gecontroleerd op inhoud:

- **437 bestanden:** directe vergelijking van de Git-blob-SHA1 tegen de Shopify-code, inclusief de ene binaire GIF.
- **4 grote JSON-bestanden:** Shopify retourneert wegens hun formaat tijdelijke asset-URL's. Voor `assets/product-switcher-data.json` en de drie bestaande QA-backups komt het Shopify-MD5 **exact overeen** met de Git-inhoud na omzetting van LF naar de CRLF-regeleinden die Shopify gebruikt. Ook de bytegroottes kloppen exact.
- **Resultaat:** 441/441 inhoudelijk geverifieerd, 0 ontbrekende theme-bestanden; de regeleinden kunnen tussen Git en Shopify verschillen.
- Deze controle bewijst de theme-code, **niet** dat elk product volledig is ingevuld, filters live gezond zijn, alle links bestaan of Core Web Vitals zijn geslaagd.

Gebruik `docs/BASELINE_MANIFEST_2026-10-07.json` voor pad, Shopify-grootte, contenttype en MD5 per bestand. De originele Git-geschiedenis wordt bewaard en niet geforceerd herschreven.

### 1.2 Elke nieuwe sessie verifieert opnieuw wat MAIN is

Thema's wisselen bij een Shopify-publicatie van naam/rol. Oude IDs zoals `189463068938`, `192770375946`, `194840461578` en `194835742986` kunnen in historische chats en documenten voorkomen; **nooit blind aannemen dat ze nog live zijn**.

~~~powershell
shopify theme list --store fpa9hu-i3.myshopify.com
~~~

Voordat je code naar Shopify pusht, controleer de rol `MAIN` of `UNPUBLISHED`, de store-URL en de gewenste bestanden. Alleen de merchant publiceert een thema naar productie.

## 2. Architectuur en bestanden

BadkamerCity is een **Shopify Online Store 2.0 theme**, gebaseerd op Shopify/Dawn-concepten, met BadkamerCity-uitbreidingen. Het is geen losse React/Next.js SPA en er is voor deze theme-repo geen algemene npm-build nodig.

~~~text
layout/theme.liquid
 ├─ header-group → sections/header.liquid, snippets/header-*, BC-navigatie
 ├─ content_for_layout
 │   ├─ templates/index.json                      homepage
 │   ├─ templates/product.json                    productdetail
 │   ├─ templates/collection.bc-meubelhub.json    speciale hoofdcategorie
 │   ├─ templates/collection.category-landing.json algemene categoriehub
 │   ├─ templates/collection.json                 producten + native filters
 │   ├─ templates/search.json                     zoeken
 │   └─ overige page/cart/account/blog templates
 └─ footer-group → sections/footer.liquid

templates/*.json → sections/*.liquid → snippets/*.liquid
                       ↓                  ↓
                   assets/*.css       assets/*.js/data/images
                       ↓
               Shopify Admin gegevens + externe diensten
~~~

| Map | Betekenis |
| --- | --- |
| `layout/` | Global HTML-shell, head/canonical/viewport, Shopify layoutslots |
| `templates/` | Welke secties, settings en blokken op een paginatype geladen worden |
| `sections/` | Grotere Shopify Liquid-secties met `{% schema %}` voor Theme Editor |
| `snippets/` | Kleine, herbruikbare Liquid-renderers via `{% render %}` |
| `assets/` | CSS, browser-JS, SVG, data-JSON; publieke bestanden |
| `config/` | Theme settings en huidig `settings_data.json`; niet hetzelfde als alle Admin-data |
| `locales/` | Vertalingen (`nl.json`, `en.default.json` enz.) |
| `scripts/` | Lokale ontwikkel-/controlehulpen, niet automatisch geladen door Shopify |
| `docs/` | Handoff, historische audits, data-overeenkomsten, bewijs en snapshot |

**Conventie:** `bc-*` duidt meestal BadkamerCity-custom code aan; bestaande Dawn-componenten blijven vaak onder hun oorspronkelijke namen bestaan. Ook bestanden zonder `bc-` kunnen fors zijn aangepast, met name `main-product.liquid`, `header.liquid` en `footer.liquid`.

## 3. Waar de waarheid voor gegevens staat

**In Git/theme:** weergave, page templates, koppelingen van componenten, dynamische Liquid-voorwaarden, JS, CSS, sommige expliciete SKU-tabellen en statische data-assets.

**In Shopify Admin en dus NIET volledig in Git:**
- Producten en varianten, actieve `ACTIVE/DRAFT`-status, online-publicaties, SKU's, titel, vendor, producttype, prijzen, voorraad en media.
- Collecties, memberships, `templateSuffix`, SEO title/description, collectieomschrijving, productstatus.
- Menustructuur, admin-metafielddefinities en -waarden, app-instellingen, Search & Discovery, verzend-/betaal-/belastinginstellingen.
- Redirects, markets, domeinen, klant- en orderdata.
- Bestanden op Shopify Files/CDN die niet als theme-asset zijn ingecheckt.

**Extern:** leverancierssheets, Hotbath/Wiesbaden/JEE-O-importers, scraperprojecten, VPS/Typesense-filters en syncs. De aanwezigheid van frontend-code bewijst niet dat de externe dienst werkt.

**Gevolg:** een verse `git clone` reproduceert de theme-code, maar niet de gehele webshop inclusief Admin-content, prijzen en serverdiensten. Verzín nooit een ontbrekende datalaag.

## 4. HTML-shell, header, navigatie en footer

### 4.1 Basis en head

`layout/theme.liquid` bevat onder meer:

- `<html lang="{{ request.locale.iso_code }}">`.
- `meta charset`, viewport voor mobiel, canonical via `{{ canonical_url }}`.
- Shopify `page_title` in de `<title>`, `page_description` voor meta description.
- `{% render 'meta-tags' %}` voor Open Graph/sociale metadata (waaronder product-specifieke OG-informatie).
- Shopify `content_for_header` en `content_for_layout`; niet verwijderen.
- `base.css`, `constants.js`, `pubsub.js`, `global.js`, `search-form.js`, conditionele CSS/JS.
- Skip-to-content-link naar `#MainContent`.

### 4.2 Header

`sections/header.liquid` beheert de BadkamerCity desktop/mobiele header. Functionele onderdelen in de code zijn o.a.:

- Desktop zoekveld en toegang tot Shopify search/predictive search.
- Horizontale categorie- en meganavigatie, inclusief subniveaus en backdrop.
- Mobiele drawer met terug/volgende navigatie (`bc-mobile-drawer`, `bc-mobile-panel`, `bc-mobile-next`, `bc-mobile-back`).
- Account-, winkelwagen- en navigatie-iconen; winkelwagenindicator via `snippets/bc-header-cart.liquid`.
- Shopify-lokalisatiecomponenten wanneer ingeschakeld.

Controleer bestaande menu's onder Shopify **Inhoud → Menu's** voordat je routes of breadcrumbs aanpast. Een menu-link kan naar een toekomstige/lege collectie wijzen; maak geen onbedoelde 404-landings.

### 4.3 Footer

`sections/footer.liquid` bevat de compacte/donkere BadkamerCity-footer en wordt via `footer-group` getoond. Linkgroepen/labels en informatie komen voor een deel uit Shopify theme settings/Admin-menu's. Eerst bestaande blokconfiguratie controleren, niet een generieke footer overnemen.

## 5. Homepage

`templates/index.json` bevat op deze snapshot de volgende **actieve volgorde**:

| # | Section | Rol |
| --- | --- | --- |
| 1 | `home-hero` | hero en promotionele afbeeldingen/banners |
| 2 | `home-category-grid` | acht categorie-/navigatieblokken |
| 3 | `home-popular-products` | selectie populaire producten |
| 4 | `home-complete-bathroom` | content “Van idee naar complete badkamer” |
| 5 | `home-shop-by-style` | vier stijl-/inspiratiekaarten |
| 6 | `home-brand-rail` | merkenstrip (zes blokken) |
| 7 | `home-mijn-badkamercity` | merk-/service-/inspiratieblokken (zes) |
| 8 | `home-help-cta` | hulp/contact-call-to-action |

Exacte instellingen staan in `templates/index.json` en de desbetreffende `sections/home-*.liquid`. Shopify CDN-images, linkdoelen en klantbeloftes moet je per implementatie controleren; gegenereerde afbeeldingen in oudere gesprekken zijn geen bewijs van echt assortiment of korting.

## 6. De drie soorten collectiepagina

### 6.1 Speciale Badkamermeubels-hub

De collectie `/collections/badkamermeubels` heeft in Shopify Admin suffix `bc-meubelhub`. Daardoor gebruikt hij:

| Rol | Pad |
| --- | --- |
| JSON-compositie | `templates/collection.bc-meubelhub.json` |
| Liquid-pagina | `sections/bc-meubelhub.liquid` |
| Scoped CSS | `assets/bc-meubelhub.css` |
| Progressive-enhancement JS | `assets/bc-meubelhub.js` |
| Iconen | `snippets/bc-meubelhub-icon.liquid` |

**Werkingsvolgorde:**
1. Breadcrumb `Home › Badkamermeubels` in `<nav>`.
2. Eén zichtbare `<h1>Badkamermeubels</h1>`, intro, desktop hero en korte voordelen.
3. Een echte `<h2>` **Kies een categorie**; zes categoriekaarten met `<h3>`:
   - `badmeubel-sets` — Badmeubel sets
   - `toiletmeubels` — Toiletmeubels
   - `losse-onderkasten` — Losse onderkasten
   - `kolom-zijkasten` — Kolom & Zijkasten
   - `wastafelbladen` — Wastafelbladen
   - `spiegels-en-spiegelkasten` — Spiegels.
4. De kaart gebruikt `block.settings.category` (Shopify collectieobject), label, caption, image picker of image-URL. De Liquid-code bepaalt `can_link`: alleen als de collectie bestaat én producten heeft, of `allow_empty` bewust is gekozen. Zonder link blijft een pending kaart.
5. Sectie **Vind het perfecte badkamermeubel**: groepen `Op type / Op maat / Op stijl / Op merk`. De bijbehorende optionele Shopify menus heten `type_menu`, `maat_menu`, `stijl_menu`, `merk_menu`. Zonder menu gebruikt type de kaarten; maat/stijl toont niet-klikbare voorbeelden; merk kan terugvallen op `collection.all_vendors`.
6. Het merkenblok gebruikt ingestelde merkblokken of bestaande vendors, met alleen geldige URL's.
7. Lifestyle-inspiratie + informatieve servicekaarten.
8. Onderste SEO-/keuzeadviestekst, opgebouwd uit de Shopify-beschrijving na `[SPLIT]`.

**Scheid bron en weergave:** het JSON-template bevat het design/afbeeldinginstellingen; de bestaande collectieomschrijving bevat advies en extra CSS; de koppeling van de collectie aan dit template is een Admin-veld. Alle drie moeten correct zijn.

### 6.1.1 De tekstsplit `[SPLIT]`

In `bc-meubelhub.liquid` wordt `collection.description` opgesplitst rond `[SPLIT]`:
- boven: korte intro als er géén expliciete `section.settings.intro` is;
- onder: uitgebreid advies op de pagina;
- headings uit die tekst worden bij rendering semantisch verschoven: bron `h2` → zichtbare `h3` en bron `h3` → `h4`, passend onder `h2 Advies over badkamermeubels`;
- geen tweede H1 in ondertekst.

### 6.1.2 Mobiel ontwerp is door de gebruiker goedgekeurd

Op mobiel is **zo min mogelijk scrollen tot navigatie** het leidende UX-principe. De compacte lijst met thumbnails/titels/pijlen verschijnt direct onder de korte intro; de grote sfeerhero/USP's verdwijnen daar. Desktop behoudt luxe cards en een compactere hero. De gebruiker heeft dit mobiele resultaat expliciet goedgekeurd.

**CRUCIALE VERBORGEN AFHANKELIJKHEID:** drie designpatches bevinden zich als HTML-`<style>` **in de Shopify Admin-collectieomschrijving**, **niet** alleen in het Git-thema:

| Marker | Style-ID | Functie |
| --- | --- | --- |
| `BCM_MOBILE_NAV_V2_START` | `bcm-mobile-nav-v2` | mobiele rijnavigatie, hero/USP's verborgen, korte intro; bij ≤749 px |
| `BCM_DESKTOP_CTA_V1_START` | `bcm-desktop-cta-v1` | duidelijke desktop klikbaarheid, CTA “Bekijk categorie”, hover, pijl |
| `BCM_HERO_COMPACT_V1_START` | `bcm-hero-compact-v1` | desktop hero lager, minder bovenruimte |

Die volledige Admin-omschrijving staat ook **als read-only snapshot** in `docs/shopify-admin/collection-badkamermeubels-description-2026-10-07.html`; metadata, SEO-velden en templatekeuze in `docs/shopify-admin/collection-badkamermeubels-2026-10-07.json`.

De Liquid-template bevat inmiddels een **echte H2** “Kies een categorie”; de oude CSS-pseudo-heading `.bcm-categories::before` wordt uitgeschakeld in de theme-CSS. **Verwijder de Admin-`<style>`-blokken niet voordat je hun effect gecontroleerd hebt overgezet naar `assets/bc-meubelhub.css`.** Anders breek je onbedoeld het goedgekeurde mobiele ontwerp. Ook Shopify's WYSIWYG kan de omschrijving onbedoeld veranderen.

### 6.1.3 SEO en structured data van deze hub

`bc-meubelhub.liquid` rendert één JSON-LD `@graph` met `CollectionPage`, `BreadcrumbList` en `ItemList` voor klikbare subcategorieën. De H1/H2/H3/H4-structuur is expliciet; gebruik echte `<a href>`-links. In `layout/theme.liquid` staat de canonical. Dit helpt zoekmachines de structuur begrijpen, maar garandeert **geen** Google-ranking.

Shopify Admin SEO op snapshotmoment:
- title: **Badkamermeubels en wastafelmeubels**;
- description: **Vergelijk badkamermeubels, complete badmeubelsets en losse onderkasten. Kies de maat, indeling en uitstraling die passen bij jouw badkamer bij BadkamerCity.**
- de collectie had administratief 235 gekoppelde producten; dit is **geen bevestiging** dat ze alle actief/gepubliceerd zijn.

### 6.2 Andere hoofdcategorieën: algemene landing

`templates/collection.category-landing.json` gebruikt:
- `sections/main-category-landing.liquid`;
- `sections/bc-collection-advice.liquid`;
- `snippets/bc-category-breadcrumbs.liquid` voor hiërarchisch pad + BreadcrumbList;
- `snippets/bc-category-children.liquid` voor kindcategorieën en afbeeldingen;
- `snippets/bc-category-destination.liquid` voor bestaande URL of zoekfallback;
- `snippets/bc-category-link-index.liquid` en `bc-category-index-entry.liquid` voor interne-linkindex;
- `snippets/bc-collection-intro.liquid` voor SEO-tekst vóór `[SPLIT]`.

De categorieboom komt hoofdzakelijk uit Shopify menu `main-menu`; in de JSON staan specifieke menu-koppelingen voor `wastafels` (`bc-wastafels-categorieen` / `bc-wastafels-a-z`) en `accessoires` (`bc-accessoires-categorieen` / `bc-accessoires-a-z`). Die menubronnen leven in Shopify Admin.

`show_product_grid=false` in deze algemene categorie-hub: normaal dient hij als **keuzepagina**, niet meteen als productoverzicht. Afbeeldingen/kaarten en adviesteksten kunnen worden bewerkt via Theme Editor/collecties, maar menu's/producten blijven losse Admin-data.

### 6.3 Normale product-collecties

`templates/collection.json` gebruikt `main-collection-banner` + `main-collection-product-grid` + `bc-collection-advice`.

`sections/main-collection-product-grid.liquid` heeft Shopify native `paginate collection.products`, sorteerkeuzes, `facets.liquid`/`facets.js`, active-filter-pills (`bc-collection-active-filters.liquid`), productkaarten en lege-resultaatstatus. In de JSON staan filtering én sorting op `true`. De filterdefinities zelf moeten in Shopify Admin/Search & Discovery worden beheerd. Verwijder servergerenderde cards/paginering niet vanwege een nog experimentele JS-filterlaag.

## 7. Productdetailpagina (PDP)

**Template:** `templates/product.json` → `sections/main-product.liquid` + `sections/related-products.liquid`.

`main-product.liquid` is groot (ruim 160 kB) en combineert custom CSS met Shopify/Dawn-renderers. Belangrijkste functies:

| Functionaliteit | Belangrijkste bron / werking |
| --- | --- |
| Media | `product-media-gallery`, `media-gallery.js`, `product-modal.js`, Shopify media; gallery/thumbnails en responsive layout |
| Koopbox | native product/vendor/SKU, prijs, evt. vergelijkprijs, voorraad-/leveringscopy uit geselecteerde Shopify-variant/data |
| Opties en variantkeuze | `product-variant-picker` en/of `bc-product-switcher`; niet verwarren met elkaar |
| Toevoegen aan winkelwagen | `buy-buttons`, `product-form.js`; Shopify cart/checkout |
| Sticky koopgedrag | `assets/bc-product-sticky.js` |
| Productbeschrijving | uit Shopify `product.description`, met inkorten/uitklappen en informatienavigatie |
| Specificaties | `snippets/bc-product-detail-specs.liquid` en `bc-product-detail-row.liquid` |
| Plus- en minpunten | `product-pros-cons` en `component-product-pros-cons.css`; alleen tonen als velden/data dat toelaten |
| Complete set | `bc-product-set-components` en expliciete SKU-datamapping |
| Aanvullende accessoires | `bc-product-accessories` en expliciete relaties |
| Gerelateerd | `sections/related-products.liquid` via Shopify productaanbevelingen |

Test PDP's met: één afbeelding, meerdere afbeeldingen, bijzonder brede/hoge foto's, lege metafields, wel/geen switcher, sets, losse onderdelen en verschillende varianten. Niet alleen het testproduct gebruiken.

### 7.1 Specificatievelden

`bc-product-detail-specs.liquid` genereert alleen groepen met daadwerkelijk beschikbare velden, onder andere:
- **Product**: SKU/artikelnummer, fabrikantnummer, EAN, merk/vendor, serie;
- **Algemeen**: vormgeving/stijlgroep, kleurgroep, basiskleur, glansgraad, kraanmateriaal, montagewijze, afwerking greep;
- **Douche/thermostaat**: hoofddouche, diameter/dikte, straalsoorten, bevestiging/douchearm, handdouche, glijstang/slang, thermostatisch, inbouwdeel, uitgangen en bediening;
- **Hotbath systemen**: EcoAir, Shower Power, Flühs en Plumber Friendly.

Bron: bestaande `product.metafields.custom.*`-velden en native SKU/vendor. **Nooit** niet-bestaande producteigenschappen invullen op basis van titels of merkvermoedens. Metafield-schema en waarden staan in Shopify Admin.

### 7.2 Switcher V2: zelfstandige producten

**Bestanden:** `snippets/bc-product-switcher.liquid`, `assets/bc-product-switcher.js`, `assets/product-switcher-data.json` en drie QA-backupvarianten.

Liquid leest `product.metafields.custom.switch_group`. Alleen bij een gevulde waarde ontstaat een `data-bc-product-switcher-v2`-root met o.a. `data-switch-group`, product-handle/URL en asset-URL.

JS:
1. Laadt één keer het switcher-databestand met `fetch` (gedeelde promise/cache).
2. Vindt `groups`-record op group-ID en huidige uitvoering op product-handle/URL.
3. Leest menu's, opties, beschikbare waarden en gekoppelde producten.
4. Berekent geldige combinaties; onmogelijke keuzes worden disabled.
5. Gebruikt doorgaans knoppen tot vijf keuzes, anders select; focus/aria status aanwezig.
6. Voltooide keuze navigeert naar de **aparte, echte product-URL** van de gekozen uitvoering.

Zo'n switcher-uitvoering is functioneel niet noodzakelijk een Shopify variant binnen één product. Veel Hotbath-uitvoeringen zijn zelfstandige Shopify-producten met eigen SKU/URL. Bij ontbrekende groep/data logt de JS waarschuwingen en mag geen niet-bestaande SKU bestelbaar lijken.

**Datarisico:** `product-switcher-data.json` is ~1,9 MB. Dat is niet automatisch een performant formaat op mobiel; meet belasting/HTTP-compressie en API/asset caching voordat je grote uitbreidingen maakt. Historische `generated_at` in die JSON is geen live leverancier-syncgarantie.

### 7.3 Sets

**`snippets/bc-product-set-data.liquid`** bevat exact geverifieerde regels per relevante Hotbath-SKU, in tekstformaat `status|quantity|sku|name~`. De drie statussoorten zijn `included` (inbegrepen), `required` (apart nodig) en `optional` (optioneel).

**`bc-product-set-components.liquid`**, `bc-product-set-product-handle.liquid` en `bc-product-set-item.liquid` zetten deze data in UI om, controleren doelproduct/vendor en SKU/variant. Gerenderde prijs en beschikbaarheid horen uit het Shopify-doelproduct te komen, niet uit de tekst van de mapping.

`testproduct-badkamercity-productpagina` heeft aparte voorbeeldregels. **Kopieer demo-onderdelen nooit blind naar echte producten.** Samenstellingsdata wordt niet “geraden” uit de producttitel.

### 7.4 Maak je bestelling compleet

**`bc-product-accessories-data.liquid`**, `bc-product-accessories.liquid` en `bc-product-accessory-item.liquid` beheren gericht passende gerelateerde artikelen. Dit zijn handmatig gecureerde `required`/`optional`-SKU-/handle-koppelingen met validatie; geen algemene AI-cross-sell of compleet assortiment. Sommige Hotbath-SKU's koppelen een passend onderhoudsartikel. Voeg alleen relaties toe op basis van geverifieerde compatibiliteit.

## 8. Externe filters: experimenteel, niet standaard uitgerold

**Bestanden:** `assets/bc-external-filters.js`, `assets/bc-external-filters.css`, `snippets/bc-external-filters.liquid` en integratie in `sections/main-collection-product-grid.liquid`.

**Activeringsvoorwaarden in de actuele code:**
- Liquid laadt het snippet alleen voor `collection.handle == 'wastafelkranen'`.
- JS stopt onmiddellijk tenzij de URL `bcfilters=1` heeft.
- Voor normale bezoekers zonder die parameter blijft Shopify native filtering gebruikt.

**API-base in snippet:** `https://vps-7ffd625d.vps.ovh.net/v3`  
**Request:** `POST {apiBase}/api/v1/search`, met collectiehandle, filters, sortering, paginering. De frontend leest `facets` en `products` uit de response.

**Functies in het experiment:** facetdetails, filtervalues en counts, numerieke min/max, checkboxen, actieve filterchips, wissen, sorteren op relevantie/prijs, productcards, pagination en een mobiele filterdrawer. URL-state via `bcf_*`, `bcr_*`, `bcsort`, `bcpage`.

**Kritieke waarschuwing:** CSS verbergt bij class `bc-external-filters-active` de native filters en paginering. De JS zet die class vóór bewezen API-succes. De fouttekst belooft dat het normale productoverzicht blijft, maar de volledige netwerkfoutfallback en VPS/CORS/Typesense-gezondheid zijn **niet end-to-end bewezen**. Niet standaard voor klanten inschakelen tot backend/search/UI/fallback getest zijn.

Backend/Typesense, VPS-deployment, indexsync, credentials en leveranciersmappings horen **niet** tot deze theme-repo. Er is historisch een aparte lokale map `C:\Projects\badkamercity-filters-LIVE`. Maak geen backend-API-sleutels openbaar via theme-assets.

## 9. Overige pagina's

| Pagina | Theme-code | Achterliggende data |
| --- | --- | --- |
| Zoekresultaten | `templates/search.json`, `sections/main-search.liquid` | Shopify search |
| Productlisting | `templates/collection.json`, `main-collection-product-grid` | Shopify collectie + Search & Discovery |
| Cart | `templates/cart.json`, `main-cart-items`, `main-cart-footer`, JS drawer | Shopify cart |
| Contact | `templates/page.contact.json`, `contact-form` | Shopify Page/contact |
| Contentpagina | `templates/page.json`, `main-page.liquid` | Shopify Page |
| Begrippenlijst | `page.begrip.json` / `page.begrippenlijst.json`, `main-glossary*` | Shopify content |
| Blog/artikel | `templates/blog.json` / `article.json` | Shopify blogs |
| Accounts | `templates/customers/*.json` | Shopify Customer Account-config |
| 404/password | `templates/404.json` / `password.json` | Theme + Shopify store state |

Verzend-/BTW-/betaalregels kunnen **niet** betrouwbaar uit dit theme worden gereconstrueerd. Controleer daarvoor Shopify Admin/checkout.

## 10. SEO: feitelijke opbouw en resterend werk

**Al aanwezig:**
- Canonical, title en optionele meta description in `layout/theme.liquid`.
- `meta-tags.liquid` voor OG/sociale metadata.
- Echte H1 op Badkamermeubels; H2 categorie/keuzehulp/merken/advies; H3 kaarten en subonderwerpen; H4 bij nested vragen.
- Crawlbare interne links naar Shopify-collecties, semantische `<nav>` en breadcrumbs.
- `CollectionPage`, `BreadcrumbList`, `ItemList` JSON-LD **op Badkamermeubels-hub**.
- Op algemene landingspagina's aparte breadcrumb/intro/SEO-split.
- Informatieve adviescontent onder het hoofdkeuzeproces.

**Niet bewezen/blijft controleren:**
- Google Search Console-indexatiestatus, duplicate content, queryposities, redirects, robots/sitemap, hreflang en cannibalization.
- Product- en CollectionPage-schemaoverlap met andere theme-snippets of apps.
- Correcte canonical/noindex bij filterparameters en routes.
- Geladen product-/subcollectie-URL's, informatiekwaliteit en daadwerkelijke catalogusdekking.
- Lighthouse en Core Web Vitals; SEO-opmaak alleen levert geen top-3-ranking.

Let op: de hero-image van de hub heeft `fetchpriority="high"` en `loading="eager"`, ook al wordt hero-media mobiel via CSS verborgen. Dat kan extra mobiele requests geven. Controleer in DevTools/real-user metingen voordat je “super snel” als bewezen markeert.

## 11. Productdata, import en externe projecten

Theme-code toont data; import en verrijking zijn andere workflows. In eerdere werksessies is gewerkt aan Hotbath, Wiesbaden en JEE-O (titels, teksten, foto's, SEO, categories en metafields), maar individuele compleetheid/publicatiestatus moeten **opnieuw via Shopify** worden gecontroleerd. Historische export- en scrape-mappen zijn geen betrouwbare huidige bron zonder bestand/bronversie:

- `C:\Projects\badkamerxxl_scraper` — historische Hotbath-scrape-werkmap;
- `C:\Projects\badkamercity-filters-LIVE` — aparte filterfrontend/-backendworkflow;
- `C:\Projects\badkamercity-shopify-current` — historisch lokale Shopify-codekopie;
- `C:\Projects\badkamercity` — eerdere Git-repository/CLI-map.

Voor productdata bestaat historisch `docs/PRODUCT_DATA_CONTRACT.md`. Dat beschrijft een **conceptueel** informatiecontract en kan afwijken van daadwerkelijke huidige `custom.*`-metafielddefinities; nooit blind importeren. De aanwezigheid van een product in Admin bewijst niet dat de Online Store-publicatie aanstaat. Controleer prijs, voorraadbeleid, variantidentiteit, SKU, foto's, rechten, BTW en logistiek per importbatch.

## 12. Veilig Git en Shopify synchroniseren

### 12.1 Windows-worktree opschonen zonder verliezen

**Eerst inspecteren:**

~~~powershell
cd C:\Projects\badkamercity-shopify-current
git rev-parse --show-toplevel
git remote -v
git branch --show-current
git status --short
git fetch origin
git log -1 --oneline origin/main
~~~

Als `git status --short` leeg is en je op `main` zit:

~~~powershell
git pull --ff-only origin main
git status --porcelain=v1
~~~

Voor een niet-schone tree: **geen `reset --hard` en geen `git clean -fd`**. Eerst diff en ongetrackte bestanden beoordelen. Maak indien nodig bewust een lokale checkpointcommit of stash:

~~~powershell
git status --short
git stash push --include-untracked -m "BadkamerCity voor live baseline 2026-10-07"
git pull --ff-only origin main
git stash list
~~~

Stash is **lokaal** en blijft bestaan; wijzig/restore alleen nadat je die inhoud hebt beoordeeld. De GitHub-connector kan de lokale Windows-worktree niet op afstand schoonmaken.

Er wordt ook een beschermend script bijgeleverd: `scripts/git-align-worktree.ps1`. Het weigert te werken buiten de juiste Git-origin, branch of bij onbewaarde wijzigingen, doet nooit force/reset/clean.

### 12.2 Shopify-theme veilig ontwikkelen

1. Controleer de werkelijk **live MAIN** theme-rol/ID.
2. Begin vanaf de actuele Git `main` en commit je werk in een aparte featurebranch.
3. Gebruik een ongepubliceerd Shopify preview/development-thema dat inhoudelijk overeenkomt met live.
4. Pas alleen de relevante theme-bestanden aan. `shopify theme push --only` voor een selectieve preview is veiliger dan een volledige blinde push.
5. Test mobiel/desktop, navigatie, koopbox, filterpagina's en SEO; laat opdrachtgever beoordelen.
6. Commit gecontroleerde changes met begrijpelijke commitmelding en changelog.
7. Alleen de gebruiker publiceert naar live; daarna noteer je het nieuwe MAIN theme-ID en leg je opnieuw een baseline vast.
8. Controleer na een “success”-melding dat bestanden daadwerkelijk in het bedoelde thema zijn opgeslagen; een CLI-melding is niet genoeg.

Voor alleen-lezen vergelijking van thema's kan een `shopify theme pull` naar een **nieuwe tijdelijke map buiten de Git-repo** worden gebruikt:

~~~powershell
$store = "fpa9hu-i3.myshopify.com"
shopify theme list --store $store
$dir = Join-Path $env:TEMP "BadkamerCity-Live-Audit"
New-Item -ItemType Directory -Force $dir | Out-Null
shopify theme pull --store $store --theme 194864677130 --path $dir --nodelete
~~~

Check vóór dit commando of dit ID nog MAIN is. `--nodelete` is geen reden om de echte werkmap te gebruiken: maak een aparte map en vergelijk de zeven theme-mappen.

### 12.3 Hoe merk je wat werkelijk gewijzigd is?

- `git status --porcelain=v1`: niet-gecommitte wijzigingen lokaal.
- `git log -1 --oneline`: lokale tip.
- `git rev-parse HEAD`: exacte lokale commit.
- `git ls-remote origin refs/heads/main`: remote tip.
- `shopify theme list`: huidige live theme rol.
- `docs/BASELINE_MANIFEST_2026-10-07.json`: oude verifieerbare Shopify-codebasis met 441 bestanden en MD5.
- Voor Shopify Admin-collectieteksten, menu's, producten en metafields moet je **apart** vergelijken.

## 13. Review- en regressiechecklist

| Scope | Controle |
| --- | --- |
| Git | juiste map/origin/main, local-remote tip, lege `git status`, geen secrets |
| Homepage | hero, 8 categorietiles, productselectie, stijlkaarten, merkenstrip, help CTA |
| Header/footer | desktop/mobile menu, search, cart badge, links, toetsenbordfocus, overlays |
| Badkamermeubels desktop | kortere hero, H2 “Kies een categorie”, 6 kaarten, CTA/hover, advies |
| Badkamermeubels mobiel | compacte direct zichtbare lijst, weinig scrollen, goedgekeurde opmaak |
| Responsiviteit | 320, 375, 390, 430, 768, 1024, 1440, 1920 px en landscape |
| Algemene categorieën | correcte breadcrumb, categories, alfabetische links, `[SPLIT]` |
| Listing | 0 producten, filter, sorteer, paginering, native fallback |
| Filterproef | `wastafelkranen?bcfilters=1`, VPS health, CORS, API error en herstel |
| PDP | media, thumbnails, prijzen, voorraadlabels, switcher, SKU, sticky/cart |
| Sets/accessoires | exact SKU en juiste status, prijs uit Shopify; testproduct gescheiden |
| SEO | 1 H1, logische headings, meta/canonical, JSON-LD en interne links |
| Performance | WebPageTest/Lighthouse én velddata LCP, CLS, INP, bandbreedte mobiele afbeeldingen |
| Accessibility | screenreader labels, alt, keyboard, drawer en details, touch targets |
| Checkout | testcart en werkelijke betaal-/verzend-/belastinginstellingen |

Geen “alles groen” claim zonder gedateerde, reproduceerbare checks en concrete URLs/browserresultaten.

## 14. Belangrijkste bekende risico's en open eindjes

1. **Technische CSS staat deels in Shopify-collectieomschrijving:** snapshot opgeslagen, maar deze drie overrides blijven een externe dependency tot ze bewust zijn gemigreerd.
2. **Externe filters zijn opt-in**, niet live sitebreed; backend, paginering en error fallback zijn niet end-to-end bewezen.
3. **Grote switcher JSON:** inhoud bij snapshot geverifieerd, maar performance op mobiel nog te meten.
4. **Lege subcategorieën:** enkele navigatiekaarten kunnen niet klikbaar zijn tot echte producten en publicatie aanwezig zijn; maak geen lege landings.
5. **Data-onvolledigheid:** importstatus varieert per merk; Shopify Admin en bronbestanden leidend.
6. **Theme backup-/pilotbestanden zitten ook in live:** niet blind verwijderen om de repo visueel “op te schonen”.
7. **Historische documentatie bevat verouderde theme-ID's/staten:** lees deze als auditverleden, niet als actuele productie-instructie.
8. **Theme Check-/browserchecks van eerdere maanden zijn geen tests van deze nieuwe baseline.**
9. **SEO-schema kan overlappen** met andere apps; controleer gerenderde DOM/structured-data.
10. **Repository is publiek**: nooit .env, API-secrets, klantgegevens, orders of private bestanden committen.

## 15. Wat een nieuwe AI als eerste moet doen

1. Lees dit document, `AGENTS.md` en `docs/BASELINE_MANIFEST_2026-10-07.json`.
2. Vraag actuele Shopify `MAIN`-rol en thema-update op; controleer de werkelijke branch en `git status` lokaal.
3. Zoek `templates/{page}.json` → `sections/...` → `snippets/...` → `assets/...` en de bijbehorende Shopify Admin-bronnen.
4. Bepaal expliciet: **bewezen**, **historisch**, **niet getest**.
5. Vraag welke paginatypen/merkdata geraakt mogen worden; geen verzonnen productwaarden of serviceclaims.
6. Maak alleen geïsoleerde veranderingen op ongepubliceerde preview; test, commit, documenteer en laat gebruiker publiceren.
7. Nooit een extern filter/VPS-verzoek als automatisch opgelost markeren puur omdat de frontend bestaat.
8. Na nieuwe goedgekeurde release: nieuw manifest, vernieuwde snapshot, nieuw live thema-ID en beknopte changelog.

### Kopieerbare startprompt voor de volgende AI

~~~text
Je werkt aan BadkamerCity, Shopify Online Store 2.0, repository
https://github.com/jlamping1997/badkamercity. Lees eerst helemaal
docs/AI_HANDOFF_CURRENT.md, docs/BASELINE_MANIFEST_2026-10-07.json
en AGENTS.md. De gecertificeerde snapshot van 7 oktober 2026 is
Shopify fpa9hu-i3.myshopify.com met thema 194864677130
(BadkamerCity - SEO categoriehub). Controleer NU zelf welk thema MAIN is
en wat de Git-worktree status is. Werk niet blind met oude IDs uit docs.

Architectuur: Liquid/JSON templates, product PDP met V2 switcher via
assets/product-switcher-data.json, sets en accessoires op exact SKU,
collection.category-landing en collection.bc-meubelhub. Op de
Badkamermeubels hub zit cruciale mobiele/desktop CSS deels in de
Shopify-collectieomschrijving (snapshot docs/shopify-admin/).
Externe filters zijn alleen opt-in bij wastafelkranen?bcfilters=1,
met een aparte VPS-backend; niet sitebreed klaar verklaren.

Behoud goedgekeurde responsive UX en werk alleen in een veilige,
ongepubliceerde preview. Geen destructieve Git-acties, geen ongecontroleerde
live-push/publicatie en geen verzonnen leveranciers- of voorraaddata.
Stel eerst een controleerbaar wijzigings- en testplan op.
~~~

## 16. Bestandswijzer en historiek

**Actuele documenten:**
- `docs/BASELINE_MANIFEST_2026-10-07.json` — alle 441 bestanden met Shopify-MD5, grootte en contenttype.
- `docs/shopify-admin/collection-badkamermeubels-2026-10-07.json` — collectie-ID, suffix, SEO, beschrijvingsstatus.
- `docs/shopify-admin/collection-badkamermeubels-description-2026-10-07.html` — read-only volledige Admin-beschrijving inclusief `[SPLIT]` en 3 inline CSS-overrides.
- `scripts/git-align-worktree.ps1` — veilige controle van lokale Git-state.
- `README.md` — startpagina van repo.
- `AGENTS.md` — Codex-/veiligheidsregels; **lees actuele bovenste aanvulling vóór historische regels**.

**Historische (gedateerde) achtergrond:**
- `docs/MASTERPLAN.md` — oorspronkelijke projectsturing en beslis-/taakregister, niet automatisch actuele live-status.
- `docs/PRODUCT_DATA_CONTRACT.md` — logische, brononafhankelijke veldmatrix; geen garantie op actuele Shopify metafieldmapping.
- `docs/HANDOFF_2026-10-05.md` — eerdere werkstationsessie.
- `docs/SHOPIFY_ENVIRONMENT.md` en `docs/LIVE_THEME_COMPARISON.md` — oude themastanden.
- `docs/TECHNICAL_CHANGE_WORKFLOW.md`, `docs/CODEX_EXECUTION_LOG_PROTOCOL.md` en `docs/TEST_EVIDENCE_STANDARD.md` — ontwikkel-/bewijsmethodiek.

---

**Status:** uitvoerige technische documentatie van de Shopify-code en bekende admin-afhankelijkheden per 2026-10-07. De feitelijke storefront, externe systemen en winkeldata kunnen daarna wijzigen; verifieer die altijd opnieuw.
