# RET-02 — Retour aanmelden naast Verlanglijst

30 oktober 2026. Eigenaar ziet op desktop geen retourknop en vraagt expliciet om een ingang naast de verlanglijst. Uitvoering op de bestaande branch `fix/product-cards-2026-10-14`.

## Bron en scope

Nieuwe verse read: **195947036938 — BadkamerCity - Retour aanmelden en footer is MAIN**. De eigenaar heeft het vorige retourconcept dus inmiddels gepubliceerd. Page166668894474, `/pages/retour-aanmelden`, is nog verborgen. Daardoor rendert de bestaande gezamenlijke URL-helper op MAIN geen nieuwe paginalink; alleen het publiceren van de themacode maakte de nieuwe Page nog niet zichtbaar.

Nieuw reviewconcept **195948839178 — BadkamerCity - Retourknop in header**, gedupliceerd van deze MAIN. De MAIN-nulmeting telt1354bestanden. Vóór runtimewrites is de volledige kopiepariteit1354/1354 bewezen. Geen MAIN-write of Page-publicatie door deze uitvoering.

Alleen `sections/header.liquid` krijgt een blijvende runtimewijziging. De retourlink staat direct vóór Verlanglijst, met dezelfde utility-vormgeving, retourpijl en bestaande vertaling `bc_returns.heading`. De bestaande gedeelde URL-helper wordt gecaptured en gestript: echte gepubliceerde Page waar beschikbaar, conceptpreview wanneer verborgen, geen dode MAIN-link. Onder990px blijft de nieuwe headerlink verborgen; de bestaande mobiele header en sticky zoekfunctie blijven behouden. De desktopgrid reserveert voldoende ruimte voor de actieknoppen en laat de zoekkolom meeschalen. Geen nieuwe JavaScript-code of library.

## Eindcontrole

**PREVIEW_VERIFIED / OWNER_RELEASE_PENDING.** Voor de eerste runtimewrite1354/1354bestanden MD5-identiek aan de nieuwe MAIN. Kopie was volledig verwerkt; theme-roleUNPUBLISHED. Finale conceptstand1354files met exact één gewijzigd pad: sections/header.liquid, MD5 `78a34a0d90ff1df449f3f6ac05db476d`. Body text-exact teruggelezen. MAIN1354/1354ongewijzigd, nogMAIN. Page nogverborgen. [Eindread](header-final-verification.json).

Theme Checkrevision2SUCCESS; tweede revisie houdt het label op één regel, zodat de iconen dezelfde verticale positie hebben. De GraphQL-compatibiliteitsvalidator slaat zijn validatie over; de echte query/mutation valideert en heeft geen userErrors. De definitieve header gebruikt alleen CSS en een link; geen nieuwe JS.

Echte desktopbrowser1348px: knop direct links van Verlanglijst, hele homepage zonder horizontale overloop. De knop echt aangeklikt en het native retourformulier met H1 Retour aanmelden bereikt op de conceptfallback `/pages/contact?view=retour-aanmelden`. Geen formulierinzending. Daarna de homepage met de zichtbare knop als browserresultaat klaargezet.

Zeven componentframes met echte conceptmarkup/styles:990/1024/1280/1440px met de bestaande offertepreview,990px met die CTA verborgen en390/989px mobiel. Alle scrollWidths gelijk aan clientWidth. Desktop: retour vóórwishlist, labelnowrap, retour- en wishlisticoon exact dezelfde top, logo en zoekrij zonder onderlinge overlap. De zoekbalk is op990px met offerte nog281pxbreed; zonder offerte467px. Mobiel: retourlinkdisplaynone, nulbreedte; bestaande bovenrij neemt dezelfde ruimte. Dit is geen fysieke telefoon-, native resize-, volledige sticky-/menuregressie- of mailboxproef. [Metingen](header-browser-measurements.json), [ThemeCheck](header-theme-check-r2.json), [beeld](return-header-desktop.jpg).

Voor de breedteproef alleen de bestaande QA-template in het nieuwe UNPUBLISHED-concept tijdelijk gebruikt; exact hersteld naar371bytes/MD5 `24ae4cff55afe7f2453e4e9b6a0c2479`. Geen extra runtimefile achtergelaten. Geen nieuwe branch, geen privéaccounttoegang en geen wijziging aan de andere concepten.

## Vrijgave en bestaande grenzen

De eerdere mailboxproef blijft open; deze headerwijziging doet geen succesvolle formulierinzending, klantmail, retourlabel, refund of ordermutatie. Geen fysieke telefoon- of Windows-controle. Publicatie blijft bij de eigenaar volgens AGENTS.md. Bij vrijgave de retour-Page zichtbaar maken en het nieuwe concept publiceren; de verdwenen footeradresregel zit al in de huidige MAIN.

Terugzetten: alleen de header herstellen uit de nulmeting (oude MD5 hierboven), of het eerdere MAIN-thema aanhouden. Andere retourfiles en de Page worden niet verwijderd.
