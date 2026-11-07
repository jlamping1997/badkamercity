# Hotbath brede uitrol: theme-integratie

## Bestanden en contract

- `build_rollout_theme.py` bouwt lokale theme-output; geen netwerk- of Admin-mutaties.
- `test_rollout_theme.py` controleert generatie- en uitsluitingsregels.
- Input: `{groups:[{id,label,menus,products}]}` in de bestaande V2-vorm, de actuele productcatalogus en de oude centrale 433-groepen-dataset.
- Bron: de verse drie main-product/V2-snippet/JS-bestanden onder `source-theme`.
- De input mag een volledige union bevatten. Byte-/inhoudelijk gelijk gebleven bestaande groepen worden niet opnieuw uitgeserveerd. Voor bestaande uitbreidingen blijven alle oude records en keuzevelden behouden.
- Neem de eerdere vier proefgroepen mee in de input. De oude `bc-hotbath-preview-group` wordt niet meer aangeroepen.

## Uitvoering

```bash
python3 build_rollout_theme.py --source-dir source-theme --groups groups-input.json --existing-data ../hotbath-menu-20261024/baseline/product-switcher-data.json --catalog ../hotbath-menu-20261024/catalog_snapshot.json --option-additions-sidecar colour_option_additions.json --output-dir rollout-theme
```

Het script schrijft `rollout-theme-manifest.json` en `routing-index.json` naast de uitvoermap. Het overschrijft alleen zelf gegenereerde paden en verwijdert geen oude theme-assets.

## Routing en grootte

Exacte product-IDs leiden naar een korte numerieke routesleutel. Een tweede lookup levert bestaande groeps-ID en assetnaam. Helpers worden alleen indien nodig in deterministische modulo-buckets verdeeld; iedere individuele helper blijft onder 98.000 bytes. Per pagina wordt één relevante ID-bucket en één bron-bucket gelezen.

Groepen blijven volledig in één JSON-asset. Assets worden compact verpakt tot maximaal 300.000 bytes en maximaal tachtig groepen. Een onverdeeld te grote familie veroorzaakt een expliciete bouwfout; er wordt geen onvolledige groep gepubliceerd.

De bestaande V2-JS en het gedeelde oorspronkelijke JSON worden niet gewijzigd. Het al aanwezige opt-in positieherstel wordt gebruikt via de bestaande `data_url`-parameter. Ongewijzigde oude groepen behouden hun gewone databron.

## SPOM en behoud

SPOM in SKU, titel of handle verwijdert een record uit de nieuwe datagroepen. Op de productpagina staat de SPOM-controle vóór groepsresolutie en onderdrukt deze zowel V2-, legacy- als native keuzemarkup. De productprijs, koopknop en variant blijven bestaan.

Deze ruime controle vindt 697 artikelen. Het verschil met de 696 SPOM-SKU-prefixen is G50, waarvan titel en handle expliciet SPOM3 noemen.

Bestaande metadata blijven voorrang houden; een afwijkende nieuwe groeps-ID wordt tijdens bouwen geweigerd. De root heeft alle 8.237 actuele `custom.group`-waarden apart gelezen: nul ingevuld, bewijs `legacy-groups.json`.

Alleen de zeven expliciet genoemde oude IX-records in de twee Archie AR105EXT/ARHF-groepen mogen `options.kleur: RVS 316` erbij krijgen. Het sidecarbestand koppelt groep, handle en actuele SKU aan de bron. Andere recordvelden, alle oude opties en de oude menudefinities moeten identiek blijven. Een onjuiste, ontbrekende of ongebruikte sidecartoestemming veroorzaakt een bouwfout.

De vijf expliciete titel/SKU-conflicten `SDS32BGP`, `IBS33BGP4`, `IBS20AGN357`, `IBS20BBP` en `IBS20BCP` zijn harde blokkades voor iedere ingevoerde groep; ze kunnen niet ongemerkt via een andere familie terugkomen.

## Bewijs en grenzen

- Twaalf lokale generatie-/veiligheidstests PASS, waaronder behoud oude records, zeven beperkte additieve kleuruitzonderingen, vijf harde HOLD-SKU-blokkades, SPOM midden in SKU/titel/handle, singletons na opschoning, ongeldige combinaties, nieuwe publicatiegate, begrensde assets/helpers en optiesrendering.
- Definitieve integratie inclusief aanvulling: 605 inputgroepen met 7.165 unieke producten; 380 bestaande groepen gebruiken de ongewijzigde oude bron. Output: 225 nieuwe/gewijzigde groepen, waarvan 53 bestaande uitgebreid en 172 nieuw, met 4.252 exact gerouteerde IDs. Tien assets, maximaal 299.177 bytes; grootste helper 73.698 bytes. Veertien bestanden om te uploaden, alleen de bestanden uit het manifest.
- De aanvulling voegt 261 producten toe; alle 6.904 eerdere handles blijven behouden. Alleen de drie expliciet genoemde nieuwe SDS32-groepsIDs zijn vervangen. Exacte backup in `groups-input.pre-supplemental-595.json`, rekencontrole in `supplemental-union-audit.json`.
- Officiële stateless Liquid-validatie: vier files `success:true`, geen errors. Main-product behoudt de drie waarschuwingstypen (complexiteit 227, `seo_media`, `continue`). De twee gegenereerde `case`-datatabellen hebben elk alleen een complexiteitswaarschuwing 227. Een full-themecheck van uitsluitend de diffmap is niet geschikt voor dependencychecks omdat de onveranderde assets/locales daarin ontbreken.
- Herhaalde build levert identiek manifest en routing-index. Alle veertien outputbestanden zijn tegen manifestgrootte en SHA256 gecontroleerd. Bewijs in `architecture-tests.json` en `architecture-liquid-validation.json`.
- Dit zijn lokale generatie- en statische controles. Shopify-readback en echte browseracceptatie doet root. Geen mobiele of performancemeting geclaimd.
