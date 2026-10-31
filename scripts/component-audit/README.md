# Afzonderlijke componentcontracten onderzoeken

Offline audit van vier benoemde actuele JS-bronnen, met synthetische data en harde fetch-/navigatiestubs. Geen Shopify-auth, echte netwerk-/cartacties of theme-writes. Dit is een reproductie-/regressiebasis, geen volledige browser- of verkooptest.

Vanaf de actieve branch, met een afzonderlijke gecontroleerde bronmap:

```bash
npm ci --prefix scripts/component-audit --ignore-scripts
node scripts/component-audit/audit.mjs \
  --source /pad/naar/gecontroleerde-themefiles \
  --manifest docs/architecture/evidence/2026-10-28-micro/source-provenance.json \
  --output /tmp/badkamercity-component-audit.json
```

De bronmap moet assets/cart-notification.js, bc-product-switcher.js, bc-sunshower-page.js en bc-product-inbouw.js bevatten. Iedere bron wordt vóór uitvoering op de vastgelegde SHA-256 gecontroleerd. Dit manifest is gedateerd; bij andere bronbytes een nieuwe inhoudelijke audit en nieuw bewijs maken, geen hashcontrole uitschakelen. Optioneel --dom-module geeft een expliciete ESM-modulefile voor een reeds geïnstalleerde happy-dom 21.0.4; de gepinde lock is vergeleken met de werkelijk gebruikte dependency-installatie.

Het rapport benoemt CONTROL_PASSED, BOUNDARY_CONFIRMED en DEFECT_REPRODUCED afzonderlijk. Een geslaagde uitvoering kan dus bewust een bestaande fout reproduceren. CN-02/CN-03 zijn dezelfde inhoudsfout onder twee stimuli; SS-01 is een andere actierace. Een toekomstige correctie moet die verwachtingen herschrijven naar het gekozen veilige gedrag en de normale controles behouden. Geen bekende fout als “alle tests groen, winkel klaar” doorgeven.

Broncode blijft buiten deze harness; er wordt geen deploybare themecopy gemaakt of productdata geëxporteerd. Lees de dossiers onder docs/architecture/components/micro en bewaar relevante oude proofresultaten bij een nieuwe audit.

## Volledige ketens sinds DOC-03B

`transitions.mjs` voegt de daadwerkelijke product-form en inbouwcontroller samen in synthetische formulieren. Daarnaast voert hij het exacte JavaScript uit footer-/begrippensecties en productdisclosure uit, met gecontroleerde mediaqueries, geometrie, timers en animatiepromises. Geen Liquid-rendering, browserviewport- of server/cartvrijgave.

```bash
node scripts/component-audit/transitions.mjs \
  --source /pad/naar/gecontroleerde-themefiles \
  --manifest docs/architecture/evidence/2026-10-28-transitions/source-provenance.json \
  --output /tmp/badkamercity-transitions.json
```

Gebruik dezelfde gepinde happy-dom 21.0.4/installatie als boven; `--dom-module` werkt ook hier. Alle zes daadwerkelijk uitgevoerde bronbestanden worden vooraf op SHA-256 gecontroleerd. Sectie-JavaScript wordt ongewijzigd uit de expliciete plain script/javascript-blocks gehaald; Liquidtokens daarin worden geweigerd. Het bewijsmanifest bevat tien gelezen bronnen, waaronder vier aanvullende bron-/mappingbestanden die inhoudelijk zijn gevolgd maar niet als JS worden uitgevoerd.

De 39 cases bestaan uit 33 CONTROL_PASSED en zes BOUNDARY_CONFIRMED. Grenzen zijn geen nieuwe bewezen live defects. De fixtures dispatchen submit rechtstreeks om de JS-route te volgen; native HTML formvalidation, echte focus/CSS/touch en Shopify carttransacties zijn niet nagebootst als browsersucces. De inhoudsscan van 109 Page-bodies en mappingcontrole van 715 regels zijn afzonderlijke structurele analyses, geen onderdeel van de 39 synthetische cases.

## Filterketen sinds DOC-03C

`filters.mjs` voert de volledige externe filterclosure, listinghelper en in één interactiecase de native facets-handler/gridmethode uit. Alle drie bronbestanden worden vooraf op SHA-256 gecontroleerd; de overige zes in het bewijsmanifest zijn inhoudelijke code-/CSS-/Liquid-context. Geen echte API, cart of index in de replay.

```bash
node scripts/component-audit/filters.mjs \
  --source /pad/naar/gecontroleerde-themefiles \
  --manifest docs/architecture/evidence/2026-10-28-filters/source-provenance.json \
  --output /tmp/badkamercity-filters.json
```

Dezelfde pinned happy-dom 21.0.4 en optionele --dom-module gelden. De 41 cases omvatten 35 controles, twee defectreproducties en vier grenzen. FX-37 behoudt de echte native popstate-handler en containervervangingsmethode; alleen native requestorkestratie is een stub. Numerieke validity gebruikt een expliciet tolerant testmodel vanwege een aangetroffen DOMlibrary-precisieverschil. Dit is geen native browser/CSS-/focus-/mobiel-/volledige historytest. Lees de proof-README vóór conclusies.

## Wishlist en browseropslag sinds DOC-03D

`wishlist.mjs` voert de hele wishlistclosure en in één adaptercase ook de hele Sunshower-shopclosure uit. Beide bronnen worden vooraf op SHA-256 gecontroleerd. Gebruik de bestaande gepinde installatie; --dom-module werkt ook hier.

```bash
node scripts/component-audit/wishlist.mjs \
  --source /pad/naar/gecontroleerde-themefiles \
  --manifest docs/architecture/evidence/2026-10-28-wishlist/source-provenance.json \
  --output /tmp/badkamercity-wishlist.json
```

43 cases: 34 CONTROL_PASSED, twee DEFECT_REPRODUCED, zeven BOUNDARY_CONFIRMED. Twee synthetische windows delen een Map; storage-events worden handmatig bezorgd. Product-GET/cart-POST zijn uitsluitend fetchstubs, navigatie/timers/imagepreload zijn gecontroleerd. Twee cases gebruiken de DOMlibrary-observer; geen echte browser-multitab-, CSS-, focus-, touch-, cart- of restoretest. Lees de proof-README voor bronhergebruik, guardcontrole en per-casegrenzen. Een nieuwe bronhash vraagt inhoudelijke herbeoordeling, geen uitschakelen van de hashguard.

## Kandidaat-galerij UI-01

`gallery.mjs` voert de bestaande hashgecontroleerde global.js/SliderComponent samen met de kandidaat-MediaGallery uit. Geef --source, --candidate, --manifest en --output; --dom-module kan dezelfde gepinde happy-dom21.0.4 gebruiken. De15 cases bewijzen selectie-/grens-/variant-/reduced-motion-/annuleringscontracten onder gecontroleerde geometrie/mediaqueries. Lees [het UI-01-dossier](https://github.com/jlamping1997/badkamercity/blob/fix/product-cards-2026-10-14/docs/ui-consistency/2026-10-28/README.md) voor de volledige opdracht. Native browser-/touch-/koopgedrag volgt niet uit deze replay.
