# Sunshower scrollpositie — 23 oktober 2026

Eigenaar vraagt kleur/model/formaat/montage tussen aparte Sunshower-productpagina’s te kunnen wisselen zonder terug naar de paginatop te springen.

Actieve branch: `fix/product-cards-2026-10-14`. Bron is vers uit Shopify MAIN `195491168522` gelezen, niet de afwijkende root-themacode in Git. Alleen `assets/bc-sunshower-page.js` wijzigen. Bewaar bron en aangepaste productiefile hier; push deze niet blind naar root zolang de Shopify-Git-koppeling onbekend is.

Nieuwe conceptkopie `195610116362` — `BadkamerCity - Sunshower scrollpositie 23 okt`. Bij dit checkpoint nog aan het kopiëren; pariteit, upload en storefronttest volgen. MAIN is niet geschreven of gepubliceerd.

Contract: vóór een geslaagde configuratie-navigatie de doelroute incl. previewquery, veldcode en schermoffset van het gekozen veld in sessionStorage bewaren. Eén keer op precies die route binnen 30 seconden herstellen. Een korte ResizeObserver/load/fonts-correctie vangt verschuivende layout op, stopt na 2 seconden en direct bij pointer/touch/wheel/keyboard/pagehide. Geen record bij gewone links, geen effect op andere PDP’s en bij geblokkeerde opslag normale productnavigatie behouden.

Bewezen bij voorbereiding: Node syntaxcheck PASS; geïsoleerde JavaScript-VM-proef PASS voor ankerherstel, layoutverschuiving, afbreken bij scrollinput, eenmalig gebruik, juiste doelroute, verlopen/toekomstige/ongeldige waarden, ontbrekend veld, geblokkeerde opslag en previewquery. Dit is geen browser-/telefoontest. De Shopify Toolkit Theme Check kon niet starten door ontbrekend `@shopify/theme-check-common`; geen Theme Check PASS geclaimd.

Browsernulmeting desktop 1363×936: ONE Large Hoek Black → Organic grey: kleurveld vóór 161,828 px (scrollY421), na 582,828 px (scrollY0). Probleem gereproduceerd.

Terugzetten: uitsluitend deze asset terugzetten uit `bc-sunshower-page.before.js`, of huidige MAIN laten staan. Productdata, prijzen, voorraad, winkelmand en overige theme-files vallen buiten de wijziging.

Volgende handeling: wacht tot concept volledig is gekopieerd; vergelijk alle 512 checksums met MAIN vóór enige upload, pas de ene asset toe en controleer echte productwissels in de browser. Eindstand en publicatie blijven apart vastleggen.
