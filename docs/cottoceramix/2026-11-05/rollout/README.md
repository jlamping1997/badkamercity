# COTTO-03 — gecontroleerde uitrol Cottoceramix

5 november 2026. **PUBLISHED_VERIFIED / NEXT_BATCHES_OPEN.**

824 nieuwe artikelen zijn ACTIVE en op de Webshop gepubliceerd, onafhankelijk teruggelezen op alle 832 aangemaakte ID’s: 824 gepubliceerd, acht DRAFT/niet gepubliceerd, nul afwijkingen. Met de behouden 22 Re-Bel-artikelen zijn 846 Cottoceramix-artikelen actief. Dit rondt de eerste grote uitrolbatch af; 2.916 bronartikelen en acht conceptconflicten blijven open.

## Scope en stand

De eigenaar gaf opdracht het Cottoceramix-assortiment in kwaliteitsbatches online te zetten, met Cottoceramix als winkelmerk en de goedgekeurde vierkante tegelkeuze.

| Scope | Aantal | Bewezen eindstand |
| --- | ---: | --- |
| Gecorrigeerde werkset | 3.770 | Vastgestelde importscope |
| Re-Bel reeds bestaand | 22 | Bestaande identiteit en gegevens behouden |
| Nieuwe artikelen aangemaakt en teruggelezen | 832 | Inclusief vijf Monaco-R-artikelen met afzonderlijk bevestigd fabrikantgewicht |
| Voor activering/publicatie geschikt | 824 | ACTIVE en Webshop-publicatie teruggelezen |
| Nieuwe artikelen met bronconflict | 8 | Eigen HOLD-groep, DRAFT; niet publiceren |
| Nog niet aangemaakt uit de werkset | 2.916 | Afzonderlijke vervolgbatches; geen automatische vrijgave |
| Totaal actief na eindcontrole | 846 | 824 nieuwe plus 22 bestaande, bevestigd |

De bron bevat daarnaast 146 bewust uitgesloten samples/vervallen artikelen. De XML telt drie extra records buiten de gecorrigeerde werkset; die vragen een afzonderlijke bronbeoordeling.

## Bron en gegevenscontract

Uitgangspunt is de gecorrigeerde werkmap versie 2 van 5 november, SHA256 `2c8764005f254f9d3d8ace119cbebb82bb8f335b8e7eb8ad37ec94577c808d45`. De beschikbare XML is gegenereerd op `2026-11-05T12:01:36`; de leverancier geeft hierbij geen tijdzone. Een nieuwe ophaalpoging gaf HTTP403. Dit bronmoment is bewaard als momentopname en niet als een later uitgevoerde live voorraadcontrole gepresenteerd.

Eén leveranciers-SKU blijft één Shopify-product met één verkochte variant. De SKU-controle over de volledige werkset vond uitsluitend de 22 bestaande Re-Bel-identiteiten. Nieuwe titels en vendor gebruiken Cottoceramix; oorspronkelijke fabrikant, serienamen en bronfeiten blijven intern herleidbaar. Prijs is inclusief btw per verkochte doos, native eenheidsprijs per m²; de bestelhoeveelheid is het gehele aantal dozen. m²/doos komt uit de bevestigde verpakking, nooit uit een berekende omhullende rechthoek van een gevormde tegel. Ongeldige EAN's zijn weggelaten.

Een mapper-regressie is vóór publicatie gevonden en hersteld: de gekozen maattekst **Z/AA** en dikte **AF** moeten leidend zijn; oudere Excel-numerieke kolommen AB/AC/AE overschreven deze aanvankelijk. Reeds aangemaakte concepten zijn gericht hersteld. De volledige uiteindelijke veldvergelijking is tegen de gecorrigeerde verwachte input uitgevoerd. Prijzen, SKU's, gewichten, URL's en overige bestaande artikelidentiteiten zijn daarbij behouden.

## Keuzegroepen

Er zijn **125 technisch samenhangende kleurfamilies**, plus één gecontroleerde Monaco-R-familie. Dit is geen verklaring dat alle menus exact van de leverancier zijn gekopieerd. Onderzoek van echte bronmenus leverde de werkwijze op; waar het bestaande scherm geen afzonderlijke uitvoering/modelvorm kan weergeven, zijn de artikelen op expliciete bronwaarden opgesplitst in model-, afwerkings- of formaatfamilies.

Dezelfde vierkante kleurkeuze en tegelcalculator worden hergebruikt. Binnen een kleurkeuze veranderen geen andere technische keuzen ongemerkt. Alleen brongebonden diktewissels bij een expliciete formaatkeuze blijven bestaan. Onbeschikbare combinaties zijn niet uitgevonden. Een uniforme selector over de afgescheiden model-/formaatfamilies blijft afzonderlijk UX-vervolgwerk.

De acht bronconflicten blijven geïsoleerd: Doha-R `VA3201`, `VA3202`, `VA3203` en Marea `MAR128L`, `MAR129L`, `MAR130L`, `MAR131L`, `MAR132L`. Bij Doha spreken gekozen formaten en bronnamen elkaar tegen; bij Marea spreken titel, afwerking of kleurlabel elkaar tegen. Geen maat, kleur of glansgraad geraden.

## Uitvoering en bewijs

De algemene bulkmutatie werd door de connector geweigerd. Er is geen omweg via onbeheerde credentials gebruikt; de toegestane Admin-productmutaties zijn in begrensde batches uitgevoerd, met exacte SKU-identiteiten, herstelkopieën en teruglezing. Bestaande producten zijn niet blind via volledige lijstvervanging bijgewerkt. Groepsvelden en groepsreferenties zijn apart op de aangemaakte product-ID's aangesloten.

De volledige controle vóór publicatie slaagt met **64.900 controles over alle 832 nieuwe artikelen**, inclusief veldwaarden, verpakking, prijs/eenheidsprijs, gewicht, voorraadinstellingen, metafields, groepsreferenties en gereed media. Vijftien exacte leveranciersfoto's met een onjuist response-contenttype zijn als echte JPEG gestaged en gericht gekoppeld; geen vervangende sfeerbeelden of verzonnen productfoto's gebruikt. De verifier accepteert uitsluitend betekenisgelijke HTML-entiteiten; afwijkende tekst of markup blijft blokkeren.

Het volledige keuzematrixonderzoek gebruikt de bestaande echte selectiekern. Het bewijst geen visuele browserkwaliteit of volledige bronmenu-equivalentie. Funky is als eerste echte bronmenu-batch met twaalf kleuren, prijs, calculator en kleurwissel in Chrome gecontroleerd. Live Chrome-proeven: Funky Amber→Seaport behoudt formaat, alle twaalf kleuren laden; 10 m² + 10% geeft veertien dozen en €1.234,24. Twee dozen daadwerkelijk toegevoegd: 1,68 m², €176,32, bevestiging/cart tonen per doos en de juiste levering. Alleen de eigen testregel verwijderd; cart leeg. Monaco-R Beige→Verde behoudt 80×80 cm en alle vijf kleuren laden; €79,95/m² en €102,34/doos van 1,28 m². Alle 824 Webshop-publicaties en acht ongepubliceerde concepten onafhankelijk teruggelezen; nul afwijkingen. Checkout, adresafhankelijke verzending, betaling en fysieke telefoon zijn in deze uitrol niet volledig opnieuw getest. Zoekindex-/Google-opname blijft een apart systeem.

Er zijn geen themabestanden gewijzigd door deze import. De actuele, reeds door eigenaar gepubliceerde MAIN is `196238639370 — BadkamerCity - Re-Bel tegelkeuze`; die rol en de drie kleurcomponentchecksums zijn na publicatie van de producten opnieuw bevestigd. Geen themefilewrite of themapublicatie in COTTO-03.

## Herbruikbare uitvoering

Broncode staat op de bestaande codebranch onder `scripts/cottoceramix/`. Alleen code, testfixtures en openbare beleids-/voortgangsdocumentatie horen in Git. Volledige leveranciersbestanden, privéplannen, herstelkopieën, API-receipts, credentials en browserbeelden horen niet in de publieke repository.

```sh
python3 scripts/cottoceramix/build_import_plan.py \
  --source-json /private/normalized-products.json \
  --output-dir /private/import-plan \
  --existing-json /private/current-sku-registry.json \
  --menu-evidence /private/verified-menu-groups.json \
  --collections-json /private/verified-collection-ids.json \
  --source-snapshot 2026-11-05T12:01:36

python3 scripts/cottoceramix/subdivide_groups.py \
  --planned /private/import-plan/products.json \
  --normalized /private/normalized-products.json \
  --publication-review /private/publication-review.json \
  --output-dir /private/final-plan

node scripts/cottoceramix/audit_choice_matrix.mjs /private/final-plan/final-products.json

python3 scripts/cottoceramix/verify_readback.py \
  --planned /private/final-plan/final-products.json \
  --readback /private/full-admin-readback.json \
  --active-skus /private/expected-active-skus.json \
  --require-group-refs \
  --output /private/readback-verification.json

python3 -m unittest discover -s scripts/cottoceramix -p 'test_*.py' -v
```

De oorspronkelijke v2-input blijft onveranderd; de afgeleide eindkopie bevat uitsluitend de bedoelde groepsmetadata. Monaco-R-bronaanvulling en eventuele gerichte media-/veldreparaties moeten als afzonderlijk, gecontroleerd herstel worden vastgelegd. Testen van de scripts: **29 betekenisvolle controles PASS**; maak geen Windows-lokale uitvoeringsclaim.

## Latere feed: eigenaarschap en uitzonderingen

Er is **geen automatische Cottoceramix-feedworker geïmplementeerd of ingepland**. Voor de latere koppeling geldt:

- Koppel op leverancier plus exact SKU en bewaar de echte Shopify-/variant-ID's; herhaalde verwerking mag geen duplicaten maken.
- Voorraad en levertijd mogen later uit een succesvol gevalideerde feed vernieuwen, met bronmoment en laatste geslaagde verwerking.
- Titels, winkelmerk, SEO, omschrijving, groepen, groepsreferenties en handmatige correcties blijven beschermd tegen een generieke overschrijving.
- Prijsverversing vraagt expliciet beleid voor m²-prijs, verpakking en doosprijs; handmatige prijs-/verpakkingscorrecties blijven afzonderlijk herleidbaar.
- Meld nieuwe/verdwenen SKU's, wijziging van m²/doos, ongekende verkoopeenheden, conflicterende gewichten/afwerking, opvallende prijswijzigingen, mislukte verwerking en verlopen verwachte leverdatums. Grenzen en automatische vervolgacties moeten vooraf worden gekozen.
- Een ontbrekend veld wordt niet stil nulvoorraad of een verzonnen levertijd. Bij een fout blijft de laatste gevalideerde toestand bewaard en ontstaat een zichtbare uitzondering.

Zo wordt later het normale onderhoud automatisch en blijft controle gericht op echte uitzonderingen. Dat vervangt geen periodieke controle van bestelbaarheid, nieuwe/vervallen artikelen en bronkwaliteit.

**Exact één volgende handeling voor COTTO-03:** de aparte stuks-/m¹-verkooproute voor onder meer Casablanca-randstukken en Enso afbakenen en als volgende kleine batch voorbereiden, met de bestaande SKU-identiteiten en bronprijsbasis. Geen nieuwe bulkimport voordat die verkoopeenheid aantoonbaar klopt. Geen actieve schrijver of import-/feedworker na overdracht.

Herstel: uitsluitend de 824 aangemaakte/gepubliceerde product-ID’s uit deze batch van Webshop ontkoppelen en naar DRAFT terugzetten. De acht HOLD-producten blijven concept. De 22 bestaande Re-Bel-artikelen en andere merken niet terugrollen. De privébatch bevat exacte input, actuals, register, herstelfoto’s en correctie-/uitzonderingslijsten.

Bewijs is gefaseerd verzameld: volledige basisvelden, vervolgens de daadwerkelijk gewijzigde groeps- en fotovelden, en ten slotte status/publicatie. Het is geen wereldwijde atomaire Shopify-snapshot. API-operaties zijn door de koppeling tegen Admin2026-10 gevalideerd; de losse Toolkit-GraphQL-validator kon niet worden gestart zonder zijn ontbrekende schemabundel. Er is daarom geen afzonderlijke Toolkit-Admin-PASS geclaimd.

