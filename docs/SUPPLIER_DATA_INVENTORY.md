# BadkamerCity leveranciersbronnen- en productveldeninventaris

## 1. Taak, datum, status en scope

| Veld | Waarde |
| --- | --- |
| Taak | `BC-DATA-002` - Leveranciersbronnen en productvelden read-only inventariseren |
| Onderzoeksdatum | 2026-08-10 |
| Status | `DONE` |
| Menselijk goedgekeurd | 2026-08-10 |
| Masterplan bij goedkeuring | Versie 0.10, `ACTIVE FOR DISCOVERY - IMPLEMENTATION BLOCKED` |
| Repository | `CITY_MASTER` op branch `main` |
| Onderzochte HEAD | `12aabf6217c5babbc1dd41aa813fa54770437d87` |
| Scope | Alleen repository, projectdocumentatie, lokale bestanden, statische code, Git-metadata en bestandsmetadata |
| Buiten scope | Shopify benaderen, imports uitvoeren, brondata corrigeren, mappings besluiten, theme-code wijzigen, scripts uitvoeren, committen en pushen |

Dit rapport is een feitelijke lokale nulmeting. Het is geen productdatamodel, importontwerp, mappingbesluit, bronacceptatie of implementatietoestemming.

## 2. Bewijslabels

- **BEWEZEN:** rechtstreeks vastgesteld uit een lokaal bestand, veilige parseruitvoer of Git-metadata.
- **AFGELEID:** onderbouwde gevolgtrekking uit meerdere bewezen feiten, maar niet rechtstreeks als bronmetadata aanwezig.
- **NOG ONDERZOEKEN:** aanvullend read-only bewijs is nodig.
- **ONTBREEKT:** binnen de volledig onderzochte lokale repository niet gevonden.
- **OPEN BESLISSING:** een bevoegde menselijke eigenaar moet later kiezen.
- **NIET TOEGANKELIJK:** valt buiten de toegestane lokale route of vereiste tooling/data is niet aanwezig.

## 3. Gebruikte bronnen en methode

### 3.1 Bronnen

- `AGENTS.md`;
- `docs/MASTERPLAN.md` versie 0.8 bij start;
- `docs/SHOPIFY_ADMIN_INVENTORY.md`;
- `docs/ACTIVE_THEME_USAGE.md`;
- `docs/COMPETITOR_SEO_ANALYSIS.md`;
- `docs/REPOSITORY_AUDIT.md`;
- alle 405 bestanden die bij aanvang lokaal onder `CITY_MASTER` stonden;
- `git ls-files`, `git status`, `git log`, bestandsgrootte, wijzigingstijd en SHA-256-hashes;
- statische zoekacties met `rg` en read-only parsing met PowerShell `ConvertFrom-Json`.

### 3.2 Methode

1. De verplichte Git- en masterplanvoorcontrole is uitgevoerd voordat een bestand werd gewijzigd.
2. Alle lokale paden zijn recursief vergeleken met `git ls-files`.
3. Bestandsnamen, extensies, directorystructuur en inhoudelijke verwijzingen zijn doorzocht op leveranciers-, productdata-, import-, prijs-, voorraad-, identifier-, media-, specificatie- en switchertermen.
4. De bereikbare Git-geschiedenis is op huidige en vroegere relevante paden onderzocht.
5. Zes JSON-achtige switcherbestanden zijn volledig geparsed zonder ze te schrijven. Alleen schema's, tellingen, hashes en beperkte kwaliteitscontroles zijn vastgelegd.
6. JavaScript en Liquid zijn uitsluitend gelezen. Geen bestaand script is uitgevoerd.
7. Bestaand Shopify-bewijs is alleen uit de al aanwezige documentatie overgenomen. Shopify is niet benaderd.

### 3.3 Beperkingen

- **BEWEZEN:** de nulmeting dekt de volledige lokale repository en de bereikbare Git-padgeschiedenis op onderzoeksdatum.
- **NIET TOEGANKELIJK:** leveranciersportalen, mailboxen, cloudmappen, lokale bestanden buiten `CITY_MASTER`, externe jobs, apps en Shopify waren verboden of buiten scope.
- **NOG ONDERZOEKEN:** bestanden die nooit in deze Git-repository stonden, externe generatoren en mondeling bekende maar niet vastgelegde bronnen kunnen niet met deze route worden bewezen.
- **NOG ONDERZOEKEN:** bestandswijzigingstijden zijn voor de relevante themebestanden gelijk aan de lokale theme-import/checkout van 2026-08-03 en bewijzen niet de oorspronkelijke aanmaakdatum.

## 4. Veiligheidsbevestiging

**BEWEZEN:** tijdens dit onderzoek:

- is Shopify Admin niet benaderd;
- is geen nieuwe scope aangevraagd;
- is geen import, generator, converter of productdatascript uitgevoerd;
- is geen CSV, XLS, XLSX, JSON, XML of ander bronbestand gewijzigd;
- is geen theme-code gewijzigd en is geen theme gepusht, gepulld, gepubliceerd, hernoemd of verwijderd;
- is niets buiten `CITY_MASTER` doorzocht;
- zijn geen packages of apps geinstalleerd;
- is geen commit of push uitgevoerd.

Alleen dit rapport en `docs/MASTERPLAN.md` zijn voor taakadministratie gewijzigd.

## 5. Managementsamenvatting

1. **BEWEZEN:** bij aanvang bevatte `CITY_MASTER` 405 lokale bestanden; exact dezelfde 405 paden waren tracked in Git. Er waren geen lokale untracked of ignored databronnen.
2. **ONTBREEKT:** er is geen aantoonbaar oorspronkelijk leveranciersbestand. Er staat geen CSV, XLS, XLSX, XML, TSV, databasebestand of vergelijkbaar productexportbestand in de repository.
3. **ONTBREEKT:** er is geen Shopify-importbestand en geen import-, generator-, converter-, mapping-, validatie- of analysescript voor leveranciersproductdata.
4. **BEWEZEN:** er zijn zes valide UTF-8 JSON-achtige switcherassets: een actuele dataset en vijf backup-/QA-varianten. Zij zijn `SHOPIFY/THEME-DATA`, niet `BRONBESTAND` en niet bewezen als Shopify-importoutput.
5. **BEWEZEN:** de actuele dataset bevat 433 unieke groepen, 560 menu's en 3.383 unieke producthandles. Alle 3.383 titels en handles bevatten `Hotbath`; een expliciet vendorveld ontbreekt.
6. **BEWEZEN:** vijf JavaScriptbestanden zijn direct relevant voor de switcher: de actuele V2-runtime, drie backup-/QA-versies en `assets/global.js` met de legacy-runtime. Geen ervan genereert een leveranciers- of importbestand.
7. **BEWEZEN:** de actuele switcherdataset bevat geen SKU, leveranciersartikelnummer, EAN/GTIN, vendor, producttype, inkoopprijs, verkoopprijs, adviesprijs, BTW, valuta, voorraadhoeveelheid, levertijd, gewicht, verpakking, media, document, SEO-title of meta description.
8. **BEWEZEN:** `docs/SHOPIFY_ADMIN_INVENTORY.md` documenteert 7.550 producten met vendor `Hotbath` en 277 met vendor `THE MOSAIC FACTORY`. Alleen Hotbath is lokaal in afgeleide switcherdata vertegenwoordigd; voor beide vendors ontbreekt een oorspronkelijke lokale leveranciersbron.
9. **BEWEZEN:** de Admin-documentatie meldt 17 ontbrekende SKU's, 72 groepen met dubbele niet-lege SKU-waarden en 69 producten met producttype `undefined`. De lokale assets bevatten geen SKU waarmee deze problemen aan een bron kunnen worden gekoppeld.
10. **GEBLOKKEERD:** `BC-DATA-001` kan nog niet verantwoord een definitieve veldcatalogus of mapping ontwerpen. Eerst zijn oorspronkelijke leveranciersbestanden, bronhouders, actualiteitsdata, velddefinities en het ontbrekende generatie-/importproces nodig.

## 6. Volledige lokale bestandsinventaris

### 6.1 Repositorybrede formaatscan

| Controle | Resultaat | Conclusie |
| --- | ---: | --- |
| Lokale bestanden bij start | 405 | **BEWEZEN** volledig recursief binnen `CITY_MASTER` |
| Tracked paden | 405 | **BEWEZEN** exacte setgelijkheid met lokale bestanden |
| Untracked/ignored databronnen bij start | 0 | **BEWEZEN** via Git-status inclusief ignored-weergave |
| `.liquid` | 116 | Themecode; geen oorspronkelijke productrecordbestanden |
| `.svg` | 92 | Theme-assets; geen productmedia-export of leveranciersbron bewezen |
| Exacte extensie `.json` | 80 | 3 switcherdatasets en 77 themeconfiguratie-, template- of localebestanden |
| JSON-inhoud met niet-standaard backupsuffix | 3 | Drie extra switcherdatasetbackups |
| `.css` | 68 | Themepresentatie |
| `.js` | 34 | Storefrontruntime; 5 direct switcherrelevant, geen Node/importtooling |
| `.md` voor toevoeging van dit rapport | 9 | Projectdocumentatie/bewijs |
| `.gif` | 1 | Themebeeld, geen productbron bewezen |
| `.csv`, `.tsv`, `.xls`, `.xlsx`, `.xml` | 0 | **ONTBREEKT** |
| `.py`, `.ps1`, `.sh` of vergelijkbare datascripts | 0 | **ONTBREEKT** |
| Package manifest / CI-importconfiguratie | 0 | **ONTBREEKT** |

De 80 bestanden met exacte extensie `.json` bestaan uit 3 switcherdatasets, 2 configuratiebestanden, 51 localebestanden, 2 section groups en 22 templates. De drie bestanden met een QA-backupsuffix hebben JSON-inhoud, maar niet `.json` als laatste extensie. Geen van de 77 overige JSON-bestanden bevat een leveranciersproducttabel.

### 6.2 Kerninventaris bron-, data- en scriptbestanden

| Klasse | Aantal | Uitkomst |
| --- | ---: | --- |
| `BRONBESTAND` | 0 | **ONTBREEKT**: geen oorspronkelijke leveranciersexport bewezen |
| `AFGELEID IMPORTBESTAND` | 0 | **ONTBREEKT**: geen bestand is bewezen als Shopify-importpayload |
| `SHOPIFY/THEME-DATA` | 6 | Actuele switcherdataset plus vijf backups/QA-varianten |
| `SCRIPT/TOOLING` | 5 | Alleen storefront-JavaScript voor actuele/legacy switchers; geen import-/generatietooling |
| `DOCUMENTATIE/BEWIJS` | 5 primair | De vijf voor deze taak inhoudelijk relevante bestaande documenten |
| `REFERENTIE MAAR BESTAND ONTBREEKT` | 3 broncategorieen | Oorspronkelijke leveranciersbestanden, switchergenerator/mapping en import-/validatieketen; exacte bestandsnamen zijn niet bewezen |
| `ONBEKEND` | 0 lokale kernbestanden | De rol van de zes data-assets is aantoonbaar theme/switcherdata; hun externe oorsprong/eigenaar blijft onbekend |

**BEWEZEN:** er zijn daarmee 11 lokale kernbestanden in de categorieen data/script, maar nul oorspronkelijke bronbestanden en nul afgeleide importbestanden.

### 6.3 Data-assets

Alle onderstaande bestanden zijn tracked, niet ignored, toegevoegd in commit `085860b` (`Initial Shopify theme import`, auteur `Jason L`) en lokaal gewijzigd op 2026-08-03 14:25:05 +02:00. Deze Git-auteur is alleen repositoryprovenance en geen bewijs van bronhouderschap.

| Pad | Bytes | Interne `generated_at` | Groepen | Menu's | Productentries | Classificatie | Bronhouder |
| --- | ---: | --- | ---: | ---: | ---: | --- | --- |
| `assets/product-switcher-data.json` | 1.894.030 | 2026-07-07T09:16:33.143Z | 433 | 560 | 3.383 | `SHOPIFY/THEME-DATA`, **AFGELEID**, actief bereikbaar | **ONBEKEND** |
| `assets/product-switcher-data.backup.json` | 3.731 | 2026-07-06T12:30:00Z | 1 | 3 | 6 | `SHOPIFY/THEME-DATA`, backup/testfixture | **ONBEKEND** |
| `assets/product-switcher-data.backup-before-production.json` | 6.889 | 2026-07-06T13:30:25.486Z | 1 | 2 | 12 | `SHOPIFY/THEME-DATA`, pre-productiebackup | **ONBEKEND** |
| `assets/product-switcher-data.json.backup-qa-round-1-20260706-214223` | 1.807.052 | 2026-07-06T14:34:55.247Z | 433 | 568 | 3.383 | `SHOPIFY/THEME-DATA`, QA-backup | **ONBEKEND** |
| `assets/product-switcher-data.json.backup-qa-round-1-rerun-20260707-110751` | 1.894.070 | 2026-07-06T19:44:55.844Z | 433 | 560 | 3.383 | `SHOPIFY/THEME-DATA`, QA-backup | **ONBEKEND** |
| `assets/product-switcher-data.json.backup-qa-round-2-20260707-111611` | 1.894.070 | 2026-07-07T09:07:52.679Z | 433 | 560 | 3.383 | `SHOPIFY/THEME-DATA`, QA-backup | **ONBEKEND** |

Aanvullend bewijs:

- alle zes bestanden zijn valide UTF-8 zonder BOM en parsen als JSON;
- alle zes hebben top-level keys `version`, `generated_at` en `groups`;
- de actuele SHA-256 is `44DADF9ABEBBD6F0961DFF5F8C385D1A425AF8050C78BAF359E508844B4B0B27`;
- QA round 1 rerun en QA round 2 hebben inhoudelijk gelijke groepen en verschillen in `generated_at`;
- de actuele dataset bevat dezelfde 433 groeps-ID's en inhoudelijk gelijke afzonderlijke groepen als QA round 2, maar een andere groepsvolgorde en `generated_at`;
- de eerste grote QA-backup heeft 568 menu's zonder expliciete `values`; de actuele dataset heeft 560 menu's met 2.478 niet-lege stringwaarden;
- de kleine backup bevat een enkele testgroep en is geen bewijs van leveranciersdata;
- geen backupnaam wordt door de actieve code aangeroepen.

### 6.4 Direct relevante JavaScriptbestanden

| Pad | Bytes | SHA-256 / relatie | Rol | Classificatie |
| --- | ---: | --- | --- | --- |
| `assets/bc-product-switcher.js` | 11.902 | `2073B878...FA35A` | Actuele V2-storefrontruntime | `SCRIPT/TOOLING`, runtime; geen generator |
| `assets/bc-product-switcher.backup-debug.js` | 10.036 | `546044CC...3945` | Oudere/debugvariant; mist onder meer gebruik van vooraf berekende menuwaarden | `SCRIPT/TOOLING`, backup/debug |
| `assets/bc-product-switcher.js.backup-qa-round-1-20260706-214223` | 11.742 | `7E229428...CCCDB` | QA-variant; leidt menuwaarden alleen af uit productopties | `SCRIPT/TOOLING`, QA-backup |
| `assets/bc-product-switcher.js.backup-qa-round-1-rerun-20260707-110751` | 11.902 | Bytegelijk aan actuele V2-JavaScript | QA-backup | `SCRIPT/TOOLING`, QA-backup |
| `assets/global.js` | 63.019 | `41D96B97...89253` | Algemene storefrontcode met legacy `BCProductSwitcher` | `SCRIPT/TOOLING`, runtime; geen importtool |

Alle vijf zijn tracked en kwamen via dezelfde initiële theme-import in Git. Vier hebben lokale wijzigingstijd 2026-08-03 14:24:59 +02:00; `global.js` heeft 14:25:00 +02:00. Geen bronhouder of oorspronkelijke auteur is uit dit bewijs af te leiden.

### 6.5 Relevante themeconsumenten en veldbewijs

Deze bestanden zijn geen leveranciersbronnen. Zij bewijzen alleen welke Shopifyvelden of afgeleide data de storefront verwacht.

| Pad | Rol in de dataketen | Classificatie |
| --- | --- | --- |
| `templates/product.json` | Actief producttemplate met vendor, titel, prijs, variantpicker en beschrijving | `SHOPIFY/THEME-DATA` configuratie |
| `sections/main-product.liquid` | Leest standaard productvelden, 54 statische custom keys en dynamische legacyvelden; bouwt legacy inline JSON | Themeconsument/transformatie |
| `snippets/bc-product-switcher.liquid` | Leest `custom.switch_group` en koppelt V2-JavaScript/dataset | Themeconsument/transformatie |
| `sections/product-specs.liquid` | Losse, niet actief toegewezen specificatiesectie met 32 statische veldreferenties | Themeconsument; kandidaat-legacy |
| `sections/short-specs.liquid` | Losse korte specificatiesectie met vijf velden | Themeconsument; niet actief toegewezen |
| `snippets/bc-product-spec-row.liquid` | Presenteert strings en booleans uit een metafieldobject | Themeconsument/transformatie |
| `snippets/bc-product-spec-header.liquid` | Koprij voor specificaties | Themeconsument |
| `snippets/product-pros-cons.liquid` | Leest lijsten `custom.pluspunten` en `custom.aandachtspunten` | Themeconsument |
| `snippets/bc-card-product-search.liquid` | Leest twee zoekkaartvelden en standaard prijs/media | Themeconsument |
| `snippets/price.liquid` | Leest Shopifyprijs, compare-at, valutaweergave en unit price | Themeconsument |
| `snippets/buy-buttons.liquid` | Leest availability, inventory policy/quantity en quantity rules | Themeconsument |
| `snippets/product-media-gallery.liquid` | Leest Shopify product- en variantmedia | Themeconsument |
| `snippets/unit-price.liquid` | Presenteert Shopify unit-price measurement | Themeconsument; geen tegelbron |

### 6.6 Primair documentatiebewijs

| Pad | Bewezen bijdrage | Beperking |
| --- | --- | --- |
| `docs/SHOPIFY_ADMIN_INVENTORY.md` | Vendors, product/SKU-totalen, metafielddefinities en bestaande Admin-dekking | Snapshot 2026-08-04; niet opnieuw benaderd |
| `docs/ACTIVE_THEME_USAGE.md` | Actieve V2- en legacyketens, backups en live bereikbaarheid | Statisch onderzoek; runtimevolledigheid open |
| `docs/REPOSITORY_AUDIT.md` | Eerdere bestands- en switcherbevindingen, ontbrekende generator/documentatie | Statische momentopname |
| `docs/COMPETITOR_SEO_ANALYSIS.md` | Eisen- en marktcontext, geen leveranciersbron | Geen BadkamerCity-productbron |
| `docs/MASTERPLAN.md` | Taken, eisen, afhankelijkheden, risico's en open bronvragen | Eisen zijn geen bewijs dat velden/bronnen bestaan |

## 7. Bronnen per leverancier of merk

### 7.1 Hotbath

| Aspect | Bevinding |
| --- | --- |
| Lokale oorspronkelijke bron | **ONTBREEKT** |
| Lokale afgeleide data | **BEWEZEN:** vijf van de zes switcherdatasets bevatten Hotbath-productdata; de actuele dataset heeft Hotbath in alle 3.383 titels en handles |
| Expliciet vendorveld in dataset | **ONTBREEKT** |
| Documentatiebewijs | **BEWEZEN:** Admin-rapport telt 7.550 producten met vendor `Hotbath` |
| Relatie bron naar asset | **NOG ONDERZOEKEN:** generator, mapping en originele input ontbreken |
| Bronhouder/eigenaar | **ONBEKEND** |
| Actualiteit | Interne generatie 2026-07-07 voor actuele asset; betekenis en updatefrequentie **NOG ONDERZOEKEN** |

De naamdekking maakt Hotbath als inhoud van de actuele dataset **BEWEZEN**. Zij bewijst niet dat de JSON rechtstreeks door Hotbath is geleverd of dat Hotbath de bronhouder is.

### 7.2 The Mosaic Factory

| Aspect | Bevinding |
| --- | --- |
| Lokale oorspronkelijke bron | **ONTBREEKT** |
| Lokale afgeleide productdata | **ONTBREEKT**; `Mosaic` komt niet voor in de zes datasets |
| Lokaal script | **ONTBREEKT**; ook geen Mosaic-pad in bereikbare Git-geschiedenis |
| Documentatiebewijs | **BEWEZEN:** Admin-rapport telt 277 producten met vendor `THE MOSAIC FACTORY` en producttype `Mozaiektegel` |
| Bronhouder/eigenaar | **ONBEKEND** |

The Mosaic Factory is dus alleen in lokale documentatie vertegenwoordigd, niet in een lokaal leverancier-, import- of theme-databestand.

### 7.3 Overige leveranciers

**NOG ONDERZOEKEN:** het projectdoel noemt circa 20.000 producten, terwijl het bestaande Admin-bewijs alleen Hotbath en The Mosaic Factory noemt. Er is geen lokaal bestand dat andere leveranciers of toekomstige assortimentbronnen identificeert. Namen mogen niet worden verzonnen.

## 8. Oorspronkelijke versus afgeleide bronnen

### 8.1 V2-switcherketen

```text
[ONTBREEKT] oorspronkelijke Hotbath-bron
  -> [ONTBREEKT] generator, mapping en validatieregels
  -> [AFGELEID] assets/product-switcher-data.json plus backups
  -> [BEWEZEN] snippets/bc-product-switcher.liquid
  -> [BEWEZEN] assets/bc-product-switcher.js
  -> storefrontnavigatie naar een bestaand product
```

Een eventuele Shopify-importschakel is **NOG ONDERZOEKEN**. Geen lokaal bestand of document bewijst dat de JSON zelf is geimporteerd in Shopify.

### 8.2 Legacy-switcherketen

```text
[ONTBREEKT] oorspronkelijke leveranciersbron en importmapping
  -> [bestaande Shopify-objecten; alleen eerder documentatiebewijs]
  -> sections/main-product.liquid bouwt inline JSON uit collectie/product/metafielddata
  -> assets/global.js leest en verrijkt die runtime-data via publieke section-GET's
  -> storefrontnavigatie naar een bestaand product
```

**BEWEZEN:** deze keten heeft geen lokaal tussenbestand. Het is een runtimeweergave, geen generator voor een leveranciers- of importbestand.

### 8.3 Productspecificaties, prijs, voorraad en media

```text
[ONTBREEKT] leveranciersvelden en bronhouder
  -> [ONTBREEKT] mapping/importbewijs
  -> [bestaande Shopifyvelden; deels bewezen in bestaand Admin-rapport]
  -> Liquidpresentatie in product-, kaart-, prijs-, voorraad- en mediasnippets
```

De storefrontcode bewijst een verwachte veldnaam, maar niet dat de leverancier die naam, datatype, waarde of semantiek aanlevert.

## 9. Dataformaatanalyse

### 9.1 CSV

**ONTBREEKT:** er is geen CSV of TSV. Delimiter, encoding, headers, rijen, nullwaarden en duplicaten zijn daarom niet van toepassing.

### 9.2 XLS/XLSX

**ONTBREEKT:** er is geen XLS of XLSX. Er was geen workbook om read-only te openen; er is geen package geinstalleerd.

### 9.3 XML

**ONTBREEKT:** er is geen XML-productfeed of XML-configuratiebestand.

### 9.4 JSON en JSON-achtige backups

Het actuele schema is:

```text
version: integer
generated_at: ISO-8601 string
groups: array
  id: string
  label: string
  menus: array
    key: string
    label: string
    order: integer
    display_type: string
    hide_if_single_value: boolean
    values: array<string>
  products: array
    handle: string
    url: string
    title: string
    available: boolean
    sort_order: integer
    options: object<string,string>
```

**BEWEZEN actuele kwaliteit:** alle objectvelden zijn aanwezig; alle stringidentifiers, titels, URL's en optionwaarden zijn niet leeg. Groepen bevatten 2 tot 140 producten, mediaan 4. Groepen bevatten 1 tot 5 menu's, mediaan 1.

### 9.5 Representatieve beperkte steekproef

De groep `hotbath-ace-ac003-wastafelkraan` bevat 12 productentries en de menu's `kleur` en `type`. Een representatieve entry heeft handle `hotbath-ace-ac003-wastafelkraan-laag-zonder-waste-geborsteld-messing-pvd`, titel `Hotbath Ace AC003 wastafelkraan - geborsteld messing pvd` en de stringopties `kleur = Geborsteld messing PVD`, `type = Laag`. Dit illustreert het schema; er is geen productdump opgenomen.

## 10. Scripts- en toolingmatrix

| Script/pad | Doel volgens code | Input | Output/transformatie | Leverancier/prijs/titel | Validatie | Writes/mutaties | Read-only uitvoeren? |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `assets/bc-product-switcher.js` | V2-switcher initialiseren | JSON-URL, groep, handle, product-URL | Trimt waarden, sorteert menu/productorder, matcht opties, bouwt DOM en navigeert | Geen vendor- of prijslogica; titel alleen in data | HTTP-status, groep, huidig product, menu's, minstens 2 producten, partial/exact match | DOMwijziging en browsernavigatie; alleen GET naar asset, geen bestand/Admin-write | Niet uitgevoerd; geen data-analysetool |
| `assets/bc-product-switcher.backup-debug.js` | Oudere/debug V2-runtime | Zelfde actuele standaard-URL | Leidt menuwaarden uit producten af; minder diagnostiek | Geen leverancier-/prijslogica | Beperkter dan actueel | DOM/navigatie/GET | Niet uitvoeren; backup |
| `assets/bc-product-switcher.js.backup-qa-round-1-20260706-214223` | QA-runtime | Zelfde actuele standaard-URL | Als actueel, maar gebruikt vooraf berekende `menu.values` nog niet | Geen leverancier-/prijslogica | Groep/product/matchcontroles | DOM/navigatie/GET | Niet uitvoeren; backup |
| `assets/bc-product-switcher.js.backup-qa-round-1-rerun-20260707-110751` | QA-rerun | Zelfde actuele standaard-URL | Bytegelijk aan actuele runtime | Geen leverancier-/prijslogica | Gelijk aan actueel | DOM/navigatie/GET | Niet uitvoeren; backup |
| `assets/global.js` | Algemene storefront plus legacy switcher | Inline JSON uit `main-product`, section-HTML | NL-sortering, ontbrekende opties aanvullen, partial/exact match, GET van extra collectiepagina's | Geen vendorlogica; inline data bevat prijs/compare-at maar matcht er niet op | JSON parse, bestaande URL, deduplicatie op id/handle/URL | Legacyklasse gebruikt GET/DOM/navigatie; het volledige bestand bevat daarnaast een generieke POST-confighelper voor storefrontacties | Niet uitvoeren als read-only tooling |
| `sections/main-product.liquid` | Actieve PDP en legacy-dataopbouw | Shopify product, variant, collecties en metafields | Inline JSON met id/handle/URL/titel/availability/prijs/compare-at en legacyfields | Hotbath-specvelden; geen normalisatie; hardcoded levertijdtekst | Alleen aanwezigheid/vergelijkingen in Liquid | Rendert formulier/UI; geen lokaal bestandsschrijven | Alleen statisch gelezen |
| `snippets/bc-product-switcher.liquid` | V2 koppelen | `custom.switch_group`, handle en URL | Data-attributen plus script/assetreferentie | Geen prijs-/titeltransformatie | Alleen niet-leeg switch_group | Rendert DOM/script | Alleen statisch gelezen |

### 10.1 Afwezige tooling

**ONTBREEKT:** scripts voor The Mosaic Factory, CSV-import, XLSX-conversie, productdata-analyse, titel-/vendor-normalisatie, prijsberekening, switcherdatageneratie, productievalidatie, mapping en Shopify-productimport.

De 34 JavaScriptbestanden bevatten geen Node `require`/`import`, `node:fs`, `writeFile`, GraphQL, Admin API of GraphQL-mutatie. Dit bewijst dat de huidige repository geen herkenbare lokale Node-datatooling bevat. Het bewijst niet dat een externe job niet bestaat.

## 11. Feitelijke veldcatalogus van lokale data

### 11.1 Actuele datasetvelden

| Domein | Exacte bronnaam | Datatype | Dekking | Identifierrol | Relevantie |
| --- | --- | --- | ---: | --- | --- |
| Metadata | `version` | integer | 1/1 | Schema-/versieaanduiding | `BC-DATA-001`, `BC-SWITCH-001` |
| Metadata | `generated_at` | ISO string | 1/1 | Snapshotdatum, geen product-ID | `BC-DATA-001`, `BC-SWITCH-001` |
| Relatie | `groups[].id` | string | 433/433 niet leeg, 433 uniek | Beoogde groepkoppeling; feitelijke Admin-match niet gemeten | `BC-SWITCH-001` |
| Relatie | `groups[].label` | string | 433/433 niet leeg, 433 uniek | Presentatie/zelfde waarde als id | `BC-SWITCH-001` |
| Relatie | `menus[].key` | string | 560/560 niet leeg | Optieveldsleutel binnen groep | `BC-DATA-001`, `BC-SWITCH-001` |
| Presentatie | `menus[].label` | string | 560/560 niet leeg | Geen identifier | `BC-SWITCH-001` |
| Presentatie | `menus[].order` | integer | 560/560 | Sorteervolgorde | `BC-SWITCH-001` |
| Presentatie | `menus[].display_type` | string | 560/560 | `buttons`, `dropdown` of `auto` | `BC-SWITCH-001` |
| Presentatie | `menus[].hide_if_single_value` | boolean | 560/560, alle `false` | Geen identifier | `BC-SWITCH-001` |
| Relatie | `menus[].values[]` | string | 2.478/2.478 niet leeg | Toegestane/gesorteerde optiewaarden | `BC-SWITCH-001` |
| Identiteit/SEO | `products[].handle` | string | 3.383/3.383 niet leeg en uniek | **BEWEZEN UNIEK binnen deze asset** | `BC-DATA-001`, `BC-PROD-001`, `BC-SWITCH-001` |
| Identiteit/SEO | `products[].url` | string | 3.383/3.383; exact `/products/` + handle | **BEWEZEN UNIEK binnen deze asset** | `BC-PROD-001`, `BC-SWITCH-001` |
| Identiteit/content | `products[].title` | string | 3.383 gevuld; 3.382 unieke waarden | **NIET UNIEK** | `BC-DATA-001`, `BC-PROD-001` |
| Logistiek | `products[].available` | boolean | 3.383/3.383, alle `true` | Geen voorraad-ID; betekenis/snapshotactualiteit open | `BC-LOG-001`, `BC-PROD-001` |
| Relatie | `products[].sort_order` | integer | 3.383/3.383; binnen groepen uniek | Presentatievolgorde | `BC-SWITCH-001` |
| Relatie/specificatie | `products[].options` | object met stringwaarden | 3.383/3.383; 6.172 toepasselijke waarden gevuld | Combinatiematch binnen groep | `BC-DATA-001`, `BC-SWITCH-001` |

### 11.2 Optievelden in de actuele dataset

`Producten` is hier het aantal productentries in groepen waar het menuveld van toepassing is. Alle gemeten toepasselijke waarden zijn strings en niet leeg.

| Exacte key | Groepen | Producten | Unieke waarden | Relevantie |
| --- | ---: | ---: | ---: | --- |
| `aantal_stangen` | 3 | 34 | 4 | Switcher/spec |
| `aantal_stopkranen` | 2 | 10 | 5 | Switcher/spec |
| `aantal_uitsparingen` | 1 | 54 | 3 | Switcher/spec |
| `afmeting` | 4 | 263 | 18 | Switcher/maatvoering |
| `afsluitbaar` | 1 | 8 | 2 | Switcher/spec |
| `afwerking` | 10 | 104 | 2 | Switcher/spec |
| `breedte` | 5 | 95 | 7 | Switcher/maatvoering |
| `breedte_diameter_hoofddouche` | 15 | 369 | 10 | Switcher/spec |
| `diameter_handdouche` | 1 | 13 | 2 | Switcher/spec |
| `frame` | 1 | 140 | 2 | Switcher/spec |
| `hangend` | 2 | 16 | 2 | Switcher/spec |
| `hoogte` | 8 | 161 | 4 | Switcher/maatvoering |
| `inclusief_toiletborstel` | 1 | 14 | 2 | Switcher/spec |
| `kleur` | 424 | 3.353 | 21 | Hoofdrelatie/switcher |
| `led` | 4 | 162 | 2 | Switcher/spec |
| `lengte` | 2 | 8 | 5 | Switcher/maatvoering |
| `lengte_plafondbuis` | 2 | 35 | 2 | Switcher/maatvoering |
| `lengte_uitloop` | 16 | 216 | 7 | Switcher/maatvoering |
| `met_geintegreerde_wateraansluiting` | 4 | 61 | 2 | Switcher/spec |
| `met_glijstang` | 2 | 96 | 2 | Switcher/spec |
| `met_handdouche` | 1 | 6 | 2 | Switcher/spec |
| `met_uitloop` | 11 | 94 | 2 | Switcher/spec |
| `met_vulcombinatie` | 1 | 24 | 2 | Switcher/spec |
| `plaatsing` | 2 | 30 | 4 | Switcher/spec |
| `speakers` | 1 | 4 | 2 | Switcher/spec |
| `type` | 11 | 146 | 15 | Switcher/type |
| `type_bevestiging_hoofddouche` | 5 | 163 | 7 | Switcher/spec |
| `type_handdouche` | 10 | 283 | 6 | Switcher/spec |
| `type_uitloop` | 4 | 100 | 5 | Switcher/spec |
| `vorm` | 6 | 110 | 3 | Switcher/spec |

### 11.3 In themecode verwachte velden

De lokale Liquid bevat 58 unieke statische `product.metafields.custom.<key>`-referenties:

- identiteit/content: `artikelnummer`, `fabrikantnummer`, `ean`, `serie`, `pluspunten`, `aandachtspunten`, `search_card_spec_1`, `search_card_spec_2`;
- switcher/relatie: `switch_group`, `group`, `switch_key`, `menu_1` tot en met `menu_5`;
- algemene en Hotbath-specificaties: `aantal_straalsoorten_handdouche`, `aantal_straalsoorten_hoofddouche`, `aantal_uitgangen_tegelijk_bedienbaar`, `afmeting`, `afwerking`, `afwerking_greep`, `basiskleur`, `bediening_voor_aan_uit`, `belgaqua_keurmerk`, `breedte_diameter_douchekop`, `breedte_diameter_hoofddouche`, `dikte_hoofddouche`, `frame`, `glansgraad`, `handdouche`, `hoofddouche`, `hoogte`, `hotbath_ecoair_system`, `hotbath_fluhs`, `hotbath_plumber_friendly`, `hotbath_shower_power_system`, `kleurgroep`, `led`, `lengte`, `lengte_douchearm`, `lengte_doucheslang`, `materiaal_kraan`, `met_doucheslang`, `met_glijstang`, `met_handdouche`, `met_hoofddouche`, `met_inbouwdeel`, `montage`, `montagewijze`, `plaatsing`, `thermostatisch`, `type`, `type_bevestiging_hoofddouche`, `type_handdouche`, `vorm`, `vorm_thermostaat`, `vormgeving_stijlgroep`.

Daarnaast kan de legacycode dynamisch `product.metafields.custom[menu_field]` lezen. De statische lijst is daarom geen bewezen bovengrens voor alle mogelijke legacyvelden.

**BEWEZEN uit bestaand Admin-rapport:** alleen `custom.switch_group` heeft een definitie en exacte dekking: 3.658/7.827 (46,74%). `custom.group`, `menu_1` tot en met `menu_5`, `pluspunten`, `aandachtspunten` en `switch_options` hebben exact 0/7.827. De 32 onderzochte specificatiekeys hadden geen definitie en kwamen niet voor in een steekproef van 40 producten; volledige waardedekking buiten die steekproef blijft **NOG ONDERZOEKEN**.

## 12. Identifier- en koppelsleutelanalyse

| Kandidaat | Bronnen | Bevinding | Label |
| --- | --- | --- | --- |
| `products[].handle` | Actuele switcherdataset | 3.383 gevuld, 3.383 uniek, URL sluit exact aan | **BEWEZEN UNIEK binnen asset** |
| `products[].url` | Actuele switcherdataset | 3.383 gevuld en uniek | **BEWEZEN UNIEK binnen asset** |
| `groups[].id` | Actuele switcherdataset | 433 gevuld en uniek; gelijk aan label | **BEWEZEN UNIEK binnen asset** |
| Optiecombinatie per groep | Actuele switcherdataset | Geen dubbele exacte combinatie binnen een groep gevonden | **BEWEZEN UNIEK binnen asset/snapshot** |
| `products[].title` | Actuele switcherdataset | Een dubbele titel voor twee verschillende handles | **NIET UNIEK** |
| Shopify SKU | Bestaand Admin-rapport | 7.810 gevuld, 17 leeg, 72 groepen met dubbele niet-lege waarde | **NIET UNIEK**, deels gedekt |
| `custom.switch_group` naar `groups[].id` | Admin-rapport plus lokale code/asset | Structuur is bedoeld voor koppeling, maar waarden zijn in deze taak niet uit Shopify gelezen/vergeleken | **NOG ONDERZOEKEN** |
| EAN/GTIN | Alleen statische themeverwachting `custom.ean` | Geen lokale waarden of bronbestand | **ONTBREEKT lokaal** |
| Leveranciersartikelnummer | Alleen statische themeverwachting `custom.fabrikantnummer` | Geen lokale waarden of bronbestand | **ONTBREEKT lokaal** |
| Vendor + artikelnummer | Geen gezamenlijke lokale data | Niet meetbaar | **NOG ONDERZOEKEN** |

De 3.658 Admin-producten met `custom.switch_group` en 3.383 lokale unieke handles verschillen numeriek met 275. Dit is geen bewezen missende set: zonder de Admin-waarden/handles naast de asset te leggen is de een-op-eenrelatie **NOG ONDERZOEKEN**.

Geen veld wordt in dit rapport definitief als primaire sleutel aangewezen.

## 13. Prijsvelden

- **ONTBREEKT lokaal in leveranciers-/switcherdata:** inkoopprijs, verkoopprijs, adviesprijs, korting, BTW-indicatie en valuta.
- **BEWEZEN themeverwachting:** Shopify `price`, `compare_at_price`, prijsbereiken, quantity price breaks en unit price worden in Liquid gepresenteerd.
- **BEWEZEN legacy-runtime:** `sections/main-product.liquid` neemt `price` en `compare_at_price` op in inline JSON, maar `BCProductSwitcher` gebruikt ze niet voor matching.
- **NOG ONDERZOEKEN:** bron, munteenheid, BTW-semantiek, adviesprijsbeleid, inkoopprijs, kortingsregels en updatefrequentie.

## 14. Voorraad- en levertijdvelden

- **BEWEZEN lokaal veld:** alleen `products[].available`; alle 3.383 waarden in de actuele asset zijn `true`.
- **Risico:** `available` is geen voorraadhoeveelheid, locatievoorraad, leveranciersvoorraad of levertijd. De betekenis en actualiteit van de gegenereerde snapshot zijn onbekend.
- **BEWEZEN themeverwachting:** variant `available`, `inventory_management`, `inventory_policy`, `inventory_quantity` en quantity rules.
- **BEWEZEN inhoudelijk risico:** de actieve `sections/main-product.liquid` bevat binnen de prijsweergave de vaste tekst `Verwachte levertijd: 8 - 9 weken`, zonder lokaal dataveld of leverancierregel.
- **ONTBREEKT:** lokale leverancierfeed voor voorraad/status, cutoff, backorder, dropshipvoorraad en levertijd.

## 15. Media- en documentvelden

- **ONTBREEKT in de zes data-assets:** afbeelding-URL, lokale productafbeeldingsreferentie, video, document, handleiding en datasheet.
- **BEWEZEN themeverwachting:** Shopify `product.media`, `featured_media`, variantmedia en alttekst worden door de mediagalerij gelezen.
- **ONTBREEKT:** lokale mapping van leveranciersmedia naar Shopifymedia en documentvelden.
- **NOG ONDERZOEKEN:** auteursrecht, bronhouder, bestandskwaliteit, naamconventie, deduplicatie en updateproces.

## 16. Specificatievelden

- De actuele switcherasset heeft 30 optiekeys en exact 6.172 niet-lege toepasselijke stringwaarden.
- Themecode verwacht daarnaast meerdere identificatie-, algemene, douche-/thermostaat- en Hotbath-systeemvelden.
- **BEWEZEN:** `kleur` in V2 en `basiskleur` in legacy/theme zijn verschillende keys. Een bewuste mapping is niet lokaal vastgelegd.
- **BEWEZEN:** de specificatierenderer accepteert booleans of strings die als `true`/`false` lezen, maar dit is presentatielogica en geen brontypebewijs.
- **NOG ONDERZOEKEN:** eenheden, toegestane waarden, taal, bron per veld, definities en volledige productdekking.

## 17. Tegel- en eenheidsvelden

- **ONTBREEKT:** m2/doos, stuks/doos, doosinhoud, verpakking, palletinformatie, snijverlies, verkoop-/besteleenheid en tegelcalculatorinput.
- **BEWEZEN themevoorziening:** generieke Shopify `unit_price` en `unit_price_measurement` kunnen worden gepresenteerd. Er zijn geen lokale productwaarden die tegelgeschiktheid bewijzen.
- **BEWEZEN documentatiecontext:** The Mosaic Factory heeft 277 producten in het eerdere Admin-rapport, maar geen lokale bron of tegelvelden.
- `BC-TILE-001` blijft geblokkeerd tot de tegelbron, eenheden, verpakking, voorraad- en afrondingsregels zijn aangeleverd en menselijk gevalideerd.

## 18. Switcher- en relatievelden

### V2

- trigger: `custom.switch_group`;
- lokale groepssleutel: `groups[].id`;
- productkoppeling: handle en URL;
- keuzevelden: 30 menu-/optionkeys;
- runtime: exacte combinatie leidt naar een bestaand product-URL;
- geen SKU, EAN of variant-ID in de asset.

### Legacy

- trigger: `custom.group` wanneer `custom.switch_group` leeg is;
- broncollectie via groepswaarde of collectiecontext;
- menuvelden via `custom.menu_1` tot en met `custom.menu_5`, anders vijf vaste fallbackkeys;
- dynamische custom-metafieldlookup;
- inline productvelden bevatten id, handle, URL, titel, availability, prijs en compare-at.

**BEWEZEN huidig Admin-bewijs:** `custom.group` en alle vijf menuvelden zijn leeg/afwezig op 7.827 producten. De legacycode bestaat, maar het actuele databereik is niet aangetoond.

## 19. Datakwaliteitsbevindingen

| Bevinding | Bewijs | Gevolg |
| --- | --- | --- |
| Geen oorspronkelijke bron | Volledige 405-bestandenscan en Git-padgeschiedenis | Afgeleide data kan niet tegen de leverancier worden gevalideerd of betrouwbaar opnieuw worden gegenereerd |
| Geen generator/mapping/schema | Geen lokaal script/config/document met proces | Reproduceerbaarheid en eigenaarschap ontbreken |
| Assetdekking versus trigger | 3.383 handles versus 3.658 Admin-triggerproducten | Mogelijke drift; exacte setvergelijking blijft nodig |
| Identifierkwaliteit asset | Handles, URL's, group-id's en optiecombinaties uniek binnen snapshot | Goede interne assetconsistentie, geen bewijs van bronuniekheid |
| Niet-standaard group-id | 432/433 slugachtig; een ID bevat hoofdletters en spaties | Normalisatie-/matchrisico als Admin-waarde afwijkt |
| Dubbele titel | Een titel hoort bij twee verschillende handles | Titel ongeschikt als sleutel |
| Availability eenzijdig | 3.383/3.383 `true` | Geen bruikbare voorraad- of leverbelofte; mogelijke veroudering |
| Veldnaamverschil | V2 `kleur`, legacy `basiskleur` | Mappingbesluit en migratietest nodig |
| Backups divergeren | 568 versus 560 menu's; ontbrekende versus aanwezige `values`; verschillende timestamps/order | Onbekende productie-/QA-selectie en geen bewaarbeleid |
| SKU/producttype uit Admin-documentatie | 17 SKU's leeg, 72 duplicaatgroepen, 69 `undefined` producttypes | Import- en categorisatierisico kan lokaal niet naar bron worden herleid |
| Vendorweergave | Theme gebruikt `product.metafields.vendor`; Admin bewees alleen `product.vendor` gevuld | Risico op ontbrekend merk in specificaties |
| Levertijd | Vaste `8 - 9 weken` in actieve PDP-code | Klantbelofte is niet aan leverancier/product/voorraad gekoppeld |
| Specificaties | 58 statische custom keys, maar slechts een Admin-definitie | Type, validatie, dekking en eigenaarschap ontbreken |
| Tegeldata | Geen eenheids-/verpakkingsvelden | Calculator en juiste bestelhoeveelheid niet ontwerpbaar |

## 20. Ontbrekende of niet gevonden bronnen

Er is geen exact ontbrekend historisch bestandspad bewezen. Daarom worden geen bestandsnamen verzonnen.

| Leverancier/onderwerp | Benodigde bron/type | Waarom aantoonbaar nodig | Blokkeert | Verwijzing | Status |
| --- | --- | --- | --- | --- | --- |
| Hotbath | Oorspronkelijke productexport met velddefinitie en snapshotdatum | 7.550 Admin-producten en 3.383 lokale switcherhandles bestaan, maar oorsprong ontbreekt | `BC-DATA-001`, `BC-LOG-001`, `BC-PROD-001`, `BC-SWITCH-001` | Adminrapport, switcherassets en themevelden | **ONTBREEKT LOKAAL**, bronhouder onbekend |
| The Mosaic Factory | Oorspronkelijke product-/tegelexport | 277 Admin-producten bestaan; lokaal geen record- of tegelbron | `BC-DATA-001`, `BC-PROD-001`, `BC-TILE-001`, `BC-LOG-001` | Adminrapport | **ONTBREEKT LOKAAL**, bronhouder onbekend |
| Switcher | Generator, mapping, inputdefinitie en validatieregels voor `product-switcher-data.json` | Asset bevat `generated_at`; bestaand auditbewijs vraagt expliciet naar generatieproces | `BC-SWITCH-001`, `BC-DATA-001` | Repository-audit, actieve-themeanalyse, asset | **REFERENTIE GEVONDEN, BESTAND NIET GEVONDEN** |
| Shopify-import | Importpayloads, mapping, uitvoerlog en statusbewijs | Productonboarding en bestaande producten moeten aan bronnen herleidbaar zijn | `BC-DATA-001`, `BC-PROD-001` | Masterplan en Adminrapport | **NOG ONDERZOEKEN**; geen exact pad bewezen |
| Prijs | Inkoop-, verkoop-, adviesprijs-, BTW- en valutabron | Commerciele velden zijn vereist maar ontbreken lokaal | `BC-DATA-001`, `BC-PROD-001`, `BC-PRICE-001` | Masterplan/themeprijsvelden | **ONTBREEKT LOKAAL** |
| Voorraad/levertijd | Leverancierfeed, semantiek en updatefrequentie | Huidige asset heeft alleen `available`; PDP heeft vaste tekst | `BC-LOG-001`, `BC-PROD-001` | Masterplan en themecode | **ONTBREEKT LOKAAL** |
| Media/documenten | Bronlijst, rechten, URL's/bestanden en mapping | Theme verwacht media; lokale leveranciersmedia ontbreken | `BC-DATA-001`, `BC-PROD-001` | Themecode en masterplan | **ONTBREEKT LOKAAL** |
| Tegel-/eenheidsdata | m2/doos, stuks/doos, verpakking, pallet en afrondingsregels | Nodig voor The Mosaic Factory en calculator | `BC-TILE-001`, `BC-PROD-001`, `BC-LOG-001` | Masterplan en Adminvendorbewijs | **ONTBREEKT LOKAAL** |
| Overige toekomstige leveranciers | Bronnenlijst en exports | Doel circa 20.000 versus 7.827 bestaande producten | `BC-DATA-001`, `BC-PROD-001`, `BC-LOG-001` | Masterplan versus Adminrapport | **NOG ONDERZOEKEN**, namen onbekend |

## 21. Bronhouders en eigenaarschap

| Domein | Status | Wat nog nodig is |
| --- | --- | --- |
| Hotbath oorspronkelijke data | **ONBEKEND** | Naam/rol eigenaar, overdrachtsroute, contractuele bron, updatefrequentie |
| The Mosaic Factory oorspronkelijke data | **ONBEKEND** | Naam/rol eigenaar, export/feed, eenheden en updatefrequentie |
| Switcherasset | **ONBEKEND** | Technisch eigenaar, generatorlocatie, inputbron, runbook en validatie |
| Shopify-importproces | **ONBEKEND** | Uitvoerder, tooling, loglocatie, batch-/rollbackprocedure |
| Prijs | **ONBEKEND** | Commercieel eigenaar en bron per prijssoort |
| Voorraad/levertijd | **ONBEKEND** | Operationeel eigenaar, bronsemantiek en servicelevels |
| Media/documenten | **ONBEKEND** | Rechtenhouder, kwaliteits- en publicatieregels |
| Velddefinities/metafields | **NOG ONDERZOEKEN** | Productdata-eigenaar en formele datadictionary |

De Git-auteur van de initiële theme-import is niet als een van deze eigenaars aangemerkt.

## 22. Gevolgen voor BC-DATA-001

- `BC-DATA-001` blijft `BLOCKED`.
- Er kan een eisenlijst worden onderhouden, maar geen definitieve Shopifymapping worden vastgesteld zonder echte bronheaders, datatypes, eenheden, voorbeelden en dekking.
- De 58 statische themevelden mogen niet automatisch tot definitief datamodel worden verheven.
- De 30 V2-optionkeys zijn een afgeleide Hotbath-selectie en geen leverancierbrede taxonomie.
- Handle is bruikbaar voor een latere vergelijking, maar is alleen bewezen uniek binnen de huidige asset.
- SKU is op Adminniveau niet uniek en EAN/leveranciersartikelnummer zijn lokaal niet beschikbaar.

## 23. Gevolgen voor BC-LOG-001

- Er is geen lokale voorraad- of levertijdbron per leverancier.
- `available` kan niet als voorraadhoeveelheid of levertermijn worden gebruikt.
- De vaste PDP-tekst `8 - 9 weken` heeft geen lokaal bewezen bron en vormt een direct klantbelofterisico.
- Leverancierregels, cutoff, dropshipping, backorder, locatievoorraad, uitzonderingen en updatefrequentie blijven **NOG ONDERZOEKEN**.

## 24. Gevolgen voor BC-PROD-001

- Een schaalbare import voor circa 20.000 producten kan niet worden ontworpen op basis van alleen 3.383 Hotbath-switcherhandles.
- Voor iedere bron zijn eerst recordaantal, identifiers, prijs, media, voorraad, specificaties, relaties, SEO en kwaliteitsdrempels nodig.
- De bestaande 17 lege SKU's, dubbele SKU-groepen en niet-genormaliseerde producttypes vereisen bronvergelijking voordat correctie of opschaling wordt overwogen.
- Er is geen lokaal importlog, batchbewijs, mappingversie of rollbackproces.

## 25. Gevolgen voor BC-SWITCH-001 en BC-TILE-001

### BC-SWITCH-001

- De actuele asset is intern consistent voor handles, URL's en optiecombinaties.
- Volledige dekking tegenover 3.658 `switch_group`-producten is niet bewezen.
- Generator, bronhouder, input en schema-/kwaliteitsgate ontbreken.
- V2 `kleur` en legacy `basiskleur` vereisen later een expliciet mapping-/architectuurbesluit.
- Backups zijn geen verwijdertoestemming; bewaarbeleid blijft **OPEN BESLISSING**.

### BC-TILE-001

- The Mosaic Factory is alleen als vendor/productgroep in bestaand Admin-bewijs aanwezig.
- Geen tegelbron, eenheid, doosinhoud, palletdata, snijverlies- of afrondingsregel is lokaal aanwezig.
- Generieke Shopify unit-pricepresentatie is geen tegelcalculatorbron.
- De taak blijft geblokkeerd tot feitelijke tegeldata en bedrijfsregels zijn aangeleverd.

## 26. Open vragen

1. **NOG ONDERZOEKEN:** wie is bronhouder voor Hotbath en The Mosaic Factory, en via welke route worden actuele exports geleverd?
2. **NOG ONDERZOEKEN:** bestaan leveranciersbestanden, generators, mappings of importlogs buiten `CITY_MASTER`?
3. **NOG ONDERZOEKEN:** hoe is `assets/product-switcher-data.json` gegenereerd en welke snapshot/input lag eraan ten grondslag?
4. **NOG ONDERZOEKEN:** waarom hebben 3.658 producten een V2-trigger terwijl de asset 3.383 unieke handles heeft?
5. **NOG ONDERZOEKEN:** welke sleutel is bronoverstijgend betrouwbaar: SKU, EAN, leverancierartikelnummer, handle of een samengestelde sleutel?
6. **NOG ONDERZOEKEN:** welke prijssoorten, BTW-/valutaregels, voorraadbetekenissen en levertijdregels gelden per leverancier?
7. **NOG ONDERZOEKEN:** waar staan media, handleidingen, datasheets en gebruiksrechten?
8. **NOG ONDERZOEKEN:** welke tegelvelden en eenheden levert The Mosaic Factory?
9. **OPEN BESLISSING:** welke bron wordt later per veld gezaghebbend en wie keurt mapping en kwaliteit goed?
10. **OPEN BESLISSING:** welk bewaarbeleid geldt later voor QA-/backupassets? Dit rapport geeft geen verwijdertoestemming.

## 27. Risico's

| Risico | Impact | Beheersing |
| --- | --- | --- |
| Afgeleid themebestand wordt als leverancierbron behandeld | Onjuiste types/mapping en niet-reproduceerbare import | Bronprovenance verplicht voor ontwerp |
| Ontbrekende bronhouder | Verouderde data en onduidelijke correctieverantwoordelijkheid | Menselijke eigenaar per bron/veld aanwijzen |
| Onbekende generator | Asset en Shopify-triggerdata lopen uiteen | Generator/input/runbook aanleveren en read-only vergelijken |
| Niet-unieke of ontbrekende SKU | Verkeerde productkoppeling/import | Bronidentifieranalyse per leverancier |
| Geen EAN/artikelnummerwaarden lokaal | Koppeling tussen bronnen niet bewijsbaar | Werkelijke exports aanleveren |
| Alle asset-availability `true` | Verkeerde voorraad-/leverbelofte | Niet als logistieke bron gebruiken |
| Vaste PDP-levertijd | Onjuiste klantinformatie | In `BC-LOG-001` bron en regels besluiten voor enige wijziging |
| Ontbrekende prijsbron | Marge-, BTW- en adviesprijsfouten | Commerciele bron en eigenaar vastleggen |
| Ontbrekende tegel-/eenheidsdata | Verkeerde hoeveelheid en prijs | `BC-TILE-001` geblokkeerd houden |
| Backup-/QA-divergentie | Onbedoeld verkeerde dataset kiezen | Later gecontroleerd bewaarbeleid en versieproces besluiten |

## 28. Aanbevolen volgende stap

1. De projecteigenaar beoordeelt dit rapport en bevestigt of de lokale inventaris compleet is.
2. Lever daarna, zonder import uit te voeren, de actuele oorspronkelijke Hotbath- en The Mosaic Factory-bronnen aan binnen een expliciet goedgekeurde locatie en met bronhouder/snapshotdatum.
3. Lever de locatie of kopie van de switchergenerator, mapping, validatieregels en laatste import-/runbewijs aan als die extern bestaan.
4. Voeg per bron een menselijke eigenaar, updatefrequentie en betekenis voor prijs, voorraad, levertijd, media en eenheden toe.
5. Plan pas daarna een kleine vervolgopdracht voor read-only bronvergelijking. `BC-DATA-001` blijft tot menselijke review en aanvullende input `BLOCKED`.

Deze aanbeveling beschrijft de ontbrekende broninput voor latere brongebonden taken. De menselijke goedkeuring hieronder staat uitsluitend toe dat een afzonderlijk brononafhankelijk productinformatiecontract wordt voorbereid; er is geen implementatietoestemming verleend.

## 29. Menselijke goedkeuring

De BadkamerCity-projecteigenaar heeft dit rapport op 2026-08-10 menselijk beoordeeld en `BC-DATA-002` goedgekeurd als afgeronde lokale read-only leveranciersbronneninventarisatie.

De goedkeuring bevestigt uitsluitend:

- de lokale inventaris is binnen de toegestane scope compleet;
- nul oorspronkelijke lokale leveranciersbronnen is een geaccepteerde onderzoeksbevinding en geen mislukking van de taak;
- deze bevinding bewijst niet dat externe leveranciersbestanden niet bestaan;
- externe Hotbath-, The Mosaic Factory- en overige leveranciersbestanden worden later per leverancier afzonderlijk aangeleverd en beoordeeld;
- er wordt nu geen extra tijd besteed aan het zoeken naar bestanden die niet in `CITY_MASTER` aanwezig zijn;
- `BC-DATA-002` mag naar `DONE`;
- ontbrekende externe bronnen, bronhouders en procesdocumentatie blijven open afhankelijkheden;
- `BC-DATA-001` blijft `BLOCKED` voor een definitief datamodel en een definitieve Shopify-mapping.

Deze goedkeuring verandert geen inhoudelijke telling of conclusie in het rapport. Alle bewijsgrenzen, risico's, open vragen en ontbrekende input blijven gelden. Zij geeft geen toestemming voor Shopify-velden, leveranciermappings, imports, bronacceptatie, productdatacorrecties, theme- of codewijzigingen of implementatie.
