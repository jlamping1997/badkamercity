# Verlanglijst: gedeelde hartjes en actuele uitvoering

> **31 oktober 2026 — FIX-01, UNPUBLISHED195948839178:** Klik legt add/remove-intent vast uit bekende identiteit/geheugen; vertraagde afhandeling toggelt een onafhankelijke add niet weg. Scoped refresh synchroniseert nieuw gerenderde kaart direct. WISH-F02-regressie geslaagd. [Actueel bewijs en rollback](../../../repairs/2026-10-31/README.md). De bronregels/hashes en defectreplays hieronder beschrijven de eerdere nulmeting.

**28 oktober 2026 · DOC-03D.** Eigenaar van selectie/knopidentity en adapters. [Opslag](WISHLIST_STORAGE.md) verklaart bewaren/events; [renderen en toevoegen](WISHLIST_RENDER_AND_ADD.md) verklaart de wishlistpagina. [Bewijs](../../evidence/2026-10-28-wishlist/README.md) scheidt echte broncode, synthetische stimuli en open browsercontroles.

## Eén controller, verschillende ingangen

`layout/theme.liquid:265–266` laadt de gedeelde CSS en uitgestelde `bc-wishlist.js`. Het singleton-guard op JS:3 voorkomt een tweede controller bij herhaald uitvoeren; het bewijst geen volledige Theme Editor teardown. Het Liquid-snippet `bc-wishlist-button` levert een button type=button, producthandle, geselecteerde/eerste beschikbare variant, titel, afbeelding, source en aria-attributen. Geen aparte localStoragehelper per merk toevoegen.

| Caller / adapter | Bron | Identity op het klikmoment |
| --- | --- | --- |
| Algemene PDP | buy-buttons.liquid:114, source=detail | Dichtstbijzijnde productformulier-ID heeft voorrang boven initiële knopdata |
| Native collectiekaart | card-product.liquid:44, source=card | Formulier-ID als aanwezig, anders snippet-ID |
| Native zoekkaart | bc-card-product-search.liquid:43, source=card | Knopdata binnen zoekkaartscope |
| Homepage populair | home-popular-products.liquid:395, source=card | Snippetdata; deze kaart heeft geen eigen scopebranch in details |
| Sunshower-PDP | main-sunshower.liquid:81, source=sunshower | data-variant van data-ss-page heeft laatste voorrang |
| Sunshower accessoirekaart | bc-sunshower-shop-card.liquid:43, source=card | Huidige shop-linkhandle en huidige shop-form-ID |
| Externe lijstkaart | JS decorateCards + bc-external-filters.js:569–574 | Aanvankelijk mogelijk alleen handle; verrijking zet handle/variant/titel/image en vraagt refresh |

Dit is een bronkaart, geen bewijs dat iedere caller op iedere huidige route actief is. Hashes staan bij het bewijs; gelijknamige Git-rootfiles zijn niet automatisch deze live bytes.

## Volgorde van identity bepalen

`details` (:56–89) zoekt achtereenvolgens Sunshower-shopkaart, Sunshower-page, product-info, zoekkaart, externe kaart of standaardkaart als scope. Bij een shopkaart komt de handle uit de actuele productlink. Een button in een form/product-form kiest eerst zijn eigen input[name=id]; anders zoekt de scope shop-form, ss-product-form of product-form. Zonder veld gebruikt hij de variantdataset. Alleen de Sunshower-pagevariant kan die uitkomst daarna nog overschrijven.

Handle + `:` + variantId is de exacte opslagidentity. Twee uitvoeringen zijn dus twee favorieten, ook bij dezelfde handle. Titel/beeld/source zijn metadata en geen onderdeel van de identity. WL-12/13 bevestigen de veldprioriteit; een verkeerd geplaatst formulier of nieuw markupnest kan die prioriteit veranderen. Houd prijs, productlink, afbeelding en wishlist bij dezelfde gekozen uitvoering; voeg geen CSS-fix toe voor een data-adapterprobleem.

## Klik met en zonder variant

Een disabled button of eigen `data-bc-wishlist-busy=true` stopt de toggle. De knop krijgt een busyflag totdat try/finally is afgerond. Een geldige expliciete variant kan zonder productrequest worden bewaard of verwijderd; bewaren bevestigt geen actuele beschikbaarheid.

Zonder geldige variant zijn er drie routes (:202–215): precies één bestaande uitvoering voor die handle wordt gebruikt om te verwijderen; meerdere bestaande uitvoeringen geven de uitleg om de PDP te gebruiken; zonder bestaande uitvoering haalt readProduct product.js op en kiest de eerste beschikbare variant, of de eerste variant als geen enkele beschikbaar is. Een onbeschikbare favoriet bewaren mag dus wel; de latere kooproute blijft apart. WL-14…20 volgen fallback, ambiguïteit, busyblokkade en retry na een fetchfout.

Busy geldt per button. Het is geen globale transactie tussen alle hartjes of tabbladen. De opslagschrijfrace staat als WISH-F01 in het [opslagdossier](WISHLIST_STORAGE.md).

## Presentatiestatus en verversing

`syncButtons` (:137–161) zet class is-saved, aria-pressed, title en aria-label. Bij een ontbrekende variant telt iedere opgeslagen uitvoering van dezelfde handle als actief; dit is een productbrede indicatie, geen identificatie van één gekozen uitvoering. Headerbadge en utility-label tellen lijstentries.

`BCWishlist.refresh()` is een gecoälesceerde requestAnimationFrame: decoreren en knop/headerstatus synchroniseren. Hij leest **niet** opnieuw localStorage, rendert de wishlistpagina niet opnieuw en haalt geen nieuwe producten op. Het change-listener op select, input[name=id] en radio, section:load en geselecteerde kaarttoevoegingen via MutationObserver vragen dezelfde framebewerking aan. WL-40 gebruikt de echte DOMlibrary-observer voor een nieuwe kaart; WL-41/42 bevestigen singleton, één frame en een expliciet variant-change-event. Geen native observer-/keyboard-/focusvrijgave.

Externe decoratie markeert een kaart en voegt een hartje toe vanuit de kaartlink. De externe filterrenderer vraagt na verrijking zelf refresh. DOC-03D voert die filtercontroller niet opnieuw uit; de eerdere [kaartverrijkingsreplay](CARD_HYDRATION_AND_COLORS.md) en deze echte wishlistreplay hebben elk hun eigen grens.

## WISH-F02: hartjesstatus blijft achter na Sunshower-kaartkleur

**VERIFIED_ISOLATED, P2-kandidaat voor zichtbare/aangekondigde selectiestatus.** WL-43 voert volledige ongewijzigde `bc-sunshower-shop.js` en `bc-wishlist.js` samen uit, met synthetische kaartmarkup en gecontroleerde afbeelding-preload. Product A staat al opgeslagen. De kaart kiest B en commitChoice (:146–158) verandert link en formulier-ID nadat het beeld geladen is.

Het hartje houdt dan is-saved en aria-pressed=true van A, terwijl `BCWishlist.has` voor B false teruggeeft. De Sunshower-controller roept geen wishlistrefresh aan en dispatcht geen variant-change-event; de wishlistobserver luistert niet naar deze attribuut-/tekstwijziging. Een volgende klik op het hartje leest **wel** B en bewaart de juiste nieuwe identity. Het probleem zit in de voorafgaande presentatie/aankondiging, geen bewezen verkeerde cartvariant of opslagidentity.

Kleinste voorgestelde richting: na een bevestigde Sunshower-keuzecommit de bestaande gedeelde refresh aanvragen, met behoud van preload/cancel/nieuwste-keuze-guards. Geen kopie van wishliststate of nieuwe merkstorage invoeren. Test opgeslagen A → niet-opgeslagen B en omgekeerd, twee opgeslagen kleuren, beeldfout, snel wisselen, onbeschikbaar product, beide scriptlaadvolgorden en section-unload. De replay gebruikt één benoemde laadvolgorde en geen echte browserbeelden.

## Stijl en soepelheid

`bc-wishlist.css` deelt de hartvorm, hover/focus/is-saved, een opacity/pointer-events-busystaat en focusring. De fill gebruikt scaleY met 200 ms ease; buttonkleuren 180 ms. Reduced-motion verwijdert transitions voor producthartjes; de header heeft een afzonderlijke fillspecificiteit. PDP, kaart en Sunshower-configurator hebben functioneel verschillende plaatsing/maat; dat is geen reden voor aparte opslaglogica.

De wishlistgrid heeft vier kolommen, drie tot 990px en twee tot 690px; tot 350px worden afstanden kleiner. Dit zijn gelezen CSS-waarden, geen gemeten touchdoelen, computed styles, contrast, framerate of mobiele smoothness. Controleer die visueel na een eventuele correctie.
