# JEE-O kleurkeuze — 3 november 2026

Status: **LIVE_THEME_CONFIRMED / DESKTOP_PREVIEW_TESTED**.

Actuele controle3november2026: thema196110090506 is nu MAIN; alle24featurefiles exact gelijk aan de eerder geteste implementatie. Actuele Git-bron staat in shopify/current/ op de bestaande codebranch. De publicatieblokkade en opdracht tot publiceren hieronder beschrijven het eerdere implementatiemoment, niet een nog open publicatie. [Nieuwe Git-broncontrole](../git-sync/2026-11-03/README.md).

## Opdracht en resultaat

De eigenaar heeft kleurbolletjes zoals Hotbath goedgekeurd voor JEE-O op productpagina’s en productkaarten. Alle65goedgekeurde modelfamilies/228producten gekoppeld. De273eerder verbeterde titels behouden. Eén SWMBAS71-groep/2producten uitgesloten vanwege conflicterende fabrikantcode;43producten zonder bestaande kleurtegenhanger blijven los. De8fabrikantbevestigde en57catalogusgevalideerde groepen blijven onderscheiden in de privéwerkset.

Er zijn456metafields aangemaakt: custom.color_variants (bestaande list.product_reference) en custom.kleur (bestaande single_line_text_field). Alle groepsleden krijgen dezelfde geordende lijst inclusief zichzelf. Eerst15proefproducten, daarna20atomaire batches met213producten. Per batch verse voorcontrole, create-only compareDigest:null en exacte readback. Geen blind overschrijven van bestaande waarden.

Volledige eindinventaris273/273:228correct gekoppeld/45ongemoeid, nul titel-/handleafwijkingen en nul onverwachte wijzigingen in vergeleken velden: ID, vendor, status, productType, templateSuffix, onlineStoreUrl en alle beschikbare varianten met ID/SKU/prijs/inventoryQuantity. Geen nieuwe producten of wijzigingen aan SEO, beschrijvingen of media aangevraagd.

## Thema en code

Bron MAIN196052189450 bleef ongewijzigd:1356files. themeDuplicate maakte UNPUBLISHED196110090506 **BadkamerCity - JEE-O kleurkeuzes**. Asynchrone kopie eerst volledig laten afronden; vóór elke featurewrite1356/1356checksumpariteit bewezen.

Finaal1374files: exact6bestaande paden gewijzigd en18nieuwe, alle24checksums exact teruggelezen, geen onverwachte of ontbrekende paden. [Bestandscontract en checksums](JEEO_COLOURS_THEME_FILES_2026-11-03.json). Codecheckpoint e249975fc43c1666a7e740254b4134de1226fcd2, bestaande branch fix/product-cards-2026-10-14.

Git-root was geen actuele themasnapshot. De zes bestaande featurefiles zijn eerst vers uit MAIN gelezen. Een groot Git-diff bevat daarom ook synchronisatie van eerder bestaande livecode. Eigen wijziging in main-product is uitsluitend de JEE-O-elsif/render van twee regels. Upload nooit de hele Git-root. MAIN-rollen uit oudere NAV-03-dossiers zijn historie.

## Gemeenschappelijk kleurcontract

bc-jeeo-colors valideert JEE-O, gelijk producttype, gelijke SKU-modelcode, wederkerig groepsanker, unieke kleuren en aanwezigheid van huidig product. Numeric SKU met acht tekens: eerste zeven vormen model; overige SKU’s gebruiken code vóór eerste koppelteken. Alleen expliciete referenties leveren keuzes. Kleurwissel behoudt maat/model.

PDP gebruikt de bestaande V2-navigatie met onveranderde Hotbath/Wiesbaden-CSS en vijftien eigen SVG-afwerkingen. Vier zichtbare kleuren met Bekijk alle kleuren; actieve kleur blijft zichtbaar. Kleurwissel opent het bestaande product met eigen foto, prijs en winkelwagenvariant. Geen nieuwe variantstructuur gemaakt.

Externe kaarten gebruiken dezelfde groep en wisselen kleur, foto, titel, prijs en links samen. De SVG-origin/CDN- en protocolcontroles blijven gelden; JEE-O gericht toegevoegd naast Wiesbaden. Alleen gekoppelde JEE-O-producten krijgen custom.kleur-voorrang op filtermanifest. Afwerking niet dubbel in externe kaarttitel en kleurregel.

Native zoek- en collectiekaarten gebruiken mode:card van dezelfde adapter. Ronde links naar elke bestaande kleuruitvoering, bruikbaar zonder JavaScript; geen geneste anchors in zoekkaarten. Native specs tonen de canonieke kleur. Andere merken en externe index/filteractivatie niet gewijzigd.

## Verificatie

- Theme Check: oorspronkelijke20featurefiles revisie3 geldig; native uitbreiding vijf nieuwe/gewijzigde files revisie1 geldig. Bestaande bronwaarschuwingen behouden. Eerste twee runs misten huidige MAIN-afhankelijkheden in de oude Git-checkout; uitsluitend tijdelijke validatiekopie aangevuld.
- Node syntaxcheck externe kaart-JavaScript en XML-parse van15SVG’s PASS.
- Vijftien Slimline-plafondarmen (15/25/35cm) plus veertien extra Soho/Flow/Bloom-uitvoeringen:29PDP’s en29kaartdataresponses HTTP200, exacte groep/volgorde/kleur/H1/winkelwagenvariant/kaartidentiteit/prijs. Inclusief SKU zonder kleursuffix en zes afwerkingen.
- Echte Cloud Chrome1363×936: RVS→Mat goud→Brons behoudt15cm/model; juiste H1/SKU/foto; vijfkleuruitbreiding en selectie hersteld. Externe kaart Mat goud→RVS wisselt foto/kleur/alle productlinks; titel bevat kleur niet dubbel.
- Prijsverschil daadwerkelijk getest op externe kaart701-002: RAW RVS200,00→Hammercoat zwart mat248,00 met juiste selectie/link.
- Native zoekkaart: twee ronde links, correcte actieve kleur, canonieke kleurtekst, nul geneste anchors; desktopbreedte280px zonder interne overloop. Native collectieHTTP200 met16kleurrijen/88links; bron bevat standaardkaart-renderer.
- Laatste PDP na native uitbreiding opnieuw geladen: kleurbediening correct aanwezig.

Geen echte cart-,wishlist-,order- of checkoutactie. Geen fysieke telefoon, touch-hardware, Windows, volledige andere-merkenregressie, performance- of zoekindexvrijgave. Mobiele componentcontrole niet uitgevoerd: lokale file-URL door browserveiligheidsbeleid geweigerd; geen alternatieve route gebruikt. Eigenaar controleert telefoon vóór publicatie.

Zoekobservatie: volledige nieuwe frase JEE-O slimline plafondarm gaf0resultaten; SKU-prefix801-681 gaf5correcte kaarten. Oorzaak niet vastgesteld; externe index niet aangepast. Dit blijft een afzonderlijk aandachtspunt voor verdere dataversterking.

## Publicatie en herstel

themePublish geweigerd door veiligheidsbeleid setup-mcp: publiceren van thema’s is hier geblokkeerd. Geen dedicated theme_publish-tool beschikbaar; geen browseromweg. Concept blijft UNPUBLISHED; huidige MAIN behouden. Geen actieve schrijver na afronding.

Volledige productvooropname, canonieke groep-ID’s, digests, writes en readbacks privé bewaard. Alleen custom.color_variants/custom.kleur uit eigen receipts herstellen; oorspronkelijk leeg. Eerst actuele digests vergelijken om latere wijzigingen te behouden. Geen producttitels terugzetten voor deze kleurwijziging.

Themaherstel: huidige MAIN196052189450 behouden, of indien eigenaar later publiceert dat vorige thema terug publiceren. Voor afzonderlijke codeherstel zes bronfiles uit vorige MAIN gebruiken en18nieuwe featurefiles weghalen. Voor publicatie hoeft geen thema verwijderd te worden.

Volgende handeling: eigenaar opent Webshop→Thema’s→**BadkamerCity - JEE-O kleurkeuzes**→Voorbeeld, controleert telefoon en publiceert zelf. Code en actuele status op GitHub opgeslagen; geen Windows-controle geclaimd.
