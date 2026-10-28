# Apps, privacy en systemen buiten het thema

Bronmoment **28 oktober 2026**. Zeven appinstallaties zijn read-only op titel/handle en herkomst geïnventariseerd. Installatie is geen bewijs van actieve storefrontcode, correcte configuratie, volledige gegevensstromen of een werkende bedrijfsfunctie.

| App | Aantoonbaar / nader uit te zoeken |
| --- | --- |
| Messaging | Shopify-app geïnstalleerd; inbox-/automatiseringswerking niet getest |
| Metafields Guru | Beheertool geïnstalleerd; geen app-private dataset geëxporteerd |
| Badkamercity Glossary Upload | Eigen uploadapp geïnstalleerd; code/deploy/secrets/rollback niet in themafiles aangetoond |
| Shopify CLI Connector App | Shopify-connector aanwezig; geen bewijs van automatische Git→live-deployment |
| Shopify ChatGPT MCP App | Shopify-connector aanwezig; bereik van de huidige verbinding verschilt per resource |
| BadkamerCity Collection Images | Eigen app geïnstalleerd; bron/pipeline/hosting als afzonderlijk systeem volgen |
| Mollie - in3 | Betaalapp geïnstalleerd; geen bewijs dat iedere checkout in3 aanbiedt of accepteert |

Voor alle zeven ontvangen apprecords was `isPostPurchaseAppInUse=false`. Dit ene veld sluit andere appblokken, embeds, pixels of betaalintegraties niet uit. Er zijn geen API-keys, abonnementen, facturen of secrets opgehaald.

## Waar kan code worden toegevoegd?

Thema: `sections/apps.liquid`, `@app`-blocks waar de betreffende schema's die toelaten, settings/embeds en platform `content_for_header`. Buiten thema: Shopify Web Pixels/Customer Events, gehoste checkout/accountuitbreidingen en appbackend. De huidige `settings_data.json`-body wijkt van de metadata af; de volledige embedstatus kan daarom niet als bytegeverifieerde truth worden vrijgegeven.

## Consent en browseropslag

De Admin-consentpolicy voor **NL** meldt `consentRequired=true`, `dataSaleOptOutRequired=false`. Dat zijn geconfigureerde platformwaarden, geen bewijs dat banner, bewaartermijnen en ieder script correct reageren. De beleidsread bevat één bestaande policy van type privacy. Dit document beoordeelt geen juridische volledigheid.

Functionele opslag omvat wishlist, bewaarde cart en kortlevende keuze-/scrollhandoff; zie [opslagregister](NAVIGATION_AND_STORAGE.md). Analytics-/marketingopslag moet afzonderlijk aan consent en werkelijk geladen requests worden gekoppeld. Een `localStorage`-vermelding is niet automatisch marketingtracking, en een app zonder lokaal script is niet automatisch afwezig.

## Externe filterdienst

De frontend verwijst naar de publieke `/verified/api/v1/search`-route op de bekende OVH-host. Backend/index/profielen, Caddy/TLS/CORS, auth, jobs en backups zijn afzonderlijke onderdelen. [FILTER_ENGINE](FILTER_ENGINE.md) onderscheidt huidige frontendcode, publieke zoekproeven, historische serverkennis en nog niet gelezen serverstaat. Geen publieke API-URL als secret behandelen, maar geheime serverconfiguratie hoort nooit in dit Git.

## Overdracht per extern systeem

Nodig om een extern onderdeel inhoudelijk af te sluiten: eigenaar/beheerlocatie; exacte repo en bronversie; omgeving/deploy; publieke/private endpoints; datavelden en bewaartermijnen; configuratie zonder secretwaarden; monitoring; backup/restore; laatste read-only controle en resterende test. Voor de eigen apps, VPS, Google-tools en gehoste checkout ontbreken delen daarvan. Een tabel met “onbekend” is hier een expliciet open dossier, geen voltooiing.

Geen klant-/order-/inboxdata is gelezen of naar de publieke documentatie gekopieerd. Ontbrekende rechten worden niet omzeild. [Dekkingsregister](../COVERAGE.md) houdt deze systeemgrenzen open tot de benodigde bron daadwerkelijk is gecontroleerd.

## Wishlistopslag inhoudelijk gevolgd

[WISHLIST_STORAGE](micro/WISHLIST_STORAGE.md) legt het feitelijke schema, ontbreken van TTL/accountsync, lees-/schrijffouten, eventroute en multitabconflict vast. De replay gebruikt uitsluitend fictieve entries; geen bezoekeropslag of werkelijk consentgedrag gelezen. Dit is technische bron-/replaydocumentatie, geen juridische of platformconsentvrijgave.
