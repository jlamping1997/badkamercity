# LAGOO-19 — geen productafbeeldingen

Datum: 4 november 2026. Uitvoerder: Codex via gekoppelde Shopify- en GitHub-tools. Bestaande codebranch: fix/product-cards-2026-10-14. Eigenaar vroeg expliciet alle Lagoo-afbeeldingen nu te verwijderen.

## Uitvoering en scope

Shopify-winkel Badkamercity, domein badkamercity.nl. Zoekscope `vendor:Lagoo OR title:Lagoo*` leverde precies 232 producten op; alle 232 hadden vendor Lagoo. Alle statusgroepen en de 24 losse proefuitvoeringen zijn meegenomen. 57 producten waren al zonder media; 175 producten hadden 1.788 afbeeldingen, verdeeld over 1.763 unieke MediaImage-bestanden. Er waren geen andere mediatypen of onvoltooide bestanden.

Alle productbeschrijvingen gecontroleerd op inline img/picture/background-image: nul. Eén bestand eerst losgekoppeld en nul media/featuredMedia bevestigd. Daarna 1.762 bestanden in acht opeenvolgende batches (7 × 250 + 12) gericht losgekoppeld met fileUpdate.referencesToRemove. Bij gedeelde bestanden alleen de gemeten Lagoo-productreferenties verwijderd. Alle negen mutatie-antwoorden zonder userErrors; aantal teruggegeven bestanden gelijk aan aantal aangevraagde bestanden.

De operatie verwijdert de afbeeldingen uit de productgalerij en wist ook variantafbeeldingen die eraan gekoppeld waren. De bestanden zelf zijn niet globaal verwijderd.

## Verificatie

- Volledige verse eindquery: 232 producten, pageInfo.hasNextPage=false, alle mediaCount.count=0.
- Alle titels, handles, vendor, status en descriptionHtml bytegelijk aan de vóórwaarden.
- Get-product voor Lagoo Garda wastafelmengkraan: images=[], featuredImageUrl=null.
- Openbare productpagina https://badkamercity.nl/products/lagoo-garda-wastafelmengkraan na verlaten van preview: main bevat nul img-elementen; screenshot intern bekeken, geen productfoto.
- De bestaande lege galerijruimte/teller 1/0 blijft zichtbaar; geen layout-/themamutatie in deze data-opdracht.
- Zoeken via de echte header leverde eerst native Lagoo-kaarten zonder foto's. De externe filterlaag vervangt deze daarna door vier Wiesbaden Lagos-producten; de acht daar aanwezige img-elementen behoren allemaal tot Wiesbaden. Die bestaande zoekafwijking is niet als afbeeldingsherstel of Lagoo-foto behandeld en niet aangepast.
- MAIN bij opening en einde: 196116087050, BadkamerCity - Lagoo foto's en productkeuzes. Andere rollen ook gelijk. Geen themefilewrite/publicatie, prijs-/voorraad-/BTW-/verzend-/betaalmutatie.
- NOT_TESTED: fysieke telefoon, Windows, cart/checkout en alle individuele klantpagina's visueel. Alle 232 producten wel administratief volledig gecontroleerd.

## Herstel en nieuw beleid

Privéherstelbestand: Lagoo-afbeeldingen-herstel-2026-11-04.json. Het bevat de volledige vóórinventaris, product-mediarelaties, CDN-URL's, geplande ontkoppelingen, omgekeerde referencesToAdd en eindcontroletellingen. Geen secrets in dit dossier of het herstelbestand.

Herstel alleen na nieuwe expliciete eigenaaropdracht: bestaande bestand-ID's via fileUpdate.referencesToAdd aan de genoemde product-ID's koppelen. Galerijvolgorde en individuele varianttoewijzingen worden niet automatisch door die eenvoudige omkering hersteld en zouden afzonderlijk moeten worden bepaald.

Alle eerdere instructies om Lagoo-foto's te corrigeren of verder uit te rollen zijn door de nieuwste eigenaaropdracht vervangen: **geen Lagoo-productfoto's opnieuw importeren of koppelen zonder nieuwe opdracht.** LVS1/2/3 blijft geparkeerd. Kleurkeuze-, productnavigatie-, offerte- en overige taken zijn niet gewijzigd.

Exact één volgende handeling: wacht op een nieuwe expliciete eigenaaropdracht voor Lagoo-foto's. Geen actieve schrijver na overdracht.
