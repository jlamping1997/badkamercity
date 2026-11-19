# Verzendinstellingen Badkamercity

**Stand: 17 november 2026.** Vaste referentie voor de afgesproken tarieven, de werkende Shopify-inrichting en het nog onafgeronde Google-deel. Alle bedragen zijn inclusief btw; huidige verzendland is Nederland.

| Onderdeel | Status | Bewijs |
| --- | --- | --- |
| Shopify-checkout, vier tariefgroepen | LIVE; op 17 november native teruggelezen | [Readback en actuele telling](repairs/2026-11-16-shipping/documentation-check-2026-11-17.json) |
| Gemengde manden en gratisgrenzen | 18 echte tariefquotes geslaagd op 16 november; niet herhaald op 17 november | [Tariefquotes](repairs/2026-11-16-shipping/native-quotes.json) |
| Bezorgpagina en pakketverzendtekst | Eigenaarpublicatie eerder gecontroleerd; huidige MAIN 196690379018 | [Publicatie en voorbereiding](repairs/2026-11-16-shipping/shipping-copy-preview.json) |
| Google-proef Wandtegels → pallet | Eén positief voorbeeld zichtbaar op eigenaarscreenshot van 17 november | [Preview en huidige correctie](repairs/2026-11-16-shipping/documentation-check-2026-11-17.json) |
| Google volledige palletregel | CONCEPT; bronvelden van rij 2–10 moeten worden gecorrigeerd | Geen volledige test/activatie bevestigd |
| Google overige groepen, kosten en drempels | NOG NIET AFGEROND | Oude productoverschrijvingen apart oplossen |

## 1. Bedragen en gratisgrenzen

| Groep | Wat valt eronder? | Kosten | Gratis verzending |
| --- | --- | --- | --- |
| Pakket | Gewone pakketartikelen, kranen, douchesets, alle mozaïek per stuk/mat/doos en meubels | €6,95 tot en met €100,00 | Vanaf €100,01 |
| Pallet | Gewone tegels, exclusief mozaïek en XXL, plus baden | €75,00 onder €500,00 | Vanaf €500,00 |
| Glas | Complete douchewanden, deuren, zijwanden, cabines, badwanden en complete losse glasplaten | €45,00 onder €500,00 | Vanaf €500,00 |
| XXL | Tegels van 120 × 250–320 cm | €300,00 onder €1.000,00, inclusief krat en het volledige transport | Vanaf €1.000,00 |

Kleine glasaccessoires, zoals profielen, knoppen en scharnieren, zijn pakketartikelen. Mozaïek kent geen limiet van één of twee dozen. Er komt geen afzonderlijk meubeltarief bij. XXL is €300 totaal, dus geen €75 extra bovenop die €300.

## 2. Verschillende producten en merken combineren

De waarde van alle producten in de hele bestelling telt mee, ook wanneer die uit verschillende merken of verzendgroepen bestaan. De native inrichting gebruikt de productwaarde na korting; er is geen aparte kortingsmand opnieuw getest.

Er wordt **één keer het hoogste toepasselijke groepstarief** berekend. Kosten van leveranciers of merken worden niet bij elkaar opgeteld voor de klant.

| Voorbeeld | Verzendkosten |
| --- | --- |
| €400 gewone tegels + €200 kranen = €600 | Gratis |
| Gewone tegeldoos €268,07 + glas €199 = €467,07 | €75; geen €75 + €45 |
| Glas €199 + kranen €300 = €499 | €45 |
| Glas samen precies €500 | Gratis |
| Bestelling met XXL, totaal €600 | €300 |
| Bestelling met XXL, totaal precies €1.000 | Gratis |

De XXL-voorbeelden beschrijven de ingestelde staffel; er is op 17 november geen product in de XXL-collectie om een echte XXL-mand mee te testen. Een actueel bad onder €500 was tijdens de eerdere controle niet beschikbaar; de betaalde palletstaffel is met echte tegels getest.

## 3. Hoe Shopify dit uitvoert

Huidige MAIN: **196690379018 — BadkamerCity - verzendtarieven per productgroep**. De Nederlandse Market is 94864998666. Eén actieve value-based verzendoptie, **1272199119114**, bevat vier rate groups. De algemene pakketgroep is de fallback; de specifieke groepen zorgen voor het passende hogere tarief. De gehele mandwaarde bepaalt de gratisgrens.

De nieuwe optie heeft geen algemene gratisgrens op optieniveau. Anders zou een grens van €100 de pallet-, glas- en XXL-staffels kunnen overrulen. De oude algemene optie **1251671343370** is inactief gebleven als rollback.

| Interne collectie | Shopify-ID | Actieve artikelen op 17 november |
| --- | --- | ---: |
| BC verzending – Pakket | 587456708874 | 23.579 |
| BC verzending – Pallettransport | 587456676106 | 3.562 |
| BC verzending – Glastransport | 587456610570 | 1.836 |
| BC verzending – XXL transport | 587456643338 | 0 |

Alle vier collecties zijn ongepubliceerde technische selecties. Samen tellen zij 28.977 actieve producten. Dat is geen bewijs dat ieder actief product ook in Google is gepubliceerd. Normale producten volgen de gecontroleerde producttypen. Voor XXL is na maatcontrole de expliciete tag **bc_shipping_xxl** nodig; die sluit het product uit de gewone palletgroep. Nieuwe producttypen bij imports moeten op dekking worden gecontroleerd.

De technische rollback staat in [native-deployment.json](repairs/2026-11-16-shipping/native-deployment.json). Eerst actuele actieve flags lezen, daarna nieuwe optie uit / oude aan in één marketUpdate. Bij terugzetten van tarieven ook de publieke bezorgtekst beoordelen. Geen latere wijzigingen blind overschrijven.

## 4. Waarom de badnamen dubbel lijken

De catalogus bevat niet-uniforme producttypen. `Vrijstaand bad` en `Vrijstaande Baden` zijn enkelvoud/meervoud van hetzelfde begrip. `Half Vrijstaande Baden`, `Halfvrijstaand bad` en `Halfvrijstaande baden` zijn varianten met andere spaties/woordvormen. Ze krijgen dezelfde verzendgroep, maar staan als verschillende waarden opgeslagen.

Een hoekbad en een whirlpoolbad zijn wel verschillende soorten producten; hun verzendtarief is ook pallettransport. De zeven badwaarden bevatten samen **68 actieve artikelen**, native geteld op 17 november. De precieze historische importoorzaak is niet onderzocht; de huidige schrijfvarianten zijn wel aangetoond.

We behouden de huidige waarden voor de verzendselectie, zodat geen bestaande artikelen wegvallen. **Er is deze beurt geen producttype hernoemd.** Latere opschoning hoort via een vaste importmapping en gecontroleerde migratie van afhankelijkheden: collecties, filters, menu's, verzendselecties en Google-regels. Tot die migratie blijven alle relevante huidige varianten geldig.

## 5. Google: exacte bedoelde palletregel

Bron: **Shopify App API**, bron-ID 10793224912. Doelattribuut: **shipping_label**. In elke rij wordt het bestaande bronveld **Shopify App API → product type** vergeleken met één vaste tekstwaarde. Vergelijking is **equals**. Alle rijen zijn met **OR** verbonden. De uitkomst onderaan is de vaste waarde **pallet**.

| Rij | Letterlijke producttypewaarde | Betekenis | Actieve Shopify-artikelen op 17 november |
| --- | --- | --- | ---: |
| 1 | `Wandtegels` | Gewone wandtegels | 2272 |
| 2 | `Vloertegels` | Gewone vloertegels | 1222 |
| 3 | `Tegels` | Algemene tegelwaarde; nu geen actieve artikelen | 0 |
| 4 | `Half Vrijstaande Baden` | Halfvrijstaande baden | 13 |
| 5 | `Halfvrijstaand bad` | Halfvrijstaande baden | 6 |
| 6 | `Halfvrijstaande baden` | Halfvrijstaande baden | 1 |
| 7 | `Hoekbad` | Hoekbaden | 14 |
| 8 | `Vrijstaand bad` | Vrijstaande baden | 29 |
| 9 | `Vrijstaande Baden` | Vrijstaande baden | 4 |
| 10 | `Whirlpoolbad` | Whirlpoolbaden | 1 |

`Tegels` is als algemene invoerwaarde opgenomen, maar heeft nu geen actieve artikelen. De som van de tien rijen is 3.562: gelijk aan de actuele gewone palletcollectie. Dat controleert de Shopify-selectie, niet automatisch de Google-aanbiedingen of de werking van fout ingestelde Google-bronvelden. Mozaïektypen zijn bewust niet opgenomen.

### Huidige fout in het Google-concept

De eigenaar heeft de tien gewenste tekstwaarden, OR-verbindingen en **Set to → pallet** ingevuld. Maar in de screenshots van 17 november tonen rijen 2–10 bronvelden zoals **Shopify App API.shopi**, **.shopify**, **.shop** en **.shopif**. Dat is niet het bedoelde veld **product type**.

**Eerst corrigeren:** klik het eerste veld van elke betrokken rij aan, zoek op **product type** en selecteer het bestaande **Shopify App API.product type**. De bronnaam alleen is niet het veld. De rechterkant blijft de letterlijke waarde uit de tabel; daar wordt de tekst onder **Add value** geselecteerd. Laat equals, OR en de uitkomst pallet staan.

Daarna **OK → Save as draft → Test rules**. Controleer een wandtegel, vloertegel en bad als positieve voorbeelden, plus mozaïek en een klein pakketartikel als negatieve voorbeelden. Pas de complete regel na correctie en geslaagde controle toe. De eerdere positieve wandtegelpreview bewijst alleen die ene eerste voorwaarde, niet alle later toegevoegde rijen.

Bekend positief proefproduct: **shopify_ZZ_10687518703882_54000406331658**, Porcelanosa Matt White wandtegel 60 × 150 cm. De eigenaar liet bij die aanbieding **pallet** in de preview zien. Dit is gebruikersscreenshotbewijs; deze beurt is geen nieuwe Google-browsercontrole uitgevoerd.

### Google-kosten zijn een aparte stap

Op 16 november is bij dit proefproduct nog per aanbieding aangetroffen: **shipping NL/Standaard/€6,95** en **free_shipping_threshold NL/€100,01**. Dat is fout voor deze gewone tegeldoos onder €500. Het is op 17 november niet opnieuw uit Google gelezen.

Alleen shipping_label toevoegen is daarom geen bewijs dat de uiteindelijke getoonde kosten kloppen. Voor live kosten moet worden gecontroleerd dat de oude per-productvelden verdwijnen of correct per groep worden aangepast. Ook moet de handmatige verzendinstelling in het Shopify Google & YouTube-kanaal na de eigenaarshandeling worden teruggelezen; productsynchronisatie blijft aan.

Daarna de overige labels/groepen en passende tarieven instellen en concrete Google-aanbiedingen controleren. Maak geen overlappende goedkope All-products-services. Google-labels komen niet automatisch voort uit de interne Shopify-collecties. Voor een toekomstige XXL-aanbieding moet Google de XXL-uitzondering vóór de gewone palletselectie herkennen; de huidige producttypevergelijking alleen herkent de Shopify-tag niet.

## 6. Voorraad en werkdagen

De eigenaar houdt alle huidige artikelen standaard op voorraad tot een latere betrouwbare voorraad-/levertijdkoppeling. Er zijn geen fictieve voorraadhoeveelheden gemaakt.

Voor de bevestigde PostNL-pakketmelding: maandag–vrijdag, cutoff 14:00 Europe/Amsterdam. Vóór 14:00 op een werkdag: volgende werkdag. Daarna: twee werkdagen. Vrijdag vóór 14:00 → maandag; vrijdag na 14:00 of in het weekend → dinsdag.

De productmelding is ingericht voor de eerder gecontroleerde 66 pakketproducttypen; niet iedere productsoort buiten die lijst krijgt automatisch dezelfde tekst. Er is geen volgende-dagtermijn voor pallet/XXL bevestigd. Die belofte niet voor alle Google-producten instellen. De eerdere automatische afwijzing van een All-products-ééndagservice blijft behouden; deze beurt geen retry.

## 7. Bewijs en beheer

- [Actuele technische regels](repairs/2026-11-16-shipping/rules.json)
- [Readback, aliastellingen en screenshotbeoordeling van 17 november](repairs/2026-11-16-shipping/documentation-check-2026-11-17.json)
- [Eerdere 18 geslaagde tariefquotes](repairs/2026-11-16-shipping/native-quotes.json)
- [Actuele Google-overdracht](repairs/2026-11-16-shipping/google-setup-check.json)
- [Eerdere productniveaucontrole in Google](repairs/2026-11-16-shipping/google-wall-tile-preview.json)
- [Dossier en eerdere uitvoering](repairs/2026-11-16-shipping/README.md)

Deze beurt zijn alleen documentatiebestanden in Git aangepast. Geen Shopify-/Google-instelling, producttype, prijs, voorraad of themafile gewijzigd. De beschermde canonieke config/settings_data.json-uitzondering blijft bestaan. Geen lokale Git-checkout in deze scratchmap en geen Windows-synchronisatie geclaimd.
