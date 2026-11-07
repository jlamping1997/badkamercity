# Metingen — GA4 en winkelresultaten

## Beginstand

Geen GA4-property, webstream of Google-conversierapport gelezen. In de gelezen initiële HTML zijn geen herkenbare G-, GTM- of AW-tag-ID's gevonden; dat bewijst niet dat via pixels of toestemming geen meting bestaat. Google & YouTube is niet in de zeven app-installaties aangetroffen.

## Inrichting

1. Zoek de bestaande GA4-property en juiste webstream voordat een nieuwe wordt gemaakt.
2. Gebruik bij voorkeur de ondersteunde Google & YouTube-koppeling en Shopify-privacyintegratie. Controleer eerst eventuele bestaande aangepaste pixels/GTM/andere tags; voorkom dubbele meetroutes.
3. Leg zakelijke property-/streamidentificatie en beheerrol vast zodra bevestigd. Geen klantidentiteiten, privéaccountgegevens of herstelcodes in Git.
4. Test toestaan, weigeren en intrekken. Toestemmingsplichtige tracking start pas na geldige toestemming; weigeren mag de normale winkel niet onbruikbaar maken. Consent Mode is geen vervanging voor een juiste toestemmingskeuze.
5. Valideer gebeurtenissen met passend runtimebewijs; alleen een geïnstalleerde tag is onvoldoende.

## Gebeurtenissen

| Gebeurtenis | Wat moet kloppen? |
| --- | --- |
| view_item | Werkelijk bekeken artikel/uitvoering, valuta en prijs |
| add_to_cart | Gekozen variant, aantal en eventuele toegevoegde onderdelen |
| begin_checkout | Werkelijke winkelwagen en bedrag |
| purchase | Eén bevestigde transactie, correcte transaction_id, value en currency |
| Contact/retour | Alleen nuttige niet-inhoudelijke gebeurtenis; geen formuliertekst/e-mail meesturen |

Een geslaagde consenttest, tagtest en betaling zijn drie verschillende bewijzen. Een herladen bedankpagina mag geen dubbele omzet geven. Leg ook vast of testverkeer/testorders uit gewone rapportage worden gehouden.

## Eerste meetoverzicht

| Bron | Volgen | Betekenis |
| --- | --- | --- |
| Search Console | Indexatie, zoektermen, vertoningen, klikken, CTR | Organische zoekvindbaarheid |
| Merchant Center | Geschikte/afgekeurde items, gratis vertoningen/klikken | Productfeed en productbereik |
| GA4 | Sessies, winkelwagen, checkout, omzet | Gedrag binnen de meetgrenzen |
| Shopify | Bestellingen en werkelijke omzet | Operationele verkoopcontrole |

Controleer dit in het begin handmatig regelmatig en vergelijk na wijzigingen opnieuw. Dit dossier maakt geen automatische rapportage of geplande taak aan.

[Shopify GA4 en privacy, AP-toestemmingsinformatie](../BRONNEN.md) · [Taken](../TAKEN.md)
