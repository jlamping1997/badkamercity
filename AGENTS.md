# Codex-projectinstructies

> **ACTUELE STAND 2026-10-07:** lees vóór elke taak `docs/AI_HANDOFF_CURRENT.md` en het manifest `docs/BASELINE_MANIFEST_2026-10-07.json`. De geverifieerde live-snapshot heeft theme-ID `194864677130`; verifieer de rol `MAIN` opnieuw in Shopify. De hieronder vermelde oude theme-ID's, status “implementation blocked” en taaknummers zijn historische context. **Behouden blijven**: geen ongeautoriseerde live-publicatie, geen ongecontroleerde Shopify Admin-mutatie, geen geheime data loggen/committen, reviewer/gebruikersgoedkeuring en geen destructieve Git-clean. Lees ook het historische masterplan voor oorspronkelijke besluiten.


`AGENTS.md` is alleen een permanente instructie voor Codex. `docs/MASTERPLAN.md` blijft de centrale bron van waarheid.

- Lees voor iedere taak eerst volledig `docs/MASTERPLAN.md`.
- Gebruik het dashboard, de actieve taak, het taakregister, de besluiten, open vragen, risico's en actuele route als leidraad.
- Voer alleen de expliciet actieve en toegestane taak uit.
- Verzin geen ontbrekende informatie.
- Markeer ontbrekende informatie volgens het masterplan.
- Wijzig nooit live theme `189463068938` zonder afzonderlijke expliciete menselijke toestemming.
- Gebruik theme `192770375946` uitsluitend voor previews wanneer een latere taak dit expliciet toestaat.
- Wijzig geen Shopify Admin-data zonder afzonderlijke expliciete opdracht.
- Publiceer nooit zelfstandig naar live.
- Werk na iedere afgeronde taak het masterplan bij, waaronder minimaal dashboard, taakstatus, bewijsregister, open vragen, risico's, actuele route en wijzigingslog.
- Zichtbaar of functioneel werk blijft `REVIEW` totdat de projecteigenaar het expliciet heeft goedgekeurd.
- Stop en rapporteer bij tegenstrijdigheden of onverwachte wijzigingen.

## Verplicht Codex-uitvoeringslogboek

- Lees voor iedere taak eerst volledig docs/CODEX_EXECUTION_LOG_PROTOCOL.md.
- Initialiseer voor inhoudelijk werk een lokale run met
  scripts/codex-run-init.ps1.
- Voer ieder inhoudelijk shellcommando uit via
  scripts/codex-run-command.ps1.
- Leg iedere interne bestandsbewerking vast met een FILE_CHANGE-note via
  scripts/codex-run-note.ps1 en een gelogde volledige Git-diff.
- Behoud mislukte opdrachten, foutuitvoer en herstelpogingen met eigen
  step-ID's; overschrijf eerder bewijs niet.
- Bewaar grote uitvoer volledig onder de rawmap en houd terminaluitvoer
  beperkt tot korte statusregels.
- Houd alle runs lokaal onder docs/_codex_runs/ en commit deze genegeerde
  bewijsmap nooit.
- Rond geen taak af zonder niet-lege FULL_EXECUTION_LOG.md,
  FINAL_REPORT.md, UPLOAD_MANIFEST.md, REVIEW_FILES_MANIFEST.md en een
  gecontroleerde runbundle.
- Draag een normale menselijke review aan ChatGPT over met een enkele
  `<RUN_ID>_BUNDLE.zip`; afzonderlijke handmatige upload-ZIP's zijn niet
  nodig.
- Laat de finalizer alle te beoordelen repositorybestanden uit UploadPaths
  onder `review_files/` opnemen met behoud van repositorystructuur en
  bewezen bron-/kopiehashes in REVIEW_FILES_MANIFEST.md.
- Laat de finalizer voor succes mechanisch bewijzen dat ieder raw
  commandrecord een compleet command-/stdout-/stderr-/meta-quartet heeft.
- Maak alleen na een aantoonbare finalisatiefout en een expliciete
  menselijke herstelopdracht een alternatief reviewpakket.
- Log nooit secrets, credentials, klantgegevens, ordergegevens,
  persoonsgegevens of verborgen interne redeneerstappen.
- Herstel na contextcompactie eerst de context uit AGENTS.md, het
  masterplan, het protocol en het actuele uitvoeringslog en voeg een
  CONTEXT_RESTORED-note toe.
- Alleen de gebruiker beslist welke bestanden naar ChatGPT worden
  geupload en wanneer lokale runbestanden worden verwijderd.
- Dit loggingprotocol wijzigt geen enkele Shopify-, theme-,
  livepublicatie- of menselijke goedkeuringsregel in dit bestand of het
  masterplan.
