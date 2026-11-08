# Acero bij tegels → Grijs

8 november 2026. Status: **READY_FOR_OWNER_EXECUTION; niet live bevestigd**.

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
- Echte serverstaging, nieuwe activatie en publieke nacontrole van deze Acero-correctie zijn **nog niet uitgevoerd**. De vorige filterrelease blijft de laatst bewezen liveversie.

Private fixtures zijn niet opgenomen. Optionele testpaden: `BC_ACERO_WORKER_SOURCE`, `BC_ACERO_API_SOURCE` en `BC_ACERO_TILE_CATALOG`. Zonder private fixtures worden die integratietests expliciet overgeslagen.

**Eén volgende handeling:** eigenaar voert het vastgepinde PowerShell-installatieblok uit en deelt de volledige uitvoer voor de publieke nacontrole. Het ontbrekende tegelformaatfilter in het Cottoceramix-merkprofiel blijft apart vervolgwerk.
