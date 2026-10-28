# Cartnotification — inhoud en lifecycle afzonderlijk

**Doel:** de bevestiging moet bij het laatst bevestigde artikel horen en voorspelbaar kunnen sluiten. Hoofdcontract: [cart en feedback](../CART_AND_FEEDBACK.md). Bronnen: assets/cart-notification.js en de gelijknamige snippet/CSS, opnieuw checksumgelijk gelezen. Resultaten CN-01 t/m CN-07 in [isolated-results.json](../../evidence/2026-10-28-micro/isolated-results.json).

## Functies en eigenaarschap

| Functie | Invoer / voorwaarde | Effect / resultaat |
| --- | --- | --- |
| renderContents(state), :62 | key of items[0].key; optionele sections | Kiest itemkey, vervangt sectioninhoud waar mogelijk en roept open aan |
| getSectionsToRender, :76 | Huidige itemkey | Productsection met specifieke selector, cart-CTA en badge |
| getSectionInnerHTML, :84 | HTML-string + selector | Gevonden innerHTML of null; geen request |
| open, :35 | Bestaande dialogroot | Annuleert close/frame, bewaart oude scrollstijlen, showModal en active op volgend frame |
| close, :50 | Dialog open, niet al closing | Verwijdert active; sluit na 230ms of 0 bij reduced motion |
| close-event, :19 | Dialog inmiddels echt dicht | Herstelt documentstijlen en verbonden openerfocus |
| isOutside, :28 | Event target is dialog | Boundingbox bepaalt of backdropklik echt buiten de dialog is |

Die verantwoordelijkheden niet door elkaar halen: open kan geen onjuiste artikelinhoud herstellen; renderContents bevestigt niet zelf dat een POST gelukt is. De caller moet het koopresultaat beoordelen. Een timer is geen bewijs dat de server niets meer doet.

## Inhoudsfout CART-F01: oude artikelinformatie bij ontbrekende section

Reproductie met de ongewijzigde broncode in een afgesloten DOM:

1. Geef een volledige succesvolle response voor fictief artikel A; de productinhoud toont A.
2. Geef daarna key B met een ontbrekende productsection, of met die section op null.
3. Regel 68 slaat dit over. Er wordt niets uit de oude productcontainer verwijderd.
4. open wordt alsnog aangeroepen; de productinhoud blijft A terwijl cartItemKey B is.

**Uitkomst: DEFECT_REPRODUCED**, CN-02 en CN-03. De onvolledige serverrespons is gesimuleerd; er is niet vastgesteld dat Shopify deze fout in de onderzochte browsersessie heeft geleverd. Het probleem zit in de fouttolerantie van de component, niet in een aangetoonde foutieve bestelling.


Shopify beschrijft in de [Cart API-documentatie](https://shopify.dev/docs/api/ajax/reference/cart#bundled-section-rendering) dat sectionrendering na de datawijziging gebeurt en een falende section als null kan terugkomen zonder dat de HTTP-status die renderfout weerspiegelt. De null-stimulus sluit dus aan op een gedocumenteerde API-mogelijkheid. Dat bewijst nog steeds niet dat deze winkel die response in deze ronde heeft ontvangen; juist daarom mag herstel niet stil een tweede kooprequest sturen.

Ter vergelijking: bij een HTML-string waarin de gevraagde productselector niet voorkomt, maakt regel 71 de productcontainer wél leeg (CN-04). “Geen matching selector” en “geen bruikbare sectionstring” hebben dus verschillende gevolgen. De guard tegen een oude inhoud is maar op één van die paden aanwezig.

| Reactie | Huidige bron | Gewenst veiligheidscontract |
| --- | --- | --- |
| Volledige B-productsection | Vervangt A door B | Behouden; CN-01 |
| HTML-string zonder B-selector | Leegt productcontainer | Geen oud artikel tonen; eventuele generieke feedback afspreken |
| Productsection ontbreekt/null | Laat A staan en opent | Oude productspecifieke inhoud ongeldig maken; geen A als B presenteren |
| Badge/CTA ontbreekt | Afzonderlijke update wordt overgeslagen | Compleet responsecontract beoordelen; geen nieuwe add uitvoeren om markup te herstellen |

**Prioriteit: P1-kandidaat**, omdat de bevestiging de identiteit van het zojuist toegevoegde artikel kan verwarren. Geen gemeten frequentie of sitebrede impactclaim.

Kleinste voorstel: behandel een ontbrekende/niet-string productsection expliciet, wis de oude productspecifieke inhoud en toon een afgesproken veilige cartverwijzing/generieke bevestiging wanneer de koopactie zelf al bevestigd is. Alternatief: valideer het volledige vereiste sectioncontract vóór productspecifiek openen. Geen automatische tweede POST. Een fix moet beide ontbrekende-responsecases en de geldige vervanging controleren.

## Lifecycle: wat al beschermt

CN-05 bevestigt in de gecontroleerde stub dat sluiten → onmiddellijk heropenen de oude close-timer annuleert. Na een volgende echte stubclose komen overflow, scrollbarGutter en de verbonden opener terug. CN-06/07 bevestigen de codekeuze 230ms versus 0ms bij cancel/reduced motion. De native dialogmethoden en frames/timers zijn daarbij bewust nagebootst; dit is geen browserfocus-/animatievrijgave.

Het component houdt closing, closeTimer, openFrame, previousOverflow, previousScrollbarGutter en activeElement apart bij. Een veilige wijziging behoudt hun eigenaar: de close-eventhandler ruimt op nadat dialog.close heeft plaatsgevonden. Tijdens heropenen mag een oude close-event geen nieuwe modalcontext opruimen; de bestaande open-check beperkt dat pad.

## Nog te controleren

Echte native Escape/backdrop/Tab, aanraken en slepen over de backdrop, groot productblok, herhaalde koopbevestiging, ontbrekende sectionresponse in een transportstub die de volledige caller bevat, mobiel/safe-area en iOS-scroll. De echte popup is in deze ronde niet geopend door een koopactie. Het apart geteste Sunshower-hulpdialog heeft een andere controller en bewijst dit popupcontract niet.
