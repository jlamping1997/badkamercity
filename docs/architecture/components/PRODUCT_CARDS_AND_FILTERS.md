# Productkaarten, zoeken en filters

**Klantdoel:** producten vinden, herkennen, vergelijken en de juiste uitvoering openen of toevoegen. **Eigenaarrol:** storefront voor kaart/gedrag; catalogus/indexbeheer voor data en dekking. Status VERIFIED_THEME + twee native lijst-HTML-responses; externe API, computed styles en interacties NOT_TESTED.

**Aanvulling DOC-02C:** vier publieke API-reads en verse lijst-HTML zijn gecontroleerd; Wastafelkranen 573 en Inloopdouches 305 sluiten op de HTML-context aan. De beperkte eerdere desktopkaartwaarneming blijft apart. Zie [filterketen](FILTER_ENGINE.md); geen volledige index-/prijs-/browserfallback-/mobielvrijgave.

## Renderers en gedeelde delen

| Renderer | Eerste gebruiksplaats | Bron / gedeelde helpers | Verschil dat behouden moet blijven |
| --- | --- | --- | --- |
| card-product.liquid | Standaard collectie, related-products en andere callers | bc-card-title, specs, delivery, price, wishlist; callerparameters | Quick-add kan none/standard/bulk zijn; caller bepaalt dit |
| bc-card-product-search.liquid | Native main-search | Titel/specs/delivery/wishlist; eigen prijsmarkup en hele kaart als link | CTA-label is een span binnen de kaartlink; geen extra geneste link toevoegen |
| JS renderProducts | Externe zoek-/collectielijst | bc-external-filters.js + CSS; verrijking via bc-card-data | Index geeft eerste lijst; Shopify-response bepaalt aanvullende kaartdetails en koop-ID |
| Sunshower shopkaart | bc-sunshower-landing | bc-sunshower-shop-card + bc-sunshower-shop.js | Lokale kleurwissel, optionele lifestylefoto, eigen add/status |
| Sunshower lichtkeuzekaart | Landingspagina | bc-sunshower-landing + bijbehorende CSS | Link naar configurator met decoratieve pijl; geen product-gridkaart of fotonavigatie |
| Homepageblokken | index.json | Eigen home-sectiemarkup | Niet aannemen dat een wijziging in card-product hier alle kaarten raakt |

De globale bc-product-cards.css wordt vanuit layout geladen. Externe filterstijl en sectiestijlen komen later in de pagina bij. Welke selector wint, hangt af van scope, volgorde en viewport. Dezelfde classnaam bewijst dus geen gelijke getoonde stijl.

## Native kaartcontract

card-product toont titel-/afbeeldingslinks, specificaties, prijs en optioneel leverlabel/quick-add. `:210` bevat een Bekijk-product-link met pijl. De standaard collection.json zet quick_add op none, zodat een aangetroffen standaard/bulk-add in het snippet niet automatisch actief is. Related-products en andere callers moeten afzonderlijk worden bekeken.

De native zoekkaart (`bc-card-product-search:43–140`) gebruikt een afzonderlijke wishlistknop naast één kaartlink. De CTA/pijl op :137 is presentatietekst in die link. Het leverlabel uit bc-card-delivery is de neutrale vertaling lead_time_on_request; het rekent geen leveranciersvoorraad om naar een belofte. Externe kaartverrijking kan een expliciet andere levertekst uit de serverselectie krijgen. Dat is een datacontract om te vergelijken, geen reden voor een algemene vaste levertijd.

## Het gemelde pijltjesverschil afbakenen

| Locatie / bron | Functie van de pijl | Huidige bronregel |
| --- | --- | --- |
| Native card-product:210 | Productpagina openen | Eigen anker/CTA met → |
| Native search-card:137 | Productpagina openen | Span met → binnen de bestaande kaartlink |
| bc-product-cards.css:204, :282–285 | Mobiele lijstpresentatie | Binnen max-width:749px wordt bc-card-view in het productgrid verborgen |
| bc-external-filters.css:452 | Externe kaartactie | Actieve externe mode zet de CTA weer op display:flex; cascade controleren |
| Sunshower landing:85–107 | Licht-/configuratiebestemming | Decoratieve → binnen een volledige linkkaart |
| main-sunshower:48–49 | Vorige/volgende foto | Echte buttons met disabled-randstaten |
| Sunshower configurator:83 | Naar accessoires op dezelfde pagina | Ankerlink met → |

De acht HTML-responses tonen de native CTA-markup en de Sunshower-landingsstructuur. Dat bewijst **niet** welke pijlen Jackson op zijn scherm bedoelde. Wel is er nu een concrete bronverklaring om te onderzoeken: mobiele grid-CSS verbergt het native CTA-label terwijl de aparte Sunshower-linkkaart eigen opmaak houdt. Externe JS kan de lijst later vervangen en de cascade veranderen. Classificeer pas na dezelfde route/functie/viewport als INCONSISTENCY, INTENTIONAL_VARIANT of UNKNOWN. Verwijder geen galerijpijlen op basis van een kaartverschil.

## Externe filters: activatie en terugval

De huidige snippet levert API-basis, collectiehandle of __all__, zoekmodus/term, collectieaantal, section-id bc-card-data en vertaalde labels. De JS vereist context, layout, #ProductGridContainer en #product-grid. Zoektype zonder product wordt overgeslagen. **De gelezen versie probeert de zoekroute automatisch; er staat geen bcfilters=1-opt-inguard in de activatieketen.** Dit vervangt oudere pilotclaims voor deze bronversie, zonder daarmee de externe dienst als gezond te certificeren.

De oorspronkelijke native nodes en inline displaywaarden worden bewaard. De externe request gebruikt collection/q/page/per_page/sort/filters/ranges; response moet products[]/facets[], niet-negatieve found en passende collectiecontext bevatten. Voor een collectie moet profile_products exact het Shopify collectionaantal zijn; zoekmodus verwacht __all__. Die guard controleert dekking als getal, niet ieder product/prijs/voorraadrecord.

| Staat | Bronmechanisme | Te toetsen gevolg |
| --- | --- | --- |
| Eerste laadpoging | runSearch; native inhoud bestaat al | Native inhoud blijft bruikbaar tot een geldig resultaat |
| Nieuwe filter/zoekterm | Request-ID omhoog, vorige AbortController stoppen | Verouderde response mag de laatste keuze niet overschrijven |
| Traag / timeout | 12 seconden per request | Geen oneindige spinner; native terugval zichtbaar |
| Geldig antwoord | Render filters/cards/count/pagination; active class aan | Dezelfde q/filters/sort/page in UI en URL |
| Netwerk/schema/tellingfout | setExternalMode(false), foutmelding, oorspronkelijke native nodes herstellen | Native URL-staat en eigen paginering blijven begrijpelijk |
| Drawer | Breakpoint max-width:989px | Focus, scrolllock, Escape, sluiting en triggerherstel moeten kloppen |

URL-contract: bcf_ voor filterwaarden, bcr_*_min/max voor ranges, bcsort en bcpage. Terugknop en popstate horen bij de requestcyclus. Dit is een clientcontract; er is in deze ronde geen VPS-query of indexvergelijking uitgevoerd.

### Kaartverrijking en kleuren

renderProducts bouwt eerst een kaart uit indexvelden. Daarna haalt de code via de Shopify Section Rendering-route `sections=bc-card-data` productgegevens op, met eigen cache/timeout. De section heeft eigen identiteit-/beschikbaarheids-/can_add-velden, volledige en korte titel, afbeeldingen, leverinformatie en eventueel een herbruikbare switchergroep. Zonder juiste verrijking begint de add-knop disabled.

bc-card-data laat direct toevoegen alleen toe bij één variant, quantity_rule.min/increment == 1 en geen verplicht selling plan. Die guard is niet vanzelf een bewijs dat iedere productconfiguratie zonder PDP-keuze begrijpelijk is; compareer het daadwerkelijke productcontract. Bij can_add false gaat de actie naar de PDP.

Kleurwissel heeft een versie/volgordecontrole; titel, URL, prijs, afbeelding, variant en wishlistidentiteit moeten samen wisselen. Een mismatch tussen foto en variant is verkooprelevant. “Alle kleuren” kan naar de PDP met bc_colors=groep leiden, waar de gedeelde switcher de lijst opent. Externe kaartkleuren en de serverlijst moeten dezelfde groep bedoelen.

### Toevoegen

De externe add stuurt items:[{id:variant_id,quantity:1}], sections en sections_url. Bij HTTP/status-fout verschijnt kaartfeedback; bij succes kan notification/drawer renderContents worden aangeroepen. Dit is een andere handler dan product-form. Het is deze ronde niet uitgevoerd. Zie [cart/feedback](CART_AND_FEEDBACK.md) voor verschillen tussen alle ingangspaden.

## Sunshower-shopkaart

De landings-template levert block.settings.product en eventuele product_white/black/grey/sand. Het snippet bouwt inline choices met prijs, koop-ID, URL en beelden. Zonder JS blijven kleurankers productlinks en het productformulier bestaan. Met JS wisselt de kaart lokaal; Enter/Space-gedrag, foto laden/fout en wishlistmetadata worden apart bijgewerkt. Een seat kan een lifestylefoto gebruiken; een wiper heeft een expliciete kleuroverzichtsnotitie. Dat is geen bewijs van een andere echte finishfoto per kleur.

Tijdens beeldwissel of add blijft de actie geblokkeerd. De add-handler in bc-sunshower-shop.js:228–269 geeft inline status en werkt bij CART-NOTIFICATION alleen de badge bij; hij opent de notification niet. Dat is een bronmatig vastgesteld verschil met de externe lijst en gewone PDP. De gewenste sitebrede regel moet afzonderlijk worden bepaald; geen blinde vervanging van een local-choicekaart door een navigatiekaart.

## Mobiele filtersnelkoppeling

bc-mobile-listing.js voegt geen tweede filterengine toe. Hij verplaatst één zwevende knop naar body en kiest afhankelijk van de active class de externe of native opener. Alleen bij max-width:749px, grid in beeld en opener boven de viewport wordt de shortcut getoond. Een ander open dialog/menu/filteroverlay onderdrukt hem. De onderliggende externe filterdrawer gebruikt 989px als grens; die grenzen hebben verschillende functies. Wijzig ze niet globaal om alleen één knop zichtbaar te maken.

## Onderhoud en acceptatie

Begin bij de route en vastgestelde renderer. Wijzig daarna de kleinst gedeelde helper: titel/specs/leverlabel, adapter of scoped CSS. Voor een pijlcorrectie alle native/externe/mobile/callerstaten vergelijken; voor een datacorrectie Shopify → index → verrijking → kaart → PDP volgen. Houd keyboardfocus, wishlistidentiteit en add-validatie in dezelfde regressie.

Minimale matrix voor DOC-02B/03: desktop/mobiel; native/externe succes/terugval; nulresultaten; één/multi-variant; ontbrekende afbeelding; meerdere kleuren; snelle kleurwissel; navigatie versus add; dubbele klik; API-timeout; terugknop; filterdrawer met ander dialog open. Dit zijn nog te testen scenario's. Geen performance- of conversiewinst uit een statische CSS-/kaartwijziging afleiden.

## Kaart-/filterketen op methodeniveau

[Kaartverrijking](micro/CARD_HYDRATION_AND_COLORS.md) volgt section-ID, vier workers, vijfseconden-timeout, cache en de nieuwste kleurintentie. [Filterstate/fallback](micro/FILTER_STATE_AND_FALLBACK.md) beschrijft ook de gereproduceerde native DOM-overdrachtsrace. [Waarden/controls](micro/FILTER_VALUES_AND_CONTROLS.md) scheidt raw waarden van zichtbare eenheden en beleidsflags; [drawer/shortcut](micro/MOBILE_LISTING_AND_DRAWER.md) behandelt de aparte mobiele statecontracten. De 41 replays zijn geen echte mobiele of carttest.

## Wishlistadapters afzonderlijk gevolgd

[WISHLIST_IDENTITY](micro/WISHLIST_IDENTITY.md) volgt het gedeelde snippet naar PDP, native/externe/home-/Sunshowerkaarten en de prioriteit van actuele formulierdata. De externe renderer vraagt refresh na verrijking; Sunshower-shop doet dat bij kleurcommit niet, waardoor WL-43 een achterblijvende aria-pressed/is-saved reproduceert. De volgende klik bewaart wel de juiste nieuwe identity. Geen nieuwe filtercontrollerreplay of live fix in DOC-03D.

## Pijlbedoeling verduidelijkt in UI-01

De eigenaar heeft inmiddels **pijlen bij de productfoto’s** gekozen. De oudere kaart-CTA-/mobiele-CSS-hypothese hierboven blijft broncontext, geen verklaring van de nu bevestigde melding. [UI-01](../../ui-consistency/2026-10-28/README.md) vergelijkt Sunshower-overlay en native thumbnailrail en bewaakt de gedeelde conceptcorrectie. Productkaartpijlen worden door die galerijcorrectie niet gewijzigd.
