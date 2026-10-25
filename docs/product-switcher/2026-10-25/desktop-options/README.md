# Compacte desktopkeuzes — 25 oktober 2026

Werkcheckpoint: implementatie lokaal getest, Shopify-conceptkopie nog in verwerking. MAIN 195704357130; concept 195704848650 — BadkamerCity - compacte keuzes desktop. Nog geen themabestanden geschreven, geen publicatie.

De Hotbath-bediening die op mobiel al goedgekeurd is, wordt op desktop hergebruikt: vier ronde kleurkeuzes met volledige namen, alle kleuren uitklapbaar, compacte uitloopknoppen, één checkbox Inbouwdeel toevoegen met meerprijs, hoeveelheid en actuele totaalprijs. Niet aangevinkt betekent uitsluitend het afbouwdeel. Een bewuste keuze blijft volgens het bestaande groep/body-contract bewaard bij productwissels. Volumeproducten en andere merken houden hun bestaande bediening. De interne mobile-asset-/klassenamen blijven voorlopig behouden om alle bestaande koppelingen te respecteren; hun actieve bereik wordt alle schermbreedtes.

Vijf gewijzigde assets in `theme/assets`, exacte MAIN-beforeversies in `before/assets`. `bc-product-sticky.js` is uitsluitend ongewijzigde testdependency. Geen root-theme-sync of publicatie. Tests met Node24 en `npm install && npm test`: 10 positietests, 11 switcherchecks, 13 aankoopgroepen en vier observerproeven PASS. De daadwerkelijke cart-handler is met een transportstub getest; geen echte winkelwagen- of checkoutactie uitgevoerd. Shopify-validator vijf assets PASS met bestaande gecachte schema's na een docs-netwerktimeout. Visuele preview volgt na de volledige conceptkopie.

Rollback: huidige MAIN behouden of de vijf before-assets via een gecontroleerd concept herstellen. Actieve branch fix/product-cards-2026-10-14; main uitsluitend documentatie. Geen fysieke telefoontest of Windows-checkoutcontrole.
