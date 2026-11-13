# Wiesbaden — prijsbroncontract en kalibratie

**Vastgelegd op 21 oktober 2026.** Deze notitie onderbouwt de prijsbinding uit het [uitvoeringsplan](../WIESBADEN_EXECUTION_PLAN.md). Het is een bron- en rekencontract; het bevestigt geen uitgevoerde Shopify-wijzigingen of geslaagde terugleescontrole. De onderstaande winkelvergelijking gebruikt de snapshot van **21 oktober 2026, 21:46:12 UTC**.

## 1. Bindende bronbetekenis

De consumentenprijs volgt het fabrikantadvies **inclusief btw**, in EUR. Voor de hieronder vastgelegde Wiesbaden-bronversies geldt:

| Bronveld | Betekenis voor deze uitvoering | Omrekening |
| --- | --- | --- |
| CSV: `advertentieprijs (excl. btw)` | Fabrikantconsumentenadvies inclusief btw; de kolomkop wordt expliciet overruled | Factor **1,00** |
| Fabrikantcache: `source_advice_eur` | Hetzelfde fabrikantconsumentenadvies inclusief btw | Factor **1,00** |
| Historisch cachelabel `EXCL_TAX_SELECTED_BY_MANUFACTURER_COMPONENT` | Verouderde interpretatie; vervangen door dit gekalibreerde contract | Geen extra btw |

Deze binding geldt uitsluitend voor de vastgelegde bronversies en het merk Wiesbaden. Een aantoonbaar exclusieve adviesprijs uit een andere bron krijgt eerst eenmaal 21% btw. Andere prijsvelden, andere merken en toekomstige bronversies vallen niet automatisch onder deze uitzondering op de kolomkop.

## 2. Bewijs en bronversies

De gerichte officiële steekproef bevat **20 SKU's; alle 20 bronbedragen zijn exact gelijk aan de openbare Wiesbaden-adviesprijs**, vóór afronding. De selectie omvat verschillende productgroepen, vijf bedragen onder € 100 en zeven leden van de oorspronkelijke importqueue. De bedragen lopen van € 29,00 tot € 1.199,00.

Daarnaast zijn **alle 2.411 Wiesbaden-regels uit de CSV** op exact artikelnummer gekoppeld aan de fabrikantcache: **2.411 van 2.411 bedragen zijn exact gelijk**, zonder prijsverschillen. Hiervan zijn 2.410 positief; `41.3563` is nul. Ook alle 20 officiële steekproefbedragen komen exact overeen met `source_advice_eur`.

| Bewijsbestand | SHA-256 |
| --- | --- |
| Leveranciersbestand `1186(2).csv` | `80d2d72aea47073fbd185f94a46e23f6fbb3b8812889131717dfbc438090dc2e` |
| Fabrikantcache `product-master.jsonl`, datarun 19 oktober 2026 | `19f1a19d5c3a323f3dcdecb959f31628ff56c897b5c5cb3bf75b35ccb8f045fa` |
| Kalibratiebewijs `source_price_calibration.json` | `9277d769a2a921acea04f25a9189ab0913307d024f96a5f0c4e26daa01980398` |

De oorspronkelijke bestanden en volledige winkel-/uitvoergegevens blijven privé. Deze notitie bevat uitsluitend openbare consumentenprijzen en veilige controletellingen.

**Bewijsgrens:** de geraadpleegde fabrikantvermeldingen noemen het bedrag “Adviesprijs”; in deze gerichte controle is niet op iedere pagina een expliciete btw-zin gevonden. De inclusieve binding combineert het bestaande projectcontract voor fabrikantconsumentenadvies met de exacte bedragvergelijkingen. De 20 voorbeelden zijn geen afzonderlijke controle van elk artikel. Bij beperkte paginatoegang is officiële zoekcache of een officiële categoriepagina gebruikt; de methode staat hieronder. Dit onderzoek controleert geen actuele voorraad.

## 3. Exacte eindafronding

Bereken met exacte decimalen. Gebruik het exacte inclusieve bedrag om de grens te bepalen. **Boven € 100**: afronden naar de dichtstbijzijnde hele euro, met een halve euro naar boven (`ROUND_HALF_UP`). **Tot en met € 100**: afronden op centen. Er is geen tussentijdse afronding.

| Voorbeeld | Berekening | Eindprijs |
| --- | --- | --- |
| Exact € 100,00 incl. | Valt binnen de centenregel | € 100,00 |
| `22.2723`: € 100,90 incl. | Boven de grens; dichtstbijzijnde hele euro | € 101,00 |
| `22.2730`: € 99,25 incl. | Centen behouden | € 99,25 |
| Rekenvoorbeeld € 149,49 incl. | Naar beneden naar de dichtstbijzijnde euro | € 149,00 |
| Rekenvoorbeeld € 149,50 incl. | Halve euro naar boven | € 150,00 |
| Rekenvoorbeeld € 100,41 aantoonbaar excl. | × 1,21 = exact € 121,4961; direct afronden | € 121,00 |

Het laatste voorbeeld mag niet eerst € 121,50 en daarna € 122 worden. Het is een rekenvoorbeeld voor een exclusieve bron, geen reden om op de huidige CSV extra btw toe te passen.

## 4. Twintig officiële prijsvoorbeelden

Alle bronbedragen in deze tabel zijn gelijk aan zowel CSV als fabrikantcache. De links zijn exact de officiële bronnen uit het kalibratiebewijs. “Zoekcache” betekent een opgehaalde zoekvermelding van die officiële URL, geen rechtstreekse actuele pagina-uitlezing.

| SKU met officiële bron | Adviesbedrag | Eindprijs | Geraadpleegd bewijs |
| --- | ---: | ---: | --- |
| [24.3710](https://www.wiesbaden.nl/bekijk-assortiment/wastafels/wastafelkranen.html?p=4) | € 209,00 | € 209,00 | Categoriepagina |
| [36.4028](https://www.wiesbaden.nl/bekijk-assortiment/badmeubels/meubelwastafels.html) | € 445,00 | € 445,00 | Categoriepagina |
| [33.4422](https://www.wiesbaden.nl/unimatch-fonteinsifon-5-4-x-32-mm-geborsteld-brons-koper-pvd-33-4422.html) | € 70,95 | € 70,95 | Productpagina |
| [41.3686](https://www.wiesbaden.nl/elara-elektrische-radiator-smart-wifi-118-5-x-45-cm-geborsteld-staal-pvd-41-3686.html) | € 415,00 | € 415,00 | Productpagina |
| [41.3676](https://www.wiesbaden.nl/bekijk-assortiment/radiatoren/elektrische-radiatoren.html) | € 639,00 | € 639,00 | Categoriepagina |
| [29.2020](https://www.wiesbaden.nl/bekijk-assortiment/douche.html?merk=Wiesbaden) | € 840,15 | € 840,00 | Officiële zoekcache |
| [29.2040](https://www.wiesbaden.nl/bekijk-assortiment/douche.html?merk=Wiesbaden) | € 774,34 | € 774,00 | Officiële zoekcache |
| [29.2080](https://www.wiesbaden.nl/bekijk-assortiment/douche.html?merk=Wiesbaden) | € 778,34 | € 778,00 | Officiële zoekcache |
| [29.5095](https://www.wiesbaden.nl/) | € 1.074,20 | € 1.074,00 | Officiële zoekcache |
| [29.5942](https://www.wiesbaden.nl/bekijk-assortiment/douche/douchegarnituren/handdouchehouders.html) | € 76,93 | € 76,93 | Officiële zoekcache |
| [20.3840](https://www.wiesbaden.nl/bekijk-assortiment/douche/douchecabines.html?serie%5B0%5D=Salone&serie%5B1%5D=Entra) | € 579,00 | € 579,00 | Officiële zoekcache |
| [32.3451](https://www.wiesbaden.nl/vesta-junior-wandcloset-rimless-verkort-met-vesta-junior-toiletzitting-softclose-en-quick-release-glans-wit-32-3451.html) | € 339,00 | € 339,00 | Officiële zoekcache |
| [38.3760](https://www.wiesbaden.nl/tigris-spiegel-rechthoek-met-led-60-x-80-cm-38-3760.html) | € 199,00 | € 199,00 | Officiële zoekcache |
| [21.3650](https://www.wiesbaden.nl/libero-vrijstaand-ligbad-178-x-80-cm-acryl-glans-wit-met-waste-wit-glans-21-3650.html) | € 1.199,00 | € 1.199,00 | Officiële zoekcache |
| [22.3701](https://www.wiesbaden.nl/caral-amador-fonteinkraan-kiwa-1-2-chroom-22-3701.html) | € 59,40 | € 59,40 | Officiële zoekcache |
| [33.4123](https://www.wiesbaden.nl/bekijk-assortiment/douche/afvoeren/losse-roosters-voor-de-douchegoten.html?p=2) | € 29,00 | € 29,00 | Officiële zoekcache |
| [22.2723](https://www.wiesbaden.nl/bekijk-assortiment/toilet.html?p=10) | € 100,90 | € 101,00 | Officiële zoekcache |
| [22.2730](https://www.wiesbaden.nl/bekijk-assortiment/toilet.html?p=10) | € 99,25 | € 99,25 | Officiële zoekcache |
| [38.4050](https://www.wiesbaden.nl/bekijk-assortiment/badmeubels/meubelwastafels.html) | € 820,00 | € 820,00 | Categoriepagina |
| [41.3657](https://www.wiesbaden.nl/bekijk-assortiment.html) | € 309,00 | € 309,00 | Officiële zoekcache |

## 5. Bestaande artikelen buiten de CSV

De volledige snapshot bevat 2.449 Wiesbaden-producten met ieder één variant. Daarvan ontbreken **43 SKU's** in de huidige Wiesbaden-CSV. Voor **18** is in de fabrikantcache een positieve adviesprijs met exacte artikelidentiteit en officiële bronverwijzing gevonden. **15** snapshotprijzen voldoen al aan het contract; **3** hebben het volgende voorgestelde prijsverschil:

| SKU en fabrikantbron | Snapshotprijs | Advies incl. btw | Voorgestelde eindprijs |
| --- | ---: | ---: | ---: |
| [38.4011](https://www.wiesbaden.nl/shall-onderkast-100-x-36-cm-grafietgrijs-38-4011.html) | € 591,69 | € 489,00 | € 489,00 |
| [29.2025](https://www.wiesbaden.nl/caral-inbouwthermostaat-2-weg-rond-compleet-met-beam-hoofddouche-en-3-standen-handdouche-geborsteld-brons-koper-29-2025.html) | € 1.084,20 | € 1.084,20 | € 1.084,00 |
| [29.4045](https://www.wiesbaden.nl/caral-inbouwthermostaat-2-stopkranen-compleet-met-hoofddouche-30-cm-en-staafhanddouche-geborsteld-brons-koper-29-4045.html) | € 1.270,75 | € 1.270,75 | € 1.271,00 |

De overige **25** hebben geen exacte SKU-match in CSV of fabrikantcache. **Behoud hun bestaande prijs.** Het uiterlijk van een huidig bedrag rechtvaardigt geen automatische deling door 1,21. Ontbreken in deze bronbestanden is ook geen reden tot verwijderen of archiveren.

## 6. De 28 historische kandidaten zonder prijs

De volledige historische groep is opnieuw vergeleken: **geen van de 28 staat in de gebruikte winkelsnapshot; alle 28 hebben in de fabrikantcache € 0,00**. De huidige CSV bevat 27 ervan niet. De enige CSV-match, **`41.3563`**, heeft eveneens € 0,00.

Daarmee zijn **0 van 28** met de huidige CSV/cache van een bruikbare positieve adviesprijs te voorzien. Een nieuwe verkoopbare nulprijsvermelding wordt niet voorgesteld. Deze afzonderlijke prijsuitzonderingen verhinderen de verwerking van de overige artikelen niet. Een latere betrouwbare prijsbron kan ze alsnog oplossen.

## 7. Uitvoering en bewijsgrens

Het private aanvullende manifest bevat alle 43 bestaande SKU's, met bronverwijzingen, oude waarden, variantidentiteit en uitsluitend eventuele `variant_price`-wijzigingen. Vóór schrijven moet de actuele identiteit/prijs nog bij het voorstel passen. Deze notitie bewijst de bronkalibratie en de voorgestelde verschillen op het genoemde meetmoment; uiteindelijke aantallen toegepast, teruggelezen, al gelijk of bewaard horen in het uitvoerresultaat en de [actuele uitvoerstatus](execution-state.json).
