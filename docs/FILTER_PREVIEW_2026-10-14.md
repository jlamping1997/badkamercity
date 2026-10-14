# Gecontroleerde filters — conceptcontrole 14 oktober 2026

> **Aanvulling na merchantfeedback:** de verplichte `bcfilters=1`-schakelaar is verwijderd uit concept `195038216458`, omdat de merchant bij gewone conceptnavigatie geen filters zag. De filters laden nu standaard in de conceptcollecties. Wastafelkranen is zonder queryparameter in de browser gecontroleerd: externe bediening actief, 454 producten. Alle 10 regressietests draaien nu zonder proefparameter en slagen; themevalidatie revisie 7 en exacte Shopify-readback zijn geslaagd. MAIN blijft `194981003530`; deze standaardactivering geldt niet voor de gepubliceerde site. De opt-inbeschrijving hieronder is de eerdere stand van deze dag. Herstel via de vorige concept-JS brengt de opt-in terug; alleen verwijderen van de URL-parameter schakelt deze nieuwe conceptcode niet meer uit.

## Actuele stand

MAIN blijft `194981003530`. Alleen ongepubliceerd concept `195038216458` (Afronding basis 10 okt) is bijgewerkt. De opt-in `?bcfilters=1` blijft verplicht; gewone bezoekers zijn niet omgeschakeld. Het externe snippet staat nu in standaard collectieproductlijsten, met native terugval voor ontbrekende profielen, API-fouten en afwijkende productaantallen.

De merchant heeft op de VPS de volledige indexproef (11.050 producten), de 20 API-controles en de HTTPS/CORS-routecontrole uitgevoerd en de geslaagde uitvoer in de werksessie aangeleverd. Oude root- en `/v3/`-routes zijn behouden. Het concept gebruikt `/verified` op de bestaande externe filterhost. Serverbron, geheime instellingen en volledige productexports staan niet in dit openbare themarepository.

## Wijzigingen

- Eurobedragen worden naar gehele centen omgezet; labels, invoer en actieve filters tonen euro's.
- Booleans tonen Ja/Nee, met oorspronkelijke true/false verzoekwaarden.
- Aantallen gebruiken gehele invoer; fysieke maten kunnen decimalen bevatten.
- Open filtergroepen en actieve invoer blijven behouden na vernieuwen.
- Snel wijzigen van beide bereikgrenzen bewaart beide waarden; alleen het zoeken wordt vertraagd.
- Externe browsergeschiedenis voorkomt dat Dawn tegelijk een native lijst terugplaatst. Na terugval blijft de native geschiedenis werken.
- Dubbele maateenheden in filterlabels zijn verwijderd.

## Uitgevoerde controles

| Controle | Bewijs/resultaat |
| --- | --- |
| Shopify readback | Alle drie gewijzigde bestanden exact teruggelezen; MAIN ongewijzigd, concept UNPUBLISHED |
| Liquid/theme validatie | Revisie 6: drie gewijzigde bestanden geldig; cachefallback na netwerkfout bij docsupdate |
| Node/JSDOM | 10 gerichte tests geslaagd, inclusief prijs, beide bereikgrenzen, booleans, refresh, history, API-fout en afwijkend indexaantal |
| Wastafelkranen basis | 454 actuele leden; 360 Hotbath, 66 Wiesbaden, 28 JEE-O in actuele index |
| Chroom + opbouw productsoort/montage | 41 resultaten in echte desktoppreview |
| Zelfde selectie, maximaal €200 | 12 resultaten; zichtbare prijzen maximaal €200, 7 Hotbath en 5 Wiesbaden |
| Prijssortering en browser terug | Oplopende prijzen; terug behoudt externe lijst en 12 resultaten |
| Inbouwdouchesets, chroom, hoofddouche 30 cm | 204 resultaten; pagina 2 toont 24 kaarten, pagina 2 van 9 |
| Inclusief hoofddouche | Ja met 204 als facetkeuze bij bovenstaande selectie |
| Inbouwdouchesets, chroom, hoofddouche 25 cm | 98 resultaten na echte invoer van beide grenzen |
| Hoofddouche 31 cm | 0 resultaten, geen API-fout |
| Ongeldig omgekeerd bereik | API weigert; native lijst en foutmelding blijven beschikbaar in echte browser |

Lokale testopdracht: `NODE_PATH=/pad/naar/tijdelijke/node_modules node --test scripts/test-external-filters.cjs`. Alleen testafhankelijkheid `jsdom` is nodig; geen runtime-afhankelijkheid voor de webshop toegevoegd.

## Open werk en grenzen

- **NOT_TESTED:** visuele controle en bediening in een echte mobiele viewport; huidige browserbediening biedt geen viewport/emulatie.
- Niet alle 148 gevulde collectieprofielen zijn visueel gecontroleerd. Controleer volgende productfamilies, passende facetkeuzes en ontbrekende gegevens vóór brede activering.
- De 742 bevestigde service/reparatieartikelen worden door de geteste API buiten algemene koopfilters gehouden; exact volledig artikelnummer en onderdelenprofielen blijven beschikbaar. Dit bewijst niet dat ieder onbekend onderdeel al geclassificeerd is.
- De gewone zoekbalk/predictive search is nog niet aangesloten op deze gecontroleerde filterservice. Oude zoekvraagtesten zijn geen actuele test van deze nieuwe collectiebediening.
- Bronconflicten en ontbrekende kenmerken blijven ontbrekend; geen 100%-dekkingclaim of ingevulde aannames.
- Indexverversing bij latere prijs/productwijzigingen en operationele bewaking moeten nog worden vastgelegd vóór publicatie.
- Geen MAIN-publicatie, checkoutcontrole of volledige winkelbrede acceptatie in deze ronde.

## Terugval/herstel

Zonder `bcfilters=1` gebruikt de collectie gewone Shopify-filtering. Bij externe fouten worden de oorspronkelijke native productnodes en bediening teruggezet. Voor themacodeherstel: herstel uitsluitend de drie hieronder genoemde conceptbestanden vanuit basiscommit `aa22393f2459a19a771278a8bd60c4d12db27fe1`; publiceer MAIN niet. De Caddy-back-up en routecontrole zijn op de VPS vastgelegd in het resultaatbestand van de merchant.

Gewijzigd: `assets/bc-external-filters.js`, `snippets/bc-external-filters.liquid`, `sections/main-collection-product-grid.liquid`. Het bijbehorende testscript is `scripts/test-external-filters.cjs`.
