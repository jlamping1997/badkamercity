# Brauer — visuele kraankeuzes herstellen

12 november 2026 · BRAUER-VISUAL-CHOICES-01 · PREVIEW_VERIFIED / OWNER_REVIEW_PENDING.

## Actueel na tweede eigenaarreview

De eigenaar wil vijf hendelvormen en afzonderlijk **Plaatsing uitloop: Links / Rechts**, plus **Uitloop: Recht / Gebogen**. De eerder getoonde tien gecombineerde hendel-/positiekeuzes zijn daarmee vervangen. Nog geen publicatie of definitieve eigenaar-UI-goedkeuring.

In bestaande groep BRAUER-F3F2437BF3BB2A5C (338 inbouw-wastafelkranen) is model A1/A2 etc. verliesloos opgesplitst: A–E is de hendelvorm; suffix 1 betekent uitloop Links, suffix 2 uitloop Rechts. De oorspronkelijke code blijft als options.handle_code in de publieke groepsdata behouden. De hendel staat tegenover de uitloop. Dit volgt uit het afgebakende bestaande vorm-/hendelpositiecodeboek, de exacte productfoto’s en de officiële [Brauer-installatiehandleiding](https://www.brauerkranen.nl/site/0075EFB1AD174250C1258704003ED697/%24FILE/BRAUER%20Handleiding%20inbouw%20wastafelkraan.pdf): 328–331 hebben hendel rechts/uitloop links, 332–335 andersom. Geen universele decoder buiten deze groep.

De vijf hendelfoto’s tonen alleen Lang en smal, Kort en smal, Breed en plat, Smal en plat en Dikkere greep. De plaatsing staat in de aparte tekstknoppen. De toelichting beschrijft vormvoorbeelden in chroom en verwijst voor de uitlooppositie naar de aparte keuze. Uitloop behoudt intern Rechte maar toont Recht; Gebogen blijft Gebogen. Dat label is in beide bestaande uitloopgroepen aangepast (338 inbouwkranen en 38 fonteinkranen). Wandafwerking Rozetten/Afdekplaat blijft behouden.

## Aangetoonde oorspronkelijke regressie en behouden verbetering

De publieke pagina 5-S-331 toonde codes A1 t/m E2, tekst voor uitloop en lange greepafwerkinglabels. De eerdere [UX-goedkeuring](../2026-11-06/UX_GOEDKEURING_EN_RESTERENDE_CONTROLES.md) vroeg expliciet om afzonderlijke hendelvormbeelden. De renderer gebruikte alleen voor colour een fototak; product_first_image en finish_detail_photo werden voor andere assen tekstknoppen. Logica-/identiteitscontroles bewezen dus niet dat de afgesproken beelden waren overgenomen.

Veertig finish-groepen, samen 2.390 bestaande artikelen, behouden de vereenvoudigde labels **Streepjes / Gekarteld / Glad**, intern Stripe/Carving/Standaard. De vijf hendelbeelden gebruiken bestaande eigen Shopify-foto’s van exact gekoppelde chromen gladde referenties 5-CE-004-S2-65, -S5-65, -S3-65, -S4-65 en -S1-65. CSS kadreert de hendel, zonder nieuwe bitmap, spiegeling, omkleuring of generatief beeld. De twee uitloopgroepen tonen uitsluitend de eerste foto van het exacte kandidaatartikel. De uitloopfotohoogte is 70px.

Onmogelijke combinaties blijven grijs/geblokkeerd. Wijzigen van hendelvorm behoudt uitlooppositie en omgekeerd; ook kleur, greepafwerking, uitloopvorm en wandafwerking blijven behouden. SKU, product/variant-ID, handle, route, foto en andere bronopties zijn ongewijzigd. De nieuwe keuzestructuur is verliesloos terug te zetten naar de eerdere product.options; voor alle gewijzigde groepsrecords exact gecontroleerd. Geen Admin-product-/prijs-/voorraad-/mediavelden gemuteerd.

## Shopify- en codeoverdracht

Actieve codebranch fix/product-cards-2026-10-14. Eerste implementatiecheckpoint a24ac9e455e3dfad1e9c49dc4a492e46abead180; gecontroleerde eerste preview/CSS-overdracht 5905d9f33f7daf25ef8e6a7963d8d4d2de6140a5. Aansluitende commit bevat deze tweede eigenaarcorrectie.

Hetzelfde concept blijft **UNPUBLISHED 196578803978 — BadkamerCity - Brauer visuele kraankeuzes**. Eerste fase: native kopie vóór upload 2.522/2.522 identiek aan MAIN196542005514; na upload exact 42 bedoelde verschillen en MAIN alle 2.522 bestanden onveranderd. Tweede fase: uitsluitend drie bestaande conceptassets bijgewerkt (bc-brauer-choices.js en de groepen f3f2437bf3bb2a5c/a32c8d8b559ff89a), alle drie checksums exact teruggelezen. Verse rollen MAIN196542005514/UNPUBLISHED196578803978 bevestigd; de drie corresponderende MAIN-checksums onveranderd. Geen nieuwe volledige 2.522-bestandenread in tweede fase claimen. Brauer-specificatieconcept196557144330 en Lagoo niet gewijzigd.

Generator refine_visual_choices.py verzorgt beide fasen, inclusief idempotente splitsing en verliesloze broncontrole. build_storefront_choices.py roept dit aan. test_storefront_choices.cjs controleert renderer, foto’s, blokkades en afzonderlijke hendel/positie. De dubbele referenties in storefront_handle_photos.json blijven historische broncodes; de UI gebruikt vijf unieke vormen.

## Bewijs en grenzen

- Volledige renderer: 827 groepen / 12.142 exacte startstanden / 150.652 geldige keuzes / 8.746 onmogelijke keuzes / 1.172 voorwaardelijke tussenstanden PASS. Alle 12.142 producten bereikbaar; cartguard, native select en zes zichtbare kleuren behouden. De aantallen keuzes dalen door vijf vormen plus twee posities in plaats van tien gecombineerde keuzes.
- Alle 338 kraanstartstanden, 672 exacte kandidaat-uitloopfoto’s, vijf hendelfoto’s/twee posities en 1.974 geldige vorm-/positiewissels gecontroleerd. Iedere wissel behoudt alle overige assen en leidt tot hoogstens één exact artikel. Stripe→B blijft geblokkeerd. Zie VISUELE_KRAANKEUZES_TESTS.json.
- Toolkitvalidatie drie nieuwe assetbodies PASS; JS-syntaxis, Python-compile, verliesloze data-invariant, idempotent hergenereren en git diff --check PASS. Validator gebruikte gebundelde docs-fallback na netwerk-time-out; docssearch zelf gaf relevante officiële variantpicker-documentatie.
- Echte Chrome-conceptnavigatie: 5-S-331 (A1, uitloop Links, Recht, zwart/Streepjes/rozetten) → plaatsing Rechts → 5-S-335 (A2); vervolgens Glad → 5-S-083-S2-65; Kort en smal → 5-S-083-S5-65, Rechts behouden; plaatsing Links → 5-S-004-S5-65; Gebogen → 5-S-004-B5-65, Links/Kort en smal/Glad/zwart/rozetten behouden. Terug naar origineel; vijf hendelfoto’s geladen en nieuwe labels/plaatsingsknoppen visueel vastgelegd.
- Eerdere fase had native cart PASS op 5-S-083-B5-65/variant54103819026698/€388,29/aantal1; eigen proefregel verwijderd en eindcart leeg. Tweede fase heeft geen nieuwe cart-/checkoutmutatie of herhaalde cartproef. Geen aankoop.
- Eerdere fase had smalle layout bij 340 CSS-px zonder overflow en drie hendelkolommen bewezen. Die browserlayoutproef is niet na deze tweede splitsing herhaald. Fysieke telefoon/touch, nieuwe mobiele interactie en checkout NOT_TESTED. Geen Windows-check.
- Deelbare exacte Shopify-conceptpagina opnieuw geopend en schermbewijs in het gesprek bewaard; geen previewcapability, carttoken of klantdata in publieke Git.

## Herstel en volgende handeling

Herstel tweede fase: zet uitsluitend de drie conceptassets terug naar codecheckpoint 5905d9f33f7daf25ef8e6a7963d8d4d2de6140a5. Voor herstel eerste fase bestaan MAIN-baseline en eerdere oorspronkelijke bronchecksums. Niet zelfstandig publiceren of MAIN aanpassen.

**Exact één volgende handeling:** eigenaar beoordeelt het bijgewerkte gedeelde conceptvoorbeeld. Vóór een eventuele latere release actuele MAIN-rol en gelijktijdige wijzigingen vergelijken; ander Brauer-/Lagoo-werk behouden. Geen actieve schrijver na overdracht.
