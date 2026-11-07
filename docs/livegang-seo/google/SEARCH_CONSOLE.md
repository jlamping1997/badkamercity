# Search Console — gewone Google-zoekresultaten

Search Console helpt eigendom, sitemapverwerking, indexatie en zoekprestaties te controleren. Merchant Center vervangt dit niet.

## Beginstand

- Website: https://badkamercity.nl.
- Sitemap: https://badkamercity.nl/sitemap.xml — HTTP 200 en parsebaar.
- Robots.txt verwijst naar die sitemap; bij de gelezen gewone homepage/categorie-/productresponses geen algemene noindex gezien.
- Eigendom, ingestuurde sitemap, indexeringsrapporten, handmatige acties en daadwerkelijke zoekprestaties: **TO_VERIFY**.
- Een ontbrekende google-site-verification-meta bewijst niet dat eigendom ontbreekt; DNS en andere methoden zijn mogelijk.

## Uitvoering

1. Open [Search Console](https://search.google.com/search-console) met de bedoelde Google-identiteit. Hergebruik een bestaande juiste property.
2. Gebruik waar passend een domeinproperty voor badkamercity.nl. Verifieer met het door Google verstrekte DNS-TXT-record bij de actuele DNS-beheerder. Bewaar bestaande mail-/webrecords.
3. Dien de bestaande sitemap in. Shopify onderhoudt die zelf; maak geen tweede handmatig product-sitemapbestand.
4. Controleer URL-inspectie voor homepage, Wastafelkranen, een gewone PDP, een tegel-PDP en de Sunshower-route. Onderscheid live test van opgeslagen Google-indexstatus.
5. Vraag eventueel voor enkele belangrijke URL's indexering aan; gebruik de sitemap voor het geheel.
6. Bekijk rapporten voor pagina-indexering en product-/verkopersvermeldingen waar beschikbaar. Leg fouten, Google's gekozen canonical en echte uitsluitingsredenen vast.
7. Gebruik zoekopdrachten, klikken en vertoningen als nulmeting zodra gegevens beschikbaar zijn. Geen gegarandeerde indexeringsdatum of ranking toezeggen.

## Technische controle

| Onderwerp | Beoogde uitkomst |
| --- | --- |
| Domein | HTTP/www gaan naar het gekozen HTTPS-hoofddomein |
| Belangrijke pagina | 200, relevante inhoud, bruikbare interne links |
| Canonical | Bedoelde voorkeurs-URL; varianten en query-routes afzonderlijk beoordelen |
| Robots/noindex | Geen onbedoelde uitsluiting; noindex kan alleen gelezen worden als crawlen mogelijk is |
| Paginering | Vervolgpagina's en producten via gewone crawlbare links bereikbaar, ook bij externe filtering |
| Sitemap | Alleen bedoelde publieke canonieke bestemmingen; sitemapstatus is geen indexatiestatus |
| Structured data | Syntaxis én inhoud bij actuele prijs, voorraad en uitvoering; toets met Rich Results Test |

Geen algemene robots- of canonicalwijziging uitvoeren vanuit alleen dit plan. De externe filters/zoekindex verdienen een aparte crawl-/rendercontrole; Git-code alleen bewijst geen Google-toegang.

## Resultaat vastleggen

Datum, propertytype, sitemapstatus, gecontroleerde URL's, indexatiestatus, gekozen canonical, fouten en vervolgactie in taken/logboek. Geen verificatiecodes of persoonlijke accountgegevens publiceren.

[Google's livegangrichtlijn en sitemapdocumentatie](../BRONNEN.md) · [SEO-roadmap](../seo/ROADMAP.md)
