# Filterherstel na OVH-verlenging — 8 november 2026

**FILTER-RESTORE-01 · PUBLIC_API_RECOVERED / LIVE_UI_VERIFIED.** Eerst herstel, daarna filterverbeteringen. MAIN196328685834 — BadkamerCity - Homepage SEO8nov, door eigenaar gepubliceerd. Geen Shopify-/serverwrite door deze uitvoering.

## Oorzaak en herstelgrenzen

De eerste openbare meting rond11:55–11:56UTC: huidige filtermarkup op Wastafelkranen gebruikt https://vps-7ffd625d.vps.ovh.net/verified; verified-health en POST-search gavenHTTP502. Host-DNS bleef57.129.175.195; oude /health gafHTTP200 en Typesenseok. SSH vanuit deze uitvoering gaf Network is unreachable; geen remote opdracht bereikt.

De eigenaar deelde de uitvoer van een alleen-lezen Docker-inventaris:
- badkamercity-filter-api-verified-candidate: Exited(0),27uur.
- badkamercity-caddy, beide oudere API's en badkamercity-typesense: Up2uur.

Het eigenaarblok is verstrekt voor docker update --restart unless-stopped op exact die bestaande kandidaat, gevolgd door docker start,12seconden stabilisatie en status/health. Geen containerrecreatie, installatie, indexherbouw of volumewrite opgedragen. De eigenaar deelde daarna het commando zelf, zonder terminalresultaat. Alleen de onafhankelijk gemeten publieke werking is hieronder bewezen. Restartbeleid, automatische timer en rebootgedrag nog niet rechtstreeks teruggelezen.

## Onafhankelijke nacontrole rond12:02–12:05UTC

| Controle | Resultaat |
| --- | --- |
| /verified/health | HTTP200,ok=true, juiste kandidaatservice, versie0.4.0 |
| Index / generatie | bc_sync_20261107t080100_ca321b /20261107T080100_ca321b |
| Profielen |227 |
| Wastafelkranen | API615, profiel615, native Shopify615;10facetten |
| Inloopdouches | API358, profiel358, native Shopify358;8facetten |
| Tegels | APIHTTP200,3496resultaten;6facetten; geen volledige browserproef |
| Verlavio-zoekread | HTTP200 met producten; geen nieuwe volledige ID-dekkingvergelijking |
| CORS | allow-origin=https://badkamercity.nl; echteOPTIONS-preflightHTTP200, POST/content-type toegestaan |

Een gezonde API bewijst niet dat alle geïndexeerde prijzen/voorraadvelden actueel zijn; de actieve snapshot dateert van7november. Het herstel heeft de orderability-afspraak van8november en Lagoo-afbeeldingsgrens niet gewijzigd.

## Echte Chrome-desktopproef

Live Wastafelkranen zonder previewparameters:
1. Uitgebreide Plaatsing/Kleur/Prijs/Merk/Serie/Meerfilters zichtbaar;615producten.
2. Inbouw aangevinkt:200producten, URL bcf_f_kraanmontage=Inbouw.
3. Chroom toegevoegd:26producten, beide selecties en URL correct.
4. Alles wissen:615producten, beide facetselecties uit, schone collectie-URL.

Eén locator-wachtcontrole na wissen mislukte door vier gelijknamige DOM-elementen waarvan slechts één zichtbaar; de verse echte accessibilityweergave bevestigde615 en lege selecties. Dit is geen productdefect of gefaalde wisactie. Geen winkelwagen-/bestelmutatie. Geen nieuwe mobiele, geforceerde netwerkfout/fallback-, paginatie-, sorteer- of serverrebootproef. De desktopscreenshot is te ver in de productlijst genomen en geldt niet als visueel filterbewijs; de echte interacties/accessibility zijn hierboven het beperkte bewijs.

## Verbeterpilot Wastafelkranen — nog niet toegepast

De actuele API meldt incomplete data: Plaatsing93,17%, Kleur91,87%, Serie90,73%, kraangaten55,61%, hoogte-uitloop49,27%, lengte-uitloop70,41%. Inclusief-inbouwdeel24,39% is niet zonder toepassingscontrole als75,61%ontbrekende informatie te behandelen; niet elk veld past op elk producttype. Geen waarden raden of ontbrekend als nee behandelen.

Concrete schrijfvarianten in de kleurfacet: Mat zwart/Mat Zwart en Gun Metal/Gun metal. Eerst per exacte waarde aantonen welke semantisch gelijk zijn, coatings/PVD en fabrikantkleuren behouden, en bestaande URL-/OR-filtercontracten testen. De bestaande UI heeft reeds kleurgroepen; geen tweede normalisatielaag blind toevoegen. Kleuren vullen vóór een andere sortering ontwerpen.

Daarna categorieafhankelijke relevante filters/eenheden/volgorde en echte mobiele drawer/keuzechips bespreken en testen. Backendprofielen/code eerst actueel lezen; publieke themebron is geen volledige VPS-back-up. Geen sitebrede activering, veiligheidscheckverwijdering of theme-publicatie door deze taak.

## Exact één volgende handeling

Eigenaar deelt de terminaluitvoer van het al gegeven herstelblok; niet opnieuw installeren. Bij ontbreken van uitvoer is een gerichte read-only restartpolicy/statuscontrole nodig. Daarna met Wastafelkranen de verbeterpilot concretiseren.

Actieve codebranch fix/product-cards-2026-10-14; main alleen documentatie. Eerdere homepage-SEO, bestelbaarheid, leveranciers-/BRAUER-holds en andere overdrachten behouden. Geen secrets, volledige inspect/env-configuratie, ruwe catalogus of wachtwoord in Git. Geen actieve schrijver na checkpoint.
