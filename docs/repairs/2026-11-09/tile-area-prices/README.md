# Tegelkaarten met alleen de m²-prijs

9 november 2026 · TILE-AREA-PRICE-01 · PREVIEW_VERIFIED / OWNER_PUBLICATION_PENDING

De eigenaar vraagt één leidende m²-prijs op de productkaart en boven de tegelcalculator. Onder de calculator staat het werkelijke bedrag voor het gekozen aantal hele dozen. Artikelen per stuk, pak of set behouden hun eigen prijs. De rekenkundige correctie bij het verzoek is expliciet gemeld: 3 dozen van 0,5 m² à €50/m² kosten €75, niet €150.

## Uitvoering

Codebranch `fix/product-cards-2026-10-14`, basis `6968de5a0bf300f2adf807f8f77c0d44494cea5d`. Themabron uitsluitend `shopify/current/`. Vijf relevante bestanden zijn vooraf bytegelijk met de verse MAIN-bron gecontroleerd. MAIN is **196368531722 — Hele europrijzen 8 nov**.

Het bestaande UNPUBLISHED thema **196354474250** is eerst met 27 vastgestelde prijs-/zoekverschillen naar de huidige MAIN-baseline bijgewerkt. De twee ontbrekende geldhelpers zijn hierin inbegrepen. De overige bronchecksums en config/settings_data.json waren al gelijk; die beschermde settings-body is niet geschreven. Daarna zijn uitsluitend onderstaande vijf functiepaden gewijzigd. Het concept heet nu **BadkamerCity - Tegelprijzen per m2 9 nov**.

Een eerder gestarte Shopify-duplicatie (196395073802) kopieerde traag en miste tijdens de controle nog essentiële bestanden. Die reserve is niet gebruikt voor features of review en heet nu **Reserve - kopie tegelbasis (geen review)**. Publiceer die reserve niet als deze release.

| Bestand | Verandering |
| --- | --- |
| snippets/bc-card-tile-price.liquid | Gedeelde primaire m²-prijs en kaartdata, uitsluitend bij positieve doosinhoud en buiten expliciete stuksmodus; variantfamilies krijgen de laagste m²-prijs met Vanaf waar nodig. |
| snippets/price.liquid | Native kaarten gebruiken de gedeelde m²-prijs; gewone verkoopprijzen behouden hun oorspronkelijke renderer. |
| snippets/bc-card-product-search.liquid | De eigen zoekkaart gebruikt dezelfde tegelprijs. |
| assets/bc-external-filters.js | Na actuele Shopify-kaartverrijking toont de externe kaart één m²-prijs; de extra doosprijs en losse prijslijnen verdwijnen. |
| snippets/bc-porcelanosa-buybox.liquid | Losse doosprijs boven de calculator verwijderd; m²-prijs en totaal onder de calculator behouden. |

Alle catalogusprijzen, adviesprijzen, doosinhouden, productdata en rekencontrollers zijn behouden. De winkelwagen blijft afrekenen in echte dozen: aantal × opgeslagen doosprijs. Gebruik bij afronding de echte doosprijs in centen; het totaal opnieuw uit een afgeronde m²-prijs afleiden kan centverschillen veroorzaken. Dit is geen afrondingsopdracht voor tegelprijzen.

## Bewijs

- Finale volledige manifestread: **1.390 bestanden per thema**, precies de vijf bedoelde verschillen; de overige 1.385 checksums gelijk. Alle 1.390 MAIN-checksums zijn ongewijzigd. [Bronpariteit](theme-parity.json).
- Alle vijf geschreven bronbodies exact teruggelezen uit het concept en vergeleken met de payload: PASS.
- Tegelcontroles met echte Liquid-snippets en de bestaande rekencontroller: primaire prijs, native/eigen zoekkaart, gewone prijzen, expliciete stuksmodus met achtergebleven doosdata, afgeleide m²-prijs, adviesprijsweergave, variantfamilie, totaalpositie, 3 × 0,5 m² = €75, afronden naar hele dozen en 3 × €69,07 = €207,21. [Controles](checks.json).
- De bestaande 26 kaartregressies en 31 prijsregressies zijn herhaald met uitsluitend de nu gewijzigde tegelverwachting aangepast. De oude dossiers blijven als historische contracten intact; `checks.mjs` maakt reproduceerbare replays. De 17 voorspellende-zoekcontroles slagen eveneens.
- Shopify-validator op alle vijf functiepaden: VALID, geen errors; één bestaande ongebruikte `has_specs`-waarschuwing. Officiële gecachte schema's gebruikt na een netwerk-time-out bij verversen. [Uitvoer](theme-check.txt).
- Echte browserpreview, 1348 × 926: Cottoceramix Chelsea-R Bone VS4512 toont **€68,95/m²** bovenaan. Eén doos van 1,08 m² geeft **€74,47**; drie dozen geven 3,24 m² en **€223,41**. Werkelijk toegevoegd via de bestaande knop; winkelwagen toont aantal 3 en hetzelfde bedrag €223,41. Eigen testregel verwijderd en de lege winkelwagen zichtbaar bevestigd. [Productpagina](browser-pdp.jpg).
- Echte externe zoekkaart voor VS4501: Sentier-R Natural toont uitsluitend **€63,95 per m²**, zonder €69,07 doosprijs of extra doosprijslijn. [Kaart](browser-card.jpg).

Deze ronde bewijst desktopweergave en de genoemde koopactie tot de winkelwagen. Fysieke telefoon, volledige mobiele filterflow, betaal-/mail-/purchaseketen, iedere variantfamilie en fout-/laadtiming van alle netwerkpaden zijn niet getest. Externe kaarten behouden de bestaande asynchrone verrijking uit Shopify. Overige consent-/policy-/btw-/filter-/Cotto-/BRAUER-holds behouden hun eerdere status.

## Review, publicatie en herstel

**Eén volgende handeling:** eigenaar beoordeelt en publiceert **196354474250 — Tegelprijzen per m2 9 nov** via Shopify. De connector ondersteunt geen themapublicatie; de agent heeft niet gepubliceerd en geen MAIN-bestand geschreven. Na publicatie MAIN en de vijf checksums opnieuw lezen.

De oorspronkelijke vijf bodies staan in `rollback/`. Voor herstel vóór publicatie: zet alleen deze vijf paden terug vanuit de nog ongewijzigde MAIN, of herstel de rollbackbestanden in hetzelfde concept. Publicatie van een ouder thema kan andere latere wijzigingen terugdraaien: eerst vergelijken. Geen force-push, instellingenwrite of blinde root-deploy.

Testherhaling: installeer `liquidjs@10.21.1` en `happy-dom@21.0.4`, voer `node checks.mjs` uit in dit dossier. Voor de aparte voorspellende suite: `node ../predictive-search-prices/checks.mjs` met dezelfde dependencies. Geen lokale Windows-/PowerShell-run geclaimd. Geen actieve schrijver na overdracht.
