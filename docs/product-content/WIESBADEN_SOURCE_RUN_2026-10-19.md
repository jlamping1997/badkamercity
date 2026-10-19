# Wiesbaden bronrun — 19 oktober 2026

## Opdracht en actuele fase

Eigenaar vraagt nu eerst het volledige fabrikantassortiment te verzamelen, inclusief producten die nog niet in BadkamerCity staan. Daarna gecontroleerd toepassen voor specificaties, categorieën, breadcrumbs, filters, eigen content en prijzen. EAN wordt geen koppelsleutel en komt niet in nieuwe klantteksten.

Status: **IN_PROGRESS — volledige HTML-aanvulling loopt**. Bestaande werkbranch: `fix/product-cards-2026-10-14`. Uitvoering in ChatGPT/Linux; Windows-werkmap en lokale PowerShell-wrappers niet gecontroleerd. Geen Shopify-mutaties in deze run.

## Bewezen bronontdekking

- Homepage rechtstreeks opgehaald op `https://www.wiesbaden.nl/`; in deze sessie was alleen de eerdere product-HTML als bijlage aanwezig.
- De gebruikelijke `/sitemap.xml` en `/sitemap_index.xml` geven 404. Geen niet-bestaande sitemap als bron gebruiken.
- Het HTML-hoofdassortiment meldt **1.857** producten. De openbare fabrikant-GraphQL-interface meldt **2.841** producten. Daarom niet alleen de homepage of de zichtbare assortimentlijst volgen.
- Openbare interface met introspectie gecontroleerd. Alle **29 pagina's van 100** op SKU gesorteerd gelezen; 2.841 unieke product-UID's, gelijk aan gedeclareerde telling. Bron is de publieke websitecatalogus, geen leveranciersvoorraad- of inkoopfeed.
- Opgehaald: identiteit, brontitel, bronbeschrijving, bronprijs, categorieën en volledige categorie-breadcrumbs. **173** verschillende broncategorieën.
- Attribuutmetadata: **907** attributen; gefilterde bronmetadata: **860** attributen. Dit zijn brondefinities/opties, geen opdracht om 860 winkelfilters te activeren.
- `custom_attributesV2` geeft bij het gecontroleerde artikel een interne bronfout. Daarom worden daadwerkelijke specificatiewaarden, Compano-afbeeldingen, lijntekeningen en handleidinglinks uit iedere product-HTML gehaald. GraphQL-beeldvelden bevatten bij de proef een placeholder en zijn geen bewijs van bruikbare productfoto's.

## Actuele winkelvergelijking

- Verbonden winkel BadkamerCity bevestigd. Verse MAIN-read: **195392143626 — BadkamerCity - Winkelwagen helder**. Dit is alleen een waarneming; geen themawrite/publicatie.
- Alle **2.265** Wiesbaden-producten gelezen, met titels, omschrijvingen, ID's, SKU's, actuele prijzen, producttypen en collecties. Alle product-, variant- en collectiepaginering compleet. ACTIVE en niet-lege onlineStoreUrl voor deze 2.265 waargenomen; geen afzonderlijke HTTP-controle van elke product-URL.
- **11.157** varianten uit de hele winkel gelezen voor een complete SKU-index, inclusief andere merken. Nieuwe kandidaten dus niet alleen uit een merkzoekresultaat afgeleid.
- **2.240** fabrikant-SKU's bestaan als Wiesbaden-product; **601** komen niet voor in de volledige winkel-SKU-index; **25** bestaande Wiesbaden-SKU's niet teruggevonden in deze fabrikantmomentopname.
- Geen automatische verwijdering, archivering of nieuwe publicatie. Nieuwe kandidaat is nog geen publicatieklaar product. Exacte bronmerkidentiteit, ontbrekende feiten en set-/onderdeelstatus blijven controles.
- Actuele structuur gelezen: **221** collecties, **9** menu's en **246** productmetafielddefinities. De verschillende `custom`, `specs`, `bc_filters` en overige namespaces mogen niet stil samengevoegd worden.

## Prijscontrole — aangevulde btw-context

Voor 24.3710: actuele winkelprijs **252,89 EUR**; fabrikant-API en gelabelde HTML-adviesprijs beide **209,00 EUR**. Aanvullende inspectie toont dat de actieve fabrikantprijscomponent `regularPriceExclTaxKey` en `finalPriceExclTaxKey` selecteert bij `initialFinalPrice: 209`. Dit is expliciete technische broncontext: de weergegeven fabrikantprijs gebruikt de exclusief-btw-prijscomponent. Shopify `shop.taxesIncluded` is vers als **true** teruggelezen. Bij de bestaande winkelconventie van factor 1,21 sluiten de twee bedragen aan. Het ruwe verschil mag dus niet als bewezen prijsfout of korting worden behandeld.

De btw-component wordt over alle bronpagina's gecontroleerd en bij de bronhash opgeslagen. De uitvoer krijgt naast de ruwe vergelijking een afzonderlijk btw-genormaliseerd prijsvoorstel, met factor 1,21 expliciet als waargenomen bestaande winkelconventie. Geen factuur-/inkoopprijsverificatie geclaimd en geen verkoopprijzen gewijzigd. Alle **36** bronartikelen met nulprijs ontbreken in de winkel en krijgen een reviewblokkade; geen gratis producten aanmaken.

## Doelkoppeling — alleen voorstel

De verse momentopname van alle 2.265 Wiesbaden-productmetafields bevestigt dat Wiesbaden de **custom**-namespace gebruikt. `specs` behoort tot de andere merkmapping. Er zijn 49 bestaande custom-definities en 62 bc_filters-definities. De scriptvoorstellen gebruiken bestaande veldtypen en collection-ID's; geen honderden nieuwe definities aanmaken.

- `scripts/wiesbaden-import-plan.py` koppelt bronpaden en expliciete productnamen aan bestaande collecties en echte menupaden. Voor 24.3710: Kranen → Wastafelkranen → Opbouw wastafelkranen, met lidmaatschap van alle drie collecties. Afbouwdelen, inbouwdelen, fonteinsets en andere sets krijgen afzonderlijke regels; one-pack is geen synoniem voor fonteinset.
- Bronproducten zonder categorie, onduidelijke toepassingen en ontbrekende doelcollecties blijven expliciet in review. De bron kent 978 artikelen zonder categorie; alleen een globale navigatieboom is dus onvoldoende voor classificatie.
- Voorstel voor alle tabelwaarden in het reeds gedefinieerde `custom.complete_specificaties` JSON-formaat. De actuele Wiesbaden-renderer leest dit volledige JSON-veld nog niet; route eerst in concept valideren. De bestaande Hotbath-afscherming niet verruimen om dit te forceren.
- Losse custom-veldvoorstellen en filterveldvoorstellen behouden bronwaarde, huidige waarde, voorgesteld type en wijzigingsstatus. Nee blijft false; nul blijft nul; een ontbrekende maat of eenheid wordt niet ingevuld. Generieke waarden zoals Overig vervangen geen specifiek bestaand materiaal.
- `bc_data.filter_manifest` en de externe VPS-index vereisen een gecontroleerde contract-/indexstap. Alleen een metafield vullen bewijst niet dat zoeken/filteren is bijgewerkt. Geen indexverversing of live filtertest geclaimd.

## Extractieproef en tests

- Bestaande tien proefartikelen 20.3755, 20.3756, 32.3411, 32.3594, 32.2510, 32.3670, 38.4125, 41.3540, 24.3710 en 29.8007 alle gevonden en uit echte fabrikant-HTML geëxtraheerd.
- Exacte paginatype/SKU-controle, specificaties, afbeeldingen en aanwezige documenten gelezen; nul extractiefouten in deze proef. Dit is geen inhoudelijke goedkeuring van alle feiten: 32.3594 heeft bijvoorbeeld slechts drie tabelvelden.
- **28 uitvoerbare regressietests geslaagd:** 13 bron-/prijs-/identiteitstests en 15 doelmappingtests. Inclusief SKU-mismatch, behoud leading zeroes/punctuatie, EAN uitsluiten, leeg versus Nee, breadcrumbs, mediaklassen, bronhost, onvolledige inventaris, daadwerkelijke btw-component versus generieke tax-helper, geen dubbele btw, nulprijsblokkade, onderdelen/sets, hoofdproduct versus meegeleverd product, expliciete eenheden, conflicterende filteraliassen en behoud van huidige waarden.
- Bekende UTF-8/euro-extractiefout in de eerste synthetische proef gecorrigeerd; tests daarna geslaagd. Actuele parserversie `2026-10-19.2`.

## Uitvoering en opslag

Collector: `scripts/wiesbaden-data-run.py`; tests: `scripts/test_wiesbaden_data_run.py`. Alleen-lezen collector; bevat geen Shopify-mutaties of credentials. Gebruik een afgeschermde runmap **buiten** deze publieke Git-repository.

```sh
python scripts/wiesbaden-data-run.py catalogue --run-dir /private/run-directory
python scripts/wiesbaden-data-run.py pages --run-dir /private/run-directory --workers 8
python scripts/wiesbaden-data-run.py build --run-dir /private/run-directory
```

De build vereist een complete actuele Shopify-snapshot en volledige winkel-SKU-index; hij kan die niet uit de themarepository reconstrueren. Ruwe HTML, bronbeschrijvingen, herstelkopieën en volledige winkeldata niet naar deze publieke repository pushen.

Iedere bronrequest bewaart URL, UTC-moment, responsehash en gecomprimeerde bronbytes. Productbestanden hebben bron-SKU, bron-UID, metadata, raw en EAN-vrije specificatielijst, bronomschrijving, mediaverwijzingen, prijsvergelijking en issues. Onderbroken paginaruns hervatten op de parserversie; reeds opgeslagen bronbytes worden met SHA-256 gecontroleerd.

Beoogde uitvoer: volledige broncatalogus; nieuwe kandidaten; bestaande artikelen; bestaande artikelen zonder bronmatch; prijsverschillen; broncategorieën en specificatievelden. Alles heeft `NOT_APPLIED`/reviewstatus. Een bronfilter of broncategorie is niet automatisch dezelfde betekenis als een doelveld of collectie.

## Nog uit te voeren

1. Volledige HTML-aanvulling en datakwaliteitscontrole afronden; foutpagina's gericht opnieuw proberen.
2. Doelcategorieën/onderdelen/complete sets en relevante filtervelden koppelen aan de verse winkelstructuur. Geen ontbrekende maten, setinhoud, keurmerken of voorraad/levertijd verzinnen.
3. Doelveldtypen en werkelijk gebruikt PDP-/zoek-/filtercontract verifiëren; consistente eenheden en leegstaten bewaren.
4. Eigen productcontent en prijsvoorstellen ter beoordeling klaarmaken; bronmateriaal is geen kant-en-klare eigen webshoptekst.
5. Afgebakende winkelverwerking met verse wijzigingscontrole, herstelkopie en read-after-write. Deze broncollector zelf wijzigt de winkel nooit.

**Exact één volgende handeling:** de lopende volledige HTML-aanvulling afronden en de ontbrekende/afwijkende records rapporteren.
