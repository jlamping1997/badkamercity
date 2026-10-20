# Zeven Wiesbaden-zoektitels bijwerken — nog niet uitgevoerd

**PREPARED_NOT_EXECUTED,20oktober2026.** Shopify heeft de zeven nieuwe producttitels al; de externe index nog niet. ExacteSKU en actuele korte kaarttitels werken. Van vier gewone tekstproeven slaagt één niet: “Barco ovale waskom” geeft0, terwijl de oude index “Barco waskom ovaal” bevat.

[Standalone script](sync-wiesbaden-proefgroep2-index-titles.py) en [offline veiligheidstests](test-index-title-sync.py) zijn voorbereid.12 tests PASS. Live schema/document/API/patch/restoreproeven van dit nieuwe script zijn NOT_EXECUTED: de read-only SSH-proef vanuit ChatGPT gaf “Network is unreachable”, geen remote opdracht uitgevoerd.

## Scope

Alleen veldtitle op de bestaande index bc_verified_full_20261013_874e415c15, vaste product-ID/SKU’s20.3755,20.3756,32.3411,32.3594,32.2510,32.3670,38.4125. Geen bulkimport, herbouw, schema-, prijs-, voorraad-, collectie-, facet- of Shopifywrite. Definities en andere indexvelden blijven behouden.

Het script leest de bestaande Typesense-sleutel uitsluitend in geheugen via dockerinspect van badkamercity-filter-api-verified-candidate, gebruikt die alleen op loopback en print geen sleutel/omgeving/rawexception. Niet afzonderlijk dockerinspect-output delen. Er zijn geen nieuwe credentials nodig.

Vóór de eerste write: actieve index/service, schema, SKU/GID/collectie-identiteit, oude of gewenste titel en exacte zoekresultaten controleren. Volledige private herstelkopie: /var/backups/badkamercity-wiesbaden-proefgroep2/index-titles-20261020.json, map0700/bestand0600. SHA256 en vast plan worden gecontroleerd. Bij hervatten accepteert de scriptlogica alleen oorspronkelijke of exact gewenste volledige documenten. Andere bewerkingen veroorzaken stop. Writes zijn afzonderlijke PATCHes met alleentitle en volledige readback. Bij fout wordt herstel geprobeerd zonder andermans wijzigingen te overschrijven; bij onbereikbaar/partieel herstel expliciet BLOCKED.

apply voert zelf de voorcontrole, backup en eindcontrole uit. verify test iedereSKU en nieuwe tekstquery bij lokale én publiekeAPI en vergelijkt volledige documenten met de backup. Geen succes rapporteren op alleen offline tests.

## Eén uitvoerblok vanaf de bestaande Windows-pc

Gebruik het bestaande PowerShellvenster met werkende SSH-toegang. Het blok downloadt de beoordeelde vaste scriptversie, controleert de checksum, zet één bestand over en start éénSSH-sessie. Voer het niet gelijktijdig met een andere index-/productbatch uit.

```powershell
& {
    $titelScript = Join-Path $env:TEMP 'bc-wiesbaden-proefgroep2-index-titles.py'
    $titelUrl = 'https://raw.githubusercontent.com/jlamping1997/badkamercity/fix/product-cards-2026-10-14/docs/product-content/wiesbaden/proefgroep2/sync-wiesbaden-proefgroep2-index-titles.py'
    Invoke-WebRequest -UseBasicParsing -Uri $titelUrl -OutFile $titelScript
    $verwachteHash = 'E932A56588240BAB5497EBA87AF6124E0475C2DD127CC41B2FCE2AEFB8FDABD6'
    if ((Get-FileHash -LiteralPath $titelScript -Algorithm SHA256).Hash -ne $verwachteHash) {
        throw 'Bestandscontrole wijkt af; niets uitgevoerd.'
    }
    $titelServer = 'ubuntu@57.129.175.195'
    $titelRemote = '/home/ubuntu/bc-wiesbaden-proefgroep2-index-titles.py'
    scp $titelScript "${titelServer}:$titelRemote"
    if ($LASTEXITCODE -ne 0) { throw 'Overzetten mislukt; gestopt.' }
    ssh -t $titelServer "sudo python3 $titelRemote apply"
    if ($LASTEXITCODE -ne 0) { throw 'Titelcorrectie niet bewezen. Deel alleen de gesaneerde JSON-uitvoer; stop met andere wijzigingen.' }
}
```

Voer wachtwoorden alleen in bij de bestaande SSH-/sudoprompt in eigen terminal. Deel geen wachtwoord in chat. Verwachte eindstatus APPLIED_VERIFIED met28 geslaagde zoekcontroles (7SKU+7tekst ×2API’s). Een afwijkend profiel/index/document laat de scriptuitvoering stoppen; niet de guards versoepelen.

Voor afzonderlijke alleen-lezen controle na SSH-login: `sudo python3 /home/ubuntu/bc-wiesbaden-proefgroep2-index-titles.py verify`. Voor bewust herstel van uitsluitend de zeven oude titels: dezelfde scriptnaam met `restore`. Alleen uitvoeren na beoordeling van de actuele staat; het script weigert een herstelconflict.

## Daarna vastleggen

Registreer de daadwerkelijke gesaneerde JSON-output in het batchbewijs en actuele status. Verifieer opnieuw /search met “Barco ovale waskom” en nieuwe titels. Deze scriptsynchronisatie verandert geen filterwaarden of profielen. Beoordeel daarna het UNPUBLISHED concept195491168522 op mobiel en laat de eigenaar publiceren als akkoord. Publicatie ververst de externe index niet automatisch.

ScriptSHA256: e932a56588240bab5497eba87af6124e0475c2dd127cc41b2fce2aefb8fdabd6.
