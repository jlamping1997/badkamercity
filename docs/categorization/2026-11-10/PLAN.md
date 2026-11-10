# Categorieën, titels en merkpagina’s

10 november 2026. Eigenaaropdracht CATALOG-UX-01. Onderzoek en uitvoerbare voorstellen; geen categorieën, URL’s, producttitels of SEO-metadata gemigreerd.

Aanvulling tijdens uitvoering: retouradres in het concept vereenvoudigd; twee Cinto-breedtes gericht in Shopify hersteld (indexnacontrole nog nodig). Een stabiele aanbevolen productmix is voorbereid in dezelfde serverrelease als Gunmetal. [Mondiaz](../../imports/mondiaz/PLAN.md) is als later traject met lage prioriteit toegevoegd; de vijf aangeleverde merkvoorbeelden zijn in het [merkplan](../../brands/2026-11-10/PLAN.md) verwerkt.

## Wat is nu aangepast

Het bestaande conceptthema bevat beeldhover op alleen het beeldvlak en gewone categorietekst met tussenkoppen. De grote generieke advieskaarten verdwijnen. De Gunmetal-swatch krijgt een eigen koele metaaltint. De echte kleurindeling vereist daarnaast de afzonderlijke [serverupdate](../../filters/gunmetal-2026-11-10/README.md).

[Thema, bewijs en herstel](../../repairs/2026-11-10/catalog-ux/README.md). De eerdere rustige homepage blijft in hetzelfde concept behouden. Publicatie door de eigenaar blijft nodig.

## Uitgangspunt en bewijs

De volledige Shopify-read bevat **227 collecties**, opgehaald in drie pagina’s van 100/100/27. Het actuele hoofdmenu en de Admin-lidmaatschappen staan in [catalog-baseline.json](catalog-baseline.json). Aantallen zijn geen telling van afzonderlijke modellen of publiek koopbare artikelen. Een kleurvariant kan een apart Shopify-product zijn. Ontbrekende collectietoewijzing bewijst niet dat het product ontbreekt in de winkel.

Actueel gecontroleerd:

| Punt | Bewijs | Voorstel |
| --- | --- | --- |
| Houtlook / Keramisch parket | Beide volledige product-ID-sets gelezen; exact dezelfde 74 artikelen, geen volgende pagina | Houtlook als duidelijke hoofdingang; Keramisch parket als synoniem. Eerst verkeer, links en zoekintentie controleren; daarna pas beslissen over samenvoegen/301. Nu niets verwijderd. |
| Spiegelkasten | Bestaande collectie heeft 32 artikelen; ontbreekt in het hoofdmenu | Bestaande ingang terugbrengen onder Spiegels. De twee lege licht-subcollecties eerst op regels en productdata controleren; geen nieuwe kopieën. |
| Badaccessoires | 18 Admin-artikelen; Badgrepen 12 | Badgrepen zelfstandig houden: andere functie dan badplanken, krukjes en kussens. Badaccessoires blijft het overzicht. |
| Hotbath badgrepen | 12 BAA16-artikelen, alle zonder custom.card_title | Eén familie als titelproef; 12 afwerkingen zijn geen 12 aparte producttypen. |
| Inbouwbaden / vrijhangende wastafels | Beide nul collectieleden in deze read | Eerst toewijzing/assortiment controleren. Niet toevoegen aan het hoofdmenu op basis van een concurrent alleen. |
| Hotbath-vendorroute | Echte browser: 8.236 producten, native kaarten, externe filters niet actief | Een echte merkcollectie en werkend merkprofiel voorbereiden. Een mooie banner op de vendor-URL lost de filters niet op. |

## Wat we uit beide winkels gebruiken

Openbare pagina’s bekeken op 10 november; momentopname van menu’s en pagina-inhoud, geen volledige catalogusscrape, verkeers- of rankingmeting.

| Bron | Waargenomen structuur | Vertaling naar BadkamerCity |
| --- | --- | --- |
| [Sanitairwinkel](https://www.sanitairwinkel.nl/) | Onderscheid tussen categorieën, toebehoren en advies. Dezelfde passende bestemming kan vanuit meerdere afdelingen bereikbaar zijn. | Producttypen voorop. Losse onderdelen en aanvullingen herkenbaar apart, met dezelfde bestaande collectie-URL. |
| [BadkamerXXL](https://www.badkamerxxl.nl/) | Diepere type-ingangen: bijvoorbeeld douchedeur naar draai-/schuif-/pendel-/vouwdeur en afzonderlijke doucheonderdelen. | Diepgang op echte verschillende producten. Maten, kleur en andere combineerbare eigenschappen blijven ook filters. |
| [Sanitairwinkel wastafelkranen](https://www.sanitairwinkel.nl/kranen/wastafelkranen/) en [inbouw](https://www.sanitairwinkel.nl/kranen/wastafelkranen/inbouw/) | Montage-ingangen naast kleur-/merk-/hoogtekeuzes en productfilters. | Opbouw/inbouw als hoofdkeuze; hoge kraan als gericht te onderzoeken landing. Geen pagina voor elke kleur × maat × merk. |
| [BadkamerXXL wastafelkranen](https://www.badkamerxxl.nl/kranen/wastafelkranen) | Typekeuzes opbouw, inbouw, vrijstaand en elektronisch; aparte keuzehulp. | Onze bestaande montage-ingangen behouden. Vrijstaand/elektronisch pas uitbreiden bij bewezen assortiment en nuttige scope. |
| [Sanitairwinkel douchedeuren](https://www.sanitairwinkel.nl/douche/douchedeuren/) en [BadkamerXXL douchedeuren](https://www.badkamerxxl.nl/douche/douchedeuren) | Deurtype en maat/glas/profiel zijn afzonderlijke keuzeassen. | Draaien/schuiven/pendelen/vouwen niet samenvoegen; breedte, hoogte, glas en draairichting combineren via filters. |
| [BadkamerXXL badaccessoires](https://www.badkamerxxl.nl/accessoires/bad-accessoires) | Overzicht met verschillende functionele subgroepen. | Badgrepen, planken en zitproducten duidelijk houden; geen restbak waarin alles hetzelfde lijkt. |
| [Sanitairwinkel Hotbath](https://www.sanitairwinkel.nl/merkenpagina/hotbath/) | Merkuitleg en serie-ingangen. | Merkidentiteit en series verbinden aan een bruikbare productkeuze. |
| [BadkamerXXL Hotbath badkranen](https://www.badkamerxxl.nl/kranen/badkranen/hotbath) | Merk plus producttype met montage-ingangen en productlijst. | Merk × type is een kandidaat na de hoofdmerkpagina; eigen selectie en zoekintentie aantonen. |

Dit zijn ontwerpvoorbeelden, geen bewijs dat hun structuur de oorzaak van hun posities is. We nemen geen concurrententeksten, afbeeldingen of code over. Het plan blijft aangesloten op [het bestaande categoriebeleid](../../CATEGORIZATION_AND_SEO_POLICY.md).

## Voorgestelde boom per afdeling

Gebruik de bestaande collectie-identiteiten uit het register. Dit is een voorstel voor navigatie en klantvragen; een inspringing vraagt geen nieuwe geneste Shopify-URL.

| Afdeling | Primaire groepen en nuttige verdieping | Apart bij onderdelen / filters |
| --- | --- | --- |
| Kranen | Wastafelkranen → opbouw/inbouw; Fonteinkranen → opbouw/inbouw; Douchekranen; Badkranen → opbouw/inbouw/vrijstaand/badrand; Keukenkranen; Bidetkranen; Buitendouches | Thermostatisch/mengkraan als combineerbare uitvoering. Afbouwdelen, losse inbouwdelen, uitlopen en serviceonderdelen helder benoemen. Douchesets blijven ook vanuit Kranen bereikbaar. |
| Douche | Douchesets → inbouw/opbouw/glijstangsets; Inloopdouches; Douchewanden; Douchedeuren → draai/schuif/pendel/vouw; Douchecabines; Douchebakken; Doucheafvoer → goot/put; Sunshower | Hoofddouches, handdouches, slangen, glijstangen, houders/uitlaten en zijdouches zijn losse onderdelen. Breedte/hoogte/glas/draairichting filteren. |
| Badkamermeubels | Werkelijke complete sets apart van onderkasten, wastafelbladen, meubelwastafels, badkamerkasten en fonteinmeubels | Eerst complete-setdekking bewijzen: bestaande setcollecties zijn leeg. Breedte/diepte/aantal laden/materiaal via filters; spiegel/kraan/afvoer niet stilzwijgend inbegrepen noemen. |
| Wastafels | Waskommen en opzetwastafels als één herkenbare ingang; Meubelwastafels; Fonteinen → los/set/meubel | Vrijhangende wastafels pas na datacontrole. Sifons, pluggen en montage apart. Vorm, maat, kraangat en materiaal combineerbaar. |
| Toiletten en fonteinen | Hangtoiletten; Douche-wc’s; Fonteinen; Bedieningsplaten; Toiletzittingen; Reservoirs → inbouw waar gevuld | Compact en spoelrandloos blijven nuttige bestaande landingen én filters. Staande toiletsets/urinoirs/bidetten pas bij echte dekking. |
| Baden | Vrijstaand; Halfvrijstaand; Whirlpool; Badwanden; Badafvoer en vulling | Inbouwbaddekking onderzoeken. Badkranen als aanvullende ingang; Badgrepen, badplanken, krukjes en kussens op functie onderscheiden. |
| Tegels | Toepassing: vloer/wand. Type: mozaïek/decor. Uitstraling: steen/marmer/beton/hout/metaal/terrazzo; overige bestaande looks via filter | Maat, kleur en afwerking combineren. Toepassingen kunnen overlappen. Houtlook/Keramisch parket eerst één hoofdroute geven; geen technische tegeltoepassing uit een kleurnaam afleiden. |
| Spiegels en verlichting | Badkamerspiegels; Spiegelkasten; Scheer-/make-upspiegels; Spiegelverlichting; Badkamerverlichting → spots/plafond/hang waar gevuld | Spiegelverwarming en verlichting zijn andere eigenschappen. Vorm/licht/verwarming combineerbaar; relevante bestaande vormlandingen behouden. Spiegelkasten weer zichtbaar maken. |
| Accessoires | Handdoekhouders → haak/stang/rek/ring; Toiletaccessoires → rol/borstel/reserverol; Zeepaccessoires → dispenser/houder; Nissen; Planchetten; Glashouders; Wissers; Afvalemmers; Onderhoud | Dezelfde accessoires ook vanuit douche/bad/toilet bereikbaar. Badkrukje niet zonder bewijs als douchezitje verkopen. Kleur en exacte afwerking apart houden. |
| Verwarming en ventilatie | Radiatoren → handdoek/design/elektrisch; Handdoekwarmers; Elektrische vloerverwarming; Ventilatie | Aansluitmateriaal apart. Type, energiebron en vermogen zijn geen exclusieve alternatieven; alleen gevulde bestaande radiatortakken tonen. |
| Merken | Eén overzicht → eigen merklanding → relevante producttypen en echte series | Merken zijn geen nieuwe producttypen. Geen volledige kopie van de categorietaxonomie voor ieder merk. |

## Samenvoegen, behouden of eerst onderzoeken

| Keuze | Voorstel | Voorwaarde vóór uitvoering |
| --- | --- | --- |
| Waskom / opzetwastafel | Eén hoofdingang met beide begrijpelijke woorden | Bestaande /opzetwastafels hergebruiken; geen extra identieke collectie |
| Toiletrolhouder / wc-rolhouder; bedieningsplaat / bedieningspaneel | Synoniemen voor dezelfde productfunctie | Eén URL en gedeelde zoektermen |
| Houtlook / keramisch parket | Kandidaat voor één hoofdbestemming | ID-sets zijn gelijk; eerst zoekintentie/traffic/canonical/interne links beoordelen |
| Kranen versus Douches → douchekranen | Beide navigatiepaden houden | Eén collectie, geen dubbele product- of SEO-pagina |
| Badgrepen versus badplanken | Zelfstandige subcategorieën houden | Verschillende functies; Badaccessoires als parent |
| Doucheset versus losse hoofddouche | Gescheiden houden | Complete samenstelling en los onderdeel niet vermengen |
| Complete kraan versus afbouwdeel/inbouwdeel | Gescheiden herkenbaarheid | Inhoud exact controleren; ‘compleet’ alleen met bewijs |
| Gunmetal versus Grijs | Zelfstandige filterwaarden | Exacte bronafwerking behouden; Verouderd ijzer blijft Grijs |
| Kleur/maat × ieder merk/type | Eerst filters, selectieve SEO-landingen later | Zoekvraag, eigen nuttige selectie en overlap aantonen |
| Lege bestaande collecties | Inventarisatiewerk, geen automatische verwijdering | Eerst ontbrekende toewijzingen en werkelijk aanbod controleren |

## Simpele SEO-presentatie

Korte introductie boven de keuze/producten. Daaronder gewone leesbare inhoud met concrete H2/H3’s, alinea’s en passende links. Geen vaste woordquota, drie universele adviezen of opgeblazen servicebanner. FAQ alleen als echte vragen te beantwoorden zijn; FAQ wordt niet als garantie op rich results gepresenteerd.

Het bestaande `[SPLIT]`-mechanisme blijft leidend: tekst vóór de marker is de introductie, tekst erna de onderste inhoud. Op `category-landing` verzorgt de bestaande hub die onderste inhoud; de adviessectie herhaalt die niet. Op standaardcollecties toont de vernieuwde sectie deze inhoud. Extra beheertekst blijft beschikbaar. Voor Badaccessoires/Badgrepen is korte specifieke terugvaltekst toegevoegd; andere lege categorieën krijgen geen nieuwe generieke vulling.

De andere SEO-chat kan collectieomschrijving, SEO-titel en metaomschrijving verder verbeteren zonder een nieuwe presentatietemplate te bouwen. In deze opdracht zijn die Admin-velden niet geschreven.

## Uitvoering in afgebakende stappen

| Batch | Resultaat | Klaar wanneer |
| --- | --- | --- |
| 1. Interface | Foto-hover, tekstpresentatie, eigen Gunmetal-weergave in bestaand concept | Preview beoordeeld en eigenaarpublicatie; serverkleurupdate afzonderlijk gecontroleerd |
| 2. Titelproef | [Hotbath BAA16](../../product-content/2026-11-10/TITLE_PLAN.md) als eerste familie | Kort/lang voorstel en broncontrole beoordeeld; pas daarna beperkte write |
| 3. Categorieproef | Wastafels/Spiegels: bestaande ingangen, sets en lege routes controleren | Exacte URL-/product-/filtermapping en concreet navigatievoorstel |
| 4. Eerste merk | [Hotbath-landing](../../brands/2026-11-10/PLAN.md) | Merkselectie blijft behouden in ieder filter en iedere productgroep; desktop/mobiel en directe landing getest |
| 5. Uitbreiden | Per afdeling en merk dezelfde beslissingen hergebruiken | Register bijgewerkt, foutgevallen geblokkeerd, bron en terugzetpad aanwezig |

Vóór een bestaande URL vervangen wordt: verkeer/zoekintentie, indexatie, backlinks waar beschikbaar, huidige canonical en gewenste bestemming vergelijken. Geen brede redirects of indexeringswijziging in deze onderzoeksronde.

Google beschrijft interne links van categorie naar subcategorie naar producten als hulp voor ontdekking en structuur. Een steeds diepere URL of gekopieerde concurrentieboom is daarvoor geen vereiste: [Google Search Central](https://developers.google.com/search/docs/specialty/ecommerce/help-google-understand-your-ecommerce-site-structure). Positie top 3 of 1 blijft een doel, geen aangetoond of gegarandeerd gevolg. Na publicatie meten we per bedoelde pagina indexatie, zoekopdrachten en klikken, en houden we advertentieconversie apart.
