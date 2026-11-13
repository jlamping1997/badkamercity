# Merchant Center — productvermeldingen

**Stand: 8 november 2026 — DOC-LIVE-01.** De [live audit](../../audits/2026-11-08/README.md) leest website en Shopify-configuratie. Huidige Merchant-toegang, domeinclaim, productbron, afkeuringen en bestemmingen zijn niet in het Merchant-account teruggelezen. De historische onboardingstatus 3/6 en het eerdere ontbreken van Google & YouTube zijn geen actuele accountstatus.

Doel: geschikte producten laten verschijnen op Google met dezelfde koopbare prijs, beschikbaarheid en voorwaarden als de website. De eigenaar is ook met Ads-onboarding begonnen; campagneactivatie en budget blijven een apart besluit.

## Huidige route en websitevereisten

Google & YouTube-configuratie is aanwezig. Gebruik de bestaande Shopify-integratie als primaire productbron en controleer het bedoelde Merchant-account (historisch opgegeven ID 5898992928), rollen, claim en eventuele eerdere bronnen. Geen tweede account of parallelle API-feed maken omdat de wizard nog niet klaar is.

Retour, contact, privacy, voorwaarden en kennisgeving zijn live. Voorwaarden/kennisgeving tonen letterlijke HTML-tags; native verzendbeleid ontbreekt. Contactpagina bevat alleen een formulier, contactbeleid/footer missen telefoon; btw-id heeft een formatfout. Deze taken staan in [TAKEN](../TAKEN.md). Een homepage-/cartproef tot gastcheckout bewijst geen werkende betaling of goedgekeurde feed.

## Volgorde

1. **Winkelinformatie:** corrigeer identiteit/contact en policy-opmaak; publiceer echte verzendinformatie en houd die vindbaar. Geen onjuiste vestiging of btw-id invullen om een scherm af te vinken.
2. **Account en bron:** lees de huidige gekoppelde accountselectie, domeinclaim en ontvangen productbron terug vóór vervangen/synchroniseren.
3. **Markt:** begin met werkelijk ondersteund NL, Nederlands en EUR; andere landen pas met passende lever-/retourafspraken.
4. **Verzending:** kies bewust gesynchroniseerde of handmatig beheerde instellingen. Controleer pakket/pallet/zware goederen, kosten, regio's en echte doorlooptijden naast checkout. €75 is een retourpalletraming, geen heenzendtarief.
5. **Retouren:** neem de live websiteafspraken hieronder over en lees de opgeslagen Merchant-waarden terug. Websitepublicatie alleen sluit deze stap niet.
6. **Kleine feedproef:** circa tien uiteenlopende items/varianten, inclusief gewone kraan, gekozen uitvoering, tegeldoos en set; geen Google-minimum maar controleerbare batch.
7. **Readback:** ontvangen item-ID, URL, foto, artikelidentiteit, variant, koopprijs, valuta, voorraad en bestemming naast echte landingspagina controleren.
8. **Uitbreiden:** aantallen verzonden/ontvangen/geschikt/beperkt/afgekeurd en oorzaken registreren. Geschiktheid garandeert geen vertoning; ACTIVE is geen feedvrijgave.

## Productgegevens

| Gegeven | Acceptatie |
| --- | --- |
| Titel / beschrijving / URL | Herkenbaar artikel en uitvoering; landingspagina hoort bij de aanbieding |
| Afbeelding | Juiste bereikbare productfoto; geen logo of placeholder als vervanging |
| Prijs / beschikbaarheid | Koopbare eenheid en actuele staat gelijk op site, cart, checkout en feed |
| Identifiers | Echte GTIN/EAN waar toegewezen; anders toepasselijke merk/MPN-regels; nooit verzinnen of generiek `identifier_exists=false` gebruiken |
| Varianten | Alleen echte relatie/groepering; losse Hotbath-productlinks zijn niet vanzelf native varianten |
| Categorie | Passende Google-taxonomie; winkelcategorie is een ander veld |
| Eenheidsprijs | Doosprijs en inhoud/base bij tegels correct scheiden |
| Productinformatie | Toepasselijke fabrikant-/veiligheidsinformatie en documenten op landingspagina toetsen |

## Tegels: bestelverpakking is de aanbieding

De actuele RR6001-steekproef toont €68,95/m², **1 doos van 1,44 m² = €99,29**, schema Offer €99,29. Voor zo'n doosaanbieding is het te controleren Google-voorbeeld: `price=99.29 EUR`, `unit_pricing_measure=1.44 sqm`, `unit_pricing_base_measure=1 sqm`. De daadwerkelijk gesynchroniseerde feedvelden moeten worden teruggelezen; dit voorbeeld bewijst geen al correcte appmapping.

Andere gedateerde HTML-voorbeelden: RR1001 €79,95/m² en 2 m²/doos = €159,90; VP8002 €79,95/m² en 1,28 m²/doos = €102,34. Geen €/m² als koopprijs sturen als de klant per hele doos koopt. Oudere prijsvoorbeelden van 5 november niet als huidige prijzen gebruiken.

## Te behouden uitzonderingen

- **Lagoo blijft zonder foto's.** Houd beeldloze items doelgericht buiten de Google-productbestemming zolang geschikte media ontbreken. Geen fototerugplaatsing en geen automatische wijziging van de webshopbestelling.
- **Verlavio:** FAB-03/04 bewijzen rebrand en gericht koopbaarheidsherstel; oude Fabriecio-OutOfStock-meting historisch. Beelden, identifiers en huidige feedstatus nog per batch toetsen.
- **Sunshower / samengestelde sets:** de doorklik moet de geadverteerde uitvoering en prijs bieden; onderdelen/meerprijzen correct.
- **Levertijden:** alleen onderbouwde actuele regels synchroniseren. Een herhaalde 8–9-wekenweergave is op zichzelf geen gecontroleerde leveranciersregel.

## Live retourafspraken voor afstemming met Google

De gezaghebbende URL is [de Shopify-retourpolicy](https://badkamercity.nl/policies/refund-policy): jaarrond binnen **30 kalenderdagen aanmelden**, daarna **14 dagen terugsturen**. Klant regelt/betaalt gewone spijtretour; afgeven is gratis op afspraak. **€75 incl. btw per standaard NL-pallet is een raming**, geen universele vaste prijs voor ieder product/land. Verkeerd of ondeugdelijk geleverd krijgt een afzonderlijke kosteloze passende oplossing, inclusief noodzakelijk retourtransport.

Terugbetaling uiterlijk 14 dagen na melding met toegestaan uitstel tot goederen of verzendbewijs (wat eerder is). Na goederen/bewijs verwerkt de policy uiterlijk binnen 7 kalenderdagen, met behoud van een eerder aflopende wettelijke termijn. Geen gratis retour of algemene maatwerk-/tegel-/leveranciersuitsluiting invullen. Alleen aantoonbaar geldige productuitzonderingen.

Controleer hoe de actuele Merchant-interface werkdagen/kalenderdagen, retourmethode, verwerking en uitzonderingen modelleert. Noteer de opgeslagen waarden en eventuele noodzakelijke toelichting. **Deze accountreadback is nog OPEN.** Het historische retourconcept is geen tweede klantpolicy.

[Google-productcontrole](../GOOGLE_PRODUCTCONTROLE.md) · [Accounts](ACCOUNTS_EN_KOPPELINGEN.md) · [Bronnen](../BRONNEN.md) · [Taken](../TAKEN.md)
