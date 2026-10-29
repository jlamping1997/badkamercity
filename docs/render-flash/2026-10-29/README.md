# FLASH-01 — stabiel eerste laadmoment

29 oktober 2026. Eigenaar meldt kort een grote blauwe pijl tijdens navigeren en een hoog blauw vlak bij de zoekbalk bij opstarten. Op expliciete opdracht wordt de laadvolgorde hersteld. De precieze oorspronkelijke flits is nog niet op zijn iPhone opgenomen; houd reproduceerbare risico's en het incidentele eigenaarsbeeld gescheiden.

## Actuele bronnen en scope

Verse Shopify-read: menuconcept 195913482506 is inmiddels MAIN, gepubliceerd door eigenaar. Nieuw concept 195915448586 **BadkamerCity - Stabiele header en iconen** is een volledig gecontroleerde kopie van deze MAIN. Actieve branch `fix/product-cards-2026-10-14`; startcheckpoint 0b43825409828d583f5e709eed8e1ce892937fd6. Main alleen documentatie. Lokale checkout vóór werk schoon; geen Windowsmeting.

Status: **PREVIEW_READY / CONTROLLED_STARTUP_COMPARISON_PASSED / SEARCH_AND_NAVIGATION_PASSED / IPHONE_NOT_TESTED / NOT_PUBLISHED**. Vóór writes alle 1.337 bestanden checksumgelijk; na afloop alleen drie gewijzigde bestaande bestanden en één nieuw snippet. Alle vier exact teruggelezen. MAIN opnieuw volledig vergeleken: 1.337 bestanden ongewijzigd. De tijdelijke QA-view is exact hersteld.

Codecheckpoint **901ebfdd35400233da1337c1f1e9822739ff60cc**; documentatiecheckpoint **692220a76078a5a8c57bce33d33ea2b109f04b6c**. Latere afrondingscommit bevat alleen documentatie/bewijs.

## Gevonden oorzaken en oplossing

1. `component-search.css` stond in de body/header als media=print/onload; predictive-search CSS stond ook asynchroon. De gesloten suggestiecontainer en de aangepaste loader krijgen pas in dat laatste bestand display:none/afmetingen. `loading-spinner` vervangt bij een opgegeven class de standaard hidden-klasse. Zonder de component-CSS kan die lege laadcontainer dus de header vergroten.
2. `icon-arrow.svg` had alleen viewBox, geen intrinsieke width/height. De normale maat hing volledig van CSS af. Het is een aantoonbaar risico op een groot standaard SVG-vlak als die stijl ontbreekt, niet het bewijs dat exact dit icoon de gemelde iPhone-flits veroorzaakte.

`layout/theme.liquid` laadt beide zoekstyles nu synchroon in de head, in dezelfde cascadevolgorde na base.css. De dubbele component-search-aanvraag uit header.liquid vervalt. Een klein inline `bc-first-paint` snippet staat vóór content_for_header: minimale SVG-wrapper-/pijl-/spinnermaten en een guard die gesloten suggesties verbergt. Open/loading-staten blijven door de bestaande zoekcontroller bestuurd. De pijl krijgt daarnaast width 14/height 10 in het SVG zelf; CSS height:auto bewaart zijn verhouding bij schalen.

Geen sitebrede verberglaag, kunstmatige wachttimer of wijziging van de zoekcontroller. Menugedrag/homepage/checkout blijven zoals gepubliceerd. Geen algemene snelheid-/Lighthouseclaim.

## Git en deployment

Vier bestanden uploaden, zie deployment-manifest.json. De huidige layout uit Shopify bevatte eerdere live-wijzigingen die nog niet in de Git-root stonden (o.a. typografie/wishlist): die zijn behouden. Drie ongewijzigde live-afhankelijkheden zijn ook in Git en de lokale validatieboom opgenomen, maar horen niet bij de Shopify-upload. De runtimekopie is geen volledige product-/Admin-export.

De bestaande bronbestanden staan met LF-genormaliseerde regeleinden als baseline-*.txt in dit dossier. Originele Shopify-checksums staan in het manifest. Terugzetten: herstel de drie oorspronkelijke bestanden; het nieuwe snippet kan ongebruikt blijven. Nooit de volledige Git-root uploaden.

## Uitgevoerde controle

ThemeCheck R2: vier bestanden zonder errors; bestaande waarschuwing over scheme_classes in de overgenomen layout blijft zichtbaar. R1 vond drie bestaande live-afhankelijkheden die in de onvolledige lokale runtimekopie ontbraken; ze zijn uit MAIN gelezen voor R2. De tijdelijke noindex QA-view rendert de nieuwe Shopify-header in echte srcdoc-frames. Voor de oude starttoestand zijn de zoekstyles bewust weggelaten; rechts staan de nieuwe volledige starttoestand op 390px en de minimale inline guard zonder zoekstyles op 320px. Dit is een gecontroleerde componentvergelijking, geen opname van een echte vertraagde iPhone-netwerkverbinding.

Meetresultaten in `startup-metrics.json` en screenshot `startup-comparison.jpg`:

- Zonder zoekstyles/guard: header 494,66px hoog, suggestievlak 357px hoog en horizontale overloop (431px inhoud op 375px beschikbare breedte door scrollbar). Dit reproduceert het gemelde hoge blauwe vlak met een onbegrensde spinner.
- Nieuwe volledige starttoestand 390px: header 137,66px hoog, gesloten suggesties 0px/display:none en geen overloop. De losse inline guard op 320px verbergt de gesloten suggesties ook zonder de zoekstyles; header 131px hoog, geen overloop.
- Oude losse pijl zonder enige externe CSS: circa 359×256px en blauw als browserlink. Nieuwe identieke pijl met intrinsieke maten: 14×10px. Dit reproduceert het blauwe-pijl-effect onder de gecontroleerde ontbrekende-CSS-conditie; de oorspronkelijke incidentele iPhone-opname ontbreekt nog.

De gewone concept-homepage is daarnaast werkelijk geopend. Beide zoekstyles staan éénmaal in HEAD, media=all, zonder onload. De nieuwe inline guard is aanwezig. Volledig geladen desktopmeting vóór/na is exact gelijk: header 112,59375px, zoekveld 485×48px, knop 58×48px. Gesloten suggesties 0px. Hotbath-suggesties openen, Escape sluit; een opnieuw ingevulde zoekopdracht met de zoekknop opent de echte resultatenpagina met h1 ‘Zoekresultaten voor Hotbath’. Daarna via de headerlink naar Kranen en via het logo terug naar de homepage: juiste pagina's, stabiele headerhoogte en nul grote headericonen. De test heeft geen bestelling, cartmutatie, e-mail of checkoutactie gedaan.

`startup-fixture.liquid.txt` bewaart de reproduceerbare QA-bron, die alleen tijdelijk op het concept stond. De oorspronkelijke inerte QA-template is exact teruggezet (checksum in theme-verification.json). Geen actieve testpagina/controller achtergelaten.

**NOT_TESTED:** fysieke iPhone/Safari, netwerkfilmstrip met echte vertraagde assets, volledige catalogus-/PDP-/checkoutregressie, Lighthouse/FCP/LCP/CLS. Geen algemene performanceclaim. De oorspronkelijke incidentele flits op de fysieke telefoon moet door de eigenaar nog worden gecontroleerd.

## Exact volgende handeling

Eigenaar opent concept **BadkamerCity - Stabiele header en iconen** op zijn iPhone, herlaadt de homepage en wisselt tussen homepage, categorie en product. Controleer ook één zoekopdracht; na akkoord publiceert de eigenaar. Deze sessie heeft niet gepubliceerd.
