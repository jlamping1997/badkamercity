# BadkamerCity — actuele werkstatus

**28 oktober 2026 · DOC-03D verlanglijst en browseropslag.** Eigenaar vraagt de volgende documentatieverdieping. Checkout blijft expliciet buiten scope. Eerdere microdossiers en bevindingen zijn behouden; dit vervolg volgt bewaren → identity → events → render/cache → gecontroleerde kooproute.

## Ingang en resultaat

[Architectuur](architecture/README.md) → [dekking](architecture/COVERAGE.md) → [microdossiers](architecture/components/micro/README.md). Drie nieuwe eigenaarspagina's:

- [Opslag en tabbladen](architecture/components/micro/WISHLIST_STORAGE.md): schema, fouten, commitgrens, events en selectieoverschrijving.
- [Identity en hartjes](architecture/components/micro/WISHLIST_IDENTITY.md): gedeelde callers, variantprioriteit, refresh en Sunshower-kleurcommit.
- [Renderen en toevoegen](architecture/components/micro/WISHLIST_RENDER_AND_ADD.md): productpromise/cache, vier workers per render, late antwoorden, koopguards en cartnavigatie.

Geen productiecorrectie uitgevoerd. De eerdere brede naslag/private productexport blijven de bovenliggende bronnen; geen volledige thema- of productexport herhaald.

## Werkelijk uitgevoerd

| Bron / methode | Resultaat en grens |
| --- | --- |
| Git-start actief | fix/product-cards-2026-10-14 op 8227eaed86c2386391b8b27a210d1490942ce2b3 |
| Git-start main | cb685367c3ab75738a3ba2644eb5dd28d8e09ab7 |
| MAIN aanvang/einde | 195818389770 — Smooth winkelwagen pop-up, dezelfde rol/updatedAt |
| Gerichte broncontrole | Vijftien verse MD5/grootte-metadatareads passen bij eerder ontvangen bronbytes; eindread opnieuw gelijk. Geen nieuwe bodydownload geclaimd |
| Uitgevoerde broncode | Volledige wishlistclosure; in WL-43 ook volledige Sunshower-shopclosure, beide vooraf SHA-256-gecontroleerd |
| Replay | **43 cases: 34 CONTROL_PASSED, twee DEFECT_REPRODUCED, zeven BOUNDARY_CONFIRMED** |
| Omgeving | Node 24.22.1, bestaande happy-dom 21.0.4; synthetische storage/events/transport/timers/navigatie/imagepreload; twee cases met DOMlibrary-MutationObserver |
| Browser en bedrijfswerking | Geen nieuwe browseractie, echte bezoekersopslag, cart-/restore-/indexactie, productdatawrite of checkoutread. Geen mobiele/focus/a11y/prijs-/voorraadvrijgave |

[Bewijs, exacte scenario's en reproduceerbare methode](architecture/evidence/2026-10-28-wishlist/README.md). Alleen documentatie en offline audittooling gewijzigd; ruwe bron-/winkelbodies blijven buiten publiek Git. Geen nieuwe dependency, formulier-/mailverzending, deployment of publicatie.

## Nieuwe bevindingen en bevestigde bescherming

- **WISH-F01 / VERIFIED_ISOLATED / P2-kandidaat:** twee tabbladen schrijven vanuit eigen geheugen. Bij bewust vertraagde storage-eventbezorging overschrijft de tweede toevoeging de eerste. Twee echte closures/gedeelde synthetische opslag; geen native browser-timing of huidig bezoekersincident gemeten.
- **WISH-F02 / VERIFIED_ISOLATED / P2-kandidaat:** Sunshower-shopkleur commit nieuwe handle/variant, maar hartje houdt is-saved/aria-pressed van vorige kleur. Volgende hartklik bewaart wel de juiste nieuwe identity. Imagepreload nagebootst; geen actuele visuele browserwaarneming.
- **WISH-B01 / grenzen:** malformed/ander schema/read-denied ogen leeg; opgeslagen duplicaten blijven; unavailable favoriet mag; productcache heeft geen TTL/requesttimeout. Geen zeven extra live bugs of gegarandeerd realtime prijs-/voorraadgedrag.
- Positief: mislukte opslag houdt oude staat en meldt geen succes-event; eigen busybutton blokkeert dubbelklik; missende variant krijgt geen koopbutton; laat productantwoord zet verwijderde kaart niet terug; synthetische add gebruikt exact toegestane variant en behoudt de favoriet.
- Eerdere FILTER-F01/F02, CART-F01, SS-F01, FOOTER-F01, GLOSS-F01, UI-F04 en DATA-F04 blijven open. Settingspariteit, verse VPS/appbron, Google/deploy en echte browser-/bedrijfscontroles blijven afzonderlijk open.

## Exact één volgende handeling

**DOC-03E — headernavigatie en predictive search als afzonderlijke controllers volgen:** desktopcategorieën, mobiele panelStack, overlay/focus/resize/section-lifecycle en nieuwste zoekintentie/cache/foutpad met synthetische markup en responses. Geen account-/bezoekersdata, formulierverzending, cartactie of checkoutread. Werkelijke browser-/mobielcontrole apart registreren.

## Hervatten en Git

Actieve doelbranch blijft fix/product-cards-2026-10-14; main alleen documentatie. Lees deze status → AGENTS.md → betrokken microdossier/bewijs. Controleer verse MAIN/hashes en eigen werkmap; start geen oude import-/publicatiestappen. Deze omgeving werkt op geverifieerde remote checkpoints; oudere lokale branchtips zijn behouden en niet geforceerd herschreven. Geen Windows-synchronisatieclaim. Geen schrijver of achtergrondworker blijft actief na oplevering.
