# BadkamerCity — actuele werkstatus

**Bijgewerkt: 28 oktober 2026.** Dit is de vaste actuele ingang. De [vorige status van 1.209 regels](LIVE_STATUS_ARCHIVE_BEFORE_2026-10-28.md) blijft exact bewaard als geschiedenis; oude volgende stappen daarin zijn geen huidige opdracht.

## Huidige opdracht

De eigenaar vraagt sterke, diep doorzoekbare documentatie in Git: wat we gebruiken, wat is opgebouwd, hoe het samenhangt en waar dezelfde functie onnodig anders is vormgegeven. Eerst de scanmogelijkheden en een diep onderzoeksplan; daarna onderbouwde inconsistenties en kleine verbeteringen. Richting: verantwoord online gaan en stap voor stap uitbreiden.

**Taak DOC-00: onderzoeksbasis en plan opgesteld.** Begin bij [architectuur en documentatie](architecture/README.md), daarna [de onderzoeksboom](architecture/DEEP_SCAN_PLAN.md). Dit vervangt niet stil de commerciële/assortimentsafspraken uit oudere plannen. Korte producttitels en de bijbehorende filteroptimalisatie blijven buiten de huidige implementatiescope.

## Gecontroleerde bronstand

| Bron | Stand op meetmoment |
| --- | --- |
| Repository | jlamping1997/badkamercity, publiek |
| Actieve codebranch | fix/product-cards-2026-10-14 |
| Onderzochte codebron | 4a85d063b750b74fd398fe106c11bfe05b6ce277 |
| main bij aanvang | c265f9e91049ae57bb2ffb5e297004042161a178; vaste documentatie-ingang |
| Shopify MAIN | 195818389770 — BadkamerCity - Smooth winkelwagen pop-up |
| Vorige MAIN | 195805085962 — Winkelwagen compact - 27 okt; nu UNPUBLISHED |
| Live manifest | Volledig: 1.262 bestanden, geen vervolgpagina |
| Git-root tegenover MAIN | 441 bestanden: 384 gelijk, 57 afwijkend; daarnaast 821 alleen live; 0 alleen Git-root |
| Actuele inhoudelijke live steekproef | 15 checksumgelijke bestanden; overige 1.247 nog niet inhoudelijk in deze ronde onderzocht |
| Cloudcheckout | Nieuw en schoon bij aanvang; geen andere werkmap aangepast |
| Windows / externe server | Niet gecontroleerd; geen servermutaties of synchronisatieclaim |

Nieuwe publicatie kan deze themarollen veranderen. Lees ze vóór de volgende uitvoering opnieuw. De aangetroffen MAIN-rol van de popup is een waarneming; deze documentatieronde heeft niets gepubliceerd.

## Wat is vastgelegd

Systeem-/bronnenregister, diepe scanboom, componentcontracten, bevindingenregister, overdrachtswerkwijze, scannerhandleiding en gedateerd bewijs staan in docs/architecture/. De statische scanner en vijf gerichte offline checks staan uitsluitend op de actieve branch in scripts/architecture_scan.py en scripts/test_architecture_scan.py.

De Git-root is volledig statisch geïnventariseerd (830 gevonden verwijzingen); een actuele live steekproef heeft 149 gevonden verwijzingen. De scanner is een zoekkaart, geen volledige runtime-/a11y-/security-/performance-audit. Historische tests worden niet als nieuw bewijs opgevoerd.

## Grenzen

Geen themabestanden, productdata, winkelwagen, checkout, apps of VPS gewijzigd. Geen nieuwe thema's, publicatie, planning of brede refactor. Geen blinde root-sync. Documentatie staat ook op main; tooling blijft op de actieve branch. Rootcode op main/werkbranch is niet vanzelf de actuele productiecode; recent werk bestaat mede in releasedossiers.

De eigenaar noemt Sunshower-pijlen als voorbeeld. Live fotopijlen zijn in de sectie aangetoond; de exacte gemelde kaart-/keuzefunctie is nog niet volledig gereproduceerd. Eerst functie en gebruiksplaats vaststellen, daarna eenheid beoordelen.

## Exact één volgende handeling

**DOC-01 uitvoeren:** opnieuw MAIN/branch controleren; een volledige read-only snapshot naast de root ophalen en alle 1.262 bytesets tegen een vers compleet manifest controleren. Tegelijk de bereikbare Shopify-template-/collectie-/menutoewijzingen inventariseren. Uitvoer: actuele bron-/routekaart en herkomst van verschillen, zonder rootcode of productie te overschrijven. Daarna volgt DOC-02 uit het plan.

DOC-01 is gepland, niet afgerond in deze ronde. Er is na oplevering geen schrijver of achtergrondworker actief. De remote documentatiecommit is te vinden met git log -1 -- docs/architecture; de uiteindelijke commitlinks worden bij oplevering gedeeld.

## Hervatten

Lees deze status → AGENTS.md → docs/architecture/README.md → taak DOC-01. Controleer eigen werkmap, actuele bron en toegang. Bewaar bestaande wijzigingen; maak niet per nieuwe chat een nieuwe codebranch. Oude onvoltooide imports of publicatiestappen niet opnieuw starten op basis van het archief.
