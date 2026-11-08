# Filterherstel na OVH-verlenging — 8 november 2026

**FILTER-RESTORE-01 · DIAGNOSED / BLOCKED_SSH_ACCESS.** De eigenaar vraagt eerst de bestaande filters weer te tonen en daarna pas verbeteringen. Geen herinstallatie of indexherbouw gestart.

## Verse openbare meting rond 11:55–11:56 UTC

| Controle | Resultaat |
| --- | --- |
| Huidige MAIN | 196328685834 — BadkamerCity - Homepage SEO 8 nov; door eigenaar gepubliceerd |
| Wastafelkranen | HTTP 200; echte MAIN-ID bevestigd; filtermarkup aanwezig, 615 native producten |
| Werkelijke filterbasis | https://vps-7ffd625d.vps.ovh.net/verified |
| Host-DNS | A = 57.129.175.195; dezelfde bekende VPS |
| /health | HTTP 200, ok=true, service=badkamercity-filter-api, Typesense ok=true |
| /verified/health | HTTP 502, lege body |
| POST /verified/api/v1/search | HTTP 502 voor wastafelkranen, één resultaat gevraagd |
| SSH vanuit deze uitvoering | Network is unreachable; geen remote opdracht uitgevoerd |

De host, TLS en oude API zijn bereikbaar. De webshop gebruikt de aparte verified-route; die is niet beschikbaar. Dit bewijst nog niet dat de kandidaatcontainer gestopt is: containerstatus, reverse-proxydoel, poorten en logs zijn nog niet vanaf de server gelezen. Geen verkeerde DNS-koppeling bewezen. Native Shopify-HTML is aanwezig; geen nieuwe browser-fallbacktest geclaimd.

De frontend naar de oude API omzetten is geen bewezen herstel: die heeft een ander historisch index-/profielcontract. Eerst de bestaande verified-dienst diagnosticeren en herstellen.

## Exact één volgende handeling

De eigenaar voert vanuit eigen PowerShell deze alleen-lezen controle uit en deelt de geschoonde output:

~~~powershell
ssh -t ubuntu@57.129.175.195 "sudo docker ps -a --format 'table {{.Names}}\t{{.Status}}\t{{.Ports}}'"
~~~

Deze opdracht inventariseert bestaande containers; geen herstart, recreatie, volume-/indexwrite of instellingenwijziging. Gebruik de bestaande SSH-aanmelding; wachtwoord alleen in de lokale prompt, niet in chat. Bij timeout/authenticatiefout eerst die exacte fout beoordelen.

Na de inventaris: alleen het aantoonbaar getroffen onderdeel herstellen, daarna verified-health, zoekresultaten, profieldekking, CORS en echte storefrontweergave/fallback controleren. Nog geen filterverbeteringen toepassen of sitebrede veiligheidscontroles verwijderen.

## Bewaargrenzen

Geen Shopify-theme-/product-/voorraadwrite, publicatie, serverwrite of nieuwe credentials. De gepubliceerde homepage-SEO en eerdere bestelbaarheidsafspraak behouden. Geen installer herhalen; de SEARCH-01-reparatie van 5 november is historie en geen bewijs dat de huidige verified-route gezond is. Geen wachtwoorden, tokens, volledige inspect/env-configuratie of private catalogusdata opgeslagen. Actieve codebranch fix/product-cards-2026-10-14; main alleen documentatie. Bestaande BRAUER-26- en overige overdrachten behouden. Geen actieve schrijver na dit checkpoint.
