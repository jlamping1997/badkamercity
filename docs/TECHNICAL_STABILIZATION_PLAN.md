# BadkamerCity Technical Stabilization Plan

## 1. Documentstatus

| Veld | Waarde |
| --- | --- |
| Taak | `BC-TECH-002` - Technische stabilisatie opdelen en uitvoeringsvolgorde vaststellen |
| Status | `DONE` |
| Menselijk goedgekeurd | 2026-08-11 |
| Onderzoeksdatum | 2026-08-11 |
| Basiscommit | `2b11f1efe1af9e06b9741cdc12393771a970d1a5` op `main` |
| Documentstatus | Read-only onderzoeks- en decompositie-uitvoer; geen implementatieopdracht |
| Algemene projectstatus | `ACTIVE FOR DISCOVERY - IMPLEMENTATION BLOCKED` |

**BEWEZEN:** de brede epic `BC-TECH-001` is nog `BLOCKED`. Dit plan bevat alleen kandidaatopdrachten die later afzonderlijk moeten worden beoordeeld en geautoriseerd.

## 2. Doel en grenzen

Doel is bekende technische risico's terugbrengen tot kleine, bewijsbare en veilig testbare kandidaatopdrachten. Het plan bepaalt bereikbaarheid, zekerheid, impact, afhankelijkheden, vereiste tests, preview en rollback. Het lost geen defect op en kiest geen definitieve code-, data-, UX-, informatiearchitectuur- of bedrijfsregel.

Buiten scope bleven Shopify Admin, themebeheer, theme-codewijzigingen, product- of brondata, imports, packages, branches, publicatie en verwijdering of verplaatsing van bestanden. `LEGACY_OR_ORPHAN_CANDIDATE` en `BACKUP_OR_DEBUG` zijn onderzoeksclassificaties, geen verwijdertoestemming.

## 3. Gebruikte bewijsbronnen

| Bron | Gebruik | Belangrijkste grens |
| --- | --- | --- |
| `docs/REPOSITORY_AUDIT.md` | Primaire historische audit, bestandsrisico's en eerdere Theme Check-run | Tijdgebonden; verdachte code is niet automatisch een runtime-defect |
| `docs/ACTIVE_THEME_USAGE.md` | Actieve JSON-configuratie, statische bereikbaarheid, switchers en injectie | Geen browserruntime; dynamisch gebruik kan statische analyse omzeilen |
| `docs/SHOPIFY_ADMIN_INVENTORY.md` | Product-/template- en metafielddekking | Snapshot; in deze taak is Shopify Admin niet benaderd |
| `docs/SUPPLIER_DATA_INVENTORY.md` | Lokale bronnulmeting en switcherdataset | Geen oorspronkelijke leveranciersbron of generator aanwezig |
| `docs/PRODUCT_DATA_CONTRACT.md` | Begrippen, open data- en bedrijfsregels | Conceptuele werkbasis; geen definitieve mapping of beschikbare waarden |
| `docs/LIVE_THEME_COMPARISON.md` | Historische lokale/live-pariteit op 2026-08-03 | Geen actuele remote hercontrole toegestaan |
| `docs/DEVELOPMENT_THEME.md`, `docs/SHOPIFY_ENVIRONMENT.md` | Vastgelegde preview- en omgevingsgrenzen | Geen actuele remote status; preview vereist aparte toestemming |
| Repository op basiscommit | Gerichte regels, referenties, hashes, groottes en JSON-parsing | Statisch bewijs; geen storefront- of Theme Editor-runtime |
| Lokale Shopify CLI / Theme Check | Een volledige lokale statische controle | Tooluitvoer is geen functionele goedkeuring |

## 4. Methode

1. De vereiste projectdocumenten zijn volledig gelezen en de hervatbasis is mechanisch gecontroleerd.
2. Bestaande auditbevindingen zijn alleen gericht herbevestigd met `git`, `rg`, bestandsmetadata, hashes, veilige JSON-parsing en bronregels.
3. De reeds binnen de gedeeltelijke taak uitgevoerde ene volledige Theme Check-run is geconsolideerd; er is geen tweede volledige run uitgevoerd.
4. Iedere opgenomen bevinding heeft precies een bereikbaarheidsstatus, zekerheid, impact en blokkadestatus.
5. Kandidaten zijn afgebakend met bestanden, acceptatie, tests, preview, menselijke goedkeuring en rollback.

Geen onbeperkte nieuwe repository-audit, browserruntime, Shopify-query of remote themecontrole is uitgevoerd.

## 5. Veiligheidsbevestiging

Tijdens `BC-TECH-002` zijn geen Shopify-data, themes, Liquid-, JavaScript-, CSS-, JSON-, JSONC-, locale-, template-, bron- of productdatabestanden gewijzigd. Er is geen theme gestart, gepusht, gepulld of gepubliceerd, geen import uitgevoerd en geen defect opgelost. Alleen dit rapport en `docs/MASTERPLAN.md` zijn de toegestane documentatie-uitvoer.

## 6. Managementsamenvatting

- **BEWEZEN:** `sections/main-product.liquid` is met 3.223 regels en 146.809 bytes het actieve PDP-kernbestand voor alle 7.827 producten in de Adminsnapshot. Het combineert presentatie, formulier, prijs, media, specificaties, beide switchers, inline CSS en inline JavaScript.
- **BEWEZEN:** de actieve prijsweergave bevat de vaste klanttekst `Verwachte levertijd: 8 - 9 weken`, zonder bewezen product-, leverancier- of operationele databron. Dit is het hoogste actieve klant-/bedrijfsrisico.
- **BEWEZEN:** V2 wordt bij 3.658 producten getriggerd, terwijl de asset 3.383 unieke handles bevat. Het verschil van 275 bewijst geen 275 defecten; setvergelijking en runtimebewijs ontbreken.
- **BEWEZEN:** het legacy-pad bestaat en kan conditioneel starten, maar `custom.group` heeft in de Adminsnapshot dekking 0/7.827. Behoud, refactor of verwijdering vereist runtimebewijs en een menselijke keuze.
- **BEWEZEN:** acht backup-/QA-/debugassets, samen 5.639.492 bytes, hebben geen statische inkomende theme-referentie. Zij blijven onderdeel van de historische live asset-set en mogen niet zonder bewaarbeleid en aparte taak worden verwijderd.
- **BEWEZEN:** er is geen testframework, CI-workflow, lintconfiguratie, formele fixturebasis, browsermatrix of rollbackrunbook in de bereikbare repositorygeschiedenis.
- **NIET BEWEZEN:** volledige app-, pixel-, script- en runtime-injectie. Actieve JSON bevat nul bewezen app blocks/embeds, maar meerdere actieve sections en layouts ondersteunen dynamische injectie.
- **AANBEVELING:** maak eerst een afzonderlijke taak voor een reproduceerbare lokale Theme Check-/kwaliteitsbasis. De vaste levertijdtekst heeft hogere klanturgentie, maar de oplossing blijft geblokkeerd totdat de projecteigenaar de toegestane klantweergave en operationele eigenaar vaststelt.

## 7. Huidige technische basis

| Onderdeel | Feitelijke stand | Gevolg |
| --- | --- | --- |
| Git | `main`; basis `2b11f1e...`; lokaal alleen documentatie gewijzigd | Geschikt als bewijsbasis, niet als implementatietoestemming |
| Live theme-snapshot | Historische pariteit van 396 lokale en 396 live bestanden op 2026-08-03 | Huidige remote pariteit niet opnieuw bewezen |
| Producttemplate | Alle 7.827 producten gebruiken default producttemplate met `main-product` | PDP-wijzigingen hebben potentieel brede regressie-impact |
| V2-switcher | Trigger 3.658; dataset 433 groepen, 560 menu's, 3.383 unieke handles | Dekking en runtime moeten apart worden bewezen |
| Legacy-switcher | Conditioneel codepad; `custom.group` 0/7.827 in Adminsnapshot | Niet actief bewezen, ook niet veilig verwijderbaar bewezen |
| Test/CI | Geen formele tests, CI, lintconfig of fixtures gevonden | Eerst reproduceerbare kwaliteits- en smokebasis nodig |
| Preview | Unpublished development-theme `192770375946` historisch vastgelegd | Gebruik uitsluitend na afzonderlijke expliciete toestemming |
| Dynamische integraties | Nul app blocks/embeds in actieve JSON; injectiepunten bestaan | Externe afhankelijkheden blijven onbewezen |

## 8. Classificatiemodel

| Dimensie | Toegestane waarden | Betekenis |
| --- | --- | --- |
| Bereikbaarheid | `ACTIVE_LIVE`, `REACHABLE_FROM_ACTIVE`, `CONDITIONALLY_REACHABLE`, `AVAILABLE_NOT_ACTIVE`, `LEGACY_OR_ORPHAN_CANDIDATE`, `BACKUP_OR_DEBUG`, `DYNAMIC_OR_NOT_PROVEN`, `NOT_REPRODUCED` | Relatie tot actieve configuratie of statisch codepad |
| Zekerheid | `CONFIRMED`, `HIGH_CONFIDENCE`, `PROBABLE`, `CANDIDATE`, `NOT_PROVEN` | Sterkte van code-, configuratie-, tool- of runtimebewijs |
| Impact | `P0`, `P1`, `P2` | P0 is directe project-/klantgate; P1 nodig voor veilige kernontwikkeling; P2 beheers- of kwaliteitswerk |
| Blokkade | `READY_FOR_SEPARATE_TASK`, `BLOCKED_BY_PRODUCT_DATA`, `BLOCKED_BY_INFORMATION_ARCHITECTURE`, `BLOCKED_BY_BUSINESS_RULE`, `BLOCKED_BY_RUNTIME_EVIDENCE`, `BLOCKED_BY_APP_OR_EXTERNAL_DEPENDENCY`, `HUMAN_DECISION_REQUIRED` | Voorwaarde voordat een afzonderlijke taak uitvoerbaar kan worden |

Een `CONFIRMED` classificatie bevestigt alleen het omschreven feit. Zij bevestigt niet automatisch klantimpact, oorzaak of oplossing.

## 9. Centraal issueregister

| ID | Titel | Impact | Type | Bereikbaarheid | Zekerheid | Exacte bestanden | Regels/zoekverwijzing | Bewijs | Mogelijke impact | Niet bewezen | Blokkade | Kandidaat | Verplichte test | Rollback | Menselijke beslissing |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `TS-001` | Vaste onbewezen levertijd | P0 | klantinformatierisico | `ACTIVE_LIVE` | `CONFIRMED` | `sections/main-product.liquid`, `templates/product.json` | main-product 768/771; producttemplate 33-35 | Letterlijke tekst in actief price-block; geen bron in beschikbare data | Onjuiste klantbelofte op alle relevante PDP's | Juiste waarde/tekst en feitelijke storefrontweergave | `BLOCKED_BY_BUSINESS_RULE` | `PROPOSED-TECH-03` | PDP-varianten, lege data, mobiel/desktop, cartcontext | Geisoleerde revert plus preview-smoke | Kies tonen/verbergen/fallback, eigenaar en bron |
| `TS-002` | V2-trigger en datasetdekking verschillen | P0 | data-afhankelijkheid | `REACHABLE_FROM_ACTIVE` | `HIGH_CONFIDENCE` | `sections/main-product.liquid`, `assets/product-switcher-data.json` | main-product 510-514; dataset-safe parse | Admin 3.658 triggers tegenover 3.383 unieke handles | Stille ontbrekende switcheropties of navigatie voor een onbekende productset | Welke triggers geen datasetmatch hebben, welke handles geen trigger hebben en hoe de numerieke delta 275 wordt verklaard | `BLOCKED_BY_PRODUCT_DATA` | `PROPOSED-TECH-07` | Setvergelijking, ontbrekende groep/product, representatieve groepen | Geen datawijziging; herstel naar bewezen assetversie | Autoriseer latere Admin-/bronvergelijking en fixtures |
| `TS-003` | PDP-kernbestand concentreert verantwoordelijkheden | P1 | regressierisico | `ACTIVE_LIVE` | `CONFIRMED` | `sections/main-product.liquid` | 146.809 bytes; 3.223 regels; style 28-475; script 1631-1692 | Actief voor 7.827 producten en bevat formulier, prijs, media, specs en switchers | Een lokale wijziging kan meerdere actieve PDP- en koopfuncties tegelijk raken | Dat omvang op zichzelf een functioneel defect veroorzaakt | `HUMAN_DECISION_REQUIRED` | `PROPOSED-TECH-08` | Volledige PDP-/cart-/switcherregressie | Kleine stappen en herstelcommit per stap | Keur grens en volgorde van latere opsplitsing goed |
| `TS-004` | Specificaties lezen custom vendorbron | P1 | klantinformatierisico | `CONDITIONALLY_REACHABLE` | `HIGH_CONFIDENCE` | `sections/main-product.liquid`, `sections/product-specs.liquid` | main-product 1536; product-specs 11; native vendor 693-694 | Codeverschil met bewezen native `product.vendor` | Merk kan in zichtbare specificaties ontbreken of van native vendor afwijken | Dat merk nu zichtbaar ontbreekt; `has_specs` is conditioneel | `BLOCKED_BY_RUNTIME_EVIDENCE` | `PROPOSED-TECH-04` | Product met/zonder specs en vendor, structured data | Revert van een latere geisoleerde broncorrectie | Bevestig gewenste merkbron en zichtbare semantiek |
| `TS-005` | V2 laadt grote asset en logt runtime-informatie | P1 | performance | `REACHABLE_FROM_ACTIVE` | `CONFIRMED` | `snippets/bc-product-switcher.liquid`, `assets/bc-product-switcher.js`, `assets/product-switcher-data.json` | snippet 13-15; JS 28-45, 133-189, 327-360 | 1.894.030-byte assetfetch en `console.info`/`warn`-paden | Extra netwerk-, parse- en consolebelasting op V2-producten | Netwerk-/CPU-impact en logfrequentie op echte apparaten | `READY_FOR_SEPARATE_TASK` | `PROPOSED-TECH-07` | Netwerk, console, render en navigatie op mobiel/desktop | Asset-/JS-revert met preview-hermeting | Kies meetdrempels en toegestane runtimeomgeving |
| `TS-006` | Legacy-switcher blijft conditioneel aanwezig | P1 | regressierisico | `CONDITIONALLY_REACHABLE` | `CONFIRMED` | `sections/main-product.liquid`, `assets/global.js` | main-product 516-686/1114-1202; global 1225-1640 | Lege V2-trigger plus `custom.group`; Adminsnapshot custom.group 0/7.827 | Dubbele switcherlogica vergroot onderhouds- en toekomstige regressieruimte | Toekomstige/dynamische activatie en functionele correctheid | `HUMAN_DECISION_REQUIRED` | `PROPOSED-TECH-07` | Legacyfixture, section-fetch, navigatie, fallback | Behoud huidige code tot apart besluit; revert latere wijziging | Kies behoudsperiode en bewijsdrempel |
| `TS-007` | `kleur` en `basiskleur` conflicteren | P1 | data-afhankelijkheid | `CONDITIONALLY_REACHABLE` | `HIGH_CONFIDENCE` | `sections/main-product.liquid`, `assets/product-switcher-data.json` | main-product 570-573; datasetkeys | Bestaande code/data gebruiken beide begrippen | Opties kunnen over verschillende assen worden verdeeld of niet matchen | Gewenste semantiek, normalisatie en productdekking | `BLOCKED_BY_PRODUCT_DATA` | `PROPOSED-TECH-07` | Waarde-as, volgorde en combinatie-uniciteit | Geen mapping wijzigen; herstel asset bij latere proef | Productdata-eigenaar kiest contractbegrip na bronnen |
| `TS-008` | Losse media-section mist `variant_images` | P1 | defect | `LEGACY_OR_ORPHAN_CANDIDATE` | `CONFIRMED` | `sections/product-media.liquid` | regel 3; Theme Check `UndefinedObject` | Lokale assign ontbreekt; nul actieve sectionreferenties | Runtimefout wanneer later via Theme Editor geactiveerd | Dat de section ooit wordt geactiveerd en het exacte runtimegedrag | `BLOCKED_BY_RUNTIME_EVIDENCE` | `PROPOSED-TECH-05` | Toegestane Theme Editor-/sectionfixture en media | Section niet activeren; revert aparte correctie | Kies behouden, repareren of later verwijderen na bewijs |
| `TS-009` | Losse product-info mist bewezen context | P1 | defect | `LEGACY_OR_ORPHAN_CANDIDATE` | `PROBABLE` | `sections/product-info.liquid` en gerenderde snippets | product-info 7-8; snippetcontracten vereisen block/form/section | Nul actieve referenties; contextverschil statisch zichtbaar | Productformulier, variantpicker of buy-buttons kunnen bij activering falen | Dat activering werkelijk faalt en welke blocks geraakt zijn | `BLOCKED_BY_RUNTIME_EVIDENCE` | `PROPOSED-TECH-05` | Sectionfixture, variant picker en buy-buttons | Niet activeren; latere wijziging apart revertbaar | Kies doel/eigenaarschap van section |
| `TS-010` | Losse related-section nest een sectiontag | P1 | defect | `LEGACY_OR_ORPHAN_CANDIDATE` | `PROBABLE` | `sections/bc-related-products.liquid` | regel 5 | Nul actieve referenties; geneste `{% section %}` statisch gevonden | Activering kan parsen of renderen van gerelateerde producten breken | Parser-/runtimegedrag bij activering | `BLOCKED_BY_RUNTIME_EVIDENCE` | `PROPOSED-TECH-05` | Theme Check gericht en toegestane sectionruntime | Niet activeren; latere fix geisoleerd revertbaar | Kies doel of afvoerpad na bewijs |
| `TS-011` | Header bevat zes `href="#"`-doelen | P1 | toegankelijkheid | `ACTIVE_LIVE` | `CONFIRMED` | `sections/header.liquid`, `sections/header-group.json` | header 1628-1635; group 15 | Zes onvoorwaardelijke doelen; geen clickhandler gevonden | Dode acties en verwarrende focus-/navigatie-ervaring | Gewenste routes en exacte browser-/toetsenbordimpact | `BLOCKED_BY_INFORMATION_ARCHITECTURE` | `PROPOSED-TECH-09` | Klik, toetsenbord, focus, mobiel drawer, routes | Content/configuratie terugzetten via previewbewijs | Kies doelen of expliciet verbergen |
| `TS-012` | Actieve homeconfiguratie bevat lege doelen | P1 | data-afhankelijkheid | `ACTIVE_LIVE` | `CONFIRMED` | `templates/index.json`; betrokken home-sections | 17 lege linkvelden; 14 lege collectionvelden | Actieve JSON plus disabled/non-link renderpaden | Zichtbare disabled acties of ontbrekende contentjourneys | Welke lege velden bewust zijn en gewenste content | `BLOCKED_BY_INFORMATION_ARCHITECTURE` | `PROPOSED-TECH-09` | Home-CTA's, kaarten, brandrail, mobiel/keyboard | Alleen aparte configuratie-/codetaak met herstelbewijs | Kies content, doelen en verborgen states |
| `TS-013` | Theme Check-basis is niet volledig reproduceerbaar bestuurd | P1 | tooling | `DYNAMIC_OR_NOT_PROVEN` | `CONFIRMED` | Hele theme; geen `.theme-check.yml` | Volledige run: 19 offenses/15 bestanden; configuratie ontbreekt | Theme Check-JSON, CLI-versies en Git-scan | Latere taken kunnen verschillende of netwerkafhankelijke kwaliteitsuitslagen krijgen | Welke toolversie/config later normatief is en externe schemastabiliteit | `READY_FOR_SEPARATE_TASK` | `PROPOSED-TECH-01` | Herhaalbare versie, commando, counts en exitsemantiek | Alleen toolingdocumentatie/config in aparte taak revertbaar | Kies pinning, toegestane configuratie en baselinebeleid |
| `TS-014` | Formele test-, CI- en lintbasis ontbreekt | P1 | testgat | `NOT_REPRODUCED` | `CONFIRMED` | Bereikbare repositorygeschiedenis | Geen workflows/package/test/spec/fixture/lintconfig | Git-padscan van 407 huidige/historische paden | Automatische regressiedetectie ontbreekt | Gewenst framework, CI-platform en browsermatrix | `READY_FOR_SEPARATE_TASK` | `PROPOSED-TECH-02` | Mechanische en menselijke minimale regressiematrix | Testdocumentatie/config per kleine commit terugdraaien | Kies tool, runtime en vereiste checks |
| `TS-015` | Dynamische apps/pixels/scripts zijn onvolledig bekend | P1 | externe afhankelijkheid | `DYNAMIC_OR_NOT_PROVEN` | `CONFIRMED` | Actieve JSON, layouts en acht `@app`-sections | nul app blocks/embeds; `content_for_header` en `@app` aanwezig | Configuratie- en codebewijs | Refactors kunnen verborgen integraties, tracking of checkoutgedrag breken | Volledige runtime-injectie en externe eigenaars | `BLOCKED_BY_APP_OR_EXTERNAL_DEPENDENCY` | `PROPOSED-TECH-11` | Toegestane previewbron, netwerk, events en appfuncties | Geen refactor zonder inventaris; herstelcommit | Autoriseer bewijsroute en externe eigenaren |
| `TS-016` | Branch-, preview- en rollbackrunbook ontbreekt | P1 | governance/release | `NOT_REPRODUCED` | `CONFIRMED` | Git-metadata en projectdocumentatie | Alleen main-ref; geen volledig runbook/CI/PR-bewijs | Repository- en docs-scan | Onveilige uitvoering of lastig herstel | Branch protection en actuele previewstatus | `HUMAN_DECISION_REQUIRED` | `PROPOSED-TECH-10` | Procesdry-run zonder theme-mutatie; checklistreview | Niet-destructieve revert en bestaand rollbacktheme | Kies branch/PR/reviewers/preview/rollbackrollen |
| `TS-017` | Acht backup-/QA-/debugassets staan in theme-assets | P2 | technische schuld | `BACKUP_OR_DEBUG` | `CONFIRMED` | Acht bestanden in paragraaf 15 | Naam, bytes, hashes en nul statische refs | Samen 5.639.492 bytes; historische live asset-set | Assetbeheer, publiceerbare omvang en bronverwarring nemen toe | Directe HTTP-download, bewaardoel en eigenaarschap | `HUMAN_DECISION_REQUIRED` | `PROPOSED-TECH-06` | Hash-, referentie-, runtime- en rollbackbewijs | Eerst externe/artefactbewaring bewijzen; niets verwijderen | Kies bewaarbeleid en eigenaar |
| `TS-018` | Overige losse productonderdelen hebben geen actieve referentie | P2 | technische schuld | `LEGACY_OR_ORPHAN_CANDIDATE` | `CONFIRMED` | Zes sections, twee snippets en een CSS-asset | Matrix in paragraaf 14 | Nul statische inkomende referenties | Onbedoelde activering of opruiming kan verborgen functionaliteit breken | Dynamische Theme Editor-activatie en oorspronkelijk doel | `HUMAN_DECISION_REQUIRED` | `PROPOSED-TECH-05` | Preset/runtime/referentiecontrole per bestand | Geen verwijdering; later per bestand herstellen | Kies eigenaar, doel en bewaartermijn |
| `TS-019` | Debugcomments en console-uitvoer zijn bereikbaar | P2 | technische schuld | `REACHABLE_FROM_ACTIVE` | `CONFIRMED` | `sections/main-product.liquid`, `assets/bc-product-switcher.js` | main-product 591-598/1115-1116; JS 12-26 en calls | Statische code in actieve paden | Productieconsole-/HTML-ruis en extra support- of performancebelasting | Exacte klant-, performance- of supportimpact | `READY_FOR_SEPARATE_TASK` | `PROPOSED-TECH-07` | HTML-bron, console, ontbrekende data en normale groep | Geisoleerde revert van latere loggingwijziging | Kies gewenst productie-logbeleid |
| `TS-020` | Productuitleg gebruikt `#`-doelen | P2 | toegankelijkheid | `ACTIVE_LIVE` | `CONFIRMED` | `sections/main-product.liquid`, `sections/product-specs.liquid`, `sections/short-specs.liquid` | main-product 1543/1546; specs 17/20; short 13 | Letterlijke placeholderdoelen | Zichtbare uitlegactie kan nergens heen navigeren en focus verwarren | Zichtbaarheid per product en gewenste uitlegcontent | `BLOCKED_BY_INFORMATION_ARCHITECTURE` | `PROPOSED-TECH-09` | Product met specs, keyboard/focus en targetroutes | Revert content-/renderwijziging na preview | Kies doelcontent of verbergbeleid |
| `TS-021` | CLI-versie kan tijdens controle driften | P1 | tooling | `DYNAMIC_OR_NOT_PROVEN` | `CONFIRMED` | Globale Shopify CLI; geen repobestand | Eerdere gedeeltelijke run wijzigde 4.6.0 naar 4.6.1 | Versie voor/na en onveranderde Git-status | Toolresultaten en lokale omgeving kunnen zonder gepland beleid veranderen | Toekomstige reproduceerbaarheid en een stabiel pinpad | `HUMAN_DECISION_REQUIRED` | `PROPOSED-TECH-01` | Versiecheck zonder self-update, schone Git-status | Geen repo-rollback; herstel van globale tooling apart beheren | Kies gepinde versie en updatebeleid |

Verdeling: **21 bevindingen**, waarvan **2 P0**, **15 P1** en **4 P2**. Zekerheid: **16 CONFIRMED**, **3 HIGH_CONFIDENCE**, **2 PROBABLE**, **0 CANDIDATE** en **0 NOT_PROVEN**. `NOT_REPRODUCED` wordt alleen als bereikbaarheidsstatus gebruikt waar een ontbrekende inrichting of uitgesloten verdenking is onderzocht.

## 10. P0-bevindingen

| ID | Waarom P0 | Direct uitvoerbaar? |
| --- | --- | --- |
| `TS-001` | Een vaste levertijdbelofte staat in het actieve prijsblok zonder bewezen bron; onjuiste klantinformatie kan verkoop, service en vertrouwen raken | Nee. Eerst commerciële/operationele keuze over tonen, verbergen of goedgekeurde fallback, plus eigenaar en bron |
| `TS-002` | V2 is actief bereikbaar, maar trigger- en datasetpopulatie verschillen aantoonbaar; switchernavigatie kan voor een onbekende set ontbreken | Alleen validatie kan apart worden voorbereid; definitieve dekking/mapping blijft door productdata en runtimebewijs geblokkeerd |

Geen P0 is in deze taak opgelost.

## 11. P1-bevindingen

De vijftien P1-bevindingen vallen uiteen in vier werkstromen:

| Werkstroom | Issues | Veilige grens |
| --- | --- | --- |
| Tooling en regressiebasis | `TS-013`, `TS-014`, `TS-016`, `TS-021` | Eerst reproduceerbaarheid en proces vastleggen; geen theme-code wijzigen |
| PDP en switchers | `TS-003` t/m `TS-007` | Eerst runtime-/databewijs en testbasis; geen brede refactor |
| Kandidaatsections | `TS-008` t/m `TS-010` | Niet activeren, repareren of verwijderen zonder eigen taak en previewbewijs |
| Navigatie en externe grenzen | `TS-011`, `TS-012`, `TS-015` | IA/content- en appbesluiten vooraf; geen doelen of integraties verzinnen |

## 12. Productpagina-risico's

`sections/main-product.liquid` is **ACTIVE_LIVE** en **CONFIRMED** bereikbaar via `templates/product.json`. De combinatie van 3.223 regels, 146.809 bytes, inline CSS (regels 28-475), inline JavaScript (1631-1692), productformulier, prijs, media, specificaties, V2-switcher, legacyfallback en structured data vergroot de wijzigings- en regressieomvang. Omvang is geen defectbewijs, maar wel een bewezen onderhoudsrisico.

De kooproute steunt daarnaast op `product-info.js` en dynamische section-rendering. Een brede afbakening mag pas na een regressiebasis, runtimebewijs en goedgekeurde previewvolgorde. De native structured-data-output gebruikt `product | structured_data`; de aparte vendorregel in de specificatietabel bewijst daarom geen structured-datafout.

**Hoogste klantbevinding:** de vaste levertijd staat in het actieve prijsblok. Beschikbare Admin-, contract- en leveranciersdocumentatie bewijzen geen bron voor acht tot negen weken. Een technisch team mag daarom geen alternatieve tekst, berekening of verbergregel kiezen zonder bedrijfsbesluit.

## 13. V2-/legacy-switcher

| Aspect | V2 | Legacy |
| --- | --- | --- |
| Activering | `custom.switch_group` via main-product 510-514 en render 1112-1113 | Alleen bij lege V2-trigger plus niet-lege `custom.group`, main-product 516-589 |
| Huidig bewijs | 3.658 Admin-triggers; asset met 433 groepen, 560 menu's en 3.383 unieke handles | `custom.group` heeft 0/7.827 dekking in de Adminsnapshot |
| Runtime | Same-origin fetch van `product-switcher-data.json`; groep/productmatch en navigatie in `bc-product-switcher.js` | Inline product-/collectiedata; extra section-fetches en navigatie in `global.js` |
| Bereikbaarheid | `REACHABLE_FROM_ACTIVE`, codepad `CONFIRMED` | `CONDITIONALLY_REACHABLE`, codepad `CONFIRMED`; huidige UI-nonactivatie snapshotgebonden |
| Open bewijs | Setgelijkheid, ontbrekende matches, console-/netwerkimpact en geldige combinaties | Toekomstige/dynamische activatie, correctness en noodzaak |
| Data-afhankelijkheid | Numerieke populatiedelta 275, onbekende setrelatie, `kleur`/`basiskleur`, bron/generator en snapshotketen | `custom.group`, collectie-/menuvelden en prijs-/specificatiepayload |
| Veilige volgorde | Eerst meetbare set- en runtimevalidatie; pas daarna eventuele refactor | Eerst menselijke behoudskeuze en toegestane fixture; geen verwijdering |

De handle is alleen binnen de actuele asset bewezen uniek. Dit maakt handle nog niet tot definitieve primaire sleutel of switcherarchitectuur. De twee zichtbare afwijkende Hotbath-groepen tussen primaire dataset en QA2 zijn bevestigd, maar oorzaak en juistheid zijn zonder bron/generator **NOG ONDERZOEKEN**.

## 14. Losse productsections/snippets

| Bestand | Grootte | Bereikbaarheid | Inkomende referentie | Gerichte bevinding | Adviescategorie |
| --- | ---: | --- | --- | --- | --- |
| `sections/product-info.liquid` | 757 B / 23 regels | `LEGACY_OR_ORPHAN_CANDIDATE` | Geen statische sectionreferentie | Geeft alleen `product` door waar snippets ook block/form/sectioncontext verwachten; activeringsdefect `PROBABLE` | Reproduceren per eigen taak; niet activeren/verwijderen |
| `sections/product-media.liquid` | 366 B / 17 | `LEGACY_OR_ORPHAN_CANDIDATE` | Geen | Gebruikt ongedefinieerde `variant_images`; Theme Check bevestigt dit | Reproduceren en doel laten beslissen |
| `sections/product-description.liquid` | 571 B / 22 | `LEGACY_OR_ORPHAN_CANDIDATE` | Geen | Rendert description; actieve main-product heeft een lege blockbranch en aparte hardcoded render | Code-/configuratie-anomalie analyseren; geen defect claimen |
| `sections/product-specs.liquid` | 5.356 B / 62 | `LEGACY_OR_ORPHAN_CANDIDATE` | Geen | Gebruikt custom vendor en `#`-uitlegdoelen, net als geintegreerde actieve variant | Samen met actieve specs testen, niet los repareren |
| `sections/bc-related-products.liquid` | 508 B / 20 | `LEGACY_OR_ORPHAN_CANDIDATE` | Geen | Nestelt `{% section 'related-products' %}`; potentieel ongeldig, runtime niet bewezen | Gerichte parse/runtime-reproductie |
| `sections/short-specs.liquid` | 1.529 B / 40 | `AVAILABLE_NOT_ACTIVE` | Geen actieve configuratie | Hardcoded titel ondanks schema-instelling; een `#`-uitlegdoel | Behoud tot doel/contentbesluit |
| `snippets/bc-product-short-specs.liquid` | 39 B / 1 | `LEGACY_OR_ORPHAN_CANDIDATE` | Geen renderreferentie | Bevat alleen verwijdercommentaar | Eigenaarschap/bewaarbesluit, geen directe verwijdering |
| `snippets/product-pros-cons.liquid` | 1.669 B / 46 | `LEGACY_OR_ORPHAN_CANDIDATE` | Geen renderreferentie | Verwacht `section_id`; bijbehorende CSS heeft eveneens nul refs | Samen met contentvelden/runtime beoordelen |

Afwezigheid van een statische referentie bewijst niet dat een preset nooit via Theme Editor kan worden toegevoegd.

## 15. Backup-/QA-/debugassets

| Asset | Bytes | Actieve referentie | Overlap/afwijking | Publieke theme-asset | Vervolgvoorwaarde |
| --- | ---: | --- | --- | --- | --- |
| `assets/bc-product-switcher.backup-debug.js` | 10.036 | Nee | Verschilt van primair; 57 toevoegingen/4 verwijderingen in gerichte vergelijking | In historische live asset-set; HTTP niet getest | Herkomst, bewaardoel en rollbackwaarde vaststellen |
| `assets/bc-product-switcher.js.backup-qa-round-1-20260706-214223` | 11.742 | Nee | Verschilt; primair gebruikt aanvullend `menu.values` | Idem | QA-context en behoudstermijn vaststellen |
| `assets/bc-product-switcher.js.backup-qa-round-1-rerun-20260707-110751` | 11.902 | Nee | SHA-256 bytegelijk aan primaire JS | Idem | Duplicaatstatus bewijzen en extern rollbackpad kiezen |
| `assets/product-switcher-data.backup.json` | 3.731 | Nee | 1 groep, 3 menu's, 6 handles | Idem | Bron/doel onbekend; niet verwijderen |
| `assets/product-switcher-data.backup-before-production.json` | 6.889 | Nee | 1 groep, 2 menu's, 12 handles | Idem | Productieketen en eigenaar bewijzen |
| `assets/product-switcher-data.json.backup-qa-round-1-20260706-214223` | 1.807.052 | Nee | 433 groepen, 568 menu's, 3.383 handles; nul expliciete values | Idem | Generatorketen ontbreekt; behoud vereist |
| `assets/product-switcher-data.json.backup-qa-round-1-rerun-20260707-110751` | 1.894.070 | Nee | 433/560/3.383; 2.478 values; andere hash dan primair | Idem | Semantiek en rollbackwaarde bewijzen |
| `assets/product-switcher-data.json.backup-qa-round-2-20260707-111611` | 1.894.070 | Nee | Zelfde aantallen; andere hash; twee groepen verschillen gericht van primair | Idem | Bronkeuze en verschilbetekenis bewijzen |

De acht assets zijn samen 5.639.492 bytes. Nul inkomende referenties bewijst geen client-download, maar ook geen veilige verwijderbaarheid. Een latere opruimtaak vereist minimaal hash-/inhoudsmatrix, eigenaar, externe bewaarlocatie, runtimebewijs, preview en een rollback zonder afhankelijkheid van het te verwijderen bestand.

## 16. Header-, link- en placeholderbevindingen

- `sections/header.liquid` is `ACTIVE_LIVE` en bevat zes onvoorwaardelijke `href="#"`-doelen voor Inspiratie, Advies, MijnBadkamerCity, Showrooms, Afspraak maken en Zakelijk. De gewenste routes zijn niet bewezen.
- `templates/index.json` bevat in actieve configuratie 17 lege linkvelden en 14 lege collectionvelden. Verschillende sections degraderen naar non-link- of disabled-states; drie lege hero-links hebben ook lege labels en bewijzen dus geen zichtbare CTA.
- `collection.category-landing.json` bewaart vier placeholderbeschrijvingen. De actieve section leest `block_description` niet, dus storefrontweergave daarvan is niet statisch bewezen.
- `#`-uitlegdoelen in product-/specificationcode zijn placeholders; normale skiplinks, interne anchors en SVG/inputfallbacks zijn niet als defect meegeteld.

De juiste scheiding is: letterlijke lege bestemming is technisch bewezen; gewenste route/content is `BLOCKED_BY_INFORMATION_ARCHITECTURE`; wel/niet tonen kan ook een Theme Editor- of bedrijfsbesluit zijn. Er is niets hersteld.

## 17. Theme Check en lokale tooling

| Onderdeel | Resultaat |
| --- | --- |
| CLI bij volledige run | Shopify CLI `4.6.0` |
| Volledige lokale run | `shopify theme check --path . --no-color --output json` |
| Exitcode | `1`; niet automatisch als codefout geinterpreteerd |
| Totaal | 19 offenses in 15 bestanden: 3 errors en 16 warnings |
| Errors | 1 externe `ValidJSON`-schemafetch/parse bij `config/settings_schema.json`; 2 `ValidSchemaTranslations` in `sections/featured-product.liquid` |
| Warnings | 5 orphan snippets; 2 variabelenaamwaarschuwingen; 3 unused assigns; `continue` buiten loop; 2 deprecated `img_tag`; ongedefinieerde `variant_images`; 2 ongedefinieerde `scheme_classes` |
| Assertion | In deze volledige run geen Windows-/Ruby-assertion; historische audit had die wel |
| Configuratie | Geen `.theme-check.yml`; remote schema-afhankelijkheid maakt een deel niet volledig lokaal stabiel |
| Huidige CLI | `shopify version` geeft na de gedeeltelijke uitvoering `4.6.1`; `shopify theme check --help` bevestigt `shopify theme check` met lokale `--path` |

Toolingbeperking: de als versieprobe bedoelde opdracht `shopify theme check -v` activeerde in de eerdere gedeeltelijke uitvoering een globale CLI-self-update van 4.6.0 naar 4.6.1 en wijzigde buiten de repository 26 globale packages; die probe geldt niet als gebruikte Theme Check-resultaatset. Er kwam geen repositorybestand bij. De hervatte opdrachten `shopify version` en `shopify theme check --help` wijzigden niets en in deze hervatting is niets geinstalleerd of geupdate. Dit is geen theme-codefout, maar wel bewijs dat versiepinning en een niet-mutatieve controleprocedure nodig zijn. Daarom is geen tweede volledige Theme Check-run uitgevoerd.

De eerdere verdenking van foutieve encoding in `assets/global.js:1509` is gericht **NOT_REPRODUCED**: de bron bevat correct Unicode-codepoint U+2713. Zij is gemotiveerd uitgesloten als issue.

## 18. Test-, CI- en regressiegaten

**BEWEZEN afwezig in 407 huidige/historische Git-paden:** CI-workflows, `package.json`/lockfile, Theme Check-config, lintconfig, test-/specdirectories, fixtures, Playwright, Cypress, Jest, Vitest, Lighthouse, pa11y, axe, aparte tooling- of datascripts en een README. De 34 JavaScriptbestanden zijn storefrontassets.

Projectdocumentatie bevat voorgestelde checklists, maar geen uitgevoerde functionele regressies, browsermatrix, performancebudget of zelfstandig rollbackrunbook. Backup-/QA-bestanden zijn geen formele fixtures of test-suite.

Dit gat maakt eerst een documenteerbare, reproduceerbare kwaliteits- en smokebasis nodig. Een tool- of CI-keuze is nog `HUMAN_DECISION_REQUIRED`.

## 19. Dynamische app-/scriptgrenzen

- In 18 actieve configuratiebestanden zijn nul `shopify://apps/...`-typen en nul geconfigureerde `@app`-blocks bewezen.
- `@app` wordt ondersteund door actieve sections `footer`, `header`, `main-article`, `main-cart-footer` en `main-product`; daarnaast door niet actief geconfigureerde `apps`, `featured-product` en `newsletter`.
- `content_for_header` bestaat in theme-, password- en gift-cardlayouts; `content_for_layout` en additional-checkout-injectie zijn eveneens aanwezig.
- `reviews.*`-paden bewijzen geen eigenaar of actieve app.

Conclusie: nul actieve app blocks/embeds in JSON is **BEWEZEN**. De volledige app-, pixel-, script-, event- en externe-injectielijst blijft `DYNAMIC_OR_NOT_PROVEN`. Voor refactors rond header, product, cart of layouts is eerst een afzonderlijk toegestane runtime-/integratiecontrole nodig.

## 20. Git-, preview- en rollbackbasis

**VOORSTEL, geen vastgesteld proces:** start latere taken vanaf schoon `main == origin/main`, leg de basiscommit en toegestane diff vast, gebruik een korte taakbranch na toestemming, maak kleine logische commits, review de diff, voer statische en functionele tests uit, preview alleen op unpublished theme `192770375946` na expliciete toestemming en behandel livepublicatie als aparte menselijke go/no-go-taak.

Rollbackvoorstel: bewaar basiscommit en testbewijs, gebruik een niet-destructieve revert van de geisoleerde wijziging, houd een bewezen rollbacktheme beschikbaar en voer na herstel dezelfde smoke tests uit. Branchnaam, PR-verplichting, reviewers, vereiste checks, previewcommando, rollbackrollen en bewaarbeleid zijn `OPEN BESLISSING`.

## 21. Kandidaatdeeltaken

De volgende twaalf ID's zijn uitsluitend voorstellen in dit rapport. Zij zijn geen officiele taken, niet actief en geven geen implementatietoestemming.

### PROPOSED-TECH-01 - Reproduceerbare Theme Check- en kwaliteitsbasis

| Veld | Voorstel |
| --- | --- |
| Prioriteit / omvang / volgorde | P0 / S / 1 |
| Status | `READY_FOR_SEPARATE_TASK` |
| Probleem en bewijs | Een run gaf 19 offenses in 15 bestanden; configuratie ontbreekt, een externe schemafout is instabiel en de CLI-versie dreef van 4.6.0 naar 4.6.1 |
| Exacte bestanden | Read-only input: `assets/`, `config/`, `layout/`, `locales/`, `sections/`, `snippets/`, `templates/`; voorgestelde nieuwe `.theme-check.yml` en `docs/THEME_CHECK_BASELINE.md`; geen themebestand aanpassen |
| Doel | Een gepinde, herhaalbare lokale controle met stabiel commando, exitsemantiek, baseline en scheiding tussen code- en toolingfouten |
| Bereikbaarheid / zekerheid | `DYNAMIC_OR_NOT_PROVEN` / `CONFIRMED` toolinggat |
| Scope | Versiepinning, configvoorstel, een baseline-run, compacte telling en reproduceerbaarheid |
| Buiten scope | Bestaande offenses oplossen, theme-code refactoren, Shopify of previewtheme benaderen |
| Afhankelijkheden | Technische eigenaar kiest CLI-/Theme Check-versie en updatebeleid; geen productdata/IA nodig |
| Verwachte wijzigingscategorie | Toolingconfiguratie en documentatie, alleen na aparte toestemming |
| Acceptatie | Zelfde basis geeft herhaalbare versie, commando, outputcategorieen en exitcode; externe schemafout apart gelabeld; Git-diff exact begrensd |
| Theme Check | Dit is de taakuitvoer; maximaal afgesproken runs en geen self-update |
| Functionele smoke | Geen storefrontclaim; alleen controleren dat tooling geen repobestand buiten scope maakt |
| Regressie/apparaten | N.v.t. voor browser; wel Windows-shell en eventueel tweede goedgekeurde omgeving |
| Preview | Niet nodig tenzij een latere offensefix wordt gecombineerd, wat buiten scope is |
| Menselijke goedkeuring | Versie, configuratie, baselinebeleid en outputlocatie vooraf goedkeuren |
| Rollback | Verwijder/revert uitsluitend de nieuw goedgekeurde config-/doccommit; globale tooling apart herstellen |

### PROPOSED-TECH-02 - Minimale smoke- en regressiebasis

| Veld | Voorstel |
| --- | --- |
| Prioriteit / omvang / volgorde | P0 / M / 2 |
| Status | `HUMAN_DECISION_REQUIRED` |
| Probleem en bewijs | Geen tests, fixtures, CI, linting, browsermatrix of uitgevoerd smokebewijs in Git |
| Exacte bestanden | Voorgestelde nieuwe `docs/SMOKE_REGRESSION_BASELINE.md`; eventuele testconfig/-fixtures zijn buiten deze eerste documentatiestap totdat de toolkeuze apart is goedgekeurd |
| Doel | Reproduceerbare minimale regressiematrix en representatieve, niet-persoonlijke fixtures vastleggen |
| Bereikbaarheid / zekerheid | `NOT_REPRODUCED` / `CONFIRMED` afwezigheid |
| Scope | Home, header/drawer, collectie, search, kaarten, PDP, cart, V2, toegestane legacyfixture, accountbasis, 404/lege states, mobiel/desktop/keyboard/structured data/performancebasis |
| Buiten scope | Defects oplossen, klantdata lezen, livepublicatie of volledige end-to-end launch-QA |
| Afhankelijkheden | Menselijke keuze van tooling, viewports, fixtures en previewrechten; geen leveranciersbron vereist |
| Verwachte wijzigingscategorie | Test-/QA-documentatie en later mogelijk testtooling |
| Acceptatie | Ieder kernpad heeft preconditie, stappen, verwacht resultaat, bewijsformaat en eigenaar; nul persoonsgegevens |
| Theme Check | Baseline uit kandidaat 01 als aparte statische gate |
| Functionele smoke | Alle genoemde kernpaden, inclusief add-to-cart zonder bestelling te plaatsen |
| Regressie/apparaten | Minimaal overeengekomen desktop, mobiel en toetsenbord; browsermatrix menselijk kiezen |
| Preview | Development-theme uitsluitend na aparte toestemming en targetcontrole |
| Menselijke goedkeuring | Fixtures, tool, browsermatrix, toegestane cartactie en bewijsopslag |
| Rollback | Test-/doccommit revertbaar; geen product- of theme-data als fixture muteren |

### PROPOSED-TECH-03 - Onbewezen vaste levertijd veilig behandelen

| Veld | Voorstel |
| --- | --- |
| Prioriteit / omvang / volgorde | P0 / XS-S / na bedrijfsbesluit, daarna zo vroeg mogelijk |
| Status | `BLOCKED_BY_BUSINESS_RULE` |
| Probleem en bewijs | `sections/main-product.liquid:768/771` toont vaste levertijdinformatie in het actieve price-block zonder bewezen bron |
| Exacte bestanden | Read-only bewijs: `sections/main-product.liquid`, `docs/PRODUCT_DATA_CONTRACT.md`, `docs/SUPPLIER_DATA_INVENTORY.md`; latere codewijziging uitsluitend `sections/main-product.liquid` tenzij een goedgekeurde bron apart wordt aangewezen |
| Doel | Na besluit voorkomen dat onbewezen logistieke informatie als klantbelofte verschijnt |
| Bereikbaarheid / zekerheid | `ACTIVE_LIVE` / `CONFIRMED` |
| Scope | Alleen de goedgekeurde displayregel en bijbehorende lege state; geen logistiek model ontwerpen |
| Buiten scope | Levertijden verzinnen, voorraadmapping, leverancierintegratie, bredere PDP-refactor |
| Afhankelijkheden | Projecteigenaar plus operationeel/logistiek eigenaar kiezen tonen, verbergen of exact goedgekeurde fallback en bron/actualiteit |
| Verwachte wijzigingscategorie | Kleine Liquid-/dataweergavecorrectie na aparte implementatietoestemming |
| Acceptatie | Geen onbewezen waarde; bron/lege state aantoonbaar; prijs/form/cart ongewijzigd; alle PDP-representanten slagen |
| Theme Check | Gerichte en volledige afgesproken run na wijziging |
| Functionele smoke | Product met waarde, zonder waarde, verschillende types, cartcontext |
| Regressie/apparaten | Mobiel, desktop, keyboard/reading order en visuele prijsblokcontrole |
| Preview | Verplicht op development-theme na toestemming; menselijk tekst-/bedrijfsregelreview |
| Menselijke goedkeuring | Exacte keuze vereist voor wat de klant ziet bij wel/geen bewezen levertijd; geen fallback is in dit plan gekozen |
| Rollback | Geisoleerde herstelcommit; vorige weergave alleen tijdelijk terug na expliciete risicoacceptatie |

### PROPOSED-TECH-04 - Vendor-/merkbron gericht reproduceren

| Veld | Voorstel |
| --- | --- |
| Prioriteit / omvang / volgorde | P1 / XS / 4 |
| Status | `BLOCKED_BY_RUNTIME_EVIDENCE` |
| Probleem en bewijs | Specificaties lezen `product.metafields.vendor`, terwijl native `product.vendor` bewezen bestaat |
| Exacte bestanden | `sections/main-product.liquid`, `sections/product-specs.liquid`, `templates/product.json` |
| Doel | Bewijzen of en wanneer merk in specificaties ontbreekt en welke bron semantisch bedoeld is |
| Bereikbaarheid / zekerheid | `CONDITIONALLY_REACHABLE` / `HIGH_CONFIDENCE` |
| Scope | Representatieve producten met/zonder specs/vendor; DOM en structured data vergelijken |
| Buiten scope | Vendorwaarden wijzigen, nieuwe metafields, brede specificatierefactor |
| Afhankelijkheden | Toegestane preview-/runtimefixture en menselijke bevestiging van merksemantiek; geen leveranciersbestand nodig voor reproductie |
| Verwachte wijzigingscategorie | Eerst bewijsdocumentatie; mogelijke kleine Liquidcorrectie pas later |
| Acceptatie | Codepad, zichtbaarheid, datawaarden en gewenste bron per state bewezen; geen aanname uit alleen Liquid |
| Theme Check | Gerichte controle op betrokken files plus afgesproken volledige gate na latere fix |
| Functionele smoke | PDP met specs, zonder specs, native vendor, ontbrekende vendor |
| Regressie/apparaten | Desktop/mobiel/keyboard plus structured-data-diff |
| Preview | Verplicht voor zichtbare wijziging, niet voor statische reproductie |
| Menselijke goedkeuring | Productdata-eigenaar bevestigt bron en label |
| Rollback | Eventuele broncorrectie als eenregelige geisoleerde revert |

### PROPOSED-TECH-05 - Losse kandidaatdefectsections per bestand valideren

| Veld | Voorstel |
| --- | --- |
| Prioriteit / omvang / volgorde | P1 / M / 5 |
| Status | `BLOCKED_BY_RUNTIME_EVIDENCE` |
| Probleem en bewijs | Acht losse onderdelen missen actieve referenties; drie hebben gerichte context-/nestingrisico's en overige hebben onbekend doel |
| Exacte bestanden | `sections/product-info.liquid`, `sections/product-media.liquid`, `sections/product-description.liquid`, `sections/product-specs.liquid`, `sections/bc-related-products.liquid`, `sections/short-specs.liquid`, `snippets/bc-product-short-specs.liquid`, `snippets/product-pros-cons.liquid`, `assets/component-product-pros-cons.css` |
| Doel | Per bestand doel, presetbaarheid, parse/runtime, afhankelijkheden en behouden/repareren/verwijderen-categorie bewijzen |
| Bereikbaarheid / zekerheid | `LEGACY_OR_ORPHAN_CANDIDATE` of `AVAILABLE_NOT_ACTIVE`; `CONFIRMED` statische status, `PROBABLE` mogelijke defects |
| Scope | Een matrix en alleen toegestane tijdelijke previewactivatie per onderdeel |
| Buiten scope | Bestanden verwijderen, activeren in live config of tegelijk refactoren |
| Afhankelijkheden | Eigenaar/doel en previewtoestemming; geen productdata behalve veilige representatieve fixtures |
| Verwachte wijzigingscategorie | Eerst bewijs; latere afzonderlijke reparatie- of opruimtaak per samenhangende set |
| Acceptatie | Iedere contextvariabele, schema/preset, referentie, renderuitkomst en eigenaar aantoonbaar |
| Theme Check | Gerichte filecontrole met stabiele baseline |
| Functionele smoke | Alleen in geautoriseerde previewstate; media, form, specs, related en pros/cons apart |
| Regressie/apparaten | Mobiel/desktop/keyboard waar output zichtbaar is |
| Preview | Verplicht voor activeringsclaims; nooit live |
| Menselijke goedkeuring | Per bestand behouden, repareren of apart verwijderonderzoek kiezen |
| Rollback | Tijdelijke previewconfig volledig herstellen; bestanden blijven behouden |

### PROPOSED-TECH-06 - Backup-/debugassetstrategie vaststellen

| Veld | Voorstel |
| --- | --- |
| Prioriteit / omvang / volgorde | P2 / S / 6 |
| Status | `HUMAN_DECISION_REQUIRED` |
| Probleem en bewijs | Acht theme-assets hebben nul statische refs, 5,64 MB totaal, overlap/divergentie en onbekend bewaardoel |
| Exacte bestanden | `assets/bc-product-switcher.backup-debug.js`, `assets/bc-product-switcher.js.backup-qa-round-1-20260706-214223`, `assets/bc-product-switcher.js.backup-qa-round-1-rerun-20260707-110751`, `assets/product-switcher-data.backup.json`, `assets/product-switcher-data.backup-before-production.json`, `assets/product-switcher-data.json.backup-qa-round-1-20260706-214223`, `assets/product-switcher-data.json.backup-qa-round-1-rerun-20260707-110751`, `assets/product-switcher-data.json.backup-qa-round-2-20260707-111611` |
| Doel | Eigenaarschap, herkomst, rollbackwaarde, externe bewaarlocatie en bewaartermijn beslissen |
| Bereikbaarheid / zekerheid | `BACKUP_OR_DEBUG` / `CONFIRMED` |
| Scope | Hash-/semantische vergelijking, historische Git-herleidbaarheid, directe URL/runtimebewijs en bewaarvoorstel |
| Buiten scope | Verwijderen, verplaatsen, comprimeren of primaire assets vervangen |
| Afhankelijkheden | Projecteigenaar/technisch eigenaar; voor data-inhoud ook productdata-eigenaar |
| Verwachte wijzigingscategorie | Governance/documentatie; latere aparte assetopruiming eventueel |
| Acceptatie | Per bestand eigenaar, reden, unieke inhoud, rollbacknoodzaak en bewezen bewaarlocatie |
| Theme Check | Baseline voor en na een eventuele latere opruimtaak |
| Functionele smoke | V2/legacy en directe assetrequests in preview na latere wijziging |
| Regressie/apparaten | Desktop/mobiel voor switcher; toetsenbord bij UI-ongewijzigdheid |
| Preview | Verplicht voor elke latere assetverwijdering |
| Menselijke goedkeuring | Bewaarbeleid en verwijderlijst afzonderlijk expliciet goedkeuren |
| Rollback | Externe/hash-gevalideerde kopie plus herstelcommit; nooit uitsluitend vertrouwen op verwijderd theme-asset |

### PROPOSED-TECH-07 - V2-/legacydekking en runtimebewijs

| Veld | Voorstel |
| --- | --- |
| Prioriteit / omvang / volgorde | P0 / M / 3 voor brononafhankelijke meting; datadeel later |
| Status | `BLOCKED_BY_PRODUCT_DATA` |
| Probleem en bewijs | V2 trigger/dataset verschillen, legacy bestaat conditioneel, logging en grote assetfetch zijn bereikbaar, bron/generator ontbreekt |
| Exacte bestanden | `snippets/bc-product-switcher.liquid`, `assets/bc-product-switcher.js`, `assets/product-switcher-data.json`, `sections/main-product.liquid`, `assets/global.js`; de acht exact benoemde backup-/QA-paden uit paragraaf 15 uitsluitend read-only |
| Doel | Setverschil, match-/fallbackstates, netwerk/console, combinaties en legacybereikbaarheid reproduceerbaar bewijzen voor architectuurbesluit |
| Bereikbaarheid / zekerheid | V2 `REACHABLE_FROM_ACTIVE`; legacy `CONDITIONALLY_REACHABLE`; code `CONFIRMED` |
| Scope | Read-only setanalyse, representatieve fixtures, previewruntime en bronketenvragen |
| Buiten scope | Switcherdata corrigeren, legacy verwijderen, keys mappen of JS refactoren |
| Afhankelijkheden | Leveranciers-/brondata voor volledige dekking; runtimetoestemming; keuze over legacy en `kleur`/`basiskleur` |
| Verwachte wijzigingscategorie | Eerst bewijs/test; later kleine data- of codeopdrachten per gevonden defect |
| Acceptatie | De 3.658/3.383-populatie- en setrelatie inclusief numerieke delta 275 verklaard, alle gekozen states getest, geen navigatie naar onbewezen target, metrics vastgelegd |
| Theme Check | Stabiele baseline; gerichte controle na iedere latere JS/Liquidwijziging |
| Functionele smoke | Geldige groep/product, ontbrekende groep/product, te weinig opties, navigatie, terug/refresh; legacyfixture alleen toegestaan |
| Regressie/apparaten | Mobiel/desktop/keyboard, netwerk, console en performancebaseline |
| Preview | Verplicht voor runtime; theme en testproducten vooraf menselijk goedkeuren |
| Menselijke goedkeuring | Bewijsroute, legacybeleid, bronkeuze en toegestane testset |
| Rollback | Geen mutatie in validatiefase; latere wijzigingen per asset geisoleerd herstellen |

### PROPOSED-TECH-08 - `main-product`-afbakening ontwerpen na testbasis

| Veld | Voorstel |
| --- | --- |
| Prioriteit / omvang / volgorde | P1 / L / pas na 01, 02, 03/04 en 07 |
| Status | `HUMAN_DECISION_REQUIRED` |
| Probleem en bewijs | Een actief bestand concentreert formulier, media, prijs, specs, beide switchers, inline CSS/JS en klantteksten |
| Exacte bestanden | Read-only input `sections/main-product.liquid`; voorgestelde nieuwe decompositie-uitvoer `docs/MAIN_PRODUCT_DECOMPOSITION.md`; andere codebestanden pas in afzonderlijk bewezen vervolgstappen |
| Doel | Verantwoordelijkheidsgrenzen en kleine refactorstappen ontwerpen zonder gedrag te veranderen |
| Bereikbaarheid / zekerheid | `ACTIVE_LIVE` / `CONFIRMED` onderhoudsrisico |
| Scope | Boundarydesign, afhankelijkheidsgraaf, extractievolgorde, prestatie- en regressiegates |
| Buiten scope | In een keer herschrijven, UX wijzigen, switcherarchitectuur kiezen of data-/bedrijfsregels invullen |
| Afhankelijkheden | Kandidaat 01/02, switcherbewijs, appcontrole en menselijke architectuurreview |
| Verwachte wijzigingscategorie | Latere reeks kleine Liquid/CSS/JS-refactors |
| Acceptatie | Iedere stap heeft exact gedragssurface, files, baseline, budget en rollback; nul functionele verandering zonder aparte acceptatie |
| Theme Check | Volledige stabiele gate per stap |
| Functionele smoke | Volledige PDP/form/cart/media/specs/switchermatrix |
| Regressie/apparaten | Mobiel/desktop/keyboard/structured data/performance |
| Preview | Verplicht per kleine stap |
| Menselijke goedkeuring | Grenzen, volgorde en toegestane eerste extractie |
| Rollback | Een kleine commit per extractie; revert en smoke per stap |

### PROPOSED-TECH-09 - Placeholder- en dode-linkafhandeling

| Veld | Voorstel |
| --- | --- |
| Prioriteit / omvang / volgorde | P1 / S-M / na IA/contentbesluit |
| Status | `BLOCKED_BY_INFORMATION_ARCHITECTURE` |
| Probleem en bewijs | Zes header-`#`-links, productuitleg-`#`-links en actieve lege homevelden zijn bewezen |
| Exacte bestanden | `sections/header.liquid`, `templates/index.json`, `sections/home-hero.liquid`, `sections/home-category-grid.liquid`, `sections/home-shop-by-style.liquid`, `sections/home-mijn-badkamercity.liquid`, `sections/home-brand-rail.liquid`, `sections/main-product.liquid`, `sections/product-specs.liquid`, `sections/short-specs.liquid`, `templates/collection.category-landing.json` |
| Doel | Alleen goedgekeurde doelen/content tonen en ontoegankelijke placeholderinteractie voorkomen |
| Bereikbaarheid / zekerheid | `ACTIVE_LIVE` / `CONFIRMED` lege doelen |
| Scope | Per item classificeren als route, content, Theme Editor-config of bewust verborgen state |
| Buiten scope | Categorieboom, URL's, labels of commerciele content verzinnen |
| Afhankelijkheden | `BC-IA-001`, content-eigenaar, eventueel bedrijfsregel en Theme Editor-eigenaarschap |
| Verwachte wijzigingscategorie | Later afzonderlijke content/config- of kleine rendercorrectie |
| Acceptatie | Geen zichtbare lege bestemming; juiste verborgen state; links bestaan; focusgedrag correct |
| Theme Check | Gerichte plus stabiele volledige gate bij codewijziging |
| Functionele smoke | Header desktop/mobile, homekaarten/CTA's, productuitleg en category landing |
| Regressie/apparaten | Mobiel/desktop/keyboard/screenreadernaam |
| Preview | Verplicht voor zichtbare wijziging |
| Menselijke goedkeuring | Per bestemming doel, label, content en tonen/verbergen kiezen |
| Rollback | Config-/codewijziging per groep geisoleerd herstellen |

### PROPOSED-TECH-10 - Branch-, preview- en rollbackwerkwijze

| Veld | Voorstel |
| --- | --- |
| Prioriteit / omvang / volgorde | P0 / XS-S / parallel met 01 |
| Status | `HUMAN_DECISION_REQUIRED` |
| Probleem en bewijs | Alleen main is lokaal bewezen; volledig PR-, preview-, release- en rollbackrunbook ontbreekt |
| Exacte bestanden | Voorgestelde nieuwe `docs/TECHNICAL_CHANGE_WORKFLOW.md`; geen branch of theme in deze kandidaatdefinitie |
| Doel | Herhaalbaar proces voor kleine branches/commits, diffreview, preview, go/no-go, revert en post-change smoke |
| Bereikbaarheid / zekerheid | `NOT_REPRODUCED` / `CONFIRMED` procesgat |
| Scope | Rollen, gates, commandoverboden, targetcontrole, bewijs, incident-/rollbackstappen |
| Buiten scope | Branch aanmaken, previewtheme muteren, GitHubinstellingen of live theme wijzigen |
| Afhankelijkheden | Projecteigenaar en technisch eigenaar; actuele previewthemecontrole later apart |
| Verwachte wijzigingscategorie | Governance-documentatie; externe branch protection eventueel later |
| Acceptatie | Exact basis/branch/commit/review/preview/release/rollback/post-smokeproces met eigenaar per gate |
| Theme Check | Plaats als verplichte pre-/postgate na kandidaat 01 |
| Functionele smoke | Verwijs naar matrix uit kandidaat 02 |
| Regressie/apparaten | Gate vereist relevante mobiel/desktop/keyboardset per wijziging |
| Preview | Theme `192770375946` alleen na expliciete toestemming en role/targetcontrole |
| Menselijke goedkeuring | Branch-/PR-model, reviewers, mergebeleid, preview- en rollbackrollen |
| Rollback | Runbook zelf via docrevert; implementatierollback niet-destructief per kleine commit |

### PROPOSED-TECH-11 - App- en dynamische afhankelijkheidscontrole

| Veld | Voorstel |
| --- | --- |
| Prioriteit / omvang / volgorde | P1 / S-M / voor header/PDP/cart/layout-refactors |
| Status | `BLOCKED_BY_APP_OR_EXTERNAL_DEPENDENCY` |
| Probleem en bewijs | Actieve JSON bewijst nul app blocks, maar `@app`, `content_for_header`, checkout en reviews-injectiepunten bestaan |
| Exacte bestanden | `layout/theme.liquid`, `layout/password.liquid`, `templates/gift_card.liquid`, `sections/footer.liquid`, `sections/header.liquid`, `sections/main-article.liquid`, `sections/main-cart-footer.liquid`, `sections/main-product.liquid`, `snippets/card-product.liquid`, `sections/featured-product.liquid` |
| Doel | Toegestane runtime inventaris van apps, pixels, scripts, events en eigenaars voor refactorveiligheid |
| Bereikbaarheid / zekerheid | `DYNAMIC_OR_NOT_PROVEN` / `CONFIRMED` bewijsgrens |
| Scope | Previewbron, netwerk/eventconsole, beheer-/eigenaarbevestiging zonder persoonsgegevens |
| Buiten scope | Apps/scopes wijzigen, scripts blokkeren, consent-/analyticsarchitectuur kiezen |
| Afhankelijkheden | Expliciete toegangstoestemming en app-/privacy-/analytics-eigenaren |
| Verwachte wijzigingscategorie | Eerst bewijsdocumentatie; later integratietests |
| Acceptatie | Alle zichtbare injecties op gekozen routes met bron/eigenaar/criticaliteit; onbekenden expliciet |
| Theme Check | Alleen statische grens, geen bewijs van runtime-apps |
| Functionele smoke | Header, PDP, cart, checkout-overgang en consent zonder bestelling |
| Regressie/apparaten | Mobiel/desktop/keyboard en relevante events/netwerk |
| Preview | Verplicht; live alleen read-only indien later afzonderlijk toegestaan |
| Menselijke goedkeuring | Toegestane bewijsroute, accounts/scopes en externe eigenaren |
| Rollback | Geen wijziging in inventarisfase; latere refactor per integratie herstelbaar |

### PROPOSED-TECH-12 - Test- en bewijsopslag standaardiseren

| Veld | Voorstel |
| --- | --- |
| Prioriteit / omvang / volgorde | P1 / XS-S / 2, samen met smokebasis |
| Status | `READY_FOR_SEPARATE_TASK` |
| Probleem en bewijs | Checklists bestaan verspreid, maar bewijsformaat, fixtureversies, screenshots/logs en retentie zijn niet bestuurd |
| Exacte bestanden | Voorgestelde nieuwe `docs/TEST_EVIDENCE_STANDARD.md`; eventuele `tests/`-/artefactpaden blijven buiten scope totdat opslag en tooling apart zijn goedgekeurd |
| Doel | Elke latere technische taak koppelen aan basiscommit, commando, versie, fixture, resultaat, preview en reviewer |
| Bereikbaarheid / zekerheid | `NOT_REPRODUCED` / `CONFIRMED` governancegat |
| Scope | Schema, naamgeving, privacy, retentie, pass/fail en kruisverwijzing naar masterplanbewijs |
| Buiten scope | Grote binaries/productdumps committen, persoonsgegevens opslaan of tests uitvoeren |
| Afhankelijkheden | Repo-eigenaar, privacy/juridisch verantwoordelijke en toolingkeuze |
| Verwachte wijzigingscategorie | Documentatie en eventueel ignore-/artefactbeleid na aparte toestemming |
| Acceptatie | Een compacte template met herleidbaarheid, geen secrets/persoonsdata en expliciete retentie |
| Theme Check | Sla alleen compacte samenvatting en versie/exit/counts op, geen duizenden regels |
| Functionele smoke | Bewijsformat voor alle routes uit paragraaf 29 |
| Regressie/apparaten | Verplicht viewport/browser/input metadata bij visueel/functioneel bewijs |
| Preview | Preview-ID, theme-role, datum en menselijke beoordeling vastleggen |
| Menselijke goedkeuring | Opslaglocatie, retentie, privacy en vereiste artefacten |
| Rollback | Documentatiestandaard als aparte revertbare commit |

De onderwerpen zijn niet samengevoegd omdat tooling, smoke-uitvoering en bewijsopslag verschillende beslissers en acceptatiecriteria hebben. Switcherdekking, logging en legacy zijn wel in kandidaat 07 gecombineerd: dezelfde runtimefixtures en setvergelijking zijn nodig voordat een gerichte code- of datataak zinvol kan worden afgebakend.

## 22. Afhankelijkhedenmatrix

| Kandidaat | Productdata | IA/content | Bedrijfsregel | Runtime/app | Menselijke keuze | Huidige uitkomst |
| --- | --- | --- | --- | --- | --- | --- |
| 01 Theme Check-basis | Nee | Nee | Nee | Lokale tooling | Versie/config | Kan apart worden aangemaakt |
| 02 Smoke-/regressiebasis | Alleen representatieve fixtures | Nee | Teststates niet verzinnen | Previewtoegang | Tool/browsermatrix | Kan na keuze apart |
| 03 Levertijd | Ja voor dynamiek | Nee | Ja | Preview | Klantweergave/eigenaar | Geblokkeerd |
| 04 Vendor | Nee voor reproductie | Nee | Merksemantiek | Preview | Bronkeuze | Eerst runtimebewijs |
| 05 Losse sections | Beperkte fixtures | Nee | Nee | Theme Editor/preview | Doel per bestand | Eerst runtimebewijs |
| 06 Backups | Bron/generator voor betekenis | Nee | Nee | Directe asset/runtime | Bewaarbeleid | Geblokkeerd op besluit |
| 07 Switchers | Ja voor volledige dekking | Nee | Legacy-/logbeleid | Preview/runtime | Bron en legacy | Deels geblokkeerd |
| 08 Main-product | Afhankelijk per onderdeel | Mogelijk | Mogelijk | App/runtime | Architectuurgrens | Na basiswerk |
| 09 Placeholders | Nee | Ja | Soms | Preview | Doelen/tonen | Geblokkeerd |
| 10 Releasewerkwijze | Nee | Nee | Nee | Previewstatus | Proces/rollen | Eerst besluit |
| 11 Apps/dynamiek | Nee | Nee | Consent mogelijk | Ja | Toegang/eigenaren | Geblokkeerd extern |
| 12 Bewijsopslag | Nee | Nee | Nee | Tooling | Privacy/retentie | Kan apart worden aangemaakt |

## 23. Wat zonder leveranciersbestanden verder kan

| Werk | Voorwaarde | Geen toestemming in deze taak |
| --- | --- | --- |
| Reproduceerbare Theme Check-/kwaliteitsbasis | Gepinde versie en configuratiebesluit | Kandidaat 01 eerst officieel maken |
| Test- en bewijsformat | Tool-/privacy-/retentiekeuze | Kandidaten 02/12 eerst officieel maken |
| Branch-/preview-/rollbackrunbook | Menselijke governancekeuze | Geen branch/themehandeling nu |
| Vendorprobleem read-only reproduceren | Toegestane previewfixture | Geen broncorrectie nu |
| Losse sections statisch/previewmatig reproduceren | Per bestand doel en previewtoestemming | Geen activering of verwijdering nu |
| V2-netwerk-, console- en UI-meting | Toegestane representatieve previewproducten | Geen volledige dekking of datawijziging claimen |
| App-/dynamische grens voorbereiden | Toegestane bewijsroute | Geen app- of scopewijziging |

## 24. Wat een menselijke beslissing vereist

| Beslissing | Exacte vraag | Eigenaarrol |
| --- | --- | --- |
| Levertijd | Moet de vaste tekst worden verborgen, of alleen worden vervangen door een exact goedgekeurde, brongebonden waarde/fallback; wie beheert bron en actualiteit? | Projecteigenaar + operationeel/logistiek eigenaar |
| Tooling | Welke Shopify CLI/Theme Check-versie en configuratie zijn normatief; mag een configbestand worden toegevoegd? | Technisch eigenaar |
| Testbasis | Welke browsers, viewports, fixtures, cartacties en performancegrenzen zijn vereist? | Projecteigenaar + technisch eigenaar |
| Branch/release | Is PR verplicht, wie reviewt, welke checks blokkeren merge en wie autoriseert preview/rollback? | Projecteigenaar + repositoryeigenaar |
| Legacy | Welke bewijsdrempel en bewaartermijn gelden voordat legacycode kan worden aangepast of verwijderd? | Projecteigenaar + technisch/productdata-eigenaar |
| Backups | Welke bestanden hebben rollback-/auditwaarde, waar worden zij buiten publiceerbare assets bewaard en hoe lang? | Projecteigenaar + technisch eigenaar |
| Navigatie | Wat zijn correcte doelen/content en welke items moeten tot die tijd verborgen blijven? | IA-/content-eigenaar + projecteigenaar |
| Apps | Welke runtime-/beheerroute mag worden gebruikt en wie bezit apps, pixels, scripts en consent? | Technisch + privacy/analytics-eigenaar |
| Eerste implementatie | Welke kandidaat wordt na review een officiele taak en krijgt exacte wijzigingstoestemming? | Projecteigenaar |

## 25. Wat geblokkeerd blijft

- Definitieve switcherbron, handle-/SKU-koppelsleutel en volledige 3.658/3.383-dekking.
- Leveranciermapping, productkwaliteitsvalidatie voor circa 20.000 producten en definitieve Shopify-opslag.
- Voorraad-, levertermijn-, prijs-, fiscale, garantie-, retour- en overige klantbeloftes.
- Tegelcalculatorwaarden en calculatorlogica op werkelijke data.
- Definitieve categorie-, URL-, filter- en navigatiestructuur.
- Legacyverwijdering en backup-/debugassetverwijdering.
- Grootschalige `main-product`-refactor zolang kwaliteits-, smoke-, app- en rollbackbasis ontbreken.
- Refactors rond dynamische apps, pixels of scripts zonder toegestane runtime-inventaris.

## 26. Aanbevolen uitvoeringsvolgorde

| Volgorde | Kandidaat/richting | Reden |
| ---: | --- | --- |
| 1 | `PROPOSED-TECH-01` | Maakt statische kwaliteitsuitvoer reproduceerbaar en voorkomt versie-/toolingdrift in alle latere taken |
| 2 | `PROPOSED-TECH-10` en `PROPOSED-TECH-12` na governancekeuze | Leggen veilige branches, bewijs en rollback vast zonder productdata |
| 3 | `PROPOSED-TECH-02` | Bouwt minimale functionele regressiebasis voor actieve routes |
| 4 | Menselijk besluit voor `PROPOSED-TECH-03` | Hoogste actieve klantinformatierisico, maar geen technische fallback verzinnen |
| 5 | `PROPOSED-TECH-04` en brononafhankelijk deel van `PROPOSED-TECH-07` | Kleine gerichte reproductie van PDP-/switcherrisico's |
| 6 | `PROPOSED-TECH-11` | Vangt dynamische afhankelijkheden af voor kernrefactors |
| 7 | `PROPOSED-TECH-05`, `06` en `09` | Vereisen eigenaars-/IA-/bewaarbesluiten en zijn niet eerste klantfix |
| 8 | `PROPOSED-TECH-08` | Brede PDP-afbakening pas nadat test- en afhankelijkheidsbewijs bestaat |

## 27. Eerste ongeblokkeerde technische taak

**Aanbevolen:** maak `PROPOSED-TECH-01 - Reproduceerbare Theme Check- en kwaliteitsbasis` als eerste afzonderlijke officiele taak aan.

Reden: zij heeft geen leveranciersdata, klantbelofte, IA of Shopify-toegang nodig; zij adresseert een bewezen toolinggat en maakt alle volgende technische acceptatie betrouwbaarder. De taak is klein en kan beperkt blijven tot versie/configuratie/baseline/documentatie. De projecteigenaar moet vooraf alleen CLI-versie, updatebeleid, configuratiebestand en acceptatie van de bestaande baseline kiezen. Dit plan activeert die taak niet.

## 28. Hoogste actieve klant-/bedrijfsrisico

`TS-001`, de vaste tekst `Verwachte levertijd: 8 - 9 weken`, is het hoogste actieve klant-/bedrijfsrisico. De tekst staat aantoonbaar in het actieve prijsblok; een actuele, productspecifieke of leveranciergebonden bron is niet bewezen.

Benodigde menselijke beslissing voordat implementatie `READY` kan worden:

1. of de tekst zonder bewezen bron volledig wordt verborgen;
2. of alleen een exact door commercieel/operationeel eigenaar goedgekeurde fallback mag worden getoond;
3. welke bron, actualiteitsgrens en eigenaarsrol later een productspecifieke waarde autoriseren;
4. wat de goedgekeurde lege state is.

Er is in dit plan geen vervangende levertijdtekst gekozen.

## 29. Minimale regressiematrix

| Route/onderdeel | Kerncontrole | Desktop | Mobiel | Toetsenbord | Extra bewijs |
| --- | --- | :---: | :---: | :---: | --- |
| Homepage | Sections, zichtbare CTA's, lege states, interne links | Ja | Ja | Ja | Console/netwerk en layout |
| Header/drawer | Navigatie, submenu's, `#`-doelen, focus en sluiten | Ja | Ja | Ja | Focusvolgorde/naam |
| Collectie | Grid, sortering, filters, paginering, lege state | Ja | Ja | Ja | URL/canonical/structured data |
| Productkaart | Titel, merk, prijs, badges, media en link | Ja | Ja | Ja | Geen layoutshift |
| Zoekresultaat | Resultaten, nulresultaat, foutstate en kaarten | Ja | Ja | Ja | Zoek-URL/indexgrens |
| PDP basis | Media, titel, SKU, prijs, tekst, specs en links | Ja | Ja | Ja | Structured data en console |
| Productformulier/cart | Variant, aantal, fouten, add-to-cart en cart | Ja | Ja | Ja | Geen bestelling; netwerkresponse |
| V2-switcher | Geldige/ontbrekende groep/product, opties en navigatie | Ja | Ja | Ja | Assetgrootte, timing, console |
| Legacyfallback | Alleen met geautoriseerde fixture; section-fetch en navigatie | Ja | Ja | Ja | Bewijs dat pad werkelijk actief is |
| Tegel zonder calculator | Geen defecte of verzonnen calculatorweergave | Ja | Ja | Ja | Producttypefixture goedkeuren |
| Klantaccountbasis | Toegankelijke entry/errorstate zonder persoonsgegevens | Ja | Ja | Ja | Accountmodelgrens |
| 404/lege/errorstates | Correcte status, herstelroute en geen dode actie | Ja | Ja | Ja | HTTP/status indien toegankelijk |
| Dynamische injectie | Apps/scripts/events op home/PDP/cart | Ja | Ja | Ja | Bron/eigenaar/netwerk |
| Performancebasis | Home, collectie, search en PDP op vaste fixtures | Ja | Ja | N.v.t. | Budget en tool nog kiezen |

Dit is een voorgesteld testplan, geen uitgevoerde functionele goedkeuring.

## 30. Preview- en rollbackvereisten

Voor iedere later geautoriseerde zichtbare of functionele wijziging:

1. controleer schoon `main == origin/main` en leg de basiscommit vast;
2. begrens exacte bestanden en verboden zij-effecten;
3. maak een kleine taakbranch en kleine commits alleen na toestemming;
4. voer stabiele Theme Check plus gerichte tests uit;
5. gebruik development-theme `192770375946` alleen na expliciete target-/roltoestemming;
6. leg desktop-, mobiel- en toetsenbordbewijs vast waar relevant;
7. laat de projecteigenaar preview en klanttekst/gedrag beoordelen;
8. behandel livepublicatie als afzonderlijke opdracht;
9. leg niet-destructieve herstelcommit en rollbacktheme vooraf vast;
10. herhaal dezelfde smoke tests na wijziging en na eventuele rollback.

## 31. Open vragen

1. Welke CLI-/Theme Check-versie en configuratie worden normatief zonder self-update?
2. Welke browsermatrix, viewports, fixtures en performancebudgetten gelden?
3. Welke exacte klantweergave is toegestaan wanneer levertijd niet bewezen is?
4. Is native `product.vendor` de gewenste merkbron voor alle zichtbare specificatiecontexten?
5. Welke V2-triggers hebben geen datasetmatch, welke dataset-handles hebben geen trigger en hoe wordt de numerieke delta 275 verklaard?
6. Welke bron/generator/eigenaar verklaart de switcherdataset en twee gerichte QA2-afwijkingen?
7. Welke legacy- en kandidaatbestanden hebben nog Theme Editor- of toekomstig doel?
8. Wat is het bewaarbeleid voor backup-/QA-/debugassets?
9. Welke header-, home- en productuitlegdoelen/content zijn goedgekeurd?
10. Welke apps, pixels en scripts worden dynamisch geinjecteerd en wie bezit ze?
11. Welke branch-, PR-, preview-, release- en rollbackrollen zijn verplicht?
12. Welke kandidaat wordt na menselijke review als eerste officiele taak aangemaakt?

## 32. Risico's

| Risico | Beheersing |
| --- | --- |
| Classificatie wordt als defect- of verwijderbewijs gelezen | Per issue expliciet scheiden wat bewezen en onbewezen is; aparte taak en toestemming verplicht |
| Vaste levertijd blijft onterecht staan tijdens planning | Projecteigenaar prioriteert bedrijfsbesluit; geen onbewezen technische fallback |
| Toolinguitvoer verandert door versie/netwerk | Versie pinnen, config en exitsemantiek vastleggen, externe schemafout apart labelen |
| Brede PDP-refactor veroorzaakt regressies | Eerst kwaliteits-, smoke-, app- en rollbackbasis; kleine commits en preview |
| V2-dekkingsverschil wordt foutief als 275 defects geclaimd | Set-/runtimebewijs verplicht; brondata en generator ontbreken expliciet houden |
| Legacy/backups worden te vroeg verwijderd | Eigenaarschap, runtime, bewaar- en rollbackbewijs als gate |
| Statische nulreferentie mist dynamisch gebruik | Theme Editor-, app- en runtimevalidatie voor iedere kandidaat |
| Testbewijs bevat persoonsgegevens of secrets | Alleen representatieve niet-persoonlijke fixtures en goedgekeurd retentiebeleid |
| Historische livepariteit wordt als actueel gelezen | Snapshotdatum noemen; remote hercontrole alleen in aparte toegestane taak |

## 33. Aanbevolen volgende stap

De projecteigenaar beoordeelt dit plan en beslist afzonderlijk:

1. of `PROPOSED-TECH-01` als nieuwe officiele read-only/toolingtaak wordt aangemaakt;
2. welke bedrijfsregel geldt voor de vaste levertijdtekst;
3. welke branch-/preview-/rollback- en bewijskeuzes vooraf nodig zijn.

Die beoordeling heeft op 2026-08-11 plaatsgevonden: `BC-TECH-002` staat `DONE`, `BC-TECH-001` blijft `BLOCKED` en geen kandidaat is actief.

## 34. Veiligheidsbevestiging

`BC-TECH-002` heeft uitsluitend lokale read-only analyse en documentatie uitgevoerd. Shopify Admin is niet benaderd; Shopify-data, themes, theme-code, producten, leverancier-/brondata en apps zijn niet gewijzigd. Er is geen theme-push, pull, publicatie, dev-server, import, generator, branch, commit of push uitgevoerd. De eerdere globale CLI-self-update is als toolingbeperking vastgelegd en wijzigde geen repositorybestand. Dit rapport geeft geen implementatie- of verwijdertoestemming.

## 35. Menselijke goedkeuring

De BadkamerCity-projecteigenaar heeft `BC-TECH-002` op 2026-08-11 binnen de read-only onderzoeks- en decompositiescope goedgekeurd. Het plan is daarmee een bestuurbare technische werkbasis en de taak staat `DONE`.

De 21 bevindingen en 12 `PROPOSED-TECH-*`-kandidaten zijn geen implementatieopdrachten en geen officiele taken. Hun classificaties geven geen toestemming om bestanden te wijzigen, verplaatsen of verwijderen. Binnen `BC-TECH-002` is geen defect opgelost.

De eerste technische taak wordt later afzonderlijk gekozen, afgebakend en expliciet toegestaan. De vaste levertijdtekst vereist eerst een afzonderlijk commercieel en operationeel besluit; er is geen vervangende tekst of fallback goedgekeurd. Shopify, themes, theme-code, producten en data zijn niet gewijzigd.
