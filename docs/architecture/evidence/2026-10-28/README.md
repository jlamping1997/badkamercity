# Onderzoeksbewijs 28 oktober 2026

## Bronnen

- Shopify Admin read-only theme-rollen en volledig bestandsmanifest van **MAIN 195818389770 — BadkamerCity - Smooth winkelwagen pop-up**; 1.262 bestanden, geen vervolgpagina.
- Git actieve branch **fix/product-cards-2026-10-14**, broncommit **4a85d063b750b74fd398fe106c11bfe05b6ce277**; schone nieuwe cloudcheckout bij aanvang.
- Git `main` bij aanvang **c265f9e91049ae57bb2ffb5e297004042161a178**. Windows-werkmap en eventuele andere lokale wijzigingen niet gecontroleerd of aangepast.
- Bestaande documentatie, releasedossier code-cleanup, toolconfiguratie en actuele code-steekproef.

## Bestanden in dit bewijsdossier

| Bestand | Wat het bewijst |
| --- | --- |
| [shopify-main-manifest.json](shopify-main-manifest.json) | Bestandsnamen, checksums, grootte, mediatype en wijzigingsmoment op het genoemde theme |
| [repository-root/README.md](repository-root/README.md) en [inventory.json](repository-root/inventory.json) | Statische inventaris van alle 441 root-themabestanden op het broncommit; 830 statische verwijzingen |
| [live-sample/README.md](live-sample/README.md) en [inventory.json](live-sample/inventory.json) | Inhoudelijke inspectie van 15 actuele bestanden, elk checksumgelijk; 149 statische verwijzingen |

De huidige live steekproef omvat layout/theme, main-product, main-sunshower, product.sunshower-template, algemene/zoekkaart, switchersnippet/JS, externe filtersnippet/JS, Sunshower pagina-CSS/JS/shop-JS, cart-JS en popupsnippet. De exacte lijst en hashes staan in de machinekaart. De bronbytes zijn intern read-only ingelezen; dit dossier kopieert geen volledig productie-thema over de Git-root.

## Uitkomst en grenzen

Git-root tegenover het verse manifest: **384 gelijk / 57 afwijkend / 821 alleen live / 0 alleen root**. De 821 omvatten **656 bc-choice-data-*.json-kandidaten** plus andere code/data/media en back-upbestanden. Die categorie is uit de naam afgeleid en moet met de generator/bronrelatie worden bevestigd; het is geen telling van 656 verschillende componenten.

De overige **1.247 live bestanden** zijn niet inhoudelijk onderdeel van de 15-bestandensteekproef. Er is geen volledige actuele runtime-, telefoon-, checkout-, VPS-, app-, catalogus-, performance-, security- of SEO-audit uitgevoerd in deze documentatieronde. Historische tests zijn uitsluitend als historische context gelezen.

Geen Shopify-theme-/product-/cartmutaties, publicatie, VPS-mutaties of nieuwe achtergrondplanning door deze onderzoeksronde. De nieuwe scanner en zijn checks schrijven alleen lokale rapporten/testfixtures; Git-opslag van documentatie en tooling is de bedoelde wijziging.

Deze meting wordt bewaard als gedateerd bewijs. Een nieuwe MAIN/publicatie krijgt een nieuwe meting; de actuele ingang wordt bijgewerkt zonder oude feiten stil te herschrijven.
