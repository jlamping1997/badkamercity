# Mobiele categorie-iconen — eerste ontwerp

Status: USER_APPROVED_UI / IMPLEMENTED_PREVIEW. 17 oktober 2026, Europe/Amsterdam. Eigenaar werkt vandaag vanaf mobiel; Wiesbaden blijft openstaan. Eerste zeven hoofdcategorieën uit de aangeleverde schermafbeelding. Eigenaar heeft op 17 oktober de toepassing van deze zeven iconen goedgekeurd.

## Bestanden

- Zeven originele bc-nav-*.svg-bronbestanden, 32×32 viewBox, stroke 1.65, ronde lijnuiteinden en currentColor.
- mobile-menu-proposal.svg/png: ontwerpschets van het menugedeelte op 390px breed. Dit is geen screenshot van de live site; de bestaande logo-/zoekheader valt buiten deze schets.
- svg-set-overview.svg/png: overzicht op groot formaat, plus de iconen op hun bedoelde 32px-formaat.
- manifest.json: categorienamen, bestandsnamen en ontwerpmaten.

## Ontwerpkeuze

Grotere, optisch gelijkwaardige tekeningen: meubel met wastafel/kraan, wastafelkraan, toilet, waskom, regendouche, vrijstaand bad en wandspiegel. Een lichtblauw iconenvlak van 44px, rijhoogte 68px en bestaande donkerblauwe kleur. Labels blijven de primaire herkenning en toegankelijke naam. De SVG's zijn decoratief; aria-hidden en focusable=false zijn meegeleverd.

## Gecontroleerde bron

Actuele MAIN op 17 oktober: 195326247178, Specificaties en homepage. De eerder gemelde publicatie is nu VERIFIED_ADMIN. Header, drawer en bc-category-icon rechtstreeks uit dit thema gelezen. De bestaande iconen zijn al SVG; de effectieve paden vullen hun 24×24-vak ongelijk. Zo beslaat de huidige wastafeltekening slechts circa 11×6 zichtbare pixels bij de ingestelde 22px-svgbox.

De hoofdgridkolom is 2.4rem, terwijl de iconhouder 2.8rem breed is. De implementatie trekt die maten voor de zeven hoofditems gelijk. bc-category-icon wordt ook vanuit submenu's en homepagecategorieën aangeroepen; daarom een afgebakende mobiele variant gebruiken of de gevolgen per aanroeper controleren.

## Controle en vervolg

De zeven bron-SVG's zijn als XML gecontroleerd: geen scripts, externe resources of rasterafbeeldingen. De PNG's zijn uit het ontwerp geëxporteerd; dit blijven ontwerpschetsen en geen Shopify-screenshots. Eigenaar heeft toepassing van deze zeven iconen op 17 oktober expliciet goedgekeurd.

## Implementatie 17 oktober

Codecheckpoint 4a71dfdf926f17107ac23ba7067971d6f7c13aea op fix/product-cards-2026-10-14. Patch: ../../patches/BC-mobile-category-icons-2026-10-17.patch. Gebaseerd op de verse header.liquid en header-drawer.liquid van MAIN 195326247178. Concept: **195334668554 — BadkamerCity - Mobiel menu SVG**. Vóór wijziging 473/473 bestanden checksum-identiek aan MAIN, processing=false. Concept blijft UNPUBLISHED.

De patch voegt zeven assets en bc-mobile-category-icon.liquid toe; uitsluitend root-items krijgen nieuwe iconen en CSS-modifiers. De gedeelde bc-category-icon, submenu's, panel-ID's, links en sluit-/focuscode blijven gelijk. Tien bedoelde bestanden totaal: twee gewijzigd en acht toegevoegd. Finale readback: 481 bestanden, alle tien bedoelde inhouden exact, overige 471 bestaande bestanden checksum-identiek. MAIN blijft 195326247178 met 473/473 ongewijzigde checksums. Geen wijzigingen aan zoeken, levertijden, producten of live.

Theme Check 10/10 geslaagd, met gebundelde schemafallback toen de docs-updater niet bereikbaar was. LiquidJS-test voor mapping, aliases, onbekende categorie, titelterugval en link-/panelcontract geslaagd; submenu en gedeelde iconbron vergeleken. Patch voorwaarts en omgekeerd gecontroleerd met --ignore-space-change. Tweede read-only diffreview: geen blokkerende fouten.

Testopdracht: NODE_PATH naar de liquidjs-installatie, BC_THEME_PATH naar de gepatchte themabasis, optioneel BC_BASELINE_THEME_PATH naar de verse basis, vervolgens node scripts/test-mobile-category-icons.cjs. De lokale volledige themamap is uitsluitend validatiecontext; alleen de twee verse gewijzigde bronbestanden plus acht nieuwe bestanden zijn geschreven. Het volledige externe manifest bewijst behoud van overige bestanden.

Browsercontrole: echte conceptpagina geopend; previewbalk toont de conceptnaam. Bij 1348px zijn alle zeven root-items met 32×32-SVG en bestaande paneldoelen in de DOM aangetroffen; geen Liquid error. Dit bewijst geen mobiele rendering. Mobiele Shopify-runtime en echte 360px-browser zijn **NOT_TESTED**: de beschikbare browser biedt geen mobiele viewportinstelling. Zie implementation-checks.json voor controlebereik.

Volgende handeling: eigenaar opent in Shopify op telefoon de preview van **BadkamerCity - Mobiel menu SVG**. Controleer labels/chevrons, scrollen, submenu heen/terug en sluiten/heropenen. Publicatie blijft bij eigenaar. Terugzetten in het concept: patch omkeren tegen dezelfde basis, acht toegevoegde bestanden verwijderen; na latere wijzigingen eerst opnieuw vergelijken. De GitHub–themakoppeling en Windows-synchronisatie zijn nog NOT_VERIFIED; daarom is de productiecode als patch bewaard en zijn geen themapaden gepusht.
