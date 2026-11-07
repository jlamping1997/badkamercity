# Heldere winkelwagen — 19 oktober 2026

De eigenaar wil de winkelwagen verduidelijken en het bestelproces verder laten staan. Deze wijziging toont meerdere producten, echte kortingen, een kortingscodeveld en de prijsopbouw onder de producten. De primaire knop naar de bestaande Shopify-checkout is groen.

## Status en scope

- Werkbranch: `fix/product-cards-2026-10-14`; broncheckpoint `561cb01d67159a45b381dd72a0ceed068c4fdea1`.
- Verse gepubliceerde baseline: **195388080394 — BadkamerCity - Winkelwagen vernieuwd**, 501 bestanden. De vorige winkelwagenrelease staat inmiddels live.
- Hergebruikt concept: **195392143626 — BadkamerCity - Winkelwagen helder**. Eerst gelijkgemaakt aan de verse MAIN-baseline; uitsluitend dit ongepubliceerde thema is bestemd voor de nieuwe themacode.
- De productiepatch bevat zes gewijzigde bestanden en één nieuw JavaScript-bestand. Finale readback: concept **UNPUBLISHED**, processing=false, **502 bestanden**, zeven productie-inhouden exact, overige **495 baselinebestanden checksum-identiek** en QA-template exact hersteld. MAIN blijft MAIN met **501/501 checksums ongewijzigd**. Zie de [verificatie](cart-clear-verification-2026-10-19.json).
- Geen publicatie, MAIN-themabestandswijziging, zoekaanpassing, checkoutontwerp, betaalmethodewijziging of bestelling hoort bij deze release.

**De Nederlandse verzendregel is een afzonderlijke, al toegepaste Admin-wijziging en geldt dus ook vóór publicatie van het concept.** De twee bestaande Nederlandse tarieven zijn aangepast aan de expliciete opdracht. De EU- en internationale tarieven zijn ongewijzigd. Dit verandert de verzendprijs, niet de checkoutvormgeving of betaalflow.

GitHub–Shopify-integratie blijft **NOT_VERIFIED**. Daarom bevat de Git-overdracht de patch, tests en documentatie; er worden geen theme-bronpaden naar Git gepusht. Er is geen controle op de lokale Windows-computer uitgevoerd.

## Bestanden en gedrag

| Bestand | Wijziging |
| --- | --- |
| `assets/bc-cart-page.css` | Frisse, compacte artikelkaarten; overzicht onder alle producten op desktop en mobiel; groene afrekenknop; afgebakende cart-stijlen. |
| `assets/bc-cart-page.js` | Nieuwe, alleen op deze winkelwagen actieve kortingscodecontroller en gedeelde afhandeling van winkelwagenupdates. Geen externe browserbibliotheek. |
| `assets/cart.js` | Bewaakte koppeling tussen bestaande Dawn-aantalbediening en de nieuwe controller; oorspronkelijke aantallen-, bundel-, regelfout- en drawerlogica behouden. |
| `sections/main-cart-items.liquid` | Duidelijke productrijen met echte prijzen, aantallen, varianten, eigenschappen en aanwezige kortingen. |
| `sections/main-cart-footer.liquid` | Apart codeformulier, prijsuitsplitsing, Nederlandse verzendschatting en native afrekenknop. |
| `locales/nl.json`, `locales/en.default.json` | Labels en feedback uitsluitend in de bestaande `bc_cart_page`-localegroep. |

`templates/cart.json`, checkoutformulieren, algemene themalayout en de overige afhankelijkheden blijven ongewijzigd. De cart toont de primaire native afrekenknop; versnelde walletknoppen worden op deze cart niet daarnaast getoond. De beschikbare betaalmethoden in de bestaande Shopify-checkout blijven intact.

Het totaal gebruikt Shopify-bedragen: `original_total_price`, de werkelijke `total_discount`, het reeds verlaagde `total_price` en de relevante verzendschatting. Kortingen worden niet nogmaals van `total_price` afgetrokken. Alleen daadwerkelijk aanwezige product-/regelkortingen worden doorgestreept of als korting aangeduid; er worden geen besparingen verzonnen.

## Verzending

| Situatie | Getoonde verzending |
| --- | --- |
| Nederlandse fysieke bestelling, EUR, producttotaal na korting t/m €100,00 | €6,95 |
| Nederlandse fysieke bestelling, EUR, producttotaal na korting vanaf €100,01 | Gratis |
| Producten die geen verzending vereisen | Geen verzendkosten |
| Andere bestemming of valuta | Berekening bij afrekenen; geen Nederlandse gratis-verzendbelofte |
| Toegepaste code zonder identificeerbare geldkorting | Verzendprijs bij afrekenen en producttotaal, totdat Shopify de code en bestemming heeft gecontroleerd |

De bestemming op de winkelwagen komt uit de huidige storefront-lokalisatie en is nog geen ingevuld bezorgadres. Daarom blijft het bedrag een **schatting** met een duidelijke bestemmingsvermelding. Shopify berekent de uiteindelijke verzending bij het echte adres. Een code zonder identificeerbare geldkorting kan bijvoorbeeld een verzendkorting zijn; de interface doet daarover geen ongeverifieerde toezegging.

**VERIFIED_ADMIN:** het algemene bezorgprofiel `132488659210`, locatiegroep `134461358346`, Nederlandse zone `611727081738` houdt de bestaande methoden `1142057009418` (gratis) en `1142057042186` (€6,95). Hun prijscategorieën zijn nu respectievelijk vanaf €100,01 en €0,00 t/m €100,00. Voorheen was dit gratis vanaf €55,00 en betaald t/m €54,99. Andere zones, tarieven en prijzen zijn niet in deze wijziging aangepast.

**Werkelijke verzendoffertes na Admin-aanpassing:** producttotalen €58,00 → €6,95, €87,00 → €6,95 en €116,00 → €0,00 zijn via het echte storefront-verzendendpoint gecontroleerd. Dit zijn geen geplaatste bestellingen of afgeronde checkouttests. De exacte centgrenzen worden daarnaast met de echte Liquid-bron in de lokale suite gecontroleerd.

## Kortingscodes en herstel

Het veld is zichtbaar zodra de controller gereed is; zonder JavaScript verwijst de tekst naar het kortingscodeveld van de bestaande checkout. Het codeformulier staat buiten `cart-items` en buiten het native cartformulier, zodat code-invoer geen aantalupdate activeert.

De controller leest eerst de actuele cart via de localegebonden Ajax-API. Toevoegen bewaart andere nog toepasselijke codes; verwijderen verstuurt de resterende codes. Shopify controleert de code op de server. Een HTTP 200 is op zichzelf geen bewijs van een geldige korting: de controller controleert `discount_codes[].applicable`. De uiteindelijke voorwaarden kunnen bij afrekenen opnieuw worden beoordeeld.

Elke geslaagde wijziging ververst alle vier Dawn-secties: productregels, carticoon, live region en prijsoverzicht. Alle sectiefragmenten worden gecontroleerd vóór de DOM-vervanging. Ontbreekt een fragment, dan wordt de weergave via GET hersteld; de mutatie wordt niet herhaald. Bij een onzekere netwerkuitkomst wordt de cart opnieuw gelezen. Als de toestand niet veilig te herstellen is, blijven de acties geblokkeerd tot een paginaherlading, zodat oude aantallen niet alsnog worden ingestuurd.

Aantal- en codewijzigingen kunnen niet gelijktijdig dezelfde cart muteren. De tijdelijke blokkering geldt ook voor nieuw ingevoegde knoppen; toetsenbordfocus keert na ontgrendeling terug. De bestaande drawerroute op andere pagina’s behoudt haar oorspronkelijke gedrag.

Primaire API-bronnen: [Shopify Ajax Cart](https://shopify.dev/docs/api/ajax/reference/cart) en [Shopify Horizon-kortingscodecontroller](https://github.com/Shopify/horizon/blob/main/assets/cart-discount.js).

## Patch en herhaalbare tests

[Productiepatch](patches/BC-cart-clear-2026-10-19.patch): **64.244 bytes**, SHA-256 **`b883c31d79da993cd418987d28eb5f358c92ebe2be679f4478ec528bde43ffdf`**.

Een onafhankelijke, tijdelijke exportkopie bewijst voorwaarts alle bytes en de volledige bestandsset: 14 geëxporteerde baselinebestanden worden exact de 15 werkbestanden. Omgekeerd worden alle 14 oorspronkelijke bestanden hersteld en de nieuwe JS verwijderd. Acht overige geëxporteerde afhankelijkheden blijven exact gelijk. Bestaande CRLF-regeleinden zijn behouden; `git diff --check` met `cr-at-eol` is geslaagd.

Pas de patch alleen toe op een vers geëxporteerde en gecontroleerde baseline. De themabron in deze Git-branch is niet automatisch gelijk aan de huidige Shopify-baseline. Gebruik eerst `git apply --check` op de exportkopie; pas niet blind op de repository of op een inmiddels gewijzigd thema toe.

De losstaande testpackage staat in `scripts/cart-clear-tests/` en pint JSDOM **26.1.0** en LiquidJS **10.30.0**. Vanuit die map:

```sh
npm ci --ignore-scripts
BC_CART_THEME_PATH=/absolute/pad/naar/gepatchte-theme-export npm test
```

Zonder omgevingsvariabele is de repositoryroot de bronmap; die bevat door de bovengenoemde integratiegrens mogelijk niet de nieuwe themacode. Beide tests accepteren ook een themamap als eerste CLI-argument wanneer ze afzonderlijk worden gestart. De controllertest accepteert daarnaast `BC_CART_ASSETS` voor de assetmap.

- **16 controller-scenariogroepen:** echte authored JS met gecontroleerde API-responses; geldige/ongeldige/meerdere codes, metadata voor mogelijke verzendkorting, verwijderen, vier secties, atomair fragmentherstel, onzekere netwerkuitkomst, geen dubbele mutatie, gelijktijdige aantal-/codeacties, initiële leesvolgorde, lege cart, externe updates, veilig tonen van codetekst en focusherstel.
- **13 verzendbeleid- plus 13 volledige footer-rendergevallen:** onder/op/boven de grens, meerdere producten, kortingen over de grens, gratis product, lege/niet-fysieke cart, andere landen en valuta. Ook native cart-/checkoutformuliercontract, progressieve verrijking en sectievolgorde.

Dit zijn gedragstests met JSDOM en LiquidJS. Zij bewijzen geen fysieke iPhone-/Androidbediening, volledige mobiele header/footer, Shopify-kortingsconfiguratie of betaalafronding. De browsercontrole en definitieve Theme Check/readback worden apart vastgelegd. **NOT_TESTED:** fysieke telefoons, bundel-/abonnementsaankopen, echte geldige winkelkortingscode end-to-end, checkout/betaling en Windows lokaal, tenzij de finale verificatie expliciet aanvullend bewijs bevat.

## Finale browsercontrole

Werkelijke Shopify-preview op desktop **1363×936**: drie verschillende producten met aantallen 1, 1 en 3 geven **€3.137,01**, gratis verzending en een groene afrekenknop. Douchewisser 3→4→3 geeft **€3.137,01→€3.166,01→€3.137,01**; knop tijdelijk geblokkeerd tijdens bijwerken. Een werkelijk ingestuurde ongeldige code krijgt duidelijke feedback zonder geldkorting. Verwijderen geeft drie→twee→één→geen productregels; bij de laatste fysieke productregel van €87,00 verschijnt **€6,95 verzending en €93,95 totaal**. De testcart is weer leeg. Er is geen checkout bezocht of bestelling geplaatst in deze beurt.

Mobiele visuele controle gebruikt een **statische kopie van de werkelijke productiecomponent**, met dezelfde CSS en productgegevens, in iframes van **320/390/430px**. Door de browserscrollbar is de inhoudsbreedte 305/375/415px. Op alle drie passen drie producten en het overzicht zonder horizontale overflow; alle negen afbeeldingen zijn geladen; aantalvelden zijn 16px en het overzicht staat onder de producten. Alleen in deze fixture is het codeveld statisch zichtbaar gemaakt ondanks `:not(:defined)` en de noscripttekst verborgen. Scripts/formulieren zijn geblokkeerd. Dit bewijst de layout, geen mobiele code-interactie of volledige telefoonsite. [Productweergave](cart-clear-mobile-2026-10-19.jpg), [kostenoverzicht](cart-clear-mobile-summary-2026-10-19.jpg) en [desktop met codefeedback](cart-clear-desktop-2026-10-19.jpg).

Theme Check **bc-cart-clear-20261019 R2** slaagt voor alle zeven productiebronnen; alle geteste bytes komen overeen met de definitieve upload. De tijdelijke fixture slaagt voor **bc-cart-clear-qa R3** en is daarna verwijderd door het originele QA-template byte-exact terug te zetten. De validator gebruikte aanwezige schemas na remote ophaalfouten. Validatie voor de Admin-operaties: **bc-cart-clear-admin R2, VALID, 2026-07**.

## Terugzetten

Vóór publicatie kan de merchant het nieuwe concept ongebruikt laten; de bestaande MAIN-themacode is niet vervangen. De Admin-verzendregel wordt daardoor **niet** teruggedraaid.

Na publicatie: exporteer en controleer eerst het dan actuele thema. Als geen conflicterende vervolgwijzigingen bestaan, herstelt `git apply --reverse` op een werkkopie de zes oorspronkelijke bestanden en verwijdert het nieuwe JS-bestand. Lees de teruggeschreven Shopify-inhouden opnieuw uit. Publiceer of verwissel geen thema zonder aparte opdracht van de eigenaar.

Voor een expliciete rollback van de verzendopdracht: lees het profiel, de methoden en hun **actuele DeliveryCondition-ID’s** opnieuw uit. Shopify genereert nieuwe conditie-ID’s bij het wijzigen van voorwaarden; oude IDs uit een eerdere mutatie mogen daarom niet worden hergebruikt. Zet alleen de bestaande Nederlandse gratis methode terug op ≥€55,00 en de betaalde methode op €0,00–€54,99, behoud methoden/ratebedragen/overige zones, en verifieer de volledige relevante readback. Dit is een aparte Admin-mutatie, geen gevolg van de reverse theme-patch.

**Volgende handeling na geslaagde finale controles:** eigenaar beoordeelt **BadkamerCity - Winkelwagen helder** op telefoon en beslist over publicatie.
