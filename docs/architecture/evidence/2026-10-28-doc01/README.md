# DOC-01 — bewijs, 28 oktober 2026

Lees [de bronkaart](../../DOC01_SOURCE_MAP.md) voor betekenis en beperkingen. Dit is een read-only bron-/datainventaris, geen volledige UI-audit of identieke deploysnapshot.

| Bestand | Bewijs |
| --- | --- |
| normalized-manifest.json | Alle 1.262 bestandsnamen, metadata en MD5 uit Shopify MAIN |
| theme-readback-check.json | 1.261 exact; 1 open uitzondering voor settings_data.json, inclusief feitelijke hashes/groottes |
| theme-inventory.json | Volledige ontvangen snapshot statisch geïnventariseerd; 955 refs; 0 parsefouten |
| source-provenance.json | Bytevergelijking met alle gevolgde bestanden op broncommit: 384 root, 84 elders, 794 zonder match |
| manifest-stability.json | Canonieke voor-/nahashes, rol en aantal |
| reverse-dependencies.json | Omgekeerde kaart van dezelfde 955 statische refs |
| STATIC_SCAN.md | Gegenereerde zoekingang met scannerbeperkingen |
| admin-assignment-counts.json | Product-/collectietemplates en menu-aantallen, zonder private waarden |
| metafield-register.json | Eigenaar, key, type, aantallen en vulling; geen veldwaarden |
| data-validation.json | Exporttellingen en database-/joincontroles |

Manifest vóór en na uitlezing had dezelfde paden/checksums; MAIN bleef 195818389770. Eén tekstbody komt niet overeen met zijn Shopify-metadata. `--require-parity` gaf exitcode 2; die controle is niet afgezwakt. De ruwe themebestanden blijven buiten de publieke Git-root. Publieke bewijsbestanden bevatten geen productomschrijvingen, kostprijzen, voorraadregels of document-URL's.

Root-/steekproefrapporten in ../2026-10-28 blijven als historische nulmeting behouden. Gebruik ze niet als vervanging voor deze volledige statische inventaris. Dynamische Liquid/JS/CSS/appafhankelijkheden, runtime, pagina-/blogtoewijzingen, VPS en visuele consistentie blijven expliciet vervolgwerk.
