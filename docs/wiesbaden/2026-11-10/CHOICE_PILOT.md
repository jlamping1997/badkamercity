# Wiesbaden keuzemenu's — overdracht 10 november 2026

**Status: zes keuzegroepen voor51artikelen aangebracht en gecontroleerd in het bestaande ongepubliceerde concept. Eén echte winkelwagenproef met handdoekhouder24.3820 geslaagd en testartikel verwijderd. UniMatch-winkelwagenproef en native mobiel staan nog open. Niet gepubliceerd.**

Het concept is bij de vorige ronde gelijkgetrokken met het actuele live thema. Deze uitbreiding behoudt die samengevoegde basis en alle vijf eerdere groepen. Geen extra thema aangemaakt.

| Familie | Artikelen | Keuzes | Conceptvoorbeeld |
|---|---:|---|---|
| Maki vouwbare nisdeur, helder glas/chroom |6|Breedte80/90/100cm; scharnierzijde Links/Rechts|[Maki](https://badkamercity.nl/products/wiesbaden-maki-nisdeur-vouwbaar-links-800-x-2000-x-8-mm-nano-helder-glas-chroom-20-3720?preview_theme_id=196416504074&_fd=0&_sc=1&_ab=0)|
| Derde generatie douchegoot met flens en rooster |8|Lengte50t/m120cm, stappen10cm|[Met rooster](https://badkamercity.nl/products/wiesbaden-3e-generatie-douchegoot-met-flens-en-rooster-50-x-7-cm-rvs-33-4168?preview_theme_id=196416504074&_fd=0&_sc=1&_ab=0)|
| Derde generatie douchegoot met flens, zonder rooster |8|Lengte50t/m120cm, stappen10cm|[Zonder rooster](https://badkamercity.nl/products/wiesbaden-3e-generatie-douchegoot-met-flens-zonder-rooster-50-x-7-cm-rvs-33-4140?preview_theme_id=196416504074&_fd=0&_sc=1&_ab=0)|
| Uovo LED-spiegel, dimbaar en verwarmd |7|Formaat70/80/90/100/120/140/150cm|[Uovo](https://badkamercity.nl/products/wiesbaden-uovo-spiegel-ovaal-met-led-dimbaar-en-spiegelverwarming-70-cm-38-4163?preview_theme_id=196416504074&_fd=0&_sc=1&_ab=0)|
|304enkele handdoekhouder|2|Lengte25/60cm|[Handdoekhouder](https://badkamercity.nl/products/wiesbaden-304-handdoekhouder-enkel-25-cm-rvs-24-3822?preview_theme_id=196416504074&_fd=0&_sc=1&_ab=0)|
|UniMatch douchearm met plafondbevestiging|20|Kleur/afwerking; lengte15/20/30cm|[UniMatch](https://badkamercity.nl/products/wiesbaden-unimatch-douchearm-met-plafondbevestiging-20-cm-chroom-29-3810?preview_theme_id=196416504074&_fd=0&_sc=1&_ab=0)|

De twee gootfamilies houden hun verschillende leveringsinhoud. Uovo60cm zonder verwarming blijft buiten de verwarmde familie. Vaste eigenschappen krijgen geen menu. Bij Maki blijven Links/Rechts fabrikantbenamingen; kijkrichting en stelbereik zijn niet aangevuld.

## UniMatch: kleine uitbreiding van het bestaande systeem

Twintig bestaande artikelen vormen één plafondarmfamilie. De zeven exacte afwerkingen zijn Chroom, Geborsteld koper, Geborsteld messing PVD, Geborsteld staal PVD, Mat zwart, Geborsteld brons koper PVD en Gunmetal PVD.30cm/GeborsteldstaalPVD ontbreekt in de actuele winkelmatrix. Die combinatie is uitgeschakeld; dit is geen claim over wereldwijd fabrikantassortiment.

De bestaande referenties bevatten per lengte zes of zeven actuele producten. Liquid gebruikt deze voor de actuele variantprijs en eerste foto; JavaScript controleert product-ID, variant-ID, SKU, handle en één variant voordat het de gegevens gebruikt. Alleen passende kleuren worden op de actuele prijs van dezelfde lengte geordend. Bij ontbrekende of ongeldige prijs blijft de oorspronkelijke gehele volgorde behouden. De groepsasset bevat geen vaste prijzen of foto's.

Zes kleuren zijn direct zichtbaar; een geselecteerde zevende kleur blijft zichtbaar. Uitklappen toont alle afwerkingen. Ontbrekende en dubbele volledige combinaties blijven niet selecteerbaar. Een expliciete generieke groepsoptie activeert dit gedrag; bestaande Hotbath-/Verlavio- en de vijf eerdere Wiesbaden-groepen zijn behouden.

De eerste echte preview bracht een stijlprobleem aan het licht: foto's waren juist geladen maar met de oude300%-uitsnede vrijwel wit. Het conditionele attribuut `data-bc-compact-colors="true"` activeert nu de bestaande100%/contain-fotostijl. Geen nieuw stylesheet of afzonderlijke Wiesbaden-renderer gebouwd. Bij terugkomst vanuit bfcache herlaadt uitsluitend deze aangemelde groep de pagina om hoofdprijs en kandidaatfeiten samen te verversen.

## Bewijs en grenzen

- Deze ronde:20nieuwe `custom.switch_group`-velden beveiligd aangemaakt en exact teruggelezen; totaal51. Bestaande kleurreferenties en de overige vergeleken productidentiteiten, prijzen, foto's, publicatievelden en waarden bleven gelijk. Metafields zijn winkelbreed; de nieuwe weergaveroutes staan uitsluitend in het concept.
- Alle51conceptpagina's leveren de juiste titel, artikelcode, prijs, formuliervariant en eerste afbeeldingsbestand/revisie. Alle20UniMatch-pagina's leveren de juiste begrensde asset en samen134exacte actuele kandidaatfeiten.
- Echte Chrome-desktop:20cm chroom→20cm staal→15cm staal→15cm zwart→30cm zwart. De andere keuze bleef behouden. Ontbrekende staal/30cm-combinatie, uitklappen, Enter-keuze, zes zichtbare kleuren met gekozen zevende, herladen en terug naar15cm zwart gecontroleerd. Foto's geladen op juiste42px/contain-kadering; geen horizontale overloop bij1363px.
- De echte winkelwagenproef geldt uitsluitend voor de60cmhouder24.3820: één artikel via de PDP-knop toegevoegd, variant53859770695946, juiste foto en €54,99. Daarna via de eigen verwijderlink weggehaald; lege beginstand hersteld. Geen bestelling of betaling.
- Finale volledige themavergelijking: MAIN196395073802 telt1.401files, concept1964165040741.407;1.397gedeeld identiek, zes nieuwe assets en vier gewijzigde files. MAIN is ongewijzigd. Router-MD5 `e37073d63534dfff2f0175f1355ace11`; de zes groepsroutes staan vóór de oude gedeelde assetrevisievoorwaarde.
- Lokale regressies:866oude groepspagina's,31eerder gebouwde pagina's en21Verlavio-gevallen identiek;20UniMatch-pagina's,152geldige wissels,8ongeldige en20dubbele combinaties gecontroleerd. De zes baseline/voorstel-Liquid-syntaxiscontroles slagen, inclusief de uiteindelijke stijlkoppeling.

**Open:** native mobiel/fysiek toestel, daadwerkelijke UniMatch-winkelwagentoevoeging en volledige eigenaarsreview vóór publicatie. De houderproef vervangt deze niet. De officiële externe codevalidator was eerder automatisch geweigerd wegens codeoverdracht en is niet opnieuw geprobeerd; geen ThemeCheck-PASS. Voorraad, levertijd en ontbrekende technische eigenschappen zijn niet ingevuld. Geen lokale Windows-Gitcontrole geclaimd.

## Bronholds blijven apart

Alleen wiesbaden.nl en officiële Korver-gegevens zijn fabrikantbronnen. Onvolledige technische bronvelden van29.3852/29.3863 zijn niet van andere kleuren geleend. Caral vraagt exact setinhoud-/componentbewijs en correcte bestaande inbouwdeelpartners;29.4115bevat het deel al. Cadans heeft officiële hoge uitvoeringen, maar de drie onderzochte hoge SKU's ontbreken in de winkel; daarom geen fictieve laag/hoog-keuze. Slide houdt acht onopgeloste dubbele combinaties; geen willekeurige eerste SKU of verzonnen oud/nieuw-menu.

## Gericht herstel en vervolg

Lees actuele rollen, bronhashes en velden opnieuw. Voor W02 verwijder uitsluitend de twintig deze ronde aangemaakte groepsvelden als identiteit en waarde nog exact overeenkomen met het privébewijs; oorspronkelijke kleurreferenties behouden. Neem vervolgens alleen W02's twee routerregels en de begrensde asset weg. Zonder die twee regels is de router bytegelijk aan de voorafgaande vijf-groepenversie, MD5 `f4a640149ba4fe1198ad5d0b2162081d`.

De opt-in-hunks in drie bestaande weergavebestanden kunnen alleen gericht worden teruggedraaid als geen later werk ze gebruikt. Laat de vijf eerdere routes/31velden en twaalf samengevoegde basisbestanden intact. Een oude volledige themefile terugzetten is geen geschikt herstel. Product-, thema- en testbewijzen staan in het bestaande privéoverdrachtpakket onder `continuation-batch/`; de code staat in de actieve Git-branch `fix/product-cards-2026-10-14` onder `shopify/current/`.

**Volgende handeling:** de zes conceptgroepen gericht op mobiel en het UniMatch-winkelwagenartikel toetsen voordat de eigenaar publiceert. Daarna gericht verder met Caral-componentbewijs. Andere SEO-/Ads-werkstromen blijven behouden; geen actieve schrijver na overdracht.
