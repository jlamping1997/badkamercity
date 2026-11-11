# Brauer-keuzemenu’s — 11 november 2026

Status: IMPLEMENTED_TEST_ONLY, publicatie nog niet uitgevoerd.

De eigenaar heeft gevraagd de eerder voorbereide keuzemenu’s online te zetten. De bestaande livebasis is thema 196441932042 (Wiesbaden vervolg concept, nu MAIN). Een exacte Shopify-kopie wordt opgebouwd in UNPUBLISHED 196542005514 (BadkamerCity - Brauer keuzemenus 11 nov).

## Uitvoering

- 13.161 huidige native producten gecontroleerd op exact merk, SKU, handle, één variant, ACTIVE en openbare product-URL; geen identiteitsafwijkingen.
- 827 voorbereide groepen met 12.142 artikelen; negen bestaande CONTROLEREN-groepen en 732 overige enkelartikelgroepen blijven buiten de renderer.
- De groepsdata komen uit de bestaande privévoorbereiding. Alleen publieke productidentiteiten, de eerste exact gekoppelde afbeelding en goedgekeurde opties worden als theme-assets opgeslagen. Geen bronexports, inkoopdata, private eigen invoer of credentials in Git.
- Alleen twee regels toegevoegd aan main-product.liquid. Brauer heeft een eigen, geïsoleerde renderer en hergebruikt bestaande knop-/kleurstijlen. Andere merken en bestaande JavaScript blijven behouden.
- Geen Admin-productvelden, prijzen, voorraad, statussen, publicaties, media of metafielddefinities gewijzigd. De routes gebruiken exact gecontroleerde product-ID’s.
- Eén kleine groeps-JSON per huidige productpagina. Kleuren eerst; zes zichtbaar met uitklapper. Maten met meer dan drie keuzes gebruiken een native select.
- Voorwaardelijke draairichting/afvoerkeuzes vragen eerst een expliciete vervolgstap. Zolang meerdere echte artikelen overblijven wordt kopen geblokkeerd; er wordt geen willekeurig artikel gekozen.

## Bewijs

De lokale renderercontrole omvat alle 12.142 beginstanden, 151.274 geldige keuzes, 9.138 onmogelijke keuzes en 1.172 voorwaardelijke tussenstanden. Alle artikelen zijn bereikbaar. De native select, zeskleurenlimiet, exacte foto-/SKU-koppeling en tijdelijke cartguard zijn gecontroleerd. Zie STOREFRONT_VERIFICATION.json. Shopify Toolkit-validatie van 839 bestanden geeft nul fouten; complexiteitswaarschuwingen bij de gegenereerde routebestanden en bestaande sectie zijn apart zichtbaar in het privébewijs.

Alle 838 nieuwe conceptbestanden zijn na upload op door Shopify geretourneerde MD5 gecontroleerd. De aansluiting via main-product.liquid volgt pas nadat Shopify de themakopie compleet heeft afgerond. De oorspronkelijke 1684 bestanden worden daarna op behoud gecontroleerd.

## Nog te bewijzen

Echte desktop-/responsieve productwissels, native cartactie en herstel, complete conceptbronvergelijking, publicatie en verse publieke controle zijn op dit checkpoint nog niet uitgevoerd. Geen liveclaim.

## Herstel

Publiceer de ongewijzigde basis 196441932042 terug. Omdat uitsluitend themacode wordt gewijzigd, vereist dit geen herstel van productdata. Het Brauer-concept kan ook worden teruggezet door de twee Brauer-regels uit main-product.liquid te verwijderen; overige nieuwe bestanden zijn dan ongebruikt.

## Exact volgende handeling

Laat de themakopie afronden, sluit de renderer aan en voer preview-QA uit. De eigenaar heeft publicatie in deze sessie expliciet gevraagd.
