# HDR-01 — vaste mobiele header

30 oktober 2026. Uitvoerder: Codex via connector en geïsoleerde werkboom; Windows niet gecontroleerd. Actieve branch blijft `fix/product-cards-2026-10-14`. De expliciete gebruikersvraag na DOC-ALL-01 bepaalt deze prioriteit. De offerte-mailcontrole is geparkeerd, niet afgerond.

## Vraag en bron

De eigenaar toont drie iPhone/Safari-beelden: het logo verschuift tussen homepage en Hotbath CB041BB-PDP; de bovenste header moet blijven staan terwijl de zoekrij bij omlaag scrollen verdwijnt en bij bewust omhoog scrollen terugkomt; het grijze vierkant om Terug moet verdwijnen bij aanraken.

Verse bron: MAIN **195915448586 — BadkamerCity - Tegelkleuren juiste uitvoering**, 1.350 bestanden. Los nieuw concept **195932061962 — BadkamerCity - Vaste mobiele header**, UNPUBLISHED; het offerteconcept **195916628234** wordt niet overschreven. Voor featurewrites eerst volledige kopiepariteit controleren. Geen MAIN-write of publicatie geautoriseerd/uitgevoerd.

De headerroute is `layout/theme.liquid → sections/header-group.json → sections/header.liquid → snippets/header-drawer.liquid + snippets/header-search.liquid`. De eigenaarfoto's zijn UI-evidence; er is geen claim over de exacte Safari-versie.

## Oorzaak en oplossing

| Onderdeel | Oorzaak | Nieuwe afspraak |
| --- | --- | --- |
| Logo | Op de homepage staat de link in een H1, elders is de link zelf het grid-item; bestaande linkpadding/gridgeometrie verschillen | Op iedere route dezelfde `bc-header__brand` als grid-item; dezelfde breedte, mobiele linkpadding/marge nul; desktoppadding behouden; homepage-H1 behouden |
| Sticky | `header_tag` is expliciet div; de oude StickyHeader-class is daardoor niet actief | Tot en met 989px CSS-sticky sectie; bovenste rij blijft vast; alleen zoekrij verandert |
| Springen tijdens inklappen | Een steeds kleiner wordende sticky sectie zou de documentstroom veranderen | Vaste ruimte voor de uitgeklapte header; alleen de binnenste zoekrij klapt in; transparante lege ruimte vangt geen clicks |
| Terug-focus | Het menu focust Terug automatisch na navigeren; de bestaande inset-focusopmaak wordt na aanraken zichtbaar | Aanraak-/pointerfocus zonder kader, uitsluitend binnen het mobiele menu; toetsenbordfocus heeft een blauwe 2px-indicator |
| Menu-aansluiting | De reserveringssectie blijft groter dan de zichtbare compacte header | Drawer meet de werkelijk zichtbare `.bc-header`; ResizeObserver houdt offset tijdens de overgang bij |

Twee runtimebestanden: `sections/header.liquid` en nieuw `assets/bc-mobile-header.js`. Geen nieuw framework, geen klanttekst/locale, geen gewijzigde catalogus, prijzen, checkout, offertetoggle of account-/cartcontract. De oude ongebruikte StickyHeader-class blijft behouden; deze taak ruimt geen andere code op.

## Gedrag en vorm

- Mobiel tot en met 749px: bovenste gridrij64px, zoekveld44px, tussenruimte10px, horizontale padding12px. Logo maximaal160px; op320px mag het binnen de vrije kolom krimpen.
- 750–989px: dezelfde indeling, zoekveld48px, logo maximaal180px. Vanaf990px behoudt de desktop de bestaande indeling/zoekfunctie; dezelfde merk-wrapper voorkomt routeverschillen.
- Naar beneden: pas inklappen nadat de oorspronkelijke header voorbij is en minimaal24px neerwaartse intentie is opgebouwd. Naar boven:32px intentie; binnen24px van de top altijd uitklappen. Ook trage bewegingen van1px tellen op. Kleine richtingswisselingen laten de zoekrij niet knipperen.
- Hoogte/marge/kleine verplaatsing240ms met rustige easing, opacity160ms. `prefers-reduced-motion: reduce` schakelt die overgang uit.
- De zoekrij is compact `inert` en `aria-hidden`; een onzichtbaar veld zit niet in de tabvolgorde. Focus in de zoekrij verhindert inklappen. Open predictive resultaten, geopend mobiel menu en een open native dialog bevriezen het scrollgedrag.
- Scrollmeting eenmaal per animation frame; passieve scrolllistener; clamping aan documentranden voorkomt onbedoelde omschakeling door rubberband-scroll. Logo/menu/iconen zelf worden niet getransformeerd.
- Menu-openen/sluiten/vooruit/terug gebruiken focus met `preventScroll`. Keyboard/pointer-modus wordt centraal binnen deze header bijgehouden; geen globale verwijdering van focusranden.
- Breakpointwissel, history/pageshow, section-load/unload, listener- en observercleanup zijn afgedekt. Gedeelde hoogtevariabelen worden bij verlaten van mobiel alleen teruggezet als ze nog door deze controller beheerd worden.

## Controle en vrijgave

Theme Check revision4: beide gewijzigde bestanden SUCCESS in een geïsoleerde runtimeboom met echte en.default.schema.json. Revision1 miste die ongebruikte editorlocale in de onderzoeksselectie; na ontvangst uit MAIN is dit opgelost. De validator gebruikte de bestaande lokale Shopify-doccache nadat de online refresh timeout gaf; geen succesvolle refresh claimen.

21 geïsoleerde JavaScript-scenario's PASS: eerste staat, inklappen/terugkomen, kleine/trage bewegingen, top-/bottom-clamping, zoekfocus, predictive/menu/dialogguards, desktop/breakpoint, inputmodus, dubbele initialisatie, editor unload/reload en pageshow. Kunstmatige geometrie bewijst geen visuele browser-/telefoonkwaliteit. Zie `behavior-checks.json` en `test-mobile-header.cjs` (Node + jsdom26.1.0).

Browsercontrole PASS in echte Chrome met componentframes320/390/750/989/1024px en gewone preview op1348px. De 390px-home/PDP-headers zijn bronmatig gelijk na alleen normaliseren van H1/whitespace; de fixture deelt daarom één header. PDP-inhoud is voor de componentproef beperkt tot titel/foto; geen volledige mobiele PDP-vrijgave.

Op390px heeft het logo op beide routes x59/y19.671875,160×42.65625px. Uitgeklapt is de zichtbare header138px, compact84px; de reservering blijft138px. Logo/menu/iconen verschuiven niet; zoekrij44→0px en inert aanwezig. Op320px krimpt het logo tot140px zonder overloop, met dezelfde x59. Tablet750/989: header142px/zoek48px/logo180px. Alle zes frames hebben scrollWidth=clientWidth. Bij kleine12px-terugbeweging blijft compact; bij60px omhoog keert zoeken terug.320px omlaag/omhoog en750px inklappen afzonderlijk bediend.

Menu na scroll400: zichtbare headerbottom84px en paneltop84px, ook bij volgende/terug. Het openen van de bestaande html/body-scrolllock maakte CSS-sticky aanvankelijk afhankelijk van een nieuwe scrollcontainer; daarom staat de binnenste wrapper tijdens `bc-mobile-menu-open` expliciet fixed op top0. Pointer-Terug: outline none/boxShadow none; via Tab/Shift+Tab blauwe2px-outline. PreventScroll behoudt scrollpositie. In de eerste testfixture ontbrak het verplichte id/data-sections-attribuut van Shopify’s compiled script; na herstel van die fixturedependency zijn de echte menucontrollers getest. Dit was geen geclaimde storefrontcodefout.

Predictive zoekactie CB041 gaf echte Hotbath-resultaten, inclusief CB041BB; native wheel-scroll met zoekfocus hield zoekrij44px zichtbaar en header top0. Geen resultaat gekocht of formulier ingestuurd. Reduced-motion is bronmatig gecontroleerd, niet met een fysieke OS-instelling.

Volledige kopie vóór featurewrites **1350/1350 MD5-gelijk**. Finaal **MAIN1350/1350 ongewijzigd**; concept1351 met exact één gewijzigde bestaande file (`sections/header.liquid`) en één nieuwe asset (`assets/bc-mobile-header.js`), nul ontbrekende bestanden. Beide runtimefiles volledig tekstgelijk teruggelezen. De bestaande `templates/page.bc-mobile-qa.liquid` is exact hersteld naar MD5 `24ae4cff55afe7f2453e4e9b6a0c2479`. De eerste te grote fixturewrite werd door Shopify afgewezen op256kB; daarna een gedeelde fixture van203791bytes gebruikt, geen nieuwe QA-file aangemaakt. Broncontroles en tijdelijke browserbeelden blijven begrensd tot deze componentproef.

Zie [meetwaarden](browser-measurements.json), [manifestcontrole](final-manifest-check.json) en [beeld](header-mobile-proof.jpg). Fysieke iPhone/Safari, trage telefoonhardware, echte bestelling en betaling zijn NOT_TESTED; eigenaarreview/publicatie blijven open. Het aparte offerteconcept is niet samengevoegd; vóór een latere offertepublicatie dit headerwerk opnieuw meenemen.

## Herstel

Zolang niet gepubliceerd blijft MAIN de terugval. Voor herstel binnen het concept uitsluitend de bewaarde `header.before.liquid.txt` terugzetten naar `sections/header.liquid`; de nieuwe asset is daarna ongebruikt en hoeft niet te worden verwijderd. Geen complete oude Git-root naar Shopify uploaden. Na eventuele eigenaarspublicatie opnieuw de rollen/bronstand lezen voordat een volgende taak schrijft.
