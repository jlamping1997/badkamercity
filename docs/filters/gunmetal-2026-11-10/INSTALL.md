# Serverupdate uitvoeren

10 november 2026. Gunmetal, aanbevolen productmix en indexcontrole van de twee Cinto-breedtes. Nog niet uitgevoerd op de VPS.

Het bronbestand is vastgezet op codecommit `12988ae2c774d2c8c3c659e5eaa76eebe7746a7d`. SHA256: `df5fc8dbc038ffa8bdac6c8f86a0ade7a089889b64e9a7a6e4cd2e71d1538e82`. De download wijzigt niet mee met latere Git-aanpassingen.

Plak het volledige blok in Windows PowerShell. Het gebruikt dezelfde bestaande SSH-verbinding als eerdere filterupdates. Het pakket neemt op de server eerst een private herstelkopie, gebruikt het bestaande slot en test de nieuwe index voordat die wordt geactiveerd. Dezelfde worker blijft daarna bij toekomstige synchronisaties actief.

```powershell
& {
    $ErrorActionPreference = "Stop"
    $bestand = Join-Path $env:TEMP "badkamercity-catalogusfilters.py"

    Invoke-WebRequest -UseBasicParsing -Uri "https://raw.githubusercontent.com/jlamping1997/badkamercity/12988ae2c774d2c8c3c659e5eaa76eebe7746a7d/scripts/filter-sync/simplification/gunmetal/repair_gunmetal_filter.py" -OutFile $bestand

    if ((Get-FileHash -LiteralPath $bestand -Algorithm SHA256).Hash.ToLowerInvariant() -ne "df5fc8dbc038ffa8bdac6c8f86a0ade7a089889b64e9a7a6e4cd2e71d1538e82") {
        throw "Bestandscontrole mislukt; niets uitgevoerd."
    }

    Get-Content -Raw -LiteralPath $bestand | ssh ubuntu@57.129.175.195 "sudo -n python3 -"
    if ($LASTEXITCODE -ne 0) {
        throw "Update niet voltooid. Deel de volledige uitvoer."
    }
}
```

Geen ZIP of handmatig uitpakken nodig. De lokale download gaat naar de tijdelijke map. Herstelkopie en generatiecontrole staan op de server; bestaande gegevens worden niet lokaal vervangen.

De volledige uitvoer terugsturen. Alleen `applied_verified` met `gunmetal_v1`, `recommendations_v1` en `cinto_widths_v1` true is een succesvolle installatie. Bij `scheduler_pending`, een bronverschil of fout stoppen en de uitvoer delen; geen oudere installer als omweg uitvoeren.

Daarna controleren we publiek: Gunmetal los van Grijs, 3cm-spiegelrange zonder deze twee artikelen, 60/80cm op de juiste plaats, aanbevolen pagina1/2 zonder dubbelingen en de prijsvolgorde. De theme-preview blijft afzonderlijk in **BadkamerCity - Categorieverbeteringen 10 nov**; dit commando publiceert geen thema.

[Scope, tests en herstel](README.md).
