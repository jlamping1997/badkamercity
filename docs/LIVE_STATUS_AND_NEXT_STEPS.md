# BadkamerCity — actuele werkstatus

**30 oktober 2026 · RET-01 preview gecontroleerd; mailboxproef en vrijgave open.**

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

**RET-01 — PREVIEW_VERIFIED / MAIL_DELIVERY_AND_OWNER_RELEASE_PENDING.** [Retouraanmelding en footeradres](returns/2026-10-30/README.md). Eigenaar heeft HDR-01 goedgekeurd/gepubliceerd; actuele MAIN195932061962 — BadkamerCity - Vaste mobiele header,1351files. VorigeMAIN195915448586UNPUBLISHED. Geen publicatie door deze uitvoerder.

Reviewconcept **UNPUBLISHED195947036938 — BadkamerCity - Retour aanmelden en footer**. Zichtenburglaan150 en het lege adreskopje uit beide footers; gezamenlijke retouringang; formulier met naam/e-mail/producten/aantallen/verzoek en optioneel bestelnummer/reden/toelichting. Native Shopify-contactmailer; afhandeling per e-mail, label/instructies handmatig en geen automatische refund. De automatische browserreview weigerde privé-Jotform-accounttoegang; geen omweg of nieuw Jotform-formulier. Veiliger alternatief gebruikt uitsluitend de al geautoriseerde website/Shopify-integratie.

Vooraf1351/1351identiek; finaalMAIN1351/1351gelijk en concept1354 met exact8featurepaden. ThemeCheckR3 8/8SUCCESS,22render-/contractcasesPASS, echte desktop1348 en componentframes320/390/880/1024zonderoverloop. Lege-submit stopte opNaam; native mailendpoint en optionelevelden geverifieerd. Beide footerresponses zonderadres en met schone retourhref; homepagefooterlink echt aangeklikt. QA-templateexacthersteld. Geen succesvolle formsubmit, mailbox-/spamtest of labellevering geclaimd.

Nieuwe Page **166668894474**, `/pages/retour-aanmelden`, template`retour-aanmelden`, **isPublished=false**. Preview via `/pages/contact?view=retour-aanmelden` in dit concept. Page- en themepublicatie zijn nog open. Offerteconcept195916628234 behouden; vóór latere publicatie header/retourwerk opnieuw meenemen. Geen order-/return-/refund-/label-/catalogus-/VPS-/prijs-/voorraadmutatie. Windows niet gecontroleerd. Branch blijft fix/product-cards-2026-10-14; main alleen documentatie.

## Exact één volgende handeling

**Eigenaar dient één herkenbare testaanvraag in via het retourconcept en controleert ontvangst op info@badkamercity.nl, inclusief spam.** Daarna pas telefoonreview en bewuste Page-/themavrijgave. De offerte-Jotform-verificatie blijft afzonderlijk geparkeerd.

## Bevindingen en achtergrond

Het naslagwerk registreert onder meer tien ontbrekende grote-footerbestemmingen, de Hygro(meter)-404, collectiemetadata, de €75/€100-verzendtekstafwijking in de native fallback, native/externe zoektellingen en tegelprijseenheden. Eerdere geïsoleerde cart/filter/wishlistbevindingen blijven met hun eigen bron-/testgrens bestaan. Mobiele bron/componentanalyse vervangt geen volledige fysieke telefoon-/koopronde; backend, Google en bedrijfsprocessen blijven expliciet begrensd.

De [vorige centrale status is exact gearchiveerd](site-reference/2026-10-30/previous-live-status.md). [Categorisatiebeleid](CATEGORIZATION_AND_SEO_POLICY.md), [toekomstprojecten](FUTURE_CONTENT_AND_PRODUCT_PROJECTS.md) en de historische architectuurdossiers blijven geldige achtergrond binnen hun eigen datum. Geen schrijver of achtergrondworker actief na deze oplevering.
