# BadkamerCity Masterplan

> **Versie 0.16 - ACTIVE FOR DISCOVERY - IMPLEMENTATION BLOCKED.** `BC-GOV-006` en fase 0 zijn na menselijke review en drie aantoonbare reviewfixes `DONE`; de tracked protocolbestanden worden met deze taak gecontroleerd gecommit. De verplichte handoff is een genegeerde one-bundle-run met raw evidence en `review_files/`. Er is geen volgende taak actief en geen `PROPOSED-TECH-*`-kandidaat gestart. Implementatie, Shopify-, theme-, bron- en datamutaties blijven geblokkeerd.

Markeringen in dit document:

- `[NOG ONDERZOEKEN]`: feitelijke informatie ontbreekt en moet read-only worden vastgesteld.
- `[OPEN BESLISSING]`: er is een expliciete keuze van de bevoegde eigenaar nodig.
- `[GEBLOKKEERD]`: werk kan niet verantwoord starten voordat genoemde input, beslissing of afhankelijkheid beschikbaar is.

## 1. Documentbeheer

| Veld | Waarde |
| --- | --- |
| Documentnaam | `docs/MASTERPLAN.md` |
| Versie | `0.16` |
| Status | `ACTIVE FOR DISCOVERY - IMPLEMENTATION BLOCKED` |
| Datum laatste wijziging | 2026-08-11 |
| Eigenaar | BadkamerCity-projecteigenaar; naam en formele rol `[NOG ONDERZOEKEN]` |
| Centrale bron van waarheid | Dit bestand op GitHub-branch `main`, naast de bewijsdocumenten in `docs/` |
| Huidige Git-branch | `main` |
| GitHub-repository | `https://github.com/jlamping1997/badkamercity.git` |
| Productieomgeving | Store `fpa9hu-i3.myshopify.com`; live theme `Categoriepagina_v1.0` (`189463068938`) |
| Developmentomgeving | Unpublished theme `BadkamerCity Development` (`192770375946`) |

De status activeert alleen het vastgelegde read-only onderzoekswerk. Theme-implementatie, Shopify Admin-mutaties, theme-pushes en publicatie blijven zonder een afzonderlijke expliciete menselijke opdracht verboden.

## 2. Dashboard bovenaan

| Onderdeel | Actuele stand |
| --- | --- |
| Algemene projectstatus | Discovery is menselijk goedgekeurd en actief; implementatie en lancering blijven geblokkeerd |
| Huidige fase | Fase 0 - fundament en projectbesturing; status `DONE` na menselijke goedkeuring van het uitvoeringslogprotocol |
| Actieve taak-ID | Geen; `BC-GOV-006` is `DONE` |
| Actieve taak | Geen |
| Eerstvolgende actie | Eerste onafhankelijke toekomstige taak gebruikt verplicht het goedgekeurde one-bundle-protocol; keuze en toestemming voor die taak blijven afzonderlijk menselijk |
| Belangrijkste blokkades | Nul oorspronkelijke lokale leveranciersbestanden, nul import-/generatiescripts, onbekende bronhouders en ontbrekende prijs-, voorraad-/levertijd-, media- en tegeleenheidsbronnen; daarnaast ontbreken volledige app-/pixelbron, runtimevalidatie, gevalideerd productdatamodel, categorieboom, leverancierregels en meerdere architectuurbesluiten |
| Laatste technisch afgeronde onderzoeksuitvoer | `BC-TECH-002` - bestuurbare technische onderzoeksbasis met 21 bevindingen en twaalf kandidaten; menselijk goedgekeurd en `DONE` |
| Laatste menselijke goedkeuring | 2026-08-11 - `BC-GOV-006` inhoudelijk goedgekeurd na aantoonbaar herstel van one-bundle handoff, child-cmdletfoutsemantiek en raw-evidencecompleteness; geen technische kandidaat of implementatie goedgekeurd |
| Laatste relevante commit | Deze commit: `chore: finalize Codex execution logging`; exacte hash staat in het genegeerde reviewfix-runbewijs en op `origin/main` |
| Previewstatus | `BadkamerCity Development` is unpublished; preview- en Theme Editor-links zijn vastgelegd; geen nieuwe theme-code is geüpload sinds de aanmaak |
| Productdoel voor lancering | Ongeveer 20.000 volledig ingerichte, gekoppelde, gecategoriseerde, doorzoekbare en filterbare producten |
| Voorlopige taken | 41 totaal: 12 `DONE`, 0 `READY`, 0 `IN_PROGRESS`, 0 `NOT_STARTED`, 26 `BLOCKED`, 0 `REVIEW`, 3 `DEFERRED` |

### Actuele route

- **Waar we nu zijn:** `BC-TECH-002`, `BC-GOV-006` en fase 0 zijn menselijk goedgekeurd en `DONE`. Het loggingprotocol vereist voortaan een enkele genegeerde bundle met volledige raw evidence en hashgecontroleerde `review_files/`. Fase 2 blijft `BLOCKED` voor definitieve data-/IA-uitvoer en fase 3 blijft `BLOCKED` voor technische uitvoering. Masterplan versie 0.16 blijft `ACTIVE FOR DISCOVERY - IMPLEMENTATION BLOCKED`.
- **Wat is vastgelegd:** de volledige lokale set van 405 bestanden bij taakstart en de bereikbare Git-padgeschiedenis bevatten nul oorspronkelijke leveranciersbestanden en nul import-/generatiescripts. Deze lokale nulbevinding is menselijk geaccepteerd. Externe bronnen kunnen bestaan en worden later per leverancier afzonderlijk aangeleverd en beoordeeld.
- **Welke input nodig is:** retentietermijn en eigenaar van lokale runbundles blijven een `[OPEN BESLISSING]`. Voor technische uitvoering blijven een afzonderlijke officiele taak, exacte scope en expliciete toestemming nodig. De vaste levertijdweergave vereist eerst een commercieel/operationeel besluit; definitieve data-/IA-uitvoer blijft bronafhankelijk.
- **Welke taken daarna komen:** geen taak is actief. De eerste onafhankelijke toekomstige taak moet het goedgekeurde protocol in echte projectuitvoering gebruiken. Alleen na een afzonderlijk menselijk besluit kan eventueel `PROPOSED-TECH-01` als officiele taak worden voorbereid; de twaalf kandidaten blijven voorstellen en `BC-TECH-001`, `BC-DATA-001`, `BC-IA-001` en alle implementatietaken blijven geblokkeerd.

## 3. Hoe dit masterplan gebruikt moet worden

Voor iedere taak moet Codex eerst lezen:

1. dit volledige masterplan, met name dashboard, taakrecord, beslislogboek, open vragen, risico's en actuele route;
2. de bewijsbronnen uit hoofdstuk 62 die voor de taak relevant zijn;
3. de actuele Git-status en uitsluitend bij read-only Shopify-onderzoek de vooraf toegestane omgevingsinformatie;
4. alle nieuwere menselijke instructies en goedkeuringen die de taak raken.

Statusbeheer:

- Alleen `NOT_STARTED`, `READY`, `IN_PROGRESS`, `BLOCKED`, `REVIEW`, `DONE` en `DEFERRED` zijn toegestaan.
- Een taak wordt pas `READY` als Definition of Ready is gehaald.
- Een taak wordt `IN_PROGRESS` zodra toegestaan werk daadwerkelijk start.
- Een technische implementatie mag pas `REVIEW` worden nadat de vastgelegde technische controles slagen.
- Visueel of functioneel werk mag alleen `DONE` worden na expliciete menselijke goedkeuring.
- Voorbereidend read-only of documentatiewerk mag `DONE` zijn als bestaand bewijs uitvoering en resultaat aantoont.
- Geen enkel lanceringsonderdeel is in versie 0.16 `DONE`; de twaalf `DONE`-taken zijn governance-, read-only onderzoeks- of conceptuele documentatietaken.

Bewijs en onderhoud:

- Bewijs krijgt een datum, taak-ID, bron, resultaat en waar mogelijk commit of previewverwijzing.
- Ontbrekend bewijs blijft gemarkeerd als `[NOG ONDERZOEKEN]`; een aanname telt nooit als bewijs.
- Open vragen krijgen een vaste ID en verwijzen naar afhankelijke taken.
- Na iedere taak worden minimaal dashboard, taakstatus, bewijsregister, risico's, open vragen, actuele route en wijzigingslog bijgewerkt.
- Een wijziging aan dit document wordt als afzonderlijke, controleerbare documentatiecommit vastgelegd.
- Tegenstrijdige nieuwere feiten worden niet stil overschreven: bron, datum en besluit worden in het beslislogboek vastgelegd.

## 4. Projectvisie

BadkamerCity moet uitgroeien tot een van de grootste complete badkamer- en tegelwebshops van Nederland en uiteindelijk van de Benelux. De webshop moet een breed assortiment combineren met deskundig advies, scherpe prijzen, exclusieve merken en een betrouwbare koopervaring.

De lancering is geen tussenversie met bewust ontbrekende kernonderdelen. Het doel is een functioneel, visueel en technisch goedgekeurde webshop met ongeveer 20.000 volledig ingerichte producten. Zelfstandige groei van BadkamerCity blijft het langetermijndoel.

## 5. Positionering en commerciële propositie

Bevestigde pijlers:

- scherpe prijzen en commerciële prijsconcurrentie bij algemeen verkrijgbare producten;
- deskundig advies;
- exclusieve merken die niet overal online verkrijgbaar zijn;
- een laagsteprijsgarantie;
- de mogelijkheid een bestaande offerte te uploaden voor een betere aanbieding;
- vertrouwen, overzicht en een rustige uitstraling.

De exacte voorwaarden, juridische formuleringen, operationele afhandeling en meetbare beloften voor laagsteprijsgarantie en offertevergelijking zijn `[OPEN BESLISSING]`.

## 6. Doelgroep en markt

- Primaire markt: Nederland.
- Taal bij lancering: Nederlands.
- Buitenlandse klanten mogen via de Nederlandse website bestellen.
- Internationale uitbreiding is nu geen hoofdprioriteit.
- Exacte doelgroepsegmenten, koopmotieven, zakelijke doelgroepen, regioverdeling en persona's zijn `[NOG ONDERZOEKEN]`.
- Onderzoek moet onderscheid maken tussen oriënterende klanten, gerichte productkopers, complete-badkamerklanten en eventuele zakelijke klanten; de definitieve segmentatie is `[OPEN BESLISSING]`.

## 7. Relatie BadkamerCity en Harry Suiker

- BadkamerCity is ontstaan vanuit Harry Suiker.
- Harry Suiker is momenteel moederbedrijf en operationele basis.
- BadkamerCity moet uiteindelijk zelfstandig opereren en een eigen showroom openen.
- Tot die tijd kan showroombezoek op afspraak plaatsvinden in de bestaande showroomomgeving van Harry Suiker.
- Er mag voorlopig over meer dan 1.000 m² showroom worden gecommuniceerd, maar de exacte openbare formulering moet worden gecontroleerd.
- De site mag niet suggereren dat BadkamerCity al een volledig zelfstandige eigen showroomlocatie exploiteert.
- Uitgebreide Harry Suiker-showroomgegevens worden voorlopig niet rechtstreeks als BadkamerCity-showroominformatie gepubliceerd.

`[GEBLOKKEERD]` Publieke showroomteksten mogen niet definitief worden gemaakt voordat eigenaar en verantwoordelijke voor inhoud/juridische controle de formulering hebben goedgekeurd.

## 8. Scope voor lancering

Bevestigde lanceringsscope:

- ongeveer 20.000 volledig ingerichte producten;
- correcte productkoppeling, categorisering, zoekbaarheid en filtering;
- werkende benodigde switchers, calculators en configurators;
- een Nederlandstalige ervaring voor mobiel en desktop;
- productpagina's volgens de standaard in hoofdstuk 17;
- verlanglijst, samples bestellen, offerte uploaden en laagsteprijsgarantie aanvragen;
- klantaccount, bestelhistorie en bestelling volgen;
- afspraak maken en WhatsApp of chat;
- inspiratieartikelen en adviespagina's;
- actuele voorraadstatus en betrouwbare levertijd volgens nog vast te stellen leverancierregels;
- pakketpost, palletlevering, afhalen, gecombineerde en gesplitste levering waar operationeel van toepassing;
- functionele, visuele en technische goedkeuring vóór publicatie.

De precieze afbakening per functie wordt pas definitief na onderzoek en taakdecompositie.

## 9. Buiten scope of later

Bevestigd voor later:

- daadwerkelijke koppeling van toekomstige leverancier-API's aan bestaande producten is een apart later werkpakket;
- API-koppelingen zijn geen eerste ontwikkelprioriteit;
- een uitgebreide configurator voor complete badkameropstellingen is toekomstig werk; werking en scope zijn `[OPEN BESLISSING]`;
- internationale uitbreiding is geen huidige hoofdprioriteit.

Nog niet als in of buiten lanceringsscope besloten:

- productreviews: `[OPEN BESLISSING]`;
- producten vergelijken: `[OPEN BESLISSING]`;
- calculators/configurators voor andere productgroepen dan tegels, douchesets en badkamermeubels: `[NOG ONDERZOEKEN]`.

## 10. Definitie van een complete lancering

Een complete lancering is pas bereikt als:

- de overeengekomen lanceringsscope aantoonbaar is gerealiseerd;
- ongeveer 20.000 producten voldoen aan vastgestelde datakwaliteitscriteria;
- productkoppelingen, categorieën, zoeken, filters, switchers, calculators en configurators zijn gevalideerd;
- voorraad-, levertijd-, verzend-, retour-, garantie- en service-informatie betrouwbaar kan worden getoond en uitgevoerd;
- kernreizen op mobiel, desktop en toetsenbord zijn getest;
- performance, toegankelijkheid, technische SEO, privacy en tracking aan nog vast te stellen acceptatiegrenzen voldoen;
- geen open P0-blokkade of onaanvaardbaar restrisico bestaat;
- de eigenaar alle zichtbare en functionele lanceringsonderdelen expliciet heeft goedgekeurd;
- publicatie naar live afzonderlijk en expliciet menselijk is goedgekeurd;
- rollback en monitoring gereed en gecontroleerd zijn.

`[GEBLOKKEERD]` De meetbare launchcriteria kunnen pas worden afgerond na Admin-, data-, logistiek-, SEO-, UX- en technisch onderzoek.

## 11. Huidige technische uitgangssituatie

De repository is een Shopify Online Store 2.0-theme, sterk gebaseerd op Dawn en uitgebreid met BadkamerCity-maatwerk. De standaard theme-mappen zijn `assets`, `config`, `layout`, `locales`, `sections`, `snippets` en `templates`. Zwaartepunten zijn `sections/main-product.liquid`, `sections/header.liquid`, `assets/global.js`, `assets/base.css` en de product-switcherdataset.

| Onderdeel | Bevestigde situatie | Bron |
| --- | --- | --- |
| Lokale basis | `CITY_MASTER`, branch `main` | Repository en Git-status |
| GitHub | `jlamping1997/badkamercity` | Git remote |
| Store | `fpa9hu-i3.myshopify.com` | `docs/SHOPIFY_ENVIRONMENT.md` |
| Live theme | `Categoriepagina_v1.0`, ID `189463068938`, role `live` | `docs/SHOPIFY_ENVIRONMENT.md` |
| Development-theme | `BadkamerCity Development`, ID `192770375946`, role `unpublished` | `docs/DEVELOPMENT_THEME.md` |
| Live-pariteit | 396 lokale en 396 live bestanden; geen lokale, live of inhoudelijke verschillen in zeven theme-mappen | `docs/LIVE_THEME_COMPARISON.md` |
| Repository-audit | Architectuur, maatwerk, risico's, backups en Theme Check-resultaten vastgelegd | `docs/REPOSITORY_AUDIT.md` |

De live-pariteit bewijst alleen gelijkheid van theme-bestanden op 2026-08-03. Producten, collecties, metafields, metaobjects, menu's, apps, markets, instellingen en andere externe data zijn daarmee niet vergeleken.

## 12. Huidige functionele uitgangssituatie

Aanwezig in code, maar niet automatisch end-to-end goedgekeurd:

- Dawn-basis voor cart, accounts, collecties, zoeken, productformulier, predictive search en localization;
- custom home-secties, category landing pages, zoekresultaatkaart en USP-strip;
- begrippenlijsttemplates en -secties;
- productpagina-maatwerk met media, buybox, specificaties en product-switcher;
- custom header/footer en links voor wishlist/showroom;
- een nieuwe switcher met 433 groepen en 3.383 producten in de dataset.

Gedeeltelijk, onaf of onzeker:

- twee switcherimplementaties naast elkaar;
- lege homepage-links/collecties, placeholderteksten en `href="#"`-links;
- losse productsecties naast de geïntegreerde productpagina;
- een verwijderd short-specsblok en een pros/cons-snippet zonder gevonden render-verwijzing;
- externe data, actieve Theme Editor-configuratie en app-afhankelijkheden `[NOG ONDERZOEKEN]`.

Mogelijk defect of experimenteel:

- vermoedelijk ongeldige section-nesting in `sections/bc-related-products.liquid`;
- ongedefinieerde `variant_images` in `sections/product-media.liquid`;
- mogelijk ontbrekende context in `sections/product-info.liquid`;
- encoding-schade in een oud switcher-vinkje;
- 1 Theme Check-error en 11 warnings, deels mogelijk tooling-gerelateerd.

Geen van deze lanceringsonderdelen is in dit masterplan als functioneel `DONE` aangemerkt.

## 13. Technische architectuur

Bevestigde huidige lagen:

1. Shopify OS 2.0-layouts, JSON/JSONC-templates, sections en snippets.
2. Dawn-basiscomponenten en globale assets.
3. BadkamerCity-maatwerk voor home, categorie, product, zoeken, header/footer en begrippen.
4. Theme-gebonden switcherdata in een grote JSON-asset plus metafield-triggers.
5. Shopify Admin en externe data als nog niet geïnventariseerde afhankelijkheidslaag.

Architectuurprincipes voor vervolgwerk:

- `main` blijft de goedgekeurde centrale basis.
- Nieuwe zichtbare ontwikkeling wordt via het unpublished development-theme beoordeeld, nooit rechtstreeks op live.
- Iedere verkoopbare uitvoering blijft een zelfstandig product met eigen URL en SKU.
- Configurators navigeren in het huidige productmodel naar een bestaand product en bouwen nu geen bundel van losse cartregels.
- Toekomstige feeds moeten door het datamodel kunnen worden ondersteund, zonder nu een API-implementatie te veronderstellen.
- Exacte grenzen tussen theme, Shopify Admin, metafields, metaobjects, apps en externe systemen zijn `[NOG ONDERZOEKEN]`.

## 14. Shopify Admin en externe data

Het read-only onderzoek van 2026-08-04 is uitgevoerd via Shopify CLI `4.6.0` met dertien door de projecteigenaar goedgekeurde en door Shopify verleende read-scopes. Gepagineerde Admin-query's hebben de volgende domeinen geïnventariseerd:

- 7.827 actieve producten en 7.827 varianten, productstatussen, SKU-dekking, vendors en producttypes;
- 201 collecties, collectievoorwaarden, productaantallen en template suffixes;
- metafielddefinities en exacte dekking voor de prioriteitsvelden, plus een begrensde specificatiesteekproef;
- één metaobjectdefinitie zonder entries en zonder zichtbare metafieldreferenties;
- vijf menu's met 247 items en hun volledige boom en targets;
- 117 pagina's, vier themes en de actieve live JSON-configuratie;
- één markt, één gepubliceerde taal, nieuwe customer accounts en één checkout-/accountconfiguratie;
- één locatie, 7.827 inventory items, één delivery profile, drie verzendzones en nul carrier services.

De volledige lijst met geïnstalleerde apps, pixels, scripts en externe integraties is via de verleende scopes **NIET TOEGANKELIJK**. De live JSON-configuratie bevat geen aantoonbare theme app blocks of app embeds, maar dat bewijst niet dat er geen apps of buiten-theme-integraties bestaan. Theme `192796786954` bestaat bewezen als unpublished theme; eigenaar, exact doel en ontstaansreden zijn `[NOG ONDERZOEKEN]` en het theme mag niet worden gewijzigd, verwijderd, gepubliceerd, gepusht of gepulld.

Deze inventarisatie is taak `BC-ADM-001` en is na expliciete menselijke beoordeling `DONE`. Zij bleef volledig read-only: geen product, collectie, metafield, metaobject, menu, app, instelling, inventory, delivery profile of themeconfiguratie is gewijzigd. Het volledige bewijs, de representatieve steekproeven, beperkingen en open vragen staan in `docs/SHOPIFY_ADMIN_INVENTORY.md` en blijven van kracht.

Het aanvullende lokale onderzoek van `BC-DATA-002` op 2026-08-10 vond geen oorspronkelijke leveranciersbron, importbestand of import-/generatiescript in de repository. Zes valide JSON-achtige assets zijn uitsluitend als afgeleide switcher-/themedata bewezen. De actuele asset bevat 433 groepen, 560 menu's en 3.383 unieke Hotbath-handles; The Mosaic Factory is lokaal alleen via het bestaande Admin-bewijs vertegenwoordigd. De projecteigenaar heeft de binnen-scope complete nulmeting en nul oorspronkelijke lokale bronnen op 2026-08-10 als geldige bevinding goedgekeurd; externe bronnen blijven open en worden later per leverancier afzonderlijk aangeleverd. Volledige details staan in `docs/SUPPLIER_DATA_INVENTORY.md`; `BC-DATA-002` is `DONE`.

## 15. Productdatamodel

Bevestigd doelmodel:

- iedere verkoopbare kleur, maat of uitvoering is een zelfstandig Shopify-product;
- ieder verkoopbaar product heeft een eigen URL en SKU;
- gewone meerkeuze-variantmenu's zijn niet de productarchitectuur;
- een technisch verplichte standaardvariant per product kan bestaan;
- onderling verwante producten worden via switcher/configurator gekoppeld;
- selectie leidt naar het passende bestaande product.

Benodigde datadomeinen omvatten identiteit, merk, commerciële tekst, prijs/adviesprijs, media, specificaties, voorraad, levertijd, documenten, garantie, levering, retouren, SEO, relaties, switchergroepen en producttype-specifieke eenheden. Dit is een eisenlijst, geen bevestiging dat deze velden al bestaan.

`docs/PRODUCT_DATA_CONTRACT.md` legt als bestuurde conceptuele werkbasis v0.1 190 unieke conceptkeys in 15 logische domeinen vast, met type, cardinaliteit, toepasselijkheid, voorgesteld vereisteniveau, broncategorie, gebruik, validatie, leegstaat en eigenaarsrol. `BC-DATA-003` is binnen die brononafhankelijke documentatiescope menselijk goedgekeurd en `DONE`; dit bewijst niet dat waarden beschikbaar zijn en keurt individuele keys, niveaus, gates of opslagkeuzes niet definitief goed. `[GEBLOKKEERD]` De definitieve veldcatalogus, Shopify-objecten, metafieldnamen, opslagtypen, leveranciermapping, producttypecatalogus, categorieboom en filterdekking wachten op oorspronkelijke bronnen en afzonderlijke menselijke beoordeling. De 58 statische custom-metafieldreferenties en 30 afgeleide V2-optiekeys zijn geen definitief datamodel.

## 16. Product-switcher en configuratorarchitectuur

Huidige V2:

- `snippets/bc-product-switcher.liquid`;
- `assets/bc-product-switcher.js`;
- `assets/product-switcher-data.json`;
- trigger `product.metafields.custom.switch_group`;
- client-side navigatie naar een exact gematcht bestaand product.

De actuele asset heeft intern unieke group-id's, handles, URL's en optiecombinaties, maar bevat geen SKU, EAN, vendor, prijs, voorraadhoeveelheid, levertijd, media of bronmetadata. De 3.383 assethandles zijn in deze lokale taak niet een-op-een vergeleken met de 3.658 Admin-producten met `custom.switch_group`.

Huidige fallback:

- inline Liquid-data in `sections/main-product.liquid`;
- `BCProductSwitcher` in `assets/global.js`;
- trigger via legacy `custom.group` en menuvelden;
- mogelijke extra section-fetches voor gepagineerde collecties.

Te besluiten in `BC-SWITCH-001`:

- één bron van waarheid en eigenaarschap van data;
- generatie- en validatieproces;
- behoud of uitfasering van de fallback;
- foutgedrag bij ontbrekende groepen/producten en dubbele combinaties;
- payloadstrategie voor de circa 1,85 MB V2-dataset;
- migratie, testmatrix en rollback.

`[GEBLOKKEERD]` De oorspronkelijke Hotbath-bron, generator, mapping en bronhouder ontbreken lokaal. Geen switcherrefactor start vóór menselijke beoordeling van `BC-DATA-002`, aanvullende broninput, de Admin/metafield-inventarisatie en een expliciet architectuurbesluit.

## 17. Productpaginastandaard

Iedere relevante productpagina moet waar van toepassing kunnen bevatten:

- breadcrumbs, merk, producttitel en SKU;
- prijs, eventuele adviesprijs/korting, actuele voorraadstatus en betrouwbare levertijd;
- afbeeldingen/media en toegankelijke bediening;
- switcher/configurator, aantal en winkelwagenactie;
- korte en volledige specificaties, pluspunten en aandachtspunten;
- korte commerciële en uitgebreide productomschrijving;
- technische documenten en montagehandleidingen;
- garantie-, leverings- en retourinformatie;
- accessoires, benodigde aanvullende artikelen, alternatieven en gerelateerde producten;
- interne links naar categorieën, merken, advies en begrippen;
- relevante FAQ;
- SEO-titel, metabeschrijving, headings, structured data, canonical en indexeringscontrole;
- bruikbaarheid op mobiel, desktop en toetsenbord.

Per element moeten databron, leegstaatgedrag, volgorde, producttype-toepassing en acceptatiebewijs nog worden vastgesteld. De huidige grote `main-product.liquid` is geen bewijs dat deze standaard volledig of betrouwbaar is gerealiseerd.

## 18. Eisen per producttype

| Producttype | Bevestigd doel | Open of geblokkeerd |
| --- | --- | --- |
| Standaard sanitairproduct | Zelfstandig product met eigen URL/SKU en relevante productpaginavelden | Datamapping, voorraad- en levertijdbron `[NOG ONDERZOEKEN]` |
| Tegel | m²-calculator voor oppervlakte, snijverlies, doosinhoud, hele dozen, prijs per m²/doos, totaal dozen en bestelde oppervlakte | Eenheden, afrondingsregels, prijsbron en cartgedrag `[OPEN BESLISSING]` |
| Doucheset | Configurator navigeert naar het passende bestaande product | Eigenschappen, groepen en datakwaliteit `[NOG ONDERZOEKEN]` |
| Badkamermeubel | Vergelijkbare configurator die naar een bestaand product navigeert | Eigenschappen, groepen en datakwaliteit `[NOG ONDERZOEKEN]` |
| Complete set, later | Uitgebreidere complete-badkamerconfigurator moet mogelijk blijven | Werking, bundeling, prijs, logistiek en fase `[OPEN BESLISSING]` |

Andere producttypes met een eigen calculator of configurator zijn `[NOG ONDERZOEKEN]`.

## 19. Assortiment en productkwaliteit

Het beoogde assortiment bestrijkt uiteindelijk de volledige badkamer- en tegelmarkt. Genoemde hoofdgroepen zijn kranen, douches, badkamermeubels, tegels, baden, toiletten, wastafels, spiegels, radiatoren, accessoires, installatiematerialen en serviceonderdelen.

Voor lancering moeten circa 20.000 producten volledig ingericht, correct gekoppeld, gecategoriseerd, doorzoekbaar en filterbaar zijn. Er is leveranciersdata beschikbaar met onder meer prijzen, afbeeldingen, teksten en specificaties; inhoud, formaat, dekking, kwaliteit en actualiteit zijn `[NOG ONDERZOEKEN]`.

Een productkwaliteitsmodel moet minimaal volledigheid, geldigheid, uniciteit, koppelingen, media, prijs, voorraad/levertijd, categorisering, filters, SEO en type-specifieke regels controleren. Drempelwaarden en uitzonderingsbeleid zijn `[OPEN BESLISSING]`.

## 20. Categorie- en navigatiearchitectuur

De exacte categorieboom moet opnieuw worden onderzocht en ontworpen. De huidige structuur is gedeeltelijk geïnspireerd op BadkamerXXL, maar mag niet blind worden gekopieerd.

Het doelmodel moet passen bij:

- het eigen assortiment en de circa 20.000 lanceringsproducten;
- zoekintentie en SEO;
- gebruiksgemak en schaalbaarheid;
- producteigenschappen en filterbaarheid;
- mobiel en desktop;
- merk-, advies-, inspiratie- en begrippenroutes.

`[GEBLOKKEERD]` Definitieve categorieën, URL's, menu's, collectievoorwaarden en redirects wachten op Admin-inventarisatie, assortimentanalyse en concurrentie-/SEO-onderzoek.

## 21. Zoekfunctie, filters en merchandising

De code bevat Dawn-achtige zoek-, predictive-search- en facetbasis plus BadkamerCity-zoekkaarten en een USP-strip. Functionele werking met het werkelijke assortiment en actieve apps is niet bewezen.

Voor lancering zijn vereist:

- vindbaarheid van relevante producten op Nederlandse zoektermen;
- filters die aansluiten op categorie en productdatamodel;
- consistente productkaarten en sortering;
- bruikbaar leeg-, fout- en nulresultaatgedrag;
- merchandisingregels zonder ongecontroleerde duplicate routes;
- mobiel, desktop en toetsenbordtests.

Zoekprovider, synoniemen, ranking, filtersets, merchandisingbeheer en meetwaarden zijn `[NOG ONDERZOEKEN]`.

## 22. SEO-architectuur

De SEO-architectuur moet samenhangende regels krijgen voor:

- categorieën en subcategorieën;
- merkpagina's en merk-categoriecombinaties;
- eigenschaplandingspagina's;
- advies, inspiratie en begrippen;
- interne links tussen producten, categorieën, merken en content;
- redirects en URL-migraties;
- indexatiebeheer;
- structured data;
- canonicalbeleid;
- preventie van duplicate content door filters, combinaties en productrelaties.

`[NOG ONDERZOEKEN]` Huidige indexatie, rankings, URL-inventaris, Search Console/data, redirects, canonical-uitvoer, structured data en contentdekking zijn niet in de bewijsdocumenten vastgesteld. Geen URL- of indexatiebesluit is daarom definitief.

## 23. Concurrentieonderzoek

BadkamerXXL, Sanitairwinkel en Sanitairkamer zijn op 2026-08-05 via een representatieve openbare read-only steekproef onderzocht. De projecteigenaar heeft `docs/COMPETITOR_SEO_ANALYSIS.md` diezelfde datum binnen de vastgelegde bewijsgrenzen goedgekeurd; `BC-DISC-002` is `DONE`.

Het rapport behandelt:

- hoe categorieën, subcategorieën, merken en eigenschappen zijn georganiseerd;
- welke zoekintenties en landingspaginatypen worden bediend;
- hoe filters, zoeken, productkaarten en productpagina's werken;
- hoe switchers, calculators, services en vertrouwen worden gepresenteerd;
- welke interne-link-, canonical-, indexatie- en structured-data-patronen zichtbaar zijn;
- welke mobiele en desktopinteracties binnen de gebruikte methode niet betrouwbaar testbaar waren;
- welke patronen passend zijn voor BadkamerCity en welke bewust niet;
- waar BadkamerCity onderscheidend kan zijn met prijs, advies, exclusieve merken en service.

Bewezen overeenkomsten zijn brede producthierarchieen, categoriespecifieke filters, prijs en leverinformatie op kaarten, uitgebreide PDP's, merk-/content-/serviceroutes, canonicals, breadcrumbs en structured data op kernpagina's. Zoekresultaten waren wegens robotsuitsluitingen niet onderzocht; werkelijke mobiele/visuele en toetsenbordinteractie, indexdekking en client-side functies bleven **NIET TOEGANKELIJK** of `[NOG ONDERZOEKEN]`. De menselijke goedkeuring bevestigt alleen afronding van het read-only onderzoek: resultaten blijven onderzoeksinput en zijn geen categorie-, URL-, filter-, PDP-, design-, SEO-, patroon- of implementatiebesluit en geven geen toestemming om concurrenten te kopieren.

## 24. Design system en gebruikerservaring

Het huidige rustige ontwerp is een bruikbare basis. Een gedeeltelijk of volledig herontwerp is toegestaan als aantoonbaar beter voor gebruiksgemak, conversie, toegankelijkheid, snelheid of schaalbaarheid. Rust, overzicht en vertrouwen moeten behouden blijven; mobiel is even belangrijk als desktop.

`[NOG ONDERZOEKEN]` Tokens, componentinventaris, visuele inconsistenties, contentpatronen, responsive gedrag, interactiestates en toegankelijkheidsbasis. `[OPEN BESLISSING]` Omvang van een herontwerp en de menselijke visuele richting.

Geen zichtbaar onderdeel wordt `DONE` zonder menselijke previewgoedkeuring.

## 25. Homepage

Aanwezig zijn custom secties voor hero, categorieën, shop-by-style, Mijn BadkamerCity en merken. `templates/index.json` bevat volgens de audit meerdere lege links of collectie-instellingen.

Voor afronding moeten doel, contenthiërarchie, categorie-ingangen, merken, inspiratie, advies, services, vertrouwen, mobiele volgorde en meetdoelen worden vastgesteld. Lege configuraties moeten bewust gevuld of conditioneel verborgen worden. Definitieve homepage-inhoud en prioriteit zijn `[OPEN BESLISSING]`.

## 26. Header, menu en footer

De header, subnavigatie, mega-menu, drawer, wishlist/showroomlinks en footer bevatten BadkamerCity-maatwerk. Meerdere headerlinks gebruiken momenteel `href="#"`, waaronder verwijzingen naar inspiratie, advies, showrooms, afspraak en zakelijk.

Vereist zijn een gevalideerde navigatieboom, echte linkdoelen, consistente mobiele/desktopbediening, toetsenbordtoegang en correcte relatie met categorieën, services en content. `[GEBLOKKEERD]` Definitieve links wachten op informatiearchitectuur en contentbesluiten.

## 27. Categorie- en collectiepagina's

Er zijn category-landing templates en secties, inclusief blokken voor subcategorieën. Er staat nog placeholdertekst in `templates/collection.category-landing.json`.

Het platform moet categorie-introductie, subcategorieën, filters, sortering, productgrid, merchandising, SEO-content, interne links en mobiel gedrag ondersteunen. Exacte templatevarianten en actieve toewijzingen zijn `[NOG ONDERZOEKEN]` via Shopify Admin.

## 28. Productkaarten

De repository bevat Dawn-achtige productkaarten en een custom zoekresultaatkaart. Een complete inventaris en consistentiecontrole over home, collectie, zoekresultaat, aanbevelingen en gerelateerde producten ontbreekt.

De kaartstandaard moet productidentiteit, media, merk, titel, prijs/adviesprijs, relevante statusinformatie, link, states en toegankelijkheid definiëren. Badges, voorraad/levertijd, snelle acties en vergelijk/reviewweergave zijn `[OPEN BESLISSING]` waar niet al door lanceringsscope bevestigd.

## 29. Productpagina's

`sections/main-product.liquid` is circa 143 KB en combineert layout, CSS, buybox, switcherfallback, specificaties en inline JavaScript. Dit is het grootste technische en regressierisico in de theme-code.

De productpagina moet naar de standaard van hoofdstuk 17 worden gebracht, per producttype worden getest en waar veilig technisch worden afgebakend. Refactoring is geen doel op zichzelf: gedrag, data, performance en toegankelijkheid moeten aantoonbaar verbeteren of beheersbaarder worden. `[GEBLOKKEERD]` Implementatie wacht op productdata-, switcher- en Adminbesluiten.

## 30. Winkelwagen en checkout

Dawn-basis voor cart en productformulier is aanwezig, maar de volledige winkelwagen- en checkoutreis is niet als lanceringsklaar bewezen.

Te valideren:

- aantallen, prijzen, fouten, beschikbaarheid en cartupdates;
- tegelhoeveelheden en eventuele calculatoruitvoer;
- productrelaties en aanvullende artikelen;
- levering via pakket, pallet, afhalen, gecombineerd of gesplitst;
- account/gastgedrag, betalingen en bevestiging `[NOG ONDERZOEKEN]`;
- grenzen tussen theme en Shopify checkout `[NOG ONDERZOEKEN]`;
- mobiel, desktop, toetsenbord en foutafhandeling.

## 31. Klantaccount en bestellingen

Klantaccount, bestelhistorie en bestelling volgen behoren tot de gewenste lanceringsfuncties. Dawn-achtige accounttemplates zijn aanwezig, maar configuratie, accountmodel, ordertrackingbron en end-to-end werking zijn `[NOG ONDERZOEKEN]`.

`[GEBLOKKEERD]` Implementatiekeuzes wachten op Admin- en app-inventarisatie en een operationele beslissing over tracking en klantenservice.

## 32. Verlanglijst

Een verlanglijst is lanceringsscope; de header bevat al een custom wishlistverwijzing. Een werkende gegevensbron, app, account-/gastmodel, synchronisatie en privacygedrag zijn niet bewezen.

`[OPEN BESLISSING]` Technische oplossing en functionele regels. `[GEBLOKKEERD]` Start pas na app-inventarisatie, UX-eisen en gegevensbesluit.

## 33. Samples

Samples bestellen is lanceringsscope. Welke productgroepen samples ondersteunen, of een sample een product/orderregel is, welke prijs, voorraad, limieten, verzending en opvolging gelden, is `[NOG ONDERZOEKEN]`.

`[GEBLOKKEERD]` Geen implementatie vóór commerciële, logistieke, data- en checkoutregels zijn goedgekeurd.

## 34. Offerte uploaden

Klanten moeten een bestaande offerte kunnen uploaden zodat BadkamerCity een betere aanbieding kan maken. Nodig zijn formulierinhoud, bestandstypen/-limieten, opslag, toegang, bewaartermijn, toestemming, beveiliging, routing, responstijd en operationele opvolging.

Al deze details zijn `[OPEN BESLISSING]`. De functie is `[GEBLOKKEERD]` tot privacy-, beveiligings- en bedrijfsprocescontrole is afgerond.

## 35. Laagsteprijsgarantie

Een laagsteprijsgarantie en aanvraagmogelijkheid behoren tot de propositie. Voorwaarden, bewijs, uitsluitingen, prijsvergelijking, besluitvorming, responstijd, juridische tekst en technische afhandeling zijn `[OPEN BESLISSING]`.

`[GEBLOKKEERD]` Publicatie of implementatie wacht op een goedgekeurd commercieel en operationeel beleid.

## 36. Afspraken en showroompropositie

Afspraak maken is lanceringsscope. Bezoek kan voorlopig op afspraak in de bestaande showroomomgeving van Harry Suiker. Communicatie over meer dan 1.000 m² is toegestaan onder voorbehoud van controle van de exacte openbare formulering.

`[OPEN BESLISSING]` Afspraakproces, beschikbaarheid, kanaal, bevestiging, locatievermelding en tekst. De site mag niet suggereren dat BadkamerCity al een zelfstandige eigen showroomlocatie heeft.

## 37. WhatsApp en chat

WhatsApp of chat behoort tot de gewenste lanceringsfuncties. Provider, openingstijden, toestemming, gegevensverwerking, routing, responstijd, fallback en meetplan zijn `[NOG ONDERZOEKEN]`.

`[GEBLOKKEERD]` Keuze en implementatie wachten op service-, privacy-, app- en analyticsbesluiten.

## 38. Inspiratie, advies en begrippen

Inspiratieartikelen en adviespagina's zijn lanceringsscope. Een begrippenlijststructuur is al in code aanwezig; uitleg-links in productspecificaties gebruiken nog placeholders.

Nodig zijn contenttypen, taxonomie, auteurschap, reviewproces, interne links, SEO-regels, actualiteit en koppeling aan producten/categorieën. `[NOG ONDERZOEKEN]` Bestaande contentvoorraad en actieve templates. Placeholderlinks moeten vóór lancering naar goedgekeurde inhoud leiden of bewust niet worden getoond.

## 39. Voorraad, levertijd en leveranciersregels

De voorraadstatus moet actueel zijn en de levertijd betrouwbaar. Werkelijke eigen voorraad kan snelle levering mogelijk maken, bijvoorbeeld de volgende werkdag. Ongeveer 90% van bestellingen/producten zal via dropshipping lopen; regels verschillen mogelijk per leverancier.

`[NOG ONDERZOEKEN]` Per leverancier: bron, updatefrequentie, voorraadbetekenis, cutoff, levertijd, uitzonderingen, backorders en foutafhandeling. Zonder deze regels kunnen geen definitieve klantbeloften worden gebouwd.

`BC-DATA-002` bewees lokaal alleen een boolean `available` in de Hotbath-switcherasset; alle 3.383 actuele waarden zijn `true`. Dit is geen voorraadhoeveelheid of levertijd. De actieve productsectie bevat bovendien een vaste tekst `Verwachte levertijd: 8 - 9 weken` zonder lokaal bewezen product- of leverancierbron. `BC-LOG-001` blijft daarom geblokkeerd.

## 40. Verzending, dropshipping en afhalen

Te ondersteunen levermethodes zijn pakketpost, palletlevering, afhalen, gecombineerde levering en gesplitste levering. Bij meerdere leveranciers kan een bestelling eerst naar het eigen magazijn gaan, gesplitst worden geleverd of in overleg met de klant worden afgehandeld.

`[OPEN BESLISSING]` Beslisregels, kosten, regio's, planning, communicatie, tracking, checkoutweergave en verantwoordelijkheid per scenario. Internationale bestel-/leverregels zijn `[NOG ONDERZOEKEN]`.

## 41. Retouren, garantie en service

Productpagina's moeten waar relevant retour-, garantie- en service-informatie tonen. Operationele regels, uitzonderingen per product/leverancier, termijnen, kosten, formulieren, routing en bronnen zijn `[NOG ONDERZOEKEN]`.

`[GEBLOKKEERD]` Klantteksten en functionaliteit wachten op goedgekeurd beleid en datamapping.

## 42. Productimport en datakwaliteit

De projectdefinitie verwacht leveranciersbestanden met prijzen, afbeeldingen, teksten en specificaties. `BC-DATA-002` heeft echter in de volledige lokale repository nul oorspronkelijke leveranciersbestanden, nul afgeleide Shopify-importbestanden en nul import-/generatiescripts gevonden. Alleen zes afgeleide switcherdata-assets en vijf direct relevante storefront-JavaScriptbestanden bestaan. De lokale nulmeting is menselijk goedgekeurd en wordt niet verlengd met zoekwerk buiten `CITY_MASTER`. Productonboarding voor circa 20.000 producten vereist later aanvullende oorspronkelijke bronnen en vervolgens een herhaalbaar proces voor mapping, validatie, fouten, duplicaten, media, relaties, categorieën, filters en SEO.

`BC-DATA-003` heeft zonder leveranciersbestanden uitsluitend de bestuurde conceptuele werkbasis v0.1 opgeleverd en is `DONE`. `[GEBLOKKEERD]` Importontwerp en `BC-DATA-001` wachten nog op oorspronkelijke Hotbath- en The Mosaic Factory-bronnen, eventuele overige leveranciersbronnen, bronhouders en waar bestaand generator-/mapping-/importbewijs. Definitieve leveranciermappings en Shopify-metafieldnamen/opslagkeuzes volgen pas na bronaanlevering en afzonderlijke menselijke beoordeling. Aanvullende leveranciersbestanden mogen later per leverancier in een eigen taak worden behandeld; het ontbreken ervan blokkeert niet de technische planningsopdracht `BC-TECH-002`, maar er wordt geen productdata gewijzigd.

## 43. Toekomstige API-koppelingen

API-koppelingen zijn geen eerste ontwikkelprioriteit. De architectuur en het datamodel moeten wel toekomstige product-, voorraad- en prijsfeeds ondersteunen. Het koppelen van API-data aan bestaande producten wordt een apart werkpakket.

Leveranciers, API-specificaties, authenticatie, limieten, updatefrequenties, foutafhandeling en eigenaarschap zijn `[NOG ONDERZOEKEN]`. De implementatie is `DEFERRED`; voorbereidende datamodelvereisten horen bij fase 2.

## 44. Performance

Bevestigde risico's:

- circa 1,85 MB ongecomprimeerde switcherdata op relevante productpagina's;
- meerdere grote backupdatasets in publiceerbare `assets`;
- veel inline CSS/JS in product- en zoeksecties;
- mogelijke extra fetches in de fallbackswitcher;
- debuglogging en omvangrijke kernbestanden.

`[NOG ONDERZOEKEN]` Huidige baselines, meetomgeving, kernpagina's en performancebudgetten. Optimalisatie moet vóór/na-bewijs leveren en functionele regressies uitsluiten.

## 45. Toegankelijkheid

Mobiel, desktop en toetsenbordbediening zijn expliciete eisen. De productpagina, switchers/configurators, calculator, navigatie, formulieren, modals, cart, search en content moeten toegankelijk worden getest.

`[NOG ONDERZOEKEN]` Huidige audit, doelstandaard, ondersteunde assistieve technologie en acceptatiedrempels. Geen toegankelijkheidsconformiteit wordt in versie 0.16 geclaimd.

## 46. Technische SEO

Technische SEO omvat minimaal crawlbaarheid, indexatie, canonicals, redirects, headings, metadata, structured data, interne links, facetten, paginering, duplicate content en foutstatussen.

De productpaginastandaard vereist correcte structured data, SEO-titel, metabeschrijving, headings, canonical en indexeringscontrole. Huidige productie-uitvoer en tooling zijn `[NOG ONDERZOEKEN]`; wijzigingen volgen pas na inventarisatie en SEO-architectuurbesluiten.

## 47. Privacy, beveiliging en gegevensuploads

Vooral offerteuploads, laagsteprijsgarantie, afspraken, chat, accounts, samples en analytics kunnen persoonsgegevens verwerken. Benodigde besluiten omvatten doel, minimale velden, toestemming, opslag, toegangsrechten, bewaartermijnen, verwijdering, leveranciers/verwerkers, logging en veilige bestandvalidatie.

Alle genoemde details zijn `[NOG ONDERZOEKEN]` of `[OPEN BESLISSING]`. Gegevensuploadfunctionaliteit is `[GEBLOKKEERD]` totdat eigenaar en relevante verantwoordelijke het proces hebben goedgekeurd.

## 48. Analytics, tracking en meetplan

`[NOG ONDERZOEKEN]` Huidige analytics-, consent-, advertentie- en appconfiguratie. Het meetplan moet kernreizen en zakelijke doelen verbinden, waaronder zoeken, filters, switcherkeuzes, calculatorgebruik, cart, aankoop, offerte, prijsgarantie, samples, wishlist, afspraak en chat.

Events, definities, eigenaarschap, consentregels, bewaartermijnen en rapportage zijn `[OPEN BESLISSING]`. Metingen mogen niet worden toegevoegd zonder privacy- en kwaliteitscontrole.

## 49. Teststrategie

De repository bevat geen zichtbare testinrichting, CI-configuratie of lintconfiguratie. Theme Check vond 1 error en 11 warnings en eindigde met een Windows assertion failure; sommige meldingen kunnen tooling-gerelateerd zijn.

De strategie moet per taak vastleggen:

- statische controles en Theme Check;
- data- en schemavalidatie;
- unit-/logische tests waar passend `[NOG ONDERZOEKEN]`;
- integratie- en end-to-end kernreizen;
- visuele vergelijking op preview;
- mobiel, desktop en toetsenbord;
- performance, toegankelijkheid en technische SEO;
- fout-, leeg-, grens- en rollbackscenario's;
- menselijke goedkeuring en bewijsopslag.

Geen implementatie mag `REVIEW` worden zonder taakgebonden technische controles.

## 50. Browser- en apparaatondersteuning

Mobiel en desktop zijn gelijkwaardig belangrijk. De exacte browser-, OS-, viewport- en apparaatmatrix is `[OPEN BESLISSING]` en moet met feitelijk gebruikers-/analyticsbewijs worden onderbouwd zodra beschikbaar.

Tot die beslissing mag een taak niet claimen dat volledige browserondersteuning bewezen is. Kritieke journeys moeten in de goedgekeurde matrix en minimaal met toetsenbord worden gecontroleerd.

## 51. Git-, branch- en commitstrategie

Bevestigde regels:

- GitHub `main` bevat de goedgekeurde centrale basis.
- Alleen expliciet gevraagde bestanden worden gestaged en gecommit.
- Theme-ontwikkeling gebeurt niet direct op live.
- Menselijke goedkeuring bepaalt wanneer zichtbaar/functioneel werk `DONE` wordt.
- Shopify-publicatie staat los van Git-commit en vereist expliciete menselijke toestemming.

`[OPEN BESLISSING]` Branchnaamconventie, pull-requestproces, reviewers, mergewijze, verplichte checks, commitgranulariteit en hotfixproces. Deze moeten vóór de eerste implementatietaak worden vastgelegd.

## 52. Shopify preview-, release- en rollbackproces

Bevestigde omgevingen:

- live: `Categoriepagina_v1.0` (`189463068938`);
- preview/development: unpublished `BadkamerCity Development` (`192770375946`).

Minimale gates:

1. taak is `READY` en wijzigingen zijn op een niet-live werkwijze uitgevoerd;
2. technische controles slagen vóór `REVIEW`;
3. zichtbare/functionele wijzigingen zijn op preview door de eigenaar goedgekeurd vóór `DONE`;
4. live-publicatie gebeurt alleen na afzonderlijke expliciete menselijke goedkeuring;
5. Codex neemt nooit zelfstandig aan dat preview naar productie mag;
6. releasebewijs en post-releasecontrole worden vastgelegd.

`[OPEN BESLISSING]` Exacte pushscope, releasevenster, backup, rollbacktheme/-commit, verantwoordelijkheden en noodprocedure. Tot dit is vastgesteld, is productiepublicatie `[GEBLOKKEERD]`.

## 53. Definition of Ready

Een taak is alleen `READY` wanneer:

- doel, scope en buiten-scope duidelijk zijn;
- eigenaar en menselijke beslisser bekend zijn;
- afhankelijkheden zijn afgerond of expliciet beschikbaar;
- benodigde Shopify-/data-/contentinput beschikbaar en gevalideerd is;
- open beslissingen die implementatie veranderen zijn genomen;
- verwachte bestanden en systemen zijn afgebakend;
- acceptatiecriteria en technische controles meetbaar zijn;
- privacy-, beveiligings-, SEO-, performance- en toegankelijkheidsimpact is beoordeeld waar relevant;
- preview-, bewijs- en herstelwijze zijn afgesproken;
- de taak klein genoeg is om afzonderlijk te beoordelen;
- het masterplan is bijgewerkt; voor implementatietaken is ontwikkeling expliciet toegestaan.

Voorlopige epics in hoofdstuk 57 die te breed zijn, moeten vóór `READY` worden opgesplitst.

## 54. Definition of Done

Een taak is alleen `DONE` wanneer:

- de afgesproken uitvoer volledig binnen scope is geleverd;
- alle acceptatiecriteria aantoonbaar zijn gehaald;
- technische controles slagen en resultaten zijn vastgelegd;
- geen onverklaarde theme-, Admin- of datawijziging aanwezig is;
- relevante regressie-, mobiel-, desktop-, toetsenbord-, performance-, toegankelijkheids- en SEO-controles zijn uitgevoerd;
- documentatie, taakrecord, risico's, open vragen, bewijsregister, dashboard en wijzigingslog zijn bijgewerkt;
- rollback/herstelwijze is gecontroleerd;
- de eigenaar zichtbare of functionele uitkomsten expliciet heeft goedgekeurd;
- de statusovergang en datum zijn vastgelegd.

Een technische implementatie zonder menselijke zichtbare/functionele goedkeuring blijft maximaal `REVIEW`. Live-publicatie is een afzonderlijke taak en nooit impliciet onderdeel van `DONE`.

## 55. Projectfasen

| Fase | Naam | Huidige status | Kernuitvoer | Gate naar volgende fase |
| ---: | --- | --- | --- | --- |
| 0 | Fundament en projectbesturing | `DONE` | Menselijk goedgekeurd permanent protocol, `AGENTS.md`-guardrails, Git-ignore, vier PowerShell-scripts en one-bundle reviewflow met raw completeness en `review_files/` | Eerste onafhankelijke toekomstige taak gebruikt het protocol; implementatie blijft niet goedgekeurd |
| 1 | Volledige inventarisatie | `DONE` | Shopify Admin-, actieve theme-, app-, data- en concurrentieonderzoeken | Op 2026-08-05 menselijk afgerond; bewijsgrenzen en open besluiten blijven bestaan |
| 2 | Informatiearchitectuur en datamodel | `BLOCKED` | Leveranciersnulmeting en brononafhankelijk productinformatiecontract v0.1 `DONE`; definitieve data-/IA-uitvoer geblokkeerd | Oorspronkelijke bronnen plus afzonderlijke besluiten over veldcatalogus, Shopify-opslag, producttypen, categorieboom en filters |
| 3 | Technische stabilisatie | `BLOCKED` | Read-only decompositie `BC-TECH-002` is `DONE`; geen kandidaat of technische uitvoering actief | Afzonderlijke officiele taak, exacte scope en expliciete menselijke implementatietoestemming |
| 4 | Design system en globale websiteonderdelen | `BLOCKED` | UX-richting, componentregels, homepage, header en footer | Menselijke visuele goedkeuring en componentbewijs |
| 5 | Categorieën, zoeken en filters | `BLOCKED` | Categorieplatform, productkaarten, zoeken, filters en merchandising | Kernreizen en SEO-routes goedgekeurd |
| 6 | Productpaginaplatform | `BLOCKED` | Productpaginastandaard en producttypebasis | Data-, functionele en visuele acceptatie gehaald |
| 7 | Switchers, calculators en configurators | `BLOCKED` | Gevalideerde switcher, tegelcalculator en productconfigurators | Datamatches, grensgevallen en navigatie bewezen |
| 8 | Conversie- en servicefuncties | `BLOCKED` | Wishlist, samples, offerte, prijsgarantie, account, afspraak en chat | Bedrijfsproces, privacy en UX goedgekeurd |
| 9 | Logistiek, voorraad en leveringslogica | `BLOCKED` | Leverancierregels, voorraad, levertijd, verzending, retour en service | Klantbeloften en uitvoering end-to-end bewezen |
| 10 | SEO-, inspiratie- en adviesstructuur | `BLOCKED` | SEO-architectuur, contenttypen en interne links | Indexatie- en contentregels goedgekeurd |
| 11 | Productonboarding en datakwaliteit voor 20.000 producten | `BLOCKED` | Gevalideerde productimport en kwaliteitsrapport | Afgesproken productdoel en kwaliteitsdrempels gehaald |
| 12 | Integrale QA, performance en toegankelijkheid | `BLOCKED` | Volledige testmatrix en opgelost/onaanvaardbaar restrisico | Geen open P0 en menselijke review gereed |
| 13 | Launch readiness en productiepublicatie | `BLOCKED` | Go/no-go, release, rollback en productiecontrole | Expliciete menselijke publicatiegoedkeuring |
| 14 | Monitoring, optimalisatie en toekomstige API's | `DEFERRED` | Monitoring, optimalisaties en afzonderlijke feedintegraties | Prioriteit na lancering `[OPEN BESLISSING]` |

Fasen mogen iteratief overlappen voor onderzoek, maar implementatiegates en afhankelijkheden mogen niet worden omzeild. `BC-TECH-002`, `BC-GOV-006` en fase 0 zijn menselijk goedgekeurd en `DONE`; fase 3 blijft `BLOCKED` voor technische uitvoering en fase 2 blijft voor definitieve data-/IA-uitvoer `BLOCKED`. Er is geen actieve taak of technische kandidaat.

## 56. Werkstromen

| Werkstroom | Verantwoordelijkheid | Primaire taken |
| --- | --- | --- |
| Governance / tooling / bewijs | Bron van waarheid, status, besluiten, goedkeuring, uitvoeringslogging en uploadbaar bewijs | `BC-GOV-*`, `BC-REL-*` |
| Onderzoek | Repository-, gebruiks-, markt- en concurrentiebewijs | `BC-DISC-*` |
| Shopify Admin | Read-only inventaris en actieve configuratie | `BC-ADM-001` |
| Datamodel | Read-only leveranciersbronneninventaris, brononafhankelijk logisch productcontract, productvelden, relaties, bronnen en validatie | `BC-DATA-002`, `BC-DATA-003`, `BC-DATA-001` |
| Producten | Productpaginaplatform en productkwaliteit | `BC-PDP-*`, `BC-PROD-*` |
| Switcher | Huidige dubbele implementatie en doelarchitectuur | `BC-SWITCH-001` |
| Configurators | Douchesets, meubels en later complete sets | `BC-CONF-*` |
| Tegels | m²-calculator en tegeldata | `BC-TILE-001` |
| SEO | Structuur, techniek, indexatie en concurrentieonderzoek | `BC-SEO-001`, `BC-DISC-002` |
| Categorieën | Informatiearchitectuur, collectieplatform en navigatie | `BC-IA-001`, `BC-CAT-001` |
| UX/design | Design system, globale onderdelen en kernreizen | `BC-UX-001` |
| Development / QA / onderzoek | Read-only stabilisatieplanning, technische nulmeting en later afzonderlijk gecontroleerde implementatie | `BC-TECH-002`, `BC-TECH-001` en latere implementatietaken |
| Performance | Budget, meting en optimalisatie | `BC-QA-001` |
| Accessibility | Toetsenbord en toegankelijke componenten/reizen | `BC-QA-001` |
| Logistiek | Voorraad, levertijd, dropshipping en verzending | `BC-LOG-*` |
| Service | Account, afspraak, chat, retour en garantie | `BC-SVC-*`, `BC-ACC-001` |
| Content | Product-, inspiratie-, advies- en begrippencontent | `BC-SEO-001`, `BC-PROD-001` |
| Privacy en analytics | Uploads, persoonsgegevens, consent en metingen | `BC-SEC-001`, `BC-ANA-001` |
| QA | Integrale functionele, visuele en technische controle | `BC-QA-001` |
| Release | Preview, go/no-go, publicatie, rollback en monitoring | `BC-REL-*`, `BC-OPS-*` |

## 57. Centraal taakregister

Dit zijn voorlopige werkpakketten. Een breed werkpakket moet vóór status `READY` worden opgesplitst in afzonderlijk testbare taken. Prioriteit `P0` is een harde project- of launchgate, `P1` is nodig voor de bevestigde lanceringsscope en `P2` is bevestigd later werk.

| Status | Aantal |
| --- | ---: |
| `DONE` | 12 |
| `READY` | 0 |
| `IN_PROGRESS` | 0 |
| `NOT_STARTED` | 0 |
| `BLOCKED` | 26 |
| `REVIEW` | 0 |
| `DEFERRED` | 3 |
| **Totaal** | **41** |

### BC-GOV-001 - Repository-audit

- **ID:** `BC-GOV-001`
- **Titel:** Volledige repository-audit uitvoeren en documenteren
- **Fase:** Fase 0 - fundament en projectbesturing
- **Werkstroom:** Governance / onderzoek
- **Status:** `DONE`
- **Prioriteit:** `P0`
- **Doel:** De technische opbouw, custom functies, onvolledigheid, switcher, oude bestanden, risico's en documentatiegaten vastleggen.
- **Aanleiding:** Er was geen centrale technische nulmeting.
- **Scope:** Read-only analyse van de volledige repository en rapportage.
- **Buiten scope:** Theme-code wijzigen, Shopify wijzigen, defects oplossen.
- **Afhankelijkheden:** Geen; voorbereidende nulmeting.
- **Benodigde input:** Lokale repository.
- **Verwachte bestanden/systemen:** Repository read-only; `docs/REPOSITORY_AUDIT.md`.
- **Uitvoer:** Repository-audit met negen onderzoeksgebieden en prioriteiten.
- **Acceptatiecriteria:** Audit bevat alle gevraagde gebieden, belangrijkste bevindingen, risico's, volgorde en bestandsverantwoording.
- **Technische controles:** Bestandsstructuur, referenties, switcherdata en Theme Check zijn onderzocht; Theme Check-beperking is vastgelegd.
- **Menselijke controle:** Gebruiker gaf na oplevering expliciet opdracht het rapport te committen en pushen.
- **Bewijs van voltooiing:** `docs/REPOSITORY_AUDIT.md`; commit `e1d655e`.
- **Risico:** Audit is een momentopname en bewijst geen runtimegedrag.
- **Rollback of herstelwijze:** Alleen via een nieuwe, beoordeelde documentatiecommit corrigeren; geen theme-rollback nodig.
- **Laatst bijgewerkt:** 2026-08-03.

### BC-GOV-002 - Shopify-omgeving vastleggen

- **ID:** `BC-GOV-002`
- **Titel:** Gekoppelde store en themestatussen read-only vaststellen
- **Fase:** Fase 0 - fundament en projectbesturing
- **Werkstroom:** Governance / Shopify Admin
- **Status:** `DONE`
- **Prioriteit:** `P0`
- **Doel:** Store, live theme en bestaande unpublished themes identificeren.
- **Aanleiding:** Veilige ontwikkeling vereist een bekende productieomgeving.
- **Scope:** `shopify theme info`, `shopify theme list` en documentatie.
- **Buiten scope:** Pull, push, publicatie, verwijdering of Admin-wijziging.
- **Afhankelijkheden:** `BC-GOV-001` als context.
- **Benodigde input:** Bestaande read-only Shopify CLI-authenticatie.
- **Verwachte bestanden/systemen:** Shopify CLI read-only; `docs/SHOPIFY_ENVIRONMENT.md`.
- **Uitvoer:** Store- en themestatusrapport.
- **Acceptatiecriteria:** Store, live theme-ID/status en onzekerheden zijn vastgelegd.
- **Technische controles:** Beide voorgeschreven CLI-commando's zijn uitgevoerd.
- **Menselijke controle:** Gebruiker gaf na oplevering expliciet opdracht het rapport te committen en pushen.
- **Bewijs van voltooiing:** `docs/SHOPIFY_ENVIRONMENT.md`; commit `ff8ceaf`.
- **Risico:** De controle bewees nog geen inhoudelijke live-pariteit.
- **Rollback of herstelwijze:** Niet van toepassing op Shopify; documentcorrectie via beoordeelde commit.
- **Laatst bijgewerkt:** 2026-08-03.

### BC-GOV-003 - Live-pariteit verifiëren

- **ID:** `BC-GOV-003`
- **Titel:** Lokale theme-code gecontroleerd vergelijken met live
- **Fase:** Fase 0 - fundament en projectbesturing
- **Werkstroom:** Governance / QA
- **Status:** `DONE`
- **Prioriteit:** `P0`
- **Doel:** Bewijzen of `CITY_MASTER` technisch dezelfde theme-bestanden bevat als live.
- **Aanleiding:** De omgevingscontrole kon die gelijkheid niet vaststellen.
- **Scope:** Tijdelijke live-download buiten de repository en SHA-256-vergelijking van zeven theme-mappen.
- **Buiten scope:** Externe Shopify-data, live overschrijven, theme-code wijzigen.
- **Afhankelijkheden:** `BC-GOV-002`.
- **Benodigde input:** Store `fpa9hu-i3.myshopify.com` en live theme-ID `189463068938`.
- **Verwachte bestanden/systemen:** `CITY_MASTER`, tijdelijke map `CITY_LIVE_COMPARE_20260803`, Shopify CLI read-only, `docs/LIVE_THEME_COMPARISON.md`.
- **Uitvoer:** Pariteitsrapport voor 396 lokale en 396 live bestanden.
- **Acceptatiecriteria:** Alleen-lokaal, alleen-live en inhoudelijk verschillend zijn afzonderlijk gerapporteerd.
- **Technische controles:** Relatieve paden en SHA-256-hashes; alle drie verschilcategorieën telden nul.
- **Menselijke controle:** Gebruiker gaf expliciet opdracht het rapport met de opgegeven commit te publiceren.
- **Bewijs van voltooiing:** `docs/LIVE_THEME_COMPARISON.md`; commit `badd5cf`.
- **Risico:** Bewijs geldt voor theme-bestanden en datum 2026-08-03, niet voor Admin-data of latere wijzigingen.
- **Rollback of herstelwijze:** Geen Shopify-herstel nodig; vergelijking opnieuw read-only uitvoeren bij twijfel.
- **Laatst bijgewerkt:** 2026-08-03.

### BC-GOV-004 - Development-theme inrichten

- **ID:** `BC-GOV-004`
- **Titel:** Afzonderlijk unpublished preview-theme aanmaken
- **Fase:** Fase 0 - fundament en projectbesturing
- **Werkstroom:** Governance / release
- **Status:** `DONE`
- **Prioriteit:** `P0`
- **Doel:** Een niet-live omgeving voor toekomstige previews beschikbaar maken.
- **Aanleiding:** Nieuwe ontwikkeling mag niet rechtstreeks op live plaatsvinden.
- **Scope:** Huidige repository eenmalig als nieuw unpublished theme uploaden en themelijst controleren.
- **Buiten scope:** Publiceren, live overschrijven, bestaand `BadkamerCity V1.0` overschrijven, verwijderen of code wijzigen.
- **Afhankelijkheden:** `BC-GOV-003`.
- **Benodigde input:** Goedgekeurde lokale basis en expliciete uploadopdracht.
- **Verwachte bestanden/systemen:** Shopify theme library; `BadkamerCity Development` (`192770375946`); `docs/DEVELOPMENT_THEME.md`.
- **Uitvoer:** Afzonderlijk unpublished theme met preview- en editorlink.
- **Acceptatiecriteria:** Nieuw ID, role `unpublished`, live theme onveranderd en bestaand unpublished theme onveranderd.
- **Technische controles:** `shopify theme list` na upload bevestigde alle drie themes en rollen.
- **Menselijke controle:** Gebruiker gaf expliciet opdracht voor upload en daarna voor commit van het rapport.
- **Bewijs van voltooiing:** `docs/DEVELOPMENT_THEME.md`; commit `3e0b4ec`.
- **Risico:** Preview is alleen een technische kopie; externe data en volledige functionaliteit zijn niet gevalideerd.
- **Rollback of herstelwijze:** Geen verwijdering zonder expliciete menselijke opdracht; theme blijft unpublished.
- **Laatst bijgewerkt:** 2026-08-03.

### BC-GOV-005 - Masterplanbasis en onderzoeksgovernance

- **ID:** `BC-GOV-005`
- **Titel:** Centraal levend masterplan opbouwen, valideren en discovery-governance activeren
- **Fase:** Fase 0 - fundament en projectbesturing
- **Werkstroom:** Governance
- **Status:** `DONE`
- **Prioriteit:** `P0`
- **Doel:** Eén centrale bron voor visie, scope, architectuur, fasen, taken, besluiten, risico's, bewijs en volgende stappen maken.
- **Aanleiding:** De vier bewijsrapporten zijn afzonderlijk en er ontbreekt projectbrede besturing.
- **Scope:** Versie 0.1 op basis van de projectdefinitie en vier bestaande documenten bouwen, valideren en als onderzoeksbasis laten goedkeuren.
- **Buiten scope:** Theme-code, Shopify-data, implementatie, publicatie en onbewezen technische invulling.
- **Afhankelijkheden:** `BC-GOV-001` t/m `BC-GOV-004`.
- **Benodigde input:** Projectdefinitie, audit-, omgeving-, pariteits- en development-themebewijs.
- **Verwachte bestanden/systemen:** `docs/MASTERPLAN.md`, rootbestand `AGENTS.md` en GitHub `main`.
- **Uitvoer:** Dit masterplan met 65 hoofdstukken en 37 voorlopige taken, plus permanente Codex-guardrails in `AGENTS.md`.
- **Acceptatiecriteria:** Verplichte structuur is compleet; onbekenden zijn gemarkeerd; statussen, criteria, afhankelijkheden, bewijs en actuele route zijn consistent; discovery en implementatie zijn duidelijk gescheiden.
- **Technische controles:** Structuur-, telling-, marker-, duplicaat-, status-, route-, instructie-, scope- en Git-diffcontrole.
- **Menselijke controle:** De projecteigenaar heeft versie 0.1 op 2026-08-04 expliciet goedgekeurd als basis voor verder onderzoekswerk, niet voor implementatie.
- **Bewijs van voltooiing:** `docs/MASTERPLAN.md`; fundamentcommit `302a42a` (`docs: add BadkamerCity masterplan foundation`); governancecommit `d22e3e32d04fc472996064cc14cff922396c2d05` (`docs: activate discovery workflow and add Codex guidance`); menselijke onderzoeksgoedkeuring van 2026-08-04.
- **Risico:** Onderzoeksgoedkeuring kan ten onrechte als implementatietoestemming worden gelezen; versie 0.16 blokkeert implementatie daarom expliciet.
- **Rollback of herstelwijze:** Corrigeer of revert uitsluitend via een afzonderlijke beoordeelde documentatiecommit.
- **Laatst bijgewerkt:** 2026-08-04.

### BC-GOV-006 - Permanent Codex-uitvoeringslogboek en uploadprotocol

- **ID:** `BC-GOV-006`
- **Titel:** Permanent Codex-uitvoeringslogboek en uploadprotocol inrichten
- **Fase:** Fase 0 - fundament en projectbesturing
- **Werkstroom:** Governance / tooling / bewijs
- **Status:** `DONE`
- **Prioriteit:** `P0`
- **Doel:** Iedere toekomstige Codex-taak volledig controleerbaar maken door alle zichtbare commando's, stdout, stderr, exitcodes, fouten, herstelhandelingen, bestandswijzigingen, validatorresultaten en eindcontroles lokaal in een uploadbaar bewijsbestand vast te leggen, terwijl de terminaluitvoer kort blijft.
- **Aanleiding:** Lange Codex-sessies klappen terminaluitvoer in, kunnen context comprimeren en maken het moeilijk om alle uitgevoerde controles en fouten later aan ChatGPT te verstrekken.
- **Scope:** Een permanent protocol, `AGENTS.md`-guardrails, lokale Git-ignore, herbruikbare Windows PowerShell-scripts, lokaal runmapformaat, fout-/outputregistratie, bestandswijzigingsregistratie, uploadmanifest, bundelvorming en zelftests.
- **Buiten scope:** Verborgen interne redeneerstappen opslaan, credentials loggen, persoonsgegevens loggen, externe telemetry, cloudlogging, CI, Shopify-toegang, theme-code, productdata, technische stabilisatiefixes of livepublicatie.
- **Afhankelijkheden:** `BC-GOV-005` en `BC-TECH-002` zijn `DONE`.
- **Benodigde input:** Huidige repository, `AGENTS.md`, dit masterplan, Windows PowerShell en ingebouwde .NET-functionaliteit.
- **Verwachte bestanden/systemen:** `.gitignore`; `AGENTS.md`; `docs/CODEX_EXECUTION_LOG_PROTOCOL.md`; `scripts/codex-run-init.ps1`; `scripts/codex-run-command.ps1`; `scripts/codex-run-note.ps1`; `scripts/codex-run-finalize.ps1`; lokale genegeerde runs onder `docs/_codex_runs/`; dit masterplan.
- **Uitvoer:** `docs/CODEX_EXECUTION_LOG_PROTOCOL.md`, permanente `AGENTS.md`-guardrails, `.gitignore`, vier PowerShell-helpers en de lokaal genegeerde reviewfix-run `BC-GOV-006-REVIEWFIX_20260811-173707` met volledig log, raw evidence, eindrapport, uploadmanifest, `REVIEW_FILES_MANIFEST.md`, hashgecontroleerde `review_files/` en een zelfstandige finale bundle.
- **Acceptatiecriteria:** Het protocol registreert per shellcommando opdracht, context, gescheiden streams, exitcode, timing, bytes en hashes; iedere commandostap heeft een compleet en uniek raw quartet. De finalizer weigert onveilige reviewpaden, controleert bron-/kopie-/bundlehashes, valideert een tijdelijke ZIP en promoveert die pas daarna. Een normale ChatGPT-review vereist uitsluitend de finale bundle. Fouten en herstel blijven zichtbaar, runbewijs blijft genegeerd en secrets/persoonsdata worden niet letterlijk gelogd.
- **Technische controles:** Vier PowerShell-parsers, cmdlet-errorzelftest, normale succes- en gescheiden-streamtest, UTF-8, Sensitive-redactie, hergebruikt groot-uitvoerbewijs, positieve one-bundle-test, negatieve quartettest, verboden-bestandsnaamtest, raw completeness, reviewhashes, building-ZIP-promotie, `git check-ignore`, Git-whitelist, `git diff --check` en secret-/privacyscan.
- **Menselijke controle:** De projecteigenaar heeft het protocol op 2026-08-11 inhoudelijk goedgekeurd nadat REVIEW-FIX-001, REVIEW-FIX-002 en REVIEW-FIX-003 aantoonbaar zijn opgelost. Individuele technische kandidaten en implementatie blijven afzonderlijke besluiten.
- **Menselijk goedgekeurd:** 2026-08-11.
- **Bewijs van voltooiing:** De eerdere run `BC-GOV-006_20260811-131019` bewijst de basis; reviewfix-run `docs/_codex_runs/BC-GOV-006-REVIEWFIX_20260811-173707/` bewijst de drie fixes, positieve en negatieve tests, complete raw evidence, hashgelijke reviewbestanden, atomische one-bundle-integriteit, deze commit en push naar `main`. De finale siblingbundle is het enige normale reviewbestand.
- **Risico:** Een onvolledig protocol kan alsnog uitvoer verliezen. Een te ruim protocol kan secrets of persoonsgegevens loggen. Interne editoracties zijn niet automatisch shelloutput en moeten daarom via een expliciete note plus Git-diff worden vastgelegd.
- **Rollback of herstelwijze:** Tracked protocolbestanden via een afzonderlijke beoordeelde commit terugdraaien; lokale genegeerde runbestanden kunnen na menselijke goedkeuring handmatig worden verwijderd.
- **Laatst bijgewerkt:** 2026-08-11; menselijk goedgekeurd en technisch gehard.

### BC-ADM-001 - Read-only Shopify Admin-inventarisatie

- **ID:** `BC-ADM-001`
- **Titel:** Shopify Admin-data en actieve configuratie volledig read-only inventariseren
- **Fase:** Fase 1 - volledige inventarisatie
- **Werkstroom:** Shopify Admin / onderzoek
- **Status:** `DONE`
- **Prioriteit:** `P0`
- **Doel:** De externe werkelijkheid vastleggen die niet door live-pariteit van theme-bestanden is bewezen.
- **Aanleiding:** Producten, collecties, metafields, metaobjects, menu's, apps, instellingen en actieve templates waren buiten de lokale theme-snapshot onvoldoende bewezen.
- **Scope:** Read-only inventaris met bron, datum, aantallen/structuur waar beschikbaar, actieve koppelingen en onzekerheden.
- **Buiten scope:** Ieder type Admin-, product-, data-, theme- of appwijziging.
- **Afhankelijkheden:** `BC-GOV-005` en `BC-GOV-006` zijn `DONE`; de projecteigenaar heeft historisch de officiële Shopify CLI `store auth`-route, de store en dertien read-scopes expliciet goedgekeurd. Versie 0.16 activeert geen Shopify-taak en blokkeert nieuwe Shopify-benadering; er is geen actieve taak.
- **Benodigde input:** Volledig ontvangen en gebruikt: Shopify CLI `4.6.0`, store `fpa9hu-i3.myshopify.com`, uitsluitend de verleende read-scopes en expliciete menselijke beoordeling van rapport, beperkingen en onzekerheden.
- **Verwachte bestanden/systemen:** Shopify Admin read-only, `docs/SHOPIFY_ADMIN_INVENTORY.md` en dit masterplan.
- **Uitvoer:** Volledig bijgewerkt `docs/SHOPIFY_ADMIN_INVENTORY.md` met aantallen, structuren, representatieve steekproeven, queryfamilies, scopes, statuslabels, beperkingen, gevolgen en aanbevolen vervolgstap.
- **Acceptatiecriteria:** Gehaald binnen de expliciet toegestane bronnen: alle gevraagde domeinen zijn onderzocht of exact als **NIET TOEGANKELIJK** / `[NOG ONDERZOEKEN]` begrensd; er is geen volledige productdump opgenomen, niets in Shopify of theme-code gewijzigd en de projecteigenaar heeft de uitkomst op 2026-08-04 expliciet goedgekeurd.
- **Technische controles:** `currentAppInstallation.accessScopes` zonder write-scopes; gepagineerde read-only queryfamilies voor producten, varianten, collecties, metafields, metaobjects, menu's, pagina's, themes/files, markets, talen, accounts/checkout, locaties, inventory en shipping; volledige resultaatsamenvattingen; live/local inhoudscontrole; geen GraphQL-mutaties of `--allow-mutations`.
- **Menselijke controle:** De projecteigenaar heeft `docs/SHOPIFY_ADMIN_INVENTORY.md` en masterplan versie 0.3 op 2026-08-04 beoordeeld en `BC-ADM-001` expliciet als afgeronde read-only inventarisatie goedgekeurd.
- **Bewijs van voltooiing:** `docs/SHOPIFY_ADMIN_INVENTORY.md`, dit masterplan, read-only CLI-uitvoer, menselijke goedkeuring van 2026-08-04 en documentatiecommit `docs: approve Shopify Admin inventory`.
- **Risico:** De ontbrekende volledige app-/pixelbron en de begrensde specificatiesteekproef kunnen ten onrechte als bewezen afwezigheid worden gelezen; het rapport scheidt deze beperkingen expliciet.
- **Blokkade:** Geen blokkade voor deze afgeronde taak. De vastgelegde bronbeperkingen en open vragen blijven bestaan; aanvullende scopes, Shopify-wijzigingen en implementatie blijven buiten toestemming.
- **Rollback of herstelwijze:** Niet van toepassing bij strikt read-only uitvoering; onmiddellijk stoppen bij onverwachte mutatieroute.
- **Laatst bijgewerkt:** 2026-08-04.

### BC-DISC-001 - Actief theme- en appgebruik inventariseren

- **ID:** `BC-DISC-001`
- **Titel:** Actieve templates, sections, snippets, app-embeds en contentkoppelingen in kaart brengen
- **Fase:** Fase 1 - volledige inventarisatie
- **Werkstroom:** Onderzoek / Shopify Admin
- **Status:** `DONE`
- **Prioriteit:** `P0`
- **Doel:** Onderscheiden welke huidige code actief, legacy, experimenteel of ongebruikt is.
- **Aanleiding:** De audit vond losse oude productsecties, backupbestanden en mogelijke defecten. `BC-ADM-001` bewees de actieve JSON-configuratie, maar nog niet de volledige runtimegebruiksmatrix of alle app-/pixelafhankelijkheden.
- **Scope:** Read-only mapping tussen templates/configuratie, sections, snippets, assets en aantoonbare app-/dynamische injectiepunten, inclusief de auditverdachten en beide switcherpaden.
- **Buiten scope:** Bestanden verwijderen, templates wijzigen, apps configureren of code herstellen.
- **Afhankelijkheden:** `BC-ADM-001` is `DONE`; de projecteigenaar heeft op 2026-08-04 een expliciete read-only startopdracht voor `BC-DISC-001` gegeven met verbod op Shopify-/theme-/scope-/app-/repositorycodewijzigingen.
- **Benodigde input:** Gebruikt: goedgekeurd Admin-inventarisrapport, live/local bytegelijke JSON-configuratie, lokale repository, Shopify CLI `4.6.0` en uitsluitend reeds verleende read-scopes. De volledige app-/pixelbron bleef niet toegankelijk.
- **Verwachte bestanden/systemen:** Repository read-only, Shopify Admin read-only, `docs/ACTIVE_THEME_USAGE.md` en dit masterplan.
- **Uitvoer:** `docs/ACTIVE_THEME_USAGE.md` met classificaties voor alle 396 bestanden, actieve template-/sectionmatrix, auditverdachten, beide switchers, backup/debug, appinjectie, contentkoppelingen, beperkingen, risico's en veilige vervolgstappen.
- **Acceptatiecriteria:** Gehaald: ieder auditverdacht bestand heeft een onderbouwde status; de volledige repositoryscope is sluitend geclassificeerd; dynamische/ontoegankelijke delen zijn begrensd; niets in Shopify of theme-code is gewijzigd; de projecteigenaar heeft het rapport op 2026-08-05 binnen deze grenzen goedgekeurd.
- **Technische controles:** Vooraf schoon `main` en `HEAD == origin/main`; live/local bodyvergelijking van 18 JSON-configuratiebestanden en acht overige templates; JSON-parsing; volledige statische referentieanalyse van 396 bestanden; gerichte JavaScript-sectionroutes, hashes, instellingen, switcherdata en appinjectiepunten; geen mutaties, `--allow-mutations`, theme-pull/push of codewijziging.
- **Menselijke controle:** De projecteigenaar heeft `docs/ACTIVE_THEME_USAGE.md` en masterplan versie 0.5 op 2026-08-05 goedgekeurd als afgerond read-only onderzoek. De classificaties zijn geen verwijdertoestemming; alle runtime-, app-, pixel- en switcherdatabeperkingen blijven bestaan.
- **Bewijs van voltooiing:** `docs/ACTIVE_THEME_USAGE.md`, dit masterplan, de read-only Shopify CLI-/repositorycontroles van 2026-08-04, menselijke goedkeuring van 2026-08-05 en documentatiecommit `docs: approve active theme usage inventory`.
- **Risico:** Statische afwezigheid is geen verwijderbewijs; dynamische Theme Editor-, section-rendering-, app-, pixel- of runtimepaden kunnen gemist zijn. De volledige app-/pixelbron bleef **NIET TOEGANKELIJK** en runtimevolledigheid van de switcherdataset blijft `[NOG ONDERZOEKEN]`.
- **Rollback of herstelwijze:** Read-only; fouten corrigeren in rapport, nooit code verwijderen binnen deze taak.
- **Laatst bijgewerkt:** 2026-08-05.

### BC-DISC-002 - Concurrentie- en SEO-structuuranalyse

- **ID:** `BC-DISC-002`
- **Titel:** BadkamerXXL, Sanitairwinkel en Sanitairkamer diepgaand onderzoeken
- **Fase:** Fase 1 - volledige inventarisatie
- **Werkstroom:** Onderzoek / SEO
- **Status:** `DONE`
- **Prioriteit:** `P0`
- **Doel:** Feitelijk bewijs verzamelen voor categorie-, zoek-, filter-, PDP-, content- en SEO-besluiten.
- **Aanleiding:** De sites zijn referenties, maar mogen niet blind worden gekopieerd en zijn nog niet diepgaand geanalyseerd.
- **Scope:** Openbare read-only steekproef van de vragen uit hoofdstuk 23, met URL-bronnen, metadata, structured data, robots/sitemaps en expliciete grenzen voor mobiele/desktopwaarnemingen.
- **Buiten scope:** Kopiëren van beschermde inhoud/ontwerp of automatisch overnemen van structuur.
- **Afhankelijkheden:** `BC-ADM-001` en `BC-DISC-001` zijn menselijk goedgekeurd en `DONE`. Dit onderzoek is de derde taak in de vastgelegde onderzoeksvolgorde.
- **Benodigde input:** Gebruikt: eigen Admin-/assortimentsbeeld, de goedgekeurde actieve-themegebruiksmatrix en uitsluitend openbare concurrentpagina's. Geen accounts, formulieren, persoonsgegevens, private bronnen of extra Shopify-scopes zijn gebruikt.
- **Verwachte bestanden/systemen:** Publieke websites read-only, `docs/COMPETITOR_SEO_ANALYSIS.md` en dit masterplan.
- **Uitvoer:** `docs/COMPETITOR_SEO_ANALYSIS.md` met bronsteekproef, drie profielen, vergelijkingsmatrix, IA, zoeken/filters, kaarten, PDP's, services, content, technische SEO, sterke patronen, anti-patronen, kansen en open beslissingen.
- **Acceptatiecriteria:** Gehaald binnen de vastgelegde methode: alle drie referenties en vragen uit hoofdstuk 23 zijn representatief behandeld; feiten, afleidingen, beperkingen en menselijke beslissingen zijn gescheiden; geen concurrentinhoud of ontwerp is gekopieerd.
- **Technische controles:** Datum, exacte URL's, paginatype en methode vastgelegd; HTML, bron, metadata, structured data, robots, sitemaps en responsstatussen representatief gecontroleerd; na Sanitairkamer `429` gestopt; geen volledige crawl of formulierinteractie.
- **Menselijke controle:** De projecteigenaar heeft `docs/COMPETITOR_SEO_ANALYSIS.md` en masterplan versie 0.7 op 2026-08-05 goedgekeurd als afgerond openbaar read-only onderzoek. Dit is geen patroon-, categorie-, URL-, filter-, PDP-, design-, SEO- of implementatiebesluit en geen toestemming om concurrenten te kopieren.
- **Bewijs van voltooiing:** `docs/COMPETITOR_SEO_ANALYSIS.md`, dit masterplan, de openbare read-only bronsteekproef en expliciete menselijke goedkeuring van 2026-08-05.
- **Risico:** Concurrentiesites veranderen; bevindingen zijn tijdgebonden. Zoekresultaten, werkelijke mobiele/visuele en toetsenbordinteractie, indexdekking, runtimefilters, wishlist, calculators en configurators zijn niet of niet betrouwbaar onderzocht.
- **Rollback of herstelwijze:** Niet van toepassing op read-only onderzoek; onjuiste conclusies corrigeren met bronbewijs.
- **Laatst bijgewerkt:** 2026-08-05.

### BC-DATA-001 - Productdatamodel en metafieldcatalogus

- **ID:** `BC-DATA-001`
- **Titel:** Schaalbaar productdatamodel en veldcatalogus vaststellen
- **Fase:** Fase 2 - informatiearchitectuur en datamodel
- **Werkstroom:** Datamodel / producten
- **Status:** `BLOCKED`
- **Prioriteit:** `P0`
- **Doel:** Eén gevalideerd model maken voor zelfstandige uitvoeringsproducten, content, logistiek, SEO en relaties.
- **Aanleiding:** De doelprincipes zijn bekend, maar huidige Admin-velden, typen, bronnen en kwaliteit niet.
- **Scope:** Conceptueel model, Shopify-mapping, metafield/metaobjectcatalogus, validaties, eigenaarschap en feedgereedheid.
- **Buiten scope:** Producten of metafields aanmaken/wijzigen en API-integraties bouwen.
- **Afhankelijkheden:** `BC-ADM-001`, `BC-DISC-001`, `BC-DISC-002`, `BC-DATA-002` en `BC-DATA-003` zijn `DONE`; ontbrekende oorspronkelijke bronnen en relevante bedrijfsregels uit `BC-LOG-001` blijven nodig voor definitieve mappings en opslagkeuzes.
- **Benodigde input:** Admin-inventaris, goedgekeurde `docs/SUPPLIER_DATA_INVENTORY.md`, bestuurde conceptuele werkbasis `docs/PRODUCT_DATA_CONTRACT.md`, oorspronkelijke Hotbath- en The Mosaic Factory-bronnen, eventuele overige leveranciersbronnen, producttype-eisen en bronhouders `[NOG ONDERZOEKEN]`.
- **Verwachte bestanden/systemen:** Documentatie en Shopify Admin read-only; exacte toekomstige schema-/codebestanden `[NOG ONDERZOEKEN]`.
- **Uitvoer:** Goedgekeurd datamodel, veldcatalogus, validatieregels en migratievragen.
- **Acceptatiecriteria:** Elk vereist PDP-, filter-, switcher-, logistiek- en SEO-veld heeft type, bron, verplichtheid, validatie en eigenaar.
- **Technische controles:** Voorbeeldproducten per type, duplicaat-/null-/referentiechecks en toekomstig feedscenario.
- **Menselijke controle:** Eigenaar, productdata- en operationeel verantwoordelijken keuren model en regels goed; namen `[NOG ONDERZOEKEN]`.
- **Bewijs van voltooiing:** Goedgekeurde catalogus, voorbeelden en besluitlog `[NOG ONDERZOEKEN]`.
- **Risico:** Verkeerd model schaalt fouten naar circa 20.000 producten.
- **Rollback of herstelwijze:** Eerst uitsluitend documenteren/prototypen; eventuele latere migratie krijgt eigen backup- en herstelplan.
- **Laatst bijgewerkt:** 2026-08-10.

### BC-DATA-002 - Leveranciersbronnen en productvelden read-only inventariseren

- **ID:** `BC-DATA-002`
- **Titel:** Leveranciersbronnen en productvelden read-only inventariseren
- **Fase:** Fase 2 - informatiearchitectuur en datamodel
- **Werkstroom:** Datamodel / producten / onderzoek
- **Status:** `DONE`
- **Prioriteit:** `P0`
- **Doel:** Vaststellen welke leveranciersbestanden, imports, scripts, veldstructuren, producttypen, identificatoren en bronhouders momenteel beschikbaar of aantoonbaar afwezig zijn voordat het definitieve productdatamodel wordt ontworpen.
- **Aanleiding:** `BC-DATA-001` kan niet verantwoord starten zolang de werkelijke leveranciersvelden, bestanden, dekking en eigenaars niet zijn geïnventariseerd.
- **Scope:** Uitsluitend read-only inventarisatie van de repository, projectdocumentatie en reeds beschikbare lokale bronbestanden. Per bron worden naam, locatie, formaat, leverancier, datum, recordaantal waar veilig meetbaar, velden, identifiers, eenheden, prijsvelden, media, voorraad/levertijd, specificaties, switcherrelaties, kwaliteit en bekende beperkingen vastgelegd.
- **Buiten scope:** Shopify-data wijzigen, imports uitvoeren, bestanden corrigeren, metafields aanmaken, mappings definitief besluiten, theme-code wijzigen of API-koppelingen bouwen.
- **Afhankelijkheden:** `BC-ADM-001`, `BC-DISC-001` en `BC-DISC-002` zijn `DONE`.
- **Benodigde input:** De huidige repository, bestaande projectdocumenten en alle daarin daadwerkelijk aanwezige leveranciers-/importbronnen. Ontbrekende externe bestanden worden exact als ontbrekende input gerapporteerd en mogen niet worden verzonnen.
- **Verwachte bestanden/systemen:** Repository, projectdocumentatie en aanwezige lokale bronnen uitsluitend read-only; uitvoer `docs/SUPPLIER_DATA_INVENTORY.md`.
- **Uitvoer:** `docs/SUPPLIER_DATA_INVENTORY.md` met volledige formaatscan, zes afgeleide switcherdata-assets, vijf relevante storefrontscripts, veld-/identifieranalyse, ontbrekende bronnen, bronhouders, gevolgen en bewijsgrenzen.
- **Acceptatiecriteria:** Iedere aantoonbare bron heeft locatie, eigenaarstatus, formaat, velddekking, identifiers, kwaliteit, beperking en relevantie voor `BC-DATA-001`, `BC-LOG-001` en `BC-PROD-001`. Ontbrekende bronnen worden expliciet genoemd.
- **Technische controles:** Bestandsinventaris, headers/schema's, recordtotalen waar veilig, duplicaat-/nullsteekproeven, identifiervergelijking en bron-/datumcontrole. Geen imports of mutaties.
- **Menselijke controle:** De projecteigenaar heeft de binnen-scope complete lokale inventaris op 2026-08-10 goedgekeurd. Nul oorspronkelijke lokale bronnen is geaccepteerd als geldige bevinding; externe bronnen worden later per leverancier afzonderlijk aangeleverd en beoordeeld.
- **Bewijs van voltooiing:** `docs/SUPPLIER_DATA_INVENTORY.md`; 405 lokale/tracked paden bij taakstart volledig onderzocht, nul oorspronkelijke leveranciersbronnen, nul importbestanden, nul import-/generatiescripts, zes afgeleide theme-datasets en vijf direct relevante JavaScriptbestanden; menselijke goedkeuring van 2026-08-10.
- **Risico:** De lokale nulbevinding sluit externe bronnen niet uit. Zonder aangeleverde oorspronkelijke bestanden, bronhouders en generator-/mappingbewijs kan een verkeerd datamodel of een grootschalige importfout ontstaan.
- **Rollback of herstelwijze:** Read-only taak; uitsluitend documentatie corrigeren.
- **Laatst bijgewerkt:** 2026-08-10.

### BC-DATA-003 - Brononafhankelijk productinformatiecontract v0.1

- **ID:** `BC-DATA-003`
- **Titel:** Brononafhankelijk productinformatiecontract v0.1 vaststellen
- **Fase:** Fase 2 - informatiearchitectuur en datamodel
- **Werkstroom:** Datamodel / producten / architectuur
- **Status:** `DONE`
- **Prioriteit:** `P0`
- **Doel:** Vastleggen welke productinformatie BadkamerCity functioneel nodig heeft, onafhankelijk van het formaat van toekomstige leveranciersbestanden en zonder al een definitieve Shopify-opslag- of importmapping te kiezen.
- **Aanleiding:** De leveranciersinventaris bewijst dat oorspronkelijke bronbestanden nog ontbreken. Toch moeten productpagina's, kaarten, filters, zoeken, switchers, calculators, logistiek, SEO en kwaliteitscontroles later allemaal op een duidelijk logisch informatiecontract kunnen aansluiten.
- **Scope:** Een conceptueel en brononafhankelijk informatiecontract met logische velden, betekenis, datatype, cardinaliteit, toepasselijkheid, belangrijkheid, validatie, leegstaatgedrag, gebruiksdoelen, eigenaarsrollen en bronafhankelijkheid.
- **Buiten scope:** Definitieve Shopify namespace/key, metafielddefinities aanmaken, leverancierkolommen mappen, imports uitvoeren, productdata wijzigen, categorieboom ontwerpen, URL's kiezen, theme-code bouwen of commerciële en logistieke regels verzinnen.
- **Afhankelijkheden:** `BC-ADM-001`, `BC-DISC-001`, `BC-DISC-002` en `BC-DATA-002` zijn `DONE`.
- **Benodigde input:** Bestaande projectdocumentatie, huidige Admin-inventaris, actieve-themegebruiksmatrix, leveranciernulmeting, projectvisie en bevestigde producttype-eisen.
- **Verwachte bestanden/systemen:** Uitsluitend documentatie en repositorycode read-only.
- **Uitvoer:** `docs/PRODUCT_DATA_CONTRACT.md` met 190 unieke conceptuele contractkeys in 15 domeinen, producttypematrix, leegstaatbeleid, validaties, kwaliteitsgates, abstracte opslagcategorieën en een leeg leveranciersmappingtemplate.
- **Acceptatiecriteria:** Het contract behandelt minimaal identiteit, commercie, content, media, documenten, specificaties, logistiek, SEO, relaties, switchers, configurators, tegels, publicatiekwaliteit en eigenaarschap. Feitelijke bestaande velden, doelcontractvelden, leverancierafhankelijke input en open beslissingen zijn duidelijk gescheiden. Er is geen definitieve Shopify- of leveranciermapping gekozen.
- **Technische controles:** Gehaald voor het concept: 190 unieke lowercase contractkeys, nul `custom.*`-keys, 19 gevulde matrixkolommen per rij, consistente vereisteniveaus/broncategorieën/leegstaatcodes/eigenaarsrollen, vijf producttypeklassen en kruisverwijzingen naar afhankelijke functies.
- **Menselijke controle:** De projecteigenaar heeft `BC-DATA-003` op 2026-08-10 binnen de brononafhankelijke documentatiescope goedgekeurd als bestuurde conceptuele werkbasis v0.1. Alle individuele keys, niveaus, gates, eigenaars-, bron- en opslagkeuzes blijven afzonderlijke voorstellen/open beslissingen.
- **Bewijs van voltooiing:** `docs/PRODUCT_DATA_CONTRACT.md` v0.1, masterplan v0.12 en expliciete menselijke goedkeuring van 2026-08-10; uitsluitend lokale read-only bewijsbronnen, geen Shopify-, theme-, product-, bron- of scriptmutatie.
- **Risico:** Het contract kan ten onrechte als definitieve Shopify-mapping of als bewijs van beschikbare leveranciersdata worden gelezen.
- **Rollback of herstelwijze:** Documentatietaak; corrigeren via een afzonderlijke beoordeelde documentatiecommit.
- **Laatst bijgewerkt:** 2026-08-10.

**Goedgekeurd resultaat:** `BC-DATA-003` is uitsluitend brononafhankelijk/read-only uitgevoerd en op 2026-08-10 `DONE` verklaard als bestuurde conceptuele werkbasis v0.1. Het contract is geen definitieve Shopify-mapping, geen leveranciermapping en geen bewijs dat data beschikbaar is.

### BC-IA-001 - Categorie- en navigatiemodel

- **ID:** `BC-IA-001`
- **Titel:** Categorieboom, navigatie en URL-concept ontwerpen
- **Fase:** Fase 2 - informatiearchitectuur en datamodel
- **Werkstroom:** Categorieën / SEO
- **Status:** `BLOCKED`
- **Prioriteit:** `P0`
- **Doel:** Een eigen schaalbare structuur maken voor assortiment, zoekintentie, UX en SEO.
- **Aanleiding:** De huidige structuur is gedeeltelijk geïnspireerd op een concurrent en moet opnieuw worden onderzocht.
- **Scope:** Hoofdgroepen, subcategorieën, merken/eigenschappen, navigatie, landingspaginatypen, URL-principes en redirectbehoefte.
- **Buiten scope:** Collecties, menu's, templates of redirects in Shopify wijzigen.
- **Afhankelijkheden:** `BC-ADM-001`, `BC-DISC-002`, `BC-DATA-001`.
- **Benodigde input:** Assortimentdekking, zoekintentieonderzoek, huidige URL's/collecties en filtervelden.
- **Verwachte bestanden/systemen:** Documentatie, Shopify Admin read-only en onderzoek; implementatiebestanden `[NOG ONDERZOEKEN]`.
- **Uitvoer:** Goedgekeurde informatiearchitectuur en migratie-/redirectvoorstel.
- **Acceptatiecriteria:** Alle bevestigde hoofdgroepen zijn plaatsbaar; routes zijn onderscheidend, schaalbaar en toetsbaar op mobiel, SEO en beheer.
- **Technische controles:** Productdekking, orphan-/duplicaatcontrole, URL-conflicten en voorbeeldnavigaties.
- **Menselijke controle:** Eigenaar keurt categorieboom, labels en prioriteiten goed.
- **Bewijs van voltooiing:** Schema, mapping, testvoorbeelden en beslislog `[NOG ONDERZOEKEN]`.
- **Risico:** Vroege URL-keuzes kunnen migratie- en duplicate-contentkosten veroorzaken.
- **Rollback of herstelwijze:** Ontwerp eerst zonder Admin-wijzigingen; implementatie krijgt apart redirect- en herstelplan.
- **Laatst bijgewerkt:** 2026-08-03.

### BC-TECH-001 - Technische stabilisatie

- **ID:** `BC-TECH-001`
- **Titel:** Bekende theme-risico's, tooling en legacy veilig stabiliseren
- **Fase:** Fase 3 - technische stabilisatie
- **Werkstroom:** Development / QA
- **Status:** `BLOCKED`
- **Prioriteit:** `P0`
- **Doel:** Een beheersbare basis maken vóór functionele uitbreiding.
- **Aanleiding:** Audit vond mogelijke defects, Theme Check-meldingen, grote inline code, backups/debugassets en ontbrekende test/CI-inrichting.
- **Scope:** Na opsplitsing: defects reproduceren, Theme Check/tooling vastleggen, legacygebruik bepalen, backups buiten publiceerbare assets behandelen en regressietests toevoegen.
- **Buiten scope:** Onbewezen refactors, functioneel herontwerp en directe livewijziging.
- **Afhankelijkheden:** `BC-TECH-002` heeft de epic read-only opgedeeld en is `DONE`; de projecteigenaar moet nog een kandidaat als afzonderlijke officiele taak kiezen. Daarna blijven exacte scope, expliciete implementatietoestemming, `BC-DISC-001` en relevante delen van `BC-ADM-001` vereist.
- **Benodigde input:** Menselijk beoordeeld stabilisatieplan, gekozen eerste afzonderlijke taak, browsermatrix, testbasis en besluiten over legacy/backups, apps en releaseproces.
- **Verwachte bestanden/systemen:** Theme-code en documentatie `[NOG ONDERZOEKEN]`; preview-theme uitsluitend na expliciete taaktoestemming.
- **Uitvoer:** Kleine afzonderlijke stabilisatietaken met fixes, tests en bewijs.
- **Acceptatiecriteria:** Elke auditbevinding heeft eigenaar/status; gereproduceerde defects zijn opgelost of bewust geaccepteerd; tooling is herhaalbaar.
- **Technische controles:** Theme Check, referentieanalyse, smoke tests, diffreview en previewcontrole per deeltaak.
- **Menselijke controle:** Eigenaar keurt iedere zichtbare/functionele wijziging goed vóór `DONE`.
- **Bewijs van voltooiing:** Commits, testuitvoer en previewbewijs per deeltaak `[NOG ONDERZOEKEN]`.
- **Risico:** Dit werkpakket is te breed; verplichte opsplitsing vóór `READY` en speciale regressiezorg voor productpagina/switcher.
- **Rollback of herstelwijze:** Kleine commits, afzonderlijke preview en vooraf vastgelegde herstelcommit/themeprocedure.
- **Laatst bijgewerkt:** 2026-08-11.

### BC-TECH-002 - Technische stabilisatie opdelen en nulmeting vastleggen

- **ID:** `BC-TECH-002`
- **Titel:** Technische stabilisatie opdelen en uitvoeringsvolgorde vaststellen
- **Fase:** Fase 3 - technische stabilisatie
- **Werkstroom:** Development / QA / onderzoek
- **Status:** `DONE`
- **Prioriteit:** `P0`
- **Doel:** De brede technische stabilisatie-epic `BC-TECH-001` omzetten in een bewijsbaar, veilig en geprioriteerd plan van kleine vervolgopdrachten, zonder binnen deze taak theme-code of Shopify te wijzigen.
- **Aanleiding:** De repository-audit en actieve-themegebruiksmatrix bevatten meerdere mogelijke defects, actieve klant- en regressierisico's, dubbele switcherlogica, grote kernbestanden, backup-/debugassets, Theme Check-meldingen en ontbrekende test- en release-inrichting. `BC-TECH-001` is te breed om direct `READY` te worden.
- **Scope:** Read-only analyse van de bestaande repository en bewijsdocumenten; gerichte herbevestiging van bekende technische bevindingen; classificatie op actieve bereikbaarheid, zekerheid, impact en afhankelijkheid; lokale read-only Theme Check-controle; opstellen van kleine kandidaatvervolgtaken met exacte bestanden, acceptatiecriteria, tests, preview, afhankelijkheden en rollback.
- **Buiten scope:** Defects oplossen, code refactoren, bestanden verwijderen of verplaatsen, backupassets opruimen, switchers wijzigen, klantteksten aanpassen, tests/configuratie toevoegen, packages installeren, Shopify benaderen, themes pushen/pullen/publiceren of enige implementatie uitvoeren.
- **Afhankelijkheden:** `BC-ADM-001`, `BC-DISC-001`, `BC-DISC-002`, `BC-DATA-002` en `BC-DATA-003` zijn `DONE`. `BC-TECH-001` blijft de geblokkeerde bovenliggende epic.
- **Benodigde input:** Repository, projectdocumentatie, actieve-themegebruiksmatrix, Admin-inventaris, productcontract, leveranciernulmeting en huidige lokale tooling uitsluitend read-only.
- **Verwachte bestanden/systemen:** Repository en lokale tooling read-only; `docs/TECHNICAL_STABILIZATION_PLAN.md`; `docs/MASTERPLAN.md`.
- **Uitvoer:** `docs/TECHNICAL_STABILIZATION_PLAN.md` met 21 geclassificeerde bevindingen, twaalf kandidaatdeeltaken, afhankelijkheden, voorgestelde uitvoeringsvolgorde, minimale regressiematrix, preview-/rollbackvereisten en een aanbeveling voor de eerste afzonderlijk goed te keuren technische taak.
- **Acceptatiecriteria:** Alle bekende technische P0- en P1-bevindingen uit bestaande bewijsdocumenten zijn herleidbaar opgenomen of gemotiveerd uitgesloten. Iedere kandidaatdeeltaak heeft een klein doel, exacte scope, bestanden, afhankelijkheden, tests, previewvereisten, rollback en menselijke beslissing. Er is duidelijk onderscheid tussen direct uitvoerbaar, geblokkeerd door data/IA/bedrijfsregels en alleen nader te reproduceren. Geen code of Shopify-data is gewijzigd.
- **Technische controles:** Git-basis, bestandsreferenties, actieve bereikbaarheid, gerichte bronregels, JSON-parsing waar relevant, lokale Theme Check-uitvoer, bestandsgroottes, known-riskcontrole, diffcontrole en een mechanische controle dat alleen toegestane documentatie is gewijzigd.
- **Menselijke controle:** De projecteigenaar heeft `BC-TECH-002` op 2026-08-11 binnen de read-only onderzoeks- en decompositiescope goedgekeurd. De kandidaten, classificaties, Theme Check-richting en uitvoeringsvolgorde zijn geen implementatie-, wijzigings- of verwijdertoestemming.
- **Bewijs van voltooiing:** `docs/TECHNICAL_STABILIZATION_PLAN.md` met sectie 35; lokale Theme Check-resultaten, gerichte bron-/referentieherbevestiging en expliciete menselijke goedkeuring op 2026-08-11. Geen code, Shopify-data of theme gewijzigd; kandidaat-ID's zijn geen officiele taken.
- **Risico:** Een onderzoeksclassificatie kan ten onrechte als defectbewijs, verwijdertoestemming of implementatiebesluit worden gelezen. Geen kandidaatbestand of kandidaatoplossing mag zonder aparte taak worden gewijzigd.
- **Rollback of herstelwijze:** Documentatietaak; fouten uitsluitend via een aparte beoordeelde documentatiecorrectie herstellen.
- **Laatst bijgewerkt:** 2026-08-11.

**Goedgekeurd onderzoeksresultaat:** 21 bevindingen (2 P0, 15 P1, 4 P2), twaalf kandidaatdeeltaken en een minimale regressie-/preview-/rollbackbasis. De eerste aanbevolen ongeblokkeerde richting is een afzonderlijke reproduceerbare Theme Check-/kwaliteitsbasistaak, maar die is niet gestart of goedgekeurd. De vaste onbewezen levertijdtekst is het hoogste actieve klant-/bedrijfsrisico en blijft voor een oplossing afhankelijk van een menselijke bedrijfsregelbeslissing. Geen defect is opgelost; classificatie geeft geen wijzigings- of verwijdertoestemming.

### BC-UX-001 - Design system en globale onderdelen

- **ID:** `BC-UX-001`
- **Titel:** Design system, homepage, header, menu en footer definiëren en realiseren
- **Fase:** Fase 4 - design system en globale websiteonderdelen
- **Werkstroom:** UX/design / development
- **Status:** `BLOCKED`
- **Prioriteit:** `P1`
- **Doel:** Een rustige, betrouwbare, toegankelijke en schaalbare globale ervaring maken.
- **Aanleiding:** Huidige basis is bruikbaar maar bevat lege configuraties en placeholderlinks; herontwerpomvang is open.
- **Scope:** Na opsplitsing: tokens/componenten, states, responsive regels, homepage en globale navigatie/footer.
- **Buiten scope:** Categorie-, PDP- en servicefuncties buiten de globale componentlaag.
- **Afhankelijkheden:** Afzonderlijke expliciete implementatietoestemming, `BC-IA-001`, `BC-DISC-002`, `BC-TECH-001` en designrichting.
- **Benodigde input:** Merk-/contentrichting, definitieve links, categorieboom en menselijke visuele voorkeuren `[OPEN BESLISSING]`.
- **Verwachte bestanden/systemen:** Bestaande home/header/footer/theme-assets; exacte bestanden na inventarisatie.
- **Uitvoer:** Goedgekeurd designfundament en afzonderlijk geteste globale onderdelen.
- **Acceptatiecriteria:** Rust/overzicht/vertrouwen behouden; mobiel en desktop compleet; states en toetsenbordgedrag gedocumenteerd; placeholders weg.
- **Technische controles:** Responsive/visuele tests, toetsenbord, Theme Check, performance en regressies.
- **Menselijke controle:** Expliciete previewgoedkeuring per zichtbaar onderdeel.
- **Bewijs van voltooiing:** Ontwerpbesluiten, commits, screenshots/testbewijs en goedkeuring `[NOG ONDERZOEKEN]`.
- **Risico:** Werkpakket is te breed en kan scope laten uitwaaieren; verplicht opdelen vóór `READY`.
- **Rollback of herstelwijze:** Componentgewijze commits en preview; herstel via vooraf geïdentificeerde vorige commit/themeversie.
- **Laatst bijgewerkt:** 2026-08-03.

### BC-CAT-001 - Categorie-, zoek- en merchandisingplatform

- **ID:** `BC-CAT-001`
- **Titel:** Categoriepagina's, productkaarten, zoeken, filters en merchandising realiseren
- **Fase:** Fase 5 - categorieën, zoeken en filters
- **Werkstroom:** Categorieën / development
- **Status:** `BLOCKED`
- **Prioriteit:** `P1`
- **Doel:** Producten logisch vindbaar, scanbaar en filterbaar maken volgens de goedgekeurde informatiearchitectuur.
- **Aanleiding:** Basiscode bestaat, maar actieve configuratie, datadekking en lanceringskwaliteit zijn niet bewezen.
- **Scope:** Na opsplitsing: category landing, collectiegrid, kaarten, search, predictive search, filters, sortering, merchandising en states.
- **Buiten scope:** Definitieve productdata-import en SEO-contentproductie.
- **Afhankelijkheden:** `BC-IA-001`, `BC-DATA-001`, `BC-UX-001`, `BC-TECH-001`.
- **Benodigde input:** Categorieboom, filtervelden, zoek-/merchandisingregels en representatieve productdata.
- **Verwachte bestanden/systemen:** Bestaande collection/search/card-secties, snippets, templates en Shopify collecties `[NOG ONDERZOEKEN]`.
- **Uitvoer:** Opgesplitste, werkende categorie-, zoek- en filterervaring.
- **Acceptatiecriteria:** Productdekking, filters, sortering, nulresultaten, kaarten, mobiel/desktop, toetsenbord en SEO-routes voldoen aan goedgekeurde criteria.
- **Technische controles:** Datafixtures/steekproeven, functionele journeys, Theme Check, responsive, performance, toegankelijkheid en technische SEO.
- **Menselijke controle:** Eigenaar beoordeelt categorie-, zoek- en productkaartpreview vóór `DONE`.
- **Bewijs van voltooiing:** Taakcommits, previewlinks, testmatrix en goedkeuring `[NOG ONDERZOEKEN]`.
- **Risico:** Breed werkpakket; moet vóór `READY` per component en categorie worden opgesplitst.
- **Rollback of herstelwijze:** Componentgewijze commits, onveranderde liveomgeving en herstel naar goedgekeurde previewbasis.
- **Laatst bijgewerkt:** 2026-08-03.

### BC-PDP-001 - Productpaginaplatform

- **ID:** `BC-PDP-001`
- **Titel:** Productpaginastandaard en standaard sanitairproduct realiseren
- **Fase:** Fase 6 - productpaginaplatform
- **Werkstroom:** Producten / development
- **Status:** `BLOCKED`
- **Prioriteit:** `P0`
- **Doel:** Een herbruikbaar, compleet en aantoonbaar betrouwbaar productpaginaplatform maken.
- **Aanleiding:** De huidige productpagina is groot, complex en bevat dubbele/inline logica; de gewenste inhoud is breder dan bewezen functionaliteit.
- **Scope:** Na opsplitsing: informatiehiërarchie, media, buybox, specificaties, content, documenten, relaties, service, SEO, states en standaard sanitairproduct.
- **Buiten scope:** Tegelcalculator en producttypeconfigurators, die eigen taken hebben.
- **Afhankelijkheden:** `BC-DATA-001`, `BC-TECH-001`, `BC-UX-001`, logistieke/servicevelden en `BC-SWITCH-001` voor koppelvlak.
- **Benodigde input:** Goedgekeurde veldcatalogus, contentregels, voorbeeldproducten en operationele informatie.
- **Verwachte bestanden/systemen:** `sections/main-product.liquid` en gerelateerde assets/snippets/templates; exacte wijzigingsset `[NOG ONDERZOEKEN]`.
- **Uitvoer:** Opgesplitste PDP-taken en een goedgekeurd standaardproducttemplate.
- **Acceptatiecriteria:** Alle toepasselijke elementen uit hoofdstuk 17 hebben bron, leegstaat, weergave en tests; kernkoopreis werkt.
- **Technische controles:** Theme Check, productfixtures, cart, responsive, toetsenbord, structured data, canonical, performance en regressies.
- **Menselijke controle:** Eigenaar keurt de zichtbare PDP en kernjourney expliciet goed.
- **Bewijs van voltooiing:** Commits, preview, matrix per PDP-element en menselijke goedkeuring `[NOG ONDERZOEKEN]`.
- **Risico:** Hoog regressierisico door `main-product.liquid`; verplicht gefaseerd en klein implementeren.
- **Rollback of herstelwijze:** Per onderdeel kleine commits, previewvergelijking en herstel naar vooraf vastgelegde basis.
- **Laatst bijgewerkt:** 2026-08-03.

### BC-SWITCH-001 - Switcherarchitectuur en hardening

- **ID:** `BC-SWITCH-001`
- **Titel:** Eén gevalideerde product-switcherarchitectuur vaststellen en verharden
- **Fase:** Fase 7 - switchers, calculators en configurators
- **Werkstroom:** Switcher / development
- **Status:** `BLOCKED`
- **Prioriteit:** `P0`
- **Doel:** Betrouwbare navigatie tussen zelfstandige uitvoeringsproducten bieden zonder dubbele onbeheerste logica.
- **Aanleiding:** V2 en legacyfallback bestaan naast elkaar; dataset is groot en afhankelijk van exacte metafield-/assetkoppeling.
- **Scope:** Bronkeuze, datavalidatie, fallbackbesluit, foutgedrag, payload, migratie, tests en monitoring.
- **Buiten scope:** Doucheset-/meubel-specifieke UX en complete-badkamerbundeling.
- **Afhankelijkheden:** `BC-ADM-001`, `BC-DISC-001`, `BC-DATA-001`, `BC-TECH-001`.
- **Benodigde input:** Werkelijke metafields, groepsdekking, datasetgenerator/eigenaar en productrelaties `[NOG ONDERZOEKEN]`.
- **Verwachte bestanden/systemen:** Huidige switchersnippet, JS, JSON, `main-product.liquid`, `global.js` en Shopify metafields.
- **Uitvoer:** Goedgekeurd architectuurbesluit plus opgesplitste implementatie-/migratietaken.
- **Acceptatiecriteria:** Elke combinatie matcht uniek of toont gecontroleerd gedrag; huidige producten blijven bereikbaar; bron en validatie zijn reproduceerbaar.
- **Technische controles:** Schema-, duplicaat-, ontbrekende-handle/URL-, groeps- en combinatietests; payloadmeting; regressiematrix.
- **Menselijke controle:** Eigenaar test representatieve groepen en keurt interactie/uitkomst goed.
- **Bewijs van voltooiing:** Besluit, validatorresultaten, commits, preview en goedkeuring `[NOG ONDERZOEKEN]`.
- **Risico:** Verkeerde match kan naar een fout product/SKU sturen; dit is een P0-risico.
- **Rollback of herstelwijze:** Migratieplan met behoud van gecontroleerde vorige route tot nieuwe dekking bewezen is; exacte aanpak `[OPEN BESLISSING]`.
- **Laatst bijgewerkt:** 2026-08-03.

### BC-TILE-001 - Tegelcalculator

- **ID:** `BC-TILE-001`
- **Titel:** m²-calculator voor tegels specificeren en realiseren
- **Fase:** Fase 7 - switchers, calculators en configurators
- **Werkstroom:** Tegels / development
- **Status:** `BLOCKED`
- **Prioriteit:** `P1`
- **Doel:** Benodigde oppervlakte correct vertalen naar volledige dozen en transparante prijs/totaalweergave.
- **Aanleiding:** De calculator is een bevestigde producttype-eis voor lancering.
- **Scope:** Oppervlakte, snijverlies, doosinhoud, afronding, prijs per m²/doos, totaal dozen en totaal bestelde oppervlakte.
- **Buiten scope:** Andere calculators en leveranciersfeedintegraties.
- **Afhankelijkheden:** `BC-DATA-001`, `BC-PDP-001`, prijs-/voorraadregels en tegelassortimentinventaris.
- **Benodigde input:** Eenheden, precisie, standaard/keuze snijverlies, doosdata, prijsbron en cartgedrag `[OPEN BESLISSING]`.
- **Verwachte bestanden/systemen:** PDP/cart/theme-code en tegeldata; exacte componentbestanden `[NOG ONDERZOEKEN]`.
- **Uitvoer:** Goedgekeurde specificatie, calculatorcomponent en bewijsset.
- **Acceptatiecriteria:** Alle genoemde outputs kloppen voor normale, grens-, afrondings-, ontbrekende-data- en wijzigingsscenario's.
- **Technische controles:** Geautomatiseerde rekenvoorbeelden, decimalen/afronding, cartintegratie, mobiel, toetsenbord en prijsconsistentie.
- **Menselijke controle:** Eigenaar valideert rekenvoorbeelden, tekst en koopflow op preview.
- **Bewijs van voltooiing:** Specificatie, testtabel, commits, preview en goedkeuring `[NOG ONDERZOEKEN]`.
- **Risico:** Eenheids- of afrondingsfouten veroorzaken verkeerde bestelling en prijsverwachting.
- **Rollback of herstelwijze:** Feature afzonderlijk schakelbaar of herstelbaar via eigen commit; exacte methode wordt vóór implementatie bepaald.
- **Laatst bijgewerkt:** 2026-08-03.

### BC-CONF-001 - Douchesetconfigurator

- **ID:** `BC-CONF-001`
- **Titel:** Douchesetconfigurator naar bestaande producten realiseren
- **Fase:** Fase 7 - switchers, calculators en configurators
- **Werkstroom:** Configurators / producten
- **Status:** `BLOCKED`
- **Prioriteit:** `P1`
- **Doel:** Eigenschapskeuzes betrouwbaar naar de juiste zelfstandige doucheset-URL/SKU laten navigeren.
- **Aanleiding:** Douchesets hebben volgens het productmodel een eigen configurator nodig.
- **Scope:** Eigenschappen, keuzevolgorde, beschikbare combinaties, disabled states, match, navigatie en foutgedrag.
- **Buiten scope:** Losse artikelen als bundel in cart samenstellen en complete badkamerconfiguratie.
- **Afhankelijkheden:** `BC-SWITCH-001`, `BC-DATA-001`, `BC-PDP-001` en gevalideerde douchesetgroepen.
- **Benodigde input:** Producteigenschappen, combinaties, URL/SKU-koppelingen en UX-labels `[NOG ONDERZOEKEN]`.
- **Verwachte bestanden/systemen:** Switcher/configuratorcomponenten, productdata en doucheset-PDP's `[NOG ONDERZOEKEN]`.
- **Uitvoer:** Geteste douchesetconfigurator en dekkingsrapport.
- **Acceptatiecriteria:** Elke geldige combinatie leidt naar exact één juist product; ongeldige/ontbrekende combinaties zijn begrijpelijk en veilig.
- **Technische controles:** Volledige combinatiematrix, navigatie, terug/vooruit, directe URL, mobiel, toetsenbord en performance.
- **Menselijke controle:** Eigenaar keurt representatieve configuraties en labels op preview goed.
- **Bewijs van voltooiing:** Matrix, datavalidatie, commits, preview en goedkeuring `[NOG ONDERZOEKEN]`.
- **Risico:** Onvolledige groepen sturen klanten verkeerd of maken producten onbereikbaar.
- **Rollback of herstelwijze:** Gecontroleerde terugkeer naar bewezen vorige switcherroute; vooraf per groep vastleggen.
- **Laatst bijgewerkt:** 2026-08-03.

### BC-CONF-002 - Badkamermeubelconfigurator

- **ID:** `BC-CONF-002`
- **Titel:** Badkamermeubelconfigurator naar bestaande producten realiseren
- **Fase:** Fase 7 - switchers, calculators en configurators
- **Werkstroom:** Configurators / producten
- **Status:** `BLOCKED`
- **Prioriteit:** `P1`
- **Doel:** Meubeleigenschappen betrouwbaar naar de juiste zelfstandige product-URL/SKU laten navigeren.
- **Aanleiding:** Badkamermeubels volgen volgens de projectdefinitie hetzelfde zelfstandige-productprincipe.
- **Scope:** Eigenschappen, keuzevolgorde, combinaties, beschikbaarheid, match, navigatie en foutgedrag.
- **Buiten scope:** Bundeling van losse cartartikelen en complete badkameropstellingen.
- **Afhankelijkheden:** `BC-SWITCH-001`, `BC-DATA-001`, `BC-PDP-001` en gevalideerde meubelgroepen.
- **Benodigde input:** Producteigenschappen, combinaties, URL/SKU-koppelingen en labels `[NOG ONDERZOEKEN]`.
- **Verwachte bestanden/systemen:** Switcher/configuratorcomponenten, productdata en meubel-PDP's `[NOG ONDERZOEKEN]`.
- **Uitvoer:** Geteste meubelconfigurator en dekkingsrapport.
- **Acceptatiecriteria:** Elke geldige combinatie leidt naar exact één juist product en alle ongeldige states zijn gecontroleerd.
- **Technische controles:** Combinatiematrix, navigatie, directe URL, history, mobiel, toetsenbord en performance.
- **Menselijke controle:** Eigenaar keurt representatieve meubelconfiguraties op preview goed.
- **Bewijs van voltooiing:** Matrix, validator, commits, preview en goedkeuring `[NOG ONDERZOEKEN]`.
- **Risico:** Veel mogelijke eigenschappen kunnen ambiguïteit en payloadgroei veroorzaken.
- **Rollback of herstelwijze:** Per groep terugkeer naar vooraf bewezen productnavigatie; methode vóór implementatie vastleggen.
- **Laatst bijgewerkt:** 2026-08-03.

### BC-CONF-003 - Complete badkamerconfigurator

- **ID:** `BC-CONF-003`
- **Titel:** Toekomstige configurator voor complete badkameropstellingen onderzoeken
- **Fase:** Fase 7 - switchers, calculators en configurators
- **Werkstroom:** Configurators / onderzoek
- **Status:** `DEFERRED`
- **Prioriteit:** `P2`
- **Doel:** Later bepalen hoe complete opstellingen kunnen worden samengesteld zonder het huidige datamodel te blokkeren.
- **Aanleiding:** Toekomstige uitbreiding is gewenst, maar exacte werking is open.
- **Scope:** Later onderzoek naar use cases, productrelaties, bundeling, prijs, voorraad, logistiek, cart en UX.
- **Buiten scope:** Huidige lanceringsimplementatie of aannemen dat losse artikelen nu worden gebundeld.
- **Afhankelijkheden:** Voltooide basis voor data, PDP, switchers, logistiek en productonboarding.
- **Benodigde input:** `[OPEN BESLISSING]` Bedrijfsdoel, functionele scope en prioriteit na basisplatform.
- **Verwachte bestanden/systemen:** `[NOG ONDERZOEKEN]`; nog geen implementatiebestand vastgesteld.
- **Uitvoer:** Toekomstige discovery en besluitdocument.
- **Acceptatiecriteria:** Use cases, grenzen, afhankelijkheden, opties, risico's en besluit zijn vastgelegd vóór eventuele bouw.
- **Technische controles:** Conceptuele data-, cart-, voorraad-, prijs- en logistieke haalbaarheidstoets.
- **Menselijke controle:** Eigenaar besluit afzonderlijk of en wanneer dit wordt ontwikkeld.
- **Bewijs van voltooiing:** Later onderzoeks- en besluitbewijs `[NOG ONDERZOEKEN]`.
- **Risico:** Vroegtijdige scope kan kernlancering vertragen.
- **Rollback of herstelwijze:** Geen implementatie zolang `DEFERRED`; architectuur vermijdt alleen onnodige blokkades.
- **Laatst bijgewerkt:** 2026-08-03.

### BC-CONV-001 - Verlanglijst

- **ID:** `BC-CONV-001`
- **Titel:** Verlanglijst voor lancering specificeren en realiseren
- **Fase:** Fase 8 - conversie- en servicefuncties
- **Werkstroom:** Service / development
- **Status:** `BLOCKED`
- **Prioriteit:** `P1`
- **Doel:** Klanten relevante producten laten bewaren en terugvinden.
- **Aanleiding:** Verlanglijst is bevestigde lanceringsscope en er bestaat een headerverwijzing.
- **Scope:** Gast/accountgedrag, toevoegen/verwijderen, lijstweergave, synchronisatie, states en privacy.
- **Buiten scope:** Productvergelijking en reviews.
- **Afhankelijkheden:** `BC-ADM-001`, `BC-DISC-001`, `BC-UX-001`, `BC-PDP-001` en accountbesluit.
- **Benodigde input:** `[OPEN BESLISSING]` App versus maatwerk, accountvereiste, bewaartermijn en UX.
- **Verwachte bestanden/systemen:** Header, productkaarten, PDP, account/app en opslag `[NOG ONDERZOEKEN]`.
- **Uitvoer:** Opgesplitste implementatie met werkende verlanglijstreis.
- **Acceptatiecriteria:** Toevoegen, verwijderen, persistentie, lege/errorstates en relevante apparaten/accountstates zijn getest.
- **Technische controles:** Functionele tests, privacy/consent, toegankelijkheid, performance en app-conflictcontrole.
- **Menselijke controle:** Eigenaar keurt UX en gedrag op preview goed.
- **Bewijs van voltooiing:** Besluit, tests, commits, preview en goedkeuring `[NOG ONDERZOEKEN]`.
- **Risico:** Onbekende app/gegevensopslag kan privacy-, performance- en lock-inrisico geven.
- **Rollback of herstelwijze:** Oplossing moet uitschakelbaar/herstelbaar zijn zonder productdata te verliezen; exact plan vóór bouw.
- **Laatst bijgewerkt:** 2026-08-03.

### BC-SAMPLE-001 - Samples bestellen

- **ID:** `BC-SAMPLE-001`
- **Titel:** Samplebestelproces specificeren en realiseren
- **Fase:** Fase 8 - conversie- en servicefuncties
- **Werkstroom:** Service / producten
- **Status:** `BLOCKED`
- **Prioriteit:** `P1`
- **Doel:** Klanten gecontroleerd samples laten aanvragen/bestellen.
- **Aanleiding:** Samples zijn bevestigde lanceringsscope, maar proces en data ontbreken.
- **Scope:** Geschiktheid, selectie, limieten, prijs, voorraad, cart/checkout, verzending, bevestiging en opvolging.
- **Buiten scope:** Normale productbestelling wijzigen buiten noodzakelijke sample-integratie.
- **Afhankelijkheden:** `BC-DATA-001`, `BC-PDP-001`, `BC-LOG-001`, `BC-LOG-002` en bedrijfsprocesbesluit.
- **Benodigde input:** Sampleassortiment, kosten, limieten, voorraad-/verzendregels en eigenaar `[NOG ONDERZOEKEN]`.
- **Verwachte bestanden/systemen:** Productdata, PDP, cart/checkout en fulfilment `[NOG ONDERZOEKEN]`.
- **Uitvoer:** Goedgekeurd sampleproces en geteste klantreis.
- **Acceptatiecriteria:** Alleen geldige samples kunnen volgens regels worden besteld en prijs/levering/limieten zijn correct zichtbaar.
- **Technische controles:** Product-/cart-/ordersteekproeven, grensgevallen, mobiel, toetsenbord en logistieke controle.
- **Menselijke controle:** Commerciële en operationele eigenaar keuren proces en preview goed.
- **Bewijs van voltooiing:** Procesbesluit, tests/ordersimulatie, commits en goedkeuring `[NOG ONDERZOEKEN]`.
- **Risico:** Onduidelijke samplelogistiek kan kosten, voorraad- en klantverwachtingsproblemen geven.
- **Rollback of herstelwijze:** Samplefunctie afzonderlijk deactiveerbaar; product-/orderdataherstel vooraf bepalen.
- **Laatst bijgewerkt:** 2026-08-03.

### BC-QUOTE-001 - Offerte uploaden

- **ID:** `BC-QUOTE-001`
- **Titel:** Veilige offerte-upload en opvolging realiseren
- **Fase:** Fase 8 - conversie- en servicefuncties
- **Werkstroom:** Service / privacy
- **Status:** `BLOCKED`
- **Prioriteit:** `P1`
- **Doel:** Een bestaande offerte veilig ontvangen voor een betere aanbieding.
- **Aanleiding:** Dit is een bevestigde commerciële propositie en lanceringsfunctie.
- **Scope:** Formulier, uploads, validatie, opslag/toegang, toestemming, routing, bevestiging en operationele opvolging.
- **Buiten scope:** Automatische prijsbeslissing zonder goedgekeurd beleid.
- **Afhankelijkheden:** `BC-SEC-001`, `BC-UX-001`, operationeel proces en juridische/privacycontrole.
- **Benodigde input:** Bestandstypen/limieten, velden, bewaartermijn, ontvangers, SLA en toestemming `[OPEN BESLISSING]`.
- **Verwachte bestanden/systemen:** Themeformulier, upload-/opslagsysteem, notificatie en beheerproces `[NOG ONDERZOEKEN]`.
- **Uitvoer:** Beveiligde en geteste upload-/opvolgreis.
- **Acceptatiecriteria:** Geldige bestanden komen alleen bij bevoegden; ongeldige uploads worden veilig afgewezen; klant krijgt duidelijke bevestiging.
- **Technische controles:** Type/size/contentvalidatie, toegangscontrole, foutstates, logging zonder onnodige data, mobiel en toegankelijkheid.
- **Menselijke controle:** Eigenaar en relevante privacy-/operationele verantwoordelijke keuren proces expliciet goed.
- **Bewijs van voltooiing:** Beleid, securitytests, commits, preview en goedkeuring `[NOG ONDERZOEKEN]`.
- **Risico:** Bestandsuploads zijn een hoog privacy- en beveiligingsrisico.
- **Rollback of herstelwijze:** Functie uitschakelen, toegang intrekken en gegevens volgens goedgekeurd incident-/verwijderproces behandelen.
- **Laatst bijgewerkt:** 2026-08-03.

### BC-PRICE-001 - Laagsteprijsgarantie

- **ID:** `BC-PRICE-001`
- **Titel:** Laagsteprijsgarantiebeleid en aanvraagflow realiseren
- **Fase:** Fase 8 - conversie- en servicefuncties
- **Werkstroom:** Service / conversie
- **Status:** `BLOCKED`
- **Prioriteit:** `P1`
- **Doel:** De prijspropositie transparant en operationeel uitvoerbaar aanbieden.
- **Aanleiding:** Laagsteprijsgarantie is een bevestigde commerciële pijler en lanceringsfunctie.
- **Scope:** Voorwaarden, bewijs, aanvraag, validatie, routing, reactie, statussen en klantcommunicatie.
- **Buiten scope:** Onbevoegde automatische prijsaanpassing of onbevestigde juridische claims.
- **Afhankelijkheden:** Goedgekeurd commercieel/juridisch beleid, `BC-SEC-001`, `BC-UX-001` en prijsdatamodel.
- **Benodigde input:** Voorwaarden, uitsluitingen, verantwoordelijke, SLA, benodigde gegevens en besluitproces `[OPEN BESLISSING]`.
- **Verwachte bestanden/systemen:** Content, formulier, eventuele upload, notificatie en opvolgsysteem `[NOG ONDERZOEKEN]`.
- **Uitvoer:** Goedgekeurd beleid en geteste aanvraagflow.
- **Acceptatiecriteria:** Voorwaarden zijn duidelijk; aanvragen bevatten benodigde minimale data; routing en klantfeedback werken; privacy is goedgekeurd.
- **Technische controles:** Validatie, foutstates, toegankelijkheid, tracking met consent en processteekproef.
- **Menselijke controle:** Eigenaar keurt voorwaarden, tekst en operationele afhandeling expliciet goed.
- **Bewijs van voltooiing:** Beleidsbesluit, tests, commits, preview en goedkeuring `[NOG ONDERZOEKEN]`.
- **Risico:** Onduidelijke of onhoudbare garantie kan commercieel en juridisch risico geven.
- **Rollback of herstelwijze:** Aanvraagmogelijkheid en claimtekst afzonderlijk kunnen intrekken na menselijk besluit; open aanvragen handmatig afhandelen.
- **Laatst bijgewerkt:** 2026-08-03.

### BC-ACC-001 - Klantaccount en bestellingen

- **ID:** `BC-ACC-001`
- **Titel:** Klantaccount, bestelhistorie en ordertracking valideren en realiseren
- **Fase:** Fase 8 - conversie- en servicefuncties
- **Werkstroom:** Service / Shopify Admin
- **Status:** `BLOCKED`
- **Prioriteit:** `P1`
- **Doel:** Klanten veilig toegang geven tot account, historie en bestellingstatus.
- **Aanleiding:** Alle drie zijn bevestigde lanceringsfuncties; alleen basisaccountcode is zichtbaar.
- **Scope:** Accountmodel, registratie/login, historie, tracking, states, privacy en klantenservicekoppeling.
- **Buiten scope:** Onbevestigde loyalty- of abonnementsfunctionaliteit.
- **Afhankelijkheden:** `BC-ADM-001`, app-/accountinventaris, `BC-UX-001`, `BC-SEC-001` en logistieke trackingregels.
- **Benodigde input:** Shopify-accountconfiguratie, trackingbron, toegang/retentie en serviceproces `[NOG ONDERZOEKEN]`.
- **Verwachte bestanden/systemen:** Customer templates, Shopify accounts/orders en eventuele trackingapp `[NOG ONDERZOEKEN]`.
- **Uitvoer:** Geteste account-, historie- en trackingreis.
- **Acceptatiecriteria:** Bevoegde klant ziet juiste informatie; fout/lege states en privacy werken; kernreizen zijn mobiel/toegankelijk.
- **Technische controles:** Account-/orderfixtures, autorisatie, sessies, links, responsive, toetsenbord en app-conflicten.
- **Menselijke controle:** Eigenaar valideert klantreis en klantenserviceproces.
- **Bewijs van voltooiing:** Configuratiebewijs, tests, commits, preview en goedkeuring `[NOG ONDERZOEKEN]`.
- **Risico:** Onjuiste autorisatie of tracking kan persoonsgegevens of verkeerde orderinformatie tonen.
- **Rollback of herstelwijze:** Themewijzigingen terugdraaien; account-/appherstelprocedure vóór implementatie vastleggen.
- **Laatst bijgewerkt:** 2026-08-03.

### BC-SHOW-001 - Afspraken en showroompropositie

- **ID:** `BC-SHOW-001`
- **Titel:** Afspraakflow en correcte showroomcommunicatie realiseren
- **Fase:** Fase 8 - conversie- en servicefuncties
- **Werkstroom:** Service / content
- **Status:** `BLOCKED`
- **Prioriteit:** `P1`
- **Doel:** Afspraken mogelijk maken zonder de huidige BadkamerCity/Harry Suiker-relatie verkeerd voor te stellen.
- **Aanleiding:** Afspraak maken is lanceringsscope en showroombezoek kan voorlopig bij Harry Suiker plaatsvinden.
- **Scope:** Goedgekeurde tekst, afspraakkanaal, beschikbaarheid, bevestiging, locatie-informatie en privacy.
- **Buiten scope:** Claim dat BadkamerCity al een zelfstandige showroom heeft of publicatie van uitgebreide onbevestigde showroomdetails.
- **Afhankelijkheden:** `BC-UX-001`, `BC-SEC-001` en expliciet showroom-/afspraakbesluit.
- **Benodigde input:** Exacte openbare formulering, eigenaar van agenda, tijdsloten, locatiegegevens en opvolgproces `[OPEN BESLISSING]`.
- **Verwachte bestanden/systemen:** Header/content/formulier en agenda-/notificatiesysteem `[NOG ONDERZOEKEN]`.
- **Uitvoer:** Goedgekeurde showroomtekst en werkende afspraakreis.
- **Acceptatiecriteria:** Geen misleidende eigendomsclaim; afspraak komt correct aan; bevestiging, fouten, mobiel en toegankelijkheid werken.
- **Technische controles:** Formulier/agenda, dubbele invoer, tijdzones `[NOG ONDERZOEKEN]`, privacy, responsive en links.
- **Menselijke controle:** Eigenaar keurt formulering, locatiepresentatie en afspraakflow expliciet goed.
- **Bewijs van voltooiing:** Tekstbesluit, tests, commits, preview en goedkeuring `[NOG ONDERZOEKEN]`.
- **Risico:** Onjuiste showroomclaim schaadt vertrouwen en kan operationeel/juridisch risico geven.
- **Rollback of herstelwijze:** Afspraak-CTA/tekst uitschakelen of terugzetten via afzonderlijke change; afspraken operationeel blijven afhandelen.
- **Laatst bijgewerkt:** 2026-08-03.

### BC-CHAT-001 - WhatsApp of chat

- **ID:** `BC-CHAT-001`
- **Titel:** WhatsApp- of chatservice selecteren en realiseren
- **Fase:** Fase 8 - conversie- en servicefuncties
- **Werkstroom:** Service / privacy
- **Status:** `BLOCKED`
- **Prioriteit:** `P1`
- **Doel:** Klanten een bruikbaar direct contactkanaal bieden.
- **Aanleiding:** WhatsApp of chat behoort tot de bevestigde lanceringsfuncties.
- **Scope:** Kanaal/provider, beschikbaarheid, consent, routing, fallback, responstijd, toegankelijkheid en meting.
- **Buiten scope:** Onbevestigde geautomatiseerde advies- of verkoopbeslissingen.
- **Afhankelijkheden:** `BC-ADM-001`, `BC-SEC-001`, `BC-ANA-001`, appinventaris en serviceproces.
- **Benodigde input:** `[OPEN BESLISSING]` WhatsApp, chat of combinatie; provider, openingstijden, eigenaar en SLA.
- **Verwachte bestanden/systemen:** Theme-integratie, eventuele app, consent/analytics en servicekanaal `[NOG ONDERZOEKEN]`.
- **Uitvoer:** Goedgekeurd kanaal en geteste contactreis.
- **Acceptatiecriteria:** Contact bereikt de juiste ontvanger; beschikbaarheid/fallback en privacy zijn duidelijk; mobiel/toetsenbord werken.
- **Technische controles:** App-/scriptimpact, consent, performance, toegankelijkheid, foutstates en trackingvalidatie.
- **Menselijke controle:** Eigenaar en serviceverantwoordelijke keuren kanaal, tekst en afhandeling goed.
- **Bewijs van voltooiing:** Providerbesluit, tests, commits, preview en goedkeuring `[NOG ONDERZOEKEN]`.
- **Risico:** Derdepartijscripts kunnen privacy, performance en beschikbaarheid beïnvloeden.
- **Rollback of herstelwijze:** Integratie afzonderlijk kunnen uitschakelen en fallbackcontact behouden; plan vóór activering.
- **Laatst bijgewerkt:** 2026-08-03.

### BC-LOG-001 - Voorraad-, levertijd- en leverancierregels

- **ID:** `BC-LOG-001`
- **Titel:** Voorraad- en levertijdlogica per leverancier vaststellen
- **Fase:** Fase 9 - logistiek, voorraad en leveringslogica
- **Werkstroom:** Logistiek / datamodel
- **Status:** `BLOCKED`
- **Prioriteit:** `P0`
- **Doel:** Actuele voorraadstatus en betrouwbare levertijdbeloften mogelijk maken.
- **Aanleiding:** Circa 90% loopt naar verwachting via dropshipping en regels kunnen per leverancier verschillen.
- **Scope:** Eigen voorraad, leveranciersvoorraad, definities, updates, cutoff, levertijd, backorder, fouten en klanttekst.
- **Buiten scope:** API-koppelingen bouwen; die zijn later werk.
- **Afhankelijkheden:** Leveranciersinventaris, `BC-ADM-001`, `BC-DATA-001` en operationele besluiten.
- **Benodigde input:** Leveranciersbestanden/regels, eigen magazijnproces, updatefrequenties en verantwoordelijken `[NOG ONDERZOEKEN]`.
- **Verwachte bestanden/systemen:** Productdata, Shopify voorraad/locaties/instellingen en leveranciersbronnen `[NOG ONDERZOEKEN]`.
- **Uitvoer:** Goedgekeurde beslismatrix en datamapping voor voorraad/levertijd.
- **Acceptatiecriteria:** Elk relevant voorraad-/levertijdscenario heeft bron, betekenis, klanttekst, fallback, eigenaar en testvoorbeeld.
- **Technische controles:** Steekproeven per leverancier, stale/missing/conflictdata, cutoff- en backorderscenario's.
- **Menselijke controle:** Operationele en commerciële eigenaar keuren beloften en uitzonderingen goed.
- **Bewijs van voltooiing:** Regeldocument, bronsteekproeven en besluiten `[NOG ONDERZOEKEN]`.
- **Risico:** Onjuiste voorraad of levertijd leidt direct tot verkeerde klantbeloften.
- **Rollback of herstelwijze:** Conservatieve fallbacktekst en handmatig proces vooraf bepalen; geen brondata wijzigen in onderzoek.
- **Laatst bijgewerkt:** 2026-08-03.

### BC-LOG-002 - Verzending, dropshipping en afhalen

- **ID:** `BC-LOG-002`
- **Titel:** Fulfilment- en levermethodebeslisregels ontwerpen en realiseren
- **Fase:** Fase 9 - logistiek, voorraad en leveringslogica
- **Werkstroom:** Logistiek / checkout
- **Status:** `BLOCKED`
- **Prioriteit:** `P0`
- **Doel:** Pakket, pallet, afhalen, gecombineerde en gesplitste levering correct afhandelen en communiceren.
- **Aanleiding:** Bestellingen kunnen eigen voorraad en meerdere dropshipleveranciers combineren.
- **Scope:** Scenario's, beslisregels, kosten, planning, checkout/cartcommunicatie, tracking en klantoverleg.
- **Buiten scope:** Onbevestigde internationale expansie en toekomstige API-automatisering.
- **Afhankelijkheden:** `BC-LOG-001`, `BC-DATA-001`, Shopify verzendinstellingeninventaris en bedrijfsproces.
- **Benodigde input:** Product-/leverancierkenmerken, magazijnroute, vervoerders, zones, tarieven en overlegregels `[OPEN BESLISSING]`.
- **Verwachte bestanden/systemen:** Shopify verzending/checkout, cart/theme, magazijn-/leveranciersprocessen `[NOG ONDERZOEKEN]`.
- **Uitvoer:** Goedgekeurde scenario-/beslismatrix en geteste klantreis per levermethode.
- **Acceptatiecriteria:** Alle bevestigde methodes en multi-leveranciersscenario's hebben correcte keuze, kosten, tekst, tracking en herstelpad.
- **Technische controles:** Testorders/simulaties per scenario, prijs/zone, cart/checkout, notificaties en foutafhandeling.
- **Menselijke controle:** Operationele eigenaar en eigenaar keuren regels en klantcommunicatie goed.
- **Bewijs van voltooiing:** Matrix, testorders, configuratie-/commitbewijs en goedkeuring `[NOG ONDERZOEKEN]`.
- **Risico:** Verkeerde routing of tarief veroorzaakt marge-, vertraging- en serviceproblemen.
- **Rollback of herstelwijze:** Goedgekeurde handmatige fallback en herstel van verzendconfiguratie vóór activering vastleggen.
- **Laatst bijgewerkt:** 2026-08-03.

### BC-SVC-001 - Retouren, garantie en service

- **ID:** `BC-SVC-001`
- **Titel:** Retour-, garantie- en servicebeleid koppelen aan klantreizen
- **Fase:** Fase 9 - logistiek, voorraad en leveringslogica
- **Werkstroom:** Service / content
- **Status:** `BLOCKED`
- **Prioriteit:** `P1`
- **Doel:** Correcte en uitvoerbare service-informatie en processen bieden.
- **Aanleiding:** PDP's moeten retour-, garantie- en service-informatie tonen; regels zijn onbekend.
- **Scope:** Beleid, uitzonderingen, product-/leveranciersmapping, aanvraag/contact, routing, statussen en content.
- **Buiten scope:** Beleid verzinnen of publiceren zonder operationele/juridische goedkeuring.
- **Afhankelijkheden:** `BC-LOG-001`, `BC-DATA-001`, `BC-PDP-001` en goedgekeurd servicebeleid.
- **Benodigde input:** Termijnen, kosten, uitzonderingen, garanties, verantwoordelijken en procedures `[NOG ONDERZOEKEN]`.
- **Verwachte bestanden/systemen:** PDP/content, account/servicekanalen en operationele systemen `[NOG ONDERZOEKEN]`.
- **Uitvoer:** Goedgekeurd beleid, datamapping en geteste servicejourneys.
- **Acceptatiecriteria:** Relevante producttypes tonen juiste informatie; aanvragen bereiken juiste proces; uitzonderingen zijn traceerbaar.
- **Technische controles:** Productsteekproeven, links/formulieren, accountstates, toegankelijkheid en contentconsistentie.
- **Menselijke controle:** Eigenaar en operationele verantwoordelijke keuren beleid en preview goed.
- **Bewijs van voltooiing:** Beleidsbron, mapping, tests, commits en goedkeuring `[NOG ONDERZOEKEN]`.
- **Risico:** Onjuiste service-informatie kan verwachtingen en afhandeling schaden.
- **Rollback of herstelwijze:** Content/functionele change terugzetten en aanvragen via goedgekeurde handmatige route afhandelen.
- **Laatst bijgewerkt:** 2026-08-03.

### BC-SEO-001 - SEO-, inspiratie- en adviesstructuur

- **ID:** `BC-SEO-001`
- **Titel:** SEO-architectuur en contentecosysteem ontwerpen en realiseren
- **Fase:** Fase 10 - SEO-, inspiratie- en adviesstructuur
- **Werkstroom:** SEO / content
- **Status:** `BLOCKED`
- **Prioriteit:** `P0`
- **Doel:** Schaalbare organische vindbaarheid en bruikbare interne kennisroutes opbouwen.
- **Aanleiding:** SEO is bepalend voor categoriearchitectuur; inspiratie/advies zijn lanceringsscope en begrippen bestaan deels.
- **Scope:** Na opsplitsing: paginatypen, zoekintenties, interne links, metadata, canonicals, indexatie, redirects, structured data, contentworkflow en begrippen.
- **Buiten scope:** Blind kopiëren van concurrenten of URL's publiceren zonder migratieplan.
- **Afhankelijkheden:** `BC-DISC-002`, `BC-IA-001`, `BC-DATA-001`, `BC-CAT-001`, `BC-PDP-001` en contentinventaris.
- **Benodigde input:** Huidige URL/indexatie-/rankingdata, keyword/intentonderzoek, assortiment en contentcapaciteit `[NOG ONDERZOEKEN]`.
- **Verwachte bestanden/systemen:** Templates/sections/content/redirects en externe SEO-bronnen `[NOG ONDERZOEKEN]`.
- **Uitvoer:** Goedgekeurde SEO-architectuur, contentmodel, prioriteiten en opgesplitste implementatietaken.
- **Acceptatiecriteria:** Alle domeinen uit hoofdstuk 22 hebben regels, eigenaar, voorbeelden, indexatie-/canonicalgedrag en controles.
- **Technische controles:** Crawl-/URL-/canonical-/schema-/redirect-/interne-linkchecks en contentsteekproeven.
- **Menselijke controle:** Eigenaar keurt structuur, prioriteiten en openbare contentrichting goed.
- **Bewijs van voltooiing:** Onderzoek, architectuur, testresultaten, commits/previews en goedkeuring `[NOG ONDERZOEKEN]`.
- **Risico:** Zeer breed werkpakket; verplicht splitsen vóór `READY`; verkeerde URL/indexatiekeuzes hebben lang effect.
- **Rollback of herstelwijze:** URL-/redirect-/indexatiewijzigingen alleen met vooraf vastgesteld migratie- en herstelplan.
- **Laatst bijgewerkt:** 2026-08-03.

### BC-PROD-001 - Productonboarding voor circa 20.000 producten

- **ID:** `BC-PROD-001`
- **Titel:** Productimport, verrijking en datakwaliteit voor lancering uitvoeren
- **Fase:** Fase 11 - productonboarding en datakwaliteit voor 20.000 producten
- **Werkstroom:** Producten / datamodel
- **Status:** `BLOCKED`
- **Prioriteit:** `P0`
- **Doel:** Ongeveer 20.000 complete, gekoppelde, gecategoriseerde, zoekbare en filterbare producten opleveren.
- **Aanleiding:** Dit is het expliciete productdoel voor een complete lancering.
- **Scope:** Na opsplitsing: broninventaris, mapping, import, verrijking, validatie, relaties, categorie/filter, media, logistiek, SEO en uitzonderingen.
- **Buiten scope:** Ongecontroleerde bulkmutaties en toekomstige API-koppelingen.
- **Afhankelijkheden:** `BC-DATA-001`, `BC-IA-001`, `BC-SWITCH-001`, `BC-LOG-001`, `BC-SEO-001` en leveranciersbestanden.
- **Benodigde input:** Werkelijke leveranciersbestanden, bronhouders, kwaliteitsdrempels, assortimentselectie en foutproces `[NOG ONDERZOEKEN]`.
- **Verwachte bestanden/systemen:** Leveranciersdata, Shopify producten/collecties/metafields/media en validatietooling `[NOG ONDERZOEKEN]`.
- **Uitvoer:** Herhaalbare onboardingpipeline, uitzonderingsproces en kwaliteitsrapport voor lanceringsset.
- **Acceptatiecriteria:** Afgesproken aantal en drempels zijn gehaald; geen onverklaarde duplicaten/relatiefouten; steekproeven en totalen sluiten aan.
- **Technische controles:** Schema, referenties, SKU/URL-uniciteit, verplichte velden, media, prijzen, relaties, categorie/filter, SEO en logistieke data.
- **Menselijke controle:** Eigenaar/productverantwoordelijke keurt drempels, steekproeven en lanceringsset goed.
- **Bewijs van voltooiing:** Importlogs, validatierapport, uitzonderingen, steekproefgoedkeuring en herstelbewijs `[NOG ONDERZOEKEN]`.
- **Risico:** Grootste schaalrisico; fouten worden over duizenden producten vermenigvuldigd en werkpakket moet per bron/type/batch worden gesplitst.
- **Rollback of herstelwijze:** Voor iedere batch export/backup, dry-run, beperkte pilot en expliciet herstelplan vóór mutatie.
- **Laatst bijgewerkt:** 2026-08-03.

### BC-SEC-001 - Privacy en beveiliging

- **ID:** `BC-SEC-001`
- **Titel:** Privacy-, beveiligings- en uploadvereisten vaststellen en toetsen
- **Fase:** Fase 8 - conversie- en servicefuncties
- **Werkstroom:** Privacy / beveiliging
- **Status:** `BLOCKED`
- **Prioriteit:** `P0`
- **Doel:** Persoonsgegevens en bestanden alleen doelgebonden, minimaal en gecontroleerd verwerken.
- **Aanleiding:** Offertes, prijsaanvragen, afspraken, chat, accounts, samples en analytics kunnen persoonsgegevens verwerken.
- **Scope:** Gegevensinventaris, doelen, minimale velden, toestemming, opslag, toegang, retentie, verwijdering, leveranciers en uploadbeveiliging.
- **Buiten scope:** Juridische aannames of activering van gegevensverwerking zonder goedkeuring.
- **Afhankelijkheden:** `BC-ADM-001`, appinventaris en bedrijfsprocessen van afhankelijke functies.
- **Benodigde input:** Verantwoordelijke, beleid, verwerkers, bewaartermijnen en toegangsrollen `[NOG ONDERZOEKEN]`.
- **Verwachte bestanden/systemen:** Formulieren, accounts, apps, opslag, analytics/consent en beleidscontent `[NOG ONDERZOEKEN]`.
- **Uitvoer:** Goedgekeurde eisen, datastromen, controles en incident-/verwijderprocedures.
- **Acceptatiecriteria:** Iedere gegevensstroom heeft doel, grondslag/goedkeuring `[NOG ONDERZOEKEN]`, velden, ontvangers, opslag, retentie en herstelpad.
- **Technische controles:** Toegangs-, upload-, validatie-, logging-, consent- en verwijdertests per functie.
- **Menselijke controle:** Eigenaar en relevante privacy-/beveiligingsverantwoordelijke keuren eisen expliciet goed.
- **Bewijs van voltooiing:** Datastroomregister, testbewijs en goedkeuring `[NOG ONDERZOEKEN]`.
- **Risico:** Hoog risico op ongewenste toegang, malwareuploads of te lange opslag.
- **Rollback of herstelwijze:** Functie uitschakelen, toegang intrekken, incidentprocedure volgen en gegevens volgens goedgekeurd proces herstellen/verwijderen.
- **Laatst bijgewerkt:** 2026-08-03.

### BC-ANA-001 - Analytics, tracking en meetplan

- **ID:** `BC-ANA-001`
- **Titel:** Consentbewust analytics- en meetplan vaststellen en realiseren
- **Fase:** Fase 8 - conversie- en servicefuncties
- **Werkstroom:** Analytics / privacy
- **Status:** `BLOCKED`
- **Prioriteit:** `P1`
- **Doel:** Zakelijke en UX-resultaten meetbaar maken zonder ongecontroleerde tracking.
- **Aanleiding:** Huidige analytics/apps/consent zijn onbekend en kernfuncties hebben meetbehoefte.
- **Scope:** Inventaris, doelen, events, definities, consent, QA, rapportage, eigenaarschap en datakwaliteit.
- **Buiten scope:** Nieuwe tracking activeren vóór privacybesluit of onbevestigde marketingintegraties.
- **Afhankelijkheden:** `BC-ADM-001`, appinventaris, `BC-SEC-001` en functionele journeys.
- **Benodigde input:** Zakelijke KPI's, huidige tooling, consentbeleid, eventeigenaarschap en rapportagebehoefte `[OPEN BESLISSING]`.
- **Verwachte bestanden/systemen:** Theme/appscripts, consent- en analyticsplatforms `[NOG ONDERZOEKEN]`.
- **Uitvoer:** Goedgekeurd meetplan en gevalideerde implementatie per opgesplitste functie.
- **Acceptatiecriteria:** Elk event heeft doel, trigger, parameters, consentstatus, eigenaar, QA-methode en geen ongewenste duplicatie.
- **Technische controles:** Debug-/netwerkvalidatie, consentstates, duplicaten, datakwaliteit, performance en privacy.
- **Menselijke controle:** Eigenaar keurt KPI's/rapportage en privacyverantwoordelijke de gegevensverwerking goed.
- **Bewijs van voltooiing:** Meetplan, eventtests, screenshots/logs en goedkeuring `[NOG ONDERZOEKEN]`.
- **Risico:** Dubbele of consentloze tracking geeft onbetrouwbare data en privacyrisico.
- **Rollback of herstelwijze:** Nieuwe tags/events uitschakelen en terugkeren naar vooraf geïnventariseerde configuratie.
- **Laatst bijgewerkt:** 2026-08-03.

### BC-QA-001 - Integrale QA, performance en toegankelijkheid

- **ID:** `BC-QA-001`
- **Titel:** Integrale launchtestmatrix uitvoeren
- **Fase:** Fase 12 - integrale QA, performance en toegankelijkheid
- **Werkstroom:** QA / performance / accessibility
- **Status:** `BLOCKED`
- **Prioriteit:** `P0`
- **Doel:** Functionele, visuele en technische lanceringskwaliteit aantoonbaar maken.
- **Aanleiding:** Er is nog geen zichtbare testinrichting, CI of goedgekeurde browser-/performance-/a11ymatrix.
- **Scope:** Na opsplitsing: kernreizen, producttypes, data, regressie, browser/apparaat, mobiel/desktop, toetsenbord, performance, toegankelijkheid en SEO.
- **Buiten scope:** Defects stil accepteren of menselijk oordeel vervangen.
- **Afhankelijkheden:** Alle relevante implementatie- en contenttaken, browsermatrix en meetbare budgetten.
- **Benodigde input:** Testaccounts/data, representatieve producten, apparaten/browsers, budgets en releasecandidate `[NOG ONDERZOEKEN]`.
- **Verwachte bestanden/systemen:** Repository, preview-theme, Shopify testdata en testtooling `[NOG ONDERZOEKEN]`.
- **Uitvoer:** Opgesplitste testsets, defectregister, hertestbewijs en restrisicoadvies.
- **Acceptatiecriteria:** Alle goedgekeurde matrices zijn uitgevoerd; geen open P0; overige risico's zijn expliciet geaccepteerd of opgelost.
- **Technische controles:** Theme Check plus alle controles uit hoofdstuk 49 en checklists in hoofdstuk 63.
- **Menselijke controle:** Eigenaar voert/accordeert visuele en functionele acceptatie op preview.
- **Bewijs van voltooiing:** Testlogs, screenshots, metingen, defectstatussen en goedkeuring `[NOG ONDERZOEKEN]`.
- **Risico:** Dit werkpakket is zeer breed; verplicht per journey/kwaliteitsdomein splitsen vóór `READY`.
- **Rollback of herstelwijze:** Afgekeurde releasecandidate niet publiceren; terug naar laatste goedgekeurde previewcommit/themebasis.
- **Laatst bijgewerkt:** 2026-08-03.

### BC-REL-001 - Launch readiness en productiepublicatie

- **ID:** `BC-REL-001`
- **Titel:** Go/no-go, release, rollback en productiecontrole uitvoeren
- **Fase:** Fase 13 - launch readiness en productiepublicatie
- **Werkstroom:** Release / governance
- **Status:** `BLOCKED`
- **Prioriteit:** `P0`
- **Doel:** Alleen een complete, goedgekeurde release gecontroleerd live zetten.
- **Aanleiding:** Publicatie mag uitsluitend na expliciete menselijke goedkeuring en met herstelmogelijkheid.
- **Scope:** Readinessaudit, releasecandidate, bewijs, go/no-go, expliciete publicatieopdracht, rollbackgereedheid en post-releasecontrole.
- **Buiten scope:** Zelfstandig publiceren, scopegaten negeren of preview automatisch promoveren.
- **Afhankelijkheden:** Alle bevestigde launchscope `DONE`, `BC-QA-001`, open P0-risico's gesloten en releaseproces besloten.
- **Benodigde input:** Expliciete menselijke go/no-go en publicatieopdracht, releasevenster, verantwoordelijkheden en rollbackplan.
- **Verwachte bestanden/systemen:** GitHub `main`, goedgekeurd preview-theme, live theme en releasebewijs; exacte commando's `[OPEN BESLISSING]`.
- **Uitvoer:** Go/no-go-dossier en alleen bij expliciete toestemming een gecontroleerde productiepublicatie.
- **Acceptatiecriteria:** Complete launchdefinitie gehaald; bewijs compleet; rollback getest; eigenaar geeft expliciet akkoord; post-check slaagt.
- **Technische controles:** Git/themepariteit, diff, QA, backups, links, orders/kernreizen, monitoring en post-release smoke tests.
- **Menselijke controle:** Eigenaar is enige expliciete productie-goedgever; verantwoordelijke namen `[NOG ONDERZOEKEN]`.
- **Bewijs van voltooiing:** Getekend/goedgekeurd go/no-go, releasegegevens en post-check `[NOG ONDERZOEKEN]`.
- **Risico:** Onbedoelde livepublicatie heeft de grootste directe bedrijfsimpact.
- **Rollback of herstelwijze:** Exact rollbacktheme, commit, verantwoordelijkheden en commando's moeten vóór `READY` aantoonbaar zijn.
- **Laatst bijgewerkt:** 2026-08-03.

### BC-OPS-001 - Monitoring en optimalisatie

- **ID:** `BC-OPS-001`
- **Titel:** Post-launchmonitoring en gecontroleerde optimalisatie inrichten
- **Fase:** Fase 14 - monitoring, optimalisatie en toekomstige API's
- **Werkstroom:** Release / analytics / service
- **Status:** `DEFERRED`
- **Prioriteit:** `P2`
- **Doel:** Na lancering technische, commerciële en servicekwaliteit volgen en verbeteren.
- **Aanleiding:** Een complete lancering vereist opvolging; concrete KPI's en tooling zijn nog onbekend.
- **Scope:** Beschikbaarheid, fouten, performance, conversie, zoeken, datafeeds, orders, service en verbeterbacklog.
- **Buiten scope:** Ongecontroleerde automatische wijzigingen of optimalisatie vóór basislancering.
- **Afhankelijkheden:** `BC-REL-001`, `BC-ANA-001` en operationele eigenaars.
- **Benodigde input:** KPI's, alerts, verantwoordelijkheden, ritme en incidentproces `[OPEN BESLISSING]`.
- **Verwachte bestanden/systemen:** Analytics, logging/monitoring, Shopify en serviceprocessen `[NOG ONDERZOEKEN]`.
- **Uitvoer:** Monitoringplan, dashboards, alerts en geprioriteerde verbetercyclus.
- **Acceptatiecriteria:** Elke kritieke metric heeft bron, grens, eigenaar, reactie en rapportageritme.
- **Technische controles:** Alerttests, datakwaliteit, incidentoefening en periodieke controles.
- **Menselijke controle:** Eigenaar keurt KPI's, prioriteiten en optimalisaties afzonderlijk goed.
- **Bewijs van voltooiing:** Monitoringconfiguratie, testalerts, rapporten en besluiten `[NOG ONDERZOEKEN]`.
- **Risico:** Zonder monitoring blijven regressies en dataproblemen onzichtbaar.
- **Rollback of herstelwijze:** Monitoringwijzigingen afzonderlijk terugdraaien; productie-optimalisaties volgen normale releasegates.
- **Laatst bijgewerkt:** 2026-08-03.

### BC-API-001 - Toekomstige leverancier-API's

- **ID:** `BC-API-001`
- **Titel:** Product-, prijs- en voorraadfeeds later aan bestaande producten koppelen
- **Fase:** Fase 14 - monitoring, optimalisatie en toekomstige API's
- **Werkstroom:** Datamodel / integraties
- **Status:** `DEFERRED`
- **Prioriteit:** `P2`
- **Doel:** Later gecontroleerde en herhaalbare leveranciersupdates mogelijk maken.
- **Aanleiding:** Leveranciersbestanden/API's volgen later; architectuur moet voorbereid zijn, implementatie is geen eerste prioriteit.
- **Scope:** Later per leverancier: specificatie, mapping, authenticatie, scheduling, validatie, fouten, audit en herstel.
- **Buiten scope:** Huidige fase, onbevestigde providers en automatische writes zonder pilot/rollback.
- **Afhankelijkheden:** `BC-DATA-001`, `BC-PROD-001`, `BC-LOG-001`, leveranciers-API-documentatie en prioriteitsbesluit.
- **Benodigde input:** API-specificaties, credentials/beveiliging, SLA's, bronhouders en updatevereisten `[NOG ONDERZOEKEN]`.
- **Verwachte bestanden/systemen:** Externe API's en integratielaag `[NOG ONDERZOEKEN]`; niet automatisch theme-code.
- **Uitvoer:** Afzonderlijke leverancierwerkpakketten en gecontroleerde integraties.
- **Acceptatiecriteria:** Per feed zijn mapping, idempotentie, validatie, conflictregels, monitoring, audit en rollback bewezen.
- **Technische controles:** Sandbox/pilot, rate limits, retries, stale/conflictdata, dry-run en hersteltest.
- **Menselijke controle:** Eigenaar en data-/operationele verantwoordelijke keuren iedere feed en activering goed.
- **Bewijs van voltooiing:** API-besluit, pilotlogs, validatie, monitoring en goedkeuring `[NOG ONDERZOEKEN]`.
- **Risico:** Geautomatiseerde foutdata kan prijzen, voorraad of duizenden producten beschadigen.
- **Rollback of herstelwijze:** Immutable bronlogs, snapshots, dry-run, beperkte batches en expliciete terugzetprocedure vóór writes.
- **Laatst bijgewerkt:** 2026-08-03.

## 58. Beslislogboek

Alleen expliciet bevestigde keuzes staan hieronder. Een ontbrekende keuze hoort in hoofdstuk 59, niet in dit logboek.

| ID | Datum | Bevestigde beslissing | Reden | Bron |
| --- | --- | --- | --- | --- |
| `BC-DEC-001` | 2026-08-03 | Nederland is de primaire markt en de site is bij lancering Nederlandstalig | Internationale uitbreiding is nu geen hoofdprioriteit | Projectdefinitie |
| `BC-DEC-002` | 2026-08-03 | BadkamerCity positioneert zich met scherpe prijzen, deskundig advies en exclusieve merken | Dit is de bevestigde commerciële propositie | Projectdefinitie |
| `BC-DEC-003` | 2026-08-03 | Doel is lancering met ongeveer 20.000 volledig ingerichte producten, niet bewust met een halve webshop | Compleetheid en goedkeuring zijn launchvoorwaarden | Projectdefinitie |
| `BC-DEC-004` | 2026-08-03 | Iedere verkoopbare uitvoering krijgt een eigen product, URL en SKU; normale meerkeuzevarianten zijn niet het productmodel | Zelfstandige producten zijn de gekozen productarchitectuur | Projectdefinitie |
| `BC-DEC-005` | 2026-08-03 | Huidige switchers/configurators navigeren naar een bestaand product en stellen geen losse cartbundel samen | Dit definieert de huidige functionele grens | Projectdefinitie |
| `BC-DEC-006` | 2026-08-03 | Tegels krijgen een m²-calculator; douchesets en badkamermeubels krijgen een productnavigerende configurator | Bevestigde producttype-eisen | Projectdefinitie |
| `BC-DEC-007` | 2026-08-03 | Wishlist, samples, offerte-upload, laagsteprijsgarantie, account/historie/tracking, afspraak, WhatsApp/chat en inspiratie/advies zijn gewenste lanceringsfuncties | Bevestigde scope | Projectdefinitie |
| `BC-DEC-008` | 2026-08-03 | Harry Suiker is nu moederbedrijf/operationele basis; BadkamerCity mag nog niet als zelfstandige showroomlocatie worden voorgesteld | Correcte en niet-misleidende positionering | Projectdefinitie |
| `BC-DEC-009` | 2026-08-03 | Rust, overzicht en vertrouwen blijven designprincipes; mobiel is even belangrijk als desktop | Bevestigde UX-richting | Projectdefinitie |
| `BC-DEC-010` | 2026-08-03 | Pakket, pallet, afhalen, gecombineerde en gesplitste levering moeten kunnen worden ondersteund | Bevestigde logistieke behoefte | Projectdefinitie |
| `BC-DEC-011` | 2026-08-03 | API-koppelingen zijn geen eerste ontwikkelprioriteit; datamodel/architectuur moeten toekomstige feeds wel toelaten | Gefaseerde integratiestrategie | Projectdefinitie |
| `BC-DEC-012` | 2026-08-03 | `main` is de goedgekeurde basis; ontwikkeling gebeurt niet direct op live; preview via development-theme; live alleen na expliciete menselijke goedkeuring | Veiligheid en eigenaarschap | Projectdefinitie en `docs/DEVELOPMENT_THEME.md` |
| `BC-DEC-013` | 2026-08-03 | `CITY_MASTER` is voor de zeven theme-mappen de technische live-snapshot van 2026-08-03 | Hashvergelijking vond geen verschillen | `docs/LIVE_THEME_COMPARISON.md` |
| `BC-DEC-014` | 2026-08-04 | Masterplan v0.1 is goedgekeurd als basis voor verder onderzoekswerk; dit geeft geen toestemming voor theme-code, Shopify Admin-mutaties, theme-pushes, publicatie of implementatie | Discovery kan gecontroleerd starten terwijl implementatiegates intact blijven | Expliciete menselijke opdracht van de projecteigenaar |
| `BC-DEC-015` | 2026-08-04 | De officiële Shopify CLI `store auth`-route voor `fpa9hu-i3.myshopify.com` en dertien benoemde read-scopes zijn uitsluitend voor `BC-ADM-001` goedgekeurd | Maakt begrensd Admin-bewijs mogelijk zonder write-scopes, mutaties of implementatietoestemming | Expliciete menselijke opdrachten en `currentAppInstallation.accessScopes` |
| `BC-DEC-016` | 2026-08-04 | Theme `192796786954` mag alleen als bestaand unpublished theme read-only worden geregistreerd | Eigenaarschap, exact doel en ontstaansreden blijven onbekend; aanpassen, verwijderen, publiceren, pushen en pullen zijn verboden | Expliciete menselijke opdracht van de projecteigenaar |
| `BC-DEC-017` | 2026-08-04 | `BC-ADM-001` is menselijk goedgekeurd als afgeronde read-only inventarisatie en gaat naar `DONE`; `BC-DISC-001` wordt de actieve taak met status `READY` | De inventaris voldoet binnen de vastgelegde grenzen; beperkingen en open vragen blijven bestaan | Expliciete menselijke goedkeuring van de projecteigenaar; geen toestemming voor Shopify-/theme-/scope-/implementatiewijzigingen |
| `BC-DEC-018` | 2026-08-04 | `BC-DISC-001` mag uitsluitend read-only worden uitgevoerd; repositorydocumentatie mag na onderzoek worden bijgewerkt, maar Shopify, themes, theme-code, apps en scopes mogen niet wijzigen | Maakt een begrensde actieve-themegebruiksmatrix mogelijk zonder implementatie- of publicatietoestemming | Expliciete menselijke startopdracht van de projecteigenaar; `BC-DISC-002` mag niet worden geactiveerd |
| `BC-DEC-019` | 2026-08-05 | `BC-DISC-001` is als afgerond read-only onderzoek goedgekeurd en gaat naar `DONE`; `BC-DISC-002` wordt de actieve volgende taak op `READY`, zonder inhoudelijke uitvoering | De gebruiksmatrix voldoet binnen de vastgelegde bewijsgrenzen; classificaties zijn geen verwijdertoestemming en alle beperkingen blijven bestaan | Expliciete menselijke goedkeuring van de projecteigenaar; buiten deze twee projectadministratiedocumenten geen Shopify-, theme-, app-, scope-, bestands- of implementatietoestemming |
| `BC-DEC-020` | 2026-08-05 | `BC-DISC-002` mag uitsluitend als openbare read-only steekproef van BadkamerXXL, Sanitairwinkel en Sanitairkamer worden uitgevoerd; alleen het rapport en masterplan mogen wijzigen | Maakt begrensd concurrentie-/SEO-bewijs mogelijk zonder account-, formulier-, crawl-, Shopify-, theme- of implementatiehandelingen | Expliciete menselijke startopdracht van de projecteigenaar; geen patroonkeuze of volgende taak geactiveerd |
| `BC-DEC-021` | 2026-08-05 | `BC-DISC-002` en fase 1 zijn `DONE`; `BC-DATA-002` wordt als actieve kleine read-only voorbereidingstaak `READY` aangemaakt maar niet inhoudelijk gestart; `BC-DATA-001` blijft `BLOCKED` | Rondt de goedgekeurde inventarisatiefase af en maakt uitsluitend bronbewijs voor het latere datamodel bestuurbaar klaar | Expliciete menselijke goedkeuring/opdracht van de projecteigenaar; geen patroon-, ontwerp-, SEO-, Shopify-, theme-, data- of implementatietoestemming |
| `BC-DEC-022` | 2026-08-10 | `BC-DATA-002` mag uitsluitend als lokale read-only repositoryinventarisatie worden uitgevoerd, gaat bij technische afronding naar `REVIEW` en activeert geen volgende taak | Maakt volledig lokaal bron-, script-, veld- en ontbrekende-inputbewijs mogelijk zonder imports, Shopify- of codewijziging | Expliciete menselijke startopdracht van de projecteigenaar; alleen `docs/SUPPLIER_DATA_INVENTORY.md` en dit masterplan mogen wijzigen, geen commit of push |
| `BC-DEC-023` | 2026-08-10 | `BC-DATA-002` is binnen de lokale scope compleet en `DONE`; nul oorspronkelijke lokale bronnen is een geaccepteerde bevinding. Externe bronnen volgen later per leverancier. `BC-DATA-003` wordt actief `READY`, maar is nog niet inhoudelijk gestart | Voorkomt nutteloos zoekwerk buiten `CITY_MASTER` en maakt een logisch brononafhankelijk contract mogelijk zonder definitieve mapping of opslagkeuze | Expliciete menselijke goedkeuring/opdracht van de projecteigenaar; alleen documentatie, geen Shopify-, bron-, theme-, data- of implementatietoestemming |
| `BC-DEC-024` | 2026-08-10 | `BC-DATA-003` mag na de gepushte fase-A-commit uitsluitend als brononafhankelijke read-only documentatietaak worden uitgevoerd en gaat technisch afgerond naar `REVIEW`; er wordt geen volgende taak geactiveerd | Legt functionele informatiebehoefte en kwaliteitsprincipes vast zonder te wachten op bronnen of een Shopify-/leveranciermapping te verzinnen | Expliciete tweefasenopdracht van de projecteigenaar; geen Shopify-, theme-, bron-, import-, categorie-, URL-, SEO-, design- of implementatietoestemming |
| `BC-DEC-025` | 2026-08-10 | `BC-DATA-003` is binnen zijn brononafhankelijke documentatiescope `DONE`; productinformatiecontract v0.1 is een bestuurde conceptuele werkbasis. `BC-TECH-002` wordt uitsluitend als read-only planningsopdracht actief `READY` en blijft **NIET INHOUDELIJK GESTART** | Sluit de conceptuele contracttaak bestuurbaar af en splitst de brede technische epic eerst op zonder implementatie | Expliciete beperkte menselijke goedkeuring/opdracht; individuele contractkeuzes, Shopify-/leveranciermapping en alle technische wijzigingen blijven onbevoegd |
| `BC-DEC-026` | 2026-08-11 | `BC-TECH-002` mag vanuit de exact gecontroleerde gedeeltelijke uitvoering uitsluitend read-only worden afgerond en gaat daarna naar `REVIEW`; kandidaat-ID's blijven voorstellen en geen volgende taak wordt actief | Rondt de technische nulmeting en decompositie af zonder fase A te herhalen of een defect, theme of Shopify te wijzigen | Expliciete hervatopdracht van de projecteigenaar; geen commit, push, implementatie, verwijdering, theme- of Shopify-toestemming |
| `BC-DEC-027` | 2026-08-11 | `BC-TECH-002` is binnen read-only onderzoeks- en decompositiescope `DONE`; `BC-GOV-006` wordt uitsluitend als lokale governance-/toolingtaak actief `READY` en blijft **NIET INHOUDELIJK GESTART** | Sluit het goedgekeurde stabilisatieplan bestuurbaar af en maakt controleerbare toekomstige Codex-uitvoering mogelijk zonder technische kandidaat te starten | Expliciete menselijke goedkeuring en tweefasenopdracht; geen Shopify-, theme-, code-, data-, kandidaat- of implementatietoestemming |

**Aanvullende beslisregel `BC-DEC-028` (2026-08-11):** `BC-GOV-006` mag uitsluitend lokaal het permanente loggingprotocol, guardrails, vier PowerShell-helpers en genegeerd runbewijs bouwen en zelftesten en gaat daarna naar `REVIEW`; geen technische kandidaat wordt gestart. Dit maakt toekomstige Codex-uitvoering controleerbaar zonder Shopify-, theme-, productdata- of implementatiehandeling. Bron is de expliciete fase-B-opdracht van de projecteigenaar; dit is geen protocolgoedkeuring, kandidaatstart, commit- of pushtoestemming.

**Aanvullende beslisregel `BC-DEC-029` (2026-08-11):** de projecteigenaar keurt `BC-GOV-006` inhoudelijk goed nadat drie concrete reviewbevindingen aantoonbaar zijn opgelost: de normale bundle bevat voortaan hashgecontroleerde `review_files/`, child PowerShell-cmdletfouten gebruiken `ErrorActionPreference = Stop` en de finalizer weigert ieder incompleet of inconsistent raw command-quartet. `BC-GOV-006` en fase 0 gaan naar `DONE`; de acht protocolbestanden mogen met `chore: finalize Codex execution logging` naar `main`. Dit is geen goedkeuring van `PROPOSED-TECH-01`, Shopify-, theme-, productdata- of implementatiewerk.

## 59. Open vragenregister

| ID | Open vraag | Waarom belangrijk | Afhankelijke taak | Beslisser | Status |
| --- | --- | --- | --- | --- | --- |
| `BC-Q-001` | Wie is de formele projecteigenaar en wie vervangt deze bij afwezigheid? | Goedkeuring en escalatie vereisen eigenaarschap | Alle taken | BadkamerCity-eigenaar | `[NOG ONDERZOEKEN]` |
| `BC-Q-002` | Welke exacte showroomtekst en locatiegegevens mogen openbaar? | Voorkomt misleiding en operationele onduidelijkheid | `BC-SHOW-001` | Eigenaar en relevante inhoud/juridische verantwoordelijke | `[OPEN BESLISSING]` |
| `BC-Q-003` | Wat staat werkelijk actief in producten, collecties, metafields, metaobjects, menu's, apps en templates? | Externe data bepaalt vrijwel alle implementatie | `BC-ADM-001` en vervolg | Eigenaar/Shopify-beheerder `[NOG ONDERZOEKEN]` | Kernobjecten, live JSON en statische themegebruiksmatrix zijn bewezen; runtimepaden en volledige app-/pixelbron blijven onvolledig respectievelijk **NIET TOEGANKELIJK** |
| `BC-Q-004` | Welke metafields bestaan, met welke types, validaties en eigenaars? | Nodig voor definitieve opslag, PDP en switcher | `BC-DATA-003`, `BC-DATA-001`, `BC-SWITCH-001` | Productdata-eigenaar `[NOG ONDERZOEKEN]` | Theme-code verwijst naar 58 statische custom keys en kan legacykeys dynamisch lezen; alleen `custom.switch_group` heeft een bewezen definitie. `BC-DATA-003` beschrijft alleen logische begrippen; definitieve namen, opslag en eigenaarschap blijven `[NOG ONDERZOEKEN]` |
| `BC-Q-005` | Wie beheert/genereert `product-switcher-data.json` en wat is de bron van waarheid? | Data en metafields moeten exact synchroon zijn | `BC-SWITCH-001` | Technisch/productdata-eigenaar `[NOG ONDERZOEKEN]` | Asset bevat 433 groepen en 3.383 unieke handles tegenover 3.658 Admin-producten met trigger; lokale generator, mapping en oorspronkelijke bron zijn **ONTBREEKT**, bronhouder en volledige setvergelijking `[NOG ONDERZOEKEN]` |
| `BC-Q-006` | Blijft de legacy `custom.group`-fallback bestaan of wordt deze gemigreerd? | Dubbele codepaden verhogen regressierisico | `BC-SWITCH-001` | Eigenaar plus technisch verantwoordelijke | `[OPEN BESLISSING]`; code is actief bereikbaar, maar huidige Admin-dekking van `custom.group` is 0/7.827 |
| `BC-Q-007` | Wat wordt de definitieve categorieboom, URL-structuur en navigatie? | Bepaalt assortiment, UX en SEO | `BC-IA-001` | Eigenaar na onderzoek | `[OPEN BESLISSING]` |
| `BC-Q-008` | Welke leveranciers, regels, bestanden en updatefrequenties gelden? | Nodig voor actuele voorraad/levertijd en imports | Latere taken per leverancier, `BC-LOG-001`, `BC-PROD-001` | Operationele/productdata-eigenaar `[NOG ONDERZOEKEN]` | `BC-DATA-002` is `DONE` met nul oorspronkelijke lokale bronnen. Externe bronnen worden later per leverancier afzonderlijk aangeleverd; bronhouders, regels en frequenties blijven `[NOG ONDERZOEKEN]` |
| `BC-Q-009` | Hoe wordt elke multi-leveranciersbestelling gerouteerd en gecommuniceerd? | Bepaalt checkout, kosten en klantbelofte | `BC-LOG-002` | Operationele eigenaar | `[OPEN BESLISSING]` |
| `BC-Q-010` | Welke buitenlandse leverlanden en voorwaarden gelden bij lancering? | Buitenlandse klanten mogen bestellen, regels ontbreken | `BC-LOG-002` | Eigenaar/operationeel | `[OPEN BESLISSING]` |
| `BC-Q-011` | Zijn productreviews lanceringsscope? | Beïnvloedt data, apps, PDP, privacy en moderatie | `BC-PDP-001` | Eigenaar | `[OPEN BESLISSING]` |
| `BC-Q-012` | Is producten vergelijken lanceringsscope? | Beïnvloedt kaarten, PDP, data en UX | `BC-CAT-001`, `BC-PDP-001` | Eigenaar | `[OPEN BESLISSING]` |
| `BC-Q-013` | Welke technische/operationele oplossing geldt voor wishlist en samples? | Nodig voor accounts, cart, data en logistiek | `BC-CONV-001`, `BC-SAMPLE-001` | Eigenaar na Admin/appinventaris | `[OPEN BESLISSING]` |
| `BC-Q-014` | Welke uploadvelden, bestandstypen, opslag, toegang en retentie gelden voor offertes? | Hoog privacy- en securityrisico | `BC-QUOTE-001`, `BC-SEC-001` | Eigenaar en privacy/securityverantwoordelijke `[NOG ONDERZOEKEN]` | `[OPEN BESLISSING]` |
| `BC-Q-015` | Wat zijn voorwaarden en afhandeling van de laagsteprijsgarantie? | Claim moet uitvoerbaar en correct zijn | `BC-PRICE-001` | Eigenaar/commercieel verantwoordelijke | `[OPEN BESLISSING]` |
| `BC-Q-016` | Welke accountjourneys en ordertrackingbron worden gebruikt naast het bewezen `NEW_CUSTOMER_ACCOUNTS`-model? | Nodig voor accountjourneys en persoonsgegevens | `BC-ACC-001` | Eigenaar/Shopify-beheerder | `[OPEN BESLISSING]` |
| `BC-Q-017` | Wordt WhatsApp, chat of beide gebruikt, met welke provider/SLA? | Bepaalt service, scripts, privacy en performance | `BC-CHAT-001` | Eigenaar/serviceverantwoordelijke | `[OPEN BESLISSING]` |
| `BC-Q-018` | Welke analytics-, consent- en marketingtools zijn actief en gewenst? | Nodig voor betrouwbaar en toegestaan meetplan | `BC-ANA-001`, `BC-SEC-001` | Eigenaar/privacy/marketing `[NOG ONDERZOEKEN]` | Live JSON bevat geen app blocks/embeds; volledige app-/pixelconfiguratie **NIET TOEGANKELIJK** |
| `BC-Q-019` | Welke browsers, apparaten en assistieve technologie worden formeel ondersteund? | Nodig voor meetbare QA en DoD | `BC-QA-001` | Eigenaar na analytics/UX-advies | `[OPEN BESLISSING]` |
| `BC-Q-020` | Welke performancebudgetten gelden per kernpagina? | Zonder grens is verbetering niet toetsbaar | `BC-QA-001`, performancewerk | Technisch verantwoordelijke/eigenaar | `[OPEN BESLISSING]` |
| `BC-Q-021` | Welke apps zijn afhankelijk van theme-markup of app-embeds? | Wijzigingen kunnen verborgen integraties breken | `BC-DISC-001`, alle implementatie | Shopify-beheerder `[NOG ONDERZOEKEN]` | Nul actieve JSON-appblocks/embeds bewezen; acht sections ondersteunen `@app` en dynamische injectiepunten bestaan; volledige applijst **NIET TOEGANKELIJK** |
| `BC-Q-022` | Wat is het exacte branch-, PR-, release- en rollbackproces? | Nodig vóór veilige implementatie/publicatie | `BC-TECH-001`, `BC-REL-001` | Eigenaar en technisch verantwoordelijke | `[OPEN BESLISSING]` |
| `BC-Q-023` | Welke andere productgroepen krijgen een calculator/configurator? | Beïnvloedt datamodel en fase 7-scope | Toekomstige `BC-CONF-*` | Eigenaar na assortimentonderzoek | `[NOG ONDERZOEKEN]` |
| `BC-Q-024` | Hoe werkt een toekomstige complete-badkamerconfigurator? | Moet later mogelijk zijn zonder huidige scope te verstoren | `BC-CONF-003` | Eigenaar | `[OPEN BESLISSING]` |
| `BC-Q-026` | Wie is eigenaar van theme `192796786954`, wat was het exacte doel en waarom is het ontstaan? | Voorkomt onbedoelde wijziging of verwijdering van een bestaande testomgeving | `BC-DISC-001`, alle themetaken | Projecteigenaar/technisch eigenaar | `[NOG ONDERZOEKEN]` |
| `BC-Q-027` | Welke bevoegde read-only bron mag de volledige app-, pixel-, script- en externe-integratielijst leveren? | De huidige scopes bewijzen alleen de huidige CLI-installatie en actieve JSON-referenties | `BC-DISC-001`, `BC-SEC-001`, `BC-ANA-001` | Projecteigenaar/Shopify-beheerder | `[OPEN BESLISSING]` |
| `BC-Q-028` | Welke kandidaat-legacy-, orphan- en backup/debugbestanden mogen na runtimevalidatie behouden of in een aparte taak verwijderd worden? | Geen inkomende statische referentie is geen verwijderbewijs en sommige kandidaten bevatten bekende defectrisico's | `BC-TECH-001`, `BC-SWITCH-001` | Projecteigenaar plus technisch verantwoordelijke | `[OPEN BESLISSING]`; onderzoeksclassificaties op 2026-08-05 goedgekeurd, maar geen verwijdering of wijziging toegestaan |
| `BC-Q-029` | Welke onderzochte IA-, filter-, kaart-, PDP-, content- en servicepatronen passen na eigen assortiment-/klantbewijs werkelijk bij BadkamerCity? | Concurrentieobservaties zijn geen eigen ontwerp- of SEO-besluit | `BC-IA-001`, `BC-CAT-001`, `BC-PDP-001`, `BC-SEO-001` | Projecteigenaar na data- en zoekintentieonderzoek | `[OPEN BESLISSING]`; `BC-DISC-002` levert alleen onderzoeksinput |
| `BC-Q-030` | Welke toegestane tooling, viewports en criteria gelden voor een latere echte mobiele, desktop-, zoek- en toetsenbordtest? | HTML alleen bewijst geen visueel of interactief gedrag | `BC-UX-001`, `BC-CAT-001`, `BC-PDP-001`, `BC-QA-001` | Projecteigenaar en technisch/UX-verantwoordelijke | `[OPEN BESLISSING]` |
| `BC-Q-031` | Welke leveranciers-/importbestanden en scripts zijn lokaal werkelijk aanwezig, welke ontbreken en wie is bronhouder per veld? | Zonder bron-, veld- en eigenaarschapbewijs kan `BC-DATA-001` een verkeerde definitieve mapping vastleggen | Latere taken per leverancier, daarna `BC-DATA-001`, `BC-LOG-001`, `BC-PROD-001` | Projecteigenaar en productdata-/operationele eigenaar `[NOG ONDERZOEKEN]` | Lokaal **BEWEZEN en goedgekeurd**: nul oorspronkelijke bronnen, nul importbestanden, nul import-/generatiescripts, zes afgeleide switcherdata-assets en vijf relevante storefront-JavaScriptbestanden. Externe bestanden, veldbronhouders en eigenaarschap blijven `[NOG ONDERZOEKEN]`; geen verder lokaal zoekwerk binnen `BC-DATA-002` |
| `BC-Q-032` | Welke van de 190 logische contractkeys, vereisteniveaus, leegstaatregels, kwaliteitsgates en eigenaarsrollen worden veld- en typegewijs definitief goedgekeurd? | De bestuurde werkbasis mag niet stil als definitieve Shopify-mapping of bedrijfsregel worden gebruikt | `BC-DATA-001` en functionele taken | Projecteigenaar plus bevoegde domeineigenaars | `[OPEN BESLISSING]`; v0.1 is als conceptuele werkbasis goedgekeurd, individuele keuzes niet |
| `BC-Q-033` | Welke kleine kandidaatdeeltaak uit `BC-TECH-002` krijgt als eerste afzonderlijke uitvoeringstoestemming? | De brede epic mag niet direct starten en technische classificatie is geen implementatiebesluit | `BC-TECH-002`, daarna eventueel een `BC-TECH-001`-deeltaak | Projecteigenaar plus technisch verantwoordelijke | `[OPEN BESLISSING]`; plan adviseert eerst een reproduceerbare Theme Check-/kwaliteitsbasis, maar activeert die niet |
| `BC-Q-034` | Wat mag een klant zien wanneer geen actuele, brongebonden levertijd is bewezen? | De actieve PDP toont nu vaste tekst `Verwachte levertijd: 8 - 9 weken` zonder bewezen databron | Afzonderlijke toekomstige technische taak, `BC-LOG-001` | Projecteigenaar plus commercieel en operationeel/logistiek eigenaar | `[OPEN BESLISSING]`; kies verbergen of een exact goedgekeurde fallback, bron, actualiteitsgrens en eigenaar; geen vervangende tekst is vastgesteld |
| `BC-Q-035` | Welke Shopify CLI-/Theme Check-versie, configuratie en updateprocedure gelden als reproduceerbare kwaliteitsbasis? | De volledige run is bewijsbaar, maar configuratie ontbreekt, een externe schemafout is instabiel en de CLI dreef tijdens de gedeeltelijke uitvoering van 4.6.0 naar 4.6.1 | Eventuele eerste afzonderlijke technische toolingtaak | Projecteigenaar plus technisch eigenaar | `[OPEN BESLISSING]`; geen repositoryconfiguratie of repositorypackage gewijzigd; de globale self-update staat als toolingbeperking vast |
| `BC-Q-036` | Welke definitieve retentietermijn en eigenaar gelden voor lokale Codex-runbundles na menselijke review? | Volledige logs en reviewbestanden verbeteren controleerbaarheid maar kunnen onnodig lang lokaal blijven | Alle toekomstige taken | Projecteigenaar plus technisch en privacyverantwoordelijke | `[OPEN BESLISSING]`; protocol en one-bundle-uploadselectie zijn menselijk goedgekeurd en `DONE`, maar retentietermijn, lokale opschoning en eigenaar blijven afzonderlijk te besluiten |

De goedkeuring van `BC-ADM-001`, `BC-DISC-001`, `BC-DISC-002`, `BC-DATA-002` en `BC-DATA-003` sluit deze resterende vragen niet; zij bevestigt en begrenst het beschikbare read-only bewijs en de conceptuele werkbasis. Geen van deze goedkeuringen neemt een bronacceptatie-, individueel veld-, data-, ontwerp-, Shopify-, theme- of implementatiebesluit.

## 60. Risicoregister

| ID | Risico en bewijs | Impact | Beheersing / taak | Status |
| --- | --- | --- | --- | --- |
| `BC-R-001` | V2- en legacyproduct-switcher bestaan naast elkaar; V2 is door 3.658 producten getriggerd, legacycode is globaal aanwezig maar `custom.group` staat op 0/7.827 | Verkeerde/afwijkende productnavigatie | Volledige Admin/asset-setvergelijking, architectuurbesluit en combinatietests in `BC-SWITCH-001` | `[GEBLOKKEERD]` |
| `BC-R-002` | Primaire switcherdataset is 1.894.030 bytes; acht backup/debugassets staan live en V2 schrijft informatieve debugregels naar de console | Performance, ruis en theme-beheer | Payloadmeting, bronkeuze en afzonderlijk goedgekeurde backup/legacytaak na runtimebewijs | `[NOG ONDERZOEKEN]` |
| `BC-R-003` | `main-product.liquid` is circa 143 KB met inline CSS/JS en veel verantwoordelijkheden | Hoog regressie- en onderhoudsrisico | Kleine stabilisatie- en PDP-taken met previewbewijs | `[GEBLOKKEERD]` |
| `BC-R-004` | Actief bewijs toont zes hardcoded `#`-headerlinks, twee productuitleg-`#`-links, 17 lege homepage-linkvelden, 14 lege collectievelden en vier placeholderbeschrijvingen | Dode routes, onvolledige UX en SEO-schade | IA/contentbesluit en checklist vóór launch; niets herstellen binnen discovery | `[GEBLOKKEERD]` |
| `BC-R-005` | Zes losse product-/collectiesections en zes snippets zijn orphan/legacykandidaat; productmedia mist context en `bc-related-products` nest een section | Theme Editor of onzorgvuldige opruiming kan defect gedrag veroorzaken | Classificatie is menselijk goedgekeurd als onderzoek; wijziging/verwijdering blijft geblokkeerd tot runtimebewijs en een aparte `BC-TECH-001`-subtaak | `[GEBLOKKEERD]` |
| `BC-R-006` | Theme Check vond 1 error en 11 warnings; CLI eindigde met Windows assertion failure | Echte issues en toolingissues kunnen door elkaar lopen | Herhaalbare tooling, classificatie en expliciete uitzonderingen | `[GEBLOKKEERD]` |
| `BC-R-007` | Geen zichtbare tests, CI, lintconfig of volledige releasehandleiding | Regressies en inconsistente kwaliteit | Teststrategie, checks en releaseproces vóór implementatie | `[GEBLOKKEERD]` |
| `BC-R-008` | Admin- en themegebruiksmatrix zijn beschikbaar en actieve JSON bevat nul appblocks/embeds, maar acht sections ondersteunen `@app`, dynamische injectiepunten bestaan en de volledige app-/pixel-/scriptlijst bleef niet toegankelijk | Verborgen afhankelijkheden kunnen bij implementatie worden gemist | Bevoegde aanvullende bewijsbron afzonderlijk besluiten; afwezigheid nooit claimen | `[NOG ONDERZOEKEN]` |
| `BC-R-009` | Circa 20.000 producten vergroten ieder mapping-/kwaliteitsprobleem | Grootschalige commerciële/datafouten | Datamodel, pilots, batchvalidatie en rollback in `BC-PROD-001` | `[GEBLOKKEERD]` |
| `BC-R-010` | Leverancierregels verschillen en circa 90% loopt via dropshipping | Verkeerde voorraad, levertijd, kosten of levering | `BC-LOG-001` en `BC-LOG-002` met scenario-/bronbewijs | `[GEBLOKKEERD]` |
| `BC-R-011` | Showroomrelatie kan onjuist worden gecommuniceerd | Vertrouwens-, operationeel en mogelijk juridisch risico | Alleen goedgekeurde formulering via `BC-SHOW-001` | `[GEBLOKKEERD]` |
| `BC-R-012` | Offerteuploads en servicefuncties verwerken mogelijk gevoelige bestanden/persoonsdata | Privacy- en beveiligingsincident | `BC-SEC-001` als harde afhankelijkheid, veilige uploadtests | `[GEBLOKKEERD]` |
| `BC-R-013` | Grote lanceringsscope kan taken te breed maken en kwaliteitsgates onder druk zetten | Onvolledige of uitgestelde lancering | Epics vóór `READY` splitsen; complete-launchdefinitie handhaven | Actief |
| `BC-R-014` | Onbedoelde livepush/publicatie of onduidelijke rollback | Direct productie- en omzetimpact | Expliciete menselijke go/no-go, gescheiden preview en `BC-REL-001` | `[GEBLOKKEERD]` |
| `BC-R-015` | Alle 7.827 producten hebben `product.vendor`, terwijl geen metafielddefinitie `vendor` is gevonden; themegebruik van `product.metafields.vendor` lijkt daardoor onjuist | Verkeerd/ontbrekend merk in specificaties | Bronkeuze en mapping vastleggen in `BC-DATA-001` vóór wijziging | `[GEBLOKKEERD]` |
| `BC-R-016` | Reviews en vergelijken zijn nog open lanceringsbeslissingen | Late scopewijziging raakt data, UX en apps | Besluiten vóór relevante epics `READY` worden | `[OPEN BESLISSING]` |
| `BC-R-017` | 17 SKU's ontbreken, 72 niet-lege SKU-waarden vormen duplicaatgroepen en 649 producttypewaarden bevatten onder meer 69 keer `undefined` | Import-, zoek-, filter- en orderfouten bij opschaling | Datakwaliteitsregels, eigenaar en herstelplan in `BC-DATA-001`/`BC-PROD-001` | `[GEBLOKKEERD]` |
| `BC-R-018` | 199 van 201 collecties zijn leeg en meerdere collectie-/menulabels wijzen semantisch naar opvallende targets | Lege categorieën, verkeerde navigatie en SEO-schade | Bedoeling valideren in `BC-DISC-001` en doelmodel in `BC-IA-001` | `[GEBLOKKEERD]` |
| `BC-R-019` | Theme `192796786954` bestaat unpublished, maar eigenaar, doel en ontstaansreden zijn onbekend | Onbedoelde wijziging, verwijdering of verwarring tussen testomgevingen | Alleen read-only registreren; expliciet eigenaarschap vaststellen vóór enige themetaak | `[NOG ONDERZOEKEN]` |
| `BC-R-020` | Slechts 259 van 7.827 inventory items zijn getrackt; één delivery profile bevat brede nationale, EU- en internationale zones | Voorraad- en verzendbelofte kan operationeel onjuist zijn | Bronhouders, tarieven en leverregels vastleggen in `BC-LOG-001`/`BC-LOG-002` | `[GEBLOKKEERD]` |
| `BC-R-021` | De statische graaf vindt geen inkomende referentie voor meerdere kandidaten, maar dynamische Liquid-, section-rendering-, Theme Editor- en apppaden kunnen buiten letterlijke referenties vallen | Onterechte verwijdering kan verborgen functionaliteit breken | Geen verwijdering zonder runtimebewijs, eigenaar, aparte taak en herstelplan | `[GEBLOKKEERD]` |
| `BC-R-022` | Concurrentiepagina's, aantallen, prijzen, levertijden, reviews en commerciele claims veranderen; de analyse is een momentopname van 2026-08-05 | Verouderde observaties kunnen later als actuele waarheid worden gebruikt | Bron, datum en bewijsstatus uit `docs/COMPETITOR_SEO_ANALYSIS.md` behouden en kernbesluiten later opnieuw valideren | `[NOG ONDERZOEKEN]` |
| `BC-R-023` | De steekproef toont facetgroei, zeer lange lijsten/titels en zichtbare placeholder-, review-, garantie-, showroom- en foutpagina-inconsistenties | Kopieren kan duplicate content, onduidelijke UX en onbetrouwbare claims naar BadkamerCity overbrengen | Eigen datamodel, routeklassen, bronhouders en acceptatiecriteria besluiten voor `BC-IA-001`, `BC-CAT-001`, `BC-PDP-001` en `BC-SEO-001` | `[GEBLOKKEERD]` |
| `BC-R-024` | De goedgekeurde volledige lokale inventaris vond nul oorspronkelijke leveranciersbestanden, nul importbestanden en nul import-/generatiescripts; externe bronnen en bronhouders blijven onbekend | Een afgeleid themebestand kan ten onrechte als bron worden gemodelleerd en fouten over circa 20.000 producten schalen | Externe bronnen later per leverancier afzonderlijk aanleveren en beoordelen vóór definitieve mapping in `BC-DATA-001`; geen extra lokaal zoekwerk | `[GEBLOKKEERD]` |
| `BC-R-025` | De actieve productsectie toont vaste levertijdtekst `8 - 9 weken`, terwijl geen leverancier-, product- of operationele levertijdbron is bewezen | Hoogste actieve klant-/bedrijfsrisico: onjuiste klantbelofte en operationele/servicefouten | Eerst expliciet kiezen tussen verbergen of exact goedgekeurde fallback en bron/eigenaar/actualiteit vastleggen; geen vervangende tekst verzinnen | `[GEBLOKKEERD]` door bedrijfsregel |
| `BC-R-026` | De V2-asset heeft 3.383 unieke handles tegenover 3.658 Admin-triggerproducten; oorspronkelijke bron, generator, mapping en volledige setvergelijking ontbreken | Stille switchergaten of verkeerde productnavigatie | Externe generator/input aanleveren en in afzonderlijke read-only taak volledig vergelijken vóór `BC-SWITCH-001` | `[GEBLOKKEERD]` |
| `BC-R-027` | Voor 277 gedocumenteerde The Mosaic Factory-producten ontbreekt lokaal iedere tegel-, eenheids-, verpakking- en palletbron | Verkeerde berekening, bestelhoeveelheid, prijs of logistiek | Oorspronkelijke tegelbron en bedrijfsregels verplicht vóór `BC-TILE-001` | `[GEBLOKKEERD]` |
| `BC-R-028` | Het goedgekeurde v0.1-werkkader met 190 conceptkeys, 34 voorgestelde publication blockers en 42 type blockers kan ten onrechte als definitieve Shopify-mapping, beschikbare leveranciersdata of goedgekeurde bedrijfsregel worden gelezen | Voortijdige veldcreatie, te strenge gates, onjuiste mapping of onbewezen klantbeloften | Bewijs-/contractlabels, abstracte opslagcategorieën en latere veldgewijze review; `BC-DATA-003 = DONE` keurt de individuele voorstellen niet definitief goed | Actief |
| `BC-R-029` | Een van de 21 classificaties of 12 kandidaatdeeltaken uit het goedgekeurde `BC-TECH-002`-plan kan ten onrechte als bevestigd defect, verwijdertoestemming of implementatieopdracht worden gelezen | Ongecontroleerde theme-wijziging, regressie of verlies van mogelijk dynamisch gebruikte bestanden | `docs/TECHNICAL_STABILIZATION_PLAN.md` scheidt bereikbaarheid, zekerheid, impact en blokkade; iedere uitvoering vereist een aparte officiele taak en expliciete menselijke toestemming | Actief; onderzoeksplan `DONE` |
| `BC-R-030` | Theme Check is niet gepind of geconfigureerd; de als versieprobe bedoelde opdracht `shopify theme check -v` activeerde eerder een globale CLI-self-update buiten de repository van 4.6.0 naar 4.6.1 | Niet-reproduceerbare kwaliteitsgate en onverwachte lokale toolingwijziging | Eerst afzonderlijk versie-, configuratie- en updatebeleid goedkeuren; code- en toolingfouten gescheiden rapporteren | `[OPEN BESLISSING]`; geen repositorypackage gewijzigd |
| `BC-R-031` | Een onvolledig uitvoeringslog kan fouten of herstelacties verliezen; een te ruim log kan credentials, klant-/orderdata of persoonsgegevens vastleggen | Oncontroleerbaar bewijs of ernstig privacy-/securityrisico | Menselijk goedgekeurde one-bundle-flow met raw-quartetcompleteness, unieke step-ID's, gescheiden streams, hashes, foutbehoud, verboden reviewbestandklassen, Sensitive-redactie, secret-/privacyscan en genegeerde runmap; eerste onafhankelijke praktijktest en terughoudende commandokeuze blijven vereist | Beheerst na menselijke review, maar niet absoluut uitgesloten; retentie en menselijk upload-/privacytoezicht blijven `[OPEN BESLISSING]` |

## 61. Afhankelijkhedenregister

| ID | Afhankelijkheid | Blokkeert | Benodigde uitkomst | Eigenaar/status |
| --- | --- | --- | --- | --- |
| `BC-DEP-001` | Scheiding tussen onderzoeksgoedkeuring en implementatietoestemming | Alle implementatietaken | Versie 0.1 is als onderzoeksbasis goedgekeurd; iedere implementatietaak vereist later afzonderlijke expliciete toestemming na benodigde onderzoeken en besluiten | Discovery actief; implementatie `[GEBLOKKEERD]` |
| `BC-DEP-002` | Shopify Admin-inventaris | Data, apps, actieve templates en vrijwel alle functies | Menselijk goedgekeurd read-only bewijs met expliciete beperkingen | `BC-ADM-001`; `DONE` op 2026-08-04, volledige appbron blijft niet toegankelijk |
| `BC-DEP-003` | Actief theme-/appgebruik | Stabilisatie en verwijderbesluiten | Menselijk goedgekeurde gebruiksmatrix met blijvende kandidaat- en bewijsgrenzen | `BC-DISC-001`; `DONE` op 2026-08-05; geeft geen verwijder- of implementatietoestemming |
| `BC-DEP-004` | Concurrentie-/SEO-onderzoek na Admin- en actief-gebruiksonderzoek | IA, SEO, categorieën en UX-besluiten | Menselijk goedgekeurde vergelijkingsmatrix met blijvende bewijsgrenzen; patroonbesluiten blijven afzonderlijk | `BC-DISC-002`; `DONE` op 2026-08-05, geen ontwerp-/SEO-besluit |
| `BC-DEP-005` | Productdatamodel en definitieve Shopify-opslag | PDP, filters, switchers, imports en feeds | De bestuurde conceptuele werkbasis is aanwezig; voor definitieve mappings blijven oorspronkelijke bronnen, bronhouders en veldgewijze besluiten nodig | `BC-DATA-001`; `[GEBLOKKEERD]`. `BC-DATA-002` en `BC-DATA-003` zijn `DONE`; bronnen ontbreken |
| `BC-DEP-006` | Categorie-/navigatiemodel | Globale navigatie, collectieplatform en SEO | Goedgekeurde IA en URL-principes | `BC-IA-001`; `[GEBLOKKEERD]` |
| `BC-DEP-007` | Leveranciers- en logistieke regels | Voorraad, levertijd, checkout, samples en PDP | Beslis-/bronnenmatrix | `BC-LOG-*`; `[GEBLOKKEERD]` |
| `BC-DEP-008` | Privacy-/securitybesluiten | Uploads, accounts, chat, afspraken en analytics | Goedgekeurde datastromen/controles | `BC-SEC-001`; `[GEBLOKKEERD]` |
| `BC-DEP-009` | Browser-, performance- en toegankelijkheidscriteria | DoR/DoD en integrale QA | Goedgekeurde meetbare matrix | `BC-QA-001`; `[OPEN BESLISSING]` |
| `BC-DEP-010` | Menselijke visuele/functionele goedkeuring | `DONE` voor zichtbaar/functioneel werk | Expliciet vastgelegd akkoord | Eigenaar; doorlopend |
| `BC-DEP-011` | Release-/rollbackbesluit | Productiepublicatie | Getest plan, rollen en expliciet go/no-go | `BC-REL-001`; `[GEBLOKKEERD]` |
| `BC-DEP-012` | Leveranciersbestanden/API-specificaties | Definitieve `BC-DATA-001`-mapping, productonboarding, logistieke regels en latere feeds | Oorspronkelijke bronnen, velddekking en eigenaarschap per leverancier; mappingbesluiten volgen later | Lokale inventaris `BC-DATA-002` `DONE`; externe bronnen en bronhouders `[NOG ONDERZOEKEN]`; blokkeerden het brononafhankelijke v0.1-contract niet |
| `BC-DEP-013` | Brononafhankelijk productinformatiecontract | Definitieve datamodelreview en samenhang tussen PDP, kaarten, zoeken, filters, relaties, logistiek, SEO en typefuncties | Menselijk goedgekeurde conceptuele werkbasis met betekenis, voorgesteld vereisteniveau, validatie, leegstaat en eigenaar zonder definitieve opslagmapping | `BC-DATA-003`; `DONE` op 2026-08-10; individuele veldbesluiten blijven open |
| `BC-DEP-014` | Read-only technische decompositie en nulmeting | Veilige opsplitsing van de brede `BC-TECH-001`-epic | 21 bevindingen, twaalf kandidaatdeeltaken, regressiebasis, uitvoeringsvolgorde en expliciete blokkades zonder codewijziging | `BC-TECH-002`; `DONE` op 2026-08-11; kandidaten zijn niet actief en implementatie blijft geblokkeerd |
| `BC-DEP-015` | Permanent lokaal Codex-uitvoeringslogboek | Controleerbaarheid van alle toekomstige Codex-taken | Menselijk goedgekeurde genegeerde runmap, commandologging, note/diffregistratie, raw completeness, hashgecontroleerde reviewbestanden en zelfstandige one-bundle-handoff | `DONE` via `BC-GOV-006` op 2026-08-11; eerste onafhankelijke toekomstige taak moet het protocol in echte projectuitvoering gebruiken |

## 62. Bewijs- en referentieregister

| Bewijs-ID | Bron | Wat het bewijst | Datum/commit | Beperking |
| --- | --- | --- | --- | --- |
| `BC-EV-001` | [`docs/REPOSITORY_AUDIT.md`](REPOSITORY_AUDIT.md) | Technische opbouw, maatwerk, switchers, oude/backups, bevindingen, risico's en documentatiegaten | 2026-08-03; `e1d655e` | Statische momentopname; geen volledige runtime-/Adminvalidatie |
| `BC-EV-002` | [`docs/SHOPIFY_ENVIRONMENT.md`](SHOPIFY_ENVIRONMENT.md) | Gekoppelde store en toenmalige themelijst | 2026-08-03; `ff8ceaf` | Vóór aanmaak van het nieuwe unpublished development-theme |
| `BC-EV-003` | [`docs/LIVE_THEME_COMPARISON.md`](LIVE_THEME_COMPARISON.md) | Gelijkheid van 396 lokale/live bestanden in zeven theme-mappen | 2026-08-03; `badd5cf` | Geen externe Shopify-data; tijdgebonden snapshot |
| `BC-EV-004` | [`docs/DEVELOPMENT_THEME.md`](DEVELOPMENT_THEME.md) | Nieuw unpublished `BadkamerCity Development` (`192770375946`), links en live theme onveranderd | 2026-08-03; `3e0b4ec` | Bewijst geen functionele acceptatie van preview |
| `BC-EV-005` | Bijgevoegde projectdefinitie bij opdracht voor masterplan | Visie, scope, productmodel, processen, governance en verplichte masterplanstructuur | 2026-08-03; duurzaam bronbestand in repository `[NOG ONDERZOEKEN]` | Niet als afzonderlijk repositorydocument aanwezig |
| `BC-EV-006` | Dit masterplan | Versies 0.1-0.14 legden fundament, discovery, inventarisaties, productcontract, technisch stabilisatieplan en loggingvoorbereiding vast; versie 0.15 legde de lokaal zelfgeteste uitvoering van `BC-GOV-006` op `REVIEW` vast; versie 0.16 legt menselijke goedkeuring, drie reviewfixes en `DONE` vast | Fundament: 2026-08-03, commit `302a42a`; governance: 2026-08-04, commit `d22e3e32d04fc472996064cc14cff922396c2d05`; v0.10: commit `8f4c5ddbdaf229d996042446825614b028dc1d37`; v0.12: commit `2b11f1efe1af9e06b9741cdc12393771a970d1a5`; v0.14: commit `2af434b50738ccfd6f0c3b212bbe31b1205c6597`; v0.16: deze commit `chore: finalize Codex execution logging` | Geen bronacceptatie-, definitieve mapping-, data-, ontwerp-, SEO-, theme-, Admin-, scope-, publicatie- of implementatietoestemming |
| `BC-EV-007` | [`AGENTS.md`](../AGENTS.md) | Permanente Codex-guardrails en verplichte raadpleging van dit masterplan | 2026-08-04; commit `d22e3e32d04fc472996064cc14cff922396c2d05` | `docs/MASTERPLAN.md` blijft de centrale bron van waarheid |
| `BC-EV-008` | [`docs/SHOPIFY_ADMIN_INVENTORY.md`](SHOPIFY_ADMIN_INVENTORY.md) | Shopify CLI `4.6.0`, dertien read-scopes en gepagineerd bewijs voor producten, collecties, metafields, metaobjects, navigatie, pagina's, themes, actieve JSON-configuratie, markets, talen, accounts, locaties, inventory en shipping | 2026-08-04; commit `docs: approve Shopify Admin inventory` | Volledige app-/pixel-/scriptbron niet toegankelijk; specificatiewaarden buiten de steekproef en inhoudelijk eigenaarschap blijven open; taak menselijk goedgekeurd en `DONE` |
| `BC-EV-009` | Expliciete menselijke goedkeuring van de projecteigenaar | `BC-ADM-001` mag naar `DONE`; `BC-DISC-001` mag als actieve eerstvolgende read-only taak naar `READY`; alle beperkingen en open vragen blijven bestaan | 2026-08-04; vastgelegd in masterplan v0.4 en commit `docs: approve Shopify Admin inventory` | Geeft geen toestemming voor Shopify-data, theme-code, push/pull, publicatie, themebeheer, aanvullende scopes of implementatie |
| `BC-EV-010` | [`docs/ACTIVE_THEME_USAGE.md`](ACTIVE_THEME_USAGE.md) | Live/local gelijkheid van 18 JSON-configuratiebestanden; sluitende classificatie van 396 bestanden; actieve sections/blocks, conditionele routes, auditverdachten, beide switchers, backup/debug, appinjectie en contentkoppelingen | Onderzoek 2026-08-04; menselijk goedgekeurd 2026-08-05; commit `docs: approve active theme usage inventory` | Statisch/read-only onderzoek; runtimegedrag en volledige app-/pixelbron blijven beperkt; classificaties geven geen verwijdertoestemming |
| `BC-EV-011` | Expliciete menselijke startopdracht van de projecteigenaar | `BC-DISC-001` mocht uitsluitend read-only starten; alleen rapport/masterplan mochten wijzigen; `BC-DISC-002` mocht niet worden geactiveerd | 2026-08-04; vastgelegd in masterplan v0.5 | Geen toestemming voor Shopify-, theme-, app-, scope-, implementatie-, commit- of pushhandelingen |
| `BC-EV-012` | Expliciete menselijke goedkeuring van de projecteigenaar | `BC-DISC-001` mag naar `DONE`; `BC-DISC-002` mag als actieve volgende read-only taak naar `READY`; alle runtime-, app-, pixel-, switcherdata-, kandidaat- en backuplimieten blijven bestaan | 2026-08-05; vastgelegd in masterplan v0.6 en commit `docs: approve active theme usage inventory` | Buiten deze twee projectadministratiedocumenten geen toestemming voor Shopify-data, theme-code, bestanden, themebeheer, aanvullende scopes, apps of implementatie; `BC-DISC-002` is niet inhoudelijk gestart |
| `BC-EV-013` | Expliciete menselijke startopdracht van de projecteigenaar | Alleen openbare read-only analyse van drie benoemde concurrenten en documentatie van `BC-DISC-002` zijn toegestaan | 2026-08-05; vastgelegd in masterplan v0.7 | Geen accounts, formulieren, persoonsgegevens, onbeperkte crawl, blokkade-omzeiling, Shopify-, theme-, app-, scope-, implementatie-, commit- of pushhandelingen |
| `BC-EV-014` | [`docs/COMPETITOR_SEO_ANALYSIS.md`](COMPETITOR_SEO_ANALYSIS.md) | Exacte openbare URL-steekproef, drie concurrentprofielen, vergelijkingsmatrix, IA, zoeken/filters, kaarten, PDP's, services, content, technische SEO, sterke patronen, anti-patronen, kansen en bewijsgrenzen | Onderzoek en menselijke goedkeuring 2026-08-05; deze documentatiecommit | Tijdgebonden steekproef; zoekroutes, echte mobiele/visuele en toetsenbordinteractie, indexdekking en client-side functies blijven niet of niet betrouwbaar toegankelijk; goedkeuring is geen patroon-/ontwerp-/SEO-/implementatiebesluit |
| `BC-EV-015` | Expliciete menselijke goedkeuring en projectadministratieopdracht van de projecteigenaar | `BC-DISC-002` en fase 1 mogen naar `DONE`; `BC-DATA-002` wordt actief `READY` maar niet inhoudelijk gestart; `BC-DATA-001` blijft `BLOCKED` | 2026-08-05; vastgelegd in masterplan v0.8 en commit `docs: approve competitor research and prepare data inventory` | Geen Shopify-, theme-, app-, scope-, product-, collectie-, metafield-, ontwerp-, SEO-, concurrentkopieer- of implementatietoestemming |
| `BC-EV-016` | Expliciete menselijke startopdracht van de projecteigenaar | `BC-DATA-002` mag uitsluitend de huidige repository, documentatie, lokale bestanden en Git-metadata read-only onderzoeken; alleen rapport en masterplan mogen wijzigen | 2026-08-10; vastgelegd in masterplan v0.9 | Geen Shopify, bestanden buiten `CITY_MASTER`, imports, scripts uitvoeren, bron-/theme-code wijzigen, mappings besluiten, commit of push |
| `BC-EV-017` | [`docs/SUPPLIER_DATA_INVENTORY.md`](SUPPLIER_DATA_INVENTORY.md) | Volledige scan van 405 lokale/tracked paden bij taakstart; nul oorspronkelijke leveranciersbronnen, nul importbestanden en nul import-/generatiescripts; zes afgeleide switcherdata-assets, vijf relevante storefront-JavaScriptbestanden, feitelijke velden/identifiers, datakwaliteit en ontbrekende input | Onderzoek en menselijke goedkeuring 2026-08-10; deze documentatiecommit; `BC-DATA-002` `DONE` | Alleen lokale repository/Git-bewijsroute; externe bestanden, generatoren en bronhouders blijven onbekend; geen mapping- of implementatiebesluit |
| `BC-EV-018` | Expliciete menselijke goedkeuring en tweefasenopdracht van de projecteigenaar | `BC-DATA-002` mag naar `DONE`; nul oorspronkelijke lokale bronnen is geaccepteerd; externe bronnen volgen later per leverancier; `BC-DATA-003` wordt actief `READY` maar blijft vóór de fase-A-commit **NIET INHOUDELIJK GESTART** | 2026-08-10; vastgelegd in masterplan v0.10 en commit `docs: approve supplier inventory and prepare product contract` | Alleen documentatie; geen Shopify-, bron-, mapping-, theme-, code-, import- of implementatietoestemming |
| `BC-EV-019` | [`docs/PRODUCT_DATA_CONTRACT.md`](PRODUCT_DATA_CONTRACT.md) | Bestuurde brononafhankelijke conceptuele werkbasis v0.1 met 190 unieke contractkeys in 15 domeinen, vijf producttypeklassen, leegstaatbeleid, validaties, tien kwaliteitsgates, abstracte opslagcategorieën en leeg mappingtemplate | Onderzoek en beperkte menselijke goedkeuring 2026-08-10; `BC-DATA-003` `DONE`; deze documentatiecommit | Geen definitieve Shopify-/leveranciermapping en geen bewijs van beschikbare data; individuele keys/niveaus/gates, leveranciersbronnen en veldbesluiten blijven open |
| `BC-EV-020` | Expliciete beperkte menselijke goedkeuring en tweefasenopdracht van de projecteigenaar | `BC-DATA-003` mag naar `DONE`; contract v0.1 wordt conceptuele werkbasis; `BC-TECH-002` wordt actief `READY` maar blijft vóór de fase-A-commit **NIET INHOUDELIJK GESTART** | 2026-08-10; vastgelegd in masterplan v0.12 en commit `docs: approve product contract and prepare technical stabilization` | Geen definitieve contract-, Shopify-, leverancier-, data-, theme- of implementatiekeuze; fase B blijft read-only planning |
| `BC-EV-021` | [`docs/TECHNICAL_STABILIZATION_PLAN.md`](TECHNICAL_STABILIZATION_PLAN.md) | Gerichte herbevestiging met 21 issues (2 P0, 15 P1, 4 P2), twaalf niet-officiele kandidaatdeeltaken, Theme Check-samenvatting, minimale regressiematrix en veilige uitvoeringsvolgorde | Onderzoek en menselijke goedkeuring 2026-08-11; `BC-TECH-002` `DONE`; deze documentatiecommit | Statisch/lokaal en read-only; geen runtimegoedkeuring, defectoplossing, verwijdertoestemming of actieve implementatietaak |
| `BC-EV-022` | Expliciete hervatopdracht van de projecteigenaar | De gedeeltelijk gestarte `BC-TECH-002` mag vanaf exact commit `2b11f1e...` read-only worden afgerond; fase A en contractgoedkeuring worden niet herhaald; alleen masterplan en stabilisatieplan mogen wijzigen | 2026-08-11; masterplan v0.13; niet gecommit | Geen Shopify-, theme-, code-, package-, bron-, import-, branch-, commit-, push- of implementatietoestemming |
| `BC-EV-023` | Expliciete menselijke goedkeuring en tweefasenopdracht van de projecteigenaar | `BC-TECH-002` mag naar `DONE`; twaalf kandidaten blijven niet-officieel; `BC-GOV-006` wordt actief `READY` maar vóór de fase-A-commit **NIET INHOUDELIJK GESTART** | 2026-08-11; masterplan v0.14; deze documentatiecommit | Fase A uitsluitend documentatie; fase B uitsluitend lokale governance-/loggingtooling. Geen Shopify-, theme-, productdata-, kandidaat- of implementatietoestemming |

Chronologie voorkomt een schijnbare tegenspraak: `BC-EV-002` meldde nog geen development theme; `BC-EV-004` bewijst de latere aanmaak van een afzonderlijk unpublished development theme. `BC-EV-008` bewijst daarnaast het bestaan van unpublished theme `192796786954`, zonder eigenaarschap, doel of wijziging te claimen. `BC-EV-010` bouwt uitsluitend read-only voort op die omgeving en verandert geen theme; `BC-EV-012` keurt alleen dat onderzoeksresultaat goed. `BC-EV-014` gebruikt uitsluitend openbare concurrentbronnen; `BC-EV-015` zette `BC-DATA-002` alleen klaar. De latere starttoestemming `BC-EV-016` begrensde het werk tot lokale read-only analyse; `BC-EV-017` is met `BC-EV-018` menselijk goedgekeurd. `BC-EV-019` is met `BC-EV-020` uitsluitend als conceptuele werkbasis goedgekeurd. `BC-EV-021` is na `BC-EV-022` met `BC-EV-023` als read-only onderzoeksplan goedgekeurd; kandidaat-ID's blijven geen taakrecords. Alleen de lokale loggingtaak is voorbereid; externe bronvragen, contractkeuzes, defectoplossingen en implementatie blijven open.

**`BC-EV-024` - Uitvoeringsopdracht (2026-08-11):** de projecteigenaar gaf expliciet toestemming om na fase-A-commit `2af434b50738ccfd6f0c3b212bbe31b1205c6597` uitsluitend `BC-GOV-006` lokaal uit te voeren en op `REVIEW` te zetten. Geen technische kandidaat, Shopify-, theme-, productdata-, branch-, tweede commit- of pushactie was toegestaan.

**`BC-EV-025` - Lokaal protocolbewijs (2026-08-11):** `docs/CODEX_EXECUTION_LOG_PROTOCOL.md`, `.gitignore`, de permanente `AGENTS.md`-guardrails, vier scripts onder `scripts/` en run `docs/_codex_runs/BC-GOV-006_20260811-131019/` bewijzen de lokale implementatie en zelftests. `FULL_EXECUTION_LOG.md`, `FINAL_REPORT.md`, `UPLOAD_MANIFEST.md` en de ZIP-bundle met SHA-256 zijn uploadbaar bewijs. Beperking: lokaal zelftestbewijs, nog geen menselijke goedkeuring en geen fase-B-commit of push.

**`BC-EV-026` - Voorwaardelijke menselijke review (2026-08-11):** de projecteigenaar keurde de bestaande `BC-GOV-006`-opzet inhoudelijk goed onder drie expliciete voorwaarden: one-bundle `review_files/`, child `ErrorActionPreference = Stop` en verplichte raw command-quartetcompleteness. Alleen deze hardening en de uiteindelijke protocolcommit/push zijn geautoriseerd; technische kandidaten, Shopify, themes en data blijven uitgesloten.

**`BC-EV-027` - Reviewfix-run (2026-08-11):** `docs/_codex_runs/BC-GOV-006-REVIEWFIX_20260811-173707/` bevat de volledige opdracht, context, command-/note-evidence, positieve one-bundle-test, intentionele cmdlet-errorzelftest, negatieve completeness-test, verboden-bestandsnaamtest, reviewhashcontrole, parser-/Git-/securitycontroles en het finale eindrapport.

**`BC-EV-028` - One-bundle-integriteit (2026-08-11):** de nieuwe finalizer valideert alle raw commandquartetten en step-ID's, weigert onveilige reviewpaden, bewijst bron-/kopie-/ZIP-hashes in `REVIEW_FILES_MANIFEST.md`, opent de tijdelijke `.building.zip` read-only en promoveert pas daarna. De finale `BC-GOV-006-REVIEWFIX_20260811-173707_BUNDLE.zip` bevat logs, raw evidence en acht actuele repositorybestanden onder `review_files/`.

**`BC-EV-029` - Uiteindelijke protocolcommit (2026-08-11):** commit `chore: finalize Codex execution logging` bevat exact `.gitignore`, `AGENTS.md`, `docs/CODEX_EXECUTION_LOG_PROTOCOL.md`, `docs/MASTERPLAN.md` en de vier `scripts/codex-run-*.ps1`-helpers en staat na deze opdracht op `origin/main`; de exacte commit-hash staat in `FINAL_REPORT.md` en de finale runbundle.

De loggingbewijzen `BC-EV-024` tot en met `BC-EV-029` activeren geen technische kandidaat en geven geen Shopify-, theme-, productdata-, defectoplossings- of implementatietoestemming.

## 63. Controlechecklists

Een niet-relevante controle krijgt `N.v.t.` met reden en bewijs; zij wordt niet stil overgeslagen.

### Onderzoek

- [x] Git-status en toegestane scope vooraf vastgelegd.
- [x] Alleen read-only bronnen gebruikt waar voorgeschreven.
- [x] Datum, bron, toegang en beperkingen genoteerd.
- [x] Feiten, gevolgtrekkingen en aanbevelingen gescheiden.
- [x] Onbekenden/open beslissingen/blokkades gemarkeerd.
- [x] Geen Shopify-, code- of datamutatie uitgevoerd.

### Leveranciersbronneninventaris (`BC-DATA-002`)

- [x] Afzonderlijke expliciete read-only startopdracht ontvangen; taak van `READY` naar `IN_PROGRESS` en na technische afronding naar `REVIEW` gezet.
- [x] Alleen repository, projectdocumentatie en reeds aanwezige lokale bronnen gelezen; niets verplaatst, gecorrigeerd of geimporteerd.
- [x] Iedere aantoonbare data-/scriptbron heeft naam, locatie, formaat, leverancierstatus, datum en eigenaarstatus; nul oorspronkelijke bronnen is expliciet vastgelegd.
- [x] Schema's, veilige recordtotalen, identifiers, eenheden, prijs, media, voorraad/levertijd, specificaties en switcherrelaties zijn vastgelegd of expliciet als ontbrekend gemarkeerd.
- [x] Duplicaat-/nullsteekproeven, identifiervergelijking en bron-/datumcontrole zijn zonder mutaties uitgevoerd.
- [x] Ontbrekende externe bestanden en onbekende bronhouders zijn expliciet gemarkeerd en niet verzonnen.
- [x] Relevantie en blokkades voor `BC-DATA-001`, `BC-LOG-001`, `BC-PROD-001`, `BC-SWITCH-001` en `BC-TILE-001` zijn vastgelegd in `docs/SUPPLIER_DATA_INVENTORY.md`.
- [x] Alleen vooraf toegestane documentatiebestanden zijn gewijzigd; Shopify-data en theme-code zijn onaangeraakt.
- [x] Projecteigenaar heeft de binnen-scope complete nulmeting en nul oorspronkelijke lokale bronnen op 2026-08-10 goedgekeurd; `BC-DATA-002` is `DONE`.

### Productinformatiecontract (`BC-DATA-003`)

- [x] Volledig taakrecord, brononafhankelijke scope, buiten-scope, acceptatie en risico zijn vastgelegd.
- [x] Taak was vóór de fase-A-commit `READY` en **NIET INHOUDELIJK GESTART**; de fase-A-commit is gepusht en de werkboom was daarna schoon.
- [x] Bestaande bewijsbasis is na de fase-A-commit opnieuw volledig gelezen en de Git-basis is gecontroleerd.
- [x] Alle 190 contractkeys zijn uniek, lowercase, underscoregescheiden en geen enkele key begint met `custom.`.
- [x] Iedere centrale veldmatrixrij bevat betekenis, type, vereisteniveau, broncategorie, gebruik, validatie, leegstaat en eigenaar.
- [x] Feit, voorstel, leverancierafhankelijkheid en open beslissing zijn zichtbaar gescheiden.
- [x] Producttypematrix, leegstaatbeleid, validaties, tien kwaliteitsgates, abstracte opslagcategorieën en leeg mappingtemplate zijn compleet.
- [x] Alleen `docs/PRODUCT_DATA_CONTRACT.md` en dit masterplan zijn na de fase-A-commit gewijzigd; geen bron-, Shopify- of theme-mutatie.
- [x] De projecteigenaar heeft het resultaat op 2026-08-10 als bestuurde conceptuele werkbasis goedgekeurd; `BC-DATA-003` staat `DONE` zonder individuele veld- of mappingbesluiten te impliceren.

### Technische stabilisatieplanning (`BC-TECH-002`)

- [x] Volledig taakrecord, read-only scope, buiten-scope, acceptatie, risico en herstelwijze zijn vastgelegd.
- [x] `BC-TECH-001` blijft de geblokkeerde brede epic; `BC-TECH-002` is alleen een decompositie- en nulmetingstaak.
- [x] Taak is na de schone fase-A-commit van `READY` naar `IN_PROGRESS` gezet.
- [x] Fase 3 stond na read-only technische afronding op `REVIEW`; de projecteigenaar heeft `BC-TECH-002` op 2026-08-11 goedgekeurd en de taak staat `DONE`.
- [x] Bestaande bewijsdocumenten en technische risicoclusters zijn gericht read-only herbevestigd; 21 bevindingen hebben bereikbaarheid, zekerheid, impact en bewijs.
- [x] De ene volledige lokale Theme Check-run is samengevat en gescheiden in codebevindingen, externe schemafout en tooling-/versiebeperking; geen tweede volledige run uitgevoerd.
- [x] Twaalf niet-officiele kandidaatdeeltaken, volgorde, regressiematrix, preview en rollback zijn ter menselijke review vastgelegd.
- [x] Iedere kandidaat heeft doel, exacte bestanden, scope/buiten-scope, afhankelijkheden, acceptatie, tests, preview, menselijke beslissing en rollback.
- [x] Alleen `docs/MASTERPLAN.md` en `docs/TECHNICAL_STABILIZATION_PLAN.md` zijn gewijzigd; classificatie is geen verwijdertoestemming en geen defect is opgelost.
- [x] Geen kandidaat is als officiele taak toegevoegd of geactiveerd; fase 3 staat voor technische uitvoering weer `BLOCKED`.

### Codex-uitvoeringslogboek (`BC-GOV-006`)

- [x] Volledig taakrecord, scope, buiten-scope, technische controles, privacyrisico en rollback zijn vastgelegd.
- [x] De fase-A-commit `2af434b50738ccfd6f0c3b212bbe31b1205c6597` staat op `origin/main`; de werkboom was schoon voor fase B.
- [x] Basisrun `BC-GOV-006_20260811-131019` en reviewfix-run `BC-GOV-006-REVIEWFIX_20260811-173707` bevatten volledige opdrachten, context, logs en raw evidence.
- [x] Protocol, permanente `AGENTS.md`-guardrails, `.gitignore` en vier PowerShell 5.1-compatibele scripts zijn gebouwd, gehard en zonder parserfouten gecontroleerd.
- [x] Child-cmdletfout, succes, stdout/stderr, UTF-8, Sensitive-redactie, eerder 500-regelsbewijs, notes, diffs, ignore en SHA-256 zijn aantoonbaar getest.
- [x] De finalizer accepteert een complete one-bundle-run en weigert aantoonbaar een incompleet quartet en een onschadelijke verboden bestandsnaam.
- [x] Raw command-evidence, unieke step-ID's, `REVIEW_FILES_MANIFEST.md`, reviewkopiehashes, tijdelijke ZIP, finale entries en ZIP-hashes zijn mechanisch gecontroleerd.
- [x] Iedere tracked bewerking heeft FILE_CHANGE plus gelogde diff/diffstat; kandidaat-, technical-stabilization-, theme- en databestanden zijn niet gewijzigd.
- [x] De acht toegestane protocolbestanden worden in een afzonderlijk gecontroleerde commit naar `main` gepusht; de finale bundle bevat dezelfde acht bestanden onder `review_files/`.
- [x] `BC-GOV-006` en fase 0 zijn menselijk goedgekeurd en `DONE`; er is geen volgende taak of technische kandidaat actief.

### Codewijziging

- [ ] Taak is `READY`, opgesplitst en expliciet toegestaan.
- [ ] Doel, scope, bestanden, acceptatie en rollback zijn vastgesteld.
- [ ] Actuele Git-status en diff zijn gecontroleerd; gebruikerswijzigingen blijven intact.
- [ ] Geen direct livewerk; previewomgeving en testdata zijn bekend.
- [ ] Theme Check en taakgerichte tests zijn uitgevoerd.
- [ ] Masterplan, bewijs, risico's en changelog zijn bijgewerkt.
- [ ] Zichtbaar/functioneel resultaat blijft `REVIEW` tot menselijke goedkeuring.

### Productpagina

- [ ] Alle toepasselijke elementen uit hoofdstuk 17 hebben bron en leegstaat.
- [ ] Media, buybox, prijs, SKU, voorraad en levertijd zijn correct.
- [ ] Specificaties, content, documenten, relaties en service-informatie zijn correct.
- [ ] Switcher/configurator toont juiste states en productnavigatie.
- [ ] Cartactie en fouten zijn getest.
- [ ] Structured data, metadata, headings, canonical en indexatie zijn gecontroleerd.
- [ ] Mobiel, desktop en toetsenbord zijn getest en menselijk goedgekeurd.

### Tegelcalculator

- [ ] Oppervlakte en snijverlies zijn gevalideerd.
- [ ] Doosinhoud en afronding naar hele dozen zijn correct.
- [ ] Prijs per m², prijs per doos en totalen sluiten aan.
- [ ] Totaal dozen en totaal te bestellen oppervlakte zijn zichtbaar.
- [ ] Nul, negatief, decimalen, ontbrekende data en grensgevallen zijn getest.
- [ ] Cartgedrag, mobiel en toetsenbord zijn gecontroleerd.

### Configurator

- [ ] Alle eigenschappen en waarden komen uit de goedgekeurde bron.
- [ ] Geldige combinaties matchen exact één bestaand product/URL/SKU.
- [ ] Ongeldige en gedeeltelijke keuzes hebben begrijpelijke states.
- [ ] Huidig product, directe URL en browser history werken.
- [ ] Datasetvalidatie, performance, mobiel en toetsenbord zijn getest.
- [ ] Representatieve groepen zijn menselijk goedgekeurd.

### Collectiepagina

- [ ] Categorie-intro, subcategorieën en echte links/content zijn correct.
- [ ] Productgrid, kaarten, sortering, filters en nulresultaten werken.
- [ ] Productdekking en filterwaarden sluiten aan op datamodel.
- [ ] Facetten, canonical, indexatie, interne links en paginering zijn gecontroleerd.
- [ ] Mobiel, desktop, toetsenbord en performance zijn getest.

### Mobiel

- [ ] Goedgekeurde viewports/apparaten zijn gebruikt.
- [ ] Geen overlap, afsnijding of onbedoelde layoutshift.
- [ ] Navigatie, zoeken, filters, PDP, configurators, cart en formulieren werken.
- [ ] Touchdoelen, focus, toetsenbord waar relevant en oriëntatie zijn gecontroleerd.
- [ ] Laadtijd en interactierespons zijn vastgelegd.

### Desktop

- [ ] Goedgekeurde browsers/viewports zijn gebruikt.
- [ ] Header/mega-menu, zoeken, filters, PDP, cart en formulieren werken.
- [ ] Toetsenbordvolgorde, focus en modals zijn gecontroleerd.
- [ ] Brede en minimale desktopbreedte tonen geen overlap/afsnijding.
- [ ] Visueel/functioneel resultaat is menselijk beoordeeld.

### Performance

- [ ] Baseline, omgeving, pagina, data en meetmethode zijn vastgelegd.
- [ ] Goedgekeurd budget is bekend.
- [ ] JS/CSS/assets, switcherpayload, afbeeldingen en netwerkverzoeken zijn onderzocht.
- [ ] Voor/na-metingen en regressies zijn gedocumenteerd.
- [ ] Product-, collectie-, zoek-, home- en cartkernpagina's zijn gemeten.

### Toegankelijkheid

- [ ] Semantiek, labels, headings en alternatieve tekst zijn gecontroleerd.
- [ ] Volledige toetsenbordreis en zichtbare focus werken.
- [ ] Dialogen, drawers, filters, switchers, calculator en formulieren hebben juiste states.
- [ ] Contrast, zoom/reflow, foutmeldingen en dynamische updates zijn getest.
- [ ] Geautomatiseerde en handmatige bevindingen zijn vastgelegd; doelstandaard `[NOG ONDERZOEKEN]`.

### SEO

- [ ] Zoekintentie en paginatype zijn bevestigd.
- [ ] URL, titel, metabeschrijving, headings en content zijn uniek/passend.
- [ ] Canonical, indexatie, robots en redirects zijn gecontroleerd.
- [ ] Structured data is geldig en inhoudelijk correct.
- [ ] Interne links, breadcrumbs, facetten en duplicate routes zijn gecontroleerd.
- [ ] Geen placeholder- of `#`-links blijven in goedgekeurde routes.

### Preview

- [ ] Juiste commit en diff zijn vastgelegd.
- [ ] Alleen het unpublished development-theme is doelomgeving.
- [ ] Shopify/themelijst is vóór risicovolle acties gecontroleerd.
- [ ] Technische tests en kernreizen zijn geslaagd.
- [ ] Previewlink, testdata, screenshots en bekende beperkingen zijn gedeeld.
- [ ] Menselijke feedback en status `REVIEW`/`DONE` zijn vastgelegd.

### Live release

- [ ] Complete-launchdefinitie en Definition of Done zijn gehaald.
- [ ] Geen open P0-blokkade; restrisico's zijn expliciet geaccepteerd.
- [ ] Git-, preview- en releasecandidatepariteit zijn gecontroleerd.
- [ ] Backup, rollbacktheme/-commit, rollen en commando's zijn getest.
- [ ] Eigenaar heeft productiepublicatie expliciet goedgekeurd.
- [ ] Post-release smoke tests, monitoring en bewijs zijn uitgevoerd.
- [ ] Codex heeft publicatie niet zelfstandig verondersteld.

## 64. Huidige eerstvolgende stappen

### Actuele route

- **Waar we nu zijn:** `BC-TECH-002`, `BC-GOV-006` en fase 0 zijn `DONE`; fase 2 en fase 3 blijven voor definitieve data-/IA- en technische uitvoering `BLOCKED`. Masterplan versie 0.16 blijft `ACTIVE FOR DISCOVERY - IMPLEMENTATION BLOCKED`; er is geen actieve taak.
- **Wat is vastgelegd:** `docs/SUPPLIER_DATA_INVENTORY.md` bewijst en de projecteigenaar accepteert voor de lokale repository nul oorspronkelijke leveranciersbronnen, nul importbestanden en nul import-/generatiescripts. Externe bronnen kunnen bestaan en volgen later afzonderlijk per leverancier.
- **Welke input nodig is:** de retentietermijn en eigenaar van lokale runbundles blijven open. Voor technische uitvoering blijven keuze van een afzonderlijke kandidaat, exacte scope, bedrijfs-/IA-/runtimebesluiten en expliciete implementatietoestemming nodig.
- **Welke taken daarna komen:** geen taak is actief. De eerste onafhankelijke toekomstige taak moet het one-bundle-protocol in echte projectuitvoering gebruiken. `PROPOSED-TECH-01` kan alleen na een afzonderlijk menselijk besluit als officiele taak worden voorbereid; kandidaat-ID's blijven nu uitsluitend voorstellen.

Aanbevolen eerstvolgende handeling: bepaal later afzonderlijk welke onafhankelijke taak het goedgekeurde protocol voor het eerst gebruikt. Start nog geen Theme Check-kandidaat. De vaste levertijdtekst blijft afzonderlijk geblokkeerd op een commercieel/operationeel besluit en heeft geen goedgekeurde vervangende tekst.

## 65. Wijzigingslog

| Datum | Versie | Taak-ID | Wijziging | Reden | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-08-03 | 0.1 DRAFT | `BC-GOV-005` | Eerste centrale masterplanfundering met 65 hoofdstukken, 37 taken en governance-/beslis-/vragen-/risico-/afhankelijkheden-/bewijsregisters | Eén levende bron van waarheid maken vóór ontwikkeling | `302a42a` - `docs: add BadkamerCity masterplan foundation` |
| 2026-08-04 | 0.2 | `BC-GOV-005`, `BC-ADM-001` | Onderzoeksgoedkeuring vastgelegd, discovery geactiveerd, implementatie geblokkeerd, onderzoeksvolgorde gecorrigeerd en `AGENTS.md` als Codex-guardrail toegevoegd | Projectbesturing afronden voordat read-only Admin-onderzoek start | `d22e3e32d04fc472996064cc14cff922396c2d05` - `docs: activate discovery workflow and add Codex guidance` |
| 2026-08-04 | 0.2 | `BC-ADM-001` | Read-only toegang onderzocht, theme-context en tijdgebonden configuratiebewijs vastgelegd, alle ontoegankelijke Admin-domeinen en benodigde leesrechten gedocumenteerd en taak op `BLOCKED` gezet | Er is geen bestaande uitvoerbare Admin API-/browser-readcontext; afwezigheid mag niet uit theme-code worden afgeleid | Niet gecommit; opdracht verbiedt commit en push |
| 2026-08-04 | 0.3 | `BC-ADM-001` | De door de eigenaar geautoriseerde Shopify CLI-route en dertien read-scopes gebruikt voor de gepagineerde Admin-inventaris; rapport, dashboard, taakrecord, besluiten, vragen, risico's, afhankelijkheden, bewijs en route bijgewerkt; taak op `REVIEW` gezet | De kernobjecten en instellingen zijn nu read-only bewezen; beperkingen en menselijke beoordeling blijven expliciet | Niet gecommit; opdracht verbiedt commit en push |
| 2026-08-04 | 0.4 | `BC-ADM-001`, `BC-DISC-001` | Menselijke goedkeuring van de Admin-inventaris vastgelegd; `BC-ADM-001` naar `DONE`; `BC-DISC-001` als actieve taak naar `READY`; dashboard, tellingen, route, taakrecords, besluiten, bewijs en beperkingen bijgewerkt | Goedgekeurd read-only onderzoek afsluiten en het volgende read-only onderzoek bestuurbaar klaarzetten zonder implementatietoestemming | Deze commit: `docs: approve Shopify Admin inventory` |
| 2026-08-04 | 0.5 | `BC-DISC-001` | Live JSON read-only herbevestigd; statische en conditionele gebruiksmatrix voor 396 bestanden gemaakt; auditverdachten, beide switchers, backups/debug, appinjectie en contentkoppelingen vastgelegd; taak op `REVIEW`; dashboard, tellingen, route, taakrecord, besluiten, vragen, risico's, afhankelijkheden en bewijs bijgewerkt | Actief, beschikbaar, kandidaat-legacy en dynamisch onbewezen themegebruik scheiden zonder Shopify- of themewijziging | Niet gecommit; opdracht verbiedt commit en push |
| 2026-08-05 | 0.6 | `BC-DISC-001`, `BC-DISC-002` | Menselijke goedkeuring van de actieve-themegebruiksmatrix vastgelegd; `BC-DISC-001` naar `DONE`; `BC-DISC-002` als actieve volgende taak naar `READY`; dashboard, tellingen, route, taakrecords, besluiten, vragen, risico's, afhankelijkheden en bewijs bijgewerkt | Goedgekeurd read-only onderzoek afsluiten en de volgende read-only taak bestuurbaar klaarzetten zonder inhoudelijke uitvoering of implementatietoestemming | Deze commit: `docs: approve active theme usage inventory` |
| 2026-08-05 | 0.7 | `BC-DISC-002` | Taak tijdens uitvoering op `IN_PROGRESS` en na afronding op `REVIEW`; openbare representatieve steekproef van BadkamerXXL, Sanitairwinkel en Sanitairkamer vastgelegd; concurrentprofielen, vergelijking, IA, zoeken/filters, kaarten, PDP's, services, content, technische SEO, patronen, anti-patronen, kansen en bewijsgrenzen gedocumenteerd; dashboard, fase, tellingen, route, taakrecord, besluiten, vragen, risico's, afhankelijkheden en bewijs bijgewerkt | Feitelijke concurrentie-input leveren voor latere menselijke IA-/SEO-/UX-besluiten zonder Shopify-, theme-, implementatie- of publicatiehandeling | Niet gecommit; opdracht verbiedt commit en push |
| 2026-08-05 | 0.8 | `BC-DISC-002`, `BC-DATA-002` | Menselijke goedkeuring van het concurrentie-/SEO-onderzoek vastgelegd; `BC-DISC-002` en fase 1 naar `DONE`; nieuwe kleine read-only leveranciersbron-/veldeninventaris `BC-DATA-002` als actieve taak naar `READY` maar niet gestart; `BC-DATA-001` `BLOCKED`; dashboard, fasen, werkstromen, tellingen, route, taakrecords, besluiten, vragen, risico's, afhankelijkheden, bewijs en checklists bijgewerkt | Goedgekeurd fase-1-onderzoek afsluiten en alleen de benodigde bronvoorbereiding voor het latere datamodel klaarzetten zonder ontwerp- of implementatietoestemming | Deze commit: `docs: approve competitor research and prepare data inventory` |
| 2026-08-10 | 0.9 | `BC-DATA-002` | Taak tijdens uitvoering op `IN_PROGRESS` en na technische afronding op `REVIEW`; volledige lokale set van 405 bestanden bij taakstart en Git-padgeschiedenis onderzocht; nul oorspronkelijke leveranciersbronnen, nul importbestanden, nul import-/generatiescripts, zes afgeleide switcherdata-assets en vijf relevante storefrontscripts vastgelegd; veld-, identifier-, keten-, kwaliteits-, ontbrekende-input- en eigenaarschapsanalyse gedocumenteerd; dashboard, fase, tellingen, route, taakrecords, besluiten, vragen, risico's, afhankelijkheden, bewijs en checklists bijgewerkt | Feitelijke lokale basis en ontbrekende externe input vastleggen vóór enig datamodel of importontwerp, zonder Shopify-, bron-, theme- of codewijziging | Niet gecommit; opdracht verbiedt commit en push |
| 2026-08-10 | 0.10 | `BC-DATA-002`, `BC-DATA-003` | Menselijke goedkeuring van de lokale leveranciersnulmeting vastgelegd; `BC-DATA-002` naar `DONE`; externe bronnen blijven latere leveranciersafhankelijkheden; `BC-DATA-003` als actieve brononafhankelijke documentatietaak naar `READY` maar niet inhoudelijk gestart; dashboard, fase, werkstroom, taakregister, route, besluiten, vragen, risico's, afhankelijkheden, bewijs en checklists bijgewerkt | Goedgekeurd lokaal onderzoek afsluiten en een logisch informatiecontract mogelijk maken zonder bronmapping, Shopify-opslagbesluit of implementatie | Deze commit: `docs: approve supplier inventory and prepare product contract` |
| 2026-08-10 | 0.11 | `BC-DATA-003` | Brononafhankelijk productinformatiecontract v0.1 met 190 unieke conceptkeys in 15 domeinen opgesteld; vijf producttypeklassen, leegstaatbeleid, validaties, tien kwaliteitsgates, abstracte opslagcategorieën en leeg leveranciersmappingtemplate vastgelegd; fase en taak naar `REVIEW`; dashboard, route, taakrecord, besluiten, vragen, risico's, afhankelijkheden, bewijs en checklists bijgewerkt | Functionele productinformatiebehoefte bestuurbaar maken zonder beschikbare leveranciersdata, definitieve Shopify-/leveranciermapping, mutatie of implementatie te claimen | Niet gecommit of gepusht; fase-B-opdracht verbiedt tweede commit en push |
| 2026-08-10 | 0.12 | `BC-DATA-003`, `BC-TECH-002` | Beperkte menselijke goedkeuring van het productcontract vastgelegd; `BC-DATA-003` naar `DONE`; fase 2 voor resterend definitief data-/IA-werk naar `BLOCKED`; nieuwe read-only technische decompositietaak `BC-TECH-002` actief `READY` maar niet inhoudelijk gestart; dashboard, fasen, werkstromen, taakregister, route, besluiten, vragen, risico's, afhankelijkheden, bewijs en checklists bijgewerkt | Het contract als bestuurde conceptuele werkbasis afsluiten en technische stabilisatie eerst veilig opdelen zonder implementatie | Deze commit: `docs: approve product contract and prepare technical stabilization` |
| 2026-08-11 | 0.13 | `BC-TECH-002` | Bestaande audits gericht herbevestigd; 21 technische bevindingen, twaalf niet-officiele kandidaatdeeltaken, Theme Check-/toolingbasis, afhankelijkheden, minimale regressiematrix en preview-/rollbackvereisten vastgelegd; fase en taak naar `REVIEW`; geen volgende taak geactiveerd | De brede technische epic bestuurbaar opdelen en veilige volgorde bepalen zonder defect, Shopify- of theme-wijziging | Niet gecommit of gepusht; hervatopdracht verbiedt commit en push |
| 2026-08-11 | 0.14 | `BC-TECH-002`, `BC-GOV-006` | Menselijke goedkeuring van het stabilisatieplan vastgelegd; `BC-TECH-002` naar `DONE`; fase 3 terug naar `BLOCKED`; nieuwe lokale governance-/loggingtaak `BC-GOV-006` actief `READY` maar niet inhoudelijk gestart; dashboard, fasen, taakregister, route, besluiten, vragen, risico's, afhankelijkheden, bewijs en checklists bijgewerkt | Goedgekeurd technisch onderzoek afsluiten en eerst permanent controleerbaar uitvoeringsbewijs inrichten zonder technische kandidaat of implementatie te starten | Deze commit: `docs: approve technical stabilization plan and prepare execution logging` |

**Wijzigingslog 2026-08-11, versie 0.15, `BC-GOV-006`:** permanent lokaal uitvoeringslogprotocol, `.gitignore`, `AGENTS.md`-guardrails en vier PowerShell-helpers gebouwd; bootstraprun, command-/note-evidence, parser-, succes-, failure-, UTF-8-, grote-output-, redactie-, hash-, ignore-, Git-, secret- en ZIP-controles vastgelegd; taak en fase naar `REVIEW`; geen volgende taak geactiveerd. Reden: volledige controleerbaarheid en uploadbaar bewijs bieden voordat enige technische kandidaat start. Commit: niet gecommit of gepusht; fase B vereist menselijke review.

**Wijzigingslog 2026-08-11, versie 0.16, `BC-GOV-006`:** voorwaardelijke menselijke review verwerkt; de finalizer maakt hashgecontroleerde `review_files/`, weigert gevoelige/externe paden en incomplete raw quartetten en promoveert alleen een gevalideerde `.building.zip`; de command-helper behandelt cmdletfouten met `ErrorActionPreference = Stop`; protocol en `AGENTS.md` vereisen een one-bundle-handoff. Positieve en negatieve selftests zijn gelogd, `BC-GOV-006` en fase 0 gaan naar `DONE`, geen volgende taak is geactiveerd. Commit: deze commit `chore: finalize Codex execution logging`, gevolgd door push naar `main` en finale reviewfix-bundle.

### Zelfcontrole versie 0.16

- **Tegenstrijdigheden:** De tijdlijn van omgevingscontrole en latere development-theme-aanmaak is expliciet verklaard; geen inhoudelijke tegenspraak gevonden.
- **Dubbele taken:** Geen dubbele taak-ID of bewust dubbel werk gevonden; raakvlakken zijn via afhankelijkheden gekoppeld.
- **Ontbrekende hoofdonderdelen:** Alle 65 verplichte hoofdstukken zijn opgenomen.
- **Onbewezen aannames:** Onbekende runtime, apps/pixels, externe leveranciersbronnen, data-eigenaars, kandidaatbestanden en besluiten zijn gemarkeerd met `[NOG ONDERZOEKEN]`, `[OPEN BESLISSING]`, `[GEBLOKKEERD]`, **ONTBREEKT**, **NIET TOEGANKELIJK**, `DYNAMIC_OR_NOT_PROVEN` of een expliciete lagere zekerheid.
- **Statusduidelijkheid:** Alleen de zeven toegestane taakstatussen zijn gebruikt; tellingen staan in dashboard en taakregister.
- **Onderzoeksstatus:** `BC-ADM-001`, `BC-DISC-001`, `BC-DISC-002`, `BC-DATA-002`, `BC-DATA-003`, `BC-TECH-002` en `BC-GOV-006` zijn consequent `DONE`; fase 0 is `DONE`; fase 2, fase 3, `BC-DATA-001`, `BC-IA-001` en `BC-TECH-001` zijn `BLOCKED`; geen taak is actief.
- **Acceptatiecriteria en afhankelijkheden:** Iedere voorlopige taak bevat beide velden.
- **Te grote taken:** `BC-TECH-001`, `BC-UX-001`, `BC-CAT-001`, `BC-PDP-001`, `BC-SEO-001`, `BC-PROD-001` en `BC-QA-001` blijven brede werkpakketten. De twaalf kandidaatdeeltaken staan alleen in het goedgekeurde stabilisatieplan en zijn geen officiele taakrecords.
- **Taaktelling:** 41 unieke taakrecords: 11 `DONE`, 0 `READY`, 0 `IN_PROGRESS`, 0 `NOT_STARTED`, 26 `BLOCKED`, 1 `REVIEW` en 3 `DEFERRED`.
- **Contractcontrole:** 190 unieke contractkeys in 15 domeinen; nul `custom.*`-keys; iedere matrixrij heeft 19 gevulde gegevenskolommen; labels, bronnen, eigenaars, validatie en leegstaat zijn structureel gecontroleerd.
- **Technisch plan:** 21 bevindingen hebben impact, bereikbaarheid, zekerheid, bewijs en blokkade; twaalf kandidaten hebben bestanden, scope, afhankelijkheden, acceptatie, tests, preview en rollback. Geen kandidaat is in het centrale taakregister opgenomen.
- **Loggingtaak:** `BC-GOV-006` heeft een volledig taakrecord en staat na menselijke review `DONE`; de drie reviewfixes, raw completeness, reviewhashes, atomische bundle en negatieve weigeringstests zijn lokaal bewezen. De acht protocolbestanden worden in deze commit naar `main` gepusht en de finale one-bundle-run bevat alle reviewbestanden.
- **Tellingcontrole:** 41 unieke taakrecords; 12 `DONE`, 0 `READY`, 0 `IN_PROGRESS`, 0 `NOT_STARTED`, 26 `BLOCKED`, 0 `REVIEW` en 3 `DEFERRED`.
- **Ontwikkeltoestemming:** Niet verleend; versie 0.16 houdt bronacceptatie, definitieve mapping/opslag, ontwerp, Shopify-/theme-/datawijzigingen, verwijdering en technische implementatie expliciet geblokkeerd.
