# Apps, privacy en systemen buiten het thema

**Actuele aanvulling: 8 november 2026.** MAIN is `196328685834 — BadkamerCity - Homepage SEO 8 nov`. [De centrale audit](../../audits/2026-11-08/README.md) vervangt oudere beginstanden over de Google-koppeling en policies. Installatie, configuratie, zichtbaar gedrag en werkelijk verstuurde meetevents zijn afzonderlijke bewijsniveaus.

## Actuele integratie- en privacygrenzen

| Onderdeel | Bewijs op 8 november | Nog open |
| --- | --- | --- |
| Google & YouTube / GA4 | Meet-ID `G-H9YFB5TC6N` aanwezig in live Google & YouTube-configuratie; eigenaar meldt Realtime-activiteit | Geen zelfstandig gelezen GA4-eventrapport of bewijs van `purchase`, value/currency, ontdubbeling of advertentieconversies |
| Consentbediening | In een beperkte desktopbrowsercontrole eerder op 8 november waren accepteren, weigeren en heropenen als UI bedienbaar | Geen netwerk-/opslagvergelijking vóór/na iedere keuze; intrekken en technische tagwerking niet daarmee bewezen |
| Cookievoorkeuren in footer | Niet in de onderzochte server-HTML van de footerprobes | De privacylaag kan dit na laden toevoegen; afwezigheid in server-HTML bewijst geen ontbrekende runtimeknop |
| Native policies | Contact, privacy, terugbetaling, voorwaarden en wettelijke kennisgeving aanwezig | Verzendbeleid ontbreekt; voorwaarden en kennisgeving tonen letterlijke HTML; aanwezigheid is geen juridische volledigheidsverklaring |
| Bronpariteit | 1.387 live bestanden; Git onder `shopify/current/`: 1.363 gelijk, 15 verschillend, negen alleen live, nul alleen Git | Geen volledige deploypariteit; afwijkende of beschermde API-bodies niet normaliseren om een groene controle te maken |

De zeven apprecords uit 28 oktober hieronder zijn een gedateerde inventaris, geen actuele telling van alle installaties. Google & YouTube mag op basis van die oude lijst niet langer als afwezig worden beschreven. Merchant-rechten, feedstatus, Google Ads-campagnes en accountgoedkeuring zijn niet door de aanwezigheid van een pixel bewezen. [Meetplan en controles](../../livegang-seo/google/METINGEN.md) houdt de afzonderlijke verificaties bij.

## Historische appinventaris — 28 oktober 2026

Zeven appinstallaties zijn toen read-only op titel/handle en herkomst geïnventariseerd. Installatie bewijst geen actieve storefrontcode, juiste configuratie, volledige gegevensstromen of werkende bedrijfsfunctie.

| App | Aantoonbaar op 28 oktober / nader uit te zoeken |
| --- | --- |
| Messaging | Shopify-app geïnstalleerd; inbox-/automatiseringswerking niet getest |
| Metafields Guru | Beheertool geïnstalleerd; geen app-private dataset geëxporteerd |
| Badkamercity Glossary Upload | Eigen uploadapp geïnstalleerd; code/deploy/secrets/rollback niet in themafiles aangetoond |
| Shopify CLI Connector App | Shopify-connector aanwezig; geen bewijs van automatische Git→live-deployment |
| Shopify ChatGPT MCP App | Shopify-connector aanwezig; bereik van de verbinding verschilt per resource |
| BadkamerCity Collection Images | Eigen app geïnstalleerd; bron/pipeline/hosting als afzonderlijk systeem volgen |
| Mollie - in3 | Betaalapp geïnstalleerd; geen bewijs dat iedere checkout in3 aanbiedt of accepteert |

Voor die zeven records was `isPostPurchaseAppInUse=false`. Dit ene veld sluit andere appblokken, embeds, pixels of betaalintegraties niet uit. Er zijn geen API-keys, abonnementen, facturen of secrets opgehaald.

## Waar code en meting worden toegevoegd

Themacode kan worden toegevoegd via `sections/apps.liquid`, `@app`-blocks waar het schema die toelaat, settings/embeds en platform `content_for_header`. Buiten het thema staan Shopify Web Pixels/Customer Events, gehoste checkout/accountuitbreidingen en appbackends. Een initiële HTML-scan kan die lagen niet volledig inventariseren.

De op 28 oktober ontvangen `settings_data.json`-body week van de toenmalige metadata af. Die oude uitzondering en de huidige Git/live-verschillen blijven bronbeperkingen; geen volledige embedstatus of automatische deploykoppeling uit een onvolledige kopie afleiden. De bronmanifesten in de centrale audit behouden hun eigen datum en hashes.

## Consent en browseropslag

De Admin-consentpolicy van **28 oktober** voor NL meldde `consentRequired=true` en `dataSaleOptOutRequired=false`. De beleidsread bevatte toen alleen privacy. Deze oude policytelling is ingehaald door de vijf huidige policies. De consentwaarden blijven configuratiebewijs met die datum, geen controle van banner, bewaartermijnen of ieder script.

Functionele opslag omvat wishlist, bewaarde cart en kortlevende keuze-/scrollhandoff; zie het [opslagregister](NAVIGATION_AND_STORAGE.md). Analytics-/marketingopslag moet afzonderlijk aan toestemming en werkelijk geladen requests worden gekoppeld. Een `localStorage`-vermelding is niet automatisch marketingtracking; een app zonder lokaal script is niet automatisch afwezig.

Voor technische afsluiting: leg per keuze accepteren, weigeren en intrekken de relevante opslag en requests vast, controleer dubbele meetroutes en toets de benodigde ecommerce-events apart. Zichtbare knoppen en een Realtime-melding sluiten deze controle niet af.

## Externe filterdienst en overdracht

De historisch onderzochte frontend verwijst naar de publieke `/verified/api/v1/search`-route op de bekende OVH-host. Backend/index/profielen, Caddy/TLS/CORS, auth, jobs en backups zijn afzonderlijke onderdelen. [FILTER_ENGINE](FILTER_ENGINE.md) scheidt broncode, publieke zoekproeven, historische serverkennis en ontbrekende serverstaat. Deze documentatieactualisatie geeft geen nieuwe server-/index-/deployvrijgave; het afzonderlijke filteruitroldossier behoudt zijn eigen status.

Voor ieder extern systeem zijn nodig: eigenaar/beheerlocatie, exacte repo en bronversie, omgeving/deploy, publieke/private endpoints, datavelden en bewaartermijnen, configuratie zonder secrets, monitoring, backup/restore en laatste controle. Voor eigen apps, VPS, Google-tools en gehoste checkout ontbreken delen hiervan. Een geregistreerde grens blijft open tot het passende bewijs bestaat.

[WISHLIST_STORAGE](micro/WISHLIST_STORAGE.md) beschrijft het gedateerde technische schema, ontbreken van TTL/accountsync, foutgedrag, events en multitabconflict. De replay gebruikt fictieve entries en bewijst geen werkelijk consentgedrag. Geen klant-/order-/inboxdata of geheime serverconfiguratie wordt naar publieke documentatie gekopieerd. [Dekkingsregister](../COVERAGE.md) en [centrale audit](../../audits/2026-11-08/README.md) houden deze grenzen expliciet.
