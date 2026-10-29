# ASSORT-01 — assortimentoverzicht

29 oktober 2026. Eigenaar heeft het desktop- en mobiele ontwerp goedgekeurd en opdracht gegeven het werkend uit te voeren op `/collections`.

## Stand

**PREVIEW_READY / VERIFIED_THEME / NOT_PUBLISHED.** Uitvoering afgerond; eigenaar beoordeelt en publiceert het concept. Review op een echte telefoon blijft open.

MAIN bij eindcontrole: **195915448586 — BadkamerCity - Stabiele header en iconen**, alle 1.338 bestanden ongewijzigd. Concept **195916628234 — BadkamerCity - Assortiment overzicht**, UNPUBLISHED, processing=false. Actieve branch `fix/product-cards-2026-10-14`; eerste remote codecheckpoint `f8ba3e68760a4406ee2a30a92fb98400873c2d5b`, definitieve verfijning en bewijs in de daaropvolgende ASSORT-01-commit. Deze ronde volgde op FLASH-01. Geen Windowscontrole of publicatie uitgevoerd.

Open in Shopify het genoemde concept en bekijk `/collections`. De bezochte previewingang was `https://badkamercity.nl/collections?preview_theme_id=195916628234`; Shopify verwijdert de parameter tijdens de previewsessie. De previewbalk bevestigde de juiste conceptnaam. De Copy link-knop leverde in deze browser geen clipboardtekst op; geen tijdelijke deel-URL verzonnen.

## Uitvoering

- Alleen standaard `/collections` vervangen; gewone categoriepagina's, merkenview en productpagina's behouden hun eigen templates.
- Tien hoofdafdelingen uit het actuele hoofdmenu. De bestaande negen illustratieve homepagefoto's hergebruikt; radiatorbeeld uit de bestaande collectie geoptimaliseerd. Afbeeldingen/titels per afdeling zijn via de editor te vervangen.
- Native links en details voor alle onderliggende menukeuzes. Op desktop als kolommen, op mobiel uitklapbaar. Essentiële links blijven zonder JavaScript bereikbaar.
- Aanvullende categorieën afzonderlijk onder Maak het compleet, configureerbaar met expliciete handles; geen wijziging van het hoofdmenu of collectie-/productlidmaatschappen.
- Meer categorieën toont gevulde collecties die niet al in de menustructuur staan. Paginering is voorzien voor groei boven 250 collecties. Dit is geen automatische uitbreiding van het hoofdmenu.
- Categoriezoeker filtert plaatselijk de zichtbare directory, ondersteunt onderliggende context en herstelt uitklapstaat na wissen; geen externe requests of analytics toegevoegd. De input verschijnt pas na controllerinitialisatie.
- Sunshower gebruikt de bestaande gepubliceerde merklanding en bestaande IR-illustratie. Porcelanosa linkt naar het bestaande merkassortiment; de hoogwaardige merkpagina blijft een apart toekomstproject.
- Porcelanosa-sfeerbeeld uit de Bottega-galerij van product 10687508807946, geverifieerd via actuele mediaread. Een algemene merk-/seriesfeerfoto, geen claim van een exacte kleur of set. Bron: https://cdn.shopify.com/s/files/1/0941/7959/0410/files/porcelanosa-kogros-ddc1308f5ff966874f46.jpg?v=1793208373 .
- Titel en metaomschrijving alleen op de standaard list-collections-route aangepast, met vertalingen. Bestaande canonicals/robots behouden; geen SEO-rankingsclaim.

## Bestanden en behoud

Nieuwe sectie bc-assortment, snippet bc-assortment-item en eigen CSS/JS. Template list-collections.json wijst de sectie toe. Twee extra WebP-assets. Locale-uitbreiding uitsluitend bc_assortment. Layout krijgt uitsluitend een routegebonden metadata-override. Actuele baselinebestanden en openbare menuboom staan naast dit document; geen klantgegevens.

build-config.py bouwt template en vertalingen vanuit de vastgelegde baseline; dit is geen importtool voor catalogusdata. Bij hergebruik eerst een verse baseline vastleggen, anders kan een latere vertaling verloren gaan.

## Controle en bewijs

- Vóór writes: alle 1.338 conceptbestanden checksum-identiek aan de verse MAIN-nulmeting. Na afloop: 1.344 conceptbestanden; exact de tien bedoelde nieuwe/gewijzigde paden, overige 1.334 gelijk; geen ontbrekende bestanden. MAIN blijft 1.338/1.338 gelijk. Zie [deployment-verification.json](deployment-verification.json) en [main-before.json](main-before.json).
- Acht tekstbestanden teruggelezen: Liquid/CSS/JS exact; Shopify-normalisatie bij JSON semantisch gelijk. Beide WebP-bestanden MD5-exact. Zie [source-readback-checks.json](source-readback-checks.json). Geen Admin-menu-/product-/collectiemutaties.
- ThemeCheck R8 geslaagd voor acht gewijzigde code-/configbestanden, met alleen de al bestaande `scheme_classes`-waarschuwing in de layout. [Resultaat](themecheck-r8.json). De controlemap bevat alleen themebestanden; R7 vanaf de volledige repository vond tevens de historische baseline-locale en gaf daardoor onterechte ontbrekende vertalingen. R8 gebruikte een verse kopie van alle actuele gewijzigde paden en de echte themadependencies. De nieuwe localegroep is ook op Shopify zichtbaar.
- Twintig lokale LiquidJS/DOM-cases geslaagd: tien kaarten, native links, enkelvoud/alias/onderliggende context, Enter, geen resultaten, Escape, responsieve staat en scheiding van aanvullende links. [Cases](controller-tests.json), [testscript](test-directory.cjs), [versies](package.json). Fixture, geen vervanging voor Shopify-runtime.
- Echte desktoppreview: tien kaarten, twaalf geladen beelden, één H1, juiste metadatatitel, geen horizontale overloop/Liquid-fout. Alle tien hoofdlinks en beide merklinks geklikt. [Hoofdlinks](link-checks.json), [merklinks](promo-checks.json). Bestaande Sunshower- en meubelhub gaven bij het directe uitleesmoment geen H1; geen algemene SEO-vrijgave van die pagina's.
- Zoekactie `inbouw wastafel` toont de passende bovenliggende/onderliggende categorieën; onbekende zoekterm geeft de melding en herstelknop. Werkelijke mobiele componenttest: Wastafels openen, zoeken op `wastafelkraan`, Escape en herstel van de eerder geopende afdeling geslaagd.
- Responsieve componentframes in echte Shopify-HTTPS-preview: 320, 390 en 1024px (effectieve contentbreedte 305/375/1009 wegens iframe-scrollbalk). Twee/twee/drie kolommen; nul titeloverloop, geen documentoverloop, alle twaalf beelden geladen. [Metingen](responsive-metrics.json). Desktoppreview vijf kolommen bij 1348px documentbreedte. Dit zijn componenttests, geen volledige mobiele header/footer of native Safari-/telefoontest.
- Tijdelijke bestaande QA-template na controle exact teruggezet: `templates/index.bc-homepage-review.liquid`, MD5 `c76529d094fb4d534f9cd3352c63f4b4`. De testweergave is afgesloten.
- [Desktop bovenkant](desktop-overview.jpg), [volledige desktop](desktop-preview.jpg), [mobiele componentframes](mobile-component-preview.jpg). De laatste afbeelding toont de QA-frames naast elkaar, geen echt telefoonscreenshot.

Geen Lighthouse-/Core Web Vitals-, indexering-/ranking-, conversie-, volledige cataloguslink-, betaal- of fysieke telefoontest geclaimd. De zoekfunctie filtert de gerenderde categorieën van de huidige pagina; boven 250 collecties kan de extra directory meer pagina's hebben. Hoofdmenu blijft leidend.

## Logica voor uitbreiding

Het bestaande [categorisatiecontract](../../CATEGORIZATION_AND_SEO_POLICY.md) blijft leidend. Een nieuwe productsoort hoort bij een bestaande hoofdafdeling; een nieuw merk maakt niet automatisch een afdeling. Voeg nieuwe categorieën na productdekking-/overlapcontrole aan het ingestelde hoofdmenu toe. De directory volgt die boom automatisch. Een gevulde collectie buiten de boom verschijnt onder Meer categorieën; beoordeel haar plaats voordat ze als hoofdroute wordt gepromoveerd.

De bovenste kaarten gebruiken de rootbestemmingen van het menu, met een editorblok per collectiehandle voor afbeelding, desktoptitel en korte mobiele titel. Nieuwe of gewijzigde rootafdelingen vragen een afbeelding en controle van alle breakpoints. Aanvullende categoriehandles per afdeling blijven onder Maak het compleet: bijvoorbeeld Wastafelkranen bij Wastafels. De productcategorie zelf blijft dezelfde bestaande bestemming onder Kranen.

Een merk-/serie-/SEO-landingspagina krijgt pas een eigen route na onderzoek naar zoekintentie, assortiment, unieke inhoud en overlap. De twee promotieblokken zijn in de editor te wijzigen en linken nu naar bestaande bestemmingen. Geen nieuwe dunne SEO-pagina's automatisch genereren.

## Eerste gecontroleerde bestemmingen

De echte Porcelanosa-vendorpagina geopend: heading Porcelanosa en 337 producten. Er staat bestaande verkeerde kranenadviescontent onder die productlijst; vastgelegd als afzonderlijk vervolgonderzoek, niet aangepast binnen deze overzichtspagina.

## Terugzetten en vervolg

Voor review alleen de nieuwe conceptkopie gebruiken. Herstel template, layout en beide locales uit baseline om de functie uit te schakelen; nieuwe ongebruikte bestanden hoeven niet verwijderd. Geen volledige Git-root uploaden.
Exact volgende handeling: eigenaar beoordeelt dit concept op een echte telefoon en desktop en publiceert het via Shopify wanneer akkoord. Daarna MAIN opnieuw verifiëren. Publicatie is volgens AGENTS.md de merchantstap.
