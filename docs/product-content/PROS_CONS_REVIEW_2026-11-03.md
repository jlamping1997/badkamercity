# CONTENT-01 — review plus- en aandachtspunten

Peildatum: 3 november 2026. Status: **READ_ONLY_AUDIT / PROPOSALS_READY / NOT_APPLIED**.

De eigenaar vraagt nuttige, klantvriendelijke eigen teksten in plaats van mogelijke letterlijke overname. Deze taak heeft alleen gelezen en voorstellen gemaakt. Geen product-, thema-, prijs-, media- of publicatiemutatie.

## Gecontroleerde scope

- Volledige read-only Shopify-inventaris: 11.887 ACTIVE producten, 48 pagina's, unieke product-ID's en laatste hasNextPage=false gecontroleerd.
- `custom.pluspunten`: 6.289 producten met minstens één tekst; `custom.aandachtspunten`: 1.522. Samen 6.318 unieke producten met minstens één gevuld veld.
- 148 verschillende veld/tekstcombinaties: 118 plus, 30 aandacht. Alle 148 redactioneel beoordeeld. Binnen JEE-O: 273 producten, 67 teksten (47 plus, 20 aandacht).
- Bij twee gecontroleerde JEE-O-producten komt de volledige bestaande puntenlijst woordelijk overeen met BadkamerXXL: flow 500-1750 en slimline toiletborstel 801-0030. Dit bewijst overlap bij deze voorbeelden, geen volledige historische herkomst van de catalogus.
- Bij 48 JEE-O-waskommen wordt geen overloop zowel als voordeel als aandachtspunt genoemd.

## Redactioneel contract voor het voorstel

Geen verplicht minimum aan plus- of aandachtspunten. Pluspunten beschrijven een concrete functie met bruikbaar voordeel. Aandachtspunten betreffen gebruik, montage, compatibiliteit of ontbrekende onderdelen. Materiaal/kleur/maat naar specificaties, onderdelen naar setinhoud. Algemene stijlclaims schrappen; niet opvullen met nieuwe claims. Zelfde technische modellen in verschillende kleuren mogen dezelfde inhoud gebruiken.

Alle voorstellen hebben een reden en verificatievoorwaarde. JEE-O: 11 herschrijven, 11 samenvoegen, 16 naar specificaties, 9 naar setinhoud, 2 schrappen, 18 eerst controleren. Deze categorieën tellen teksten, geen unieke producten.

Extra controle nodig bij temperatuurstop/Cooltouch, koude-start-/cv-uitspraken, universele passing, onderhoudsadvies en ontbrekende maateenheden. De officiële fabrikantdocumentatie ondersteunt niet automatisch de huidige claims; geen synoniemenbatch uitvoeren. Voorbeeld: fabrikant benoemt pure 300-6100 met keramische mengcartridge en flow 500-6210 als progressieve mengkraan. Bedienings- en veiligheidsclaims per artikel vaststellen.

## Renderer en begrenzing

Bronpaden relatief aan `shopify/current/`: `snippets/product-pros-cons.liquid` toont gewone niet-lege `custom`-lijsten zonder verplicht minimum. `bc_sunshower.configuration` routeert naar `snippets/bc-sunshower-panel.liquid`, mode pros. Die aparte vertaalsleutelteksten zijn niet in de 148 opgenomen. Lege velden betekenen dus niet dat een Sunshower-PDP geen punten heeft.

Een ACTIVE status of teruggegeven onlineStoreUrl is geen volledige openbare runtimecontrole. Geen volledige fabrikantcontrole van alle artikelen, geen storefront/browser/telefoon-/checkouttest en geen productwrite uitgevoerd. Geen nieuwe performance- of juridische claim. Verse eindcontrole: MAIN **196110090506**, Lagoo-concept **196116087050** UNPUBLISHED. Bestaande Lagoo-werkstatus blijft behouden.

## Opgeleverd en getoetst

Privérapport met alle 148 huidige teksten, productaantallen/voorbeelden, voorstel, reden en voorwaarden; standaardfilter voor de 67 JEE-O-teksten. Volledige inventaris en rapport blijven buiten publieke Git. Geen klant-/orderdata geraadpleegd.

PASS: unieke inventaris, 148/148 beoordelingsdekking, 118/30 veldverdeling, 67 JEE-O-teksten, alle redenen/voorwaarden gevuld, HTTPS-links en zelfstandig HTML-bestand zonder externe scripts. Filterlogica met Node/DOM-stub: JEE-O67 / alle148 / overige81 / JEE-O eerst controleren18 en lege zoekresultaatstatus correct. Geen visuele browsercontrole geclaimd.

## Bronnen

- Huidige Shopify-velden en huidige canonieke renderer.
- [Officiële JEE-O-prijslijst maart 2026](https://jee-o.com/app/uploads/2025/02/NL-JEE-O-prijslijst-MS-maart-2026.pdf): artikelen en onderhoudssectie; geen vervanger voor iedere technische tekening of onderdelenlijst.
- [Officieel pure 300-6100-specificatieblad](https://jee-o.com/app/uploads/2024/10/JEE-O-pure-shower-01-specifications-300-6100.pdf).
- [BadkamerXXL flow 500-1750](https://www.badkamerxxl.nl/jee-o-flow-opbouw-wastafelkraan-met-eengreepsmengkraan-geborsteld-rvs-500-1750) en [slimline toiletborstel 801-0030](https://www.badkamerxxl.nl/jee-o-slimline-toiletborstel-met-wandhouder-geborsteld-rvs-801-0030), uitsluitend als overlapcontrole.

## Overdracht

Uitvoerder: ChatGPT via GitHub/Shopify-connectors; geen lokale Windows-run of schone lokale checkout geclaimd. Bestaande lokale wijzigingen behouden. Codebranch `fix/product-cards-2026-10-14`; deze checkpoint bevat uitsluitend dit dossier en de centrale status. Runtime-/Lagoo-codecheckpoint uit de bestaande status blijft ongewijzigd van toepassing. Geen actieve schrijver na overdracht.

**Exact één volgende handeling voor CONTENT-01:** Jackson beoordeelt de JEE-O-termvoorstellen; pas daarna een kleine bevestigde productgroep gericht voorbereiden. Geen productmutatie op basis van dit dossier alleen. Voor uitvoering actuele waarden opnieuw lezen en herstelwaarden bewaren. Deze audit heeft geen productrollback nodig.
