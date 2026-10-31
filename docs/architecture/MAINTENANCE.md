# Onderhoud en overdracht voor een nieuwe ontwikkelaar of AI

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
