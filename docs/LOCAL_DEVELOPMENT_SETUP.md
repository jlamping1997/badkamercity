# Lokale ontwikkelomgeving — nieuwe computer

Datum: 2026-09-09. Taak: `BC-LOCAL-001`. Status: `DONE` — op 2026-09-09 menselijk goedgekeurd, inclusief de Git-identiteitsaanvulling en beide reviewbundels.

De projecteigenaar heeft lokale installatie, herstel en noodzakelijke bestandsaanpassingen expliciet toegestaan. Dit onderhoud voert geen storefrontpilot uit en verandert geen theme-code, Shopify-data of goedgekeurde kwaliteitsbaseline.

## Gecontroleerde omgeving

| Onderdeel | Aangetroffen | Eindresultaat |
| --- | --- | --- |
| Git | `2.55.0.windows.3` | Werkt; objectconnectiviteit gecontroleerd; aangeleverde auteursnaam/e-mail uitsluitend repository-local ingesteld en geverifieerd |
| Node.js | `24.19.0`, Windows x64 | Werkt; voldoet aan de package-engines `>=22.12.0` |
| npm | `11.17.0` | Werkt; publieke registry en gerichte package-installatie gecontroleerd |
| Shopify CLI | `4.8.0` | Exact `4.6.1` hersteld; automatische upgrade uit |
| esbuild bij Shopify CLI | `0.28.1` | Installatiescript uitgevoerd; native versie, TypeScript-transformatie en bundeling geslaagd |
| Windows PowerShell | `5.1` | `CurrentUser = RemoteSigned`; uitvoering zonder tijdelijke procesoverride gecontroleerd |
| Projectscripts | Vier logginghelpers en Theme Check-wrapper | Alle vijf parsen zonder fouten; logging gebruikt en Theme Check uitgevoerd |
| Chrome Stable | `152.0.7977.83` | Offline launch-, viewport- en toetsenbordtest geslaagd |
| Edge Stable | `152.0.4191.66` | Installatie en versie vastgesteld; geen tweede browsertest nodig |
| Tijdelijke browserautomation | `puppeteer-core@25.4.0` | Buiten repository geïnstalleerd, offline getest en daarna verwijderd |

De repository bevat geen `package.json`, npm-/pnpm-lockfile of aanvullende buildpipeline. Er is daarom geen projectbrede dependency-installatie nodig. npm volstaat; pnpm en PowerShell 7 zijn voor de aanwezige projecttools niet vereist. Er is geen projectmanifest of lockfile toegevoegd.

## Herstel en waargenomen fouten

De eerste runinitialisatie werd door de standaard PowerShell-policy geblokkeerd. De run is vervolgens met een tijdelijke procesoverride gestart. Het instellen van `RemoteSigned` meldde binnen die procescontext een `SecurityException`; de vervolgstap bewees dat de gebruikersinstelling wel was opgeslagen en zonder de procesoverride correct werkt. Machinebeleid is niet gewijzigd.

De projectwrapper weigerde CLI `4.8.0` terecht met exitcode `2`. De eerste installatie van `4.6.1` slaagde, maar de daaropvolgende `shopify version` activeerde onverwacht de ingebouwde upgrade terug naar `4.8.0`. De volledige uitvoer is bewaard. Na `shopify config autoupgrade off` is `4.6.1` opnieuw geïnstalleerd en gecontroleerd. Dit herstelt de bestaande projectversie; het is geen rebaseline.

De automatische upgrade reproduceerde de npm-waarschuwing over het nog niet toegestane `esbuild@0.28.1`-installatiescript. De native esbuild-functionaliteit werkte al vóór herstel. De definitieve installatie heeft daarnaast aantoonbaar `postinstall: node install.js` uitgevoerd met uitsluitend de eenmalige allowlist `--allow-scripts=esbuild`. Er is geen algemene toestemming voor alle installatiescripts ingesteld en geen blijvende npm-configuratie versoepeld. Er is geen resterend esbuild-defect vastgesteld. De indirecte package `boolean@3.2.0` geeft een deprecation-waarschuwing; die blokkeerde installatie of controles niet.

Twee overige onderzoeksafwijkingen zijn hersteld met afzonderlijke logstappen: een gezocht npm-documentatiepad bestond niet, en een PowerShell-arrayinterpretatie gaf eerst een onjuiste afgeleide bestandstelling. De oorspronkelijke uitvoer is intact; de definitieve telling en fingerprintvergelijking zijn rechtstreeks uit de Theme Check-JSON berekend.

## Kwaliteitscontrole

De ongewijzigde `scripts/run-theme-check.ps1` en `.theme-check.yml` werken met CLI `4.6.1`. Eén volledige lokale run eindigde normaal met exitcode `1` wegens bestaande codebevindingen:

- 18 offenses in 14 bestanden: 2 errors en 16 warnings.
- Alle 18 fingerprints komen exact overeen met de goedgekeurde lokale codebaseline; 0 nieuwe fingerprints.
- De vroegere externe `ValidJSON`-schemafout is deze keer niet gereproduceerd. De goedgekeurde baseline blijft historisch 19 offenses; deze meting vervangt die niet.
- Actuele fingerprintset SHA-256: `d2580685174555530bf8b42fba6b5418b9ad448ea176b0fc7e6a8065d6b931d1`.

De offline browserprobe gebruikte uitsluitend zelfgemaakte HTML, de viewports `375 × 812` en `1280 × 900` en bediening met Enter. Chrome startte succesvol, beide controles slaagden en de testpagina deed 0 netwerkrequests. Er zijn geen screenshots of storefrontresultaten gemaakt. De tijdelijke toolmap en het geïsoleerde profiel zijn na controle van hun absolute paden verwijderd. Dit bewijst lokale toolingwerking, geen websitekwaliteit of formele browserdekking.

## Git en volgende projecttaak

Bij start was de werkboom schoon. `HEAD`, `origin/main` en de via `git ls-remote` gecontroleerde remote `refs/heads/main` waren alle:

`3bd1cfd4f2ba5c463e49ac122c800af2c9148379` — `docs: approve evidence standard and prepare runtime pilot`.

Deze commit bevat precies het masterplan en de goedgekeurde evidence-standaard. De in masterplan 0.25 genoemde voorganger `d0b43c0` is daarmee historisch achterhaald als actuele tip. De voorbereidende commit/push hoeft niet opnieuw te worden uitgevoerd. De oorspronkelijke onderhoudsruns hebben niets gecommit of gepusht. Na menselijke goedkeuring autoriseert de vervolgopdracht uitsluitend dit rapport en masterplan 0.25.3 voor een normale commit/push naar origin/main. De uitvoeringshash en remote verificatie volgen in run BC-TECH-007_20260909-205903 en de pilotrapportage; de geschiedenis en beide lokale bewijsbundels blijven behouden.

De oorspronkelijke eindcontrole vond geen ingestelde Git-auteursnaam of e-mailadres (runstap `034`). De gebruiker heeft de gewenste waarden vervolgens expliciet aangeleverd en alleen voor deze repository toegestaan. In aanvullende run `BC-LOCAL-001-IDENTITY_20260909-205144` zijn beide waarden met `git config --local` ingesteld, exact vergeleken en met `git var GIT_AUTHOR_IDENT` gecontroleerd zonder uitvoer van persoonsgegevens. De globale en systeemidentiteit zijn aantoonbaar ongewijzigd. `BC-Q-039` is daarmee opgelost; de waarden staan uitsluitend in de lokale Git-configuratie en niet in de bewijsdocumenten.

Op dezelfde expliciete opdracht is Windows Verkenner geopend met de bestaande `BC-LOCAL-001_20260909-203405_BUNDLE.zip` geselecteerd. De selectie is via de Windows Shell gecontroleerd. Deze eerdere bundel is ongewijzigd behouden (SHA-256 `CE8A345F447F1422C5F3EE37921A21758E5DE2F6368AC66AAA7BC905FE3E32DD`) en bevat de historische stand vóór het instellen van de identiteit. De aanvullende run documenteert alleen deze vervolghandeling; hij vervangt de door de gebruiker geselecteerde bundel niet.

Na de afzonderlijk toegestane fase-A-push start de expliciet geautoriseerde volgende projecttaak `BC-TECH-007`: exact vijf publieke/anonieme read-only cases (`SMK-HOME-001`, `SMK-HEADER-001`, `SMK-HEADER-002`, `SMK-CART-001`, `SMK-CONTENT-004`). Die taak is `READY` en niet inhoudelijk gestart. Bij de daadwerkelijke pilot moeten tooling, target, fixtures, GET/HEAD-interception en evidencegates opnieuw binnen de taakcontext worden gecontroleerd. De tijdelijke browsertooling moet dan opnieuw buiten de repository worden ingericht.

Het project blijft `ACTIVE FOR DISCOVERY - IMPLEMENTATION BLOCKED`. Leveranciersbronnen, definitieve data-/categoriearchitectuur, bedrijfsregels en afzonderlijke implementatiebesluiten blijven open. Live theme `189463068938`, previewtheme `192770375946` en Shopify Admin zijn binnen dit onderhoud niet benaderd of gewijzigd.

## Normaal lokaal gebruik en herstel

Gebruik vanuit de repository de bestaande projectwrapper:

```powershell
& .\scripts\run-theme-check.ps1
```

Voor toekomstige uitdrukkelijk toegestane herinstallatie blijft de exacte CLI-versie bepalend. De tijdens dit onderhoud bewezen installatie was:

```powershell
npm.cmd install --global '@shopify/cli@4.6.1' --allow-scripts=esbuild --ignore-scripts=false --include=optional --foreground-scripts --no-audit --no-fund --registry=https://registry.npmjs.org
```

Automatische upgrades blijven uit. `shopify theme check -v` wordt niet gebruikt. Een wijziging van CLI-versie, regelset of baseline vereist een afzonderlijk besluit. De lokale PowerShell-wijziging is omkeerbaar naar de eerdere `CurrentUser = Undefined`; terugzetten zou de oorspronkelijke scriptblokkade terugbrengen.

## Bewijs en bronnen

Alle commando's, fouten, herstel, versies en controles staan lokaal in run `BC-LOCAL-001_20260909-203405`. Relevante stappen: `006` versieguard, `011`/`016` installatie, `013` policy en auto-upgrade, `014` parsers/Git/esbuild, `017` Theme Check, `018` remote commit/package-installatie, `020` offline browser en `022` definitieve fingerprints/esbuild/cleanup. De finale runbundle bevat dit rapport en het bijgewerkte masterplan als hashgecontroleerde reviewbestanden. Lokale runbestanden blijven genegeerd; de gebruiker beslist over upload en retentie.

De versiekeuze volgt de projectbaseline. Ondersteunende primaire documentatie, geraadpleegd op 2026-09-09: [Shopify CLI](https://shopify.dev/docs/api/shopify-cli) voor vereisten en uitschakelen van automatische upgrades; [npm allow-scripts](https://docs.npmjs.com/cli/v11/using-npm/config/#allow-scripts) voor de gerichte globale installatietoestemming; [esbuild-installatie](https://esbuild.github.io/getting-started/#additional-npm-flags) voor native binaries en installatiescripts. Exacte package-engines zijn daarnaast rechtstreeks via npm-metadata vastgesteld.

## Menselijke goedkeuring

De projecteigenaar heeft op 2026-09-09 BC-LOCAL-001 goedgekeurd op basis van beide reviewbundels: BC-LOCAL-001_20260909-203405 en BC-LOCAL-001-IDENTITY_20260909-205144. Dit omvat de lokale inrichting, herstelstappen, vastgelegde beperkingen en uitsluitend repository-local ingestelde Git-identiteit. BC-Q-038 is gesloten; BC-Q-039 blijft opgelost. De goedkeuring verandert geen Theme Check-baseline en geeft geen reparatie- of publicatietoestemming. De afzonderlijke vijf-case runtimepilot blijft onderwerp van een nieuwe REVIEW.
