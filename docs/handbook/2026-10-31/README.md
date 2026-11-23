# Bron van de praktische naslagwerkuitbreiding

Deze map voegt 32 hoofdstukken (48–79) toe aan het bestaande [volledige naslagwerk](../../MASTER_SITE_REFERENCE.md). De bestaande productcatalogus is hoofdstuk 80 geworden. De eerste samenvattingen zijn geactualiseerd en oude registers blijven expliciet gedateerd.

- `PRACTICAL_REFERENCE.md`: inhoudelijk beheerverhaal en componentcontracten.
- `practical-tasks.json`: 50 vragen met eigenaar, bron, controle, hoofdstuk en status; ook gebruikt door de HTML-takenzoeker.
- `diagnosis.json`: 40 symptoom-/bron-/eigenaar-/regressiepaden.
- `acceptance.json`: 50 concrete proeven; ontwerp, eerder bewijs en verse GETs expliciet gescheiden.
- [Verse bronkaart en testgrenzen](../../site-reference/2026-10-31/README.md).

De master is het volledige leesdocument; deze bestanden zijn de onderhoudsbron voor de nieuwe secties. Gebruik `tooling/compile-practical.py` om alleen hoofdstukken 48–79 idempotent uit deze bestanden te hercompileren. Het script verandert de oude registers en actuele samenvattingen niet.

## HTML opnieuw opbouwen

Gebruik Node met `marked` beschikbaar via `CODEX_PRIMARY_RUNTIME_NODE_MODULES`, of lokaal geïnstalleerd als module. Vanuit de repository:

```bash
python docs/handbook/tooling/compile-practical.py .
node docs/handbook/tooling/render-handbook.cjs . /absolute/output/Badkamercity-volledig-naslagwerk-2026-10-31.html
node docs/handbook/tooling/check-handbook.cjs /absolute/output/Badkamercity-volledig-naslagwerk-2026-10-31.html /absolute/output/document-validation.json
```

De checker gebruikt `jsdom`; indien dat niet lokaal is geïnstalleerd, geeft `HANDBOOK_JSDOM_MODULE` het absolute modulepad aan. Versies bij deze ronde: marked 17.0.5 en jsdom 26.1.0. Er worden geen pakketten, winkelwrites of netwerkrequests door de renderer/checker uitgevoerd. De HTML bevat alle tekst, stijlen, zoeklogica, taken en het publieke productrouteregister.

De checks bewijzen structuur en offline DOM-functionaliteit. Ze bewijzen geen echte browserlayout, fysieke telefoonweergave, mailaflevering, productkoop of checkout. Brede brontabellen zijn lokaal scrollbaar; dat staat los van het categoriebarcontract van de winkel.
