# Brauer — visuele kraankeuzes herstellen

12 november 2026 · BRAUER-VISUAL-CHOICES-01 · PREVIEW_VERIFIED / OWNER_REVIEW_PENDING.

## Opdracht en aangetoonde regressie

De eigenaar meldt bij 5-S-331 dat de goedgekeurde hendelbeelden ontbreken: de publieke pagina toont codes A1 t/m E2, tekst voor de uitloop en lange greepafwerkinglabels. In de goedkeuring van 7 november staat expliciet dat de afzonderlijke hendelvormbeelden behouden blijven (../2026-11-06/UX_GOEDKEURING_EN_RESTERENDE_CONTROLES.md). De huidige renderer gebruikte alleen voor colour een fototak; de kinds product_first_image en finish_detail_photo werden voor andere assen tekstknoppen. Eerdere logica-/identiteitscontroles bewezen dus niet dat de afgesproken visuele keuzehulp was overgenomen.

De huidige eigenaaropdracht bepaalt nu de labels: **Streepjes / Gekarteld / Glad**, herkenbare hendelfoto’s en kleine productfoto’s bij de uitloop. Wandafwerking blijft tekst.

## Wijziging

- Veertig bestaande finish-groepen, samen 2.390 bestaande artikelen: uitsluitend labels vereenvoudigd; interne waarden Stripe/Carving/Standaard blijven behouden.
- Bestaande inbouw-wastafelkraangroep BRAUER-F3F2437BF3BB2A5C (338 artikelen): hendelkeuzes krijgen vijf herkenbare vormbeelden, met voor elke vorm de afzonderlijke links/rechts-keuze. Namen Lang en smal, Kort en smal, Breed en plat, Smal en plat, Dikkere greep volgen het eerdere afgebakende codeboek. Geen nieuwe universele fabrikantdecoder.
- Vormbeelden gebruiken eigen actuele Shopify-productfoto’s van de vijf exact gekoppelde chromen, gladde referentieartikelen 5-CE-004-S2-65, 5-CE-004-S5-65, 5-CE-004-S3-65, 5-CE-004-S4-65 en 5-CE-004-S1-65. CSS toont de hendel in een afgebakend venster; geen nieuwe bitmap, spiegeling, omkleuring of generatief beeld. Dezelfde vormfoto mag links/rechts ondersteunen; positie staat expliciet in het label. De tekst legt uit dat dit vormvoorbeelden in chroom zijn, niet de gekozen verkoopafwerking.
- De twee bestaande spout-groepen (338 inbouwkranen en 38 fonteinkranen) tonen de eerste foto van uitsluitend het exacte kandidaatartikel; geen foto van een andere kleur/uitloop als vervanging. Bij ontbrekende foto blijft de benoemde keuze behouden.
- Bestaande onmogelijke combinaties blijven grijs/geblokkeerd. Geen stille verandering van kleur, afwerking, wandafwerking of positie. Productrecords, opties, SKU/variant/handle/routes en prijs-/voorraadvelden blijven behouden.
- Generator past dezelfde visuele verrijking toe; hergenereren mag de verbetering niet verliezen.

## Bestanden en herstel

Twee renderer-assets (bc-brauer-choices.js/.css) en veertig groeps-JSON’s onder shopify/current/assets. Generator build_storefront_choices.py, nieuwe refine_visual_choices.py en storefront_handle_photos.json, plus bestaande test_storefront_choices.cjs. Geen andere merken of MAIN-bestanden geschreven.

MAIN **196542005514** is volledig vóór en na gelezen: alle 2.522 bestanden ongewijzigd. Nieuwe native kopie **UNPUBLISHED 196578803978 — BadkamerCity - Brauer visuele kraankeuzes** was vóór upload volledig 2.522/2.522 checksum-identiek. Daarna uitsluitend 42 bestaande assets geschreven en teruggelezen: exact 42 bedoelde verschillen, nul onverwachte verschillen, nul ontbrekende/verkeerde uploads. Eindrol UNPUBLISHED bevestigd. Bestaand Brauer-specificatieconcept 196557144330 blijft ongemoeid. Geen publicatie.

Codecheckpoint a24ac9e455e3dfad1e9c49dc4a492e46abead180 bevat de implementatie. De aansluitende overdrachtscommit bevat de definitieve 70px-uitloopfotohoogte en onderstaande browserbewijzen. Actieve codebranch: fix/product-cards-2026-10-14. Geen actieve schrijver na overdracht.
Herstel: de 42 assets uit de vóórmeting terugzetten in hetzelfde concept; bij ongepubliceerde oplevering blijft live onveranderd. Bij eventuele latere publicatie kan de eerdere MAIN als herstelpunt dienen, mits rollen en andere gelijktijdige wijzigingen eerst vers zijn gecontroleerd.

## Bewijs en grenzen

- Volledige bestaande logica: 827 groepen /12.142 exacte startstanden /151.274 geldige keuzes /9.138 onmogelijke keuzes /1.172 voorwaardelijke tussenstanden PASS; cartguard, native select en zes zichtbare kleuren behouden.
- Aanvullend 338 kraanstartstanden en672exacte kandidaat-uitloopfoto’s gecontroleerd; tien hendelkeuzes, vijf bronfoto’s; geblokkeerde Stripe→B1-wissel verandert niets. Zie VISUELE_KRAANKEUZES_TESTS.json.
- Alle40gewijzigde groepsbestanden bewaren alle productrecords en aswaarden exact. Alleen presentatievelden wijzigen.
- Toolkitvalidatie42files PASS na aanvullen van ontbrekende runtime-dependencies. Validator gebruikt gebundelde docs-fallback doordat ophalen actuele docs time-out gaf; geen onbewezen actuele documentatieclaim.
- Echte Chrome-conceptpagina op desktop gecontroleerd. Zichtbare hendelvormen, eenvoudige finishlabels en kleine 70px-uitloopfoto’s bevestigd. Afzonderlijke deelbare Shopify-previewlink met exact dit product geopend en visueel gecontroleerd; schermbewijs in gesprek, geen previewcapability in publieke Git.
- Echte navigatie: 5-S-331 → Gebogen → 5-S-328 → A2/links → 5-S-332, telkens zwart/Streepjes/rozetten behouden en €421,56. Vervolgens Glad en Kort en smal/links → 5-S-083-B5-65, €388,29. Onmogelijke Stripe-hendels blijven zichtbaar grijs.
- Native winkelwagenknop op 5-S-083-B5-65 gebruikt: succesvolle modal met juiste titel/€388,29 en onafhankelijk cartread met variant 54103819026698, aantal 1. Vooraf leeg; uitsluitend eigen proefregel verwijderd; eindread nul regels. Geen checkout/aankoop.
- Smalle layout met native Chromezoom 400%: 340 CSS-px viewport, documentbreedte 337px, drie kolommen, circa 79,66px brede hendelknoppen, alle tien vormbeelden geladen. Dit bewijst layout/overflow/afmetingen; mobiele klik/navigatie en fysiek telefoon-/touchgebruik NOT_TESTED. Zoom naar 100% hersteld.
- De eerdere lokale Chromiumtest kon door een runtimebeperking niet starten. De uiteindelijke desktop-, smalle-layout- en cartbewijzen hierboven zijn in de echte cloudbrowser uitgevoerd. Geen algemene volledige smartphone-/alle-producten-/checkoutvrijgave.
- Nul Admin-product-, media-, prijs-, voorraad- of kanaalmutaties. Lagoo en andere Brauer-specificatiewerkstroom niet gewijzigd. Geen lokale Windows-check.

## Exact volgende handeling

Eigenaar opent het gedeelde conceptvoorbeeld en beoordeelt de herstelde keuzehulp. Nog geen eigenaar-UI-goedkeuring of publicatie. Vóór een eventuele latere release eerst actuele MAIN-rol en gelijktijdige wijzigingen vergelijken; andere Brauer-specificaties of Lagoo-werk niet overschrijven. Het huidige concept is een afzonderlijk gecontroleerd reviewresultaat.
