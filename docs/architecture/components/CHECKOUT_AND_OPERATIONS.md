# Checkout, verzending, betaling en operationele grenzen

> **9 november 2026 — GIT-SYNC-02:** de al gepubliceerde bc-cart-delivery-vertakking voor settings.bc_temporary_in_stock staat nu exact in Git; alleen de bestaande levertekst wordt daardoor gekozen. Voorraad, fulfillment, verzendtarief, betaling, mails en checkout zijn door deze bronreconciliatie niet gewijzigd of end-to-end getest. [Bronreview](../../repairs/2026-11-09/published-source-sync/README.md).

> **Nieuwste controle — SHIPPING-COVERAGE-01:** actieve NL-Market met beide oorsprongen exact teruggelezen; acht nieuwe cartoffertes PASS en cart leeg. Het oude locatie-/coversAllItems-signaal is binnen deze scope verklaard. [Bewijs](../../repairs/2026-11-08/shipping-and-blog/README.md). Geen verzendconfiguratie, voorraad, betaling of mail gewijzigd/verstuurd.

**Actuele aanvulling: 8 november 2026 — bezorginformatie en tariefproef.** MAIN is `196368531722 — BadkamerCity - Klantenservice 8 nov`. [Het actuele bezorgdossier](../../repairs/2026-11-08/delivery-information/README.md) en [de gedateerde centrale audit](../../audits/2026-11-08/README.md) onderscheiden nieuwe proeven en eerdere bronstand. De thematische winkelwagen en de door Shopify gehoste checkout zijn afzonderlijke systemen. Goede cartfeedback bewijst geen betaling, ordercommunicatie of fulfilment.

## Wat op 8 november is vastgesteld

| Onderdeel | Bewijs | Resterende grens |
| --- | --- | --- |
| Gastcheckout | Beperkte desktopbrowserproef eerder op 8 november: Wiesbaden Ribbd van €245, twee stuks voor €490, van product via cart tot gastcheckout | Geen adres ingevoerd, betaling, bestelling of ordermail; de latere routecrawler heeft deze flow niet opnieuw uitgevoerd |
| NL-verzendtarieven | Verse Admin-regels: €6,95 t/m €100; €0 vanaf €100,01. AJAX-cartquotes €96,15 → €6,95 en €109,00 → €0; eigen geïsoleerde cart daarna leeg | Alleen het geteste NL-scenario; geen volledige product-/regio-/kortingsmatrix, checkoutbestelling of configuratiewijziging |
| Effectieve product-/locatiedekking | marketDrivenShipping=true; actieve NL-optie én tariefgroep omvatten winkel- en leverancierslocatie, geen collectiebeperking. Alle 851 actieve/gepubliceerde leveranciersvarianten gelezen; acht cartquotes PASS | Legacy coversAllItems=false/één locatie zonder rates is hier geen actueel checkoutdefect. Andere adressen/extreme hoeveelheden/kortingen/fysieke levering blijven apart |
| Betaalmethoden | Payments-leesscope ontbreekt; de footer-HTML toont geen betaaliconen | Geen actuele lijst of geslaagde betaling bewezen; dit betekent niet dat betalingen uitstaan |
| Bezorginformatie en native policies | Page 166963937546 /pages/bezorgen-en-afhalen live; Contact, privacy, terugbetaling, voorwaarden en wettelijke kennisgeving als native policy aanwezig | Native SHIPPING_POLICY blijft afwezig; voorwaarden/kennisgeving tonen escaped HTML. write_legal_policies ontbreekt; een gewone Page vervangt die native bron niet |
| Retourafspraak | Gepubliceerd beleid: aanmelden binnen 30 dagen, daarna 14 dagen terugsturen; gewone spijtretour voor klant, fout/defect apart opgelost; afgeven op afspraak | €75 incl. btw is de raming per standaardpallet voor retourvervoer, geen heenzendtarief of universeel buitenlandtarief |
| Operationele keten | Contact- en retourformulieren bereikbaar | Ontvangst, klantbevestiging, opvolging, terugbetaling en fulfilment niet end-to-end getest |

De beperkte browserproef en de latere geïsoleerde tariefcart zijn elk opgeruimd. Er is geen testorder geplaatst, betaling gedaan of klantenmail verstuurd. De nieuwe verzendquotes geven aanvullend bewijs voor hun specifieke NL-scenario; overige afleveradressen, productcombinaties en kortingen blijven te controleren. De lege GET-cart in de footercontrole blijft alleen HTML-bewijs.

## Publieke bezorginformatie en vindbaarheid

De live Page [Bezorgen en afhalen](https://badkamercity.nl/pages/bezorgen-en-afhalen) gebruikt de gecontroleerde NL-tarieven en de afspraak dat afhalen bij Zichtenburglaan 150 alleen na bevestiging en op afspraak kan. Geen vaste leverdoorlooptijd, vervoerder, bezorgniveau of uitgaand pallettarief wordt uit de configuratie afgeleid. De Contacttekst linkt naar deze Page en vraagt het bestelnummer indien bekend.

Footer-/homepageverwijzingen en retourcopy zijn door de eigenaar gepubliceerd op MAIN 196368531722. De publicatienacontrole en tekstreparaties staan in [CONTENT-ENCODING-02](../../repairs/2026-11-08/glossary-encoding/README.md). Geen nieuwe themapublicatie nodig.

## Actieve verzending — SHIPPING-COVERAGE-01

De oude DeliveryProfile-laag alleen is onvoldoende bij marketDrivenShipping=true. De actieve Nederlandse Market-optie en haar tariefgroep bevatten beide locaties. FAB-04 had deze leveranciersoorsprong eerder al toegevoegd; de configuratie is opnieuw exact bevestigd en niet geschreven. Alle 851 huidige actieve/gepubliceerde Verlavio-varianten zijn via de leverancierslocatie gelezen: CONTINUE, requiresShipping, default profiel. De profielvlag coversAllItems is niet op true gezet.

Acht daadwerkelijke Ajax-carts geven het huidige tarief: gemengd €81,18→€6,95 en €148,33→€0; ook één/twee tegeldozen en een nulvoorraad-CONTINUE-item hebben de verwachte optie. Alleen eigen geïsoleerde artikelen gebruikt en verwijderd, cart leeg; geen checkout/order/mail. [Market-bron, proeven en grenzen](../../repairs/2026-11-08/shipping-and-blog/README.md). Niet elke SKU/postcode/korting of fysieke levering is getest.

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

De legacy-locatiewaarschuwing is verklaard door de actieve Markets-configuratie en acht gerichte NL-offertes. Voor verdere afronding blijven andere adressen, bijzondere leveringen/kortingen, daadwerkelijke betaalmethoden en de echte orderketen te toetsen. Daarna volgt een afgesproken scenario voor korting, levering, betaling, bevestiging, fulfilment, retour en terugbetaling. Ordermail, contact-/retourmail, echte mobiele bediening en GA4-aankoopmeting blijven open. Geen algemene testbetaalmodus in de openbare winkel activeren om alleen deze documentatie af te sluiten.

De operationele keten is: betaald/afgewezen/afgebroken → bevestiging → voorraad-/leverancierhandeling → fulfilment/track&trace → klantenservice → retour/terugbetaling. Vertrouwelijke ontvangers, leveranciersafspraken en rollen horen in een private operationele aanvulling. Publieke documentatie bevat geen checkoutreferenties, klant-/orderdata of betaalgegevens.

[Dekkingsregister](../COVERAGE.md) · [actuele livegangcontroles](../../livegang-seo/CONTROLES.md) · [centrale audit en vervolg](../../audits/2026-11-08/README.md).
