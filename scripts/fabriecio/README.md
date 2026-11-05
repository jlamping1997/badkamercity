# Fabriecio productkeuzes

Deze hulpmiddelen lezen de echte gekoppelde keuzemenu's van Fabriecio en maken een controleerbaar plan voor bestaande Shopify-producten. De scripts importeren geen producten en schrijven niets naar Shopify. Zij regelen geen periodieke voorraadsynchronisatie.

De bron is de openbare productsitemap en de productpagina's van `fabriecio.nl`. Iedere koppeling volgt een daadwerkelijk waargenomen productlink. De koppelsleutel naar Shopify is het exacte artikelnummer/SKU, met gecontroleerde vendor en één artikel per product. Er worden geen groepen of combinaties uit productnamen verzonnen.

## Installeren

Voer de opdrachten uit vanuit de repositoryroot op de bestaande codebranch. Getest met Python 3.12.14, lxml 6.1.1 en aiohttp 3.14.4. De JavaScript-controles hergebruiken de bestaande vastgelegde Happy DOM- en LiquidJS-versies onder `scripts/component-audit/`.

```sh
python3 -m pip install -r scripts/fabriecio/requirements.txt
npm ci --prefix scripts/component-audit
```

Op Windows kan `python` worden gebruikt wanneer dat de geïnstalleerde Python 3-opdracht is. Een uitvoering op de Windows-pc is niet geclaimd.

## Bron verzamelen en hervatten

Kies een privéwerkmap buiten deze openbare repository. Onderstaand voorbeeld gebruikt een naastgelegen map. Gebruik dezelfde map om een onderbroken verzameling te hervatten.

```sh
python3 scripts/fabriecio/collect_choices.py --work-dir ../fabriecio-private --workers 6
```

De collector bewaart de sitemap, HTML-cache, geparste bronrecords, voortgang en `normalized-catalog.json` in die werkmap. Het eindrapport vermeldt ontbrekende SKU's, onopgeloste bestemmingen, dubbele combinaties en inconsistente menudimensies.

Opnieuw ontleden van bestaande HTML zonder alle productpagina's opnieuw te downloaden:

```sh
python3 scripts/fabriecio/collect_choices.py --work-dir ../fabriecio-private --reparse
```

Gebruik `--force` alleen voor een bewust nieuwe broncapture. Standaard worden bestaande cachebestanden hergebruikt; een hervatting is daarom geen bewijs dat alle broninformatie opnieuw actueel is opgehaald. De publieke B2B Store API wordt uitsluitend gebruikt wanneer een SKU op de exacte product-URL ontbreekt; er worden geen accountsessies of opgeslagen aanmeldgegevens gebruikt.

## Shopify-koppeling voorbereiden

Leg eerst een verse read-only Shopify-inventaris vast als privébestand. `builder.py` verwacht een array met bestaande producten, ieder met `id`, `handle`, `title`, `vendor`, `status`, `variants.nodes` met exact één `sku`, en optioneel `featuredMedia.preview.image.url`. De uitvoeringssessie die Admin-toegang heeft is verantwoordelijk voor deze inventaris en voor de controle op tussentijdse wijzigingen.

```sh
python3 scripts/fabriecio/builder.py --source ../fabriecio-private/normalized-catalog.json --shopify ../fabriecio-private/catalogue.json --output ../fabriecio-private/plan.json
```

Het plan bevat `updates`, `holds`, `warnings`, `skipped` en een getelde samenvatting. Alleen `ACTIVE` Fabriecio-producten met een ondubbelzinnige bestaande artikelidentiteit zijn schrijfbaar. Gearchiveerde producten blijven buiten de uitvoer en buiten de actieve productbestemmingen. Een ontbrekende of dubbele bron-/Shopify-identiteit wordt niet geraden.

Een menu-payload bevat de huidige productbestemming en de rechtstreeks door de bron aangeboden tegenhangers. Iedere klik opent de echte Shopify-product-URL; het bestemmingsartikel levert zijn eigen menu, prijs, foto's en overige gegevens. Deze lokale buurten voorkomen een onnodige volledige kleur × maat × uitvoering-matrix in ieder productveld. Alle aangeboden acties blijven expliciet aan de bron getoetst.

Als een bronlink bijvoorbeeld bij een kleurkeuze ook de lengte verandert, krijgt de hele betrokken productfamilie `HOLD`. Het plan bevat de concrete bronkeuze, gewenste combinatie en werkelijke bestemming. Voorraadverschillen worden als waarschuwing vastgelegd; de builder zet geen fictieve aantallen of voorraadbeleid.

## Productvelden

| Veld | Inhoud |
| --- | --- |
| `custom.fabriecio_choices` | JSON met `groups`, menulabels/waarden en expliciete bestaande productbestemmingen; swatches gebruiken alleen het bijbehorende Shopify CDN-productbeeld |
| `custom.fabriecio_delivery` | JSON met brongebaseerde `in_stock`, `expected_text`, `discontinued`, `source_url` en `observed_at` |

Alleen de eigen voorraadmelding van het huidige Fabriecio-product wordt voor levering gebruikt. Voorraad van onderdelen in een bundel wordt afzonderlijk bewaard en wordt niet als voorraad van het complete artikel overgenomen. Verwachte weekteksten blijven letterlijk broninformatie; er wordt geen kalenderdatum of volgende-werkdaggarantie afgeleid.

De Shopify-limiet van 256 product-metafielddefinities blokkeerde tijdens deze uitvoering het toevoegen van definities. Er zijn geen bestaande definities verwijderd. De nieuwe velden worden als merchant-owned, ongestructureerde JSON-velden gebruikt, overeenkomstig de bestaande Lagoo-aansluiting. De aangepaste Liquid-rendering is hiermee getest.

Een aparte, expliciet geautoriseerde uitvoeringsstap schrijft de gecontroleerde velden met `metafieldsSet` en `compareDigest: null` voor aantoonbaar nog niet bestaande waarden. Lees de waarden daarna terug. De nieuwe velden mogen geen bestaande prijzen, aantallen, artikel-ID's, handles of andere merken wijzigen. De collector, builder en tests hieronder voeren deze stap niet uit.

## Controleren

```sh
python3 -m unittest discover -s scripts/fabriecio -p 'test_*.py' -v
node scripts/fabriecio/test-theme.mjs
node scripts/fabriecio/test-plan.mjs --plan ../fabriecio-private/plan.json --source ../fabriecio-private/normalized-catalog.json --output ../fabriecio-private/runtime-test-report.json
```

De Python-controles behandelen onder meer foutieve bronlinks, dubbele artikelidentiteiten, ontbrekende bestemmingen, verwarrende bundelvoorraad en verwachte weekteksten. De JavaScript-controles renderen de echte Liquid-adapter en bedienen de bestaande Hotbath-switcher; zij vervangen geen echte browser-, mobiele of checkouttest.

Bewaar de volledige broncapture, Admin-inventaris, schrijfplan, write/readback-antwoorden en herstelgegevens privé. Commit alleen code, beperkte openbare uitleg en aantoonbare testtotalen. HTML-cache, volledige catalogi en ruwe Admin-exports horen niet in deze openbare Git-repository.

Voor themarollen, implementatiestand, herstel en vrijgave: [uitvoeringsdossier](../../docs/fabriecio/2026-11-05/product-choices/README.md).
