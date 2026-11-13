# Sunshower — hoogte per gekozen productfoto

Status: IMPLEMENTED_PREVIEW / REVIEW; uitvoering afgerond, nog niet gepubliceerd. Datum: 17 oktober 2026.

De eigenaar meldt een groot wit vlak onder de eerste foto van Sunshower Round ONE Large – Opbouw – White. De tweede foto is een staande installatietekening. SKU BC-SET-SML0700-L0500-L0101, producthandle sunshower-round-one-large-opbouw-white.

## Verse basis en oorzaak

- VERIFIED_ADMIN: MAIN is 195335356682, BadkamerCity - Mobiele subcategorieen. De vorige submenu-release is dus inmiddels gepubliceerd. Volledig manifest: 487 bestanden.
- Nieuwe kopie: 195336700170, BadkamerCity - Sunshower fotogalerij, UNPUBLISHED. Vóór schrijven processing=false en 487/487 checksums gelijk aan de basis. Na schrijven: 487 bestanden, precies drie gewijzigd, alle drie inhouden exact en overige 484 identiek. MAIN blijft MAIN met alle 487 checksums ongewijzigd.
- Route: templates/product.sunshower.json → sections/main-sunshower.liquid → bc-sunshower-page.css → later geladen bc-sunshower-configurator.css, met bc-sunshower-page.js voor thumbnails en zoom.
- De configurator-CSS reserveert aspect-ratio:3/4 op desktop en 4/5 op mobiel. De foto gebruikt height:100%, object-fit:contain en object-position:top center. Een brede foto past daardoor bovenin een hoog kader. De tweede foto bepaalt die hoogte niet dynamisch; het vaste kader veroorzaakt de witte staart.
- Originele media: foto 1 2363×1477, foto 2 1104×2041. De bestaande thumbnailhandler wisselt src en verwijdert srcset, maar laat de width/height-attributen van foto 1 staan.
- Echte browser vóór wijziging, 1363×936: kader 564×752px bij beide foto's. Foto 1 is breed (geladen 560×350), terwijl foto 2 staand is (geladen 858×1587). Attributen blijven bij foto 2 onjuist 1400×875.

## Afbakening en uitvoering

Alleen het Sunshower-hoofdfotovak, thumbnailafmetingen en foto-overgang. Geen productdata, prijzen, voorraad, levertijden, zoeken, navigatie of aankooplogica wijzigen. Wiesbaden blijft geparkeerd. De eigenaar beoordeelt en publiceert het concept zelf.

De productiepatch wordt bewaard onder docs/patches; geen themabronpaden op de mogelijk gekoppelde Git-branch schrijven zolang de GitHub–themakoppeling NOT_VERIFIED is. Bestaande werklijn: fix/product-cards-2026-10-14. Windows-synchronisatie niet gecontroleerd.

## Validatie en overdracht

Codecheckpoint: 6ad6009fcef98847d5e037a71a61ea358d9baea3 op fix/product-cards-2026-10-14. Productiepatch: docs/patches/BC-sunshower-gallery-2026-10-17.patch; gedragstests: scripts/test-sunshower-gallery.cjs (themeRoot als argument).

- Acht gedragstests op het werkelijke JS-galerijblok geslaagd: voorladen, dimensies, fallback op geladen dimensies, laadfout, twee racevolgordes, annuleren via huidige thumbnail, ontbrekende foto en juiste zoombron. De acht testgevallen combineren sommige van deze controles.
- node --check geslaagd; patch voorwaarts en omgekeerd gecontroleerd tegen de verse basis/kandidaat.
- Shopify Theme Check revisie 1: alle drie bestanden geslaagd, met gebundelde docs/schemafallback na ontbrekende cache/netwerkproblemen; uitvoering met telemetry opt-out.
- Onafhankelijke read-only diffreview: geen materiële blocker in scope, CSS-specificiteit, bronmetadata, selectie, races, laadfouten of zoom.
- Concept-readback geslaagd: zie docs/sunshower-gallery-verification-2026-10-17.json voor manifesten, exactheid en Theme Check-resultaat.
- Echte productpagina 1363×936, conceptnaam/Draft in de previewbalk bevestigd: foto1 kader564×352,5px (was564×752), thumbnails16px eronder. Foto2 kader564×760, object-fit:contain en juiste attributen1104×2041. Terug naar foto1: opnieuw352,5px en attributen2363×1477. Zoom bevat de actuele technische tekening en sluit correct. Geen Liquid error. Zie docs/sunshower-gallery-browser-2026-10-17.json en screenshot sunshower-gallery-preview-1792226932363.jpg.
- De desktopbrowser kan geen mobiele viewport instellen; de mobiele 570px-cap is code-/cascadebeoordeeld, niet visueel op telefoon getest. Geen bestel-/checkout-/helecatalogustest uitgevoerd.

 Mobiele runtime/visuele iPhone-controle is NOT_TESTED: de beschikbare cloudbrowser heeft geen mobiele viewportinstelling. Dit is een expliciete beperking, geen verklaring dat de mobiele wijziging is getest.

Terugzetten: uitsluitend de drie gewijzigde bestanden herstellen uit de gecontroleerde 195335356682-basis, of de bijbehorende patch omkeren na vergelijking met eventuele vervolgwijzigingen. Geen Admin-dataherstel nodig.

Exact één volgende handeling: eigenaar opent de preview van BadkamerCity - Sunshower fotogalerij op telefoon, controleert foto1 → foto2 → foto1 en zoom en beoordeelt daarna publicatie. Geen achtergrondtaak.
