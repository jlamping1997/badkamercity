# Acero bij tegels → Grijs

8 november 2026. Status: **APPLIED_VERIFIED / PUBLIC_API_VERIFIED**.

De eigenaar heeft bevestigd dat Acero bij de tegels grijs is. De correctie past alleen de afgeleide filterkleur aan bij een exacte, genormaliseerde bronkleur `Acero` en lidmaatschap van een bekende tegelcollectie. De fabrikantkleur blijft in `f_kleur_exact` en in Shopify behouden. De regel blijft ook gelden bij volgende automatische indexverversingen.

In de eerder uitgelezen 3.496 gepubliceerde tegels zijn er 27 met exacte kleur Acero: 26 Porcelanosa-producten veranderen van Zilver naar Grijs; één Cottoceramix/Malaga-product stond al op Grijs. De drie samengestelde namen Bone acero/Bone-acero vallen buiten deze gerichte correctie.

## Uitvoering

Gebruik uitsluitend `repair_acero_color.py` uit dit dossier, met de SHA256 uit `acero-correction-release.json`. De vorige v2-installer hoeft niet opnieuw te worden uitgevoerd. Deze correctie vereist de exact beoordeelde v2-worker en API; gewijzigde bronbestanden worden niet overschreven.

De bestaande procedure maakt een private back-up, pauzeert de actieve ververstimer, bouwt een volledige verse index, voert de bestaande controles plus een Acero-controle uit en activeert alleen na succes. De permanente worker wordt daarna geïnstalleerd. Bij een fout herstelt de procedure alleen haar eigen wijziging en hervat de eerder actieve timer. Er worden geen Shopify-producten of thema's gewijzigd. De API-bron moet byte voor byte gelijk blijven.

De nieuwe generatie moet `variant_aliases_v1`, `filter_simplification_v1`, `tile_format_codes_v1` en `acero_gray_v1` bevestigen. Succes wordt gemeld als `ACERO GECORRIGEERD` en `applied_verified`; het resultaat bevat `acero_gray_products`.

## Bewijs en grenzen

- 40 lokale tests geslaagd: 10 worker-/catalogustests en 30 installatietests.
- Vergelijking van alle 3.496 tegels: uitsluitend de 26 bedoelde kleurwijzigingen; alle andere productvelden blijven gelijk.
- De 132 formaatcodes en exacte maatvelden blijven gelijk; de API blijft byte voor byte gelijk.
- De standalone installer is als ASCII gecontroleerd en bevat alleen de openbare patch, geen private runtimebron of catalogus.
- Echte serverstaging en activatie zijn geslaagd: 238 GOED en nul FOUT, waaronder alle 132 formaatselecties. De publieke nacontrole bevestigt alle 27 verwachte Acero-producten onder Grijs en geen daarvan onder Zilver.

Private fixtures zijn niet opgenomen. Optionele testpaden: `BC_ACERO_WORKER_SOURCE`, `BC_ACERO_API_SOURCE` en `BC_ACERO_TILE_CATALOG`. Zonder private fixtures worden die integratietests expliciet overgeslagen.

**Eén volgende handeling:** eigenaar test de vereenvoudigde filters op de live productlijsten en noteert gerichte productcorrecties. Het ontbrekende tegelformaatfilter in het Cottoceramix-merkprofiel blijft apart vervolgwerk. De Acero-installer niet opnieuw uitvoeren.

## Bevestigde uitvoering en publieke nacontrole

De eigenaar voerde de installer uit vanaf commit `ea0d0cdb5887f9881e83b23baaca0272458bc897`. Eindstatus `applied_verified`, collectie `bc_sync_20261108t154938_a5477c`, 15.897 producten en 227 profielen. Alle vier vereiste vlaggen zijn true; `acero_gray_products` is 27. Worker SHA256 `3c6dd21f50081f4ad8d770194dc35a97c101a09910dd8892403e51b93f1495eb`; API SHA256 `3a7701134be7ac55b0a83436ceb16ebb19ac0a88aba17c283490f90047f02094` blijft gelijk. Back-up `/opt/badkamercity/filter-sync/filter-simplification-backups/20261108T154937-6ec4e2`; rapport `/opt/badkamercity/filter-sync/runs/20261108T154938_a5477c/RESULTAAT.json`. Timer is volgens de uitvoer hervat.

De assistent heeft daarna de publieke API opnieuw gelezen: precies de 27 verwachte product-ID's vallen bij zoeken op Acero onder Grijs en geen daarvan onder Zilver. Eén samengesteld Acero-zoekresultaat blijft onder Zilver en valt buiten de exacte Acero-correctie. De oorspronkelijke Acero-naam blijft op de productkaarten aanwezig. De formaten 60 × 60 / 60 × 120 / 60 × 150 geven nog 159 / 58 / 92 producten. De actieve generatie bleef stabiel tijdens de nacontrole.

Dit is een nieuwe API-controle, geen nieuwe browser- of mobiele proef. Een volgende automatische verversing of reboot is nog niet onafhankelijk waargenomen. MAIN bleef `196328685834`; geen thema- of Shopify-productwijzigingen door deze correctie. De volledige eigenaaruitvoer blijft privé; bron-SHA256 `c461f36354f3105073fc3493e244de62b7b25d4f8ba85d6e87a5b06ae71de929`.
