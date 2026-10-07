# BadkamerCity — instructies voor AI, Codex en ontwikkelaars

## 1. Verplichte bronvolgorde

Bij **elke** taak:
1. Lees `docs/HANDOVER_START_HERE.md` en `docs/AI_HANDOFF_CURRENT.md`.
2. Gebruik `docs/LIVE_STATUS_AND_NEXT_STEPS.md` voor de *gedateerde* status, `docs/THEME_COMPONENT_REFERENCE.md` / `docs/THEME_CODE_MAP_2026-10-07.json` voor bestandsafhankelijkheden, en `docs/SHOPIFY_ADMIN_STRUCTURE_2026-10-07.json` voor read-only Admin-context.
3. Controleer in Shopify **welk thema NU MAIN is**; op 2026-10-07 was dat `194864677130`, maar na publicaties kan dat veranderen.
4. Controleer werkelijke lokale Git-repo/origin/branch/worktree. Remote GitHub-commit bewijst **niet** dat Windows lokaal schoon is.
5. Lees de relevante historische bronnen `docs/MASTERPLAN.md` en detailaudits als achtergrond; deze bevatten expliciet oude theme-ID's, oude projectstatus en eerder gemelde blokkades. Ze mogen niet stil als actuele productiegegevens worden gebruikt.
6. Behoud expliciete veiligheids-/goedkeuringsregels en rapporteer tegenstrijdigheden in plaats van ze weg te redeneren.

**Bronprioriteit bij inconsistenties:** recente expliciete gebruikersinstructie en veiligheidsgrenzen → verse read-only Shopify/Git/meting → gedateerde actuele handoff → historische logs/masterplan. Een oud plan dat “implementation blocked” zegt bewijst **niet** dat later geïmplementeerde en gepubliceerde onderdelen nog ontbreken; het bevat wel belangrijke oorspronkelijke besluiten en open vragen.

## 2. Wat altijd verboden is zonder aparte toestemming

- Live/MAIN-thème bestanden schrijven of zelfstandig publiceren/omwisselen.
- Bestaande lokale wijzigingen verwijderen, force-push, `git reset --hard`, `git clean -fd` of iets overschrijven enkel om “schoon” te zijn.
- Producten/prijzen/voorraad/BTW/verzend- of betaalinstellingen massaal muteren.
- Uit ontbreken van data verzonnen specificaties, setcomponenten, levertijden, voorraadaantallen, beoordelingen, kortingen of klantbeloftes afleiden.
- Externe filters voor alle bezoekers activeren zonder VPS/API/index/fallbacktests.
- Onbewezen tests, Search Console-rankings of performance als succesvol opschrijven.
- Tokens, VPS-wachtwoorden, app secrets, klant-/ordergegevens, privécontracten of API-auth in publieke code, documentatie, screenshots of logs zetten.

**Standaardbeleid:** theme-wijzigingen via een bewezen identiek `UNPUBLISHED` conceptthema; merchant beoordeelt en publiceert. Shopify Admin-datamutaties alleen op expliciete opdracht, met read-after-write, risico en rollback.

## 3. Een taak aanpakken

- Maak de vraag concreet: gebruikersdoel, beoogde URL, bestaande UX, scope, desktop/mobiel, SEO/data-impact en acceptatie.
- Traceer de daadwerkelijke route: `templates/*.json → sections/*.liquid → snippets/*.liquid → assets/*` én Shopify Admin.
- Scheid `VERIFIED_THEME`, `VERIFIED_ADMIN`, `USER_APPROVED_UI`, `IMPLEMENTED_TEST_ONLY`, `HISTORICAL` en `NOT_VERIFIED`.
- Maak een kleine veilige wijziging op featurebranch/draft, doe tests en leg alleen bewezen resultaat vast.
- Schrijf bij verandering van contract/architectuur ook de relevante actuele handoff bij.
- Maak elke niet-uitgevoerde test zichtbaar als `NOT_TESTED/BLOCKED`; gebruik geen generieke “klaar”.
- Controleer git status en theme ID na afloop, plus wat de volgende sessie als eerste moet doen.

## 4. Codex lokaal: bestaand uitvoeringslogboek

De repository heeft een uitgebreid historisch, menselijk beoordeeld lokaal bewijsprotocol:
`docs/CODEX_EXECUTION_LOG_PROTOCOL.md` en PowerShell helpers
`scripts/codex-run-init.ps1`, `codex-run-command.ps1`,
`codex-run-note.ps1` en `codex-run-finalize.ps1`.

**Wanneer je een lokale Codex-uitvoeringssessie binnen die workflow uitvoert**, lees dat protocol volledig en gebruik de scripts/logfiles zoals gespecificeerd. Bewijsbundels blijven lokaal genegeerd onder `docs/_codex_runs/`; sla daarin geen secrets op. 
**Wanneer je via ChatGPT/GitHub/Shopify-connectors werkt zonder toegang tot de Windows-pc**, claim je NIET dat lokale Codex-wrappers of browserchecks zijn uitgevoerd; gebruik connector-readbacks, branch/commit/diff en bronmomenten als bewijs en noteer de beperking. Een connector-actie is niet automatisch een volledige lokale Codex-run.

## 5. Vaste correctheidswaarschuwingen

- `docs/MASTERPLAN.md` versie 0.26.3 beschrijft september 2026; de huidige gepubliceerde theme-code is sindsdien ver ontwikkeld. Historische gegevens behouden, actuele stand in nieuw dossier.
- De Badkamermeubels-mobiel/desktopweergave leunt op **drie inline style-blokken in Shopify collection descriptionHtml**. Alleen code uit Git inspecteren kan die afhankelijkheid missen.
- De actuele `main` bevat een geverifieerde theme-snapshot, niet de volledige Shopify-productdatabase/menu-instellingen/externe VPS.
- `custom.*` in bepaalde PDP-code komt niet altijd overeen met de actuele `specs.*`-definities; verifieer echte waarden vóór migratie.
- Externe filters zijn opt-in bij `wastafelkranen?bcfilters=1`; niet sitebreed klaar.
- Een Shopify `ACTIVE` productstatus is niet identiek aan aantoonbare Online Store-publicatie en voorraad.
- GitHub is **publiek**. Verifieer privacy en rechten bij elk nieuw bestand.

## 6. Werk- en reviewoverdracht

Minimaal vastleggen: taak/reden, eerdere/current MAIN, branch/commit, betrokken codefiles en Admin-objecten, aangewezen review/merchant, tests met resultaat en viewport/URL, niet-geteste onderdelen, terugzetpad en actuele documentatie. Voor praktische scenario's: `docs/WORKED_EXAMPLES_AND_HANDOFF_TEST.md`, `docs/TROUBLESHOOTING.md` en `docs/RELEASE_AND_QA.md`.

**Je doel is dat een volgende ontwikkelaar de volgende veilige stap kan zetten op basis van bewijs, niet op basis van aannames.**
