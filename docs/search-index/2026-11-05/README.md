# Zoekindex — ontbrekende Verlavio-resultaten

5 november 2026. **PREVIEW_VERIFIED / BACKEND_BLOCKED_SSH / OWNER_PUBLICATION_PENDING**.

De eigenaar vraagt de volledige zoekindex te herstellen. De externe zoekroute mist Verlavio en vervangt daarbij bestaande Shopify-resultaten door nul. De begrensde frontendbescherming is in een echt conceptthema gecontroleerd. Het volledige backendindexherstel blijft open en vraagt eerst een alleen-lezen VPS-diagnose. De frontendbescherming maakt ontbrekende indexdocumenten niet aan.

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

De live service en collectie tonen dat oudere oktoberbeschrijvingen niet als bewijs voor de huidige synchronisatiestatus kunnen dienen. Welke taak de collectie opbouwt, hoe incrementele updates lopen en of een automatische taak faalt, zijn nog niet op de VPS vastgesteld. Geen conclusie dat automatische synchronisatie ontbreekt, en geen claim van een werkende vijfminutenkoppeling.

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

## Volledige backendindex nog geblokkeerd

In deze uitvoeromgeving is geen bruikbare SSH-authenticatie voor de VPS beschikbaar. Er is niet ingelogd en geen backendindex, actieve collectie, scheduler of zoekservice gewijzigd. De eerstvolgende stap is een alleen-lezen runtime-diagnose via de bestaande SSH-toegang van de eigenaar.

Het vastgepinde [diagnosescript `scripts/filter-sync/diagnose_runtime.py`](https://raw.githubusercontent.com/jlamping1997/badkamercity/a8b056a20c5a7e57089832b6774fc21440d43b8e/scripts/filter-sync/diagnose_runtime.py) verzamelt runtime-metadata zonder authwaarden af te drukken en zonder serverwrites. Codecheckpoint: `a8b056a20c5a7e57089832b6774fc21440d43b8e`. **Acht beveiligingstests PASS.** De eigenaar krijgt de PowerShell-/SSH-instructie die precies deze vastgepinde versie uitvoert; niet een veranderlijke branchtip.

Voer deze drie regels uit in PowerShell:

```powershell
$controle = Join-Path $env:TEMP "badkamercity-zoekindex-controle.py"
Invoke-WebRequest -Uri "https://raw.githubusercontent.com/jlamping1997/badkamercity/a8b056a20c5a7e57089832b6774fc21440d43b8e/scripts/filter-sync/diagnose_runtime.py" -OutFile $controle
Get-Content -Raw -LiteralPath $controle | ssh ubuntu@57.129.175.195 "sudo -n python3 -"
```

Plak daarna de uitvoer terug in de chat. Deel geen wachtwoorden of sleutels.

De diagnose moet de werkelijk draaiende service, configuratiepaden, actieve indexcollectie, profielen en bestaande synchronisatie-/opbouwtaken vaststellen. Het verslag moet geschoond blijven van secrets. Een oude werkinstructie of een nieuwe lege collectie is geen vervanging voor die diagnose.

Na ontvangst kan de volledige productdekking tegen Shopify worden vergeleken en de bestaande opbouw-/incrementele synchronisatieroute gericht worden hersteld. Schema, werkelijke synchronisatietaak, eventuele herindexering, wisseling van actieve collectie en rollback moeten op de gevonden runtime worden gebaseerd. **Deze backendstappen zijn nog niet uitgevoerd.** Er is geen blind reparatiescript of automatische collectieomzetting toegevoegd.

## Overdracht en publicatie

**Exact één volgende handeling voor het volledige indexherstel:** eigenaar voert de alleen-lezen VPS-diagnose vanuit de vastgepinde Git-commit uit en levert het geschoonde verslag aan. Nog geen index opnieuw opbouwen of actieve collectie omzetten.

De eigenaar kan **BadkamerCity - Zoekresultaten herstel (196116087050)** afzonderlijk publiceren. De preview is gecontroleerd; dit voorkomt dat aanwezige native resultaten door een externe nul worden verborgen. Het voltooit het volledige indexherstel niet. Na publicatie moeten MAIN-rol, één Verlavio-nulresultaatgeval, een externe Hotbath-zoekopdracht en een echt gefilterd nulresultaat gericht worden teruggelezen.

**Samenloop met COTTO-01:** het afzonderlijke Re-Bel-concept 196238639370 is op de huidige MAIN gebaseerd, waarin deze zoekwijziging nog ontbreekt. De huidige inhoud van dat andere concept is door SEARCH-01 niet opnieuw gecontroleerd. Vóór publicatie van dat concept moet de COTTO-schrijver deze ene zoekwijziging meenemen en gericht controleren; anders verdwijnt de zoekbescherming bij een latere themapublicatie. Dit zoekconcept bevat omgekeerd niet de nog ongepubliceerde vier winkelwagenwijzigingen. Geen van beide concepten is door SEARCH-01 over het andere heen geschreven.

De Verlavio-voorraadtekst is door de eigenaar gepubliceerd: MAIN is nu 196227170570. De oude FAB-04-publicatiegrens is geschiedenis; de afzonderlijke voorraad-/Market-reparatie blijft behouden. Andere merken, zes leveranciersconflicten, 53 vastgehouden bronmenu's, de merkenoverzichtvraag en het Lagoo-fotoverbod blijven buiten deze zoekwijziging. De aparte COTTO-01-schrijver en prioriteit in de centrale status blijven behouden. Na overdracht is geen SEARCH-01-schrijver of backendworker actief.

Volledige catalogusdata, privé-runtimeverslagen en screenshots horen niet in de publieke repository. Dit dossier bevat uitsluitend aggregaten, publieke code-identiteiten, controlegrenzen en het vervolgpad.
