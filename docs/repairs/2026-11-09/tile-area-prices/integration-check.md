# Tegelprijzen en uitstraling gebruiken dezelfde live versie

9 november 2026 · THEME-MERGE-CHECK-01 · OWNER_PUBLISHED_VERIFIED / NO_THEME_MERGE_NEEDED

De eigenaar wil de goedgekeurde m²-prijzen behouden en combineren met de tegelindeling uit de andere chat. De aangeleverde PowerShell-uitvoer meldt een geslaagde installatie van het uitstralingfilter. Eerst zijn beide werkstromen en alle bestanden van beide genoemde thema’s opnieuw gelezen.

## Uitkomst

**Gebruik het huidige gepubliceerde thema: BadkamerCity - Tegelprijzen per m2 9 nov, ID196354474250.** Dit is de volledige juiste themabron. Er is geen tweede wijzigingsset in de reserve die nog overgenomen moet worden.

| Onderdeel | Waar opgeslagen | Gecontroleerd resultaat |
| --- | --- | --- |
| Tegelprijzen en calculator | Live thema196354474250 | Alle1.390checksums exact gelijk aan het eerder beoordeelde prijsconcept. |
| Reserve - kopie tegelbasis (geen review),196395073802 | Oude themabasis |1.390files;1.385gelijk aan MAIN, uitsluitend vijf oude prijsfiles afwijkend; nul extra/missende bestanden. |
| Tegelindeling, lookvelden en collectieleden | Gedeelde Shopify-product-/collectiedata | De andere werkstroom beschrijft3.495van3.496 ingedeeld en expliciet geen themawrite. Deze gegevens horen niet bij een losse themakopie. |
| Uitstralingfilter | Gedeelde VPS-worker/API/index | De eigenaaruitvoer meldt applied_verified en tile_looks_v1=true. Het live thema toont en gebruikt het nieuwe filter. |

De vijf verschillen zijn assets/bc-external-filters.js, snippets/bc-card-product-search.liquid, snippets/bc-card-tile-price.liquid, snippets/bc-porcelanosa-buybox.liquid en snippets/price.liquid. MAIN bevat bij alle vijf de goedgekeurde prijsversie; de reserve bevat de oude bron. De reserve is exact gelijk aan de vorige basis in het bestaande prijsdossier.

Ook alle overige themefiles, templates, categoriecode en de settings_data-checksum zijn onderling gelijk. De beschermde settings_data-body is niet gelezen of geschreven. Geen derde thema aangemaakt, geen themabestand geschreven, niets gepubliceerd of verwijderd en geen product-/serverinstelling gewijzigd. De oude reserve blijft bewaard als reserve; publiceer die niet als combinatieversie.

## Nieuwe live controle

Chrome is expliciet uit de eerdere preview gezet. Op de openbare Cottoceramix-collectie zijn3159producten getoond. De nieuwe keuze Uitstraling is geopend; Marmerlook is geselecteerd en geeft90producten plus de actieve filterchip. Op dezelfde pagina tonen de kaarten uitsluitend de m²-prijs, onder andere Statuario €53,03, Marble Brown €89,95 en Seine Hexagon €159,95 per m². Dit bevestigt beide functies samen in de gepubliceerde versie. De live zoekkaart VS4501 toont eveneens alleen €63,95 per m².

[Gecontroleerde live combinatie](https://badkamercity.nl/collections/cottoceramix?bcf_f_tegel_uitstraling=Marmerlook) · [Browserbeeld](browser-live-combined.jpg) · [Volledige hashvergelijking](integration-manifests.json) · [Verificatie en grenzen](integration-verification.json).

De aangeleverde serveruitvoer vermeldt generatie bc_sync_20261109t104047_352ae2,15.897producten,227profielen,3.495lookproducten, één ontbrekende look, worker79f676d035fdd6d250e2daec51b886d1aa54c117707718d7ea9695300c21c43d en de behouden API-hash. Dit is eigenaaraangeleverd uitvoerbewijs; deze controle heeft geen nieuwe SSH-/systemd-read uitgevoerd. De live Cotto-browserproef is onafhankelijk uitgevoerd. Er is geen claim dat alle lookwaarden, volledige IDsets, kleur-/formaatcombinaties of volgende timerverversing opnieuw zijn getest. Fysieke telefoon, checkout, mail en purchase-events zijn niet getest.

## Overdracht

Git-codebron bij start: fix/product-cards-2026-10-14 op de8c472607884d0460b194d7434a209bf130b47b; themacode staat uitsluitend in shopify/current/. Main-documentatiebasis89098e9bd80578a4501400a5edd6c8da51392e63. Alleen documentatie en bewijs toegevoegd in deze controle. Geen verandering van de categorie-/prijscontracten en geen bestaande gegevens of historie vervangen.

**Eén volgende handeling:** vervolgwerk starten vanaf een verse read van MAIN196354474250, zonder de reserve als nieuwere bron te behandelen. Er is voor deze combinatie niets te installeren of te publiceren. De143ontbrekende basiskleuren, het Cotto-merkformaatfilter en twijfelgevalWM2600 blijven ongewijzigd open/uitgesteld volgens hun eerdere besluit. Geen actieve schrijver na overdracht.
