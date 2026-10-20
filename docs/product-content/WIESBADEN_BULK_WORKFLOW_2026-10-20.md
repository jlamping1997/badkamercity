# Wiesbaden bulkverrijking — ontwerp en acceptatie, 20 oktober 2026

**DESIGN_READY / NIET GEÏMPLEMENTEERD ALS BULKVERWERKER.** Eigenaar vraagt na goedkeuring van de proefgroep om schaalbare verrijking met behoud van inhoudelijke kwaliteit, sterke SEO, filters en gedeelde breadcrumbs. Deze ronde onderzoekt en documenteert het ontwerp; geen nieuwe product-, index- of themamutaties.

## Bewezen uitgangspunt en afbakening

Verse Shopify-read: **195491168522 — BadkamerCity - Wiesbaden proefgroep 2 is nu MAIN**. Alle512 bestandschecksums zijn exact gelijk aan het eerder geteste concept. Voorganger195488317706 is UNPUBLISHED. Publicatie door eigenaar vastgesteld via Admin; geen nieuwe fysieke telefoontest geclaimd. De zeven productupdates uit het vorige dossier blijven de referentie, plus24.3710. Twee kernconflicten blijven open:29.8007 en41.3540.

De bronrun van19oktober heeft2.841 fabrikantartikelen van meerdere merken, daarvan2.457 Wiesbaden. Winkelmomentopname:2.265 Wiesbaden-producten;2.240 exacte bronkoppelingen,25 bestaande zonder bronmatch,217 nieuwe Wiesbaden-kandidaten. Dit zijn gedateerde tellingen, geen nieuwe volledige winkelinventarisatie. De601 nieuwe bron-SKU’s omvatten andere merken en zijn geen601 nieuwe Wiesbaden-producten. Volledige bron heeft978 ontbrekende categorieën en415 artikelen met schaarse specs; dat zijn overlappende groepen over alle merken. Niet als volledig automatische doorloop kwalificeren.

Hergebruik scripts/wiesbaden-data-run.py, scripts/wiesbaden-import-plan.py, bestaande broncache, winkelvergelijking en getypeerde veldmapping. De scripts zijn nu bron-/voorstelverwerkers zonder bulkmutaties. De bulkuitvoerder, claimcontrole, datakwaliteitsregels en gezamenlijke indexsynchronisatie moeten nog worden gebouwd en getest. Geen nieuw PIM, externe app of database nodig voor deze eerste merkuitrol.

## 1. Eén controleerbare feitenbasis

Bewaar per feit waarde, datatype, expliciete eenheid/maatas, oorspronkelijke bronverwijzing/datum, bewijs en status bevestigd/onbekend/conflict. Eenheidomrekening is exact en behoudt herkomst:800mm wordt80cm, geen onbenoemde lengte tot breedte promoveren. Ontbrekend blijft onbekend; false en0 zijn zelfstandige waarden. SKU blijft fabrikantnummer; geen EAN als koppelsleutel of nieuw verzonnen GTIN.

Fabrikantgegevens en bijbehorende tekeningen zijn de eerste bron. Een fabrikantentabel kan aantoonbaar fout zijn; een tegenstrijdigheid wordt niet automatisch gewonnen door een algemene bronprioriteit. Andere shops alleen gericht raadplegen waar een relevant gat of conflict bestaat, op exact hetzelfde artikel. Beoordeel brononafhankelijkheid: drie winkels kunnen dezelfde onjuiste leveranciersfeed kopiëren. Nieuwe feiten pas na passende bevestiging; eigen winkeltekst is geen onafhankelijke bewijsbron.

Gebruik bestaande HTML/cache eerst. Download dezelfde media-URL/inhoud eenmaal; controleer bestanden op daadwerkelijk type/bruikbaarheid. Extra PDF-/tekeninganalyse waar essentiële maatvoering, setinhoud of compatibiliteit onduidelijk is. Geen volledige hercrawl van meerdere webshops per artikel zonder noodzaak.

## 2. Regels per producttype, centraal beheerd

Voeg versiebeheer toe voor producttypeprofielen, bestaande veldaliases en categorie-/filtermapping. Opbouw wastafelkraan, losse uitloop, inbouwdeel, afbouwdeel en complete set zijn verschillende typen. Maak geen complete kraan van een onderdeel op basis van een brede broncategorie. Een model-/familierelatie mag alleen bevestigde gezamenlijke eigenschappen delen; kleur, maat, aansluiting en meegeleverde onderdelen blijven perSKU gecontroleerd.

Elk profiel definieert: kernfeiten voor veilig classificeren/verkopen, aanvullende nuttige specs, toegestane inhoudelijke uitleg, getypeerde filters en bestaande doelcollecties. Identiteit, productsoort, toepassing/montage en relevante maat-/compatibiliteits-/setfeiten zijn harde poorten waar ze voor het type essentieel zijn. Ontbrekende optionele bijlagen blokkeren niet een verder voldoende onderbouwd product. Onbekende essentiële aansluit-/setgegevens blokkeren wel de betreffende verrijking. De precieze kernvelden worden in de eerste proef op echte brongevallen vastgesteld.

Een centraal mappingbestand koppelt een bewezen producttype aan een bestaande bladcollectie en het gekozen categoriepad. Verifieer collectie-ID’s, echte URLs en beschikbare parentcollecties tegen de actuele winkelstructuur; Shopify-collecties hebben niet vanzelf deze onderlinge hiërarchie. Meerdere toepasselijke collectieleden kunnen blijven bestaan, met één vast hoofdpad. Geen categorie kiezen op basis van alleen de bezoekerreferrer of eerste toevallige collectie.

## 3. Eén bron voor alle klantweergaven

| Onderdeel | Herkomst en uitvoering |
| --- | --- |
| Eigen tekst, titel, korte titel, SEO | Alleen geselecteerde bevestigde feiten plus goedgekeurde uitleg per producttype |
| Specificatietabel | Getypeerde feiten naar bestaand custom.complete_specificaties, logisch gegroepeerd |
| Filters | Dezelfde feiten via bestaande custom/bc_filters-mapping en het echte manifest-/indexcontract |
| Collectielidmaatschap | Gevalideerde categorietoewijzing aan bestaande collecties; verwijderingen apart beoordelen |
| Breadcrumbs | Gedeeld bc-product-breadcrumbs-snippet leest gecontroleerd productpad en echte collectieobjecten |
| Product-/breadcrumbstructureddata | Bestaande markup eerst auditen; dezelfde product-/prijs-/padgegevens, geen tweede afwijkende bron |
| Bijlagen | Bestaand gedeeld bc-product-documents-snippet met bevestigde list.url |
| Zoekresultaten | Actuele titels én relevante zoek-/filtervelden synchroniseren met externe index; korte kaartbrug alleen is onvoldoende |

De gedeelde weergave is al aanwezig en getest. category_handles per product zijn gegevens, geen eigen Liquid per pagina. Genereer deze gegevens vanuit één centrale mapping; een padwijziging wordt als gerichte datawijziging uitgerold. Dezelfde padselectie moet zichtbare breadcrumb en BreadcrumbList sturen. Leg geen tweeduizendSKU’s of paden vast in if/else-blokken. De oude24.3710-pilotuitzondering kan later gecontroleerd naar dezelfde marker worden overgezet, met33specs als regressiecontrole; dit is geen reden om de bestaande route nu te herschrijven.

Hergebruik custom.card_title, complete_specificaties, technische_documenten en bc_data.content_review; controleer bestaande definities vóór writes, maak alleen aantoonbaar ontbrekende noodzakelijke definities, schrijf waarden en lees ze terug. Geen metafield per willekeurig bronlabel. De reviewmarker blijft een renderpoort, geen bewijs van volledige commerciële gereedheid.

Liquid rendert de huidige productdata op de server. AI, crawl, classificatie en zware controles draaien vooraf in de verwerking. Geen groot catalogusbestand of onnodig nieuw JavaScript op iedere productpagina. Gebruik de bestaande generieke componenten, varianten-/fallbackafscherming en styles. Codeverandering alleen bij een bewezen ontbrekende algemene functie.

## 4. Productinhoud en SEO

Gebruik per producttype een vaste leesbare opbouw: korte herkenbare intro, enkele bevestigde onderscheidende kenmerken, praktische keuze-/montage-informatie waar onderbouwd, expliciete setinhoud/los benodigde onderdelen en gegroepeerde specificaties. De bestaande producttitel levertH1; omschrijving gebruikt passendeH2/H3. Een eenvoudige glashouder heeft geen lang verhaal nodig. Stel geen verplicht woordenaantal of kunstmatige synoniemvariatie in.

Titel/SEO noemen het concrete producttype en relevante echte verschillen zoals serie, maat of afwerking. Kleur-/maatartikelen krijgen de juiste eigen onderscheidende informatie; verzin geen afwijkende claims om tekst uniek te maken. Brede categoriezoekvragen horen ook op de categoriepagina, niet allemaal in iedere productomschrijving. Alttekst beschrijft alleen aantoonbaar passend beeld, zonder verzonnen camera-/interieurdetails.

De schrijver krijgt uitsluitend de goedgekeurde facts en begrensde uitleg. Bewaar intern welke tekstclaims bij welke feiten horen. Een aparte inhoudelijke check beoordeelt betekenis, setlogica, informatiewaarde, taal en inconsistenties. Bepaalde feiten (afmetingen, aantallen, materiaal, claims, inclusief/exclusief) krijgen tevens vaste machinecontroles. Een tweede AI-oordeel of kwaliteitspercentage bewijst niet dat tekst klopt; geen automatische vrijgave uitsluitend op een AI-score.

Technische controle: title/H1/canonical, indexeerbaarheid, interne categorie-/breadcrumb-links, bestaande Product/Offer- en BreadcrumbList-markup, echt overeenkomende prijzen/beschikbaarheid en geldige HTML. Geen onbevestigde voorraad, reviewscore, garantie, levertijd of GTIN toevoegen. Controleer bestaande markup vóór aanpassing zodat geen dubbele strijdige schemaobjecten ontstaan. Test Rich Results per relevante template/type en parseer de gerenderde markup automatisch per product. Goede markup maakt de pagina geschikt voor bepaalde zoekweergaven, garandeert geen vertoning of ranking.

Meet later via Search Console per productgroep/URL vóór en na: indexatie, vertoningen, passende zoekvragen en klikken. Onderhoud/cohortvergelijking over voldoende tijd, geen rankingclaim op basis van een geslaagde import of interne SEO-score.

Primaire richtlijnen:
- [Google over generatieve content](https://developers.google.com/search/docs/fundamentals/using-gen-ai-content)
- [Google Search Essentials](https://developers.google.com/search/docs/essentials)
- [Productstructureddata](https://developers.google.com/search/docs/appearance/structured-data/product)
- [BreadcrumbList](https://developers.google.com/search/docs/appearance/structured-data/breadcrumb)
- [Kwaliteit/geen garantie op rich results](https://developers.google.com/search/docs/appearance/structured-data/sd-policies)
- [Shopify herbruikbare snippets](https://shopify.dev/docs/storefronts/themes/architecture/snippets)

## 5. Wat krijgt echt controle?

Elk product krijgt vóór toepassing een eigen controleverslag, met bronidentiteit, relevante feiten/tegenstrijdigheden, getypeerde waarden, categoriepad, voorgenomen filters, contentclaims, ontbrekende essentials en wijzigingsdiff. Opnieuw lezen van leverancierproza door alleen een taalmodel is geen volledige feitenvalidatie.

Alle producten: vaste data-/consistentiecontroles; inhoudelijke redactiecontrole; veilige HTML/escaping en schema-/linkchecks. Na toepassing: onafhankelijke Admin-readback van alle gewijzigde producten, vergelijking van beschermde velden en controle van gerenderde product-HTML. Valideer alle opgegeven interne doelcollecties en de productidentiteit. Filters: vergelijk alle geschreven filter-/indexwaarden met de goedgekeurde dataset; test API-profielen met positieve/negatieve gevallen, aantallen en numerieke grenzen. Geen claim dat elke mogelijke combinatie van filters visueel is bediend.

Menselijke inhoudscontrole:
- Eerste automatische proef van50kranen: alle50 inhoudelijk nalopen vóór eerste echte toepassing; bestaande heldcases dienen als verwachte blokkade/regressiecases.
- Ieder nieuw producttypeprofiel eerst inhoudelijk kalibreren vóór automatische doorloop.
- Daarna als begininstelling10% van iedere batch, minimaal5 per aanwezig producttype, gespreid over serie, kleur/maat en complexiteit. Dit is risicobeheer, geen statistisch bewijs van foutloosheid.
- Alle conflicten, ontbrekende kerngegevens, nieuwe/afwijkende regels en riskante compatibiliteits-/keurmerk-/setclaims apart inhoudelijk behandelen.
- Bij een bevestigde inhoudelijke fout betreffende regel/productfamilie stoppen, eerder gerelateerde uitvoer terugzoeken en de controle uitbreiden vóór hervatten.

Browsercontrole mobiel/desktop per gedeelde weergave, nieuw type en lange/afwijkende inhoud. Volledige individuele handmatige pagina-inspectie van tweeduizend producten past niet bij de gewenste versnelling. Automatische controle van alles plus gerichte menselijke controle beperkt werk, maar geeft geen absolute foutloosheidsgarantie.

## 6. Uitvoer, herstel en zoeken moeten samen kloppen

Gebruik één hervatbare verwerking: bronselectie → feitenvalidatie → classificatie → inhoud → controles → wijzigingsplan → toepassing → Admin/HTML/indexverificatie. Statussen onderscheiden onder meer voorbereiden, goedgekeurdvoorstel, gegevensgeschreven, indexinwachting, geverifieerd en reviewnodig. ready in de bestaande marker blijft alleen de renderpoort; houd de volledige uitvoerstatus in het runlog.

Lees huidige waarden/digests en maak private backups vóór writes. Schrijf alleen de beoordeelde veldverschillen, met rate-limitbeheer en checkpoints per product/API-batch. Behoud handles, product-/variantidentiteit, voorraad, media en prijzen tenzij apart een concrete wijziging is beoordeeld. Een bronwijziging of handmatige bewerking sinds de voorbereiding veroorzaakt conflict; geen blind overschrijven.

Shopify en VPS vormen geen gezamenlijke transactie. Leg iedere geslaagde stap vast, lees na en hervat alleen onafgemaakte stappen. Markeer een cohort pas voltooid na gewenste indexdocumenten en zoek-/filtertests. Kleine titelcorrectie voor de vorige zeven is voorbereid maar nog niet bewezen uitgevoerd; laat de bestaande lokaleCodex/SSH-omgeving dit controleren, niet afleiden uit themapublicatie. Bulkindexcontract eerst op een beperkt cohort bewijzen en schema-/facet-/prijsvelden beschermen.

Rollback herstelt alleen de eigen gewijzigde velden uit de private snapshot en weigert een conflict met latere bewerkingen. Volledige oude Adminbeschrijvingen, fabrikantHTML en secrets niet in publieke Git zetten. Bewijs/privacy gescheiden houden. Geen ongecontroleerde volledige indexrebuild.

## 7. Efficiëntie en meetbare uitkomst

Gebruik één vaste bron-/regel-/inhoudsversie en een hash van alle inhoudelijk relevante input. Herstart van dezelfde ongewijzigde versie mag geen nieuwe tekstgeneratie of writes veroorzaken. Alleen gewijzigde feiten, regels of eerder onvolledige stappen opnieuw verwerken. Cache bronbestanden/media en groepeer uitzonderingen per foutsoort; een bewezen regelcorrectie kan veelSKU’s tegelijk oplossen.

Voorgestelde stappen: bulkverwerker bouwen → offline dry-run van50kranen → bevindingen/regels herstellen → beperkte echte toepassing met volledige readback en werkende indexroute → vervolgens cohorten van ongeveer250.250 is een eerste operationele omvang, geen API-limiet. Bij nieuw producttype eerst opnieuw kalibreren. Meet verwerkingstijd, modelkosten, foutsoorten, herstel en handmatige behandeltijd in de eerste run; vóór deze meting geen uurprijs, doorlooptijd of automatisch slagingspercentage beloven.

Runrapport: aantal bekeken/bestaand/nieuw/zondermatch; voorstellen gereed; tegengehouden met redenen; gegenereerd versus hergebruikt; toegepaste velden; Admin/HTML/index geslaagd; ontbrekende bewijsstappen; steekproefomvang en gevonden fouten; gewijzigde/ongemuteerde beschermde velden; kosten/duur. Dubbele producten of dezelfde bron mogen niet twee keer tellen. Uitzonderingen die nog live oude inhoud hebben blijven herkenbaar; deze ronde archiveert ze niet.

Nieuwe217Wiesbaden-kandidaten zijn een aparte stroom met product-/media-/prijs- en publicatiecontrole. Begin met bestaande exact gekoppelde producten. Andere merken en25bestaande zonder bronmatch niet stil creëren/verwijderen of in de eerste bulkbatch opnemen.

**Exact één volgende implementatiestap:** breid de bestaande voorstelverwerker uit tot een alleen-lezen bulkproef voor50kranen, met typeprofiel, feitenherkomst, claim-/consistentiecontroles, categorie-/filtervoorstellen en afzonderlijke gereed/reviewrapporten. Geen2k-livewrites of nieuwe productaanmaak op grond van dit ontwerp. De werkende externe indexschrijf-/verifyroute moet vóór de eerste nieuwe bulktoepassing zijn bewezen.
