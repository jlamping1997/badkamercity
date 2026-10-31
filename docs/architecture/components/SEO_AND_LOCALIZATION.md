# Metadata, structured data, redirects en talen

> **31 oktober 2026 — FIX-01, UNPUBLISHED195948839178:** Alleen lege collectie-page_description krijgt titelgebonden gelokaliseerde fallback van max160tekens, met escape_once en expliciete meta-snippetparameters. Bestaande SEO behouden; geen stylelekkage in gemeten pagina’s. Zoekstatus/titel volgen actieve bron; verzendcopy€100 consistent zonder onbewezen zelfde-dagbelofte. [Actueel bewijs en rollback](../../repairs/2026-10-31/README.md). De bronregels/hashes en defectreplays hieronder beschrijven de eerdere nulmeting.

Bronmoment **28 oktober 2026**. Dit dossier beschrijft de technische uitvoer en beheerlocaties. Het is geen verklaring van ranking, indexatie, juridische juistheid of Core Web Vitals.

## Globale uitvoer

`layout/theme.liquid` levert canonical via `canonical_url`, paginatitel en optionele `page_description`. Het snippet `meta-tags` kiest Open Graph-/Twittertitel, beschrijving, URL en afbeelding; productroutes kunnen prijs-/valutametadata toevoegen. Wijzig het echte product-/Page-/collection-SEO-veld voordat je een globale tekstfallback vervangt. Shopify kan gelijke expliciete SEO-titels als leeg normaliseren; de effectieve gerenderde titel blijft de relevante controle.

Voor Page-handle **verlanglijst** staat expliciet `noindex,follow` in de layout. Dat is geen algemene noindex-regel voor alle QA-templates of alle browseropslagpagina's. Een `noindex` verandert ook niet vanzelf de toegang tot inhoud.

`content_for_header` is een platforminjectiepunt voor Shopify en apps. Wat daarin live verschijnt, is niet uitsluitend uit de Liquid-root af te leiden. Het ontbreken van een lokaal analyticsbestand bewijst dus niet dat geen analytics wordt geladen.

## Structured data per renderer

| Familie | Bron / controle |
| --- | --- |
| Algemene PDP | `main-product` en platformproductdata; identiteit, aanbiedingen en zichtbaarheid samen beoordelen |
| Sunshower PDP | Eigen sectie; niet blind het algemene PDP-contract aannemen |
| Adviesartikel | `bc-advice-article`: `article | structured_data` |
| Meubelhub | Eigen JSON-LD met collectie-/breadcrumb-/itemlijstgegevens; linkguards bepalen entries |
| Andere lijsten / inhoud | Alleen claimen wat de betreffende actuele response werkelijk levert |

Controle bestaat uit twee verschillende vragen: is de JSON parsebaar, en klopt de inhoud bij het zichtbare aanbod? De HTTP-checks leggen het eerste vast op de bezochte routes; geen prijs-/voorraad-/rich-resultvrijgave. Vermijd dubbele schema-uitvoer door een extra algemene JSON-LD boven bestaande renderers te zetten.

## Redirects en publicatie

Verse Admin-read: **120 redirects**, volledig gepagineerd. Belangrijkste koppeling is de begrippenroute naar Pages. Een redirect wijzigt niet de templateSuffix of publicatie van het doel. Bij hernoemen: oud pad → bedoeld gepubliceerd doel → canonical → interne links controleren; loops/ketens en hoofdletter-/slashverschillen apart behandelen.

Er zijn 119 Pages en 226 collectietoewijzingen geregistreerd. `isPublished`, productstatus, kanaalpublicatie en een bereikbare response zijn verschillende meetpunten. Het publieke Git bevat geen volledige private productwaarden; daarvoor bestaat de afzonderlijke [productdata-export en het datamodel](../PRODUCT_DATA.md).

## Talen, markt en geld

Admin meldt alleen **Nederlands (`nl`) primair en gepubliceerd**, één actieve markt Nederland, EUR en `taxesIncluded=true`. Het thema bevat 51 locale-assets inclusief editor-schema's. Aanwezige Duitse/Engelse vertaalbestanden betekenen geen gepubliceerde storefront in die taal. Markt-, taal- en verzendbestemming zijn afzonderlijke instellingen.

Vertaalde labels worden via `t` gebruikt; eigen componenten hebben ook hardcoded Nederlandse tekst. Nieuwe gedeelde UI-tekst in de bestaande localegroep opnemen en consumers/lege-fallback controleren. Globale font-/kleursettings staan in [SETTINGS](../reference/SETTINGS.md); de feitelijke CSS-cascade blijft routeafhankelijk. Prijzen niet als tekst parsen om opnieuw btw toe te voegen.

## Open controles en onderhoud

Search Console, sitemapdekking, robots.txt, echte indexatie, crawlstatistiek, consentafhankelijke analytics en veldperformance zijn niet via deze themabron bewezen. Er is geen Google-accounttoegang gecontroleerd. Voor een SEO-wijziging: bronresource, effectieve head, canonical/robots, schema, interne links en redirects naast elkaar beoordelen; documenteer het verschil tussen syntaxis, inhoud en externe indexatie.

[Admin-bronmoment](../reference/ADMIN.md) · [Bronhashes](../reference/source-index.json) · [HTTP-bewijs](../evidence/2026-10-28-complete/README.md).
