# Hotbath SPOM-adviespagina — vormgeving 17 november 2026

Status: **LIVE_ADMIN_READBACK_VERIFIED / DESKTOP_BROWSER_VERIFIED / NARROW_CSS_VIEWPORT_VERIFIED**.

## Opdracht en resultaat

Eigenaar vroeg de bestaande SPOM-adviespagina overzichtelijker te maken. Alleen de inhoud/opmaak van bestaande Shopify Page 167264813322 is aangepast.
URL: https://badkamercity.nl/pages/hotbath-thermostaat-draait-stroef

- Kortere introductie en vier ankerlinks.
- Twee kaarten met bestaande, door eigenaar goedgekeurde productfoto’s: SPOM745 voor temperatuurregeling en SPOM700 voor stop-omstel.
- Bestaande HB009-bouwjarenvergelijking zichtbaar in een afzonderlijke tabel.
- Native stappenlijst met montage-/gereedschapsinformatie ernaast.
- Vier native uitklapvragen plus een uitklapbaar technisch bronnenblok.
- Contactblok met duidelijke hulpknop.

De model-/bouwjaargrenzen, bestaande officiële videoverwijzing en technische bronlinks blijven aanwezig. Geen nieuwe compatibiliteit, kalkpercentage of herstelgarantie toegevoegd. De foto-to-do voor een verkalkt en schoon binnenwerk blijft open.

## Implementatie

[page.html](page.html) is de versiebron van de Page.body. [page-before.json](page-before.json) bewaart de oorspronkelijke pagina-inhoud vóór deze vormgevingsronde.
Scoped CSS werkt binnen #bc-spom-guide; alleen de bestaande smalle pagina-wrapper en titel worden met :has(#bc-spom-guide) op deze pagina aangepast. Geen JavaScript, nieuwe fontprovider, nieuw template of themafile.
Teksten blijven in de Shopify-pagina te bewerken. Productlinks en foto-URL’s zijn de gecontroleerde bestaande bronnen; bij latere productfoto-/URL-wijzigingen deze pagina gericht mee beoordelen.

Actuele MAIN bij start:196690379018 — BadkamerCity - verzendtarieven per productgroep.
Bestaande codebranch: fix/product-cards-2026-10-14. Alleen documentatie/versiebron, geen thema-release.

## Bewijs en grenzen

- Native read-after-write: oorspronkelijke titel, handle en null-templateSuffix behouden; style aanwezig, twee foto’s, twee kaarten, vijf details-elementen.
- Desktop echte Chrome1363px: content1080px, twee kaarten van530px, beide afbeeldingen geladen, geen horizontale pagina-overloop. Vergelijking en stappen visueel gecontroleerd.
- Echte native details-bediening: vraag over terugkerende stroefheid geopend; antwoord zichtbaar, andere vragen gesloten.
- Native Chrome-zoomtest met CSS-viewport340px: kaarten onder elkaar, documentbreedte340px, nul guide-elementen buiten de viewport; alle tabelcellen zonder inhoudsoverloop. Dit is een smalle CSS-viewportproef, geen fysieke telefoon.
- Native ordered-listopmaak: decoratieve dubbele counters verwijderd.
- Contrastberekening: groene knop/wit5,08:1; donkerblauw/wit13,64:1; bodytekst/wit9,08:1.
- Vier lokale ankerdoelen bestaan en IDs zijn uniek; geen script/form in deze pagina-inhoud.
- Mobiele ankermarge160px voor de bestaande sticky header; desktop140px.
- De thema-previewtool gaf theme_not_renderable en kon de themabestanden niet lezen. Geen defect aan live afgeleid; visuele nacontrole rechtstreeks in echte Chrome uitgevoerd.
- Niet uitgevoerd: fysieke iPhone/touchproef, checkout, betaling, SEO-indexerings-/rankingmeting en Windows-lokale synchronisatie.

## Herstel en vervolg

Herstel alleen deze vormgevingsronde door Page.body van ID167264813322 terug te zetten naar body uit page-before.json. Titel, handle, template en SEO-velden daarbij behouden.
Bewijsbron is de native Shopify-readback en echte browserweergave; geen volledige site-/thematest geclaimd.

Volgende eigenaarshandeling: nieuwe pagina bekijken. De reeds vastgelegde vergelijkingsfoto kan later worden toegevoegd.
