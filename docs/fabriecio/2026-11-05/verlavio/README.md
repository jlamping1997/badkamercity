# Verlavio — private label Fabriecio

> **Vervolg FAB-04 — 5 november 2026:** de rebrand hieronder is het bewezen checkpoint van 15:51:12 UTC. Daarna zijn 29 echte voorraadaantallen gesynchroniseerd en is de Nederlandse Market-verzendoorsprong gericht hersteld. Volledige backendcontrole en echte winkelwagenproef PASS; alleen de voorraadtekst wacht op eigenaarspublicatie van **BadkamerCity - Verlavio voorraad en levertijd (196227170570)**. Zie [het actuele voorraaddossier](../stock/README.md). Het oude koopbaarheidsonderzoek is daarmee afgerond; de rebrand zelf blijft voltooid.

5 november 2026. **APPLIED_VERIFIED / MERCHANT_PUBLISHED**.

Het commerciële merk is **Verlavio**. Fabriecio blijft de interne leverancier en bronkoppeling. De eigenaar heeft **BadkamerCity - Verlavio merknaam** gepubliceerd; verse Shopify-controle bevestigt **MAIN 196116087050**. Voormalig MAIN 196227170570 is UNPUBLISHED. De publicatieblokkade uit FAB-02 is daarmee vervallen. Er zijn in deze uitvoering geen bestanden naar MAIN geschreven en geen thema's door de uitvoerder gepubliceerd.

## Publicatie en compatibiliteit

Vóór de merkdatamutaties zijn de drie gepubliceerde compatibiliteitsbestanden exact gecontroleerd. De guards ondersteunen zowel Fabriecio als Verlavio, zodat bestaande keuzemenu's en leverinformatie behouden blijven na de vendorwijziging.

| Bestand in `shopify/current/` | Gepubliceerde MD5 |
| --- | --- |
| `sections/main-product.liquid` | `2aac7f2aa3443560e016a3aa71c31fba` |
| `snippets/bc-fabriecio-choices.liquid` | `eab962d1ff1e998140d9adbd12d163a4` |
| `snippets/bc-fabriecio-delivery.liquid` | `89f25b1af70bc0a997032c4850c8a800` |

De compatibiliteitsversie was eerst gericht vanuit het toenmalige MAIN gelijkgemaakt: beginmanifesten 1.381 tegenover 1.378 gaven zes featureverschillen, alle zes na overname hashgelijk. Geen blinde repo-push of `settings_data.json`-write. Gedeelde Hotbath-CSS/JS blijven ongewijzigd.

## Merkdatamutaties

Verse nulmeting: 861 producten met vendor Fabriecio, nul met Verlavio. Alle 861 actuele producten zijn vóór uitvoering opnieuw gelezen; identiteit, bestaande titel/tagwaarden, SEO, omschrijving en keuzemenu-digests komen overeen met het begrensde uitvoerplan. De huidige producttitels worden als bron gebruikt; geen oudere importtitels terugzetten.

| Onderdeel | Uitvoerscope |
| --- | --- |
| Producten | 861 bestaande producten: vendor, merkprefix in titel en exacte merk-tag naar Verlavio |
| Keuzemenu's | 665 bestaande JSON-velden: uitsluitend de zichtbare producttitels |
| Afbeeldingen | 1.665 bestaande altwaarden: uitsluitend het merk in de tekst |
| Omschrijving en SEO | Geen Fabriecio-vermelding in de nulmeting; geen wijziging nodig |

De vier Malmö-producten VSB_2001–VSB_2004 zijn als proef omgezet en teruggelezen: vendor/titel/tags, vier menuvelden en zestien altwaarden correct. Publieke pagina's VSB_2001 en VSB_2004 tonen Verlavio in H1, JSON-LD Brand, menutitels en productafbeelding-alt. Kleur/Maat-menu's en bestaande product-URL's zijn aanwezig.

**Volledige eindcontrole PASS — 5 november 2026, 15:51:12 UTC.** Alle 861 producten hebben de geplande vendor, titel en merk-tag; alle 665 menuvelden en 1.665 altwaarden komen exact overeen met het uitvoerplan. Eindtelling: 861 Verlavio, nul Fabriecio. Alle bestaande product-ID's, handles, variant-ID's, SKU's, prijzen, voorraadaantallen/-beleid, omschrijvingen, SEO, leveringsvelden, media-ID's/-URL's en leveranciersbrontags zijn gelijk aan de nulmeting. Menuopbouw, opties en bestemmingen zijn behouden. Statusverdeling blijft 851 ACTIVE en 10 ARCHIVED; nul afwijkingen.

Behouden contract: product-ID's, variant-ID's, SKU's, handles/URL's, prijzen, voorraad, voorraadbeleid, status, media-ID's/-koppelingen/-bestands-URL's, omschrijvingen, SEO en leveringsdata. De statusverdeling blijft 851 ACTIVE / 10 ARCHIVED; gearchiveerde producten worden niet actief gemaakt. Interne `custom.fabriecio_choices`, `custom.fabriecio_delivery`, bron-SKU's en bron-/importtags blijven behouden. Bestaande `fabriecio-*`-URL's worden niet gemigreerd. Geen producten of varianten aangemaakt.

## Bewijs en testgrenzen

Vooraf: 18 Python-tests PASS; 16 merk-/productnavigaties PASS; 12 leveringsgevallen PASS. Alle 665 menu's onder vendor Verlavio: 5.425 keuzecontroles, 4.096 URL-wissels, nul fouten. Officiële Liquidcontrole van drie bestanden geldig met bestaande niet-blokkerende main-productwaarschuwingen. Publieke eindcontrole op 15:49:20 UTC: Malmö 170 cm wit (VSB_2001), Malmö 180 cm mat wit (VSB_2004) en Malaga hoge wastafelkraan mat zwart (BKK_1001) geven HTTP 200 met Verlavio in H1, JSON-LD Brand, alle keuzemenutitels en productafbeelding-alt. De menu's zijn aanwezig. Deze controle bewijst servermarkup; geen nieuwe fysieke telefoon-, cart-, checkout- of betalingstest.

Volledige brondata, plan, nulmeting en mutatiebonnen blijven in de privéaudit, niet in deze publieke Git-repository. Publieke documentatie bevat alleen de scope, totalen en bewijsgrenzen. Herstel gebruikt uitsluitend de oorspronkelijke vendor/titel/exacte merk-tag, menutitels en altwaarden uit die nulmeting; geen prijzen/voorraad of andere productdata terugschrijven. Metafieldwrites gebruiken `compareDigest`; een conflict vereist actuele herlezing.

## Open werk

De 53 producten met vastgehouden bronmenu’s blijven open. Het toenmalige Uitverkocht-probleem is later onderzocht en de Nederlandse Market-oorsprong is in FAB-04 hersteld; volledige controle en winkelwagenproef zijn daar vastgelegd. De merknaamwijziging zelf bewijst geen koopbaarheid. Automatische feedsynchronisatie is uitgesteld. Overige merken en het Lagoo-fotoverbod blijven buiten deze wijziging.

Verlavio ontbreekt nog in het bestaande merkenoverzicht, zoals Fabriecio daar vóór deze wijziging ook ontbrak. Dat is geen regressie van de rebrand; eventuele toevoeging vereist een afzonderlijke conceptthemawijziging.

**Exact één volgende handeling voor de rebrand:** geen verdere merkdatabatches uitvoeren; de rebrand is afgerond. Voor de vervolgvraag over voorraad en verzending geldt [FAB-04](../stock/README.md): de eigenaar publiceert het gecontroleerde concept **BadkamerCity - Verlavio voorraad en levertijd (196227170570)**. Automatische feedsynchronisatie blijft uitgesteld.
