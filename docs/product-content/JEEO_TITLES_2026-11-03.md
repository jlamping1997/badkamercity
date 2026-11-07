# JEE-O titels — 3 november 2026

Status: **VERIFIED_ADMIN / TITLE_ONLY_COMPLETE**.

## Opdracht en stijl

De eigenaar vroeg expliciet alle JEE-O-titels klantvriendelijk te maken voordat keuzemenu's worden aangepakt. Het aangewezen voorbeeld is: **JEE-O flow hoge wastafelkraan Geborsteld RVS**.

Merk + serie in kleine letters + natuurlijke productnaam + afwerking. Geen scheidingsstreepjes of lange cartridge-/materiaal-/montageomschrijvingen. Houd lengte/diameter alleen aan waar daarmee verschillende uitvoeringen herkenbaar blijven. Onderscheid onder meer laag/hoog, wand/inbouw/vrijstaand, handdouche/thermostaat, korte/lange uitloop en sensor.

## Uitvoering en verificatie

- Verse vooropname van exact **273 JEE-O-producten** met volledige ID/SKU/handle/titelkoppeling; alle ACTIVE en met onlineStoreUrl.
- Alle 273 producttitels gewijzigd via productUpdate met uitsluitend product-ID, nieuwe titel en de expliciet gelijk gehouden bestaande handle.
- Eerst drie proefproducten, daarna vijf groepen van 50 en één groep van 20. Iedere groep vooraf op merk/oude titel/handle gecontroleerd en na de wijziging exact teruggelezen.
- Eindinventaris opnieuw volledig gelezen: **273/273 titels exact**, **0 dubbele nieuwe titels**, **0 onverwachte wijzigingen** in de vergeleken overige velden.
- Gelijk gebleven: product-ID, handle, vendor, status, productType, descriptionHtml, onlineStoreUrl, templateSuffix, options en variants inclusief ID/SKU/titel/prijs.
- Drie oorspronkelijke openbare product-URL's geven HTTP200 met exact de nieuwe H1: Flow hoge wastafelkraan, Slimline plafondarm 15cm en Soho inbouw wastafelkraan.
- De korte/lange Soho-uitlopen zijn op fabrikantartikelnummer onderscheiden; de eerdere dubbele titels zijn opgelost. Pure geïntegreerde wandkraan en uitvoering met losse bediening zijn apart benoemd.
- Langste nieuwe titel: 78 tekens. SKU's zijn niet veranderd.
- Volledig voor/na-overzicht, oude titels en herstelkoppelingen zijn privé bewaard. Geen volledige catalogus of uitvoerlog in deze publieke repository.

## Grenzen en herstel

Alleen producttitels. Geen theme-write of publicatie; geen keuzemenu-, SEO-, metafield-, beschrijvings-, prijs-, voorraad- of mediabatch. De productUpdate-input bevat geen van die velden. Voorraad- en SEO-waarden zijn niet als afzonderlijk eindvergelijkingsbewijs opgevoerd.

De drie openbare GET-controles zijn server-HTML-bewijs. Geen fysieke telefoon, browserinteractie, winkelwagen, checkout of externe zoekindexvrijgave. Oude titels blijven beschikbaar in het privé voor/na-overzicht. Terugzetten: op exact product-ID de oude titel schrijven met dezelfde bestaande handle en daarna teruglezen.

Er is na afronding geen actieve JEE-O-schrijver of achtergrondworker.

## Volgende JEE-O-stap

Keuzemenu's per exacte model-/uitvoeringsfamilie uitwerken op de bestaande losse producten. Begin met de 15 Slimline-plafondarmen: lengte15/25/35cm en vijf afwerkingen. Controleer de werkelijk gebruikte huidige storefrontbron vóór implementatie. Andere lopende merken en bestaande themareview behouden hun eigen status.

## Vervolgcontrole — JEE-O kleurkoppelingen, 3 november 2026

Op het verzoek de upload/titels te controleren en kleurkoppelingen te onderzoeken is de actuele volledige JEE-O-inventaris opnieuw gelezen. Alle273titels en handles komen overeen met de eerder uitgevoerde titelverbetering; geen herhaalde productwrite nodig.

**READ_ONLY_PROPOSAL_NOT_APPLIED:**66mogelijke kleurgroepen met230producten en43losse producten zonder bestaande kleurtegenhanger. Iedere groep heeft dezelfde basisnaam, hetzelfde producttype en dezelfde modelcode, met unieke afwerkingen.8groepen/28producten zijn ook op eerder gecontroleerde fabrikantartikelcodes bevestigd;57groepen zijn catalogusgevalideerd. SWMBAS71 blijft één afzonderlijke HOLD-groep met2producten vanwege de fabrikant-PDF-code voor zwart. Geen relationele metafieldwaarden geschreven.

Live MAIN196052189450 read-only onderzocht: main-product rendert color_variants uitsluitend voor Wiesbaden; bc-wiesbaden-colors bevat een harde Wiesbaden-vendorcontrole. bc-card-data heeft dezelfde vendorgrens. De bestaande V2-JavaScriptbediening kan inline groepen en kleurstalen verwerken; er is geen nieuwe navigatie-engine nodig. Alleen refs invullen activeert dus geen JEE-O-UI.

Bestaande definitie custom.color_variants is list.product_reference. Het voorstel gebruikt per exact model dezelfde geordende referentielijst inclusief huidig product. Kleurwissels behouden lengte/vorm/type. Let op: bc-card-data laat een bestaand verified-product-filters-v1 manifest de kaartkleur overschrijven;137van230kandidaatlabels wijken tekstueel af van specs.kleur. Niet alle afwijkingen zijn inhoudelijke fouten; voorkom label-/selectieverschillen door bewuste veldprecedentie.

Groepsuniekheid, productscope, dekking en keuze→exact één product zijn gecontroleerd. Volledige koppellijst met oorspronkelijke ID's/SKU's/URL's privé opgeslagen; geen catalogus in publieke Git. Geen theme-write of publicatie. Geen browser-/mobiele kleurwisseltest of externe indexvrijgave geclaimd.

**Volgende JEE-O-actie:** kleuradapter op de productpagina en kaartgegevens in een bewezen identiek UNPUBLISHED-concept voorbereiden; eerst3Slimline-plafondarmgroepen van5 per lengte15/25/35cm, vervolgens selectie/prijs-/SKU-/fotokoppeling en navigatie testen. De overige merken behouden hun huidige bediening.
