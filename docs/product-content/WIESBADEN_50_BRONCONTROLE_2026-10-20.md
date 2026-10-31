# Wiesbaden 50 — onafhankelijke bronverrijking en foutcorrectie (20 oktober 2026)

**Bewijsniveau: OFFLINE_QA / VERIFIED_MANUFACTURER_IDENTITY / 8 VERIFIED_ADMIN_READ / NOT_PUBLISHED.**

Vervolg op de bestaande 50-artikel bulkproef. Dit checkpoint is een onderzoeks- en overdrachtsrapport, **geen code-, product-, thema- of VPS-publicatie**. Verbeterde Python-verwerker, tests, 50 gestructureerde productdossiers, CSV, Excel en interactieve HTML zijn als gesprekspakket opgeleverd, maar de v2-bestanden zijn **nog niet naar GitHub gepusht**. Gebruik de gespreksexport of kopieer de pakketbestanden onder bronbeheer na lokale vergelijking; deze documentatie is alleen een pointer.

## Afgebakende uitkomst

- Exacte fabrikant-Wiesbadenpagina, SKU en producttitel opnieuw nagekeken: **50/50**.
- **45** nieuwe basisdossiers voldoende onderbouwd voor inhoudelijke *redactiecheck*; **1** eerder goedgekeurd artikel 24.3710 beschermd; **4** technische twijfelgevallen apart gehouden. **46/50=92% basisdekking is géén statistische garantie op 92% juistheid van elke spec, maat of SEO-claim.**
- **10** centrale hoofdcategorievoorstellen gecorrigeerd. **11** verdachte/tegenstrijdige bronvelden bewust weggefilterd; **34** lege, nutteloze of voor mechanische kranen onlogische velden niet overgenomen.
- **22.3734** en **22.3737** setinhoud bevestigd: fonteinkraan, sifon, plugboutenset, waste. Geen onbewezen flexslang meeleveren.
- **29.8007:** volgens fabrikant matzwart Dreams **afbouwdeel** met afzonderlijk **29.8004** inbouwdeel; foutieve leverancierstabel met Basiskleur=Chroom, Model=Inbouwdeel uitgesloten. Technische rozetmaten nog controlegeval.
- **29.1510** en **29.2541**: fabrikant noemt inbouwdeel **29.2500**. Overige relaties krijgen apart bewijslabel, retailer is niet fabrikant.
- **29.6929**: leverancierstekst bevestigt 150 mm hartafstand, 38°C-blokkering en messing.
- **29.1705** is thermostatische *badmengkraan*, niet douchekraan.
- Eerste live-check Shopify op 8 geselecteerde artikelen: 29.8007,29.1705,22.3734,22.3737,29.1634,29.1635,29.2502,29.2600. Niet automatisch extrapoleren naar 50 actuele Admin-metafields.
- **32/32 offline regressiechecks PASS**, inclusief tekstvelden, unieke SEO, HTML basisstructuur en tweede deterministische dry-run zonder outputdrift.
- **0** live productupdates, collectiewrites, themawijzigingen, prijs/voorraadwrites of externe VPS-indexmutaties.

## Huidige uitzonderingen

- **29.8007** — correct producttype/kleur/29.8004 bekend; rozetmaten vs tekening controleren.
- **29.1634 en 29.1635** — inbouwwastafelkranen Style; losse of inbegrepen inbouwdeel uit fabrikant/technische handleiding bevestigen.
- **29.2502** — fabrikant noemt thermostatische Caral inbouwbox met 2 stopkranen, maar productveld bevat *handbediend*; dit veld weglaten tot technische verificatie. Partner-afbouwdeel 29.2514 slechts met verkopersbewijs.

## Nog open vóór bulkproductaanpassingen

Alle 45 nieuwe concepten redactioneel beoordelen. Controleer voor elk apply-product de **actuele** Shopify-ID/variant/SKU, metafielddefinities en digests, categorie-ID's en lidmaatschappen; bescherm prijzen, status, voorraad, afbeeldingen en handles. De historische 19 oktober snapshot toont voor 10 voorstellen een ontbrekend collectielidmaatschap; is geen actuelere Shopify-read. Werkelijke storefront, mobiele weergave, JSON-LD en externe zoek-/filter-VPS readback zijn nog niet voor deze nieuwe producten geverifieerd. Gebruik pas gecontroleerde beperkte apply + indexverify en rollback, niet blind alle 2.240 artikelen.

## Fabrikantbewijzen (selectie)

- https://www.wiesbaden.nl/caral-victoria-fonteinkraanset-mat-zwart-22-3737.html
- https://www.wiesbaden.nl/caral-victoria-fonteinkraanset-geborsteld-brons-koper-22-3734.html
- https://www.wiesbaden.nl/dreams-afbouwdeel-thermostatische-douchekraan-met-2-stopkranen-mat-zwart-29-8007.html
- https://www.wiesbaden.nl/dreams-inbouwdeel-thermostatische-douchekraan-met-2-stopkranen-29-8004.html
- https://www.wiesbaden.nl/caral-afbouwdeel-inbouwthermostaat-2-weg-mat-zwart-29-1510.html
- https://www.wiesbaden.nl/caral-cool-touch-thermostatische-douchemengkraan-geborsteld-brons-koper-pvd-29-6929.html
- https://www.wiesbaden.nl/style-thermostatische-badmengkraan-waterval-cooltouch-geborsteld-brons-koper-pvd-29-1705.html

**Volgende uitvoerhandeling:** 45 redactionele voorstellen uit HTML/Excel beoordelen, vier kernuitzonderingen apart houden; daarna pas beperkte apply met Adminreadback en bewezen externe indexsynchronisatie.
