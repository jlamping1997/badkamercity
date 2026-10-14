# Productkaarten voor zoeken en categorieën — 14 oktober 2026

> **Goedgekeurd ontwerp, latere stand 14 oktober:** merchant heeft de gegenereerde productkaartopbouw goedgekeurd, expliciet zonder headerwijziging, en directe toepassing op het bestaande thema gevraagd. De actuele MAIN is nu `195211919626`. De Shopify-koppeling staat alleen writes op UNPUBLISHED toe en kan niet publiceren. Daarom staat de uitvoering klaar in identieke kopie `195213656330` — **BadkamerCity - Goedgekeurde productkaarten**. Merchant hoeft die versie alleen te publiceren; dit is een connectorbeperking, geen ontbrekende gebruikersautorisatie.

De gedeelde CSS wordt nu ook globaal geladen voor featured collections, category landings, collage, complementaire en gerelateerde producten die `card-product` gebruiken. Geen headersectie/markup gewijzigd. Native en zoekkaarten tonen maximaal twee eigenschappen uit het bestaande bevestigde manifest, uitsluitend bij overeenkomend SKU en formaat; anders producttype/artikelnummer. Externe API-kaarten tonen producttype en SKU, omdat die API geen materiaal/kleur per resultaat retourneert. Geen kenmerken uit titels geraden, geen nieuwe databundel of API-verzoeken per kaart. BTW-tekst verschijnt alleen wanneer `shop.taxes_included` waar is. ‘Bekijk product’ leidt naar de bestaande product-URL. Hartjes/wishlistfuncties uit de conceptafbeelding zijn niet als decoratieve werkloze knop toegevoegd.

Validatie: alle negen gewijzigde themabestanden exact teruggelezen, 10 filterregressietests geslaagd, 4 Liquid-rendercontroles geslaagd (bevestigde eigenschappen, verkeerd SKU, HTML-escaping, volledig ontbrekende data). Thema revisie 2 geldig met niet-blokkerende waarschuwingen; gecorrigeerd snippet revisie 3 geldig. Testscript: `scripts/test-card-specs.cjs` met `liquidjs` 10.30.0 als tijdelijke testdependency. Visuele desktop-/mobiele eindcontrole blijft NOT_TESTED; eerdere browserpreview werd geblokkeerd. MAIN niet geschreven of gepubliceerd. De paragrafen hieronder beschrijven de eerdere ontwerpronde.

## Scope en bron

De merchant vraagt duidelijkere productkaarten op zoekresultaat- en categoriepagina's, met filters links. De aangeleverde screenshot toont zoekterm `test`, lange afbeeldingsvakken, afgekorte titels en kleine grijze reguliere prijzen.

Een verse Shopify-read toont `195038216458` (Afronding basis 10 okt) inmiddels als MAIN. Daarom is via themeDuplicate een nieuwe ongepubliceerde kopie `195211919626` gemaakt: **BadkamerCity - Productkaarten 14 okt**. Geen MAIN-bestanden geschreven of thema gepubliceerd.

## Wijzigingen

- Eén gedeeld stylesheet voor zoekkaarten, externe collectiekaarten en native collectiekaarten.
- Vierkante witte afbeeldingsvakken, afbeeldingen gecentreerd zonder uitsnijden.
- Rustige rand, consistente binnenruimte, drie regels voor titels en duidelijkere prijzen.
- Merk toegevoegd aan zoekkaarten; externe kaarten hadden al een merkregel.
- Reguliere zoekprijzen worden nadrukkelijk weergegeven; verkoop- en vergelijkprijs gebruiken de Shopify money-filter met valuta.
- Drie kolommen op desktop vanaf 990 px, vier vanaf 1600 px, twee op kleinere schermen.
- Filterpositie, zoekmatching, prijsdata, voorraad, bestelgedrag en index niet aangepast.

## Validatie en open controle

Themevalidatie revisie 1: vier bestanden geldig. Bestaande ongebruikte snippetargumenten/variabele geven niet-blokkerende waarschuwingen. Git-whitespacecontrole met CRLF-herkenning geslaagd.

**BLOCKED / NOT_TESTED:** de cloudbrowser meldt ERR_BLOCKED_BY_CLIENT bij de nieuwe conceptpreview; geen succesvolle nieuwe visuele browsercontrole. Geen desktop- of mobiele goedkeuringsclaim. Merchant moet zoekresultaten, aanbiedingen, lange titels, categoriekaarten en mobiele weergave controleren voordat publicatie wordt overwogen.

De eerste Shopify-readback liet het nieuwe CSS-bestand zien maar de drie bestaande bestanden nog in oorspronkelijke vorm. Na voltooide duplicatie (processing=false) zijn alleen die drie bestanden opnieuw geplaatst. De definitieve readback bevestigt alle vier bestanden exact. MAIN blijft `195038216458`, de nieuwe kopie is UNPUBLISHED.

## Bestanden en herstel

Nieuw: `assets/bc-product-cards.css`. Gewijzigd: `sections/main-search.liquid`, `sections/main-collection-product-grid.liquid`, `snippets/bc-card-product-search.liquid`.

Herstel: verwijder de twee stylesheetverwijzingen in dit concept en herstel de zoekkaartsnippet vanuit de voorafgaande broncommit. MAIN blijft intact. Productgegevens hoeven niet teruggezet te worden.
