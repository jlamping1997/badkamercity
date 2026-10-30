# BadkamerCity — Productcontrole

## Actueel QC-04 — notities, willekeurig hervatten en dag/nacht

Dezelfde private Site, DB-binding, tabellen, productcache en item-ID's blijven leidend. Geen nieuwe database, gegevensreset, seed, schemamigratie of Shopify-write. Bestaande checkpoints, beoordelingen, revisies en historie blijven leesbaar met dezelfde gebruikersidentiteit. De agent schrijft geen testbeoordelingen naar productie.

De fotocontrole blijft één hoofdfoto per product met Ja/Nee/Twijfel/Technische tekening. **Notitie toevoegen** is optioneel en standaard dicht. Vrije tekst of snelle redenen; je keuze bewaart de notitie. **Notitie bewaren** slaat op zonder verder te gaan en zonder een nog onbeoordeelde foto goed te keuren. De aanleverlijst toont de reden en biedt opnieuw openen/bewerken. Een nog gewijzigde notitie wordt bewaard vóór overslaan, selectie-/schermwissel of checkpoint; bij onbevestigde opslag blijft de kaart staan met retry. Sluiten van het browservenster zonder bewaren/keuze is geen opslagbevestiging.

Beoordelingen zijn altijd **globaal over alle merken** opgeslagen. Een checkpoint is een bladwijzer voor selectie/ronde/positie; het draait recentere beoordelingen nooit terug. Nieuwe checkpoints leggen progressScope=all-products en de gekozen volgorde vast, met merk=all voor gemengde rondes. Oude merkspecifieke checkpoints blijven geldig. **Willekeurig verder** kiest nieuwe onbeoordeelde hoofdfoto's uit alle merken; al beoordeelde items worden overgeslagen, 'Later' kan later terugkomen. Specifieke afkeur/twijfelfilters zijn beschikbaar voor bewuste herbeoordeling.

De oorspronkelijke volledige catalogus blijft ongewijzigd. De reviewroute kan nu alle merken selecteren en stuurt per product alleen de hoofdfoto en een kort omschrijvingsuittreksel. Identiteiten blijven exact gelijk; Hotbath raw JSON daalt van17.275.825 naar9.868.512bytes, geen claim over gemeten telefoonlatentie.

De rustige interface heeft een kleine vaste dag/nachtknop rechtsboven. Alleen deze apparaatvoorkeur gebruikt localStorage (bc-qc-theme); geen beoordelingen/checkpoints naar browseropslag verplaatst. Foto's blijven ongefilterd op hun originele witte canvas voor kleurbeoordeling. Toegang blijft uitsluitend de bestaande eigenaar.

TypeScript, build en30API-/echte-SQLite-/selectiecontracttests zijn gecontroleerd. UI-voorkeur na herladen, notitieveld/snelle reden en320/390componentbreedtes zijn in lokale preview gecontroleerd. Hosted visitor-write en fysieke telefoon worden niet namens de eigenaar geclaimd. Lokale preview zonder visitoridentiteit schakelt schrijven zichtbaar uit. Tijdelijke QA-route niet publiceren.

Onderstaande QC-03/QC-02-delen zijn historische implementatiestappen. De optionele notities en globale willekeurige voortgang hierboven vervangen eerdere zinnen over geen foto-notities/merkgebonden rondes.


## Actuele aanpassing QC-03 — 30 oktober 2026

De fotocontrole toont uitsluitend de eerste bestaande foto per product (hoofdfoto in deze momentopname). De ongewijzigde bronimport heeft geen producten met een niet-afbeeldingsmedia-item vóór die eerste foto. Geen nieuwe import of Shopify-write.

Vier directe keuzes: **Ja, Nee, Twijfel, Technische tekening**. Geen foto-notitieveld, fototype-dropdown of hoofdfotogeschiktheids-dropdown meer. `lib/main-photo.ts` maakt het complete oordeel automatisch. Technische tekening bewaart `role=technical`, `main=no`, `status=wrong` en een vaste reden; geen goedkeuring als hoofdfoto. Deze classificatie blijft zichtbaar in de aanleverlijst en export. Productgegevens heeft zijn afzonderlijke checklist behouden.

Foto en volledige producttitel staan groter; titel boven de foto, zonder afkapping. Mobiel drie hoofdkeuzes met een aparte brede knop voor technische tekeningen. Eerdere reviews en hun auditgeschiedenis blijven behouden. Oude galerijcheckpoints worden bij hervatten gefilterd naar hoofdfoto’s met overeenkomstige positie; productcheckpoints blijven staan. Geen reset/migratie van beoordelingen nodig.

De hoofdfotoronde bevat **11.034 kaarten** (11.679 producten min645 zonder foto); Hotbath7.591 en Wiesbaden2.451. De volledige galerij blijft in de ongewijzigde bronwerkkopie; de reviewselectie kiest er één per product uit.

TypeScript en20 echte API-/SQLite-/selectiecontracttests geslaagd; hosted visitor-write en fysieke telefoon niet namens eigenaar geclaimd. De rest van dit document beschrijft de oorspronkelijke QC-02-basis; bovenstaande QC-03-interactie vervangt de oude fototype/notitie/galerijbediening.


Mobiele, afgeschermde reviewtool. Op verzoek van de eigenaar gebouwd naast de Shopify-webshop, in projecttak `quality-control`. Geen thema- of productwrites. Live ingang en definitieve teststatus staan in het bovenliggende QC-dossier in de BadkamerCity-repository.

## Gebruik

1. Meld aan met het ChatGPT-account van de eigenaar. Beoordelingen zijn eigenaarsgebonden en staan in D1; browseropslag is niet de bron.
2. Kies een merk, foto’s of productgegevens, en een batch van 25/50 kaarten. Cobber en Caral krijgen werkvolgordevoorrang op basis van hun huidige titel; dit is geen gecontroleerd serieattribuut of kwaliteitskeurmerk.
3. Foto: links = fout, rechts = klopt; knoppen bieden dezelfde acties. Twijfel en overslaan blijven beschikbaar. Je kunt vergroten, het soort afbeelding aangeven, hoofdfotogeschiktheid kiezen en noteren wat ontbreekt.
4. Product: controleer identiteit/uitvoering, specificaties, PDF, omschrijving en onderdelen. Een product kan alleen 'klopt' krijgen als elk onderdeel klopt of niet van toepassing is. Een ontbrekende PDF is niet voor elk type een fout.
5. Elke beoordeling wacht op serverbevestiging. Bij netwerkfouten blijft de kaart staan; herhaal dezelfde actie, niet een ander oordeel. Niet blind herladen bij onbevestigde opslag. Een verloren bevestiging is met dezelfde actie-id opnieuw opvraagbaar zolang de pagina openblijft. Na sluiten zijn onbevestigde acties niet gegarandeerd bewaard; bevestigde acties wel.
6. Maak een checkpoint met een eigen naam vóór stoppen. Het bewaart merk, controletype, batch-ID's en positie. Het is een bladwijzer, geen terugzetpunt voor oude beoordelingen. Een onopgeslagen kaartnotitie hoort er niet bij. Hervat via Checkpoints.
7. Aanleverlijst toont fout/twijfel, ongeschikte huidige hoofdfoto’s en producten zonder foto. Beoordelingen/checkpoints zijn als JSON te exporteren.

## Datacontract en bronnen

`data/catalogue.json` is een gedateerde read-only werkkopie van publiek zichtbare Shopify-productvelden en CDN-URL’s, geen tweede bronregister. Bestaande productregisters blijven leidend voor brononderzoek; bijvoorbeeld `docs/product-content/wiesbaden-register.json`, het uitvoeringsoverzicht van 21 oktober en de bestaande verrijkingsresultaten. Er worden geen historische kwaliteitsbeoordelingen uit die registers stil als nieuwe foto-goedkeuring geïmporteerd.

`data/import-summary.json` beschrijft de volledige gepagineerde inventaris, inclusief 645 Hotbath-producten zonder afbeelding. Alle opgenomen producten hadden op het bronmoment een `onlineStoreUrl`; die URL's zijn niet stuk voor stuk in de browser geopend. ACTIVE op zichzelf is onvoldoende. Varianten/media zijn op begrensde verbindingen gelezen; `hasNextPage` is gecontroleerd en alle huidige producten hebben complete media/variantverbindingen. Geen aankoop-, prijs- of voorraadtest.

De huidige merken worden volledig uit de bron gelezen, inclusief één bestaand publiek testartikel onder 'BadkamerCity Test'. Dit is een reviewgeval, geen automatische verwijderopdracht. Niet-actieve producten vallen buiten deze werkkopie.

`image:*` sleutels combineren product-/media-identiteit en een SHA-256-afgeleide van de bronidentiteit, SKU/uitvoering, productdatum, mediadatum en beeldvelden/URL. Productsleutels binden aan productidentiteit en brondatum. Dit is **geen hash van de gedownloade beeldbytes**. De 29k+ foto’s zijn niet massaal gekopieerd of automatisch inhoudelijk gekeurd. Hetzelfde URL-bestand dat zonder mediadatum-/URLwijziging wordt overschreven kan pas met een toekomstige byte-hashcontrole worden ontdekt. Een nieuwe import met gewijzigde sleutels hergebruikt oude goedkeuringen niet. Geen live synchronisatie gebouwd; een oordeel geldt voor deze momentopname, niet voor later stil gewijzigde Shopify-data.

Onafhankelijke fabrikantreferenties, gebruiksrechten, PVD/materiaal en compatibiliteit zijn niet door visueel swipen bewezen. Onbekend blijft twijfel.

## Opslag en beveiliging

- Vinext + Cloudflare D1 (`DB`); platform-private Site en ChatGPT-identiteit. Geen Shopify Admin-token, externe API-proxy of nieuwe authenticatiestack in de browser.
- `app/api/review/route.ts`: identiteit vereist op GET/POST, eigenaarfilter, same-origin POST, begrensde/geverifieerde invoer, whitelist van actuele items, optimistic revision, unieke action-id en geschiedenis per kaart. Undo schrijft een nieuwe historische versie.
- Checkpoints zijn onveranderlijke bladwijzers met unieke ID; dubbele verzending maakt geen tweede checkpoint. Geen delete-endpoint.
- Bij concurrente wijzigingen geeft de API 409; herladen haalt de actuele beoordelingen op. Niet automatisch overschrijven.
- `/api/catalogue` geeft alleen de publieke werkkopie; de volledige Site blijft afgeschermd door het platform. Beoordelingen en privénotities horen nooit in de publieke Git-repository.
- Drizzle-migraties zijn schema-only. Data zit niet in migraties. Nieuwe migraties toevoegen; eerder toegepaste bestanden niet herschrijven.

## Ontwikkeling en controle

Gebruik de Sites-skill voor openen, bouwen, verpakken en publiceren; behoud `project_id`, D1, Worker-authcontext en private toegang. De Sites-bronrepo verzorgt hosting; publieke reviewbare code wordt daarnaast naar `jlamping1997/badkamercity`, branch `quality-control`, map `quality-control/review-app` gespiegeld. Geen tweede kopie in documentbibliotheken nodig.

- Installeren: de Sites-helper `scripts/install-dependencies.mjs` uit de geïnstalleerde plugin.
- Typecheck: `node node_modules/typescript/bin/tsc --noEmit`.
- Betekenisvolle API-/SQLite-tests: `node scripts/test-qc.mjs`.
- Schemawijzigingen: `npm run db:generate`; alle nieuwe migraties opnemen.
- Bouwen: Sites `scripts/build-site.mjs`; dat levert ook D1/Wrangler-configuratie.
- Managed preview: `sites-preview start <checkout>`. Platform-identiteit is in de lokale managed preview niet automatisch aanwezig; de UI toont dan aanmelden en schakelt schrijfknoppen uit. Geen nepidentiteit als productiefallback.

De normalizer verwacht genegeerde `.sites-runtime/Hotbath.json`, `Wiesbaden.json` en `Others.json` met geautoriseerde Admin-queryresultaten (`nodes`, `pageInfo`), en weigert onvolledige paginering. Dit is een onderhoudsscript, geen willekeurige browser-upload of automatisch draaiende import. Ververs bij een nieuwe import alle merken en controleer volledige media/variantdekking. Querydocumentatie: https://shopify.dev/docs/api/admin-graphql/2026-07/queries/products .

## Open grenzen

Geen offline wachtrij, automatische Shopify-correctie, ranking, fabrikantbronophaalservice, periodieke synchronisatie of verificatie van alle originele fotobestanden. Telefoonhardware/swipegedrag moet met de eigenaar worden getest. Een geslaagde build/API-test bewijst geen succesvolle hosted aanmelding; rapporteer dat afzonderlijk in het QC-dossier.

## Publieke Git-spiegel

De publieke spiegel bevat geen volledige data/catalogue.json; herstel de complete private Sites-bronrepo van hetzelfde project of doe de gedocumenteerde read-only import vóór snapshot-test/build. data/import-summary.json bevat scope. Kopieer geen private D1-beoordelingen, notities of checkpoints naar Git.
