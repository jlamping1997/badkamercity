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
