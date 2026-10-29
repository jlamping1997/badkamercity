# ASSORT-02 — duidelijke mobiele categorielijst

30 oktober 2026, Europe/Amsterdam. Eigenaar keurt één compacte uitklapbare lijst goed na review van de gepubliceerde tweekolomsweergave. Status **PREVIEW_READY / NOT_PUBLISHED**.

## Huidige omgeving

MAIN **195916628234 — BadkamerCity - Assortiment overzicht**: de eigenaar heeft ASSORT-01 gepubliceerd. Alle 1.344 livebestanden zijn tijdens deze ronde ongewijzigd gebleven.

Reviewconcept **195915448586 — BadkamerCity - Mobiel assortiment**, UNPUBLISHED, processing=false. Dit ID was de eerdere headerkopie en is nu bewust hergebruikt. De verse volledige themaduplicatie **195917644042 — BadkamerCity - Assortiment reserve** bleek nog in verwerking; die is uitsluitend reserve, geen mobiele reviewversie. Controleer later de kopiestatus voordat die reserve als volledige rollback wordt beschouwd.

Snellere, gecontroleerde basisopbouw: de ongepubliceerde headerkopie verschilde op exact tien paden van MAIN. Die tien bronbestanden zijn uit de actuele MAIN overgenomen; 1.341/1.344 bestanden daarna byte-identiek, drie Shopify-herschreven JSON-bestanden volledig semantisch gelijk. Deze uitzonderingen zijn gesloten op volledige JSON-inhoud, niet genegeerd. Pas daarna zijn de vijf featurebestanden geschreven. Zie [verificatie](deployment-verification.json) en [MAIN-nulmeting](main-before.json).

## Gewijzigd gedrag

- Onder 750px: één bestaande directory direct onder de intro en categoriezoeker, vóór de merkblokken. Het tegeltjesraster is daar verborgen. Geen dubbele directory of aparte mobiele databron.
- Tien hoofdafdelingen met 56×56px vierkante foto, korte mobiele naam, de eerste twee primaire submenuvoorbeelden en een plus/min-teken. Native summary is de gehele tikbare rij; gewone details blijven de fallback zonder JavaScript.
- Openklappen toont eerst Bekijk alle, daarna bestaande subcategorieën en apart Maak het compleet. Meerdere afdelingen mogen tegelijk open. Meer categorieën blijft beschikbaar voor gevulde collecties buiten het menu.
- Mobiele titel Ons assortiment; korte zoekplaceholder Zoek een categorie. De nieuwe mobiele titel is vertaald in NL/EN; de kortere placeholder geldt ook op desktop.
- De directory wordt met echte DOM-verplaatsing naar de mobiele plaats gezet en bij breedtewissel teruggeplaatst. Zo volgen focus en schermlezer dezelfde volgorde als de zichtbare pagina. Zonder JavaScript blijven de native links en details bereikbaar; de directory staat dan op haar oorspronkelijke plaats na de merkblokken.
- Desktop behoudt titel, categoriekaarten, merkblokken en directoryvolgorde. De voorbeeldtekst in mobiele rijen wordt niet als zoekcontext voor alle onderliggende links gebruikt: zoeken op wastafelkraan mag geen keukenkranen opleveren.

## Productiebestanden

`sections/bc-assortment.liquid`, `assets/bc-assortment.css`, `assets/bc-assortment.js`, `locales/nl.json`, `locales/en.default.json`. Geen Admin-menu-/product-/collectiemutaties. De bestaande template is inhoudelijk dezelfde als MAIN; alleen door Shopify gegenereerde JSON-opmaak/metadata verschilt.

## Controles

- [ThemeCheck](themecheck.json): vijf bestanden geslaagd, nul bevindingen. Uitgevoerd in de theme-only-controlemap met de echte dependencies, zonder historische doc-locale-snapshots. Toolkit-instrumentatie via de ondersteunde omgevingsoptie uitgeschakeld.
- [39 lokale cases](controller-tests.json) in [LiquidJS/DOM-test](test-directory.cjs), met 390/800/1366px-model: zoeken, nulresultaten/reset, Escape, Enter, native links, responsief verplaatsen en terugplaatsen, behoud van openstaat, primaire/aanvullende categorieën. Fixturetests zijn geen echte browser of telefoon.
- [Werkelijke browsercontrole](browser-checks.json): uit Shopify gerenderde componentframes 320/390/1024px, effectieve breedte305/375/1009 door scrollbalk. Mobiel tien gesloten afdelingen, alle tien vierkante foto's geladen, geen horizontale/titeloverloop, één directory vóór promoties. 1024px behoudt raster en desktopvolgorde. Gewone desktoppreview behoudt vijf kolommen.
- Op 390: Wastafels geopend; juiste Bekijk alle-link en subcategorieën zichtbaar; wastafelkraan gezocht, vijf resultaten zonder keukenkranen; Escape herstelt geopende Wastafels. Op320 onbekende term en Toon alle categorieën gecontroleerd.
- Navigatie binnen het geïsoleerde frame werd door de bestemming geblokkeerd. Daarom dezelfde link in de gewone previewtab geklikt: `/collections/opzetwastafels`, H1 Opzetwastafels en gelijke canonical bevestigd. Geen storefrontfout geclaimd op basis van iframebeperking.
- Vijf productie-inhouden teruggelezen: drie exact tekstueel, twee JSON semantisch gelijk. Eindconcept1.344bestanden, vijf bedoelde featurepaden plus uitsluitend genormaliseerde ongewijzigde template; overige1.338checksums gelijk aan MAIN. MAIN1.344/1.344ongewijzigd.
- Tijdelijke QA-template exact hersteld: MD5 `c76529d094fb4d534f9cd3352c63f4b4`.

[Screenshot mobiele componenten](mobile-list.jpg) toont de echte gerenderde component naast verschillende breedtes; geen fysieke telefoon of volledige mobiele header/footer. Geen native Safari-, performance-, ranking-, conversie-, Windows- of publicatiecontrole geclaimd.

## Onderhoud, rollback en volgende handeling

Bestaande [categorisatieafspraken](../../CATEGORIZATION_AND_SEO_POLICY.md) en [ASSORT-01-uitbreidregels](../2026-10-29/README.md) behouden. De mobiele foto's/namen gebruiken dezelfde editorblokken; de submenuvoorbeelden komen uit het bestaande menu en slaan aanvullende links over.

Rollback: vijf featurebestanden terug uit baseline; die zijn de actuele MAIN-bron vóór ASSORT-02. De inhoudelijk gelijke list-collections-template hoeft voor deze feature niet te veranderen. Geen volledige Git-root uploaden. Publicatie blijft volgens AGENTS.md bij de eigenaar.

**Exact volgende handeling:** eigenaar bekijkt concept195915448586 op een echte telefoon en publiceert via Shopify bij akkoord. Daarna MAIN en storefront opnieuw verifiëren. Geen verdere schrijver of achtergrondtaak van deze sessie; de eventuele Shopify-kopie is een native platformproces.
