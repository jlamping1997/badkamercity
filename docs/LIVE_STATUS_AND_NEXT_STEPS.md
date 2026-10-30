# BadkamerCity — actuele werkstatus

**30 oktober 2026 · BC-QUOTE-001 — Eenvoudiger offertedesign in concept; Jotform gekoppeld.**

## Actuele uitvoering

[Nieuwste ontwerp en controle](quote/2026-10-30/DESIGN.md): één uploadkaart, kortere uitleg, compacte velden en uitklapbare garantie-uitleg. Vier themebestanden exact teruggelezen, vier ThemeCheck-bestanden en17rendercases PASS;320/390component zonder overflow. Alleen design gewijzigd; actuele gates en openstaande mailverificatie behouden.

[Actuele Jotform-configuratie, test en aansluitstatus](quote/2026-10-30/INTEGRATION.md). Status **FORM_CREATED / CONCEPT_CONNECTED / EMAIL_VERIFICATION_AND_DELIVERY_PENDING / CUSTOMER_ACTIVATION_DISABLED**.

- MAIN **195915448586 — BadkamerCity - Offerteknop alleen desktop**,1.349files, in deze sessie ongewijzigd. Reviewconcept **195916628234 — BadkamerCity - Offerte vergelijken**, UNPUBLISHED,1.350files.
- Eigenaar heeft een Jotform-account gemaakt en veilig aangemeld; geen credentials/OTP in Git. Formulier **263018521531044**, publiek providerformulier; de Shopify-pagina166573539594 is nog ongepubliceerd. Op expliciete keuze van eigenaar melding naar **info@badkamercity.nl**.
- Formulier: volledige offerte/één product; voor-/achternaam, e-mail en bestand verplicht; toelichting optioneel. PDF/JPG/JPEG/PNG, maximaal3bestanden/10MB per bestand, als instellingen gelezen. Geen telefoonveld, betaling of marketinginschrijving.
- Eén fictieve testaanvraag succesvol verzonden, in Jotform teruggelezen en PDF van781bytes ingelogd gedownload; exact gelijk aan origineel. .txt geweigerd met Nederlandse melding. Dit zijn geen echte klantgegevens. Testrecord gemarkeerd en nog aanwezig.
- Require log-in to see submissions en Require log-in to view uploaded files stonden aangevinkt. Anonieme downloadweigering niet bewezen: externe uitleestool kon de test-URL niet ophalen. Geen privacyvrijgave op basis van die fout.
- Notificatie naar eigenaar geconfigureerd met Nederlandse tekst, zonder losse bestandsbijlagen. Bezorging in de mailbox nog niet bevestigd. Automatische klantmail expliciet **disabled**, omdat accountverificatie nodig is voor aanpassing; eigenaar meldt verificatiemail nog niet te hebben ontvangen.
- Concept: form_id ingevuld, **integration_preview=true** alleen bij theme.role=unpublished; **integration_enabled=false**, **show_preview=false**. Publicatie van het concept activeert de provider niet automatisch. Klantlinks/header/footer en homepage-teaser blijven uit volgens hun bestaande gates. Geen mobiele headerbalk.
- Drie ThemeCheck-files en17lokale render-/gatecases PASS. Drie productie-inhouden exact/JSON-semantisch teruggelezen; alleen die drie gewijzigde bestanden in concept. Desktopiframe zichtbaar; providerframes320/390zonder horizontale overloop. Tijdelijke QA-template exact hersteld. Geen fysieke telefoon-, grensgrootte-, servervalidatie-, verwijder-, spam- of performancevrijgave.

## Exact één volgende handeling

**Eigenaar controleert de Jotform-verificatiemail en testmelding op info@badkamercity.nl, ook ongewenste mail.** Daarna klantbevestiging afronden en ontvangst bevestigen; resterende toegang-/bewaar-/telefooncontrole vóór klantactivatie en publicatie door eigenaar.

## Overdracht

Geen Shopify MAIN-write of Shopify-publicatie. Jotform-formulier bestaat wel als publieke, nog niet via klantlinks ontsloten providerroute. Geen betaald plan, API-key of nieuwe app. Huidige plan toont Jotform-branding. Bewaartermijn is nog niet vastgesteld/geconfigureerd. Geen achtergrondworker actief. Oude bewijsblokken hieronder horen bij de eerdere fasen.

## Parkeerplaats — nieuwe toekomstprojecten, 29 oktober 2026

[Content, merkpagina's, offerteaanvragen en productplan](FUTURE_CONTENT_AND_PRODUCT_PROJECTS.md): Living Colours/PVD met productuitleg en vergelijkingsbeelden; bestaande Sunshower-blog versterken; hoogwaardige Porcelanosa-merkpagina; bestaande offerte-upload-/prijsaanvraagtaken aanscherpen; gefaseerde productkwaliteit en verrijking. Status **BACKLOG / NOG UIT TE VOEREN**. Geen start van deze uitvoering of wijziging van de NAV-01-reviewvolgorde.

Historisch backlogcheckpoint vóór FLASH-01: GitHub-connector, uitsluitend documentatie op de bestaande werkbranch en main. Bestaande blog-/productdossiers en historische offerte-/prijstaken hergebruikt; Hotbath-bronnen voor het algemene patinaprincipe gecontroleerd. Nieuwe functies en productdetails niet getest of gebouwd. Shopify-rollen in deze sessie niet opnieuw gelezen; bovenstaande theme-metingen behoren bij NAV-01. Geen winkelmutatie, Windowscontrole, publicatie of geplande achtergrondtaak. Eigenaar kiest later welk toekomstproject start; de ene eerstvolgende handeling hierboven blijft staan.

## TAX-01 — vaste categorisatie- en SEO-werkwijze, 29 oktober 2026

Eigenaar vraagt nu schaalbare categorisatieafspraken en documentatie voor nieuwe merken/producten en toekomstige SEO-/serieonderzoeken. [Vast contract en fasering](CATEGORIZATION_AND_SEO_POLICY.md) · [gedateerde nulmeting en eerste beslissingen](categorization/2026-10-29/baseline-and-decisions.json). Status **DOCUMENTED / TAXONOMY_PROPOSALS_NOT_IMPLEMENTED**. AGENTS.md verwijst toekomstige imports/categoriewijzigingen naar dit contract.

Read-only inventaris eerder in deze doorlopende sessie: 9 menu's, 226 collecties, hoofdmenu156vermeldingen/144bestemmingen; 12 dubbele bestemmingen zijn reviewgevallen, geen automatische fouten. Eerste afdelingsvoorstellen, importprocedure en selectiecriteria voor SEO-landings zijn beschreven. Verse beperkte concurrentiesteekproef en officiële Google-richtlijnen gelezen; geen keywordvolumes, rankings of conversieresultaat vastgesteld. Geen Shopify-mutatie of nieuwe themacontrole in deze documentatiestap. Volledige visuele/klik-/importtests nog open.

Dit documentatiecheckpoint neemt de afzonderlijke FLASH-01-uitvoering niet over en verandert de ene volgende uitvoeringshandeling hierboven niet. Eerstvolgende categorisatiehandeling ná afronding/overdracht daarvan: TAX-02, één concreet Wastafels-voorstel met productmapping en gescheiden aanvullende links in preview beoordelen. SEO-onderzoeken staan als vervolgwerk, niet als gestarte achtergrondtaken.

## QC-02 — aparte privétool, 30 oktober 2026

Eigenaar heeft expliciet de eigen tak `quality-control` en mobiele foto-/productreviews met checkpoints gevraagd. [Actuele tool, code, brondekking en testgrenzen](https://github.com/jlamping1997/badkamercity/blob/quality-control/quality-control/README.md). [Privétool openen](https://badkamercity-quality.jason015.chatgpt.site). Status **PRIVATE_DEPLOYED / AUTHENTICATED_PHONE_REVIEW_PENDING**; QC-codecheckpoint 195f3f07ed6da728c7d9a5fdda5526da96786936. Beoordelingen/checkpoints in afgeschermde D1, geen Shopify-/storefrontmutatie. 11.679producten/34.713beeldkoppelingen in gedateerde read-only werkkopie;645Hotbath-producten zonder foto op aanleverlijst. Typecheck/build en13API-/SQLite-groepen geslaagd; hosted catalogusread en identity-afwijzing bewezen. Echte visitorlogin/-write en fysieke telefoon nog niet getest wegens nieuwe browseraanmelding. Volgende QC-handeling: eigenaar probeert één batch en maakt/hervat een named checkpoint. Deze afzonderlijke tool neemt de ASSORT-02-uitvoering en diens eerstvolgende storefrontstap hierboven niet over. Publieke Git bevat code/documentatie, geen privébeoordelingen of volledige extra mastercatalogus.

## QC-03 — hoofdfotocontrole vereenvoudigd, 30 oktober 2026

Op eigenaarsverzoek staat op dezelfde privétool versie4: één hoofdfoto per product, vier directe keuzes Ja/Nee/Twijfel/Technische tekening, geen fototekstvelden, grotere foto en volledige grotere producttitel. [Actuele code, dekking en bewijs](https://github.com/jlamping1997/badkamercity/blob/quality-control/quality-control/README.md); branch `quality-control`, checkpoint d4e656f9abe0d208680eeb709c998fb2f3d48ddb. 11.034hoofdfotokaarten; eerdere reviews/checkpoints behouden, oude galerijcheckpoints gefilterd bij hervatten. Typecheck/build en20tests PASS;320/390componentbrowser zonder overflow. Fysieke telefoon-/hosted visitor-write niet opnieuw geclaimd. Volgende QC-handeling: eigenaar herlaadt de privétool en beoordeelt een hoofdfotobatch. Bestaande storefrontuitvoering hierboven blijft zelfstandig; geen Shopify-mutaties.

## QC-04 — notities, alle merken en dag/nacht, 30 oktober 2026

Dezelfde privétool is versie5 met optionele fotonotities/snelle redenen, aparte notitie-opslag en zichtbare redenen in aanleverlijst, standaard alle merken/willekeurig en een rustige dag-/nachtinterface. [Actuele code, databehoud en bewijs](https://github.com/jlamping1997/badkamercity/blob/quality-control/quality-control/README.md), codecheckpoint 9642a8fb9f52a83b45f8b3e8c372738d0038500e. Alle bevestigde beoordelingen waren en blijven globaal per eigenaar; checkpoints onthouden selectie/plek, rollen nieuwe beoordelingen niet terug, en ondersteunen nu gemengde merken. Oude checkpoints blijven geldig. Dezelfde DB/authclient/import/ID's, geen migratie/reset of Shopify-write; begrensde vóór/na-readback van bestaande data identiek. Typecheck/build en30tests PASS;320/390componentlayout en dag/nacht-herladen bewezen; hosted compacte all-brandcatalogus HTTP200/11.679producten/11.034hoofdfoto’s, identityloze reviewread401. Visitor-write en fysieke telefoon niet namens eigenaar geclaimd. Volgende QC-handeling: eigenaar herlaadt dezelfde privélink en gebruikt de bestaande voortgang met optionele notitie of willekeurig verder. Bestaande storefront/offerte-uitvoering blijft afzonderlijk.
