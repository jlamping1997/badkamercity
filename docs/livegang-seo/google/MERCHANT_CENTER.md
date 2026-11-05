# Merchant Center — productvermeldingen

> **LAUNCH-02:** zie de [eenvoudige Google-productcontrole](../GOOGLE_PRODUCTCONTROLE.md). Verlavio is nu het publieke merk; Fabriecio is de interne leverancier. Eerdere momentopnamen over koopbaarheid zijn door FAB-04 aangevuld. [Retourconcept en publicatieplan](../retouren/RETOURBELEID_CONCEPT.md): jaarrond30dagen, maar nog niet in Shopify of Merchant gepubliceerd.

Doel: eerst geschikte producten gratis kunnen laten verschijnen op Google. Google Ads en advertentiebudget zijn een aparte latere keuze.

## Beginstand en route

Bestaand account **5898992928** is op 4 november door de eigenaar genoemd; de toenmalige 3/6-onboardingstatus is historisch. Huidige toegang, domeinclaim, productbron, goedkeuringen en bestemmingen zijn niet in Merchant Center gelezen. Google & YouTube is op 5 november niet in de volledige Shopify-appinstallatielijst aangetroffen.

Gebruik voorlopig **Shopify → Google & YouTube → bestaand Merchant Center**. Dit houdt de productbron bij de webshop. Controleer vóór verbinden of er al een andere bron actief is.

## Stappen

1. **Websitevereisten:** openbaar, werkende betaalroute, duidelijke contact-/retour-/voorwaardeninformatie. Los de ontbrekende standaard beleidsinformatie op en maak die in de footer vindbaar.
2. **Account:** bevestig beheerderstoegang en selecteer expliciet het bestaande Merchant-ID. Maak geen tweede account als de bestaande toegang oplosbaar is.
3. **Kanaal:** installeer de officiële Google & YouTube-app vanuit Shopify; verbind de juiste Google-identiteit. Controleer de domeinverificatie/claim en eventuele bestaande feed vóór synchronisatie.
4. **Markt:** begin met de daadwerkelijk ondersteunde markt NL, taal Nederlands en EUR. Voeg andere landen pas toe met passende winkel-/verzendinstellingen.
5. **Verzending/retouren:** stem website, checkout en Merchant af. Maak een bewuste keuze tussen gesynchroniseerde en handmatig beheerde verzendinstellingen. Controleer pakket, pallet, zware artikelen en uitzonderingen; neem geen algemene levertijd of gratis-verzendclaim over zonder dekking.
6. **Productselectie:** publiceer alleen feedklare artikelen naar het Google-kanaal/bestemming. Begin met circa tien representatieve artikelen/varianten; dit is een werkwijze, geen Google-minimum.
7. **Controle:** lees de ontvangen item-ID, URL, foto, artikelidentiteit, variant, prijs, valuta en voorraad terug. Controleer de werkelijke landingspagina. Herstel fouten in de primaire bron, meestal Shopify.
8. **Gratis vermeldingen:** controleer de status in Merchant Center. Onderscheid in beoordeling, beperkt, geschikt en afgekeurd; geschiktheid garandeert geen vertoning.
9. **Opschalen:** voeg geschikte batches toe en noteer verzonden/ontvangen/geschikt/afgekeurd, oorzaak en uitzonderingen. Niet blind alle ACTIVE-producten als Google-klaar behandelen.

## Productgegevens

| Gegeven | Controle voor BadkamerCity |
| --- | --- |
| Titel, beschrijving en URL | Herkenbaar artikel/uitvoering; landingspagina hoort bij de aangeboden variant |
| Afbeelding | Correct artikel, bruikbaar en bereikbaar; geen logo/placeholder als vervanging voor een productfoto |
| Prijs en beschikbaarheid | Dezelfde koopbare eenheid en actuele staat als op website/checkout |
| Merk en identifiers | Echte GTIN/EAN waar toegewezen; anders toepasselijke merk/MPN-regels volgen |
| Varianten | Kleur/maat en groepering volgens de echte relatie; losse Hotbath-productlinks niet zomaar native varianten noemen |
| Productcategorie | Passende Google-taxonomie; Shopify-winkelcategorie is een ander veld |
| Eenheidsprijs | Bij tegels/m² en verpakking apart bepalen welke velden van toepassing zijn |

Ontbrekende identifiers nooit verzinnen. Ook niet standaard identifier_exists=false invullen om een foutmelding te omzeilen.

## Vast te behouden uitzonderingen

- **Lagoo blijft zonder foto's.** Daarom nu uit de Google-productbestemming houden zolang geen geschikte afbeelding beschikbaar is. Dit document autoriseert geen fototerugplaatsing en verandert de webshopstatus niet.
- **Verlavio (Fabriecio-bron):** FAB-03/04 bewijzen de latere rebrand en het gerichte koopbaarheidsherstel. Het eerdere GM_1002-OutOfStock-resultaat is historisch; foto's/identifiers en huidige beschikbaarheid per batch blijven apart te controleren.
- **Tegels:** de voorbeeldpagina verkoopt een doos van 1,44 m² voor €158,33 en toont daarnaast €109,95/m². Verzend-/eenheids-/feedprijs moet dezelfde echte bestelverpakking beschrijven.
- **Sunshower en samengestelde sets:** juiste gekozen uitvoering en prijs toetsen; geen andere uitvoering in de advertentie beloven dan de doorklik aanbiedt.
- **Levertijd:** de herhaalde 8–9-wekenweergave is nog geen gecontroleerde leveranciersregel.


## Retourbeleid voor Google

Gebruik de uiteindelijke openbare Shopify-policy-URL, jaarrond30dagen en de werkelijk gekozen retourmethode/kosten. Geen novemberverlenging, geen algemene speciaal-besteld-uitzondering en geen gratis retour invullen zonder die afspraak. Maak alleen productuitzonderingen voor aantoonbaar geldige gevallen. Lees de opgeslagen Merchant-waarden terug naast de openbare tekst; Google-inrichting is in LAUNCH-02 niet uitgevoerd.

## Acceptatie

De juiste winkel/accountkoppeling is teruggelezen; winkelvereisten zijn afgedekt; een kleine proef klopt in Merchant én op de site; gratis bestemming is gecontroleerd; uitzonderingen zijn doelgericht uitgesloten; er is een bruikbaar foutenoverzicht. Storefront-publicatie en Google-goedkeuring blijven afzonderlijke resultaten.

[Officiële vereisten, feedgegevens en gratis vermeldingen](../BRONNEN.md) · [Taken](../TAKEN.md)
