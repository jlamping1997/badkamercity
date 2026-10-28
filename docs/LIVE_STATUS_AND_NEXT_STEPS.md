# BadkamerCity — actuele werkstatus

**28 oktober 2026 · DOC-03C filterketen.** Eigenaar vraagt verder onderzoek en documentatie. Checkout blijft expliciet buiten scope. De eerdere inbouw-/footer-/content-/motionverdieping is behouden; dit vervolg behandelt de externe lijst en overdracht naar native Shopify.

## Ingang en resultaat

[Architectuur](architecture/README.md) → [dekking](architecture/COVERAGE.md) → [microdossiers](architecture/components/micro/README.md). Vier nieuwe verdiepingen:

- [Filterstaat en native terugval](architecture/components/micro/FILTER_STATE_AND_FALLBACK.md): URL, nieuwste request, timeout, popstate en DOM-eigenaarschap.
- [Waarden en controls](architecture/components/micro/FILTER_VALUES_AND_CONTROLS.md): eenheden, exact/group/boolean, draft/debounce, Meer/Minder en beleidsflags.
- [Kaartverrijking en kleuren](architecture/components/micro/CARD_HYDRATION_AND_COLORS.md): ID, cache, vier workers, section-timeout en nieuwste kleurintentie.
- [Drawer en zwevende shortcut](architecture/components/micro/MOBILE_LISTING_AND_DRAWER.md): twee breakpoints, opener, overlay, inert en focusgrenzen.

Geen productiecorrectie uitgevoerd. De bestaande brede naslag en private productexport blijven de bovenliggende bronnen; geen volledige thema-/productexport opnieuw gedaan.

## Werkelijk uitgevoerd

| Bron / methode | Resultaat en grens |
| --- | --- |
| Git-start actief | fix/product-cards-2026-10-14 op 5f0dd414f9243e46757930b7924329f4abc4fe1f |
| Git-start main | dd780e9a19d18d36da33780885489cf47dc86893 |
| MAIN aanvang/einde | 195818389770 — Smooth winkelwagen pop-up, niet gewijzigd |
| Gerichte source-read | Negen bestanden, alle MD5/grootte passend; drie JS-bronnen in de harness uitgevoerd |
| Replay | **41 cases: 35 CONTROL_PASSED, twee DEFECT_REPRODUCED, vier BOUNDARY_CONFIRMED** |
| Native interactie | FX-37 gebruikt echte facets-popstate-handler/gridmethode met nagebootste requestorkestratie; geen volledige native/browsercyclus |
| Omgeving | Node 24.22.1, bestaande happy-dom 21.0.4; transport/navigatie/timers/geometry/media/scroll gestubd; numerieke validity met expliciet tolerant testmodel |
| Publieke API | Twee read-only zoek-POST's, beide 200; facetmetadata Wastafelkranen (10) en Inloopdouches (7), alle visible_values=6 |
| Browser/cart/index | Geen nieuwe browser-, echte cart- of indexactie. Geen mobiele, CSS-, native validity-, a11y- of serverfrequentievrijgave |

[Bewijs, fixturegrenzen en reproduceerbare methode](architecture/evidence/2026-10-28-filters/README.md). Geen theme-/product-/cart-/indexwrite, formulier-/mailverzending, checkoutread, nieuwe dependency of publicatie. Ruwe source-/winkelbodies staan buiten publiek Git.

## Nieuwe bevindingen en bevestigde bescherming

- **FILTER-F01 / VERIFIED_ISOLATED / P1-kandidaat:** na fallback kan popstate zowel native als extern starten. Native vervangt de containerinhoud; een later extern succes schrijft naar oude losse nodes en zet active=true met native live grid en ontbrekende toolbar. Onder gecontroleerde timing gereproduceerd; geen bewezen huidig bezoekersincident.
- **FILTER-F02 / VERIFIED_ISOLATED / conditionele P2-kandidaat:** visible_values=2 wordt na Meer/Minder zes. De twee gelezen live profielen gebruiken zes, dus geen actuele fout op die twee routes aangetoond.
- **FILTER-B01 / grenzen:** verkeerde collectiehandle kan bij gelijk profielcount worden geaccepteerd; native URL-dialect niet vertaald; omgekeerde range doorgestuurd; searchable/section-flags hebben frontenduitzonderingen. Geen extra bewezen live backendfouten.
- Positief: oude antwoorden/fouten overschrijven de nieuwste zoekintentie niet; gewone fallback herstelt nodes/displays; mispassende kaart-ID activeert toevoegen niet; falende section-cache kan opnieuw worden gelezen; nieuwste kleurintentie houdt handle/kleur/link samen.
- Eerdere CART-F01, SS-F01, FOOTER-F01, GLOSS-F01, UI-F04 en DATA-F04 blijven open en ongewijzigd. Settingspariteit, verse VPS/appbron, Google/deploy en echte mobiele-/bedrijfscontroles blijven afzonderlijk open.

## Exact één volgende handeling

**DOC-03D — verlanglijst en browseropslag als keten isoleren:** toevoegen/verwijderen → exacte variantidentiteit → opslagfout/ongeldige of oude data → state-event → render/herstel. Gebruik alleen synthetische opslag en lokale productresponses; geen echte bezoekersopslag of cart-restoremutatie. Checkout blijft buiten scope.

## Hervatten en Git

Actieve branch blijft fix/product-cards-2026-10-14; main alleen documentatie. Lees deze status → AGENTS.md → betrokken microdossier/bewijs. Controleer verse MAIN/hashes en eigen werkmap; start geen oude import-/publicatiestappen. Geen schrijver of achtergrondworker blijft actief na oplevering.
