# BadkamerCity Hotbath categorieën en filterterugval 12 oktober 2026

## Gecontroleerde stand

Alle 8.235 echte Hotbath-artikelen zijn toegewezen aan de bedoelde webshopcollecties en teruggelezen op SKU, product-ID, actieve status en alle doelcategorieën. Twee testproducten zijn uitgesloten. De ronde voegde 27.083 ontbrekende categoriekoppelingen toe over 84 categorieën. Producttype en de standaard Shopify-taxonomie zijn niet aangepast.

De 15 resterende MHF011–MHF015-uitvoeringen zijn als afbouwdelen geplaatst. De Hotbath-catalogus onderscheidt MHF001–MHF005-inbouwboxen van MHF011–MHF015-afbouwdelen; de actuele fabrikantpagina bevestigt de overeenkomstige PVD-uitvoeringen binnen dezelfde familie. Bronnen: https://www.yumpu.com/nl/document/view/65256145/hotbath-catalogus-2020-2e-druk/251 en https://hotbath.com/nl-nl/product/mate-mhf013/ .

Er zijn 17 collecties aangemaakt. Bij de routecontrole bleken ze nog niet op Online Store gepubliceerd: alle 17 gaven een 404. Publicatie naar het bestaande Webshop-kanaal is vervolgens uitgevoerd en teruggelezen. Alle 17 openbare routes geven nu HTTP 200 met de juiste H1 en een productgrid. Inbouw douchesets is ook in de browser gecontroleerd: 2.959 artikelen, productkaarten, native filters en sortering aanwezig.

Het hoofdmenu kreeg 22 links naar deze 17 categorieën, inclusief de gedeelde douchecategorieën onder Kranen en Douche. Alle 234 bestaande menu-items behielden hun ID, titel, type, URL, resource en tags. De aangepaste navigatie bevat 256 items.

## Filtercorrectie in het concept

MAIN blijft 194981003530. Het bestaande concept 195038216458 blijft UNPUBLISHED. Alleen assets/bc-external-filters.js en snippets/bc-external-filters.liquid zijn aangepast. Vier betrokken bestanden zijn op MAIN en concept vóór en na teruggelezen; precies de twee bedoelde conceptwijzigingen en geen live codewijzigingen.

De proef blijft beperkt tot Wastafelkranen met bcfilters=1. De native lijst, filters, sortering en paginering blijven beschikbaar tijdens het eerste verzoek. Externe bediening activeert na een geldig antwoord. API-uitval, timeout, onbruikbare antwoorden en afwijkende collectieaantallen herstellen de originele native lijst en bediening. Een tellervergelijking gebruikt collection.all_products_count en API collection.profile_products; gelijke aantallen zijn geen bewijs van identieke membership of volledige datakwaliteit.

Verdere verbeteringen: eerdere verzoeken worden geannuleerd; alleen het nieuwste antwoord mag renderen; ieder verzoek heeft een timeout van 12 seconden; filteracties gebruiken browsergeschiedenis zodat terug/vooruit daadwerkelijk werkt. De drawer sluit met Escape en bij terugval.

## Validatie en beperkingen

- JavaScript syntaxcontrole geslaagd.
- Shopify Liquid-validator voor beide bestanden geslaagd; één niet-blokkerende unused-snippetwaarschuwing vanwege de minimale controlefixture. Documentatie-update timeoutte; gebundelde validatorgegevens zijn gebruikt.
- Negen jsdom-controles geslaagd: proef uit, laden, initiële API-uitval, afwijkende index, uitval na geslaagde resultaten, geldig leeg resultaat, filter/reset/terug/vooruit, snelle sorteeracties, drawer/Escape/terugval. Dit zijn DOM-tests, geen mobiele layouttests.
- Echte conceptbrowser bij Wastafelkranen: Shopify-aantal 454; native filters en paginering zichtbaar, externe toolbar verborgen, duidelijke terugvalmelding. Het concept is geïdentificeerd via de Shopify-previewbalk en de toegevoegde teller.
- Lokale Playwright-browserinstallatie mislukte; er wordt geen lokale browser- of mobiele eindcontrole als geslaagd opgevoerd.
- De externe index blijft verouderd: API-profiel Wastafelkranen 531 tegenover Shopify 454; Inbouw douchesets 2.973 tegenover Shopify 2.959; Kraan-toebehoren heeft geen API-profiel (404).
- Numerieke facetwaarden en eenheden moeten vóór verdere uitrol worden gecontroleerd; huidige API-profielen tonen onder meer grote maatwaarden met cm-labels.
- SSH naar de bestaande filterserver is vanuit deze uitvoering niet bereikbaar. Geen serverimport, profielherbouw, deployment of sitebrede filteractivering uitgevoerd.

## Bewijs en terugzetten

De bijgewerkte resultaatbundel bevat alle exacte producttoevoegingen, oorspronkelijke memberships, nieuwe readbacks, menu vóór/na, publicatie vóór/na, themabestanden vóór/na en testresultaten. Een verified_hotbath_membership.json bevat 8.235 echte Shopify-product-ID/SKU/categorierecords voor de vervolgstap. Productexports, bulkdatabestanden en servergeheimen staan niet in de publieke repository.

Voor terugzetten: herstel alleen de twee conceptbestanden uit theme_before/195038216458; het live thema is niet aangepast. Verwijder alleen deze ronde toegevoegde menu-items en memberships, met de exacte voor/na-bestanden. Pas een ongerichte categorie- of theme-rollback niet toe.

## Vervolg

Ververs via het bestaande Windows/VPS-filterproject de Shopify-master en universele index. Controleer eerst de actieve Typesense-collectie, bronpipeline en API-profielen. Verwerk ook de overige gepubliceerde merken; voeg geen tweede backend toe. Test categorieaantallen, echte memberships, merkdekking en maat-eenheden, daarna prijsfilter/reset/sortering/terug/vooruit/mobile drawer en API-uitval. Mobiele eindcontrole en publicatie van het samengebrachte concept blijven apart open. PR 5 blijft draft; issue 4 blijft open.
