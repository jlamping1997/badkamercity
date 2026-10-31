> **29 oktober2026 — HOME-01:** gekozen homepage met negen cirkels, configureerbare banners en 3D-afspraakaanvraag staat in concept195910795530. Zie [actuele werkstatus](../../LIVE_STATUS_AND_NEXT_STEPS.md) en het HOME-01-dossier. Oudere homepagevolgordes hieronder zijn historische bronnen; MAIN is niet aangepast.

# Homepage: volgorde, inhoud en eigen kaarttypen

Bronmoment **28 oktober 2026**. `templates/index.json` kiest de volgorde; de inhoud komt uit de sectieconfiguratie, menu's, Shopify-resources en beeldbestanden. Een niet-uitgeschakelde sectie is niet automatisch zichtbaar: Liquid kan op ontbrekende data stoppen.

## Actuele opbouw

| Volgorde | Sectie | Gegevens / werking |
| ---: | --- | --- |
| 1 | `home-sunshower` | Beeld met link naar `/pages/sunshower`; eigen CSS |
| 2 | `home-hero` | **Uitgeschakeld**; opgeslagen beelden/links bestaan nog |
| 3 | `home-category-grid` | `source_mode=menu`, `main-menu`; eigen categoriekaarten en beeldkeuze |
| 4 | `home-popular-products` | Geen collectie geselecteerd; de guard onderdrukt het hele blok |
| 5 | `home-complete-bathroom` | Drie advies-/ontwerpstappen; contactbestemming |
| 6 | `home-shop-by-style` | Vier stijlblocks; uitgebreide inhoud uit; advies-CTA's |
| 7 | `home-brand-rail` | Vijf merkblocks; link naar `/collections?view=merken` |
| 8 | `home-mijn-badkamercity` | Zes inspiratieblocks; titel Badkamerinspiratie, contact-CTA |
| 9 | `home-help-cta` | Advies/contactknoppen; beide momenteel naar contact |

Dit is de volgorde uit de JSON-`order`, niet de toevallige volgorde van properties in het bestand. Het aanzetten van de hero of kiezen van een populaire collectie verandert de zichtbare pagina zonder een nieuwe renderer te schrijven.

## Kaarten zijn verschillende functies

Categoriekaarten sturen naar assortimenten; stijl-/inspiratiekaarten dragen adviesinhoud; merkkaarten voeren een vendorroute uit; populaire producten hebben een eigen productkaart en productformulier. Het populaire-productsblok gebruikt dus niet automatisch `card-product.liquid`. Alle kaarttypen krijgen dezelfde afspraken voor focus, klikdoel, afbeelding, prijs en CTA wanneer zij dezelfde functie vervullen; een advieskaart hoeft geen koopknop te krijgen.

`home-popular-products` heeft een horizontale scroll-snaprail en eigen responsive breedtes. De bron kiest `section.settings.collection`, maximaal `product_count` producten en een view-all-bestemming. Zonder geselecteerde, gevulde collectie wordt niets gerenderd. De opgeslagen knoptekst “In winkelwagen” bewijst niet dat deze route nu live gebruikt wordt. Als dit blok wordt geactiveerd, moeten variant-/quantity-/selling-plan-guards en cartfeedback als eigen ingang worden gecontroleerd.

De hulpfunctie probeert alleen bij lege configuratie bestaande pagina's voor afspraak/contact als terugval. De huidige expliciete contactlinks hebben voorrang. Een marketingtekst over montage, ontwerp of persoonlijk advies is configuratie-inhoud; de operationele mogelijkheid en voorwaarden worden niet door de code bewezen.

## Afbeeldingen en onderhoud

Beelden worden geconfigureerd als Shopify-image of URL, afhankelijk van de sectie. Houd intrinsieke afmetingen, `sizes`, laadprioriteit en decoratieve/informatieve alttekst bij dezelfde plaatsing. De hero bevat positionering voor mobiel/desktop; de Sunshowerbanner heeft een eigen uitsnede. Eén algemene `object-fit`-wijziging kan verschillende doelen raken.

Beheer: Theme Editor → Homepage → juiste sectie/block. Categorieboom: Shopify Navigatie → gekoppeld menu. Collectie-inhoud: Shopify Collecties. Een themawijziging is niet nodig om een bestaand instellingveld te vullen. Bewaar uitgeschakelde inhoud totdat de eigenaar over hergebruik/verwijderen beslist.

Acceptatie: lege/gevulde populaire collectie, geldige/ontbrekende beelden, alle CTA's, menu versus handmatige blocks, mobiele horizontale rail, keyboardfocus, reduced motion, tekstomloop en section reload. Huidige HTTP-waarnemingen bewijzen serverstructuur; er is geen nieuwe conversie-, mobiele of performancevrijgave.

[Alle homepage-secties en instellingen](../reference/SECTIONS.md) · [Exacte templatevolgorde](../reference/TEMPLATES.md) · [Kaartvarianten](PRODUCT_CARDS_AND_FILTERS.md).
