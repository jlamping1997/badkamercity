# Oude productkaarten en 404-afhandeling

15 november 2026 · CARD-AVAILABILITY-01 · VERIFIED_PREVIEW / PUBLICATION_PENDING.

Een externe lijst kon een inmiddels verborgen product blijven tonen met 'Bekijk prijs' en een link naar een 404. De kaartverrijking maakte geen onderscheid tussen een ontbrekend product en een tijdelijke laad-/renderfout.

## Werkend gedrag in het concept

- Een expliciete 404/410 verwijdert alleen de betreffende kaart. Shopify geeft voor G6110 bij sections=bc-card-data echter HTTP200 met een lege sectie. Bij ontbrekende kaartdata volgt daarom één aanvullende product-JSON-read; alleen een bevestigde404/410 daar bewijst onbeschikbaarheid.
- Time-out, netwerkfout, 5xx, ongeldige JSON, null-sectie met bestaande product-JSON en verkeerde product-ID blijven onzeker: kaart behouden, geen koopknop activeren op onbetrouwbare data.
- Kaarten zijn tijdens de controle inert. Een onbeschikbare kleurkeuze behoudt de laatst bevestigde productkaart/link/prijs.
- Succesvolle kaartdata worden bij iedere nieuwe lijstrequest opnieuw gecontroleerd. Terugkomen via bfcache en terugkeren naar een minstens30seconden verborgen tab verversen de lijst; een lopende cart-add wordt bij tabterugkeer ontzien.
- Na bevestigde veroudering wordt geen exact catalogustotaal verzonnen: de teller vermeldt expliciet het aantal op deze pagina. Originele pagina-offsets en volgende/vorige blijven behouden; een lege pagina geeft een passende melding. Facetcounts blijven indexgegevens en zijn hiermee niet volledig gerepareerd.

## Bron en doel

MAIN **196690379018 — BadkamerCity - complete filterkleuren** blijft ongewijzigd. Doel **UNPUBLISHED196542005514 — BadkamerCity - bescherming oude productkaarten**. Beide hadden2522bestanden; vóór de patch verschilde uitsluitend de oude kleuren-JS in het doel. De patch is gemaakt op de verse MAIN-bron en behoudt dus de zes kleurcorrecties en Lagoo-documenten.

Vier functionele wijzigingen in shopify/current/: assets/bc-external-filters.js, snippets/bc-external-filters.liquid, locales/nl.json en locales/en.default.json. Alle vier doelbodies exact teruggelezen. [Volledige vergelijking en tests](verification.json): MAIN2522ongewijzigd, doel2524, uitsluitend deze vier gewijzigde bestaande bestanden plus twee eigen QA-bestanden.

**QA-opruiming:** de connector blokkeert themeFilesDelete generiek als destructief. Geen andere verwijderroute geprobeerd. Veiliger herstel: eigen testsectie teruggebracht tot een lege schema-sectie; het alternatieve paginatemplate exact gelijkgemaakt aan het bestaande standaard page.json. Beide bodies exact teruggelezen. De twee ongebruikte bestanden bevatten geen mock-fetch, testproducten of actief testscript meer. De volledige oorspronkelijke proefsectie staat alleen hier als [reproduceerbare fixture](qa-section.liquid). Er is geen live template of catalogusdata gewijzigd.

## Bewijs en grenzen

**30gerichte JSDOM-gedragstests PASS**, nul skips/fouten. Volledige JS-uitvoering: collectie/zoeken,200lege sectie+404/410, transportfouten, verkocht/niet-op-voorraad, lege pagina, originele offsets, herpublicatie, racebescherming, kleurwissel, cache/bfcache/tabterugkeer, cart-busy-guard, filters en sortering.

De bestaande32-testsuite geeft zowel op originele MAIN als op de kandidaat26PASS/6FAIL: dezelfde zes historische prijsverwachtingen. Er zijn nul nieuwe fouten in die vergelijking; prijs-/tegeleenheidsopmaak niet gewijzigd. Niet als32PASS opvoeren. Node syntax PASS; officiële Theme Validator rev2 alle zes toenmalige patch-/QA-files PASS. De stateless templatecheck miste eerst de sectiecontext; de volledige themacontext bevestigt de koppeling. Officiële meegeleverde docset gebruikt na netwerk-time-out bij de nieuwste docset; bronoverdracht/telemetrie uitgeschakeld.

**Echte Chrome desktop:** geïsoleerd verouderd indexantwoord met G1104TC+G6110, zonder catalogus-/indexwrite. De productreads lopen werkelijk naar Shopify. Na controle blijft één kaart/G1104TC over; nul G6110-links; correcte pagina-telling. Bekijk product opent G1104TC met €510. Reguliere Wastafelkranen → Zilver → prijslaag-hoog:224resultaten; pagina1en2van10;24kaarten op pagina2, nul pending, geen horizontale overloop. Fysiek mobiel, echte cart-add/checkout, volledige indexdekking en productie-runtime na publicatie zijn NOT_TESTED.

## Vervolg en herstel

Eigenaar beoordeelt en publiceert uitsluitend **BadkamerCity - bescherming oude productkaarten**. Daarna MAIN-rol en publieke categorie/zoeken buiten preview controleren. Oude Brauer-/Wiesbaden-concepten niet rechtstreeks als opvolgende volledige release behandelen.

Vóór publicatie is geen winkelherstel nodig: huidige MAIN blijft actief. Na publicatie is het complete-filterkleuren-thema het vorige publicatiepunt. Gerichte code-terugzet alleen op de vier oorspronkelijke bronbestanden met controle op latere wijzigingen. Producten, prijzen, media, voorraad en VPS/index zijn niet geschreven. Productvolgorde blijft op eigenaarverzoek geparkeerd.
