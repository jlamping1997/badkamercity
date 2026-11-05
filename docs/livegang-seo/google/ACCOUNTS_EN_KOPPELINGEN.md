# Accounts en koppelingen

Stand **5 november 2026**. Deze publieke documentatie bevat beheerstructuur, geen inloggegevens.

| Systeem | Bekend | Actuele bewijsstatus | Functie |
| --- | --- | --- | --- |
| Webshop | badkamercity.nl | VERIFIED_ADMIN + HTTP | Verkoop en publieke inhoud |
| Shopify | fpa9hu-i3.myshopify.com | VERIFIED_ADMIN | Producten, collecties, checkout, kanalen |
| Google-account | Beheer gewenst via info@badkamercity.nl | USER_REPORTED; toegang TO_VERIFY | Eigendom van Google-diensten |
| Merchant Center | Bestaand account 5898992928 | USER_REPORTED op 4 november; inrichting TO_VERIFY | Gratis en betaalde productbestemmingen |
| Google & YouTube | Niet aangetroffen in zeven app-installaties; hasNextPage=false | VERIFIED_ADMIN | Standaard productkoppeling Shopify → Google |
| Search Console | Geen property/toegang in deze ronde gelezen | TO_VERIFY | Sitemap, indexatie en zoekprestaties |
| GA4 | Geen property/stream gelezen | TO_VERIFY | Bezoekers en verkoopgebeurtenissen |
| Google Ads | Geen account of campagne gelezen | TO_VERIFY / LATER | Advertenties met apart budget |
| DNS | Domein eerder bij Mijndomein genoemd | HISTORICAL; beheerder TO_VERIFY | Domeinverificatie |
| Git | jlamping1997/badkamercity | VERIFIED_GITHUB | Code en documentatie, geen vervanging voor Admin/Google |

## Gegevensstromen

| Van | Naar | Wat wordt beheerd? |
| --- | --- | --- |
| Leveranciersfeeds en gecontroleerde imports | Shopify | Artikelen, identifiers, prijs en beschikbare media |
| Git-codebranch shopify/current/ | Shopify-thema via bestaande releaseprocedure | Weergave en technische SEO; geen volledige productdatabase |
| Shopify | Google & YouTube → Merchant Center | Productgegevens, bestemmingen en afgestemde instellingen |
| Publieke website + sitemap | Google Zoeken | Crawlbare categorieën, producten en content |
| Google Zoeken | Search Console | Indexatie en zoekprestaties; SC is geen productfeed |
| Website/checkout via Google-integratie | GA4 | Gebeurtenissen binnen juiste privacy-instellingen |

## Accountkeuzes

- Gebruik het bestaande Merchant Center-account. Controleer toegang, rol, eventuele datastromen en domeinclaim vóór koppelen.
- Gebruik de bestaande Google-identiteit rond info@ waar mogelijk. Een e-mailadres en een Google-account zijn verschillende zaken. Google ondersteunt ook een bestaand niet-Gmail-adres; Workspace is geen voorwaarde voor deze inrichting. Verplaats geen e-mailhosting/MX-records om Google-vindbaarheid aan te zetten.
- Zoek bestaande Search Console- en GA4-properties vóór nieuwe te maken. Noteer daarna property, stream en verantwoordelijke beheerrol zonder persoonlijke herstelgegevens.
- Wijzig niet zomaar een bestaande domeinclaim of feed. Een verbinding met Shopify kan bestaande productfeedgegevens vervangen; eerst de actuele broninventaris maken.
- Eén primaire productkoppeling is voorlopig voldoende. Geen eigen Merchant API, tweede parallelle leveranciersfeed of extra feedplatform bouwen zonder aangetoonde behoefte.
- Een Google Bedrijfsprofiel is alleen aan de orde als BadkamerCity zelf aan de voorwaarden voor persoonlijk klantcontact voldoet. Een uitsluitend online winkel komt daarvoor niet in aanmerking.

[Officiële bronnen](../BRONNEN.md) · [Merchant Center](MERCHANT_CENTER.md) · [Search Console](SEARCH_CONSOLE.md)
