# BadkamerCity technische wijzigings-, preview- en rollbackwerkwijze

## 1. Documentstatus

| Veld | Waarde |
| --- | --- |
| Status | `DONE` - menselijk goedgekeurd binnen de governance-/documentatiescope |
| Projectstatus | `ACTIVE FOR DISCOVERY - IMPLEMENTATION BLOCKED` |
| Taak | `BC-TECH-004` |
| Menselijk goedgekeurd | 2026-08-16 |
| Theme-code gewijzigd | **NEE** |
| Branch aangemaakt | **NEE** |
| Shopify benaderd | **NEE** |

Dit document is een runbook en geen permanente algemene implementatietoestemming. Iedere toekomstige technische taak vereist opnieuw een officiële taak, exacte scope en de toepasselijke afzonderlijke menselijke gates.

## 2. Taak en datum

- Taak: `BC-TECH-004` - Technische wijzigings-, preview- en rollbackwerkwijze vastleggen.
- Datum: 2026-08-12.
- Herkomst: `PROPOSED-TECH-10` uit `docs/TECHNICAL_STABILIZATION_PLAN.md`.
- Goedgekeurde basiscommit voor deze documentatietaak: `10254b5ca652ebbc88b2dc33b134dc74b324fba6` op `main` en `origin/main`.
- Binnen deze taak is geen branch gemaakt, gepusht, gemerged of verwijderd en is geen preview- of liveactie uitgevoerd.

## 3. Doel

Dit runbook maakt toekomstige theme-codewijzigingen bestuurbaar vanaf officiële taakgoedkeuring tot branchisolatie, technische validatie, eventuele development-preview, menselijke review, merge en herstel. Het legt de volgorde, stopcondities, bewijsvereisten en menselijke bevoegdheden vast zodat een eerdere gate nooit stil als toestemming voor een latere gate wordt gelezen.

## 4. Scope

Binnen het runbook vallen:

- het branchmodel en de branchnaamconventie;
- controle van de exacte basiscommit;
- commit-, diffreview- en remote-branchbeleid;
- Theme Check pre-/postgates en fingerprintdelta;
- taakgebonden smoke-/regressiecriteria;
- development-preview en targetcontrole;
- menselijke gates A tot en met G;
- mergebeleid, branchopruiming en vier rollbackposities;
- bewijsvolgorde, one-bundle-eisen en fout-/herstelpad;
- Definition of Ready, Review en Merge Ready voor toekomstige implementatie.

## 5. Buiten scope

`BC-TECH-004` voert niet uit:

- een lokale of remote branch maken, wijzigen, pushen, mergen of verwijderen;
- een Pull Request maken of GitHub-instellingen/branch protection wijzigen;
- Liquid, JavaScript, CSS, JSON/JSONC, locale, section, snippet, template of andere theme-code wijzigen;
- een van de 19 Theme Check-offenses oplossen of onderdrukken;
- Shopify, Shopify Admin, een store of theme benaderen;
- een theme pushen, pullen, publiceren, verwijderen, dupliceren of hernoemen;
- een development-preview of smoke-/browsermatrix werkelijk uitvoeren;
- een package of Shopify CLI installeren/updaten;
- live release of productierollback uitvoeren.

## 6. Gebruikte bewijsbronnen

Dit runbook gebruikt uitsluitend bestaande lokale documentatie:

- `AGENTS.md` voor permanente veiligheids- en masterplanregels;
- `docs/CODEX_EXECUTION_LOG_PROTOCOL.md` voor one-bundle-uitvoeringsbewijs;
- `docs/MASTERPLAN.md` voor taakstatus, besluiten, risico's, afhankelijkheden en route;
- `docs/THEME_CHECK_BASELINE.md` voor CLI `4.6.1`, config, wrapper en 19 fingerprints;
- `docs/TECHNICAL_STABILIZATION_PLAN.md` voor `PROPOSED-TECH-10`, technische risico's en de nog afzonderlijke smoke-kandidaat;
- `docs/REPOSITORY_AUDIT.md` voor code-/legacy-/releasegaten;
- `docs/ACTIVE_THEME_USAGE.md` voor actieve, conditionele en onbewezen themegebruikspaden;
- `docs/LIVE_THEME_COMPARISON.md` voor de gedateerde live-snapshotbasis;
- `docs/DEVELOPMENT_THEME.md` voor het bestaande unpublished development-theme;
- `docs/SHOPIFY_ENVIRONMENT.md` voor de gedateerde store-/themecontext en bewijsgrenzen.

De Shopify-documenten zijn in `BC-TECH-004` alleen als lokale bron gelezen. Hun tijdgebonden inhoud vervangt nooit de verplichte actuele targetcontrole vóór een latere toegestane previewactie.

## 7. Fundamentele veiligheidsregels

1. `main` is de enige goedgekeurde integratiebranch en bron van waarheid.
2. Een technische theme-codewijziging wordt nooit rechtstreeks op `main` uitgevoerd.
3. Een documentatie-, onderzoeks- of administratieve approvaltaak mag alleen rechtstreeks op `main` committen wanneer de specifieke menselijke opdracht dat uitdrukkelijk toestaat.
4. Iedere implementatietaak heeft vóór uitvoering een officiële taak-ID, `READY`, exacte scope, toegestane bestanden, tests, rollback en expliciete menselijke start-/implementatietoestemming.
5. Geen gate impliceert een volgende gate.
6. Geen force push, history rewrite of reset om verschillen te verbergen.
7. Geen rebase op een reeds gedeelde task branch.
8. Geen automatische merge, branchverwijdering, previewpush, rebaseline, suppressie of livepublicatie.
9. Onverwachte lokale/remote drift, targetafwijking, CLI/configmismatch of onverklaarde diff betekent `STOP`.
10. Live theme `189463068938` is nooit een development-pushtarget.

## 8. Branchmodel

- Integratie-/bronbranch: uitsluitend `main`.
- Technische implementatie: een korte, taakgebonden branch vanaf de exact goedgekeurde `origin/main`-basiscommit.
- Een task branch is isolatie, geen merge- of releasegoedkeuring.
- De branch bevat alleen bestanden die in de officiële taak zijn toegestaan.
- Documentatie-/onderzoekstaken blijven zonder technische branch wanneer de concrete menselijke opdracht rechtstreeks committen op `main` expliciet toestaat.
- Een remote branch bestaat alleen wanneer GATE C afzonderlijk is verleend.
- Een development-preview bestaat alleen wanneer GATE D afzonderlijk is verleend.
- `main` verandert pas na GATE F; live verandert pas in een afzonderlijke releaseopdracht onder GATE G.

## 9. Branchnaamconventie

Verplichte vorm:

`task/<lowercase-task-id>-<korte-slug>`

Regex:

```text
^task/bc-[a-z]+-[0-9]{3}-[a-z0-9]+(?:-[a-z0-9]+)*$
```

Regels:

- uitsluitend lowercase ASCII-letters, cijfers en koppeltekens;
- exact één slash, direct na `task`;
- drie cijfers in de taak-ID;
- minimaal één niet-lege slugcomponent;
- geen spaties, underscores, trailing koppelteken of uppercase.

Geldige voorbeelden:

- `task/bc-tech-005-smoke-regression`
- `task/bc-pdp-001-product-page`
- `task/bc-switch-001-switcher-runtime`

Ongeldige voorbeelden:

- `feature/test`
- `task/BC-TECH-005-Test`
- `task/bc-tech-5-test`
- `task/bc-tech-005_test`
- `task/bc-tech-005-`
- `task/bc-tech-005 test`

`BC-TECH-004` valideert dit uitsluitend als strings/regex en maakt geen Git-ref.

## 10. Basiscommit- en startcontrole

Vóór een toekomstige branchaanmaak moet de taak bewijzen:

1. huidige branch is `main`;
2. niet-genegeerde werkboom en index zijn schoon;
3. lokale `main`, lokaal bekende `origin/main` en de expliciet door de mens goedgekeurde volledige basiscommit zijn exact gelijk;
4. de officiële taak staat `READY` en GATE A is expliciet verleend;
5. scope, toegestane bestanden, validators, previewbehoefte en rollback zijn vastgelegd;
6. er bestaat geen onverwachte lokale branch-/ref- of bestandsdrift.

Een read-only `fetch` is geen stil standaardonderdeel. Wanneer remote hercontrole nodig is, moet de specifieke taak die netwerkactie expliciet toestaan. Zonder die toestemming wordt uitsluitend de lokaal bekende `origin/main` vergeleken; twijfel betekent `STOP`.

## 11. Verschil documentatie-/onderzoekstaak versus implementatietaak

| Kenmerk | Documentatie/onderzoek/approval | Technische implementatie |
| --- | --- | --- |
| Direct op `main` | Alleen als de specifieke menselijke opdracht dit expliciet toestaat | Verboden |
| Task branch | Niet standaard nodig | Verplicht na start- en basiscontrole |
| Code-/configmutatie | Buiten scope tenzij exact afzonderlijk toegestaan | Alleen na GATE B en binnen whitelist |
| Theme Check pre/post | Alleen wanneer taak dit inhoudelijk vereist | Verplicht volgens sectie 16 |
| Preview | Normaliter niet relevant | Alleen indien vereist en na GATE D |
| Menselijke mergegate | Niet van toepassing als expliciet directe documentatiecommit is toegestaan | Altijd GATE F |
| Live release | Nooit impliciet | Altijd afzonderlijke taak/GATE G |

Een documentatiebesluit is geen implementatiebesluit. Een goedgekeurd runbook is evenmin toestemming om de eerste codebranch te starten.

## 12. Taakbranch lifecycle

1. Maak de task branch pas na officiële taak, GATE A en exacte basiscontrole.
2. Leg branchnaam en basiscommit onmiddellijk als bewijs vast.
3. Ontvang GATE B vóór de exacte code-/configwijzigingen.
4. Werk uitsluitend in kleine, verklaarde wijzigingen binnen de bestandswhitelist.
5. Leg elke wijziging, diff en validator vast volgens het one-bundle-protocol.
6. Voer Theme Check en taaktests uit.
7. Push alleen na GATE C wanneer remote review nodig is.
8. Gebruik development-preview alleen na GATE D en actuele targetcontrole.
9. Houd de branch op `REVIEW` tot menselijke functionele/visuele beoordeling waar van toepassing.
10. Merge pas na nieuwe GATE F.
11. Valideer `main` na merge opnieuw.
12. Verwijder de branch niet automatisch; opruiming volgt een bewuste latere controle.

## 13. Commitbeleid

- Commits zijn klein, logisch afgebakend en herleidbaar tot de officiële taak.
- Eén commit combineert geen ongerelateerde refactor, formattering, cleanup of documentatiewijziging.
- Een commitbericht beschrijft het geleverde resultaat, niet alleen de activiteit.
- Voor iedere commit zijn diff, diffstat, toegestane bestanden en relevante validators vastgelegd.
- Onverwachte wijzigingen van de gebruiker blijven intact en worden niet met reset/restore/revert verborgen.
- Geen amend, rebase, squash of andere geschiedenisherschrijving wordt automatisch uitgevoerd.
- Een herstel op een gedeelde branch gebeurt niet-destructief met een nieuwe verklaarde herstel-/revertcommit, uitsluitend wanneer de taak dit toestaat.

## 14. Remote branch pushbeleid

Remote push van een task branch vereist afzonderlijk GATE C. Vóór die gate moeten branchnaam, basiscommit, lokale commits, volledige diff, technische gates, gevoelige-datareview en restrisico beschikbaar zijn.

- Push nooit stil omdat een lokale branch gereed lijkt.
- Force push is verboden.
- Een remote branch push is geen mergegoedkeuring en geen previewgoedkeuring.
- Een formele GitHub Pull Request is nu niet verplicht.
- De voorlopige verplichte route is: task branch → controleerbare diff → one-bundle-bewijs → eventuele development-preview → expliciete menselijke mergegoedkeuring.
- Een later verplicht PR-beleid vereist een afzonderlijk governancebesluit.

## 15. Diffreview

Minimale diffreview vóór `REVIEW`:

- basiscommit, actuele branch en staged/unstaged status;
- exacte gewijzigde bestanden versus whitelist;
- volledige diff en diffstat;
- nul onverwachte theme-, tooling-, package-, data- of documentwijziging;
- uitleg per functionele wijziging en per verwijderd/nieuw bestand;
- onverwachte verdwijning van een bestaande Theme Check-offense verklaard;
- geen secrets, credentials, klant-, order- of persoonsgegevens;
- `git diff --check` geslaagd;
- rollbackimpact en resterende risico's vastgelegd.

Een grote of onoverzichtelijke diff betekent: `STOP`, taak verder opsplitsen en nieuwe menselijke scopebevestiging vragen.

## 16. Theme Check pre-/postgate

Goedgekeurde basis:

- Shopify CLI `4.6.1`;
- `.theme-check.yml` met `extends: theme-check:recommended`;
- `scripts/run-theme-check.ps1`;
- 19 fingerprints in 15 bestanden;
- 3 errors en 16 warnings;
- geen suppressies.

Een toekomstige theme-codeimplementatie voert de wrapper vóór de wijziging uit, tenzij binnen dezelfde gecontroleerde taak mechanisch is bewezen dat repositorysnapshot, basiscommit, CLI, config, wrapper en baseline identiek zijn. Na de wijziging wordt exact dezelfde wrapper opnieuw uitgevoerd.

De gate stopt bij:

- CLI-versie anders dan `4.6.1`;
- config- of wrapperdrift;
- toolingexitcode buiten de gedocumenteerde semantiek;
- onparseerbare output;
- nieuwe, uitgebreidere of ernstigere offense zonder expliciete oplossing binnen scope;
- stille suppressie of rebaseline.

## 17. Offensefingerprintbeleid

- De goedgekeurde fingerprintmethode blijft die uit `docs/THEME_CHECK_BASELINE.md`.
- Een bestaande fingerprint betekent alleen dat de melding vooraf bestond; zij is geen kwaliteitsacceptatie.
- Een nieuwe fingerprint is een regressiesignaal.
- Een bestaande offense die ernstiger wordt, naar meer bestanden/locaties uitbreidt of inhoudelijk verandert is een regressiesignaal.
- Een verdwijnende offense is alleen gewenst wanneer de taak die offense mocht beïnvloeden. Anders is uitleg en aanvullende regressiecontrole verplicht.
- Lokale codebevindingen en aantoonbare tooling-/externe meldingen blijven apart geclassificeerd.
- Geen offense wordt stil geaccepteerd, onderdrukt of in severity verlaagd.
- Wijziging van CLI, config, regelset, fingerprintmethode of beleid vereist een afzonderlijke menselijke rebaseline.

## 18. Smoke-/regressiegate

`BC-TECH-004` kiest nog geen volledige smoke-, browser-, viewport- of toegankelijkheidsmatrix. `PROPOSED-TECH-02` blijft een afzonderlijke niet-officiële kandidaat.

Voor iedere toekomstige implementatietaak geldt wel:

- taakgebonden smokecriteria worden vóór implementatie vastgelegd;
- tests sluiten aan op gewijzigde codepaden en bekende actieve/conditionele routes;
- zichtbaar of functioneel werk vereist relevante desktop-, mobiel- en toetsenbordcontroles zodra de smoke-baseline menselijk is goedgekeurd;
- productpagina-/switcherwerk krijgt representatieve data- en navigatiescenario's;
- zonder werkelijk browser-/devicebewijs wordt geen volledige browserondersteuning geclaimd;
- een mislukte gate stopt preview en merge totdat herstel en hertest zijn bewezen.

## 19. Development-previewbeleid

Een development-preview is optioneel en taakafhankelijk, maar vereist altijd afzonderlijk GATE D. Geen eerdere taak-, implementatie- of remote-branchtoestemming impliceert previewtoestemming.

- De specifieke taak bepaalt of een preview nodig is.
- Een previewpush gebruikt alleen de exact toegestane bestanden/scope.
- Een brede of full-theme push is nooit de stille standaard.
- Exacte pushflags worden in die toekomstige taak read-only uit de geïnstalleerde CLI-help vastgesteld wanneer nodig.
- Target-ID, scope, basiscommit en rollbackpad worden vóór de push vastgelegd.
- Na push volgt taakgebonden technische controle en, voor zichtbaar/functioneel werk, GATE E.
- Theme pull is geen standaard synchronisatiestap; vermoede drift leidt tot `STOP` en een aparte read-only vergelijkingstaak.

## 20. Previewtargetcontrole

Het enige momenteel goedgekeurde **potentiële** development-previewtarget is:

- naam: `BadkamerCity Development`;
- theme-ID: `192770375946`;
- verwacht role/status: `unpublished`.

Dit is geen algemene wijzigingstoestemming. Direct vóór iedere later toegestane previewpush moet de taak read-only en actueel verifiëren:

1. store-identiteit;
2. target-ID `192770375946`;
3. targetnaam `BadkamerCity Development`;
4. role/status `unpublished`;
5. actuele live theme-ID;
6. target-ID is niet gelijk aan live theme-ID;
7. exacte wijzigingsscope en rollbackroute.

Iedere onverwachte afwijking in store, naam, ID, role/status of live-ID betekent `STOP`; niet corrigeren, omzeilen of naar een ander target uitwijken.

## 21. Verboden themes/targets

| Theme | ID | Workflowstatus | Regel |
| --- | ---: | --- | --- |
| `BadkamerCity Development` | `192770375946` | Potentieel development-previewtarget | Alleen na nieuwe taaktoestemming, GATE D en actuele targetcontrole; binnen `BC-TECH-004` niet benaderd |
| `badkamercity-phase-c-paris-rectangle-test-v2` | `192796786954` | **VERBODEN TARGET** | Niet benaderen, wijzigen, pushen, pullen, publiceren, verwijderen of hernoemen totdat een aparte menselijke taak doel en eigenaarschap vaststelt |
| `Categoriepagina_v1.0` | `189463068938` | Live productie | Nooit development-pushtarget; iedere liveactie vereist afzonderlijke releaseopdracht/GATE G |

Een backup- of ander unpublished theme is zonder actueel inhouds-, doel-, eigenaarschap- en herstelbewijs nooit automatisch een geldig preview- of productierollbacktarget.

## 22. Menselijke gates

| Gate | Naam | Expliciete beslissing | Minimale input | Wat de gate niet toestaat |
| --- | --- | --- | --- | --- |
| A | TASK START | Officiële `READY`-taak inhoudelijk starten en exact basisbewijs verzamelen | Taakrecord, scope, bestanden, tests, rollback, goedgekeurde basiscommit | Nog geen code/configwijziging, remote push, preview, merge of liveactie |
| B | IMPLEMENTATION | Exact benoemde code-/configwijzigingen op de juiste task branch uitvoeren | Branch-/basisbewijs, whitelist, implementatieplan, taaktests | Geen remote push, preview, merge of liveactie |
| C | REMOTE BRANCH PUSH | De gecontroleerde task branch naar GitHub pushen | Commits, diff, gates, securityreview, remote doel | Geen merge, preview of liveactie |
| D | DEVELOPMENT PREVIEW PUSH | Exacte scope naar het geverifieerde developmenttarget pushen | Actuele store/theme/role/livecontrole, pushscope, rollback | Geen previewacceptatie, merge of liveactie |
| E | PREVIEW ACCEPTANCE | Menselijke functionele/visuele preview beoordelen | Previewbewijs, testdata, screenshots/journeys, beperkingen | Geen automatische merge of liveactie |
| F | MERGE TO MAIN | Nieuwe expliciete toestemming om de beoordeelde branch naar `main` te mergen | Goedgekeurde diff, technische gates, vereiste preview/smoke, restrisico, rollback | Geen live release |
| G | LIVE RELEASE | Afzonderlijke toekomstige releaseopdracht | Releasecandidate, live-targetcontrole, go/no-go, bewezen rollback, post-releaseplan | Geen stil vervolg buiten exacte releaseopdracht |

Een eerder verleende gate vervalt niet automatisch, maar de bevoegdheid blijft beperkt tot de exacte taak, scope, commit(s), target en datum. Gewijzigde omstandigheden vereisen herbeoordeling.

## 23. Mergebeleid

- Een task branch wordt nooit automatisch naar `main` gemerged.
- GATE F is altijd een nieuwe expliciete menselijke beslissing na diffreview, technische gates, vereiste smoke-/previewcontrole en restrisicoregistratie.
- De beleidsvoorkeur voor een latere toegestane merge is een expliciete niet-destructieve mergecommit met `git merge --no-ff`.
- `BC-TECH-004` voert dit commando niet uit.
- Geen automatische squash, rebase, fast-forwardvereenvoudiging of history rewrite.
- Vóór merge wordt opnieuw bewezen dat target `main` en de goedgekeurde mergebasis niet onverwacht zijn veranderd.
- Bij onverwachte drift: `STOP`; herbaseer niet stil en maak geen verborgen conflictresolutie.
- Na merge volgt post-mergevalidatie op `main` met dezelfde statische en taakgebonden gates.
- Mergegoedkeuring is geen live-releasegoedkeuring.

## 24. Branchopruiming

Task branches worden na merge niet automatisch lokaal of remote verwijderd. Opruiming vereist later een bewuste read-only controle van:

- mergecommit en bereikbaarheid van alle taakcommits;
- open review-, incident- of rollbackbehoefte;
- remote/local branchstatus;
- bewijsbundle en commitreferenties;
- eventuele preview die nog aan de branch/snapshot is gekoppeld;
- expliciete menselijke opruimtoestemming.

Geen branch wordt verwijderd om een fout, onverwachte diff of ontbrekend bewijs te verbergen.

## 25. Rollback vóór preview

**Rollbackscenario A — vóór merge, geen preview**

- `main` is onaangetast.
- De task branch kan met nieuwe kleine correctiecommits worden hersteld.
- Een ongeschikte implementatie wordt niet gemerged en bereikt geen theme.
- Geen reset, force push of history rewrite is nodig of toegestaan.
- Na correctie worden Theme Check en taaktests opnieuw uitgevoerd.
- Indien de taak wordt gestopt, blijven branch, commits en one-bundle-bewijs behouden totdat bewuste opruiming is toegestaan.

## 26. Rollback na preview vóór merge

**Rollbackscenario B — vóór merge, wel development-preview**

- `main` blijft onaangetast.
- Stop verdere preview- en mergehandelingen.
- Maak op de branch een niet-destructieve herstel-/revertcommit binnen expliciet toegestane scope.
- Voer dezelfde statische, smoke- en regressiegates opnieuw uit.
- Leg vast welke previewinhoud teruggezet moet worden en naar welke bewezen branchcommit.
- Alleen na nieuwe expliciete GATE D mag de herstelde branch/scope opnieuw naar het geverifieerde developmenttarget worden gestuurd.
- Menselijke afkeuring van preview betekent nooit automatisch branchverwijdering of merge.

## 27. Rollback na merge vóór live

**Rollbackscenario C — na merge, vóór livepublicatie**

- Live is onaangetast.
- Stop releasevoorbereiding.
- Herstel `main` uitsluitend via een afzonderlijk goedgekeurde revert-/hersteltaak met eigen scope, bewijs en menselijke gates.
- Geen reset, force push of geschiedenisherschrijving.
- Voer Theme Check, taaktests en relevante regressiegates opnieuw uit op de herstelde `main`.
- Documenteer gevolg voor development-preview en open branches.
- Een herstelcommit op `main` is nog steeds geen liveactie.

## 28. Live-releasegrens

**Rollbackscenario D — na livepublicatie**

- Valt buiten `BC-TECH-004` en buiten een gewone implementatietaak.
- Vereist een afzonderlijk `BC-REL-*`-, incident- of rollbackproces met GATE G, exacte live-identiteit, impactanalyse, bevoegd eigenaar, herstelbron en post-herstelvalidatie.
- Codex zet live nooit stil terug en kiest nooit zelfstandig een backup-/unpublished theme.
- Een backup- of unpublished theme geldt zonder inhouds-, actualiteits-, compatibiliteits- en herstelbewijs niet als voldoende productierollback.
- Behoud incidenttijdlijn, releasecommit, live target, rollbackactie en functioneel bewijs.

LIVE RELEASE staat buiten de technische implementatiestate-machine en is nooit geïmpliceerd door `DONE` van een implementatietaak.

## 29. Bewijs- en one-bundlevereisten

Iedere toekomstige technische taak gebruikt het goedgekeurde one-bundle-uitvoeringslogprotocol. Minimaal bewijs vóór menselijke review:

- volledige menselijke opdracht en taak-ID;
- officiële taakstatus en toepasselijke menselijke gates;
- goedgekeurde basiscommit en actuele branch;
- gewijzigde bestanden en staged/unstaged status;
- volledige diff en diffstat;
- Theme Check vóór/na en fingerprintdelta;
- taakgebonden validators en smoke-/regressiebewijs;
- previewtarget en actuele targetcontrole wanneer preview is gebruikt;
- rollbackstappen en rollbackpositie;
- restrisico's en open vragen;
- lokale/remote commit-hashes en pushstatus waar toegestaan;
- `FINAL_REPORT.md` volgens sectie 30;
- één gevalideerde `<RUN_ID>_BUNDLE.zip` met raw evidence en hashgelijke reviewbestanden.

Raw command evidence en `FULL_EXECUTION_LOG.md` zijn de primaire chronologische bron van waarheid.

## 30. FINAL_REPORT-volgorde

De eerste onafhankelijke run `BC-TECH-003` bewees dat raw evidence volledig kan zijn terwijl een eerder geschreven `FINAL_REPORT.md` niet alle latere finalization-retries samenvat. Er ging geen bewijs verloren, maar de samenvattingsvolgorde wordt aangescherpt.

Nieuwe standaardvolgorde:

1. voer alle normale projectchecks uit;
2. voer alle normale preflightchecks uit;
3. ververs `FINAL_REPORT.md` definitief en neem alle tot dan toe ontstane onverwachte failures en recovery-acties op;
4. voer zonder nieuwe gewone projectanalyse of validator direct de finalizer uit;
5. bij finalizerfailure: bewaar foutbewijs, log ERROR/RECOVERY, herstel uitsluitend binnen scope, ververs `FINAL_REPORT.md` opnieuw en voer daarna de finalizer opnieuw uit.

Dit is een operationele workflowregel. `BC-TECH-004` wijzigt het centrale loggingprotocol of de logginghelpers niet.

## 31. Fout- en herstelpad

Bij iedere onverwachte fout:

1. stop de volgende risicovollere overgang;
2. behoud command, stdout, stderr, exitcode en meta in raw evidence;
3. voeg een ERROR-note toe met oorzaak en impact;
4. wijzig niets buiten de taakscope;
5. kies een niet-destructieve herstelactie;
6. voeg een RECOVERY-note toe en herhaal alleen de noodzakelijke controle;
7. herbevestig Git-state, branch, target en bewijsgrens;
8. actualiseer restrisico en taakstatus;
9. ververs `FINAL_REPORT.md` pas na de laatste normale preflight;
10. finaliseer direct; bij finalizerfailure wordt de rapportrefresh opnieuw uitgevoerd.

Een herhaalde mismatch in basiscommit, branch, target, CLI/config, remote drift of scope wordt niet omzeild: taak `BLOCKED` of menselijke herbeslissing is dan vereist.

## 32. State machine

Verplichte hoofdroute:

```text
OFFICIAL TASK
→ READY
→ HUMAN TASK START
→ EXACT BASE COMMIT
→ TASK BRANCH
→ IMPLEMENTATION AUTHORIZED
→ SMALL COMMITS
→ STATIC VALIDATION
→ TASK-SPECIFIC TESTS
→ OPTIONAL REMOTE BRANCH PUSH
→ OPTIONAL DEVELOPMENT PREVIEW
→ HUMAN REVIEW
→ MERGE APPROVAL
→ MERGE TO MAIN
→ POST-MERGE VALIDATION
→ DONE FOR IMPLEMENTATION TASK
```

`LIVE RELEASE` staat buiten deze state machine en vereist een afzonderlijke taak plus GATE G.

| Overgang | Vereiste input | Menselijke gate | Technisch bewijs | Stopconditie | Rollbackpositie |
| --- | --- | --- | --- | --- | --- |
| OFFICIAL TASK → READY | Volledig officieel taakrecord, scope, bestanden, tests, rollback, afhankelijkheden | Menselijk officialiseringsbesluit | Unieke taak-ID en status-/tellingcontrole | Ontbrekende input of open scopebesluit | Geen mutatie; taak blijft niet actief |
| READY → HUMAN TASK START | Schone toegestane basis en uitvoeropdracht | GATE A | Masterplanstatus en volledige opdracht in run | Geen expliciete start of basisdrift | Geen mutatie; `READY`/`BLOCKED` |
| HUMAN TASK START → EXACT BASE COMMIT | Goedgekeurde volledige commit en lokaal bekende remote ref | GATE A | `main = origin/main = goedgekeurde commit`, schoon index/worktree | Commit/ref/status wijkt af | Stop op `main`; geen branch |
| EXACT BASE COMMIT → TASK BRANCH | Geldige naam, exacte taak, branch nog afwezig | GATE A binnen exacte taakscope | Regexzelftest en refmomentopname | Naamconflict, ongeldige naam of drift | Geen branch maken; terug naar basiscontrole |
| TASK BRANCH → IMPLEMENTATION AUTHORIZED | Juiste branch/basis en exact wijzigingsplan | GATE B | Branch-/HEAD-bewijs, whitelist, geplande validators | Gate/scope ontbreekt of branch fout | Branch blijft onveranderd |
| IMPLEMENTATION AUTHORIZED → SMALL COMMITS | Exact toegestane bestanden en implementatie | GATE B | FILE_CHANGE-notes, diffs, validators per wijziging | Onverwacht bestand, gedrag of gebruikerswijziging | Stop; niet-destructief corrigeren binnen branch |
| SMALL COMMITS → STATIC VALIDATION | Volledige lokale diff en config/toolingbasis | Bestaande GATE B | Theme Check pre/post, parser/lint en diffcheck | Nieuwe regressie, CLI/configmismatch of toolingfailure | Scenario A; nieuwe herstelcommit |
| STATIC VALIDATION → TASK-SPECIFIC TESTS | Statische gates geslaagd en vooraf bepaalde criteria | Bestaande GATE B | Taaktests en resultaten | Testfaal of onvoldoende bewijs | Scenario A; herstel en hertest |
| TASK-SPECIFIC TESTS → OPTIONAL REMOTE BRANCH PUSH | Lokale branch gereed voor remote review | GATE C indien push nodig | Commits, diff, securityscan, remote naam | Geen gate, remote drift of gevoelige data | Lokaal blijven; niets pushen |
| OPTIONAL REMOTE BRANCH PUSH → OPTIONAL DEVELOPMENT PREVIEW | Previewbehoefte, exacte scope en actueel target | GATE D indien preview nodig | Store/ID/naam/role/livecontrole en rollbackplan | Targetafwijking, live target of verboden ID | Geen push; stop en laat target beslissen |
| OPTIONAL DEVELOPMENT PREVIEW → HUMAN REVIEW | Statische/smokegates en previewbewijs indien gebruikt | GATE E voor zichtbaar/functioneel werk | Previewlink, journeys, screenshots, beperkingen; anders lokaal reviewbewijs | Preview faalt/afgekeurd of bewijs ontbreekt | Scenario B indien preview gebruikt, anders A |
| HUMAN REVIEW → MERGE APPROVAL | Beoordeelde diff, tests, previewfeedback, restrisico | GATE F | One-bundle, commitset en expliciet oordeel | Changes requested, nieuwe drift of open P0 | Branch corrigeren; A/B |
| MERGE APPROVAL → MERGE TO MAIN | Ongewijzigde goedgekeurde branch en actuele `main` | GATE F | Mergeplan met voorkeur `--no-ff`, parent-/targetbewijs | `main`/branch wijzigde of conflict ontstaat | Niet mergen; nieuwe review/basisbeslissing |
| MERGE TO MAIN → POST-MERGE VALIDATION | Expliciete mergecommit op `main` | Bestaande GATE F | Git-state, Theme Check en taaktests op `main` | Post-merge regressie of verkeerde inhoud | Scenario C via aparte hersteltaak |
| POST-MERGE VALIDATION → DONE FOR IMPLEMENTATION TASK | Alle criteria, bewijs en documentatie compleet | Menselijke taakgoedkeuring; geen GATE G | Masterplan, one-bundle, merge-/testbewijs, restrisico | Ontbrekende acceptatie of review | `REVIEW`/`BLOCKED`; live blijft onaangetast |

Optionele stappen mogen worden overgeslagen als de officiële taak ze niet vereist, maar de bijbehorende gate mag nooit stil als verleend worden geregistreerd.

## 33. Scenario-overzicht

`BC-TECH-004` voert geen van deze scenario's uit; de tabel definieert de toekomstige route.

| # | Scenario | Vereiste route/gates | Verplicht bewijs | Stop-/hersteluitkomst |
| ---: | --- | --- | --- | --- |
| 1 | Documentatietaak zonder code | Expliciete directe-main-toestemming; geen technische branch | Scope, diff, validators, one-bundle | Geen theme-/Shopifyactie; documentcorrectie via reviewcommit |
| 2 | Kleine Liquidfix | A, B; C/D/E indien nodig; F vóór merge | Branchbasis, Theme Check pre/post, Liquid-/taaktest, diff | Nieuwe offense/testfaal → scenario A/B |
| 3 | Kleine JavaScriptfix | A, B; relevante browser/smoke; C/D/E indien nodig; F | JS-parser/lint waar beschikbaar, journeys, Theme Check, diff | Runtime-/smokefaal → niet mergen, herstelbranch |
| 4 | Theme Check-offensefix | A, B, expliciete offense-scope, F | Exacte fingerprint voor/na, geen nevenverdwijning/regressie | Onverwachte fingerprintdelta → STOP en verklaren |
| 5 | Zichtbare PDP-wijziging | A, B, D, E, F | Desktop/mobiel/toetsenbord zodra baseline bestaat, productdatajourney, preview | Afkeur → scenario B; geen merge |
| 6 | Preview faalt | Bestaande D; geen E/F | Pushscope, target, fout-/smokebewijs | Stop; scenario B en nieuwe D voor herpush |
| 7 | Theme Check krijgt nieuwe offense | Geen volgende gate | Nieuwe fingerprint/severity/path/message en diff | Regressie herstellen of expliciet taak herbeslissen; niet suppressen |
| 8 | Task branch wijkt onverwacht van `main` af | Stop vóór volgende stap | Refs, merge-base, onverwachte commits/diff | Geen rebase/reset; menselijke basis-/integratiebeslissing |
| 9 | Development-theme blijkt niet unpublished | Stop vóór preview | Actuele store/theme/role/live-uitvoer | Geen alternatief target kiezen; aparte menselijke beslissing |
| 10 | Gebruiker keurt preview af | E weigert; geen F | Feedback gekoppeld aan commit/preview | Scenario B; branch behouden en gericht herstellen |
| 11 | Gebruiker keurt merge goed | F na complete review | Exacte commitset, diff, gates, restrisico, rollback | Alleen goedgekeurde niet-destructieve merge; daarna post-mergegate |
| 12 | Probleem na merge maar vóór live | Geen liveactie | Mergecommit, probleemreproductie, impact | Scenario C via aparte goedgekeurde hersteltaak |
| 13 | Probleem na live | Buiten implementatietaak | Release-/incidentbewijs en actuele livecontext | Scenario D; afzonderlijk BC-REL-/incident-/rollbackproces |

## 34. Verboden-actiematrix

| Actie | Status | Reden | Vereiste gate | Stop-/herstelactie |
| --- | --- | --- | --- | --- |
| Direct technische code committen op `main` | **VERBODEN** | Omzeilt isolatie en review | Geen gate kan dit binnen gewone implementatie toestaan | Stop; maak pas na A/basiscontrole een geldige task branch |
| Force push | **VERBODEN** | Herschrijft gedeeld bewijs/geschiedenis | Geen | Stop; gebruik nieuwe niet-destructieve commit |
| Rebase van gedeelde task branch | **VERBODEN** | Wijzigt reeds gedeelde hashes | Geen | Stop; integreer alleen na nieuw besluit zonder history rewrite |
| Merge zonder menselijk akkoord | **VERBODEN** | Omzeilt GATE F | F | Niet mergen; verzamel reviewbewijs |
| Previewpush zonder targetcontrole | **VERBODEN** | Kan verkeerde/live omgeving raken | D plus actuele targetcontrole | Stop; verifieer store/ID/naam/role/live opnieuw |
| Push naar live theme `189463068938` | **VERBODEN** binnen implementatieworkflow | Live is nooit developmenttarget | Alleen aparte G | Stop; start afzonderlijke releaseopdracht |
| Gebruik van theme `192796786954` | **VERBODEN** | Doel/eigenaarschap niet geverifieerd | Eerst aparte menselijke onderzoekstaak | Niet benaderen; geen alternatief gebruik aannemen |
| Theme pull als generieke synchronisatie | **VERBODEN** als standaard | Kan lokale basis stil overschrijven | Aparte read-only vergelijkingstaak | Stop bij vermoede drift; vergelijk eerst gecontroleerd |
| Brede/full-theme push zonder expliciete scope | **VERBODEN** | Onnodige impact en rollbackonduidelijkheid | D voor exact taakbereik | Beperk scope; leg flags/target/rollback vooraf vast |
| Suppressie van nieuwe Theme Check-offense | **VERBODEN** zonder apart besluit | Verbergt regressie | Afzonderlijke menselijke suppressiebeslissing | Herstel regressie of stop/rebaseline apart |
| Rebaseline zonder besluit | **VERBODEN** | Kan kwaliteitsverslechtering normaliseren | Afzonderlijke menselijke rebaseline | Behoud oude/nieuwe sets en stop gate |
| Branch automatisch verwijderen | **VERBODEN** | Kan review-/rollbackbewijs verliezen | Latere expliciete opruimtoestemming | Behoud branch en controleer bereikbaarheid/bewijs |
| Live rollback zonder aparte taak | **VERBODEN** | Productieactie met hoog risico | G plus incident-/rollbackopdracht | Stop; scenario D en menselijke leiding |
| Onverwachte remote drift negeren | **VERBODEN** | Basis en diff worden onbetrouwbaar | Nieuwe menselijke basisbeslissing; fetch alleen indien toegestaan | Stop; aparte read-only hercontrole en scopebesluit |

Alle overige technische mutaties zijn maximaal **EXPLICIETE TOESTEMMING VEREIST** binnen de officiële taak; read-only lokale controles zijn alleen **TOEGESTAAN** wanneer zij binnen scope blijven en geen verboden netwerk-/Shopifyactie impliceren.

## 35. Definition of Ready voor toekomstige implementatie

Een implementatietaak is pas `READY` wanneer minimaal:

- officiële unieke taak-ID, titel, doel, aanleiding en eigenaar vaststaan;
- scope en buiten-scope exact zijn;
- toegestane bestanden/systemen benoemd zijn;
- afhankelijkheden `DONE` of aantoonbaar beschikbaar zijn;
- goedgekeurde volledige `origin/main`-basiscommit vaststaat;
- branchnaam volgens de regex is voorgesteld;
- exacte code-/configwijziging en GATE B-beslisser bekend zijn;
- Theme Check pre-/postroute en verwachte fingerprintimpact zijn vastgelegd;
- taakgebonden smoke-/regressiecriteria zijn vastgelegd;
- previewbehoefte, target en gates D/E zijn bepaald;
- rollbackpositie en concrete herstelstappen bestaan;
- privacy/security/data/app-/runtimeimpact is beoordeeld;
- one-bundle UploadPaths en reviewbestanden zijn afgebakend;
- GATE A expliciet is verleend.

Een workflowdocument, kandidaat-ID of eerdere soortgelijke toestemming voldoet niet zelfstandig aan deze Definition of Ready.

## 36. Definition of Review voor toekomstige implementatie

Een implementatietaak mag pas `REVIEW` worden wanneer:

- werk uitsluitend op de juiste task branch en binnen whitelist is uitgevoerd;
- alle wijzigingen, commits, diffs en validators volledig zijn gelogd;
- Theme Check pre/post en fingerprintdelta zijn vastgelegd;
- geen onverklaarde nieuwe/uitgebreidere/ernstigere offense bestaat;
- taaktests en vereiste smoke-/regressiecontroles slagen;
- eventuele remote push GATE C had;
- eventuele development-preview GATE D en actuele targetcontrole had;
- zichtbaar/functioneel resultaat beschikbare preview-/reviewevidence heeft;
- rollbackstappen en restrisico actueel zijn;
- masterplan, taakstatus, bewijs, risico's en route zijn bijgewerkt;
- alle normale preflights zijn geslaagd;
- `FINAL_REPORT.md` daarna definitief is ververst en de one-bundle direct is gefinaliseerd.

Zichtbaar/functioneel werk blijft `REVIEW` tot expliciete menselijke acceptatie.

## 37. Definition of Merge Ready

Een branch is pas Merge Ready wanneer:

- exacte branch en commitset overeenkomen met de menselijke review;
- basis/merge-base en actuele `main` aantoonbaar zijn;
- volledige diff is beoordeeld en geen scope drift bevat;
- statische, taak-, smoke- en vereiste previewgates zijn geslaagd;
- GATE E is verleend wanneer previewacceptatie nodig was;
- alle reviewfeedback is opgelost of expliciet als restrisico geaccepteerd;
- one-bundle-bewijs compleet en beschikbaar is;
- post-mergevalidatie en scenario-C-herstelroute klaarstaan;
- GATE F nieuw en expliciet is verleend.

Merge Ready geeft geen GATE G en geen toestemming om een branch op te ruimen.

## 38. Open vragen

- Wordt later een formele GitHub Pull Request verplicht? Nu niet; dit vereist een apart governancebesluit.
- Onder welke exacte taken en voorwaarden wordt een read-only `fetch` toegestaan voor remote hercontrole?
- Welke volledige smoke-/browser-/viewport-/toetsenbordmatrix wordt menselijk goedgekeurd? `PROPOSED-TECH-02` blijft daarvoor een afzonderlijke kandidaat.
- Welke exacte pushflags ondersteunt de dan geïnstalleerde CLI en welke minimale file scope is per toekomstige previewtaak veilig? Dit wordt pas in die taak read-only vastgesteld.
- Wie beslist en documenteert eigenaarschap/doel van verboden theme `192796786954`?
- Welke retentietermijn en eigenaar gelden voor lokale one-bundle-runs en branches na menselijke review?

Geen open vraag mag stil worden ingevuld om een gate te passeren.

## 39. Risico's

| Risico | Gevolg | Beheersing | Reststatus |
| --- | --- | --- | --- |
| Runbook wordt als algemene toestemming gelezen | Ongecontroleerde implementatie | Officiële taak plus gates A-G blijven per taak verplicht | Doorlopend |
| Verkeerde basis/branch | Vermengde diff of verlies van isolatie | Exact `main = origin/main = basiscommit`; regex; stop bij drift | Doorlopend |
| Verkeerd previewtarget | Onbedoelde theme-/live-impact | GATE D, actuele zesdelige targetcontrole, verboden-ID-matrix | Hoog tot actuele controle slaagt |
| Baseline wordt kwaliteitsacceptatie | Technische schuld/regressie wordt genormaliseerd | Fingerprintdelta, geen suppressie, aparte fix-/rebaselinetaken | Doorlopend |
| Previewbewijs vervangt tests | Runtimefouten of onbewezen browserdekking | Taaktests plus afzonderlijke smoke-baseline | Smoke-basis nog open |
| Mergegoedkeuring wordt als livegoedkeuring gelezen | Onbedoelde release | GATE G en live state machine expliciet buiten scope | Doorlopend |
| Backup/unpublished theme wordt als rollback aangenomen | Onbruikbaar of verouderd productieherstel | Inhouds-/actualiteits-/compatibiliteitsbewijs vereist | Open tot releaseplan |
| FINAL_REPORT te vroeg geschreven | Late retries ontbreken in samenvatting | Definitieve refresh na preflight, direct finalizer, refresh bij failure | Operationeel beheerst |

## 40. Aanbevolen volgende stap

De projecteigenaar beoordeelt dit runbook, met name branchregex, gates A-G, previewtargetgrenzen, state machine, forbidden-actiematrix en rollbackscenario's. `BC-TECH-004` blijft `REVIEW` totdat die menselijke beoordeling expliciet is vastgelegd.

Na menselijke goedkeuring is de waarschijnlijk logische volgende technische governancebasis de afzonderlijke smoke-/regressie- en testbewijsbasis uit `PROPOSED-TECH-02`. Deze kandidaat wordt binnen `BC-TECH-004` **niet** officieel gemaakt, niet geactiveerd en niet uitgevoerd.

## 41. Veiligheidsbevestiging

Tijdens `BC-TECH-004`:

- is geen Git-branch gemaakt, gepusht, gemerged, gerebased, verwijderd of geforce-pusht;
- is alleen Git read-only gebruikt, behalve de expliciet toegestane fase-A-commit/push vóór de inhoudelijke uitvoering;
- is Shopify, Shopify Admin en geen enkel theme benaderd;
- is geen theme gepusht, gepulld, gepubliceerd, verwijderd, gedupliceerd of hernoemd;
- is theme `192770375946` niet benaderd en theme `192796786954` als verboden target gedocumenteerd;
- is geen Liquid-, JavaScript-, CSS-, JSON/JSONC-, locale-, section-, snippet- of templatebestand gewijzigd;
- is geen offense opgelost, suppressed of gerebaselined;
- is geen package of CLI geïnstalleerd/geüpdatet;
- is geen technische implementatie of scenario werkelijk uitgevoerd;
- zijn na de fase-A-commit uitsluitend dit document en `docs/MASTERPLAN.md` gewijzigd;
- volgt menselijke review vóór `DONE` en vóór de eerste daadwerkelijke technische codebranch.

## 42. Menselijke goedkeuring

De BadkamerCity-projecteigenaar heeft `BC-TECH-004` op 2026-08-16
goedgekeurd als definitieve technische wijzigings-, preview-, merge- en
rollbackwerkwijze binnen de governance-/documentatiescope.

Concreet zijn goedgekeurd:

- `main` als centrale integratie- en bron-van-waarheidbranch, met het verbod
  om theme-code rechtstreeks op `main` te implementeren;
- task branches vanaf een exact goedgekeurde basiscommit en de branchregex
  `^task/bc-[a-z]+-[0-9]{3}-[a-z0-9]+(?:-[a-z0-9]+)*$`;
- de afzonderlijke menselijke gates A-G voor task start, implementatie,
  remote branch push, development-previewpush, previewacceptatie, merge en
  live release, waarbij geen gate een latere gate impliceert;
- `BadkamerCity Development` (`192770375946`) uitsluitend als potentieel
  toekomstig previewtarget na nieuwe toestemming en actuele targetcontrole;
- theme `192796786954` als verboden target en live theme `189463068938` als
  nooit toegestaan developmenttarget;
- Theme Check als verplichte statische pre-/postgate, zonder stille
  suppressie of rebaseline en met nieuwe, uitgebreidere of ernstigere
  fingerprints als regressiesignaal;
- kleine logisch afgebakende implementatiecommits, geen force push, history
  rewrite of rebase van gedeelde technische task branches, geen automatische
  merge of branchverwijdering, afzonderlijke GATE F en `git merge --no-ff`
  als beleidsvoorkeur voor een later expliciet goedgekeurde merge;
- rollbackscenario's A-D: vóór merge zonder preview, vóór merge na een
  development-preview, na merge vóór live en na live uitsluitend via een
  afzonderlijk release-/incidentproces;
- de FINAL_REPORT-volgorde: normale controles, normale preflight,
  definitieve rapportrefresh en daarna direct finaliseren; na een
  finalisatiefout eerst fout en herstel loggen, daarna het rapport opnieuw
  verversen en opnieuw finaliseren.

De bestaande open vragen in hoofdstuk 38 en restrisico's in hoofdstuk 39
blijven van kracht. Tijdens deze goedkeuring is geen branch gemaakt, Shopify
niet benaderd en geen theme-code gewijzigd. Deze goedkeuring is een
procesbesluit en geeft geen algemene implementatie-, preview-, merge- of
releasetoestemming.
