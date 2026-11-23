# Mobiele subcategorieën — 17 oktober 2026

Status: USER_APPROVED_UI / IMPLEMENTED_PREVIEW. Eigenaar vraagt toepassing van het getoonde Kranen-submenuvoorbeeld. Dit dossier beschrijft de uitvoering; de getoonde afbeelding was een ontwerp en geen screenshot van werkende code.

## Basis en scope

MAIN 195334865162 bevat alle 13 hoofdiconen en 487 bestanden. Kopie 195335356682, BadkamerCity - Mobiele subcategorieen, is UNPUBLISHED en vóór wijziging 487/487 checksum-identiek, processing=false. Twee bestanden geschreven; finale readback 487 bestanden, beide inhouden exact en overige 485 bestanden checksum-identiek. MAIN blijft 487/487 ongewijzigd. De code gebruikt uitsluitend verse header/drawerbron. De overige lokale themamap is validatiecontext; het externe manifest bewijst behoud van niet-geschreven bron.

Twee gewijzigde themabestanden: sections/header.liquid en snippets/header-drawer.liquid. Nieuwe modifier alleen op niveau 2/3: compacte kop met Terug/titel naast elkaar, lichtblauwe fullwidth CTA, gegroepeerde lijst met lichte lijnen, minimale rij/CTA 48px en leesbare 16px-labels. Geen subcategorie-SVG's. Root 13 iconen, zoekheader, desktopmenu en controller blijven gelijk.

Lange titels en CTA's mogen afbreken. Kop/CTA/lijst hebben flex-shrink:0 zodat de scrollende panelcontainer alle inhoud bereikbaar houdt. Lijst heeft geen overflow:hidden dat focusranden kan afknippen. Eerste/laatste rij hebben passende hoekronding; laatste rij geen dubbele onderrand. CTA-URL blijft die van de huidige categorie. Kranen krijgt ‘Bekijk alle kranen’; veilige meervoudstitels volgen dat patroon, andere titels behouden ‘Bekijk alles in…’.

## Verificatie

Actueel main-menu in menu-snapshot.json: 13 hoofditems, 91 subitems, 152 onderliggende keuzes. Testbestand: scripts/test-mobile-submenus.cjs met BC_THEME_PATH en BC_BASELINE_THEME_PATH. De test vergelijkt 51 subpanelen op alle hrefs, paneltargets/backcontrols en aria-current, plus escaping en ontbrekende sub-SVG's. Twee actieve-linkroutes gecontroleerd. LiquidJS heeft geen Shopify forloop.parentloop; alleen de fixture vangt daarom de buitenste loopindex af. De productiebron en JS zijn daarvoor niet veranderd. Echte Shopify-baseline-DOM: 52 panelen inclusief root, 52 uniek, 0 onopgeloste doelen.

scripts/test-mobile-category-icons.cjs is gericht bijgewerkt: root-only invarianten, alle 13 assets en aliases, onbekende categorie/titelterugval, directe Outlet-link, ongewijzigde rootmarkup/shared renderer/controller. Beide fixtures geslaagd. Patch voorwaarts en achterwaarts gecontroleerd met --ignore-space-change. Theme Check revisie 3 geslaagd na extra flex-/bordercorrectie. Gebundelde schemafallback gebruikt bij onbereikbare docs-updater.

Tweede read-only review: geen routing-/scopeblockers; flexhoogte en dubbele onderrand gericht gecorrigeerd. Volledige echte mobiele bediening/360px-weergave, scroll, focus en back/close/reopen zijn NOT_TESTED. Beschikbare cloudbrowser kan de mobiele viewport niet instellen; desktop-DOMcontrole vervangt die test niet.

## Opslag en vervolg

Aanvullende patch: ../../patches/BC-mobile-submenus-2026-10-17.patch. Toepassen op dezelfde actuele basis, niet op de oudere Git-themesnapshot. Code/overdracht blijven op fix/product-cards-2026-10-14; main krijgt uitsluitend documentatie. GitHub–themakoppeling en Windows-synchronisatie blijven NOT_VERIFIED.

Finale Theme Check revisie 3 voor beide bestanden geslaagd. Echte Shopify-DOMvergelijking vóór/na: 413 navigatie-elementen identiek na normaliseren van de thema-afhankelijke section-ID, 52/52 unieke panelen, nul onopgeloste doelen, 51 lijstgroepen, nul sub-SVG's en 13 rooticonen. ‘Bekijk alle kranen’ heeft /collections/kranen als bestemming; geen Liquid error. Zie implementation-checks.json. Dit bewijst DOM/bron bij 1348px, niet de echte mobiele bediening.

Volgende handeling: eigenaarreview op telefoon van **BadkamerCity - Mobiele subcategorieen**: Kranen → Douchekranen → Terug → Terug, juiste CTA-bestemming, lange titels en doorscrollen. Uitvoering afgerond; concept niet gepubliceerd en geen achtergrondtaak. Terugzetten: uitsluitend deze patch tegen dezelfde conceptbasis omkeren; na latere wijzigingen eerst opnieuw vergelijken. De hoofdiconen blijven daardoor behouden.

Codecheckpoint: d155a13bd9a04764cbbfda97d6beeae6ba1efadc op fix/product-cards-2026-10-14.
