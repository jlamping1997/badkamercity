## Werkdagen bevestigd — gecontroleerd concept staat klaar

De eigenaar houdt maandag t/m vrijdag aan. Vóór 14:00 geldt de volgende werkdag; vanaf 14:00 twee werkdagen. Vrijdag vóór 14:00 → maandag, vrijdag daarna of in het weekend → dinsdag. Nederlandse tijd (Europe/Amsterdam).

**Opgeslagen concept: BadkamerCity - PostNL werkdagen 14u, thema 196542005514; niet gepubliceerd.** De gekoppelde Shopify-publicatietool vereist een apart akkoord voor dit benoemde thema.

De twee teksten zijn aanpasbaar in Thema-instellingen → Tijdelijke voorraadweergave:

- Op werkdagen vóór 14:00 besteld, volgende werkdag in huis.
- Na 14:00 of in het weekend besteld: binnen 2 werkdagen in huis.

De melding verschijnt alleen bij66 gecontroleerde PostNL-productsoorten en een bestelbare variant, ook in de aparte mozaïek-buybox. Onbekende types en pallet/XXL krijgen geen dagbelofte. Voorraadstatus, aantallen en bestaande leveranciersgegevens blijven behouden. Later kan de tijdelijke voorraadweergave uit en kunnen echte status-/levertijdkoppelingen worden gebruikt.

Controle: echte Shopify-render en browser op kraan + mozaïek positief, gewone pallettegel negatief. Actuele Brauer-menu's veiliggesteld:174 bestanden gelijkgetrokken met MAIN en hun hashes teruggelezen. Acht kalendergevallen doorgerekend. Geen echte checkout-/betalingstest voor deze tekstwijziging. Mobiele screenshots via de koppeling mislukten; geen mobiele visuele pass geclaimd.

**Google bleef ongewijzigd.** Automatische goedkeuringscontrole wees het opslaan van één werkdag voor All products af: groottransporttermijn niet bevestigd en nieuwe transporttarieven nog niet live. De editor is geannuleerd; bestaande Complete NL All products-service met2–5dagen is teruggelezen. Geen omweg geprobeerd. Eerst Shopify-tariefgroepen en productindeling afronden; daarna Google labels/tarieven en specifiek PostNL-levertijden gelijkzetten.

[Implementatie en exact vervolg](weekday-implementation.json) · [Kalendergevallen](weekday-calendar-examples.json) · [Conceptafbeelding](weekday-theme-preview.jpg) · [Vijf opgeslagen themabestanden](weekday-theme/).

**Volgende eigenaarshandeling:** expliciet publicatie van dit benoemde thema bevestigen. Daarna native publicatie, verse MAIN-readback en de vijf bestanden naar shopify/current op de codebranch synchroniseren. De oorspronkelijke MAIN196690379018 blijft tot dan live.

---

# Actueel verzendschema — 16 november 2026

## Voorraad en levertijd — laatste eigenaarsinstructie

De eigenaar bevestigt dat alle huidige artikelen op voorraad zijn en wil **Op voorraad** behouden totdat later echte voorraadstatussen en afwijkende termijnen worden gekoppeld. Gewenste Google-voorraadstatus: **in_stock**. Geen fictieve aantallen invullen.

Gewenste dagbelofte, Nederlandse tijd:

- Vóór 14:00 besteld: morgen in huis.
- Vanaf 14:00: overmorgen in huis (exacte 14:00-grens als technische conventie).
- Later product-/leveranciersspecifieke levertijden toevoegen op dezelfde basis.

**Nog twee bedrijfsafspraken nodig:** welke dagen orders worden verwerkt/verzonden en bezorgd (vrijdag, weekend, feestdagen), en of dezelfde termijn ook voor tegels/baden/douchewanden/XXL geldt of dat die op afspraak/eigen termijn gaan. De nieuwe dagbelofte is daarom nog niet live gezet.

Controle: twee publieke productpagina's tonen al Op voorraad en Offer.InStock in de gestructureerde gegevens. Dit bewijst geen volledige verwerking in Google Merchant Center; de eerder gelezen algemene Google-service van 2–5 werkdagen is niet aangepast. Geen voorraad-, kanaal- of themawijziging uitgevoerd.

[Levertijdafspraken en controle](delivery.json). De vier onderstaande verzendtarieven blijven ongewijzigd.

Status: **tarieven uitgewerkt en doorgerekend; productindeling, live instellingen en echte checkoutcontrole nog uitvoeren**. De onderstaande eigenaarsregels vervangen eerdere onvolledige bedragen en de limiet van 1–2 mozaïekdozen. Alles inclusief btw.

| Groep | Producten | Tarief | Gratis bij totaal productbedrag |
| --- | --- | ---: | --- |
| Pakket | Kranen, douchesets, meubels en alle mozaïek | €6,95 | Boven €100 |
| Pallet | Gewone tegels behalve mozaïek/XXL, en baden | €75 | Vanaf €500 |
| Douchewand | Douchewanden | €45 | Vanaf €500 |
| XXL | XXL-tegels in genoemd bereik 120×250–320 cm | €300 totaal | Vanaf €1.000 |

Mozaïek volgt de pakketregels per doos, matje of stuk, zonder de oude limiet van twee dozen. Meubels hebben geen apart groottransporttarief.

XXL is **€300 volledig transport**, inclusief krat en vervoer; nooit €300 plus €75. De eigenaar noemt expliciet gratis vanaf €1.000.

## Combinaties en grenzen

Het **hele productbedrag** van de bestelling telt mee, ongeacht merk of productgroep. Leverancierstarieven zijn interne kosten en leveren geen aparte toeslag per merk op.

Werkafspraak uit het gesprek: één keer het hoogste toepasselijke tarief bij gemengde groepen. Exact €100 blijft €6,95 zoals nu; pakket gratis vanaf €100,01. Voor gewone pallets en douchewanden wordt de voorgestelde grens vanaf exact €500 gebruikt. XXL is gratis vanaf exact €1.000, volgens de expliciete eigenaarsformulering. Als technische conventie producttotaal na korting en vóór verzendkosten gebruiken; nog verifiëren in de echte checkout.

| Voorbeeld | Besteltotaal | Transport |
| --- | ---: | ---: |
| Eén mozaïekmatje | €45 | €6,95 |
| Mozaïekdozen, ook meer dan twee | €180 | Gratis |
| €400 tegels + €200 kranen | €600 | Gratis |
| €250 tegels + €100 douchewand | €350 | €75 |
| XXL | €400 | €300 totaal |
| XXL met andere producten | €900 | €300 |
| XXL | €999,99 | €300 |
| XXL | €1.000 | Gratis |
| €800 XXL + €250 kranen | €1.050 | Gratis |

**20 rekenvoorbeelden PASS in het regelmodel. Dit zijn geen live checkoutproeven.** De oude actieve tarieven zijn niet gewijzigd.

## Exact vervolg

1. Producten betrouwbaar indelen in pakket, pallet, douchewand en XXL. Mozaïek en meubels expliciet naar pakket; nieuwe producten moeten dezelfde indeling krijgen.
2. Binnen de bestaande market-driven Shopify-opzet groepsstaffels uitwerken. De huidige algemene gratis-grens van €100,01 mag pallet/XXL niet blijven overrulen.
3. Echte grens-/gemengde manden testen, inclusief verschillende merken, locaties en korting; geen modelberekening als live geslaagd rapporteren.
4. Google productgroepen, tarieven, gratisdrempels en publieke bezorg-/verzendteksten gelijkzetten. Google kan de geldende betaalde verzending tonen voor een losse bestelling onder de drempel; geen belofte om €75 te verbergen.
5. Voorraad en 14:00-dagbelofte zijn nu door eigenaar aangeleverd; bevestig alleen nog de verwerk-/bezorgkalender en pallet-/XXL-termijn. Latere product-/leverancierskoppelingen volgen apart.

## Specificatie en bewijs

- [Regels en bron/conventies](rules.json)
- [20 rekenvoorbeelden, geen live checkouttest](rule-examples.json)
- [Technische nulmeting](audit.json)
- [Vijf eerdere live mandproeven van de oude instelling](cart-quotes.json)

BC-LIVE-014 blijft PARTIAL tot tarieven, productdekking en beleid echt zijn aangepast en gecontroleerd. BC-GOOGLE-004 blijft PARTIAL tot Google en checkout aansluiten. BC-LIVE-004 blijft IN_PROGRESS_USER voor de nog ontbrekende levertijdbronnen.

---

## Historische nulmeting vóór de tariefverduidelijking

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
