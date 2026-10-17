# Mobiele categorie-iconen — eerste ontwerp

Status: DESIGN_REVIEW_ONLY. 17 oktober 2026, Europe/Amsterdam. Eigenaar werkt vandaag vanaf mobiel; Wiesbaden blijft openstaan. Eerste zeven hoofdcategorieën uit de aangeleverde schermafbeelding. Dit is een concreet SVG-voorstel, geen gewijzigde Shopify-versie.

## Bestanden

- Zeven originele bc-nav-*.svg-bronbestanden, 32×32 viewBox, stroke 1.65, ronde lijnuiteinden en currentColor.
- mobile-menu-proposal.svg/png: ontwerpschets van het menugedeelte op 390px breed. Dit is geen screenshot van de live site; de bestaande logo-/zoekheader valt buiten deze schets.
- svg-set-overview.svg/png: overzicht op groot formaat, plus de iconen op hun bedoelde 32px-formaat.
- manifest.json: categorienamen, bestandsnamen en ontwerpmaten.

## Ontwerpkeuze

Grotere, optisch gelijkwaardige tekeningen: meubel met wastafel/kraan, wastafelkraan, toilet, waskom, regendouche, vrijstaand bad en wandspiegel. Een lichtblauw iconenvlak van 44px, rijhoogte 68px en bestaande donkerblauwe kleur. Labels blijven de primaire herkenning en toegankelijke naam. De SVG's zijn decoratief; aria-hidden en focusable=false zijn meegeleverd.

## Gecontroleerde bron

Actuele MAIN op 17 oktober: 195326247178, Specificaties en homepage. De eerder gemelde publicatie is nu VERIFIED_ADMIN. Header, drawer en bc-category-icon rechtstreeks uit dit thema gelezen. De bestaande iconen zijn al SVG; de effectieve paden vullen hun 24×24-vak ongelijk. Zo beslaat de huidige wastafeltekening slechts circa 11×6 zichtbare pixels bij de ingestelde 22px-svgbox.

De hoofdgridkolom is 2.4rem, terwijl de iconhouder 2.8rem breed is. Bij latere implementatie die maten gelijktrekken. bc-category-icon wordt ook vanuit submenu's en homepagecategorieën aangeroepen; daarom een afgebakende mobiele variant gebruiken of de gevolgen per aanroeper controleren.

## Controle en vervolg

Alle zeven SVG's als XML gecontroleerd, zonder scripts, externe resources of rasterafbeeldingen. PNG's rechtstreeks uit de SVG's geëxporteerd en visueel beoordeeld. Nederlandse labels passen op één regel bij de voorgestelde maatvoering. Werkelijke mobiele browser-/Shopify-previewcontrole en submenu-implementatie zijn NOT_TESTED.

Volgende stap: eigenaar beoordeelt de herkenbaarheid en stijl van deze zeven iconen. Daarna de gekozen stijl per categorie verfijnen, overige categorieën volgen en pas vervolgens de bestaande drawer gericht in concept aanpassen. Menulinks, focusbeheer, sluitknop, panel-ID's en data-bc-mobile-attributen behouden. Geen wijzigingen aan zoeken, levertijden, productgegevens, desktopmenu of Shopify-live uitgevoerd.
