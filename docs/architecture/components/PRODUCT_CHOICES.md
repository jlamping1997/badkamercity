# Productkeuzes — varianten, productwissels en inbouwdelen

**Doel:** de klant kiest een exacte uitvoering en behoudt overzicht, prijsidentiteit en positie. **Eigenaarrol:** storefront voor bediening; productdatahouder voor toegestane relaties. Bronstatus VERIFIED_THEME; één V2 Hotbath-pagina en de Sunshower-configurator VERIFIED_HTML. Geen klik-/koop-/mobieltest in deze ronde.

## Vier contracten die niet uitwisselbaar zijn

| Systeem | Input | Uitkomst | Hoofdbestanden |
| --- | --- | --- | --- |
| Native Shopify-variant | product.options / geselecteerde option-values | Zelfde product, variant-ID; sectionfetch en replaceState | product-variant-picker, product-info.js, variant-selects in global.js |
| V2 cross-product | groups[] met menus[] en products[].options | Exact één ander product → volledige navigatie | bc-product-switcher.liquid + bc-product-switcher.js |
| Sunshower-configurator | bc_sunshower.configuration + products[].selection | Andere configuratie → ander product-URL | main-sunshower + bc-sunshower-page.js + bc-sunshower-products.json |
| Inbouwdeel toevoegen | Exacte parent/body-variant-/SKU-relatie, hoeveelheid en expliciete keuze | Eén of twee cartitems | bc-product-inbouw.liquid + bc-product-inbouw.js; haakt in op product-form |

Wiesbaden-kleuren zijn een **adapter naar V2**, geen vijfde navigatie-engine. Sunshower-accessoirekaarten hebben juist een eigen lokale kaartkeuze zonder PDP-navigatie; die hoort bij [kaarten](PRODUCT_CARDS_AND_FILTERS.md). De oudere collectiegestuurde custom.group-route blijft apart in main-product; de V2-uitleg is daarop niet automatisch toepasbaar.

## V2: bronkeuze en volgorde

`bc-product-switcher.liquid:11–23` bepaalt de groep en oorspronkelijke asset_url. De bronasset/revisie/groep gaan naar bc-choice-data-source. Alleen een passende bronrevisie levert een kleiner groepsbestand op. data-switcher-fallback-url blijft de oorspronkelijke URL. V2 laadt in deze volgorde:

1. Inline JSON onder data-bc-switcher-inline, wanneer de caller dat levert.
2. Een geldige tijdelijke group-handoff uit sessionStorage, passend bij route/groep/data-URL.
3. De primaire asset via fetch; bij een netwerk-/parsefout de oorspronkelijke fallback wanneer die verschillend is.

De promise-cache is per primaire URL en per paginalevensduur; een mislukte volledige load wordt uit die cache verwijderd. Dit is geen centrale persistente cataloguscache. Een syntactisch geldige maar inhoudelijk onvolledige primaire dataset veroorzaakt niet automatisch dezelfde netwerkterugval. Een ontbrekende groep/currentProduct of minder dan twee producten verbergt de switcher. De Liquid-serverbeslissing wordt niet opnieuw uitgevoerd; daarmee verschijnt niet alsnog automatisch een native variantpicker.

### Datamodel en match

Een groep heeft een exacte id, menus met key/label/order/display_type en products met handle/url/sort_order/options. Menus en producten worden op order gesorteerd. menu.values kan de expliciete waardevolgorde bepalen; anders wordt die uit de producten afgeleid. In niet-compacte modus gaat display_type buttons/dropdown voor; anders kiest V2 boven vijf waarden een dropdown. Compacte kleurmenus worden stalen en overige compacte menus buttons.

De begintoestand komt van het huidige product dat op handle of URL wordt gevonden. Bij elke keuze moeten **alle menuwaarden exact één product** aanwijzen. Geen of meerdere exacte matches geven geen navigatie. URL, same-origin, `/products/` en handle worden gecontroleerd. De selectie is dus niet bedoeld om vrij combinaties samen te stellen die niet als toegestaan product bestaan.

De gewone buttons/selects krijgen aria-pressed/disabled of disabled options via syncControls. Compacte kleurkeuze gebruikt stalen, houdt de huidige kleur in de eerste vier zichtbare waarden en kan de overige tonen. Compact betekent hier een scopeflag, niet alleen een mobiel breakpoint: Hotbath en de Wiesbaden-adapter gebruiken deze bediening ook op desktop. De historische bestandsnamen met mobile zijn behouden om bestaande hooks te sparen.

### Navigatie, opslag en races

`bc-product-switcher.js:669–715` blokkeert een nieuwe productwissel tijdens navigatie of een lopende product-form-add. Het vergrendelt relevante koopknoppen via product-info.dataset.bcNavigating, bewaart positie/uitgeklapte kleuren en gebruikt location.assign. Bij een direct gegooide navigatiefout wordt de oorspronkelijke selectie hersteld. pageshow maakt achtergelaten navigatiestaat weer vrij.

Opslagcontracten, alle bedoeld voor korte navigatieoverdracht:

| Sleutel | Geldigheid | Guard |
| --- | --- | --- |
| bc:product-switcher:position:v1 | 30 seconden; versie 1; eenmalig consumeren | Zelfde groep/targetroute, getallen geldig; preview_theme_id genegeerd in routekey |
| bc:product-switcher:expanded-colors:v1 | 30 seconden | Zelfde groep/bestemming; alleen nog bestaande kleurmenus |
| bc-sunshower-choice-scroll | 30 seconden | Exacte Sunshower-doelroute en veld; eenmalig consumeren |
| Inbouwdeelkeuze | 30 seconden | Zelfde groep én bodyvariant; andere bronroute; expliciete yes/no |

Zie [navigatie en opslag](NAVIGATION_AND_STORAGE.md) voor andere browserdata. Opslag kan ontbreken/vol zijn; geen blokkade of verzonnen waarde afleiden. Positiebehoud is alleen actief bij de bijbehorende callerflag; het is geen garantie voor iedere willekeurige V2-root.

### Gedeelde positiecorrectie

`bc-choice-position.js` wordt door Hotbath/V2 en Sunshower gebruikt. prepare zet tijdelijk history.scrollRestoration op manual, scroll-behavior op auto en overflow-anchor uit; optioneel stabiliseert minHeight. activate wacht op 80 ms stabiele layout, met maximaal 1.000 ms meettijd. Daarna volgt hoogstens één correctie naar de bewaarde viewportpositie. Pointer/touch/wheel/key/pagehide annuleert en herstelt de tijdelijke stijlen. Een breedteverschil groter dan 24 px annuleert; een nog niet geactiveerde keeper ruimt na 15 seconden op. Deze grenzen zijn bronwaarden, geen prestatiemeting.

## Wiesbaden-kleurenadapter

`bc-wiesbaden-colors.liquid:7–64` leest custom.color_variants (list.product_reference). Het eerste product is groepsanker. Alleen hetzelfde merk, hetzelfde wederzijdse anker, niet-lege kleur en URL tellen mee. De huidige product-ID moet in de geldige groep zitten en er moeten meer dan één geldige producten zijn. Daarna bouwt Liquid één inline V2-groep en gebruikt dezelfde JS en compacte stalenstijl met een Wiesbaden-aanvulling. Een lijst van gelijkende kleuren is op zichzelf geen relatiebewijs.

DOC-01 vond 1.150 producten met color_variants en 3.658 met switch_group. Dat is geen telling van actieve controls: de serverprioriteit en validatie kunnen een renderer overslaan of onderdrukken.

## Sunshower-configurator

`main-sunshower:64–71` rendert fields en geselecteerde waarden uit configuration. Voor plaatsing legt de huidige markup de volgorde Inbouw/Opbouw/Hoek vast. `bc-sunshower-page.js:67–96` bewaart de overige gekozen velden en zoekt in catalog.products een item waarvan iedere selection-key exact past. Het gebruikt de **eerste gevonden match**; de dataset moet dus zelf unieke configuraties waarborgen. Dat verschilt van V2, dat precies één match eist.

Tijdens laden/navigeren worden opties en koop-/wishlistcontrols geblokkeerd. Geen match of fetchfout geeft een statusmelding en herstelt de eerdere disabled-staten. Bij beschikbare positieopslag wordt de URL-hash leeggemaakt om dubbele scroll te vermijden; anders is #sunshower-configurator de terugval. Preview/designMode kan een preview_url/view/sourcetoken meenemen; dat is geen gewone productieproductrelatie.

Vier optionvelden staan in de onderzochte HTML; 72 producten hebben configuration in de export. Dat bewijst niet dat alle denkbare configuraties verkoopbaar of uniek zijn. De integriteit van bron-ID → Shopify-URL → variant-ID hoort bij de [datapijplijn](DATA_PIPELINES.md).

## Inbouwdeel: expliciete betaalde toevoeging

De Liquid-relatie bestaat uit zes pipe-gescheiden waarden: parentvariant, parent-SKU, bodyhandle, body-SKU, bodyvariant, quantity-per-trim. Vendor, beide variant-/SKU-identiteiten, quantity == 1, positieve bodyprijs en niet reeds inbegrepen inbouwdeel worden gecontroleerd. JS controleert ook dat het actieve form-id nog die parentvariant is. Een CSS-wijziging mag die guards niet uitschakelen.

Bij de huidige compacte Hotbath-scope en geen volume-row gebruikt de JS een checkbox, standaard **uit**. De yes/no-radio's blijven de onderliggende niet-compacte terugval. Alleen expliciete keuzes mogen kort naar een product met dezelfde groep/body worden overgedragen. Uit betekent normale product-form verder laten gaan; aan bouwt twee items, vermenigvuldigt bodyQuantity met parentQuantity en neemt alleen de bedoelde parentproperties/selling_plan mee.

De add-interceptor heeft 30 seconden timeout. Hij controleert HTTP/result.status, beide teruggegeven variant-/SKU-identiteiten en hoeveelheden vóór cartnavigatie. Een onduidelijk antwoord wordt uncertain en nodigt niet tot blind opnieuw toevoegen uit. Gewone hoofdartikel-add, gecombineerd inbouw-add en Sunshower-set hebben daarom afzonderlijke bevestigingspaden; zie [CART_AND_FEEDBACK](CART_AND_FEEDBACK.md).

## Acceptatie en kleinste veilige wijziging

| Staat | Te bewaken resultaat | Nog te controleren |
| --- | --- | --- |
| Geen/één/meerdere keuzes | Geen lege bediening; huidige keuze zichtbaar; toegestane combinaties behouden | Werkelijke doelroutes en mobiele/desktopweergave |
| Snelle tweede klik / lopende add | Geen tweede navigatie of verkeerd product in cart | Browser + transportstubscenario |
| Bron mislukt / geldige maar verkeerde JSON | Netwerkterugval of duidelijke beperkte staat; geen verzonnen opties | Beide fouttypen afzonderlijk |
| Kleur wijzigen / terugknop / opslag geblokkeerd | Identiteit, gekozen kleur, uitgeklapte lijst en positie logisch | pageshow/bfcache en opslaguitval |
| Inbouw uit/aan/uitverkocht/identity mismatch | Geen betaalde voorselectie; correcte variant en hoeveelheid; fout blokkeert | Nul echte koopacties in deze documentatieronde |
| Reduced motion / scrollinput | Geen concurrerende scroll; gebruiker kan onmiddellijk overnemen | Browser, vooral iOS/Safari |

Voor een visuele harmonisatie eerst de adapter/CSS veranderen, met behoud van productidentiteit, data-attributen, callbacks en opslagguards. Maak niet een tweede switcher omdat alleen de chevron of rand anders moet. Bestaande releasefixtures zijn terug te vinden in code-cleanup/2026-10-25 en product-switcher/2026-10-25; hun historische testresultaten zijn geen nieuwe runtimevrijgave.
