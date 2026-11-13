# Keuzematch en fallback — losse beslissingen

Hoofdcontract: [productkeuzes](../PRODUCT_CHOICES.md). Dit dossier maakt onderscheid tussen bron laden, bron begrijpen en een exacte uitvoering aanwijzen. Bewijs: V2-01 t/m V2-03 en [catalog-validation.json](../../evidence/2026-10-28-micro/catalog-validation.json).

## Matchfunctie

| Functie | Regel | Gevolg |
| --- | --- | --- |
| getMenus | Alleen menus met key; sorteer op order | De menus bepalen welke velden bij een exacte match meetellen |
| getProducts | Kopie en sortering op sort_order | Sorteervolgorde is geen bewijs van prioriteit bij ambiguïteit |
| getValuesForMenu | Expliciete menu.values, anders afleiden uit producten | De bron kan de zichtbare volgorde vastleggen |
| hasPartialMatch | Alle niet-lege geselecteerde waarden moeten bij minstens één product passen | Bepaalt of een individuele keuze nog mogelijk is |
| findExactMatch, :266 | Alle menuvelden gelijk; precies één match | 0 of >1 geeft undefined, geen willekeurige eerste productkeuze |
| getDisplayType, :273 | Expliciete buttons/dropdown, anders grens vijf/zes | Alleen het niet-compacte pad gebruikt deze beslissing voor een dropdown |

V2-01 bevestigt één unieke match, afwijzing van geen/ambigue matches en vijf buttons versus zes dropdownwaarden. Hiervoor worden alleen de private pure helpers in een sandboxcopy toegankelijk gemaakt; de code van die functies blijft gelijk. Dit is geen native-select-/keyboardtest.

Een mogelijke deelmatch bewijst geen unieke volledige match. Bij dubbele volledige records kan een control nog een passende waarde hebben terwijl de uiteindelijke navigatie wordt geweigerd. De dataset moet daarom niet alleen unieke group-ID's, maar ook unieke gekozen combinaties waarborgen. De constructor blokkeert ontbrekende menus/currentProduct en te kleine groepen; de URL-guard controleert daarna ook origin, productpad en handle.

## Laadfallback is geen semantische fallback

loadSwitcherData:206 cachet per primaire URL een promise. Een fetch-/JSON-parsefout kan de afwijkende fallback-URL laden. Een succesvolle JSON-parse gaat rechtstreeks naar de constructor.

| Stimulus | Werkelijke gecontroleerde uitkomst |
| --- | --- |
| Primaire fetch faalt, fallback geldig | Beide URL's in volgorde opgevraagd; keuze wordt gerenderd — V2-03 |
| Primaire JSON geldig maar groups leeg | Alleen primary gevraagd; switcher verborgen — V2-02 |

De tweede uitkomst is **BOUNDARY_CONFIRMED**, geen bewijs dat de echte huidige dataset kapot is. Het is ook geen terugval naar de native Liquid-variantpicker: de server heeft eerder al een andere tak gerenderd. Wil men semantische terugval, dan moet expliciet worden bepaald welke validatiefouten dat veroorzaken en hoe dezelfde currentProduct/groep wordt gecontroleerd. Een catch toevoegen rond alleen JSON.parse lost ontbrekende groepen niet op.

Bij wijziging ook de promise-cache onderzoeken: een geldige maar ongeschikte dataset is een andere toestand dan een afgewezen fetchpromise. “We hebben een fallback” is daarom te algemeen als onderhoudsinstructie. Zie [datapijplijnen](../DATA_PIPELINES.md) voor de revisieguard vóór deze laadfunctie.

## Sunshower: andere matchregel, huidige bron wel uniek

De Sunshower-optiehandler gebruikt products.find met een every-vergelijking van selected velden. Dat kiest de eerste passende record, terwijl V2 juist ambiguïteit afwijst. Deze codepaden zijn geen uitwisselbare helper zonder eerst dat contract gelijk te maken.

De opnieuw opgehaalde Sunshower-catalogus heeft:

- 72 records, 72 unieke volledige selection-objecten en geen dubbele selectiongroep;
- 72 unieke product-URL's en variantidentiteiten;
- vier selection-keys: kleur, met_uv, plaatsing en uitvoering;
- 72 relatieve productpaden en 72 geldige niet-negatieve integer price_cents-waarden.

Dit is een **positieve structurele datacontrole**. De afwijkende first-matchregel geeft bij deze gecontroleerde catalogus dus geen aangetoonde dubbele-keuzefout. De test bewijst geen overeenstemming met alle actuele Shopify-prijzen, kanaalpublicatie, variantbeschikbaarheid of leveranciersbron. Die controles moeten bij een nieuwe import of inhoudelijke wijziging apart volgen.

## Kleinste onderhoudsregel

Bij een nieuwe groep: verifieer huidige productidentiteit, veldnamen/typen, volledige combinaties, gewenste volgorde, URL/handle en revisie voordat de UI wordt aangepast. Test vervolgens lege/één/meerdere/ambigue combinaties, fetchfout versus geldige verkeerde JSON, gekozen waarde en terugknop. Gebruik bestaande adapters voor kleurweergave; maak geen nieuwe matchengine om alleen een chevron of border te veranderen.
