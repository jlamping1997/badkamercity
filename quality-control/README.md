# QC-04 — optionele notities, globale voortgang, rustige dag/nachtinterface

30 oktober 2026 · **PRIVATE_DEPLOYED / EXISTING_DATA_PRESERVED / NOTES_AND_GLOBAL_RANDOM_ROUNDS**.

[Dezelfde privétool](https://badkamercity-quality.jason015.chatgpt.site). Versie5 succeeded; Sites-broncommit6095868c69cab2bfd667f0bbdd024678b5261d6c, deployment appgdep_6ae3e69ac9548191beb9180a3b61d591. De eigenaar vraagt notities bij afkeuringen, globaal/willekeurig hervatten, minimaler ontwerp en een kleine nacht/dagknop; dit zijn nu de actuele interactieafspraken boven QC-03/QC-02 hieronder.

## Gedrag

- Eén hoofdfoto per product, Ja/Nee/Twijfel/Technische tekening blijven direct. Geen verplichte notitie of afkeurmodal. Notitie toevoegen opent vrije tekst en snelle redenen (kleur/model/bijsnijden/resolutie/achtergrond/andere foto).
- Keuze bewaart notitie; Notitie bewaren slaat apart op zonder doorspringen of automatische goedkeuring. Aanleverlijst toont en heropent reden. Wijzigingen worden vóór overslaan, selectie-/schermwissel en checkpoint bewaard. Bij onbevestigde opslag blijft de kaart met retry staan; revisie409 voorkomt overschrijven van andere apparaten. Een nog niet bewaarde notitie bij abrupt browser sluiten is geen bevestigde opslag.
- Alle beoordelingen stonden al globaal per eigenaar in D1. Checkpoint bewaart selectie/positie en alle voortgang blijft daarnaast bestaan; geen rollback van latere beoordelingen. Nieuwe checkpoints ondersteunen alle merken en gemengde item-ID’s, progressScope=all-products en volgorde. Oude merkspecifieke checkpoints blijven leesbaar en hervatbaar; actuele hoofdfotofilter/positie behouden.
- Standaard Alle merken + willekeurig. Willekeurig verder start een nieuwe pending-ronde uit alle merken en slaat beoordeelde kaarten over. Later is geen goedkeuring/afkeuring en kan opnieuw verschijnen. Afkeur/twijfel/alle-filters maken bewuste herbeoordeling mogelijk. Start wacht op de eerste poging om opgeslagen voortgang op te halen, zodat een nog ladende gebruikersregistratie geen nieuwe pending-ronde vormt.
- Rustige interface zonder grote zijbalk. Kleine vaste dag/nachtknop rechtsboven; apparaatvoorkeur bc-qc-theme in localStorage, geen reviewrecords naar browseropslag verplaatst. Foto’s blijven kleurgetrouw zonder filter/inversie. Donkere UI betekent niet dat originele witte fotoachtergronden worden omgekleurd.

## Data behouden en afgeschermd

Geen nieuwe Site, DB, authclient, tabellen, item-ID’s, bronimport, schemamigratie, datareset, seed, verwijdering of Shopify-write. Dezelfde eigenaarstoegang is behouden. Na deployment is de authclient gelijk aan ervoor. Bestaande reviews en checkpoint zijn vóór/na via begrensde native D1-readback vergeleken: de daadwerkelijk teruggegeven steekproeven identiek. Dit is een begrensde controle, geen claim dat elk historisch oordeel inhoudelijk opnieuw beoordeeld is. Geen agent-testnotitie/-checkpoint naar productie geschreven; tests gebruiken afzonderlijke tijdelijke SQLite.

Productwerkkopie SHA256 onveranderd:5d4bc24f411c68f4f32006068e9637cdf37da681a238b5ab065c01d53bd448e8. Beoordelingen/notities/geschiedenis en checkpointinhoud blijven uitsluitend in afgeschermde D1 en zijn niet naar publieke Git gekopieerd. Volledige bronwerkkopie blijft in private Sites-bronrepo. Publieke spiegel heeft code, importscope, documentatie en een lokale screenshot zonder visitoridentiteit.

## Bewezen controle

- TypeScript en productiebuild PASS; **30API-/echte-SQLite-/selectiecontractgroepen PASS**, waaronder bestaande data-/owner-/origin-/idempotentie-/409guards, notitie-update met behoud classificatie, note-only unchecked, globaal checkpoint zonder reviewsreset, oude checkpoint behouden, merkgebonden scopeafwijzing, random pending/selectie/omvang en compacte catalogus met identieke hoofdfoto-ID’s.
- Lokale managed browser: notitieveld en snelle reden, nachtstand wisselen en behouden na herladen. Ongefilterde foto, echte productdata. Werkelijke UI in320/390px-iframes: geen horizontale overflow (inner303/373px), titel22px op390, foto circa395px bij900px iframehoogte. Tijdelijke QA-route verwijderd vóór bouwen.
- Hosted service-read: /api/catalogue?brand=all&scope=review HTTP200,11.679producten,11.034met hoofdfoto, maximaal1afbeelding per product. Response14.057.086bytes. /api/review zonder visitoridentiteit HTTP401, zoals bedoeld; geen identiteit geïmiteerd.
- Compacte Hotbath rawJSON17.275.825→9.868.512bytes. Dit is pakketinhoud, geen gemeten telefoonlatentie-/Lighthouseclaim. Oorspronkelijke volledige catalogusroute blijft beschikbaar; galerijen niet vernietigd.
- Fysieke telefoon, hosted visitor-write en langdurige offline/reconnectproef niet namens eigenaar uitgevoerd. De lokale demo heeft zichtbaar uitgeschakelde schrijfknoppen zonder visitoridentiteit. Owner gebruikt de bestaande privélink met hetzelfde ChatGPT-account.

![Lokale dag- en nachtweergave320/390px, zonder ingelogde visitor](qa/calm-day-night.jpg)

## Volgende handeling

Eigenaar herlaadt dezelfde privétool, controleert eigen voortgang, voegt optioneel een notitie toe en kiest willekeurig verder of hervat een bestaand checkpoint. Bij een probleem de concrete kaart/actie en opslagmelding onderzoeken; geen productiegegevens resetten. De storefront/offerte-uitvoering blijft afzonderlijk.

---

# QC-03 — hoofdfoto’s met vier directe keuzes

30 oktober 2026 · **PRIVATE_DEPLOYED / MAIN_PHOTO_PASS_IMPLEMENTED**.

Op expliciet verzoek van de eigenaar: één hoofdfoto per product; Ja/Nee/Twijfel/Technische tekening; geen tekstveld of extra foto-dropdowns. Foto groter (mobiel44svh, gemeten370px bij844px iframehoogte) en volledige producttitel22px op mobiel/27px desktop, boven de foto, zonder afkapping. Productgegevens behoudt de afzonderlijke checklist.

De huidige eerste afbeelding per product is de hoofdfoto van deze gedateerde werkkopie. De oorspronkelijke media-inventaris heeft geen niet-afbeeldingsmedia vóór deze foto (alle drie bronsets gecontroleerd); geen verse Shopify-import of claim van live synchronisatie. **11.034 hoofdfotokaarten**, waaronder7.591Hotbath en2.451Wiesbaden.645foto-loze producten blijven op de aanleverlijst.

Technische tekening bewaart een eigen role=technical met main=no en vaste reden, status=wrong voor de correctiewachtrij; geen getypte toelichting nodig. Ja/Nee/Twijfel bouwen eveneens een compleet oordeel in één actie. Oudere oordelen/audit blijven staan. Galeriecheckpoints worden bij hervatten gefilterd op huidige hoofdfoto-ID’s en overeenkomstige voortgang; productcheckpoints blijven ongewijzigd. Geen datareset of schemamigratie.

**Bewijs:** TypeScript en productiebuild PASS;20API-/echte-SQLite-/selectiecontractgroepen PASS. Zeven nieuwe scenario’s bewijzen één foto per product, lege galerij, vier volledige keuzen, aparte tekeningclassificatie, checkpointfilter/positie en productcheckpointbehoud, tekening save/read, volledige steekproefdekking11.034. Lokale browser:0tekstvelden in de fotocontrole, vierde knop aanwezig, Hotbath-totaal7.591. Tijdelijke echte app-iframes320/390px: geen horizontale overflow, titel22px/foto370px. De tijdelijke QA-route is verwijderd en zit niet in de deployment. Fysieke telefoon-/touch- en hosted visitor-schrijfproef niet opnieuw namens eigenaar geclaimd; geen private beoordeling gelezen of gewijzigd.

Deployment **versie4 succeeded**, broncommit e14dadfcb7e4758b0ec47df11ff58be0f95d137c, deployment appgdep_6ae3dd8432d081919cce24dd3666d45d. [Dezelfde privélink](https://badkamercity-quality.jason015.chatgpt.site). Toegang uitsluitend bestaande eigenaar; geen audience-/authwijziging. Geen webshop-, ranking-, collectie- of productwrite.

![Lokale mobiele controle320/390px; schrijfacties uit zonder visitoridentiteit](qa/main-photos-mobile.jpg)

Volgende handeling: eigenaar herlaadt dezelfde privétool en doet de hoofdfotobatch met vier keuzes; checkpoint blijft beschikbaar. Publieke code in review-app; volledige productwerkkopie in private Sites-bronrepo en beoordelingen uitsluitend in D1. Onderstaande QC-02/QC-01-instructies zijn historische basis waar ze afwijken van deze vierkeuzebediening.

---

# QC-02 — mobiele productcontrole

30 oktober 2026 · **PRIVATE_DEPLOYED / CATALOGUE_VERIFIED / AUTHENTICATED_PHONE_REVIEW_PENDING**.

[Open de privétool](https://badkamercity-quality.jason015.chatgpt.site). Toegang staat uitsluitend op het bestaande eigenaarsaccount; geen uitnodigingen/groepen toegevoegd. Meld aan met ChatGPT. Geen Shopify-thema, product, prijs, voorraad, publicatie of sortering gewijzigd.

## Opgeleverd

- Per merk foto’s en productgegevens beoordelen; batches25/50; Cobber/Caral als eerste werkselectie op huidige titel, zonder kwaliteitsclaim of automatisch serieattribuut.
- Links/fout, rechts/klopt, twijfel, overslaan, undo, fotovergroting, fototype, hoofdfotogeschiktheid en notities. Knoppen bieden een alternatief voor gestures.
- Productchecklist identiteit, specificaties, PDF, omschrijving en onderdelen; geen volledige goedkeuring zonder complete checklist.
- Directe bevestigde D1-opslag per eigenaar, revisieconflicten, idempotente actie-ID’s en historie. Geen offline wachtrij; bij onbevestigde opslag blijft de kaart staan. Niet als opgeslagen presenteren vóór bevestiging.
- Named checkpoints bewaren merk, controletype, batch en positie. Hervatten is een bladwijzer, geen terugdraaiing van nieuwere oordelen. Op dit moment onopgeslagen kaartnotities vallen erbuiten.
- Aanleverlijst voor fout/twijfel/ongeschikte huidige hoofdfoto en ontbrekende foto; JSON-export van beoordelingen/checkpoints.

## Brondekking

Volledige gepagineerde active-inventaris: **11.679 producten / 34.713 afbeeldingen** met een huidige Shopify-webshop-URL. 8.236 Hotbath /23.266afbeeldingen, 2.451Wiesbaden/6.585,277THE MOSAIC FACTORY/1.084,273JEE-O/766,104Sunshower/358,337Porcelanosa/2.649,1bestaand BadkamerCity Test-artikel/5. Alle media-/variantverbindingen hebben hasNextPage=false. Geen ontbrekende pagina’s als 'klaar' behandeld.

**645 Hotbath-producten hebben geen foto**; automatisch op aanleverlijst, niet verstopt in de swipestapel. Geen automatische foutcorrectie of publicatiewijziging.

Gedateerde werkkopie, geen live synchronisatie, tweede masterregister of nieuwe fabrikantbron. Bestaande registers/verrijkingsresultaten blijven brononderzoek dragen. Geen onafhankelijke foto-/kleur-/setcontrole uitgevoerd. Geen fotorechten, PVD, materiaal, sterkte, compatibiliteit, beschikbaarheid of conversie bewezen. Webshop-URL’s niet allemaal individueel in browser geopend. SHA-256 van metadata/URL/datum is geen hash van de beeldbytes; gelijkblijvende URL/mediadatum met gewijzigde bytes blijft een open grens.

## Architectuur en opslag

Sites/Vinext-worker met private platformtoegang, ChatGPT-gebruiker en D1-tabellen qc_reviews en qc_checkpoints. Servercontrole op identiteit/eigenaar, same-origin POST, invoer, actuele items, revisions en dubbele aanvragen. Geen Admin-token of willekeurige connectorproxy in browser. Beoordelingen, notities, checkpoints en eventuele eigenaarsgegevens nooit naar publieke Git.

Complete deploymentbron inclusief gedateerde catalogus staat in private Sites-bronrepo; publieke reviewbare code onder review-app, met importoverzicht en herstelinstructies. Volledige productwerkkopie niet opnieuw als openbare mastercatalogus gecommit. Het ontbreken van data/catalogue.json in de publieke spiegel is expliciet gedocumenteerd; herstel de private bron of voer een nieuwe volledige read-only import uit vóór bouwen/testen van de momentopname.

Project appgprj_6ae3d58930e48191b4dea11d39180671. Definitieve Sites-broncommit **b0a2d9514443ed487e5d09580c04b1fffa2808b6**; versie3, deployment appgdep_6ae3db3bd2d88191b3403a7b3b22b78b **succeeded**, URL hierboven. Broncache SHA256 5d4bc24f411c68f4f32006068e9637cdf37da681a238b5ab065c01d53bd448e8.

## Controlebewijs en grenzen

- TypeScript geen fouten; productiebuild geslaagd.
- **13 betekenisvolle tests geslaagd**: echte SQLite met gegenereerde migraties plus echte API-handlerlogica, waaronder identiteit/eigenaar, origin, invoer, save/read, audit/undo, dubbele aanvraag, stale revision409, checklist, checkpoint/reread/dubbel en catalogusidentiteit/dekking. Geen mock-test als hosted login gepresenteerd.
- Lokale managed browser: echte productdata, batches, merk wisselen naar Wiesbaden/Caral, zoom/Escape. Auth ontbreekt in die preview; schrijven is zichtbaar uitgeschakeld.
- Echte app in tijdelijke lokale iframe op320/390px; geen horizontale overflow (inner303/373px wegens scrollbar). Compacte batch toont controles op ongeveer595–630px top bij framehoogte1000; geen fysieke iPhone-/touchgesturetest. Tijdelijke QA-route verwijderd en niet gepubliceerd.
- Hosted service-read via door Sites teruggegeven bestaande service-toegang: /api/catalogue HTTP200/7groepen; Wiesbaden HTTP200/2.451producten. /api/review zonder visitoridentiteit HTTP401 zoals bedoeld. Geen identiteitheaders geïmiteerd.
- Hosted D1-overview bevestigt DB met qc_reviews en qc_checkpoints; geen productieoordeel of testcheckpoint aangemaakt.
- Privé-gate toont correct ChatGPT-aanmelden. Browser kwam bij nieuwe aanmeldkeuze; geen credentials gevraagd/verwerkt. **Hosted visitor-login, visitor-write, echte telefoon, offline/reconnect en gelijktijdige apparaten niet end-to-end getest**. Versie3 bewaart bovendien dezelfde checkpoint-ID bij een geslaagde insert gevolgd door een mislukte verversing, zodat opnieuw proberen geen dubbele bladwijzer maakt. De update van versie2 bewaart de aanmeldmelding bij merkwissel en toont opnieuw aanmelden na een verlopen schrijfsessie; geen nieuwe server-/datastructuur.

## Volgende handeling

**Eigenaar opent de privélink op zijn telefoon, beoordeelt één echte batch en maakt/hervat een named checkpoint.** Daarna waargenomen telefoon-/opslagproblemen gericht oplossen vóór grotere werksessies. Fouten alleen signaleren; geen Shopify-correcties activeren.

Bestaande ASSORT/TAX/storefrontuitvoering niet overgenomen. Bestaande werkcheckout ongemoeid gelaten; geen branchwissel, reset of forcepush. Nieuwe QC-tak is expliciet door de eigenaar gevraagd. GitHub-spiegel via connector met expected_sha; main uitsluitend documentatie-ingang. Rollback: deze geïsoleerde Site terug naar een bestaande versie via Sites; beoordelingen/D1 behouden. Geen destructieve reset of schemarollback.

## Schermbewijs

![Lokale reviewinterface met echte productdata](qa/review-desktop.jpg)

Dit is de lokale managed preview: schrijfknoppen uitgeschakeld zolang visitoridentiteit ontbreekt. Geen screenshot van een succesvol ingelogde hosted sessie of fysiek toestel.

---

## Historische QC-01-afspraken

# BadkamerCity — Quality Control

30 oktober 2026 · QC-01 · eigen projecttak: `quality-control`.

## Status en opdracht

**FOUNDATION_DOCUMENTED / NO_PRODUCT_AUDIT_YET / MOBILE_APP_NOT_BUILT.**

De eigenaar vraagt expliciet een eigen Git-tak voor kwaliteitscontrole van online producten. Dit is de toegestane uitzondering op de algemene regel geen nieuwe branch per chat. De tak start vanaf main, commit d5dbc60eeea4029a84b7a88659d14a18084ee69c; het is een zelfstandig QC-project, geen actuele Shopify-deploysnapshot. De bestaande storefront-uitvoering/werkbranch blijft apart. Geen wijziging aan Shopify, sortering, productinhoud of afbeeldingen.

Deze eerste oplevering legt de werkwijze en projectstatus vast. Er is nog geen catalogus ingelezen, geen foto beoordeeld en geen werkende telefoonapp of automatische opslag aangesloten. De kwaliteitscontroles zijn dus niet fictief alvast ingevuld.

## Doel

De eigenaar kan in korte sessies op zijn telefoon foto's controleren en daarna zien welke productdata hij moet aanleveren. Dezelfde administratie ondersteunt later betrouwbare productverrijking en de aanbevolen productvolgorde.

Een foto bestaat is iets anders dan een juiste foto. Geïmporteerde/gescrapete gegevens en een producttitel zijn geen onafhankelijke referentie voor elkaar.

## Telefoonscherm — te bouwen

Per kaart:
- Grote, zoombare foto; teller binnen de batch en eenvoudige voortgang.
- Merk, serie, exact fabrikantartikelnummer/SKU, producttype en relevante uitvoering/kleur.
- Bijbehorende variant en rol van de foto: product, sfeer, detail, maatvoering of montage.
- Indien beschikbaar een onafhankelijke fabrikantreferentie/bron naast de winkelfoto. Ontbreekt die, dan is dat zichtbaar.
- Knoppen **Fout**, **Twijfel** en **Klopt**. Links swipen = Fout; rechts = Klopt. De knoppen blijven altijd beschikbaar.
- Na Fout of Twijfel een korte reden, bijvoorbeeld verkeerd product, verkeerde uitvoering, alleen sfeerbeeld, slechte uitsnede/kwaliteit of onvoldoende bewijs.
- Ongedaan maken, overslaan en later hervatten. Een swipe start niet wanneer iemand een foto zoomt of de pagina scrolt.

Een sfeerfoto kan bij het product horen zonder geschikt te zijn als hoofdfoto. Daarom worden deze twee vragen apart bewaard:
1. Hoort deze foto bij dit artikel/deze uitvoering?
2. Is deze foto geschikt voor de bedoelde plaats, zoals hoofdafbeelding?

## Batches en hervatten — contract

Begin met een proef van circa 25–50 foto's, geen verplichte beoordeling van een heel merk. Eerste prioriteit: Hotbath Cobber en Wiesbaden Caral bij kranen. Selecteer op echte artikel-/seriegegevens; een losse titelmatch is niet voldoende.

Elke beoordeling wordt direct duurzaam opgeslagen met bevestiging. Een openstaande opslag mag niet als voltooid meetellen. Een foutieve verbinding blijft zichtbaar; een lokaal wachtende actie moet later veilig kunnen synchroniseren zonder dubbele uitslag. Op een ander apparaat hervatten moet mogelijk zijn: uitsluitend localStorage is onvoldoende.

Bewaar batch-ID, bronmoment, reviewvolgorde, openstaande items en wijzigingenlog. Gebruik controle op gelijktijdige bewerking en een unieke actie-ID. Terugdraaien voegt een herstelactie toe; het wist het oude oordeel niet stil.

Een afgeronde batch betekent uitsluitend dat alle items een uitkomst hebben. Twijfel/fout kan dan nog open opvolgwerk bevatten. Een product is niet automatisch compleet als één foto is goedgekeurd.

## Wat de eigenaar moet kunnen terugzien

Een eenvoudig overzicht met filters op merk/serie en:
- Nog te beoordelen.
- Foto verkeerd: vervangende foto nodig.
- Foto niet geschikt als hoofdafbeelding.
- Twijfel: referentie of bevestiging nodig.
- Specificaties, documenten of productuitleg ontbreken.
- Visueel gecontroleerd; overige controles nog open.
- Alle toepasselijke controles afgerond, met datum.

Per artikel een concrete aanleverlijst: **wat ontbreekt, waarom, voor welk SKU/variant, welk bewijs nodig is en wat daarna opnieuw gecontroleerd wordt**. Lever liever aantoonbare fabrikantdata dan opgevulde velden.

## Controle van de rest van de productdata

| Onderdeel | Wat we controleren |
| --- | --- |
| Identiteit | Merk, exact fabrikantnummer, variant en producttype kloppen |
| Foto's | Juiste uitvoering en passende beeldrol; scherp en bruikbaar |
| Specificaties | Verplichte keuzegegevens voor dit producttype zijn bewezen |
| Documenten | Juiste handleiding, technische tekening/PDF waar toepasselijk |
| Uitleg | Toepassing, setinhoud, afwerking en benodigde onderdelen duidelijk |
| Verkoopgegevens | Juiste prijs-/eenheid en actuele, onderbouwde beschikbaarheidsinformatie |
| Relaties | Categorie en eventuele compatibele onderdelen gecontroleerd |

Gebruik per controle **nog te beoordelen / akkoord / fout / twijfel / niet van toepassing**, met bron en datum. 'Niet van toepassing' vraagt een reden per producttype. Een haakje hoeft niet hetzelfde documentenpakket te hebben als een inbouwkraan.

Een visuele goedkeuring bewijst geen materiaalsamenstelling, PVD-coating, technische compatibiliteit of gebruiksrecht. Die feiten hebben een aparte broncontrole nodig. Bij onvoldoende informatie geen schijnzekerheid of verzonnen kwaliteitsscore.

## Eén productadministratie, geen dubbel werk

Bestaande productregisters en verrijkingsresultaten blijven uitgangspunt. Gebruik de bestaande product-ID/variant-ID en voeg QC-controles/beeldbeoordelingen daaraan toe of koppel ernaar. De lege projectstatus is geen nieuwe kopie van de catalogus.

Zie [bestaand productplan](../docs/PRODUCT_CONTENT_PLAN.md), [vervolg productkwaliteit](../docs/FUTURE_CONTENT_AND_PRODUCT_PROJECTS.md) en [categorisatiecontract](../docs/CATEGORIZATION_AND_SEO_POLICY.md). Het oude Wiesbaden-pilotregister is niet automatisch een actuele online-publicatielijst; raadpleeg ook het [uitvoeringsresultaat](../docs/product-content/WIESBADEN_EXECUTION_RESULTS_2026-10-21.md).

Voor de eerste import de actuele Online Store-publicatie controleren. Alleen ACTIVE is geen bewijs dat een product online bereikbaar is. Neem ook ontbrekende foto's op als aanlevertaak, niet alleen bestaande media.

## Identiteit, geldigheid en opvolging

Een beeldoordeel koppelt aan shop/product-ID, variant-ID of expliciete productbrede scope, media-ID, bron-URL en inhoudsvingerafdruk. Bewaar de gecontroleerde verwachtingen: SKU, uitvoering/kleur, beeldrol en referentiebron.

Als foto, variantkoppeling of relevante artikelgegevens veranderen, vervalt het eerdere oordeel voor die combinatie en komt die opnieuw in de wachtrij. Dezelfde URL kan nieuwe inhoud krijgen; alleen een URL vergelijken is onvoldoende.

Geef een oordeel nooit automatisch aan alle kleurvarianten of producten met dezelfde foto. Een bronbeeld mag op inhoud worden hergebruikt, maar de match moet per artikel/uitvoering bevestigd blijven.

Een afkeuring markeert een probleem. Het verwijdert, verwisselt of verbergt niet automatisch winkelbeelden/producten. De correctiewachtrij en het toepassen in Shopify zijn afzonderlijke stappen, met controle op tussentijdse wijzigingen en terugleescontrole.

## Voorkeursmerken en rangschikking

De eigenaar wil Hotbath **Cobber** en Wiesbaden **Caral** bij kranen verkoopvoorrang geven. Dat is een commerciële voorkeur, geen automatisch kwaliteitskeurmerk. Ook deze artikelen doorlopen dezelfde controles.

Een latere sorteerproef combineert passendheid, geverifieerde kwaliteit, variatie en expliciete verkoopvoorkeur. Bezoek-/koopdata en een klantkeuze voor prijsvolgorde blijven afzonderlijke signalen. Geen sortering of ranking gebouwd/aangepast in QC-01.

## Opslag en toegang — te bouwen

Git bewaart regels, versies, contracten en veilige openbare productstatus/exporten. De telefooninterface krijgt duurzame, afgeschermde opslag voor dagelijkse beoordelingen; niet bij elke swipe een handmatige Git-commit.

Deze repository is openbaar: geen sleutels, klantgegevens, privé-leveranciersfeeds, inkoopvoorwaarden, privéfoto's of ongecontroleerde gekopieerde mediabestanden committen. Git is geen wachtwoordbeveiliging. De uiteindelijke reviewapp krijgt server-side toegangscontrole; geen Admin-token in browsercode.

Techniekkeuze voor de app/opslag volgt pas na controle van bestaande beschikbare beheer-/opslagvoorzieningen. Geen nieuw abonnement, infrastructuur of tracker aangemaakt.

## Eerste proef en acceptatie

1. Controleer bestaande registers en actuele publicatie; kies 25–50 echte beeld-artikelparen uit Cobber/Caral, inclusief varianten, sfeerbeelden en twijfelgevallen.
2. Bouw de mobiele kaart en duurzame beoordelingen; test op de telefoon van de eigenaar.
3. Controleer swipen/knoppen, zoom, reden, opslaan, undo, hervatten en verbindingverlies.
4. Bewijs dat verkeerde foto's, verwisselde kleuren, dubbele acties, tussentijds gewijzigde media en onbekende gevallen correct worden afgehandeld.
5. Controleer de gegenereerde aanleverlijst per SKU en vergelijk de eerste proef met de eigenaar.
6. Pas daarna opschalen. Geen automatische Shopify-correcties of sortering aan deze proef verbinden.

## Exact één volgende handeling

**Inventariseer de bestaande productregisters en beschikbare beheer-/opslagvoorzieningen voor één echte, read-only Cobber/Caral-proefbatch; bouw daarna de mobiele reviewproef binnen deze projecttak.**

QC-01-controle: documentatie en project-JSON opgeslagen en via GitHub teruggelezen. Niet getest: catalogusmatching, beeldinhoud, telefooninterface, synchronisatie, autorisatie, scoring of productcorrecties. Bestaande storefronttaken worden hiermee niet overgenomen.
