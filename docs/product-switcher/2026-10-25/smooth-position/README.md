# Rustige kleur- en lengtewissel — 25 oktober 2026

Status: LIVE bevestigd in laatste Shopify-readback: thema 195704357130 is MAIN en alle 553 bestanden zijn exact gelijk aan de geteste versie. Publicatie is niet door de agent uitgevoerd. De onderstaande beschrijving legt het vooraf geteste concept vast. Bron bij aanvang was MAIN `195703996682` (compacte titel en kruimelpad). Concept: `195704357130` — **BadkamerCity - rustige kleur en lengtewissel**.

## Probleem en oplossing

Na navigatie naar een andere kleur of uitlooplengte corrigeerde de oude positiehouder de scrollpositie herhaaldelijk: elke 100 ms, bij laden en tot twee seconden na window.load, met een bovengrens van 15 seconden. Dit kon layoutverschuivingen en gebruikersinvoer tegenwerken.

De nieuwe positiehouder meet eerst de layout, wacht kort op stabiele afmetingen en lettertypen en herstelt de positie maximaal één keer. Touch, pointer, wiel of toetsenbord stoppen het herstel direct. Daarna worden timers, listeners, history-instelling en tijdelijke CSS volledig teruggezet. Een onbereikbaar doel kan geen correctielus meer veroorzaken.

De al geladen keuzegroep gaat maximaal 30 seconden mee naar het exacte volgende product. Alleen bij dezelfde groep, bron-URL inclusief assetversie en een passend product wordt die direct gerenderd. Dit voorkomt opnieuw wachten op de dataset. Bij ongeldige of geblokkeerde opslag blijft de normale fetch werken. Prijs, voorraad en koopformulier komen uit de nieuwe Shopify-productpagina. De bestaande uitgeklapte kleurstaat blijft behouden.

## Scope

Enige permanente theme-wijziging: `assets/bc-product-switcher.js`. De `before/`-versie is de exacte MAIN-readback; `theme/` bevat de nieuwe versie. De bestaande ronde mobiele kleuren, titel, breadcrumbs, galerij en aankooplogica zijn niet aangepast. Dit blijft volledige productnavigatie; het is geen AJAX-productwissel. Een korte paginalaad kan nog zichtbaar zijn.

## Verificatie

- Concept vóór patch: 553/553 bestanden identiek aan MAIN.
- Finale readback: 553 bestanden, alleen de switcher-JavaScript gewijzigd; 552 identiek. MAIN 553/553 ongewijzigd. JavaScript exact teruggelezen.
- JavaScript-syntax en Shopify-validator: PASS.
- 10 deterministische positietests en 11 volledige switcher-regressiegroepen: PASS. Inclusief vertraagde fonts, veranderende layout, gebruikersinvoer, opslagproblemen, fout doel, verouderde data, ontbrekende initialisatie, gewijzigde schermbreedte en uitgeklapte mobiele kleuren.
- Echte desktopbrowser: verouderd messing 25 cm → geborsteld nikkel 25 cm → geborsteld nikkel 18 cm. Bij beide navigaties één scrollTo, daarna geen herhaalde correcties in de meting. Eindafwijking respectievelijk -2 en -1 px. Handoff beide keren gebruikt; juiste product, selectie en prijs zichtbaar.
- Daarna handmatig gescrold: menu van circa 340 naar 59 px; bleef op de nieuwe positie. Geen terugtrekken.
- Tijdelijke meetcode in `layout/theme.liquid` na de test exact hersteld, checksum gelijk aan MAIN, meetpaneel na reload afwezig. `qa-scroll.js` is alleen testgereedschap en hoort niet in het gepubliceerde thema.
- Geen fysieke iPhone/Safari-test; mobiele logica is afgedekt door DOM-regressietests. Geen conversiemeting of volledige checkouttest.

## Testen

Met Node 24: `npm install` en `npm test` in deze dossiermap. De enige testdependency is happy-dom 21.0.4. De resultaten staan in `position-test-results.json`, `switcher-test-results.json` en `browser-results.json`; checksums in `readback.json`.

## Vervolg en terugzetten

Eigenaar opent Shopify → Webshop → Thema's en bekijkt/publiceert **BadkamerCity - rustige kleur en lengtewissel**. Publiceren is niet uitgevoerd: de Shopify-connector biedt geen theme-publicatie. Na publiceren theme-rol opnieuw controleren en op de eigen telefoon kleur, lengte en direct handmatig scrollen nalopen.

Rollback: vorige thema `195703996682` opnieuw publiceren, of alleen de bewaarde `before/assets/bc-product-switcher.js` terugzetten via een gecontroleerde conceptwijziging. Geen root-theme-sync of main-code-merge uitvoeren; deze repository bevat een scoped dossier op `fix/product-cards-2026-10-14`. Lokale Windows-checkout is niet gecontroleerd.


## Laatste live-verificatie

Na oplevering van het concept bleek 195704357130 MAIN en 195703996682 UNPUBLISHED. Alle 553 live checksums zijn gelijk aan de finale geteste conceptversie. Er is geen publicatieactie meer nodig. Volgende stap is de controle door de eigenaar op een fysieke telefoon. De agent heeft geen MAIN-bestanden geschreven.
