## 48 Leesroutes en dagelijkse beheertaken

Dit deel maakt de technische registers bruikbaar voor het dagelijkse werk. Begin bij de handeling die je wilt uitvoeren. Een onderwerp dat in meerdere pagina’s voorkomt heeft één hoofdcontract; de andere hoofdstukken verwijzen naar de relevante uitzondering. Daardoor hoeft bijvoorbeeld het verschil tussen een variant en een ander product niet opnieuw te worden bedacht voor een tegelstaal, productkaart of verlanglijst.

| Lezer | Begin hier | Daarna | Wanneer klaar |
| --- | --- | --- | --- |
| Winkeleigenaar | Actuele publicatiekaart, hoofdstuk 49 | Header, categorieën, footer, retouren: 52–55 en 68–70 | Juiste live-/conceptstand vastgesteld en de klanttaak op de bedoelde route gecontroleerd |
| Klantenservice | Klantreizen, hoofdstuk 50 | Retourbehandeling 70; zoeken 56; bestellen 66 | Aanvraag of vraag heeft een eigenaar en een vastgelegde volgende stap |
| Contentbeheerder | Homepage en collecties, 57–58 | Redactie 72; gegevens 73; SEO 74 | Inhoud, bestemming, template en publicatie passen bij elkaar |
| Productbeheerder | Productidentiteit, hoofdstuk 61 | Tegels 62; merkdata 63; onderdelen 64 | De verkochte uitvoering, prijs, foto en koopactie horen bij hetzelfde artikel |
| Ontwikkelaar | Bronprioriteit 49 | Componentcontract, diagnose 77, regressie 78, release 79 | Wijziging herleidbaar, passend getest en veilig overdraagbaar |

Een klantmelding begint met URL, apparaat, schermbreedte indien bekend, handeling en verwacht/werkelijk resultaat. Vraag geen order- of persoonsgegevens om een puur visueel probleem te reproduceren. Voor ordergerelateerde service gebruikt de medewerker de eigen bevoegde omgeving; zulke gegevens horen niet in dit openbare naslagwerk of Git.

De onderstaande takenkaart is ook als zoekbare takenzoeker voorin het HTML-bestand opgenomen. De kaart geeft aan wie de taak behandelt, waar de bron staat en welke controle nodig is. Het is een werkroute; een vermelde controle is niet automatisch vandaag uitgevoerd.

<!-- TASK_TABLE -->

## 49 Actuele publicatiekaart en bronprioriteit

Peildatum van deze uitbreiding: 31 oktober 2026. De verse Shopify-lezing begon om 07:49 UTC, 08:49 in Nederland. De oudere registers vanaf hoofdstuk 30 blijven nulmetingen van 30 oktober; de productrouteregistratie is niet volledig opnieuw geëxporteerd. Gelijke aantallen bewijzen geen gelijke identiteit van alle records.

| Onderdeel | Verse stand | Betekenis voor beheer |
| --- | --- | --- |
| MAIN | 195948839178, BadkamerCity - Retourknop in header | Dit thema serveert de onderzochte openbare pagina’s |
| Laptopconcept | 195947036938, BadkamerCity - Categorieen zonder schuiven, UNPUBLISHED | NAV-02 is beoordeelbaar in preview; de live rail blijft aanwezig |
| Offerteconcept | 195916628234, UNPUBLISHED | Afzonderlijk traject; geen bewijs dat de uploadroute klantactief is |
| Retour-Page | 166668894474, gepubliceerd, suffix retour-aanmelden | Page-publicatie en themapublicatie zijn afzonderlijke schakels |
| Catalogustellingen | 11.680 totaal, 11.679 ACTIVE, één DRAFT, 11.679 gepubliceerd | Exacte Admin-tellingen; geen voorraad- of koopbaarheidsbewijs |
| Content | 121 Pages, 119 gepubliceerd, twee verborgen; 226 collecties; negen menu’s | Verborgen offerte- en merken-Page niet verwarren met beschikbare templates of merkendirectory |
| Themapaden | 1.354 | Vier nieuwe paden en zes gewijzigde paden tegenover de nulmeting van 30 oktober |
| Relevante tekstbronnen | 409; 407 bytegelijk aan metadata | Twee uitzonderingen expliciet behouden, hieronder |

`config/settings_data.json` blijft een bronpariteitsuitzondering. De opgehaalde tekst verschilt van de metadatahash; er is geen onafhankelijke exacte bron waarmee die afwijking is gesloten. Bij `templates/page.retour-aanmelden.json` bevat de opgehaalde tekst een Shopify-commentaar waardoor de bytehash afwijkt. De eerdere retourcontrole toetste de semantische JSON afzonderlijk. Noem deze twee situaties niet samen een bewezen runtimefout, maar schrijf ook geen 409/409-bytepariteit op.

De nieuwe openbare steekproef bevat 18 GET-responses: 17 HTTP 200 en de bekende Hygrometer-404. Op de onderzochte HTML-pagina’s staan de MAIN-ID en retourlink; de twee scrollknoppen in de categorierail zijn nog aanwezig. Deze controle voert geen JavaScript, koopactie of mailverzending uit. Het bewijst daarom niet dat een dropdown beweegt, een mailbox ontvangt of een fysieke telefoon soepel scrollt.

Bronvolgorde bij verschil: recente opdracht en bevoegdheidsgrens → verse Admin-/bron-/runtimemeting voor hetzelfde object → actuele overdracht → gedateerd dossier. Gebruik een menu-editor om een menu-item te wijzigen, een Page om de Page te publiceren en een thema om presentatie aan te passen. Het omwisselen van een thema publiceert geen verborgen Page.

## 50 Klantreizen en overdracht tussen functies

| Klantdoel | Ingang en stappen | Overdracht | Kritisch controlepunt |
| --- | --- | --- | --- |
| Artikel vinden | Headerzoeker → suggestie of resultaten → product | Van zoekterm naar producthandle/variant | Suggestie en resultaat kunnen verschillende zoekbronnen gebruiken |
| Categorie ontdekken | Categoriebar/drawer → hub of collectie → productkaart | Van menulink naar toegewezen collectie-template | Een hub biedt navigatie; een productlijst biedt filters en koopselectie |
| Merk bekijken | Assortiment of Merken → merkcollectie → artikel | Directoryselectie naar echte collectie | `/collections?view=merken` is de directory; een verborgen Page met dezelfde naam is iets anders |
| Tegels bestellen | Tegel-PDP → oppervlakte/verlies → dozen → winkelwagen | Rekenuitkomst naar verkoopvariant en hoeveelheid | m²-presentatie en bestelbare dooshoeveelheid moeten overeenkomen |
| Uitvoering kiezen | Productkaart of PDP → kleur/variant/ander product | Identiteit wisselt soms naar een andere URL | Foto, URL, prijs en geselecteerde variant moeten samen veranderen |
| Bewaren | Hartje → verlanglijst → later opnieuw openen | Productidentiteit naar browseropslag | Bewaren is geen voorraadreservering of accountkoppeling |
| Retour aanmelden | Header/footer → retourpagina → aanvraag → medewerker | Native contactformulier naar handmatige service | Ontvangst en terugkoppeling zijn pas bewezen met mailboxcontrole |
| Offerte laten vergelijken | Voorbereide offerte-Page → externe uploader | Shopify naar afzonderlijke aanbieder | Klantactivatie blijft uit totdat de open ontvangst-/privacycontroles rond zijn |

Een goede foutmelding benoemt waar de keten stopt. “Zoeken werkt niet” wordt bijvoorbeeld: suggesties laden wel, maar de resultatenpagina blijft in laden staan. “Retourknop ontbreekt” wordt: desktop, live thema, Page verborgen of gepubliceerd, en wel of geen link in de response. Deze precisie voorkomt dat een presentatiefout met productdata of een mailprobleem met een themawijziging wordt geprobeerd op te lossen.

Onderzoek eerst één reproduceerbare route. Herhaal daarna alleen de relevante zusterroutes: homepage en PDP voor globale headeropmaak; beide footers voor serviceverwijzingen; native en externe lijst voor kaartgedrag. Een geslaagde homepagecontrole dekt geen Sunshower-configurator of retourmail.

## 51 Schermcontract per component

Schermbreedte betekent hier de CSS-viewport, niet de schermdiagonaal of fysieke pixels. Browserzoom, zijpanelen en venstergrootte veranderen de beschikbare ruimte. Een laptop van 1.920 fysieke pixels kan dus een veel smallere CSS-viewport hebben.

| Component | Tot 749px | 750–989px | 990–1359px | Vanaf 1360px |
| --- | --- | --- | --- | --- |
| Headerbediening | Mobiele bovenrij en drawer | Mobiele bovenrij en drawer | Desktopbediening | Desktopbediening |
| Zoekrij mobiel | 44px veld; eigen inklapgedrag | 48px veld; eigen inklapgedrag | Desktopzoeker | Desktopzoeker |
| Categorieën MAIN | Via mobiele drawer | Via mobiele drawer | Horizontale rail | Horizontale rail als ruimte tekortkomt |
| Categorieën NAV-02-concept | Bestaande drawer | Bestaande drawer | Twee rijen, 6+5 | Eén rij, wrap-vangnet |
| Filters | Drawer; shortcut onder extra voorwaarden | Drawer | Zijbalk | Zijbalk |
| Homepagebanners | Onder elkaar | Naast elkaar | Naast elkaar | Naast elkaar |
| Footer | Accordion bij grote footer | Open kolommen | Open kolommen | Open kolommen |

Controleer bij elke responsieve wijziging de grens zelf én beide kanten. Voor de header zijn 989 en 990 essentieel; voor NAV-02 ook 1359 en 1360. Een test op alleen 390 en 1920 mist de oorspronkelijke laptopfout. Tabellen, technische code en brede specificaties mogen lokaal kunnen scrollen; dat is een ander contract dan een horizontaal schuivende hoofdnavigatie.

Naast breedte horen lange labels, grotere tekst, een geopende drawer en een breedtewissel bij het scenario. Een mobiel geopend menu moet bij terugkeer naar desktop zijn scrolllock opruimen. Het verbergen van een knop met CSS mag geen onzichtbare focusbestemming achterlaten. De gedateerde NAV-02-tests dekken componentframes en specifieke browseracties; zij vormen geen fysieke laptop-/iPhonevrijgave.

## 52 Headerpositie, logo en vaste merkidentiteit

De oorspronkelijke melding liet een kleine logoverschuiving tussen homepage en productpagina zien. De homepage gebruikt een andere semantische wrapper dan vervolgpagina’s. Die wrappers moeten dezelfde afmetingen, uitlijning en ruimte in de mobiele bovenrij krijgen. Alleen de afbeelding een vaste breedte geven lost afwijkende wrappermarges of gridruimte niet op.

Het live HDR-01-contract gebruikt op mobiel een bovenrij van 64px en dezelfde logo-uitlijning over paginatypen. Hamburger, logo, verlanglijst en winkelwagen krijgen voorspelbare plaatsen. Het aantal in de winkelwagen mag de logokolom niet wegduwen. De retouropdracht voegt op desktop een aparte actie links van Verlanglijst toe; die desktopactie wordt tot en met 989px verborgen.

| Wijziging | Bron | Controle |
| --- | --- | --- |
| Logo en wrapper | `sections/header.liquid`, logo-instellingen | Homepage en PDP met dezelfde viewport en scrollpositie vergelijken |
| Mobiele hoogte/zoekrij | Header-CSS en `assets/bc-mobile-header.js` | Bovenrij blijft gelijk wanneer de zoekrij inklapt |
| Returnactie | Header en `snippets/bc-returns-url.liquid` | Echte bestemming, label op één regel, geen overlap met Verlanglijst |
| Menu-items | Gebruikt `main-menu` | Headeropmaak verandert geen menubestemmingen |

Een lege retour-URL wordt niet als een klikbare lege link gerenderd. Het zichtbaarheidssysteem kijkt naar de echte Page en de themarol. Kijk bij een ontbrekende knop daarom eerst naar viewport, Page-publicatie en actuele MAIN; voeg niet meteen een tweede knop toe. Toegankelijkheid blijft onderdeel van het contract: de homepagekop en logolinksemantiek mogen behouden blijven zonder visuele verschuiving.

Aanvaardingsproef: dezelfde CSS-breedte, bovenaan de pagina, menu gesloten; vergelijk linkerrand, bovenrand en visuele logomaat op home, categorie, PDP en retourpagina. Herhaal met winkelwagenbadge en open menu. Leg zowel de gebruikte bron als de afbeelding/metingen vast; een afbeelding op een ander zoomniveau is geen betrouwbare vergelijking.

## 53 Sticky zoekbalk: toestanden en overgangen

De mobiele header heeft een vaste bovenrij en een zoekrij die afhankelijk van de scrollrichting inklapt. Het doel is meer productruimte tijdens lezen, met zoeken snel terug wanneer de bezoeker bewust omhoog beweegt. De implementatie staat in `assets/bc-mobile-header.js`; de desktopinstelling `on-scroll-up` uit de headergroep is geen volledige beschrijving van dit mobiele gedrag.

| Toestand | Aanleiding | Verwacht gedrag |
| --- | --- | --- |
| Uitgebreid bovenaan | Binnen ongeveer 24px van de top | Zoekrij beschikbaar |
| Inklappen | Voldoende voorbij de header en circa 24px omlaag opgebouwd | Alleen de zoekrij verdwijnt; bovenrij blijft staan |
| Terug tonen | Circa 32px bewuste opwaartse beweging | Zoekrij keert terug zonder logo te verplaatsen |
| Vastgehouden | Zoekfocus, voorspellende resultaten, drawer of dialoog actief | Geen onverwacht inklappen tijdens bediening |
| Menu geopend | Body scrolllocked | Mobiele headerwrapper blijft bovenaan gepind |
| Desktop | Viewport vanaf 990px | Mobiele controller laat de desktopstaat over aan de desktopopbouw |

De code gebruikt scrollverwerking via requestAnimationFrame en hoogtebewaking via ResizeObserver. Het uitgebreide reserveringscontract is 138px onder 750px en 142px tot 989px; de compacte visuele header is 84px. Deze bronwaarden verklaren de implementatie. Meet bij een nieuwe wijziging de werkelijke bounding boxes; behandel de getallen niet als bewijs dat alle browsers identiek tekenen.

Een verborgen zoekrij krijgt ook de passende interactiestaat: inert/aria-hidden waar van toepassing, zodat toetsenbordfocus niet achter een verdwenen veld terechtkomt. Verminderde beweging wordt gerespecteerd. Test neartop, lange neerwaartse scroll, korte richtingsruis, bewuste opwaartse scroll, typen met open toetsenbord en menu openen na scroll. Geautomatiseerde componenttests en eerdere frames staan in het HDR-01-dossier; fysieke Safari-controle blijft afzonderlijk.

## 54 Categoriebar op laptop: live rail en concept zonder schuiven

De screenshotmelding is terecht gekoppeld aan de beschikbare viewport: elf hoofdingangen passen bij de oude lettergrootte en tussenruimte niet altijd op één regel. MAIN bevat nog de scrollrail met twee schuifknoppen. NAV-02 vervangt dat patroon in het bestaande conceptthema. Deze documentatieronde publiceert het concept niet.

| Detail | Live MAIN | NAV-02, UNPUBLISHED |
| --- | --- | --- |
| 990–1359px | Horizontaal schuiven mogelijk | Grid met zes en vijf ingangen; tweede rij gecentreerd |
| Vanaf 1360px | Rail met eventuele overflow | Eén flexrij; wrap als vangnet, maximale inhoudsbreedte 1600px |
| Bedieningspijlen | Aanwezig | Verwijderd uit markup en controller |
| Labels | Bestaande railregels | 14px in twee rijen, 15px in brede rij |
| Trefvlak | Bestaand | Minimaal 48px rijhoogte in de smalle desktopopbouw |
| Mobiel | Drawer | Bestaande drawer behouden |

Het hoofdbestand is `sections/header.liquid`. De voorgestelde wijziging raakt geen menu-identiteiten of collectiegegevens. Openen/sluiten van categoriepanelen houdt de bestaande vertragingen van 120/160ms, Escape-afhandeling en focuslogica. Het dropdownpaneel moet onder de volledige navigatie beginnen, ook wanneer er twee rijen zijn.

Het dossier bevat twaalf breedteframes van 390 tot 1920px, alle elf ingangen zichtbaar zonder horizontale overloop, toetsenbordnavigatie, tweede-rijpaneel en breedtewissel met open mobiel menu. Merken is als echte top-level websitebestemming geopend. Een geweigerde iframe-embedding is niet omzeild. Het QA-template is na de proef exact hersteld.

Na eigenaarsbeoordeling/publicatie volgt een verse MAIN-read en een gewone live controle op laptopbreedtes. Tot dat moment hoort een klantmelding over schuiven bij de bekende live stand; de previewresultaten mogen die melding niet als opgelost in productie laten lijken.

## 55 Mobiele menustack, Terug en focus

De mobiele menustack is een UI-structuur binnen de headerdrawer. De bovenste categorie opent een paneel; onderliggende groepen kunnen inline uitklappen. De knop Terug sluit een menuniveau, niet de browsergeschiedenis. Een pijl voor een categorie, een plus voor een uitklapper en een productlink hebben verschillende taken en mogen niet op basis van hun icoon worden samengevoegd.

De gemelde grijze rechthoek rond Terug hoort bij pointerfocus/styling. HDR-01 verwijdert dat ongewenste pointerkader in de drawer, terwijl toetsenbordfocus zichtbaar blijft met een blauwe 2px-markering. Focusherstel gebruikt waar nodig `preventScroll`, zodat terugkeren niet tegelijk een sprong in de menulijst veroorzaakt.

| Actie | Verwachte uitkomst | Herstelcontrole |
| --- | --- | --- |
| Menu openen | Drawer zichtbaar, onderliggende pagina geblokkeerd voor scroll | Sluiten maakt de body weer normaal scrollbaar |
| Categorie openen | Juiste titel en kinditems | Terug keert naar vorige menustaat |
| Groep uitklappen | Alleen betreffende groep wijzigt | Link blijft een link; plus is geen navigatie |
| Escape | Actieve laag sluit volgens contract | Focus keert naar logische opener |
| Naar desktop resizen | Mobiele openstaat opgeruimd | Geen onzichtbare overlay of vastzittende body |

Diagnoseer een vierkant focuskader met de gebruikte invoermethode. Klik/tap en Tab mogen anders worden gestyled, maar verwijderen van alle outlines is geen oplossing. Test ook een lang menu dat zelf moet scrollen en het sluiten na een diepe scroll. Controleer bij overlayproblemen zowel de headercontroller als het draweronderdeel; twee onafhankelijke scrolllocks kunnen elkaar maskeren.

## 56 Drie zoekroutes en vindbaarheidsdiagnose

De winkel heeft geen enkele uniforme zoekmachine. De header kan native voorspellende suggesties tonen. `/search` heeft een native serverresponse en kan daarna door de externe lijst worden overgenomen. De begrippen- en assortimentzoekers filteren lokale content. Een treffer in één route garandeert geen treffer in de andere.

| Zoekroute | Invoer | Resultaatbron | Controle bij klacht |
| --- | --- | --- | --- |
| Headerpredictive | Ingetypte term | Shopify predictive endpoint/controller | Minimuminvoer, requeststatus, lege staat, linkdoel, toetsenbord |
| Resultatenpagina native | Querystring `q`, producttype | Shopify serverresultaten | HTTP, titel, termbehoud, producten/publicatie |
| Externe productlijst | Zoekterm, facet/range/sort/pagina | Externe index/API met fallback | Aanvraag, indexactualiteit, abort/race, fallback, URL-staat |
| Begrippen-/directoryzoeker | Lokale zoekterm | Reeds gerenderde items | Normalisatie, geen resultaten, reset, open-/dichtstaat |

Leg bij een mismatch de exacte term vast en vergelijk tegelijk dezelfde publicatie-/voorraadcontext. Controleer eerst of het product online gepubliceerd is en via de directe product-URL bestaat. Bekijk dan welke zoekbron de gebruiker werkelijk zag. Een thema-aanpassing synchroniseert geen externe index; een producttitelcorrectie lost geen vastgelopen frontendrequest op.

Bij snel typen of filteren mag een oud antwoord de nieuwere zoekopdracht niet overschrijven. De externe controller gebruikt daarom annulering en requestidentiteit. Bij een externe storing is de native fallback essentieel. Een 200-response voor de zoekpagina bewijst slechts serverbereikbaarheid; de producttelling en interactie na JavaScript moeten afzonderlijk worden bekeken.

## 57 Homepage, assortiment en merken beheren

De homepage wordt door `index.json` en `bc-homepage` opgebouwd. Oude uitgeschakelde homepage-secties zijn niet automatisch klantzichtbaar. Bewerk de actieve sectie en controleer de werkelijke publicatie, afbeelding, bestemming en mobiele uitsnede. Een campagne “Shop kranen” heeft een linkcontract; een mooie afbeelding zonder juiste categorie-URL voltooit die klanttaak niet.

| Onderdeel | Beheerbron | Belangrijkste controles |
| --- | --- | --- |
| Twee hoofdcampagnes | Actieve homepage-sectie | Mobiel onder elkaar, desktop naast elkaar, tekstcontrast en linkdoel |
| Negen categoriecirkels | Homepageblokken | 3×3 mobiel, negen naast elkaar vanaf 750px, betekenisvolle labels |
| Adviesaanvraag | Actieve sectie/formulier | Verplichte velden, feedback, bestemming; mailbox apart bewijzen |
| Assortiment | `list-collections.json` → `bc-assortment` | Mobiele verplaatsing en uitklapstaat, desktopkaarten, echte categorielinks |
| Merkendirectory | `list-collections.merken.json` → `bc-brand-directory` | Route `/collections?view=merken`, zoeken, merkdoelen, lege staat |

Het assortiment gebruikt onder 750px een andere contentvolgorde met echte DOM-verplaatsing. Een CSS-kolomtest alleen dekt dat niet. De directory heeft daarnaast een eigen 990px-grens voor uitklapbediening. Test zoeken, wissen en de eerder open afdelingen; een reset mag niet willekeurig alle gebruikerstaat verliezen.

Houd campagnecopy en bedrijfsbeloftes gelijk aan vastgestelde winkelafspraken. De oudere inventaris signaleert een €75/€100-verzendtekstverschil tussen componenten. Die melding is geen opdracht om verzendinstellingen te wijzigen en geen verse volledige tariefaudit. Laat de eigenaar de geldige afspraak bepalen en werk daarna alle zichtbare bronplaatsen gericht bij.

## 58 Collecties, hubs en breadcrumbs

Een collectie kan een productlijst of een categoriehub gebruiken. De template-toewijzing in Admin bepaalt de familie; een bestaande template in Git bewijst geen gebruik. De nulmeting beschrijft 209 standaardcollecties, zestien category-landings en één meubelhub. De nieuwe ronde bevestigt het totaal 226, maar exporteert niet opnieuw alle producttemplate-identiteiten.

Een wijziging begint bij het collectieobject: handle, titel, beschrijving, templateSuffix, publicatie en productselectie. Volg daarna het template naar sectie, snippets en assets. Voor Badkamermeubels bestaan drie inline style-blokken in `descriptionHtml`; die Admin-afhankelijkheid is niet volledig zichtbaar door alleen de themabron te lezen. Verwijder ze niet als vermeende overbodige opmaak zonder de betrokken schermstaten te testen.

Breadcrumbs geven de paginapositie weer. Controleer linkdoelen en tekst zowel op een directe product-URL als op een route vanuit de collectie; context kan verschillen. Een product dat in meerdere collecties staat heeft niet automatisch één unieke commerciële ouder. Het categorisatiebeleid bepaalt de identiteit; menu en SEO-landingspagina zijn aanvullende ingangen.

Acceptatie voor een collectie: juiste template, zinvolle titel/intro, correcte kindcategorieën of productset, werkende kaartlinks, mobiel/desktop, filters waar van toepassing, paginering en terugnavigatie. Controleer canonical/SEO op de daadwerkelijke response. Voeg bij een nieuw merk niet automatisch nieuwe hoofdproductcategorieën toe; hergebruik bestaande categorie-identiteiten en onderzoek echte zoekintentie vóór nieuwe SEO-landingspagina’s.

## 59 Filters, sortering, ranges en browsergeschiedenis

De externe lijst vult de serverpagina aan en heeft een eigen toestand: zoekterm, facetselecties, numerieke ranges, sortering en pagina. De URL gebruikt onder andere `bcf_*`, `bcr_*_min/max`, `bcsort` en `bcpage`. Deze parameters horen samen met de zichtbare selectie en resultaten één consistente staat te vormen.

| Gebeurtenis | Verplicht gevolg | Fout die voorkomen moet worden |
| --- | --- | --- |
| Facet wijzigen | Nieuwe selectie en passend resultaat | Oud antwoord overschrijft de nieuwste selectie |
| Range invoeren | Geldige grenzen, resultaat en URL gelijk | Slider en tekstveld tonen verschillende waarden |
| Sorteren | Zelfde scope met andere volgorde | Stille verlies van filters of verkeerde pagina |
| Browser Terug | Vorige URL-staat herstelt via popstate | Alleen URL wijzigt, zichtbare lijst blijft nieuw |
| Timeout/storing | Bruikbare native fallback | Lege blijvende laadstaat zonder uitweg |
| Mobiele drawer sluiten | Focus en scroll herstellen | Body blijft geblokkeerd of filterfocus onzichtbaar |

De controller heeft een 12seconden-timeout en requestannulering. Aanvullende kaartdata wordt via de `bc-card-data`-sectieroute opgehaald en gecachet. Het bestaan van die code is geen bewijs dat backendindex of synchronisatie nu gezond is. Leg bij een fout de API-response, queryscope, timing en fallback vast zonder tokens of persoonlijke zoekdata publiek te publiceren.

Historische FILTER-F01/F02-reproducties staan in de methodedossiers met hun eigen fixturegrens. Controleer ze opnieuw tegen de actuele bron vóór een live impactclaim. Een reparatie moet zowel een succesrespons als timeout, nulresultaat, snelle invoer en Terug/Vooruit behandelen; alleen de eerste geladen lijst is onvoldoende.

## 60 Productkaart: identiteit, kleur, afbeelding en prijs

Een productkaart is een klein koopcontract. De getoonde uitvoering moet overeenkomen met afbeelding, product-URL, variant-ID, prijs, beschikbaarheid en hartje. Een kleurwissel die alleen de foto verandert kan de klant naar de verkeerde uitvoering sturen. Daarom moeten gerelateerde nodes als één samenhangende staat worden bijgewerkt.

De kaart kan uit Liquid, native resultaten, externe resultaten of verlanglijst worden opgebouwd. Zoek de werkelijke renderer vóór een wijziging. Een kleurstaal kan een variant binnen hetzelfde product kiezen of naar een ander product met een andere handle verwijzen. Verwar een fotogalerijpijl niet met een kleur- of productkeuze; die mag slechts media veranderen.

| Te vergelijken | Controle na kleurkeuze |
| --- | --- |
| Identiteit | Producthandle en variant-ID horen bij de gekozen uitvoering |
| Media | Afbeelding, alttekst en eventuele zoom passen bij dat artikel |
| Commercieel | Huidige prijs-/vergelijkprijsnodes en eenheden kloppen |
| Navigatie | Titellink, afbeeldingslink en knop gaan naar dezelfde uitvoering |
| Bewaren | Verlanglijst bewaart de nieuwe identiteit, niet de vorige selectie |

Test initieel laden, eerste kleurwissel, tweede kleurwissel, terug naar eerste en een gedeeltelijk ontbrekende dataset. Bij tegels moet een kaartprijs per m² herkenbaar blijven en de PDP uitleggen hoe dozen worden besteld. Een screenshot van de juiste kraanfoto bewijst niet dat de koopknop het juiste variant-ID verstuurt.

## 61 Productpagina, variant en productwissel

De algemene PDP gebruikt `main-product`; Sunshower heeft een eigen hoofdrenderer. De tegeltemplate hergebruikt de algemene productpagina met een gespecialiseerd koopblok. Toewijzing, niet alleen vendornaam, bepaalt welke renderer de bezoeker krijgt. Controleer daarom product-URL, templateSuffix en gerenderde sectie samen.

Binnen één product kan `product-info` variantinformatie via AJAX bijwerken en de URL met `history.replaceState` aanpassen. Een keuze voor een ander product kan `location.assign` gebruiken en hoort dan een nieuwe pagina te laden. Dat verschil bepaalt ook wat browser Terug doet en welke data opnieuw moet worden geladen.

Werk met een identiteitstuple: product-ID, handle, variant-ID, SKU en gekozen opties. De SKU alleen is geen universele unieke sleutel voor alle leveranciersdata. Een import of merkadapter moet expliciet toetsen of gegevens bij het actuele artikel horen. Bewaar geen specificaties van het vorige product wanneer een verzoek mislukt.

De klantcontrole volgt de hele keten: titel/merk → selectie → prijs/eenheid → voorraadtekst → relevante documenten/onderdelen → aantal → winkelwagenregel. Controleer daarnaast onbeschikbare variant, foutfeedback en browsergeschiedenis. Checkout, betaling en een echte order zijn afzonderlijke platform-/bedrijfscontroles; ze zijn niet uitgevoerd door deze documentatieronde.

## 62 Tegels, oppervlakte, snijverlies en doosafronding

Een tegel heeft een presentatielaag in m² en een bestelbare eenheid, vaak een doos. De calculator vertaalt gewenste netto-oppervlakte en gekozen snijverlies naar hele dozen. De brondata voor inhoud per doos en verkoopvariant moeten aantoonbaar bij het product horen. Zonder geldige inhoud per doos mag de interface geen verzonnen hoeveelheid suggereren.

Rekencontract: benodigde oppervlakte = netto-oppervlakte × (1 + verliespercentage/100). Dozen = naar boven afgeronde benodigde oppervlakte / inhoud per doos. Geleverde oppervlakte = dozen × inhoud per doos. Rond het aantal dozen omhoog, niet de invoeroppervlakte stilzwijgend naar beneden. Houd interne precisie en Nederlandse getalnotatie uit elkaar.

**Uitsluitend rekenvoorbeeld, geen Badkamercity-product- of prijsclaim:** bij 10m², 10% verlies en een fictieve doosinhoud van 1,2m² is de behoefte 11m²; 11/1,2 vraagt tien dozen, dus 12m² levering. Dit voorbeeld vervangt geen echte productmetafields. Een prijsvoorbeeld is bewust niet nodig om de hoeveelheidslogica te begrijpen.

| Randgeval | Verwachte controle |
| --- | --- |
| Exacte doosveelvoud | Geen extra doos door onbedoelde floating-pointafwijking |
| Iets boven doosgrens | Volgende hele doos |
| Leeg, nul, negatief of onleesbaar | Duidelijke veldfeedback; geen NaN of onbedoelde koopactie |
| Komma als decimaal | Normalisatie volgens invoercontract; resultaat uitlegbaar |
| Snijverlies wijzigen | Dozen, geleverde m² en prijsnodes tegelijk bijwerken |
| Ontbrekende doosinhoud | Veilige uitleg en geen gefabriceerde calculatoruitkomst |

Controleer het uiteindelijke cartpayload en de getoonde regel, niet alleen de rekentekst. Leg vast of de variantprijs per doos is en welke m²-prijs wordt afgeleid. De eerdere Verona Cubik-browserproef heeft een eigen product en datum; zij maakt niet alle 337 tegelartikelen automatisch inhoudelijk correct.

## 63 Merkdata, specificaties en fallback

De PDP combineert algemene velden met gecontroleerde merkadapters. Specificatieprioriteit is doelgericht: Sunshower-specificaties waar die renderer dat verwacht, gecontroleerde Hotbath-data onder identiteit/importguard, beoordeelde Wiesbaden/JEE-O-data, daarna gemapte of legacyvelden. Een namespace met een bekende naam is geen garantie dat alle producten daar consistente waarden hebben.

| Situatie | Werkroute | Niet afleiden uit ontbrekende data |
| --- | --- | --- |
| Nieuwe Hotbath-import | Product-/SKU-/importscope toetsen, adapter en zichtbaarheid controleren | Dat een claim bij de hele serie hoort |
| Wiesbaden/JEE-O-correctie | Beoordeelde bron en mappings volgen | Technische maten uit een producttitel verzinnen |
| Sunshower | Eigen specificatie- en documentcontract volgen | Algemene PDP-velden zonder controle kopiëren |
| Lege of conflicterende velden | Bronconflict registreren en eigenaar aanwijzen | Willekeurig de meest gevulde namespace kiezen |

Onder identiteitguards kan een geïmporteerde beschrijvingstabel in de renderlaag worden onderdrukt zodat informatie niet dubbel verschijnt. Dat is iets anders dan de Shopify-beschrijving verwijderen. Geautomatiseerde import en handmatige content moeten daarom een duidelijke eigenaar en bronprioriteit hebben.

Gegenereerde caches versnellen weergave, maar zijn afgeleide data. Leg bij regeneratie vast welke bronrecords, mappingversie en selectie zijn gebruikt, hoe ontbrekende gegevens worden afgehandeld en wat de fallback toont. Na een wijziging test je een volledige bron, een gedeeltelijke bron en een product buiten de adapterguard. Massale migratie van `custom.*` naar `specs.*` vraagt een afzonderlijke opdracht en echte waardecontrole; de 258-definitieregistratie is geen waardemigratieplan.

## 64 Inbegrepen, vereist, optioneel en inbouwonderdelen

De PDP moet onderscheiden wat bij de verkoopprijs hoort, wat de installatie nog vereist en wat een optionele aanvulling is. Een foto met meerdere onderdelen bewijst geen setinhoud. Een gerelateerd product is evenmin automatisch inbegrepen. Gebruik alleen aantoonbare productrelaties en beoordeelde leveranciersinformatie.

| Klasse | Betekenis voor klant | Gewenst gedrag |
| --- | --- | --- |
| Inbegrepen | Onderdeel hoort bij de aangeboden uitvoering | Geen tweede betaalde toevoeging suggereren |
| Vereist | Nodig voor de bedoelde installatie maar niet aantoonbaar inbegrepen | Duidelijk uitleggen; gecontroleerde relatie naar juiste variant |
| Optioneel | Klant kan aanvullen | Geen automatische betaalde selectie |
| Alternatief | Andere uitvoering of oplossing | Niet als benodigd accessoire presenteren |

Inbouwkranen en Sunshower-installaties vragen extra zorg voor compatibiliteit. Leg bij een koppeling vast welk hoofdproduct, binnenwerk, montageonderdeel of accessoire de relatie draagt. Serienaam of kleur alleen is onvoldoende bewijs. Controleer variant-ID, hoeveelheid en zichtbare samenvatting vóór het cartverzoek.

Een succesvolle add-to-cartresponse is pas inhoudelijk juist wanneer de bedoelde regels en aantallen terugkomen. Bij meerdere regels moet duidelijk zijn hoe een gedeeltelijke fout wordt gemeld en welke producten al zijn toegevoegd. De huidige documentatieronde voert geen cartwrite uit. De acceptatiecatalogus noemt de concrete proef zodat die later gecontroleerd en met passende toestemming kan worden uitgevoerd.

## 65 Afbeeldingen, galerijen en documenten

Een mediacontrole heeft drie niveaus: het bestand bestaat, het wordt correct geladen en het toont de juiste uitvoering. Alleen de eerste twee zijn technisch automatisch te toetsen. De productcontroletool ondersteunt inhoudelijke beoordeling; een label in die privétool schrijft niet automatisch productmedia naar Shopify.

Controleer per galerij de hoofdafbeelding, volgorde, thumbnails, vorige/volgende, teller, zoom en sluitgedrag. Bij een kleurwissel mogen afbeelding en productidentiteit niet uiteenlopen. Na een mediawissel moet ook de alttekst passen. Maak onderscheid tussen een galerijpijl, productlink en kleurkeuze.

Documentdownloads volgen een apart broncontract. `custom.technische_documenten` kan een lijst URL’s leveren; beoordeelde Wiesbaden- of zichtbare Hotbath-documenten kunnen aanvullend meedoen. Deduplicatie, HTTPS en de toepasselijke visibilityguard blijven nodig. Sunshower gebruikt een eigen route. Een geldige PDF-link bewijst niet dat de handleiding bij het exacte artikel hoort.

Bij een defect document: noteer de openbare bron-URL, statuscode, productidentiteit en de gebruikte bronlaag. Gebruik geen privécontract of intern bestand als publieke vervanging. Bij een ontbrekend bestand mag de interface geen lege knop tonen. Test een product zonder documenten en één met meerdere bronnen, zodat de afwezigheids- en deduplicatiestaat ook worden gecontroleerd.

## 66 Winkelwagen, popup, bewaren en herstellen

Shopify is de bron voor de echte winkelwagen. De productpagina verstuurt variant-ID en hoeveelheid; de popup en cartpagina tonen de teruggekomen regels. Een lokale lijst met bewaarde artikelen is geen actuele cart en geen reservering.

| Bewerking | Datastroom | Controle |
| --- | --- | --- |
| Toevoegen | Selectie → Shopify-cartverzoek → teruggelezen regels | Variant, aantal, foutmelding en popupstatus |
| Hoeveelheid wijzigen | Cartregel → update → herberekende totalen | Geen oude prijs-/aantalweergave na fout |
| Verwijderen | Regelidentiteit → verwijderverzoek | Juiste regel, lege staat en focus |
| Bewaren | Huidige regels → browseropslag | Heldere betekenis en opslagfoutafhandeling |
| Herstellen | Opgeslagen regels → nieuwe POST/toevoeging | Actuele geldigheid en risico op dubbele aantallen |

Herstellen is een schrijfhandeling: opgeslagen regels worden opnieuw toegevoegd. Gebruik die knop niet tijdens een “alleen lezen”-controle. Herhaald klikken, timeouts en terugkeren naar een oude tab kunnen dubbele of verouderde toestanden veroorzaken; test de werkelijke controller en Shopify-response vóór een conclusie over de orderinhoud.

Bij een cartprobleem leg je variant-ID, hoeveelheid, component en responsefout vast in een passende privétestomgeving; publiceer geen klantcart of orderdata. Historische CART-F01-fixtures zijn gedateerde, geïsoleerde reproducties. Ze bewijzen geen nieuwe live storing. Checkout, betaalmethoden, belasting- en verzendberekening liggen verder in de keten en vereisen afzonderlijke scope en echte platformcontrole.

## 67 Verlanglijst en browseropslag

De verlanglijst bewaart productidentiteit lokaal in de browser. Het hartje op de kaart, headeraantal en `/pages/verlanglijst` moeten dezelfde opslagstaat gebruiken. Identiteit combineert waar nodig handle en variant. De browsergebeurtenis `bc:wishlist-changed` ondersteunt synchronisatie tussen componenten binnen de pagina.

| Gebruikersverwachting | Werkelijk contract | Controle |
| --- | --- | --- |
| Later terugvinden | Zelfde browser/opslagcontext | Herladen en nieuwe tab in dezelfde context |
| Op ander apparaat zien | Niet bewezen als accountfunctie | Geen accountsynchronisatie beloven |
| Prijs bewaren | Opgeslagen weergave kan verouderen | Actuele productdata bij openen/koop controleren |
| Hartje verwijderen | Identieke bewaarde uitvoering verwijderen | Geen andere variant wissen |
| Privémodus gebruiken | Opslag kan tijdelijk of beperkt zijn | Begrijpelijke lege-/foutstaat |

Een opgeslagen product kan later niet meer gepubliceerd, beschikbaar of identiek geprijsd zijn. `product.js`-cachegedrag verdient daarom een aparte versheidscontrole. Toon geen oude opslag als voorraadbevestiging. De historische WISH-F01/F02-cases hebben een eigen bron en datum; controleer cache, multitab en gewijzigde productdata opnieuw vóór een reparatie.

Een zinvolle regressie voegt twee verschillende uitvoeringen toe, herlaadt, opent de lijst, verwijdert één uitvoering en controleert de teller. Voeg ook corrupte opslag, geblokkeerde opslag en een verdwenen product toe als foutproef. Het wissen van klantbrowseropslag is geen algemene eerste oplossing; diagnoseer eerst welke sleutel en identiteit werkelijk fout zijn.

## 68 Beide footers, adres en serviceverwijzingen

Badkamercity gebruikt een grote footer en een compacte homepagefooter. Zij delen serviceonderwerpen maar hebben verschillende renderers: `sections/footer.liquid` met `footer-group.json`, en `snippets/bc-home-footer.liquid`. Een wijziging in één bron is niet automatisch op de andere paginatypen zichtbaar.

De opdracht om Zichtenburglaan 150 weg te halen is verwerkt in RET-01. Het adresveld is leeg; het contactadresblok krijgt geen lege kop. De compacte footer bevat het adres evenmin. De verse HTTP-steekproef controleert alleen aanwezigheid van deze adresstring in de footer van de onderzochte responses. Dat is geen bewijs dat de tekst nergens in de hele winkel of externe systemen voorkomt.

Retourlinks gebruiken dezelfde URL-helper als de header. De helper retourneert de echte gepubliceerde Page, alleen in een concept een toegestane contact-templatepreview, of een lege waarde in MAIN wanneer de Page verborgen is. Dit voorkomt een klantlink naar een onbeschikbare retour-Page.

Het register van 30 oktober noemt tien grote-footerlabels zonder gekoppelde bestemming. Behandel dat als een gedateerde beheerbevinding. Voor elke nieuwe link controleer je inhoud, Page-publicatie, juiste route, betekenisvolle linktekst en beide footerweergaven. Maak van een label geen verzonnen beleidsbestemming. Retourvoorwaarden, verzendbelofte en contactinformatie vragen een eigenaarsbesluit over de inhoud; themacode bepaalt de weergave.

## 69 Retouraanmelding: veld- en verzendcontract

De retourpagina gebruikt `templates/page.retour-aanmelden.json` en `sections/bc-returns.liquid`. Het native Shopify-contactformulier heeft `return_to: 'back'` en post naar `/contact`. Het is een aanvraagkanaal voor handmatige beoordeling, geen orderportaal of automatisch retoursysteem.

| Veld | Verplicht | Begrenzing/contract | Doel |
| --- | --- | --- | --- |
| Naam | Ja | Maximaal 100 tekens | Medewerker kan de aanvrager aanspreken |
| E-mail | Ja | E-mailveld, maximaal 254 tekens | Antwoordadres |
| Aanvraagtype | Ja | Retour, omruilen of probleem melden | Eerste triage |
| Artikelen en aantallen | Ja | Contactbody, maximaal 2500 tekens | Herkennen wat de klant wil melden |
| Ordernummer | Nee | Maximaal 80 tekens | Ondersteunt handmatige ordercontrole |
| Reden | Nee | Ook geen reden opgeven toegestaan | Vooraf begrijpen wat kan helpen |
| Toelichting | Nee | Maximaal 3000 tekens | Aanvullende context |
| Onderwerp | Verborgen vaste waarde | Retouraanvraag Badkamercity | Herkenning in het contactkanaal |

De reden is optioneel. Maak die niet stil verplicht om meer analysegegevens te verzamelen. Het formulier bevat geen foto-upload, klantaccount, automatische orderlookup, retourlabelaankoop, refund of automatisch RMA-nummer. De eigenaar beslist handmatig of een label of andere instructie volgt. Schrijf daarom ook geen vaste gratis-retourbelofte in de interface zonder vastgesteld beleid.

Controleer lege verplichte velden, een ongeldige e-mail, lange invoer, geldige invoer en native fout-/succesfeedback. De veldopbouw en live bereikbaarheid zijn geverifieerd; echte mailontvangst en labellevering zijn nog niet bewezen. Een succesbericht in de browser is geen bewijs van aflevering in de mailbox.

De vertalingen staan in `bc_returns` binnen NL/EN-locales. FAQ’s gebruiken native details. Velden gebruiken op mobiel 16px-tekst als onderdeel van het lees-/invoercontract. Een wijziging aan labels moet ook de vertaling, helptekst en foutfeedback meenemen, zonder de native contactveldnamen onbedoeld te breken.

## 70 Retouren behandelen: voorgesteld handmatig werkproces

Dit is een praktische werkinstructie voor het bestaande aanvraagkanaal. Er is geen retourdashboard gebouwd. Ontvangst, taakverdeling, responstijd en registratie moeten door de eigenaar worden bevestigd. De instructie hieronder beschrijft hoe een medewerker consequent kan handelen; zij is geen claim dat dit proces al operationeel is ingericht.

| Stap | Medewerker doet | Vast te leggen resultaat |
| --- | --- | --- |
| 1 Ontvangst | Controleert bevoegde inbox en spam; herkent onderwerp | Ontvangen datum en toegewezen behandelaar in eigen privésysteem |
| 2 Identiteit | Vergelijkt opgegeven bestelling, e-mail, artikelen en aantallen | Geverifieerd of welke aanvulling nodig is |
| 3 Reden begrijpen | Leest optionele reden en toelichting | Retour, omruilen, schade/defect, adviesvraag of onvoldoende gegevens |
| 4 Oplossing bepalen | Beoordeelt order en geldende winkelafspraken | Aanvullende vraag, hulp, instructie of voorgesteld label |
| 5 Antwoorden | Stuurt via bevoegde servicemail een concrete volgende stap | Wat de klant moet doen en wie verder behandelt |
| 6 Ontvangst verwerken | Controleert terugontvangen artikel en aantallen | Ontvangst-/inspectiestaat in privéregistratie |
| 7 Afsluiten | Rondt omruil/refund/andere oplossing via bevoegd proces af | Datum, uitkomst en eventuele resterende actie |

Vraag alleen aanvullende gegevens die nodig zijn voor de betreffende aanvraag. Er is geen verplichting in dit document om bewijsfoto’s, een reden of een ordernummer via het formulier af te dwingen. Een probleemmelding kan soms met advies worden opgelost; leg de keuze van de klant en de afgesproken volgende stap zorgvuldig vast.

Een retourlabel wordt handmatig beoordeeld en eventueel verstuurd. Een retourformulier genereert geen verzendlabel en boekt geen terugbetaling. Voor een label-/refundkoppeling is een afzonderlijk functioneel ontwerp nodig: vervoerder, kosten, rechten, dubbele aanvraag, status, klantcommunicatie en foutafhandeling. Deze uitbreiding activeert zulke processen niet.

Open vrijgavecontrole: één afgesproken fictieve testaanvraag versturen, ontvangst en spam controleren, antwoordpad bewijzen en testgegevens verantwoord opruimen. Pas daarna mag “mailbezorging getest” worden vastgelegd. Gebruik geen echte klantgegevens voor openbaar bewijs.

## 71 Offerte-upload: activatie en bewijsgrenzen

De offertevergelijker is een ander traject dan retouraanmelding. Het ontwerp en de externe uploadkoppeling zijn voorbereid, maar de Page is verborgen en klantactivatie staat uit. Een bestaande componentpreview met upload bewijst niet dat mailverificatie, klantcommunicatie, bewaartermijn en bevoegd beheer volledig zijn afgerond.

| Schakel | Vastgelegde stand | Benodigde controle vóór klantactivatie |
| --- | --- | --- |
| Shopify-Page | Ongepubliceerd | Juiste Page/template en expliciete vrijgave |
| Integratie | `integration_enabled=false`; preview apart gated | Geen ongewenste publieke ingang |
| Externe upload | Eerdere fictieve upload en bevoegde download hebben eigen bewijs | Ontvangst, verificatie en beheerrechten bevestigen |
| Klantmail | Nog open | Afzender, inhoud en echte aflevering controleren |
| Privébestanden | Buiten thema | Bewaren, toegang en verwijderen bepalen |
| Header/footer/teaser | Klantactivatie uit | Alleen na complete vrijgave zichtbaar maken |

De eerdere afwijzing van toegang tot het privéformulieraccount blijft een toegangsgrens. Deze documentatieronde opent dat account niet opnieuw en gebruikt geen alternatieve route. Openstaande punten blijven expliciet open; beschikbare publieke formulierinhoud vervangt geen bevoegd accountbeheer.

Beheer een offerte en een retour als verschillende onderwerpen: andere gegevens, andere verwachtingen en andere bedrijfsuitkomst. Verwijs bij wijzigingen naar de offertedossiers in hoofdstuk 43–47 en de actuele status. Neem geen oudere theme-ID of toenmalige publicatiestand over als huidige live waarheid.

## 72 Redactie, begrippen en artikelstructuur

Content leeft in Shopify Pages, collectieomschrijvingen, sectieblocks en blogartikelen. Een tekstcorrectie begint daarom met de echte bronplaats. Een titel die in een template staat verandert niet door alleen een Page-body te bewerken. Een uitgeklapt accordion kan bovendien andere content tonen dan de gewone intro.

De begrippenlijst bevat 109 verbindingen in de nulmeting. De lokale zoekfunctie filtert die gerenderde content en is niet de externe productzoekmachine. Begripkaarten en doorgelinkte Pages moeten samen worden gecontroleerd. Hygro(meter) eindigt op de bekende 404; de verse steekproef bevestigt dat opnieuw. Het document benoemt de fout, maar maakt zonder opdracht geen Page of redirect aan.

De adviesartikelrenderer verdeelt inhoud op letterlijke `<h2>`-structuur. Een editorwijziging die koppen als vette alinea of met een afwijkende markup invoegt kan de beoogde sectie-indeling verbreken. Controleer daarom niet alleen de tekst maar ook de gerenderde kophiërarchie en inhoudsblokken. De glossarykaartopbouw heeft daarnaast een contract rond directe H2-kinderen.

Publiceer content na controle van titel, unieke bedoeling, linkdoelen, beeldrechten, koppen, mobiel lezen en eventuele relatie met een commerciële categorie. Schrijf geen leverancierclaim, medische werking of technische maat zonder passende bron. Een begripspagina is uitleg; zij creëert geen bewezen productspecificatie voor alle artikelen waarin het woord voorkomt.

## 73 Productdata, imports en kwaliteitseigenaarschap

Een bruikbaar datawoordenboek beschrijft naast naam en type ook betekenis, eenheid, bron, eigenaar, toegestane leegte en afnemende component. De 258 geregistreerde productmetafielddefinities zijn een schema-inventaris; zij tonen niet dat ieder product een waarde heeft of dat die waarde klopt.

| Gegeven | Primaire controle | Typische fout |
| --- | --- | --- |
| Product/variant/SKU | Exacte identiteit en leveranciermatch | Data van een verwante uitvoering overnemen |
| Prijs en vergelijkprijs | Shopify-verkoopdata, valuta en eenheid | €/m² als doosprijs interpreteren |
| Doosinhoud | Productgebonden eenheid en numerieke geldigheid | Komma/tekst verkeerd parsen |
| Kleur/media | Artikelinhoudelijk beoordelen | Generieke foto als uitvoeringbewijs behandelen |
| Specificaties | Beoordeelde bron en namespaceguard | `custom`/`specs` blind samenvoegen |
| Relaties | Compatibele variant en bedoelde rol | Accessoire als inbegrepen onderdeel tonen |
| Publicatie | Status én verkoopkanaal | ACTIVE gelijkstellen aan koopbaar |

Een import hoort een droog overzicht te geven van nieuwe, gewijzigde, ontbrekende en conflicterende records. Review de mappings vóór schrijven, leg de bronversie vast en controleer daarna representatieve uitzonderingen. Prijs, voorraad, belastingen en productmassa vallen buiten deze documentatieronde; een register is geen toestemming voor bulkmutaties.

De quality-controltool is een afzonderlijke privéomgeving met beoordelingen, notities en checkpoints. Haar status is ondersteunend bewijs, geen automatische Shopifybron. Publiceer geen privébeoordelingen, klantgegevens of toegangsinformatie in het openbare repo. Gebruik openbare artikelidentiteiten en geaggregeerde kwaliteitssamenvattingen wanneer die nodig zijn voor technische overdracht.

## 74 SEO, canonical en gestructureerde gegevens

SEO-controle begint met de exacte URL en serverresponse. Titel, canonical, robots, H1 en JSON-LD worden per route beoordeeld. Een geldige HTTP 200 is geen bewijs van indexering; een sitemapvermelding evenmin. Search Console, Merchant Center en Analytics zijn afzonderlijke bronnen en zijn niet opnieuw onderzocht in deze uitbreiding.

| Vraag | Te lezen bron | Beslisgrens |
| --- | --- | --- |
| Bestaat de pagina? | HTTP en route/toewijzing | Soft-404 of verkeerde template apart herkennen |
| Wat is de voorkeurs-URL? | Canonical in HTML | Query-, collectie- en productcontext vergelijken |
| Mag de route worden geïndexeerd? | Robotsmeta en robots.txt | Geen zoekmachine-indexclaim zonder externe meting |
| Kloppen productgegevens? | Product-JSON-LD en zichtbare verkoopdata | Prijs/valuta/beschikbaarheid moeten coherent zijn |
| Heeft een nieuwe landing nut? | Categorisatiebeleid, intentie, dekking en overlap | Niet automatisch per merk/serie een Page maken |

Behandel filters, zoekopdrachten en alternatieve views zorgvuldig. Een nuttige gebruikers-URL is niet automatisch een gewenste indexlandingspagina. Een SEO-ingreep mag geen actieve klantnavigatie of correcte productidentiteit breken. Controleer redirects met de eindbestemming, niet alleen het bestaan van een redirectregel.

Een documentatiefout of ontbrekende meta in een oude response rechtvaardigt geen massale metadataherschrijving. Leg eerst omvang, actuele bron en eigenaar vast. De registers uit hoofdstuk 40 blijven hun gedateerde responsebewijs; de nieuwe steekproef is een beperkte aanvulling, geen nieuwe volledige SEO-audit van alle 11.679 producten.

## 75 Toegankelijkheid, toetsenbord en overlays

Toegankelijkheid wordt per taak gecontroleerd. Een focusring heeft alleen betekenis wanneer de focus ook op de juiste, zichtbare bediening staat. Een overlay die er goed uitziet kan nog steeds achtergrondfocus of scroll toelaten. Automatische semantiekcontroles vullen handmatige bediening aan, maar vervangen die niet.

| Onderdeel | Contract | Handmatige proef |
| --- | --- | --- |
| Headerzoeker | Label, suggestiestaat en bruikbare toetsen | Typen, pijlen, Enter, Escape en focusherstel |
| Mobiel menu | Openstaat, logische niveaus, scrolllock | Openen, diep niveau, Terug, sluiten en resize |
| Desktopcategorie | Bereikbare link/opener en zichtbaar paneel | Tab, submenu, Escape en tweede rij |
| Retourformulier | Labels, required, e-mailtype en foutfeedback | Leeg verzenden en veldfeedback lezen |
| Galerij/zoom | Benoemde knoppen en sluitroute | Vorige/volgende, Escape, terug naar opener |
| Filters | Samenvatting, selectie en terugkeer | Openen, toepassen, wissen en terugnavigeren |
| Verborgen zoekrij | Geen bereikbare onzichtbare invoer | Tab in compacte headerstaat |

De verwijderde grijze Terug-rechthoek is geen reden om toetsenbordfocus overal uit te schakelen. Gebruik de bedoelde `focus-visible`-scheiding. Respecteer verminderde beweging en controleer of statusmeldingen begrijpelijk worden aangekondigd zonder continue storende updates.

Contrast, tekstvergroting, schermlezerbediening en een fysieke telefoon blijven benoemde controles wanneer ze niet daadwerkelijk zijn uitgevoerd. Dit naslagwerk claimt geen volledige WCAG-certificering. Leg bij een gevonden probleem de concrete taak, gebruikte hulptechniek en mislukte stap vast, zodat een herstel toetsbaar is.

## 76 Prestaties, afbeeldingen en opstartgedrag

Snelheid kent verschillende oorzaken: netwerk, afbeeldingsgewicht, fonts, eerste opmaak, JavaScriptinitialisatie, externe API en layoutverschuiving. Een kleine HTML-response of een 200-status is geen LCP-/CLS-/INP-meting. De verse GET-steekproef bevat bron- en bereikbaarheidsbewijs, geen nieuwe performancevrijgave.

Het eerdere FLASH-01-werk richtte zich op stabiele startopmaak en icoonmaten. Het headercontract voorkomt daarnaast dat een logo na initialisatie een andere plek krijgt. Houd daarvoor servermarkup, kritieke CSS en latere controllerstaat samen in beeld. Een cache-warme tweede weergave kan een eerste-visitprobleem verbergen.

| Symptoom | Meetroute | Vergelijking |
| --- | --- | --- |
| Logo/inhoud springt | Filmstrip en layout-shiftbronnen | Eerste bezoek, home/PDP, zelfde viewport |
| Grote banner traag | Gekozen afbeeldingsbron, bytes, prioriteit | Mobiel en desktopuitsnede, geen onnodig grote bron |
| Filterlijst wacht | API-timing plus fallback | Snel succes, traag antwoord, timeout |
| Haperende header | Scrollprofiel en event-/layoutwerk | Lange scroll, zoekfocus, menu, reduced motion |
| Trage productwissel | Variant-/productrequests en renderwerk | Binnen product tegenover nieuwe product-URL |

Publiceer bij nieuwe metingen testomgeving, viewport, cacheconditie, verbinding, URL, herhalingen en datum. Noem een gerichte componentverbetering geen complete winkelsnelheidsverbetering zonder passende meting. Verwijder geen onbekende assets uitsluitend omdat ze groot of ongebruikt lijken; traceer afnemers en werkelijke laadpaden eerst.

## 77 Foutdiagnose: symptoom naar bron en eigenaar

Deze kaart verkort het eerste onderzoek. Elke rij is een diagnosepad, geen bewering dat het symptoom nu live aanwezig is. De detailhoofdstukken beschrijven de inhoudelijke contracten.

<!-- DIAGNOSIS_TABLE -->

Stop een wijziging wanneer de bron onduidelijk blijft. Leg het conflict vast, geef de beheerder één concrete vraag en werk ondertussen alleen aan onafhankelijke onderdelen. Herhaald aan CSS sleutelen zonder de actieve template of Admin-toewijzing te kennen vergroot de kans op een reparatie die alleen één voorbeeld raakt.

## 78 Acceptatie- en regressiecatalogus

De catalogus is een uitvoerbaar testontwerp. **ONTWERP** betekent dat de proef hier is beschreven; **EERDER BEWIJS** verwijst naar een gedateerd componentdossier; **NIEUW GET** is uitsluitend de 31-oktober-servercontrole. Geen rij met een ontwerpstatus mag als geslaagde test worden overgenomen. Mail, cart, checkout, fysieke apparaten en privébackend vragen hun eigen bewijs.

<!-- ACCEPTANCE_TABLE -->

Bij iedere uitvoering noteer je datum, bronhash/theme-ID, URL, viewport, testdata, resultaat en bewijsbestand. Een mislukte proef krijgt een reproduceerbare stap en impact. Een blokkade krijgt een reden en eigenaar. Test na een kleine wijziging de betrokken contracten en hun foutstaat; herhaal niet gedachteloos de hele catalogus wanneer geen afhankelijkheid is veranderd.

## 79 Release, onderhoud, versiebeheer en overdracht

Een documentatie-update en een winkelrelease zijn verschillende handelingen. Deze versie verrijkt het naslagwerk en leest de winkel; zij schrijft geen themabestanden, Pages, producten, prijzen, voorraad of formulieren. NAV-02 blijft eigenaarsbeoordeling/publicatie nodig hebben. RET-03 blijft een mailboxproef nodig hebben. De offerteklantactivatie blijft uit.

| Aanleiding | Documentatie bijwerken | Passende verificatie |
| --- | --- | --- |
| Thema publiceren | MAIN/conceptkaart, status en componentdossier | Verse rollen, hashes, live ingang en betrokken taken |
| Page publiceren/verbergen | Paginaregister en linkguards | Page-read en openbare URL/header/footer |
| Product-/categoriecontract wijzigen | Component/datawoordenboek en categorisatiebeleid | Identiteit, template, render en koop-/navigatieketen |
| Bedrijfsafspraak wijzigen | Bevestigde servicecopy en beheerkaart | Alle zichtbare bronplaatsen plus eigenaar |
| Externe integratie wijzigen | Eigenaarschap, gates en bewijsgrenzen | Bevoegde ontvangst/fout-/fallbackproeven |
| Alleen naslagwerk uitbreiden | Versie, bronnen, zoekindex en interne verwijzingen | Offline documentvalidatie; geen onnodige winkelwrite |

De vaste repository-ingang staat in `docs/LIVE_STATUS_AND_NEXT_STEPS.md`; de actieve branch staat daar expliciet. MAIN in Shopify is niet hetzelfde als de Gitbranch `main`. Houd de handoff op beide relevante branches gelijk en publiceer geen secrets of privégegevens. Een remote commit bewijst geen schone of gesynchroniseerde Windowswerkmap.

Dit naslagwerk is één leesbestand. De bron bestaat uit het bestaande masterdocument, de nieuwe praktische hoofdstukken, taken-/diagnose-/acceptatieregisters en gedateerd bewijs. De HTML-renderer maakt inhoudsopgave, tekstzoeker, takenzoeker en productrouteregister zonder externe runtimecalls. Brede technische tabellen hebben lokale overflow; de reader heeft eigen mobiele inhoudsbediening. Offline DOM-tests bewijzen functionaliteit en structuur, geen browserlayout of fysieke telefoonweergave.

Werk bij een volgende ronde eerst de actuele samenvatting bij. Vervang historische getallen niet stilzwijgend in oude meetdossiers. Leg vast wat opnieuw is gemeten, wat uit een oudere bron komt en wat nog onbekend is. Daardoor kan een volgende beheerder een concrete veilige stap zetten zonder het hele onderzoek opnieuw te moeten doen.
