# BadkamerCity Theme Check-baseline

## 1. Documentstatus

| Veld | Waarde |
| --- | --- |
| Status | `DONE` - technisch uitgevoerd en menselijk goedgekeurd |
| Masterplanstatus | `ACTIVE FOR DISCOVERY - IMPLEMENTATION BLOCKED` |
| Baseline reproduceerbaar | **JA**, binnen de twee lokale runs en de hieronder vastgelegde grenzen |
| Theme-code gewijzigd | **NEE** |
| Menselijk goedgekeurd | 2026-08-12 |

## 2. Taak en datum

- Taak: `BC-TECH-003` - Reproduceerbare Theme Check- en kwaliteitsbasis vastleggen.
- Uitvoeringsdatum: 2026-08-12.
- Basiscommit: `be0d48c27b55b348a0a3d0e69fcfb51f0346831c` op `main` en `origin/main`.
- Fase-A-commitbericht: `docs: prepare reproducible theme check baseline`.
- Fase B is niet gecommit of gepusht.

## 3. Doel

Deze baseline legt een vaste, lokale en niet-mutatieve Theme Check-route vast. Toekomstige technische taken kunnen dezelfde snapshot, configuratie en wrapper gebruiken om nieuwe of uitgebreidere offenses als regressiesignaal te herkennen.

## 4. Veiligheidsgrenzen

- Geen Shopify Admin-, store- of themebenadering.
- Geen theme-push, pull, publicatie, preview of dev-server.
- Geen package- of Shopify CLI-installatie/update.
- Geen Liquid-, JavaScript-, CSS-, JSON/JSONC-, locale-, template- of sectionwijziging.
- Geen offense opgelost, suppressed, genegeerd of in severity verlaagd.
- Volledige tooluitvoer staat uitsluitend als raw evidence in de lokale Codex-run.

## 5. Goedgekeurde CLI-baseline

De projectbaseline is Shopify CLI `4.6.1`. Dit is een reproduceerbaarheidskeuze en geen claim dat `4.6.1` de nieuwste beschikbare versie is. De versie is uitsluitend gecontroleerd met:

```text
shopify version
```

De gemeten semantische versie was exact `4.6.1`. `shopify theme check -v` is niet gebruikt.

## 6. Configuratie

Repositorybestand `.theme-check.yml` bevat exact:

```yaml
extends: theme-check:recommended
```

- SHA-256: `80253e6172bbbff9b0666ed1e561e3efe97838739f85f606e4e1bd18e5440db3`.
- UTF-8 zonder BOM.
- Geen ignorelijst, disabled checks, severityoverride of andere suppressie.
- Beide volledige runs accepteerden de configuratie.

## 7. Wrapper

`scripts/run-theme-check.ps1`:

- ondersteunt Windows PowerShell 5.1 en parseert zonder fouten;
- bepaalt de repositoryroot vanuit `$PSScriptRoot`;
- vereist de aanwezige `.theme-check.yml`;
- voert eerst uitsluitend `shopify version` uit en vereist exact `4.6.1`;
- installeert of update niets;
- schrijft geen repository- of reportbestand;
- voert na de guard alleen het voorgeschreven lokale Theme Check-commando uit;
- laat Theme Check-stdout/stderr door en retourneert de Theme Check-exitcode.

Wrapper SHA-256: `b8c4496ed99485f36d14f0f16129b7eefd663e3c8b46852ed5d6e85f1d055fc6`.

## 8. Exacte baselinecommand

Normale aanroep vanuit de repositoryroot:

```powershell
& .\scripts\run-theme-check.ps1
```

De wrapper voert na de versieguard exact uit:

```text
shopify theme check --path <repo-root> --no-color --output json
```

`<repo-root>` wordt runtime als absoluut lokaal repositorypad ingevuld en wordt niet in fingerprints opgenomen.

## 9. Exitcodesemantiek

| Exitcode | Betekenis binnen deze baseline |
| ---: | --- |
| `0` | Theme Check voltooide zonder offenses. |
| `1` | Theme Check voltooide normaal en rapporteerde offenses; dit is de actuele baseline-uitkomst. |
| Anders | Toolingfailure of guardfailure; niet als groene code-uitkomst behandelen. |

De wrapper geeft de Theme Check-exitcode ongewijzigd terug. Een versie-, versieparse- of ontbrekende-configfout stopt vóór Theme Check met een niet-nulcode.

## 10. Run 1

| Veld | Waarde |
| --- | --- |
| Codex-step | `050` |
| Shopify CLI | `4.6.1` |
| Config SHA-256 | `80253e6172bbbff9b0666ed1e561e3efe97838739f85f606e4e1bd18e5440db3` |
| Wrapper SHA-256 | `b8c4496ed99485f36d14f0f16129b7eefd663e3c8b46852ed5d6e85f1d055fc6` |
| Basiscommit | `be0d48c27b55b348a0a3d0e69fcfb51f0346831c` |
| Exacte aanroep | `& .\scripts\run-theme-check.ps1` |
| Exitcode | `1` |
| Offenses | `19` |
| Errors / warnings / info | `3 / 16 / 0` |
| Betrokken bestanden | `15` |
| Raw JSON SHA-256 | `e124b30dd16f97c9dcfed6a60901e65997f23d79801d4922e1369f8700da10ec` |
| Fingerprintset SHA-256 | `79b76ec4226df18c7cc68aca755ade5878a0b4bfab767f376b53d265794fe959` |

## 11. Run 2

| Veld | Waarde |
| --- | --- |
| Codex-step | `057` |
| Shopify CLI | `4.6.1` |
| Config SHA-256 | `80253e6172bbbff9b0666ed1e561e3efe97838739f85f606e4e1bd18e5440db3` |
| Wrapper SHA-256 | `b8c4496ed99485f36d14f0f16129b7eefd663e3c8b46852ed5d6e85f1d055fc6` |
| Basiscommit | `be0d48c27b55b348a0a3d0e69fcfb51f0346831c` |
| Exacte aanroep | `& .\scripts\run-theme-check.ps1` |
| Exitcode | `1` |
| Offenses | `19` |
| Errors / warnings / info | `3 / 16 / 0` |
| Betrokken bestanden | `15` |
| Raw JSON SHA-256 | `e124b30dd16f97c9dcfed6a60901e65997f23d79801d4922e1369f8700da10ec` |
| Fingerprintset SHA-256 | `79b76ec4226df18c7cc68aca755ade5878a0b4bfab767f376b53d265794fe959` |

## 12. Eventuele run 3

Niet uitgevoerd. Run 1 en run 2 waren gelijk voor exitcode, command, werkmap, offensecount, bestandcount, severitycounts, fingerprintset en raw JSON-hash. De opdracht stond een derde volledige run alleen bij inhoudelijk verschil toe.

## 13. Reproduceerbaarheidsvergelijking

| Maat | Run 1 versus run 2 |
| --- | --- |
| Exitcode | Gelijk (`1`) |
| Offenses | Gelijk (`19`) |
| Bestanden | Gelijk (`15`) |
| Errors/warnings/info | Gelijk (`3/16/0`) |
| Fingerprintset | Exact gelijk; 0 alleen in run 1 en 0 alleen in run 2 |
| Fingerprintset SHA-256 | Exact gelijk |
| Raw JSON SHA-256 | Exact gelijk |

Conclusie: **reproduceerbaar JA** voor deze lokale repositorysnapshot, CLI `4.6.1`, config en wrapper. Dit bewijst geen stabiliteit over een CLI-, regels-, netwerk- of repositorywijziging.

## 14. Historische vergelijking

`docs/TECHNICAL_STABILIZATION_PLAN.md` registreert als historische referentie één volledige run met CLI `4.6.0`: 19 offenses in 15 bestanden, 3 errors en 16 warnings. De actuele meting met CLI `4.6.1` en expliciete aanbevolen config heeft exact dezelfde totalen.

De historische referentie bevat geen genormaliseerde fingerprintset die mechanisch met deze nieuwe set kan worden vergeleken. Daarom is de verantwoorde uitspraak:

- countdelta: `0` offenses, `0` bestanden, `0` errors en `0` warnings;
- aantoonbaar nieuwe fingerprints versus historisch bewijs: **niet bepaalbaar**;
- er is geen tellingbewijs voor nieuwe offenses, maar ook geen geldige basis om `0` nieuwe historische fingerprints te claimen.

## 15. Actuele offense-samenvatting

| Check/rule | Aantal | Severity |
| --- | ---: | --- |
| `ValidJSON` | 1 | error |
| `ValidSchemaTranslations` | 2 | error |
| `OrphanedSnippet` | 5 | warning |
| `UndefinedObject` | 4 | warning |
| `UnusedAssign` | 3 | warning |
| `DeprecatedFilter` | 2 | warning |
| `VariableName` | 2 | warning |
| **Totaal** | **19** | **3 errors / 16 warnings** |

Classificatie: 18 lokale offenses zijn `EXISTING_CODE_BASELINE; NEEDS_SEPARATE_FIX_TASK`. Eén `ValidJSON`-offense is `TOOLING_OR_EXTERNAL; NEEDS_SEPARATE_FIX_TASK`, omdat de actuele message concreet een mislukte parse van een remote Shopify GitHub-schema-URL noemt. Er zijn 0 actuele `CONFIGURATION`-offenses en 0 actuele `NOT_REPRODUCED`-offenses.

## 16. Volledige compacte offense-matrix

Regel `0` betekent dat Theme Check voor die offense geen concrete bronregel gaf.

| Fingerprint | Severity | Check/rule | Bestand | Regel | Classificatie | Compacte omschrijving | Bestaande kandidaat/issue | Aparte fix nodig |
| --- | --- | --- | --- | ---: | --- | --- | --- | --- |
| `6ee1a3b7855bc0777ff583df269dee2336af1c4f1168ec977dbcfa0b20bcf809` | error | `ValidJSON` | `config/settings_schema.json` | 0 | `TOOLING_OR_EXTERNAL; NEEDS_SEPARATE_FIX_TASK` | Remote Shopify-schema kon niet worden geparseerd; URL staat in actuele output. | `TS-013`, `BC-R-030` | Ja, toolingonderzoek/rebaseline; geen codefix hier |
| `4439b079de6b15e60df5fda598e898f6cb1774832718d0b3be5ff7c0f68c6b5b` | warning | `UndefinedObject` | `layout/password.liquid` | 39 | `EXISTING_CODE_BASELINE; NEEDS_SEPARATE_FIX_TASK` | `scheme_classes` is onbekend. | `BC-R-006` / audit | Ja |
| `b23f6507e5c209df91984fcc819bef3f5b217a7a17074675c41969075508a7bd` | warning | `UndefinedObject` | `layout/theme.liquid` | 57 | `EXISTING_CODE_BASELINE; NEEDS_SEPARATE_FIX_TASK` | `scheme_classes` is onbekend. | `BC-R-006` / audit | Ja |
| `a9fe9878e21d332f3f7bd868a7544e531aa6dd9722c932c009d343dbdf0aa30c` | warning | `UnusedAssign` | `sections/featured-product.liquid` | 489 | `EXISTING_CODE_BASELINE; NEEDS_SEPARATE_FIX_TASK` | `seo_media` wordt toegewezen maar niet gebruikt. | `BC-R-006` / audit | Ja |
| `060fc561fb6a85e00f1b30c98fb0d9ff92470284404cabd23e752e49c589c79a` | error | `ValidSchemaTranslations` | `sections/featured-product.liquid` | 742 | `EXISTING_CODE_BASELINE; NEEDS_SEPARATE_FIX_TASK` | Labelkey mist in `en.default.schema.json`. | `BC-R-006` / audit | Ja |
| `f30e09008e1f83ef861c1d23ae6cffa11a570371ad9f6b3563eda7030fcef564` | error | `ValidSchemaTranslations` | `sections/featured-product.liquid` | 743 | `EXISTING_CODE_BASELINE; NEEDS_SEPARATE_FIX_TASK` | Infokey mist in `en.default.schema.json`. | `BC-R-006` / audit | Ja |
| `85fa5151df44fe0f39209b6eb4bde907de85ac68b2b0ee18aac241e5233f24bb` | warning | `VariableName` | `sections/main-article.liquid` | 101 | `EXISTING_CODE_BASELINE; NEEDS_SEPARATE_FIX_TASK` | `anchorId` gebruikt niet-toegestaan naamformaat. | `BC-R-006` / audit | Ja |
| `ff62ee04cb97966d56021d159126d8a0cd3988aa40f57380ab855d45f42df6d7` | warning | `VariableName` | `sections/main-list-collections.liquid` | 19 | `EXISTING_CODE_BASELINE; NEEDS_SEPARATE_FIX_TASK` | `moduloResult` gebruikt niet-toegestaan naamformaat. | `BC-R-006` / audit | Ja |
| `386fffbcd646a3a50e172ce490d7e99236e81e234ca5b7f58c4b1efaaf17cf68` | warning | `UndefinedObject` | `sections/main-product.liquid` | 1319 | `EXISTING_CODE_BASELINE; NEEDS_SEPARATE_FIX_TASK` | `continue` wordt als onbekend object gemeld. | `TS-003`, `BC-R-006` | Ja |
| `abe17abf892705ed97405dc500dd1dbac73593141abf62745a0cb0b26d388f54` | warning | `UnusedAssign` | `sections/main-product.liquid` | 1623 | `EXISTING_CODE_BASELINE; NEEDS_SEPARATE_FIX_TASK` | `seo_media` wordt toegewezen maar niet gebruikt. | `TS-003`, `BC-R-006` | Ja |
| `fb34a08bc8a7c04187c4a23a11e426b5b63de330d800d49cdb69b2480ed9817c` | warning | `UnusedAssign` | `sections/main-search.liquid` | 744 | `EXISTING_CODE_BASELINE; NEEDS_SEPARATE_FIX_TASK` | `skip_card_product_styles` wordt niet gebruikt. | `BC-R-006` / audit | Ja |
| `54dfe166e5da9cb0a521b8537b1137f8939db08ec0d2ba57c98f068ab33c0702` | warning | `UndefinedObject` | `sections/product-media.liquid` | 2 | `EXISTING_CODE_BASELINE; NEEDS_SEPARATE_FIX_TASK` | `variant_images` is niet gedefinieerd. | `TS-008`, `PROPOSED-TECH-05` | Ja |
| `ba12c85594fb4b18c0d1e2c2d68e3dd70f6494961284d6f51a3ca87b16c9275a` | warning | `OrphanedSnippet` | `snippets/bc-product-short-specs.liquid` | 0 | `EXISTING_CODE_BASELINE; NEEDS_SEPARATE_FIX_TASK` | Snippet heeft geen gevonden referentie. | `TS-018`, `PROPOSED-TECH-05` | Ja |
| `d6a841d9ff84c6803a0482f89c702309cc4db057f474432b0426782028a8e795` | warning | `DeprecatedFilter` | `snippets/bc-product-spec-row.liquid` | 37 | `EXISTING_CODE_BASELINE; NEEDS_SEPARATE_FIX_TASK` | `img_tag` is deprecated. | `BC-R-006` / audit | Ja |
| `cea282d4f9ad4583f96f2f9bb936ce1d5f5619bad203cb98bcb1ac7be9d7b3ef` | warning | `DeprecatedFilter` | `snippets/bc-product-spec-row.liquid` | 39 | `EXISTING_CODE_BASELINE; NEEDS_SEPARATE_FIX_TASK` | `img_tag` is deprecated. | `BC-R-006` / audit | Ja |
| `98f79be956bd7cc8bc96e166a17306476340889364333006e32d4ff95a8a7f4b` | warning | `OrphanedSnippet` | `snippets/header-dropdown-menu.liquid` | 0 | `EXISTING_CODE_BASELINE; NEEDS_SEPARATE_FIX_TASK` | Snippet heeft geen gevonden referentie. | `TS-018`, `PROPOSED-TECH-05` | Ja |
| `a6cd7e529312b4ef9da26c07722c33f974f0aca1f0e986332a9429cdd8e2a08e` | warning | `OrphanedSnippet` | `snippets/header-mega-menu.liquid` | 0 | `EXISTING_CODE_BASELINE; NEEDS_SEPARATE_FIX_TASK` | Snippet heeft geen gevonden referentie. | `TS-018`, `PROPOSED-TECH-05` | Ja |
| `595f2d3dd18e7d9dbb00db425edf5640d6255af47386a76cdd2b4a5d0bf8743d` | warning | `OrphanedSnippet` | `snippets/product-pros-cons.liquid` | 0 | `EXISTING_CODE_BASELINE; NEEDS_SEPARATE_FIX_TASK` | Snippet heeft geen gevonden referentie. | `TS-018`, `PROPOSED-TECH-05` | Ja |
| `e038e1f7b24b1175e8219e8cd13d49b5d5faa9b83ab0f2ff134ee7054a91cfcf` | warning | `OrphanedSnippet` | `snippets/quick-order-product-row.liquid` | 0 | `EXISTING_CODE_BASELINE; NEEDS_SEPARATE_FIX_TASK` | Snippet heeft geen gevonden referentie. | `BC-R-006` / audit | Ja |

## 17. Fingerprintmethode

Per offense wordt de canonical string opgebouwd als:

```text
check|severity|repository-relatief-pad|start_row|sha256(genormaliseerde-message)
```

De offensefingerprint is SHA-256 van die UTF-8-string. De message wordt getrimd, whitespace wordt samengevouwen, backslashes worden genormaliseerd en een eventueel absoluut repositorypad wordt vervangen door `<repo>`. Absolute Windows-root, terminalkleur, runtime-timestamp en tijdelijke directories tellen dus niet mee. De fingerprintset-hash is SHA-256 van de lexicografisch gesorteerde fingerprints, met LF ertussen en zonder afsluitende LF.

## 18. Code versus tooling/externe meldingen

- **Lokale codebaseline:** 18 offenses. Deze staan in repositorybestanden en zijn als bestaande codebevindingen geregistreerd, niet inhoudelijk goedgekeurd.
- **Tooling/extern:** 1 offense. `ValidJSON` noemt concreet `https://raw.githubusercontent.com/Shopify/theme-liquid-docs/main/schemas/theme/setting.json` en een parsefout. Dit ondersteunt classificatie als remote-schema-/toolingafhankelijk voor deze runs.
- **Configuratie:** 0 offenses. De nieuwe minimale config werd geaccepteerd en onderdrukt niets.
- **Niet gereproduceerd:** geen actuele offense. De historische Windows assertion uit de oudere audit trad in deze twee runs niet op en is geen offensefingerprint.

Een externe melding wordt niet stil als codefout, onderdrukte waarschuwing of groen succes behandeld.

## 19. Nieuwe-offensebeleid

Voorstel ter menselijke review:

- Iedere nieuwe fingerprint ten opzichte van deze baseline is een regressiesignaal.
- Een bestaande offense die ernstiger wordt, een andere locatie/message krijgt of naar meer bestanden uitbreidt, is eveneens een regressiesignaal.
- De baseline mag nooit als argument dienen om nieuwe offenses te accepteren.
- Externe/toolingvariatie wordt apart onderzocht en blijft zichtbaar.

## 20. Bestaande-offensebeleid

`EXISTING_CODE_BASELINE` betekent uitsluitend dat de offense vóór een toekomstige codewijziging in deze snapshot bestond. Het betekent niet dat de code correct, acceptabel of goedgekeurd is. Bestaande offenses worden alleen in afzonderlijk toegestane fix-/reproductietaken behandeld. Deze taak heeft nul offenses opgelost.

## 21. Rebaselinebeleid

Een afzonderlijke expliciete menselijke rebaseline is verplicht bij wijziging van:

- Shopify CLI-versie;
- Theme Check-regelset of configuratie;
- suppressie-/severitybeleid;
- fingerprintmethode;
- baselinebeleid of bewuste acceptatiegrens.

Een rebaseline mag verschillen niet verbergen: oorzaak, oude en nieuwe sets, counts en menselijke beslissing moeten worden vastgelegd.

## 22. Gebruik in toekomstige technische taken

Zolang `4.6.1` de goedgekeurde basis is:

1. start vanaf de expliciet vastgelegde basiscommit;
2. gebruik ongewijzigd `.theme-check.yml` en `scripts/run-theme-check.ps1`;
3. vergelijk exitcode, counts en vooral de fingerprintset vóór en na de wijziging;
4. behandel nieuwe/uitgebreidere offenses als regressiesignaal;
5. los bestaande offenses alleen binnen een afzonderlijke taak op;
6. leg tooling-/externe variatie apart vast;
7. vraag expliciete menselijke goedkeuring voor suppressie of rebaseline.

## 23. Beperkingen

- Twee opeenvolgende runs bewijzen lokale reproduceerbaarheid op deze datum en snapshot, niet eeuwige of cross-platformstabiliteit.
- De remote-schema-offense kan door netwerk- of upstreaminhoud veranderen.
- Historisch zijn alleen totals en messagesamenvatting beschikbaar; geen vergelijkbare oude fingerprintset.
- Theme Check is een statische controle en bewijst geen storefrontruntime, toegankelijkheid, performance of functionele correctheid.
- De baseline keurt geen offense en geen kandidaatfix goed.

## 24. Open vragen

- Welke afzonderlijke lokale offenses krijgen later een officiële reproductie-/fixtaak en in welke volgorde?
- Welke expliciete toolingroute geldt als de remote Shopify-schema-offense verandert of verdwijnt?
- Wanneer mag een toekomstige CLI-/regelsetrebaseline worden aangevraagd?
- Retentietermijn en eigenaar van lokale one-bundle-runs blijven volgens het masterplan open.

## 25. Aanbevolen volgende stap

Gebruik deze goedgekeurde basis als verplichte statische pre-/postgate in iedere later afzonderlijk toegestane technische theme-codetaak. Los geen van de 19 offenses zonder een eigen officiële taak op en voer geen suppressie of rebaseline zonder afzonderlijke menselijke toestemming uit.

## 26. Veiligheidsbevestiging

Tijdens `BC-TECH-003` is Shopify niet benaderd, geen Admin- of themeactie uitgevoerd, niets geïnstalleerd/geüpdatet, geen preview gebruikt en geen theme-code gewijzigd. Alleen `.theme-check.yml`, `scripts/run-theme-check.ps1`, dit document en `docs/MASTERPLAN.md` zijn in fase B gewijzigd. Fase B is niet gecommit of gepusht.

## 27. Menselijke goedkeuring

De BadkamerCity-projecteigenaar heeft `BC-TECH-003` op 2026-08-12 expliciet goedgekeurd binnen de vastgelegde toolingbaseline-scope:

- Shopify CLI `4.6.1` is de goedgekeurde reproduceerbaarheidsbaseline, zonder claim dat dit de nieuwste versie is en zonder automatische of handmatige update binnen gewone taken.
- `extends: theme-check:recommended` zonder ignorelijst, disabled checks, severityverlaging of andere suppressie is goedgekeurd.
- `scripts/run-theme-check.ps1` is als projectwrapper goedgekeurd; versiecontrole blijft uitsluitend `shopify version`.
- Twee volledige runs waren binnen de gedocumenteerde lokale grenzen reproduceerbaar: 19 offenses in 15 bestanden, 3 errors, 16 warnings en 19 unieke fingerprints, met identieke exitcode, raw JSON-hash, counts en fingerprintset.
- De 19 offenses zijn een bestaande technische baseline en geen kwaliteitsacceptatie. De onderzoeks-/toolingclassificatie van 18 `EXISTING_CODE_BASELINE; NEEDS_SEPARATE_FIX_TASK` en 1 actuele `TOOLING_OR_EXTERNAL; NEEDS_SEPARATE_FIX_TASK` is geaccepteerd; geen offense is opgelost, onderdrukt of genegeerd.
- Nieuwe, uitgebreidere of ernstigere offenses zijn een regressiesignaal. Suppressie en wijziging van CLI, regelset, fingerprintmethode of baselinebeleid vereisen later afzonderlijke menselijke toestemming en een expliciete rebaseline.
- De niet-blokkerende samenvattingsafwijking in het eerdere `FINAL_REPORT.md` verloor geen raw bewijs: alle aanvullende finalisatie-/herstelstappen staan in `FULL_EXECUTION_LOG.md`, raw command evidence en de bijbehorende ERROR-/RECOVERY-notes. De technische conclusie blijft ongewijzigd.
- Voor toekomstige runs geldt operationeel: voer eerst alle normale project- en preflightchecks uit, ververs daarna `FINAL_REPORT.md` en start direct de finalizer. Bij finalizerfailure blijven fout en herstel behouden, wordt `FINAL_REPORT.md` opnieuw ververst en volgt pas daarna een nieuwe finalizerpoging.
- Shopify en theme-code zijn tijdens `BC-TECH-003` niet gewijzigd. Deze goedkeuring geeft geen toestemming om een offense op te lossen of enige Shopify-/themewijziging uit te voeren.
