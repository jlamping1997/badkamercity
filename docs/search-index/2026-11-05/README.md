> **Publicatie-afstemming COTTO-01:** de oorspronkelijke zoekbescherming (historisch controlepunt MD5 `e0783b4ed15e1acc70ff1518cf2b5f20`, vóór de prijsuitbreiding met concept-JS `11de150d3e2797a6f35742a813281fcb`) is meegenomen in **UNPUBLISHED196238639370 — BadkamerCity - Re-Bel tegelkeuze**, samen met de vier COTTO-winkelwagenbestanden. Eigen 23 runtimechecks en gecombineerde 5/5 validatie PASS. Publiceer alleen dit gecombineerde concept. Het losse zoekconcept 196116087050 mist de winkelwagenwijzigingen en mag daarna niet als latere release worden gebruikt. De nieuwe Re-Bel-artikelen geven bij de browserproef nog nul zoekresultaten; hun vindbaarheid blijft onderdeel van het open indexonderzoek.

# Zoekindex — ontbrekende Verlavio-resultaten

5 november 2026. **PATCH_VERIFIED_LOCAL / SERVER_EXECUTION_PENDING / COMBINED_PREVIEW_VERIFIED**.

De eigenaar vraagt de volledige zoekindex te herstellen. De externe zoekroute mist Verlavio en vervangt daarbij bestaande Shopify-resultaten door nul. De begrensde frontendbescherming is in een echt conceptthema gecontroleerd. Het runtime-rapport, LAST_ERROR en de actuele worker-/API-bron zijn ontvangen en gecontroleerd. De variantcorrectie is lokaal voorbereid en getest. De serverinstallatie is nog niet uitgevoerd; de gecombineerde themapreview wordt afzonderlijk afgerond. De frontendbescherming maakt ontbrekende indexdocumenten niet aan.

## Verse productiecontrole

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

De timer is actief en ingeschakeld, maar de service is gefaald. LAST_ERROR bevestigt inmiddels de één-variantaanname als blokkade in de normalisatie. De publieke health-route blijft de collectie van 3 november melden; er is geen succesvolle nieuwe indexopbouw of werkende vijfminutenverversing bewezen. Oudere oktoberbeschrijvingen zijn geen actuele bron voor de publieke index.

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

## Complete variantcorrectie voorbereid

- **Worker:** één zoekdocument per product; alle variant-SKU's als genormaliseerde `sku_aliases`. De minimumvariantprijs wordt deterministisch gekozen; `price_varies` markeert verschillende prijzen. Geen product overslaan of Shopify-varianten aanpassen.
- **API:** normale en exacte SKU-zoekopdrachten gebruiken alle aliassen zodra de nieuwe snapshot actief is. Het bestaande snapshot-/schemacontract blijft werken vóór activatie; geen gedeeltelijke omschakeling.
- **Prijsweergave:** prijsverschillen krijgen “Vanaf” bij de minimumprijs, via de externe productkaart en de gedeelde kaartdata. Een SKU-match op een duurdere variant mag niet stil als die specifieke variantprijs worden gepresenteerd.

Geconsolideerde controle PASS: 49 Python-tests (18 worker, 11 API, 16 installer en vier release-/ASCII-controles) plus 39 frontendcontroles, samen 88. De standalone installer is ASCII en 34.166 bytes; SHA256 `7c924875d0d3378e5c21f46a481346e1f750ef16efb249d9bea19a874f5a7aec`. Deze controles bewijzen de lokale implementatie, geen geslaagde serveruitvoering.

De drie bedoelde themabestanden zijn uitsluitend naar het gecombineerde UNPUBLISHED-concept 196238639370 geschreven, met behoud van de COTTO-wijzigingen en bestaande zoekfallback. Alle drie readbacks zijn exact; MAIN is niet geschreven. Echte browserregressie: Hotbath 7.540 resultaten/24 externe kaarten en Verlavio 36 native kaarten/nul externe kaarten zonder foutbanner. Aanvullend PASS: de echte gecombineerde previewroute `bc-card-data` voor Lagoo Nesso levert `price_cents=7800` en `price_varies=true`, zonder `image_url`; het Lagoo-fotoverbod blijft behouden. Echte Chrome-SKU-proef `VSB_2001`: één native Malmö-kaart met productfoto, nul externe kaarten en geen foutbanner.

| Bestand in `shopify/current/` | Teruggelezen concept-MD5 |
| --- | --- |
| `assets/bc-external-filters.js` | `11de150d3e2797a6f35742a813281fcb` |
| `sections/bc-card-data.liquid` | `b4e58946edc02ba1e44dd876c6239ef5` |
| `snippets/bc-external-filters.liquid` | `2a0136a8420e8a710f448c99d5fc3aad` |

## Serverinstallatie nog uit te voeren

De voorbereide installer controleert eerst de exacte productiebron. Hij maakt root-back-ups met mapmodus 0700 en bouwt via de bestaande stagingroute een volledige nieuwe index. Productdekking, prijzen en alle SKU-aliassen worden teruggelezen voordat de nieuwe snapshot atomair wordt geactiveerd. Bij een mislukking is herstel van de eerdere actieve toestand voorzien.

De uitvoerfase heeft een deadline van 15 minuten en geeft elke 20 seconden voortgang. De nieuwe worker voor de bestaande uurlijkse taak wordt pas na geslaagde indexactivatie geïnstalleerd. De oorspronkelijke aan-/uitstand van de timer blijft behouden. De installer wijzigt geen Shopify-productdata, prijzen, voorraad, varianten of afbeeldingen.

De API-patch gebruikt een canonieke AST-controle zodat formatteringsverschillen tussen Python-versies de versiecontrole niet vervalsen.

Deze stappen zijn uitsluitend lokaal getest: er is nog geen productiebron, index of actieve collectie veranderd, geen worker gestart en geen volledige nieuwe publieke index bewezen.

## Overdracht en publicatie

**Exact één volgende handeling voor het volledige indexherstel:** eigenaar voert de vastgepinde installer vanaf de eigen pc uit en plakt de voortgang/einduitkomst terug in de chat:

```powershell
$reparatie = Join-Path $env:TEMP "badkamercity-zoekindex-herstel.py"
Invoke-WebRequest -Uri "https://raw.githubusercontent.com/jlamping1997/badkamercity/05a54c8d8b7df8c41644eec7abd5bd812a3cb6d5/scripts/filter-sync/repair_variant_index.py" -OutFile $reparatie
Get-Content -Raw -LiteralPath $reparatie | ssh ubuntu@57.129.175.195 "sudo -n python3 -u -"
```

Vastgepind codecheckpoint: `05a54c8d8b7df8c41644eec7abd5bd812a3cb6d5`. De gecombineerde browserregressie voor Hotbath en Verlavio is gecontroleerd; de serveruitvoering blijft open. Deel geen wachtwoorden of sleutels. Na uitvoering eerst het eindverslag en de publieke index/SKU-/prijscontroles beoordelen; geen tweede blinde herstart.

MAIN blijft 196227170570. Alleen het gecombineerde **BadkamerCity - Re-Bel tegelkeuze (196238639370)** bevat de COTTO-winkelwagenwijzigingen plus de zoekbescherming. De drie nieuwe prijsbestanden zijn daar exact teruggelezen; gecombineerde Hotbath-/Verlavio-browserregressie PASS. Publiceer uitsluitend dit gecombineerde concept volgens de actuele COTTO-afstemming. Het losse zoekconcept196116087050 mist de COTTO-wijzigingen en mag daarna niet als latere release worden gebruikt.

De Verlavio-voorraadtekst is door de eigenaar gepubliceerd: MAIN is nu 196227170570. De oude FAB-04-publicatiegrens is geschiedenis; de afzonderlijke voorraad-/Market-reparatie blijft behouden. Andere merken, zes leveranciersconflicten, 53 vastgehouden bronmenu's, de merkenoverzichtvraag en het Lagoo-fotoverbod blijven buiten deze zoekwijziging. De aparte COTTO-01-schrijver en prioriteit in de centrale status blijven behouden. SEARCH-01 heeft geen backendworker gestart; na overdracht is geen SEARCH-01-schrijver actief.

Volledige catalogusdata, privé-runtimeverslagen en screenshots horen niet in de publieke repository. Dit dossier bevat uitsluitend aggregaten, publieke code-identiteiten, controlegrenzen en het vervolgpad.
