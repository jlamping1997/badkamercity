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
| UI-F01 | USER_REPORTED · impact nog classificeren | Eigenaar ziet productpijltjes bij Sunshower en elders niet. Actuele Sunshower-sectie heeft foto-vorige/volgende-knoppen; dat identificeert de gemelde kaart-/keuzefunctie nog niet volledig | Nieuwe pijlen-/CSS-kaart in PRODUCT_CARDS_AND_FILTERS.md; mobiele native CTA wordt in bron verborgen, externe cascade kan verschillen. Exacte melding nog browser-/route-/staat-specifiek reproduceren |
| UI-F02 | VERIFIED_SOURCE / STATIC_CANDIDATE · meerdere renderpaden | Huidige `card-product.liquid`, `bc-card-product-search.liquid` en externe filter-JS zijn verschillende renderingangen; Sunshower heeft eigen sectie/bediening | DOC-02A route-/kaartmatrix vastgelegd; DOC-02B moet zichtbaarheid na JS/cascade bevestigen |
| UI-F03 | VERIFIED_SOURCE / UNKNOWN · bevestigingsbeleid | Gewone PDP/externe kaart kan popup renderen; Sunshower-shopkaart heeft inline succes + badge; inbouw/set/wishlist navigeren rechtstreeks. Zie [cartfeedback](components/CART_AND_FEEDBACK.md) | Gewenste bevestiging per ingang bepalen; geen globale submit-interceptor of dubbele POST |
| DATA-F03 | VERIFIED_HTML / STATIC_CANDIDATE · P2 | Hotbath SDS1-response gebruikt volledige product-switcher-data.json; groep bestaat maar revisieguard matcht niet. Alle 656 afgeleide groepsbytes zijn correct. Zie [datapijplijnen](components/DATA_PIPELINES.md) | Actuele bronrevisies in passend concept controleren; geen algemene performance-/datacorruptieclaim |
| DOC-F06 | VERIFIED_SOURCE · rebuildvoorwaarde | Generator in Git heeft geen gevolgde datasets/-invoer op broncommit. Originele assets staan privé/exporteerbaar en de reconstructie is gedocumenteerd | Invoer uit benoemde bron halen en valideren vóór rebuild; niet lege generatorrun als succes registreren |
| OPS-F02 | VERIFIED_SOURCE / NOT_TESTED · activering | Huidige externe-filtercode probeert runSearch automatisch na DOM-guards, zonder bcfilters=1-check. Oude opt-instatus is historisch | Werkelijk actieve renderer/API/index in DOC-02B/latere backendtak verifiëren; dit is geen servergezondheidsclaim |
| CART-F01 | VERIFIED_ISOLATED · P1-kandidaat | Bij key B + ontbrekende/null productsection behoudt cart-notification eerdere productinhoud A en opent. Twee stimuli met ongewijzigde bron gereproduceerd; productievoorkomen onbekend | Kleinste veilige missing-section-afhandeling in concept ontwerpen; geen automatische tweede add. [Microanalyse](components/micro/CART_NOTIFICATION.md) |
| SS-F01 | VERIFIED_ISOLATED · P1-kandidaat | Tijdens pending Sunshower-setadd blijven gewone submit en kleur enabled; een kleurklik kan vóór response productnavigatie aanvragen. Geen echte cart-/dubbele bestelling getest | Afgesproken actieblokkering/uncertain-contract als kleine conceptfix ontwerpen. [Microanalyse](components/micro/SUNSHOWER_ACTIONS.md) |
| DATA-F01 | HISTORICAL / NOT_TESTED · mogelijk lanceringsrelevant | Index-/Shopifyverschillen en een offline voorbereide sync zijn historisch gedocumenteerd in `scripts/filter-sync/README.md` | Verse read-only vergelijking van IDs, publicatie, prijs en filters; niet aannemen dat oud verschil nog exact bestaat |
| OPS-F01 | NOT_TESTED · mogelijke deploy-impact | Actieve branch en main wijken af; werkende Shopify-Git-autodeploykoppeling is in deze ronde niet vastgesteld | Voor rootwijzigingen deploymentkoppeling en releasepad bewijzen |

## Brede winkelcontrole DOC-02C

| ID | Status / impact | Waarneming en bewijs | Volgende actie |
| --- | --- | --- | --- |
| FOOTER-F01 | VERIFIED_THEME / VERIFIED_HTML / beperkt VERIFIED_RUNTIME · configuratie | Tien footerblocks hebben geen URL en tonen tekst; bron, 35-route-HTTP-set en desktopwaarneming passen. [Footer](components/FOOTER.md) | Per label juiste bestaande bestemming of verwijderen kiezen; geen pagina's/bedrijfsinfo verzinnen |
| GLOSS-F01 | VERIFIED_ADMIN / VERIFIED_HTML · P1-kandidaat | Hygro(meter) → /begrippenlijst/hygrometer → /pages/hygrometer geeft 404; 108 overige termdoelen gepubliceerd. [Bewijs](evidence/2026-10-28-complete/glossary-links.json) | Juiste bestaande inhoudsbestemming kiezen, daarna gerichte redirectcorrectie; geen automatische nieuwe Page |
| HOME-F01 | VERIFIED_THEME / VERIFIED_HTML · configuratie, geen defect | Hero uitgeschakeld; populaire-productencollectie leeg; guard laat inhoud weg ondanks sectionwrapper. [Homepage](components/HOMEPAGE.md) | Alleen activeren/vullen wanneer dat gewenst is; geen CSS-fix voor lege datacontext |
| CONTENT-F01 | VERIFIED_ADMIN / NOT_VERIFIED · toewijzingssignaal | Zes Pages hebben suffix page maar page.page.json ontbreekt; vijf gepubliceerd. Buffers-HTTP is 200, dus geen algemene 404-claim. [Content](components/CONTENT_AND_FORMS.md) | Effectieve template/bedoeling controleren; geen bulk-normalisatie |
| OPS-F03 | BLOCKED_ACCESS_DENIED · bron ontbreekt | Checkout/accountconfiguratie-query expliciet geweigerd; classic thematemplates vervangen de gehoste bron niet | Bevoegde configuratiebron nodig; geen alternatieve route om rechten te omzeilen |
| SOURCE-F01 | STATIC_CANDIDATE · P2 | Drie inline_asset_content-verwijzingen missen een exacte manifestnaam: icon-error in passwordheader; icon-3d-model tweemaal in product-media. SVG-namen bestaan wel. [Bronregels](evidence/2026-10-28-complete/reference-anomalies.json) | Passwordfout/3D-route gecontroleerd reproduceren; geen bewezen actuele klantfout of automatische verwijdering |
| DOC-F07 | VERIFIED_SOURCE · documentatiedrift gecorrigeerd | state.json stond nog DOC-00 met 15 onderzochte bestanden terwijl centrale status DOC-03A meldde | Machine-status in DOC-02C gelijkgetrokken; handoffcheck voortaan status/bron/volgende stap vergelijken |
| OPS-F04 | VERIFIED_ADMIN / NOT_TESTED · scopeverschil | Shop meldt alleen NL als shipsToCountries, profiel bevat 41 zonelanden; NL-rates vers gelezen | Geen internationale leverbelofte afleiden; productdekking/effectieve offerte apart beoordelen |

Positief nieuw bewijs: vier publieke zoekreads 200; Wastafelkranen 573 en Inloopdouches 305 matchen de huidige HTML-context. De eerdere precieze indexverschillen zijn historische signalen, niet blind herhaald als huidige aantallen. De begrippenzoekcyclus en één redirect/TOC zijn op desktop bevestigd. [Bewijs en grenzen](evidence/2026-10-28-complete/README.md).

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
