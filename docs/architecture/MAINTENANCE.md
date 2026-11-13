# Onderhoud en overdracht voor een nieuwe ontwikkelaar of AI

## Huidige bron kiezen — 8 november 2026

Begin bij het [centrale auditrapport](../audits/2026-11-08/README.md). MAIN **196328685834** en `shopify/current/` verschillen nog op 15 paden; 9 livebestanden ontbreken in Git. Een oude snapshot van 31 oktober of repositoryroot is geen complete livebron. Haal vóór een conceptwijziging verse rol, manifest en bytes op en verklaar verschillen; behoud actuele liveaanpassingen.

Volg voor footerwerk eerst de echte branch: `compact_homepage=true` → home `bc-home-footer`; andere storefront-routes → standaard `bcf-v3`. De kolommen zijn eigen blocks, niet Voettekstmenu. Het [canonieke voorstel voor 17 blokken](components/FOOTER.md) blijft PROPOSED; 18 blocks is het maximum en 8 huidige slots hebben lege URL's. Koppel een verzendlink pas aan een bestaande juiste openbare bestemming; behoud de return-/quoteguards. Vergelijk daarna de 14 routeklassen en relevante browserstaten. Een documentatieactualisering sluit de implementatie-/runtimecontroles niet.

Het afzonderlijke filtertraject volgt het nieuwste [centrale checkpoint](../LIVE_STATUS_AND_NEXT_STEPS.md). FILTER-SIMPLE-02v2 is LIVE/VERIFIED; de Acero→Grijs-correctie heeft een eigen uitvoeringsstap. De v2-installer niet herhalen.

Begin bij [actuele status](../LIVE_STATUS_AND_NEXT_STEPS.md) → [dekking](COVERAGE.md) → functioneel dossier → technische naslag → exact benoemde bron. De Git-root is geen automatisch actuele productiebron. Gebruik het theme-ID, de hash en de echte Admin-toewijzing, niet alleen een bestandsnaam uit een oud releaseverslag.

## Waar wijzig je wat?

| Vraag | Eerste beheerbron | Daarna controleren |
| --- | --- | --- |
| Footerlink/label | Footersectie/block in Theme Editor | Bestemming, drie kolommen en mobiel; niet een willekeurig footermenu |
| Header-/categorieboom | Gekoppeld Shopify-menu | Header desktop/mobiel, hubs, categorie-/adviesconsumers |
| Homepageblok | `index.json` / Theme Editor | Order, disabled, Liquid-dataguard, beelden en CTA |
| Collectiepagina | Collectietoewijzing/body en gekozen sectie | Native lijst versus hub, SPLIT, menukinderen en Admin-CSS |
| Productinfo | Officiële productbron → getypeerd Shopify-veld | Scope/renderer, kaart/PDP, gegenereerde keuze- en indexconsumers |
| Productkleur/uitvoering | Expliciete relatie/dataset/router | Exacte productidentiteit, bronrevisie, fallback, navigatie/cartlock |
| Begrip | Page + lijstblock + redirect | Gepubliceerd doel, headingstructuur, lokale search/TOC |
| Productfilter | Frontend én index/schema/profiel | Type/eenheid, publicatie, telling, native terugval, history |
| Betaal-/verzendregel | Shopify-platform/appbeheer | Werkelijke checkoutofferte en cartpresentatie; themakleur is geen rate |
| Stijl/beweging | Kleinste bestaande gedeelde component | Actieve cascade, alle callers, keyboard/reduced motion |

## Documentatie meeveranderen

Bij iedere betekenisvolle wijziging: doel en veranderd gedrag; exacte bronversie; beheer-/datacontract; geraakte callers; uitgevoerde scenario's en grenzen; open bevindingen; terugzetbron. Actualiseer het bestaande dossier en de centrale status, voeg bewijs gedateerd toe en behoud historische resultaten met hun oorspronkelijke meetgrens. Geen tweede “huidige waarheid” naast de vaste ingang maken.

Nieuwe actieve template/renderer: voeg toe aan routes, dekking en de juiste component. Nieuwe herbruikbare functie: één eigenaarspagina en crosslinks, geen gekopieerde uitleg per merk. Een bewijsbestand krijgt datum, bronhash, methode, inputklasse en beperkingen. Synthetische data herkenbaar houden; geen echte cart/order-/klantinhoud openbaar opslaan.

## Naslag opnieuw opbouwen

De actieve branch bevat `scripts/build_site_reference.py` (Python-standaardbibliotheek). Hij leest een apart verkregen snapshot + manifest, controleert bytes, verwerkt JSON/schema's en letterlijke refs en schrijft alleen naslagmetadata. Geen netwerk, theme-JavaScript, productmutaties of bronoverschrijving.

```bash
python scripts/build_site_reference.py \
  --snapshot /path/to/verified-theme \
  --manifest /path/to/manifest.json \
  --output /path/to/review-reference
```

Vergelijk de nieuwe output vóór overnemen. `MANIFEST_ONLY` en `BYTE_MISMATCH` zijn zichtbare onderzoeksgrenzen, geen successstatus. De actuele Admin-naslag wordt apart uit veilige read-only bewijsmetadata onderhouden; de bronbuilder haalt geen Admin-resources op en schrijft ADMIN.md niet. Geen lokale source-/private exportmap naar publiek Git kopiëren.

## Veilige release en herstel

Git-documentatie mag op main; tool-/codewerk blijft op de geregistreerde actieve branch. Een conceptthema moet vóór wijziging bewezen passen bij de bedoelde bron. Publicatie, productdata en externe indexomschakeling volgen hun eigen bestaande autorisatie-/rollbackpad; een documentatieopdracht is geen live-correctieopdracht. Geen forcepush of onbekende lokale wijzigingen opruimen.

Bij wijziging van keuzedata originele bron, revisierouter en gegenereerde uitsnedes samen valideren. Bij cartfout zekere serverafwijzing en onzekere transportuitkomst onderscheiden; geen automatische tweede koopactie. Bij externe indexfout native terugval behouden en eerst serverstaat vaststellen. Een exportbestand of Git-commit is geen volledige bedrijfsbackup.

## Overnametest

Een opvolger moet voor “footerlink werkt niet”, “product mist een kleur”, “filter toont oud artikel” en “popup toont verkeerd product” binnen deze kaart de bron, consumer, bewijsgrens en kleinste veilige vervolgstap vinden. Lukt dat niet, verbeter de vindbaarheid in plaats van nog een los statusdocument te schrijven. Praktijk-/toegangsblokkades blijven in COVERAGE.md staan totdat echt bewijs ze sluit.
