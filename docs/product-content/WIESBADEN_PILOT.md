# Wiesbaden — inventarisatie en proefselectie
Gemeten: 16 oktober 2026, Europe/Amsterdam. Status: VERIFIED_ADMIN voor onderstaande winkelwaarnemingen; externe claims nog niet gecontroleerd.

## Wat is uitgevoerd?
- Shopify-store bevestigd: fpa9hu-i3.myshopify.com.
- Exact 2.265 producten met vendor Wiesbaden geteld en alle identifiers opgehaald, inclusief volledige variantpaginering.
- 50 omschrijvingen als eerste steekproef opgehaald; dit is geen beoordeling van alle 2.265 teksten.
- 10 proefproducten volledig gelezen voor omschrijving, metafields en collectietoewijzingen. Alle relevante pagina's compleet.
- Elk geselecteerd SKU komt exact één keer voor in de volledig uitgelezen Wiesbaden-variantlijst. Merk + SKU is daarmee voor deze proef bruikbaar. Dit bewijst geen foutloze externe bronmatching.
- [Register van alle producten](wiesbaden-register.json): ieder product heeft een status; 2.255 overige teksten zijn nog niet beoordeeld.
- Nul Shopify-mutaties; geen nieuwe teksten gepubliceerd.

## Proefselectie
| SKU | Product | Reden en controlepunt |
| --- | --- | --- |
| 20.3755 | Wiesbaden Graffic inloopdouche 800 x 2000 x 10 mm nano safety glass folie helder glas/chroom | Lange generieke glasuitleg; absolute veiligheidsclaims controleren. |
| 20.3756 | Wiesbaden Graffic inloopdouche 900 x 2000 x 10 mm nano safety glass folie helder glas/chroom | Maatvariant van 20.3755; 900 mm behouden. |
| 32.3411 | Wiesbaden Barco waskom ovaal 40 x 33 x 14,5 cm keramiek glans wit | Omschrijving bestaat hoofdzakelijk uit losse specificaties. |
| 32.3594 | Wiesbaden one-pack Porta fontein + Metro kraan | Nauwelijks uitleg; exacte setinhoud en maten ontbreken in uitgelezen data. |
| 32.2510 | Wiesbaden Vesta Tornado flush wandcloset rimless met nano coating met Shade slim toiletzitting softclose en quick release glans wit | Dubbele uitleg over toiletzitting. |
| 32.3670 | Wiesbaden Marmaris onderkast met 2 laden 60 x 45 cm mat zwart | Maatconflict: titel/tabel/metaveld 60 x 45 cm; lopende tekst 60 x 46 cm. |
| 38.4125 | Wiesbaden Ambi one spiegel rechthoek met LED, dimbaar en spiegelverwarming 140 x 60 cm | Condensvrij is te breed: bestaande tekst beperkt verwarming tot twee matjes. |
| 41.3540 | Wiesbaden Elara sierradiator 76,6 x 60,0 cm antraciet | Warmteafgifte 463 W heeft in uitgelezen tekst geen temperatuurregime. |
| 24.3710 | Wiesbaden 304 wastafelkraan met coldstart geborsteld RVS | Ononderbouwde superlatieven en gezondheids-/zuiverwaterclaims verwijderen uit nieuw concept. |
| 29.8007 | Wiesbaden Dreams afbouwdeel thermostatische douchekraan met 2 stopkranen mat zwart | Afbouwdeel expliciet onderscheiden van complete kraan. |

Deze selectie bevat negen producttypen, inclusief twee Graffic-maatvarianten om consistente verwerking van maten te testen.

## Bevindingen en gevolg
1. Bestaande specificaties vormen een bruikbare start. De 10 proefproducten hebben allemaal een specificatietabel in descriptionHtml én productmetafields. Dit zijn eigen winkelgegevens, geen onafhankelijke bevestiging van productclaims.
2. EAN staat in alle 10 proefomschrijvingen. Het komt ook voor in sommige global.description_tag-velden. Conform gebruikersvoorkeur niet opnemen in nieuwe tekst; deze audit verwijdert nog niets uit Shopify.
3. 32.3670 heeft een maatconflict: titel en datavelden 60 x 45 cm, lopende tekst 60 x 46 cm. Eerst exacte fabrikanttekening controleren; niet gokken.
4. 32.3594 heeft alleen een zeer korte productuitleg. Setinhoud en benodigde onderdelen moeten vanuit fabrikant/leverancier worden vastgesteld.
5. 24.3710 bevat brede gezondheids- en materiaalclaims. Nieuwe tekst beperken tot onderbouwde eigenschappen en bruikbare uitleg over coldstart.
6. 38.4125 noemt condensvrij terwijl de tekst de werking beperkt tot verwarmingsmatjes. Nieuwe tekst moet die beperking duidelijk maken; energielabel en installatieclaims eerst opnieuw controleren.
7. Meerdere global.title_tag/description_tag-waarden eindigen midden in een woord. Deze SEO-velden apart schrijven; geen harde blinde afkaproutine.
8. Belangrijke bestaande waarschuwingen blijven in het bewijsdossier: Wisa bij 32.2510 en los inbouwdeel 29.8004 bij 29.8007. Pas na broncontrole aanpassen.
9. De huidige HTML bevat technische-documentlinks en inline-opmaak. Vervangen van descriptionHtml kan die informatie raken; vóór latere import vaststellen hoe de producttemplate documenten en specificaties toont. Geen blinde HTML-vervanging.

## Interne links
Admin bevestigt passende categorieën, onder andere opbouw-wastafelkranen, inloopdouches, opzetwastafels, fonteinsets en inbouw-douchekranen. Alle kandidaatbestemmingen staan per proefproduct in het register.
Dit bewijst het bestaan/toewijzing in Admin; openbare bereikbaarheid en relevantie vóór verwerking apart controleren. Nog geen interne links toegevoegd.

## Technische grenzen
- Een SKU-zoekquery vond sommige bekende producten niet terug. Daarom is geen afwezigheid of uniciteit uit zoekresultaten afgeleid: de volledige lijst van 2.265 producten is uitgelezen en exact op SKU vergeleken.
- De eerste Shopify-toolroute vroeg om authenticatie; de bestaande andere Shopify-connector werkte. Geen extra aanmelding nodig voor deze inventarisatie.
- Verse MAIN-read: 195313991946, BadkamerCity - Werkpreview categoriekaarten. De naam Werkpreview betekent dus inmiddels MAIN. Geen themawijziging uitgevoerd.
- Geen Windows-werkmap gecontroleerd. Geen bronextractie, publieke linktest, SEO-rankingmeting of schrijfstijlreview uitgevoerd.
- Ruwe bestaande omschrijvingen zijn niet opnieuw in deze publieke repository gepubliceerd. Vóór echte tekstmutaties is een afgeschermde herstelkopie vereist.

## Volgende handeling
Test fabrikant-/leverancierbron en één aanvullende webshop op de proefartikelen 24.3710 (kraan), 32.3594 (set) en 32.3670 (maatconflict). Bewijs eerst dat exacte artikelmatching en bruikbare gegevens werken; breid die extractie daarna uit naar alle tien proefproducten. Pas daarna conceptteksten schrijven.
