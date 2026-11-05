# Verlavio — voorraad en koopbaarheid

> **Publicatie vastgesteld tijdens SEARCH-01, 5 november 2026:** de eigenaar heeft **BadkamerCity - Verlavio voorraad en levertijd (196227170570)** gepubliceerd; verse Shopify-rollen tonen dit thema als MAIN. De onderstaande COPY_AWAITING_MERCHANT_PUBLICATION-status beschrijft het eerdere oplevermoment en is geen actuele publicatieblokkade. Het nieuwe zoekherstel wordt in het andere, ongepubliceerde thema voorbereid. Zie [SEARCH-01](../../../search-index/2026-11-05/README.md).

5 november 2026. **BACKEND_APPLIED_VERIFIED / PREVIEW_VERIFIED / COPY_AWAITING_MERCHANT_PUBLICATION**.

De eerdere rebrand is afgerond in [FAB-03](../verlavio/README.md). Dit dossier beschrijft de daaropvolgende voorraadcontrole, de gerichte reparatie van Nederlandse verzending en de voorraadtekst in concept. MAIN blijft **196116087050 — BadkamerCity - Verlavio merknaam**. De backend werkt; voor de nieuwe tekst publiceert de eigenaar **BadkamerCity - Verlavio voorraad en levertijd**, concept **196227170570**. Er zijn geen bestanden naar MAIN geschreven en geen thema's door de uitvoerder gepubliceerd.

## Voorraadbron en grenzen

De actuele Fabriecio-CSV bevat 861 gekoppelde artikelen. Alleen de voorraadwaarden met een echt getal zijn als aantal gebruikt; een lege cel is geen nul en geen toestemming om een getal te verzinnen.

| Actieve artikelen | Aantal |
| --- | ---: |
| Positief voorraadaantal | 694 |
| Voorraadaantal nul | 40 |
| Leeg aantal, leverbaar Y | 84 |
| Leeg aantal, leverbaar N | 33 |
| **Totaal actief** | **851** |

Daarnaast blijven tien artikelen gearchiveerd met bronstatus “Nooit meer”. Over alle 861 rijen staan 778 Y en 83 N. De feed bevat voorraadstatus, aantallen en een eventuele verwachte week; geen afzonderlijk veld met de termijn 1–2 werkdagen.

Bij 29 artikelen is een gewijzigd echt voorraadaantal met de CSV gesynchroniseerd, via een vergelijking met het vooraf gelezen Shopify-aantal (CAS). Eerst VSB_2001 als proef van 12 naar 11, daarna 28 overige wijzigingen. Bij de 84 actieve artikelen met leeg aantal en Y blijft de bestaande combinatie `CONTINUE` en hoeveelheid nul behouden; de overige voorraadregels behouden `DENY`. Over de volledige bron zijn 118 lege aantallen niet ingevuld met een verzonnen hoeveelheid. Geen aantallen uit Y/N afgeleid en geen producten actief gemaakt.

Zes bron-/portalconflicten zijn apart op aanvraag gezet in de leveringsdata: MD-915H-OK, FAB_1027, VSB_4001, VSB_4002, GM_3001 en GM_3002. Daarvoor geldt `delivery.stock_conflict=true` en `in_stock=null`; de tekst mag geen bevestigde voorraad suggereren. De bestaande portalverwachting **week 50** blijft behouden waar de feed week 28 meldt, waaronder VSB_2004. Deze waarden zijn niet stil door de feed vervangen.

## Bewezen oorzaak en gerichte reparatie

De winkel gebruikt **`shop.features.marketDrivenShipping=true`**. De oude DeliveryProfile-weergave leek beide locaties te bevatten, maar de werkelijke verzendoptie van de Nederlandse Market gebruikte alleen de winkel als oorsprong. Voorraad op de leverancierslocatie was daardoor niet bereikbaar via die verzendroute.

| Onderdeel | ID |
| --- | --- |
| Nederlandse Market | `94864998666` |
| Verzendoptie | `1251671343370` |
| Tariefgroep | `489069838602` |
| Bestaande winkellocatie | `106665476362` |
| Toegevoegde leverancierslocatie | `110481572106` |

De leverancierslocatie bevat uitsluitend de 861 Verlavio-artikelen; dit is voor de volledige locatie gecontroleerd. Via één gedeeltelijke `marketUpdate` is alleen deze extra oorsprong aan de bestaande Nederlandse verzendoptie toegevoegd. De volledige voor-/navergelijking bevestigt exact die ene wijziging. De winkellocatie, tarief-ID's, overige Markets en bestaande tarieven blijven behouden: **€6,95**, met bestaande gratis-verzendingdrempel **€100,01**. Geen aanpassing van prijzen, belastingen of betaalinstellingen.

Diagnostische locatievlaggen en een tijdelijke voorraadproef met twee stuks van BKK_1001 op de winkellocatie zijn volledig teruggezet. Die proef bevestigde het verschil tussen de twee oorsprongen. De blijvende oplossing is de gerichte Market-wijziging; de proefvoorraad en tijdelijke vlagwijzigingen maken geen deel uit van de eindoplossing.

## Volledige backendcontrole

**PASS — 5 november 2026, 16:37:57 UTC.** Alle 861 producten teruggelezen, nul afwijkingen. Exact 29 echte aantallen komen overeen met de actuele feed; overige voorraadhoeveelheden en locatievelden, waaronder gereserveerde en toegewezen voorraad, blijven gelijk aan de nulmeting. De zes conflictvelden komen exact overeen met het uitvoerplan.

Product-ID's, titels, handles, SKU's, prijzen, status, voorraadbeleid en tracking blijven behouden. Statusverdeling blijft **851 ACTIVE / 10 ARCHIVED**. De eerdere merknaam Verlavio en keuzemenu's blijven intact. De definitieve Nederlandse Market-configuratie verschilt uitsluitend door de toegevoegde leveranciersoorsprong; tarieven, drempel en overige velden zijn gelijk.

Publieke eindcontrole op **16:31:19 UTC**: VSB_2001, BKK_1001 en BKK_2008 geven HTTP 200, `available=true`, schema InStock en een actieve winkelwagenknop. VSB_2004 met nul blijft `available=false`, schema OutOfStock, knop uit en verwachting week 50. GM_3001 blijft beschikbaar maar krijgt geen bevestigde voorraadbelofte; live staat de eerdere tekst “Levertijd op aanvraag”. De nieuwe tekst uit het concept staat op dat moment nog niet live.

## Voorraadtekst in gecontroleerd concept

**UNPUBLISHED196227170570 — BadkamerCity - Verlavio voorraad en levertijd** is vóór de tekstwijziging volledig gelijkgemaakt aan MAIN: **1.381 / 1.381 bestanden identiek**. Het definitieve manifest bevat opnieuw 1.381 bestanden met exact drie bedoelde verschillen:

| Bestand in `shopify/current/` | Definitieve MD5 |
| --- | --- |
| `snippets/bc-fabriecio-delivery.liquid` | `73b9f1ec4dc09bb952b9579a329dd21c` |
| `locales/nl.json` | `98ad6e87229d9e10a00bfdf7a0a9a5ba` |
| `locales/en.default.json` | `7d9b67c3385870b9ab0ca9eb420c6f63` |

De drie gecontroleerde MAIN-featurehashes blijven gelijk; er zijn geen MAIN-bestanden geschreven. Gedeelde keuzemenubediening en interne Fabriecio-sleutels blijven behouden.

De aangevraagde tekst voor bevestigde voorraad is **“Op voorraad”** met **“Levertijd: 1–2 werkdagen”**. De termijn is een winkelbelofte voor de bevestigde voorraadgroep; zij is niet uit een CSV-levertijdveld gelezen. Onder de 851 actieve artikelen komen 774 bevestigde Y-artikelen zonder conflict voor die tekst in aanmerking. De overige 71 N-artikelen en zes conflicten volgen hun eigen leverstatus. De zes conflicten krijgen **“Voorraad en levertijd op aanvraag”**; echte toekomstige beschikbaarheid blijft afzonderlijk zichtbaar.

**Tests PASS:** 23 leveringsgevallen, 16 menu-/URL-overgangen en drie officiële Liquidvalidaties geldig. In echte Chrome-preview:

- VSB_2001 toont “Op voorraad” en “Levertijd: 1–2 werkdagen”, met actieve winkelwagenknop.
- De echte knop voegt één VSB_2001 toe; succesmodal bevestigd. Alleen de eigen testregel daarna verwijderd; eindwinkelwagen nul.
- Klik op Mat Wit navigeert naar de eigen URL van VSB_2003, met “Verwacht: Week 50” en uitgeschakelde koopknop.
- GM_3001 toont “Voorraad en levertijd op aanvraag”.

Geen checkout-, betalingstest of fysieke telefoontest. De screenshots blijven privé; geen lokale screenshotpaden in publieke Git-documentatie. Na eigenaarspublicatie moeten MAIN-rol en de nieuwe publieke tekst nog gericht worden teruggelezen.

## Herstel en overdracht

De volledige feed, productinventaris, CAS-nulmeting, mutatiebonnen en voor-/naregistratie van de Nederlandse verzendoptie blijven in de privéaudit. Deze publieke repository bevat alleen totalen, begrensde configuratie-identiteiten en testgrenzen.

Herstel van de permanente Market-wijziging verwijdert uitsluitend de toegevoegde leveranciersoorsprong uit de oorspronkelijke verzendoptie, na actuele herlezing. Voorraadherstel gebruikt per gewijzigde hoeveelheid de privé-nulmeting met een nieuwe vergelijking; geen volledige catalogussnapshot terugschrijven. De voorraadtekst wordt alleen in het ongepubliceerde concept teruggezet. Geen MAIN-write of zelfstandig publiceren.

De zes leveranciersconflicten, 53 vastgehouden bronmenu-uitzonderingen en het ontbreken van Verlavio in het bestaande merkenoverzicht blijven open. Automatische feedsynchronisatie is nog niet ingericht; dit is een gecontroleerde eenmalige synchronisatie, geen vijfminutenkoppeling. Bestaande URL's/SKU's, statussen en het Lagoo-fotoverbod blijven behouden.

**Exact één volgende handeling:** eigenaar publiceert **BadkamerCity - Verlavio voorraad en levertijd (196227170570)**; daarna de MAIN-rol en drie publieke leverstatussen teruglezen. Backend en preview zijn gecontroleerd; geen actieve FAB-04-schrijver of feedworker na overdracht. De aparte werkprioriteit uit de centrale status blijft behouden.
