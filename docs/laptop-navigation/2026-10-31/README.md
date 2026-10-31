# NAV-02 — categorieën zonder horizontaal schuiven

31 oktober 2026. De eigenaar toont de laptopheader en wil alle categorieën direct kunnen bereiken, met goede laptop-, desktop- en mobiele versies. Bestaande actieve branch `fix/product-cards-2026-10-14`; geen Windows-/fysieke laptopcontrole.

## Bron en veilige werkstand

Actuele MAIN **195948839178 — BadkamerCity - Retourknop in header**,1354files. De retourpagina is sinds RET-03 gepubliceerd en blijft bereikbaar. Bestaand UNPUBLISHED **195947036938**, eerder Retour aanmelden en footer, hergebruikt: de volledige verse manifestvergelijking toont precies één achterlopend headerbestand en1353overige identieke paden. Alleen de header uit de huidige MAIN gesynchroniseerd; daarna opnieuw volledige **1354/1354 MD5-pariteit** bewezen vóór de navigatiewijziging. Concept hernoemd naar **BadkamerCity - Categorieen zonder schuiven**. Zo is een volledige nieuwe kopie vermeden, zonder andere conceptfeatures te overschrijven. Offerteconcept blijft apart.

Oorspronkelijke header MD5 `78a34a0d90ff1df449f3f6ac05db476d`; finale header `7870254f401e4fb747bcd9beb6140c89`. Alleen `sections/header.liquid` blijvend gewijzigd. MAIN1354/1354ongewijzigd; concept1354files met exact één afwijkend pad en text-exact readback. Geen MAIN-write/publicatie. [Pariteit](parity.json), [eindread](final-verification.json).

## Oorzaak en gedrag

De desktopbalk gebruikte een ongebroken flexrij met overflow-x:auto, een1440pxmaximum,16pxletters en twee JS-schuifknoppen. In de echte browser was de lijst1427pxbreed tegenover1228pxzichtbare ruimte. Daardoor zaten de laatste categorieën buiten beeld, ook wanneer het scherm op zichzelf breed leek.

| CSS-viewport | Nieuwe indeling |
| --- | --- |
| Tot989px | Bestaand mobiel menu; desktopcategoriebalk verborgen |
| 990–1359px | Twee vaste, gecentreerde rijen met6en5categorieën;14pxletters, knoppen minimaal48pxhoog |
| Vanaf1360px | Alle11categorieën op één rij met15pxletters; max1600px, CSS-wrap als vangnet |

Alle labels en bestemmingen zijn behouden. De schuifknoppen, scrollbar-opmaak en bijbehorende scrollcontrollercode zijn verwijderd. Twee oude tekstinstellingen voor de voormalige pijllabels blijven om configuratieruis te voorkomen; ze renderen geen knoppen meer. Geen nieuwe library, asset, API, klanttekst of vertaling. De dropdownpanelen gebruiken nog de volledige onderkant van de categoriebalk, ook met twee rijen. Bestaande Escape-, focus-, touch- en hoverhandlers zijn behouden. De bestaande sticky-header wordt bij desktop-resize om een hoogtemeting gevraagd als dat element aanwezig is; de mobiele meetcode blijft eigenaar van zijn eigen offset.

## Verificatie

**PREVIEW_VERIFIED / OWNER_PUBLICATION_PENDING.** Theme Checkrevision1SUCCESS en Node-JavaScriptsyntaxcheckPASS. De validator heeft de ontbrekende lokale doccache vernieuwd en daarna de volledige huidige runtimeboom gebruikt. Geen Lighthouse-/snelheidsclaim.

- Twaalf browsercomponentframes met echte conceptmarkup, styles en originele runtime:390,989,990,1024,1280,1348,1359,1360,1366,1440,1536,1920CSS-pixels. Alle document-scrollWidths gelijk aan clientWidth. Desktop:11links binnen beeld, lijstscrollWidth gelijk aan lijstbreedte, nul schuifknoppen, geen tekstafsnijding; exact6+5 of11opéénrij. Mobiel: categoriebalk verborgen en bestaande menu/zoekopmaak behouden. [Metingen](browser-measurements.json).
- Laptop1280: ArrowDown opent Kranen, focus gaat naar Wastafelkranen; Escape sluit en brengt focus terug naar Kranen. Ook Spiegels en verlichting uit de tweede rij opent; beide panelen beginnen op217px, direct onder de hele balk216.59px.
- Werkend frame gewisseld van1366naar1280naar989en terug1366: twee rijen→mobiel→één rij. Mobiel menu opent en sluit bij terugschakelen, bodylock verdwijnt, mobiele headerhoogte142px en desktophoogte170px worden correct hersteld. De toestand is na het renderen gemeten; onmiddellijke tussentoestanden vóór de media-/animatieframes zijn geen eindresultaat. [Interacties](browser-interactions.json).
- Merken daadwerkelijk via de gewone conceptwebsite aangeklikt: `/collections?view=merken`, H1 Onze merken. Navigatie naar die echte Shopify-pagina werd in een testiframe geweigerd wegens embedding; daarom is de normale bovenliggende pagina gebruikt. Geen claim dat de iframebestemming werkte. [Doorklik](top-level-navigation.json).
- Echte homepage bekeken: alle11categorieën zichtbaar zonder schuifbalk/pijlen. [Beeld](laptop-navigation.jpg). De browser had1348pxcontentruimte en een iets bredere CSS-media-viewport; de precieze breakpointmetingen hierboven zijn de componentframes. Een poging tot extra uitsnede gaf een screenshot-timeout; het eerder geslaagde viewportbeeld is het bewijs, geen nieuw samengesteld beeld.
- Tijdelijk uitsluitend de bestaande QA-template in dit concept gebruikt en exact hersteld naar371bytes/MD5 `24ae4cff55afe7f2453e4e9b6a0c2479`. Geen extra publieke route of runtimebestand achtergelaten. Geen account-, Page-, product-, order-, prijs-, voorraad-, label- of mailmutatie.

## Vrijgave en herstel

Eigenaar beoordeelt **BadkamerCity - Categorieen zonder schuiven** via Webshop→Thema’s→Voorbeeld en publiceert dat concept. Volgens AGENTS.md blijft themapublicatie bij de eigenaar; huidige MAIN blijft de terugval. De retour-Page is al zichtbaar, dus daarvoor is geen nieuwe publicatie nodig. De oudere offertepreview kan in het concept zichtbaar zijn maar blijft volgens zijn bestaande instellingen op MAIN uit; deze taak activeert die niet.

Rollback vóór publicatie: huidige MAIN aanhouden. Bij alleen code terugzetten de header uit codecheckpoint `6c3c7aa2d55f25d077b86baf85a104a3c11ee74a` op de uitvoeringsbranch herstellen; geen volledige Git-root uploaden. Na publicatie kan de eigenaar het huidige MAIN-thema195948839178 terugzetten. De retourmailboxproef blijft afzonderlijk open. Geen fysieke iPhone-/Windows-/zoomproef of checkouttest geclaimd.
