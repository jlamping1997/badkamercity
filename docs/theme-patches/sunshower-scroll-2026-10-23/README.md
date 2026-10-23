# Sunshower scrollpositie — 23 oktober 2026

De eigenaar meldde na publicatie van de eerste fix dat de eerste wissel nog terugspringt. Bron is de actuele Shopify-code; afwijkende root-themacode in Git niet gebruiken.

| Rol | Thema |
| --- | --- |
| MAIN, ongewijzigd | 195610116362 — BadkamerCity - Sunshower scrollpositie 23 okt |
| Nieuwe herstelpreview | 195611197706 — BadkamerCity - Sunshower eerste wissel 23 okt |
| Actieve branch | fix/product-cards-2026-10-14 |

De kopie was vóór schrijven 512/512 checksum-identiek. Na schrijven en onafhankelijke readback: exact één gewijzigde asset, overige 511 gelijk, MAIN 512/512 gelijk. Asset-MD5: e2f193488f4e2ec132f0b2d70d161a44.

De positie wordt direct bij de klik vastgelegd, vóór opties worden uitgezet of de catalogus wordt opgehaald. Daardoor kan een eerste trage fetch geen later versprongen positie opslaan. Correctie stopt na load plus twee seconden, met vijftien seconden bovengrens en directe annulering bij pointer/touch/wheel/keyboard/pagehide. Browser-scrollrestoration staat gedurende die korte herstelperiode op manual en wordt daarna teruggezet. Normale bezoeken zonder herstelrecord blijven ongewijzigd. De native configuratorhash voorkomt terugvallen naar de paginatop als opslag niet bruikbaar is. Routematching negeert alleen preview_theme_id en sorteert de overige parameters; productroute, view en bronselectie blijven bepalend. Eénmalige opslag en 30 seconden TTL behouden.

**Tests:** Node syntax PASS; Toolkit Theme Check R1 SUCCESS met gebundelde schemafallback; 16 gecontroleerde JS-cases PASS. De vorige versie faalt vijf gecontroleerde situaties. Testharness oefent de echte configuratorcode uit de asset uit in JSDOM/VM met gecontroleerde timers/netwerk/layout. Installeer jsdom uit npm en voer uit:

```bash
node scroll-regression.cjs bc-sunshower-page.js
```

Echte browserpreview 1363×936: eerste kleur White→Black top252,828→252,828px, scrollY330; daarna handmatig verder scrollen en Medium→Small top210,625→210,625px, scrollY517. Alleen native klikken/scroll gebruikt. De oorspronkelijke fout kwam bij verse desktopnulmeting niet terug; precieze telefoonoorzaak niet vastgesteld. Trage aanvraag/late load zijn simulaties, geen bewijs van een fysieke telefoon of trage browserverbinding. Fysieke mobiel, smalle viewport, checkout en Windows lokaal NOT_TESTED. Geen aankoop of product-/indexmutatie.

**Terugzetten:** herstel alleen de asset uit bc-sunshower-page.first-switch-before.js in het nieuwe concept. bc-sunshower-page.before.js blijft de oudere bron vóór de eerste scrollfix. Houd MAIN staan als het concept niet voldoet. Geen root-theme-push zolang Shopify-Git-integratie onbekend is.

**Exact volgende handeling:** eigenaar opent het nieuwe concept, begint vanaf Sunshower, test de allereerste kleur-/modelkeuze op telefoon en beoordeelt publicatie. Daarna MAIN en openbare storefront opnieuw lezen. Agent heeft niet gepubliceerd.
