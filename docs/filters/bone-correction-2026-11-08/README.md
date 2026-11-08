# Bone bij tegels → Beige

8 november 2026. **APPLIED_VERIFIED / PUBLIC_API_VERIFIED.**

De nieuwste expliciete eigenaarcorrectie is: **Bone is Beige**. Deze regel geldt voor een exacte genormaliseerde bronkleur Bone bij bekende tegelcollecties. Zij heeft voorrang op de oudere Malaga/Bone → Wit-regel. De oorspronkelijke kleurnaam en specificaties blijven behouden. Samengestelde namen zoals Bone-acero en Bone/White vallen buiten deze gerichte correctie.

## Scope en controle

De private tegelmeting bevat 65 exacte Bone-producten: 12 Cottoceramix en 53 Porcelanosa. In de vorige Cotto-release waren er al 11 Beige. De upgrade verandert daarom 54 producten: 53 Porcelanosa van Overige kleuren naar Beige en één Cottoceramix/Malaga van Wit naar Beige. Alle 65 vallen daarna onder Beige.

**50 tests geslaagd**, inclusief echte private worker-, API- en catalogusfixtures, zonder overgeslagen integratietests. Alle andere kleuren en productvelden blijven gelijk, evenals de 202 genormaliseerde Cotto-regels (207 oorspronkelijke regels), alle 27 Acero-producten en de 132 formaatcodes. Van 47 producten onder eerdere eigenaarregels blijven er 46 gelijk; alleen de Malaga/Bone-uitzondering wordt bewust door de nieuwste instructie vervangen. De API-bron blijft byte voor byte gelijk. De standalone installer, ASCII-overdracht, hashcontrole en herhaalbeveiliging zijn ook onafhankelijk gecontroleerd.

Ten opzichte van de oorspronkelijke Acero-versie zijn Cotto plus Bone samen 407 kleurwijzigingen: 368 nieuw ingedeeld vanuit Overige kleuren en 39 bestaande classificaties gecorrigeerd. De Bone-upgrade herhaalt de Cotto-batch niet.

## Publieke meting vóór de Bone-correctie

De publieke API gebruikt inmiddels generatie `bc_sync_20261108t164313_f87c29`, 227 profielen. Binnen Cotto zijn 99 producten onder Overige kleuren gevonden; zoeken op Silver Mist met Grijs vindt 11 en Clear met Beige vindt twee. Dit past bij de reeds toegepaste Cotto-indelingen. Bone met Beige vindt daar nu 11; Bone met Wit nog één. Deze publieke meting is geen teruggelezen workerbron en geen eigenaar-installatierapport. De installer controleert de werkelijke bronhash op de VPS voordat iets wordt gewijzigd.

## Uitvoering

Gebruik de nieuwe `repair_bone_color.py` onder `scripts/filter-sync/simplification/bone/`, met de SHA256 uit `bone-color-release.json`. Vereiste bestaande worker: `cc13abd05c87a490bf06d0a7358ef36bc700edc0a736a48714d704df62f8dcc2`. Doelworker: `a8dd54597a2a372a7b0fcce9357a6bcc31a406fca2631cb9b24918f5fea0ff17`. De API blijft `3a7701134be7ac55b0a83436ceb16ebb19ac0a88aba17c283490f90047f02094`. Een afwijkende bron wordt niet overschreven.

De bewezen bestaande installatieprocedure bewaart slot, private back-up, volledige verse export, staging, indexreadback, activering, eigen wijzigingsherstel en timerafhandeling. De vijf bestaande vlaggen blijven verplicht; nieuw is `tile_bone_beige_v1` met `tile_bone_beige_products`. Op de huidige fixture is dat 65. Er zijn geen Shopify-productmutaties of themawijzigingen nodig. De laatst vers gelezen MAIN is `196354474250` (Eenduidige footer); dit thema is niet door deze taak aangepast.

Nieuwe serverstaging en Bone-activering zijn geslaagd; 240 servercontroles zijn goed en nul zijn fout. De publieke nacontrole bevestigt alle 65 verwachte Bone-producten onder Beige, ook in een nieuwere indexgeneratie. Het compacte Cotto-overzicht is bijgewerkt naar 208 kaarten, inclusief Malaga Bone → Beige. Het ontbrekende tegelformaatfilter in het Cottoceramix-merkprofiel en de 561 ontbrekende Cotto-kleurbronnen blijven apart vervolgwerk.

**Eén volgende handeling:** eigenaar test de live filters en noteert gerichte productcorrecties. Deze installatie is afgerond en hoeft niet opnieuw te worden uitgevoerd.

## Bevestigde uitvoering en publieke nacontrole

Eigenaaruitvoer: `applied_verified`, installatiegeneratie `bc_sync_20261108t165802_30078e`, 15.897 producten, 227 profielen, 240 GOED en nul FOUT. De worker- en API-hashes komen overeen met het manifest. Alle zes vlaggen zijn true: `variant_aliases_v1`, `filter_simplification_v1`, `tile_format_codes_v1`, `acero_gray_v1`, `cotto_visual_colors_v1` en `tile_bone_beige_v1`. De tellers bevestigen respectievelijk 27 Acero-, 353 Cotto- en 65 Bone-producten. Back-up `/opt/badkamercity/filter-sync/filter-simplification-backups/20261108T165801-51a38f`; rapport `/opt/badkamercity/filter-sync/runs/20261108T165802_30078e/RESULTAAT.json`. Timer volgens eigenaaruitvoer hervat. De volledige uitvoer blijft privé; bron-SHA256 `6ae17b93992c592047f29eb1cc87211c7e76bb28f38a20f5b62a9446d8ef014d`.

De assistent controleerde daarna de publieke API op de nieuwere generatie `bc_sync_20261108t170044_7f6504`. Precies de 65 verwachte Bone-product-ID's staan onder Beige: 12 Cotto en 53 Porcelanosa. Nul van deze ID's staat onder Wit of Overige kleuren. Cotto Overige blijft 99, Acero onder Grijs blijft 27 en 60 × 60 geeft 159 producten. De oorspronkelijke Bone-namen blijven in de titels aanwezig. De generatie bleef stabiel tijdens deze nacontrole.

De nieuwere index bewijst dat de correctie ook na de eerste installatiegeneratie behouden is. De oorzaak van die verversing is niet via systemd teruggelezen. Dit is een API-controle; een nieuwe browser-, mobiele of rebootproef is niet uitgevoerd. MAIN bleef bij de controle `196354474250`; geen thema- of Shopify-productmutaties door deze taak.
