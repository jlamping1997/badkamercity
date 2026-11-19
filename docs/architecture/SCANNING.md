# Wat kan automatisch gescand worden?

## Nu beschikbaar: een kleine alleen-lezen inventarisatiescanner

Tool: [scripts/architecture_scan.py op de actieve branch](https://github.com/jlamping1997/badkamercity/blob/fix/product-cards-2026-10-14/scripts/architecture_scan.py).

De tool gebruikt alleen Python-standaardbibliotheken, voert geen theme-JavaScript uit en verstuurt geen netwerkverzoeken. Hij leest de acht theme-mappen en schrijft uitsluitend naar de expliciet opgegeven rapportmap. Bestaande thema-/Admin-/serverbestanden worden niet gewijzigd. Uitvoer binnen een theme-map wordt geweigerd.

Vanaf de actieve branch, met Python 3:

```bash
python3 scripts/architecture_scan.py \
  --theme-root . \
  --manifest docs/architecture/evidence/2026-10-28/shopify-main-manifest.json \
  --source-label git-4a85d063-root-theme \
  --coverage repository_root \
  --output-dir /tmp/badkamercity-architecture-root
```

Voor een nieuwe gecontroleerde live snapshot: gebruik de daadwerkelijke snapshotmap, een vers compleet manifest, een exacte bronlabel en `--coverage full_snapshot`. `--require-parity` laat het commando met exitcode 2 stoppen als de snapshot niet exact overeenkomt. Op Windows gebruik je een passende eigen rapportmap en zo nodig `python` in plaats van `python3`; de scanner is niet afhankelijk van `/tmp`.

Een nieuwe scan mag een oud bewijsrapport niet stil overschrijven. Gebruik een nieuwe gedateerde map. `--coverage` is een expliciete invoer door de uitvoerder, geen automatisch bewijs van volledigheid.

## Uitvoer en huidige reikwijdte

| Scan | Automatisch resultaat | Beperking |
| --- | --- | --- |
| Bestandsinventaris | Pad, grootte, regels, MD5/SHA256 en typekandidaat | Geen uitleg van werkelijk gebruik |
| Pariteit | Gelijk, anders, alleen live, alleen scan | Alleen tegenover het meegegeven manifest; geen verse Shopify-query |
| Letterlijke Liquid-verwijzingen | render/include, section/sections/layout, asset_url, inline_asset_content met regelnummers | Dynamische namen en conditionele bereikbaarheid niet volledig bepaald |
| JSON-template/sectiongroepen | Section type → sectiebestand | Admin-toewijzingen en apps niet opgehaald |
| Onderhoudssignalen | Inline style/script, !important, mediaqueries, reduced-motionvermelding, fetch/events/observers/storage | Tellingen zijn geen bewezen defect, runtimeactivatie of performance-score |
| Data-/stijl-ingangen | Letterlijke metafieldkeys, CSS-custom-propertynamen, data-attributen | Geen veldwaarden, computed styles of volledige datastroom |
| Byte-identieke bestanden | Kandidatengroepen | Geen automatische verwijderactie of semantische duplicatieanalyse |
| JSON/encoding | Parseproblemen en niet-UTF8-tekstbestanden | Geen vervanging voor Shopify Theme Check |

`inventory.json` bevat de machinekaart; `README.md` de zoekingang. Er worden geen ruwe codefragmenten, volledige URL-querystrings, credentialwaarden, productdatavelden of klantgegevens naar het rapport gekopieerd. Een bronrepository kan alsnog gevoelige bestandsnamen bevatten: controleer de rapporten vóór publieke commit.

Bij een partiële steekproef betekent `live_only` vooral **niet in deze steekproef aanwezig**, niet dat productie afhankelijkheden mist. `in_live_manifest_only` betekent metadata-aanwezigheid zonder inhoudelijke inspectie. `not_resolved` vraagt vervolgonderzoek; dit is geen bevel om een bestand te verwijderen.

## Vervolgmeting DOC-01

De scanner is nu uitgevoerd op alle 1.262 ontvangen live bestanden: 955 refs, 0 parsefouten, 1.261 gelijke hashes. `--require-parity` stopt met exitcode 2 op config/settings_data.json; er is geen volledige bytevrijgave. Zie [DOC01_SOURCE_MAP.md](DOC01_SOURCE_MAP.md). De oude root-/steekproefuitvoer blijft historisch. De [productbuilder](PRODUCT_DATA.md) maakt privé JSONL/SQLite vanuit opgeslagen read-only responses en is geen downloader.

## Aanvullende scans in het plan

| Hulpmiddel / methode | Toepassing | Voorwaarde |
| --- | --- | --- |
| Bestaande Theme Check-wrapper | Liquid/schema en theme-regels | Juiste volledige snapshot en bestaande projectbaseline; deze ronde niet volledig uitgevoerd |
| JS/CSS-parser of linter | Imports, selectors, dubbel geladen code, syntax en contracthooks | Eerst bestaande projecttools/versies hergebruiken; nieuwe tool alleen bij aantoonbaar voordeel |
| Shopify read-only inventaris | Toewijzingen, menu's, schema's, settings en datadekking | Paginering bewijzen; definities en waarden apart |
| Route-/runtimeverkenning | Geladen assets, requests, DOM, computed styles, console en interacties | Exacte bron/URL/viewport; beperkte representatieve matrix |
| Visuele vergelijking | Kaarten, keuzes, iconen, spacing en staten | Dezelfde functie en staat vergelijken, dynamische verschillen verklaren |
| Accessibilitycontrole | Labels, focus, semantiek, contrast, toetsenbord en touch | Automatische signalen plus handmatige kernhandelingen |
| Performance-/SEOmetingen | LCP/CLS/INP, netwerk, metadata, structured data, indexatie | Reproduceerbare omstandigheden; GSC/velddata vereisen eigen toegang |
| Afhankelijkheids-/securityscan | Bekende kwetsbaarheden, secrets en onveilige invoerpaden | Aanvullende gerichte review; geen automatische systeemwijziging of volledige veiligheidsclaim |
| Doccontroles | Lokale links, vaste ingangen, statuscodes, bronversies en actualiteit | Historische bronpaden als historisch markeren; niet alle tekst tot actuele waarheid verheffen |

## Reproduceren en controleren

De betekenisvolle scannerchecks staan op de actieve branch in [test_architecture_scan.py](https://github.com/jlamping1997/badkamercity/blob/fix/product-cards-2026-10-14/scripts/test_architecture_scan.py). Ze controleren onder andere commentaar/JSON-headers, verwijzingsresolutie, binaire hashes en de harde pariteitsgrens; ze sturen geen cart- of serververzoeken.

```bash
python3 -m unittest discover -s scripts -p 'test_architecture_scan.py' -v
```

De scanner is bewust geen complete parser of universele auditrobot. DOC-01/02 breiden de kaart alleen uit waar dat nodig is: dynamische verwijzingen, imports, Shopify-toewijzingen, omgekeerde afhankelijkheden en runtimebewijs. Vervang de kleine tool pas als een bestaande parser aantoonbaar betrouwbaarder en eenvoudiger onderhoudbaar is.

## Componentbronnen en veldconsumenten sinds DOC-02A

[build_component_reference.py op de actieve branch](https://github.com/jlamping1997/badkamercity/blob/fix/product-cards-2026-10-14/scripts/build_component_reference.py) gebruikt de expliciete [componentregistry](component-registry.json). De tool eist hash-/grootteovereenkomst voor elk geselecteerd bestand, vergelijkt exacte Git-blobs op een expliciet broncommit en schrijft alleen bronmetadata/letterlijke consumers. Optioneel leest hij alleen typen/aantallen uit een bevoegde private SQLite-export. Dit vult de eerdere brede statische scanner aan; geen volledige parser of autonome downloader.

Zie [fundament en tooling](components/FOUNDATIONS_AND_TOOLING.md) voor de reproduceerbare opdracht en [bewijs DOC-02A](evidence/2026-10-28-doc02/README.md) voor de daadwerkelijk uitgevoerde controles. 85 geselecteerde sources zijn geverifieerd, 52 letterlijke keys gevonden en 4 dynamische consumerlocaties apart gehouden. Een match bewijst geen actieve runtime-/stijl-/datacorrectheid.

## Geïsoleerde functiereplays sinds DOC-03A

De harness [scripts/component-audit](https://github.com/jlamping1997/badkamercity/tree/fix/product-cards-2026-10-14/scripts/component-audit) draait vier expliciet hashgecontroleerde bronbestanden met synthetische data en lokale request-/navigatiestubs. Geen automatische Shopify-downloader of echte kooptest. Het [bewijs](evidence/2026-10-28-micro/README.md) scheidt 10 controles, 3 defectreproducties voor twee problemen en 2 grenzen; een geslaagde harnessrun betekent niet dat alle componentcontracten correct zijn.

## Brede naslag sinds DOC-02C

`scripts/build_site_reference.py` op de actieve branch bouwt [alle templates/secties/settings/snippets/assets](reference/README.md) uit de expliciete snapshot en het manifest. Uitvoer scheidt BYTE_MATCH, BYTE_MISMATCH en MANIFEST_ONLY en bevat geen bronbody- of settingswaarden. Admin-naslag is apart bijgehouden. Rebuildopdracht en grenzen staan in [MAINTENANCE.md](MAINTENANCE.md).

## Ketenreplay en inhoudsstructuur DOC-03B

`transitions.mjs` in de bestaande component-audit-harness toetst samenhangende inbouw/form-, footer-, content- en disclosurestaten met dezelfde gepinde happy-dom. Zes uitgevoerde bronnen zijn vooraf gehasht; tien gericht gelezen bronnen staan in het [manifest](evidence/2026-10-28-transitions/source-provenance.json). Geen netwerk of echte cartactie. De [39 cases](evidence/2026-10-28-transitions/results.json), 715-regel-mappingcontrole en 109-page-bodystructuur zijn verschillende bewijssoorten; hun aantallen niet bij elkaar optellen als featuretests.

## Filterreplay DOC-03C

Dezelfde gepinde harness bevat nu `filters.mjs`: drie hashgecontroleerde JS-bronnen, 41 cases en expliciete transport-/validity-/geometry-/historygrenzen. Negen gerichte sourcebytes en twee publieke facetmetadatareads staan in [het bewijs](evidence/2026-10-28-filters/README.md). Geen nieuwe dependency of volledige themesnapshot; geen echte cart-/indexwrite.

## Wishlistreplay sinds DOC-03D

`wishlist.mjs` op de actieve branch voert de volledige hashgecontroleerde wishlistclosure uit en in WL-43 ook de volledige Sunshower-shopcontroller. Synthetische storage, handmatig bezorgde storage-events, product-/cartresponses, timers, imagepreload en navigatiestubs voorkomen echte klant-/cartacties. Twee cases gebruiken de DOMlibrary-MutationObserver; de rest schakelt hem uit.

```bash
node scripts/component-audit/wishlist.mjs \
  --source /pad/naar/gecontroleerde-themefiles \
  --manifest docs/architecture/evidence/2026-10-28-wishlist/source-provenance.json \
  --output /tmp/badkamercity-wishlist.json
```

De 43 cases leveren 34 controles, twee defectreproducties en zeven grenzen; dezelfde gepinde happy-dom 21.0.4 en optionele --dom-module gelden. De SHA-negatiefcontrole weigert vóór uitvoering/output. Geen native eventlooptiming, CSS/focus/touch of werkelijk cartresultaat afleiden. [Bewijs](evidence/2026-10-28-wishlist/README.md).
