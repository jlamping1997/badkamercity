> **Publicatie-afstemming COTTO-01:** de bewezen zoekbescherming (MD5 `e0783b4ed15e1acc70ff1518cf2b5f20`) is inmiddels byte-exact meegenomen in **UNPUBLISHED196238639370 — BadkamerCity - Re-Bel tegelkeuze**, samen met de vier COTTO-winkelwagenbestanden. Eigen 23 runtimechecks en gecombineerde 5/5 validatie PASS. Publiceer alleen dit gecombineerde concept. Het losse zoekconcept196116087050 mist de winkelwagenwijzigingen en mag daarna niet als latere release worden gebruikt. De nieuwe Re-Bel-artikelen geven bij de browserproef nog nul zoekresultaten; hun vindbaarheid blijft onderdeel van het open indexonderzoek.

# Zoekindex — ontbrekende Verlavio-resultaten

5 november 2026. **ROOT_CAUSE_CONFIRMED / CURRENT_SOURCE_REQUIRED**.

De eigenaar vraagt de volledige zoekindex te herstellen. De externe zoekroute mist Verlavio en vervangt daarbij bestaande Shopify-resultaten door nul. De begrensde frontendbescherming is in een echt conceptthema gecontroleerd. Het runtime-rapport en LAST_ERROR zijn ontvangen. De synchronisatie stopt tijdens normalisatie op een echt product met zestien varianten; voor een complete correctie zijn nu de actuele worker- en API-bron nodig. De frontendbescherming maakt ontbrekende indexdocumenten niet aan.

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

## Begrensde frontendbescherming

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

## Oorzaak bevestigd; actuele bron nodig

Het runtime-rapport bevestigt een actieve, ingeschakelde `bc-filter-sync.timer` en een gefaalde `bc-filter-sync.service`. LAST_ERROR van **5 november 2026, 17:01:22 UTC** meldt in de normalisatiestap:

> Meer of minder dan één variant voor gid://shopify/Product/10698301571338; eerst variantlogica beoordelen

Een verse Shopify-controle bevestigt dat dit **Lagoo Nesso plafondbuis** is, met **zestien echte varianten** en variantprijzen van **€78 tot €215**. De varianten zijn geldige productdata. De synchronisatie moet meerdere varianten kunnen verwerken; dit product overslaan of Shopify-varianten aanpassen is geen volledige oplossing.

Voor de correctie zijn de actuele worker `/opt/badkamercity/filter-sync/sync.py` (98.867 bytes; SHA256 `2064b549e173d709fe1d5e8e5fe8cb549276e817d46b111510fcc4bc12471cf2`) en de API-app `/home/ubuntu/bc_apiproef_20261013/app.py` nodig. Een oudere workersnapshot is geen bewezen exacte vervanging voor deze productiebron.

Het contract blijft één zoekdocument per product, met vindbaarheid op alle variant-SKU's via een SKU-aliasveld en passende exacte SKU-zoeklogica in de API. Het prijsbeleid moet aansluiten op de getoonde product-/variantprijs. Worker, API en prijsweergave daarom samen beoordelen met de actuele bron; nog geen blinde correctie of herstart.

De runtime- en foutdiagnose zijn afgerond. Hun privéverslagen worden niet in deze publieke repository opgenomen. Er is geen index, actieve collectie, serverbron of Shopify-variant gewijzigd en de worker is niet opnieuw gestart.

## Overdracht en publicatie

**Exact één volgende handeling voor het volledige indexherstel:** eigenaar kopieert de twee actuele bronbestanden via SCP naar Downloads, maakt daar een ZIP en uploadt die in de chat:

```powershell
$bronmap = Join-Path $env:USERPROFILE ("Downloads\BC-zoekindex-bron-" + (Get-Date -Format "yyyyMMdd-HHmmss"))
New-Item -ItemType Directory -Path $bronmap | Out-Null
scp "ubuntu@57.129.175.195:/opt/badkamercity/filter-sync/sync.py" "ubuntu@57.129.175.195:/home/ubuntu/bc_apiproef_20261013/app.py" $bronmap
if ($LASTEXITCODE -ne 0) { throw "Kopiëren mislukt. Plak de foutmelding hier." }
Compress-Archive -Path (Join-Path $bronmap "*.py") -DestinationPath "$bronmap.zip"
Write-Host "Upload hier: $bronmap.zip"
```

Deze opdracht leest de twee serverbestanden en schrijft uitsluitend op de eigen pc. Geen workerherstart of serverwijziging. De correctie volgt pas na beoordeling van deze actuele bron.

**Verse themarollen:** MAIN blijft **196227170570 — BadkamerCity - Verlavio voorraad en levertijd**. Het losse zoekconcept196116087050 en het gecombineerde COTTO-concept196238639370 zijn beide UNPUBLISHED. De zoekbescherming is byte-exact opgenomen in het gecombineerde **BadkamerCity - Re-Bel tegelkeuze**, samen met vier winkelwagencorrecties; publiceer alleen dat gecombineerde concept volgens de COTTO-afstemming hierboven. Het losse zoekconcept mist die winkelwagencorrecties en mag daarna niet als latere release worden gebruikt. Publicatie herstelt de backendindex niet; na publicatie MAIN en de gerichte zoek-/winkelwagencases controleren.

De Verlavio-voorraadtekst is door de eigenaar gepubliceerd: MAIN is nu 196227170570. De oude FAB-04-publicatiegrens is geschiedenis; de afzonderlijke voorraad-/Market-reparatie blijft behouden. Andere merken, zes leveranciersconflicten, 53 vastgehouden bronmenu's, de merkenoverzichtvraag en het Lagoo-fotoverbod blijven buiten deze zoekwijziging. De aparte COTTO-01-schrijver en prioriteit in de centrale status blijven behouden. SEARCH-01 heeft geen backendworker gestart; na overdracht is geen SEARCH-01-schrijver actief.

Volledige catalogusdata, privé-runtimeverslagen en screenshots horen niet in de publieke repository. Dit dossier bevat uitsluitend aggregaten, publieke code-identiteiten, controlegrenzen en het vervolgpad.
