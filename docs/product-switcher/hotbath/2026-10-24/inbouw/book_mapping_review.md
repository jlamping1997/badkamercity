# Hotbath afbouwdeel naar inbouwdeel - broncontrole

24 oktober 2026. Alleen analyse van catalogus editie18 en de bestaande Shopify-snapshot. Geen wijzigingen aan webshop of producten.

## Uitkomst

Een betrouwbare koppeling kan via een expliciete compatibiliteitstabel. EXT helpt artikelen vinden, maar bepaalt niet zelfstandig het passende inbouwdeel of wat al bij de prijs hoort.

31 afbouwmodellen onderzocht; 208 huidige kleur-/maatartikelen gevonden. Alle doel-inbouwdelen in deze mapping komen uniek, actief en gepubliceerd voor in de snapshot. Vijf MHF-modellen vereisen een expliciete alias omdat hun Shopify-SKU geen EXT bevat.

## Methodiek

1. Classify sale content first: TRIM_ONLY, COMPLETE_SET_INCLUDES_BODY, BODY_ONLY, INCLUDED_PRICE_SEPARATE_ORDER, UNKNOWN.
2. Discover candidates through EXT/TEXT plus title Afbouwdeel/Afdekset and exact catalog models; neither signal is decisive alone.
3. Read the exact manufacturer table row or component list. Record exact body SKU, quantity, edition, printed/PDF page and evidence.
4. Expand a verified trim model across color or length only where the exact model family is supported. Keep explicitly verified aliases as exceptions.
5. Resolve the body by exact SKU to exactly one active published product; never derive or substitute a target. Retrieve live sellable variant ID before any cart work.
6. If the body is already included in the set or price, block the normal paid addon and handle inclusion/fulfilment separately.
7. For a confirmed trim-only item, Yes selects the exact body with quantity equal to trim quantity; No means the customer already has it. Default and copy require a clear customer choice.
8. Test color/length switches, body deduplication, quantity changes, remove/add, cart matching and checkout totals before deployment.

## Bronvaste representatieve koppelingen

| Afbouwmodel in Shopify | Exact inbouwdeel | Aantal | Gedrukt / PDF | Huidige SKU-aantallen |
|---|---|---:|---|---:|
| CB105EXT18 | HBCB105 | 1 | 170/172 | 10 |
| CB105EXT25 | HBCB105 | 1 | 170/172 | 10 |
| CB105TEXT18 | HBCB105T | 1 | 171/173 | 10 |
| CB105TEXT25 | HBCB105T | 1 | 171/173 | 10 |
| CB106EXT18 | HBCB105 | 1 | 172/174 | 10 |
| CB106EXT25 | HBCB105 | 1 | 172/174 | 10 |
| CB006TEXT18 | HBCB005T | 1 | 173/175 | 10 |
| CB006TEXT25 | HBCB005T | 1 | 173/175 | 9 |
| AR105EXT18 | HBCB105 | 1 | 67/69 | 4 |
| AR105EXT25 | HBCB105 | 1 | 67/69 | 4 |
| AR125EXT | HBCB105 | 1 | 68/70 | 4 |
| AR009EXT | MB009 | 1 | 77/79 | 1 |
| CB009EXT | HB009 | 1 | 194/196, 282/284 | 14 |
| CB007EXT | HB007 | 1 | 194/196, 282/284 | 11 |
| CB7009EXT | HBCB7009 | 1 | 187/189 | 10 |
| CB7067EXT | HBCB7067 | 1 | 187/189 | 10 |
| AR7009EXT | HBCB7009 | 1 | 81/83 | 4 |
| AR7067EXT | HBCB7067 | 1 | 81/83 | 4 |
| MHF011 | MHF001 | 1 | 356/358 | 5 |
| MHF012 | MHF002 | 1 | 356/358 | 5 |
| MHF013 | MHF003 | 1 | 356/358 | 5 |
| MHF014 | MHF004 | 1 | 357/359 | 5 |
| MHF015 | MHF005 | 1 | 357/359 | 5 |
| GLF011EXT | MHF001 | 1 | 358/360 | 4 |
| GLF012EXT | MHF002 | 1 | 358/360 | 4 |
| GLF013EXT | MHF003 | 1 | 358/360 | 4 |
| GLF014EXT | MHF004 | 1 | 359/361 | 4 |
| GLF015EXT | MHF005 | 1 | 256/258 | 4 |
| AC009EXT | HBAC009 | 1 | 308/310 | 6 |
| AC039EXT | HBAC039 | 1 | 308/310 | 6 |
| AC177EXT | HBCB177 | 1 | 311/313 | 6 |

Elke directe koppeling staat in een tabel met afzonderlijke kolommen Inbouwdeel, Afbouwdeel en Totaal. Een combinatieprijs in die tabel betekent niet dat een Shopify-SKU met alleen het afbouwmodel ook het inbouwdeel bevat. De exacte SKU en leveringsinhoud moeten vóór gebruik overeenkomen.

## Compleetsets: geen tweede inbouwdeel toevoegen

| Complete set | Inbegrepen inbouwdeel | Gedrukt / PDF |
|---|---|---|
| IBS7009 | HBCB7009 | 199/201 |
| IBS70 | HBCB7067 | 200/202 |
| IBS20 | HB007 | 202/204 |
| IBS20A | HB009 | 203/205 |
| IBS1 | HB007 | 286/288 |
| IBS1A | HB009 | 287/289 |
| IBS12 | HB007 | 288/290 |
| IBS12A | HB009 | 289/291 |

De onderdelenlijsten noemen de body al in de standaardset. Een apart betaald Ja/Nee-inbouwdeel bij deze sets kan dubbel leveren en dubbel berekenen.

## Belangrijke uitzonderingen

- **CB009EXT → HB009**, niet HBCB009. **AR009EXT → MB009**, niet HBAR009. **CB006TEXT → HBCB005T**, niet HBCB006T. **GLF011EXT → MHF001**. Een HB-prefixregel is dus onbetrouwbaar.
- **MHF011..015 zonder EXT** zijn toch afdek-/afbouwmodellen. Het boek gebruikt in de tabel MHF011EXT.. tot MHF015EXT..; de kop en actuele Shopify-SKU ondersteunen de expliciete alias. Die alias moet eenmalig als uitzondering worden goedgekeurd.
- **Rails RARH50-1 / MBASES2**: p462/PDF464 vermeldt dat het inbouwdeel al in de setprijs zit maar apart moet worden besteld. Dit vraagt een andere prijs-/afhandelregel dan een gewone betaalde aanvulling.
- **KHDS5EXT → HBKHDS4**: p367/PDF369. Het exacte doelartikel is niet in de snapshot gevonden. Geen vervangend of afgeleid artikel koppelen.
- **EXT-statistiek:** 843 SKU’s bevatten EXT; 27 titels daarvan zeggen niet expliciet afbouw/afdek. Omgekeerd hebben 50 SKU’s zonder EXT wel een afbouw-/afdeksetlabel. Er is binnen deze beperkte controle geen bewezen EXT-foutpositief gevonden.
- **Afbeelding of prijs is onvoldoende bewijs.** Een technische tekening kan beide delen tonen en het boek kan een totaalprijs noemen, terwijl de gekozen afbouw-SKU los verkocht wordt.

## Wat nog nodig is vóór bouwen

Leest de live productvariant-ID van elk exact doelartikel uit, controleer de omschrijving/leveringsinhoud, leg de keuze en hoeveelheid vast en test de winkelwagen. Eerst CB105EXT18/25 als pilot, daarna de overige bevestigde families. Onbekende koppelingen krijgen geen optie.

Bestanden: book_mapping_review.json bevat alle huidige gematchte SKU’s, product-ID’s, handles, bronfragmenten en uitzonderingen. book_mapping_qa.png is een interne visuele broncontrole.

## Actuele CB105-controle beschikbaar

De aparte Admin-readback bevat42records:40afbouwartikelen en2inbouwdelen. Alle40afbouwartikelen hebben met_inbouwdeel=false. CB105EXT18/25 koppelt aan HBCB105, variant53187364356362 (€174,00); CB105TEXT18/25 koppelt aan HBCB105T, variant53187899162890 (€279,99). Beide doelvarianten zijn beschikbaar voor verkoop. Deze gegevens ondersteunen een exacte40artikelpilotallowlist; ze bewijzen nog geen gebouwde of geteste winkelwagenfunctie.
