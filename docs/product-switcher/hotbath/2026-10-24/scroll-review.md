# Onafhankelijke review van opt-in scrollbehoud — 24 oktober 2026

**Uitkomst: PASS voor de onderzochte codescope.** Geen materiële bug gevonden in routevalidatie, opslagafhandeling, eerste wissel, vertraagde menu-initialisatie, late layoutwijzigingen of annulering door gebruikersinput. Geen API-, Shopify- of GitHub-mutaties uitgevoerd.

Gecontroleerd: `scroll_position.js`, de ingebedde helper en integratie in `preview-theme/assets/bc-product-switcher.js`, `test_scroll_position.cjs`, de opt-in-attributen in de snippet en de vier expliciete data-URL-toewijzingen in `main-product.liquid`.

- De 15 Node-tests opnieuw uitgevoerd: **15 PASS, 0 FAIL**.
- De ingebedde helper is exact gelijk aan `scroll_position.js`.
- Capture gebeurt vóór het uitschakelen van het menu. Herstel begint pas na renderen van het bestemmingsmenu.
- Herstel vereist dezelfde oorsprong, route, semantische query/hash, groep, geldige positie en een token van maximaal 30 seconden oud. Alleen `preview_theme_id` wordt bij vergelijken genegeerd.
- Het token wordt eenmaal verbruikt. Gebruikersinput en pagehide stoppen herstel; storagefouten blokkeren navigatie niet.
- Herstel eindigt twee seconden na load/render, met een harde limiet van vijftien seconden. De tijdelijke scrollrestoration- en stijlwaarden worden teruggezet.
- Alle **3.383 bestaande JSON-productroutes** voldoen aan de nieuwe URL-/handle-guard.
- Roots zonder opt-in raken geen positieopslag, history.scrollRestoration, scrollstijl of scrollpositie.

## Scope

De vier expliciete data-URL-groepen zijn IBS70, BAA03, BAA09 en BAA10. BAA03 is één van de bestaande 433 groepen en krijgt bewust de nieuwe positieflow. De overige **432 bestaande groepen** blijven buiten die opt-in. De bestaande gedeelde JSON hoeft hierdoor niet te wijzigen.

## Bewijsgrens

Dit is een onafhankelijke code- en synthetische regressiereview. Echte mobiele touch/inertie, visuele Shopify-preview en fysieke telefoons zijn hiermee niet getest; die resultaten moeten afzonderlijk door de uitvoerende sessie worden vastgelegd.
