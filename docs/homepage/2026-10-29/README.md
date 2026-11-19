# HOME-01 — homepage met acties, negen categorieën en advies op afspraak

29 oktober 2026. Opdracht en ontwerp goedgekeurd in de huidige conversatie. Implementatie via Shopify- en GitHub-connectors, zonder Windows-toegang.

## Bron en releasegrens

- Actieve branch: `fix/product-cards-2026-10-14`; start `83b6ab9ab9a5adf22150232920cb88cf42af0974`.
- Werkelijk MAIN: `195876815114`, BadkamerCity - Compact mobiel zoeken.
- Nieuw concept: `195910795530`, BadkamerCity - Homepage rondjes en acties, UNPUBLISHED.
- Voltooide duplicatie vóór de eerste filewrite: 1.318/1.318 bestandschecksums gelijk. De tussentijdse processing-stand was expliciet niet vrijgegeven.
- Alleen het concept gewijzigd. Geen publicatie, product-, prijs-, voorraad-, checkout- of verzendinstelling veranderd.
- De Git-root is geen complete actuele Shopify-snapshot. Deploy alleen de in `deployment-manifest.json` genoemde bestanden bovenop de geverifieerde live-kopie, nooit blind deze gehele repository.

## Implementatie en onderhoud

`templates/index.json` → `sections/bc-homepage.liquid` → `snippets/bc-home-image.liquid`, `assets/bc-homepage.css`, `assets/bc-homepage.js` en 13 WebP-bestanden. Bestaande homepageconfiguratie bewaard als disabled secties. Header, predictive search, cart en cataloguscontrollers niet herschreven.

Twee volledige bannerlinks, negen afzonderlijke categoriecirkelblokken, vier merklinks, inspiratie naar de werkelijk bestaande tegelcollectie, adviesaanvraag, afhalen en retourinformatie. Geen fictieve aanbiedingenroute, korting, prijs, voorraad of volgende-dagbelofte. Actiebanners zijn configureerbaar, maar linken initieel eerlijk naar Kranen en Badkamermeubels.

Thema-editor → Homepage → **Homepage acties & rondjes**. Bannerfoto/bovenkop/titel/knoptekst/bestemming, categoriecollectie/foto/titel, merklogo/link en adviesinhoud zijn instelbaar. Een gekozen image-picker vervangt het meegeleverde themafallbackbeeld. Negen cirkels op mobiel als 3×3; vanaf750px negen naast elkaar. `Bekijk alle categorieën` behoudt toegang tot de volledige categorieboom.

| Label | Werkelijk doel |
| --- | --- |
| Kranen | /collections/kranen |
| Douche | /collections/douches |
| Badkamermeubels | /collections/badkamermeubels |
| Tegels | /collections/tegels |
| Toiletten | /collections/toiletten |
| Spiegels | /collections/badkamerspiegels |
| Wastafels | /collections/wastafels |
| Baden | /collections/baden |
| Accessoires | /collections/accessoires |

Footer: `sections/footer.liquid` rendert alleen bij homepage + `compact_homepage` het nieuwe `bc-home-footer`-snippet. Andere pagina's behouden hun bestaande footer. De checkbox staat in `sections/footer-group.json`. Stabiele homepageankers verbinden footer, USP en service-details. Native details/summary werkt ook zonder extra dialogcontroller.

## 3D-afspraak: expliciete werking

Geen bestaande boekingsagenda of Cal.com-URL aangetroffen in het actuele thema of de relevante gepubliceerde pagina's. De primaire knop is daarom **Vraag een 3D-afspraak aan**. Deze opent een Shopify-contactformulier met naam, e-mail, optioneel telefoon/voorkeursmoment en wensen. POST-route `/contact`, verborgen onderwerp 3D-afspraak, vereiste velden en zichtbare melding dat de afspraak pas na bevestiging vaststaat.

Een echte boekingslink kan later in de homepage-instelling `booking_link` worden gezet; dan vervangt die de aanvraagroute en wordt de knop **Plan een 3D-afspraak**. Er is geen beschikbaarheidsagenda verzonnen. Ontvangst/verzending van een echte aanvraag is NOT_TESTED: er is geen testbericht verstuurd.

## Beeldbron en performance

13 illustratieve categorie-/sfeerbeelden gemaakt met de ingebouwde imagegen-functie, gebaseerd op het gekozen ontwerp: negen afzonderlijke centraal gefotografeerde producten in een rustige badkameromgeving; twee brede kraan/meubelbeelden; één groene tegelbadkamer; één gedrukt 3D-ontwerp met materiaalstalen. Geen exacte merk-/productidentiteit of echte showroomfoto geclaimd. Alleen fotografie, zonder ingebakken tekst of knoppen.

Beeldbrief: realistische Nederlandse badkamers, natuurlijk daglicht, warm hout/licht steen, één herkenbaar hoofdproduct per categoriefoto, geen collages, tekst, watermerk of logo. De inspiratie gebruikt saliegroene tegels. Productiefoto's zijn technisch verkleind en als WebP geoptimaliseerd; de oorspronkelijke gegenereerde beelden blijven afzonderlijk bestaan. Negen categoriefoto's samen200.356 bytes; alle13 assets samen512.650 bytes. Eerste campagne eager/high, overige beelden lazy; dimensies gereserveerd. Geen nieuwe storefront-runtimebibliotheek toegevoegd. Geen Lighthouse- of conversieclaim.

## Verificatie

- **PASS statisch:** Shopify Liquid/JSON/theme-check op alle10 gewijzigde tekst-/runtimebestanden, revisie3. De check draait op een runtime-only QA-boom: historische documentatie bevat eigen `en.default.json`-snapshots die anders onterechte locale-errors veroorzaken. De ongewijzigde live `home-sunshower`-dependency is alleen voor de QA-boom toegevoegd. JS-syntaxis en negen unieke categorieën/beeldbestanden gecontroleerd.
- **PASS echte desktopbrowser1363×936:** alle negen categorielinks afzonderlijk geopend, juiste URL/zichtbare categorie bevestigd; vier vendorlinks afzonderlijk geopend met juiste heading; zoekopdracht Hotbath bereikt zoekresultaten; bestaande cartlink bereikt lege winkelwagen. Geen cartwrite/checkout/order.
- **PASS echte preview:** alle13 homepagebeelden laden, compacte footer aanwezig, geen ontbrekende interne ankers; aanvraagknop opent formulier, afhaal-/retourdetails openen. Formulieractie, verplichte velden en e-mailtype gecontroleerd. Geen formulier verzonden.
- **PASS begrensde responsive componentcontrole:** exact gerenderde homepagecomponent met eigen CSS in srcdoc-fixtures op320,390 en1024CSS-pixels; negen cirkels, drie kolommen op320/390, negen op1024, documentbreedte gelijk aan viewportbreedte, geen uitlopende componentelementen. Dit is geen native telefoon- of volledige mobiele header-/touchtest.
- **BLOCKED live iframe:** Shopify-weergave weigert rechtstreekse iframe-insluiting; de srcdoc-fixture is uitdrukkelijk een componentcontrole, geen claim van native mobiele storefrontvrijgave.
- **NOT_TESTED:** echte afspraakmail/ontvangst, native telefoon Safari/touch, volledige gevulde cart-/koopflow, Lighthouse, werkelijke verzendtariefgrens. De USP boven€100 is expliciet door de eigenaar opgegeven; checkouttarieven niet gewijzigd.

## Uitvoer en opruimen

Shopify verwerkt sectieschema's en JSON-configuratie sequentieel: na het schrijven van de nieuwe sectie/footerschema zijn index.json en footer-group.json nogmaals geschreven. De eerste gedeeltelijke upsert is niet als volledig succes behandeld. Shopify normaliseert JSON en vult defaults in; Liquid/CSS/JS en assets worden exact teruggelezen, configuratie ook semantisch gecontroleerd.

De tijdelijke testtemplate `index.bc-homepage-review.liquid` kon niet via de connector worden verwijderd: `themeFilesDelete` werd als destructief geblokkeerd. Daarom is de inhoud vervangen door een inerte noindex-pagina 'Controle afgerond' met één link terug naar de homepage. Geen fixtures, scripts of tests blijven op die route actief. Deze veilige opruimtemplate staat bewust in het deploymentmanifest.

## Terugzetten en volgende handeling

De huidige MAIN195876815114 is niet veranderd en blijft de terugval. Niet publiceren vanuit deze uitvoering. Voor terugzetten van alleen het concept: nieuwe homepage-sectie uit, bewaarde oude secties weer aan volgens `previous-work-status.md`/oorspronkelijke opbouw, en de compacte-homepagefootercheckbox uit; of opnieuw een verse MAIN-kopie maken. Geen andere concepten of catalogusdata verwijderen.

**Exact één volgende handeling:** eigenaar opent het concept op zijn telefoon, beoordeelt de homepage en test één echte afspraakaanvraag inclusief ontvangst vóór publicatie.
