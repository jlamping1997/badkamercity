# Hotbath: uitbreiding koppelingen inbouwdelen, 24 oktober 2026

**94 extra modellen / 460 extra webshopartikelen** hebben een onderbouwde, eenvoudige koppeling naar een bestaand verkoopbaar inbouwdeel. Dit is aanvullend op de eerder onderzochte31 modellen/208 artikelen, inclusief de voorbereide40-artikelenproef. Het eerdere totaal208 bevat nog vijf MHF-naamaliassen in review: tel het niet bij460 op als één volledig goedgekeurde uitrol.

**Status: gegevens onderzocht en gecontroleerd; Ja/Nee-functie niet gebouwd of geïnstalleerd.** Geen thema-, product-, prijs-, metafield-, voorraad- of winkelwagenwijziging uitgevoerd. MAIN is opnieuw vastgesteld als195649929482. Gitcodebranch blijft fix/product-cards-2026-10-14; geen lokale Windowscontrole, scratch is geen Gitcheckout.

## Bewijs en afbakening

Hotbath Catalogus Editie18, volledige boekscan in drie paginaonderdelen (gedrukt1–502). Iedere nieuwe betrokken relatietabel en expliciet gebruikte kleurcode is visueel gelezen. Een onafhankelijke controle bevestigt alle460 exacte SKU-relaties en inspecteert zes aanvullende representatieve bronpagina's. Alle460 nieuwe artikelen staan buiten de eerdere31-modelmapping. Dubbelen tussen boekhoofdstukken zijn verwijderd.

956 bestaande kandidaat-/inbouwproducten opnieuw uit Shopify uitgelezen: exacte product- en variantidentiteit, publicatiestatus, beschikbaarheid en eventuele inbegrepen-indicatie. Geen volledige nieuwe scan op tussentijds nieuw aangemaakte producten. De vijf ontbrekende doelcodes zijn aanvullend via een exacte actuele SKU-zoekopdracht gecontroleerd: nul resultaten, geen vervolgpagina. Verkoopbaarheid is geen fysieke voorraadbelofte.

De460 uitvoerregels bevatten echte variant-ID's en hoeveelheid1; geen vastgezette prijs. Alleen modellen en kleuren met expliciet bewijs zijn opgenomen. Inbegrepen=true, ontbrekende bodies, tegenstrijdigheden, extra montagekeuzes, IBS en SPOM zijn uitgesloten van deze normale kandidatenlijst.

## Belangrijkste uitzonderingen

| Geval | Bevinding / vervolg |
| --- | --- |
| CB7001EXT | HBCB7001H óf HBCB7001V; horizontaal/verticaal apart laten kiezen. Niet beide toevoegen. |
| AR001EXT / CB001EXT | HBCB001 ontbreekt in huidige webshop. |
| KHDS4EXT / KHDS5EXT | HBKHDS4 ontbreekt. KHDS5 was al een bekende uitzondering. |
| CB7069EXT | HBCB7069 ontbreekt. |
| GL7071EXT / GL7072EXT | HBGL7071 / HBGL7072 ontbreken. |
| GL177EXTBBP / BGP / CR | Boek bewijst HBCB177; webshop zegt inbouwdeel inbegrepen. Eerst leveringsinhoud/data controleren. AlleenGN is normale kandidaat. |
| GT7072EXT | Tabel HBCB7072, tekening HBGT7072: fabrikantverificatie nodig. |
| GY011DEXT | Tabel HBGY031; vergelijkbare Row-omstel gebruikt HBGY011. Verdachte relatie, geen bewezen correctie. |
| 27 Rails-modellen /264 artikelen | Inbouwdeel inbegrepen in setprijs maar apart bestellen; geen gewone betaalde extra. RASV135-3 heeft bovendien verkeerde tabelcode. |
| AR077EXT / AR187EXT | Bewezen SPOM525-relatie; buiten normale uitbreiding wegens eerdere SPOM-scope. Dit is geen ontkenning van compatibiliteit. |
| KHDS3EXTAI | p367 noemt AI niet; p176 bevestigt AI expliciet. Daarmee opgelost en opgenomen. |

177 overige artikelen met EXT/afbouw-/afdeksetsignaal hebben nog geen exacte relatie binnen deze mapping. Sommige kunnen oude codes of afwijkende modellen zijn. Hun aanwezigheid bewijst niet dat allemaal een nieuwe betaalde keuzemogelijkheid nodig hebben. Zie de expliciete restlijst; geen passende body gegokt.

## Bestanden

- [Exacte460 extra variantkoppelingen](expansion-ready-variants.json)
- [Gecombineerde bronlijst, opmerkingen en uitzonderingen](expansion-consolidated.json)
- [Nog niet exact gekoppelde177 kandidaten](expansion-unresolved-articles.json)
- [Onafhankelijke controle](expansion-independent-review.json)
- [Verse Shopify-kandidaatuitlezing](expansion-live-products.json)
- [Actuele zoekcontrole ontbrekende bodies](expansion-missing-bodies-final.json)
- Bronsegmenten: [A](expansion-a.json), [B](expansion-b.json), [C](expansion-c.json).

`merge_expansion.py` bouwt gecombineerde gegevens opnieuw uit deze bestanden en de eerder opgeslagen book_mapping_review.json; wanneer de oorspronkelijke catalogussnapshot ontbreekt gebruikt het script de vastgelegde exacte kandidaatcodes. De drie extractiescripts vereisen daarnaast de oorspronkelijkePDF/catalogussnapshot. Het volledige boek wordt niet in deze publieke repository gekopieerd; bronbestand Hotbath%20Catalogus%20Editie%2018.pdf is aangeleverd door eigenaar.

**Volgende handeling:** eerst de bestaande40-artikelenproef als Ja/Nee-functie bouwen in een identieke ongepubliceerde kopie van huidigeMAIN. Daarna deze460 gecontroleerde extra varianten via dezelfde functie aansluiten. Identiteit, prijs en beschikbaarheid bij uitvoering opnieuw lezen; cart-/mobiel-/checkoutgedrag is in deze onderzoeksronde niet getest.

## Alle94 nieuwe eenvoudige modelkoppelingen

| Afbouwmodel | Inbouwdeel | Gedrukte pagina | Artikelen |
| --- | --- | --- | ---: |
| AC071EXT | HBAC071 | 309 | 6 |
| AC072EXT | HBAC072 | 309 | 6 |
| AC105EXT | HBCB105 | 300 | 6 |
| AC111EXT | HBCB111 | 306 | 6 |
| AC129EXT | HBCB129 | 307 | 6 |
| AC131EXT | HBCB131 | 306 | 6 |
| AR091EXT | HBAR091 | 89 | 1 |
| AR7070EXT | HBCB7070 | 82 | 4 |
| AR7171EXT | HBCB7071 | 82 | 4 |
| AR7172EXT | HBCB7072 | 83 | 4 |
| ARHF011 | MHF001 | 86, 360 | 4 |
| ARHF012 | MHF002 | 86, 360 | 4 |
| ARHF013 | MHF003 | 86, 360 | 4 |
| B105EXT18 | HBCB105 | 275 | 4 |
| B105EXT22 | HBCB105 | 275 | 4 |
| B111EXT | HBCB111 | 281 | 4 |
| B131EXT | HBCB131 | 281 | 4 |
| B177EXT | HBCB177 | 283 | 4 |
| C105TEXT | HBCB105T | 109 | 2 |
| C7009EXT | HBCB7009 | 112 | 3 |
| C7067EXT | HBCB7067 | 112 | 2 |
| C7070EXT | HBCB7070 | 113 | 2 |
| C7071EXT | HBCB7071 | 114 | 2 |
| C7072EXT | HBCB7072 | 114 | 2 |
| CB111EXT | HBCB111 | 183 | 10 |
| CB127EXT | HBCB105 | 184 | 9 |
| CB129EXT | HBCB129 | 183 | 10 |
| CB131EXT | HBCB131 | 182 | 10 |
| CB178WEXT | HBCB177 | 169 | 9 |
| CB7068EXT | HBCB7068 | 191, 283 | 10 |
| CB7070EXT | HBCB7070 | 188 | 10 |
| CB7080EXT | HBCB7080 | 192 | 10 |
| CB7083EXT | HBCB7083 | 192 | 10 |
| CB7171EXT | HBCB7071 | 189 | 9 |
| CB7172EXT | HBCB7072 | 189 | 9 |
| CW005TEXT18 | HBCW005T | 230 | 3 |
| CW005TEXT25 | HBCW005T | 230 | 3 |
| CW011EXT | HBCB011 | 232 | 3 |
| CW7067EXT | HBCB7067 | 234 | 3 |
| CW7171EXT | HBCB7071 | 234 | 2 |
| CW7172EXT | HBCB7072 | 235 | 2 |
| CX105EXT18 | HBCB105 | 214 | 7 |
| CX105EXT25 | HBCB105 | 214 | 7 |
| CX111EXT | HBCB111 | 220 | 7 |
| CX127EXT | HBCB105 | 221 | 6 |
| CX131EXT | HBCB131 | 220 | 7 |
| CX178WEXT | HBCB177 | 215 | 6 |
| CX187EXT | HBCB177 | 221 | 7 |
| CX7067EXT | HBCB7067 | 223 | 7 |
| CX7171EXT | HBCB7071 | 222 | 6 |
| CX7172EXT | HBCB7072 | 222 | 6 |
| GL005EXT | HBGL005 | 244 | 3 |
| GL009EXT | MB009 | 250 | 4 |
| GL031EXT | HBGL031 | 250 | 4 |
| GL177EXT | HBCB177 | 249 | 1 |
| GL7009EXT | HBCB7009 | 252 | 4 |
| GL7067EXT | HBCB7067 | 252 | 3 |
| GT105EXT | HBCB105 | 30 | 1 |
| GT105TEXT | HBCB105T | 30 | 1 |
| GT111EXT | HBCB111 | 32 | 1 |
| GT129EXT | HBCB129 | 33 | 1 |
| GT131EXT | HBCB131 | 32 | 1 |
| GT187EXT | HBCB177 | 35 | 1 |
| GT7009EXT | HBCB7009 | 36 | 1 |
| GT7067EXT | HBCB7067 | 36 | 1 |
| GT7070EXT | HBCB7070 | 37 | 1 |
| GT7071EXT | HBCB7071 | 37 | 1 |
| GY005DEXT20 | HBGY031 | 127 | 4 |
| GY005DEXT25 | HBGY031 | 127 | 4 |
| GY005REXT20 | HBGY031 | 145 | 4 |
| GY005REXT25 | HBGY031 | 145 | 4 |
| GY011REXT | HBGY011 | 148 | 4 |
| GY031DEXT | HBGY031 | 130 | 4 |
| GY031REXT | HBGY031 | 148 | 4 |
| GY177DEXT | HBGY177 | 132 | 4 |
| GY177REXT | HBGY177 | 150 | 4 |
| GY7009DEXT | HBCB7009 | 133 | 4 |
| GY7009REXT | HBCB7009 | 151 | 4 |
| GY7067DEXT | HBCB7067 | 133 | 4 |
| GY7067REXT | HBCB7067 | 151 | 4 |
| GY7070DEXT | HBCB7070 | 134 | 4 |
| GY7070REXT | HBCB7070 | 152 | 4 |
| GY7071DEXT | HBCB7071 | 134 | 4 |
| GY7071REXT | HBCB7071 | 152 | 4 |
| GY7072DEXT | HBCB7072 | 135 | 4 |
| GY7072REXT | HBCB7072 | 153 | 4 |
| KHDS3EXT | HBKHDS3 | 176, 304, 367 | 10 |
| PB009EXT | HBPB009 | 196 | 10 |
| PB009QEXT | HBPB009 | 196 | 10 |
| PB050EXT | HBPB050 | 197 | 10 |
| PB066EXT | HBPB066 | 197 | 10 |
| PB7009EXT | HBPB7009 | 198 | 10 |
| PB7039EXT | HBPB7039 | 198 | 10 |
| PB7071EXT | HBPB7071 | 253 | 3 |
