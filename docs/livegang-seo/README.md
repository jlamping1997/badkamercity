# BadkamerCity — Livegang & SEO

Startpunt voor verantwoord verkopen, Google-vindbaarheid en verdere groei.
Aangemaakt op **5 november 2026**. Actieve opdracht **LAUNCH-01**: nulmeting en uitvoerbaar dossier in Git. De Google-inrichting en winkelcorrecties zijn nog niet uitgevoerd.

## Aanpak

We bouwen verder aan de openbare winkel met het assortiment dat correct en leverbaar is. Een compleet assortiment, alle merken en een volledig contentprogramma zijn geen voorwaarden om te beginnen. Wel moeten klanten vóór aankoop kunnen zien wat ze kopen, betalen en ontvangen, en moet de bestelafhandeling werken.

Google heeft verschillende sporen:

| Spoor | Doel | Beheer |
| --- | --- | --- |
| Gewone zoekresultaten | Vindbare categorieën, producten en advies | Website + Search Console |
| Gratis productvermeldingen | Producten met prijs en foto op Google | Shopify → Google & YouTube → Merchant Center |
| Betaalde advertenties | Extra bereik met advertentiebudget | Google Ads, later afzonderlijk besluiten |
| Meten | Bezoeken, winkelwagen en omzet begrijpen | GA4 + Shopify, met passende privacy-instellingen |

Meer producten toevoegen en SEO verbeteren kan daarna per kleine groep doorgaan. Goedkeuring of sitemapinzending garandeert geen vertoning of positie.

## Dossier

| Onderdeel | Vaste plek |
| --- | --- |
| Wat moet nu, wat is bewezen en wie doet het? | [Taken en acceptatie](TAKEN.md) |
| Winkelbasis en verkoopcontrole | [Webshop](WEBSHOP.md) |
| Accounts, eigendom en gegevensstromen | [Accounts en koppelingen](google/ACCOUNTS_EN_KOPPELINGEN.md) |
| Zoekresultaten, sitemap en indexering | [Search Console](google/SEARCH_CONSOLE.md) |
| Productfeed en gratis vermeldingen | [Merchant Center](google/MERCHANT_CENTER.md) |
| GA4, gebeurtenissen en toestemming | [Metingen](google/METINGEN.md) |
| Welke SEO-pagina's eerst en waarom? | [SEO-roadmap](seo/ROADMAP.md) |
| Bestaande ingangen en voorstellen | [Paginaregister](seo/PAGINAREGISTER.md) |
| Alle niet-product-URL's uit de sitemap | [Gedateerd URL-register](seo/url-register-2026-11-05.json) |
| Wat is besloten, gemaakt en gecontroleerd? | [Logboek](LOGBOEK.md) |
| Read-only nulmeting met meetgrenzen | [Bewijs 5 november](bewijs/2026-11-05-nulmeting.json) |
| Officiële informatie | [Bronnen](BRONNEN.md) |

## Vastgesteld op 5 november

- Openbare homepage, sitemap en robots.txt antwoorden met HTTP 200; www verwijst bij de gecontroleerde requests naar https://badkamercity.nl. HTTPS is ook in Shopify bevestigd.
- De twaalf product-sitemaps bevatten **11.887 unieke /products/-URL's** en daarnaast de homepage. Er staan ook **225 collectie-URL's, 119 Pages, één blog en één artikel** in de sitemaps. Dit bewijst publicatie in een sitemap, geen Google-indexatie of koopbaarheid.
- In de volledig gepagineerde app-installatielijst staan zeven apps; **Google & YouTube is daarin niet aangetroffen**.
- Shopify retourneert alleen een ingevuld standaard privacybeleid. De standaard refund-, terms- en shipping-policy-URL's geven 404. Een openbaar retourformulier bestaat wel.
- De homepage heeft een canonical maar geen meta description; de paginatitel is alleen Badkamercity.
- De opdracht om Lagoo zonder productfoto's te houden blijft gelden. Het bezochte Lagoo-product heeft ook geen schema-afbeelding. Dit vraagt een feeduitzondering, geen automatische fototerugplaatsing.
- Merchant Center, Search Console, GA4, DNS-eigendom, echte betalingen en formulierontvangst zijn niet in die accounts of processen gecontroleerd.

## Eerstvolgende handeling

**BC-LIVE-001:** de werkelijke verkopersgegevens, bezorgafspraken en retourvoorwaarden vaststellen, zodat de ontbrekende winkelinformatie en beleidsvelden gericht kunnen worden afgerond. Zie de [takenlijst](TAKEN.md). De overige Google-voorbereiding kan onafhankelijk worden voorbereid.

## Onderhoud en overdracht

De takenlijst bewaart de actuele taakstatus; het logboek bewaart de geschiedenis. Zet een taak pas op DONE met datum en passend bewijs. Een geïnstalleerde app is geen gekoppeld account; een gekoppeld account is geen goedgekeurde productfeed.

Na iedere uitvoering: taakstatus, betrokken instellingen/URL's, resultaat, ontbrekende tests en precies één eerstvolgende handeling bijwerken. Voeg accountidentificatie alleen toe als die nodig en niet geheim is. Geen wachtwoorden, herstelcodes, API-tokens, klant-/orderdata of privécontracten in deze publieke repository.

[Globale projectstatus](../LIVE_STATUS_AND_NEXT_STEPS.md) blijft de ingang voor het hele project. Themabron: shopify/current/ op fix/product-cards-2026-10-14. Dit dossier bevat geen theme-deploy of Shopify-datamutaties.
