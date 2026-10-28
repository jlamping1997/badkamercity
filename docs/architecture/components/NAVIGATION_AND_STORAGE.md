# Navigatie, zoeken en browseropslag

**Doel:** dezelfde informatie kunnen vinden vanaf desktop/mobiel en de bedoelde selectie bewaren zonder oude data als actuele waarheid te gebruiken. **Eigenaarrol:** merchant voor menubestemmingen/content; storefront voor rendering, focus en opslagcontracten. Bronstatus VERIFIED_THEME; header-/notificationmarkup op acht responses VERIFIED_HTML. Geen menu-/storage-interactie of accounttest uitgevoerd.

## Menu: Admin → headergroep → renderer

De Admin-inventaris van DOC-01 bevat negen menu's met maximaal drie niveaus. De huidige checksumgelijke sections/header-group.json kiest menu **main-menu**, menu_type_desktop **dropdown** en sticky_header_type **on-scroll-up**. Die waarden komen uit de sectiegroep en zijn daarmee niet afhankelijk van de open globale settings_data.json-bytecontrole. De aanwezigheid van de overige acht menu's maakt ze nog niet allemaal actief in de header.

| Laag | Bron | Verantwoordelijkheid |
| --- | --- | --- |
| Menuboom | Shopify Admin menu's | Titel, type, resourceId, URL en kinderen |
| Sectieselectie | header-group.json | Welke menuhandle/settings de header gebruikt |
| Desktop | header.liquid:1168 e.v. + BcCategoryNavigation | Categorie-/groeppanelen, horizontaal scrollen, open/close en focus |
| Mobiel | header-drawer.liquid + BcMobileDrawer in header.liquid | Root/subpanelen, terugstap, sluiten en headeroffset |
| Zoeken | header-search → search/predictive-search.js + responssectie | Zoekinvoer en suggesties; andere route dan resultatenpagina |

BcCategoryNavigation en BcMobileDrawer zijn actuele maatwerkklassen. Een instelling met de Dawn-naam dropdown bewijst niet dat alleen het oorspronkelijke Dawn-dropdownsnippet de UI rendert. Dat is precies waarom de bronroute moet worden gevolgd.

### Mobiele drawer

De drawer gebruikt data-bc-mobile-trigger/overlay/panel en een panelStack die begint bij root. Vooruit/terug verandert het actieve subpaneel; dit is geen browsergeschiedenis. Open zet aria-expanded, aria-hidden, overlay en bc-mobile-menu-open-klassen, berekent offset/scrollbarpadding en focust het paneel. Escape, overlay en overgang naar desktop sluiten. Close verbergt de inhoud na 260 ms, reset de stack en focust de trigger.

Nog te controleren: tabbereik in actieve/inactieve panelen, focus bij snel heropenen, scrollherstel, overlap met cart/searchdialogs en resize/Theme Editor herladen. Alleen het bestaan van Escape- en focuscalls is geen volledige focustrap- of a11yvrijgave. De desktopgrens voor deze headerlogica is 990px; de zwevende lijstfilterknop heeft bewust een ander bereik.

### Desktopnavigatie

De categoriecontroller heeft afzonderlijke previous/next-scrollknoppen, backdrop, focusin/out, toetsenbord en cleanup. Pijlen hier scrollen de categorierail; zij zijn niet dezelfde functie als een product-CTA of galerijbutton. De code bevat een destroy-pad en herinitialisatie voor section:load. Hergebruik van een stijl moet die lifecycle behouden.

## Zoekroutes onderscheiden

Predictive search kan producten/pagina's/artikelen als suggestie teruggeven. Een volledige zoekopdracht gaat naar main-search met q/type en een native resultatenlijst; externe filters kunnen die lijst later overnemen. De HTML-check met q=sunshower&type=product bewijst de volledige resultatenroute, niet de suggestielijst, enter-/tabbediening, vertraging of typfoutkwaliteit. Zie [kaarten en filters](PRODUCT_CARDS_AND_FILTERS.md).

## Opslagregister

| Sleutel / plaats | Inhoud en grens | Autoriteit / herstel |
| --- | --- | --- |
| bc_wishlist_v1 in localStorage | Maximaal 100 genormaliseerde items; handle + variantId als identiteit; beperkte titel/image/source/savedAt | Apparaat/browsergebonden selectie; geen accountlijst of actuele voorraad |
| bc-saved-cart-v1:hostname in localStorage | Versie 1, maximaal 30 dagen oud; items met variant, hoeveelheid, properties en eventueel selling_plan | Bewaarde selectie; ophalen/herstellen gebruikt echte Shopify-requests |
| V2 position/expanded-colors in sessionStorage | Korte route-/groephandoff van 30 seconden | Eenmalige overdracht; geen productdatabase |
| bc-sunshower-choice-scroll in sessionStorage | Veld/positie/doelroute, 30 seconden | Eén volgende configuratienavigatie |
| Inbouwkeuze in sessionStorage | Expliciete yes/no met groep/body/bronroute, 30 seconden | Alleen passende betaalde-keuzeoverdracht |
| Map-caches in JS | Productresponses, choicepromises, kaartdata | Paginageheugen; geen permanente verversingstaak |

De exacte keuzeopslagguards staan bij [PRODUCT_CHOICES](PRODUCT_CHOICES.md). Deze ronde heeft geen bestaande bezoekeropslag gelezen, gewijzigd of gewist. Het register beschrijft de code.

### Wishlist

bc-wishlist.js valideert handle en variant-ID, normaliseert metadata en vangt opslagfouten af. Dezelfde helper/knoppen worden op PDP, native kaart, externe kaart en Sunshower gebruikt; bij een kleur-/variantwissel moeten alle identity-attributen meewisselen. save meldt een fout als browseropslag geblokkeerd is en verstuurt na succes bc:wishlist-changed met het aantal. Titel/image uit opslag zijn presentatiesnapshots, geen actuele factsheet.

Vanuit de wishlist haalt add eerst product.js op. Niet beschikbare/complexe producten, Sunshower-source en bepaalde multi-variant/card-/quantity-/selling-plan-gevallen gaan naar de PDP. Alleen een toegestane exacte variant wordt toegevoegd; daarna volgt cartnavigatie. De mooie notification wordt daarmee niet automatisch bereikt. Cross-device/accountsync, bewaartermijnbeleid en toestemming zijn niet in deze bronronde vastgesteld; geen accountkoppeling beloven.

### Cart bewaren en herstellen

bc-cart-tools.js leest actuele cart.js voor bewaren. De opgeslagen selectie bevat variant-ID, aantal, properties en optioneel selling_plan. restore stuurt de bewaarde items naar cart/add; dit is een echte mutatie, geen read-only render. Het verwijdert na succes de opgeslagen kopie. De code voert daarmee geen inventarisreservering of prijsbevriezing uit. Een verouderd product/plan kan bij herstel niet meer geldig zijn.

Het huidige codecontract en het gewenste klantcontract bij al gevulde cart moeten vóór verdere wijziging apart worden getest. Opslag automatisch wissen tijdens debugging kan de selectie van een klant vernietigen; gebruik een nieuwe testcontext en verklaarde bron. In deze ronde is alleen de lege anonieme cartresponse gelezen.

## Wijzigings- en controlepad

Menutitel/bestemming: lees Admin-resource/handle → sectiegroep → desktop én mobiele renderer → linkdoel. Een CSS-fix voor een subpaneel hoeft geen menudata te herschrijven. Zoekfix: bepaal predictive versus native results versus externe index vóór aanpassen. Opslagfix: behoud versie/identity of ontwerp een expliciete migratie/terugval; verander een sleutel niet om een dataprobleem te verbergen.

Acceptatiematrix: nul/één/drie menuniveaus, lange labels, actieve route, root/vooruit/terug, Escape, buitenklik, 989↔990px, sticky header, tweede overlay, zoeken met toetsenbord, opslag denied/vol/ongeldige JSON, oude variant, dubbele wishlistidentiteit en restore in lege/gevulde cart. Deze scenario's staan open; alleen hun bronketen is nu gedocumenteerd.

## History-eigenaarschap van de lijst

De externe/native filtergeschiedenis is verdiept in [FILTER_STATE_AND_FALLBACK](micro/FILTER_STATE_AND_FALLBACK.md). Na fallback kunnen beide listeners lopen en kan native het grid vervangen terwijl de externe closure oude nodes bewaart (FILTER-F01). Normale menu-/PDP-handoff is daarmee niet hetzelfde historycontract. Geen globale popstateblokkade invoeren.
