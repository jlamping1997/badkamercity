# Compacte desktopkeuzes — 25 oktober 2026

Status: PREVIEW_READY, niet gepubliceerd. Bron/actuele MAIN: 195704357130 — rustige kleur en lengtewissel. Concept: **195704848650 — BadkamerCity - compacte keuzes desktop**.

## Resultaat

De goedgekeurde mobiele Hotbath-bediening is nu gedeeld met desktop: vier ronde kleuren van48px met volledige namen, uitklapper met extra aantal, compacte uitloopknoppen en één checkbox **Inbouwdeel toevoegen** met actuele meerprijs. De oude grote desktop Ja/Nee-kaarten en uitleg verdwijnen in deze scope. Niet aangevinkt betekent alleen het afbouwdeel. Aantal en inbouwkeuze rekenen de totaalprijs direct door. Uitgeklapte kleuren en een expliciete inbouwkeuze blijven via hun bestaande veilige contracten behouden bij kleur/lengtewissels.

Vijf gewijzigde assets in `theme/assets`; exacte bron in `before/assets`. De internal mobile-namen blijven behouden; de schermbreedtevoorwaarden zijn verwijderd voor dezelfde Hotbath-scope. Geen dubbele desktopcomponent, wijziging van producten, artikelkoppelingen, checkout of scrollalgoritme. Andere merken en volumeproducten behouden bestaande bediening. `before/assets/bc-product-sticky.js` is alleen een ongewijzigde testdependency.

## Verificatie

- Vooraf concept553/553 identiek aan MAIN. Finaal vijf assets gewijzigd,548 identiek. MAIN553/553 ongewijzigd.
- Vijf uploads exact teruggelezen. Tijdelijke `product.bc-mobile-review.liquid` na tests exact hersteld; geen tijdelijke QA-wijziging in eindthema.
- Syntax en Shopify-validator5/5PASS. Validator gebruikte bestaande gecachte schema's na externe docs-timeout; geen nieuwe validatiefout.
- Node24:10positiechecks,11switchergroepen,13aankoopgroepen en4observerproeven met sticky-component PASS. Inclusief geen betaalde voorselectie, bewaakte identiteit/beschikbaarheid, echte tweeregel-cart-handler met transportstub, dubbele-submitbeveiliging, quantité, veilige opslag en responsive state. Geen echte cartrequest.
- Desktopbrowser1348px: totaal322,01 zonder body;496,01 met body;992,02 bij aantal2. Kleurwissel naar nikkel behoudt10 uitgeklapte kleuren en aangevinkt body; wissel naar18cm geeft486,00 metbody. Uitzetten geeft312,00.
- Iframe-CSSbreedtes320/390/1024: client-/scrollwidth305/375/1009 identiek, geen horizontale overloop. Kleurcirkels48×48. Uitgeklapte kleuren en geselecteerd inbouwdeel blijven bij breedtewissel behouden. Dit zijn browserframes, geen fysieke telefoons; geen volledige navigatie binnen srcdoc geclaimd.
- Niet getest: fysieke iPhone/Safari, echte checkout/betaling, conversie en Windows-checkout. Bestaande lokale wijzigingen niet aangeraakt.

## Reproduceren en vervolg

Met Node24: `npm install` en `npm test` in dit dossier. Enige testdependency: happy-dom21.0.4. `browser-results.json` bevat de echte UI-metingen; `readback.json` de checksums. `desktop.jpg` toont het eindconcept.

Eigenaar beoordeelt en publiceert **BadkamerCity - compacte keuzes desktop** in Shopify→Webshop→Thema's. De connector kan niet publiceren. Controleer daarna de MAIN-rol opnieuw. Terugval: huidige thema195704357130 of de vijf before-assets via gecontroleerd concept. Actieve branch blijft fix/product-cards-2026-10-14; main alleen documentatie; geen root-theme-sync.
