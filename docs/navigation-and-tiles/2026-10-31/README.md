# NAV-03 / TILE-02 — compact menu en tegelinformatie

**31 oktober 2026 · PREVIEW_VERIFIED / OWNER_REVIEW_PENDING.** Codecheckpoint `b7a5308038965bf874e06ed5115aa9431eb381d3`, branch `fix/product-cards-2026-10-14`. Geen actieve schrijver na overdracht.

## Publicatie en basis

De eigenaar publiceerde de herstelde FIX-01: **MAIN195974824202 — BadkamerCity - Betrouwbaar bestellen en filters**. De vorige MAIN195947036938 was UNPUBLISHED en liep alleen op de 21 FIX-01-featurepaden achter. Deze 21 bronbestanden zijn tegen verse MAIN-checksums gecontroleerd en naar dat concept gesynchroniseerd. Daarna was het concept op **alle 1.355 paden gelijk** aan MAIN, vóór de nieuwe wijziging. Geen nieuwe volledige themakopie of MAIN-write.

Het concept heet nu **195947036938 — BadkamerCity - Compact menu en tegelinformatie**. Finaal 1.356 bestanden: zes gewijzigde bestaande bestanden en één nieuwe snippet, exact zeven bedoelde afwijkingen ten opzichte van MAIN. Alle zeven checksums teruggelezen. MAIN bleef op alle 1.355 paden ongewijzigd; geen publicatie.

[Finale rollen/diff](final-verification.json) · [bronhashes](source-provenance.json).

## Gewijzigd contract

- **Categoriebalk:** één rij van 48 CSS-pixels vanaf 990px. De controller meet de echte item- en beschikbare breedtes, ook na fontladen en resize. Het passende begin van het bestaande menu blijft zichtbaar; de rest staat met alle bestaande sublinks onder **Meer categorieën**. Geen horizontale rail of tweede rij. Wanneer alle elf categorieën passen, verdwijnt Meer.
- **Smalle schermen:** tot 989px blijft het bestaande mobiele menu eigenaar. Geen nieuwe categorie-/menudata aangemaakt of verwijderd. Op brede tablets kan de enkele rij verschijnen; bediening werkt zonder hover via de disclosureknop en bestaande touchroute.
- **Zonder scripts:** één native details-knop **Alle categorieën** toont alle elf menutakken. De server rendert de bestemmingen; er is geen extra catalogus- of navigatie-API nodig.
- **Calculator:** verse keuze begint op **1 m²** en behoudt **10% snijverlies**. Een geldige expliciet opgeslagen oppervlakte of handmatige dozenkeuze gaat vóór die verse default. Ongeldige invoer wist nog steeds oude totalen en blokkeert kopen. Handmatige dozen krijgen geen dubbel snijverlies.
- **Tegelinformatie:** het i-knopje naast Bereken je bestelling opent een native dialog met benoemde titel, Sluiten, Escape, focusterugkeer en herstel van bestaande body-scrollstand. De uitleg zegt dat een vloertegel ook op de wand kan, mits ondergrond/lijm het gewicht dragen; een wandtegel is niet geschikt voor de vloer. NL en EN bijgewerkt. De bestaande snijverlies-uitleg blijft apart.

De nieuwe overflow-snippet leest hetzelfde bestaande header-menu. Dit is geen vaste selectie van populaire categorieën en geen wijziging van de catalogus. Een laptop met browserzoom heeft minder CSS-ruimte; de meting gebruikt de beschikbare ruimte in plaats van een apparaattype.

## Bewijs

[Browserbewijs](browser-evidence.json) gebruikt de echte Shopify-conceptmarkup, CSS, lettertypen en oorspronkelijke runtime in same-origin srcdoc-frames. Breedtes **320,390,768,820,989,990,1024,1180,1280,1366,1440,1600,1920px**; een echte verticale scrollbar is aanwezig. Dertienmaal document-scrollWidth = clientWidth. Vanaf990px één rij en48pxcategoriebalk; geen lijstrail-overloop.

| Voorbeeldbreedte | Gemeten categorieën in de rij | Onder Meer |
| --- | --- | --- |
| 990 / 1024 | 7 | 4 |
| 1180 / 1280 | 9 | 2 |
| 1366 / 1440 / 1600 / 1920 | 11 | 0 |
| 320–989 | Desktopbalk verborgen | Bestaand mobiel menu |

Dit zijn meetpunten met deze labels/fonts en scrollbar, geen hardgecodeerde aantallen of universele apparaatgrenzen. Op1280px opent Meer direct onder de balk, blijft binnen het scherm en toont Verwarming en ventilatie plus Merken. ArrowDown opent en focust de eerste zichtbare bestemming; Escape sluit en brengt focus terug naar Meer. De trigger heeft een expliciete buttonrol. Op820px: Menu → Douche → Terug → Escape gecontroleerd. Een geopend mobiel menu wordt bij terugschakelen naar1366px gesloten, zonder achtergebleven bodylock. Eindtoestanden na de daadwerkelijke open-/resize-events gemeten; onmiddellijke tussenframes gelden niet als eindresultaat.

De echte tegel-PDP `/products/porcelanosa-taranto-marfil-mat-120-x-59-6-cm` toont1m²/10%/1doos/1,43m²/€142,93. 10m² rekent11m² benodigd →8dozen →11,44m² →€1.143,44. 0m² geeft fout, geen oud totaal en disabled bestellen. De echte native info-dialog opent, Escape sluit, focus keert terug en body-overflow wordt hersteld. Geen cart/add, order, checkout of formulierinzending uitgevoerd.

[Tien lokale regressies](tile-regressions.json): echte buybox-lifecycle en rekenkern in happy-dom, synthetische artikel-/sessiedata. Default, geldige/ongeldige invoer, handmatige dozen, opgeslagen keuzes, niet-bestelbaar product en popupbedrading PASS. Reproduceer met `node scripts/component-audit/nav03-tiles.mjs /pad/resultaat.json`. Geen native-browserclaim uit happy-dom.

[Theme Check revisie3](theme-check.json): alle zeven gewijzigde files geldig. De eerste poging signaleerde een onjuist LiquidDoc-arraytype (verwijderd) en onvolledige/gedupliceerde validatorcontext uit de historische repositorydocumentatie. Herhaald in een schone theme-only map met de verse vereiste dependencies; revisies2/3 slagen. Geen afhankelijkheden of private instellingen naar MAIN geschreven. De oude FIX-01-provenance blijft historisch; de nieuwe default vervangt expliciet het eerdere lege-startcontract.

De bestaande QA-template `templates/page.bc-mobile-qa.liquid` is na de proef exact hersteld naar371bytes / MD5 `24ae4cff55afe7f2453e4e9b6a0c2479`. Geen extra QA-pad achtergelaten. Een extra screenshotuitsnede gaf een protocoltimeout; de geslaagde viewportfoto van de geladen echte concept-homepage is de visuele controle. Browserbeelden bevatten geen klant-/ordergegevens en zijn geen publieke repositorybijlage.

## Grenzen, terugzetten en volgende handeling

Geen fysieke iPhone/tablet/Windows of volledige checkout-/performance-/mailvrijgave. Geen echte touch-hardware- of browserzoommeting; de viewportproeven meten CSS-breedtes. De twee bekende body/hash-uitzonderingen voor settings_data en retourtemplate zijn geërfd en niet opgelost of geüpload. De Git-root blijft geen complete actuele MAIN-snapshot.

Terugzetten: eerst actuele rollen/hashes lezen; herstel alleen de zes bestaande featurebestanden uit de nog passende MAIN-baseline en verwijder de nieuwe overflow-snippet pas na herstel van de header. De oorspronkelijke stylesheet is aanvullend bewaard in [baseline](baseline/assets/bc-porcelanosa-buybox.css), omdat die file vóór deze taak niet in de historische Git-root stond. Overige bronbytes staan in codebasis b55f05f. Geen volledige oude Git-root uploaden.

**Exact volgende handeling:** eigenaar bekijkt **BadkamerCity - Compact menu en tegelinformatie** op eigen laptop en tablet/telefoon, en publiceert daarna zelf. Retourmailbewijs en offerteverificatie blijven de bestaande afzonderlijke open taken.
