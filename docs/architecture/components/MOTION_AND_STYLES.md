# Stijl en beweging — huidige bronnen en gedeelde regels

**Doel:** herkenbare bediening en rustige, directe interacties. Dit register beschrijft bronwaarden van MAIN 195818389770; het is geen nieuw goedgekeurd design system of perceptuele snelheidsmeting. De [componentafspraken](../COMPONENT_CONTRACTS.md) blijven het voorgestelde harmonisatiekader.

**Latere DOC-03A-waarneming:** de [Sunshower-microanalyse](micro/SUNSHOWER_ACTIONS.md) bevat één echte desktopgalerijstap en Maathulp/Escape/focus. Dat is geen nieuwe duur-/smoothness-/mobielmeting; onderstaande bronwaarden blijven het DOC-02A-register.

## Waar de stijl vandaan komt

| Laag | Huidige bron | Gevolg voor onderhoud |
| --- | --- | --- |
| Basis en fonts | layout/theme.liquid genereert font-/kleurvariabelen; base.css | Theme-instellingen en schema's horen bij de CSS-waarde |
| Gedeelde productkaart/prijs/type | layout:260–266 → bc-product-cards, component-price, bc-typography, wishlist | Eerst gedeelde betekenis wijzigen, daarna alle callers controleren |
| Algemene PDP | bc-product-page + Dawn/componentstyles | Bestaande sectie-ID-/modifier-specificiteit behouden |
| Hotbath/Wiesbaden keuze | bc-hotbath-swatches/mobile + bc-wiesbaden-colors | Dezelfde V2-engine, adapter-/merkstijl erboven |
| Sunshower | --ss-* in page/configurator/landingstyles | Eigen merkpresentatie; betekenis op --bc-/Dawn-tokens mappen vóór samenvoegen |
| Externe lijst | bc-external-filters.css en active-classscope | Kan globale kaartregels overschrijven na JS-activatie |
| Overlay | component-cart-notification.css | Eigen begrensde tokens --bc-popup-ink/green, native dialog |
| Legacy/content | Inline sectionstyles en Admin-description | Eerst bron/cascade aantonen; niet aannemen dat alles in losse CSS zit |

Een gelijke hexkleur is geen bewijs van dezelfde semantische rol. Een andere border/radius is niet automatisch een bug. Begin met dezelfde functie en staat: label, selectie, focus, disabled, loading, fout en overgang. Introduceer geen globale button/svg-regel om één merkcomponent te corrigeren.

## Huidige bewegingscontracten

| Component | Bronwaarden | Afbreken / reduced motion / beperking |
| --- | --- | --- |
| Cartnotification openen | Opacity 280ms ease; transform 380ms cubic-bezier(.2,.8,.2,1) | rAF active-class; heropenen annuleert close-timer |
| Cartnotification sluiten | CSS 220ms; JS wacht 230ms | Bij reduce 0ms/geen transition; niet afhankelijk van transitionend |
| Algemene beschrijving/specs | Web Animations API 320ms cubic-bezier(.22,1,.36,1) | Lopende animation cancel; reduce/fallback direct; focus van verborgen inhoud beheren |
| Sunshower beschrijving | CSS height 440ms cubic-bezier(.25,.8,.25,1) | Eigen expanded/animating-staat; reduce voltooit direct; transitionend hermeet |
| Sunshower galerij | Native smooth scroll, geen vaste duurclaim | Bij reduce instant; intended index voorkomt stapverlies bij snel klikken; 180ms settle-timer |
| Gedeeld positiebewaren | 80ms stabiele layout, max 1000ms meetvenster | Hoogstens één correctie; gebruikersinput annuleert; breedteguard |
| Mobiele headerdrawer | Close verbergt/reset na 260ms | Escape/overlay/breakpointclose aanwezig; race/focus/reduce interactief nog te toetsen |

Geen van deze getallen is een gegarandeerde laadtijd of Core Web Vitals-score. Een state-/navigatieovergang met serverwerk hoeft niet dezelfde duur te krijgen als een decoratieve hover. “Smooth” vraagt vooral dat de laatste bedoeling klopt, gebruikerinput voorrang houdt en focus/scroll niet onverwacht springen.

## Productkeuze: wat we gedeeld houden

Gedeeld: V2-matchengine, state-/disabledlogica en BCChoicePosition. Hotbath en Wiesbaden gebruiken de kleuradapter naar dezelfde engine. Verschillend: Sunshower heeft configuratievelden met inhoudelijke pictogrammen en een eigen catalogus; gewone native varianten gebruiken Shopify-variantstate. Eenzelfde selectiestijl kan worden toegepast zonder die datamodellen samen te voegen.

Let bij de nieuwe stijlkeuze ook op de compacte scope: bestanden met mobile in de naam zijn niet overal meer alleen mobiel. Een mediaquery toevoegen op basis van de naam kan desktopbediening terugdraaien. De echte scope staat in data-attributen en callerlogica, beschreven bij [PRODUCT_CHOICES](PRODUCT_CHOICES.md).

## Pijlen en iconen: functie bepaalt het contract

| Functie | Semantiek | Gedeelde acceptatie |
| --- | --- | --- |
| Product/configuratie openen | Link, eventueel hele kaart | Duidelijk doel, geen dubbele/geveinsde interactieve CTA |
| Volgende/vorige foto | Button | Correcte index, rand-disabled, naam, swipe/keyboardconsistentie |
| Paneel in/uit | Disclosure/trigger | aria-expanded en chevronrichting volgen dezelfde staat |
| Menu één niveau terug | Button naar vorig drawerpaneel | Focus/stack klopt; geen onbedoelde browser-back |
| Dialog sluiten | Button + Escape/backdropcontract | Bereikbaar vlak, benoemd icoon, focusherstel, werkt tijdens animatie |

De huidige mobile-list-CSS verbergt sommige Bekijk-product-labels; Sunshower heeft eigen lichtkaarten met decoratieve pijl. De exacte gemelde inconsistentie is nog niet visueel gereproduceerd. Zie de [pijlenkaart](PRODUCT_CARDS_AND_FILTERS.md) voor bronnen en mogelijke cascade-overschrijving.

## Praktische harmonisatiewerkwijze

Kies één functie in twee werkelijk actieve routes, leg desktop/mobiel en dezelfde staat vast, noteer huidige computed waarden en kies de bestaande referentievariant. Houd functionele hooks en dataidentiteit intact. Een scoped helper/modifier is meestal genoeg voor alleen rand, chevron of spacing; een nieuwe componentengine is daar niet automatisch voor nodig.

Controleer daarna herhaalde interactie, focus, touch, resize, reduced motion, ontbrekende inhoud, APIfout en browserterugkeer. Foto-, keuze- en dialogstaat moeten het laatste bedoelde resultaat volgen, zonder dubbele koopactie. Oude releasefixtures kunnen regressies ondersteunen, maar eerst hash-/contextovereenkomst vaststellen. Deze ronde heeft geen screenshotvergelijking, computed-style- of interactiemeting uitgevoerd.

Verdere tokens voor spacing, radius, controlhoogte, schaduwen en lagen worden pas als één gekozen bron vastgelegd nadat de werkelijk gebruikte cascade is vergeleken. Tot die tijd is dit een herkomst-/bewegingsregister, geen toestemming om iedere hardcoded waarde te vervangen.
