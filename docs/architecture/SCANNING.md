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
