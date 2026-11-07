# Filterdrawer en zwevende lijstknop: twee breakpoints, twee taken

**28 oktober 2026 · DOC-03C.** Bronnen: `bc-external-filters.js/.css`, `bc-mobile-listing.js` en de contextsnippets. FX-30/31 en FL-01…04 gebruiken gecontroleerde mediaqueries en geometrie. Dit is **geen mobiele browser- of telefoontest**. [Bewijs](../../evidence/2026-10-28-filters/README.md).

## Drawer tot en met 989px

De externe filtercontroller maakt sidebar, toolbaropener, overlay en sluitknop. Bij de drawerquery krijgt de sidebar role=dialog, aria-modal=true en inert wanneer hij gesloten is. De toolbaropener weerspiegelt expanded. Op desktop verdwijnen de dialogrollen en blijft de sidebar gewoon bedienbaar.

Open vereist externe mode én de drawerquery. De controller bewaart het actieve element, zet de rootclass en focust de sluitknop. Sluitknop, overlay, Escape, mode-terugval en querywissel sluiten. Bij sluiten wordt de bewaarde trigger alleen gefocust als die nog verbonden is. FX-30 bevestigt Escape/inert/triggerherstel in de simulatie; FX-31 bevestigt sluiten en rolopruiming bij desktopquery.

De Tab-handler verzamelt binnen de sidebar focusbare, niet-disabled nodes met clientrects en probeert aan de uiteinden te wrappen. Deze werkelijke native focus-/details-/screenreaderinteractie is **niet** als geslaagd getest. De harnessrects zijn eenvoudige testwaarden; zij kunnen browserlayout of verborgen detailinhoud niet certificeren.

CSS verzorgt de transform/overlaytransitions en overflowlock op html/body zolang `bc-filter-drawer-open` staat. De controller schrijft hiervoor geen oude inline overflowwaarde terug. Andere overlays en hun lockeigenaars moeten daarom in een echte gecombineerde browsercontrole worden bekeken. De stylesheet bevat reduced-motion voor kaartbeelden; er is geen lokale reduced-motionbranch voor de drawertransition of paginatiescroll vastgesteld. Globale styles/browsergedrag kunnen nog meespelen; geen berekende duur- of a11yclaim.

## Zwevende knop tot en met 749px

`bc-mobile-listing.js` is een shortcut naar een bestaande opener, **geen extra filterengine**. Hij verplaatst de knop naar body en zet een initialized-marker. De knop wordt alleen getoond wanneer:

- de aparte telefoonquery actief is;
- een bruikbare opener bestaat en boven de viewport staat;
- het grid de viewport raakt en nog onder de gehanteerde ondergrens komt;
- geen native/externe filterdrawer en geen ander gemeld menu/cart/dialog/search-overlay open staat.

FL-01/02/04 bevestigen bodyplaatsing, de synthetische zichtbaarheidsvoorwaarden, suppression door een open dialog en verbergen buiten de telefoonquery. Opnieuw init op dezelfde marker maakt geen tweede knop. Dit zegt nog niets over cleanup van alle globale listeners bij volledige sectionvervanging; de bron heeft hier geen overeenkomstig disconnectedCallback zoals productdisclosure.

## Openerkeuze en focusretour

De shortcut kiest bij externe activeclass `[data-bc-open-filters]`, anders de native `.mobile-facets__open-wrapper`. FL-03 bevestigt die selectie; de native openerafhandeling is daarbij een stub, niet de volledige native drawercontroller.

Klikken zet een returnFocus-vlag en roept de bestaande opener aan. Scroll, resize, toggle, mediaquerychange en relevante DOM-/classmutaties plannen maximaal een frame. Zodra de drawer gesloten is, kan de helper focus teruggeven aan de zwevende knop of — als die niet meer getoond wordt — aan de gewone opener. Werkelijke sluitanimatie, scrollpositie en focus tussen beide controllers blijven browserwerk.

## Waarom de grenzen verschillen

989px bepaalt sidebar versus drawer. 749px bepaalt of de extra zwevende telefoonshortcut gewenst is. Het gebied daartussen kan dus een drawer hebben zonder zwevende shortcut. Dit is een functioneel verschil, geen automatisch breakpointdefect. Een globale mediaquerywijziging om alleen de knop te verplaatsen kan sidebar, focus en overlaygedrag raken.

De [fallbackrace](FILTER_STATE_AND_FALLBACK.md) kan de externe activeclass laten bestaan terwijl native het nieuwe grid bezit. De shortcut baseert zijn openerkeuze op precies die class en kan daardoor ook afhangen van een correct opgelost eigenaarschap. De nieuwe cases bewijzen deze specifieke shortcutuitkomst na de race niet afzonderlijk.
