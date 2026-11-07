# BadkamerCity — actuele werkstatus

**29 oktober 2026 · FLASH-01 — opmaakflits bij laden/navigeren herstellen.** Eigenaar heeft opdracht gegeven de zoekbalk/icoonflits te verhelpen. NAV-01 is inmiddels door de eigenaar gepubliceerd: verse MAIN 195913482506.

## Actuele uitvoering

[Dossier, bron, oplossing en testgrenzen](render-flash/2026-10-29/README.md). [Vorige werkstatus](render-flash/2026-10-29/previous-work-status.md).

- MAIN 195913482506 — BadkamerCity - Menu openklappen en strakke rijen. Geen writes/publicatie door deze sessie.
- Concept 195915448586 — BadkamerCity - Stabiele header en iconen, UNPUBLISHED; klaar voor review.
- Status **PREVIEW_READY / CONTROLLED_STARTUP_AND_SEARCH_NAV_PASSED / IPHONE_NOT_TESTED / NOT_PUBLISHED**.
- Actieve branch `fix/product-cards-2026-10-14`, codecheckpoint 901ebfdd35400233da1337c1f1e9822739ff60cc. Main uitsluitend documentatie.
- Zoekstyles synchroon in head, dubbele body-link weg, minimale inline afmetingen/gesloten-suggestieguard, intrinsieke pijlmaat. Vier deployfiles; ongewijzigde bestaande dependencies alleen naar Git geïmporteerd.
- ThemeCheck R2 zonder errors, één bestaande layoutwaarschuwing. Gecontroleerde ontbrekende-CSS-vergelijking reproduceert de hoge header/grote blauwe pijl; nieuwe variant blijft begrensd. Normale zoekfunctie/navigatie geslaagd. Fysieke iPhone/Safari nog open.

## Verificatie

Kopie 1.337/1.337 checksumgelijk vóór writes; na afloop alleen de vier bedoelde deployfiles afwijkend/toegevoegd. Vier exacte readbacks; QA-view exact hersteld. MAIN 1.337/1.337 ongewijzigd. Header in gecontroleerde oude starttoestand 494,66px hoog, nieuwe toestand 137,66px en alleen de guard op 320px: 131px, gesloten suggesties 0px; nieuwe frames geen overloop. Losse oude blauwe pijl circa 359×256px zonder CSS, nieuwe pijl 14×10px. Normale desktopafmetingen exact gelijk vóór/na; zoeksuggesties, Escape, zoekresultaten, Kranen en terug naar home gecontroleerd. Geen native iPhone/netwerkfilmstrip/Lighthouse-claim. Zie bewijs in dossier.

## Exact één volgende handeling

**Eigenaar controleert concept ‘BadkamerCity - Stabiele header en iconen’ op zijn iPhone: homepage herladen, tussen homepage/categorie/product wisselen en één zoekopdracht; na akkoord publiceert hij.**

## Overdracht

Zie FLASH-01-dossier/AGENTS.md; MAIN, branch en bestanden vóór elke vervolgstap vers verifiëren. Eerdere telefoon-/afspraakontvangstcontrole en andere UI-/filter-/cart-/wishlistbevindingen blijven afzonderlijk bestaan. Git-root geen complete livebron. Geen Windowscontrole claimen.

## Parkeerplaats — nieuwe toekomstprojecten, 29 oktober 2026

[Content, merkpagina's, offerteaanvragen en productplan](FUTURE_CONTENT_AND_PRODUCT_PROJECTS.md): Living Colours/PVD met productuitleg en vergelijkingsbeelden; bestaande Sunshower-blog versterken; hoogwaardige Porcelanosa-merkpagina; bestaande offerte-upload-/prijsaanvraagtaken aanscherpen; gefaseerde productkwaliteit en verrijking. Status **BACKLOG / NOG UIT TE VOEREN**. Geen start van deze uitvoering of wijziging van de NAV-01-reviewvolgorde.

Historisch backlogcheckpoint vóór FLASH-01: GitHub-connector, uitsluitend documentatie op de bestaande werkbranch en main. Bestaande blog-/productdossiers en historische offerte-/prijstaken hergebruikt; Hotbath-bronnen voor het algemene patinaprincipe gecontroleerd. Nieuwe functies en productdetails niet getest of gebouwd. Shopify-rollen in deze sessie niet opnieuw gelezen; bovenstaande theme-metingen behoren bij NAV-01. Geen winkelmutatie, Windowscontrole, publicatie of geplande achtergrondtaak. Eigenaar kiest later welk toekomstproject start; de ene eerstvolgende handeling hierboven blijft staan.

## TAX-01 — vaste categorisatie- en SEO-werkwijze, 29 oktober 2026

Eigenaar vraagt nu schaalbare categorisatieafspraken en documentatie voor nieuwe merken/producten en toekomstige SEO-/serieonderzoeken. [Vast contract en fasering](CATEGORIZATION_AND_SEO_POLICY.md) · [gedateerde nulmeting en eerste beslissingen](categorization/2026-10-29/baseline-and-decisions.json). Status **DOCUMENTED / TAXONOMY_PROPOSALS_NOT_IMPLEMENTED**. AGENTS.md verwijst toekomstige imports/categoriewijzigingen naar dit contract.

Read-only inventaris eerder in deze doorlopende sessie: 9 menu's, 226 collecties, hoofdmenu156vermeldingen/144bestemmingen; 12 dubbele bestemmingen zijn reviewgevallen, geen automatische fouten. Eerste afdelingsvoorstellen, importprocedure en selectiecriteria voor SEO-landings zijn beschreven. Verse beperkte concurrentiesteekproef en officiële Google-richtlijnen gelezen; geen keywordvolumes, rankings of conversieresultaat vastgesteld. Geen Shopify-mutatie of nieuwe themacontrole in deze documentatiestap. Volledige visuele/klik-/importtests nog open.

Dit documentatiecheckpoint neemt de afzonderlijke FLASH-01-uitvoering niet over en verandert de ene volgende uitvoeringshandeling hierboven niet. Eerstvolgende categorisatiehandeling ná afronding/overdracht daarvan: TAX-02, één concreet Wastafels-voorstel met productmapping en gescheiden aanvullende links in preview beoordelen. SEO-onderzoeken staan als vervolgwerk, niet als gestarte achtergrondtaken.
