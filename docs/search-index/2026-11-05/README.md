# Zoekindex — ontbrekende Verlavio-resultaten

5 november 2026. **PREVIEW_VERIFIED / SYNC_FAILURE_CONFIRMED / ERROR_DETAILS_PENDING**.

De eigenaar vraagt de volledige zoekindex te herstellen. De externe zoekroute mist Verlavio en vervangt daarbij bestaande Shopify-resultaten door nul. De begrensde frontendbescherming is in een echt conceptthema gecontroleerd. Het alleen-lezen runtime-rapport is ontvangen: de automatische timer staat aan, maar de synchronisatieservice heeft gefaald. Voor het volledige backendherstel ontbreekt nog de precieze foutmelding. De frontendbescherming maakt ontbrekende indexdocumenten niet aan.

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

Het ontvangen runtime-rapport bevestigt dat automatische synchronisatie is ingericht: de timer is actief en ingeschakeld, maar de service staat op failed. De oorzaak is nog niet vastgesteld. De publieke health-route blijft de collectie van 3 november melden; het rapport bewijst geen succesvolle nieuwe indexopbouw of werkende vijfminutenverversing. Oudere oktoberbeschrijvingen zijn geen actuele bron voor de publieke index.

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

## Runtime-rapport ontvangen; precieze fout nog nodig

De eigenaar heeft het alleen-lezen runtime-rapport aangeleverd. Het bevestigt:

| Onderdeel | Vastgesteld |
| --- | --- |
| `bc-filter-sync.timer` | `enabled` en `active` |
| `bc-filter-sync.service` | `failed` |
| Werkelijke worker | `/opt/badkamercity/filter-sync/sync.py`, 98.867 bytes |
| Worker-SHA256 | `2064b549e173d709fe1d5e8e5fe8cb549276e817d46b111510fcc4bc12471cf2` |

De automatische taak ontbreekt dus niet; de uitvoering heeft gefaald. Het metadata-rapport bevat niet de exacte foutoorzaak. Aan- of afwezige variabelen in het diagnoseproces bewijzen niet hoe de worker zijn authenticatie laadt. Er is geen ontbrekende authenticatie als oorzaak vastgesteld.

De eerdere vastgepinde runtime-diagnose is hiermee afgerond; het verslag blijft privé en wordt niet in deze publieke repository opgenomen. Er is geen index of actieve collectie gewijzigd en de worker is niet opnieuw gestart. De volgende stap leest uitsluitend het bestaande foutbestand; geen workerstatusopdracht of herstart uitvoeren.

## Overdracht en publicatie

**Exact één volgende handeling voor het volledige indexherstel:** eigenaar leest de precieze fout en plakt de uitvoer terug in de chat:

```powershell
ssh ubuntu@57.129.175.195 "sudo -n cat /opt/badkamercity/filter-sync/LAST_ERROR.json"
```

Deel geen wachtwoorden of sleutels. Pas na deze foutmelding de oorzaak gericht herstellen; geen worker herstarten, index opnieuw opbouwen of actieve collectie omzetten voordat die oorzaak bekend is.

De eigenaar kan **BadkamerCity - Zoekresultaten herstel (196116087050)** afzonderlijk publiceren. De preview is gecontroleerd; dit voorkomt dat aanwezige native resultaten door een externe nul worden verborgen. Het voltooit het volledige indexherstel niet. Na publicatie moeten MAIN-rol, één Verlavio-nulresultaatgeval, een externe Hotbath-zoekopdracht en een echt gefilterd nulresultaat gericht worden teruggelezen.

**Samenloop met COTTO-01:** het afzonderlijke Re-Bel-concept 196238639370 is op de huidige MAIN gebaseerd, waarin deze zoekwijziging nog ontbreekt. De huidige inhoud van dat andere concept is door SEARCH-01 niet opnieuw gecontroleerd. Vóór publicatie van dat concept moet de COTTO-schrijver deze ene zoekwijziging meenemen en gericht controleren; anders verdwijnt de zoekbescherming bij een latere themapublicatie. Dit zoekconcept bevat omgekeerd niet de nog ongepubliceerde vier winkelwagenwijzigingen. Geen van beide concepten is door SEARCH-01 over het andere heen geschreven.

De Verlavio-voorraadtekst is door de eigenaar gepubliceerd: MAIN is nu 196227170570. De oude FAB-04-publicatiegrens is geschiedenis; de afzonderlijke voorraad-/Market-reparatie blijft behouden. Andere merken, zes leveranciersconflicten, 53 vastgehouden bronmenu's, de merkenoverzichtvraag en het Lagoo-fotoverbod blijven buiten deze zoekwijziging. De aparte COTTO-01-schrijver en prioriteit in de centrale status blijven behouden. SEARCH-01 heeft geen backendworker gestart; na overdracht is geen SEARCH-01-schrijver actief.

Volledige catalogusdata, privé-runtimeverslagen en screenshots horen niet in de publieke repository. Dit dossier bevat uitsluitend aggregaten, publieke code-identiteiten, controlegrenzen en het vervolgpad.
