# Browsercontrole Hotbath-keuzemenu's — 24 oktober 2026

Status: **PASS voor de hieronder uitgevoerde desktopsteekproeven**. Dit is geen controle van iedere combinatie of van mobiel.

## Omgeving en afbakening

- Browser: Chrome via de ondersteunde CUA-browserinterface.
- Domein: `https://badkamercity.nl`.
- Exact in de pagina waargenomen thema: **195649929482**, `BadkamerCity - Hotbath keuzemenus 24 okt`, role **unpublished**.
- Preview bleef na productwissels actief via de previewcookie, ook wanneer `preview_theme_id` niet meer in de URL stond. Thema-ID en role zijn opnieuw uit de DOM gelezen.
- Werkelijk gemeten `document.documentElement.clientWidth`: **1348 CSS-px**. Hoogte en device-pixel-ratio: **NOT_RECORDED**. Geen viewport-resize of mobiele emulatie uitgevoerd.
- Geen Shopify-instellingen, publicatie, betaling of bestelling via de browser gewijzigd. Alleen vier eigen tijdelijke testwinkelwagenregels toegevoegd en daarna verwijderd.

## Keuzemenu's en artikelwissels

| Groep | Werkelijk uitgevoerd en waargenomen |
|---|---|
| IBS70 | Vijf velden geladen: kleur (10 opties), diameter (20/25/30 cm), bevestiging (wandarm/plafondbuis 15/plafondbuis 30 cm), handdouche (staaf/rond), houder (wandhouder/glijstang). |
| IBS70-route | IBS70CR €1.541,01 → kleur GN: IBS70GN €1.937,02 → 25 cm: IBS70GN4 €2.066,01 → plafondbuis 15 cm: IBS70GN24 €2.120,02 → ronde handdouche: IBS70GN124 €2.304,01 → glijstang: IBS70GN1247 €2.619,01. Andere gemaakte keuzes bleven behouden. Terug naar wandhouder gaf IBS70GN124 €2.304,01. |
| BAA03 | 12 kleurkeuzes in het geladen keuzemenu. Verouderd messing BAA03AB €49,01 → geborsteld gunmetal PVD BAA03BGP €99,00. |
| BAA09 | 12 kleurkeuzes. Chroom BAA09CR €149,00 → geborsteld gunmetal PVD BAA09BGP €334,00. Bleef wandmodel; specificatie montage Wand en diepte 11,2 cm. |
| BAA10 | 12 kleurkeuzes. Chroom BAA10CR €99,00 → geborsteld gunmetal PVD BAA10BGP €199,00. Bleef vrijstaand, diepte 7,2 cm. Geen vermenging met BAA09 gezien. |
| Bestaande CB003 | Kleur, hoogte en type uitloop bleven werken: CB003CCR €199,00 → GN CB003CGN €244,00 → Hoog CB003HCGN €386,99 → Recht CB003HSGN €386,99. De volledige familie is niet stuk voor stuk getest. |

Alle genoemde bedragen en artikelnummers zijn uit de zichtbare productpagina's gelezen. De actuele leveranciersprijslijst is niet door deze browsercontrole opnieuw gevalideerd.

## Winkelwagencontrole

Elke regel is met de normale productkoopknop toegevoegd, met aantal 1. Daarna zijn de zichtbare productvariantlinks, prijzen en het totaal gecontroleerd.

| Artikel | Variant-ID | Aantal | Regelbedrag incl. btw |
|---|---:|---:|---:|
| IBS70GN124 — rond, 25 cm, plafondbuis 15 cm, wandhouder, geborsteld nikkel | 53187618275594 | 1 | €2.304,01 |
| BAA10BGP — vrijstaande zeepdispenser | 53187487531274 | 1 | €199,00 |
| BAA09BGP — wandzeepdispenser | 53795146694922 | 1 | €334,00 |
| BAA03BGP — handdoekhaak | 53795345826058 | 1 | €99,00 |

Zichtbaar totaal: **€2.936,01 inclusief btw**, Nederlandse verzending **Gratis**. Rekensom klopt. Eerder, met alleen BAA03BGP in de winkelwagen, was €99,00 + €6,95 verzending = **€105,95** zichtbaar.

Opruiming: alle vier eigen testregels via hun normale verwijderlinks verwijderd. Tussenstanden 3 → 2 → 1 artikel geobserveerd; eindtoestand **“Je winkelwagen is leeg”** geverifieerd. Geen checkout of order aangemaakt.

## Scrollherstel en regressie

Vóór de patch was een sprong bewezen bij IBS70 glijstang → wandhouder: `scrollTop` **439 → 0** terwijl de knop vóór de klik zichtbaar was op ongeveer y=446.

Na uitrol van de patch is de nieuwe script-URL uit de DOM waargenomen en `data-bc-preserve-position="true"` op IBS70, BAA03 en BAA09 gecontroleerd.

| Controle na patch | Voor wissel | Na stabilisatie | Resultaat |
|---|---|---|---|
| IBS70, eerste kleur CR → GN | scrollTop 439; container-top 100,6875 px | scrollTop 439; container-top 100,6875 px | PASS. Directe tussenmeting tijdens laden was scrollTop 446/top 99,7274 px. |
| BAA03, eerste kleur AB → BGP | scrollTop 310; container-top 193,71875 px | scrollTop 310; container-top 193,71875 px | PASS, exact dezelfde containerpositie. |
| BAA09, eerste kleur CR → BGP | scrollTop 442; container-top 35,328125 px | scrollTop 478; container-top 35,296875 px | PASS, afwijking ongeveer 0,03 px; andere titelhoogte opgevangen. |
| IBS70, vervolgwissels diameter/houder | Configurator in beeld | Configurator bleef in beeld | PASS voor zichtbare bruikbaarheid; native focus/autoscroll en tussenmetingen maken dit geen aanvullende exacte eindpositiemeting. |
| Eigen doorscrollen na wissel | PageDown na de diameterwissel | Uiteindelijk scrollTop 1258; geen terugtrekken waargenomen | PASS voor de uitgevoerde toetsinvoer. Native smooth-scroll gaf tussentijdse waarden. |
| CB003 buiten opt-in | `data-bc-preserve-position` ontbreekt (`null`) | Kleur/hoogte/uitloop werken | PASS. Geen scrollopt-in op deze bestaande groep. |

Na de locale-aanpassing is de zichtbare specificatiekop **“Specificaties”**; de eerder waargenomen `Translation missing: nl.bc_specs.heading` is op vervolgpagina's verdwenen.

## Bekende resterende punten en grenzen

- **BAA03BGP en BAA09BGP missen een productfoto** in de gecontroleerde galerij en winkelwagen. BAA10BGP en de geteste IBS70-uitvoering toonden wel een foto. Dit is bestaande productinhoud, geen verkeerde kleurkoppeling.
- **mobile_NOT_TESTED**: geen iPhone/Android, smalle viewport, touchbediening of mobiele scrollgarantie getest.
- Niet alle productcombinaties doorgeklikt; geen volledige familie- of catalogusdekking geclaimd.
- Geen checkout, verzendtariefberekening in checkout, betaling, ordermail of orderafhandeling getest.
- Screenshots zijn alleen intern in tooluitvoer bekeken; er zijn door deze controle geen screenshotbestanden of Library-artikelen gemaakt.
