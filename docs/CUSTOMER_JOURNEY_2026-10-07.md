# BadkamerCity — CJ-01: uitvoering en echte browserbewijzen

**Datum:** 7 oktober 2026. **Scope:** klant zoekt een koperkleurige opbouwwastafelkraan. **Levertijden:** buiten scope. **PR:** #3. **Volgende zoek-/filtertaak:** #4 (CJ-02).

## 1. Echt gewijzigd in Shopify Admin

### Collecties: 43 producten, 129 koppelingen

Query: `vendor:Hotbath AND status:active AND title:wastafelkraan AND tag:Koper` leverde 46 records met `hasNextPage=false`. Bij 31 opbouw- en 12 inbouwartikelen stond een exact passend `bc_data.source_category_path` van type `list.single_line_text_field`. Drie records zonder dit bronpad zijn ongemoeid gelaten.

Eerst vier producten gekoppeld, daarna alle twaalf pilotkoppelingen opnieuw gelezen en prijzen/seriecollecties gecontroleerd. Vervolgens de overige 39 geschikte producten gekoppeld. De eindquery las alle 129 vereiste koppelingen als true terug; de tegenovergestelde opbouw/inbouw-leaf bleef false.

| Collectie | ID | Voor | Na |
|---|---|---:|---:|
| Kranen | 569428181258 | 739 | 782 |
| Wastafelkranen | 570058506506 | 94 | 137 |
| Opbouw wastafelkranen | 570059522314 | 52 | 83 |
| Inbouw wastafelkranen | 570059555082 | 42 | 54 |

De nieuwe aantallen zijn ook op echte storefrontpagina's gezien. Geen producten opnieuw aangemaakt. Bestaande seriecollecties bleven behouden. Dit is uitsluitend de gecontroleerde koperselectie, niet de volledige Hotbath-catalogus.

Exacte IDs, oude afwezigheid, bronpaden en terugzetgrens: `CUSTOMER_JOURNEY_MEMBERSHIP_RECEIPT_2026-10-07.json`.

### Titels: kleine, afzonderlijke proef

Bij AC003BCP, AR033BCP, B103BCP en CB003CBCP is alleen `opbouw` vóór `wastafelkraan` toegevoegd. Het getypte broncategoriepad bevestigt dit. De bestaande handles zijn expliciet behouden. Vier Admin-readbacks bevestigden titel, URL, SKU, prijs, ACTIVE-status en memberships. Producttypes, tags, omschrijvingen, media, SEO-overrides en levertijden niet gewijzigd.

De daaropvolgende echte zoekproef leverde geen afdoende oplossing op. Sommige gewijzigde artikelen kwamen hoger, maar gewone opbouwzoekvragen hielden veel inbouwdelen en een teller van 1000. De volgorde verschilde tussen gewone input en een afzonderlijke sessie. Daarom niet blind opgeschaald naar duizenden titels. De vier titels zijn inhoudelijk duidelijker; er wordt geen algemene rankingverbetering geclaimd.

Oude/nieuwe waarden en rollback: `CUSTOMER_JOURNEY_TITLE_PILOT_2026-10-07.json`.

## 2. Theme-wijziging: alleen bestaande UNPUBLISHED draft

MAIN bij controles: `194864677130` — BadkamerCity - SEO categoriehub. Niet geschreven of gepubliceerd.

Bestaande draft: `194924904714` — BadkamerCity - Hotbath publicatiebasis 7 okt.

Alleen `templates/cart.json` aangepast: `disabled: true` toegevoegd aan de `featured-collection`-sectie die uit `all` willekeurige producten toonde onder de Engelse kop “Featured collection”. De configuratie bleef verder behouden. Productregels, checkoutknoppen en cart-JavaScript niet herschreven.

Draft-readback MD5 vóór: `adeaf28e1f9ff452bd460ccb100ec66b`; na: `76c34ebf6a9ea2564d16fbbfed1ca4ed`. Nacontrole op desktop en mobiel: het blok is weg, de lege winkelwagen blijft bruikbaar.

De draft had al uitgebreidere Hotbath-specificaties. Die zijn behouden en nu echt bekeken: dezelfde Ace AC003BCP toont in het concept onder meer uitloopdiepte 12 cm, uitloophoogte 8,7 cm en kraanhoogte 15,6 cm, naast afwerking, aansluitingen en wel/geen plug/sifon. De live pagina toonde vooral artikelnummer, merk en serie. Dit bestaande werk is niet opnieuw gebouwd en niet zelfstandig gepubliceerd.

**Deploywaarschuwing:** deze branch is gebaseerd op MAIN en is geen volledige snapshot van het Hotbath-concept. Push hem niet volledig over die draft heen. Alleen cart.json is door deze taak naar de draft geschreven. Eerst conceptreview/publicatie door merchant, daarna volledige nieuwe baseline met Git synchroniseren.

## 3. Wat echt in Chromium getest is

Desktop 1440×900 en mobiele emulatie 390×844; anonieme geïsoleerde sessies. Eerste browserrun `37689932113`, artifact `11512433730`: 38 screenshots, 14 expliciete PASS-stappen, nul gefaalde of geblokkeerde uitvoeringsstappen. Zoekresultaten zijn OBSERVED, niet automatisch goedgekeurd.

- Via zichtbare links Home → Kranen → Wastafelkranen → Opbouw wastafelkranen aangeklikt op beide viewports.
- Zoekinput daadwerkelijk gevuld en Enter gebruikt voor vier zoekvragen; exacte SKU AC003BCP gaf één passend resultaat.
- Hotbath Ace en Wiesbaden Style-productpagina's geopend.
- AC003BCP via de echte knop toegevoegd. Variant-ID, SKU, prijs €301,00 en hoeveelheid 1 in de teruggegeven cart gecontroleerd.
- Cart geopend, checkout-entry geopend zonder gegevens in te vullen of in te dienen, terug naar cart, hoeveelheid 2, daarna artikel verwijderd. Beide carts aan het eind aantoonbaar leeg.
- Geen horizontale overflow gemeten in de vastgelegde viewports/pagina's.

In de bekeken checkout was PayPal zichtbaar. Andere betaalmethoden, iDEAL, verzending na adresinvoer, belastingberekening, betaaltransactie, orderbevestiging en leveranciersafhandeling zijn niet getest. Geen order aangemaakt. Dit is geen bewijs van volledige checkoutgereedheid of alle browsers/menuroutes.

## 4. Belangrijkste open probleem: gewone zoekvraag en filters

De publieke filter-UI in de onderzochte collecties/zoekpagina's biedt Beschikbaarheid en Prijs. Kleur/afwerking/montage worden daar niet als bruikbare keuzes getoond. De externe VPS-filterproef is niet sitebreed aangezet.

Vóór de titelproef gaf `opbouw wastafelkraan koper` 1000 getoonde resultaten, met inbouw/afbouwdelen op alle eerste tien plaatsen. `koperen opbouw wastafelkraan` gaf vergelijkbaar ongeschikt aanbod. `wastafelkraan koper` bevatte een mix. De teller is weergegeven, niet onafhankelijk als volledige relevante productset geteld.

Diagnose in echte browser:
- AND toevoegen: onvoldoende.
- Exacte woorden tussen quotes: vóór de titelproef slechts een hendel; na de proef ook de verduidelijkte artikelen. De teller en geladen kaarten waren in één momentopname niet gelijk; niet als volledig betrouwbare resultaatscore behandelen.
- `title:wastafelkraan AND title:koper NOT title:inbouw NOT title:afbouwdeel NOT title:hendel NOT title:vloermontage`: 43 getoonde resultaten en geen dergelijke onderdelen in de eerste tien. Dit is alleen diagnose, geen verborgen query-hack toegevoegd voor klanten.

CJ-02 / issue #4: eenduidige producttypering en bronvelden, zoekconfiguratie, bestaande VPS/index en fallback onderzoeken; dezelfde queryset herhalen. Acceptatie: minstens 8 van 10 handmatig gecontroleerde resultaten passend bij de koopvraag; correcte kleur/afwerking, reset en mobiele filterwerking. Nog niet gehaald.

## 5. Nacontrole en herhaalbaarheid

Run `37691090119`:
- Eerste poging: artifact `11513716449`; 14 planner-tests geslaagd; read-only klantreis geslaagd; zes draftcontroles geslaagd (cart zonder aanbevelingen, echte specs, geen overflow; ieder op desktop en mobiel).
- Tweede poging, na titelproef: artifact `11514190257`; dezelfde controles opnieuw geslaagd. Zoekrelevantie bleef onvoldoende zoals hierboven beschreven.
- Artefacten bevatten report.json/followup.json en PNG's; bewaren vóór de 7-dagenretentie afloopt.

Bestanden:
- `scripts/cj_collection_plan.py`: alleen-lezen planner; geen Shopify-writes. Exacte bronpaden, expliciete booleans, identiteitscontrole, uitzonderingenlijst, herhaald uitvoeren is een no-op als memberships al bestaan.
- `tests/test_cj_collection_plan.py`: 14 tests voor die garanties.
- `scripts/customer_journey_browser.py`: gewone browserroute. Default read-only; alleen apart `--cart` voor de begrensde eigen sessies. Nooit order/customerinfo indienen.
- `scripts/customer_journey_followup.py`: read-only draftcontrole en zoekdiagnose.
- `.github/workflows/customer-journey.yml`: read-only herhaalruns, contents:read, gepinde actions en Playwright. Geen credentials.
- `.gitignore`: test-results/playwright-report buiten openbare Git-history.

## 6. Overname en vervolg

1. Geen nieuwe banner/designronde vóór zoekintentie en filters bruikbaar zijn. Gebruik issue #4 als eerstvolgend werkblok en sluit aan op het bestaande filterproject, niet een tweede backend.
2. Categorisatie na dit bewezen voorbeeld uitbreiden met read-only bronexport, uitzonderingen en per-batch readback. In de importer borgen.
3. Het bestaande Hotbath-concept laten beoordelen; deze beperkte taak is geen volledige publicatiegoedkeuring. Na merchant-publicatie de volledige theme-baseline vernieuwen.
4. Gewenste betaal-/verzendregels en echte veilige testorder apart afhandelen. Levertijden volgens de afgesproken latere API-planning.

Rollback: eerst drift lezen. Alleen geregistreerde toegevoegde memberships verwijderen, nooit producten/collecties. Titelrollback is apart en mag de collectieverbetering niet terugdraaien. Cartrollback: uitsluitend de nieuwe disabled-vlag terugnemen. Nooit een volledig oud thema over nieuwer werk schrijven.

**Git main is niet gewijzigd door merge; een remote status bewijst geen schone Windows-werkmap. Geen algemene SEO-, performance-, catalogus- of checkoutgoedkeuring.**
