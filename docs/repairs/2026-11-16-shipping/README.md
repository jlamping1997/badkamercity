# Verzendtarieven en teksten live; Google-inrichting volgt

**Stand: 16 november 2026.** De vier tariefgroepen staan actief in de echte Nederlandse checkout. Alle 18 gecontroleerde tariefquotes zijn goed. De pagina [Bezorgen en afhalen](https://badkamercity.nl/pages/bezorgen-en-afhalen) is live bijgewerkt.

## Nu doen

**Eigenaarpublicatie is voltooid.** Thema **196690379018 — BadkamerCity - verzendtarieven per productgroep** is vers als MAIN teruggelezen. Niet opnieuw om publicatie vragen.

1. Eigenaar kiest in Shopify → Google & YouTube → Instellingen → Verzendgegevens: **Verzendgegevens handmatig instellen in Google Merchant Center** en slaat dit op. Productsynchronisatie aan laten. De dialoog staat open; automatische import is nu nog aan, er is niets opgeslagen.
2. Daarna uitvoering: instelling teruglezen; shipping_label voor pakket/pallet/glas/XXL vanuit gecontroleerde brondata toevoegen of afleiden, op enkele actuele Google-aanbiedingen testen en vervolgens groepsstaffels plus alleen de bevestigde PostNL-termijn instellen.

**Verse Google-controle:** account 5902025216 heeft nog één algemene service met €6,95 / gratis boven €100 en 2–5 werkdagen. Specific products toont geen selecteerbare labels en alleen aanleverinstructies. De service-editor is zonder opslaan geannuleerd. Shopify-interne collecties zijn geen automatisch aangemaakte Google-labels. Geen All-products-ééndagservice of vier overlappende algemene services opslaan. [Actuele Google-controle en hervatpunt](google-setup-check.json).

## Actieve tarieven

Alle bedragen inclusief btw; NL, één hoogste passend tarief. De hele productwaarde van de bestelling telt mee, inclusief verschillende merken/groepen. Geen extra bedrag per leverancier.

| Groep | Kosten | Gratis vanaf | Actieve artikelen |
| --- | --- | --- | ---: |
| Pakket, inclusief alle mozaïek en meubels | €6,95 t/m €100 | €100,01 | 23.579 |
| Gewone tegels en baden | €75 onder €500 | €500 | 3.562 |
| Complete douche-/badglasproducten | €45 onder €500 | €500 | 1.836 |
| XXL-tegels 120 × 250–320 cm | €300 inclusief krat en volledig transport | €1.000 | 0 |

Mozaïek heeft geen limiet van één of twee dozen. Kleine glasaccessoires zoals profielen, knoppen en scharnieren vallen onder pakket. Complete losse glasplaten vallen onder glastransport. Een gewone 30 × 100 cm wanddecor met ‘Mosaico’ in de titel blijft een gewone tegel; geen titelgok.

Vier nieuwe **ongepubliceerde interne collecties** vormen de automatische selectie. Hun aantallen tellen op tot alle 28.977 actieve producten. Geen nieuwe publieke categorie of navigatie, geen producttypen/tags in bulk vervangen. Nieuwe reguliere producten volgen de bestaande producttypen. XXL heeft nu geen actief artikel; bij gecontroleerde import is expliciet **bc_shipping_xxl** nodig. Controleer de maat en het lidmaatschap vóór publicatie.

## Native inrichting en herstel

NL-Market **94864998666** gebruikt één actieve value-based optie **1272199119114** met vier rate groups. Het algemene pakketbedrag is de fallback; de specifieke groep voegt geen tweede verzendbedrag toe. Beide bestaande verzendlocaties zijn behouden. Er is geen globale gratisgrens van €100 op de nieuwe optie, omdat die de transportgroepen zou overrulen.

De vorige optie **1251671343370** is inactief en ongewijzigd bewaard. [Vóórtoestand, actieve inrichting en exacte rollback-input](native-deployment.json). Bij rollback eerst verse actieve flags lezen, nieuwe optie uit / oude aan in één marketUpdate; latere wijzigingen nooit blind overschrijven. Herstel indien nodig ook [de vorige bezorgtekst](delivery-page-before.html). [Huidige bezorgtekst](delivery-page-after.html).

## Gecontroleerd

[18 echte tariefquotes](native-quotes.json), via afzonderlijke anonieme winkelwagens op het publieke NL-verzendtariefendpoint:

- €99,99 en precies €100 pakket: €6,95; €112 pakket: gratis.
- Gemengde merken onder €100: één keer €6,95.
- Mozaïek onder/boven €100, ook drie matten onder €100: pakketstaffel.
- Tegel €268,07: €75; twee dozen €536,14: gratis.
- Tegel + kraan €368,07: €75; samen €568,07: gratis.
- Glas €250: €45; precies €500: gratis; glas + kranen €499: €45.
- Tegel + glas €467,07: één keer €75; samen €503,07: gratis.
- Bad €1.199: gratis.

Geen order, betaling of klantcontact aangemaakt; geen gebruikerswinkelwagen aangepast. Alle 16 volledig afgeronde parallelle proefmanden zijn leeg teruggelezen. De twee eerste geslaagde quotes kwamen uit een onderbroken anonieme pilot; het opruimen van die pilotmand kon niet worden bevestigd. Geen voorraadreservering of order geclaimd.

**Bewijsgrenzen:** XXL is native teruggelezen op €300 / gratis vanaf €1.000, maar er bestaat nu geen echt XXL-artikel voor een mandproef. Er is geen actueel bad onder €500 (laagste gevonden €1.175); de betaalde palletstaffel is met echte tegels getest. Geen kortingsspecifieke mand of betaling getest. Het kortingssubtotal is de native cart-conventie. Geen mobiele visuele pass.

## Concept en bronbehoud

[Conceptcontrole en hashes](shipping-copy-preview.json). Het eerdere Brauer-thema is vóór de tekstwijziging gelijkgetrokken met de actuele MAIN: vijf ontbrekende/afwijkende werkdagenfiles native opgeslagen en dezelfde checksums teruggelezen; de overige 2.521 bestanden waren al gelijk. Daarna alleen twee locale-files aangepast. Zeven geschreven files bytegelijk teruggelezen. De browser toonde de juiste Draft en ‘Gratis pakketverzending boven €100’.

Publieke HTTP met preview_theme_id gaf MAIN terug; die antwoorden zijn **geen** succesvolle concepttest. [HTTP-resultaten en grenzen](public-checks.json). De live bezorgpagina gaf wel 200 en alle vier bedragen/het gemengde voorbeeld terug.

Canonieke wijzigingen op fix/product-cards-2026-10-14: alleen twee locale-files in shopify/current/. De vier werkdagenbronfiles waren al gesynchroniseerd. **config/settings_data.json blijft beschermd** door de bestaande .shopifyignore/pariteitsuitzondering; native concept/live-checksumgelijkheid sluit die canonieke bronuitzondering niet. Geen Windows-sync of volledige bronherstelpariteit geclaimd.

## Google en levertijd blijven apart

Deze beurt geen Google-instelling gewijzigd. De eerdere automatische afwijzing van één werkdag voor All products blijft gelden: groottransport heeft nog geen bevestigde dagtermijn. Eerst actuele sync en bestaande productlabels lezen; bij handmatige Merchant-tarieven de kanaalsynchronisatie bewust behandelen. Shipping labels moeten de groepen afbakenen, zodat een algemene goedkope service de palletkosten niet overschrijft. Geen minimum bestelbedrag instellen om lagere verzendkosten te verbergen; klanten kunnen onder de gratisgrens bestellen.

PostNL: maandag–vrijdag, 14:00 Europe/Amsterdam; vóór cutoff volgende werkdag, daarna twee werkdagen; vrijdag na cutoff/weekend dinsdag. Dit is al zichtbaar op de eerder gecontroleerde pakkettypen. Geen volgende-dagbelofte voor pallet/XXL. Alle huidige voorraadstatussen en M444AB-publicatie behouden.

## Bewijsbestanden

- [Actuele regels](rules.json)
- [Indeling, exacte producttypen, selectievoorwaarden en aantallen](product-group-classification.json)
- [Native voor/na en rollback](native-deployment.json)
- [Echte tariefquotes](native-quotes.json)
- [Tekstconcept](shipping-copy-preview.json)
- [Eerdere eigenaarpublicatie van de werkdagenmelding](weekday-publication.json)

De eerdere voorbereiding blijft in Git-historie en de bestaande dossierbestanden beschikbaar. Geen actieve schrijver na overdracht.
