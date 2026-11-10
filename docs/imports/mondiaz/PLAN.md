# Mondiaz toevoegen — later traject

10 november 2026. **BACKLOG / lage prioriteit in deze fase.** Eigenaar geeft aan Mondiaz te kunnen verkopen. Alleen een eerste bronscope gemaakt; geen volledige scrape, downloadbatch, Shopify-import of merkpublicatie gestart.

## Wat er aantoonbaar beschikbaar is

| Bron | Eerste bevinding | Gebruik bij de latere proef |
| --- | --- | --- |
| [Fabrikantsite](https://www.mondiaz.nl/) | Menu met meubelsets, losse onderkasten, hoge/halfhoge kasten, toiletmeubels, wastafels, kommen, bladen, toiletten, baden, spiegels/spiegelkasten en toebehoren | Bestaande BadkamerCity-categorieën hergebruiken. Niet voor ieder merk een kopieboom maken. |
| [Meubeloverzicht](https://www.mondiaz.nl/badmeubel-met-wastafel/) | Gepagineerde lijst; artikelcodes op kaarten. Filters onderscheiden meubelmaat van wastafelmaat, meubelkleur van wastafelkleur, bakpositie, kraangaten en lade-indeling | Een koopbare SKU en een productfamilie apart modelleren. Aantallen zijn veel configuraties, geen bewezen aantal unieke modellen. |
| [JOYA-DLUX-proefartikel](https://www.mondiaz.nl/artikel/1400432/joya-dlux-51-6cm-toiletmeubel-ronding-links-kleur-oak-wastafel-faye-positie-rechts-zonder-kraangat-kleur-meli.html) | Openbare productinhoud, prijs incl./excl. btw, foto's met verschillende rollen, lijntekening, maataansluiting en videoreferentie zichtbaar via webretrieval | Exact artikel koppelen; verkoopeenheid, kast/wastafelcombinatie en gekozen uitvoering controleren. Foto, tekening en sfeerbeeld apart labelen. Geen fabrikantlevertijd als eigen winkelvoorraad tonen. |
| [Toiletmeubels](https://www.mondiaz.nl/fonteinmeubel-met-wastafel) en [LED-spiegels](https://www.mondiaz.nl/spiegel-met-led/) | Afzonderlijke productgroepen met eigen configuratie | Geschikt als andere producttypen voor een kleine proef; geen meubelkeuzes op spiegels hergebruiken. |
| [3D-configurator](https://www.mondiaz.nl/3d-badkamermeubel-configurator/) | Afzonderlijke configurator aanwezig | Niet meteen nabouwen of combinaties genereren. Eerst bestaande verkoopartikelen en leveranciersstructuur begrijpen. |
| Officiële PDF’s in /files/ | Gevonden: ALAN-presentatie, LAGOM-maatwerk en VICA-prijslijst. De namen/inhoud verwijzen naar oudere versies rond 2020 | Kandidaten voor maat-/modelonderzoek, geen actuele prijslijst. Versie, datum en toepasselijkheid per artikel controleren. |

Voorbeelden van de gevonden bestanden: [ALAN](https://www.mondiaz.nl/files/ALAN%20presentatie%20maatwerk%20MONDIAZ%20PDF%2027-04-2020%20PDF%20versie%2020.02%20beta_16901262607020.pdf), [LAGOM](https://www.mondiaz.nl/files/Lagom%20maatwerk%2020.024438762570270.pdf), [VICA](https://www.mondiaz.nl/files/VICA%20adviesprijslijst%20presentatie%20maatwerk%20MONDIAZ%2027-04-2020%20PDF_16901262607079.pdf). Dit is een kleine eerste inventaris, geen volledige bestandslijst. Een directe HTML-download van het proefartikel kreeg HTTP403 in deze omgeving. Webretrieval lukte wel; er is nog geen werkende scraper, publieke feed, API of complete bronexport aangetoond.

## Kortste betrouwbare route

Eerst nagaan of Mondiaz een dealerbestand, XML/CSV/Excel-feed, actuele prijslijst en mediapakket kan leveren. Dat voorkomt het reconstrueren van duizenden configuraties. Bestaande exports of een feed hebben voorrang op een nieuwe grote scraper. Beschikbaarheid en gebruik van zo’n bestand zijn nu nog onbekend.

Als we later moeten scrapen: eerst sitemap/lijstpaginering in kaart brengen, vervolgens alleen productdetailpagina’s en werkelijk gekoppelde openbare media/documenten. Geen 3D-assets, CAD-verzameling of hele downloadbibliotheek als startvoorwaarde. Bewaar bron-URL, fabrikantcode, taal, versie/datum, bestandstype en checksum. Alleen nieuwe of gewijzigde records opnieuw ophalen.

## Datamodel dat vóór import moet kloppen

- Merk + exacte fabrikantartikelcode als identiteit; EAN alleen aanvullend. Dubbele codes en gewijzigde samenstellingen blokkeren.
- Eén productfamilie met werkelijk beschikbare SKU’s. Geen verzonnen combinatie van kastkleur, wastafelkleur, maat, bakpositie, kraangaten en draairichting.
- Meubelbreedte en wastafelbreedte apart: de fabrikant licht toe dat een blad/wastafel bij sommige series breder kan zijn dan de kast. Maten niet uitwisselen om een filter te vullen.
- Losse onderkast, complete set, los blad, wastafel, spiegel en onderdelen apart houden. ‘Compleet’ alleen met bevestigde setinhoud.
- Foto’s koppelen aan exacte SKU/uitvoering en rol. Een gedeeld seriebeeld blijft seriebeeld; verkeerde kleur niet als zekere productfoto inzetten.
- Actuele advies-/verkoopprijs, btw-basis en eventuele toeslagen uit elkaar houden. Geen inkoopcondities in publieke Git. Geen oude PDF-prijzen overnemen als actuele verkoopprijs.
- Gebruik de bestaande korte/ lange titelvelden, filters en keuzesystemen. Geen los Mondiaz-platform bouwen als brondataherstel voldoende is.

## Latere batches

| Batch | Omvang | Eindcriterium |
| --- | --- | --- |
| M0: bronnen | Eén bronregister en representatieve voorbeelden | Bekend welke data uit feed, pagina, foto of document komt en wat ontbreekt |
| M1: proef | 5–10 SKU’s: meubelset, losse kast, toiletmeubel, wastafel en spiegel | Identiteit, maatbetekenis, prijs/btw en media handmatig inhoudelijk gecontroleerd |
| M2: één familie | Eén serie met beperkte echte keuzes | Iedere keuze één bestaand verkoopartikel; foto/SKU/prijs/setinhoud kloppen na wisselen |
| M3: beperkte import | Circa 25–50 gecontroleerde SKU’s als concept | Geen nieuwe URL-duplicaten; categorieën, filters, card title en PDP-inhoud correct |
| M4: uitbreiden | Per producttype/serie | Herhaalbaar register met READY/HOLD, herstelpad en gerichte updates |
| M5: merkpagina | Na de eerste betrouwbare catalogus | Nuttige productgroepen, filters en eigen merkinhoud; aansluiten op het bestaande merkplan |

Eerst de huidige categorie-/filter-/titelbasis afronden. **Volgende Mondiaz-handeling wanneer dit prioriteit krijgt:** beschikbare dealerbestanden controleren en een definitieve kleine proefselectie maken. Geen informatie bij de eigenaar opvragen die we eerst uit bestaande bronnen kunnen halen.
