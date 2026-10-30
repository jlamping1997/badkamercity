# RET-02 — Retour aanmelden naast Verlanglijst

30 oktober 2026. Eigenaar ziet op desktop geen retourknop en vraagt expliciet om een ingang naast de verlanglijst. Uitvoering op de bestaande branch `fix/product-cards-2026-10-14`.

## Bron en scope

Nieuwe verse read: **195947036938 — BadkamerCity - Retour aanmelden en footer is MAIN**. De eigenaar heeft het vorige retourconcept dus inmiddels gepubliceerd. Page166668894474, `/pages/retour-aanmelden`, is nog verborgen. Daardoor rendert de bestaande gezamenlijke URL-helper op MAIN geen nieuwe paginalink; alleen het publiceren van de themacode maakte de nieuwe Page nog niet zichtbaar.

Nieuw reviewconcept **195948839178 — BadkamerCity - Retourknop in header**, gedupliceerd van deze MAIN. De MAIN-nulmeting telt1354bestanden. Voor runtimewrites moet de volledige kopiepariteit1354/1354 zijn bewezen. Geen MAIN-write of Page-publicatie door deze uitvoering.

Alleen `sections/header.liquid` krijgt een blijvende runtimewijziging. De retourlink staat direct vóór Verlanglijst, met dezelfde utility-vormgeving, retourpijl en bestaande vertaling `bc_returns.heading`. De bestaande gedeelde URL-helper wordt gecaptured en gestript: echte gepubliceerde Page waar beschikbaar, conceptpreview wanneer verborgen, geen dode MAIN-link. Onder990px blijft de nieuwe headerlink verborgen; de bestaande mobiele header en sticky zoekfunctie blijven behouden. De desktopgrid reserveert voldoende ruimte voor de actieknoppen en laat de zoekkolom meeschalen. Geen nieuwe JavaScript-code of library.

## Checkpoint

**IMPLEMENTATION_PREPARED / COPY_AND_BROWSER_QA_PENDING.** Header gegenereerd vanaf de vers teruggelezen MAIN-body; oorspronkelijke MD5 `f7aa6c8b09db50f7f8c582db1ddc49d8` exact gelijk aan Git. Theme Check revision1 SUCCESS. Kopieproces loopt; browsercontrole volgt na volledige pariteit en upload.

## Vrijgave en bestaande grenzen

De eerdere mailboxproef blijft open; deze headerwijziging doet geen succesvolle formulierinzending, klantmail, retourlabel, refund of ordermutatie. Geen fysieke telefoon- of Windows-controle. Publicatie blijft bij de eigenaar volgens AGENTS.md. Bij vrijgave de retour-Page zichtbaar maken en het nieuwe concept publiceren; de verdwenen footeradresregel zit al in de huidige MAIN.

Terugzetten: alleen de header herstellen uit de nulmeting (oude MD5 hierboven), of het eerdere MAIN-thema aanhouden. Andere retourfiles en de Page worden niet verwijderd.
