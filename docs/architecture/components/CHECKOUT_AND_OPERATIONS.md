# Checkout, verzending, betaling en operationele grenzen

**Actuele aanvulling: 8 november 2026.** MAIN is `196328685834 — BadkamerCity - Homepage SEO 8 nov`. [De centrale audit](../../audits/2026-11-08/README.md) bevat de huidige bronstand en bewijsgrenzen. De thematische winkelwagen en de door Shopify gehoste checkout zijn afzonderlijke systemen. Goede cartfeedback bewijst geen betaling, ordercommunicatie of fulfilment.

## Wat op 8 november is vastgesteld

| Onderdeel | Bewijs | Resterende grens |
| --- | --- | --- |
| Gastcheckout | Beperkte desktopbrowserproef eerder op 8 november: Wiesbaden Ribbd van €245, twee stuks voor €490, van product via cart tot gastcheckout | Geen adres ingevoerd, betaling, bestelling of ordermail; de latere routecrawler heeft deze flow niet opnieuw uitgevoerd |
| Productdekking verzending | Admin meldt `coversAllItems=false` en één locatie zonder tarieven | Dit wijst op te onderzoeken dekking; het bewijst geen verzendfout voor ieder product of de bezochte proefcart |
| Betaalmethoden | Payments-leesscope ontbreekt; de footer-HTML toont geen betaaliconen | Geen actuele lijst of geslaagde betaling bewezen; dit betekent niet dat betalingen uitstaan |
| Native policies | Contact, privacy, terugbetaling, voorwaarden en wettelijke kennisgeving aanwezig | Verzendbeleid ontbreekt; voorwaarden en kennisgeving tonen letterlijke HTML en vragen een opmaakcorrectie |
| Retourafspraak | Gepubliceerd beleid: aanmelden binnen 30 dagen, daarna 14 dagen terugsturen; gewone spijtretour voor klant, fout/defect apart opgelost; afgeven op afspraak | €75 incl. btw is de raming per standaardpallet voor retourvervoer, geen heenzendtarief of universeel buitenlandtarief |
| Operationele keten | Contact- en retourformulieren bereikbaar | Ontvangst, klantbevestiging, opvolging, terugbetaling en fulfilment niet end-to-end getest |

De beperkte proefcart is na de eerdere browsercontrole opgeruimd. Er is in deze audit geen testorder geplaatst, betaling gedaan of klantenmail verstuurd. Adresafhankelijke leveropties en kortingen zijn nog afzonderlijk te controleren. De lege GET-cart in de footercontrole is alleen HTML-bewijs.

## Historisch configuratiebewijs — 28 oktober 2026

Onderstaande waarden behouden hun oorspronkelijke meetdatum. De toenmalige opdracht sloot checkoutinteractie uit; die scopebeperking beschrijft niet de latere beperkte gastcheckoutproef van 8 november.

| Bron | Waarneming op 28 oktober | Wat dit niet bewijst |
| --- | --- | --- |
| Shop | EUR, `taxesIncluded=true`, `shipsToCountries=[NL]` | Correcte btw voor ieder scenario/product |
| Markt | Eén actieve regionale markt Nederland | Alle prijs-/levervoorwaarden of internationale verkoop |
| Taal | `nl` primair/gepubliceerd | Complete vertaling van iedere foutmelding |
| Accounts | `OPTIONAL` | Actief classic/nieuw accountmodel of succesvolle login |
| Delivery profiles | Eén default profiel, vier actieve methodedefinities, 41 zonelanden, nul locaties zonder tarieven, `coversAllItems=false` | Geen actuele 8-novembertelling: toen nul, nu één locatie zonder tarieven; geen bewijs dat 41 landen of alle artikelen worden aangeboden |
| Betaalapp | Mollie - in3 geïnstalleerd | Zichtbaarheid, goedkeuring of succesvolle betaling |
| Checkoutconfiguratie | Read geweigerd: `Access denied for checkoutAndAccountsConfigurations` | Geen branding-/extension-/publicatiestatus vrijgegeven door die read |

De volledige rate-read van 28 oktober bevestigde opgeslagen NL-regels: **€6,95 bij TOTAL_PRICE van €0 t/m €100; €0 vanaf €100,01**. Andere aanwezige zones bevatten €12,95 en €19,95 vanaf €0. Alle drie zone- en vier methodepagina's waren zonder volgende pagina uitgelezen. Dit blijft historisch configuratiebewijs, geen nieuwe verzendbelofte of actuele checkoutofferte. `supportedDigitalWallets` was leeg; dat bewijst niet dat alle betaalmethoden uitstaan.

Een zonelandentelling is niet hetzelfde als `shipsToCountries`; een profielconfiguratie is geen live verzendofferte. De effectieve checkout hangt ook van afleveradres, artikelen, voorraad, kortingen en methoderegels af.

## Winkelwagencontract en beheer

De op 28 oktober onderzochte bronketen gebruikt `main-cart-items`, `main-cart-footer`, `cart.js`, `bc-cart-page.js` en `bc-cart-tools.js` voor regels, aantallen, kortingscode en bewaren/herstellen. De cartcontroller ververst secties en leest actuele cartstaat; pub/sub-koppelingen horen bij dat contract. [Cart en feedback](CART_AND_FEEDBACK.md) en de [microdossiers](micro/README.md) beschrijven de afzonderlijke toevoegpaden en gedateerde bronreplays. Een oude replay wordt geen actuele runtimevrijgave door deze aanvulling.

Verzendbedragen in de cart zijn presentatie of schatting voor de bedoelde bestemming; de echte checkoutofferte is apart. Kopieer historische bedragen/drempels alleen na een actuele rate-read. Een kortingscode met onbekend verzendeffect mag geen verzendbelofte opleveren. Herhaal een kooprequest niet automatisch na een onzekere transportuitkomst.

Checkout bevat adres-/contactinvoer, leveropties, betaling, orderbevestiging en eventuele account-/appuitbreidingen. Beheer gebeurt in Shopify checkout/accounts, shipping/delivery, payments, taxes/markets, notifications en de betrokken apps. Theme-CSS of één gedeelde storefrontfooter verandert die gehoste schermen niet automatisch. Toegang en bronversie van uitbreidingen moeten afzonderlijk worden vastgelegd.

## Open acceptatie en overdracht

Voor afronding moeten de verzendregels aan daadwerkelijke productdekking en adresoffertes worden gekoppeld, de ene locatie zonder tarieven worden verklaard en de werkelijke betaalmethoden worden vastgesteld. Daarna volgt een afgesproken scenario voor korting, levering, betaling, bevestiging, fulfilment, retour en terugbetaling. Ordermail, contact-/retourmail, echte mobiele bediening en GA4-aankoopmeting blijven open. Geen algemene testbetaalmodus in de openbare winkel activeren om alleen deze documentatie af te sluiten.

De operationele keten is: betaald/afgewezen/afgebroken → bevestiging → voorraad-/leverancierhandeling → fulfilment/track&trace → klantenservice → retour/terugbetaling. Vertrouwelijke ontvangers, leveranciersafspraken en rollen horen in een private operationele aanvulling. Publieke documentatie bevat geen checkoutreferenties, klant-/orderdata of betaalgegevens.

[Dekkingsregister](../COVERAGE.md) · [actuele livegangcontroles](../../livegang-seo/CONTROLES.md) · [centrale audit en vervolg](../../audits/2026-11-08/README.md).
