# Sunshower — hoogte per gekozen productfoto

Status: uitvoering in concept; nog niet gepubliceerd. Datum: 17 oktober 2026.

De eigenaar meldt een groot wit vlak onder de eerste foto van Sunshower Round ONE Large – Opbouw – White. De tweede foto is een staande installatietekening. SKU BC-SET-SML0700-L0500-L0101, producthandle sunshower-round-one-large-opbouw-white.

## Verse basis en oorzaak

- VERIFIED_ADMIN: MAIN is 195335356682, BadkamerCity - Mobiele subcategorieen. De vorige submenu-release is dus inmiddels gepubliceerd. Volledig manifest: 487 bestanden.
- Nieuwe kopie: 195336700170, BadkamerCity - Sunshower fotogalerij, UNPUBLISHED. Voor schrijven moeten processing=false en alle 487 checksums gelijk zijn aan de basis.
- Route: templates/product.sunshower.json → sections/main-sunshower.liquid → bc-sunshower-page.css → later geladen bc-sunshower-configurator.css, met bc-sunshower-page.js voor thumbnails en zoom.
- De configurator-CSS reserveert aspect-ratio:3/4 op desktop en 4/5 op mobiel. De foto gebruikt height:100%, object-fit:contain en object-position:top center. Een brede foto past daardoor bovenin een hoog kader. De tweede foto bepaalt die hoogte niet dynamisch; het vaste kader veroorzaakt de witte staart.
- Originele media: foto 1 2363×1477, foto 2 1104×2041. De bestaande thumbnailhandler wisselt src en verwijdert srcset, maar laat de width/height-attributen van foto 1 staan.
- Echte browser vóór wijziging, 1363×936: kader 564×752px bij beide foto's. Foto 1 is breed (geladen 560×350), terwijl foto 2 staand is (geladen 858×1587). Attributen blijven bij foto 2 onjuist 1400×875.

## Afbakening en uitvoering

Alleen het Sunshower-hoofdfotovak, thumbnailafmetingen en foto-overgang. Geen productdata, prijzen, voorraad, levertijden, zoeken, navigatie of aankooplogica wijzigen. Wiesbaden blijft geparkeerd. De eigenaar beoordeelt en publiceert het concept zelf.

De productiepatch wordt bewaard onder docs/patches; geen themabronpaden op de mogelijk gekoppelde Git-branch schrijven zolang de GitHub–themakoppeling NOT_VERIFIED is. Bestaande werklijn: fix/product-cards-2026-10-14. Windows-synchronisatie niet gecontroleerd.

## Validatie en overdracht

Wordt ingevuld na tests, concept-readback en browsercontrole. Mobiele runtime/visuele iPhone-controle is NOT_TESTED: de beschikbare cloudbrowser heeft geen mobiele viewportinstelling. Dit is een expliciete beperking, geen verklaring dat de mobiele wijziging is getest.

Terugzetten: uitsluitend de drie gewijzigde bestanden herstellen uit de gecontroleerde 195335356682-basis, of de bijbehorende patch omkeren na vergelijking met eventuele vervolgwijzigingen. Geen Admin-dataherstel nodig.
