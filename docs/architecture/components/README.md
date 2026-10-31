> **31 oktober 2026 — actuele ingang DOC-04:** [80 hoofdstukken met praktische beheertaken](../../MASTER_SITE_REFERENCE.md), [verse bronkaart](../../site-reference/2026-10-31/README.md). De tellingen en bronnen hieronder behouden hun oorspronkelijke datum. MAIN 195948839178; NAV-02 is concept, retourmailbewijs open.

# Componentdossiers — zo vind je de juiste bouwsteen

**DOC-02A/02C · 28 oktober 2026.** Dit is de verdiepte uitleg van de op deze datum gelezen productiecode. De [centrale werkstatus](../../LIVE_STATUS_AND_NEXT_STEPS.md) blijft leidend voor de actieve taak en bron. Geen nieuwe feature of UI-correctie is in deze ronde uitgevoerd.

| Je wilt begrijpen of veranderen… | Eigenaar van de uitleg |
| --- | --- |
| Welk fundament, libraries en testgereedschap we gebruiken | [Fundament en tooling](FOUNDATIONS_AND_TOOLING.md) |
| Welke pagina welke code gebruikt | [Routes en renderers](../ROUTE_RENDERER_MATRIX.md) |
| Productopbouw, specificaties, omschrijving en documenten | [Productpagina's en gegevens](PRODUCT_PAGES.md) |
| Kleur, uitvoering, lengte, inbouwdeel en navigatie na kiezen | [Productkeuzes](PRODUCT_CHOICES.md) |
| Productkaarten, zoeken, filters en mobiele lijstbediening | [Kaarten en filters](PRODUCT_CARDS_AND_FILTERS.md) |
| Toevoegen, bevestiging, sluiten en afwijkende kooproutes | [Winkelwagen en feedback](CART_AND_FEEDBACK.md) |
| Header, menuboom, zoeken en lokale opslag | [Navigatie en opslag](NAVIGATION_AND_STORAGE.md) |
| Oorspronkelijke data, generatie, revisies en terugval | [Datapijplijnen](DATA_PIPELINES.md) |
| Bestaande stijl, beweging en harmonisatiegrenzen | [Stijl en beweging](MOTION_AND_STYLES.md) |
| Welke afwijkingen eerst onderzocht moeten worden | [Bevindingenregister](../FINDINGS.md) |

## Brede winkelonderdelen sinds DOC-02C

| Onderdeel | Dossier |
| --- | --- |
| Footer en beheer van links/contact | [Footer](FOOTER.md) |
| Homepage, blokvolgorde en eigen kaarten | [Homepage](HOMEPAGE.md) |
| Collecties, meubelhub en merken | [Categoriehubs](COLLECTIONS_AND_HUBS.md) |
| Begrippen, blog, advies en formulieren | [Content/formulieren](CONTENT_AND_FORMS.md) |
| Accounts, 404, password, giftcard en reservebouwstenen | [Accounts/systemen](ACCOUNTS_AND_SYSTEM_PAGES.md) |
| Canonical, structured data, redirects, taal/markt | [SEO/talen](SEO_AND_LOCALIZATION.md) |
| Apps, consent en systemen buiten het thema | [Apps/privacy](APPS_PRIVACY_AND_EXTERNAL_SYSTEMS.md) |
| Native/externe filterketen en index | [Filterengine](FILTER_ENGINE.md) |
| Checkout, betaling, verzending en bedrijfsproces | [Bestelketen](CHECKOUT_AND_OPERATIONS.md) |

[Alle bron-/instellingenreferenties](../reference/README.md), [dekkingsregister](../COVERAGE.md), [eenheidskaart](../CONSISTENCY.md) en [onderhoudsroute](../MAINTENANCE.md) bewaken de hele winkel. DOC-02C voegt 35 HTTP-responses, vier zoek-API-reads en beperkte desktopbegrippen-/footercontroles toe. Dit vervangt geen open mobiele, server-, account- of checkoutcontrole.

## Afzonderlijke functies onderzoeken

De [microdossiers](micro/README.md) verdiepen nu renderContents/open/close, Sunshower-actievlaggen, exacte keuzematching/fallback en aantal-/identiteitsguards. Vijftien afgesloten replays maken normale bescherming, grenzen en twee reproduceerbare foutgevallen onderscheidbaar. Drie beperkte desktopwaarnemingen zijn toegevoegd; mobiel blijft open.

## Bronnen lezen zonder de verkeerde code te pakken

Alle bronverwijzingen in deze dossiers zijn **theme-relatieve paden en regelnummers van MAIN 195818389770**, opnieuw tegen het complete manifest gecontroleerd op 28 oktober. Dit is niet automatisch het gelijknamige bestand in de Git-root. De [bronindex](../evidence/2026-10-28-doc02/source-index.json) geeft per onderzocht bestand MD5/SHA-256, aantal regels en exacte Git-kandidaten op broncommit `c8f76eea2bf8a81ab0f54196e239e0b3930fe20a`.

Bij geen Git-match: lees het bestand uit de benoemde Shopify-bron en controleer de hash. Gebruik geen ouder rootbestand als vervanging. Bij gewijzigde MAIN/hash zijn de regelnummers aanwijzingen voor een eerdere versie; heropen het dossier. De settings_data.json-uitzondering uit DOC-01 blijft open. De onderzochte codebestanden vallen buiten die uitzondering; geen volledige deployvrijgave afleiden.

De [bewijsingang](../evidence/2026-10-28-doc02/README.md) scheidt verse broncontrole, acht openbare HTML-responses en nog niet uitgevoerde interactieve controles. HTML aanwezigheid is **VERIFIED_HTML**: de server heeft de structuur teruggegeven. Het bewijst geen zichtbaarheid na CSS, focus, soepelheid, API-succes of koopactie. De Admin-aantallen komen uit het benoemde productexportvenster van DOC-01; ze zijn geen nieuwe realtime voorraadtelling.

## Hoe diep ieder dossier gaat

Ieder dossier beschrijft klantdoel, activeringsvoorwaarde, bronbestanden, input/output, relevante staten, fout/terugval, afhankelijkheden en concrete wijzigings-/controlegrenzen. De regels beschrijven eerst wat bestaat. Gewenste harmonisatie blijft PROPOSED tot functie, staat en eigenaarbesluit duidelijk zijn.

Een nieuwe ontwikkelaar begint bij een gebruikersdoel, kiest één dossier en volgt van daaruit de bron- en datakoppelingen. Gedeelde code wordt eenmaal uitgelegd; merkvarianten verwijzen naar dat contract. Kopieer deze dossiers niet per leverancier of product.

## Dekking die nog ontbreekt

DOC-02A is een bron-/HTML-verdieping, geen volledige DOC-02/03-afronding. Nog open: alle viewport-/toetsenbord-/touchstaten, echte browserinteracties, apps/pixels, volledige CSS-cascade, Shopify Section Rendering bij fouten, alle native variantgevallen, commerciële datajuistheid en VPS/indexgezondheid. Blog-/advies-/servicepagina's en checkout hebben nu eigen dossiers; ontbrekende bron-/praktijk-/bedrijfscontroles staan per onderdeel in COVERAGE.md. De [onderzoeksboom](../DEEP_SCAN_PLAN.md) bewaakt die dekking.

## Verlanglijst en opslag verdiept

[Opslag](micro/WISHLIST_STORAGE.md), [identity](micro/WISHLIST_IDENTITY.md) en [render/kooproute](micro/WISHLIST_RENDER_AND_ADD.md) hebben elk één eigenaarspagina. DOC-03D koppelt vijftien opnieuw geverifieerde bronbestanden aan 43 lokale cases en twee open code-reproducties. Bronhergebruik en native-browsergrenzen staan in [het bewijs](../evidence/2026-10-28-wishlist/README.md).
