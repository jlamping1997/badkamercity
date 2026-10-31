# BadkamerCity — actuele werkstatus

**31 oktober 2026 · FIX-01 actief: winkelwagen-/Sunshower- en filterreparaties, lokale regressie geslaagd; conceptverificatie volgt.**

## Begin hier

[Het volledige naslagwerk](MASTER_SITE_REFERENCE.md) bevat **80 hoofdstukken**, 36 gedateerde technische brondossiers, 50 beheertaken, 40 diagnosepaden, 50 acceptatiescenario’s en het ingebouwde register van 11.679 publieke productroutes. De 32 nieuwe praktische hoofdstukken behandelen klantreizen, dagelijks beheer, schermcontracten, header/menu, zoeken/filteren, productidentiteit, tegels, data, media, cart/opslag, beide footers, retouren, offertegates, redactie, SEO, toegankelijkheid en releases. [Bronuitbreiding en reproduceerbare renderer](handbook/2026-10-31/README.md) · [verse bron en controles](site-reference/2026-10-31/README.md).

## Verse bronstand 31 oktober

- **MAIN 195947036938 — BadkamerCity - Categorieen zonder schuiven**, door eigenaar gepubliceerd; verse rolread en volledig manifest 1.354 paden. updatedAt 2026-10-31T08:57:37Z.
- **195948839178 is UNPUBLISHED** en wordt hergebruikt voor FIX-01. Aanvankelijk exact één headerachterstand tegenover MAIN; actuele header gesynchroniseerd en bytegelijk teruggelezen. NAV-02 is nu LIVE volgens verse rollen; publicatie door eigenaar, niet uitvoerder.
- Retour-Page **166668894474** gepubliceerd; /pages/retour-aanmelden bereikbaar. Headerlink in verse openbare HTML. **MAIL_DELIVERY_PENDING** blijft open.
- 121 Pages, 119 gepubliceerd/twee verborgen; 226 collecties en negen menu’s volledig gepagineerd. Producttellingen EXACT: 11.680 totaal, 11.679 ACTIVE, één DRAFT, 11.679 gepubliceerd. Catalogusidentiteiten blijven de export van 30 oktober; geen nieuwe volledige setgelijkheid geclaimd.
- 409 geselecteerde tekstbronnen: **407 BYTE_MATCH en twee BYTE_MISMATCH**. settings_data.json blijft open; retourtemplate bevat Shopify-commentaar en heeft aparte semantische beoordeling uit RET-01. Geen 409/409-bytepariteit.
- Ten opzichte van de 30-oktobernulmeting: vier nieuwe en zes gewijzigde themapaden. Huidig: 85 Liquid-secties, 119 snippets en 153 CSS-/JS-assets. Oude registers 30–47 zijn duidelijk gedateerd.
- 18 openbare GETs: 17 HTTP 200 en bekende Hygrometer-404. Controle omvat servermarkup/metadata, retourlink, railcontrols en adresafwezigheid in onderzochte footers; geen JavaScriptuitvoering of koop-/formulieractie.

## Actieve reparatie FIX-01

[Bron, correcties en tussenbewijs](repairs/2026-10-31/README.md). CART-F01, SS-F01, FILTER-F01 en FILTER-F02 opnieuw gereproduceerd en lokaal hersteld. 18 cart/Sunshower- en 41 filtercases slagen voor het gekozen contract; gesimuleerde requests, geen echte koopactie. Uitvoering actief, één schrijver. De opdracht omvat ook verdere open verbeterpunten; shipping, zoektelling, eenheden, wishlist, inhoud en SEO worden hierna gericht onderzocht. Mailbox-/offertebewijs blijft apart.

## DOC-04 resultaat en verificatie (historisch, vóór FIX-01)

DOCUMENTATION_VERIFIED / HANDOFF_READY. Het bestaande boek is in plaats uitgebreid; geen tweede concurrerende actuele uitleg. De HTML-reader heeft tekstzoeken, inhoudsopgave, snelle ingangen, **takenzoeker met eigenaar/stand** en merk-/productrouteregister. 80 opeenvolgende hoofdstukken, één H1, unieke IDs en geldige interne anchors; taakfilters, nulresultaten, catalogusfilter (337 Porcelanosa, drie Verona Cubik), paginering, tekstzoeken, Escape en inhoudsbediening offline PASS. Ook zonder scripts blijven alle hoofdstukken en 50 taken leesbaar. Geen externe runtimecalls of scriptfouten in de offline controle.

[Volledige validatie](site-reference/2026-10-31/document-validation.json) is een **jsdom DOM-controle**, geen browserlayout-/fysieke telefoon-/laptop-/Windows-/checkoutvrijgave. Geen nieuwe cartwrite, testinzending, mailboxcontrole of privébackendonderzoek. De eerdere weigering van lokale HTML-browservoorvertoning is niet opnieuw geprobeerd of omzeild.

## Code, branch en uitvoeringsgrens

Repository jlamping1997/badkamercity; bestaande uitvoeringsbranch **fix/product-cards-2026-10-14**. Bron vóór deze docsuitbreiding: remote uitvoering 0d2da1819ce582e1717aefb24899a66050f99449, remote main 3205c6f31516fd86282dd7554e4f490a6551321d. DOC-04 bevatte uitsluitend documentatie. FIX-01 voegt drie gerichte runtimecorrecties en twee regressieharnesses toe; de actuele header is uitsluitend in UNPUBLISHED gesynchroniseerd. Geen MAIN-write/publicatie of catalogus-/prijs-/voorraad-/VPS-mutatie. Git-root blijft geen volledige huidige MAIN-snapshot. Windows niet onderzocht. De handoff en centrale ingang worden op beide branches gelijk gehouden.

## Open uitvoering blijft behouden

**NAV-02 — OWNER_PUBLISHED / MAIN_ROLE_VERIFIED.** [Dossier](laptop-navigation/2026-10-31/README.md). Concept 195947036938 heeft exact één bedoelde headerafwijking tegenover de toen gemeten MAIN.990–1359 CSS-px twee rijen 6+5; vanaf1360 één rij met wrap-vangnet; mobiel tot989 bestaand menu. Twaalf breedteframes, menu/focus/Escape, tweede rij en resize gecontroleerd; QA-template hersteld. Dit gedateerde componentbewijs is niet opnieuw uitgevoerd door DOC-04.

**RET-03 — LIVE_VISIBILITY_VERIFIED / MAIL_DELIVERY_PENDING.** [Publicatie](returns/2026-10-30/PUBLICATION.md). Native contactaanvraag, handmatig order-/retourproces. Geen automatisch RMA, label, refund of klantbevestigingsmail. Footeradres verwijderd; beide footers delen de retourroute. Echte mailboxontvangst/spam/antwoord en labellevering nog open.

**BC-QUOTE-001 — FORM_CREATED / CONCEPT_CONNECTED / EMAIL_VERIFICATION_AND_DELIVERY_PENDING / CUSTOMER_ACTIVATION_DISABLED.** [Integratie](quote/2026-10-30/INTEGRATION.md). Offerte-Page verborgen; integration_enabled=false, preview apart gated, klantlinks/teaser uit. Mailverificatie, klantmail, privétoegang, bewaartermijn, verwijderen en fysieke telefooncontrole open. Geen nieuwe poging tot het eerder geweigerde privéformulieraccount.

QC-04 blijft afzonderlijke privétool op quality-control, zonder automatische Shopify-mutatie. [Overdracht](https://github.com/jlamping1997/badkamercity/blob/quality-control/quality-control/README.md). Geen privébeoordelingen gelezen of gepubliceerd.

## Exact één volgende handeling

**Uitvoerder valideert de FIX-01-kandidaat en schrijft uitsluitend de bedoelde featurepaden naar UNPUBLISHED 195948839178.** Daarna readback en browsercontrole; MAIN blijft behouden. Retourmailboxbewijs blijft afzonderlijk open.

## Historie en verdere bevindingen

[Vorige centrale status exact gearchiveerd](site-reference/2026-10-31/previous-live-status.md). Oudere registers en 36 brondossiers blijven hun meetdatum houden. Hygrometer is opnieuw 404; oude footerbestemmingen, verzendcopy, zoektellingen, tegelprijseenheden en geïsoleerde cart/filter/wishlistcases blijven met hun eigen bewijsgrenzen bestaan. [Categorisatiebeleid](CATEGORIZATION_AND_SEO_POLICY.md) en [toekomstprojecten](FUTURE_CONTENT_AND_PRODUCT_PROJECTS.md) blijven achtergrond. Geen automatische reparaties of nieuwe publicatie uit documentatiebevindingen afleiden.
