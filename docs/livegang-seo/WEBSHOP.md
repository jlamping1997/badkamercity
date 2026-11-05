# Webshop — voorwaarden voor een bruikbare livegang

> **LAUNCH-02, 5 november:** [bedrijfsgegevens](BEDRIJFSGEGEVENS.md) ontvangen, [dertig-dagenretourconcept](retouren/RETOURBELEID_CONCEPT.md), [concrete controles](CONTROLES.md) en [universele-footerroute](FOOTER_EN_BELEID.md) toegevoegd. Onderstaande HTTP-/productvoorbeelden komen uit de eerdere nulmeting. Rebrand en koopbaarheidsherstel zijn inmiddels apart in FAB-03/04 vastgelegd; de oude Fabriecio-blokkade niet als nieuw feit herhalen. Nog geen beleids-/footerpublicatie in LAUNCH-02.

## Wat deze controle al bewijst

Shopify bevestigt HTTPS, hoofdadres https://badkamercity.nl, verzending naar NL en taxesIncluded=true. Openbare GET-requests geven 200 voor homepage, Wastafelkranen, Tegels, Contact, Retour aanmelden en zes uiteenlopende producten. Dat is geen afgeronde checkouttest.

De eigenaar meldt dat de bestaande producten goed en bestelbaar zijn. Dat blijft een uitgangspunt voor de scope; afwijkingen uit de nulmeting vragen gerichte controle, geen catalogusbrede afkeuring.

## Eerst afronden

1. **Bedrijfsinformatie.** Het [nieuwe gegevensregister](BEDRIJFSGEGEVENS.md) bewaart het opgegeven adres/KvK/IBAN en de nog te corrigeren btw-id/ontbrekende telefoon. De eerder gelezen contactpagina bevat in de gelezen hoofdinhoud alleen een formulier. De footer noemt info@badkamercity.nl. Controleer en publiceer de juiste verkopersnaam, zakelijke adresgegevens, telefoon, e-mail, KvK, btw-id en klachtroute waar vereist. Gebruik de werkelijke BadkamerCity-verkoper; het showroomadres van Harry Suiker is geen automatische winkel-/retourlocatie.
2. **Beleid.** In Shopify Instellingen → Beleid is alleen privacy ingevuld aangetroffen. De openbare standaard-URL's voor retourbeleid, algemene voorwaarden en verzending geven 404. Vul de ontbrekende informatie aan en verbind deze met de footer en checkout. Een retourformulier is niet hetzelfde als uitleg over bedenktijd, retourkosten, retouradres en terugbetaling.
3. **Levering.** Jackson werkt hier nu aan; markeer dit als IN_PROGRESS_USER en hergebruik de latere FAB-04-controle. Maak pakket, pallet/grote artikelen, regio-uitzonderingen, levertijden en bijkomende kosten duidelijk. Controleer de footeractie Bezorgen en afhalen, die nu naar #HomeDelivery verwijst; een anker alleen bewijst geen volledige leveringsinformatie.
4. **Bestellen.** Gebruik de [korte checklist voor Jackson en uitvoering](CONTROLES.md). Test de geselecteerde uitvoering vanaf product tot checkout. Leg apart vast welke betaling/ordercommunicatie echt is gecontroleerd. Activeer geen algemene testbetaalmodus in de openbare winkel om één proef te doen.
5. **Contactafhandeling.** Zie de [uitgeschreven mailproef en aparte herroepingscontrole](CONTROLES.md). Een succesmelding op de pagina is niet hetzelfde als een ontvangen mail of directe klantbevestiging. Verifieer een contact-/retourmelding in de juiste mailbox en een werkend antwoordproces. Er is in deze ronde niets ingezonden.
6. **Privacy.** Controleer werkelijk gebruikte pixels/cookies en de keuzes accepteren, weigeren en intrekken. Een bestaande privacytekst bewijst geen juist werkende toestemming.

[ACM en Ondernemersplein](BRONNEN.md) beschrijven de informatie die vóór en na een online koop nodig is; dit dossier is geen juridische beoordeling van de volledige winkel.

## Productcontrole per batch

| Controle | Bewijs |
| --- | --- |
| Product en uitvoering | Merk + fabrikantcode, juiste kleur/maat, echte variant of echte gekoppelde productbestemming |
| Prijs | Consumentenprijs incl. btw, juiste eenheid en meerprijs; dezelfde waarde op kaart, PDP, cart en checkout |
| Beschikbaarheid | Werkelijke bestelbaarheid en voorraadbeleid; niet uit ACTIVE afleiden |
| Levering | Leveranciers-/bedrijfsregel met bronmoment, geen generieke belofte zonder bron |
| Afbeelding | Correct artikel en kleur, bruikbaar beeld en gebruiksrecht; uitzonderingen benoemen |
| Productinformatie | Belangrijke kenmerken, inbegrepen/benodigde onderdelen, toepasselijke documenten |
| Kanaal | Online Store en Google zijn afzonderlijke publicatiebestemmingen |
| Identifiers | Echte SKU, merk, GTIN/EAN en MPN waar van toepassing; ontbrekend niet verzinnen |

Begin met een gewone kraan, een kleur-/maatwisseling, een set met onderdeelkeuze en een tegeldoos. Test mobiel. Meer assortimentsgroepen alleen toevoegen als hun eigen prijs-/keuzelogica dat vraagt.

## Concrete uitzonderingen uit de nulmeting

- **Lagoo:** de fotoverwijdering is een expliciete eigenaarskeuze. Het bezochte RE9012-product heeft geen Product.image en een galerijteller met nul beelden. Niet automatisch beelden terugzetten. Google-productvermeldingen wachten voor deze producten zolang een geschikte afbeelding ontbreekt; de website en de rest van het Google-assortiment zijn afzonderlijke keuzes.
- **Historisch, vóór FAB-03/04 — Fabriecio GM_1002:** de productpagina is bereikbaar en de collectie linkt ernaar. Het Product Offer meldt OutOfStock. De twaalf gelezen product-sitemaps bevatten geen Fabriecio-handle. Dit kan samenhangen met publicatie/beschikbaarheid/verversing; oorzaak nog niet vastgesteld. Controleer de werkelijke kooproute en kanaalstatus vóór opname als bestelbaar feedartikel.
- **Levertermijn:** de HTML-steekproeven van Hotbath, JEE-O, Lagoo en Fabriecio bevatten 8–9 weken; een Porcelanosa-product noemt 10–14 werkdagen. Dit bewijst niet dat de termijnen onjuist zijn. Controleer wel hun bron voordat ze met Google worden gesynchroniseerd.
- **Tegels:** het onderzochte Porcelanosa-product toont €109,95/m² en €158,33 per doos van 1,44 m²; de schema-aanbieding is €158,33. Google-feed en landingspagina moeten dezelfde daadwerkelijk bestelbare eenheid volgen; toets de benodigde eenheidsprijs-/maatvelden. Geen €/m² als koopprijs opsturen als de klant per doos koopt.
- **Sunshower:** de server-HTML bevat vijf afbeeldingsfoutteksten en ook schema-afbeeldingen. Zichtbaarheid en echte beeldrequests zijn niet getest; dit is een onderzoekspunt, geen bewezen kapotte galerij.
- **Offerte-upload:** de eerdere klantactivatie blijft uit totdat ontvangst en bestaande pagina/koppeling zijn afgerond. Dit is geen voorwaarde voor een gewone productbestelling zolang geen kapotte offerteactie wordt aangeboden.

## Vrijgave

Verkopen en vindbaarheid uitbreiden zodra de noodzakelijke winkelinformatie klopt en de afgesproken product-/bestelroutes bewezen zijn. Een ontbrekende blog, extra merk of cosmetische verbetering schuift daarna mee in de roadmap. Leg een uitzondering per betrokken route/product vast; geen algemene claim dat de hele catalogus is gekeurd.
