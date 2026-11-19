# Gunmetal, aanbevolen volgorde en spiegelmaten

10 november 2026. **SERVER_PACKAGE_PREPARED / NOT_DEPLOYED**. Dit is één gezamenlijke update van de bestaande filterworker, met een volledige nieuwe index en controles vóór activering. Geen nieuwe filterservice of losse frontend-schijncorrectie.

## Functie

1. Gunmetal, Gun metal, Gun-metal en bijbehorende afwerkingen krijgen de eigen basiskleur **Gunmetal**. Grijs en Verouderd ijzer blijven eigen bestaande grijze keuzes; echte samengestelde kleurwaarden houden meerdere groepen. Exacte fabrikantkleuren en Shopify-specificaties blijven behouden.
2. Aanbevolen krijgt een stabiele afwisseling tussen merk, producttype en serie. Eerst producten met een afbeeldings-URL, vervolgens completere beschikbare filter-/SKU-data. Binnen iedere ronde een artikel per groep; daarna de volgende uitvoeringen. Gelijke scores krijgen een vaste hashvolgorde. Geen willekeur per paginabezoek, geen verlies of duplicatie tussen pagina’s en geen onbewezen bestsellerlabel. Prijskeuzes blijven de bestaande expliciete prijssortering gebruiken; tekstzoeken houdt tekstmatch als eerste relevantiesignaal.
3. De index moet Cinto 38.4177 als 600 mm en 38.4178 als 800 mm inlezen. De twee broncorrecties staan al gecontroleerd in Shopify; bij 30 mm in de nieuwe index stopt de release vóór activering.

Een beeld-URL is een compleetheidssignaal, geen bewijs dat iedere foto inhoudelijk is gecontroleerd. De groepen voor afwisseling zijn merk/type/serie, niet nieuw vastgestelde technische keuzefamilies. Er is geen verkoop-/reviewscore gebruikt of verzonnen. Bij later beschikbare verkoopdata kan een afzonderlijk, gemeten populariteitssignaal worden toegevoegd.

## Kleine echte nulmeting

Publieke API /badgrepen: 12 producten, Grijs=2; alias Geborsteld gunmetal PVD wijst expliciet naar Grijs. Dat is de oorzaak van de gemelde kleurindeling. Het nieuwe thema heeft al een herkenbare Gunmetal-gradient, maar toont geen verzonnen aparte facet zolang de server die nog niet levert.

De opgegeven 30mm-spiegelrange gaf exact twee Cinto-producten, SKU38.4177 en38.4178. Officiële fabrikant beschrijft 3 cm als bandbreedte, met een spiegeldiameter van60/80cm. [Admin-herstel en bronlinks](../../repairs/2026-11-10/catalog-ux/README.md).

## Release en werking

Bron: `scripts/filter-sync/simplification/gunmetal/`. De builder bundelt alleen de openbare beoordeelde patch en de bestaande openbare tile-look lifecycle; geen private servercode, credentials of catalogus. De geïnstalleerde worker moet exact SHA256 `79f676d035fdd6d250e2daec51b886d1aa54c117707718d7ea9695300c21c43d` hebben; de API exact `3a7701134be7ac55b0a83436ceb16ebb19ac0a88aba17c283490f90047f02094`. Andere code wordt niet overschreven.

De patch is een deterministische invoeging met één gecontroleerde schemahook. De doelhash wordt berekend uit de exact geverifieerde geïnstalleerde bron. Bij herhaling moet het verwijderen van precies die invoeging en hook weer de oorspronkelijke toegestane hash opleveren. Een latere andere wijziging wordt dus niet als deze release geaccepteerd. De API-bron blijft byte-identiek.

De bestaande lock, private herstelkopie, timerpauze/-herstel, geïsoleerde stagingindex, volledige index-/productsetcontrole, API-activering en herstel van alleen de eigen generatie blijven intact. De acht bestaande filterlagen inclusief tegeluitstraling zijn verplicht. De nieuwe index moet Gunmetal-, aanbevolen-volgorde- en Cinto-vlaggen bevatten. Niet geslaagde checks blokkeren succes/activering; bij herstelonzekerheid wordt expliciet handmatige controle gemeld.

De sortering gebruikt een intern int32-rangveld en Typesense default_sorting_field. Geen openbaar filterveld of gewijzigde API-parameter. Referentie: [Typesense collections](https://typesense.org/docs/30.2/api/collections.html), [search sorting](https://typesense.org/docs/26.0/api/search.html).

## Tests en grenzen

- 25 nieuwe geïsoleerde tests PASS: Gunmetalvarianten en niet-Gunmetalpariteit, multi-kleur, bronbehoud, schemahook, onbekende/gewijzigde code blokkeren, herhaling, stabiele mix, beeld-/datacompleetheid, afwisseling, unieke paginering en Cinto-/snapshotgates.
- 55 bestaande ongewijzigde lifecycle-mocktests PASS: herstel, tijdslimiet, handmatige wijzigingen, timer en bronbescherming.
- Python-syntaxis en zelfstandige bundle gecontroleerd. Geen integratietest met de private volledige worker of echte Typesense vanuit deze omgeving. De installer moet die echte staging-/readback-/lokale en publieke API-proeven nog op de VPS uitvoeren. Dit is geen ‘live opgelost’-claim.
- De nieuwe controle vergelijkt pagina1/2 van de aanbevolen volgorde in meerdere scopes, afzonderlijke Gunmetal-/Grijs-selectie, aliasselectie, bestaande tegeluitstralingen en de twee spiegelranges.

SSH vanaf deze omgeving: Network is unreachable. Er is geen serverwrite uitgevoerd en er is geen nieuwe index geactiveerd.

## Installeren

Gebruik het vastgepinde commando in [INSTALL.md](INSTALL.md). Installerhash staat ook in `gunmetal-release.json`. Geen oude kleur- of uitstralinginstaller herhalen. Het pakket is niet alleen een themawijziging; het vernieuwt de filterindex en bewaart de nieuwe worker voor volgende synchronisaties.

Succes pas aannemen bij eindstatus `applied_verified` plus `gunmetal_v1`, `recommendations_v1` en `cinto_widths_v1` true. Bij een `scheduler_pending`-status is de timer niet vrijgegeven. Deel de volledige uitvoer; daarna volgen publieke nacontrole en echte filter-/pagineringproeven. De gunmetal-facet is niet alleen door publicatie van het thema te activeren.

Herstelgegevens blijven privé onder `/opt/badkamercity/filter-sync/filter-simplification-backups/`. Een oude index wordt niet vooraf verwijderd. Handmatig terugzetten alleen op basis van de vastgelegde eigen generatie en codehash; geen oudere brede reparatie herhalen over nieuwe wijzigingen.

**Volgende handeling:** eigenaar voert het vastgepinde pakket uit en deelt de uitvoer. De themafeature staat apart in [het bestaande concept](../../repairs/2026-11-10/catalog-ux/README.md).
