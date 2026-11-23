# Brauer-keuzemenu’s — 11 november 2026

Status: VERIFIED_LIVE — gepubliceerd en daarna zonder preview gecontroleerd.

De eigenaar heeft gevraagd de eerder voorbereide keuzemenu’s online te zetten. De gemeten livebasis vóór deze ingreep was thema196441932042 (Wiesbaden vervolg concept). De exacte Shopify-kopie196542005514 (BadkamerCity - Brauer keuzemenus 11 nov) is via de Shopify-beheerpagina gepubliceerd en heeft de vers gecontroleerde rolMAIN. De oude basis196441932042 is UNPUBLISHED en blijft het herstelpunt.

## Uitvoering

- 13.161 huidige native producten gecontroleerd op exact merk, SKU, handle, één variant, ACTIVE en openbare product-URL; geen identiteitsafwijkingen.
- 827 voorbereide groepen met 12.142 artikelen; negen bestaande CONTROLEREN-groepen en 732 overige enkelartikelgroepen blijven buiten de renderer.
- De groepsdata komen uit de bestaande privévoorbereiding. Alleen publieke productidentiteiten, de eerste exact gekoppelde afbeelding en goedgekeurde opties worden als theme-assets opgeslagen. Geen bronexports, inkoopdata, private eigen invoer of credentials in Git.
- De Brauer-route en de weergavevoorwaarde voor de buybox zijn toegevoegd aan main-product.liquid. Brauer heeft een eigen, geïsoleerde renderer en hergebruikt bestaande knop-/kleurstijlen. Andere merken en bestaande JavaScript blijven behouden.
- Geen Admin-productvelden, prijzen, voorraad, statussen, publicaties, media of metafielddefinities gewijzigd. De routes gebruiken exact gecontroleerde product-ID’s.
- Eén kleine groeps-JSON per huidige productpagina. Kleuren eerst; zes zichtbaar met uitklapper. Maten met meer dan drie keuzes gebruiken een native select.
- Voorwaardelijke draairichting/afvoerkeuzes vragen eerst een expliciete vervolgstap. Zolang meerdere echte artikelen overblijven wordt kopen geblokkeerd; er wordt geen willekeurig artikel gekozen.

## Bewijs

De lokale renderercontrole omvat alle 12.142 beginstanden, 151.274 geldige keuzes, 9.138 onmogelijke keuzes en 1.172 voorwaardelijke tussenstanden. Alle artikelen zijn bereikbaar. De native select, zeskleurenlimiet, exacte foto-/SKU-koppeling en tijdelijke cartguard zijn gecontroleerd. Zie STOREFRONT_VERIFICATION.json. Shopify Toolkit-validatie van 839 bestanden geeft nul fouten; complexiteitswaarschuwingen bij de gegenereerde routebestanden en bestaande sectie zijn apart zichtbaar in het privébewijs.

Alle 838 nieuwe conceptbestanden zijn na upload op door Shopify geretourneerde MD5 gecontroleerd. De kopie is afgerond en alle2522bestanden zijn onafhankelijk teruggelezen:1684oudebronbestanden+838nieuwebestanden, nul verschillen. Daarna zijn uitsluitend de bedoelde sectie-aansluiting en thumbnailresizing bijgewerkt en teruggelezen. De eerste browserproef bracht een oude buybox-gate voor producten zonder metafield aan het licht; die is gecorrigeerd vóór publicatie.

## Browser, native cart en publicatie

Desktop: Amaze100Chateau→80Chateau→80Damascus; Collision100chroom→90chroom; StandaardA1gebogenrozettenchroom→Stripe5-CE-328. Spiegelkast100→60 geeft expliciet een onopgeloste draairichting met uitgeschakelde koopknop; Rechts opent exactSK-IMD60RHW. Nativecart:5-CE-328/variant54103527457034/€331,78, één regel. Testregel verwijderd en lege cart bevestigd. Responsieve controle op340CSS-px: scrollWidth337, menubreedte255; native breedtewissel100→80 correct. Zoom100% hersteld. Publicatie via Shopify-beheerpagina voltooid. MAIN196542005514 en oude basisUNPUBLISHED196441932042 onafhankelijk teruggelezen. Vijftien cookie-vrije openbare pagina’s PASS: dertien menu-artikelen over alle acht routepartities, één hold en één enkelartikelgroep. Nativevariant en volledige geselecteerde groeps-JSON exact; geen Liquidfout. De browser is uit de preview gehaald en toont de publieke Amaze-keuzes. Zie PUBLIC_VERIFICATION.json.

## Herstel

Publiceer de ongewijzigde basis 196441932042 terug. Omdat uitsluitend themacode wordt gewijzigd, vereist dit geen herstel van productdata. Het Brauer-concept kan ook worden teruggezet door de twee Brauer-regels uit main-product.liquid te verwijderen; overige nieuwe bestanden zijn dan ongebruikt.

## Exact volgende handeling

Deze publicatietaak is voltooid. De negen bestaande CONTROLEREN-groepen blijven geparkeerd; alleen na een nieuwe inhoudelijke opdracht oplossen. Voor aanpassingen aan artikelen/opties/foto’s de groepen opnieuw genereren uit het privébronpakket en een verse Shopify-identiteitsread met scripts/brauer/build_storefront_choices.py; geen nieuwe crawl of herimport nodig.

## Bewijsgrenzen en opslag

Broncode en publieke menu-assets staan op fix/product-cards-2026-10-14 onder shopify/current. Main krijgt uitsluitend dit dossier en actuele documentatie. De volledige private bron- en identiteitsbestanden zijn niet in Git opgenomen. De controles zijn uitgevoerd in een geïsoleerde Linux-checkout; de Windows-pc is niet gecontroleerd. Geen native telefoon-, volledige checkout-, alle12.142HTTP-pagina’s- of productieconversietest geclaimd. De algemene technische bronvragen en ontbrekende productmedia buiten deze menutaak zijn niet door deze publicatie opgelost. Geen actieve schrijver na overdracht.
