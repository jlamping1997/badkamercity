# Productpagina bij halve desktopbreedte — 20 oktober 2026

Status: **IMPLEMENTED_PREVIEW**, niet gepubliceerd. Eigenaar meldt een te grote foto en een koopblok onder de foto bij een browservenster van circa950px. De bestaande inhoud, prijs en33 specificaties blijven behouden.

- MAIN:195486253322 — BadkamerCity - Wiesbaden33 specs20 okt.
- Concept:195488317706 — BadkamerCity - Productpagina smal desktop.
- Vooraf508/508 themabestanden checksum-identiek. Live blijft508/508 ongewijzigd.
- Productiecorrectie uitsluitend CSS bij750–989px: twee kolommen45/55%, krimpbare griditems en koopblok zonder de oude600px-limiet.
- <750px en≥990px houden hun oorspronkelijke regels.

## Controle

De gewone Shopify-productpagina mocht niet in een iframe worden geladen. Daarom is de actuele, publiek gerenderde productmarkup met dezelfde echte themastyles in een tijdelijke srcdoc-testweergave geladen. Scripts waren daarin uitgeschakeld. Dit toetst de CSS, geen volledige interactieve winkelwerking op die zes breedtes.

| Breedte | Vooraf | Daarna |
| --- | --- | --- |
|950px|Foto893px hoog; koopblok start op1265px|Foto389,94px hoog; koopblok naast foto vanaf147px|
|750px|Foto693px hoog; koopblok eronder|Foto299,94px hoog; koopblok ernaast|
|989px|Foto932px hoog|Foto407,5px hoog; koopblok ernaast|
|320/390px|Gestapelde telefoonweergave|Afmetingen en posities gelijk|
|990px|Bestaande brede indeling|Afmetingen en posities gelijk|

Alle zes breedtes: geen horizontale paginaoverloop,33 specificatieregels. De gewone interactieve productpagina in de cloudbrowser bij1363px toont titel,33 rijen, koopknop en verlanglijst; geen overloop. In deze ronde geen cart- of wishlistmutaties. Geen fysieke telefoon getest.

Theme Check: CSS en tijdelijke controletemplate SUCCESS; de uiteindelijke neutrale template eveneens SUCCESS.

[Voorbeeld950px](design/pdp-responsive-950px-20261020.jpg).
[Meetgegevens](pdp-responsive-2026-10-20-verification.json).
[CSS-patch](patches/BC-pdp-responsive-20261020.patch).

## Testtemplate en grenzen

De connector wees **themeFilesDelete** af onder categorie destructive/theme deletion, ook voor de door deze taak aangemaakte ongepubliceerde QA-template. Geen alternatieve verwijderingsroute gebruikt. Als niet-destructieve opruiming is uitsluitend de eigen tijdelijke testinhoud vervangen door een gevalideerde noindex/canonical-doorverwijzing naar de normale productpagina. De geïsoleerde testweergave en snapshot staan daardoor niet meer in het concept. Het ongebruikte bestand templates/product.bc-responsive-qa.liquid blijft bestaan; geen gewone producttemplate verwijst ernaar. Opgeslagen bron: [neutrale template](patches/BC-pdp-responsive-qa-neutral.liquid).

Finale concept509 bestanden: één bestaand CSS-bestand gewijzigd, één neutraal ongebruikt template nieuw, overige507 checksum-identiek aan MAIN. Beide gewijzigde inhouden exact teruggelezen. Geen productdata, menu's, voorraad, prijs, documentweergave of publicatie gewijzigd.

## Vervolg en herstel

Eigenaar bekijkt het concept via Shopify en publiceert desgewenst **BadkamerCity - Productpagina smal desktop**. Publicatie is door de connector geblokkeerd; agent heeft geen publicatie geprobeerd. Vóór release opnieuw controleren dat MAIN nog195486253322 is en de overige507 checksums gelijk zijn. Na publicatie verse MAIN/venstercontrole.

Herstel van de CSS: de29 toegevoegde regels uit de patch terugdraaien; ongewijzigd vorige MAIN blijft als terugzetmogelijkheid bestaan. Het neutrale testbestand hoeft voor het herstel van de normale productpagina niet te worden verwijderd.
