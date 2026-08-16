# BadkamerCity test- en bewijsstandaard

> **DEZE STANDAARD IS GEEN TESTUITVOERING.**  
> Dit document heeft status `DONE`. Het legt uitsluitend lokale governance voor toekomstig testbewijs vast; het bevat geen runtime-, browser-, preview- of storefrontresultaat.

## 1. Documentstatus

`DONE` — inhoudelijk goedgekeurd door de BadkamerCity-projecteigenaar op 2026-08-16. Geen testcase is binnen `BC-TECH-006` uitgevoerd en geen resultaat is als functionele `PASS` vastgelegd.

## 2. Taak en datum

- Taak: `BC-TECH-006` — Test- en bewijsopslag standaardiseren.
- Datum: 2026-08-16.
- Projectstatus: `ACTIVE FOR DISCOVERY - IMPLEMENTATION BLOCKED`.
- Uitvoeringsvorm: uitsluitend lokale governance en documentatie.

## 3. Doel

Een compacte, herhaalbare en privacyveilige bewijsstandaard vastleggen waarmee een later werkelijk uitgevoerde testcase uniek herleidbaar wordt naar taak, run, testcase, fixture, basiscommit, omgeving, resultaat, bewijsbestanden en menselijke beoordeling.

## 4. Scope

De standaard omvat een ignored evidence-directory, resultaatrecords, een manifest, naamgeving, minimale metadata, bewijsbestands-hashes, resultaat- en oorzaaklabels, reviewerstatus, privacy- en mutatieclassificatie, proportionele L0/L1/L2-minima, retentiegrenzen en one-bundle-overdracht.

## 5. Buiten scope

Geen browser- of storefronttest, screenshot, runtime-/browserlog, netwerkcapture, metricmeting, preview, Shopify-query, cartstate, login, formulier, checkout, package-installatie, CI, cloud-/artifactserverkeuze, grote binarycommit, theme-codewijziging of defectoplossing. Deze taak kiest geen runtimeframework en stelt geen performancebudget vast.

## 6. Bronnen

- `docs/SMOKE_REGRESSION_BASELINE.md`: goedgekeurde routes, fixtures, test-ID's, L0/L1/L2, resultaat-/oorzaaklabels en mutatiegrenzen.
- `docs/TECHNICAL_CHANGE_WORKFLOW.md`: basiscommit, branches, gates A-G, previewtargetcontrole, merge- en rollbackgrenzen.
- `docs/CODEX_EXECUTION_LOG_PROTOCOL.md`: runmap, raw commandbewijs, privacy, reviewbestanden en one-bundle-retentie.
- `docs/THEME_CHECK_BASELINE.md`: statische kwaliteitsbasis en fingerprintdelta.
- `scripts/codex-run-finalize.ps1`: in deze taak uitsluitend read-only beoordeeld op recursieve bundle-opname.
- `docs/MASTERPLAN.md`: taakstatus, besluiten, afhankelijkheden, risico's en bewijsregister.

## 7. Kernprincipes

1. Een bewijsset hoort bij exact één officiële taak en één Codex-run.
2. `PASS` is alleen toegestaan na werkelijke, geautoriseerde uitvoering en compleet vereist bewijs.
3. Technische teststatus en menselijke reviewstatus zijn afzonderlijke velden.
4. Bewijs is minimaal en impactgericht; niet iedere case vereist screenshots, netwerkdata of metrics.
5. Secrets en verboden inhoud worden nooit opgeslagen, gecommit of gebundeld.
6. Hashes bewijzen byte-identiteit, niet inhoudelijke juistheid.
7. Een oude of onvolledige bewijsset wordt niet stil als nieuwe baseline gebruikt.

## 8. Evidence-directory

Toekomstige geautoriseerde testtaken gebruiken standaard:

```text
docs/_codex_runs/<RUN_ID>/evidence/
  TEST_EVIDENCE_MANIFEST.md
  results/
  screenshots/
  logs/
  metrics/
```

Het pad is lokaal, valt onder de bestaande Git-ignore, hoort bij één run en wordt niet automatisch tracked. Subdirectories worden alleen gemaakt wanneer het betreffende toegestane bewijs werkelijk bestaat. `BC-TECH-006` maakt deze directories en artefacten zelf niet aan.

## 9. Resultaatrecords

De vaste standaard is één UTF-8-Markdownbestand per daadwerkelijk opgenomen testcase:

```text
evidence/results/<TEST_ID>.md
```

Markdown is gekozen omdat het zonder extra package zowel mens- als eenvoudig machineleesbaar is, goed reviewbaar blijft en aansluit op het bestaande logprotocol. Eén record per test-ID voorkomt ambiguïteit; een heruitvoering krijgt een nieuwe run-ID, niet een overschreven record.

Ieder record bevat minimaal: taak-ID, Run-ID, testcase-ID, fixture-ID, basiscommit, actuele branch, wijzigingscommit indien van toepassing, route/component, datum/tijd met timezone, testlaag, viewport, browser/tool, toolversie, inputmethode, mutatieclassificatie, verwachte uitkomst, feitelijke uitkomst, resultaat, oorzaaklabel indien relevant, bewijsbestanden, hun SHA-256, reviewerstatus en opmerkingen/restrisico.

## 10. TEST_EVIDENCE_MANIFEST

`evidence/TEST_EVIDENCE_MANIFEST.md` is de index van de bewijsset. De kop bevat taak-ID, Run-ID, basiscommit, branch, testomgeving, datum/tijd met timezone, aantallen `PASS`, `FAIL`, `BLOCKED`, `NOT_RUN`, `NOT_APPLICABLE`, totaal, ontbrekend bewijs en manifeststatus.

Per testcase bevat de tabel minimaal: testcase-ID, fixture-ID, resultaatstatus, pad naar resultaatrecord, bewijsbestanden, SHA-256, bytes, privacyclassificatie, mutatieclassificatie en reviewerstatus. Een manifest mag nooit `PASS` claimen wanneer het resultaatrecord of vereist bewijs ontbreekt. Totalen worden uit de testcase-rijen afgeleid en moeten sluitend zijn.

## 11. Resultaatstatussen

| Status | Betekenis |
| --- | --- |
| `PASS` | Werkelijk uitgevoerd; verwacht resultaat gehaald en alle verplichte bewijsvelden/bestanden compleet. |
| `FAIL` | Werkelijk uitgevoerd; verwacht resultaat niet gehaald of verplichte gate faalt. |
| `BLOCKED` | Uitvoering kon niet verantwoord worden voltooid door een aantoonbare blokkade. |
| `NOT_RUN` | Niet uitgevoerd; nooit gelijk aan `PASS`. |
| `NOT_APPLICABLE` | Voor deze expliciete scope niet van toepassing, met gemotiveerde reden. |

Een onbekende fixture, verkeerde basiscommit, ontbrekend bewijs of mislukte privacycontrole kan nooit `PASS` zijn.

## 12. Oorzaaklabels

Waar relevant gebruikt het record één of meer vaste technische oorzaaklabels: `REGRESSION`, `PRE_EXISTING`, `TOOLING_FAILURE`, `FIXTURE_INVALID`, `ENVIRONMENT_MISMATCH` en `NEEDS_HUMAN_REVIEW`. `PRE_EXISTING` vereist gedateerd basisbewijs; een onverwachte afwijking wordt nooit stil als baseline geaccepteerd.

## 13. Reviewerstatus

Technische teststatus wordt gescheiden van menselijke review:

- `UNREVIEWED`
- `REVIEWED_ACCEPTED`
- `REVIEWED_REJECTED`
- `REVIEW_BLOCKED`

Een technische `PASS` is niet automatisch menselijke acceptatie. Menselijke acceptatie is niet automatisch toestemming voor preview, merge, release of een latere gate.

## 14. Screenshotbeleid

Screenshots zijn alleen toegestaan wanneer een toekomstige officiële taak ze expliciet toestaat. Standaardpad en naamgeving:

```text
evidence/screenshots/<TEST_ID>__<VIEWPORT>__<STATE>__NN.png
```

Gebruik de minimaal relevante uitsnede wanneer componentbewijs volstaat; leg geen volledige desktop vast zonder noodzaak. Geen persoonsgegevens, account-/orderdata, tokens of developer panels met gevoelige headers. Een veilig origineel blijft naast een afgeleide crop bewaard en beide bestanden krijgen een afzonderlijke hash; de crop krijgt een onderscheidende `STATE` of volgnummer. Een origineel met verboden inhoud geldt niet als sanitiseerbaar bewijs: het wordt niet gecommit of gebundeld en vereist menselijke incident-/verwijderbeslissing. `BC-TECH-006` maakt geen screenshot.

## 15. Logbeleid

Toekomstige runtime-/browserlogs zijn alleen toegestaan binnen expliciete taakscope en staan onder `evidence/logs/`. Bewaar uitsluitend relevante console errors/warnings, parserresultaten en taakgerichte testuitvoer. Cookies, authorization headers, session tokens, credentialstores, klant-/accountdata en volledige onnodige dumps zijn verboden. Logbestanden worden vóór hashing en bundeling privacygericht beoordeeld.

## 16. Netwerkbewijs

Een volledige HAR is standaard niet toegestaan omdat headers, cookies, queryparameters en bodies gevoelige inhoud kunnen bevatten. Wanneer later netwerkbewijs noodzakelijk en toegestaan is, worden alleen minimale requestmetadata, status, methode, host-/padgrens en relevante timing of responsclassificatie vastgelegd, met redactie vóór opslag. Secrets, payloads met persoonsgegevens en sessiegegevens blijven uitgesloten.

## 17. Metrics

Metrics staan alleen onder `evidence/metrics/` wanneer een geautoriseerde testcase ze vereist. Metadata bevat route, testcase-ID, fixture-ID, basiscommit, viewport, tool/versie, cold/warm-state, datum/tijd, eenheid, gemeten waarde en uitsluitend een vooraf menselijk goedgekeurde interpretatiegrens. Deze taak voegt geen budget, Core Web Vitals-doel of millisecondennorm toe en maakt geen metricsbestand.

## 18. Privacyclassificatie

| Klasse | Beleid |
| --- | --- |
| `PUBLIC_STOREFRONT` | Standaard toegestaan wanneer taak en bewijssoort zijn geautoriseerd. |
| `INTERNAL_NON_PERSONAL` | Toegestaan wanneer minimaal nodig en niet gevoelig. |
| `PERSONAL_DATA` | Verboden zonder afzonderlijke expliciete privacy- én taaktoestemming. |
| `SECRET_OR_CREDENTIAL` | Nooit opslaan, committen of bundelen. |
| `PROHIBITED` | Nooit opslaan, committen of bundelen. |

Een onzeker bestand wordt niet gebundeld totdat een bevoegde menselijke review de classificatie heeft bepaald.

## 19. Verboden inhoud

Verboden zijn minimaal credentials, tokens, cookies, sessie-ID's, authorization headers, credentialstores, klantnamen, adressen, e-mailadressen, telefoonnummers, account-/orderhistorie, betaalgegevens, offerteuploads en onnodige request-/responsebodies. Verborgen interne redeneerstappen worden evenmin vastgelegd. Een bestandsnaam of hash maakt verboden inhoud niet toegestaan.

Wanneer tijdens een toekomstige bewijsopname onverwacht een artefact ontstaat met credentials, tokens, cookies, session identifiers, Authorization headers, klant-/order-/accountdata, andere verboden persoonsgegevens of andere `PROHIBITED` inhoud, is dat artefact geen geldig bewijs. Het mag niet als pending review onder `evidence/` blijven staan, niet voor normaal evidencegebruik worden gehasht, niet naar `review_files/` worden gekopieerd en niet in de finale runbundle terechtkomen. Verwijder het binnen de veilige mogelijkheden van de taak onmiddellijk uit de evidence- en bundlestaging. Bewaar uitsluitend een veilige `ERROR`/`SECURITY_REDACTION`-note zonder de verboden waarde. Wanneer veilige verwijdering of classificatie niet zeker is, stopt de taak vóór finalisatie voor menselijke controle.

## 20. Git versus runartefact

Tracked projectdocumentatie kan bestaan uit testcaseontwerp, teststandaard, compacte menselijk goedgekeurde samenvatting en beleid/configuratie. Normaal niet tracked zijn screenshots, runtimeconsolelogs, netwerklogs, metricsrawdata, browserrecordings, tijdelijke fixtures, runspecifieke manifesten en testcase-resultaatrecords. Deze blijven standaard onder `docs/_codex_runs/<RUN_ID>/evidence/` en worden via one-bundle beoordeeld. Alleen een latere expliciete taak kan een compacte, privacyveilige samenvatting voor Git goedkeuren.

## 21. Naamgeving

| Type | Standaard |
| --- | --- |
| Resultaatrecord | `results/<TEST_ID>.md` |
| Screenshot | `screenshots/<TEST_ID>__<VIEWPORT>__<STATE>__NN.png` |
| Log | `logs/<TEST_ID>__<LOG_TYPE>__NN.log` |
| Metricset | `metrics/<TEST_ID>__<METRIC_SET>__NN.json` |

`TEST_ID`, viewport en state gebruiken alleen de vooraf vastgelegde identifier; `NN` begint bij `01`. Bestandsnamen bevatten geen producttitel, zoekterm, account, e-mail, ordernummer of andere mogelijk persoonlijke/vrije invoer.

## 22. Hashing en integriteit

Voor ieder evidencebestand legt het manifest relatief pad, bytes, SHA-256, bestandstype, testcase-ID en privacyclassificatie vast. Hash pas nadat het bestand is gesloten. Verandert een bestand na hashing, dan is het manifest ongeldig totdat bytes en SHA-256 opnieuw zijn berekend en de wijziging is beoordeeld. De manifesthash zelf wordt pas na definitieve inhoud berekend waar een latere taak dat vereist. Een hash bewijst alleen byte-identiteit.

## 23. Basiscommit en branch

Ieder resultaatrecord en manifest noemt de volledig uitgeschreven goedgekeurde basiscommit en de actuele branch. Een eventuele wijzigingscommit staat in een afzonderlijk veld. Afwijking van de toegestane basis/branch is minimaal `BLOCKED` of `FAIL` met `ENVIRONMENT_MISMATCH`; tests op de verkeerde target of basis worden niet als geldige regressiebasis gebruikt.

## 24. Fixture- en testcasekoppeling

Iedere uitgevoerde case verwijst naar één unieke `SMK-<DOMEIN>-NNN` en een vooraf gedefinieerde `FIX-*`-klasse of gemotiveerd `n.v.t.` voor een puur statische gate. Concrete fixtures worden direct vóór runtime read-only hervalideerd. Een onbekende, verouderde of niet-geautoriseerde fixture wordt `BLOCKED`/`FIXTURE_INVALID`, nooit stil vervangen of als `PASS` behandeld.

## 25. Viewport en inputmethode

Leg de gebruikte viewport-ID én exacte pixels vast, bijvoorbeeld een later geautoriseerde `VP-MOBILE`, `VP-DESKTOP` of gepaarde boundary-state. Noteer inputmethode zoals toetsenbord, muis/pointer of touch-emulatie. Een viewportvoorstel is geen browser-/apparaatsupportclaim; verkeerde of ontbrekende viewportmetadata maakt vereist responsive bewijs incompleet.

## 26. Tool- en versiegegevens

Noem toolnaam, exacte versie, uitvoeringsmodus en browser/engine waar van toepassing. Wanneer geen tool is gebruikt, noteer `n.v.t.` met reden. Toolinstallatie, update of frameworkkeuze vereist afzonderlijke toestemming. Toolingfailure krijgt `TOOLING_FAILURE` en wordt nooit als product-`PASS` geïnterpreteerd.

## 27. Mutatieclassificatie

Gebruik de goedgekeurde klassen `READ_ONLY`, `EPHEMERAL_STOREFRONT_STATE`, `WRITE_OR_TRANSACTIONAL` en `PERSONAL_DATA`. Een gewone GET, publieke search en switchernavigatie zijn read-only; add-to-cart en cart quantity zijn tijdelijke storefrontstate en vereisen aparte toestemming; formulierverzending en checkout/order zijn write/transactional; login en orderhistory raken persoonsgegevens. Het record noemt klasse en concrete autorisatiegrens.

## 28. Incomplete bewijs

Het manifest toont ontbrekende records, bestanden, hashes, fixturevalidatie of metadata expliciet. Een incomplete case is `BLOCKED`, `NOT_RUN` of `FAIL` volgens oorzaak en uitvoering; nooit `PASS`. Een manifest met niet-sluitende totalen, ontbrekende rij of hashmismatch heeft status `INCOMPLETE` of `INVALID` en kan geen acceptatiebasis zijn.

## 29. Failurebeleid

Een testcase mag niet `PASS` zijn wanneer vereist bewijs ontbreekt, de fixture ongeldig is, basiscommit/branch/viewport/target afwijkt, tooling faalt, de omgeving niet overeenkomt of privacycontrole faalt. Gebruik `FAIL`, `BLOCKED` of `NOT_RUN` met oorzaaklabel. Onverwachte afwijkingen blijven zichtbaar; herstel of heruitvoering overschrijft het eerste bewijs niet maar gebruikt een nieuw record/run.

## 30. Menselijke review

De reviewer controleert minimaal scope, target, recordvelden, verwachte versus feitelijke uitkomst, bewijsbestanden, hashes, privacyclassificatie, mutationklasse, oorzaaklabel en restrisico. De reviewer legt één reviewerstatus en datum vast zonder persoonsgegeven dat niet nodig is. Gates A-G uit de technical change workflow blijven apart; reviewacceptatie impliceert geen merge of release.

## 31. One-bundle-integratie

Een toekomstige runbundle met `evidence/` bevat minimaal normale runlogs, `FINAL_REPORT.md`, `review_files/`, de volledige toegestane `evidence/`-subtree en `TEST_EVIDENCE_MANIFEST.md`. De huidige finalizer is in `BC-TECH-006` read-only beoordeeld: zowel de verwachte entrylijst als `New-ZipSnapshot` gebruikt recursieve bestandsinventarisatie van de volledige runmap. Daardoor wordt een aanwezige evidence-subtree automatisch opgenomen en mechanisch tegen de ZIP-entries gecontroleerd. Geen finalizerwijziging is nodig of uitgevoerd.

Daarom geldt vóór iedere finalisatie van een toekomstige run met `evidence/` een verplichte taakspecifieke pre-bundle evidence gate. Voor ieder bestand onder `docs/_codex_runs/<RUN_ID>/evidence/` moet mechanisch bewezen zijn dat het bestand in `TEST_EVIDENCE_MANIFEST.md` staat of het manifest zelf is; testcase-ID en evidencerol bekend zijn; bytes en SHA-256 vastliggen; de privacyclassificatie toegestaan en zeker is; de classificatie niet `SECRET_OR_CREDENTIAL` of `PROHIBITED` is; het bestand bij de huidige Run-ID hoort; en het na hashing niet onverwacht is gewijzigd. Wanneer één bestand niet aan deze gate voldoet, is finalisatie `BLOCKED`. De centrale finalizer hoeft hiervoor binnen `BC-TECH-006` niet te worden gewijzigd.

## 32. Retentie

Interimbeleid: runspecifieke artefacten blijven lokaal en ignored totdat menselijke review is afgerond; automatische verwijdering is verboden; de gebruiker beslist over verwijdering; one-bundle kan als tijdelijke reviewoverdracht dienen. Permanente/langdurige bewaartermijn, formele eigenaar en eventuele cloud-/CI-opslag blijven `OPEN BESLISSING`. Dit wijzigt het bestaande Codex-runretentiebeleid niet.

## 33. Minimale evidence per L0

L0 vereist proportioneel: command-/test-ID, basiscommit, branch, tool/versie, exitcode, relevante output of fingerprintdelta, resultaatrecord en waar van toepassing raw commandbewijs. Een screenshot is niet verplicht voor een niet-visuele statische gate. Whitelist, parser/syntaxis, Theme Check en `git diff --check` volgen hun eigen vastgelegde outputeisen.

## 34. Minimale evidence per L1

L1 vereist testcase-record, hervalideerde fixture, route/component, viewport, inputmethode, verwachte en feitelijke uitkomst, resultaat, relevante fout-/console-informatie en reviewerstatus. Een screenshot is alleen verplicht wanneer de case werkelijk een visuele beoordeling vereist; niet-visuele functionele feiten gebruiken geschikter minimaal bewijs.

## 35. Minimale evidence per L2

L2 gebruikt dezelfde kern als L1 en voegt alleen impact-specifiek bewijs toe: bijvoorbeeld minimale netwerkmetadata, geparseerde structured data, toetsenbordstappen/focusstate, responsive boundarygegevens of metricsmetadata. Er is geen algemene verplichting om voor iedere L2-case alle bewijssoorten of een volledige-sitecapture te maken.

## 36. Voorbeeld testcase-record

Onderstaand voorbeeld is synthetisch en niet uitgevoerd:

```text
Voorbeeldmarker: EXAMPLE_ONLY
Taak-ID: BC-EXAMPLE-000
Run-ID: BC-EXAMPLE-000_20990101-000000
Testcase-ID: SMK-PDP-001
Fixture-ID: FIX-PDP-V2
Basiscommit: <FULL_SHA>
Branch: <APPROVED_BRANCH>
Route/component: productpagina / basisrender
Datum/tijd: 2099-01-01T00:00:00+01:00
Laag: L1
Viewport: VP-MOBILE / 375x812
Browser/tool: <OPEN BESLISSING>
Toolversie: n.v.t.
Inputmethode: n.v.t.
Mutatieclassificatie: READ_ONLY
Verwachte uitkomst: volgens SMK-PDP-001
Feitelijke uitkomst: niet vastgesteld
Resultaat: NOT_RUN
Oorzaaklabel: NEEDS_HUMAN_REVIEW
Bewijsbestanden: geen
SHA-256: n.v.t.
Reviewerstatus: UNREVIEWED
Restrisico: voorbeeld is geen runtimebewijs
```

## 37. Voorbeeld manifestregel

Synthetisch, niet uitgevoerd:

| Testcase-ID | Fixture | Status | Resultaatrecord | Bewijsbestanden | Hashes | Bytes | Privacy | Mutatie | Reviewer |
| --- | --- | --- | --- | --- | --- | ---: | --- | --- | --- |
| `SMK-PDP-001` | `FIX-PDP-V2` | `NOT_RUN` | `results/SMK-PDP-001.md` (voorbeeldpad) | geen | n.v.t. | 0 | `PUBLIC_STOREFRONT` | `READ_ONLY` | `UNREVIEWED` |

Deze rij is `EXAMPLE_ONLY`, geen werkelijk manifest of testresultaat.

## 38. Relatie met SMOKE_REGRESSION_BASELINE

De smoke-baseline bepaalt wat later proportioneel wordt getest: routes, fixtures, test-ID's, lagen, verwachte resultaten, failurelabels en change-impactgroepen. Deze standaard bepaalt alleen hoe geautoriseerde uitvoering wordt vastgelegd. Zij verandert geen testcase naar uitgevoerd en laat alle eerdere BC-TECH-005-runtimecases historisch `UNEXECUTED`.

## 39. Relatie met TECHNICAL_CHANGE_WORKFLOW

Basiscommit, branchregex, whitelists, Theme Check-gates, previewtargetcontrole, gates A-G, mergebeleid en rollback blijven volledig gelden. Bewijsopslag verleent geen gate. Een complete evidencebundle kan menselijke review ondersteunen maar vervangt geen GATE E, F of G.

## 40. Relatie met CODEX_EXECUTION_LOG_PROTOCOL

Commanduitvoering blijft via de bestaande command-helper met raw command/stdout/stderr/meta-quartetten lopen; FILE_CHANGE-notes en volledige diffs blijven verplicht. `evidence/` is een aanvullende runspecifieke bewijslaag, niet een vervanging voor `FULL_EXECUTION_LOG.md`, `FINAL_REPORT.md`, `REVIEW_FILES_MANIFEST.md` of de centrale one-bundle-controles.

## 41. Open beslissingen

- Exact runtime-/browserframework en toegestane toolversie.
- Definitieve browser-/apparaatsupportmatrix buiten de drie testreferenties.
- Permanente/langdurige bewaartermijn en formele retentie-eigenaar.
- Eventuele cloud-, CI-artifact- of centrale testdatabasearchitectuur.
- Wanneer een compacte resultatenhistorie later tracked mag worden.
- Welke toekomstige taken screenshots, netwerkbewijs, metrics of tijdelijke cartstate expliciet mogen gebruiken.

## 42. Risico's

- Een hash kan ten onrechte als inhoudelijke kwaliteitsgarantie worden gelezen.
- Een technische `PASS` kan ten onrechte als menselijke acceptatie, merge- of releasegoedkeuring worden gelezen.
- Screenshots/logs kunnen ondanks intentie gevoelige data bevatten; minimale capture en review vóór bundeling blijven nodig.
- Oude fixtures, branches, commits of targets kunnen bewijs ongeldig maken.
- Grote binaries kunnen lokale runs en bundles onnodig laten groeien.
- Een runspecifiek manifest kan ten onrechte als permanente centrale testdatabase worden gebruikt.
- Onbesliste retentie kan tot onnodig lang lokaal bewaren leiden.

## 43. Aanbevolen volgende stap

Gebruik deze goedgekeurde standaard alleen binnen een afzonderlijk officieel gemaakte en expliciet toegestane runtime-, browser-, preview- of testtaak. De standaard zelf verleent geen uitvoerings- of implementatietoestemming.

## 44. Veiligheidsbevestiging

Binnen `BC-TECH-006` is uitsluitend lokale governance/documentatie uitgevoerd. Er is geen browser, storefront, developmentserver, preview, Shopify Admin, Shopify CLI store-/themecommando, account, cart, formulier, checkout, screenshot, runtime-/browserlog, netwerkcapture, metric, package-installatie, branch of theme-codehandeling uitgevoerd. De finalizer is alleen read-only beoordeeld en geen centraal logging-/finalizerscript is gewijzigd. Het ontworpen evidencepad is niet aangemaakt; dit document zelf is geen testuitvoering.

## 45. Menselijke goedkeuring

De BadkamerCity-projecteigenaar heeft `BC-TECH-006` en deze bewijsstandaard op 2026-08-16 inhoudelijk goedgekeurd. De goedkeuring omvat het ignored directorymodel, één resultaatrecord per testcase, `TEST_EVIDENCE_MANIFEST.md`, privacy- en mutatieclassificaties, SHA-256 en bytes, aparte reviewerstatus, interimretentie en one-bundle-integratie.

De goedkeuring bevat twee bindende aanscherpingen: forbidden evidence mag nooit als pending artefact blijven staan, normaal worden gehasht, naar `review_files/` worden gekopieerd of worden gebundeld; en iedere toekomstige run met `evidence/` moet vóór finalisatie de mechanische pre-bundle evidence gate uit hoofdstuk 31 halen. Binnen `BC-TECH-006` is geen runtime uitgevoerd. Deze goedkeuring is geen runtime-, browser-, preview-, Shopify- of implementatietoestemming.
