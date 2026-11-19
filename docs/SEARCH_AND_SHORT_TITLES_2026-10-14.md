# Zoekfilters en korte productkaarttitels — 14 oktober 2026

## Actuele uitvoering

Verse Admin-read: MAIN `195216048394` (Productkaarten verfijnd). Nieuwe identieke kopie `195218047242` (Zoekfilters en korte titels), UNPUBLISHED. Merchant vroeg filters op zoeken en een invulfunctie voor korte titels; titels worden later ingevuld. Connector blokkeert MAIN-bestandswrites en publiceren.

## Zoekcontract

`main-search` laadt dezelfde geverifieerde filterfrontend als collecties. Zoeken gebruikt API-profiel `__all__` en geeft de huidige URL-zoekterm als `q` door. Facetten worden door de API binnen die zoekvraag berekend; filters, paginering, prijs en sortering behouden de zoekterm. Geen nieuwe filterwaarden afgeleid.

De geverifieerde index bevat 11.050 leverancierproducten. Algemene koopresultaten sluiten geverifieerde serviceonderdelen uit; exact artikelnummer blijft rechtstreeks zoekbaar. Zoekresultaten kunnen daardoor afwijken van native Shopify (die ook omschrijvingen, content en het testproduct kan doorzoeken). Gewone tekstzoekvragen worden geen automatische interpretatie van bijvoorbeeld '30 cm douchekop'; daarvoor worden de bestaande exacte filters gebruikt. Expliciet artikel-/pagina-only zoeken blijft native. Predictive search in de header blijft native.

Native resultaten en controls blijven aanwezig en worden bij fout/timeout hersteld. De collectieledencontrole blijft behouden voor collecties. Zoeken controleert het globale profiel; de native zoekresultaat-telling wordt niet vergeleken met het totale catalogusprofiel.

## Korte titels

Merchant-owned PRODUCT-definitie `custom.card_title`, naam **Korte productkaarttitel**, type `single_line_text_field`, ID `418932031754`, gepind en PUBLIC_READ. Na aanmaak teruggelezen: nul ingevulde waarden. Geen producttitel, SEO-veld of productprijs gewijzigd.

Gedeelde Liquid-titelhelper gebruikt het ingevulde veld; een leeg veld behoudt de bestaande weergavetitel. Alle productkaarten tonen de volledige titel zonder line-clamp. Full-title tooltip en de productpagina blijven behouden.

API-kaarten lezen de actuele titel uit Shopify via de lichte Section Rendering API-sectie `bc-card-data`, met vier gelijktijdige aanvragen, 5s timeout en begrensde paginacache. Matching gebeurt op product-ID (GID normaliseren). Geen VPS-indexvernieuwing nodig na het invullen van een titel. Bij ontbrekende data blijft de bestaande titel zichtbaar; tekst wordt via textContent gezet. Productpaden zijn locale-aware. Geen verzonnen reviews/levertijden.

## Validatie en beperkingen

- 12 frontendtests: bestaande 10 plus zoekterm/filter/fallback en actuele korte titel met escaping.
- 13 Liquid-rendercontroles: kenmerken, bestaande titels, ingevulde/lege korte titel en HTML-escaping.
- JavaScript syntax check geslaagd.
- Liquid/theme-validator: 7 bestanden VALID, met bestaande niet-blokkerende main-search-waarschuwingen; cached Shopify-schema omdat online manifestverversing timeout gaf. Alle 7 geüploade bestanden exact teruggelezen in concept. MAIN opnieuw gecontroleerd en ongewijzigd.
- Live VPS-tests in deze sessie NIET UITGEVOERD: netwerkverbinding vanuit werkruimte timeout. Vorige door merchant uitgevoerde API/HTTPS-proeven staan in FILTER_PREVIEW_2026-10-14.md.
- Desktop/mobiel preview: NOT_TESTED, browserbeleid blokkeerde eerdere Shopifypreview. Niet als visueel getest presenteren.

## Afronding

Na conceptcontrole publiceert de merchant `BadkamerCity - Zoekfilters en korte titels`. Daarna eerst op /search?q=wastafelkraan merk/montage/kleur/prijs, sortering en terugknop controleren; ook mobiel. Een korte titel kan bij Producten → product → Metavelden worden ingevuld. Bulk editor kan hetzelfde veld als kolom gebruiken. Leeg maken herstelt fallback. Terugzetten: vorige theme `195216048394` publiceren; het ongebruikte lege veld kan blijven bestaan.
