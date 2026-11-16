# Verzendkosten en levertijden — 16 november 2026

Status: **controle afgerond; wachten op concrete transporttarieven en levertijden van eigenaar**. Er zijn geen live verzendinstellingen gewijzigd.

## Besluiten van eigenaar

- M444AB blijft gepubliceerd, ook op Google. De juiste kleurfoto blijft wachten op Hotbath; niet opnieuw uitsluiting voorstellen.
- Tegels, baden en badkamermeubels krijgen een apart transporttarief.
- Levertijd verschilt per artikel. Een algemene belofte van 2–5 werkdagen past niet bij het hele assortiment.

## Feitelijke huidige situatie

| Onderdeel | Gecontroleerde instelling |
| --- | --- |
| Shopify standaard NL | €6,95 tot en met €100,00; gratis vanaf €100,01 |
| Shopify grote goederen | Geen afzonderlijk transporttarief in de actieve NL-Market |
| Google Merchant 5902025216 | Complete NL-service voor All products; €6,95, gratis boven ingestelde waarde €100; algemeen 2–5 werkdagen |
| Google termijnopbouw | 1 werkdag verwerking + 1–4 werkdagen vervoer, maandag–vrijdag |
| Publieke bezorgpagina | Standaardprijzen kloppen; grote goederen: eerst contact opnemen; levertijd per artikel |
| Native verzendbeleid | SHIPPING_POLICY ontbreekt; /policies/shipping-policy geeft 404 |
| €75 in retourbeleid | Raming voor retourpallet inclusief btw; **geen bevestigd heentarief** |

De Google-editor is alleen gelezen. Een tijdelijke Amsterdam-tijdzonekeuze om verder te kunnen lezen is via Annuleren verworpen. Er is niets opgeslagen. Eventuele productoverrides voor levertijd zijn niet voor alle artikelen gecontroleerd. De gratis-grens van €100 in Google is op zichzelf geen bewezen centverschil met Shopify; deze niet blind naar €100,01 wijzigen.

## Vijf actuele tariefproeven

| Winkelmand | Subtotaal | Gevonden verzendkosten |
| --- | ---: | ---: |
| Klein artikel | €99,99 | €6,95 |
| Klein artikel op grens | €100,00 | €6,95 |
| Kleine artikelen boven grens | €112,00 | Gratis |
| Gemengde merken | €81,18 | €6,95 |
| Porcelanosa tegeldoos, formaat 150 cm | €268,07 | Gratis |

Alle vijf komen overeen met de **huidige** technische instelling. De laatste proef toont juist de ontbrekende zakelijke uitzondering aan. Deze is dus niet als gewenste eindsituatie goedgekeurd.

Getest met een aparte verse anonieme sessie en een publiek zakelijk Nederlands postcodegebied. Alleen eigen testmand na afloop geleegd en lege mand teruggelezen. Geen bestelling, betaalhandeling of e-mail aangemaakt. Geen uitspraak over alle postcodes of een apart bad/meubel gemaakt.

## Nodig voor uitvoering

1. Uitgaande transporttarieven voor tegels, baden en meubels, inclusief btw; per bestelling/pallet/levering, en eventuele uitzonderingen, gratis grens en gemengde bestellingen.
2. Werkelijke levertijdgroepen en termijnen: voorraad, bestelartikelen en afwijkende leveranciers, met onderbouwde bron.

Daarna in één ronde: ondersteunde tariefgroepen en productindeling controleren, Shopify aanpassen, Google en publieke bezorg-/verzendteksten gelijkzetten en standaard-/grote-/gemengde manden opnieuw controleren. Geen willekeurig tarief invullen en geen algemene levertijd verzinnen.

## Bewijs en status

- [Gestructureerde controle](audit.json)
- [Vijf actuele tariefproeven](cart-quotes.json)
- BC-LIVE-014: PARTIAL — transportbedragen ontbreken, native verzendpolicy nog open.
- BC-GOOGLE-004: PARTIAL — retouren eerder ingesteld; verzending en levertijden nog niet gelijkgezet.
- BC-LIVE-004: IN_PROGRESS_USER — bron/termijn per productgroep nodig.
- Geen automatische vervolgrun of actieve schrijver na overdracht.
