# BadkamerCity — actuele werkstatus

**31 oktober 2026 · NAV-02: laptop-/desktopcategorieën zonder schuiven, preview gecontroleerd.**

## Begin hier

[Het volledige naslagwerk](MASTER_SITE_REFERENCE.md) brengt de actuele website, functies, desktop/mobielverschillen, alle pagina-/template-/menu-/instellingenregisters en 36 technische brondossiers samen. De bijbehorende [gedateerde bron en controles](site-reference/2026-10-30/baseline-and-checks.json) scheiden Admin, broncode, server-HTML, desktopgedrag, eerder componentbewijs en open controles.

## Verse bronstand

- MAIN **195915448586 — BadkamerCity - Tegelkleuren juiste uitvoering**; **195916628234 — Offerte vergelijken** is UNPUBLISHED. Begin- en eindread van deze documentatieronde zijn gelijk; updatedAt MAIN 2026-10-30T09:34:20Z.
- 11.680 productrecords: 11.679 ACTIVE en één DRAFT; 11.679 Online Store-URL’s. Deze publieke URL-set sluit exact aan op de product-sitemapset.
- 226 collecties, 120 Pages waarvan 118 gepubliceerd, negen menu’s en258 productmetafielddefinities, volledig gepagineerd. Eén blog/één artikel.
- 1.350 themapaden geïnventariseerd; 405 relevante tekstbronnen ontvangen, 404 MD5-gelijk. De bestaande uitzondering config/settings_data.json blijft open.
- 397 hoofd-GETs: 395 HTTP 200 en twee 404; één 404 is de bewuste foutpaginaproef. tegeltoebehoren ontbreekt in de sitemap en is niet gelinkt in de onderzochte responses. 109 begrippenverbindingen opnieuw gevolgd: 108 HTTP 200, Hygro(meter) eindigt nog op 404.
- Gerichte desktopcontrole op 1.348 CSS-pixels: homepage/categorie, predictive zoekfunctie, native→externe lijst, Verona Cubik-PDP en 10m²/10%-calculator. Geen cartwrite, formulierinzending, checkout, betaling of order.
- Naslagwerk offline gecontroleerd: 48 hoofdstukken, unieke interne anchors, volledige catalogus, merkfilter, zoekfunctie, nulresultaat, paginering en inhoudsknop. Dit is geen visuele browserlayout-/telefoonvrijgave. De cloudbrowser stond lokale HTML-voorvertoning niet toe; er is geen omweg gebruikt.

## Code en uitvoeringsgrens

Centrale repository jlamping1997/badkamercity; bestaande uitvoeringsbranch **fix/product-cards-2026-10-14** behouden. Broncommits voor dit onderzoek: main 8a9f0684f25aba145d78830c49ab724c3395d677 en uitvoeringsbranch 379a0e2c2e1aa682a479b2a3c26fca3fc0145881. Geen nieuwe codebranch, geen Shopify-write/publicatie en geen VPS-/product-/prijs-/voorraadmutatie. Deze checkpoint schrijft uitsluitend documentatie; de Git-root is nog geen volledige actuele MAIN-snapshot. Windows is niet onderzocht.

## Bestaande open uitvoering

**BC-QUOTE-001: FORM_CREATED / CONCEPT_CONNECTED / EMAIL_VERIFICATION_AND_DELIVERY_PENDING / CUSTOMER_ACTIVATION_DISABLED.** [Integratie](quote/2026-10-30/INTEGRATION.md), [design](quote/2026-10-30/DESIGN.md), [branding](quote/2026-10-30/BRANDING.md). Page offerte-vergelijken is ongepubliceerd; integration_enabled=false, integration_preview=true alleen bij unpublished, show_preview=false. Header/footer-klantlinks en homepage-teaser blijven uit. Mailontvangst/verificatie, klantmail, privétoegang, bewaartermijn, verwijderen en fysieke telefooncontrole zijn nog open. De publicatie-/themarollen in oudere offertedossiers zijn hun historische opleverstand.

QC-04 blijft een afzonderlijke privétool op branch quality-control: notities, alle merken/willekeurig, checkpoints en dag/nacht; geen automatische Shopify-mutatie. [Overdracht](https://github.com/jlamping1997/badkamercity/blob/quality-control/quality-control/README.md). Deze documentatieronde heeft geen privébeoordelingen gelezen of gewijzigd.

## Actieve uitvoering

**NAV-02 — PREVIEW_VERIFIED / OWNER_PUBLICATION_PENDING.** [Categorieën zonder schuiven](laptop-navigation/2026-10-31/README.md). Actuele MAIN **195948839178 — BadkamerCity - Retourknop in header**,1354files, behouden. Bestaand UNPUBLISHED **195947036938** hergebruikt en hernoemd naar **BadkamerCity - Categorieen zonder schuiven**; eerst alleen de achterlopende header gesynchroniseerd, daarna1354/1354pariteit bewezen. Geen nieuwe volledige themakopie of branch.

Alle elf desktopcategorieën bereikbaar zonder scrollbalk of schuifpijlen.990–1359CSS-px twee gebalanceerde rijen6+5; vanaf1360één rij, CSS-wrap als vangnet. Mobiel tot989behoudt bestaand menu. Exact één blijvend pad sections/header.liquid; finaleMAIN1354/1354gelijk, concept1354/exactéénheaderafwijking, bodyexact. ThemeCheckR1 en JS-syntaxPASS; twaalf breedteframes390–1920zonderoverloop, alle11linkszichtbaar, nulschuifknoppen. Dropdown/focus/Escape, tweede rij, breedtewissel en mobielmenu→desktopherstel gecontroleerd; Merken echt via gewone website geopend. QA-templateexacthersteld. Geen MAIN-write/publicatie.

**RET-03 blijft LIVE_VISIBILITY_VERIFIED / MAIL_DELIVERY_PENDING.** Retour-Page166668894474 gepubliceerd en bereikbaar; knop/retourwerk zit in dit concept. Mailbox-/spamproef en echte labellevering blijven open. Offerteverificatie afzonderlijk geparkeerd, klantactivatie uit. Geen Page-/catalogus-/order-/return-/refund-/prijs-/voorraad-/VPS-mutatie in NAV-02. Geen fysieke laptop-/telefoon- of Windows-controle. Uitvoering afgerond; branch fix/product-cards-2026-10-14, main uitsluitend documentatie.

## Exact één volgende handeling

**Eigenaar beoordeelt en publiceert concept195947036938 — BadkamerCity - Categorieen zonder schuiven.** De retour-Page is al zichtbaar; geen aanvullende Page-publicatie nodig. Het eerdere retourmailboxbewijs blijft afzonderlijk open.

## Bevindingen en achtergrond

Het naslagwerk registreert onder meer tien ontbrekende grote-footerbestemmingen, de Hygro(meter)-404, collectiemetadata, de €75/€100-verzendtekstafwijking in de native fallback, native/externe zoektellingen en tegelprijseenheden. Eerdere geïsoleerde cart/filter/wishlistbevindingen blijven met hun eigen bron-/testgrens bestaan. Mobiele bron/componentanalyse vervangt geen volledige fysieke telefoon-/koopronde; backend, Google en bedrijfsprocessen blijven expliciet begrensd.

De [vorige centrale status is exact gearchiveerd](site-reference/2026-10-30/previous-live-status.md). [Categorisatiebeleid](CATEGORIZATION_AND_SEO_POLICY.md), [toekomstprojecten](FUTURE_CONTENT_AND_PRODUCT_PROJECTS.md) en de historische architectuurdossiers blijven geldige achtergrond binnen hun eigen datum. Geen schrijver of achtergrondworker actief na deze oplevering.
