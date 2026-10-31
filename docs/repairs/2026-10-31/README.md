# FIX-01 — betrouwbaar bestellen, filters en vervolgreparaties

31 oktober 2026. De eigenaar geeft opdracht de gedocumenteerde fouten te herstellen. Bestaande uitvoeringsbranch fix/product-cards-2026-10-14 blijft behouden. Windows niet onderzocht.

## Actuele bron en preview

De eigenaar heeft NAV-02 inmiddels gepubliceerd: MAIN **195947036938 — Categorieen zonder schuiven**, updatedAt 08:57:37Z. Bestaand UNPUBLISHED **195948839178** wordt hergebruikt. Volledige verse manifests van beide bevatten 1.354 paden en verschillen aanvankelijk uitsluitend in sections/header.liquid. Alleen die header is vanuit de verse MAIN-body in het concept bijgewerkt en bytegelijk teruggelezen; de andere 1.353 metadatapaden waren gelijk. Geen nieuwe volledige kopie, geen MAIN-write/publicatie.

409 tekstbronnen opnieuw aan de verse manifesthashes getoetst; 407 bytegelijk. De bestaande settings_data- en retourtemplatecommentaaruitzondering blijven apart. Alleen de drie hieronder beschreven runtimepaden worden in deze eerste correctiestap veranderd; niet de hele Git-root uploaden.

## Eerste reparatiestap

| Probleem | Herstelcontract | Bewijs |
| --- | --- | --- |
| CART-F01 | Ontbrekende/null/onbruikbare productsection wist vorige artikelinhoud; ontbrekende CTA wordt generieke cartlink; onbekende badge wordt verborgen tot geldige markup terugkomt. Geen tweede add-request. | CN-02/03/08 |
| SS-F01 | Pending set-add blokkeert configuratie, hoeveelheid, extras en andere kooproutes. Bij iedere niet bevestigde uitkomst eerst cart controleren; geen blinde retry. Bfcache ontgrendelt geen onzekere koopactie. | SS-01…04 |
| FILTER-F01 | Na fallback geeft de externe controller de pagina definitief aan native Shopify tot een volledige nieuwe navigatie. Geen externe zoekread op latere popstate en geen schrijven naar oude losse nodes. | FX-37 met echte native gridmethode en requeststubs |
| FILTER-F02 | Toon minder gebruikt dezelfde per-facetlimiet als eerste render; geselecteerde opties blijven zichtbaar. | FX-22 met limiet2 |

## Testgrenzen

De oude harness blijft onveranderd als gedateerd bewijs. De nieuwe repair-cart-sunshower.mjs en repair-filters.mjs bevatten het nieuwe contract en expliciete kandidaat-hashcontrole. Alle producten/verzoeken zijn synthetisch. Geen echte cart, order, checkout of mail. Vooraf: 15 cases met drie defectstimuli voor twee problemen; 41 filtercases met twee defectreproducties. Daarna: 18 cart/Sunshowercases en 41 filtercases zonder DEFECT_REPRODUCED. Overige benoemde grenzen blijven zichtbaar.

De huidige JSON-bundel is een tussencheckpoint. Theme Check, conceptwrite/readback en echte browsercontrole volgen. Shippingcopy, zoektelling, tegelprijseenheden, wishlist, ontbrekende bestemmingen en SEO zijn nog geen afgeronde onderdelen van dit checkpoint. Retourmail en offerteverificatie blijven afzonderlijke open bedrijfscontroles. Geen oude bevinding stil sluiten.
