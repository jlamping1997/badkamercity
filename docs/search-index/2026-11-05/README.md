> **5 november 2026 — actuele publicatie bevestigd:** de eigenaar heeft **BadkamerCity - Re-Bel tegelkeuze (196238639370)** gepubliceerd; dit is nu MAIN. Voormalig MAIN 196227170570 is UNPUBLISHED. Zoekindex en nieuwe kaartprijsweergave zijn live gecontroleerd; SEARCH-01 is afgerond. De gedateerde COTTO-/SEARCH-publicatieverzoeken hieronder beschrijven eerdere checkpoints en zijn geen resterende actie.

> **Publicatie-afstemming COTTO-01:** de oorspronkelijke zoekbescherming (historisch controlepunt MD5 `e0783b4ed15e1acc70ff1518cf2b5f20`, vóór de prijsuitbreiding met concept-JS `11de150d3e2797a6f35742a813281fcb`) is meegenomen in **UNPUBLISHED196238639370 — BadkamerCity - Re-Bel tegelkeuze**, samen met de vier COTTO-winkelwagenbestanden. Eigen 23 runtimechecks en gecombineerde 5/5 validatie PASS. Publiceer alleen dit gecombineerde concept. Het losse zoekconcept 196116087050 mist de winkelwagenwijzigingen en mag daarna niet als latere release worden gebruikt. De onafhankelijke publieke controle na reparatie vindt Verlavio 851, Re-Bel 22 en RR6001 als exact Cottoceramix-artikel.

# Zoekindex — ontbrekende Verlavio-resultaten

5 november 2026. **OWNER_PUBLISHED / INDEX_LIVE_VERIFIED / UI_LIVE_VERIFIED**.

De eigenaar vraagt de volledige zoekindex te herstellen. De externe zoekroute mist Verlavio en vervangt daarbij bestaande Shopify-resultaten door nul. De begrensde frontendbescherming is in een echt conceptthema gecontroleerd. De eigenaar heeft de vastgepinde installer succesvol uitgevoerd én het gecombineerde thema gepubliceerd. De index en de nieuwe “Vanaf”-/kaartweergave zijn onafhankelijk in de publieke API en echte live Chrome bevestigd. MAIN is nu196238639370; SEARCH-01 is afgerond. De frontendbescherming maakt ontbrekende indexdocumenten niet aan.

## Nulmeting vóór de serverreparatie

| Bron of controle | Waarneming |
| --- | --- |
| Actuele MAIN | `196227170570 — BadkamerCity - Verlavio voorraad en levertijd`; door eigenaar gepubliceerd |
| Externe service | Versie `0.4.0` |
| Actieve indexcollectie | `bc_sync_20261103t120045_4e7799` |
| Profielen | 226 |
| Globaal indexprofiel | 11.679 producten |
| Shoppingprofiel | 10.937 producten |
| Shopify ACTIVE en gepubliceerd | 12.760 producten; waaronder 851 Verlavio |
| Externe zoekopdrachten | Verlavio, Fabriecio en VSB_2001 elk nul; Hotbath 7.540 |
| Native Shopify | Aanwezige Verlavio-resultaten en vijf suggesties; resultaatcounts wisselen tussen metingen |

De aantallen horen bij verschillende query-/profielscopes; trek er geen ongeteste exacte ontbrekende-productenlijst van af. De native Verlavio-resultaattelling wisselde tijdens de controles van 188 tot 214. Dit bewijst geen dekking van alle 851 Verlavio-artikelen. Het concrete defect is wel bewezen: Shopify levert resultaten die de externe route door nul vervangt.

Het eerste runtime-rapport toonde een actieve timer en een gefaalde service; LAST_ERROR bevestigde de één-variantaanname als blokkade. De index van 3 november in bovenstaande nulmeting is inmiddels volgens de installeruitvoer vervangen door de gecontroleerde generatie van 5 november. De onafhankelijke publieke nacontrole bevestigt de nieuwe generatie en correcte Verlavio-/SKU-resultaten; zie de eindcontrole hieronder. Dit bewijst geen vijfminutenkoppeling voor leveranciersfeeds.

## Begrensde frontendbescherming — eerder gecontroleerde losse preview

De huidige MAIN-versie van `assets/bc-external-filters.js` is via Shopify teruggelezen en gelijk aan de lokale uitgangsversie: MD5 `8b99d6d9f8a1fedf8f6f96ca5f007f3a`. De publieke CDN-versie wordt geminificeerd; een afwijkende ruwe CDN-body is daarom geen bewijs van andere logica.

Het concept behoudt de aanwezige native Shopify-productkaarten als alle voorwaarden gelden:

- dezelfde zoekopdracht als waarvoor de native kaarten werkelijk zijn geladen;
- geen actieve filters;
- de externe zoekroute retourneert nul producten;
- er staan daadwerkelijk native productkaarten in de pagina.

Deze situatie toont geen foutbanner. Echte fouten behouden de bestaande waarschuwing. Een lege gefilterde zoekopdracht blijft leeg. Prijs nul, querygeschiedenis en navigatie blijven behouden. Een deels gevulde externe resultaatset met ontbrekende artikelen blijft een backendprobleem: deze bescherming vult die niet aan.

**UNPUBLISHED 196116087050 — BadkamerCity - Zoekresultaten herstel** is opgebouwd vanuit de werkelijke MAIN. Eerst zijn de drie eerder gepubliceerde voorraadtekstbestanden overgenomen en is **1.381 / 1.381 volledige bestandspariteit** bevestigd. De volledige eindmanifestvergelijking bevat opnieuw **1.381 bestanden met exact één verschil**: `assets/bc-external-filters.js`, MD5 `e0783b4ed15e1acc70ff1518cf2b5f20`. Alle overige bestanden zijn gelijk aan MAIN. Geen MAIN-write of publicatie door de uitvoerder.

**PASS:** 23 runtimecontroles en officiële validator revisie 2. Echte Chrome-preview, telkens via zoeken met Enter:

| Zoekopdracht | Werkelijk resultaat in concept |
| --- | --- |
| `verlavio` | 214 native resultaten, 36 native kaarten; nul externe kaarten, geen foutbanner |
| `Hotbath` | 7.540 resultaten, 24 externe kaarten; bestaande externe route behouden |
| `VSB_2001` | Eén native Malmö-kaart met echte productfoto; externe zoekroute geeft nul |

Deze proeven bewijzen de begrensde fallback en behoud van de bestaande Hotbath-route, geen volledige indexdekking. Geen nieuwe cart-, checkout- of betalingstest voor deze zoektaak.

## Oorzaak en actuele bron gecontroleerd

LAST_ERROR van **5 november 2026, 17:01:22 UTC** stopt tijdens normalisatie op product 10698301571338: “Meer of minder dan één variant”. Dit is **Lagoo Nesso plafondbuis**, met zestien echte Shopify-varianten en prijzen €78–€215. De aangeleverde actuele bron is exact geverifieerd:

| Bestand | Bytes | SHA256 |
| --- | ---: | --- |
| Synchronisatieworker | 98.867 | `2064b549e173d709fe1d5e8e5fe8cb549276e817d46b111510fcc4bc12471cf2` |
| API-app | 12.998 | `6e4895a1ebc7937da9fbec0a92b141213320e87a382a2fcf5d479daedde0a573` |

De diagnose en bronoverdracht zijn afgerond. Privébronbestanden, catalogusdata en credentialbestanden worden niet in publieke Git opgeslagen. De publieke implementatie bevat uitsluitend de gerichte patchmodules, installatiecode en tests.

## Complete variantcorrectie

- **Worker:** één zoekdocument per product; alle variant-SKU's als genormaliseerde `sku_aliases`. De minimumvariantprijs wordt deterministisch gekozen; `price_varies` markeert verschillende prijzen. Geen product overslaan of Shopify-varianten aanpassen.
- **API:** normale en exacte SKU-zoekopdrachten gebruiken alle aliassen zodra de nieuwe snapshot actief is. Het bestaande snapshot-/schemacontract blijft werken vóór activatie; geen gedeeltelijke omschakeling.
- **Prijsweergave:** prijsverschillen krijgen “Vanaf” bij de minimumprijs, via de externe productkaart en de gedeelde kaartdata. Een SKU-match op een duurdere variant mag niet stil als die specifieke variantprijs worden gepresenteerd.

Geconsolideerde controle PASS: 49 Python-tests (18 worker, 11 API, 16 installer en vier release-/ASCII-controles) plus 39 frontendcontroles, samen 88. De standalone installer is ASCII en 34.166 bytes; SHA256 `7c924875d0d3378e5c21f46a481346e1f750ef16efb249d9bea19a874f5a7aec`. Deze controles bewijzen de lokale implementatie, geen geslaagde serveruitvoering.

De drie bedoelde themabestanden zijn uitsluitend naar het gecombineerde UNPUBLISHED-concept 196238639370 geschreven, met behoud van de COTTO-wijzigingen en bestaande zoekfallback. Alle drie readbacks zijn exact; MAIN is niet geschreven. Echte browserregressie: Hotbath 7.540 resultaten/24 externe kaarten en Verlavio 36 native kaarten/nul externe kaarten zonder foutbanner. Aanvullend PASS: de echte gecombineerde previewroute `bc-card-data` voor Lagoo Nesso levert `price_cents=7800` en `price_varies=true`, zonder `image_url`; het Lagoo-fotoverbod blijft behouden. Echte Chrome-SKU-proef `VSB_2001`: één native Malmö-kaart met productfoto, nul externe kaarten en geen foutbanner.

| Bestand in `shopify/current/` | Teruggelezen LIVE-MAIN-MD5 |
| --- | --- |
| `assets/bc-external-filters.js` | `11de150d3e2797a6f35742a813281fcb` |
| `sections/bc-card-data.liquid` | `b4e58946edc02ba1e44dd876c6239ef5` |
| `snippets/bc-external-filters.liquid` | `2a0136a8420e8a710f448c99d5fc3aad` |

## Serverreparatie uitgevoerd en gecontroleerd

De eigenaar heeft installercommit `05a54c8d8b7df8c41644eec7abd5bd812a3cb6d5` uitgevoerd en de eindstatus **`applied_verified`** gedeeld. Het serververslag meldt:

| Onderdeel | Gerapporteerd en door installer gecontroleerd |
| --- | --- |
| Actieve collectie | `bc_sync_20261105t180750_9caf43` |
| Producten | 12.760 |
| Profielen | 226 |
| Variantsnapshot | `variant_aliases_v1=true` |
| Automatische timer | Hervat |

Alle controles melden GOED: volledige ID-dekking en documentteruglezing, prijzen en mediareferenties, primaire en secundaire SKU's, lokale/publieke API, CORS, B2C/RVS en behoud van de catalogus. De gecontroleerde worker en API zijn geïnstalleerd; een root-back-up is gemaakt. De uitvoer en herstelgegevens blijven privé; geen ruwe logs, bronbestanden of credentialbestanden in deze publieke repository.

De installatie is bewezen door de gedeelde serveruitvoer én de onderstaande onafhankelijke publieke nacontrole. Er zijn geen Shopify-producten, varianten, prijzen, voorraad of afbeeldingen gewijzigd.

De bestaande uurlijkse timer is volgens het eindverslag hervat. Een volgende toekomstige timeruitvoering is nog niet waargenomen; geen claim dat toekomstige automatische verversingen al zijn getest. Geen nieuwe scheduler of ChatGPT-automatisering aangemaakt en geen vijfminutenverversing van leveranciersfeeds ingericht.

De installatie voorziet volledige staging en alle SKU-teruglezing vóór atomaire activatie, root-back-ups met modus 0700 en herstel bij fouten, een deadline van 15 minuten en voortgang elke 20 seconden. De nieuwe worker is pas na geslaagde indexactivatie geïnstalleerd. De oorspronkelijke timerstand is behouden.

## Onafhankelijke publieke eindcontrole

De onderstaande eindcontrole hoort bij de generatie van 5 november rond 18:07 UTC. Latere COTTO-03-imports vallen buiten deze momentopname; directe indexdekking daarvan is niet beweerd.

**API_PUBLIC_VERIFIED.** Health en alle gecontroleerde zoekantwoorden melden dezelfde nieuwe generatie `20261105T180750_9caf43` / collectie `bc_sync_20261105t180750_9caf43`:

| Controle | Werkelijk resultaat |
| --- | --- |
| Profielen / globaal / shopping | 226 / 12.760 / 12.018 |
| Verlavio | 851 |
| `N8271TC` en `N8270CH` | Elk één exacte SKU-match op product 10698301571338; aliassen werken |
| Nesso-prijs / foto | `price_cents=7800`, `price_varies=true`, geen afbeelding conform Lagoo-fotoverbod |
| `RR6001` | Eén exacte match, merk Cottoceramix |
| Re-Bel / Hotbath | 22 / 7.540 |
| Niet-bestaande zoekterm | Nul resultaten |

**LIVE_BROWSER_VERIFIED.** In echte Chrome na Exit preview, zonder preview-iframe, via de werkelijke header “verlavio” ingevoerd en Enter gedrukt: correcte zoekkop, **851 producten, 24 externe kaarten, nul native kaarten, geen foutbanner**. De eerste Helsingborg-kaart hoort bij het gezochte assortiment. De huidige MAIN gebruikt dus de herstelde externe index; dit is geen native fallback of conceptpreview.

**OWNER_PUBLISHED / UI_LIVE_VERIFIED.** Verse rollen: MAIN 196238639370; voormalig voorraadthema 196227170570 en los zoekconcept 196116087050 zijn UNPUBLISHED. Alle drie live prijsbestanden zijn checksum-exact teruggelezen: JS `11de150d3e2797a6f35742a813281fcb`, kaartdata `b4e58946edc02ba1e44dd876c6239ef5`, vertaalsnippet `2a0136a8420e8a710f448c99d5fc3aad`.

Echte live Chrome ná deze publicatie, zonder preview-iframe: via de werkelijke header `N8271TC` + Enter geeft correcte zoekkop, **één product / één externe Nesso-plafondbuiskaart, “Vanaf € 78,00”, geen foutbanner**. Daarmee zijn SKU-aliaszoeken en de nieuwe prijsweergave samen op MAIN bewezen.

## Overdracht en publicatie

**SEARCH-01 afgerond.** Geen server- of publicatiehandeling meer nodig. De installer niet opnieuw uitvoeren; de geslaagde installatie, publieke index en live “Vanaf”-/kaartweergave zijn gecontroleerd. De bestaande uurlijkse timer is hervat; een volgende toekomstige uitvoering is nog niet waargenomen.

Het gepubliceerde gecombineerde thema bevat de COTTO-kleur-/winkelwagenwijzigingen en de actuele zoek-/prijswijzigingen. Het oude losse zoekconcept mist de COTTO-wijzigingen en mag niet als latere release worden gebruikt. De eigenaar heeft gepubliceerd; deze uitvoering heeft geen thema gepubliceerd.

De eerder gepubliceerde Verlavio-voorraadtekst is behouden in het huidige gecombineerde MAIN 196238639370. De oude FAB-04-publicatiegrens is geschiedenis; de afzonderlijke voorraad-/Market-reparatie blijft behouden. Andere merken, zes leveranciersconflicten, 53 vastgehouden bronmenu's, de merkenoverzichtvraag en het Lagoo-fotoverbod blijven buiten deze zoekwijziging. De aparte COTTO-01-schrijver en prioriteit in de centrale status blijven behouden. SEARCH-01 heeft geen backendworker gestart; na overdracht is geen SEARCH-01-schrijver actief.

Volledige catalogusdata, privé-runtimeverslagen en screenshots horen niet in de publieke repository. Dit dossier bevat uitsluitend aggregaten, publieke code-identiteiten, controlegrenzen en het vervolgpad.
