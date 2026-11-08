# Vereenvoudigde filters — installatie gereed

8 november 2026. FILTER-SIMPLE-02 / RELEASE_READY / NOT_DEPLOYED.

De eigenaar wil zelfstandig handelen op redelijke naamzekerheid en test daarna zelf. Geen nieuwe toestemming voor kleurvoorstellen vragen. De release wijzigt de afgeleide filters, inclusief maat- en enumgroepering, met exact gebleven Shopify-productinformatie. [Eén inhoudelijke code-/herstelbeschrijving](https://github.com/jlamping1997/badkamercity/tree/135ada92366349cbc29ea080894a8e0f5e434fad/scripts/filter-sync/simplification/README.md).

Codecheckpoint: 135ada92366349cbc29ea080894a8e0f5e434fad. MAIN196328685834 ongewijzigd; geen thema-aanpassing/publicatie nodig. Runtimebron geverifieerd tegen bekende hashes; actuele serverhash wordt vóór installatie gecontroleerd. De uitvoeromgeving bereikt SSH niet. Deze installatie is daarom nog niet uitgevoerd.

## PowerShell

Dit volledige blok downloadt exact het vastgezette script, controleert de inhoud en voert het via de bestaande SSH-toegang uit. De installer maakt de serverback-up; geen lokale catalogusbestanden worden verplaatst. Laat de uitvoering afronden; voortgang verschijnt iedere 20 seconden.

```powershell
& {
    $ErrorActionPreference = "Stop"
    $bestand = Join-Path $env:TEMP "badkamercity-filterupdate.py"
    Invoke-WebRequest -Uri "https://raw.githubusercontent.com/jlamping1997/badkamercity/135ada92366349cbc29ea080894a8e0f5e434fad/scripts/filter-sync/simplification/repair_filter_simplification.py" -OutFile $bestand
    if ((Get-FileHash -LiteralPath $bestand -Algorithm SHA256).Hash.ToLowerInvariant() -ne "7ac33496f818e0c2ee70fb47ce54ba5d63a32e5d583274281d863703cc5dc727") { throw "Bestandscontrole mislukt; niets uitgevoerd." }
    Get-Content -Raw -LiteralPath $bestand | ssh ubuntu@57.129.175.195 "sudo -n python3 -"
    if ($LASTEXITCODE -ne 0) { throw "Update niet voltooid. Deel de uitvoer." }
}
```

Succes wordt uitsluitend als applied_verified gemeld na staging, volledige indexreadback, lokale/publieke tests en worker-teruglezing. Geef bij een stop de uitvoer door; geen hashes overslaan of oude installer herhalen. Bij bronverschil blijft de huidige service behouden en moet de actuele wijziging eerst worden bekeken. Bestaand veilig eigen-generatieherstel en timerstand blijven behouden. Back-ups onder /opt/badkamercity/filter-sync/filter-simplification-backups/.

## Aangetoonde voorbereiding

41 release-/worker-/API-tests PASS; zes kleurtests, 46 JS-asserties en acht maat-/enumtests PASS. 786/1.002 namen ingedeeld; 216 onduidelijke namen naar Overige kleuren. De 3.496 tegelrecords: 3.490 maatparen, 132 labels, zes zonder maatpaar; 2.412 herkenbare basiskleur,523Overige,561zonderbron,117meervoudig. Geen vrije titelinferentie voor ontbrekende bronkleur.

Dit zijn offline bron-/fixturetests. Nieuwe Typesense-import, FastAPI/ASGI, livebrowser/mobiel, serverreboot en een toekomstige uurlijkse sync blijven NOT_TESTED totdat de serveruitvoer en publieke nacontrole binnen zijn. Baseline vóór deze release: healthok=true,227profielen,bc_sync_20261108t130100_bc1233. Geen nieuwe productieclaim op basis van Git-opslag.

**Eén volgende handeling:** eigenaar voert bovenstaand blok uit en deelt de uitvoer, daarna publieke API en storefrontfilterkeuzes testen.
