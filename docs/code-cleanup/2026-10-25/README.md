# BadkamerCity — gedeelde keuzecode en lichtere bronnen

25 oktober 2026 · PREVIEW_READY, niet gepubliceerd.

MAIN: **195704848650 — BadkamerCity - compacte keuzes desktop**. Preview: **195706257674 — BadkamerCity - code opschoning en gedeelde keuzes**. Actieve codebranch `fix/product-cards-2026-10-14`. Dit dossier bevat de releasebestanden; de root-theme snapshot is niet bijgewerkt.

## Resultaat

- Hotbath en Sunshower delen `bc-choice-position.js`: maximaal één scrollcorrectie na stabiele layout, onmiddellijke annulering bij gebruikersinvoer, opruimen van timers en tijdelijke scrollstijlen. Sunshower vraagt bij een bewaarde positie geen concurrerende native hash-scroll meer aan; bij geblokkeerde opslag blijft het anker de terugval.
- `main-product.liquid` bevat circa 900 regels minder. Dezelfde CSS-declaraties staan in `bc-product-page.css`; sectiepadding blijft instelbaar via vier CSS-variabelen, selectors behouden hun ID-specificiteit.
- Prijsopmaak laadt eenmaal centraal; dubbele verwijzingen in product-, zoek-, collectie-, winkelwagen- en andere secties zijn verwijderd. Collectieopmaak laadt eenmaal op de betreffende collectietemplates; Badkamermeubels houdt zijn eigen stylesheet.
- Drie Badkamermeubels-styleblokken zijn verplaatst naar `bc-meubelhub.css`. Het preview-thema filtert die blokken uit de weergegeven collectie-inhoud. Alle overige tekst en links blijven exact gelijk. **Shopify Admin descriptionHtml is niet aangepast**: de huidige live versie en rollback blijven daardoor bruikbaar.
- Menudata wordt per productgroep aangeboden via één gemeenschappelijke switcher. De CB105EXT-groep gaat van **227.754 naar 8.424 ongecomprimeerde bytes**; dit is geen claim over totale laadtijd of Lighthouse-score.

Er zijn **23 bestaande themabestanden gewijzigd**, **4 nieuwe codebestanden** en **656 gegenereerde JSON-data-assets** toegevoegd. Deze JSON-bestanden bevatten data, geen afzonderlijke scripts of templates. In totaal 1.213 themabestanden. Originele databronnen blijven de bron van waarheid en terugval.

## Onderhoud van de keuzedata

`build-choice-data.py` bouwt alle groepsbestanden en de Liquid-router deterministisch uit `datasets/*.json`. `source-revisions.json` bevat de publiek gerenderde `asset_url`-queryversies van die bronnen. **Bewerk gegenereerde groepsbestanden niet handmatig.**

Na wijzigingen aan de originele databronnen: haal de actuele bronnen en hun `asset_url`-revisies uit het doelconcept, werk `datasets/` en `source-revisions.json` bij, draai de generator en datatest, plaats eerst de gegenereerde assets en daarna de router. De router gebruikt een groepsbestand alleen als de oorspronkelijke bronrevisie exact overeenkomt. Bij een nieuwe bronrevisie/nieuwe groep valt Liquid terug op de originele data; bij netwerkfouten doet JavaScript hetzelfde. Een gekopieerd thema kan andere revisies krijgen: controleer dan of de optimalisatie actief blijft. Correctheid blijft door de terugval behouden.

## Bewijs

- Vooraf 553/553 bestanden identiek aan MAIN. Finaal MAIN 553/553 ongewijzigd; 683 uploadbestanden exact op checksum gecontroleerd, alle 27 codebestanden ook inhoudelijk teruggelezen. Tijdelijke product-QA-template exact hersteld.
- Shopify-validator: alle 683 bestanden PASS; aangepaste revisiebewaking en Sunshower-navigatie opnieuw PASS. Externe documentatieserver had een timeout; validator gebruikte aanwezige Shopify-schema's.
- Tests: 10 positie-, 11 switcher-, 13 aankoopgroepen; vier observerproeven; 10 Sunshowergevallen. Alle 656 JSON-groepen exact gelijk aan hun bron en alle 656 Liquid-mappings gecontroleerd. Tests voor meerdere menu's, cache per URL, netwerkterugval, opnieuw proberen en gewijzigde bronrevisies slagen.
- Product-CSS is inhoudelijk gelijk na de gedocumenteerde selector-/variabelensubstituties; drie Admin-styleblokken zijn exact behouden in het thema. Alle collectie-inhoud buiten styles blijft gelijk.
- Echte desktopbrowser Hotbath: kleur en 18/25cm wisselen, 10 kleuren blijven uitgeklapt, inbouwdeel behouden, totaal 322,01 → 496,01 → 992,02 bij aantal 2; 18cm met inbouwdeel 486,00. Aantal reset zoals voorheen bij een volledige productnavigatie.
- Echte desktopbrowser Sunshower: White → Black en terug naar White; juiste product/prijs, uiteindelijke navigatie zonder hash, daarna vrij scrollen zonder terugtrekken. Geen instrumentatieclaim over exacte pixels of gemeten navigatietijd.
- Responsive test met echte server-HTML in srcdoc-iframes van 320/390/1024 CSS-pixels: Hotbath, Sunshower en Badkamermeubels zonder horizontale overloop. Scrollbars verkleinen de inhoud tot respectievelijk 305/375/1009px. Ronde kleuren 48×48px, radius 50%, mobiele uitklapper en checkbox werken. Dit is geen fysieke iPhone-test.
- Acht HTTP-paginatypen: 200, juiste preview-assets, geen Liquid error. Prijs-CSS overal één verwijzing; categorie-CSS eenmaal waar van toepassing. Badkamermeubels desktop: nul inline style-elementen in main, één eigen stylesheet, geen overloop.

## Grenzen / open punten

- Korte producttitels en de bijbehorende filteroptimalisatie zijn op verzoek geparkeerd. De externe filtercode en index zijn niet gewijzigd.
- Acht oude back-upassets hebben geen gevonden codeverwijzingen. `themeFilesDelete` is geweigerd door de veiligheidsregel van de Shopify-koppeling: “Theme deletion is blocked — it could take down the live storefront.” Ze zijn daarom behouden. Niet via een andere route verwijderd. Deze bestanden worden niet via de gevonden themaverwijzingen geladen.
- Geen Lighthouse/CrUX-score, conversie- of volledige winkelbrede snelheidsmeting. De eerdere PageSpeed API gaf 429. Geen echte winkelwagenmutatie, betaling, fysieke Safari-test of garantie dat alle mogelijke cataloguscombinaties bugvrij zijn.
- Windows-checkout is niet gecontroleerd. Bestaande lokale wijzigingen zijn ongemoeid gelaten.

## Bestanden, tests en terugzetten

De 27 leesbare codebestanden staan onder `theme/`. `theme-after.zip` bevat exact alle 683 te plaatsen bestanden, `theme-before.zip` de 23 oorspronkelijke bestanden, `source-datasets.zip` alle brondata, `test-support.zip` ongewijzigde testafhankelijkheden/fixtures, `unused-backups.zip` de acht bewaarde back-upassets. Checksums en testuitkomsten staan naast dit document.

Tests reproduceren: pak `theme-after.zip` uit in `theme/`, `theme-before.zip` in `before/`, `source-datasets.zip` in `datasets/`, en `test-support.zip` in de dossiermap; installeer de opgegeven ontwikkeldependencies met `npm install` en draai `npm test`. Tests sturen geen winkelwagen- of betaalverzoeken.

Merchant beoordeelt het concept in Shopify → Webshop → Thema's en publiceert zelf. Daarna MAIN-rol, actieve menudatabron en de kernpaden opnieuw controleren. Terugval: het huidige thema **195704848650**; Admin-inhoud is behouden. Bij bestandsterugzetting herstellen de 23 `before`-bestanden de oude code; extra gegenereerde assets hebben daarna geen actieve verwijzing. Verwijderen van oude Admin-styles kan pas afzonderlijk na publicatie en het beëindigen van de rollback-afhankelijkheid.
