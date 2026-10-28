# Bevindingen en onderzoekswachtrij

**Peildatum 28 oktober 2026.** Alleen onderstaande bron-/documentatiebevindingen zijn in deze ronde onderzocht. Geen algemene verklaring over webshopkwaliteit of koopgereedheid.

## Vastgesteld en gemeld

| ID | Status / impact | Waarneming en bewijs | Volgende actie |
| --- | --- | --- | --- |
| DOC-F01 | VERIFIED_SOURCE · blokkeert betrouwbare actuele codeaudit | Git-root op `4a85d063` heeft 441 themabestanden; vers MAIN-manifest 1.262. 384 gelijk, 57 afwijkend, 821 alleen live, 0 alleen root. [Rootscan](evidence/2026-10-28/repository-root/README.md) | Snapshot opgehaald; 384 root-bytegelijk, 84 elders gevolgd, 794 zonder bytegelijke kandidaat. Zie DOC01_SOURCE_MAP.md; geen blinde root-sync |
| DOC-F02 | VERIFIED_SOURCE · overdrachtsrisico | Oud centraal statusbestand bevat 1.209 regels en meerdere historische “volgende stappen”. Archief is exact behouden, nieuwe status is kort | Beheer één actuele taak/volgende handeling; historie in archief/dossier |
| DOC-F03 | VERIFIED_SOURCE · oude status ingehaald | `195818389770` staat nu MAIN; `195805085962` UNPUBLISHED. De vorige chat leverde de popup als concept op | Vastgelegd in bronregister; bij iedere nieuwe taak rollen opnieuw lezen |
| DOC-F04 | VERIFIED_SOURCE · dekkingsgrens | Nulmeting: 15 actuele live bestanden. Vervolg DOC-01: alle 1.262 ontvangen en statisch gescand, waarvan 1.261 bytegelijk | Settings-pariteit open; statische volledigheid is geen handmatige/runtime-audit |
| DOC-F05 | VERIFIED_SOURCE · pariteitsvrijgave open | config/settings_data.json: ontvangen tekst wijkt af van Shopify-metadata; voor-/namanifest gelijk. Harde controle exitcode 2 | Read-only verklaring/exacte bron vaststellen; geen ontvangen tekst of metadata aanpassen om controle te omzeilen |
| DATA-F02 | VERIFIED_ADMIN · exportbasis aanwezig | 11.343 producten/varianten, 241.064 metafields en 32.065 mediarecords privé vastgelegd; lagen, tellingen, paginering en SQLite-integriteit gecontroleerd | Gebruikersfuncties aan veldconsumptie koppelen; API-scope en niet-atomaire uitlezing behouden |
| UI-F01 | USER_REPORTED · impact nog classificeren | Eigenaar ziet productpijltjes bij Sunshower en elders niet. Actuele Sunshower-sectie heeft foto-vorige/volgende-knoppen; dat identificeert de gemelde kaart-/keuzefunctie nog niet volledig | Exacte route, component, breedte en staat vergelijken met algemene kaart/PDP; geen pijlen verwijderen vóór functieclassificatie |
| UI-F02 | VERIFIED_SOURCE / STATIC_CANDIDATE · meerdere renderpaden | Huidige `card-product.liquid`, `bc-card-product-search.liquid` en externe filter-JS zijn verschillende renderingangen; Sunshower heeft eigen sectie/bediening | DOC-02 route-/kaartmatrix; bepalen welke implementatie op welke route werkelijk zichtbaar is |
| DATA-F01 | HISTORICAL / NOT_TESTED · mogelijk lanceringsrelevant | Index-/Shopifyverschillen en een offline voorbereide sync zijn historisch gedocumenteerd in `scripts/filter-sync/README.md` | Verse read-only vergelijking van IDs, publicatie, prijs en filters; niet aannemen dat oud verschil nog exact bestaat |
| OPS-F01 | NOT_TESTED · mogelijke deploy-impact | Actieve branch en main wijken af; werkende Shopify-Git-autodeploykoppeling is in deze ronde niet vastgesteld | Voor rootwijzigingen deploymentkoppeling en releasepad bewijzen |

## Sjabloon voor iedere nieuwe bevinding

Gebruik een vast ID en leg vast: bronversie/datum; klantdoel; exacte URL/paginatype/product; viewport/browser; actuele/toekomstige staat; herhaalstappen; verwacht contract; werkelijke uitkomst; betrokken bestanden/regelnummers en data-eigenaar; bewijsstatus; klantimpact; prioriteit; voorgestelde kleinste fix; afhankelijke componenten; test/rollback; eigenaar en besluit.

Het register bevat geen secrets of volledige klant-/orderrecords. Registreer screenshots alleen wanneer relevant en toegestaan; een opname van één scherm is geen bewijs voor alle routes.

## Beslisregels

- **BUG:** functie of aantoonbaar gegevenscontract is fout; correctie op klantimpact prioriteren.
- **INCONSISTENCY:** dezelfde functie werkt/toont onbedoeld anders; referentievariant kiezen en documenteren.
- **INTENTIONAL_VARIANT:** verschil is nodig; reden en toepassingsgebied vastleggen.
- **UNKNOWN:** onvoldoende bron, toegang of reproductie; onderzoeksvraag laten staan.

Een statische kandidaat wordt pas een bewezen defect na inhoudelijke controle. Een bevinding wordt pas gesloten met het exacte gerealiseerde resultaat, passende regressie en actuele bron-/runtimegrens. “Code aangepast” alleen is geen volledige sluiting.

## Eerstvolgende verbeteringen bepalen

DOC-01 en DOC-02 leveren eerst de actuele bron en matrix. Daarna een kleine gerichte vergelijking van keuzebediening, kaartacties/pijlen, galerijbediening, leverinformatie en modalgedrag. Koop-/dataproblemen die tijdens dat werk worden aangetoond krijgen direct voorrang boven cosmetische afwerking.

Korte titels en de eerder geparkeerde bijbehorende filteroptimalisatie worden door deze documentatieopdracht niet stil als nieuwe implementatietaak geactiveerd. Nieuwe ideeën krijgen een ID en reden, geen losse ongeregistreerde herbouw.
