# Tegeluitstraling — standalone filteraanvulling

**Lokaal releaseklaar; niet op de VPS uitgevoerd.** De eigenaar moet de vastgepinde standalone via zijn bestaande PowerShell/SSH-route uitvoeren nadat de Shopify-categorisering voltooid is. De gecontroleerde publicatiepin staat in `publication.json`; de standalone op dat checkpoint is exact teruggelezen.

## Bron en scope

De installer bevat uitsluitend de kleine publieke workerpatch. Hij leest het bestaande `tiles.look`-bronveld bij een **volledige verse Shopify-export** en maakt `f_tegel_uitstraling` als gesloten generiek checkboxfilter. De huidige API blijft byte voor byte gelijk, net als de themacode. Er zijn geen product-, tag-, collectie-, prijs-, voorraad- of andere Shopify-writes in dit pakket en er is geen catalogus of product-ID-lijst ingebed.

De tien vaste keuzes zijn Steenlook, Marmerlook, Houtlook, Betonlook, Metaallook, Terrazzo, Effen, Decoratief, Handvormlook en Terracottalook. Alleen exacte genormaliseerde waarden uit `tiles.look` tellen; onbekende en lege bronnen blijven leeg. Bestaande Terrazzolook/Design/Patroontegels-aliases blijven bruikbaar als Terrazzo/Decoratief. Zelligelook wordt Handvormlook.

Het bestaande Cottoceramix-profiel blijft `general` en krijgt uitsluitend de gesloten lookkeuze bij voldoende variatie. Het uitgestelde formaatfilter wordt niet toegevoegd. Een profiel met slechts één look krijgt geen betekenisloze zichtbare keuze, maar behoudt de keuzemogelijkheid in zijn API-contract. De eerdere maat-/kleurkeuzes en maximaal twee geopende groepen blijven behouden.

## Bewaakte uitvoering

1. Vereist exact de ecfc-basisworker, exact API3a en alle zeven bestaande snapshotvlaggen; bij afwijking stopt het pakket vóór timer/workerwijzigingen. Een oudere index zonder die vlaggen is geen ondersteunde upgradebasis.
2. Een al correct toegepaste targetworker wordt alleen geaccepteerd met alle acht vlaggen, een consistent lookprofiel/bronregister en passende lokale health. Er wordt dan geen nieuwe index gebouwd.
3. Neemt het bestaande synchronisatieslot, controleert de code opnieuw en pauzeert alleen een eerder actieve ververstimer.
4. Maakt een private `0700`-back-up van code, active.json en hersteladministratie. De volledige private code staat alleen op de VPS/in lokale privéfixtures.
5. Exporteert alle actuele gepubliceerde producten, normaliseert `tiles.look`, bouwt een nieuwe index en leest ieder productdocument volledig terug. Huidige productaantallen of looktotalen zijn nergens als upgradevoorwaarde bevroren.
6. Controleert bronherkomst, exacte look-ID-selecties, OF-selectie, kleur/formaat-combinaties en facetaantallen. Bestaande alias-, kleur-, formaat-, prijs-, variant- en categoriechecks blijven actief. De staged snapshot vereist alle acht vlaggen.
7. Activeert pas na succesvolle staging; controleert daarna de bestaande liveproeven plus lokale/publieke lookprofielen en alle tien dynamisch berekende keuzetellingen. Nul-resultaat voor onbekende look is onderdeel van de controle.
8. Vergelijkt direct vóór workeropslag de actieve snapshot byte voor byte met de vóór activering vastgelegde kandidaat. Een tussentijdse menselijke indexswap blijft behouden en wordt niet als geslaagde installatie gemeld.
9. Slaat de nieuwe worker pas op na de gecontroleerde activering en exacte readbacks. Herstelt bij fouten uitsluitend de eigen generatie/transactie, bewaart vreemde handmatige wijzigingen en herstelt de oorspronkelijke timerstatus.

Deadline: 900 seconden; aparte herstelgrens: 240 seconden. Onderbrekingen, gesloten SSH-uitvoer en bekende secrets worden volgens de eerdere lifecycle afgehandeld. Een mislukte timerhervatting wordt afzonderlijk als `applied_scheduler_pending` gerapporteerd, met behouden actieve index en worker.

## Bestandset

- `apply_tile_look_filter.py` — lifecycletemplate met aanvullende bron-, profiel-, vlag- en livecontroles.
- `build_tile_look_filter.py` — deterministische bundelaar; leest private fixtures maar embedt die niet.
- `repair_tile_look_filter.py` — complete ASCII-standalone voor de eigenaar.
- `tile-look-release.json` — alle transport-/runtimehashes en acht vereiste vlaggen.
- `test_apply_tile_look_filter.py` — 55 lifecycle-/bron-/vlagcontroles.
- `test_tile_look_bundle.py` — tien bundel-, echte snapshotcontract- en routeadaptercontroles.
- `protocol-verification.json` — geaggregeerd lokaal bewijs en onafhankelijke review.

De kleine bronpatch en 26 bijbehorende workertests staan naast dit dossier in `../worker/`. De bestanden `private-base-sync.py`, `private-candidate-sync.py` en `private-current-app.py` zijn uitsluitend lokale privéfixtures en mogen niet worden gepubliceerd.

## Bewijs en grenzen

**91 tests PASS, nul skips:** 26 workercontroles en 65 releasecontroles. De 42 oude lifecyclegevallen zijn behouden; het oude legacy-zonder-snapshot-geval is bewust een preflightweigering geworden omdat zeven bestaande lagen vereist zijn. De extra gevallen dekken de achtste vlag, dynamische dekking, gesloten profielen, publieke/lokale lookchecks en behoud van een menselijke snapshotwissel. Onafhankelijke review bevestigt dezelfde suites, ASCII-transport, verse rebuild en hashes zonder verdere blokkades.

De echte vóór-meting met 3.496 productidentiteiten bevestigt behoud van alle bestaande kleuren en 132 formaatcodes. De 358 bestaande lookbronnen worden genormaliseerd, de 3.138 destijds lege bronnen blijven leeg; deze telling is **testbewijs**, geen vastgelegde runtimeverwachting. De installer leest de later door de eigenaar aangevulde Shopify-data vers uit. De catalogusregressie gebruikt vaste fixtureprijzen als vergelijkingswaarden en is geen nieuwe liveprijsmeting.

Geen echte VPS-staging, nieuwe installatie, browser- of telefoonproef is uitgevoerd. De 143 resterende kleurloze tegels en het Cotto-formaatprofiel blijven expliciet uitgesteld; deze lookaanvulling lost die punten niet op.

Uitgevoerde testcommando's in de private bewijswerkmap (de benodigde fixtures worden niet meegepubliceerd):

```bash
python -m unittest discover -s tile-look-20261109/worker -p 'test_tile_look_worker_patch.py' -v
python -m unittest discover -s tile-look-20261109/release -p 'test_*.py' -v
```

De manifesthash is leidend voor het uiteindelijke PowerShell-blok. Na uitvoering moet de ownerlog worden gelezen en de publieke lookprofielen opnieuw worden gecontroleerd; een lokaal geslaagde build is geen live installatiebewijs.
