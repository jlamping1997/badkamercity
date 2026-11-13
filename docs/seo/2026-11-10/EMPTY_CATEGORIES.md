# Lege categorieën tijdelijk buiten Google — 10 november 2026

Status: EMPTY-CATEGORIES-01 / WITHDRAWN_BY_OWNER.

> Nieuwere opdracht: alle categorieën mogen indexeerbaar blijven. Het noindexvoorstel hieronder is historisch en teruggedraaid; publiceer het niet. De reserve-layout is weer exact gelijk aan actuele MAIN en het thema heet Reserve - gelijk aan live 10 nov. [Actuele vergelijking](../../repairs/2026-11-10/theme-consolidation/README.md).

## Opdracht en correctie

Eigenaar: “Ik heb nog geen producten voor die lege categorieen, die komen wel maar heb ik nog niet.... Dus beter even onzichtbaar dan ofzo”.

Deze expliciete assortimentkeuze vervangt de eerdere vijf voorstellen om lege categorieën te vullen met catalogusmatches. Die matches zijn geen door de eigenaar goedgekeurd assortiment voor deze collecties. Geen producten gekoppeld; geen voorwaardelijke meta’s toegepast. Historische kandidaten blijven alleen als niet-geaccepteerd onderzoek bewaard.

## Nulmeting en gekozen uitvoering

- 227 collecties vers volledig gelezen: 57 met nul leden; Tegeltoebehoren was al ongepubliceerd, 56 overige waren Online Store-gepubliceerd.
- Alle negen menu’s en alle 227 collectieomschrijvingen: nul verwijzingen naar deze 56 doelen.
- Twintig echte publieke responses vóór de wijziging: alle HTTP 200, nul gewone ankerlinks naar de doelen. Homepage, assortiment, alle producten, tien afdelingen, bestaande Sunshower-pagina, Meer, drie gevulde/merkcontroles en drie lege proefroutes.
- Meer heeft 24 leden en valt buiten de 56-doelenset. De bestaande Sunshower-Page en vendorselectie zijn andere routes en blijven behouden.
- De Online Store-publication is 283427864842, bevestigd via channel handle online_store. Andere verkoopkanalen buiten scope.

Een proef met publishableUnpublish op lege Badmeubel sets is door de Shopify-koppeling geblokkeerd vóór uitvoering: blocked=true, category=destructive, reason **Unpublishing is blocked to prevent accidental storefront catalog removal.** Geen alternatieve route gebruikt om dezelfde geblokkeerde publicatiemutatie alsnog uit te voeren. Publicatiestatussen, collectieleden, URL’s, SEO-velden en menu’s zijn niet gewijzigd.

Materieel kleinere uitvoering: alleen een noindex,follow-meta in een ongepubliceerd thema voor de expliciete lijst van 56 bestaande handles, en alleen zolang collection.all_products_count nul is. De pagina’s blijven bestaan. Een lege filteruitslag bij een gevulde collectie krijgt hierdoor geen noindex. Zodra een genoemde collectie producten bevat, past deze voorwaarde niet meer; de inhoud en selectie moeten bij herlancering nog worden gecontroleerd.

## Thema en bron

Actuele MAIN: **196441932042 — BadkamerCity - SEO afronding 10 nov**. De eigenaar heeft dit SEO-thema inmiddels gepubliceerd; vier actuele SEO-checksums zijn bevestigd. De eerdere publicatiewachtnotitie voor die tien extra meta’s is dus historisch.

Bestaande reserve **196395073802** hergebruikt en hernoemd tot **BadkamerCity - Lege categorieen tijdelijk uit**, UNPUBLISHED. Geen extra thema aangemaakt; Wiesbaden-concept 196416504074 niet beschreven.

Volledige bronvergelijking vóór writes: beide 1.401 bestanden; exact vier oude SEO-verschillen. Die vier bestanden vanuit MAIN meegenomen, met alleen de nieuwe afgebakende robotsvoorwaarde in layout/theme.liquid. Vier writes, nul userErrors en vier exacte uiteindelijke bodyreadbacks. De onmiddellijke eerste read had één vertraagde body; de daaropvolgende read was op alle vier bestanden exact. Settings_data-body niet gelezen of geschreven.

Ten opzichte van de huidige MAIN verschilt het concept functioneel alleen in layout/theme.liquid. De drie overige SEO-bestanden zijn exacte bronkopieën. Op de codebranch is daarom alleen shopify/current/layout/theme.liquid nieuw aangepast.

## Bewijs en grenzen

- Officiële lokale Shopify-validatie: geen fouten; alleen de bestaande scheme_classes-waarschuwing.
- 119 echte Liquid-rendergevallen: alle 56 lege handles krijgen noindex; dezelfde 56 met producten niet; zeven scope-/filter-/pagina-uitzonderingen correct.
- 22 eerdere metadata-renderregressies opnieuw PASS: native categorie-SEO, homepage, acht merken, beide overzichten, canonical/og:url, wishlist, paginering en fallback.
- Werkelijke Shopify-preview: **71/71 PASS**. Alle 56 doelen HTTP 200 en exact noindex,follow; 15 controles behouden exact de goedgekeurde titel/description en krijgen geen noindex. Iedere response bevestigt theme ID196395073802.
- Bestaande navigatie ongewijzigd; geen gevulde categorie onzichtbaar gemaakt.
- Native publicatie, sitemap, leden en SEO blijven ongewijzigd. De 56 routes zijn dus nog live indexeerbaar totdat het concept wordt gepubliceerd. Sitemapverwijdering wordt niet geclaimd.
- Geen Google-verwijdering, ranking/CTR-effect, mobiele koopflow of eigenaarpublicatie geclaimd. Geen browser- of Windows-uitvoering geclaimd.

## Historisch publicatievoorstel — niet uitvoeren

Eén volgende handeling: eigenaar beoordeelt/publiceert **BadkamerCity - Lege categorieen tijdelijk uit**. Daarna de echte live robotsmeta van de 56 routes en de 15 controles opnieuw nakijken. Google verwerkt noindex pas na opnieuw crawlen; geen onmiddellijk verdwijnen beloofd.

Het Wiesbaden-concept is ouder dan de huidige SEO-MAIN. Neem bij de latere gecombineerde release alle vier actuele SEO-bestanden mee, inclusief deze robotsvoorwaarde zodra goedgekeurd, zodat een ouder concept de meta’s of noindex niet terugdraait. Geen eigenhandige publicatie of MAIN-write.

Bij later toevoegen van de bedoelde producten: dezelfde bestaande IDs/handles gebruiken, setinhoud en selectie controleren, filters en zichtbare pagina testen. De noindex-voorwaarde verdwijnt bij een gevulde collectie; de eerder ongepubliceerde Tegeltoebehoren heeft daarnaast een afzonderlijke publicatiestap nodig. Alleen na een nieuwe expliciete opdracht weer publiceren via een toegestane route.

Herstel: de twee privéback-ups bevatten oorspronkelijke publicatiestaten en de vier reservebodies. Deze uitvoering veranderde publicatiestaten niet. Herstel alleen gewijzigde conceptfiles na checksumguard; niet een volledig oud thema over latere wijzigingen zetten.

Bronnen: [Shopify collectie-instellingen](https://help.shopify.com/en/manual/products/collections/collection-settings), [publishableUnpublish](https://shopify.dev/docs/api/admin-graphql/2026-10/mutations/publishableUnpublish), [Liquid collection](https://shopify.dev/docs/api/liquid/objects/collection), [Google lege categorieën](https://developers.google.com/search/docs/specialty/ecommerce/designing-a-url-structure-for-ecommerce-sites).
