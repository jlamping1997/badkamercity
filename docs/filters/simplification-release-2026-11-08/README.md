# Filtervereenvoudiging v2 — exacte formaatselectie

8 november 2026. FILTER-SIMPLE-02 / CAUSE_CONFIRMED / V2_READY / NOT_DEPLOYED.

De eerste installatie stopte veilig vóór activatie. Eigenaardiagnose: 60 × 60 cm verwacht159, query309:159juiste plus58van60×120 en92van60×150. Alle309IDs uniek,geenontbrekendeIDs,searchcutoff=false. Formaatfacettellingen en bronmaten klopten; de tekstselectie gaf extra rechthoekige formaten.

V2 gebruikt een intern numeriek formaatveld. De getoonde tekst en URLs blijven menselijk. [Gedrag, code en herstelprocedure](https://github.com/jlamping1997/badkamercity/tree/c7d83b88cdb703532b1746aa2db217176b21b273/scripts/filter-sync/simplification). Bestaande kleur-/maat-/enumregels blijven behouden; geen Shopify-productmutatie of themapublicatie nodig. Exacte specificaties blijven onaangetast.

## Actueel PowerShellblok

Dit blok vervangt het eerdere installatie- en diagnoseblok. Het downloadt codecheckpointc7d83b88cdb703532b1746aa2db217176b21b273, controleert de inhoud en voert de bestaande veilige staging-/activatieroute uit. De uitvoeromgeving bereikt serverSSH niet; eigenaar voert het blok via bestaande toegang uit.

```powershell
& {
    $ErrorActionPreference = "Stop"
    $bestand = Join-Path $env:TEMP "badkamercity-filterupdate.py"
    Invoke-WebRequest -Uri "https://raw.githubusercontent.com/jlamping1997/badkamercity/c7d83b88cdb703532b1746aa2db217176b21b273/scripts/filter-sync/simplification/repair_filter_simplification.py" -OutFile $bestand
    if ((Get-FileHash -LiteralPath $bestand -Algorithm SHA256).Hash.ToLowerInvariant() -ne "a0ad2c0bea3d19b0964f7ff86a2904efe9e880449070a36b627a855280c66c2f") { throw "Bestandscontrole mislukt; niets uitgevoerd." }
    Get-Content -Raw -LiteralPath $bestand | ssh ubuntu@57.129.175.195 "sudo -n python3 -"
    if ($LASTEXITCODE -ne 0) { throw "Update niet voltooid. Deel de uitvoer." }
}
```

De installer maakt een nieuwe private back-up en index, leest de index volledig terug en controleert alle132formaatselecties op de volledige ID-set. Daarna volgen combinaties, bestaand variant-/filtergedrag en lokale/publieke livechecks. Hij vereist variant_aliases_v1,filter_simplification_v1,tile_format_codes_v1 vóór/na activatie en bij herhaling. Pas na geslaagde activering wordt de worker voor volgende synchronisaties geschreven. Bestaande synchronisatielock, bronhashguard, eigen-generatieherstel en timerstand blijven behouden. Geen historische cleanup of v1-installatie herhalen.

## Getest en nog open

51testsPASS:23installerlifecycle,19API,9worker. Op3.496tegelrecords3.490maten/132labels, exacte maten behouden. De codes houden159van60×60,58van60×120 en92van60×150gescheiden, inclusiefherhaalpatch/codekaart/OR/AND/onbekende labels enprivateveldweigering. Volledige formaten worden ook tijdens echte serverstaging opnieuw getest; offlinecorrectie is nog geen nieuwe productieclaim.

Baseline vóórv2: healthok=true,227profielen,bc_sync_20261108t150044_583414. Tegels heeft nog f_tegel_breedte_mm/f_tegel_lengte_mm en geenfilter_simplification_v1. Reguliere legacygeneratievernieuwing waargenomen; specifieke timerunit niet rechtstreeks teruggelezen. MAIN196328685834 bevestigd; geen thema-/Shopifywrite.

Nieuwev2Typesense-/FastAPI/ASGI-/activeringstests, echtefrontend/mobiel en toekomstigev2timeruitvoering blijvenPENDING/NOT_TESTED totdat de uitvoering en nacontrole zijn ontvangen. Back-upmap:/opt/badkamercity/filter-sync/filter-simplification-backups/. Deadline900s, aparteherstelgrens240s,voortgangiedere20s. Bij fout alleen uitvoer delen, geen guards overslaan.

Historisch eerste stage:20261108T142600_81ee36. Diagnosecode:cfdd2225fe8863b626b82e4f453c6f60fe32c222; geenproductiedata gewijzigd. Bestaande oude index/API bleven volgensinstallerbehouden en zijn publiek teruggezien.

**Eén volgende handeling:** eigenaar voert bovenstaand v2blok uit en deelt de uitvoer; daarna publieke API en echte filterkeuzes controleren. Geen nieuwe inhoudelijke goedkeuring vragen.
