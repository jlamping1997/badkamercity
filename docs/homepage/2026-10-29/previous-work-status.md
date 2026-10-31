# BadkamerCity — actuele werkstatus

**28 oktober 2026 · UI-01 inconsistenties en gedeelde productfotopijlen.** De eigenaar geeft expliciet voorrang aan inconsistenties en kiest bij de verduidelijking **pijlen bij de productfoto’s**. DOC-03E header/zoeksuggesties is geparkeerd. Checkout blijft buiten scope.

## Ingang en stand

[Vergelijking, verbeterregister en implementatie](ui-consistency/2026-10-28/README.md). De bestaande [architectuur](architecture/README.md) en microdossiers blijven behouden.

- MAIN: **195818389770 — Smooth winkelwagen pop-up**; deze uitvoering schrijft of publiceert niet naar MAIN.
- Concept: **195850764554 — BadkamerCity - gelijke fotopijlen**, rol UNPUBLISHED.
- **PREVIEW_READY / DESKTOP_GETEST / MOBIEL_OPEN / NIET_GEPUBLICEERD.** Vooraf1.262/1.262 gelijk; finaal drie bedoelde bestanden gewijzigd/1.259 gelijk. Drie bodies exact teruggelezen, QA-template exact hersteld; MAIN1.262/1.262 ongewijzigd.
- Actieve doelbranch: fix/product-cards-2026-10-14; start521c487b9c58b49f5de36fb16de210170f24d4d8. Main-start178d55292a25f93a2c2639e97cfe18680dba72e0; main uitsluitend documentatie.

## Wat werkelijk is gevonden

**UI-F01:** Sunshower heeft pijlen op de hoofdfoto; de algemene PDP zet bestaande pijlen bij de thumbnailrail, bij een hoge afbeelding lager in beeld. De nieuwe gedeelde bediening zet44px pijlen op de foto, een teller en begrensde randen. Nul/één medium blijft zonder nieuwe bediening. Geen tweede zoom-/cartcontroller. De code staat uitsluitend in het genoemde concept.

Drie overige desktopverschillen zijn bevestigd: **UI-C01** Lees meer/Toon meer; **UI-C02** winkelwagenknop56px/radius40 versus49px/radius8; **UI-C03** Ja/Nee-tekst versus toegankelijke vink/kruisiconen. Dit zijn nog niet aangepaste consistentie-/ontwerpkeuzes, geen automatisch bewezen verkoopbugs. UI-S01 native no-image-dubbeltitel blijft kandidaat: de settled collectie gebruikt extern. De bestaande uitgebreide Hotbath-viewer bladert en sluit met Escape.

## Bewijs en grenzen

- 29 bestaande bronfiles opnieuw passend bij verse Shopify-metadata; volledig startmanifest1.262 paden.
- Browser desktop1363×936: Sunshowerlanding/PDP, Wiesbaden24.3710, HotbathSDS1GN14 en Wastafelkranen. Renderer/laadstaat expliciet; geen volledige winkelbrede visuele audit.
- 15 lokale galerijcontroles op bestaande SliderComponent en kandidaat-MediaGallery; simulatie van geometrie/media/timers/animatie. Geen native mobiele/keyboard/touchvrijgave hieruit afleiden. Afzonderlijk is echte Space-bediening op desktop wel bevestigd.
- Statische Shopify-validatie van drie kandidaatfiles geslaagd. Alleen testhulpmiddelen in scratch geïnstalleerd; geen runtimebibliotheek aan de winkel toegevoegd.
- Geen product-/prijs-/voorraadwrite, echte cart-/wishlistactie, account-/checkoutread of formulier-/mailverzending. Git-root-themacode wordt niet blind gesynchroniseerd.

## Exact één volgende handeling

**Eigenaar beoordeelt het concept ‘BadkamerCity - gelijke fotopijlen’ op desktop én mobiel vóór publicatie.** Desktop-Wiesbaden/Hotbath en Space-bediening zijn bevestigd; de320/390/1024px iframepoging werd geweigerd en telt niet als mobielbewijs. De15 lokale controles blijven afzonderlijk geldig. De drie overige ontwerp-/tekstverschillen staan in het verbeterregister voor gerichte vervolgstappen.

## Overdracht

Lees deze status → AGENTS.md → het UI-01-dossier. Eerdere FILTER-F01/F02, CART-F01, SS-F01, WISH-F01/F02 en overige bevindingen blijven open. Settings-bytepariteit, VPS/appbron, Google/deploy en echte bedrijfs-/apparaatcontroles blijven apart open. Geen Windowscontrole of automatische live-uitrol claimen.

Geen eigen schrijver, testserver of Shopify-kopiejob actief na oplevering. De gewone storefront-URL bevat geen blijvende previewcontext; beoordeel via het genoemde Shopify-concept of de behouden browserpreview.
