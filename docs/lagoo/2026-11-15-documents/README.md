# Lagoo-documenten onder specificaties

Status: ADMIN_VERIFIED / THEME_COPY_PROCESSING op 15 november 2026.

- 232 Lagoo-producten vers uit Admin gelezen; 140 hebben een bestaand documentblok.
- 467 gededupliceerde links overgezet naar bestaande custom.technische_documenten (list.url): 250 unieke PDF's en vijf montagevideo's, samen 255 unieke links.
- Alle 140 waarden onafhankelijk teruggelezen en semantisch gelijk aan het plan. Omschrijvingen en productstatussen intact; 105 conceptproducten blijven concept.
- Sorteervolgorde: maattekening, montage/handleiding, doorstroomgrafiek, onderhoud en overige documenten/video's.
- Twee snippets voorbereid, beide officiële Shopify-validator PASS. Lokale Liquid-runtime: alle 140 omschrijvingen zonder documentduplicaat, 467 links behouden, onvolledige metadata houdt oude links zichtbaar; drie andere merken regressie ongewijzigd.
- Bestaande main-product rendert bc_documents_markup direct onder de specificaties; geen layout-/CSS-wijziging nodig.
- Nieuwe native kopie 196690379018 van MAIN196542005514 is nog processing=true. Patch NIET schrijven zolang kopiëren loopt. Bestaande Brauer-concepten behouden.

## Volgende handeling

Wacht op processing=false van 196690379018, controleer dat beide originele snippets gelijk zijn aan MAIN, schrijf uitsluitend de twee bijgevoegde snippets, lees exact terug en controleer de echte preview (Lagoo met meerdere modellen, zonder documenten, Hotbath/Wiesbaden). Pas daarna eigenaar om publicatie vragen. Niet de huidige live omschrijvingen inkorten vóór de renderer live is.

## Herstel

Huidige live weergave is intact. Na publicatie kan het oude thema worden teruggepubliceerd. Oude documentmetafields per product staan in manifest.json; nieuw aangemaakte waarden verwijderen of bestaande exact herstellen indien terugdraaien nodig is. Geen foto's/prijzen/voorraad/varianten verwijderen.

De patch staat in snippets/. De productiebron blijft shopify/current/ op fix/product-cards-2026-10-14; deze dossierbestanden zijn geen automatische deploy. Geen browser-/mobiele-/checkout- of volledige theme-pariteitsclaim.
