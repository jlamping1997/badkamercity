# BadkamerCity Codex-uitvoeringslogprotocol

## 1. Doel

Dit protocol maakt iedere Codex-taak achteraf controleerbaar. Het bewaart
observeerbare opdrachten, uitvoer, exitcodes, fouten, herstelhandelingen,
bestandswijzigingen, validators en eindcontroles lokaal, terwijl de
terminal alleen korte statusregels toont.

## 2. Toepassingsgebied

Het protocol geldt voor iedere toekomstige Codex-taak in CITY_MASTER. Het
geldt vanaf de voorcontrole tot en met eindrapport, uploadmanifest en
runbundle. Taakspecifieke veiligheidsgrenzen uit het masterplan en de
menselijke opdracht blijven altijd leidend.

## 3. Wat wel en niet wordt gelogd

Wel gelogd:

- observeerbare shellcommando's en hun beschrijving;
- stdout, stderr, exitcode, verwachte exitcodes en duur;
- feitelijke keuzes, validatorresultaten en bewijs;
- interne bestandsbewerkingen via een note plus Git-diff;
- fouten, mislukte pogingen en herstelacties;
- eindstatus, Git-status en uploadselectie.

Niet gelogd:

- credentials, klant-, order- of persoonsgegevens;
- inhoud van credentialstores of omgevingsbestanden;
- onobserveerbare of verborgen interne modelprocessen;
- data die buiten de expliciete taakscope valt.

## 4. Geen verborgen interne redeneerstappen

Chain-of-thought, verborgen redeneerstappen en interne modeltoestanden
worden niet opgeslagen. Het log bevat alleen controleerbare handelingen,
resultaten, korte beslisredenen en bewijs dat een menselijke reviewer kan
verifieren.

## 5. Beveiliging en redactie

Voer geen commando uit dat vermoedelijk secrets of persoonsgegevens naar
stdout of stderr schrijft. Bij onverwachte gevoelige uitvoer:

1. schrijf de gevoelige waarde niet naar raw;
2. vervang alleen de waarde door [REDACTED];
3. noteer SECURITY_REDACTION zonder de waarde te herhalen;
4. bewaar geen ongeredigeerde kopie;
5. stop bij twijfel voor menselijke controle.

Een Sensitive-stap bewaart alleen [REDACTED SENSITIVE STEP] als opdracht
en uitvoer. Beschrijvingen moeten zelf ook vrij van gevoelige informatie
zijn.

## 6. Run-ID

De conventie is:

    <TASK_ID>_yyyyMMdd-HHmmss

Voorbeeld:

    BC-GOV-006_20260811-131019

Een Run-ID bevat alleen letters, cijfers, punten, underscores en
koppeltekens. Hergebruik mag bestaande evidence nooit overschrijven.

## 7. Directorystructuur

Iedere run staat lokaal onder:

    docs/_codex_runs/<RUN_ID>/

De map docs/_codex_runs/ is permanent genegeerd door Git. De ZIP is een
sibling van de runmap binnen dezelfde genegeerde hoofdmap:

    docs/_codex_runs/<RUN_ID>_BUNDLE.zip

Bundelvorming gebruikt tijdelijk:

    docs/_codex_runs/<RUN_ID>_BUNDLE.building.zip

Alleen een volledig gevalideerde tijdelijke ZIP wordt naar de finale naam
verplaatst. Een bestaande finale bundle wordt nooit overschreven.

## 8. Bestandsstructuur per run

    docs/_codex_runs/<RUN_ID>/
    |-- 00_REQUEST.txt
    |-- 01_CONTEXT.md
    |-- FULL_EXECUTION_LOG.md
    |-- CHANGES.md
    |-- FINAL_REPORT.md
    |-- UPLOAD_MANIFEST.md
    |-- REVIEW_FILES_MANIFEST.md
    |-- review_files/
    |   |-- AGENTS.md
    |   |-- docs/
    |   +-- scripts/
    +-- raw/
        |-- 001-command.txt
        |-- 001-stdout.txt
        |-- 001-stderr.txt
        +-- 001-meta.json

00_REQUEST bewaart de menselijke opdracht. 01_CONTEXT bewaart de veilige
Git- en omgevingsbasis. FULL_EXECUTION_LOG is de chronologische bron.
CHANGES registreert edits. FINAL_REPORT vat samen. UPLOAD_MANIFEST bepaalt
de controleerbare uploadselectie. REVIEW_FILES_MANIFEST bewijst per
repositorysnapshot bronpad, bytes en gelijke bron-/kopiehashes.
review_files bevat de te beoordelen repositorybestanden uit UploadPaths
met behoud van hun relatieve structuur. Raw bevat verliesvrije stapuitvoer.

## 9. Commandologging

Elk inhoudelijk shellcommando loopt via scripts/codex-run-command.ps1.
Iedere stap heeft een uniek, oplopend driecijferig ID. Het exacte commando
wordt voor uitvoering opgeslagen. Bestaande stepbestanden worden nooit
overschreven. Het child PowerShell-proces gebruikt expliciet
`$ErrorActionPreference = 'Stop'`, zodat een cmdletfout via de bestaande
catch als child failure eindigt. De native-commandsemantiek en expliciete
verwachte exitcodes blijven ongewijzigd.

## 10. Stdout en stderr

Stdout en stderr worden altijd afzonderlijk vastgelegd. Lege streams
krijgen een bestaand bestand met nul bytes. De terminal toont de streams
niet automatisch. Het log verwijst naar beide raw-bestanden.

## 11. Exitcode en verwachte exitcodes

Iedere stap krijgt een expliciete lijst verwachte exitcodes. De werkelijke
child-exitcode staat in metadata. Een verwachte niet-nulcode, bijvoorbeeld
een bewuste failuretest, is geen taakfout. Een onverwachte code krijgt
UNEXPECTED_EXIT en vereist een aparte ERROR-, RECOVERY- of stopnote.
Een PowerShell-cmdletfout krijgt door de child-preamble exitcode 1, tenzij
een eerder afzonderlijk goedgekeurde wrapper aantoonbaar een andere code
definieert.

## 12. Tijd, duur en werkmap

Metadata bevat ISO-8601 start- en eindtijd, duur in milliseconden, absolute
werkmap en een korte beschrijving. Lokale tijdzone-informatie blijft in de
ISO-waarde behouden.

## 13. UTF-8

Protocolbestanden en raw-uitvoer worden met ingebouwde .NET-functionaliteit
als UTF-8 zonder BOM geschreven waar Windows PowerShell 5.1 dit
betrouwbaar ondersteunt. Het child PowerShell-proces stelt console- en
pipeline-output expliciet op UTF-8. Zelftests gebruiken meerbytekarakters.

## 14. Grote-outputbeleid

Een stream mag volledig inline wanneer hij hoogstens 200 regels en
hoogstens 64 KiB bevat. Bij overschrijding blijft het raw-bestand volledig
bewaard en bevat FULL_EXECUTION_LOG:

- relatief raw-pad;
- bytes en regelaantal;
- SHA-256;
- eerste twintig regels;
- laatste twintig regels;
- exitcode in de stapmetadata.

De terminal toont nooit de volledige grote uitvoer.

## 15. Raw-bestanden en hashes

Per commandostap bestaan command, stdout, stderr en meta.json. Metadata
bevat bytes, regels en SHA-256 voor stdout en stderr. Hashes worden pas na
sluiten van de bestanden berekend. Sensitive-stappen publiceren geen hash
van ongeredigeerde inhoud.

Voor bundelvorming valideert de finalizer mechanisch dat ieder meta.json
exact een command-, stdout- en stderrbestand heeft, dat er geen orphan
streambestand bestaat en dat command- en note-step-ID's geldig en uniek
zijn. StepId, verplichte metadata, streampaden, bytes, regels en voor
niet-sensitive stappen SHA-256 moeten overeenkomen. Sensitive-stappen
worden uitsluitend op de geredigeerde markers gecontroleerd. Een
onvolledig quartet maakt finalisatie `FAILED`.

## 16. Bestandsbewerkingen

Een interne Codex-edit is geen shellcommando. Na iedere gemaakte of
gewijzigde tracked file zijn daarom verplicht:

- FILE_CHANGE-note met pad, reden, type en tijd;
- voor- en nastatus voor zover aantoonbaar;
- volledige gelogde Git-diff;
- diffstat;
- relevante parser-, syntax- of structuurcontrole;
- eventuele fout en herstelactie.

Een edit zonder note plus diff is een protocolfout. Verwijderen en
hernoemen vereisen ook een note, maar mogen alleen wanneer de taak dat
expliciet toestaat.

## 17. Fouten en herstel

Mislukte opdrachten blijven bestaan. Een tweede poging krijgt een nieuw
step-ID. De eerste command-, output-, error- en metafiles worden niet
gewijzigd. Een RECOVERY-note beschrijft aantoonbare oorzaak, gekozen
herstel en nieuwe validatie. Een fout wordt nooit stil als succes
gepresenteerd.

## 18. Contextcompactie en hervatten

Na contextcompactie of hervatten leest Codex eerst:

1. AGENTS.md;
2. docs/MASTERPLAN.md;
3. docs/CODEX_EXECUTION_LOG_PROTOCOL.md;
4. het actuele FULL_EXECUTION_LOG.md;
5. FINAL_REPORT.md indien aanwezig.

Daarna volgt een CONTEXT_RESTORED-note met laatst voltooide step-ID,
actuele Git-status, toegestane bestanden, open stappen en afwijkingen. Het
lokale log is de controleerbare uitvoeringsbron, niet ingeklapte
terminalhistorie.

## 19. Git-status en diffcontrole

Leg bij start, voor iedere commitgrens en bij einde vast:

- branch;
- HEAD en origin/main;
- staged, modified, deleted, renamed en untracked paden;
- ignored status van de runmap;
- git diff --check;
- whitelist van toegestane tracked wijzigingen.

Gebruik geen remote-URL-opdracht die credentials kan tonen.

## 20. Eindrapport

FINAL_REPORT.md bevat taak- en masterplanstatus, commits/pushes binnen de
opdracht, gemaakte bestanden, testresultaten, stap- en notetellingen,
verwachte en onverwachte failures, herstel, Git-status, beperkingen,
veiligheidsbevestiging en aanbevolen menselijke vervolgstap.

## 21. Uploadmanifest

UPLOAD_MANIFEST.md combineert de expliciet gevraagde commitbestanden,
lokale tracked wijzigingen en verplichte bewijsartefacten. Iedere normale
regel bevat relatief pad, volledig Windows-pad, bytes, SHA-256, Git-status
en uploadreden.

UploadPaths bepalen daarnaast welke gewone repositorybestanden onder
review_files worden gesnapshot. Paden buiten de repository, directories,
directory traversal, bestanden onder docs/_codex_runs en gevoelige klassen
zoals `.env*`, private keys, `*.pem`, `*.pfx`, `*.p12`, `id_rsa*` en `.git/`
worden niet als reviewbestand geaccepteerd. Runbestanden worden niet
gedupliceerd. REVIEW_FILES_MANIFEST.md legt hashgelijkheid vast.

Een manifest kan zijn eigen uiteindelijke hash wiskundig niet in zichzelf
vastleggen. De eigen regel is daarom SELF_REFERENCE en een expliciet
gelabelde pre-self-record snapshothash wordt apart genoemd. Dit is geen
ontbrekend bewijs maar een cryptografische zelfreferentiegrens.

## 22. Runbundle

scripts/codex-run-finalize.ps1 maakt:

    docs/_codex_runs/<RUN_ID>_BUNDLE.zip

De ZIP bevat alle run- en raw-bestanden zoals zij direct voor bundelvorming
bestonden, plus REVIEW_FILES_MANIFEST.md en review_files met de geselecteerde
repositorysnapshots, nooit de ZIP zelf. De finalizer opent eerst de
`.building.zip` read-only, controleert entries en reviewhashes en berekent
na promotie de SHA-256. De lokale manifest- en logaanvulling met die
ZIP-hash is noodzakelijkerwijs nieuwer dan hun pre-bundle kopie in de ZIP;
deze snapshotgrens wordt expliciet vermeld.

De tijdelijke ZIP wordt pas na validatie van alle runbestanden, raw
evidence, reviewbestanden en reviewhashes naar `<RUN_ID>_BUNDLE.zip`
verplaatst. Bij een fout wordt uitsluitend de tijdelijke ZIP verwijderd.
De normale menselijke ChatGPT-overdracht bestaat hierdoor uit een finale
bundle; losse MASTERPLAN-, AGENTS-, protocol- of scriptuploads zijn niet
nodig.

## 23. Terminaluitvoer

Elke helper toont exact een korte statusregel. Volledige stdout, stderr,
diffs en rapportinhoud blijven in de runmap. Het menselijke eindantwoord
bevat hoogstens de gevraagde korte samenvatting en uitsluitend de finale
`<RUN_ID>_BUNDLE.zip`. Afzonderlijke handmatige review-ZIP's zijn alleen
toegestaan na een aantoonbare finalisatiefout en een expliciete menselijke
herstelopdracht.

## 24. Secret- en privacyregels

Nooit loggen:

- wachtwoorden, tokens, API-secrets of private keys;
- sessiecookies of Authorization-headers;
- volledige credentials of credentialstore-inhoud;
- klant-, order- of persoonsgegevens;
- inhoud van .env-bestanden.

Secret-scans zoeken alleen herkenbare tokenformaten of sleutel-waarde-
toewijzingen met een concrete waarde. Losse beleidswoorden veroorzaken
geen hit. Een hitrapport noemt alleen patroon-ID, pad, regel en een hash
van de match, nooit de waarde.

## 25. Uitzonderingen

De enige bootstrapuitzondering geldt wanneer de helpers nog niet bestaan.
Dan worden runmap, eerste context en bootstrapcommando's handmatig
vastgelegd. Zodra scripts parser- en basisruntimecontroles halen, loopt
ieder volgend inhoudelijk commando via de commandhelper.

Een taak mag aanvullende strengere grenzen opleggen. Dit protocol maakt
nooit een Shopify-, live-, data-, internet-, package- of implementatieactie
toegestaan.

## 26. Retentie

Runs blijven lokaal en genegeerd totdat de projecteigenaar de review en
eventuele upload heeft afgerond. Alleen de gebruiker bepaalt retentie en
verwijdermoment. Automatische opschoning is verboden. Een latere
retentieperiode blijft OPEN BESLISSING.

## 27. Definition of Done voor logging

Logging is technisch gereed wanneer:

- aanvraag en context bestaan;
- alle inhoudelijke commands raw evidence en metadata hebben;
- alle tracked edits note plus diff hebben;
- fouten en herstel zichtbaar blijven;
- parser-, functionele, grote-output-, UTF-8-, ignore-, Git- en
  securitytests eerlijk zijn vastgelegd;
- FINAL_REPORT en UPLOAD_MANIFEST niet leeg zijn;
- ieder raw command-quartet compleet en hashgeldig is;
- REVIEW_FILES_MANIFEST bestaat en alle review_files-hashes gelijk zijn;
- tijdelijke ZIP read-only opent en exact de verwachte run-, raw- en
  reviewbestanden bevat;
- `.building.zip` na succesvolle promotie verdwenen is;
- finale ZIP opent, zichzelf niet bevat en een SHA-256 heeft;
- de runmap genegeerd is;
- terminaluitvoer compact bleef;
- menselijke review nog expliciet wordt gevraagd.

## 28. Voorbeeldworkflow

1. Lees AGENTS.md, masterplan en dit protocol.
2. Initialiseer de run met codex-run-init.ps1.
3. Valideer Git-basis via codex-run-command.ps1.
4. Noteer menselijke input of besluit via codex-run-note.ps1.
5. Bewerk alleen toegestane bestanden.
6. Log per edit FILE_CHANGE plus volledige Git-diff en diffstat.
7. Voer parsers en validators via de commandhelper uit.
8. Schrijf FINAL_REPORT.md.
9. Voer eindcontroles en securityscan uit.
10. Geef alle te beoordelen repositorybestanden als UploadPaths mee.
11. Laat de finalizer raw evidence en review_files mechanisch controleren.
12. Laat de tijdelijke ZIP valideren en naar de finale bundle promoveren.
13. Upload normaal alleen de finale bundle.
14. Laat de taak op REVIEW zonder ongeautoriseerde commit of push, tenzij
    dezelfde opdracht expliciet commit- en pushtoestemming bevat.

## 29. Voorbeeld terminal-eindblok

    Taak afgerond en bewijs lokaal opgeslagen.
    Taakstatus: <status>
    Masterplan: <versie>
    One-bundle review: GESLAAGD
    Raw evidence completeness: GESLAAGD
    Bundle SHA-256: <hash>

    === BESTAND OM NAAR CHATGPT TE UPLOADEN ===
    docs/_codex_runs/<RUN_ID>_BUNDLE.zip
    <volledig Windows-pad naar de bundle>
    === EINDE UPLOADLIJST ===

Na de eindmarker volgt geen tekst.

## 30. Rollback en protocolwijzigingen

Tracked protocolbestanden worden alleen via een afzonderlijke beoordeelde
commit gewijzigd of teruggedraaid. Een herstelcommit is te verkiezen boven
geschiedenis herschrijven. Lokale runbestanden mogen pas na menselijke
review handmatig worden verwijderd. Wijzigingen aan dit protocol vereisen
een eigen taak, nieuwe zelftests en menselijke goedkeuring.
