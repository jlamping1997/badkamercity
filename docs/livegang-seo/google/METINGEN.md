# Metingen — GA4 en winkelresultaten

**Stand: 8 november 2026 — DOC-LIVE-01.** [Bewijs en grenzen](../../audits/2026-11-08/README.md). De eerdere 5-novemberclaim “Google & YouTube niet aangetroffen” is historisch en geldt niet meer als actuele inrichting.

## Wat nu bekend is

| Onderdeel | Bewijsstatus | Betekenis |
| --- | --- | --- |
| Meet-ID | G-H9YFB5TC6N in live Google & YouTube-app/pixelconfig | VERIFIED_CONFIG; integratie heeft checkout-/e-commerceconfiguratie |
| GA4-property / stream / beheer | Eigenaar heeft GA4 aangemaakt en gekoppeld | USER_REPORTED; exacte accountrollen en rapportconfiguratie niet onafhankelijk gelezen |
| Realtime | Eigenaar meldt dat het lijkt te werken | USER_REPORTED; geen aankoop-/omzetbewijs |
| Cookiekeuzes | Accepteren, weigeren, heropenen bedienbaar in beperkte desktopbrowserproef | VERIFIED_UI; geen technische consentvrijgave |
| Aankoop en omzet | Geen purchase-test of rapportreadback | OPEN: value/currency, transaction_id en ontdubbeling |

Geen extra `gtag`/GTM-pixel in thema of HTML toevoegen zolang de bestaande integratie niet is onderzocht. Meerdere Google-container-ID's binnen de appconfig zijn op zichzelf geen bewijs van dubbele handmatige tags. Ontbreken in initiële server-HTML bewijst evenmin dat pixels niet worden geladen.

## Eerst valideren

1. Lees de huidige GA4-property, webstream en bevoegde beheerrollen terug; controleer dat de bedoelde stream G-H9YFB5TC6N is. Geen nieuwe property maken omdat een rapport nog leeg is.
2. Inventariseer Google & YouTube, eventuele custom pixels, GTM en thematags. Kies één bedoelde meetroute per gebeurtenis en controleer de feitelijke runtime.
3. Test toestaan, weigeren en intrekken/heropenen met passende opslag-/netwerk-/tagbewijzen. Consent Mode vervangt geen juiste toestemmingskeuze. Weigeren mag de gewone winkel niet onbruikbaar maken.
4. Controleer hieronder de echte gebeurtenissen met DebugView/Realtime of passend runtimebewijs. Configuratie is geen ontvangen event.
5. Valideer purchase bij de afgesproken bestelproef en vergelijk met Shopify; benoem testverkeer/testorders en attributie-/toestemmingsgrenzen.

## Gebeurtenissen

| Gebeurtenis | Acceptatie |
| --- | --- |
| view_item | Werkelijk bekeken artikel/uitvoering, valuta en koopbare prijs |
| add_to_cart | Juiste variant, aantal en eventuele gekozen onderdelen; geen dubbel event |
| begin_checkout | Werkelijke cart en bedrag |
| purchase | Eén bevestigde transactie, juiste transaction_id, value/currency; geen dubbele omzet bij herladen |
| Contact / retour | Alleen zo nodig een niet-inhoudelijke gebeurtenis; geen formuliertekst of contactgegevens |

Een cookie-UI-test, technische consenttest, eventtest en betaling zijn afzonderlijke bewijzen. Verstuur geen namen, e-mail, telefoon, adres, ordernotities of vrije tekst naar analytics.

## Eerste meetoverzicht

| Bron | Volgen | Betekenis |
| --- | --- | --- |
| Search Console | Indexatie, zoektermen, vertoningen, klikken, CTR | Organische vindbaarheid |
| Merchant Center | Geschikte/beperkte/afgekeurde items, vertoningen/klikken | Productfeed en productbereik |
| GA4 | Sessies, winkelwagen, checkout, aankopen/omzet | Gedrag binnen technische en privacygrenzen |
| Shopify | Bestellingen, werkelijke bedragen en refunds | Operationele verkoopcontrole |

Dit dossier richt geen geplande rapportage in. [Controles](../CONTROLES.md) · [Accounts](ACCOUNTS_EN_KOPPELINGEN.md) · [Officiële bronnen](../BRONNEN.md) · [Taken](../TAKEN.md)
