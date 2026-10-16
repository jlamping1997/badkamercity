# Productteksten per merk — uitvoeringsplan
Datum: 16 oktober 2026 (Europe/Amsterdam).
Onderdeel van BC-02; vaste projectingang blijft LIVE_STATUS_AND_NEXT_STEPS.md.
Opdracht: bestaande productgegevens combineren met gecontroleerde externe bronnen, eigen duidelijke productteksten maken en voortgang per merk/product in Git bijhouden.

## Eerste uitvoeringsronde
Wiesbaden: proef met 10 werkelijk aanwezige producten, verdeeld over verschillende producttypen en minstens één groep kleur-/maatvarianten. Exacte selectie volgt na een actuele read-only Shopify-inventaris. Geen aantallen of artikelcodes uit oude chats als actuele waarheid gebruiken.
Doel: aantonen dat matching, bronkwaliteit, schrijfstijl en relevante interne links werken vóór merkbrede verwerking.

## Stappen en eindcriteria
1. Inventariseren: merk, Shopify product-/variant-ID, SKU/fabrikantnummer, handle, titel, huidige omschrijving, categorie, specificaties en beschikbare documenten uitlezen. Huidige tekst apart bewaren voor vergelijking/herstel. Geen EAN als koppelsleutel.
2. Koppelen: merk + exact fabrikantnummer als kandidaat; eerst ontbrekende/dubbele SKU's en variantidentiteit controleren. Titels of foto's alleen zijn onvoldoende. Ambigue matches blokkeren.
3. Bronnen testen: fabrikant/leverancier eerst; maximaal enkele relevante webshops als aanvullende bron. Voorbeelden BadkamerXXL, Sanitairwinkel en Tegeldepot zijn kandidaten, geen reeds geteste scrapers. Per bron eerst dezelfde kleine productselectie proberen. Bestaande feeds, exports, API's of productdata gebruiken als die eenvoudiger en betrouwbaarder zijn.
4. Bewijs samenvoegen: per eigenschap waarde, eenheid, exacte bron-URL, datum en bevestigingsniveau vastleggen. Conflicten niet automatisch oplossen op meerderheid; fabrikantdocumentatie voor het exacte artikel heeft voorrang, actuele inconsistenties apart controleren.
5. Eigen concepttekst: korte uitleg, toepasselijke voordelen op basis van feiten, aandachtspunten en bevestigde meegeleverde/benodigde onderdelen. Lengte volgt informatiebehoefte. Geen gekopieerde concurrententeksten, keywordstapeling, loze claims of uitgevonden garantie/voorraad/levertijd.
6. Interne links: normaal 0–2 zinvolle contextlinks, geen SEO-quotum. Bij voorkeur de juiste concrete categorie (bijvoorbeeld opbouw wastafelkranen). Alleen bestaande, passende en bereikbare bestemmingen; geen verzonnen collectiehandles of ongeteste compatibiliteitslinks.
7. Proefreview: per product huidige tekst, nieuwe tekst, bronnen, interne links en open vragen naast elkaar beoordelen. Eigenaar beoordeelt schrijfstijl en bruikbaarheid.
8. Opschalen: pas na geslaagde proef dezelfde regels per productfamilie uitbreiden. Verschillen tussen kleur-/maatvarianten feitelijk behouden; geen kunstmatige woordvariatie om teksten anders te laten lijken.

## Voortgang per product
Maak na inventarisatie een machineleesbaar register met:
merk; product_id; variant_id; sku; handle; productfamilie; huidige_tekst_status; actie; workflowstatus; bronverwijzingen; conflicten; linkdoelen; versie_input; versie_tekst; controledatum; publicatiedatum; foutmelding.
Actie: behouden / verbeteren / nieuw schrijven / onderzoeken.
Workflowstatus: nog_bekijken / gegevens_compleet / concept / gecontroleerd / geplaatst.
Gebruik fout-/blokkadevelden naast de status; overschrijf niet stil een eerder goedgekeurde versie.

## Voortgang per merk
| Merk | Stand | Proef | Volgende handeling |
| --- | --- | --- | --- |
| Wiesbaden | 2.265 identifiers geïnventariseerd; 50 omschrijvingen steekproef; 10 in detail beoordeeld | [Selectie en bevindingen](product-content/WIESBADEN_PILOT.md); [productregister](product-content/wiesbaden-register.json) | Bronnen testen op 24.3710, 32.3594 en 32.3670 |
| Overige merken | Nog niet geïnventariseerd | Niet gestart | Na Wiesbaden-proef volgorde bepalen uit werkelijke catalogus |

Merklijst en aantallen worden uit de actuele catalogus afgeleid, niet uit historische aantallen.

## Opslag en hervatten
- Git: plan, schrijfregels, bronconfiguratie zonder secrets, openbare eigen teksten en product-/merkstatus.
- Deze repository is publiek. Volledige externe webpagina's, teksten van derden, vertrouwelijke leveranciersfeeds, inkoopinformatie en credentials niet committen. Alleen benodigde feitelijke gegevens en bronverwijzingen na inhouds-/rechtencontrole.
- Ruwe bronbestanden en herstelkopieën in passende afgeschermde opslag; registreer uitsluitend een veilige verwijzing en checksum in Git.
- Per batch inputversie en datum bewaren; ongewijzigde goedgekeurde artikelen overslaan. Hervat op status, niet telkens vanaf nul.
- Shopify blijft actuele winkelbron; Git registreert wat gecontroleerd en verwerkt is.
- Publiceren is een afzonderlijke opdracht met afgebakende scope, back-up, controle op tussentijdse wijzigingen, read-after-write en herstelpad. Huidige opdracht schrijft geen productteksten naar Shopify.

## Controle van de proef
Geslaagd wanneer 10 matches uniek en traceerbaar zijn; elke concrete claim onderbouwd is; conflicten verklaard of geblokkeerd zijn; categorie-links inhoudelijk en technisch kloppen; productteksten geen bestaande technische HTML beschadigen; eigenaar de stijl beoordeeld heeft.
Ranking/conversiewinst is niet bewezen door tekstproductie en wordt niet beloofd.

## Checkpoint 16 oktober 2026
Uitvoerder: ChatGPT via GitHub-connector. Bestaande werklijn: fix/product-cards-2026-10-14. Deze stap betreft uitsluitend documentatie; geen thema- of productmutaties.
VERIFIED_GIT: repository en bestaande overdracht gelezen; catalogus/importtools staan niet compleet in themarepository.
NOT_TESTED: actuele Shopify-merkdekking, 10-productselectie, bronextractie, teksten en linkcontrole. Geen toegang tot Windows-werkmap gecontroleerd.
Volgende handeling: actuele Wiesbaden-productdata alleen-lezen inventariseren en 10 proefproducten vastleggen.

## Vervolgcheckpoint — inventarisatie uitgevoerd 16 oktober
VERIFIED_ADMIN: exact 2.265 Wiesbaden-producten; volledige identifier-/variantlijst opgehaald. Tien geselecteerde SKU's elk uniek in deze merkcatalogus; omschrijving, metafields en collecties uitgelezen. Register bevat alle 2.265 producten en markeert 10 proefproducten; 2.255 teksten nog niet beoordeeld. Bevindingen: EAN in alle 10 proefomschrijvingen, maatconflict 32.3670, dunne setinformatie 32.3594 en meerdere onbruikbare meta-omschrijvingen. Zie proefrapport. MAIN nu 195313991946; nul winkelmutaties.
NOT_TESTED: externe bronmatching, publieke linkroutes, nieuwe teksten en ranking. Volgende handeling: bronextractie testen voor 24.3710, 32.3594 en 32.3670.
