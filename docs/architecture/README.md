# BadkamerCity — architectuur, documentatie en eenheid

**Nieuwe onderzoeksbasis: 28 oktober 2026.** Eigenaar vraagt eerst een diep onderzoeks- en documentatieplan, daarna onderbouwde inconsistenties en kleine verbeteringen. Doel: verantwoord lanceren en vervolgens beheersbaar uitbreiden. Dit dossier verklaart niet dat de volledige audit al is uitgevoerd.

## Beginnen of iets opzoeken

| Je wilt… | Lees |
| --- | --- |
| Weten wat nu de taak, branch en live versie zijn | [Centrale werkstatus](../LIVE_STATUS_AND_NEXT_STEPS.md) |
| Begrijpen wat bestaat en wat nog onbekend is | [Systeem- en bronnenregister](SYSTEMS_AND_SOURCES.md) |
| Het volledige onderzoek uitvoeren | [Onderzoeksboom en fasering](DEEP_SCAN_PLAN.md) |
| Dezelfde bediening en vormgeving hergebruiken | [Componentafspraken](COMPONENT_CONTRACTS.md) |
| Bekende afwijkingen en prioriteiten bekijken | [Bevindingenregister](FINDINGS.md) |
| Als nieuwe ontwikkelaar of AI veilig beginnen | [Werkwijze en overdracht](CONTRIBUTING_AND_HANDOFF.md) |
| De inventaris opnieuw maken | [Scannerhandleiding](SCANNING.md) |
| Een functie dieper begrijpen of gericht aanpassen | [Componentdossiers](components/README.md) en [routematrix](ROUTE_RENDERER_MATRIX.md) |
| Actuele bronkaart en template-/menutoewijzingen | [DOC-01](DOC01_SOURCE_MAP.md) |
| Productgegevens vinden of het model begrijpen | [Productdata](PRODUCT_DATA.md) |
| De nulmeting van 28 oktober controleren | [Bewijs en dekkingsgrenzen](evidence/2026-10-28/README.md) |

## Vervolgmeting DOC-01 en productexport

Alle 1.262 themebestanden zijn ontvangen en statisch geïnventariseerd: 955 verwijzingen, 1.261 bytegelijk en één open settings-pariteitsuitzondering. Admin-toewijzingen en het private pakket met 11.343 producten zijn vastgelegd. Lees [DOC01_SOURCE_MAP.md](DOC01_SOURCE_MAP.md) en [PRODUCT_DATA.md](PRODUCT_DATA.md). Dit is de huidige bronkaart; de nulmeting hieronder blijft historisch bewijs. DOC-01 heeft nog geen volledige pariteitsvrijgave of runtime-audit.

## Wat de voorafgaande nulmeting vaststelde

- De actuele Shopify MAIN is **195818389770 — BadkamerCity - Smooth winkelwagen pop-up**. De rol is opnieuw via Shopify gelezen. De eerdere conceptstatus is dus achterhaald; deze onderzoeksronde heeft niets gepubliceerd.
- Actieve codebranch: **fix/product-cards-2026-10-14**, gecontroleerd broncommit **4a85d063b750b74fd398fe106c11bfe05b6ce277**. `main` is de vaste documentatie-ingang; geen aanname dat de root-themacode gelijk is aan productie.
- Het volledige live bestandsmanifest telt **1.262 bestanden**. De Git-root telt **441 themabestanden**: **384 bytegelijk**, **57 afwijkend**, **821 uitsluitend live**, **0 uitsluitend in de Git-root**. Recente implementaties zijn ook onder releasedossiers in `docs/` opgeslagen; dit verschil bewijst niet dat al die code geheel uit Git ontbreekt.
- De Git-root is statisch geïnventariseerd: **830 letterlijke Liquid-/JSON-afhankelijkheden** gevonden. Een actuele live steekproef van **15 bestanden**, elk checksumgelijk aan het live manifest, leverde **149** zulke verwijzingen op. De steekproef is geen volledige productiecodekaart.
- Deze werkbranch bevatte bij aanvang **95 Markdown-documenten onder docs/**. De centrale status had **1.209 regels**. Die status is als archief behouden en vervangen door een korte actuele ingang.

## Verdieping DOC-02A

De [componentdossiers](components/README.md) en [route-/renderermatrix](ROUTE_RENDERER_MATRIX.md) verklaren nu de actuele productpagina's, keuzes/inbouw, kaarten/filters, cartfeedback, navigatie/opslag, datapijplijnen en stijl/beweging. 85 geselecteerde bronbestanden zijn tegen het verse manifest gecontroleerd; 52 letterlijke metafieldkeys en 4 dynamische consumerlocaties zijn gekoppeld. Acht openbare HTML-responses zijn gelezen; interactieve staten blijven NOT_TESTED. De 656 gegenereerde keuzeassets zijn daarnaast opnieuw bytegelijk uit negen oorspronkelijke assets gereconstrueerd. Zie [bewijs DOC-02A](evidence/2026-10-28-doc02/README.md).

Dit maakt DOC-02 niet geheel afgerond: eerst de werkelijk zichtbare renderers en bediening per viewport bevestigen. De settingspariteit blijft open; dit blokkeert geen bronuitleg van andere geverifieerde bestanden, maar wel een volledige bytevrijgave.

## Afzonderlijke functies: DOC-03A

De [microanalyse](components/micro/README.md) maakt de interne functies en hun staten verder expliciet. 22 actuele bestanden zijn opnieuw checksumgelijk opgehaald; 15 geïsoleerde cases op vier hashgecontroleerde JS-bronnen leveren 10 controles, 3 defectreproducties voor twee problemen en 2 bevestigde grenzen. De 72 Sunshower-cataloguscombinaties zijn structureel uniek. De desktopbrowser bevestigt een externe collectiekaart met zichtbare pijl, een sluitende Maathulp met focusherstel en één galerijstap. Geen echte cartactie, productiecorrectie of mobiele vrijgave. [Bewijs](evidence/2026-10-28-micro/README.md).

## Wat documentatie hier moet opleveren

Een opvolger moet voor een concrete wijziging kunnen vinden: welke gebruikersfunctie hij raakt, wie de data beheert, waar de code begint, welke andere onderdelen meeveranderen, welke afspraken gelden, hoe hij het resultaat controleert en hoe hij teruggaat.

Een bestandentelling of lang verslag alleen is daarvoor onvoldoende. We onderhouden drie lagen:

1. **Actuele uitleg:** korte startpagina, systemen, routes, componentcontracten en onderhoudsinstructies.
2. **Gegenereerde kaarten:** inventaris, hashes, afhankelijkheden, datavelden en scanrapporten. Opnieuw op te bouwen vanuit een benoemde bronversie.
3. **Geschiedenis en bewijs:** gedateerde releases, besluiten, oude metingen en uitzonderingen. Een oud bewijs wordt niet automatisch een actuele waarheid.

## Lees de status precies

| Status | Betekenis |
| --- | --- |
| VERIFIED_SOURCE | Bestand of instelling op de opgegeven datum/versie werkelijk gelezen |
| STATIC_CANDIDATE | Scanner of code-inspectie signaleert iets; gebruik en impact nog onderzoeken |
| USER_REPORTED | Eigenaar meldt zichtbaar gedrag; exacte route/staat nog reproduceren |
| VERIFIED_ISOLATED | Echte broncode onder benoemde synthetische stimuli uitgevoerd; geen bewijs van servervoorkomen of native browsergedrag |
| VERIFIED_HTML | Publieke serverresponse gelezen; geen uitgevoerde JS, zichtbaarheid of interactieclaim |
| VERIFIED_RUNTIME | Handeling op benoemde URL/viewport/browser werkelijk uitgevoerd |
| PROPOSED | Richting of afspraak voorgesteld; nog geen goedgekeurd ontwerp of implementatie |
| NOT_TESTED / BLOCKED | Controle ontbreekt, met concrete reden en vervolgactie |
| HISTORICAL | Eerder bewijs; niet opnieuw als huidige werking gecertificeerd |

De oudere labels uit [AGENTS.md](../../AGENTS.md) blijven geldig. VERIFIED_SOURCE kan bijvoorbeeld VERIFIED_THEME of VERIFIED_ADMIN onderbouwen; het is geen vervanging voor runtimebewijs.

## Onderhoud

Een feature is pas overdraagbaar als de actuele componentuitleg, relevante afhankelijkheden, acceptatie, bevindingenstatus en terugzetroute mee zijn bijgewerkt. Houd die wijziging bij dezelfde codewijziging. Gebruik één actuele eigenaarspagina per onderwerp en verwijs ernaar; kopieer geen hele statusgeschiedenis naar meerdere startpagina's.
