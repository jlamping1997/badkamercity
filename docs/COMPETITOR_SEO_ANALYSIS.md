# Concurrentie- en SEO-structuuranalyse

> **Taak:** `BC-DISC-002`
>
> **Status:** `DONE`
>
> **Onderzoeksdatum:** 2026-08-05
>
> **Menselijk goedgekeurd:** 2026-08-05
>
> **Scope:** openbare, read-only steekproef van BadkamerXXL, Sanitairwinkel en Sanitairkamer
>
> **Wijzigingen buiten documentatie:** geen

## 1. Statuslabels

- **BEWEZEN:** rechtstreeks vastgesteld in openbare HTML, paginabron, metadata, structured data, `robots.txt`, sitemap of HTTP-respons binnen deze steekproef.
- **AFGELEID:** redelijke conclusie uit meerdere bewezen observaties; geen bewezen werking of ontwerpbesluit.
- **NIET TOEGANKELIJK:** binnen de toegestane methode niet betrouwbaar bereikbaar of niet werkelijk testbaar.
- **NOG ONDERZOEKEN:** aanvullend bewijs is nodig voordat een conclusie bruikbaar is voor ontwerp of implementatie.
- **OPEN BESLISSING:** vereist later een expliciet menselijk besluit voor BadkamerCity.

Een waarneming bij een concurrent is geen toestemming om tekst, beeld, ontwerp of code over te nemen. Aantallen, prijzen, levertijden, beoordelingen en commerciele claims zijn momentopnamen.

## 2. Scope, methode en beperkingen

### Uitgevoerd

- Normale openbare pagina's, interne links, HTML en paginabron zijn representatief onderzocht.
- Canonicals, robotsmeta, titels, metabeschrijvingen, headings en publieke JSON-LD zijn op kernpaginatypen gecontroleerd.
- `robots.txt` en de bereikbare XML-/HTML-sitemapstructuur zijn gecontroleerd.
- Per site zijn homepage, hoofdnavigatie, een hoofdcategorie, minimaal twee subcategorieen, twee productpagina's, een merkroute, content, service en showroom onderzocht.
- Categorie-HTML is gebruikt om filters, sortering, kaarten, paginering en filter-URL-patronen vast te stellen.
- Er is geen onbeperkte of volledige crawl uitgevoerd.

### Niet uitgevoerd

- **NIET TOEGANKELIJK:** werkelijke mobiele of visuele browserweergave, hovergedrag, drawers, touchinteractie en responsive layout. De gebruikte tooling leverde geen betrouwbare interactieve desktop-/mobiele browsercontrole. HTML alleen is daarvoor geen bewijs.
- **NIET TOEGANKELIJK:** toetsenbord-, screenreader- en focusgedrag.
- **NIET TOEGANKELIJK:** voorspellend zoeken, zoekresultaten, nulresultaten en zoekfouten. Alle drie sites sluiten hun zoekroutes in `robots.txt` uit; er is geen formulier verstuurd.
- **NOG ONDERZOEKEN:** client-side filtergedrag, wishlist, snelle acties, calculators, configurators en productopties na interactie.
- **NIET TOEGANKELIJK:** werkelijke indexdekking, rankings, Search Console, Core Web Vitals, analytics, consentstatus, pixels, apps en externe integraties.
- Er zijn geen accounts gebruikt, formulieren verstuurd, persoonsgegevens gelezen of bestellingen geplaatst.
- Na een `429` van Sanitairkamer is geen verdere aanvraag naar dat domein gedaan.

## 3. Steekproef en bronnen

Methodecodes: `HTML` = openbare gerenderde tekst/HTML en interne links; `SOURCE` = metadata/paginabron/JSON-LD; `ROBOTS` = `robots.txt`; `XML` = openbare sitemap; `HTTP` = responsstatus en eind-URL. Alle bezoeken waren op 2026-08-05.

### 3.1 BadkamerXXL

| URL | Paginatype | Methode | Resultaat of beperking |
| --- | --- | --- | --- |
| https://www.badkamerxxl.nl/ | Homepage, hoofdnavigatie en vertrouwen | `HTML`, `SOURCE` | **BEWEZEN:** brede productnavigatie, service-/contentroutes, metadata en structured data |
| https://www.badkamerxxl.nl/badkamermeubels | Hoofdcategorie | `HTML`, `SOURCE` | **BEWEZEN:** subcategorieen, filters, sortering, kaarten, paginering en SEO-output |
| https://www.badkamerxxl.nl/badkamermeubels/badmeubel-sets | Subcategorie 1 | `HTML` | **BEWEZEN:** categoriepad, kaarten en filterstructuur |
| https://www.badkamerxxl.nl/badkamermeubels/badmeubel-sets/met-wastafel | Subcategorie 2 | `HTML` | **BEWEZEN:** verdere categoriediepte en productlijst |
| https://www.badkamerxxl.nl/kranen/wastafelkranen | Aanvullende subcategorie | `HTML` | **BEWEZEN:** producttype-afhankelijke filters |
| https://www.badkamerxxl.nl/search?q=%7Bquery%7D | Zoekroute uit bron | `SOURCE`, `ROBOTS` | **NIET TOEGANKELIJK:** `/search?` is uitgesloten; route niet bezocht en formulier niet verstuurd |
| https://www.badkamerxxl.nl/mondiaz-kurve-60cm-badmeubel-kleur-walnut-met-1-lade-en-0-deuren-wastafel-cloud-midden-zonder-kraangat-talc-krvclo601l0d0km-wal-tal | Productpagina 1 | `HTML`, `SOURCE` | **BEWEZEN:** gekoppelde opties, prijs, levertijd, specificaties, plus-/aandachtspunten en setaanvulling |
| https://www.badkamerxxl.nl/hotbath-guy-afbouwdeel-tbv-inbouw-wastafelkraan-20-cm-uitloop-tuscan-bronze-gy005dext20tb | Productpagina 2 | `HTML`, `SOURCE` | **BEWEZEN:** PDP-structuur, optie-/service-informatie en Product-data |
| https://www.badkamerxxl.nl/badkamermeubels/brauer | Merk-categorieroute | `HTML` | **BEWEZEN:** merk binnen categorie, series en categorie-oversteken |
| https://www.badkamerxxl.nl/merken | Merkenoverzicht | `HTML` | **NOG ONDERZOEKEN:** heading zichtbaar; volledigheid leek dynamisch en is niet bewezen |
| https://www.badkamerxxl.nl/blog | Advies en inspiratie | `HTML` | **BEWEZEN:** contenttaxonomie per onderwerp en contenttype |
| https://www.badkamerxxl.nl/bezorgen | Levering | `HTML` | **BEWEZEN:** productspecifieke vervoerders en tracking via account |
| https://www.badkamerxxl.nl/retourneren-en-annuleren | Retouren | `HTML` | **BEWEZEN:** retourinformatie en verwijzing naar extern retourproces; niet geopend |
| https://www.badkamerxxl.nl/showroom | Showroom | `HTML` | **BEWEZEN:** een showroom, afspraak-/adviespropositie en 3D-ontwerp |
| https://www.badkamerxxl.nl/robots.txt | Robots | `ROBOTS` | **BEWEZEN:** zoek-, vergelijk-, account-, cart- en veel facetparameters uitgesloten |
| https://www.badkamerxxl.nl/sitemap.xml | Sitemapindex | `XML` | **BEWEZEN:** tien sitemaps voor categorieen, content, landingspagina's, statische pagina's, producten en afbeeldingen |
| https://www.badkamerxxl.nl/sitemap-images.xml | Afbeeldingssitemap | `XML` | **BEWEZEN:** afzonderlijke publieke afbeeldingssitemap |
| https://www.badkamerxxl.nl/bc-disc-002-niet-bestaande-pagina | Foutpagina | `HTTP`, `SOURCE` | **BEWEZEN:** HTTP 404 met fouttitel, maar robotsmeta `index,follow` |

### 3.2 Sanitairwinkel

| URL | Paginatype | Methode | Resultaat of beperking |
| --- | --- | --- | --- |
| https://www.sanitairwinkel.nl/ | Homepage, hoofdnavigatie en vertrouwen | `HTML`, `SOURCE` | **BEWEZEN:** brede productnavigatie, acties, advies, service en showrooms |
| https://www.sanitairwinkel.nl/badmeubelen/ | Hoofdcategorie | `HTML`, `SOURCE` | **BEWEZEN:** subcategorieen, omvangrijke filters, kaarten, paginering en SEO-output |
| https://www.sanitairwinkel.nl/badmeubelen/meubelsets/ | Subcategorie 1 | `HTML` | **BEWEZEN:** productlijst, sortering en een resultaatweergave met bovengrens van 20.000 |
| https://www.sanitairwinkel.nl/kranen/wastafelkranen/ | Subcategorie 2 | `HTML` | **BEWEZEN:** categoriespecifieke filterstructuur en kaarten |
| https://www.sanitairwinkel.nl/zoeken/?tn_q=%7Bquery%7D | Zoekroute uit bron | `SOURCE`, `ROBOTS` | **NIET TOEGANKELIJK:** `/zoeken/*` is uitgesloten; route niet bezocht en formulier niet verstuurd |
| https://www.sanitairwinkel.nl/p/77580261/saniclass-chaci-badkamermeubelset-80x46x55cm-keramische-wastafel-wit-1-wasbak-1-kraangat-2-lades-noten-hout | Productpagina 1 | `HTML`, `SOURCE` | **BEWEZEN:** opties, reviews, levertijd, showroomstatus, plus/min, documenten en aanvulling |
| https://www.sanitairwinkel.nl/p/77746897/fortifura-calvi-wastafelkraan-inbouw-inclusief-inbouwdeel-geborsteld-koper-pvd-koper | Productpagina 2 | `HTML`, `SOURCE` | **BEWEZEN:** volledige PDP-informatie en Product-/Offer-data |
| https://www.sanitairwinkel.nl/merkenpagina/saniclass/ | Merklandingspagina | `HTML` | **BEWEZEN:** merkverhaal, categorieingangen en showroom-CTA |
| https://www.sanitairwinkel.nl/saniclass/ | Merkproductlijst | `HTML` | **BEWEZEN:** merkassortiment, series en filters |
| https://www.sanitairwinkel.nl/advies/ | Advies | `HTML` | **BEWEZEN:** advies- en doe-het-zelfcontent met onderwerpclusters |
| https://www.sanitairwinkel.nl/klantenservice/ | Klantenservice | `HTTP`, `HTML` | **BEWEZEN:** verwijst door naar een apart openbaar helpcentrum op `service.sawiday.com` |
| https://www.sanitairwinkel.nl/showrooms/ | Showrooms | `HTML` | **BEWEZEN:** twintig locaties, afspraak en persoonlijk advies in de momentopname |
| https://www.sanitairwinkel.nl/robots.txt | Robots | `ROBOTS` | **BEWEZEN:** zoeken, vergelijken, cart, wishlist, klant-/orderroutes en geselecteerde parameters uitgesloten |
| https://www.sanitairwinkel.nl/sitemap/ | Sitemapindex | `XML` | **BEWEZEN:** 24 deelsitemaps voor productgroepen, categorieen, merken, content, attributen en CMS-routes |
| https://www.sanitairwinkel.nl/bc-disc-002-niet-bestaande-pagina | Foutpagina | `HTTP`, `SOURCE` | **BEWEZEN:** HTTP 404; geen bruikbare titel of robotsmeta in de uitgelezen bron |

### 3.3 Sanitairkamer

| URL | Paginatype | Methode | Resultaat of beperking |
| --- | --- | --- | --- |
| https://sanitairkamer.nl/ | Homepage, hoofdnavigatie en vertrouwen | `HTML`, `SOURCE` | **BEWEZEN:** brede productnavigatie, advies, afspraken, showrooms en 3D-tekening |
| https://sanitairkamer.nl/badkamermeubels/ | Hoofdcategorie | `HTML`, `SOURCE` | **BEWEZEN:** subcategorieen, omvangrijke filters, kaarten, paginering en SEO-output |
| https://sanitairkamer.nl/badkamermeubels/wastafelmeubel/ | Subcategorie 1 | `HTML` | **BEWEZEN:** productlijst en eigenschapsfilters |
| https://sanitairkamer.nl/badkamermeubels/afvoer-wastafel/ | Subcategorie 2 | `HTML` | **BEWEZEN:** verdere categoriediepte en productlijst |
| https://sanitairkamer.nl/kranen/wastafelkraan/ | Aanvullende subcategorie | `HTML` | **BEWEZEN:** categoriespecifieke filters en productkaarten |
| https://sanitairkamer.nl/catalogsearch/result/?q=%7Bquery%7D | Zoekroute uit bron | `SOURCE`, `ROBOTS` | **NIET TOEGANKELIJK:** `/catalogsearch/*` is uitgesloten; route niet bezocht en formulier niet verstuurd |
| https://sanitairkamer.nl/fontana-proma-badkamermeubel-120cm-zonder-kommen-warm-eiken-sk60333.html | Productpagina 1 | `HTML`, `SOURCE` | **BEWEZEN:** opties, setonderdelen, samples, documenten, reviews en aanvullende producten |
| https://sanitairkamer.nl/saniclear-plus-wastafelkraan-zwart-mat-sk35603.html | Productpagina 2 | `HTML`, `SOURCE` | **BEWEZEN:** PDP-structuur en een alternatieve-productaanbeveling; inhoudelijke score-/garantieverschillen zichtbaar |
| https://sanitairkamer.nl/merken/saniclear/ | Merkproductlijst | `HTML` | **BEWEZEN:** merkroute met uitgebreid assortiment en filters |
| https://sanitairkamer.nl/blog/category/tips | Advies | `HTML` | **BEWEZEN:** openbare tip-/adviescategorie |
| https://sanitairkamer.nl/klantenservice/ | Klantenservice | `HTML` | **BEWEZEN:** serviceingangen voor levering, retour en overige hulp |
| https://sanitairkamer.nl/showrooms | Showrooms | `HTML` | **BEWEZEN:** locatie-/adviespropositie; aantallen verschillen binnen de onderzochte publieke inhoud |
| https://sanitairkamer.nl/robots.txt | Robots | `ROBOTS` | **BEWEZEN:** `Crawl-delay: 1`, zoeken, compare, checkout, wishlist, klant- en facet-/sorteerroutes uitgesloten |
| https://sanitairkamer.nl/sitemaps/sitemap_sanitairkamer.nl.xml | Sitemapindex | `XML` | **BEWEZEN:** acht sitemaps voor blog, producten, categorieen, CMS en landingspagina's |
| https://sanitairkamer.nl/bc-disc-002-niet-bestaande-pagina | Foutpagina | `HTTP` | **NIET TOEGANKELIJK:** HTTP 429; geen herpoging of omzeiling uitgevoerd |

## 4. Samenvatting

### Gemeenschappelijk

- **BEWEZEN:** alle drie organiseren het primaire aanbod in brede badkamerproductgroepen met verdiepende subcategorieen, merk- en seriestructuren.
- **BEWEZEN:** productlijsten combineren categoriespecifieke eigenschappen met prijs, merk, maat/kleur/materiaal en lever- of beschikbaarheidsfilters.
- **BEWEZEN:** productkaarten tonen minimaal productidentiteit, prijs en leverinformatie; badges, reviews, variantaantallen, vergelijking en wishlist verschillen per site.
- **BEWEZEN:** PDP's combineren opties, voorraad/levertijd, specificaties, aanvullende producten en service-/vertrouwenselementen.
- **BEWEZEN:** alle drie hebben advies-/inspiratiecontent, showroomroutes, retourinformatie en interne relaties tussen categorie, merk, product en content.
- **BEWEZEN:** kernpagina's in de steekproef gebruiken canonicals, metadata, breadcrumbs en structured data. Zoekroutes worden overal door robotsregels uitgesloten.
- **AFGELEID:** de schaal wordt niet alleen door navigatiediepte gedragen, maar vooral door consistente producteigenschappen, merk/serie-relaties en landingspaginaregels.

### Belangrijkste verschillen

- BadkamerXXL combineert een compacte showroompropositie met zeer gedetailleerde categoriefilters, productvergelijking en een duidelijk getaxeerde adviesbibliotheek.
- Sanitairwinkel heeft de breedste zichtbare showroomdekking, een los helpcentrum en zeer informatierijke kaarten/PDP's; de lijstweergave kan daardoor zwaar en tekstueel worden.
- Sanitairkamer gebruikt opvallend veel schone padsegmenten voor facetten en paginering, toont veel zelfstandig gekoppelde productuitvoeringen en zet sterker in op alternatieven en complete sets.
- Sitemapindeling verschilt: BadkamerXXL splitst onder meer content, landingpages, producten en afbeeldingen; Sanitairwinkel splitst zeer fijn per productgroep en paginatype; Sanitairkamer gebruikt een compactere set.

## 5. Concurrentprofielen

### 5.1 BadkamerXXL

**BEWEZEN**

- De hoofdnavigatie bevat dertien productgroepen en aanvullende ingangen voor kennis, inspiratie, showroom, afspraak, zakelijk en klantenservice.
- De onderzochte meubelcategorie is drie niveaus diep bereikbaar. Filters omvatten merk/serie, prijs, levertijd, showroom-/afhaalmogelijkheid, maat, materiaal, kleur en productspecifieke eigenschappen.
- Sortering biedt relevantie, prijs, nieuwste en verkooppopulariteit. Paginering gebruikt `?p=`.
- Kaarten tonen prijs/korting, levertijd, kenmerken, optieaantal/badges en een vergelijkselectie. De publieke vergelijkfunctie vermeldt maximaal drie producten.
- PDP's tonen artikelnummer, gekoppelde uitvoeringen, prijsbesparing, leverkeuze, samples, plus-/aandachtspunten, specificaties, onderhoud, setaanvulling en advieslinks.
- De blog is onderverdeeld in advies per productgroep, inspiratie/trends, binnenkijkers, onderhoud en nieuws.
- De foutpagina retourneert correct HTTP 404, maar heeft in de steekproef `index,follow`.
- Op de openbare homepage-HTML stond een zichtbare `Lorem ipsum`-placeholder.

**AFGELEID**

- Het model stuurt sterk op productvergelijking en productspecifieke begeleiding zonder de categorie naar een puur redactionele pagina te maken.
- De uitgebreide robotsuitsluitingen beperken crawlen van veel queryfacetten, maar bewijzen niet dat alle duplicate routes buiten de index blijven.

**NOG ONDERZOEKEN**

- Volledigheid van het algemene merkenoverzicht, runtimevergelijking, predictive search, mobiele bediening en werkelijk geindexeerde facetten.

### 5.2 Sanitairwinkel

**BEWEZEN**

- De commerce-navigatie omvat twaalf hoofdgroepen plus outlet/acties, met aparte routes voor service, inspiratie, advies, zakelijk en twintig showrooms.
- Categorieen hebben zeer uitgebreide filterlijsten, waaronder levering en beschikbaarheid per showroomstad. Sortering omvat populariteit, prijs, levertijd en nieuwste.
- Een resultaatweergave toont een bovengrens van 20.000; dit is geen bewezen uniek producttotaal.
- Kaarten tonen uitgebreide namen, prijs, leverdatum/-week, reviewaantal en badges. Wishlistselectie is in de openbare bron aantoonbaar.
- PDP's bieden artikelnummer, reviews, video/media, opties, levertijd, showroomstatus, plus/min, technische documenten, alternatieven, aanvulling, merk, verzending, retour en serie-informatie.
- Merkcontent en merkproductlijsten zijn afzonderlijke paginatypen. Klantenservice staat op een publiek extern helpcentrum.
- De sitemap is met 24 onderdelen het fijnst opgesplitst en bevat onder meer categorie-attribuut- en categorie-merkpagina's.
- De geteste fout-URL retourneert HTTP 404, maar leverde geen bruikbare titel of robotsmeta in de uitgelezen bron.

**AFGELEID**

- De combinatie van showroomfilters, levermoment en inhoudelijke PDP-details ondersteunt zowel online selectie als bezoekvoorbereiding.
- Lange productnamen en filterlijsten verhogen informatiedichtheid, maar kunnen scanbaarheid en mobiel gebruik belasten.

**NOG ONDERZOEKEN**

- Betekenis van de resultaatcap, dynamische search, mobiele drawers, runtime wishlist en indexatiebeleid voor categorie-attribuutpagina's.

### 5.3 Sanitairkamer

**BEWEZEN**

- De hoofdnavigatie bevat elf primaire productgroepen plus complete sets; inspiratie, advies, afspraak, showrooms, 3D-tekening, service en zakelijk zijn afzonderlijk bereikbaar.
- Categorieen tonen grote resultaataantallen en uitgebreide filters. Schone padfacetten zoals `/merk/` en `/levertijd/` zijn zichtbaar; paginering gebruikt `/page/2/`.
- Kaarten tonen SKU, huidige/vorige prijs, voordeelpunten, aantal opties en levermoment. Reviews zijn niet op iedere kaart in de steekproef zichtbaar.
- PDP's koppelen kleur-/maat-/configuratieopties naar afzonderlijke productroutes en tonen voorraad, levertijd, samples, documenten, specificaties, setonderdelen, reviews en gerelateerde content/producten.
- Een onderzochte PDP biedt expliciet een beter alternatief als upsellpatroon.
- De kraan-PDP had twee H1-elementen in de bron. De zichtbare reviewscore verschilde tussen bovenkant en reviewsectie; garantie-informatie verschilde tussen metabeschrijving en PDP.
- Openbare showroominhoud noemde zowel tien als elf locaties binnen de onderzochte momentopname.
- De foutpagina kon niet worden beoordeeld doordat de server `429` terugstuurde; onderzoek is daar gestopt.

**AFGELEID**

- Schone facetpaden kunnen sterke landingspagina's ondersteunen, maar vergroten zonder expliciete canonical-/indexatieregels het duplicate- en crawlbudgetrisico.
- Resultaataantallen lijken mede productuitvoeringen of combinaties te omvatten en zijn niet zonder verdere bronanalyse als uniek producttotaal bruikbaar.

**NOG ONDERZOEKEN**

- 404-output, client-side opties, wishlist/sneltaken, predictive search, mobiele filters en de feitelijke indexatie van facetpaden.

## 6. Vergelijkingsmatrix

| Onderwerp | BadkamerXXL | Sanitairwinkel | Sanitairkamer |
| --- | --- | --- | --- |
| Hoofdnavigatie | 13 productgroepen; kennis/service naast commerce | 12 groepen plus outlet/acties; sterke showroomlaag | 11 groepen plus complete sets; afspraak/3D prominent |
| Categoriepad | Diep, producttypegericht | Breed en zeer attribuutrijk | Diep, met veel schone facetpaden |
| Merkstructuur | Merk-in-categorie plus algemeen overzicht | Merkcontent en aparte merkproductlijst | Merkproductlijst met grote filterset |
| Filters | Zeer specifiek; queryparameters | Zeer specifiek; levering en showroomstad | Zeer specifiek; query- en schone padfacetten |
| Sortering | Relevantie, prijs, nieuw, verkoop | Populariteit, prijs, levertijd, nieuw | Populariteit, alfabetisch en prijs |
| Paginering | `?p=2` | `?page=2` | `/page/2/` |
| Kaarten | Opties, kenmerken, levertijd, vergelijken | Reviews, levertijd, badges, wishlist | SKU, voordeelpunten, opties, levertijd |
| PDP-opties | Gekoppelde productuitvoeringen | Opties en alternatieven | Veel gekoppelde uitvoeringen en alternatief-upsell |
| PDP-service | Samples, setaanvulling, advies | Showroomstatus, docs, aanvulling, retour | Samples, docs, setinhoud, gerelateerd |
| Content | Fijn getaxeerde blog | Adviesclusters en los helpcentrum | Blog/tips en servicecontent |
| Showrooms | Een locatie in steekproef | Twintig locaties in momentopname | Tien/elf genoemd; inconsistentie |
| Sitemaps | 10, inclusief afbeeldingen | 24, zeer fijn per type/productgroep | 8, compacter |
| Zoekroute | Uitgesloten in robots | Uitgesloten in robots | Uitgesloten in robots |
| Foutpagina | 404, maar `index,follow` | 404, metadata niet bruikbaar | `429`; niet beoordeeld |

## 7. Informatiearchitectuur

### Bewezen patronen

- Alle sites gebruiken een herkenbare route van hoofdgroep naar subcategorie en product, aangevuld met merk-, serie-, content- en servicepaginatypen.
- Breadcrumbs zijn op categorie- en productniveau aantoonbaar.
- Merk kan zowel een contextuele categorie (`categorie/merk`) als een zelfstandige landing/productlijst zijn.
- Interne links verbinden kaarten, breadcrumbs, opties, series, aanvullende producten, service en advies.
- Filters zijn categoriespecifiek; algemene kenmerken worden aangevuld met type-eigen eigenschappen.

### Schaalbaarheid en risico

- **AFGELEID voordeel:** een vast productattribuutmodel maakt categorieen, filters, kaarten, PDP's en SEO-landingen gezamenlijk schaalbaar.
- **AFGELEID risico:** dezelfde merk/eigenschap kan via categorie, merkpagina, queryfacet en schoon facetpad meerdere overlappende routes opleveren.
- **OPEN BESLISSING:** BadkamerCity moet per routeklasse bepalen welk paginatype een zelfstandige zoekintentie bedient, welke route canonical is en welke facetten indexeerbaar zijn.
- **NOG ONDERZOEKEN:** echte zoekvraag, assortimentdekking en redirectbehoefte van BadkamerCity voordat een categorieboom wordt gekozen.

## 8. Zoeken, filters en productkaarten

### Zoeken

- **BEWEZEN:** alle homepages hebben een zoekformulier en een routepatroon in de bron.
- **NIET TOEGANKELIJK:** zoekresultaten, suggesties, spelfouten, nulresultaten en mobiel zoekgedrag; routes waren robots-uitgesloten en er is niets verstuurd.
- **OPEN BESLISSING:** zoekengine, suggestiebronnen, merchandising, fouttolerantie en meetregels voor BadkamerCity.

### Filters en sortering

- **BEWEZEN:** alle drie hebben prijs, merk en productspecifieke filters; maat, kleur, materiaal, levertijd en serie keren vaak terug.
- **BEWEZEN:** BadkamerXXL en Sanitairwinkel gebruiken primair query-/statepatronen; Sanitairkamer toont ook schone facetpaden.
- **AFGELEID voordeel:** lever- en showroomfilters helpen onzekerheid vroeg reduceren wanneer brondata betrouwbaar is.
- **AFGELEID risico:** duizenden waarden, lange filterlijsten en onbegrensde combinaties schaden beheer, scanbaarheid en SEO.
- **OPEN BESLISSING:** indexatie, canonical, limieten en UX per facet voor BadkamerCity.

### Productkaarten

- **BEWEZEN:** prijs en levertijd zijn bij alle drie kerninformatie.
- BadkamerXXL legt relatief meer nadruk op kenmerken, opties en vergelijken.
- Sanitairwinkel legt relatief meer nadruk op uitgebreide namen, reviews, badges en levermoment.
- Sanitairkamer legt relatief meer nadruk op SKU, voordeelpunten, opties en korting.
- **AFGELEID passend patroon:** toon alleen onderscheidende kenmerken die een keuze ondersteunen, plus betrouwbare prijs en levertijd.
- **AFGELEID anti-patroon:** lange, formulematige titels en te veel gelijktijdige badges/acties maken kaarten moeilijk scanbaar.

## 9. Productpagina's, switchers en configuratie

### Informatievolgorde

Alle onderzochte PDP's plaatsen titel/merk of identiteit, prijs, beschikbaarheid, opties en koopactie vroeg. Specificaties, omschrijving, plus/min, documenten, service, aanvulling en reviews volgen verderop. Exacte visuele volgorde is **NIET TOEGANKELIJK**; dit is bron-/inhoudsvolgorde.

### Opties en configuratie

- **BEWEZEN:** de sites representeren veel kleur-, maat- en samenstellingsopties als links naar afzonderlijke productroutes.
- **BEWEZEN:** BadkamerXXL en Sanitairkamer bieden op relevante PDP's samples of kleurstalen.
- **BEWEZEN:** aanvullende artikelen, setcompletering of alternatieven zijn op alle drie aanwezig.
- **NOG ONDERZOEKEN:** echte switcherstate, URL-/historygedrag, foutafhandeling, calculators en complexe configurators; geen interactie uitgevoerd.
- **AFGELEID passend voor BadkamerCity:** dit routepatroon sluit conceptueel aan op het bestaande doel van een zelfstandig product per uitvoering en navigatie naar bestaand product.
- **OPEN BESLISSING:** dit onderzoek kiest niet tussen de huidige V2-switcher, legacyfallback of een andere architectuur.

### Vertrouwen rond de koopactie

- Levermoment, retourtermijn, garantie, betaal-/prijsclaims en reviewbewijs staan dicht bij product of koopactie.
- **Risico:** Sanitairkamer toont binnen een PDP verschillende review- en garantie-informatie. BadkamerXXL heeft tijdgevoelige lever-/garantieclaims op meerdere plaatsen. Zulke informatie vereist een bronhouder en consistentiecontrole.

## 10. Services en positionering

| Onderwerp | Bewezen observatie | Relevantie voor BadkamerCity |
| --- | --- | --- |
| Prijs | Alle drie communiceren prijsvoordeel; laagsteprijsclaims zijn zichtbaar bij meerdere sites | **OPEN BESLISSING:** voorwaarden, bewijs en afhandeling van eigen laagsteprijsgarantie |
| Offerte | Offerte-/adviesroutes zijn bij concurrenten zichtbaar, maar formulieren zijn niet verstuurd | Eigen offerte-upload vereist privacy-, security- en procesbesluit |
| Advies | Adviescontent en persoonlijke ondersteuning zijn structureel aanwezig | Passend bij deskundig-adviespositionering, mits inhoud een eigenaar heeft |
| Showrooms | Van een locatie tot een landelijke locatielaag | BadkamerCity mag de Harry Suiker-relatie niet als zelfstandige eigen showroom voorstellen |
| Contact/chat | Service-, contact- en chat/WhatsApp-ingangen zijn zichtbaar | Provider, SLA, privacy en fallback blijven open |
| Levering | Product- of ordergerichte levertijd en tracking zijn prominent | Alleen toepassen na bewezen leverancier-/voorraadregels |
| Retour | Alle drie publiceren retourinformatie; termijnen/uitvoering verschillen | Eigen beleid en uitzonderingen moeten eerst worden vastgesteld |
| Samples | Op relevante producten zichtbaar bij BadkamerXXL en Sanitairkamer | Past mogelijk bij scope, maar bron, kosten en logistiek zijn open |
| Account/tracking | Account-/ordertrackingroutes zijn aanwezig maar niet bezocht | Geen conclusie over runtime of persoonsgegevens; eigen journey blijft open |
| Vertrouwen | Reviews, garantie, levering, betalen en showroom worden gecombineerd | Claims centraal beheren om zichtbare inconsistenties te voorkomen |

## 11. Content en interne links

- **BEWEZEN:** adviescontent is bij alle drie inhoudelijk geclusterd en gekoppeld aan productgroepen of koopvragen.
- BadkamerXXL heeft de fijnst zichtbare contenttaxonomie in de onderzochte HTML.
- Sanitairwinkel scheidt commerciele site en servicekennisbank via een extern publiek helpcentrum.
- Sanitairkamer combineert blog/tips, service en productgerelateerde vervolgpagina's.
- **AFGELEID sterk patroon:** een contenthub werkt het best wanneer categorie, merk, product en service wederzijds relevante links krijgen.
- **AFGELEID anti-patroon:** content zonder eigenaar of actuele commerciële waarheid kan placeholders en tegenstrijdige claims opleveren.
- **OPEN BESLISSING:** contenttypen, auteurschap, reviewfrequentie en interne-linkregels van BadkamerCity.

## 12. Technische SEO

### Kernpagina's

- **BEWEZEN:** onderzochte home-, categorie- en productpagina's hebben overwegend zelfverwijzende canonicals, indexeerbare robotsmeta, een hoofdheading en schema voor organisatie/website, breadcrumbs, lijsten en/of producten.
- **BEWEZEN:** product-JSON-LD bevat offers; ratings, retour-, verzend- en garantieobjecten verschillen per site en pagina.
- **BEWEZEN:** Sanitairkamer had op een PDP twee H1-elementen.
- **BEWEZEN:** foutpagina-afhandeling is niet uniform: BadkamerXXL 404 met `index,follow`, Sanitairwinkel 404 zonder bruikbare metadata, Sanitairkamer niet beoordeelbaar door `429`.

### Facetten en paginering

- BadkamerXXL sluit een zeer brede reeks filterparameters uit en pagineert met `?p=`.
- Sanitairwinkel sluit zoeken en geselecteerde filter-/statusroutes uit en pagineert met `?page=`.
- Sanitairkamer sluit zoeken en verschillende query-/sorteerroutes uit, toont schone facetpaden en pagineert met `/page/`.
- **AFGELEID:** robotsuitsluiting alleen voorkomt geen duplicate content en is geen bewijs van feitelijke de-indexatie.
- **OPEN BESLISSING:** BadkamerCity heeft een expliciete matrix nodig voor canonical, index/noindex, crawlbaarheid, interne links en sitemapopname per routeklasse.

### Sitemaps

- BadkamerXXL: tien onderdelen, inclusief content, landingpages, producten en afbeeldingen.
- Sanitairwinkel: 24 onderdelen, zeer fijn per productgroep en paginatype.
- Sanitairkamer: acht onderdelen, waaronder drie productsitemaps, categorie, CMS en landingpages.
- **AFGELEID:** sitemaps weerspiegelen een bewuste paginatype-indeling, maar bewijzen niet dat iedere URL kwalitatief, uniek of geindexeerd is.

## 13. Mobiel versus desktop

- **NIET TOEGANKELIJK:** werkelijke mobiele en desktopweergave, menu-interactie, touchdoelen, filterdrawers, sticky koopacties, horizontale overflow en visuele hierarchie.
- **NIET TOEGANKELIJK:** toetsenbordvolgorde, focus, modals en toegankelijke naamgeving van dynamische controls.
- **AFGELEID:** broncode bevat responsive componenten en mobiele routes/states, maar daaruit wordt geen bruikbaarheidsconclusie getrokken.
- **Aanbevolen vervolgstap:** later een afzonderlijke toegestane runtime-test op afgesproken desktop- en mobiele viewports, zonder formulieren of transacties.

## 14. Sterke patronen

1. Een stabiele semantische route van hoofdgroep naar subcategorie, merk/serie en product.
2. Categoriespecifieke filters vanuit beheerde producteigenschappen, niet vanuit losse labels.
3. Productkaarten met onderscheidende kenmerken, prijs, levertijd en beperkt gekozen vertrouwen.
4. PDP's met expliciete inbegrepen/uitgesloten onderdelen, opties, specificaties, documenten, levering, retour en garantie.
5. Gekoppelde zelfstandig verkoopbare productuitvoeringen met eigen route.
6. Aanvullende producten, setcompletering, alternatieven en relevante advieslinks.
7. Contentclusters die aansluiten op categorieen en keuzevragen.
8. Zelfverwijzende canonicals en structured data op kernpaginatypen, met afzonderlijk beleid voor facetten en paginering.
9. Precieze service- en showroomclaims die operationeel aantoonbaar zijn.

Deze patronen zijn **AFGELEID** als mogelijke bouwstenen, niet als goedgekeurd BadkamerCity-ontwerp.

## 15. Anti-patronen

1. Publieke placeholdertekst zoals de aangetroffen `Lorem ipsum`.
2. Foutpagina's met `index,follow` of ontbrekende metadata.
3. Tegenstrijdige review-, garantie-, showroom- of leverclaims op dezelfde site.
4. Resultaataantallen presenteren zonder duidelijk onderscheid tussen unieke producten, uitvoeringen en caps.
5. Onbegrensde facetcombinaties en overlappende query-/padlandingen zonder expliciet SEO-beleid.
6. Kaarten met te lange titels, te veel badges of te veel concurrerende acties.
7. Tijdgevoelige commerciele informatie op meerdere plaatsen zonder centrale bronhouder.
8. Een concurrerende taxonomie, tekst of visueel ontwerp rechtstreeks kopieren zonder eigen assortiment-/klantbewijs.

## 16. Kansen voor BadkamerCity

### Feitelijke uitgangssituatie

- **BEWEZEN in eigen projectdocumentatie:** 7.827 producten en varianten, 201 collecties waarvan 199 leeg, en nog geen gevalideerde categorieboom of filterdatamodel.
- **BEWEZEN:** de V2-switcher wordt door 3.658 producten getriggerd; volledigheid en runtimegedrag blijven beperkt bewezen.
- **BEWEZEN:** prijs, advies, exclusieve merken en de zorgvuldig te formuleren Harry Suiker-showroomrelatie zijn positioneringsbouwstenen.

### Mogelijke kansen

1. **Data en IA eerst:** definieer per producttype kenmerken, filterwaarden, merk/serie en routeklasse voordat categorie-UI wordt gebouwd.
2. **Keuzekwaliteit boven aantallen:** onderscheid unieke producten van uitvoeringen en communiceer alleen aantallen die reproduceerbaar zijn.
3. **Rustige kaarten:** beperk informatie tot beslissende kenmerken, betrouwbare prijs/levertijd en doelbewust gekozen reviews/badges.
4. **Volledige PDP-basis:** maak bronhouders voor SKU, prijs, voorraad, levertijd, specificaties, plus-/aandachtspunten, documenten en service expliciet.
5. **Gekoppelde uitvoeringen:** benut het zelfstandige-productmodel, maar besluit switcherarchitectuur pas na data- en runtimevalidatie.
6. **Eigen contenthub:** verbind advies, inspiratie, begrippen, categorieen en producten met beheerde interne-linkregels.
7. **SEO-governance:** maak een routeklassenmatrix voor canonical, robots, sitemap, headings, schema en foutstatus voordat facetten schaal krijgen.
8. **Betrouwbare positionering:** combineer scherpe prijs en deskundig advies met aantoonbare lever-/servicebeloften en correcte showroomtaal.
9. **Meetbare kwaliteit:** plan later echte mobiele, desktop-, toetsenbord-, zoek- en filtertests met vooraf gekozen criteria.

## 17. Open vragen en menselijke beslissingen

- **OPEN BESLISSING:** definitieve categorieboom, labels, URL-patronen en navigatiediepte.
- **OPEN BESLISSING:** welke facet-/merk-/eigenschapsroutes zelfstandige indexeerbare landingspagina's worden.
- **OPEN BESLISSING:** gewenste kaartinformatie, reviews, vergelijking, wishlist en snelle acties.
- **OPEN BESLISSING:** contenttypen, auteurschap, updateproces en interne-linkeigenaar.
- **OPEN BESLISSING:** service-, laagsteprijs-, levering-, retour-, garantie- en showroomformuleringen.
- **OPEN BESLISSING:** meetbare criteria en tooling voor zoek-, mobiel-, desktop-, toetsenbord- en toegankelijkheidstests.
- **NOG ONDERZOEKEN:** BadkamerCity-zoekintenties, collectie-/productdekking, leverancierseigenschappen en echte filterdatakwaliteit.
- **NOG ONDERZOEKEN:** runtime van zoek-, filter-, wishlist-, switcher-, calculator- en configuratorjourneys.
- **NOG ONDERZOEKEN:** werkelijke indexatie, rankings, redirects, Search Console en performance van BadkamerCity.

## 18. Aanbevolen veilige vervolgstappen

1. De projecteigenaar heeft dit rapport op 2026-08-05 binnen de vastgelegde read-only bewijsgrenzen goedgekeurd; `BC-DISC-002` is `DONE`.
2. Activeer geen ontwerp- of implementatietaak op basis van alleen concurrentiepatronen.
3. Gebruik het rapport later als input voor een afzonderlijk goedgekeurd productdatamodel en IA-/SEO-besluit, samen met eigen assortiment- en zoekintentieonderzoek.
4. Plan een afzonderlijke, begrensde runtime-test wanneer echte desktop-/mobiele browsertooling en acceptatiecriteria beschikbaar zijn.
5. Leg per commerciele claim een bronhouder, actualiteitsregel en controlepunt vast voordat teksten worden ontworpen.

## 19. Veiligheidsbevestiging

- Er is uitsluitend openbare, read-only informatie gebruikt.
- Er zijn geen blokkades, robotsregels, rate limits of beveiligingen omzeild.
- Er zijn geen formulieren verstuurd, accounts gebruikt, persoonsgegevens gelezen of bestellingen geplaatst.
- Er is geen beschermde commerciele tekst, afbeelding, ontwerp of code gekopieerd.
- Shopify Admin is binnen deze taak niet benaderd en Shopify-data is niet gewijzigd.
- Geen theme is gewijzigd, gepusht, gepulld, gepubliceerd, verwijderd of hernoemd.
- Theme-code is niet gewijzigd.
- Geen aanvullende Shopify-scope, app of browserextensie is aangevraagd of geinstalleerd.
- Alleen dit rapport en `docs/MASTERPLAN.md` mogen door deze taak wijzigen.

## 20. Menselijke goedkeuring

De projecteigenaar heeft `docs/COMPETITOR_SEO_ANALYSIS.md` en masterplan versie 0.7 op 2026-08-05 menselijk beoordeeld en `BC-DISC-002` goedgekeurd als afgerond openbaar read-only concurrentie- en SEO-onderzoek.

Deze goedkeuring bevestigt uitsluitend dat het onderzoek binnen de vastgelegde scope is afgerond. Zij is nadrukkelijk geen keuze of toestemming voor:

- het overnemen of kopieren van concurrentiestructuren, teksten, beelden of ontwerpen;
- een categorie-, URL-, filter-, productpagina- of designbesluit;
- een SEO-, patroon-, architectuur- of implementatiebesluit;
- Shopify-, product-, collectie-, metafield-, app-, scope-, theme- of theme-codewijzigingen.

De beperkingen rond zoeken, werkelijke mobiele/visuele interactie, toetsenbordgedrag, indexdekking en dynamische functionaliteit blijven volledig bestaan. Alle statuslabels, open vragen, risico's en bewijsgrenzen in dit rapport blijven ongewijzigd van kracht.
