# BadkamerCity — actuele werkstatus

**28 oktober 2026 · DOC-03B methoden en herstelketens.** Eigenaar vraagt verdere verdieping van de overige onderdelen. **Checkout is expliciet buiten deze ronde gehouden**; de eerdere toegangsgrens is geen blokkade voor dit werk en is niet opnieuw geprobeerd.

## Ingang en resultaat

[Architectuur](architecture/README.md) → [dekking](architecture/COVERAGE.md) → [microdossiers](architecture/components/micro/README.md). Vier nieuwe inhoudelijke verdiepingen:

- [Inbouw-add en herstel](architecture/components/micro/INBOUW_RECOVERY.md): gewone product-form en addon samen, payload, timeout, responsevalidatie, uncertain en vertrek/terugkeer.
- [Footerlifecycle](architecture/components/micro/FOOTER_LIFECYCLE.md): querywissel, section load/unload en cleanup.
- [Content-DOM](architecture/components/micro/CONTENT_DOM_CONTRACTS.md): lokaal zoeken, A–Z-anchors, H2/TOC-inputcontract en verse bodystructuur.
- [Disclosure/beweging](architecture/components/micro/DISCLOSURE_MOTION.md): meten, snelle reversal, late animatiepromises, reduced motion en tabindexherstel.

De brede DOC-02C-naslag voor alle 1.262 paden, 37 templates, 80 secties en 108 snippets blijft de bovenliggende kaart. De private productexport blijft afzonderlijk. Geen claim van volledige audit, mobiele werking of 100% bedrijfscompletion.

## Daadwerkelijk gecontroleerd

| Bron / methode | Resultaat en grens |
| --- | --- |
| Git-start actief | fix/product-cards-2026-10-14 op b5de803f364a597e339ed70cae9256239c178cc9 |
| Git-start main | a2e28360ff90239b6aba2421601572b98f7fb296 |
| MAIN aanvang/einde | 195818389770 — Smooth winkelwagen pop-up, niet gewijzigd |
| Gerichte bodyreads | Tien bestanden, alle MD5/grootte passend; zes bronbestanden daadwerkelijk in de harness uitgevoerd |
| Ketenreplay | **39 scenario's: 33 CONTROL_PASSED, zes BOUNDARY_CONFIRMED**, Node 24.22.1 / happy-dom 21.0.4; harde lokale transport/navigatie/geometrie/animatiestubs |
| Inbouwmapping | 715 unieke productcases/parentvarianten → 44 bodies; zes velden, alle ratio 1, geen structurele ID/identiteitsconflicten; geen fabrikant-/prijs-/voorraadgarantie |
| Pages | Drie reads, 119 Pages ontvangen; alle 109 gepubliceerde begripspagina's structureel verwerkt |
| Bodystructuur | 655 directe H2's, nul pagina's met geneste H2 of voorspelde gegenereerde-ID-botsing; geen inhoudelijke factcheck |
| Echte browser / cart | Deze verdieping niet uitgevoerd; eerder gedateerd desktopbewijs blijft apart. Geen mobiele of echte cartclaim |

[Bewijs en reproduceerbare methode](architecture/evidence/2026-10-28-transitions/README.md). Geen theme-/product-/cart-/indexwrite, formulier- of mailverzending, nieuwe dependencies, publicatie of checkoutread. Ruwe bron-/paginabodies staan buiten publiek Git.

## Bevindingen en beschermingen

- De gezamenlijke product-form/inbouwketen blokkeert niet-ready, foutieve identiteit/aantal, dubbele pending submit en uncertain retry. Ook HTTP 422 wordt conservatief uncertain; er is geen apart direct-herprobeerbaar afwijzingspad.
- Disconnect stopt componentlisteners, maar niet de afzonderlijke addrequest. Een late response op een losgekoppeld/verlaten component navigeert niet; persisted return van busy wordt uncertain.
- UI-F04: gefilterde A–Z-anchor houdt href ondanks aria-disabled; echte keyboard-/scrollimpact open.
- DATA-F04: ongeldige keuze-JSON crasht startup niet, maar blijft opgeslagen. TOC-ID-botsing alleen met synthetische input bevestigd, niet gevonden in de 109 huidige bodies.
- Footerinit blijft eenmalig bij herhaalde section load; unload verwijdert de listener. Disclosure bewaakt late animatiepromises en herstelt verborgen tabindexwaarden.
- Bestaande CART-F01, SS-F01, FOOTER-F01 en GLOSS-F01 blijven open, ongewijzigd. Settingspariteit, VPS-/appbron, Google/deploy en mobiele-/bedrijfscontroles blijven apart geregistreerd. Checkout is buiten de huidige scope.

## Exact één volgende handeling

**DOC-03C — filterfrontend als volledige toestandsketen isoleren:** URL → selectie/range/sort/page → nieuwste request → kaarten/teller → fout/native terugval → popstate. Gebruik gecontroleerde bron en harde lokale API-/verrijkingsstubs; geen live index- of cartmutatie. Zo verdiepen we de volgende brede winkelcomponent zonder checkout opnieuw te proberen.

## Hervatten en Git

Actieve branch blijft fix/product-cards-2026-10-14; main alleen documentatie. Lees deze status → AGENTS.md → betrokken microdossier/bewijs. Controleer verse MAIN/hashes en eigen werkmap; geen oude import-/publicatiestappen starten. Er blijft geen schrijver of achtergrondworker actief na oplevering.
