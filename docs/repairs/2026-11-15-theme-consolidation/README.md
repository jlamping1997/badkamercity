# Gepubliceerd — 16 november 2026

**PUBLISHED / PUBLIC_DESKTOP_QA_VERIFIED:** samengevoegd thema196690379018 staat MAIN. Kraan-, spiegelkast- en deurkeuzes buiten preview gecontroleerd. [Publicatiebewijs en hervatpunt](PUBLICATION-2026-11-16.md). De status en publicatieopdracht hieronder zijn historie van vóór deze vrijgave.

# Gezamenlijk actueel concept — 15 november 2026

Status: VERIFIED_PREVIEW / OWNER_PUBLICATION_PENDING.
Uitvoerder: ChatGPT via Shopify/GitHub-connectors en echte Chrome.
Actieve codebranch: `fix/product-cards-2026-10-14`; themabron `shopify/current/`.
Broncheckpoint vóór deze documentatie: `9c8ec9844fb114d43a2c5e8e099b04ed4e0fa83d`.
Merchant/eigenaar beoordeelt en publiceert.

## Resultaat en correctie van de oude to-do

De eigenaar heeft **BadkamerCity - bescherming oude productkaarten (196542005514)** gepubliceerd. Dit is nu MAIN. Publieke HTTP-reads van de listing en de werkelijk gekoppelde JS leveren200 op en bevatten de actuele paginatelling/hercontrole en404/410-afhandeling. Dit is bronbewijs; geen nieuwe integrale publieke browserproef van die kaartpatch.

**BadkamerCity - complete Brauer productkeuzes (196690379018)** is het enige gezamenlijke reviewconcept van deze ronde en blijft UNPUBLISHED. Dit vervangt de oude naam complete filterkleuren. Bestaande recente fixes zijn behouden.

| Oud concept | Verse vergelijking met MAIN | Besluit |
|---|---|---|
| Wiesbaden vervolg196441932042 |1684paden; zeven bestaande files verouderd,840 latere MAIN-files ontbreken; alle overige bestaande files exact gelijk | Wiesbaden-code zit al in MAIN. Geen volledige oude conceptpublicatie. Bestaande product-/twijfelholds blijven behouden. |
| Brauer specificaties196557144330 |2522paden; dezelfde zeven files verouderd, twee ongebruikte inert gemaakte QA-files ontbreken; geen andere eigen codeverschillen | Specificatiecode zit al in MAIN. Dit is geen bewijs dat iedere productdatabase volledig is. |
| Brauer visuele keuzes196578803978 |183 bedoelde featurebestanden plus zeven ongerelateerde oude files; twee inerte QA-files ontbreken | Alleen183 bedoelde keuzebestanden overgenomen, verouderde files uitgesloten. |

De zeven uitgesloten paden zijn: assets/bc-external-filters.js; locales/en.default.json; locales/nl.json; sections/main-product.liquid; snippets/bc-external-filters.liquid; snippets/bc-product-description.liquid; snippets/bc-product-documents.liquid. De actuele MAIN-main-product bevat de Brauer-hook al.

## Exacte samenvoeging

1. Van actuele MAIN eerst zes baselinefiles in196690379018 gelijkgetrokken: vier kaart-/filterfiles en twee reeds inerte ongebruikte QA-files.
2. **Volledige voorafpariteit:2524/2524 paden en checksums exact gelijk.**
3. Alleen de183 bedoelde bestanden uit196578803978 gekopieerd:173 groeps-JSON’s, JS, CSS en acht routesnippets.
4. **Eindpariteit:** MAIN2524files, concept2525files.182 bestaande wijzigingen en één nieuw asset `assets/bc-brauer-46a454f9a15bdaa9.json`; geen ontbrekende paden, geen onbedoelde verschillen. Alle183featurechecksums exact gelijk aan de bedoelde bron. MAIN volledig ongewijzigd.
5. Alle183bodies ook via Gitblob-SHA exact gelijk aan bestaande canonieke bestanden op de actieve codebranch; geen nieuwe codefiles geschreven naar Git nodig.

De183files bundelen de eerdere173verfijnde/geprijsde groepen voor6402artikelen. Het totale rendererbestand bevat828groepen/12292artikelen. De resterende655groepen zijn hiermee niet alsnog volledig inhoudelijk verfijnd.

De twee ongebruikte QA-files uit de kaartpatch blijven bewust inert: lege sectie met schema en alternatieve paginatemplate gelijk aan standaard page.json. Geen testscript. Connector verwijdering was eerder geblokkeerd; geen omweg gebruikt.

## Verificatie

| Controle | Resultaat |
|---|---|
| Brauer-JS syntax | PASS |
| Volledige bestaande renderer |828groepen,12292exacte starts,152902geldige keuzes PASS |
| Voorwaardelijke keuzes |1172tussenstanden; koopknopguard PASS |
| Prijsvolgorde op bestaande snapshot |173groepen/6402artikelen/23503asstanden PASS |
| Kaartbescherming in gezamenlijk concept |30gerichte tests PASS |
| Officiële theme-validator |183files PASS;0fouten;8bestaande routecomplexiteitswaarschuwingen |
| Exacte Shopify-readback |alle183featurechecksums en volledige2525paden gecontroleerd |
| MAIN-behoud |alle2524checksums ongewijzigd |

Echte Chrome, desktop1348×926, previewthema196690379018:
- Kraan5-CE-001: hendel Lang en smal→Kort en smal opent5-CE-001-HD5. Uitvoering Hoog, ronde uitloop opent5-CE-003-R2, juiste foto en werkelijke weergegeven prijs€268,50. Niet-combineerbare grepen worden grijs.
- SpiegelkastSK-IMD100HW:100→60cm toont expliciete richtingsvraag; koopknop disabled zolang geen keuze gemaakt is. Linksdraaiend opentSK-IMD60LHW, prijs€882,09 en koopknop hersteld.
- VoidGS-VON2H6050200CE: Aan de muur→Aan de glaswand opentGS-VON3H6050200CE; bijbehorende foto en prijs€1153,13. Onmogelijke90/100cm-combinaties uitgeschakeld.
- Schermbewijs in de chat vastgelegd. De Shopify-screenshotwidget met grote zwarte pijlen is hiervoor niet gebruikt.

## Grenzen

Geen nieuwe cart-add, checkout, fysieke mobiele, volledige publieke naswitch- of VPS/indexproef. Niet alle individuele SKU-URL’s vandaag via Shopify opgevraagd; de grote rendererproef valideert de aanwezige snapshots. Prijsvolgorde gebruikt de bestaande12novembersnapshot;6402prijzen niet opnieuw vers gelezen. PDP-prijzen in bovenstaande Chrome-proeven komen uit Shopify. Bij prijswijziging moet de snapshot opnieuw uit verse bron worden opgebouwd.

Geen product-, prijs-, voorraad-, media-, publicatiestatus-, Typesense- of VPS-mutatie. Geen themapublicatie door uitvoerder. Windows-pc niet toegankelijk/gecontroleerd. De aanwezige Linux-repo is schoon op de bestaande branch met juiste origin, maar loopt achter op remote; dat is geen Windows-syncclaim.

Productvolgorde blijft DEFERRED_BY_OWNER. Lagoo105foto-holds,65historische Wiesbaden-twijfelgevallen, Merchant/meting/SEO en andere werkstromen niet afgesloten.

## Eén volgende handeling en herstel

Eigenaar beoordeelt en publiceert uitsluitend **BadkamerCity - complete Brauer productkeuzes (196690379018)**. Eerst in Shopify Voorbeeld openen. Daarna publieke nacontrole van kaartbescherming, Lagoo-bijlagen, filterkleuren en drie Brauer-keuzevoorbeelden.

Oude Wiesbaden-/Brauer-specificatie-/Brauer-keuzeconcepten niet los publiceren: ze missen recente fixes. Ze blijven ongewijzigd beschikbaar als historische bron.

Vóór publicatie is verlaten van het concept genoeg: MAIN196542005514 is intact. Na publicatie kan eigenaar het vorige intacte thema196542005514 opnieuw publiceren. Voor gerichte feature-rollback de183paden uit verification.json herstellen vanaf die MAIN-baseline; overige bestanden behouden.

Zie [verification.json](verification.json) voor scope, checksums, Gitblob-SHA’s en testaantallen. Geen actieve schrijver na overdracht.
