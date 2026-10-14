# BadkamerCity afronding basis 10 oktober 2026

**Status: REVIEW.** De bestaande Hotbath-productweergave, rustigere winkelwagen en Toebehoren-afbeeldingen zijn samengebracht in één nieuw ongepubliceerd thema. De desktopcontroles hieronder zijn geslaagd. Mobiele eindcontrole en publicatie staan nog open.

## Actuele basis

| Onderdeel | Vastgestelde stand |
| --- | --- |
| Store | fpa9hu-i3.myshopify.com |
| MAIN op 10 oktober | 194981003530, BadkamerCity - Collectiebeelden correctie 8 okt |
| Nieuw concept | 195038216458, BadkamerCity - Afronding basis 10 okt, UNPUBLISHED |
| Gebruikte Hotbath-bron | 194924904714, ongepubliceerd concept |
| Gebruikte Toebehoren-bron | 194988966154, ongepubliceerd concept |
| Git-uitgangspunt | ad969260eb786f0964f793c1d31e6e06dcbe5040 |
| Werkbranch | fix/afronding-basis-2026-10-10 |

De duplicatie is pas gebruikt nadat Shopify processing=false en processingFailed=false meldde en alle **441 bestanden op MD5 gelijk waren aan MAIN**. Na de wijziging zijn alle **445 bestanden** teruggelezen: precies 7 gewijzigde en 4 toegevoegde bestanden; de overige 434 hashes zijn gelijk aan MAIN. Zie [het previewmanifest](PREVIEW_MANIFEST_2026-10-10.json).

Git miste drie recentere live bestanden: assets/bc-meubelhub.css, sections/bc-meubelhub.liquid en snippets/bc-category-children.liquid. Die actuele basis is behouden voordat de conceptwijzigingen zijn toegevoegd. De historische snapshot van 7 oktober blijft historisch; die thema-ID is momenteel geen MAIN.

## Wat is veranderd

- Normale Hotbath-productpagina's lezen de bestaande gegroepeerde custom.complete_specificaties. Een korte introductie uit custom.korte_omschrijving en de bestaande concepttekst Levertijd op aanvraag worden alleen voor de gecontroleerde importscope getoond.
- De scope vereist de bekende importbatch, Hotbath als merk, één default variant, een overeenkomend artikelnummer en een niet-lege JSON-specificatie. Pilotproducten, TEST-SKU's, uitsluittags en afwijkende records vallen terug op de eerdere renderer. Een afwijkend fabrikantnummer binnen de specificaties onderdrukt de publieke tabel.
- Onbekende, lege, onbruikbare en expliciet vastgehouden bronclaims worden overgeslagen. Boolean false en nul blijven zichtbaar. Nederlandse en Engelse labels zijn toegevoegd.
- Voor deze Hotbath-scope wordt de oude kaart met 8–9 weken niet meer in de HTML gerenderd. De bestaande leverancierslogica voor Wiesbaden blijft aanwezig. Levertijdclaims van overige producten vragen nog een eigen broncontrole; bij Mosaic LO10101017 is de eerdere 8–9-wekenkaart nog zichtbaar.
- De specificatierouter bewaart de volledige bestaande renderer in bc-product-detail-specs-legacy.liquid. Andere merken en niet-passende Hotbath-records behouden die route.
- De willekeurige featured-collection-sectie in de winkelwagen is uitgeschakeld. Aantallen, bedragen en de bestaande checkoutknop blijven aanwezig.
- Toebehoren gebruikt actuele collectiebeelden voor de subcategorierijen, met productbeeld of lege placeholder als bestaande terugval. Sifons, Afvoerpluggen, Handdouchehouders en Hoofddouchehouders tonen de beelden van 9 oktober.

Producten, prijzen, varianten, categorieplaatsing, menu's, collectieomschrijvingen en filterinstellingen zijn in deze ronde niet gemuteerd. Setonderdelen en de bestaande artikelkeuzemenu's zijn behouden. Pilottemplates en oude Badkamermeubels-overrides uit het Hotbath-concept zijn niet overgenomen.

## Uitgevoerde controles

| Controle | Resultaat en bereik |
| --- | --- |
| Liquid-validator | Alle 11 gewijzigde/toegevoegde themefiles geslaagd, geen fouten. Bestaande complexiteits-/unused-waarschuwingen blijven; de introreferentie in JSON is gecontroleerd. De checker gebruikte zijn gebundelde documentatie nadat het ophalen van de nieuwste checkerdata timeoutte. |
| Lokale rendercontrole | 12 testgroepen geslaagd, waaronder 17 echte Hotbath-artikelen, label-only en keyed specificaties, scope-uitsluitingen, fabrikantmismatch, onbekende waarden, false/nul, bronclaims, escaping en NL/EN. Dit is een lokale LiquidJS-controle, geen Shopify-browsercontrole. |
| Shopify GraphQL | Iedere uitgevoerde operatie gevalideerd tegen de actuele connector-schema's. Het los gedownloade Admin-validatiescript kon niet draaien wegens ontbrekend gebundeld schema; deze fout is niet als een geslaagde test geteld. |
| Shopify readback | Alle 445 themebestanden gecontroleerd; 11 bedoelde afwijkingen, 0 onverwachte hashes. MAIN en bronconcepten behouden. |
| Browser en viewport | Chrome cloudbrowser, desktop 1348 × 936 CSS-pixels. De previewbalk én het gerenderde Shopify.theme-script bevestigen concept 195038216458. |
| Hotbath AC003BCP | Intro, specificaties, fabrikantnummer, Ja/Nee, prijs €301 en koopknop aanwezig; oude levertijdkaart afwezig. |
| Artikelkeuze | Koper → Chroom opent AC003CR met prijs €164; terug naar koper opent AC003BCP met €301. De preview blijft actief. |
| Hotbath IBS70CR347 | Gegroepeerde specificaties en introductie getoond; prijs €1.882,01. De bestaande acht setonderdelen blijven zichtbaar. Dit bewijst de renderroute, geen nieuwe leveranciersvalidatie van die bestaande mapping. |
| Andere merken | Wiesbaden 36.4046 (€216,59) en Mosaic LO10101017 (€95,95) behouden de bestaande specificatieroute en productweergave, zonder Hotbath-intro. |
| Winkelwagen | Begon leeg. AC003BCP via de echte koopknop toegevoegd, correcte variantlink 53187964993802 en €301. Aantal 2 geeft €602. Verwijderen werkt en testwinkelwagen weer leeg. Willekeurige aanbevolen productsectie afwezig. |
| Toebehoren | Alle vier bedoelde beeldbronnen geladen, zes relevante rijen inclusief hergebruik onder Wastafels; links wijzen naar de juiste collectiehandles. |
| Badkamermeubels | Compacte hero, bestaande kaarten en actuele collectiebeelden op desktop zichtbaar; zes bekeken kaartbeelden geladen. De drie Admin-stijlmarkers zijn bij de eerdere Admin-read bevestigd. |

## Nog te controleren vóór publicatie

- **NOT_TESTED:** deze nieuwe draft op 320–430 px / een echte telefoon. De beschikbare browserinterface bood in deze ronde geen ondersteunde viewportwijziging; een uitsnede geldt niet als mobiele test.
- **NOT_TESTED:** volledige catalogusdekking, alle switchergroepen, alle setmappings, browserconsole/performance, volledige checkout, betalen en orderafhandeling. Deze controles horen bij hun eigen afrondstappen.
- **REVIEW:** eigenaar beoordeelt de nieuwe conceptweergave. Publicatie gebeurt door de merchant, daarna worden MAIN, Git en de relevante verkooproute opnieuw gecontroleerd.

## Vervolg en terugzetten

De volgende inhoudelijke taak is een begrensde Hotbath-productgroep vergelijken met de broncategorieën en ontbrekende categoriekoppelingen vastleggen. IBS70CR347 en Mosaic LO10101017 zijn concrete gevallen uit de inventarisatie; die zijn in deze theme-ronde niet ingedeeld. Vervolgens de bevestigde Wiesbaden-typefouten, index en zoek-/filtertaak behandelen. Het centrale privéprojectoverzicht bewaart de volledige afrondlijst.

Voor publicatie volstaat het oude MAIN actief te houden; het nieuwe concept kan gericht worden hersteld vanuit de vastgelegde live basis. Na een eventuele publicatie kan de merchant terug naar het oude thema. Een theme-rollback herstelt geen Shopify-productdata. De bestaande PR 3 en zoektaak 4 blijven afzonderlijk open; deze wijziging neemt de cartverbetering mee zonder het hele oudere voorstel over te nemen.

De Windows-werkmap en de PowerShell-uitvoeringswrappers zijn niet gebruikt of gecontroleerd. De controles gelden voor deze verse Linux-checkout, connector-readbacks en de genoemde browserpreview.
