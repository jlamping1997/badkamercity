# BadkamerCity — actuele werkstatus

**29 oktober 2026 · NAV-01 — mobiele subcategorieën inline openklappen en accountlinks verwijderen.** De homepage met negen cirkels is inmiddels door de eigenaar gepubliceerd. Verse Shopify-read bevestigt MAIN **195910795530**; vorige MAIN195876815114 is UNPUBLISHED.

## Actuele uitvoering

[Bronnen, wijzigingen, controle en terugzetten](navigation/2026-10-29/README.md). [Eerdere HOME-01-status](navigation/2026-10-29/previous-work-status.md).

- MAIN:195910795530 — BadkamerCity - Homepage rondjes en acties. Geen writes/publicatie door deze sessie.
- Concept:195913482506 — BadkamerCity - Menu openklappen en strakke rijen, UNPUBLISHED; klaar voor review.
- Status: **PREVIEW_READY / SHOPIFY_COMPONENT_BROWSER_QA_PASSED / NATIVE_PHONE_NOT_TESTED / NOT_PUBLISHED**.
- Actieve codebranch: `fix/product-cards-2026-10-14`, codecheckpoint 9048bff16f540ef9ec7f0f3ff14e776ab4a31f2f. Main uitsluitend documentatie.
- Code: header/drawer uit huidige MAIN als basis, accountlink weg, native inline details voor tweede niveau, rechte rijen/dividers. Eerste categorieën en homepage behouden.

## Verificatie

Kopie 1.337/1.337 checksumgelijk; alleen header/drawer gewijzigd, exact teruggelezen. Tijdelijke QA-view exact hersteld. MAIN na afloop 1.337/1.337 ongewijzigd. ThemeCheck beide bestanden geslaagd. Alle 156 menu-URL's behouden. Shopify-gerenderde headerfixture 320/390: inline Kranen/Wastafelkranen en Douche/Douchesets, Enter/Space, Terug/focus, Escape en reset geslaagd; geen overloop en radius 0. Desktopheader zonder account en juiste doelcollectie geopend. Native telefoon/full-page sticky/overlay/resize en volledige focustrap niet getest. Bewijs in dossier.

## Exact één volgende handeling

**Eigenaar beoordeelt het nieuwe concept op zijn telefoon: Menu → Kranen → Wastafelkranen open/dicht → Opbouw kiezen → terug; daarna beslist hij over publicatie.**

## Overdracht

Zie NAV-01-dossier en AGENTS.md. Eerdere HOME-01-testgrenzen, open telefoon-/afspraakontvangstcontrole en overige UI-/filter-/cart-/wishlistbevindingen blijven afzonderlijk bestaan. Git-root is geen complete live-snapshot. Geen Windowscontrole claimen.
