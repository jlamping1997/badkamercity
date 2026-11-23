# Bewijs DOC-03B: toestandsovergangen, lifecycle en inputcontracten

Bronmoment **28 oktober 2026**. Eigenaar kiest verdere verdieping van de overige onderdelen; checkout blijft buiten deze ronde. Geen checkoutresource bevraagd, formulier naar de winkel verstuurd, echte cartactie, product-/theme-/indexwrite of publicatie uitgevoerd.

## Verse bronnen

[source-provenance.json](source-provenance.json) bevat tien gerichte MAIN-bodyreads met MD5/grootte uit dezelfde response en SHA-256 van de ontvangen bytes. Alle tien passen; geen volledige 1.262-bestandenscan opnieuw uitgevoerd. MAIN bij aanvang: 195818389770, Smooth winkelwagen pop-up. Git-baselines: actieve branch b5de803f364a597e339ed70cae9256239c178cc9; main a2e28360ff90239b6aba2421601572b98f7fb296.

De harness voert zes hashgecontroleerde bronnen uit: inbouwcontroller, product-form, productdisclosure en ongewijzigde JS-blocks uit footer, glossary en glossary-page. Vier extra Liquid-/mapping-/adviesbronnen zijn inhoudelijk gevolgd, niet als JavaScript uitgevoerd. Ruwe sourcebodies blijven buiten publiek Git.

## 39 geïsoleerde scenario's

[results.json](results.json): **33 CONTROL_PASSED, zes BOUNDARY_CONFIRMED**. Geen nieuwe bewezen live defectreproductie in deze ronde. De eerdere CART-F01 en SS-F01 zijn niet gecorrigeerd of opnieuw gesloten.

| Cases | Methode / uitkomst |
| --- | --- |
| IBX-01…07 | Echte product-form + addon samen; unready/keuze/identiteit/aantal/bodybeschikbaarheid en Nee-delegatie |
| IBX-04 | Exacte tweeregelpayload, properties/plan alleen parent, tweede submit geblokkeerd, payloadsnapshot en bevestigde navigatie |
| IBX-08…15 | HTTP 422, JSON/netwerk, onvolledige items, SKU/aantalafwijking en 30s-timeout; uncertain en cartcontrolelink |
| IBX-16…17 | Pagehide/persisted pageshow en disconnect; requesteigenaarschap en navigatiegrens |
| IBX-18…25 | Keuzehandoff: groep/body/route/leeftijd, corrupte JSON en expliciet versus impliciet Nee |
| FT-01…02 | MatchMedia-staten, herhaald section load, unload en opnieuw initialiseren |
| GL-01…02 | Keywords/case/trim/nul/wissen; aria-disabled anchor houdt nog href zonder klikpreventie |
| TOC-00…04 | Nul/één/twee directe H2, tweede uitvoering, geneste H2/existente ID en synthetische ID-botsing |
| DS-01…05 | Clamp/hoogte, tabindexherstel, reversal/late finished-promise, reduced motion, spec-breakpoint en cleanup |

De zes grenzen zijn: grotere responsehoeveelheid geaccepteerd; disconnect stopt request niet; corrupte keuze-JSON blijft opgeslagen; gefilterde A–Z-anchor blijft een anchor; geneste H2 is geen TOC-entry; bestaand ID kan in synthetische content botsen met een gegenereerd ID. Geen van deze zes is hier als aangetoond huidig klantincident geregistreerd.

Node **24.22.1**, happy-dom **21.0.4** uit de bestaande gepinde installatie. Geen nieuwe dependency geïnstalleerd. Transport, navigatie, timers, geometrie, matchMedia, observers en animations zijn lokale test doubles. De submitfixtures dispatchen events rechtstreeks: geen native HTML-validatie-/focus-/toegankelijkheids-/CSS-/touch-/bfcache-/echte servervrijgave. Een telefoonflag in de fixture is geen mobiele browser.

## Volledige structuurmetingen binnen de gekozen bron

- [mapping-validation.json](mapping-validation.json): 715 regels, 715 unieke productcases/parentvarianten, 44 bodyvarianten; zes velden per regel, alle verhoudingen 1, geen parent=body en geen conflicterende body-ID/handle/SKU. Geen nieuwe fabrikant-/voorraad-/prijs-/publicatiecontrole.
- [content-validation.json](content-validation.json): drie gepagineerde Pages-reads, 119 ontvangen; alle 109 gepubliceerde begripspagina's structureel verwerkt. Samen 655 directe H2's, nul pagina's met geneste H2 of voorspelde ID-botsing. Alleen handle, bodyhash, bytes en tellingen openbaar; geen ruwe bodies. Dit is geen inhoudelijke factcheck of hercontrole van alle redirectdoelen.

De eerste harnessrun vond een onjuiste fixtureaanname: corrupte JSON werd niet verwijderd. De verwachting is gecorrigeerd naar het werkelijk aangetoonde broncontract en als grens geclassificeerd. Productiecode is daarvoor niet aangepast. De finale 39-case-run is het bewaarde resultaat.

## Herhalen

[scripts/component-audit](https://github.com/jlamping1997/badkamercity/tree/fix/product-cards-2026-10-14/scripts/component-audit) bevat `transitions.mjs` en de gepinde package-lock. Lees eerst de README; voer uit tegen de benoemde aparte bronmap en dit manifest. Geen hashes uitschakelen of gelijknamige oude Git-rootfiles gebruiken.

De vier [methodedossiers](../../components/micro/README.md) geven de interpretatie, eigenaar, herstel-/wijzigingsgrens en nog open controles. Privéproductdata, klant-/order-/cartinhoud, appkeys en credentials blijven buiten deze proof.
