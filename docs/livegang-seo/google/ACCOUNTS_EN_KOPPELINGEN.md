# Accounts en koppelingen

**Stand: 8 november 2026 — DOC-LIVE-01.** Beheerstructuur zonder inloggegevens. Een integratieconfiguratie bewijst geen toegang tot het externe account, goedgekeurde productfeed of actieve campagne. [Gedateerd auditbewijs](../../audits/2026-11-08/README.md).

| Systeem | Bekend | Actuele bewijsstatus | Functie |
| --- | --- | --- | --- |
| Webshop | badkamercity.nl | VERIFIED_ADMIN + HTML | Verkoop en openbare inhoud |
| Shopify | fpa9hu-i3.myshopify.com | VERIFIED_ADMIN | Producten, collecties, checkout en kanalen |
| Google-identiteit | Beheer via info@badkamercity.nl gewenst/gebruikt | USER_REPORTED; exacte rollen TO_VERIFY | Eigendom Google-diensten |
| Merchant Center | Bestaand ID 5898992928 | HISTORICAL_USER_REPORTED op 4 november; huidige toegang, bron, claim en goedkeuring TO_VERIFY | Productbestemmingen |
| Google & YouTube | Aanwezig; live app-/pixelconfig gelezen | VERIFIED_CONFIG; account-/Merchant-koppeling afzonderlijk TO_VERIFY | Standaard Shopify/Google-integratie |
| Search Console | DNS-domeinproperty, sitemap verwerkt, homepage geïndexeerd | VERIFIED_OWNER_SCREENSHOT, 8 november; geen volledige accountrapportage | Crawl/indexatie/zoekprestaties |
| GA4 | G-H9YFB5TC6N | VERIFIED_CONFIG; Realtime USER_REPORTED; propertyrollen en purchase TO_VERIFY | Gedrag en verkoopgebeurtenissen |
| Google Ads | Eigenaar maakte account en startte eerste campagnewizard | IN_PROGRESS_USER; account, activatie, budget en meting niet onafhankelijk gelezen | Betaalde advertenties |
| DNS | Eerder Mijndomein genoemd; DNS-verificatie via screenshot bevestigd | Beheer-/toegangsrol TO_VERIFY | Domein en eigendomsverificatie |
| Git | jlamping1997/badkamercity | VERIFIED_GIT / actueel auditmoment in centrale status | Code en documentatie, geen vervanging voor Admin/Google |

## Gegevensstromen

| Van | Naar | Beheer |
| --- | --- | --- |
| Leveranciersfeeds / gecontroleerde imports | Shopify | Identiteit, prijs, beschikbare media en leverdata |
| Git `shopify/current/` | Shopify-thema via releaseprocedure | Weergave/SEO; 15 gedeelde bestanden wijken af van live in deze audit |
| Shopify | Google & YouTube → Merchant Center | Productgegevens/bestemmingen en afgestemde instellingen; echte flow teruglezen |
| Publieke website + sitemap | Google Zoeken | Crawlbare categorieën, producten en content |
| Google Zoeken | Search Console | Indexatie en zoekprestaties, geen productfeed |
| Website / checkout via Google-integratie | GA4 | Gebeurtenissen binnen geteste privacy-/meetgrenzen |

## Beheerafspraken

- Lees bestaande Merchant-toegang, rol, domeinclaim en productbronnen terug. Geen tweede Merchant-account maken of claim/feed vervangen voordat dit duidelijk is.
- Gebruik de bedoelde zakelijke Google-identiteit. Google-account en e-mailhosting zijn verschillende zaken; geen MX-/mailmigratie nodig om deze koppeling te gebruiken.
- GA4 is inmiddels aangemaakt; controleer eerst de bestaande property/stream. Geen extra property/tag toevoegen om dezelfde site dubbel te meten.
- Eén primaire Shopify-productkoppeling volstaat voor nu. Geen Merchant API of parallel feedplatform zonder aangetoonde behoefte.
- Ads-onboarding is geen besluit om een campagne te activeren. Controleer budget, marges, bestemmingen en betrouwbare conversiemeting met Jackson.
- Een Bedrijfsprofiel alleen als Badkamercity zelf aan de voorwaarden voldoet. Harry Suiker niet als eigen verkoper, showroom of profiel overnemen.
- Bewaar geen credentials, herstelcodes, privé-adres, bankrekening, klantdata of checkoutreferenties in deze publieke documentatie.

[Merchant Center](MERCHANT_CENTER.md) · [Search Console](SEARCH_CONSOLE.md) · [Metingen](METINGEN.md) · [Bronnen](../BRONNEN.md)
