# Afzonderlijke onderdelen — functies, staten en tegenvoorbeelden

**28 oktober 2026 · DOC-03A, met een beperkte DOC-02B-desktopcontrole.** Deze laag gaat onder de [componentdossiers](../README.md): niet alleen welke bestanden samenwerken, maar wat een afzonderlijke functie accepteert, wijzigt en moet tegenhouden.

| Onderdeel | Functies / beslissingen | Resultaat |
| --- | --- | --- |
| [Cartnotification](CART_NOTIFICATION.md) | renderContents, open, close, native close-event | Eén onvolledige-responsefout in twee stimuli gereproduceerd; normale vervangings-/sluitcontroles |
| [Sunshower actieregels](SUNSHOWER_ACTIONS.md) | adding/navigating, opties, set-add, native submit | Productwissel tijdens pending set-add gereproduceerd; overige aantallen/foutpad apart beschreven |
| [Keuzematch en terugval](CHOICE_RESOLUTION.md) | findExactMatch, getDisplayType, loadSwitcherData, catalog.find | Goede guards bevestigd; netwerkfout en semantische datafout geven verschillende uitkomst |
| [Aantal, identiteit en payload](QUANTITY_AND_IDENTITY.md) | validIdentity, quantity, handleSubmit, items[] | Exacte identiteit, geldige aantallen en uncertain-blokkade gecontroleerd |

Lees eerst de [meet- en bewijsmethode](../../evidence/2026-10-28-micro/README.md). Er zijn **15 geïsoleerde gevallen**: 10 controles, 3 defectreproducties en 2 bevestigde grenzen. De drie defectgevallen zijn **twee verschillende problemen**, niet drie nieuwe bugs. Alle testproducten, prijzen en requests zijn fictief. Geen echte cartmutatie of storefrontfix uitgevoerd.

Bron: 22 opnieuw opgehaalde MAIN-bestanden, alle byte-/groottegelijk aan hun actuele metadata. De uitvoerende vier JS-bronnen zijn vóór iedere replay op SHA-256 gecontroleerd. De tests gebruiken echte broncode met nagebootste externe afhankelijkheden; dat bewijst gedrag onder die stimuli, niet hoe vaak de echte server een dergelijke response geeft.

Desktopbrowser: externe collectiekaart met zichtbare CTA; Sunshower-maathulp opent/sluit met Escape en geeft focus terug; galerij gaat na asynchrone afhandeling van 1 naar 2. Viewport 1363×936, bestaande sessie met preview-UI. Mobiel en volledige kaartvergelijking blijven open. De nagebootste DOM heeft wel een testbreedte, maar is geen mobiele browser- of visuele vrijgave.

De kleinste correcties zijn als voorstellen vastgelegd. Een volgende implementatieronde moet dezelfde tegenvoorbeelden behouden, in een geverifieerd concept werken en een echte browsercontrole toevoegen. Geen automatische bulkrefactor omdat meerdere handlers op elkaar lijken.
