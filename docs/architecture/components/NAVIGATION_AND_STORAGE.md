# Navigatie, zoeken en browseropslag

> **31 oktober 2026 — NAV-03 in reviewconcept195947036938:** één passende rij met Meer categorieën, geen schuifrail of tweede rij. Bestaand mobiel menu onder990px;13breedteproeven en Menu→Douche→Terug/Escape gecontroleerd. Codecheckpoint b7a5308038965bf874e06ed5115aa9431eb381d3. [Actuele status en begrensd browserbewijs](../../navigation-and-tiles/2026-10-31/README.md). Oudere bronregels/scroll-/opslaglogs hieronder behouden hun meetmoment.

**Doel:** dezelfde informatie kunnen vinden vanaf desktop/mobiel en de bedoelde selectie bewaren zonder oude data als actuele waarheid te gebruiken. **Eigenaarrol:** merchant voor menubestemmingen/content; storefront voor rendering, focus en opslagcontracten. Bronstatus VERIFIED_THEME; header-/notificationmarkup op acht responses VERIFIED_HTML. DOC-03D voegt 43 lokale wishlistreplays toe; geen echte menu-/bezoekersopslaginteractie of accounttest.

## Menu: Admin → headergroep → renderer

De Admin-inventaris van DOC-01 bevat negen menu's met maximaal drie niveaus. De huidige checksumgelijke sections/header-group.json kiest menu **main-menu**, menu_type_desktop **dropdown** en sticky_header_type **on-scroll-up**. Die waarden komen uit de sectiegroep en zijn daarmee niet afhankelijk van de open globale settings_data.json-bytecontrole. De aanwezigheid van de overige acht menu's maakt ze nog niet allemaal actief in de header.

| Laag | Bron | Verantwoordelijkheid |
| --- | --- | --- |
| Menuboom | Shopify Admin menu's | Titel, type, resourceId, URL en kinderen |
| Sectieselectie | header-group.json | Welke menuhandle/settings de header gebruikt |
| Desktop | header.liquid → BcCategoryNavigation + bc-category-overflow.liquid | Werkelijke breedte meten, passende rij + Meer, categorie-/groeppanelen, open/close en focus |
| Mobiel | header-drawer.liquid + BcMobileDrawer in header.liquid | Root/subpanelen, terugstap, sluiten en headeroffset |
| Zoeken | header-search → search/predictive-search.js + responssectie | Zoekinvoer en suggesties; andere route dan resultatenpagina |

BcCategoryNavigation en BcMobileDrawer zijn actuele maatwerkklassen. Een instelling met de Dawn-naam dropdown bewijst niet dat alleen het oorspronkelijke Dawn-dropdownsnippet de UI rendert. Dat is precies waarom de bronroute moet worden gevolgd.

### NAV-01 — 29 oktober 2026

[Het actuele dossier](../../navigation/2026-10-29/README.md) beschrijft de nieuwe conceptversie: de eerste categorie opent nog een paneel, groepen op het tweede niveau klappen native inline open en bladeren niet naar een derde paneel. Menubladeren en Bekijk alle blijven gewone Admin-URL's. Inactieve panelen krijgen inert/aria-hidden; vooruit/terug herstelt focus. De twee accountlinks zijn op verzoek verwijderd. Rijen op het vervolgniveau hebben rechte scheidingslijnen, de eerste categorieën blijven behouden. Zie de centrale status voor test- en publicatiegraad; onderstaande historische beschrijving is geen aanvullende vrijgave.

### Mobiele drawer

De drawer gebruikt data-bc-mobile-trigger/overlay/panel en een panelStack die begint bij root. Vooruit/terug verandert het actieve subpaneel; dit is geen browsergeschiedenis. Open zet aria-expanded, aria-hidden, overlay en bc-mobile-menu-open-klassen, berekent offset/scrollbarpadding en focust het paneel. Escape, overlay en overgang naar desktop sluiten. Close verbergt de inhoud na 260 ms, reset de stack en focust de trigger.

Nog te controleren: tabbereik in actieve/inactieve panelen, focus bij snel heropenen, scrollherstel, overlap met cart/searchdialogs en resize/Theme Editor herladen. Alleen het bestaan van Escape- en focuscalls is geen volledige focustrap- of a11yvrijgave. De desktopgrens voor deze headerlogica is 990px; de zwevende lijstfilterknop heeft bewust een ander bereik.

### Desktopnavigatie

**NAV-03:** de huidige controller meet item- en lijstbreedtes na fontladen en resize; overblijvende branches verschijnen met dezelfde Admin-bestemmingen onder een native Meer-disclosure. Alle links staan al in Liquid/HTML. ResizeObserver en section-cleanup horen bij deze lifecycle. ArrowDown opent en focust de eerste zichtbare branch; Escape sluit en herstelt focus. Zonder scripts toont de native Alle categorieën-disclosure de volledige boom. Zie het gekoppelde NAV-03-dossier voor exacte bronhashes en eindmetingen.

**Historische railbeschrijving (vóór NAV-02/NAV-03):** De categoriecontroller heeft afzonderlijke previous/next-scrollknoppen, backdrop, focusin/out, toetsenbord en cleanup. Pijlen hier scrollen de categorierail; zij zijn niet dezelfde functie als een product-CTA of galerijbutton. De code bevat een destroy-pad en herinitialisatie voor section:load. Hergebruik van een stijl moet die lifecycle behouden.

## Zoekroutes onderscheiden

FLASH-01 (29 oktober 2026) laadt component-search.css en component-predictive-search.css synchroon in de head. De dubbele headerlink vervalt; bc-first-paint begrenst iconen en verbergt gesloten suggesties vóór de rest van de styles. De bestaande zoekcontroller en de open/loading-toestanden blijven intact. Zie [de bron-/browservergelijking](../../render-flash/2026-10-29/README.md) en centrale status voor review/publicatie.


Predictive search kan producten/pagina's/artikelen als suggestie teruggeven. Een volledige zoekopdracht gaat naar main-search met q/type en een native resultatenlijst; externe filters kunnen die lijst later overnemen. De HTML-check met q=sunshower&type=product bewijst de volledige resultatenroute, niet de suggestielijst, enter-/tabbediening, vertraging of typfoutkwaliteit. Zie [kaarten en filters](PRODUCT_CARDS_AND_FILTERS.md).

## Opslagregister

| Sleutel / plaats | Inhoud en grens | Autoriteit / herstel |
| --- | --- | --- |
| bc_wishlist_v1 in localStorage | Eerste 100 genormaliseerde entries; handle + variantId als identiteit; beperkte titel/image/source/savedAt; load dedupliceert niet | Browser/origingebonden selectie, geen TTL/accountlijst/actuele voorraad; multitabconflict WISH-F01 |
| bc-saved-cart-v1:hostname in localStorage | Versie 1, maximaal 30 dagen oud; items met variant, hoeveelheid, properties en eventueel selling_plan | Bewaarde selectie; ophalen/herstellen gebruikt echte Shopify-requests |
| V2 position/expanded-colors in sessionStorage | Korte route-/groephandoff van 30 seconden | Eenmalige overdracht; geen productdatabase |
| bc-sunshower-choice-scroll in sessionStorage | Veld/positie/doelroute, 30 seconden | Eén volgende configuratienavigatie |
| Inbouwkeuze in sessionStorage | Expliciete yes/no met groep/body/bronroute, 30 seconden | Alleen passende betaalde-keuzeoverdracht |
| Map-caches in JS | Productresponses, choicepromises, kaartdata | Paginageheugen; geen permanente verversingstaak |

De exacte keuzeopslagguards staan bij [PRODUCT_CHOICES](PRODUCT_CHOICES.md). Deze ronde heeft geen bestaande bezoekeropslag gelezen, gewijzigd of gewist. Het register beschrijft de code.

### Wishlist

bc-wishlist.js valideert handle en variant-ID, normaliseert metadata en vangt opslagfouten af. Dezelfde helper/knoppen worden op PDP, native kaart, externe kaart en Sunshower gebruikt; bij een kleur-/variantwissel moeten alle identity-attributen meewisselen. save meldt een fout als browseropslag geblokkeerd is en verstuurt na succes bc:wishlist-changed met het aantal. Titel/image uit opslag zijn presentatiesnapshots, geen actuele factsheet.

Vanuit de wishlist gebruikt add eerst readProduct. Die helper kan de eerder opgehaalde product.js-promise uit cache teruggeven: dit is geen gegarandeerde verse serverread per klik. Niet beschikbare/complexe producten, Sunshower-source en bepaalde multi-variant/card-/quantity-/selling-plan-gevallen gaan naar de PDP. Alleen een toegestane exacte variant wordt naar cart/add gestuurd; daarna volgt cartnavigatie. De notification wordt daarmee niet automatisch bereikt. Cross-device/accountsync en toestemmingswerking zijn niet vastgesteld; de huidige wishlistcode heeft geen expiratiebeleid of accountkoppeling.

De inhoudelijke eigenaren staan nu apart: [opslag/events/multitab](micro/WISHLIST_STORAGE.md), [identity/knoppen/Sunshower](micro/WISHLIST_IDENTITY.md) en [render/cache/toevoegen](micro/WISHLIST_RENDER_AND_ADD.md). WISH-F01 reproduceert selectieoverschrijving tussen tabbladen onder vertraagde events; WISH-F02 reproduceert achterblijvende hartjesstatus na Sunshower-kaartkleur. Geen huidige bezoekersincidenten of live correcties vastgesteld. [43 cases en bronmethode](../evidence/2026-10-28-wishlist/README.md).

### Cart bewaren en herstellen

bc-cart-tools.js leest actuele cart.js voor bewaren. De opgeslagen selectie bevat variant-ID, aantal, properties en optioneel selling_plan. restore stuurt de bewaarde items naar cart/add; dit is een echte mutatie, geen read-only render. Het verwijdert na succes de opgeslagen kopie. De code voert daarmee geen inventarisreservering of prijsbevriezing uit. Een verouderd product/plan kan bij herstel niet meer geldig zijn.

Het huidige codecontract en het gewenste klantcontract bij al gevulde cart moeten vóór verdere wijziging apart worden getest. Opslag automatisch wissen tijdens debugging kan de selectie van een klant vernietigen; gebruik een nieuwe testcontext en verklaarde bron. In deze ronde is alleen de lege anonieme cartresponse gelezen.

## Wijzigings- en controlepad

Menutitel/bestemming: lees Admin-resource/handle → sectiegroep → desktop én mobiele renderer → linkdoel. Een CSS-fix voor een subpaneel hoeft geen menudata te herschrijven. Zoekfix: bepaal predictive versus native results versus externe index vóór aanpassen. Opslagfix: behoud versie/identity of ontwerp een expliciete migratie/terugval; verander een sleutel niet om een dataprobleem te verbergen.

Acceptatiematrix: nul/één/drie menuniveaus, lange labels, actieve route, root/vooruit/terug, Escape, buitenklik, 989↔990px, sticky header, tweede overlay, zoeken met toetsenbord en restore in lege/gevulde cart blijven open. Opslag denied/vol/ongeldige JSON, missende variant, dubbele opgeslagen wishlistidentity en events zijn nu lokaal getoetst; echte browser-/cartrestorecontroles blijven afzonderlijk open.

## History-eigenaarschap van de lijst

De externe/native filtergeschiedenis is verdiept in [FILTER_STATE_AND_FALLBACK](micro/FILTER_STATE_AND_FALLBACK.md). Na fallback kunnen beide listeners lopen en kan native het grid vervangen terwijl de externe closure oude nodes bewaart (FILTER-F01). Normale menu-/PDP-handoff is daarmee niet hetzelfde historycontract. Geen globale popstateblokkade invoeren.
