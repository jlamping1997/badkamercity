# Verdere tegelkleuren en ontbrekende kleurfilters

> **9 november 2026 — vervolgkeuze eigenaar:** de 143 ontbrekende basiskleuren en het Cotto-merkformaatfilter zijn expliciet **DEFERRED**. De kleurrelease blijft live; geen nieuwe kleurwijzigingen in TILE-LOOK-01. De uitstralingindeling is inmiddels in Shopify toegepast. Zie [de huidige lookoverdracht](../tile-look-2026-11-09/README.md) voor het nog uit te voeren filterpakket.

9 november 2026. **APPLIED_VERIFIED / PUBLIC_API_VERIFIED.** Voorbereid op 8 november, door de eigenaar geïnstalleerd en publiek nagecontroleerd op 9 november. De eigenaar heeft gevraagd om verder te gaan met duidelijke basiskleuren, zonder nieuwe bevestigingen voor iedere keuze.

## Wat deze batch toevoegt

De volledige private meting van 3.496 gepubliceerde tegels geeft na installatie exact 573 nieuwe kleurindelingen:

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

## Uitvoering en vervolg

De eigenaar gebruikte de vastgepinde code `ad1ace3bb9b45ef23eaf7c619435e59893c51fcb` onder `scripts/filter-sync/simplification/more-tile-colors/`, met installer-SHA256 `006e1f4e77f9f474076e11b8aea48cbac933d04c5e8444c96a92085de527159c`. De vereiste bestaande worker was: `a8dd54597a2a372a7b0fcce9357a6bcc31a406fca2631cb9b24918f5fea0ff17`. Geïnstalleerde worker: `ecfc142a4fb15e66df297ec20884826be1bd4e8c491fb20bdb3e17cc281ba69a`. API blijft `3a7701134be7ac55b0a83436ceb16ebb19ac0a88aba17c283490f90047f02094`.

De installer behoudt de bestaande private back-up, synchronisatieslot, volledige verse export, gecontroleerde staging, indexreadback, activering, timerafhandeling en herstel van uitsluitend de eigen wijziging. Alle zes eerdere vlaggen blijven verplicht; nieuw is `more_tile_colors_v1`. Een afwijkende actuele worker of API stopt zonder overschrijven. Er zijn geen Shopify-productmutaties of themawijzigingen nodig.

De eigenaaruitvoer bevestigt **242 GOED, nul FOUT**, `applied_verified`, 15.897 producten en 227 profielen. Alle zeven vereiste vlaggen zijn true. De geïnstalleerde hashes komen overeen met de release. Installatiegeneratie: `bc_sync_20261109t085106_9d0429`. Private back-up: `/opt/badkamercity/filter-sync/filter-simplification-backups/20261109T085105-4ed22e`. Serverrapport: `/opt/badkamercity/filter-sync/runs/20261109T085106_9d0429/RESULTAAT.json`. De timer is volgens de eigenaaruitvoer hervat. Volledige indexreadback, prijzen/beelden, lokale en publieke routechecks zijn onderdeel van dat serverlog; de hashes en snapshotvlaggen zijn niet via de publieke API apart uitgelezen.

## Onafhankelijke publieke nacontrole — 9 november 2026

Alle 3.496 tegel-ID's en alle 17 volledig gepagineerde kleurproductsets komen overeen met de verwachte worker, inclusief de 573 nieuwe doelen. Er zijn 3.353 producten met basiskleur en 143 zonder; Overige kleuren geeft nul. Cotto bevat 3.159 producten met 95,47% kleurdekking. De exacte Bone-bronset van 65 producten staat onder Beige en de Acero-bronset van 27 onder Grijs. Alle 132 formaatkeuzes blijven aanwezig: 60 × 60 geeft 159, 60 × 120 geeft 58, 60 × 150 geeft 92; hun OF-selectie is exact de disjuncte unie van 309 producten.

Tijdens het meetvenster verschoof de generatie van `bc_sync_20261109t085106_9d0429` naar `bc_sync_20261109t090044_ed9be2`. Alle data- en lidmaatschapsasserties slaagden; uitsluitend de afsluitende gelijkheid van de health-generatie faalde. Dit is daarom **PASS_DATA_CHECKS_GENERATION_CHANGED**, geen atomisch bewijs dat alle verzoeken dezelfde generatie lazen. Een beperkte eindcontrole op de nieuwere generatie bevestigt opnieuw 3.496 tegels, 95,91% kleurdekking, 132 formaten en nul Overige. De aanleiding van de verversing is niet via systemd vastgesteld. Zie [geaggregeerd publiek bewijs](public-verification-2026-11-09.json) en [server-/releasebewijs](verification.json).

Geen nieuwe browser-, mobiele, checkout- of rebootproef uitgevoerd. De oorspronkelijke gedetailleerde private ID-dump werd niet geserialiseerd doordat de eindassert stopte; de voorafgaande volledige data-asserties zijn wel voltooid. De teller voor 65 oorspronkelijke Bone-producten blijft onderscheiden van vier nieuwe bronlege producten met Bone in de titel.

Het compacte foto-overzicht is in dezelfde bestaande identiteit bijgewerkt naar live status; de 520 foto's/regels blijven behouden. Het eerdere Cotto-overzicht is niet gewijzigd. Shopify MAIN is read-only opnieuw bevestigd als 196368531722 — BadkamerCity - Hele europrijzen 8 nov. Er is geen thema-, product- of instellingenwrite gedaan. De lokale containerrepo is schoon op de bestaande branch maar is een ouder checkpoint; geen claim over de Windows-pc of lokale Codex-wrappers.

**Niet opnieuw installeren. Eén volgende handeling binnen dit dossier:** eigenaar loopt de live kleurfilters praktisch door en noteert concrete productcorrecties. De 143 nog kleurloze artikelen en het ontbrekende tegelformaatfilter in het Cottoceramix-merkprofiel blijven afzonderlijk vervolgwerk; overige werkstromen en holds blijven behouden.
