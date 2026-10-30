# BadkamerCity — actuele werkstatus

**30 oktober2026 · BC-QUOTE-001 — offertevergelijker in uitvoering.** Eigenaar kiest dit project na goedkeuring van de mobiele categorielijst.

## Actuele uitvoering

[Dossier, ontwerp en aansluitstappen](quote/2026-10-30/README.md). Status **DESIGN_IMPLEMENTED / INTEGRATION_PENDING_ACCOUNT / NOT_PUBLISHED**. Geen werkende ontvangst-/uploaddienst claimen.

- MAIN **195916628234 — BadkamerCity - Offerte vergelijken**, inmiddels door eigenaar gepubliceerd;1.349files. In deze correctie alleMAIN-checksums ongewijzigd.
- Reviewconcept **195915448586 — BadkamerCity - Offerteknop alleen desktop**, UNPUBLISHED,1.349files. Eerst actuele MAIN overgenomen; daarna alleen mobiele headeractie verwijderd.
- Pagina **166573539594**, handle offerte-vergelijken, templateSuffix offerte-vergelijken, **isPublished=false** teruggelezen.
- Actieve branch `fix/product-cards-2026-10-14`; voorgaand headercheckpoint `1e4c60e5e3572b66f71aaecc36e9fe26b47feaf2`. Main alleen documentatie.
- Eigenaar heeft expliciet laagsteprijsgarantie goedgekeurd: Stuur je offerte op en ontvang een betere prijs. Kop/intro/stappen/FAQ/homepageverwijzing in NL/EN aangepast; ongepubliceerde paginatitel en inhoud bijgewerkt. Localevalidatie en14bestaande cases PASS; twee locale-inhouden en paginastatus teruggelezen. Geen upload of publicatie.
- Pagina-ontwerp, NL/EN, FAQ, contactfallback en voorbereide Jotform-iframe met expliciete activatie. Voorbeeldvelden disabled, geen POST of fakebevestiging. Homepageverwijzing voorbereid maar disabled:true; nieuwe paginaroute nog niet publiek.
- Zeven bedoelde productie-inhouden teruggelezen; overige1.341checksums gelijk. MAIN1.344/1.344ongewijzigd, QA exact hersteld.
- ThemeCheck zeven files PASS;14lokale render-/gatecases PASS. Desktop en320/390/1024componentframes zonder overloop; FAQbediening PASS. Geen fysieke telefoon, echte upload, notificatie, privétoegang of verwijdering getest.

- Nieuw eigenaarsbesluit: **geen offerteactie in mobiele header**. Render en mobiele balk-CSS verwijderd; desktop behouden. [Actuele wijziging en plaatsingsadvies](quote/2026-10-30/HEADER.md): productprijs, bestaande homepage-teaser en footer. Nieuwe plaatsen zijn voorstellen; upload en klantactivatie blijven uit. Twee ThemeCheck-files en vijf bestaande gate-/routecases PASS; exacte bronreadbacks. Geen nieuwe mobiele browsertest/publicatie.

## Exact één volgende handeling

**Eigenaar maakt een formulieraccount beschikbaar; hij bevestigt nog geen Jotform-account te hebben.** Daarna echte koppeling, ontvanger/toegang en upload-/ontvangstproef uitvoeren. Dit ontvangstdeel is geblokkeerd door ontbrekende accounttoegang, niet door een fictieve themebeperking. Ontwerp staat reviewbaar in concept via contact?view=offerte-vergelijken.

## Overdracht

Geen publicatie, appinstallatie, accountaanmaak, betaald plan of e-mailversturing. Jotform-koppeling staat uit en homepage-CTA verborgen. Bewaartermijn/ontvanger nog in te richten; geen privacy-/servervrijgave. Account eerst, dan tests, dan eigenaarspublicatie. Zie dossier voor setup en bronlinks. Geen nieuwe schrijver of achtergrondworker actief.

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
