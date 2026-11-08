# Verdere tegelkleuren en ontbrekende kleurfilters

8 november 2026. **READY_FOR_OWNER_EXECUTION; nog niet live.** De eigenaar heeft gevraagd om verder te gaan met duidelijke basiskleuren, zonder nieuwe bevestigingen voor iedere keuze.

## Wat deze batch toevoegt

De volledige private meting van 3.496 gepubliceerde tegels geeft na voorbereiding exact 573 nieuwe kleurindelingen:

| Onderdeel | Producten | Herkomst |
| --- | ---: | --- |
| Resterende bekende bronkleuren | 155 | 102 visueel beoordeelde serie/kleurcombinaties: 99 Cotto- en 56 Porcelanosa-producten |
| Ontbrekende kleurfilters met leveranciersbron | 353 | Officiële Cotto-artikellijst november 2026, kolom BMN Kleurgroep, gekoppeld aan actuele variant-SKU's |
| Extra ontbrekende kleurfilters | 65 | Expliciete kleurwoorden in exact vastgepinde titels, met representatieve productstalen gecontroleerd |

Binnen de huidige tegelmeting daalt Overige kleuren van 155 naar nul. De 561 producten zonder bruikbaar kleurfilter worden er 143. Daarmee hebben 3.353 van de 3.496 tegels een basiskleur; dit betreft filterdekking, geen nieuwe fabrikantkleuren in Shopify-specificaties.

## Bewijs voor bronherstel

Voor alle 561 bronlege Cotto-producten zijn de actuele titel, handle, enige variant-SKU en foto-URL opnieuw uit Shopify gelezen: geen titel- of handledrift, geen varianten met afgebroken paginering. Alle 353 leverancierskoppelingen gebruiken de werkelijk gelezen SKU. Ook alle gesorteerde maatparen komen overeen. 281 omschrijvingen komen na normalisatie exact overeen; 72 kleine verschillen in verpakking, diktesuffix, setvermelding of schrijfwijze zijn afzonderlijk beoordeeld.

Bron: [officiële Cotto-cataloguspagina](https://cottoceramix.nl/i/catalogus.html), download van de artikellijst november 2026, werkblad Basis lijst, kolom BMN Kleurgroep. Bron-SHA256 `e65d374f4a5b7db13a4fd979615f3de90cb3981b3019d7f8ff56879d0aa27208`. De fabrikantkleurnaam is slechts bij 80 van deze 353 artikelen gevuld; deze release verzint daarom geen fabrikantkleurnaam. Het oorspronkelijke lege kleurveld blijft in de index herkenbaar als lege `f_kleur_exact`.

De 65 extra titelgevallen zijn een finite, gecontroleerde lijst; er komt geen algemene vrije titelclassifier. Ondoorzichtige persoons- en patroonnamen worden niet blind vertaald naar kleuren. Veertien representatieve productstalen zijn bekeken. Drie gemengde La Madeleine-patronen krijgen naast Multicolor ook de expliciete en visueel bevestigde Bruin-, Blauw- of Grijs-keuze.

## Bewaakte scope en tests

**63 tests geslaagd**, inclusief echte private worker-, API-, catalogus- en actuele variantfixtures; geen overgeslagen integratietests. Een onafhankelijke review bevestigt hetzelfde resultaat.

Nieuwe bronkleurregels vereisen merk, tegelcontext, één expliciet serieveld en een exacte genormaliseerde bronkleur. De eerdere eigenaarregels, Bone → Beige, Acero → Grijs en de eerdere Cotto-regels blijven voorrang houden.

Een ontbrekende kleur wordt uitsluitend aangevuld bij een lege oorspronkelijke kleur, de juiste leverancier en tegelcontext, exact de vastgelegde handle en titel-SHA256, precies de ene goedgekeurde SKU-alias en geen prijsvariërende variantfamilie. Een inmiddels ingevulde bronkleur, gewijzigde titel, nieuwe SKU of nieuwe variantfamilie wordt niet overschreven. Herkomst wordt alleen in de private generatie-snapshot vastgelegd als OFFICIAL_COTTO_BMN of TITLE_EXPLICIT_COLOR. De publieke payloads bevatten uitsluitend de benodigde regels, geen product-ID-export, prijzen of voorraad.

Prijzen, afbeeldingen, andere documentvelden, alle 202 eerdere Cotto-sleutels, 353 eerdere Cotto-producten, 27 Acero-bronproducten, 65 Bone-bronproducten en 132 formaatcodes blijven gelijk. De volledige API-bron blijft byte voor byte gelijk. De vier extra bronlege producten met Bone in de titel krijgen nu eveneens Beige; de publieke tekstzoekopdracht kan daardoor 69 Bone-resultaten geven, terwijl de bestaande exacte Bone-bronregel correct 65 blijft tellen.

## Uitvoering en volgende handeling

Code staat onder `scripts/filter-sync/simplification/more-tile-colors/` op de bestaande actieve branch. Gebruik `repair_more_tile_colors.py` met de SHA256 uit `more-color-release.json`. Vereiste bestaande worker: `a8dd54597a2a372a7b0fcce9357a6bcc31a406fca2631cb9b24918f5fea0ff17`. Doelworker: `ecfc142a4fb15e66df297ec20884826be1bd4e8c491fb20bdb3e17cc281ba69a`. API blijft `3a7701134be7ac55b0a83436ceb16ebb19ac0a88aba17c283490f90047f02094`.

De installer behoudt de bestaande private back-up, synchronisatieslot, volledige verse export, gecontroleerde staging, indexreadback, activering, timerafhandeling en herstel van uitsluitend de eigen wijziging. Alle zes eerdere vlaggen blijven verplicht; nieuw is `more_tile_colors_v1`. Een afwijkende actuele worker of API stopt zonder overschrijven. Er zijn geen Shopify-productmutaties of themawijzigingen nodig.

Echte serverstaging, nieuwe activatie en publieke nacontrole voor deze batch zijn **nog niet uitgevoerd**. Het ontbrekende tegelformaatfilter in het Cottoceramix-merkprofiel blijft apart vervolgwerk. Het compacte foto-overzicht toont alleen deze nieuwe aanvulling en verandert het eerdere live overzicht niet.

**Eén volgende handeling:** eigenaar voert uitsluitend het nieuwe vastgepinde installatieblok uit en deelt de volledige uitvoer; daarna publieke nacontrole. Oudere kleurinstallers niet opnieuw uitvoeren.
