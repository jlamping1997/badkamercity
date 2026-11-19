# Uitstralingfilter — geteste kandidaat, niet geïnstalleerd

Deze afgebakende patch leest het bestaande Shopify-productveld `tiles.look` en voegt een optioneel `f_tegel_uitstraling`-facet toe. De huidige API en generieke themaweergave blijven byte voor byte gelijk. Dit is geen serverrelease of Shopify-mutatie.

## Inhoud

- `tile_look_worker_patch.py`: hashguarded transform voor uitsluitend worker `ecfc142a4fb15e66df297ec20884826be1bd4e8c491fb20bdb3e17cc281ba69a`; geen volledige private runtime in dit bestand.
- `test_tile_look_worker_patch.py`: 26 lokale controles zonder netwerk of write naar Shopify/VPS.
- `candidate-verification.json`: aggregate bewijs en kandidaat-hash.

## Gedrag

De voorlopige vaste woordenlijst is Steenlook, Marmerlook, Houtlook, Betonlook, Metaallook, Terrazzo, Effen, Decoratief, Handvormlook en Terracottalook. De patchfunctie accepteert een expliciete `taxonomy` en `aliases`-configuratie. Alleen exacte genormaliseerde bronwaarden tellen; er is geen vrije titel-, foto- of serieclassifier. Onbekende of lege bronwaarden blijven zonder lookfilter. Zellige/Zelligelook valt onder Handvormlook; Terrazzolook wordt Terrazzo; Design en Patroontegels worden Decoratief.

Alle bestaande productvelden en collectielidmaatschappen blijven behouden. Een niet-tegel krijgt geen lookveld. Uitstraling is een gesloten checkboxgroep op tegelprofielen en het bestaande algemene Cottoceramix-profiel, alleen wanneer er ten minste twee verschillende keuzes zijn. Een singleton-keuze blijft technisch toegestaan voor expliciete links, maar krijgt geen betekenisloos zichtbaar keuzelijstje. Maximaal twee eerder geopende groepen blijven behouden. Cottoceramix blijft `general`; het uitgestelde formaatfilter wordt niet toegevoegd.

De worker krijgt gecontroleerde wrappers voor exportquery, schema, definities, normalisatie, filter-UI, profielen, snapshot, profielchecks en stage-testcases. De nieuwe vlag is `tile_looks_v1`. De zeven vorige vlaggen blijven vereist. De latere installer moet die acht vlaggen en de definitieve workerhash controleren voordat activering als voltooid geldt.

## Bewijs en grenzen

26 tests slagen zonder skips. Een onafhankelijke read-only review bevestigt dezelfde 26 tests, correcte exportescaping met precies één extra alias en geen blokkade voor deze begrensde kandidaat. Twaalf gevarieerde brongevallen plus twee negatieve producten controleren legacy-aliases, onbekende waarden, titelwoorden en niet-tegels. De echte 3.496 productidentiteiten en huidige bronvelden zijn daarnaast vergeleken: alle bestaande documentvelden blijven identiek, de 358 bestaande lookwaarden worden bruikbaar genormaliseerd, de 3.138 lege bronvelden blijven leeg. De 3.353 kleurindelingen, 143 kleurloze producten, 27 Acero-, 65 Bone-, 353 eerdere Cotto-, 155 extra scoped- en 418 kleurherstelproducten blijven gelijk. Alle 132 formaatcodes blijven behouden, inclusief 159/58/92 voor 60×60/60×120/60×150.

De volledige catalogusproef gebruikt actuele identiteit/bronvelden en vaste **fixtureprijzen**; dit bewijst behoud tussen beide workers en is geen nieuwe actuele prijsmeting. De private broncatalogus wordt niet gepubliceerd. Er zijn geen serverstaging-, browser- of nieuwe installatiechecks uitgevoerd.

Test vanuit de projectwerkmap:

```bash
python -m unittest discover -s tile-look-20261109/worker -p 'test_tile_look_worker_patch.py' -v
```

De test vereist expliciete private fixtures. Bij andere paden: `BC_TILE_LOOK_BASE_SOURCE` en `BC_TILE_LOOK_API_SOURCE`. De actuele look- en kleurcatalogusfixtures horen bij de vastgelegde hash in het verificatiebestand; bewaar de vóór-meting als bron in plaats van die na de nieuwe indeling te overschrijven.
