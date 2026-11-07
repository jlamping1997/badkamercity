# Checkout, verzending, betaling en operationele grenzen

Bronmoment **28 oktober 2026**. De winkelwagen in dit thema en de door Shopify gehoste checkout zijn afzonderlijke systemen. Goede cartfeedback bewijst geen bestel-/betaal-/fulfilmentwerking. Er is deze ronde geen checkout gestart, bestelling geplaatst, betaling gedaan of klantenmail verstuurd.

## Vastgestelde configuratiesignalen

| Bron | Verse waarneming | Wat dit niet bewijst |
| --- | --- | --- |
| Shop | EUR, `taxesIncluded=true`, `shipsToCountries=[NL]` | Correcte btw voor ieder scenario/product |
| Markt | Eén actieve regionale markt Nederland | Alle prijs-/levervoorwaarden of internationale verkoop |
| Taal | `nl` primair/gepubliceerd | Complete vertaling van iedere foutmelding |
| Accounts | `OPTIONAL` | Actief classic/nieuw accountmodel of succesvolle login |
| Delivery profiles | Eén default profiel, vier actieve methodedefinities, 41 zonelanden, nul locaties zonder tarieven, `coversAllItems=false` | Dat 41 landen werkelijk aan bezoekers worden aangeboden of ieder artikel verzonden kan worden |
| Betaalapp | Mollie - in3 geïnstalleerd | Zichtbaarheid, goedkeuring of succesvolle betaling |
| Checkoutconfiguratie | Read geweigerd: `Access denied for checkoutAndAccountsConfigurations` | Geen actuele branding-/extension-/publicatiestatus vrijgegeven |

De aanvullende volledige rate-read bevestigt de opgeslagen NL-regels: **€6,95 bij TOTAL_PRICE van €0 t/m €100; €0 vanaf €100,01**. Andere aanwezige zones bevatten €12,95 en €19,95 vanaf €0. Dit zijn configuratieregels, geen nieuwe verzendbelofte voor andere landen. Alle drie zone- en vier methodepagina's zijn zonder volgende pagina uitgelezen. `supportedDigitalWallets` is leeg; dit bewijst niet dat alle betaalmethoden uitstaan. De afzonderlijke footerrespons bevat geen betaaliconen.

Een zonelandentelling is niet hetzelfde als `shipsToCountries`; een profielconfiguratie is geen live verzendofferte. De effectieve checkout hangt ook van afleveradres, artikelen, voorraad, kortingen en methoderegels af.

## Winkelwagencontract

`main-cart-items`, `main-cart-footer`, `cart.js`, `bc-cart-page.js` en `bc-cart-tools.js` beheren regels, aantallen, kortingscode en bewaren/herstellen. De cartcontroller ververst secties en leest actuele cartstaat; koppelingen via pub/sub moeten behouden blijven. Zie [cart/feedback](CART_AND_FEEDBACK.md) voor de verschillende toevoegpaden en [microdossiers](micro/README.md) voor bewezen grenzen.

Verzendbedragen in de cart zijn een presentatie/schatting voor de bedoelde bestemming; de echte checkoutofferte is apart. Historische bedragen/drempels uit eerdere releases mogen niet zonder actuele rate-read als huidige commerciële waarheid worden gekopieerd. Kortingscode met onbekend verzendeffect mag geen verzendbelofte opleveren. Geen automatische POST-herhaling na een onzekere transportuitkomst.

## Gehoste checkout en vervolg

Checkout bevat de adres-/contactinvoer, leveropties, betaling, orderbevestiging en eventueel account-/appuitbreidingen. De eigen theme-CSS is geen algemene methode om die gehoste schermen aan te passen. Beheerlocaties: Shopify checkout/accounts, shipping/delivery, payments, taxes/markets, notifications en de betrokken apps. Toegang en broncode van uitbreidingen afzonderlijk vastleggen.

Operationele keten: betaald/afgewezen/afgebroken → bevestiging → voorraad-/leverancierhandeling → fulfilment/track&trace → klantenservice → retour/terugbetaling. Geen van die stappen wordt door een popup-animatie gecertificeerd. Mailontvangers, leveranciersafspraken, uitzonderingen en rollen horen in een private operationele aanvulling als zij vertrouwelijke informatie bevatten.

## Acceptatie en overdracht

Voor afronding: de inmiddels gelezen verzendregels aan daadwerkelijke productdekking/offertes koppelen, werkelijke betaalmethoden/configuratie lezen, gepubliceerde checkout/accountconfiguratie kunnen controleren en een vooraf afgesproken testscenario voor korting/adres/levering/betaling/confirmation/fulfilment afhandelen. Testgegevens en screenshots blijven afgeschermd. Er wordt geen echte order aangemaakt enkel om de documentatie “100%” te noemen.

De toegangsweigering is een concrete beperking van de huidige verbinding. De overige ongelezen bedrijfsprocessen blijven OPEN. [Dekkingsregister](../COVERAGE.md) scheidt technische documentatie, praktijkcontrole en operationele gereedheid.
