# Externe productkaart: indexgegevens, Shopify-verrijking en kleurintentie

**28 oktober 2026 · DOC-03C.** Bron: actuele `bc-external-filters.js` + inhoudelijk gelezen `sections/bc-card-data.liquid`. De cases gebruiken synthetische Section Rendering-antwoorden; Liquid en echte product-/cartdata zijn niet in de harness uitgevoerd. [Kaartenhoofddossier](../PRODUCT_CARDS_AND_FILTERS.md).

## Eerste render en verrijking zijn twee fasen

De indexresponse maakt titel, vendor, URL, beeld en prijs. De koopknop begint disabled. Bij geconfigureerde card-data-section haalt de frontend via Shopify `sections=bc-card-data` aanvullende gegevens op met same-origin credentials. Een preview_theme_id wordt aan deze section-read doorgegeven wanneer die in de huidige URL aanwezig is.

`hydrateCardTitles` werkt met maximaal **vier workers**. Na iedere read controleert hij het actuele zoekrequest-ID, verbondenheid van de kaart en het Shopify-product-ID in de sectiondata tegenover de indexidentiteit. Pas daarna wordt de kaart bijgewerkt. FX-26/27/29 bevestigen passende identiteit, weigering van een afwijkend ID en het negeren van een oude verrijking nadat een nieuw grid is gemaakt.

## Cache en foutgrenzen

De section-read heeft **vijf seconden timeout**. Carddata wordt per href als promise bewaard, zodat gelijktijdige consumenten dezelfde read delen. Vanaf 200 entries wordt de eerst ingevoegde key verwijderd; dit is geen aangetoonde LRU- of tijdgebonden verversing. Een niet-succesvolle read geeft null en wordt uit de cache verwijderd. FX-28 bevestigt een nieuwe poging bij een latere lijstrefresh na zo'n mislukking.

Een ontbrekende/niet-string section, ongeldige JSON, timeout of afwijkend product-ID mag de add-knop niet activeren. De indexkaart kan wel blijven staan met zijn aanvankelijke tekst/prijs. FX-35 bevestigt dat een card-timeout geen totale lijstfallback veroorzaakt. Daardoor bestaan op dezelfde pagina afzonderlijke states: lijst geslaagd, kaartverrijking nog pending of mislukt. Een geslaagde filterresponse betekent niet dat iedere kaart koopklaar is.

## Wat de Shopify-section bepaalt

De Liquid-code leest de geselecteerde/eerste beschikbare variant en levert ID/handle, volledige/korte titel, vendor, kleur, prijs, variant-ID, beschikbaarheid, can_add, afbeeldingen, leverinformatie en switcher-HTML. Kleur kan uit expliciet passend filtermanifest komen als format en SKU aansluiten. Een gelijkende titel is geen relatiebewijs.

`can_add` vereist één variant, quantity-rule min/increment=1 en geen verplicht selling plan. `available` is apart. `updateCard` gebruikt beschikbaarheid om de knop te activeren; de klikhandler gebruikt vervolgens can_add om te kiezen tussen toevoegen en navigeren naar de PDP. Een actieve cart-icoonknop hoeft dus niet rechtstreeks te kopen als een product een configuratiepagina nodig heeft.

Leverinformatie volgt leverancier-boolean en eventueel een nog niet verstreken verwachte datum, met neutrale terugval. Dit zijn expliciete dataconsumenten; er wordt geen levertijd uit alleen een vendor/titel berekend. De huidige weergave noemt leveranciersinformatie, geen bewezen eigen magazijnvoorraad. Deze documentatieronde heeft de feitelijke waarden niet per product geverifieerd.

`productTitle` kiest short_title/title, kan een herhaalde vendorprefix en een bekende kleursuffix verwijderen, en toont tekst via DOM-textContent. Onderliggende productidentiteit en de volledige title blijven apart. Een korte kaarttitel moet daarom nooit als nieuwe SKU-/matchingbron worden gebruikt.

## Kleurkeuze is een tweede async-keten

De section kan switcher-HTML bevatten. De frontend vindt de bedoelde groep en een kleurmenu, beperkt opties tot dezelfde overige configuratiewaarden en dedupliceert canonieke kleurnamen. Alleen bij meerdere bruikbare opties verschijnen knoppen. Inline groupdata wordt direct geparsed; externe keuzeassets hebben eigen promise-cache en oorsprongsgrens. Dat is niet hetzelfde als de carddatacache.

Bij een kleurklik stijgt `model.version`, krijgt de kaart aria-busy en wordt toevoegen geblokkeerd. De aangevraagde section moet bij de bedoelde handle horen. Alleen de nieuwste versie op een nog verbonden kaart mag `updateCard` uitvoeren. FX-34 laat Black laat arriveren ná Gold: de zichtbare handle, kleurnaam en productlink blijven Gold. De hele kaart-/requestrespons is fictief; geen echte artikelwissel of koopactie uitgevoerd.

`updateCard` wisselt links, titel, beeld, hoverbeeld, prijs, levertekst, kleur en wishlistmetadata samen en vraagt BCWishlist.refresh wanneer beschikbaar. De harness bevestigt de kernvelden handle/kleur/link; de echte wishlistcontroller, hoverinteractie en voorraad-/prijsjuistheid zijn niet volledig meegedaan. Bij een kleurlaadfout blijft de laatst bevestigde modeldata de terugval.

## Zichtbare stalen en vervolgroute

De beschikbare breedte begrenst de stalen; de geselecteerde optie wordt waar nodig in de zichtbare set gehouden. Meer kleuren leidt naar de productroute met `bc_colors=<groep>` en de kleuranchor. Hoverbeelden worden alleen bij hover/fine-pointer opgebouwd en krijgen een afzonderlijke laad-/foutstatus. De tests simuleren geen echte beelddecoding, swipes of CSS-breakpoints.

Onderhoud: houd index-ID, section-ID, handle, variant, prijs, foto en wishlist bij dezelfde intentie. Een CSS-harmonisatie mag de request-/versieguards niet vervangen. De [history/fallbackrace](FILTER_STATE_AND_FALLBACK.md) raakt het grid-eigenaarschap vóór deze kaartketen en vereist een afzonderlijke correctie. Geen card-cache leegmaken of volledige gegevensherimport starten om dat DOM-probleem te omzeilen.
